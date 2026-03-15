#!/usr/bin/env python3
"""
Tool 33 — YARA Classifier
THIR · nikhilsalunkemumbai/thir-live
Input:  /tmp/cowrie-downloads/
        tools/yara_rules/   (YARA rule files, *.yar / *.yara)
Output: data/yara_matches.json

Runs YARA rule matching against files in cowrie-downloads.
Classifies malware family, tags samples by rule name.
Falls back to heuristic classification if yara-python not available.
"""

import json
import hashlib
import argparse
import sys
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from collections import defaultdict

# Attempt to import yara-python
try:
    import yara
    YARA_AVAILABLE = True
except ImportError:
    YARA_AVAILABLE = False

# Fallback: heuristic byte-string signatures when yara-python not installed
# Format: (family, description, byte_patterns)
HEURISTIC_SIGS = [
    ("Mirai",       "Mirai botnet binary",         [b"MIRAI", b"/bin/busybox", b"LZRD", b"realtek"]),
    ("Tsunami",     "Tsunami/Kaiten DDoS",          [b"tsunami", b"kaiten", b"KAITEN", b"!*TSUNAMI"]),
    ("XMRig",       "XMRig cryptocurrency miner",   [b"xmrig", b"cryptonight", b"stratum+tcp", b"donate.v2"]),
    ("Gafgyt",      "Gafgyt/BASHLITE IoT malware",  [b"BOTNET", b"PING", b"SCANNER", b"hold", b"junk"]),
    ("Hajime",      "Hajime P2P botnet",             [b".i.am.a.hacker", b"Just a few more jumps", b"hajime"]),
    ("Mushtik",     "Mushtik mining/backdoor",       [b"mushtik", b"rig.", b".onion"]),
    ("Sora",        "Sora Mirai variant",            [b"SORA", b"sora", b"hzlBMQBMEBMQ"]),
    ("Mozi",        "Mozi P2P botnet",               [b"mozi.m", b"mozi.a", b"[email]/Mozi"]),
    ("BotenaGo",    "BotenaGo multi-exploit",        [b"BotenaGo", b"BOTENA"]),
    ("ShellBot",    "ShellBot Perl IRC bot",         [b"use IO::Socket", b"my $server", b"irc.perl"]),
    ("CoinMiner",   "Generic coin miner",            [b"pool.", b"--algo", b"stratum", b"hashrate"]),
    ("Downloader",  "Shell/script downloader",       [b"wget http", b"curl http", b"/tmp/", b"chmod +x"]),
    ("Rootkit",     "Rootkit/hiding tool",           [b"/proc/", b"LD_PRELOAD", b"hide_pid", b"diamorphine"]),
]

