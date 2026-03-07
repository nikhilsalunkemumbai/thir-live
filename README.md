# THIR — Threat Hunter Intelligence Range

A live honeypot threat intelligence dashboard. A Cowrie SSH honeypot runs on AWS EC2, feeding a GitHub Actions pipeline every hour. Attacker sessions are parsed, enriched, false-positive filtered, malware-analyzed, and published to a live dashboard with automated SOC reporting.

**Live:** [threats.aegispub.com](https://threats.aegispub.com)

---

## Architecture

```
AWS EC2 Ubuntu (Cowrie SSH Honeypot — port 2222)
        │
        │  SCP every hour via GitHub Actions
        ▼
┌──────────────────────────────────────────────────────────┐
│                 GitHub Actions Pipeline                   │
│                                                          │
│  ── Hourly ──────────────────────────────────────────── │
│  Tool 05 → Honeypot liveness check  → data/posture.json │
│  Tool 26 → Parse Cowrie sessions    → data/ir_cases.json│
│  Tool 27 → Enrich attacker IPs      → data/threat_ips.json│
│  Tool 29 → FP filter                → data/fp_filter.json│
│  Tool 30 → Aggregate metrics        → data/stats.json   │
│  Tool 28 → SOC handover report      → data/soc_handover.md│
│  Tool 31 → Malware sample analysis  → data/malware_report.json│
│  Tool 32 → Save daily + peak stats  → reports/daily/    │
│  Tool 07 → Data integrity check                         │
│                                                          │
│  ── Monday 00:05 UTC ───────────────────────────────── │
│  Tool 32 --rollup weekly            → reports/weekly/   │
│                                                          │
│  ── 1st of month 00:10 UTC ─────────────────────────── │
│  Tool 32 --rollup monthly           → reports/monthly/  │
│                                                          │
└──────────────────────────────────────────────────────────┘
        │  git push data/ + reports/
        ▼
GitHub Pages → threats.aegispub.com
```

---

## Pipeline Tools

| # | Tool | Language | Role |
|---|---|---|---|
| 05 | `05_network_monitor_live.go` | Go | TCP liveness check on Cowrie port 2222 |
| 26 | `26_incident_timeline_live.py` | Python | Parses Cowrie NDJSON → IR cases with MITRE ATT&CK TTPs |
| 27 | `27_threat_intel_feeder_live.go` | Go | Concurrent IP enrichment via AbuseIPDB + OTX |
| 29 | `29_false_positive_live.py` | Python | 3-signal FP filter (score, ISP, behaviour) |
| 30 | `30_metric_exporter_live.go` | Go | Aggregates all pipeline outputs → dashboard stats |
| 28 | `28_soc_handover_live.py` | Python | Generates structured SOC handover report per run |
| 31 | `31_malware_analyzer_live.py` | Python | Analyzes Cowrie-captured files: magic bytes, hashes, suspicious strings, optional VirusTotal lookup |
| 32 | `32_report_lifecycle.py` | Python | Daily save, weekly/monthly rollup, peak stats tracking, 6-month retention pruning |
| 07 | `07_file_integrity_live.go` | Go | SHA-256 baseline verification of data/ files |

---

## Report Lifecycle (Tool 32)

Tool 32 manages a tiered SOC report retention system:

| Tier | Trigger | Output | Retention |
|---|---|---|---|
| **Daily** | Every hourly pipeline run | `reports/daily/soc_YYYY-MM-DD.md` | 5–7 days |
| **Weekly** | Monday 00:05 UTC | `reports/weekly/soc_week_YYYY-WNN.md` | 3–4 weeks |
| **Monthly** | 1st of month 00:10 UTC | `reports/monthly/soc_YYYY-MM.md` | 6 months max |

Peak stats (peak sessions, peak unique IPs, peak confirmed threats) are tracked as high-water marks in `data/stats.json` — only updated when today beats the current peak, never reset by a quieter day.

---

## Malware Analysis (Tool 31)

Tool 31 analyzes files downloaded by attackers through the Cowrie honeypot:

- **File type detection** via magic byte signatures (ELF, PE, shell scripts, archives)
- **Hash computation** — MD5, SHA1, SHA256 for every sample
- **ELF architecture detection** — x86, x86-64, ARM, AArch64, MIPS, RISC-V
- **Suspicious string scanning** — 30+ patterns covering download tools, persistence, credential access, C2 indicators, crypto miners, and destructive commands
- **VirusTotal lookup** (optional, free tier) — queries hash against VT API, reports detection ratios
- **Threat scoring** — 0–100 score mapping to LOW / MEDIUM / HIGH severity

Output: `data/malware_report.json`

---

## Quick Start

See **[SETUP.md](SETUP.md)** for the complete step-by-step deployment guide.

**Required GitHub Secrets:**

| Secret | Purpose |
|---|---|
| `ORACLE_VPS_SSH_KEY` | SSH private key for AWS EC2 |
| `ORACLE_VPS_IP` | AWS EC2 public IP |
| `ABUSEIPDB_API_KEY` | [abuseipdb.com](https://www.abuseipdb.com) free key |
| `OTX_API_KEY` | [otx.alienvault.com](https://otx.alienvault.com) free key |
| `VIRUSTOTAL_API_KEY` | *(Optional)* [virustotal.com](https://www.virustotal.com) free key — for Tool 31 malware lookup |

---

## Repository Structure

```
thir-live/
├── .github/workflows/pipeline.yml   ← 3 jobs: hourly + weekly + monthly
├── tools/                           ← 9 pipeline tools (05, 07, 26–32)
├── data/                            ← Written by pipeline each hour
│   ├── ir_cases.json
│   ├── threat_ips.json
│   ├── fp_filter.json
│   ├── stats.json
│   ├── posture.json
│   ├── soc_handover.md
│   └── malware_report.json
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
| High | YARA rule matching on malware samples | Tool 33 (planned) |
| Medium | Cowrie credential pair extraction + password analysis | Tool 34 (planned) |
| Medium | Geo-clustering for threat map (group IPs by ASN) | Dashboard enhancement |
| Low | Slack/email alert on HIGH severity cases | Notification layer |
| Low | Weekly threat trend comparison (this week vs last week) | Tool 32 extension |

---

## License

MIT — see [LICENSE](LICENSE)

## Disclaimer

Defensive security research only. See [DISCLAIMER.md](DISCLAIMER.md).
