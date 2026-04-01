#!/usr/bin/env python3
"""
Tool 35 — SSH Fingerprint Aggregator
THIR · nikhilsalunkemumbai/thir-live
Input:  data/ir_cases.json
Output: data/ssh_fingerprints.json

Reads cowrie.client.version and cowrie.client.kex events from ir_cases.json.
Computes HASSH-style fingerprints per session, aggregates by hash,
maps to known SSH client families for botnet/tool attribution.
"""

import json
import hashlib
import argparse
import sys
from datetime import datetime, timezone
from collections import defaultdict
from pathlib import Path

# Known SSH client fingerprint families
# Maps partial version string patterns to family labels
KNOWN_FAMILIES = [
    ("libssh",          "libssh"),
    ("paramiko",        "Paramiko (Python)"),
    ("asyncssh",        "AsyncSSH (Python)"),
    ("dropbear",        "Dropbear (embedded)"),
    ("bitvise",         "Bitvise"),
    ("putty",           "PuTTY"),
    ("openssh",         "OpenSSH"),
    ("golang",          "Go SSH client"),
    ("jsch",            "JSch (Java)"),
    ("nmap",            "Nmap scanner"),
    ("masscan",         "Masscan"),
    ("go-",             "Go SSH client"),
    ("ruby",            "Ruby Net::SSH"),
    ("perl",            "Perl Net::SSH"),
    ("twisted",         "Twisted (Python)"),
    ("fabric",          "Fabric (Python)"),
    ("ansible",         "Ansible"),
    ("cyberduck",       "Cyberduck"),
    ("winscp",          "WinSCP"),
    ("filezilla",       "FileZilla"),
    ("mobaxterm",       "MobaXterm"),
    ("securecrt",       "SecureCRT"),
    ("xshell",          "Xshell"),
    ("ssh-2.0-ssh",     "Generic SSH/2.0"),
    ("ssh-2.0-go",      "Go SSH scanner"),
]

# Common KEX algorithm sets for botnet identification
BOTNET_KEX_SIGNATURES = {
    "diffie-hellman-group14-sha1,diffie-hellman-group1-sha1": "Mirai/variant",
    "diffie-hellman-group1-sha1,diffie-hellman-group14-sha1": "Mirai/variant",
    "diffie-hellman-group14-sha256,diffie-hellman-group14-sha1": "Generic scanner",
    "curve25519-sha256,diffie-hellman-group14-sha256": "Modern SSH client",
    "curve25519-sha256@libssh.org,ecdh-sha2-nistp256": "libssh-based",
}


def classify_client(version_string: str) -> str:
    """Map version string to known SSH client family."""
    if not version_string:
        return "Unknown"
    vl = version_string.lower()
    for pattern, label in KNOWN_FAMILIES:
        if pattern in vl:
            return label
    return "Unknown"


def classify_kex(kex_string: str) -> str:
    """Match KEX algorithms to known botnet/scanner signatures."""
    if not kex_string:
        return None
    kl = kex_string.strip().lower()
    for sig, label in BOTNET_KEX_SIGNATURES.items():
        if sig.lower() in kl or kl.startswith(sig.lower().split(",")[0]):
            return label
    return None


def _normalise_alg(val) -> str:
    """
    Cowrie logs algorithm fields as lists in NDJSON
    (e.g. kexAlgs: ["curve25519-sha256", "diffie-hellman-group14-sha256"]).
    HASSH spec requires a comma-joined string. Accept both forms.
    """
    if isinstance(val, list):
        return ",".join(str(v) for v in val)
    return val or ""


def compute_hassh(kex_algs, encryption_algs_client,
                  mac_algs, compression_algs) -> str:
    """
    Compute HASSH fingerprint (MD5 of concatenated algorithm strings).
    Original HASSH spec: https://github.com/salesforce/hassh
    hassh = md5(kex;enc;mac;comp)
    Accepts both str and list values — Cowrie logs alg fields as lists.
    """
    components = ";".join([
        _normalise_alg(kex_algs),
        _normalise_alg(encryption_algs_client),
        _normalise_alg(mac_algs),
        _normalise_alg(compression_algs),
    ])
    return hashlib.md5(components.encode()).hexdigest()


def load_ir_cases(path: str) -> list:
    p = Path(path)
    if not p.exists():
        print(f"[Tool35] ERROR: {path} not found", file=sys.stderr)
        sys.exit(1)
    with open(p) as f:
        data = json.load(f)
    # Support both list and {"cases": [...]} formats
    if isinstance(data, list):
        return data
    return data.get("cases", data.get("ir_cases", []))


def extract_fingerprints(cases: list) -> dict:
    """
    Walk all events in all cases looking for:
      - cowrie.client.version  → software version string
      - cowrie.client.kex      → key exchange algorithms
    Returns dict keyed by session_id with collected fields.
    """
    sessions = defaultdict(lambda: {
        "session_id": None,
        "src_ip": None,
        "timestamp": None,
        "version": None,
        "kex_algs": None,
        "enc_algs_client": None,
        "mac_algs": None,
        "comp_algs": None,
    })

    for case in cases:
        # Fix: Tool 26 writes events under 'timeline', not 'events'.
        # Fallback to 'events' kept for forward compatibility.
        events = case.get("timeline", case.get("events", []))
        case_id = case.get("case_id", "")
        src_ip = case.get("src_ip", case.get("attacker_ip", ""))

        for evt in events:
            etype = evt.get("eventid", evt.get("event_type", ""))
            session = evt.get("session", evt.get("session_id", case_id))
            ts = evt.get("timestamp", evt.get("time", ""))

            if not sessions[session]["session_id"]:
                sessions[session]["session_id"] = session
                sessions[session]["src_ip"] = src_ip
                sessions[session]["timestamp"] = ts

            if etype == "cowrie.client.version":
                ver = evt.get("version", evt.get("client", ""))
                sessions[session]["version"] = ver

            elif etype == "cowrie.client.kex":
                sessions[session]["kex_algs"]       = _normalise_alg(evt.get("kexAlgs",  evt.get("kex_algs", "")))
                sessions[session]["enc_algs_client"] = _normalise_alg(evt.get("encCS",    evt.get("enc_algs_client", "")))
                sessions[session]["mac_algs"]        = _normalise_alg(evt.get("macCS",    evt.get("mac_algs", "")))
                sessions[session]["comp_algs"]       = _normalise_alg(evt.get("compCS",   evt.get("comp_algs", "")))

    return dict(sessions)


