# THIR — Threat Hunter Intelligence Range

A live honeypot threat intelligence dashboard. A Cowrie SSH honeypot runs on AWS EC2, feeding a GitHub Actions pipeline every hour. Attacker sessions are parsed, enriched, false-positive filtered, and published to a live dashboard.

**Live:** [threats.aegispub.com](https://threats.aegispub.com)

---

## Architecture

```
AWS EC2 Ubuntu (Cowrie SSH Honeypot — port 2222)
        │
        │  SCP every hour via GitHub Actions
        ▼
┌─────────────────────────────────────────────────┐
│              GitHub Actions Pipeline             │
│  Tool 05 → Honeypot liveness   → posture.json  │
│  Tool 26 → Parse sessions      → ir_cases.json │
│  Tool 27 → Enrich IPs          → threat_ips.json│
│  Tool 29 → FP filter           → fp_filter.json│
│  Tool 30 → Aggregate metrics   → stats.json    │
│  Tool 07 → Integrity check                     │
└─────────────────────────────────────────────────┘
        │  git push data/
        ▼
GitHub Pages → threats.aegispub.com
```

---

## Pipeline Tools

| Tool | Language | Role |
|---|---|---|
| `05_network_monitor_live.go` | Go | TCP liveness check on Cowrie port 2222 |
| `26_incident_timeline_live.py` | Python | Parses Cowrie NDJSON → IR cases with MITRE ATT&CK TTPs |
| `27_threat_intel_feeder_live.go` | Go | Concurrent IP enrichment via AbuseIPDB + OTX |
| `29_false_positive_live.py` | Python | 3-signal FP filter (score, ISP, behaviour) |
| `30_metric_exporter_live.go` | Go | Aggregates all pipeline outputs → dashboard stats |
| `07_file_integrity_live.go` | Go | SHA-256 baseline verification of data/ files |

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

---

## Repository Structure

```
thir-live/
├── .github/workflows/pipeline.yml
├── tools/                        ← 6 pipeline tools
├── data/                         ← Written by pipeline each hour
├── index.html                    ← Live dashboard
├── CNAME                         ← threats.aegispub.com
├── SETUP.md                      ← Full deployment guide
├── CONTRIBUTING.md
├── SECURITY.md
├── DISCLAIMER.md
└── LICENSE
```

---

## License

MIT — see [LICENSE](LICENSE)

## Disclaimer

Defensive security research only. See [DISCLAIMER.md](DISCLAIMER.md).
