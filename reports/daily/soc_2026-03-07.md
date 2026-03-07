# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-07 |
| **Generated At** | 2026-03-07T09:35:54Z |
| **Shift Time** | 09:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **16** |
| Confirmed Threats | **3** |
| False Positives Filtered | **13** (81.2%) |
| Unique Attacker IPs | **7** |
| Countries of Origin | **3** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **11** |

---

## 🚨 Confirmed Threats (3)

### 🔴 HIGH · IR-91073fd0fd5a

| Field | Detail |
|---|---|
| **Source IP** | `138.197.147.214` |
| **First Seen** | 2026-03-07T09:30:54.545747Z |
| **Last Seen** | 2026-03-07T09:31:00.055969Z |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:30:54` | `cowrie.session.connect` |
| `2026-03-07 09:30:54` | `cowrie.client.version` |
| `2026-03-07 09:30:54` | `cowrie.client.kex` |
| `2026-03-07 09:30:57` | `cowrie.login.success` |
| `2026-03-07 09:30:58` | `cowrie.session.params` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:59` | `cowrie.log.closed` |
| `2026-03-07 09:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.147.214` to AbuseIPDB if not already reported
- [ ] Block `138.197.147.214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b59fa4b68254

| Field | Detail |
|---|---|
| **Source IP** | `138.197.147.214` |
| **First Seen** | 2026-03-07T09:31:58.603021Z |
| **Last Seen** | 2026-03-07T09:32:03.647960Z |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:31:58` | `cowrie.session.connect` |
| `2026-03-07 09:31:58` | `cowrie.client.version` |
| `2026-03-07 09:31:58` | `cowrie.client.kex` |
| `2026-03-07 09:32:00` | `cowrie.login.success` |
| `2026-03-07 09:32:02` | `cowrie.session.params` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.log.closed` |
| `2026-03-07 09:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.147.214` to AbuseIPDB if not already reported
- [ ] Block `138.197.147.214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d13b9f971b

| Field | Detail |
|---|---|
| **Source IP** | `138.197.147.214` |
| **First Seen** | 2026-03-07T09:33:55.004920Z |
| **Last Seen** | 2026-03-07T09:33:59.886109Z |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:33:55` | `cowrie.session.connect` |
| `2026-03-07 09:33:55` | `cowrie.client.version` |
| `2026-03-07 09:33:55` | `cowrie.client.kex` |
| `2026-03-07 09:33:57` | `cowrie.login.success` |
| `2026-03-07 09:33:58` | `cowrie.session.params` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:59` | `cowrie.log.closed` |
| `2026-03-07 09:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.147.214` to AbuseIPDB if not already reported
- [ ] Block `138.197.147.214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `138.197.147.214` | CA | DigitalOcean, LLC | **42** | 0 |
| `135.232.224.117` | US | Microsoft Limited | **30** | 0 |
| `172.215.211.18` | US | Microsoft Limited | 17 | 0 |
| `52.190.182.224` | US | Microsoft Corporation | 7 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 16 cases |
| Tool 27 | Threat Intel Feeder         | ✅ 7 IPs enriched |
| Tool 29 | False Positive Tracker      | ✅ 13 filtered (81.2%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 28 | SOC Handover Report         | ✅ This report |

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL IR cases in `data/ir_cases.json`
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, run Tool 31 malware analyzer
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-07T09:35:54Z_
