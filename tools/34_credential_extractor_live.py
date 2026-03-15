#!/usr/bin/env python3
"""
Tool 34 — Credential Pair Extractor (THIR Live)

Reads raw Cowrie NDJSON log and extracts credential intelligence:
  - All username/password pairs attempted (failed + success)
  - Aggregated stats: top usernames, top passwords, top pairs
  - Successful auth pairs flagged separately (high value)

No external dependencies — stdlib only.

Usage:
    python tools/34_credential_extractor_live.py \\
        --input  /tmp/cowrie.json \\
        --output data/credentials.json \\
        --verbose

Output schema (data/credentials.json):
    {
      "generated_at":     "ISO timestamp",
      "total_attempts":   int,   # all login events (failed + success)
      "unique_pairs":     int,   # distinct username+password combos
      "unique_usernames": int,
      "unique_passwords": int,
      "top_usernames":    [ {"username": str, "count": int} ],   # top 10
      "top_passwords":    [ {"password": str, "count": int} ],   # top 10
      "top_pairs":        [ {"username": str, "password": str, "count": int} ], # top 10
      "success_pairs":    [ {"username": str, "password": str,
                             "src_ip": str, "timestamp": str} ]
    }

Pipeline position: Step 7a — after Tool 26, before Step 8 (IP extraction).
Reads /tmp/cowrie.json directly (same file fetched in Step 6).

THIR Live — nikhilsalunkemumbai/thir-live
"""

import argparse
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone


# ─────────────────────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────────────────────

def log(msg, level="INFO", verbose=False):
    if level == "INFO" and not verbose:
        return
    sys.stderr.write(f"[{level}] {msg}\n")
    sys.stderr.flush()


# ─────────────────────────────────────────────────────────────────────────────
# Cowrie log parser
# ─────────────────────────────────────────────────────────────────────────────

COWRIE_LOGIN_FAILED  = "cowrie.login.failed"
COWRIE_LOGIN_SUCCESS = "cowrie.login.success"

LOGIN_EVENTS = {COWRIE_LOGIN_FAILED, COWRIE_LOGIN_SUCCESS}


