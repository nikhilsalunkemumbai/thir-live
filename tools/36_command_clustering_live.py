#!/usr/bin/env python3
"""
Tool 36 — Command Clustering
THIR · nikhilsalunkemumbai/thir-live
Input:  data/ir_cases.json
Output: data/command_clusters.json

Reads cowrie.command.input events from ir_cases.json.
Groups sessions by command sequence similarity.
Labels clusters as campaigns when multiple IPs run identical commands.
Maps detected campaigns to ATT&CK TTPs.
"""

import json
import hashlib
import argparse
import sys
import re
from datetime import datetime, timezone
from collections import defaultdict
from pathlib import Path

# ATT&CK TTP mappings for known command patterns
TTP_PATTERNS = [
    # T1021.004 — Remote Services: SSH
    (r"authorized_keys",        "T1021.004", "Remote Services: SSH"),
    (r"\.ssh",                  "T1021.004", "Remote Services: SSH"),
    # T1078 — Valid Accounts
    (r"useradd|adduser|passwd", "T1078",     "Valid Accounts"),
    (r"authorized_keys",        "T1078",     "Valid Accounts"),
    # T1105 — Ingress Tool Transfer
    (r"wget|curl|tftp|fetch",   "T1105",     "Ingress Tool Transfer"),
    # T1059.004 — Command: Unix Shell
    (r"/bin/sh|/bin/bash|exec", "T1059.004", "Unix Shell"),
    # T1083 — File & Directory Discovery
    (r"ls\s|ls$|find\s|locate", "T1083",     "File & Directory Discovery"),
    # T1082 — System Info Discovery
    (r"uname|arch|lscpu|cat /proc", "T1082", "System Information Discovery"),
    # T1592 — Gather Victim Host Info
    (r"uptime|nproc|/proc/",    "T1592",     "Gather Victim Host Info"),
    # T1070 — Indicator Removal
    (r"rm\s+-rf|unlink|shred",  "T1070",     "Indicator Removal"),
    # T1140 — Deobfuscate/Decode
    (r"base64|xxd|od\s",        "T1140",     "Deobfuscate/Decode Files"),
    # T1547 — Boot/Logon Autostart
    (r"crontab|/etc/rc|init\.d|systemctl enable", "T1547", "Boot/Logon Autostart"),
    # T1496 — Resource Hijacking (crypto miners)
    (r"xmrig|minerd|cryptonight|stratum\+",   "T1496", "Resource Hijacking"),
    # T1489 — Service Stop
    (r"systemctl\s+stop|service\s+\w+\s+stop|pkill|killall", "T1489", "Service Stop"),
    # T1562 — Impair Defenses
    (r"iptables\s+-F|ufw\s+disable|setenforce\s+0", "T1562", "Impair Defenses"),
    # T1136 — Create Account
    (r"useradd|adduser",        "T1136",     "Create Account"),
    # T1003 — Credential Dumping
    (r"/etc/passwd|/etc/shadow", "T1003",    "Credential Dumping"),
]

# Known campaign signatures for direct matching
KNOWN_CAMPAIGNS = [
    {
        "name": "mdrfckr SSH Key Injection",
        "patterns": ["mdrfckr", "authorized_keys", "rm -rf .ssh"],
        "ttps": ["T1021.004", "T1078", "T1105"],
        "severity": "HIGH",
        "description": "Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.",
    },
    {
        "name": "Recon Loader Script",
        "patterns": ["export PATH", "uname", "arch", "/proc/uptime", "nproc", "lscpu"],
        "ttps": ["T1078", "T1083", "T1592", "T1082"],
        "severity": "MEDIUM",
        "description": "Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.",
    },
    {
        "name": "XMRig Miner Deploy",
        "patterns": ["xmrig", "stratum+", "pool."],
        "ttps": ["T1105", "T1496"],
        "severity": "HIGH",
        "description": "Cryptominer deployment. Downloads and executes XMRig against known mining pools.",
    },
    {
        "name": "Mirai/IoT Botnet",
        "patterns": ["busybox", "MIRAI", "/bin/busybox"],
        "ttps": ["T1105", "T1059.004"],
        "severity": "HIGH",
        "description": "Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.",
    },
    {
        "name": "Tsunami/Kaiten Backdoor",
        "patterns": ["tsunami", "kaiten", "flood"],
        "ttps": ["T1105", "T1059.004", "T1489"],
        "severity": "CRITICAL",
        "description": "Tsunami/Kaiten DDoS backdoor. Establishes persistent shell and floods.",
    },
]


