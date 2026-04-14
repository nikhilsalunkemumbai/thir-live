# THIR — Threat Hunter Intelligence Range

A live honeypot threat intelligence dashboard. A Cowrie SSH honeypot runs on AWS EC2, feeding a GitHub Actions pipeline every two hours. Attacker sessions are parsed, enriched, false-positive filtered, clustered, malware-analyzed, alerted, and published to a live dashboard with automated SOC reporting.

**Live:** [threats.aegispub.com](https://threats.aegispub.com)

---

## Architecture

```
AWS EC2 Ubuntu (Cowrie SSH Honeypot — port 2222)
        │
        │  SSH/SCP every 2 hours via GitHub Actions (port 22222)
        │  NOTE: Port 22 on EC2 redirects to Cowrie via iptables.
        │        Always use port 22222 for pipeline/admin access.
        ▼
┌──────────────────────────────────────────────────────────────┐
│                   GitHub Actions Pipeline                     │
│                                                              │
│  ── Every 2 hours ─────────────────────────────────────── │
│  Tool 05  → Honeypot liveness check     → data/posture.json │
│           →                             → data/assets.json  │
│  [SCP]    → Incremental log fetch       → /tmp/cowrie.json  │
│  Tool 26  → Parse Cowrie sessions       → data/ir_cases.json│
│  Tool 34  → Credential extraction       → data/credentials.json│
│  Tool 35  → SSH fingerprint aggregation → data/ssh_fingerprints.json│
│  Tool 36  → Command clustering          → data/command_clusters.json│
│  Tool 27  → Enrich attacker IPs         → data/threat_ips.json│
│  Tool 29  → FP filter                   → data/fp_filter.json│
│  Tool 30  → Aggregate metrics           → data/stats.json   │
│  Tool 30b → ASN clustering              → data/asn_clusters.json│
│  [cond]   → Fetch downloads (if any)    → /tmp/cowrie-downloads/│
│  Tool 31  → Malware analysis (cond.)    → data/malware_report.json│
│  Tool 33  → YARA classifier (cond.)     → data/yara_matches.json│
│  Tool 28  → SOC handover report         → data/soc_handover.md│
│  Tool 37  → Alert engine                → data/alert_history.json│
│  Tool 32  → Save daily + peak stats     → reports/daily/    │
│  Tool 07  → Data integrity check        → (exit code)       │
│                                                              │
│  ── Monday 00:05 UTC ──────────────────────────────────── │
│  Tool 32 --rollup weekly                → reports/weekly/   │
│                                                              │
│  ── 1st of month 00:10 UTC ────────────────────────────── │
│  Tool 32 --rollup monthly               → reports/monthly/  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
        │  git push data/ + reports/
        ▼
GitHub Pages → threats.aegispub.com
```

---

## Pipeline Tools

| # | Tool | Language | Role |
|---|---|---|---|
| 05 | `05_network_monitor_live.go` | Go | TCP liveness check on Cowrie port 2222; writes asset inventory |
| 07 | `07_file_integrity_live.go` | Go | SHA-256 baseline verification of `data/` files |
| 26 | `26_incident_timeline_live.py` | Python | Parses Cowrie NDJSON → IR cases with MITRE ATT&CK TTPs |
| 27 | `27_threat_intel_feeder_live.go` | Go | Concurrent IP enrichment via AbuseIPDB + OTX |
| 28 | `28_soc_handover_live.py` | Python | Generates structured SOC handover report per run |
| 29 | `29_false_positive_live.py` | Python | 3-signal FP filter (score, ISP, behaviour) |
| 30 | `30_metric_exporter_live.go` | Go | Aggregates all pipeline outputs → dashboard stats |
| 30b | `30b_asn_clustering_live.go` | Go | Groups attacker IPs by ASN; tags Tor/VPN/proxy infrastructure |
| 31 | `31_malware_analyzer_live.py` | Python | Analyzes Cowrie-captured files: magic bytes, hashes, suspicious strings, optional VirusTotal |
| 32 | `32_report_lifecycle.py` | Python | Daily save, weekly/monthly rollup, peak stats tracking, 6-month retention pruning |
| 33 | `33_yara_classifier_live.py` | Python | YARA rule matching on downloaded malware samples; heuristic fallback |
| 34 | `34_credential_extractor_live.py` | Python | Extracts attacker username/password pairs; top credentials analysis |
| 35 | `35_ssh_fingerprint_live.py` | Python | HASSH fingerprints, client family mapping, botnet KEX detection |
| 36 | `36_command_clustering_live.py` | Python | Groups sessions by Jaccard similarity; detects known campaigns |
| 37 | `37_alerts_live.py` | Python | Alert engine for HIGH/CRITICAL findings; Slack/email/dry-run channels |

---

## Incremental Log Fetching

The pipeline uses watermark-based incremental fetching to avoid re-processing the full Cowrie log every run.

After each successful run, the total line count of the remote `cowrie.json` is saved to `data/cowrie_watermark.json`. On the next run, only new lines since the watermark are fetched via `tail -n +N`. This keeps each run processing only the delta — typically 50–200 lines per 2-hour window.

**Fallback:** If the watermark file is missing, or the VPS line count is less than the stored watermark (log rotation), the pipeline falls back to a full fetch automatically.

---

## Report Lifecycle (Tool 32)

Tool 32 manages a tiered SOC report retention system:

| Tier | Trigger | Output | Retention |
|---|---|---|---|
| **Daily** | Every pipeline run | `reports/daily/soc_YYYY-MM-DD.md` | 5–7 days |
| **Weekly** | Monday 00:05 UTC | `reports/weekly/soc_week_YYYY-WNN.md` | 3–4 weeks |
| **Monthly** | 1st of month 00:10 UTC | `reports/monthly/soc_YYYY-MM.md` | 6 months max |

Peak stats (peak sessions, peak unique IPs, peak confirmed threats) are tracked as high-water marks in `data/stats.json` — only updated when the current run beats the existing peak, never reset by a quieter run.

---

## Malware Analysis (Tool 31)

Tool 31 analyzes files downloaded by attackers through the Cowrie honeypot. It runs **only when downloads are detected** in `ir_cases.json`, and runs **before Tool 28** so the SOC handover report always contains current-run malware findings.

- **File type detection** via magic byte signatures (ELF, PE, shell scripts, archives)
- **Hash computation** — MD5, SHA1, SHA256 for every sample
- **ELF architecture detection** — x86, x86-64, ARM, AArch64, MIPS, RISC-V
- **Suspicious string scanning** — 30+ patterns: download tools, persistence, credential access, C2 indicators, crypto miners, destructive commands
- **VirusTotal lookup** (optional, free tier) — queries hash against VT API, reports detection ratios
- **Threat scoring** — 0–100 score mapping to LOW / MEDIUM / HIGH severity
- **Zero-byte and known-clean handling** — empty upload attempts recorded with notes; known-clean hashes excluded from report

Output: `data/malware_report.json`

---

## Alert Engine (Tool 37)

Tool 37 fires alerts on high-priority findings after each pipeline run. Alert conditions:

- HIGH or CRITICAL malware samples (from Tool 31 / Tool 33)
- New successful-authentication IPs
- New ASN clusters identified
- TCP tunnel attempts detected
- Active known campaigns (from Tool 36 clustering)

Channels are controlled by the `ALERT_CHANNEL` secret: `slack`, `email`, `both`, or `dry-run` (default if secret not set — safe on first deploy). Deduplication state is maintained in `data/alert_history.json` to prevent repeat alerts on the same finding.

---

## Quick Start

See **[SETUP.md](SETUP.md)** for the complete step-by-step deployment guide.

**Required GitHub Secrets:**

| Secret | Purpose |
|---|---|
| `ORACLE_VPS_SSH_KEY` | SSH private key for AWS EC2 (port 22222) |
| `ORACLE_VPS_IP` | AWS EC2 public IP |
| `ABUSEIPDB_API_KEY` | [abuseipdb.com](https://www.abuseipdb.com) free key |
| `OTX_API_KEY` | [otx.alienvault.com](https://otx.alienvault.com) free key |

**Optional GitHub Secrets:**

| Secret | Purpose |
|---|---|
| `VIRUSTOTAL_API_KEY` | VirusTotal free key — enables Tool 31 hash lookups |
| `ALERT_CHANNEL` | `slack` \| `email` \| `both` \| `dry-run` (default: `dry-run`) |
| `SLACK_WEBHOOK_URL` | Slack incoming webhook URL — required if `ALERT_CHANNEL` includes `slack` |
| `SMTP_HOST` / `SMTP_USER` / `SMTP_PASS` | SMTP credentials — required if `ALERT_CHANNEL` includes `email` |
| `ALERT_EMAIL_FROM` / `ALERT_EMAIL_TO` | Sender/recipient for email alerts |

---

## Repository Structure

```
thir-live/
├── .github/workflows/pipeline.yml   ← 3 schedules: every 2h + weekly + monthly
├── tools/                           ← 15 pipeline tools (05, 07, 26–37)
├── data/                            ← Written by pipeline every 2 hours
│   ├── ir_cases.json                ← IR cases from Cowrie sessions (Tool 26)
│   ├── threat_ips.json              ← Enriched attacker IPs (Tool 27)
│   ├── fp_filter.json               ← False positive decisions (Tool 29)
│   ├── stats.json                   ← Aggregated metrics + peak stats (Tool 30)
│   ├── posture.json                 ← Honeypot liveness + CIS controls (Tool 05)
│   ├── assets.json                  ← Live asset inventory (Tool 05)
│   ├── soc_handover.md              ← Current SOC shift report (Tool 28)
│   ├── malware_report.json          ← Malware analysis results (Tool 31)
│   ├── yara_matches.json            ← YARA classification results (Tool 33)
│   ├── credentials.json             ← Attacker credential pairs (Tool 34)
│   ├── ssh_fingerprints.json        ← HASSH fingerprints (Tool 35)
│   ├── command_clusters.json        ← Session clusters + campaigns (Tool 36)
│   ├── asn_clusters.json            ← ASN groupings (Tool 30b)
│   ├── alert_history.json           ← Alert dedup state (Tool 37)
│   ├── cowrie_watermark.json        ← Incremental fetch watermark
│   └── integrity_baseline.json     ← SHA-256 baseline (Tool 07)
├── reports/                         ← SOC report archive (Tool 32)
│   ├── daily/
│   ├── weekly/
│   └── monthly/
├── css/thir.css                     ← Dashboard stylesheet
├── js/                              ← Dashboard modules
│   ├── data.js
│   ├── pipeline.js
│   ├── render.js
│   ├── map.js
│   └── main.js
├── docs/                            ← Runbooks
│   └── runbook_rc_rp_1.md           ← EC2 recovery procedure (NIST RC.RP-1)
├── index.html                       ← Live dashboard
├── CNAME                            ← threats.aegispub.com
├── SETUP.md                         ← Full deployment guide
├── CONTRIBUTING.md
├── SECURITY.md
├── DISCLAIMER.md
└── LICENSE
```

---

## Planned Roadmap

| Priority | Feature | Tool |
|---|---|---|
| Medium | Weekly threat trend comparison (this week vs last week) | Tool 32 extension |
| Low | Slack/email alert on HIGH severity cases | Tool 37 (partial — expand triggers) |
| Low | Geo-clustering for threat map (group IPs by ASN) | Dashboard enhancement |

---

## License

MIT — see [LICENSE](LICENSE)

## Disclaimer

Defensive security research only. See [DISCLAIMER.md](DISCLAIMER.md).