def aggregate_fingerprints(sessions: dict) -> dict:
    """
    Group sessions by computed HASSH fingerprint.
    Returns aggregated fingerprint records.
    """
    # fingerprint_hash -> aggregated record
    fp_map = defaultdict(lambda: {
        "hassh": None,
        "client_family": "Unknown",
        "botnet_signature": None,
        "version_strings": [],
        "session_count": 0,
        "unique_ips": set(),
        "sessions": [],
        "kex_algs": None,
        "enc_algs": None,
        "mac_algs": None,
        "comp_algs": None,
        "first_seen": None,
        "last_seen": None,
    })

    no_kex_count = 0

    for sid, sess in sessions.items():
        # Skip sessions with no usable fingerprint data
        if not sess["kex_algs"] and not sess["version"]:
            no_kex_count += 1
            continue

        hassh = compute_hassh(
            sess["kex_algs"] or "",
            sess["enc_algs_client"] or "",
            sess["mac_algs"] or "",
            sess["comp_algs"] or "",
        )

        rec = fp_map[hassh]
        rec["hassh"] = hassh
        rec["session_count"] += 1
        rec["sessions"].append(sid)

        if sess["src_ip"]:
            rec["unique_ips"].add(sess["src_ip"])

        if sess["version"] and sess["version"] not in rec["version_strings"]:
            rec["version_strings"].append(sess["version"])

        # Set algorithm strings from first seen
        if not rec["kex_algs"] and sess["kex_algs"]:
            rec["kex_algs"] = sess["kex_algs"]
            rec["enc_algs"] = sess["enc_algs_client"]
            rec["mac_algs"] = sess["mac_algs"]
            rec["comp_algs"] = sess["comp_algs"]

        # Client family classification
        if sess["version"]:
            fam = classify_client(sess["version"])
            if fam != "Unknown":
                rec["client_family"] = fam

        # Botnet KEX signature
        if not rec["botnet_signature"] and sess["kex_algs"]:
            sig = classify_kex(sess["kex_algs"])
            if sig:
                rec["botnet_signature"] = sig

        # Timestamps
        ts = sess.get("timestamp") or ""
        if ts:
            if not rec["first_seen"] or ts < rec["first_seen"]:
                rec["first_seen"] = ts
            if not rec["last_seen"] or ts > rec["last_seen"]:
                rec["last_seen"] = ts

    # Convert sets to lists for JSON serialisation
    result = {}
    for hassh, rec in fp_map.items():
        result[hassh] = {
            **rec,
            "unique_ips": sorted(rec["unique_ips"]),
            "unique_ip_count": len(rec["unique_ips"]),
        }

    return result, no_kex_count


def build_output(fp_map: dict, total_sessions: int, no_kex: int) -> dict:
    fingerprints = sorted(
        fp_map.values(),
        key=lambda x: x["session_count"],
        reverse=True
    )

    # Top families summary
    family_counts = defaultdict(int)
    for fp in fingerprints:
        family_counts[fp["client_family"]] += fp["session_count"]

    top_families = sorted(
        [{"family": k, "sessions": v} for k, v in family_counts.items()],
        key=lambda x: x["sessions"],
        reverse=True
    )

    # Botnet signals
    botnet_signals = [
        {
            "hassh": fp["hassh"],
            "signature": fp["botnet_signature"],
            "session_count": fp["session_count"],
            "unique_ips": fp["unique_ips"],
        }
        for fp in fingerprints
        if fp["botnet_signature"]
    ]

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "total_sessions_parsed": total_sessions,
        "sessions_with_fingerprint": len(fp_map),
        "sessions_without_kex": no_kex,
        "unique_fingerprints": len(fingerprints),
        "top_families": top_families,
        "botnet_signals": botnet_signals,
        "fingerprints": fingerprints,
    }


def main():
    parser = argparse.ArgumentParser(description="Tool 35 — SSH Fingerprint Aggregator")
    parser.add_argument("--input",  default="data/ir_cases.json",      help="Path to ir_cases.json")
    parser.add_argument("--output", default="data/ssh_fingerprints.json", help="Output path")
    args = parser.parse_args()

    print(f"[Tool35] Reading {args.input}")
    cases = load_ir_cases(args.input)
    print(f"[Tool35] Loaded {len(cases)} IR cases")

    sessions = extract_fingerprints(cases)
    print(f"[Tool35] Extracted {len(sessions)} sessions")

    fp_map, no_kex = aggregate_fingerprints(sessions)
    print(f"[Tool35] Unique fingerprints: {len(fp_map)} | No-KEX sessions: {no_kex}")

    output = build_output(fp_map, len(sessions), no_kex)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"[Tool35] ✓ Written → {args.output}")
    print(f"[Tool35]   Fingerprints: {output['unique_fingerprints']} | "
          f"Botnet signals: {len(output['botnet_signals'])} | "
          f"Top family: {output['top_families'][0]['family'] if output['top_families'] else 'none'}")


if __name__ == "__main__":
    main()