# Family severity mapping
FAMILY_SEVERITY = {
    "Tsunami":   "CRITICAL",
    "Mirai":     "HIGH",
    "Gafgyt":    "HIGH",
    "Hajime":    "HIGH",
    "XMRig":     "HIGH",
    "Mozi":      "HIGH",
    "BotenaGo":  "HIGH",
    "Mushtik":   "MEDIUM",
    "Sora":      "MEDIUM",
    "ShellBot":  "MEDIUM",
    "CoinMiner": "MEDIUM",
    "Rootkit":   "CRITICAL",
    "Downloader":"LOW",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def md5_file(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def detect_file_type(path: Path) -> str:
    """Basic magic-byte file type detection."""
    try:
        with open(path, "rb") as f:
            header = f.read(16)
        if header[:4] == b"\x7fELF":
            arch_byte = header[4] if len(header) > 4 else 0
            bits = "64-bit" if arch_byte == 2 else "32-bit"
            return f"ELF {bits} executable"
        if header[:2] in (b"MZ", b"ZM"):
            return "PE executable (Windows)"
        if header[:2] == b"#!":
            return "Shell script"
        if b"#!/" in header or b"python" in header[:32].lower():
            return "Script"
        if header[:4] == b"PK\x03\x04":
            return "ZIP archive"
        if header[:3] == b"\x1f\x8b\x08":
            return "Gzip archive"
        if header[:5] == b"#!/us" or header[:9] == b"#!/bin/sh":
            return "Shell script"
        # Try reading as text
        try:
            path.read_text(encoding="utf-8", errors="strict")
            return "Text/Script"
        except Exception:
            return "Binary (unknown)"
    except Exception:
        return "Unknown"


def heuristic_classify(path: Path) -> list:
    """Classify file using byte-string heuristics."""
    try:
        content = path.read_bytes()
    except Exception:
        return []

    matches = []
    for family, description, patterns in HEURISTIC_SIGS:
        hits = [p for p in patterns if p in content]
        if hits:
            matches.append({
                "rule": f"heuristic_{family.lower()}",
                "family": family,
                "description": description,
                "tags": [family, "heuristic"],
                "meta": {
                    "description": description,
                    "author": "THIR-heuristic",
                    "severity": FAMILY_SEVERITY.get(family, "MEDIUM"),
                },
                "strings_matched": [h.decode(errors="replace") for h in hits],
                "match_type": "heuristic",
            })

    return matches


def load_yara_rules(rules_dir: str) -> object:
    """Compile all YARA rules from the rules directory."""
    if not YARA_AVAILABLE:
        return None

    rules_path = Path(rules_dir)
    if not rules_path.exists():
        print(f"[Tool33] YARA rules dir not found: {rules_dir}", file=sys.stderr)
        return None

    rule_files = list(rules_path.rglob("*.yar")) + list(rules_path.rglob("*.yara"))
    if not rule_files:
        print(f"[Tool33] No .yar/.yara files found in {rules_dir}", file=sys.stderr)
        return None

    print(f"[Tool33] Loading {len(rule_files)} YARA rule files")
    filepaths = {}
    for rf in rule_files:
        namespace = rf.stem.replace("-", "_").replace(".", "_")
        filepaths[namespace] = str(rf)

    try:
        rules = yara.compile(filepaths=filepaths)
        return rules
    except yara.SyntaxError as e:
        print(f"[Tool33] YARA compile error: {e}", file=sys.stderr)
        return None


def yara_classify(path: Path, rules) -> list:
    """Run compiled YARA rules against a file."""
    if rules is None:
        return []
    try:
        matches = rules.match(str(path), timeout=30)
    except yara.TimeoutError:
        print(f"[Tool33] YARA timeout on {path.name}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"[Tool33] YARA error on {path.name}: {e}", file=sys.stderr)
        return []

    results = []
    for m in matches:
        family = (m.meta.get("malware_family")
                  or m.meta.get("family")
                  or m.meta.get("name")
                  or m.rule)
        severity = (m.meta.get("severity")
                    or FAMILY_SEVERITY.get(family, "MEDIUM"))
        strings_matched = [
            s.identifier for s in m.strings if s.instances
        ] if hasattr(m, "strings") else []

        results.append({
            "rule": m.rule,
            "namespace": m.namespace,
            "family": family,
            "description": m.meta.get("description", ""),
            "tags": list(m.tags),
            "meta": dict(m.meta),
            "strings_matched": strings_matched[:20],
            "match_type": "yara",
            "severity": severity,
        })

    return results


def analyze_file(path: Path, rules) -> dict:
    """Analyse a single downloaded file."""
    stat = path.stat()
    file_type = detect_file_type(path)

    # Run YARA first, fall back to heuristics
    matches = []
    if YARA_AVAILABLE and rules:
        matches = yara_classify(path, rules)

    if not matches:
        matches = heuristic_classify(path)

    # Determine overall classification
    classified = len(matches) > 0
    families = list({m["family"] for m in matches})
    severities = [
        m.get("severity") or m.get("meta", {}).get("severity", "LOW")
        for m in matches
    ]
    sev_order = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN"]
    top_severity = "UNKNOWN"
    for sev in sev_order:
        if sev in severities:
            top_severity = sev
            break

    return {
        "filename": path.name,
        "sha256": sha256_file(path),
        "md5": md5_file(path),
        "file_size_bytes": stat.st_size,
        "file_type": file_type,
        "classified": classified,
        "families": families,
        "severity": top_severity if classified else "UNKNOWN",
        "match_count": len(matches),
        "matches": matches,
        "analysis_method": "yara" if any(m["match_type"] == "yara" for m in matches)
                           else ("heuristic" if matches else "none"),
    }


def main():
    parser = argparse.ArgumentParser(description="Tool 33 — YARA Classifier")
    parser.add_argument("--downloads",   default="/tmp/cowrie-downloads",  help="Path to downloaded samples dir")
    parser.add_argument("--rules",       default="tools/yara_rules",       help="Path to YARA rules directory")
    parser.add_argument("--output",      default="data/yara_matches.json", help="Output path")
    parser.add_argument("--max-size-mb", type=int, default=50,             help="Max file size to scan (MB)")
    args = parser.parse_args()

    downloads_path = Path(args.downloads)
    if not downloads_path.exists():
        print(f"[Tool33] Downloads dir not found: {args.downloads} — writing empty output")
        output = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "downloads_dir": args.downloads,
            "downloads_found": False,
            "files_scanned": 0,
            "files_classified": 0,
            "yara_available": YARA_AVAILABLE,
            "analysis_method": "none",
            "families_detected": [],
            "severity_summary": {},
            "results": [],
        }
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"[Tool33] ✓ Written → {args.output} (no downloads)")
        return

    # Load YARA rules
    rules = load_yara_rules(args.rules)
    if not YARA_AVAILABLE:
        print("[Tool33] yara-python not installed — using heuristic classification")

    # Enumerate files
    files = [
        f for f in downloads_path.iterdir()
        if f.is_file() and not f.name.startswith(".")
    ]

    max_bytes = args.max_size_mb * 1024 * 1024
    results = []
    skipped = []

    for f in sorted(files):
        size = f.stat().st_size
        if size == 0:
            skipped.append({"filename": f.name, "reason": "empty file"})
            continue
        if size > max_bytes:
            skipped.append({"filename": f.name, "reason": f"exceeds {args.max_size_mb}MB limit"})
            continue
        print(f"[Tool33] Scanning {f.name} ({size} bytes)")
        result = analyze_file(f, rules)
        results.append(result)

    # Summary stats
    classified = [r for r in results if r["classified"]]
    all_families = []
    for r in classified:
        all_families.extend(r["families"])
    family_counts = defaultdict(int)
    for fam in all_families:
        family_counts[fam] += 1

    severity_summary = defaultdict(int)
    for r in results:
        severity_summary[r["severity"]] += 1

    # High/Critical samples for alert
    critical_samples = [
        {
            "filename": r["filename"],
            "sha256": r["sha256"],
            "families": r["families"],
            "severity": r["severity"],
        }
        for r in results
        if r["severity"] in ("CRITICAL", "HIGH")
    ]

    method = "yara" if (YARA_AVAILABLE and rules) else "heuristic"
    if not results:
        method = "none"

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "downloads_dir": args.downloads,
        "downloads_found": True,
        "files_scanned": len(results),
        "files_skipped": len(skipped),
        "files_classified": len(classified),
        "yara_available": YARA_AVAILABLE,
        "analysis_method": method,
        "families_detected": [
            {"family": k, "count": v}
            for k, v in sorted(family_counts.items(), key=lambda x: -x[1])
        ],
        "severity_summary": dict(severity_summary),
        "critical_samples": critical_samples,
        "skipped": skipped,
        "results": results,
    }

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"[Tool33] ✓ Written → {args.output}")
    print(f"[Tool33]   Scanned: {len(results)} | Classified: {len(classified)} | "
          f"Method: {method}")
    if critical_samples:
        for s in critical_samples:
            print(f"[Tool33]   ⚠ {s['severity']}: {s['filename']} → {', '.join(s['families'])}")


if __name__ == "__main__":
    main()