def parse_cowrie_credentials(input_path, verbose=False):
    """
    Parse Cowrie NDJSON log and extract all credential events.

    Returns:
        all_attempts  : list of dicts — every login event
        success_pairs : list of dicts — login.success events only
    """
    if not os.path.exists(input_path):
        log(f"Input file not found: {input_path}", "ERROR", True)
        return [], []

    all_attempts  = []
    success_pairs = []
    lines_read    = 0
    lines_skipped = 0

    with open(input_path, encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lines_read += 1

            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                lines_skipped += 1
                continue

            event_id = event.get("eventid", "")
            if event_id not in LOGIN_EVENTS:
                continue

            username  = event.get("username", "")
            password  = event.get("password", "")
            src_ip    = event.get("src_ip", "")
            timestamp = event.get("timestamp", "")

            # Skip events with no credentials at all
            if not username and not password:
                continue

            record = {
                "username":  username,
                "password":  password,
                "src_ip":    src_ip,
                "timestamp": timestamp,
                "success":   event_id == COWRIE_LOGIN_SUCCESS,
            }

            all_attempts.append(record)

            if event_id == COWRIE_LOGIN_SUCCESS:
                success_pairs.append({
                    "username":  username,
                    "password":  password,
                    "src_ip":    src_ip,
                    "timestamp": timestamp,
                })

    log(f"Lines read: {lines_read} | Skipped (bad JSON): {lines_skipped}", "INFO", verbose)
    log(f"Login events found: {len(all_attempts)} "
        f"({len(success_pairs)} success, "
        f"{len(all_attempts) - len(success_pairs)} failed)", "INFO", verbose)

    return all_attempts, success_pairs


# ─────────────────────────────────────────────────────────────────────────────
# Aggregation
# ─────────────────────────────────────────────────────────────────────────────

TOP_N = 10


def aggregate(all_attempts, success_pairs, verbose=False):
    """
    Build aggregated credential intelligence from raw attempt list.

    Returns the full output dict ready for JSON serialisation.
    """
    username_counter = Counter()
    password_counter = Counter()
    pair_counter     = Counter()
    pair_set         = set()

    for rec in all_attempts:
        u = rec["username"]
        p = rec["password"]
        username_counter[u] += 1
        password_counter[p] += 1
        pair_key = (u, p)
        pair_counter[pair_key] += 1
        pair_set.add(pair_key)

    top_usernames = [
        {"username": u, "count": c}
        for u, c in username_counter.most_common(TOP_N)
    ]

    top_passwords = [
        {"password": p, "count": c}
        for p, c in password_counter.most_common(TOP_N)
    ]

    top_pairs = [
        {"username": u, "password": p, "count": c}
        for (u, p), c in pair_counter.most_common(TOP_N)
    ]

    # Deduplicate success_pairs by (username, password, src_ip) while
    # preserving earliest timestamp per unique combo
    seen_success = {}
    for sp in success_pairs:
        key = (sp["username"], sp["password"], sp["src_ip"])
        if key not in seen_success:
            seen_success[key] = sp
        else:
            # Keep earliest timestamp
            existing_ts = seen_success[key]["timestamp"]
            if sp["timestamp"] and sp["timestamp"] < existing_ts:
                seen_success[key] = sp

    deduped_success = sorted(
        seen_success.values(),
        key=lambda x: x.get("timestamp", "")
    )

    log(f"Unique pairs: {len(pair_set)} | "
        f"Unique usernames: {len(username_counter)} | "
        f"Unique passwords: {len(password_counter)}", "INFO", verbose)
    log(f"Successful auth pairs (deduped): {len(deduped_success)}", "INFO", verbose)

    return {
        "generated_at":     datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_attempts":   len(all_attempts),
        "unique_pairs":     len(pair_set),
        "unique_usernames": len(username_counter),
        "unique_passwords": len(password_counter),
        "top_usernames":    top_usernames,
        "top_passwords":    top_passwords,
        "top_pairs":        top_pairs,
        "success_pairs":    deduped_success,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Output
# ─────────────────────────────────────────────────────────────────────────────

def write_output(data, output_path, verbose=False):
    out_dir = os.path.dirname(output_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        log(f"Credentials written to {output_path}", "INFO", verbose)
    except OSError as e:
        log(f"Failed to write output: {e}", "ERROR", True)
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# Summary to stderr (visible in GitHub Actions log)
# ─────────────────────────────────────────────────────────────────────────────

def print_summary(data):
    sys.stderr.write("\n━━━ [Tool 34] Credential Intelligence Summary ━━━\n")
    sys.stderr.write(f"  Total login attempts : {data['total_attempts']}\n")
    sys.stderr.write(f"  Unique pairs         : {data['unique_pairs']}\n")
    sys.stderr.write(f"  Unique usernames     : {data['unique_usernames']}\n")
    sys.stderr.write(f"  Unique passwords     : {data['unique_passwords']}\n")

    if data["top_usernames"]:
        sys.stderr.write("\n  Top usernames:\n")
        for u in data["top_usernames"][:5]:
            sys.stderr.write(f"    {u['username']:<20} {u['count']:>4} attempts\n")

    if data["top_passwords"]:
        sys.stderr.write("\n  Top passwords:\n")
        for p in data["top_passwords"][:5]:
            sys.stderr.write(f"    {p['password']:<20} {p['count']:>4} attempts\n")

    if data["success_pairs"]:
        sys.stderr.write(f"\n  ⚠️  Successful auth pairs ({len(data['success_pairs'])}):\n")
        for sp in data["success_pairs"]:
            sys.stderr.write(
                f"    {sp['src_ip']:<20} "
                f"user={sp['username']!r:<15} "
                f"pass={sp['password']!r}\n"
            )
    else:
        sys.stderr.write("\n  No successful authentications recorded.\n")

    sys.stderr.write("━━━ [Tool 34] Done ━━━\n\n")
    sys.stderr.flush()


# ─────────────────────────────────────────────────────────────────────────────
# Empty output (no cowrie.json or no login events)
# ─────────────────────────────────────────────────────────────────────────────

def empty_output():
    return {
        "generated_at":     datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_attempts":   0,
        "unique_pairs":     0,
        "unique_usernames": 0,
        "unique_passwords": 0,
        "top_usernames":    [],
        "top_passwords":    [],
        "top_pairs":        [],
        "success_pairs":    [],
    }


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tool 34 — THIR Credential Pair Extractor + Password Analyser"
    )
    parser.add_argument(
        "--input", "-i",
        default="/tmp/cowrie.json",
        help="Path to Cowrie NDJSON log file (default: /tmp/cowrie.json)"
    )
    parser.add_argument(
        "--output", "-o",
        default="data/credentials.json",
        help="Output path for credentials JSON (default: data/credentials.json)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging to stderr"
    )
    args = parser.parse_args()

    log("Tool 34 — Credential Extractor started", "INFO", True)
    log(f"Input : {args.input}", "INFO", args.verbose)
    log(f"Output: {args.output}", "INFO", args.verbose)

    # Handle missing input gracefully — write empty output so pipeline continues
    if not os.path.exists(args.input):
        log(f"Input file not found: {args.input} — writing empty output", "WARN", True)
        data = empty_output()
        write_output(data, args.output, args.verbose)
        print_summary(data)
        sys.exit(0)

    all_attempts, success_pairs = parse_cowrie_credentials(args.input, args.verbose)

    if not all_attempts:
        log("No login events found in input — writing empty output", "WARN", True)
        data = empty_output()
    else:
        data = aggregate(all_attempts, success_pairs, args.verbose)

    write_output(data, args.output, args.verbose)
    print_summary(data)

    log("Tool 34 — Credential Extractor completed successfully", "INFO", True)
    sys.exit(0)


if __name__ == "__main__":
    main()
