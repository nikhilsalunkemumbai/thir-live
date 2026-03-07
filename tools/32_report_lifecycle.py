#!/usr/bin/env python3
"""
Tool 32 — THIR Report Lifecycle Manager

Handles the full tiered retention lifecycle for SOC reports:

  DAILY   → Written every pipeline run to reports/daily/
              Format: reports/daily/soc_YYYY-MM-DD.md
              Retention: 5–7 files (one per day, overwritten same-day)

  WEEKLY  → Triggered on Monday via pipeline.yml (--rollup weekly)
              Reads all reports/daily/*.md from the past week
              Writes reports/weekly/soc_week_YYYY-WNN.md
              Deletes the daily files that were rolled up
              Retention: 3–4 files (one per week)

  MONTHLY → Triggered on 1st of month via pipeline.yml (--rollup monthly)
              Reads all reports/weekly/soc_week_*.md from the past month
              Writes reports/monthly/soc_YYYY-MM.md
              Deletes the weekly files that were rolled up
              Retention: up to 12 files per year (capped at 6 months for THIR)

OPTION 3 — Peak Stats:
  Every run (--save-daily) also reads stats.json and updates it with
  high-water marks: peak_sessions, peak_date, peak_unique_ips, peak_ip_date.
  These are NEVER overwritten by a quieter day — only updated if today beats
  the current peak.

Usage:
    # Every hourly pipeline run:
    python tools/32_report_lifecycle.py --save-daily \\
        --report data/soc_handover.md \\
        --stats  data/stats.json \\
        --date   2026-03-07

    # Monday 00:05 UTC — weekly rollup:
    python tools/32_report_lifecycle.py --rollup weekly \\
        --stats data/stats.json

    # 1st of month 00:10 UTC — monthly rollup:
    python tools/32_report_lifecycle.py --rollup monthly \\
        --stats data/stats.json

No external dependencies — stdlib only.
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone, timedelta


# ─────────────────────────────────────────────────────────────────────────────
# Logging
# ─────────────────────────────────────────────────────────────────────────────

def log(msg, level="INFO", verbose=False):
    if level == "INFO" and not verbose:
        return
    prefix = {"INFO": "[INFO]", "WARN": "[WARN]", "ERROR": "[ERROR]"}.get(level, "[INFO]")
    sys.stderr.write(f"{prefix} {msg}\n")
    sys.stderr.flush()


# ─────────────────────────────────────────────────────────────────────────────
# Directory helpers
# ─────────────────────────────────────────────────────────────────────────────

REPORTS_DAILY   = "reports/daily"
REPORTS_WEEKLY  = "reports/weekly"
REPORTS_MONTHLY = "reports/monthly"

def ensure_dirs():
    for d in [REPORTS_DAILY, REPORTS_WEEKLY, REPORTS_MONTHLY]:
        os.makedirs(d, exist_ok=True)


# ─────────────────────────────────────────────────────────────────────────────
# Option 3 — Peak stats update
# ─────────────────────────────────────────────────────────────────────────────

def update_peak_stats(stats_path, verbose=False):
    """
    Reads stats.json, compares today's session/IP counts against stored
    peak high-water marks. Updates only if today beats the current peak.
    Writes back to stats.json.
    """
    if not os.path.exists(stats_path):
        log(f"stats.json not found at {stats_path} — skipping peak update", "WARN", True)
        return

    try:
        with open(stats_path, encoding="utf-8") as f:
            stats = json.load(f)
    except Exception as e:
        log(f"Failed to read stats.json: {e}", "ERROR", True)
        return

    today     = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    changed   = False

    # Peak sessions
    today_sessions = int(stats.get("total_attacks", 0))
    peak_sessions  = int(stats.get("peak_sessions", 0))
    if today_sessions > peak_sessions:
        log(f"New peak sessions: {today_sessions} (was {peak_sessions} on {stats.get('peak_date','never')})", "INFO", True)
        stats["peak_sessions"] = today_sessions
        stats["peak_date"]     = today
        changed = True

    # Peak unique IPs
    today_ips  = int(stats.get("unique_ips", 0))
    peak_ips   = int(stats.get("peak_unique_ips", 0))
    if today_ips > peak_ips:
        log(f"New peak unique IPs: {today_ips} (was {peak_ips} on {stats.get('peak_ip_date','never')})", "INFO", True)
        stats["peak_unique_ips"] = today_ips
        stats["peak_ip_date"]    = today
        changed = True

    # Peak confirmed threats
    today_threats = int(stats.get("confirmed_threats", 0))
    peak_threats  = int(stats.get("peak_confirmed_threats", 0))
    if today_threats > peak_threats:
        log(f"New peak confirmed threats: {today_threats}", "INFO", True)
        stats["peak_confirmed_threats"] = today_threats
        stats["peak_threats_date"]      = today
        changed = True

    if changed:
        try:
            with open(stats_path, "w", encoding="utf-8") as f:
                json.dump(stats, f, indent=2)
            log(f"Peak stats updated in {stats_path}", "INFO", verbose)
        except Exception as e:
            log(f"Failed to write stats.json: {e}", "ERROR", True)
    else:
        log("No new peaks today — stats.json unchanged", "INFO", verbose)


# ─────────────────────────────────────────────────────────────────────────────
# Daily save
# ─────────────────────────────────────────────────────────────────────────────

def save_daily(report_path, date_str, verbose=False):
    """
    Copies today's soc_handover.md into reports/daily/soc_YYYY-MM-DD.md.
    If same-day file already exists it is overwritten (latest run wins).
    """
    if not os.path.exists(report_path):
        log(f"Report not found at {report_path} — skipping daily save", "WARN", True)
        return

    dest = os.path.join(REPORTS_DAILY, f"soc_{date_str}.md")
    shutil.copy2(report_path, dest)
    log(f"Daily report saved → {dest}", "INFO", verbose)


# ─────────────────────────────────────────────────────────────────────────────
# Extract key metrics from a daily Markdown report
# ─────────────────────────────────────────────────────────────────────────────

def _extract_metric(text, label):
    """Pull a bold number from a Markdown table row like '| Total Sessions | **40** |'"""
    pattern = rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|\s*\*\*(\d+)\*\*"
    m = re.search(pattern, text)
    if m:
        return int(m.group(1))
    # fallback: label not bold
    pattern2 = rf"\|\s*{re.escape(label)}\s*\|\s*\*\*(\d+)\*\*"
    m2 = re.search(pattern2, text)
    return int(m2.group(1)) if m2 else 0


def parse_daily_report(path):
    """Return a dict of key metrics extracted from a daily .md report."""
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except Exception:
        return {}

    date_m = re.search(r"soc_(\d{4}-\d{2}-\d{2})\.md", path)
    date_s = date_m.group(1) if date_m else "unknown"

    return {
        "date":               date_s,
        "total_sessions":     _extract_metric(text, "Total Sessions Captured"),
        "confirmed_threats":  _extract_metric(text, "Confirmed Threats"),
        "false_positives":    _extract_metric(text, "False Positives Filtered"),
        "unique_ips":         _extract_metric(text, "Unique Attacker IPs"),
        "countries":          _extract_metric(text, "Countries of Origin"),
        "high_sev":           _extract_metric(text, "High Severity Cases"),
        "medium_sev":         _extract_metric(text, "Medium Severity Cases"),
        "low_sev":            _extract_metric(text, "Low Severity Cases"),
    }


# ─────────────────────────────────────────────────────────────────────────────
# Weekly rollup
# ─────────────────────────────────────────────────────────────────────────────

def rollup_weekly(verbose=False):
    """
    Runs on Monday. Reads all daily reports from the past 7 days,
    produces a weekly summary Markdown, deletes the rolled-up daily files.
    """
    today     = datetime.now(timezone.utc).date()
    week_ago  = today - timedelta(days=7)

    # ISO week of the PREVIOUS week (we're rolling up Mon→Sun just ended)
    prev_monday = today - timedelta(days=7)
    year, week, _ = prev_monday.isocalendar()
    week_label = f"{year}-W{week:02d}"

    dest = os.path.join(REPORTS_WEEKLY, f"soc_week_{week_label}.md")

    if os.path.exists(dest):
        log(f"Weekly report {dest} already exists — skipping", "WARN", True)
        return

    # Collect daily files from the past 7 days
    daily_files = []
    for fname in sorted(os.listdir(REPORTS_DAILY)):
        m = re.match(r"soc_(\d{4}-\d{2}-\d{2})\.md$", fname)
        if not m:
            continue
        try:
            fdate = datetime.strptime(m.group(1), "%Y-%m-%d").date()
        except ValueError:
            continue
        if week_ago <= fdate < today:
            daily_files.append(os.path.join(REPORTS_DAILY, fname))

    if not daily_files:
        log("No daily reports found for weekly rollup — nothing to do", "WARN", True)
        return

    log(f"Rolling up {len(daily_files)} daily reports → {dest}", "INFO", verbose)

    # Parse each daily report
    days = [parse_daily_report(f) for f in daily_files]
    days = [d for d in days if d]

    # Aggregate
    total_sessions    = sum(d["total_sessions"]    for d in days)
    total_threats     = sum(d["confirmed_threats"] for d in days)
    total_fps         = sum(d["false_positives"]   for d in days)
    total_ips         = sum(d["unique_ips"]        for d in days)
    peak_day          = max(days, key=lambda d: d["total_sessions"]) if days else {}
    peak_sessions     = peak_day.get("total_sessions", 0)
    peak_date         = peak_day.get("date", "—")
    high_total        = sum(d["high_sev"]   for d in days)
    med_total         = sum(d["medium_sev"] for d in days)
    low_total         = sum(d["low_sev"]    for d in days)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    def ln(s=""): lines.append(s)

    ln(f"# 🛡 THIR · SOC Weekly Summary — {week_label}")
    ln()
    ln("| Field | Value |")
    ln("|---|---|")
    ln(f"| **Week** | {week_label} ({prev_monday} → {today - timedelta(days=1)}) |")
    ln(f"| **Generated At** | {now_str} |")
    ln(f"| **Days Covered** | {len(days)} |")
    ln(f"| **Source** | Rolled up from {len(daily_files)} daily SOC reports |")
    ln()
    ln("---")
    ln()
    ln("## 📊 Weekly Aggregate Metrics")
    ln()
    ln("| Metric | Total |")
    ln("|---|---|")
    ln(f"| Total Sessions Captured | **{total_sessions}** |")
    ln(f"| Confirmed Threats | **{total_threats}** |")
    ln(f"| False Positives Filtered | **{total_fps}** |")
    ln(f"| Unique Attacker IPs (cumulative) | **{total_ips}** |")
    ln(f"| High Severity Cases | **{high_total}** |")
    ln(f"| Medium Severity Cases | **{med_total}** |")
    ln(f"| Low Severity Cases | **{low_total}** |")
    ln(f"| Peak Activity Day | **{peak_date}** ({peak_sessions} sessions) |")
    ln()
    ln("---")
    ln()
    ln("## 📅 Daily Breakdown")
    ln()
    ln("| Date | Sessions | Threats | FPs | High | Med | Low |")
    ln("|---|---|---|---|---|---|---|")
    for d in sorted(days, key=lambda x: x["date"]):
        ln(f"| {d['date']} | {d['total_sessions']} | {d['confirmed_threats']} | "
           f"{d['false_positives']} | {d['high_sev']} | {d['medium_sev']} | {d['low_sev']} |")
    ln()
    ln("---")
    ln()
    ln("## 📋 Analyst Notes")
    ln()
    ln("> _Add shift notes, escalations, or notable incidents here before archiving._")
    ln()
    ln("---")
    ln()
    ln(f"_Generated by THIR · Tool 32 · Report Lifecycle Manager_  ")
    ln(f"_Rolled up from {len(daily_files)} daily reports · Week {week_label}_  ")
    ln(f"_Generated: {now_str}_")
    ln()

    try:
        with open(dest, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        log(f"Weekly report written → {dest}", "INFO", verbose)
    except Exception as e:
        log(f"Failed to write weekly report: {e}", "ERROR", True)
        return

    # Delete rolled-up daily files
    for fpath in daily_files:
        try:
            os.remove(fpath)
            log(f"Deleted daily report: {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not delete {fpath}: {e}", "WARN", True)

    log(f"Weekly rollup complete — {len(daily_files)} daily reports → {dest}", "INFO", True)


# ─────────────────────────────────────────────────────────────────────────────
# Monthly rollup
# ─────────────────────────────────────────────────────────────────────────────

def rollup_monthly(verbose=False):
    """
    Runs on 1st of month. Reads all weekly reports from the previous month,
    produces a monthly summary Markdown, deletes the rolled-up weekly files.
    Monthly reports are retained up to 6 months then the oldest is pruned.
    """
    today       = datetime.now(timezone.utc).date()
    # Previous month
    first_this  = today.replace(day=1)
    last_month  = first_this - timedelta(days=1)
    month_label = last_month.strftime("%Y-%m")
    month_start = last_month.replace(day=1)

    dest = os.path.join(REPORTS_MONTHLY, f"soc_{month_label}.md")

    if os.path.exists(dest):
        log(f"Monthly report {dest} already exists — skipping", "WARN", True)
        return

    # Collect weekly files that fall within the previous month
    weekly_files = []
    for fname in sorted(os.listdir(REPORTS_WEEKLY)):
        m = re.match(r"soc_week_(\d{4})-W(\d{2})\.md$", fname)
        if not m:
            continue
        year_w, week_n = int(m.group(1)), int(m.group(2))
        try:
            # Get the Monday of that ISO week
            week_monday = datetime.fromisocalendar(year_w, week_n, 1).date()
        except Exception:
            continue
        # Include if the week's Monday falls inside the previous month
        if month_start <= week_monday < first_this:
            weekly_files.append(os.path.join(REPORTS_WEEKLY, fname))

    if not weekly_files:
        log("No weekly reports found for monthly rollup — nothing to do", "WARN", True)
        return

    log(f"Rolling up {len(weekly_files)} weekly reports → {dest}", "INFO", verbose)

    # Parse each weekly report — reuse parse_daily_report (same table format)
    weeks = [parse_daily_report(f) for f in weekly_files]
    weeks_data = []
    for fpath, parsed in zip(weekly_files, weeks):
        # Weekly files have week label in filename, not date — patch it
        wm = re.search(r"soc_week_(\d{4}-W\d{2})\.md$", fpath)
        parsed["date"] = wm.group(1) if wm else parsed.get("date", "?")
        if parsed:
            weeks_data.append(parsed)

    total_sessions   = sum(d["total_sessions"]    for d in weeks_data)
    total_threats    = sum(d["confirmed_threats"] for d in weeks_data)
    total_fps        = sum(d["false_positives"]   for d in weeks_data)
    total_ips        = sum(d["unique_ips"]        for d in weeks_data)
    high_total       = sum(d["high_sev"]          for d in weeks_data)
    med_total        = sum(d["medium_sev"]        for d in weeks_data)
    low_total        = sum(d["low_sev"]           for d in weeks_data)
    peak_week        = max(weeks_data, key=lambda d: d["total_sessions"]) if weeks_data else {}
    peak_sessions    = peak_week.get("total_sessions", 0)
    peak_week_label  = peak_week.get("date", "—")

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    lines = []
    def ln(s=""): lines.append(s)

    ln(f"# 🛡 THIR · SOC Monthly Summary — {month_label}")
    ln()
    ln("| Field | Value |")
    ln("|---|---|")
    ln(f"| **Month** | {month_label} ({month_start} → {last_month}) |")
    ln(f"| **Generated At** | {now_str} |")
    ln(f"| **Weeks Covered** | {len(weeks_data)} |")
    ln(f"| **Source** | Rolled up from {len(weekly_files)} weekly SOC reports |")
    ln()
    ln("---")
    ln()
    ln("## 📊 Monthly Aggregate Metrics")
    ln()
    ln("| Metric | Total |")
    ln("|---|---|")
    ln(f"| Total Sessions Captured | **{total_sessions}** |")
    ln(f"| Confirmed Threats | **{total_threats}** |")
    ln(f"| False Positives Filtered | **{total_fps}** |")
    ln(f"| Unique Attacker IPs (cumulative) | **{total_ips}** |")
    ln(f"| High Severity Cases | **{high_total}** |")
    ln(f"| Medium Severity Cases | **{med_total}** |")
    ln(f"| Low Severity Cases | **{low_total}** |")
    ln(f"| Peak Activity Week | **{peak_week_label}** ({peak_sessions} sessions) |")
    ln()
    ln("---")
    ln()
    ln("## 📅 Weekly Breakdown")
    ln()
    ln("| Week | Sessions | Threats | FPs | High | Med | Low |")
    ln("|---|---|---|---|---|---|---|")
    for d in weeks_data:
        ln(f"| {d['date']} | {d['total_sessions']} | {d['confirmed_threats']} | "
           f"{d['false_positives']} | {d['high_sev']} | {d['medium_sev']} | {d['low_sev']} |")
    ln()
    ln("---")
    ln()
    ln("## 📋 Monthly Analyst Notes")
    ln()
    ln("> _Trends, escalations, notable threat actor patterns, or infrastructure changes this month._")
    ln()
    ln("---")
    ln()
    ln(f"_Generated by THIR · Tool 32 · Report Lifecycle Manager_  ")
    ln(f"_Rolled up from {len(weekly_files)} weekly reports · Month {month_label}_  ")
    ln(f"_Generated: {now_str}_")
    ln()

    try:
        with open(dest, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        log(f"Monthly report written → {dest}", "INFO", verbose)
    except Exception as e:
        log(f"Failed to write monthly report: {e}", "ERROR", True)
        return

    # Delete rolled-up weekly files
    for fpath in weekly_files:
        try:
            os.remove(fpath)
            log(f"Deleted weekly report: {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not delete {fpath}: {e}", "WARN", True)

    # Prune monthly reports older than 6 months (THIR lifecycle limit)
    _prune_old_monthlies(verbose=verbose)

    log(f"Monthly rollup complete — {len(weekly_files)} weekly reports → {dest}", "INFO", True)


def _prune_old_monthlies(keep=6, verbose=False):
    """Delete monthly reports beyond the 6-month retention window."""
    monthly_files = sorted([
        f for f in os.listdir(REPORTS_MONTHLY)
        if re.match(r"soc_\d{4}-\d{2}\.md$", f)
    ])
    if len(monthly_files) <= keep:
        return
    to_delete = monthly_files[:len(monthly_files) - keep]
    for fname in to_delete:
        fpath = os.path.join(REPORTS_MONTHLY, fname)
        try:
            os.remove(fpath)
            log(f"Pruned old monthly report (>6 months): {fpath}", "INFO", verbose)
        except Exception as e:
            log(f"Could not prune {fpath}: {e}", "WARN", True)


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tool 32 — THIR Report Lifecycle Manager"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--save-daily",
        action="store_true",
        help="Copy today's report to reports/daily/ and update peak stats"
    )
    group.add_argument(
        "--rollup",
        choices=["weekly", "monthly"],
        help="Trigger weekly or monthly rollup and cleanup"
    )

    parser.add_argument("--report",  default="data/soc_handover.md",
                        help="Path to today's SOC handover report (used with --save-daily)")
    parser.add_argument("--stats",   default="data/stats.json",
                        help="Path to stats.json for peak stats update")
    parser.add_argument("--date",    default=None,
                        help="Override date for daily save (YYYY-MM-DD). Defaults to today UTC.")
    parser.add_argument("--verbose", "-v", action="store_true")

    args = parser.parse_args()

    ensure_dirs()

    if args.save_daily:
        date_str = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
        log(f"Mode: save-daily for {date_str}", "INFO", True)
        update_peak_stats(args.stats, verbose=args.verbose)
        save_daily(args.report, date_str, verbose=args.verbose)

    elif args.rollup == "weekly":
        log("Mode: weekly rollup", "INFO", True)
        rollup_weekly(verbose=args.verbose)

    elif args.rollup == "monthly":
        log("Mode: monthly rollup", "INFO", True)
        rollup_monthly(verbose=args.verbose)

    log("Tool 32 completed", "INFO", True)


if __name__ == "__main__":
    main()
