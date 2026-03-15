#!/usr/bin/env python3
"""
Tool 28 — SOC Handover Report Generator (THIR Live)

Reads live pipeline outputs and generates a structured Markdown
SOC shift handover report. No external dependencies — stdlib only.

Usage:
    python tools/28_soc_handover_live.py \\
        --ir-cases       data/ir_cases.json \\
        --threat-ips     data/threat_ips.json \\
        --fp-filter      data/fp_filter.json \\
        --stats          data/stats.json \\
        --malware-report data/malware_report.json \\
        --output         data/soc_handover.md \\
        --verbose

CHANGES vs original:
    v2 — 2026-03-08
    1. Session grouping for report readability
       Confirmed cases are split into two sections:
         § Priority Cases    — individual full-detail blocks (HIGH/CRIT or
                               has auth success / commands / downloads)
         § Reconnaissance    — same-IP sessions grouped into a compact table
       ir_cases.json is NEVER modified — grouping is report-only.

    2. Malware report integration
       Reads data/malware_report.json (written by Tool 31) and links
       malware findings to IR cases that had download events. When a
       HIGH severity malware sample is found, a dedicated warning block
       appears at the top of the relevant Priority Case section.

    3. Pipeline health now shows Tool 31 row

    Grouping rules (from session analysis):
        NEVER group: login_success=True, has commands, has downloads
        ALWAYS group: same src_ip, no auth, no commands, no downloads
        Window: 120 minutes between consecutive sessions from same IP
        Min sessions to trigger grouping: 2
        Merged severity: MEDIUM if ≥10 sessions, LOW otherwise

    v2.1 — 2026-03-10
    4. IOC defanging added to all report output
       All IPs, URLs, and domains written into the markdown report are
       defanged to prevent AV/EDR heuristic false positives (e.g. Norton
       BV:Downloader-ADK[Drp]). Defanging is report-only — source JSON
       data is never modified.
       Rules applied:
         - IPv4: last octet dot → [.]   e.g. 1.2.3.4 → 1.2.3[.]4
         - http:// → hxxp://
         - https:// → hxxps://
         - ftp:// → fxxp://
         - Bare domain dots (in known bad context): example[.]com
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone


# ─────────────────────────────────────────────────────────────────────────────
# Grouping constants
# ─────────────────────────────────────────────────────────────────────────────

GROUP_WINDOW_MINUTES = 120   # max gap between sessions to stay in same group
GROUP_MIN_SESSIONS   = 2     # need at least this many sessions to group
GROUP_MEDIUM_THRESH  = 10    # sessions ≥ this → MEDIUM severity on the group


# ─────────────────────────────────────────────────────────────────────────────
# Defang helpers  (report-only — source JSON is never touched)
# ─────────────────────────────────────────────────────────────────────────────

# Compiled patterns for performance
_RE_IPV4 = re.compile(
    r'\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b'
)
_RE_URL_SCHEME = re.compile(
    r'(?i)(https?|ftp)://'
)
_RE_DOMAIN = re.compile(
    r'(?<!\[)\.(?!com\b|net\b|org\b|gov\b|io\b|ru\b|cn\b|de\b|uk\b|xyz\b|info\b)',
    # NOTE: This pattern is intentionally NOT used for generic text;
    # use defang_domain() explicitly only when you know the value is a domain.
)


def defang_ip(text: str) -> str:
    """
    Defang all IPv4 addresses in text.
    1.2.3.4  →  1.2.3[.]4
    Only the LAST dot is bracketed (industry standard).
    """
    return _RE_IPV4.sub(r'\1.\2.\3[.]\4', str(text))


def defang_url(text: str) -> str:
    """
    Defang URL schemes in text.
    http://  →  hxxp://
    https:// →  hxxps://
    ftp://   →  fxxp://
    """
    def _replace(m):
        scheme = m.group(1).lower()
        if scheme == "https":
            return "hxxps://"
        if scheme == "http":
            return "hxxp://"
        if scheme == "ftp":
            return "fxxp://"
        return m.group(0)
    return _RE_URL_SCHEME.sub(_replace, str(text))


def defang_domain(text: str) -> str:
    """
    Defang a bare domain or hostname by bracketing ALL dots.
    example.com  →  example[.]com
    sub.evil.ru  →  sub[.]evil[.]ru
    Use this only when you KNOW the value is a domain/hostname,
    not for generic text (would break markdown links etc.).
    """
    return str(text).replace(".", "[.]")


def defang(text: str) -> str:
    """
    Full defang pipeline for generic text fields that may contain
    IPs, URLs, and attacker command output.
    Order matters: URLs first (so IP inside URL gets both treatments),
    then IPs.
    """
    text = defang_url(str(text))
    text = defang_ip(text)
    return text


# ─────────────────────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────────────────────

def log(msg, level="INFO", verbose=False):
    if level == "INFO" and not verbose:
        return
    sys.stderr.write(f"[{level}] {msg}\n")
    sys.stderr.flush()


# ─────────────────────────────────────────────────────────────────────────────
# Safe JSON loader
# ─────────────────────────────────────────────────────────────────────────────

def load_json(path, label, verbose=False):
    if not os.path.exists(path):
        log(f"{label} not found at {path} — skipping", "WARN", True)
        return None
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        log(f"Loaded {label} ({path})", "INFO", verbose)
        return data
    except Exception as e:
        log(f"Failed to parse {label}: {e}", "ERROR", True)
        return None


# ─────────────────────────────────────────────────────────────────────────────
# Display helpers
# ─────────────────────────────────────────────────────────────────────────────

def severity_badge(sev):
    return {
        "CRITICAL": "🚨 CRITICAL",
        "HIGH":     "🔴 HIGH",
        "MEDIUM":   "🟡 MEDIUM",
        "LOW":      "🟢 LOW",
    }.get((sev or "LOW").upper(), "🟢 LOW")


def severity_icon(sev):
    return {
        "CRITICAL": "🚨",
        "HIGH":     "🔴",
        "MEDIUM":   "🟠",
        "LOW":      "🟢",
    }.get((sev or "LOW").upper(), "🟢")


def score_badge(score):
    s = int(score or 0)
    if s >= 80: return f"**{s}** ⚠️"
    if s >= 25: return f"**{s}**"
    return str(s)


def honeypot_icon(status):
    return {
        "HEALTHY":  "✅ HEALTHY",
        "UP":       "✅ UP",
        "DOWN":     "❌ DOWN",
        "DEGRADED": "⚠️ DEGRADED",
    }.get((status or "UNKNOWN").upper(), f"❓ {status}")


def fmt_ts(ts, length=16):
    """Trim ISO timestamp to desired length."""
    if not ts:
        return "unknown"
    return str(ts)[:length].replace("T", " ")


# ─────────────────────────────────────────────────────────────────────────────
# Timestamp parser (no external deps)
# ─────────────────────────────────────────────────────────────────────────────

def parse_dt(s):
    """Parse ISO 8601 timestamp → UTC-aware datetime. Returns datetime.min on failure."""
    if not s:
        return datetime.min.replace(tzinfo=timezone.utc)
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return datetime.min.replace(tzinfo=timezone.utc)


# ─────────────────────────────────────────────────────────────────────────────
# Grouping logic — report-only, ir_cases.json is never modified
# ─────────────────────────────────────────────────────────────────────────────

def is_groupable(case):
    """
    A case is groupable (can be merged into a reconnaissance summary row)
    if it has NO meaningful attacker activity: no auth success, no commands,
    no file downloads.

    Cases that are NOT groupable become individual Priority Case blocks.
    """
    if case.get("login_success"):
        return False
    commands  = case.get("commands",  []) or []
    downloads = case.get("downloads", []) or []
    if commands:
        return False
    if downloads:
        return False
    return True


def group_cases_for_report(cases):
    """
    Split a flat list of IR cases into:
      - priority_cases : list of individual case dicts (render as full blocks)
      - grouped_cases  : list of group-summary dicts (render as table rows)

    Grouping algorithm:
      1. Cases that are not groupable go directly to priority_cases.
      2. Remaining cases are sorted by src_ip then first_seen.
      3. For each src_ip, sessions are accumulated into a group while
         the gap between consecutive first_seen timestamps is ≤ GROUP_WINDOW_MINUTES.
         A gap larger than the window starts a new group for that IP.
      4. Groups with < GROUP_MIN_SESSIONS stay as individual entries (not
         promoted to priority, but not merged either).
      5. Merged groups carry the highest TTPs from all constituent cases.

    Returns (priority_cases, grouped_cases).
    grouped_cases entries are dicts with either:
      { 'grouped': False, 'case': <original case> }   — singleton, render individually
      { 'grouped': True,  'src_ip': ..., 'session_count': ..., ... }  — merged row
    """
    priority_cases = []
    groupable      = []

    for case in cases:
        if is_groupable(case):
            groupable.append(case)
        else:
            priority_cases.append(case)

    # Sort groupable by IP then first_seen so gap calculation is sequential
    groupable.sort(key=lambda c: (c.get("src_ip", ""), c.get("first_seen", "")))

    # Accumulate sessions into named buckets: {bucket_key: [case, ...]}
    buckets = {}   # bucket_key → list of cases
    bucket_order = []

    for case in groupable:
        ip = case.get("src_ip", "unknown")

        # Find which bucket this case belongs to (last open bucket for this IP
        # that is within the time window)
        placed = False
        for bkey in reversed(bucket_order):
            if not bkey.startswith(ip + "::"):
                continue
            last_case = buckets[bkey][-1]
            last_seen_dt = parse_dt(last_case.get("last_seen") or last_case.get("first_seen"))
            this_seen_dt = parse_dt(case.get("first_seen"))
            gap_minutes = (this_seen_dt - last_seen_dt).total_seconds() / 60
            if gap_minutes <= GROUP_WINDOW_MINUTES:
                buckets[bkey].append(case)
                placed = True
                break

        if not placed:
            # New bucket for this IP (or gap exceeded — start fresh)
            bkey = f"{ip}::{case.get('first_seen', '')}"
            buckets[bkey] = [case]
            bucket_order.append(bkey)

    # Build grouped_cases from buckets
    grouped_cases = []

    for bkey in bucket_order:
        session_list = buckets[bkey]
        actual_ip = session_list[0].get("src_ip", "?")

        if len(session_list) < GROUP_MIN_SESSIONS:
            # Singleton — render as individual row in the recon table
            grouped_cases.append({
                "grouped": False,
                "case":    session_list[0],
            })
            continue

        # Merge sessions
        all_ttps = list({t for c in session_list for t in (c.get("ttps") or [])})
        all_ttps = sorted(all_ttps) or ["T1592"]

        total_login_attempts    = sum(c.get("login_attempts", 0) for c in session_list)
        total_duration_seconds  = sum(c.get("duration_seconds", 0) for c in session_list)

        severity = "MEDIUM" if len(session_list) >= GROUP_MEDIUM_THRESH else "LOW"

        grouped_cases.append({
            "grouped":               True,
            "src_ip":                actual_ip,
            "session_count":         len(session_list),
            "first_seen":            session_list[0].get("first_seen", "?"),
            "last_seen":             session_list[-1].get("last_seen", "?"),
            "total_login_attempts":  total_login_attempts,
            "total_duration_seconds": total_duration_seconds,
            "ttps":                  all_ttps,
            "severity":              severity,
            "case_ids":              [c.get("case_id", "?") for c in session_list],
        })

    # Sort grouped_cases: MEDIUM first, then by session_count descending
    grouped_cases.sort(key=lambda g: (
        0 if g.get("severity") == "MEDIUM" else 1,
        -(g.get("session_count", 1))
    ))

    return priority_cases, grouped_cases


# ─────────────────────────────────────────────────────────────────────────────
# Malware report helpers
# ─────────────────────────────────────────────────────────────────────────────

def build_malware_index(malware_data):
    """
    Build a dict mapping SHA-256 hash → sample record from malware_report.json.
    Used to cross-reference downloads in IR cases.
    """
    if not malware_data:
        return {}
    index = {}
    for sample in malware_data.get("samples", []):
        sha256 = sample.get("sha256")
        if sha256:
            index[sha256] = sample
        # Also index by file_name (the Cowrie download filename is often the hash)
        fname = sample.get("file_name")
        if fname:
            index[fname] = sample
    return index


def get_malware_for_case(case, malware_index):
    """
    Look up malware analysis results for a given IR case.
    Checks case downloads list against malware_index.
    Returns list of matching sample records (may be empty).
    """
    downloads = case.get("downloads", []) or []
    results   = []
    seen      = set()
    for dl in downloads:
        # dl may be a hash string or a dict with sha256/filename
        if isinstance(dl, dict):
            candidates = [dl.get("sha256", ""), dl.get("filename", ""), dl.get("url", "")]
        else:
            candidates = [str(dl)]
        for key in candidates:
            if key and key in malware_index and key not in seen:
                seen.add(key)
                results.append(malware_index[key])
    return results


# ─────────────────────────────────────────────────────────────────────────────
# Individual case renderer (full detail block)
# ─────────────────────────────────────────────────────────────────────────────

def render_priority_case(case, malware_index, L):
    """Append Markdown lines for a single priority IR case."""

    def ln(s=""):
        L.append(s)

    case_id       = case.get("case_id", "?")
    src_ip        = defang_ip(case.get("src_ip", "?"))
    sev           = case.get("severity", "LOW")
    login_success = case.get("login_success", False)
    attempts      = case.get("login_attempts", "?")
    commands      = case.get("commands",  []) or []
    downloads     = case.get("downloads", []) or []
    ttps          = case.get("ttps",      []) or []
    first_seen    = case.get("first_seen", "unknown")
    last_seen     = case.get("last_seen",  "unknown")
    duration      = case.get("duration_seconds", 0)
    timeline      = case.get("timeline",  []) or []

    tl_events = [e.get("event", "") for e in timeline]
    has_tcpip = any("direct-tcpip" in e for e in tl_events)

    # Defang commands (may contain wget/curl URLs and IPs)
    commands_defanged  = [defang(cmd) for cmd in commands]

    # Defang download references (URLs / hashes in string form)
    downloads_defanged = []
    for d in downloads:
        if isinstance(d, dict):
            downloads_defanged.append(
                defang(d.get("url") or d.get("filename") or d.get("sha256") or str(d))
            )
        else:
            downloads_defanged.append(defang(str(d)))

    # Malware findings for this case
    malware_hits = get_malware_for_case(case, malware_index)
    high_malware = [m for m in malware_hits if m.get("severity") in ("HIGH", "CRITICAL")]

    # ── Malware warning banner ─────────────────────────────────────────────
    if high_malware:
        ln("```")
        ln("⚠️  MALWARE ANALYSIS — HIGH SEVERITY SAMPLE DETECTED")
        for m in high_malware:
            vt  = m.get("virustotal") or {}
            det = f"VT: {vt.get('malicious',0)}/{vt.get('total',0)}" if vt.get("found") else "Not yet in VT"
            ln(f"   File  : {m.get('file_name','?')}  ({m.get('file_type','?')})")
            ln(f"   SHA256: {m.get('sha256','?')[:48]}...")
            ln(f"   Score : {m.get('threat_score','?')}/100  |  {det}")
            for ind in (m.get("suspicious_indicators") or [])[:4]:
                # Defang indicator match strings (may contain IPs/URLs)
                match_defanged = defang(ind.get('match', '')[:60])
                ln(f"   ↳ {ind.get('indicator','?')}: {match_defanged}")
        ln("```")
        ln()

    ln(f"### {severity_badge(sev)} · {case_id}")
    ln()
    ln("| Field | Detail |")
    ln("|---|---|")
    ln(f"| **Source IP** | `{src_ip}` |")
    ln(f"| **First Seen** | {fmt_ts(first_seen)} |")
    ln(f"| **Last Seen** | {fmt_ts(last_seen)} |")
    ln(f"| **Session Duration** | {duration}s |")
    ln(f"| **Login Attempts** | {attempts} |")
    ln(f"| **Auth Success** | {'✅ Yes — session established' if login_success else '❌ No'} |")

    if has_tcpip:
        ln(f"| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |")
    if commands_defanged:
        ln(f"| **Commands Executed** | `{', '.join(commands_defanged[:5])}` |")
    if downloads_defanged:
        ln(f"| **Download Attempts** | {', '.join(downloads_defanged[:3])} |")
    if malware_hits:
        malware_sum = ", ".join(
            f"{m.get('file_name','?')} ({m.get('severity','?')})" for m in malware_hits
        )
        ln(f"| **Malware Analysis** | {malware_sum} |")
    if ttps:
        ln(f"| **TTPs (MITRE)** | {' · '.join(ttps)} |")
    ln()

    # Timeline — defang event strings
    if timeline:
        ln("**Attack Timeline:**")
        ln()
        ln("| Time (UTC) | Event |")
        ln("|---|---|")
        for e in timeline:
            ts  = fmt_ts(e.get("timestamp", "?"), 19)
            evt = defang(e.get("event", "?"))
            ln(f"| `{ts}` | `{evt}` |")
        ln()

    # Recommended actions — defang IP in action items
    ln("**Recommended Actions:**")
    if sev in ("HIGH", "CRITICAL"):
        ln(f"- [ ] Submit `{src_ip}` to AbuseIPDB if not already reported")
        ln(f"- [ ] Block `{src_ip}` at perimeter firewall / security group")
        if has_tcpip:
            ln(f"- [ ] Investigate TCP tunnel target — port forwarding via honeypot")
            ln(f"- [ ] Confirm tunnel target is not internal infrastructure")
        if commands_defanged:
            ln(f"- [ ] Review commands for lateral movement indicators")
        if downloads_defanged:
            ln(f"- [ ] Submit download hash(es) to VirusTotal")
            if not malware_hits:
                ln(f"- [ ] Run Tool 31 malware analyzer on captured payload(s)")
        if high_malware:
            for m in high_malware:
                vt_link = (m.get("virustotal") or {}).get("vt_link", "")
                if vt_link:
                    # Defang VT link — it's a legitimate URL but AV may flag it
                    ln(f"- [ ] Review VT report: {defang_url(vt_link)}")
        ln(f"- [ ] Escalate to Tier 2 if pattern repeats next shift")
    else:
        ln(f"- [ ] Monitor for repeat activity from `{src_ip}`")
        if downloads_defanged:
            ln(f"- [ ] Run Tool 31 malware analyzer on captured payload(s)")
        ln(f"- [ ] No immediate escalation required")
    ln()


# ─────────────────────────────────────────────────────────────────────────────
# Report builder
# ─────────────────────────────────────────────────────────────────────────────

def build_report(ir, threats, fp, stats, malware, creds=None, ssh_fps=None, cmd_cls=None, asn_cls=None, yara=None):
    now         = datetime.now(timezone.utc)
    now_str     = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    report_date = now.strftime("%Y-%m-%d")
    shift_time  = now.strftime("%H:%M UTC")

    # ── Key numbers ────────────────────────────────────────────────────────────
    total_cases       = (ir    or {}).get("total_cases",        0)
    confirmed_threats = (fp    or {}).get("confirmed_threats",  0)
    fp_count          = (fp    or {}).get("flagged_as_fp",       0)
    raw_fp_rate       = (fp    or {}).get("fp_rate", 0.0)
    fp_rate           = round(raw_fp_rate * 100 if raw_fp_rate <= 1.0 else raw_fp_rate, 1)
    total_ips         = (threats or {}).get("total_ips",         0)
    hstatus           = (stats  or {}).get("honeypot_status",  "UNKNOWN")
    unique_countries  = (stats  or {}).get("unique_countries",   0)
    high_sev          = (stats  or {}).get("high_severity",      0)
    med_sev           = (stats  or {}).get("medium_severity",    0)
    low_sev           = (stats  or {}).get("low_severity",       0)

    # Malware summary numbers
    malware_total  = (malware or {}).get("total_files",    0)
    malware_high   = (malware or {}).get("high_severity",  0)
    malware_medium = (malware or {}).get("medium_severity",0)
    malware_empty  = (malware or {}).get("empty_uploads",  0)

    # ── Case map: case_id → case dict ─────────────────────────────────────────
    case_map = {}
    if ir and ir.get("cases"):
        for c in ir["cases"]:
            case_map[c["case_id"]] = c

    # ── Confirmed cases (clean_cases from fp_filter) ──────────────────────────
    clean_case_refs = (fp or {}).get("clean_cases", [])
    confirmed_cases = []
    for cc in clean_case_refs:
        if isinstance(cc, str):
            full = case_map.get(cc, {})
            if not full:
                full = {"case_id": cc}
        else:
            case_id = cc.get("case_id", "?")
            full = case_map.get(case_id, cc)
        confirmed_cases.append(full)

    # ── Malware index ─────────────────────────────────────────────────────────
    malware_index = build_malware_index(malware)

    # ── Session grouping ──────────────────────────────────────────────────────
    priority_cases, grouped_cases = group_cases_for_report(confirmed_cases)
    log(f"Grouping: {len(priority_cases)} priority case(s), "
        f"{len(grouped_cases)} grouped entry/entries "
        f"from {len(confirmed_cases)} confirmed case(s)", "INFO", True)

    # ── Sort priority cases: CRITICAL first, then HIGH, MEDIUM, LOW ───────────
    sev_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    priority_cases.sort(
        key=lambda c: sev_order.get((c.get("severity") or "LOW").upper(), 3)
    )

    # ── Top IPs ───────────────────────────────────────────────────────────────
    top_ips = []
    if threats and threats.get("ips"):
        top_ips = sorted(
            [ip for ip in threats["ips"] if int(ip.get("abuse_score", 0)) > 0],
            key=lambda x: int(x.get("abuse_score", 0)),
            reverse=True
        )[:10]

    # ── Top TTPs ──────────────────────────────────────────────────────────────
    top_ttps = ((stats or {}).get("top_ttps") or [])[:5]

    # ── FP reason breakdown ───────────────────────────────────────────────────
    fp_reasons = {}
    for f in (fp or {}).get("fp_cases", []):
        reason = (f.get("reason") or "Unknown").split("—")[0].strip()
        fp_reasons[reason] = fp_reasons.get(reason, 0) + 1

    # ─────────────────────────────────────────────────────────────────────────
    # Build report lines
    # ─────────────────────────────────────────────────────────────────────────

    L = []

    def ln(s=""):
        L.append(s)

    # ── Header ────────────────────────────────────────────────────────────────
    ln("# 🛡 THIR · SOC Shift Handover Report")
    ln()
    ln("| Field | Value |")
    ln("|---|---|")
    ln(f"| **Report Date** | {report_date} |")
    ln(f"| **Generated At** | {now_str} |")
    ln(f"| **Shift Time** | {shift_time} |")
    ln(f"| **Honeypot Status** | {honeypot_icon(hstatus)} |")
    ln(f"| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |")
    ln()

    # ── Executive summary ─────────────────────────────────────────────────────
    ln("---")
    ln()
    ln("## 📊 Executive Summary")
    ln()
    ln("| Metric | Value |")
    ln("|---|---|")
    ln(f"| Total Sessions Captured | **{total_cases}** |")
    ln(f"| Confirmed Threats | **{confirmed_threats}** |")
    ln(f"| False Positives Filtered | **{fp_count}** ({fp_rate}%) |")
    ln(f"| Unique Attacker IPs | **{total_ips}** |")
    ln(f"| Countries of Origin | **{unique_countries}** |")
    ln(f"| High Severity Cases | **{high_sev}** |")
    ln(f"| Medium Severity Cases | **{med_sev}** |")
    ln(f"| Low Severity Cases | **{low_sev}** |")

    # Malware row (only if Tool 31 produced output)
    if malware_total > 0 or malware_empty > 0:
        malware_summary = (
            f"**{malware_high}** HIGH · **{malware_medium}** MED · "
            f"{malware_empty} empty upload attempt(s)"
        )
        ln(f"| Malware Samples Analyzed | {malware_summary} |")
    elif malware is None:
        ln(f"| Malware Analysis | ⚠️ malware_report.json not available (Tool 31 not run) |")
    ln()


    # ── 🔑 Credential Intelligence (Tool 34) ──────────────────────────────────
    if creds:
        total_attempts  = creds.get("total_attempts", 0)
        unique_pairs    = creds.get("unique_pairs", 0)
        top_usernames   = (creds.get("top_usernames")  or [])[:5]
        top_passwords   = (creds.get("top_passwords")  or [])[:5]
        top_pairs       = (creds.get("top_pairs")      or [])[:5]
        success_pairs   = creds.get("success_pairs",   [])

        ln("---")
        ln()
        ln("## 🔑 Credential Intelligence")
        ln()
        ln("| Metric | Value |")
        ln("|---|---|")
        ln(f"| Total Auth Attempts | **{total_attempts}** |")
        ln(f"| Unique Credential Pairs | **{unique_pairs}** |")
        ln(f"| Unique Usernames | **{creds.get('unique_usernames', 0)}** |")
        ln(f"| Unique Passwords | **{creds.get('unique_passwords', 0)}** |")
        ln(f"| Successful Auth Pairs | **{len(success_pairs)}** |")
        ln()

        if top_usernames:
            ln("**Top Usernames:**")
            ln()
            ln("| Username | Attempts |")
            ln("|---|---|")
            for u in top_usernames:
                ln(f"| `{u.get('username','?')}` | {u.get('count',0)} |")
            ln()

        if top_passwords:
            ln("**Top Passwords:**")
            ln()
            ln("| Password | Attempts |")
            ln("|---|---|")
            for p in top_passwords:
                ln(f"| `{p.get('password','?')}` | {p.get('count',0)} |")
            ln()

        if top_pairs:
            ln("**Top Credential Pairs:**")
            ln()
            ln("| Username | Password | Attempts |")
            ln("|---|---|---|")
            for pair in top_pairs:
                ln(f"| `{pair.get('username','?')}` | `{pair.get('password','?')}` | {pair.get('count',0)} |")
            ln()

        if success_pairs:
            ln("**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**")
            ln()
            ln("| Username | Password | Source IP | Timestamp |")
            ln("|---|---|---|---|")
            for sp in success_pairs:
                ln(f"| `{sp.get('username','?')}` | `{sp.get('password','?')}` | "
                   f"`{sp.get('src_ip','?')}` | {sp.get('timestamp','?')[:19]} |")
            ln()

    # ── 🖥 SSH Fingerprint Intelligence (Tool 35) ─────────────────────────────
    if ssh_fps and ssh_fps.get("unique_fingerprints", 0) > 0:
        fps_list      = (ssh_fps.get("fingerprints") or [])[:8]
        top_families  = (ssh_fps.get("top_families")  or [])[:5]
        botnet_sigs   = ssh_fps.get("botnet_signals",  [])

        ln("---")
        ln()
        ln("## 🖥 SSH Fingerprint Intelligence")
        ln()
        ln("| Metric | Value |")
        ln("|---|---|")
        ln(f"| Total Sessions Parsed | **{ssh_fps.get('total_sessions_parsed', 0)}** |")
        ln(f"| Sessions with Fingerprint | **{ssh_fps.get('sessions_with_fingerprint', 0)}** |")
        ln(f"| Unique HASSH Fingerprints | **{ssh_fps.get('unique_fingerprints', 0)}** |")
        ln()

        if top_families:
            ln("**Client Family Distribution:**")
            ln()
            ln("| Client Family | Sessions |")
            ln("|---|---|")
            for fam in top_families:
                ln(f"| {fam.get('family','?')} | {fam.get('sessions',0)} |")
            ln()

        if botnet_sigs:
            ln("**⚠️ Botnet/Scanner KEX Signatures Detected:**")
            ln()
            ln("| HASSH | Signature | Sessions | IPs |")
            ln("|---|---|---|---|")
            for sig in botnet_sigs[:5]:
                ips_count = len(sig.get("unique_ips", []))
                ln(f"| `{sig.get('hassh','?')[:12]}...` | {sig.get('signature','?')} | "
                   f"{sig.get('session_count',0)} | {ips_count} |")
            ln()

        if fps_list:
            ln("**Top Fingerprints:**")
            ln()
            ln("| HASSH | Client | Sessions | IPs | Botnet Sig |")
            ln("|---|---|---|---|---|")
            for fp in fps_list:
                ln(f"| `{fp.get('hassh','?')[:12]}...` | {fp.get('client_family','?')} | "
                   f"{fp.get('session_count',0)} | {fp.get('unique_ip_count',0)} | "
                   f"{fp.get('botnet_signature') or '—'} |")
            ln()

    # ── ⚔️ Attack Campaign Intelligence (Tool 36) ─────────────────────────────
    if cmd_cls and cmd_cls.get("campaign_clusters", 0) > 0:
        active_campaigns = cmd_cls.get("active_campaigns", [])
        all_clusters     = (cmd_cls.get("clusters") or [])

        ln("---")
        ln()
        ln("## ⚔️ Attack Campaign Intelligence")
        ln()
        ln("| Metric | Value |")
        ln("|---|---|")
        ln(f"| Total Command Clusters | **{cmd_cls.get('total_clusters', 0)}** |")
        ln(f"| Campaign Clusters | **{cmd_cls.get('campaign_clusters', 0)}** |")
        ln(f"| Highest Severity | **{cmd_cls.get('highest_severity', 'NONE')}** |")
        ln()

        if active_campaigns:
            ln("**Active Campaigns:**")
            ln()
            ln("| Campaign | Severity | Sessions | IPs | TTPs |")
            ln("|---|---|---|---|---|")
            for c in active_campaigns:
                ttps_str = ", ".join(c.get("ttps", [])[:4])
                ln(f"| **{c.get('name','?')}** | {severity_badge(c.get('severity','LOW'))} | "
                   f"{c.get('session_count',0)} | {c.get('unique_ip_count',0)} | `{ttps_str}` |")
            ln()

        # Campaign detail blocks
        campaign_clusters = [c for c in all_clusters if c.get("is_campaign")]
        for camp in campaign_clusters[:3]:
            sev = camp.get("campaign_severity", "LOW")
            ln(f"**{severity_badge(sev)} · {camp.get('campaign_name','Unknown Campaign')}**")
            ln()
            ln(f"> {camp.get('campaign_description','')}")
            ln()
            if camp.get("representative_commands"):
                ln("Representative commands:")
                for cmd in camp["representative_commands"][:5]:
                    ln(f"```")
                    ln(cmd)
                    ln(f"```")
            ips = camp.get("unique_ips", [])
            if ips:
                ln(f"Source IPs: {', '.join(f'`{ip}`' for ip in ips[:6])}")
            ln()

    # ── 🌐 ASN Cluster Intelligence (Tool 30b) ─────────────────────────────────
    if asn_cls and asn_cls.get("unique_asns", 0) > 0:
        top_asns      = (asn_cls.get("top_attack_asns") or [])[:8]
        high_risk_asns = asn_cls.get("high_risk_asns",  [])
        anon_infra    = asn_cls.get("anon_infrastructure", [])

        ln("---")
        ln()
        ln("## 🌐 ASN Cluster Intelligence")
        ln()
        ln("| Metric | Value |")
        ln("|---|---|")
        ln(f"| Total IPs Analysed | **{asn_cls.get('total_ips_analyzed', 0)}** |")
        ln(f"| Unique ASNs | **{asn_cls.get('unique_asns', 0)}** |")
        ln(f"| High-Risk ASNs | **{len(high_risk_asns)}** |")
        ln(f"| Anon Infrastructure ASNs | **{len(anon_infra)}** |")
        ln()

        if top_asns:
            ln("**Top Attack ASNs:**")
            ln()
            ln("| ASN | Provider | IPs | Risk |")
            ln("|---|---|---|---|")
            for a in top_asns:
                ln(f"| `{a.get('asn','?')}` | {a.get('asn_name','?')} | "
                   f"{a.get('ip_count',0)} | {a.get('risk_tier','?')} |")
            ln()

        if anon_infra:
            ln("**⚠️ Anonymous Infrastructure (Tor/VPN/Proxy):**")
            ln()
            ln("| ASN | Provider | IPs | Anon Count |")
            ln("|---|---|---|---|")
            for a in anon_infra[:5]:
                ln(f"| `{a.get('asn','?')}` | {a.get('asn_name','?')} | "
                   f"{a.get('ip_count',0)} | {a.get('anon_count',0)} |")
            ln()

    # ── 🦠 Malware Analysis (Tool 31 + Tool 33) ────────────────────────────────
    malware_found = malware and (malware.get("total_files", 0) > 0)
    yara_found    = yara    and (yara.get("files_classified", 0) > 0)

    if malware_found or yara_found:
        ln("---")
        ln()

    # ── Priority Cases ────────────────────────────────────────────────────────
    ln("---")
    ln()
    ln(f"## 🚨 Priority Cases — Immediate Attention ({len(priority_cases)})")
    ln()
    ln("> Cases with auth success, command execution, or file downloads.")
    ln("> Each requires individual review. Never grouped.")
    ln()

    if not priority_cases:
        ln("_No priority cases this shift. All confirmed sessions were credential scans only._")
        ln()
    else:
        for case in priority_cases:
            render_priority_case(case, malware_index, L)

    # ── Reconnaissance activity (grouped) ─────────────────────────────────────
    ln("---")
    ln()
    ln(f"## 📡 Reconnaissance Activity — Grouped by Source IP")
    ln()
    ln("> Repeated connect/close sessions with no auth success, commands, or downloads.")
    ln("> Grouped within a 120-minute window per IP to reduce noise.")
    ln()

    if not grouped_cases:
        ln("_No reconnaissance sessions this shift._")
        ln()
    else:
        # Count grouped vs singleton
        n_grouped   = sum(1 for g in grouped_cases if g["grouped"])
        n_singleton = sum(1 for g in grouped_cases if not g["grouped"])
        log(f"Recon table: {n_grouped} grouped entries + {n_singleton} singletons", "INFO", True)

        ln("| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |")
        ln("|---|---|---|---|---|---|---|---|")

        for g in grouped_cases:
            if g["grouped"]:
                duration_min = (g["total_duration_seconds"] or 0) // 60
                ttps_str     = " · ".join(g["ttps"][:3])
                sev_ico      = severity_icon(g["severity"])
                ip_defanged  = defang_ip(g["src_ip"])
                ln(
                    f"| `{ip_defanged}` | **{g['session_count']}** | "
                    f"{fmt_ts(g['first_seen'])} | {fmt_ts(g['last_seen'])} | "
                    f"{duration_min}m | {g['total_login_attempts']} | "
                    f"`{ttps_str}` | {sev_ico} {g['severity']} |"
                )
            else:
                # Singleton — render as a single-row summary
                c            = g["case"]
                ttps_str     = " · ".join((c.get("ttps") or ["T1592"])[:3])
                sev          = c.get("severity", "LOW")
                sev_ico      = severity_icon(sev)
                duration     = c.get("duration_seconds", 0)
                attempts     = c.get("login_attempts", 0)
                ip_defanged  = defang_ip(c.get("src_ip", "?"))
                ln(
                    f"| `{ip_defanged}` | 1 | "
                    f"{fmt_ts(c.get('first_seen'))} | {fmt_ts(c.get('last_seen'))} | "
                    f"{duration}s | {attempts} | "
                    f"`{ttps_str}` | {sev_ico} {sev} |"
                )
        ln()

    # ── Malware analysis results ───────────────────────────────────────────────
    if malware and malware_total > 0:
        ln("---")
        ln()
        ln(f"## 🦠 Malware Analysis Results ({malware_total} sample(s))")
        ln()
        ln("| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |")
        ln("|---|---|---|---|---|---|")
        for sample in malware.get("samples", []):
            sha_short = (sample.get("sha256") or "")[:16] + "..."
            vt        = sample.get("virustotal") or {}
            if vt.get("found") and vt.get("malicious", 0) > 0:
                vt_str = f"**{vt['malicious']}/{vt['total']}** 🔴"
            elif vt.get("found"):
                vt_str = f"0/{vt['total']} ✅"
            else:
                vt_str = "Not in VT"
            file_type = sample.get("file_type", "?")
            if sample.get("elf_arch"):
                file_type += f" ({sample['elf_arch']})"
            notes = sample.get("notes", "")
            if notes:
                file_type = "EMPTY — " + notes[:60] + "..." if len(notes) > 60 else f"EMPTY — {notes}"
            ln(
                f"| `{sample.get('file_name','?')}` | {file_type} | `{sha_short}` | "
                f"{sample.get('threat_score',0)}/100 | {severity_badge(sample.get('severity','LOW'))} | "
                f"{vt_str} |"
            )
        ln()

        # Full indicator details for HIGH/CRIT samples
        high_samples = [s for s in malware.get("samples", []) if s.get("severity") in ("HIGH", "CRITICAL")]
        if high_samples:
            ln("**Suspicious Indicators — HIGH Severity Samples:**")
            ln()
            for sample in high_samples:
                indicators = sample.get("suspicious_indicators", []) or []
                if indicators:
                    ln(f"_`{sample.get('file_name','?')}` ({sample.get('sha256','?')[:24]}...)_")
                    for ind in indicators:
                        # Defang match strings — these often contain IPs/URLs/commands
                        match_defanged = defang(ind.get('match', '')[:80])
                        ln(f"- `{ind.get('indicator','?')}` — `{match_defanged}`")
                    ln()

    elif malware_empty > 0:
        ln("---")
        ln()
        ln("## 🦠 Malware Analysis Results")
        ln()
        ln(f"> {malware_empty} empty upload attempt(s) recorded.")
        ln("> Attacker initiated file transfer but no payload was received.")
        ln("> Possible capability test or failed SCP/SFTP transfer.")
        ln()

    # ── Top attacker IPs ──────────────────────────────────────────────────────
    ln("---")
    ln()
    ln("## 🌐 Top Attacker IPs by Abuse Score")
    ln()
    if not top_ips:
        ln("_No enriched IPs with abuse scores available._")
        ln()
    else:
        ln("| IP | Country | ISP | Abuse Score | OTX Pulses |")
        ln("|---|---|---|---|---|")
        for ip in top_ips:
            ip_defanged = defang_ip(ip.get("indicator", "?"))
            ln(
                f"| `{ip_defanged}` | {ip.get('country','?')} | "
                f"{ip.get('isp','?')} | {score_badge(ip.get('abuse_score',0))} | "
                f"{ip.get('otx_pulses',0)} |"
            )
        ln()

    # ── Top TTPs ──────────────────────────────────────────────────────────────
    if top_ttps:
        ln("---")
        ln()
        ln("## 🎯 Top TTPs Observed (MITRE ATT&CK)")
        ln()
        ln("| TTP ID | Count |")
        ln("|---|---|")
        for t in top_ttps:
            if isinstance(t, dict):
                ttp_id = t.get("ttp", "?")
                count  = t.get("count", "—")
            else:
                ttp_id = str(t)
                count  = "—"
            ttp_link = f"https://attack.mitre.org/techniques/{ttp_id.replace('.', '/')}"
            ln(f"| [{ttp_id}]({ttp_link}) | {count} |")
        ln()

    # ── FP summary ────────────────────────────────────────────────────────────
    ln("---")
    ln()
    ln(f"## 🔕 False Positive Summary ({fp_count} filtered)")
    ln()
    if fp_reasons:
        ln("| Reason | Count |")
        ln("|---|---|")
        for reason, count in sorted(fp_reasons.items()):
            ln(f"| {reason} | {count} |")
        ln()
    ln("> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.")
    ln()

    # ── Pipeline health ───────────────────────────────────────────────────────
    ln("---")
    ln()
    ln("## ⚙️ Pipeline Health")
    ln()
    ln("| Tool | Role | Status |")
    ln("|---|---|---|")
    ln(f"| Tool 05  | Network Monitor (port 2222) | {'✅' if hstatus == 'HEALTHY' else '❌'} {hstatus} |")
    ln(f"| Tool 26  | Incident Timeline Generator | {'✅' if total_cases > 0 else '⚠️'} {total_cases} cases |")
    ln(f"| Tool 34  | Credential Extractor        | {'✅' if creds else '⚠️ skipped'} {'%d attempts' % (creds or {}).get('total_attempts',0) if creds else ''} |")
    ln(f"| Tool 35  | SSH Fingerprint Aggregator  | {'✅' if ssh_fps else '⚠️ skipped'} {'%d fingerprints' % (ssh_fps or {}).get('unique_fingerprints',0) if ssh_fps else ''} |")
    ln(f"| Tool 36  | Command Clustering          | {'✅' if cmd_cls else '⚠️ skipped'} {'%d clusters' % (cmd_cls or {}).get('total_clusters',0) if cmd_cls else ''} |")
    ln(f"| Tool 27  | Threat Intel Feeder         | {'✅' if total_ips > 0 else '⚠️'} {total_ips} IPs enriched |")
    ln(f"| Tool 29  | False Positive Tracker      | ✅ {fp_count} filtered ({fp_rate}%) |")
    ln(f"| Tool 30  | Metric Exporter             | {'✅ stats.json written' if stats else '❌ no output'} |")
    ln(f"| Tool 30b | ASN Clustering              | {'✅' if asn_cls else '⚠️ skipped'} {'%d ASNs' % (asn_cls or {}).get('unique_asns',0) if asn_cls else ''} |")
    ln(f"| Tool 31  | Malware Analyzer            | {'✅' if malware_found else '— no downloads'} {'%d files' % (malware or {}).get('total_files',0) if malware_found else ''} |")
    ln(f"| Tool 33  | YARA Classifier             | {'✅' if yara_found else '— no downloads'} {'%d classified' % (yara or {}).get('files_classified',0) if yara_found else ''} |")
    ln(f"| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |")
    ln()

    # ── Grouping summary (for transparency) ───────────────────────────────────
    n_priority   = len(priority_cases)
    n_recon_rows = len(grouped_cases)
    n_grouped    = sum(1 for g in grouped_cases if g["grouped"])
    total_merged = sum(g.get("session_count", 1) for g in grouped_cases if g["grouped"])
    ln("> **Report grouping:** "
       f"{n_priority} priority case(s) shown individually · "
       f"{n_recon_rows} recon entry/entries in table "
       f"({n_grouped} group(s) consolidating {total_merged} session(s)).")
    ln()

    # ── Standing orders for next shift ────────────────────────────────────────
    ln("---")
    ln()
    ln("## 📋 Standing Orders for Next Shift")
    ln()
    ln("- [ ] Verify honeypot is HEALTHY (Tool 05 green)")
    ln("- [ ] Review any new HIGH/CRITICAL priority cases above")
    ln("- [ ] Check AbuseIPDB for newly reported IPs from this shift")
    ln("- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section")
    ln("- [ ] Integrity baseline auto-recreates every 2 hours via pipeline")
    ln()

    # ── Footer ────────────────────────────────────────────────────────────────
    ln("---")
    ln()
    ln("_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  ")
    ln("_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  ")
    ln(f"_Report time: {now_str}_")
    ln()

    return "\n".join(L)


# ─────────────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tool 28 v2.3 — THIR SOC Handover Report Generator"
    )
    parser.add_argument("--ir-cases",       default="data/ir_cases.json")
    parser.add_argument("--threat-ips",     default="data/threat_ips.json")
    parser.add_argument("--fp-filter",      default="data/fp_filter.json")
    parser.add_argument("--stats",          default="data/stats.json")
    parser.add_argument("--malware-report", default="data/malware_report.json",
                        help="Output from Tool 31 (malware analyzer)")
    parser.add_argument("--output",         default="data/soc_handover.md")
    parser.add_argument("--verbose", "-v",  action="store_true")
    # Phase 2 flags — all optional, missing file = section silently omitted
    parser.add_argument("--credentials",       default="data/credentials.json")
    parser.add_argument("--ssh-fingerprints",  default="data/ssh_fingerprints.json")
    parser.add_argument("--command-clusters",  default="data/command_clusters.json")
    parser.add_argument("--asn-clusters",      default="data/asn_clusters.json")
    parser.add_argument("--yara-matches",      default="data/yara_matches.json")
    args = parser.parse_args()

    log("Tool 28 v2.3 — SOC Handover Report Generator started", "INFO", True)

    ir      = load_json(args.ir_cases,       "ir_cases.json",       args.verbose)
    threats = load_json(args.threat_ips,     "threat_ips.json",     args.verbose)
    fp      = load_json(args.fp_filter,      "fp_filter.json",      args.verbose)
    stats   = load_json(args.stats,          "stats.json",          args.verbose)
    malware = load_json(args.malware_report, "malware_report.json", args.verbose)
    creds   = load_json(args.credentials,       "credentials.json",      args.verbose)
    ssh_fps = load_json(args.ssh_fingerprints,  "ssh_fingerprints.json", args.verbose)
    cmd_cls = load_json(args.command_clusters,  "command_clusters.json", args.verbose)
    asn_cls = load_json(args.asn_clusters,      "asn_clusters.json",     args.verbose)
    yara    = load_json(args.yara_matches,      "yara_matches.json",     args.verbose)

    report = build_report(ir, threats, fp, stats, malware, creds, ssh_fps, cmd_cls, asn_cls, yara)

    out_dir = os.path.dirname(args.output)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    try:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        log(f"SOC handover report written to {args.output}", "INFO", True)
    except OSError as e:
        log(f"Failed to write report: {e}", "ERROR", True)
        sys.exit(1)

    log("Tool 28 v2.3 — SOC Handover Report Generator completed successfully", "INFO", True)


if __name__ == "__main__":
    main()
