#!/usr/bin/env python3
"""
Tool 28 — SOC Handover Report Generator (THIR Live)

Reads live pipeline outputs and generates a structured Markdown
SOC shift handover report. No external dependencies — stdlib only.

Usage:
    python tools/28_soc_handover_live.py \\
        --ir-cases   data/ir_cases.json \\
        --threat-ips data/threat_ips.json \\
        --fp-filter  data/fp_filter.json \\
        --stats      data/stats.json \\
        --output     data/soc_handover.md \\
        --verbose
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone


# ── Logging ───────────────────────────────────────────────────────────────────

def log(msg, level="INFO", verbose=False):
    if level == "INFO" and not verbose:
        return
    sys.stderr.write(f"[{level}] {msg}\n")
    sys.stderr.flush()


# ── Safe JSON loader ──────────────────────────────────────────────────────────

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


# ── Helpers ───────────────────────────────────────────────────────────────────

def severity_badge(sev):
    return {
        "CRITICAL": "🚨 CRITICAL",
        "HIGH":     "🔴 HIGH",
        "MEDIUM":   "🟡 MEDIUM",
        "LOW":      "🟢 LOW",
    }.get((sev or "LOW").upper(), "🟢 LOW")


def score_badge(score):
    s = int(score or 0)
    if s >= 80: return f"**{s}** ⚠️"
    if s >= 25: return f"**{s}**"
    return str(s)


def honeypot_icon(status):
    return {
        "HEALTHY": "✅ HEALTHY",
        "UP":      "✅ UP",
        "DOWN":    "❌ DOWN",
        "DEGRADED":"⚠️ DEGRADED",
    }.get((status or "UNKNOWN").upper(), f"❓ {status}")


# ── Report builder ────────────────────────────────────────────────────────────

def build_report(ir, threats, fp, stats):
    now         = datetime.now(timezone.utc)
    now_str     = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    report_date = now.strftime("%Y-%m-%d")
    shift_time  = now.strftime("%H:%M UTC")

    # Key numbers
    total_cases       = (ir    or {}).get("total_cases",        0)
    confirmed_threats = (fp    or {}).get("confirmed_threats",  0)
    fp_count          = (fp    or {}).get("flagged_as_fp",       0)
    raw_fp_rate       = (fp or {}).get("fp_rate", 0.0)
    # fp_rate is stored as a fraction (0.925) not a percentage — convert
    fp_rate           = round(raw_fp_rate * 100 if raw_fp_rate <= 1.0 else raw_fp_rate, 1)
    total_ips         = (threats or {}).get("total_ips",         0)
    hstatus           = (stats  or {}).get("honeypot_status",  "UNKNOWN")
    unique_countries  = (stats  or {}).get("unique_countries",   0)
    high_sev          = (stats  or {}).get("high_severity",      0)
    med_sev           = (stats  or {}).get("medium_severity",    0)
    low_sev           = (stats  or {}).get("low_severity",       0)

    # Case lookup map
    case_map = {}
    if ir and ir.get("cases"):
        for c in ir["cases"]:
            case_map[c["case_id"]] = c

    # Confirmed cases
    clean_cases = (fp or {}).get("clean_cases", [])

    # Top IPs by abuse score
    top_ips = []
    if threats and threats.get("ips"):
        top_ips = sorted(
            [ip for ip in threats["ips"] if int(ip.get("abuse_score", 0)) > 0],
            key=lambda x: int(x.get("abuse_score", 0)),
            reverse=True
        )[:10]

    # Top TTPs
    top_ttps = ((stats or {}).get("top_ttps") or [])[:5]

    # FP reason breakdown
    fp_reasons = {}
    for f in (fp or {}).get("fp_cases", []):
        reason = (f.get("reason") or "Unknown").split("—")[0].strip()
        fp_reasons[reason] = fp_reasons.get(reason, 0) + 1

    # ── Build lines ───────────────────────────────────────────────────────────

    L = []

    def ln(s=""):
        L.append(s)

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

    # Executive summary
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
    ln()

    # Confirmed threats
    ln("---")
    ln()
    ln(f"## 🚨 Confirmed Threats ({confirmed_threats})")
    ln()

    if not clean_cases:
        ln("_No confirmed threats this shift. All sessions filtered as false positives._")
        ln()
    else:
        for cc in clean_cases:
            # clean_cases can be plain strings (case_ids) or dicts
            if isinstance(cc, str):
                case_id = cc
                full    = case_map.get(case_id, {})
                src_ip  = full.get("src_ip",   "?")
                sev     = full.get("severity", "LOW")
            else:
                case_id = cc.get("case_id", "?")
                src_ip  = cc.get("src_ip",  "?")
                sev     = cc.get("severity","LOW")
                full    = case_map.get(case_id, {})

            login_success = full.get("login_success", False)
            attempts      = full.get("login_attempts", "?")
            commands      = full.get("commands",  []) or []
            downloads     = full.get("downloads", []) or []
            ttps          = full.get("ttps",      []) or []
            first_seen    = full.get("first_seen", "unknown")
            last_seen     = full.get("last_seen",  "unknown")
            duration      = full.get("duration_seconds", 0)
            timeline      = full.get("timeline",  []) or []

            # Detect special event types in timeline
            tl_events     = [e.get("event","") for e in timeline]
            has_tcpip     = any("direct-tcpip" in e for e in tl_events)
            has_kex       = any("client.kex" in e for e in tl_events)

            ln(f"### {severity_badge(sev)} · {case_id}")
            ln()
            ln("| Field | Detail |")
            ln("|---|---|")
            ln(f"| **Source IP** | `{src_ip}` |")
            ln(f"| **First Seen** | {first_seen} |")
            ln(f"| **Last Seen** | {last_seen} |")
            ln(f"| **Session Duration** | {duration}s |")
            ln(f"| **Login Attempts** | {attempts} |")
            ln(f"| **Auth Success** | {'✅ Yes — session established' if login_success else '❌ No'} |")

            if has_tcpip:
                ln(f"| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt detected |")
            if commands:
                ln(f"| **Commands Executed** | `{', '.join(commands[:5])}` |")
            if downloads:
                ln(f"| **Download Attempts** | {', '.join(downloads[:3])} |")
            if ttps:
                ln(f"| **TTPs (MITRE)** | {' · '.join(ttps)} |")
            ln()

            # Timeline
            if timeline:
                ln("**Attack Timeline:**")
                ln()
                ln("| Time (UTC) | Event |")
                ln("|---|---|")
                for e in timeline:
                    ts  = e.get("timestamp", "?")[:19].replace("T", " ")
                    evt = e.get("event", "?")
                    ln(f"| `{ts}` | `{evt}` |")
                ln()

            ln("**Recommended Actions:**")
            if sev in ("HIGH", "CRITICAL"):
                ln(f"- [ ] Submit `{src_ip}` to AbuseIPDB if not already reported")
                ln(f"- [ ] Block `{src_ip}` at perimeter firewall / security group")
                if has_tcpip:
                    ln(f"- [ ] Investigate TCP tunnel target — attacker attempted port forwarding via honeypot")
                    ln(f"- [ ] Check if target host/port in tunnel data is internal infrastructure")
                if commands:
                    ln(f"- [ ] Review commands for lateral movement indicators")
                if downloads:
                    ln(f"- [ ] Submit download hashes to VirusTotal")
                    ln(f"- [ ] Run Tool 31 malware analyzer on captured payload")
                ln(f"- [ ] Escalate to Tier 2 if pattern repeats next shift")
            else:
                ln(f"- [ ] Monitor for repeat activity from `{src_ip}`")
                ln(f"- [ ] No immediate escalation required")
            ln()

    # Top attacker IPs
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
            ln(f"| `{ip.get('indicator','?')}` | {ip.get('country','?')} | "
               f"{ip.get('isp','?')} | {score_badge(ip.get('abuse_score',0))} | "
               f"{ip.get('otx_pulses',0)} |")
        ln()

    # Top TTPs
    if top_ttps:
        ln("---")
        ln()
        ln("## 🎯 Top TTPs Observed (MITRE ATT&CK)")
        ln()
        ln("| TTP ID | Count |")
        ln("|---|---|")
        for t in top_ttps:
            # top_ttps can be plain strings ["T1110"] or dicts [{"ttp":"T1110","count":5}]
            if isinstance(t, dict):
                ttp_id = t.get("ttp", "?")
                count  = t.get("count", "—")
            else:
                ttp_id = str(t)
                count  = "—"
            ttp_link = f"https://attack.mitre.org/techniques/{ttp_id.replace('.', '/')}"
            ln(f"| [{ttp_id}]({ttp_link}) | {count} |")
        ln()

    # FP summary
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

    # Pipeline health
    ln("---")
    ln()
    ln("## ⚙️ Pipeline Health")
    ln()
    ln("| Tool | Role | Status |")
    ln("|---|---|---|")
    ln(f"| Tool 05 | Network Monitor (port 2222) | {'✅' if hstatus == 'HEALTHY' else '❌'} {hstatus} |")
    ln(f"| Tool 26 | Incident Timeline Generator | {'✅' if total_cases > 0 else '⚠️'} {total_cases} cases |")
    ln(f"| Tool 27 | Threat Intel Feeder         | {'✅' if total_ips > 0 else '⚠️'} {total_ips} IPs enriched |")
    ln(f"| Tool 29 | False Positive Tracker      | ✅ {fp_count} filtered ({fp_rate}%) |")
    ln(f"| Tool 30 | Metric Exporter             | {'✅ stats.json written' if stats else '❌ no output'} |")
    ln(f"| Tool 28 | SOC Handover Report         | ✅ This report |")
    ln()

    # Next shift actions
    ln("---")
    ln()
    ln("## 📋 Standing Orders for Next Shift")
    ln()
    ln("- [ ] Verify honeypot is HEALTHY (Tool 05 green)")
    ln("- [ ] Review any new HIGH/CRITICAL IR cases in `data/ir_cases.json`")
    ln("- [ ] Check AbuseIPDB for newly reported IPs from this shift")
    ln("- [ ] If Cowrie captures a download, run Tool 31 malware analyzer")
    ln("- [ ] Integrity baseline auto-recreates every 2 hours via pipeline")
    ln()

    # Footer
    ln("---")
    ln()
    ln("_Generated by THIR · Tool 28 · SOC Handover Report Generator_  ")
    ln("_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  ")
    ln(f"_Report time: {now_str}_")
    ln()

    return "\n".join(L)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tool 28 — THIR SOC Handover Report Generator"
    )
    parser.add_argument("--ir-cases",   default="data/ir_cases.json")
    parser.add_argument("--threat-ips", default="data/threat_ips.json")
    parser.add_argument("--fp-filter",  default="data/fp_filter.json")
    parser.add_argument("--stats",      default="data/stats.json")
    parser.add_argument("--output",     default="data/soc_handover.md")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    log("SOC Handover Report Generator (THIR Live) started", "INFO", True)

    ir      = load_json(args.ir_cases,   "ir_cases.json",   args.verbose)
    threats = load_json(args.threat_ips, "threat_ips.json", args.verbose)
    fp      = load_json(args.fp_filter,  "fp_filter.json",  args.verbose)
    stats   = load_json(args.stats,      "stats.json",      args.verbose)

    report = build_report(ir, threats, fp, stats)

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

    log("SOC Handover Report Generator completed successfully", "INFO", True)


if __name__ == "__main__":
    main()
