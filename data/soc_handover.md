# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-08 |
| **Generated At** | 2026-03-08T17:29:07Z |
| **Shift Time** | 17:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **494** |
| Confirmed Threats | **140** |
| False Positives Filtered | **354** (71.7%) |
| Unique Attacker IPs | **103** |
| Countries of Origin | **20** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **473** |
| Malware Analysis | ⚠️ malware_report.json not available (Tool 31 not run) |

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6608a900cd38

| Field | Detail |
|---|---|
| **Source IP** | `140.249.20.190` |
| **First Seen** | 2026-03-08 06:39 |
| **Last Seen** | 2026-03-08 06:44 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-08 06:39:21` | `cowrie.session.connect` |
| `2026-03-08 06:39:22` | `cowrie.client.version` |
| `2026-03-08 06:39:22` | `cowrie.client.kex` |
| `2026-03-08 06:39:23` | `cowrie.login.success` |
| `2026-03-08 06:44:23` | `cowrie.session.file_upload` |
| `2026-03-08 06:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.249.20.190` to AbuseIPDB if not already reported
- [ ] Block `140.249.20.190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f43f41e412c1

| Field | Detail |
|---|---|
| **Source IP** | `120.92.10.110` |
| **First Seen** | 2026-03-08 10:29 |
| **Last Seen** | 2026-03-08 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-08 10:29:05` | `cowrie.session.connect` |
| `2026-03-08 10:29:05` | `cowrie.client.version` |
| `2026-03-08 10:29:05` | `cowrie.client.kex` |
| `2026-03-08 10:29:06` | `cowrie.login.success` |
| `2026-03-08 10:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.92.10.110` to AbuseIPDB if not already reported
- [ ] Block `120.92.10.110` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2a7be2ce93

| Field | Detail |
|---|---|
| **Source IP** | `8.211.136.3` |
| **First Seen** | 2026-03-08 17:21 |
| **Last Seen** | 2026-03-08 17:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-08 17:21:41` | `cowrie.session.connect` |
| `2026-03-08 17:21:41` | `cowrie.client.version` |
| `2026-03-08 17:21:41` | `cowrie.client.kex` |
| `2026-03-08 17:21:42` | `cowrie.login.success` |
| `2026-03-08 17:21:43` | `cowrie.session.params` |
| `2026-03-08 17:21:43` | `cowrie.command.input` |
| `2026-03-08 17:21:43` | `cowrie.log.closed` |
| `2026-03-08 17:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.211.136.3` to AbuseIPDB if not already reported
- [ ] Block `8.211.136.3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43.7` | **47** | 2026-03-08 04:36 | 2026-03-08 06:52 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.41.65` | **24** | 2026-03-08 06:59 | 2026-03-08 07:04 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.42.190` | **11** | 2026-03-08 11:18 | 2026-03-08 11:21 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `165.22.121.5` | **7** | 2026-03-08 02:22 | 2026-03-08 02:27 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `51.89.1.86` | **6** | 2026-03-08 15:05 | 2026-03-08 15:12 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `8.211.136.3` | **6** | 2026-03-08 17:15 | 2026-03-08 17:23 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118.203` | **5** | 2026-03-08 09:21 | 2026-03-08 09:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.92.10.110` | **2** | 2026-03-08 10:28 | 2026-03-08 10:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.126.210` | **2** | 2026-03-08 01:45 | 2026-03-08 01:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `61.77.88.90` | **2** | 2026-03-08 07:53 | 2026-03-08 09:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `114.34.10.103` | 1 | 2026-03-08 03:32 | 2026-03-08 03:33 | 31s | 0 | `T1592` | 🟢 LOW |
| `115.137.64.30` | 1 | 2026-03-08 01:47 | 2026-03-08 01:47 | 30s | 0 | `T1592` | 🟢 LOW |
| `125.237.27.181` | 1 | 2026-03-08 01:33 | 2026-03-08 01:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.1.107.160` | 1 | 2026-03-08 00:25 | 2026-03-08 00:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `172.104.93.159` | 1 | 2026-03-08 06:55 | 2026-03-08 06:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `175.183.10.183` | 1 | 2026-03-08 02:23 | 2026-03-08 02:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.149.212.146` | 1 | 2026-03-08 00:31 | 2026-03-08 00:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.38.149.140` | 1 | 2026-03-08 14:53 | 2026-03-08 14:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176.7` | 1 | 2026-03-08 01:42 | 2026-03-08 01:42 | 4s | 0 | `T1592` | 🟢 LOW |
| `41.38.56.120` | 1 | 2026-03-08 09:09 | 2026-03-08 09:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.91.64.7` | 1 | 2026-03-08 10:17 | 2026-03-08 10:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.16.201.182` | 1 | 2026-03-08 10:14 | 2026-03-08 10:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.88.156.34` | 1 | 2026-03-08 02:59 | 2026-03-08 03:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156.34` | 1 | 2026-03-08 13:04 | 2026-03-08 13:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.39.73.37` | 1 | 2026-03-08 03:08 | 2026-03-08 03:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `68.220.61.198` | 1 | 2026-03-08 04:48 | 2026-03-08 04:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.179.72.28` | 1 | 2026-03-08 06:23 | 2026-03-08 06:23 | 31s | 0 | `T1592` | 🟢 LOW |
| `77.90.185.16` | 1 | 2026-03-08 04:47 | 2026-03-08 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89.144` | 1 | 2026-03-08 07:04 | 2026-03-08 07:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.231.89.145` | 1 | 2026-03-08 07:05 | 2026-03-08 07:05 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89.150` | 1 | 2026-03-08 07:05 | 2026-03-08 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109.222` | 1 | 2026-03-08 03:37 | 2026-03-08 03:37 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `93.40.14.230` | 1 | 2026-03-08 07:43 | 2026-03-08 07:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.231.206.203` | 1 | 2026-03-08 02:46 | 2026-03-08 02:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `98.94.49.146` | 1 | 2026-03-08 12:54 | 2026-03-08 12:54 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `223.123.41.65` | PK | CMPak Limited | **100** ⚠️ | 6 |
| `172.104.93.159` | JP | Linode | **100** ⚠️ | 50 |
| `114.34.10.103` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 36 |
| `185.38.149.140` | GB | Hydra Communications Ltd | **100** ⚠️ | 24 |
| `175.183.10.183` | TW | New Century InfoComm Tech. Co., Ltd. | **100** ⚠️ | 15 |
| `91.231.89.144` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `47.16.201.182` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 6 |
| `41.38.56.120` | EG | TE Data | **100** ⚠️ | 12 |
| `91.231.89.150` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `61.77.88.90` | KR | Korea Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |
| [T1105](https://attack.mitre.org/techniques/T1105) | — |

---

## 🔕 False Positive Summary (354 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 161 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 17 |
| AbuseIPDB score 18 below threshold 25 | 10 |
| AbuseIPDB score 2 below threshold 25 | 3 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 30 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 26 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 101 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 494 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 103 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 354 filtered (71.7%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ⚠️ malware_report.json not found — check pipeline order |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 3 priority case(s) shown individually · 35 recon entry/entries in table (10 group(s) consolidating 112 session(s)).

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
_Report time: 2026-03-08T17:29:07Z_
