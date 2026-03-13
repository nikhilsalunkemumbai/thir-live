# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-13 |
| **Generated At** | 2026-03-13T20:32:04Z |
| **Shift Time** | 20:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **662** |
| Confirmed Threats | **91** |
| False Positives Filtered | **571** (86.2%) |
| Unique Attacker IPs | **222** |
| Countries of Origin | **17** |
| High Severity Cases | **51** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **611** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d9f2dab58324

| Field | Detail |
|---|---|
| **Source IP** | `142.93.225[.]92` |
| **First Seen** | 2026-03-13 07:42 |
| **Last Seen** | 2026-03-13 07:48 |
| **Session Duration** | 307s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 07:42:56` | `cowrie.session.connect` |
| `2026-03-13 07:42:57` | `cowrie.client.version` |
| `2026-03-13 07:42:57` | `cowrie.client.kex` |
| `2026-03-13 07:43:04` | `cowrie.login.success` |
| `2026-03-13 07:43:08` | `cowrie.session.params` |
| `2026-03-13 07:43:08` | `cowrie.command.input` |
| `2026-03-13 07:43:08` | `cowrie.command.input` |
| `2026-03-13 07:43:08` | `cowrie.command.input` |
| `2026-03-13 07:43:08` | `cowrie.command.input` |
| `2026-03-13 07:43:10` | `cowrie.log.closed` |
| `2026-03-13 07:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `142.93.225[.]92` to AbuseIPDB if not already reported
- [ ] Block `142.93.225[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2fcb11dd792

| Field | Detail |
|---|---|
| **Source IP** | `170.64.165[.]10` |
| **First Seen** | 2026-03-13 12:47 |
| **Last Seen** | 2026-03-13 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 12:47:31` | `cowrie.session.connect` |
| `2026-03-13 12:47:32` | `cowrie.client.version` |
| `2026-03-13 12:47:32` | `cowrie.client.kex` |
| `2026-03-13 12:47:33` | `cowrie.login.success` |
| `2026-03-13 12:47:34` | `cowrie.session.params` |
| `2026-03-13 12:47:34` | `cowrie.command.input` |
| `2026-03-13 12:47:34` | `cowrie.command.input` |
| `2026-03-13 12:47:34` | `cowrie.command.input` |
| `2026-03-13 12:47:34` | `cowrie.command.input` |
| `2026-03-13 12:47:34` | `cowrie.log.closed` |
| `2026-03-13 12:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.165[.]10` to AbuseIPDB if not already reported
- [ ] Block `170.64.165[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b3ef624635

| Field | Detail |
|---|---|
| **Source IP** | `170.64.165[.]10` |
| **First Seen** | 2026-03-13 12:48 |
| **Last Seen** | 2026-03-13 12:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 12:48:19` | `cowrie.session.connect` |
| `2026-03-13 12:48:19` | `cowrie.client.version` |
| `2026-03-13 12:48:19` | `cowrie.client.kex` |
| `2026-03-13 12:48:21` | `cowrie.login.success` |
| `2026-03-13 12:48:22` | `cowrie.session.params` |
| `2026-03-13 12:48:22` | `cowrie.command.input` |
| `2026-03-13 12:48:22` | `cowrie.command.input` |
| `2026-03-13 12:48:22` | `cowrie.command.input` |
| `2026-03-13 12:48:22` | `cowrie.command.input` |
| `2026-03-13 12:48:22` | `cowrie.log.closed` |
| `2026-03-13 12:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.165[.]10` to AbuseIPDB if not already reported
- [ ] Block `170.64.165[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3e2c21cb27

| Field | Detail |
|---|---|
| **Source IP** | `170.64.165[.]10` |
| **First Seen** | 2026-03-13 12:49 |
| **Last Seen** | 2026-03-13 12:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 12:49:09` | `cowrie.session.connect` |
| `2026-03-13 12:49:09` | `cowrie.client.version` |
| `2026-03-13 12:49:09` | `cowrie.client.kex` |
| `2026-03-13 12:49:10` | `cowrie.login.success` |
| `2026-03-13 12:49:11` | `cowrie.session.params` |
| `2026-03-13 12:49:11` | `cowrie.command.input` |
| `2026-03-13 12:49:11` | `cowrie.command.input` |
| `2026-03-13 12:49:11` | `cowrie.command.input` |
| `2026-03-13 12:49:11` | `cowrie.command.input` |
| `2026-03-13 12:49:12` | `cowrie.log.closed` |
| `2026-03-13 12:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.165[.]10` to AbuseIPDB if not already reported
- [ ] Block `170.64.165[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d4c8bedeadd

| Field | Detail |
|---|---|
| **Source IP** | `170.64.165[.]10` |
| **First Seen** | 2026-03-13 12:49 |
| **Last Seen** | 2026-03-13 12:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 12:49:57` | `cowrie.session.connect` |
| `2026-03-13 12:49:57` | `cowrie.client.version` |
| `2026-03-13 12:49:57` | `cowrie.client.kex` |
| `2026-03-13 12:49:58` | `cowrie.login.success` |
| `2026-03-13 12:49:59` | `cowrie.session.params` |
| `2026-03-13 12:49:59` | `cowrie.command.input` |
| `2026-03-13 12:49:59` | `cowrie.command.input` |
| `2026-03-13 12:49:59` | `cowrie.command.input` |
| `2026-03-13 12:49:59` | `cowrie.command.input` |
| `2026-03-13 12:50:00` | `cowrie.log.closed` |
| `2026-03-13 12:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.165[.]10` to AbuseIPDB if not already reported
- [ ] Block `170.64.165[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0052d36dd8

| Field | Detail |
|---|---|
| **Source IP** | `170.64.165[.]10` |
| **First Seen** | 2026-03-13 12:50 |
| **Last Seen** | 2026-03-13 12:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-13 12:50:51` | `cowrie.session.connect` |
| `2026-03-13 12:50:51` | `cowrie.client.version` |
| `2026-03-13 12:50:51` | `cowrie.client.kex` |
| `2026-03-13 12:50:53` | `cowrie.login.success` |
| `2026-03-13 12:50:54` | `cowrie.session.params` |
| `2026-03-13 12:50:54` | `cowrie.command.input` |
| `2026-03-13 12:50:54` | `cowrie.command.input` |
| `2026-03-13 12:50:54` | `cowrie.command.input` |
| `2026-03-13 12:50:54` | `cowrie.command.input` |
| `2026-03-13 12:50:55` | `cowrie.log.closed` |
| `2026-03-13 12:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.165[.]10` to AbuseIPDB if not already reported
- [ ] Block `170.64.165[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]68` | **25** | 2026-03-13 13:52 | 2026-03-13 13:57 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `101.52.130[.]122` | **12** | 2026-03-13 15:40 | 2026-03-13 15:50 | 20m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.33[.]21` | **10** | 2026-03-13 19:40 | 2026-03-13 20:09 | 16m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.143.162[.]210` | **7** | 2026-03-13 03:03 | 2026-03-13 03:11 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `36.134.147[.]79` | **6** | 2026-03-13 16:23 | 2026-03-13 16:36 | 10m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.64.165[.]10` | **3** | 2026-03-13 12:45 | 2026-03-13 12:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `122.166.49[.]42` | **2** | 2026-03-13 15:38 | 2026-03-13 15:43 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `34.14.59[.]194` | **2** | 2026-03-13 07:55 | 2026-03-13 07:56 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.117[.]42` | 1 | 2026-03-13 20:28 | 2026-03-13 20:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.32.139[.]197` | 1 | 2026-03-13 17:36 | 2026-03-13 17:37 | 49s | 0 | `T1592` | 🟢 LOW |
| `112.5.76[.]239` | 1 | 2026-03-13 00:07 | 2026-03-13 00:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.219.244[.]155` | 1 | 2026-03-13 10:10 | 2026-03-13 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.249.103[.]89` | 1 | 2026-03-13 18:49 | 2026-03-13 18:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.26.153[.]102` | 1 | 2026-03-13 02:46 | 2026-03-13 02:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-13 00:38 | 2026-03-13 00:39 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `121.228.75[.]232` | 1 | 2026-03-13 04:18 | 2026-03-13 04:18 | 12s | 0 | `T1592` | 🟢 LOW |
| `170.83.126[.]161` | 1 | 2026-03-13 20:08 | 2026-03-13 20:09 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.183.10[.]183` | 1 | 2026-03-13 19:44 | 2026-03-13 19:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `179.125.104[.]245` | 1 | 2026-03-13 08:39 | 2026-03-13 08:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.251.1[.]179` | 1 | 2026-03-13 02:09 | 2026-03-13 02:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.215.82[.]114` | 1 | 2026-03-13 17:36 | 2026-03-13 17:36 | 31s | 0 | `T1592` | 🟢 LOW |
| `220.189.253[.]198` | 1 | 2026-03-13 18:49 | 2026-03-13 18:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]59` | 1 | 2026-03-13 05:21 | 2026-03-13 05:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.98.218[.]97` | 1 | 2026-03-13 07:52 | 2026-03-13 07:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `67.43.243[.]158` | 1 | 2026-03-13 18:59 | 2026-03-13 19:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `85.140.44[.]96` | 1 | 2026-03-13 13:30 | 2026-03-13 13:30 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (3 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `67.43.243[.]158` | US | Fidelity Communication International Inc. | **100** ⚠️ | 3 |
| `175.183.10[.]183` | TW | New Century InfoComm Tech. Co., Ltd. | **100** ⚠️ | 15 |
| `121.228.75[.]232` | CN | CHINANET jiangsu province network | **100** ⚠️ | 4 |
| `186.251.1[.]179` | BR | OnLine Assis Telecomunicações Ltda-EPP | **100** ⚠️ | 0 |
| `223.123.43[.]68` | PK | CMPak Limited | **100** ⚠️ | 35 |
| `49.124.153[.]59` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 13 |
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `85.140.44[.]96` | RU | MTS PJSC | **100** ⚠️ | 9 |
| `190.215.82[.]114` | CL | Gtd Internet S.A. | **100** ⚠️ | 14 |
| `179.125.104[.]245` | BR | RB TELECOM | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | — |
| [T1105](https://attack.mitre.org/techniques/T1105) | — |

---

## 🔕 False Positive Summary (571 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 554 |
| AbuseIPDB score 13 below threshold 25 | 7 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 662 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 222 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 571 filtered (86.2%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 6 priority case(s) shown individually · 26 recon entry/entries in table (8 group(s) consolidating 67 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.1 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-13T20:32:04Z_
