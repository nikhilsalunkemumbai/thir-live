# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-11 |
| **Generated At** | 2026-03-11T06:51:07Z |
| **Shift Time** | 06:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **81** |
| False Positives Filtered | **34** (29.6%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **16** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **103** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5e07f655cd08

| Field | Detail |
|---|---|
| **Source IP** | `83.111.76[.]194` |
| **First Seen** | 2026-03-11 01:54 |
| **Last Seen** | 2026-03-11 01:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 01:54:01` | `cowrie.session.connect` |
| `2026-03-11 01:54:01` | `cowrie.client.version` |
| `2026-03-11 01:54:01` | `cowrie.client.kex` |
| `2026-03-11 01:54:01` | `cowrie.login.success` |
| `2026-03-11 01:54:01` | `cowrie.session.params` |
| `2026-03-11 01:54:01` | `cowrie.command.input` |
| `2026-03-11 01:54:01` | `cowrie.command.failed` |
| `2026-03-11 01:54:01` | `cowrie.log.closed` |
| `2026-03-11 01:54:01` | `cowrie.session.params` |
| `2026-03-11 01:54:01` | `cowrie.command.input` |
| `2026-03-11 01:54:01` | `cowrie.session.file_download` |
| `2026-03-11 01:54:01` | `cowrie.log.closed` |
| `2026-03-11 01:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.111.76[.]194` to AbuseIPDB if not already reported
- [ ] Block `83.111.76[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301939f3fb4e

| Field | Detail |
|---|---|
| **Source IP** | `83.111.76[.]194` |
| **First Seen** | 2026-03-11 01:54 |
| **Last Seen** | 2026-03-11 01:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 01:54:03` | `cowrie.session.connect` |
| `2026-03-11 01:54:03` | `cowrie.client.version` |
| `2026-03-11 01:54:03` | `cowrie.client.kex` |
| `2026-03-11 01:54:03` | `cowrie.login.success` |
| `2026-03-11 01:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.111.76[.]194` to AbuseIPDB if not already reported
- [ ] Block `83.111.76[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca34b111b3cc

| Field | Detail |
|---|---|
| **Source IP** | `164.92.151[.]106` |
| **First Seen** | 2026-03-11 06:22 |
| **Last Seen** | 2026-03-11 06:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 06:22:54` | `cowrie.session.connect` |
| `2026-03-11 06:22:54` | `cowrie.client.version` |
| `2026-03-11 06:22:54` | `cowrie.client.kex` |
| `2026-03-11 06:22:57` | `cowrie.login.success` |
| `2026-03-11 06:22:59` | `cowrie.session.params` |
| `2026-03-11 06:22:59` | `cowrie.command.input` |
| `2026-03-11 06:22:59` | `cowrie.command.input` |
| `2026-03-11 06:22:59` | `cowrie.command.input` |
| `2026-03-11 06:22:59` | `cowrie.command.input` |
| `2026-03-11 06:23:01` | `cowrie.log.closed` |
| `2026-03-11 06:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.151[.]106` to AbuseIPDB if not already reported
- [ ] Block `164.92.151[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe492d7bfce

| Field | Detail |
|---|---|
| **Source IP** | `164.92.151[.]106` |
| **First Seen** | 2026-03-11 06:24 |
| **Last Seen** | 2026-03-11 06:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 06:24:15` | `cowrie.session.connect` |
| `2026-03-11 06:24:16` | `cowrie.client.version` |
| `2026-03-11 06:24:16` | `cowrie.client.kex` |
| `2026-03-11 06:24:21` | `cowrie.login.success` |
| `2026-03-11 06:24:22` | `cowrie.session.params` |
| `2026-03-11 06:24:22` | `cowrie.command.input` |
| `2026-03-11 06:24:22` | `cowrie.command.input` |
| `2026-03-11 06:24:22` | `cowrie.command.input` |
| `2026-03-11 06:24:22` | `cowrie.command.input` |
| `2026-03-11 06:24:23` | `cowrie.log.closed` |
| `2026-03-11 06:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.151[.]106` to AbuseIPDB if not already reported
- [ ] Block `164.92.151[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf90309ccaf6

| Field | Detail |
|---|---|
| **Source IP** | `164.92.151[.]106` |
| **First Seen** | 2026-03-11 06:25 |
| **Last Seen** | 2026-03-11 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 06:25:46` | `cowrie.session.connect` |
| `2026-03-11 06:25:46` | `cowrie.client.version` |
| `2026-03-11 06:25:46` | `cowrie.client.kex` |
| `2026-03-11 06:25:46` | `cowrie.login.success` |
| `2026-03-11 06:25:47` | `cowrie.session.params` |
| `2026-03-11 06:25:47` | `cowrie.command.input` |
| `2026-03-11 06:25:47` | `cowrie.command.input` |
| `2026-03-11 06:25:47` | `cowrie.command.input` |
| `2026-03-11 06:25:47` | `cowrie.command.input` |
| `2026-03-11 06:25:47` | `cowrie.log.closed` |
| `2026-03-11 06:25:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.151[.]106` to AbuseIPDB if not already reported
- [ ] Block `164.92.151[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]2` | **25** | 2026-03-11 04:38 | 2026-03-11 04:43 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `83.111.76[.]194` | **11** | 2026-03-11 01:49 | 2026-03-11 02:12 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.129.187[.]38` | **6** | 2026-03-11 06:21 | 2026-03-11 06:26 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `118.194.249[.]72` | **4** | 2026-03-11 00:27 | 2026-03-11 00:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.151[.]106` | **3** | 2026-03-11 06:20 | 2026-03-11 06:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.26.106[.]201` | **3** | 2026-03-11 03:36 | 2026-03-11 03:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.200.243[.]197` | **2** | 2026-03-11 03:20 | 2026-03-11 03:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.212.201[.]77` | **2** | 2026-03-11 04:41 | 2026-03-11 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]179` | **2** | 2026-03-11 04:33 | 2026-03-11 04:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | **2** | 2026-03-11 02:23 | 2026-03-11 02:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-11 01:49 | 2026-03-11 02:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]174` | **2** | 2026-03-11 06:27 | 2026-03-11 06:27 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `103.156.221[.]242` | 1 | 2026-03-11 06:05 | 2026-03-11 06:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `117.251.207[.]153` | 1 | 2026-03-11 01:37 | 2026-03-11 01:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-11 03:59 | 2026-03-11 04:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.149[.]244` | 1 | 2026-03-11 03:07 | 2026-03-11 03:07 | 8s | 0 | `T1592` | 🟢 LOW |
| `176.32.195[.]85` | 1 | 2026-03-11 05:04 | 2026-03-11 05:05 | 31s | 0 | `T1592` | 🟢 LOW |
| `211.250.12[.]75` | 1 | 2026-03-11 03:13 | 2026-03-11 03:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `24.193.152[.]228` | 1 | 2026-03-11 04:20 | 2026-03-11 04:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `37.34.242[.]99` | 1 | 2026-03-11 00:01 | 2026-03-11 00:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-11 06:09 | 2026-03-11 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `68.199.97[.]245` | 1 | 2026-03-11 01:14 | 2026-03-11 01:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-03-11 05:34 | 2026-03-11 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.215.35[.]25` | 1 | 2026-03-11 00:48 | 2026-03-11 00:49 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (2 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `172.212.201[.]77` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `45.156.129[.]179` | US | INAP-CHI-1 | **100** ⚠️ | 39 |
| `164.92.151[.]106` | NL | DigitalOcean, LLC | **100** ⚠️ | 37 |
| `24.193.152[.]228` | US | Charter Communications Inc | **100** ⚠️ | 2 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `68.199.97[.]245` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 7 |
| `45.79.181[.]94` | US | Linode | **100** ⚠️ | 50 |
| `176.32.195[.]85` | AM | Interactive TV LLC | **100** ⚠️ | 50 |
| `223.123.43[.]2` | PK | CMPak Limited | **100** ⚠️ | 31 |
| `66.228.53[.]174` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | — |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 17 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 7 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 115 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 41 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 34 filtered (29.6%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 2 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 5 priority case(s) shown individually · 24 recon entry/entries in table (12 group(s) consolidating 64 session(s)).

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
_Report time: 2026-03-11T06:51:07Z_