def load_ir_cases(path: str) -> list:
    p = Path(path)
    if not p.exists():
        print(f"[Tool36] ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(p) as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get("cases", data.get("ir_cases", []))


def extract_command_sessions(cases: list) -> list:
    """Extract sessions with their command sequences.

    Supports two IR case formats:
      1. Raw Cowrie format — commands stored as cowrie.command.input events
         inside case["events"] (original honeypot log structure).
      2. Tool 26 normalized format — commands stored directly in case["commands"]
         as a plain list of strings; case["events"] contains only timeline entries
         (no "input" field). This is the format written by Tool 26 in THIR Live.

    Bug fixed (2026-03-19): Tool 36 previously only checked case["events"] for
    cowrie.command.input eventids. Tool 26 normalizes commands into case["commands"]
    and writes an empty or timeline-only events list. This caused 0 sessions to be
    extracted despite 200+ cases with commands present in ir_cases.json.
    """
    sessions = []
    for case in cases:
        src_ip = case.get("src_ip", case.get("attacker_ip", ""))
        case_id = case.get("case_id", "")
        events = case.get("events", [])
        country = case.get("country", "")
        isp = case.get("isp", case.get("org", ""))

        commands = []
        ts_first = None

        # Path 1: raw Cowrie events array (cowrie.command.input entries with "input" field)
        for evt in events:
            etype = evt.get("eventid", evt.get("event_type", ""))
            if etype == "cowrie.command.input":
                cmd = evt.get("input", evt.get("command", "")).strip()
                if cmd:
                    commands.append(cmd)
                    ts = evt.get("timestamp", "")
                    if ts and (not ts_first or ts < ts_first):
                        ts_first = ts

        # Path 2: Tool 26 normalized format — commands stored directly on the case
        # Only use this fallback when Path 1 found nothing (avoids double-counting
        # if a future format ever populates both fields).
        if not commands:
            for cmd in case.get("commands", []):
                cmd = (cmd or "").strip()
                if cmd:
                    commands.append(cmd)
            if commands:
                ts_first = case.get("first_seen", case.get("timestamp", ""))

        if commands:
            sessions.append({
                "session_id": case_id,
                "src_ip": src_ip,
                "country": country,
                "isp": isp,
                "commands": commands,
                "command_count": len(commands),
                "timestamp": ts_first or case.get("timestamp", ""),
            })

    return sessions


def normalize_command(cmd: str) -> str:
    """Normalise a command for similarity comparison."""
    # Lowercase
    cmd = cmd.lower().strip()
    # Remove IPs
    cmd = re.sub(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', '<IP>', cmd)
    # Remove URLs (keep domain structure)
    cmd = re.sub(r'https?://[^\s]+', '<URL>', cmd)
    # Remove specific usernames/passwords in common patterns
    cmd = re.sub(r'echo\s+"[^"]{20,}"', 'echo <DATA>', cmd)
    # Normalise whitespace
    cmd = re.sub(r'\s+', ' ', cmd)
    return cmd


def sequence_hash(commands: list) -> str:
    """Compute a hash of the full normalised command sequence."""
    normalised = [normalize_command(c) for c in commands]
    joined = "|".join(normalised)
    return hashlib.sha256(joined.encode()).hexdigest()[:16]


def partial_match_score(seq_a: list, seq_b: list) -> float:
    """
    Jaccard similarity on normalised command sets.
    Returns 0.0-1.0 (1.0 = identical sets).
    """
    set_a = set(normalize_command(c) for c in seq_a)
    set_b = set(normalize_command(c) for c in seq_b)
    if not set_a and not set_b:
        return 1.0
    intersection = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersection / union if union else 0.0


def detect_ttps(commands: list) -> list:
    """Map commands to ATT&CK TTPs."""
    ttps = {}
    full_text = " ".join(commands).lower()
    for pattern, ttp_id, ttp_name in TTP_PATTERNS:
        if re.search(pattern, full_text, re.IGNORECASE):
            ttps[ttp_id] = ttp_name
    return [{"id": k, "name": v} for k, v in ttps.items()]


def match_known_campaigns(commands: list) -> list:
    """Check if commands match any known campaign signature."""
    full_text = " ".join(commands).lower()
    matched = []
    for campaign in KNOWN_CAMPAIGNS:
        hit_count = sum(1 for p in campaign["patterns"] if p.lower() in full_text)
        if hit_count >= max(1, len(campaign["patterns"]) // 2):
            matched.append({
                "name": campaign["name"],
                "ttps": campaign["ttps"],
                "severity": campaign["severity"],
                "description": campaign["description"],
                "pattern_hits": hit_count,
                "pattern_total": len(campaign["patterns"]),
            })
    return matched


def cluster_sessions(sessions: list, similarity_threshold: float = 0.7) -> list:
    """
    Cluster sessions by command sequence similarity.
    Uses greedy nearest-neighbour clustering.
    """
    if not sessions:
        return []

    # Sort by command count descending (dense sessions as cluster seeds)
    sessions_sorted = sorted(sessions, key=lambda s: s["command_count"], reverse=True)
    clusters = []
    assigned = set()

    for i, seed in enumerate(sessions_sorted):
        if seed["session_id"] in assigned:
            continue

        cluster = {
            "cluster_id": f"CLU-{len(clusters)+1:03d}",
            "seed_session": seed["session_id"],
            "seed_commands": seed["commands"],
            "members": [seed],
            "is_campaign": False,
            "campaign_name": None,
            "campaign_severity": None,
            "campaign_description": None,
            "ttps": [],
            "matched_campaigns": [],
            "sequence_hash": sequence_hash(seed["commands"]),
        }
        assigned.add(seed["session_id"])

        # Find similar sessions
        for j, candidate in enumerate(sessions_sorted):
            if candidate["session_id"] in assigned:
                continue
            score = partial_match_score(seed["commands"], candidate["commands"])
            if score >= similarity_threshold:
                cluster["members"].append(candidate)
                assigned.add(candidate["session_id"])

        # TTP detection on merged command set
        all_cmds = []
        for m in cluster["members"]:
            all_cmds.extend(m["commands"])
        cluster["ttps"] = detect_ttps(all_cmds)

        # Known campaign matching
        campaign_matches = match_known_campaigns(all_cmds)
        cluster["matched_campaigns"] = campaign_matches

        if campaign_matches:
            top = campaign_matches[0]
            cluster["is_campaign"] = True
            cluster["campaign_name"] = top["name"]
            cluster["campaign_severity"] = top["severity"]
            cluster["campaign_description"] = top["description"]
            # Merge TTP lists
            existing_ids = {t["id"] for t in cluster["ttps"]}
            for ttp_id in top["ttps"]:
                if ttp_id not in existing_ids:
                    cluster["ttps"].append({"id": ttp_id, "name": ttp_id})

        clusters.append(cluster)

    return clusters


def build_output(clusters: list, total_sessions: int) -> dict:
    # Serialize members to summary form
    serializable_clusters = []
    for cl in clusters:
        members_summary = [
            {
                "session_id": m["session_id"],
                "src_ip": m["src_ip"],
                "country": m["country"],
                "isp": m["isp"],
                "command_count": m["command_count"],
                "timestamp": m["timestamp"],
            }
            for m in cl["members"]
        ]
        unique_ips = list({m["src_ip"] for m in cl["members"] if m["src_ip"]})

        serializable_clusters.append({
            "cluster_id": cl["cluster_id"],
            "is_campaign": cl["is_campaign"],
            "campaign_name": cl["campaign_name"],
            "campaign_severity": cl["campaign_severity"],
            "campaign_description": cl["campaign_description"],
            "matched_campaigns": cl["matched_campaigns"],
            "session_count": len(cl["members"]),
            "unique_ips": unique_ips,
            "unique_ip_count": len(unique_ips),
            "sequence_hash": cl["sequence_hash"],
            "ttps": cl["ttps"],
            "representative_commands": cl["seed_commands"][:10],
            "members": members_summary,
        })

    campaigns = [c for c in serializable_clusters if c["is_campaign"]]
    max_sev = "NONE"
    sev_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "NONE"]
    for c in campaigns:
        if c["campaign_severity"] and \
           sev_order.index(c["campaign_severity"]) < sev_order.index(max_sev):
            max_sev = c["campaign_severity"]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_sessions_with_commands": total_sessions,
        "total_clusters": len(serializable_clusters),
        "campaign_clusters": len(campaigns),
        "singleton_clusters": len([c for c in serializable_clusters if c["session_count"] == 1]),
        "highest_severity": max_sev,
        "active_campaigns": [
            {
                "cluster_id": c["cluster_id"],
                "name": c["campaign_name"],
                "severity": c["campaign_severity"],
                "session_count": c["session_count"],
                "unique_ip_count": c["unique_ip_count"],
                "ttps": [t["id"] for t in c["ttps"]],
            }
            for c in campaigns
        ],
        "clusters": serializable_clusters,
    }


def main():
    parser = argparse.ArgumentParser(description="Tool 36 — Command Clustering")
    parser.add_argument("--input",     default="data/ir_cases.json",        help="Path to ir_cases.json")
    parser.add_argument("--output",    default="data/command_clusters.json", help="Output path")
    parser.add_argument("--threshold", type=float, default=0.7,              help="Similarity threshold 0.0-1.0")
    args = parser.parse_args()

    print(f"[Tool36] Reading {args.input}")
    cases = load_ir_cases(args.input)
    print(f"[Tool36] Loaded {len(cases)} IR cases")

    sessions = extract_command_sessions(cases)
    print(f"[Tool36] Sessions with commands: {len(sessions)}")

    clusters = cluster_sessions(sessions, args.threshold)
    output = build_output(clusters, len(sessions))

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"[Tool36] ✓ Written → {args.output}")
    print(f"[Tool36]   Clusters: {output['total_clusters']} | "
          f"Campaigns: {output['campaign_clusters']} | "
          f"Highest severity: {output['highest_severity']}")
    if output["active_campaigns"]:
        for camp in output["active_campaigns"]:
            print(f"[Tool36]   ⚠ CAMPAIGN: {camp['name']} "
                  f"[{camp['severity']}] — {camp['session_count']} sessions, "
                  f"{camp['unique_ip_count']} IPs")


if __name__ == "__main__":
    main()
