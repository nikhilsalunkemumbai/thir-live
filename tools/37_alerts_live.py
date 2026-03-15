#!/usr/bin/env python3
"""
Tool 37 — Alerts
THIR · nikhilsalunkemumbai/thir-live
Input:  data/*.json  (all pipeline outputs)
Output: Slack webhook POST and/or email via SMTP
        data/alert_history.json  (deduplication state)

Monitors pipeline data on each run and fires alerts when trigger
conditions are met. Deduplicates alerts to prevent noise.
Channel is selected by env var or --channel flag (slack / email / both).
"""

import json
import hashlib
import argparse
import sys
import os
import smtplib
from datetime import datetime, timezone, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import urlencode
import urllib.request

# ── Alert severity levels ────────────────────────────────────────────────────
SEV_EMOJI = {
    "CRITICAL": "🔴",
    "HIGH":     "🟠",
    "MEDIUM":   "🟡",
    "LOW":      "🟢",
    "INFO":     "🔵",
}

SEV_COLOR = {
    "CRITICAL": "#ff0000",
    "HIGH":     "#ff6600",
    "MEDIUM":   "#ffcc00",
    "LOW":      "#00cc00",
    "INFO":     "#0099ff",
}

# ── Deduplication window ─────────────────────────────────────────────────────
DEDUP_HOURS = {
    "CRITICAL": 1,
    "HIGH":     4,
    "MEDIUM":   24,
    "LOW":      48,
    "INFO":     72,
}


def load_json_safe(path: str) -> dict:
    """Load a JSON file, return empty dict if missing or corrupt."""
    p = Path(path)
    if not p.exists():
        return {}
    try:
        with open(p) as f:
            return json.load(f)
    except Exception:
        return {}


def load_alert_history(path: str) -> dict:
    """Load deduplication history."""
    p = Path(path)
    if not p.exists():
        return {"alerts": {}}
    try:
        with open(p) as f:
            return json.load(f)
    except Exception:
        return {"alerts": {}}


