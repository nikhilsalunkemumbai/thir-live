#!/usr/bin/env python3
"""
29_false_positive_live.py

THIR LIVE PIPELINE — PRODUCTION TOOL
Adapted from: InfraReadyPortfolio/06_soc_collaboration_tools/29_false_positive_tracker/

CHANGES FROM ORIGINAL (false_positive_tracker.py):
  1. read_alerts_csv()  REMOVED — read CSV with alert_id/signature_name/status
     REPLACED BY read_ir_cases_json() — reads data/ir_cases.json from Tool 26
     KEPT: Path existence/is_file() checks, PermissionError/OSError handling, log_info pattern

  2. process_alerts()  REWORKED — same stats-dict accumulation pattern, new taxonomy
     Original grouped by signature_name with "True/False Positive" status string
     Live version groups by src_ip with AbuseIPDB score + ISP + session behaviour as FP signal
     KEPT: missing-field skip+warning, log_info summary, stats dict structure

  3. generate_report()  REMOVED — CSV to stdout
     REPLACED BY write_fp_report() — writes data/fp_filter.json

  4. is_likely_fp()  NEW — three-signal FP decision function
     Signal 1: AbuseIPDB abuse_score below --threshold (default 25)
     Signal 2: Known scanner/researcher ISP name match (Shodan, Censys, Rapid7 etc.)
     Signal 3: Mass-scanner behaviour pattern (no commands, no downloads, ≤2 failed logins)
     Returns (bool, str reason) — reason written to output for analyst review

  5. load_threat_ips()  NEW — optionally loads Tool 27 enrichment data
     Builds {ip: enrichment_dict} lookup map
     If --threat-ips not provided: runs without enrichment, signal 1 unavailable

  6. parse_args()  EXTENDED
     REMOVED: --alerts-file
     ADDED:   --input (ir_cases.json), --threat-ips (threat_ips.json, optional),
              --output (fp_filter.json), --threshold (int, default 25)
     KEPT:    -v/--verbose unchanged

  7. log_info / log_warning / fatal_error  UNCHANGED — identical signatures and behaviour

ROLE IN THIR PIPELINE:
  Reads data/ir_cases.json (Tool 26 output).
  Optionally cross-references data/threat_ips.json (Tool 27 output) for AbuseIPDB scores.
  Flags scanner bots / research IPs as false positives using three independent signals.
  Writes data/fp_filter.json → pipeline and portfolio dashboard use clean_cases list only.

GITHUB ACTIONS USAGE:
  python tools/29_false_positive_live.py \
    --input data/ir_cases.json \
    --threat-ips data/threat_ips.json \
    --output data/fp_filter.json \
    --threshold 25

OUTPUT FORMAT (data/fp_filter.json):
  {
    "generated_at": "2025-01-15T11:00:05Z",
    "threshold_used": 25,
    "total_cases_in":  10,
    "confirmed_threats": 7,
    "flagged_as_fp":    3,
    "fp_rate":          0.3,
    "fp_cases": [
      {"case_id": "IR-def456", "src_ip": "45.142.212.100", "reason": "Known scanner ISP: Shodan"}
    ],
    "clean_cases": ["IR-abc123", "IR-ghi789", ...]
  }
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ----------------------------
# Known scanner / researcher ISPs
# FP Signal 2: ISP name match
# ----------------------------
KNOWN_SCANNER_ISPS = [
    "shodan",
    "censys",
    "rapid7",
    "securitytrails",
    "shadowserver",
    "binaryedge",
    "ipip.net",
    "internet measurement",
    "university",         # broad but catches most research scanners
    "research",
    "stretchoid",
    "internet-census",
]


# ----------------------------
# Logging helpers (unchanged from original)
# ----------------------------

def log_info(message: str, verbose: bool = False) -> None:
    if verbose:
        print(f"[INFO] {message}", file=sys.stderr)


def log_warning(message: str) -> None:
    print(f"[WARNING] {message}", file=sys.stderr)


def fatal_error(message: str, exit_code: int = 1) -> None:
    print(f"[ERROR] {message}", file=sys.stderr)
    sys.exit(exit_code)


# ----------------------------
# Data loading (replaces read_alerts_csv)
# ----------------------------

def read_ir_cases_json(file_path: Path, verbose: bool = False) -> List[Dict]:
    """
    Load IR cases from data/ir_cases.json written by Tool 26.
    Replaces read_alerts_csv() — same Path existence/type checks and
    PermissionError/OSError handling pattern preserved.
    """
    log_info(f"Attempting to read IR cases file: {file_path}", verbose)

    if not file_path.exists():
        fatal_error(f"IR cases file not found: {file_path}")

    if not file_path.is_file():
        fatal_error(f"Provided path is not a file: {file_path}")

    try:
        with file_path.open(mode="r", encoding="utf-8") as fh:
            data = json.load(fh)

        cases = data.get("cases", [])
        if not cases:
            fatal_error("IR cases file contains no cases — nothing to process")

        log_info(f"Read {len(cases)} IR case(s)", verbose)
        return cases

    except json.JSONDecodeError as exc:
        fatal_error(f"JSON parse error in {file_path}: {exc}")
    except PermissionError:
        fatal_error(f"Permission denied when accessing file: {file_path}")
    except OSError as exc:
        fatal_error(f"File I/O error: {exc}")

    return []  # unreachable — keeps type checkers happy


def load_threat_ips(file_path: Optional[Path], verbose: bool = False) -> Dict[str, Dict]:
    """
    Optionally load enriched IP data from data/threat_ips.json (Tool 27 output).
    Returns {ip_address: enrichment_dict} for O(1) lookup in is_likely_fp().
    Returns empty dict if path not provided — tool runs without enrichment gracefully.
    """
    if file_path is None:
        log_info("--threat-ips not provided — AbuseIPDB score signal unavailable", verbose)
        return {}

    if not file_path.exists():
        log_warning(f"Threat IPs file not found: {file_path} — continuing without enrichment")
        return {}

    try:
        with file_path.open(mode="r", encoding="utf-8") as fh:
            data = json.load(fh)

        threat_map = {
            entry["indicator"]: entry
            for entry in data.get("ips", [])
            if entry.get("indicator")
        }
        log_info(f"Loaded enrichment for {len(threat_map)} IP(s)", verbose)
        return threat_map

    except (json.JSONDecodeError, OSError) as exc:
        log_warning(f"Could not load threat IPs file: {exc} — continuing without enrichment")
        return {}


# ----------------------------
# FP decision logic (new)
# ----------------------------

def is_likely_fp(
    case: Dict,
    threat_map: Dict[str, Dict],
    threshold: int,
) -> Tuple[bool, str]:
    """
    Three-signal false positive detection for a single IR case.

    Signal 1 — AbuseIPDB score (requires Tool 27 enrichment):
      abuse_score < threshold → likely scanner or researcher, not targeted attacker

    Signal 2 — Known scanner ISP name match:
      ISP field from Tool 27 contains known scanner org name

    Signal 3 — Mass-scanner behaviour pattern (no enrichment needed):
      No commands executed AND no file downloads AND ≤ 2 login attempts
      → pure port-scanner, no interactive session, typical for Shodan/Masscan sweeps

    Returns (is_fp: bool, reason: str)
    """
    src_ip = case.get("src_ip", "")
    enrichment = threat_map.get(src_ip, {})

    # Signal 1: AbuseIPDB confidence score
    if enrichment:
        abuse_score = enrichment.get("abuse_score", -1)
        if 0 <= abuse_score < threshold:
            return True, f"AbuseIPDB score {abuse_score} below threshold {threshold}"

    # Signal 2: Known scanner ISP
    if enrichment:
        isp = enrichment.get("isp", "").lower()
        for known in KNOWN_SCANNER_ISPS:
            if known in isp:
                return True, f"Known scanner ISP: {enrichment.get('isp', isp)}"

    # Signal 3: Mass-scanner behaviour pattern (enrichment-independent)
    commands   = case.get("commands", [])
    downloads  = case.get("downloads", [])
    login_attempts = case.get("login_attempts", 0)
    login_success  = case.get("login_success", False)

    if (
        not commands
        and not downloads
        and not login_success
        and login_attempts <= 2
    ):
        return True, "Mass-scanner pattern: no commands, no downloads, ≤2 login attempts"

    return False, ""


# ----------------------------
# Core processing (replaces process_alerts)
# ----------------------------

def process_cases(
    cases: List[Dict],
    threat_map: Dict[str, Dict],
    threshold: int,
    verbose: bool = False,
) -> Dict:
    """
    Evaluate every IR case for false positive signals.
    Replaces process_alerts() — same stats-dict accumulation pattern,
    same missing-field skip+warning, same log_info summary at end.

    Original: grouped by signature_name, counted "False Positive" status strings
    Live:     groups by src_ip, uses is_likely_fp() three-signal detection
    """
    fp_cases   = []
    clean_cases = []

    for idx, case in enumerate(cases, start=1):
        case_id = case.get("case_id", "")
        src_ip  = case.get("src_ip", "")

        # Missing field handling — same pattern as original process_alerts()
        if not case_id:
            log_warning(f"Case {idx}: Missing case_id; skipping")
            continue
        if not src_ip:
            log_warning(f"Case {idx} ({case_id}): Missing src_ip; skipping")
            continue

        is_fp, reason = is_likely_fp(case, threat_map, threshold)

        if is_fp:
            fp_cases.append({
                "case_id": case_id,
                "src_ip":  src_ip,
                "reason":  reason,
            })
            log_info(f"FP flagged: {case_id} ({src_ip}) — {reason}", verbose)
        else:
            clean_cases.append(case_id)
            log_info(f"Confirmed threat: {case_id} ({src_ip})", verbose)

    total     = len(fp_cases) + len(clean_cases)
    fp_count  = len(fp_cases)
    fp_rate   = round(fp_count / total, 4) if total > 0 else 0.0

    # Same log_info summary pattern as original process_alerts()
    log_info(
        f"Processed {total} case(s): {len(clean_cases)} confirmed threat(s), "
        f"{fp_count} FP(s) ({fp_rate:.1%})",
        verbose,
    )

    return {
        "fp_cases":   fp_cases,
        "clean_cases": clean_cases,
        "total":      total,
        "fp_count":   fp_count,
        "fp_rate":    fp_rate,
    }


# ----------------------------
# JSON output (replaces generate_report)
# ----------------------------

def write_fp_report(result: Dict, threshold: int, output_path: Path) -> None:
    """
    Write FP filter results to data/fp_filter.json.
    Replaces generate_report() — same role, JSON output for pipeline and dashboard.
    """
    report = {
        "generated_at":      datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "threshold_used":    threshold,
        "total_cases_in":    result["total"],
        "confirmed_threats": len(result["clean_cases"]),
        "flagged_as_fp":     result["fp_count"],
        "fp_rate":           result["fp_rate"],
        "fp_cases":          result["fp_cases"],
        "clean_cases":       result["clean_cases"],
    }

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open(mode="w", encoding="utf-8") as fh:
            json.dump(report, fh, indent=2)
    except OSError as exc:
        fatal_error(f"Failed to write output file {output_path}: {exc}")


# ----------------------------
# CLI (extended from original)
# ----------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Filter false positives from Cowrie honeypot IR cases."
    )
    parser.add_argument(
        "--input",
        required=True,
        type=Path,
        help="Path to data/ir_cases.json written by Tool 26",
    )
    parser.add_argument(
        "--threat-ips",
        type=Path,
        default=None,
        help="Path to data/threat_ips.json from Tool 27 (optional — enables AbuseIPDB signal)",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to write fp_filter.json output",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=25,
        help="AbuseIPDB score below which an IP is treated as FP (default: 25)",
    )
    # -v/--verbose preserved unchanged from original
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose informational output",
    )
    return parser.parse_args()


# ----------------------------
# Entry point
# ----------------------------

def main() -> None:
    args = parse_args()
    verbose = args.verbose

    log_info("Starting False Positive Tracker (Cowrie Live)", verbose)

    # Load IR cases from Tool 26
    cases = read_ir_cases_json(args.input, verbose=verbose)

    # Optionally load Tool 27 enrichment
    threat_map = load_threat_ips(args.threat_ips, verbose=verbose)

    # Process — same flow as original: load → process → report
    result = process_cases(cases, threat_map, args.threshold, verbose=verbose)

    # Write JSON output
    write_fp_report(result, args.threshold, args.output)

    log_info(
        f"FP filter complete — "
        f"{result['total']} cases in, "
        f"{len(result['clean_cases'])} clean, "
        f"{result['fp_count']} FP filtered",
        verbose,
    )


if __name__ == "__main__":
    main()