def save_alert_history(history: dict, path: str):
    """Persist deduplication history."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        json.dump(history, f, indent=2)


def alert_key(alert_type: str, detail: str) -> str:
    """Compute a deduplication key."""
    raw = f"{alert_type}:{detail}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def is_duplicate(key: str, severity: str, history: dict) -> bool:
    """Check if this alert was recently fired."""
    now = datetime.now(timezone.utc)
    window_hours = DEDUP_HOURS.get(severity, 24)
    record = history.get("alerts", {}).get(key)
    if not record:
        return False
    try:
        last_fired = datetime.fromisoformat(record["last_fired"])
        if last_fired.tzinfo is None:
            last_fired = last_fired.replace(tzinfo=timezone.utc)
        if (now - last_fired).total_seconds() < window_hours * 3600:
            return True
    except Exception:
        return False
    return False


def record_alert(key: str, severity: str, title: str, history: dict):
    """Record that this alert was fired."""
    now = datetime.now(timezone.utc).isoformat()
    if "alerts" not in history:
        history["alerts"] = {}
    if key not in history["alerts"]:
        history["alerts"][key] = {"fired_count": 0}
    history["alerts"][key]["last_fired"] = now
    history["alerts"][key]["severity"] = severity
    history["alerts"][key]["title"] = title
    history["alerts"][key]["fired_count"] = history["alerts"][key].get("fired_count", 0) + 1


# ── Trigger evaluators ───────────────────────────────────────────────────────

def check_malware_alerts(malware_data: dict, yara_data: dict) -> list:
    """Alert on HIGH/CRITICAL malware detections."""
    alerts = []

    # Tool 31 malware report
    for sample in malware_data.get("samples", []):
        threat = sample.get("threat_level", "").upper()
        if threat in ("HIGH", "CRITICAL"):
            fname = sample.get("filename", "unknown")
            family = sample.get("malware_family", sample.get("family", "unknown"))
            alerts.append({
                "type": "malware_detection",
                "severity": threat,
                "title": f"Malware Sample Detected: {family}",
                "detail": f"File `{fname}` classified as **{family}** [{threat}]",
                "key_detail": f"{fname}:{family}",
                "data": sample,
            })

    # Tool 33 YARA matches
    for result in yara_data.get("results", []):
        if result.get("severity") in ("HIGH", "CRITICAL") and result.get("classified"):
            fname = result.get("filename", "unknown")
            families = ", ".join(result.get("families", ["unknown"]))
            sev = result.get("severity", "HIGH")
            alerts.append({
                "type": "yara_match",
                "severity": sev,
                "title": f"YARA Match: {families}",
                "detail": f"File `{fname}` matched YARA rules → **{families}** [{sev}]",
                "key_detail": f"{fname}:{families}",
                "data": result,
            })

    return alerts


def check_credential_alerts(cred_data: dict, cred_history: dict) -> list:
    """Alert on successful auth pairs from IPs not seen in last 7 days."""
    alerts = []
    now = datetime.now(timezone.utc)
    seen_ips = cred_history.get("seen_success_ips", {})

    for pair in cred_data.get("success_pairs", []):
        ip = pair.get("src_ip", "")
        if not ip:
            continue
        last_seen_str = seen_ips.get(ip)
        is_new = True
        if last_seen_str:
            try:
                last_seen = datetime.fromisoformat(last_seen_str)
                if last_seen.tzinfo is None:
                    last_seen = last_seen.replace(tzinfo=timezone.utc)
                if (now - last_seen).total_seconds() < 7 * 86400:
                    is_new = False
            except Exception:
                pass

        if is_new:
            alerts.append({
                "type": "new_successful_auth",
                "severity": "HIGH",
                "title": f"Successful Auth from New IP: {ip}",
                "detail": (f"Successful login `{pair.get('username','?')}` / "
                           f"`{pair.get('password','?')}` from **{ip}** "
                           f"(not seen in last 7 days)"),
                "key_detail": ip,
                "data": pair,
            })
            # Record as seen
            seen_ips[ip] = now.isoformat()

    cred_history["seen_success_ips"] = seen_ips
    return alerts


def check_asn_alerts(asn_data: dict, asn_history: dict) -> list:
    """Alert on new ASN clusters appearing for the first time."""
    alerts = []
    seen_asns = asn_history.get("seen_asns", set())
    if isinstance(seen_asns, list):
        seen_asns = set(seen_asns)

    for cluster in asn_data.get("clusters", []):
        asn = cluster.get("asn", "")
        if not asn or asn == "AS0":
            continue
        if asn not in seen_asns and cluster.get("ip_count", 0) >= 2:
            tier = cluster.get("risk_tier", "LOW")
            sev = "HIGH" if tier == "HIGH" else "MEDIUM"
            alerts.append({
                "type": "new_asn_cluster",
                "severity": sev,
                "title": f"New Attack ASN: {asn} ({cluster.get('asn_name','unknown')})",
                "detail": (f"ASN **{asn}** ({cluster.get('asn_name','?')}) "
                           f"appeared for the first time with "
                           f"{cluster.get('ip_count',0)} attacking IPs "
                           f"[{tier}]"),
                "key_detail": asn,
                "data": cluster,
            })
            seen_asns.add(asn)

    asn_history["seen_asns"] = list(seen_asns)
    return alerts


def check_tunnel_alerts(ir_cases: dict) -> list:
    """Alert on cowrie.direct-tcpip TCP tunnel attempts."""
    alerts = []
    cases = ir_cases if isinstance(ir_cases, list) else ir_cases.get("cases", ir_cases.get("ir_cases", []))

    for case in cases:
        for evt in case.get("events", []):
            etype = evt.get("eventid", evt.get("event_type", ""))
            if etype == "cowrie.direct-tcpip":
                src_ip = case.get("src_ip", case.get("attacker_ip", "unknown"))
                dst_ip = evt.get("dst_ip", evt.get("destip", "?"))
                dst_port = evt.get("dst_port", evt.get("destport", "?"))
                alerts.append({
                    "type": "tcp_tunnel_attempt",
                    "severity": "HIGH",
                    "title": f"TCP Tunnel Attempt from {src_ip}",
                    "detail": (f"**{src_ip}** attempted TCP tunnel via honeypot "
                               f"→ `{dst_ip}:{dst_port}` (T1572 Protocol Tunneling)"),
                    "key_detail": f"{src_ip}:{dst_ip}:{dst_port}",
                    "data": evt,
                })

    return alerts


def check_campaign_alerts(cmd_clusters: dict) -> list:
    """Alert on detected attack campaigns."""
    alerts = []
    for cluster in cmd_clusters.get("clusters", []):
        if not cluster.get("is_campaign"):
            continue
        sev = cluster.get("campaign_severity", "MEDIUM")
        if sev not in ("HIGH", "CRITICAL"):
            continue
        alerts.append({
            "type": "campaign_detected",
            "severity": sev,
            "title": f"Attack Campaign Detected: {cluster.get('campaign_name','unknown')}",
            "detail": (f"Campaign **{cluster.get('campaign_name','?')}** "
                       f"detected across {cluster.get('session_count',0)} sessions "
                       f"from {cluster.get('unique_ip_count',0)} IPs. "
                       f"TTPs: {', '.join(t['id'] for t in cluster.get('ttps',[]))[:80]}"),
            "key_detail": cluster.get("campaign_name", ""),
            "data": {
                "cluster_id": cluster.get("cluster_id"),
                "session_count": cluster.get("session_count"),
                "unique_ip_count": cluster.get("unique_ip_count"),
                "ttps": cluster.get("ttps"),
            },
        })
    return alerts


# ── Notification senders ─────────────────────────────────────────────────────

def send_slack(webhook_url: str, alerts: list, dry_run: bool = False) -> int:
    """Send alert batch to Slack webhook. Returns number of messages sent."""
    if not alerts:
        return 0
    if not webhook_url:
        print("[Tool37] SLACK_WEBHOOK_URL not set — skipping Slack", file=sys.stderr)
        return 0

    sent = 0
    for alert in alerts:
        sev = alert["severity"]
        emoji = SEV_EMOJI.get(sev, "⚪")
        color = SEV_COLOR.get(sev, "#cccccc")
        now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

        payload = {
            "text": f"{emoji} *THIR Alert* — {alert['title']}",
            "attachments": [
                {
                    "color": color,
                    "fields": [
                        {"title": "Severity", "value": sev, "short": True},
                        {"title": "Type",     "value": alert["type"], "short": True},
                        {"title": "Detail",   "value": alert["detail"], "short": False},
                        {"title": "Time",     "value": now_str, "short": True},
                    ],
                    "footer": "THIR · threats.aegispub.com",
                }
            ],
        }

        if dry_run:
            print(f"[Tool37] DRY-RUN Slack: {alert['title']}")
            sent += 1
            continue

        try:
            body = json.dumps(payload).encode()
            req = Request(webhook_url, data=body, headers={"Content-Type": "application/json"})
            with urlopen(req, timeout=10) as resp:
                if resp.status == 200:
                    sent += 1
                else:
                    print(f"[Tool37] Slack response {resp.status} for {alert['title']}", file=sys.stderr)
        except URLError as e:
            print(f"[Tool37] Slack send error: {e}", file=sys.stderr)

    return sent


def send_email(smtp_host: str, smtp_port: int, smtp_user: str, smtp_pass: str,
               from_addr: str, to_addr: str, alerts: list, dry_run: bool = False) -> int:
    """Send alert batch as email. Returns number of messages sent."""
    if not alerts:
        return 0
    if not smtp_host or not to_addr:
        print("[Tool37] SMTP config incomplete — skipping email", file=sys.stderr)
        return 0

    sent = 0
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    subject = f"[THIR] {len(alerts)} Alert{'s' if len(alerts)>1 else ''} — {alerts[0]['severity']} — {now_str}"

    # Build HTML body
    rows = ""
    for a in alerts:
        sev = a["severity"]
        color = SEV_COLOR.get(sev, "#cccccc")
        rows += f"""
        <tr>
          <td style="background:{color};color:#fff;padding:4px 8px;font-weight:bold">{sev}</td>
          <td style="padding:4px 8px"><strong>{a['title']}</strong><br>{a['detail']}</td>
          <td style="padding:4px 8px;color:#888">{a['type']}</td>
        </tr>"""

    html = f"""
    <html><body style="font-family:monospace;font-size:13px">
    <h2>🛡 THIR Alert Report — {now_str}</h2>
    <p>{len(alerts)} alert(s) triggered on this pipeline run.</p>
    <table border="1" cellspacing="0" style="border-collapse:collapse;width:100%">
      <tr style="background:#222;color:#fff">
        <th style="padding:6px">Severity</th>
        <th style="padding:6px">Alert</th>
        <th style="padding:6px">Type</th>
      </tr>
      {rows}
    </table>
    <p style="color:#888;font-size:11px">THIR · threats.aegispub.com · {now_str}</p>
    </body></html>"""

    if dry_run:
        print(f"[Tool37] DRY-RUN Email: {subject} → {to_addr}")
        return len(alerts)

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_addr or smtp_user
    msg["To"] = to_addr
    msg.attach(MIMEText(html, "html"))

    try:
        with smtplib.SMTP(smtp_host, smtp_port, timeout=15) as server:
            server.starttls()
            if smtp_user and smtp_pass:
                server.login(smtp_user, smtp_pass)
            server.sendmail(msg["From"], [to_addr], msg.as_string())
        sent = len(alerts)
    except Exception as e:
        print(f"[Tool37] Email send error: {e}", file=sys.stderr)

    return sent


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Tool 37 — Alerts")
    parser.add_argument("--malware-report",   default="data/malware_report.json")
    parser.add_argument("--yara-matches",     default="data/yara_matches.json")
    parser.add_argument("--credentials",      default="data/credentials.json")
    parser.add_argument("--asn-clusters",     default="data/asn_clusters.json")
    parser.add_argument("--ir-cases",         default="data/ir_cases.json")
    parser.add_argument("--command-clusters", default="data/command_clusters.json")
    parser.add_argument("--alert-history",    default="data/alert_history.json")
    parser.add_argument("--channel",          default=os.environ.get("ALERT_CHANNEL", "slack"),
                        choices=["slack", "email", "both", "dry-run"],
                        help="Notification channel")
    # Slack
    parser.add_argument("--slack-webhook",    default=os.environ.get("SLACK_WEBHOOK_URL", ""))
    # Email
    parser.add_argument("--smtp-host",        default=os.environ.get("SMTP_HOST", ""))
    parser.add_argument("--smtp-port",        type=int, default=int(os.environ.get("SMTP_PORT", "587")))
    parser.add_argument("--smtp-user",        default=os.environ.get("SMTP_USER", ""))
    parser.add_argument("--smtp-pass",        default=os.environ.get("SMTP_PASS", ""))
    parser.add_argument("--email-from",       default=os.environ.get("ALERT_EMAIL_FROM", ""))
    parser.add_argument("--email-to",         default=os.environ.get("ALERT_EMAIL_TO", ""))
    args = parser.parse_args()

    print(f"[Tool37] Channel: {args.channel}")

    # Load all data
    malware_data  = load_json_safe(args.malware_report)
    yara_data     = load_json_safe(args.yara_matches)
    cred_data     = load_json_safe(args.credentials)
    asn_data      = load_json_safe(args.asn_clusters)
    cmd_clusters  = load_json_safe(args.command_clusters)
    ir_cases_raw  = load_json_safe(args.ir_cases)
    ir_cases      = ir_cases_raw if isinstance(ir_cases_raw, list) else ir_cases_raw.get("cases", [])

    # Load history
    history = load_alert_history(args.alert_history)
    cred_history = history.setdefault("credential_ips", {})
    asn_history  = history.setdefault("asn_seen", {})

    # Evaluate all triggers
    raw_alerts = []
    raw_alerts.extend(check_malware_alerts(malware_data, yara_data))
    raw_alerts.extend(check_credential_alerts(cred_data, cred_history))
    raw_alerts.extend(check_asn_alerts(asn_data, asn_history))
    raw_alerts.extend(check_tunnel_alerts(ir_cases))
    raw_alerts.extend(check_campaign_alerts(cmd_clusters))

    print(f"[Tool37] Raw alerts: {len(raw_alerts)}")

    # Deduplicate
    dedup_history = history.setdefault("alerts", {})
    alerts_to_fire = []
    for alert in raw_alerts:
        key = alert_key(alert["type"], alert.get("key_detail", ""))
        if is_duplicate(key, alert["severity"], {"alerts": dedup_history}):
            print(f"[Tool37] Suppressed (duplicate): {alert['title']}")
            continue
        alerts_to_fire.append((key, alert))

    print(f"[Tool37] Alerts to fire: {len(alerts_to_fire)}")

    if not alerts_to_fire:
        print("[Tool37] No new alerts — pipeline clean")
        save_alert_history(history, args.alert_history)
        return

    # Sort by severity
    sev_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}
    alerts_to_fire.sort(key=lambda x: sev_order.get(x[1]["severity"], 9))
    alerts_list = [a for _, a in alerts_to_fire]

    # Send notifications
    dry_run = (args.channel == "dry-run")
    sent_slack = sent_email = 0

    if args.channel in ("slack", "both", "dry-run"):
        sent_slack = send_slack(args.slack_webhook, alerts_list, dry_run=dry_run)
        print(f"[Tool37] Slack sent: {sent_slack}")

    if args.channel in ("email", "both"):
        sent_email = send_email(
            args.smtp_host, args.smtp_port,
            args.smtp_user, args.smtp_pass,
            args.email_from, args.email_to,
            alerts_list, dry_run=dry_run
        )
        print(f"[Tool37] Email sent: {sent_email}")

    # Record fired alerts in history
    for key, alert in alerts_to_fire:
        record_alert(key, alert["severity"], alert["title"], {"alerts": dedup_history})

    save_alert_history(history, args.alert_history)
    print(f"[Tool37] ✓ Done — {len(alerts_to_fire)} alerts fired")

    for _, a in alerts_to_fire:
        emoji = SEV_EMOJI.get(a["severity"], "⚪")
        print(f"[Tool37]   {emoji} [{a['severity']}] {a['title']}")


if __name__ == "__main__":
    main()
