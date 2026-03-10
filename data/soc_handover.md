# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-10 |
| **Generated At** | 2026-03-10T12:56:04Z |
| **Shift Time** | 12:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **544** |
| Confirmed Threats | **308** |
| False Positives Filtered | **236** (43.4%) |
| Unique Attacker IPs | **112** |
| Countries of Origin | **28** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **503** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ebcfb3c48891

| Field | Detail |
|---|---|
| **Source IP** | `103.153.190[.]105` |
| **First Seen** | 2026-03-10 00:05 |
| **Last Seen** | 2026-03-10 00:06 |
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
| `2026-03-10 00:05:57` | `cowrie.session.connect` |
| `2026-03-10 00:05:57` | `cowrie.client.version` |
| `2026-03-10 00:05:57` | `cowrie.client.kex` |
| `2026-03-10 00:05:58` | `cowrie.login.success` |
| `2026-03-10 00:05:58` | `cowrie.session.params` |
| `2026-03-10 00:05:58` | `cowrie.command.input` |
| `2026-03-10 00:05:58` | `cowrie.command.failed` |
| `2026-03-10 00:05:58` | `cowrie.log.closed` |
| `2026-03-10 00:05:59` | `cowrie.session.params` |
| `2026-03-10 00:05:59` | `cowrie.command.input` |
| `2026-03-10 00:05:59` | `cowrie.session.file_download` |
| `2026-03-10 00:05:59` | `cowrie.log.closed` |
| `2026-03-10 00:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.190[.]105` to AbuseIPDB if not already reported
- [ ] Block `103.153.190[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a2597cfe7f

| Field | Detail |
|---|---|
| **Source IP** | `103.153.190[.]105` |
| **First Seen** | 2026-03-10 00:06 |
| **Last Seen** | 2026-03-10 00:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 00:06:02` | `cowrie.session.connect` |
| `2026-03-10 00:06:02` | `cowrie.client.version` |
| `2026-03-10 00:06:02` | `cowrie.client.kex` |
| `2026-03-10 00:06:03` | `cowrie.login.success` |
| `2026-03-10 00:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.190[.]105` to AbuseIPDB if not already reported
- [ ] Block `103.153.190[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ec724ef7cd

| Field | Detail |
|---|---|
| **Source IP** | `167.71.0[.]105` |
| **First Seen** | 2026-03-10 00:17 |
| **Last Seen** | 2026-03-10 00:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 00:17:23` | `cowrie.session.connect` |
| `2026-03-10 00:17:23` | `cowrie.client.version` |
| `2026-03-10 00:17:23` | `cowrie.client.kex` |
| `2026-03-10 00:17:25` | `cowrie.login.success` |
| `2026-03-10 00:17:26` | `cowrie.session.params` |
| `2026-03-10 00:17:26` | `cowrie.command.input` |
| `2026-03-10 00:17:26` | `cowrie.command.input` |
| `2026-03-10 00:17:26` | `cowrie.command.input` |
| `2026-03-10 00:17:26` | `cowrie.command.input` |
| `2026-03-10 00:17:26` | `cowrie.log.closed` |
| `2026-03-10 00:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.0[.]105` to AbuseIPDB if not already reported
- [ ] Block `167.71.0[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-304beeb3aafd

| Field | Detail |
|---|---|
| **Source IP** | `167.71.0[.]105` |
| **First Seen** | 2026-03-10 00:18 |
| **Last Seen** | 2026-03-10 00:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 00:18:11` | `cowrie.session.connect` |
| `2026-03-10 00:18:11` | `cowrie.client.version` |
| `2026-03-10 00:18:11` | `cowrie.client.kex` |
| `2026-03-10 00:18:13` | `cowrie.login.success` |
| `2026-03-10 00:18:14` | `cowrie.session.params` |
| `2026-03-10 00:18:14` | `cowrie.command.input` |
| `2026-03-10 00:18:14` | `cowrie.command.input` |
| `2026-03-10 00:18:14` | `cowrie.command.input` |
| `2026-03-10 00:18:14` | `cowrie.command.input` |
| `2026-03-10 00:18:14` | `cowrie.log.closed` |
| `2026-03-10 00:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.0[.]105` to AbuseIPDB if not already reported
- [ ] Block `167.71.0[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc29073fe153

| Field | Detail |
|---|---|
| **Source IP** | `167.71.0[.]105` |
| **First Seen** | 2026-03-10 00:18 |
| **Last Seen** | 2026-03-10 00:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 00:18:53` | `cowrie.session.connect` |
| `2026-03-10 00:18:53` | `cowrie.client.version` |
| `2026-03-10 00:18:53` | `cowrie.client.kex` |
| `2026-03-10 00:18:54` | `cowrie.login.success` |
| `2026-03-10 00:18:55` | `cowrie.session.params` |
| `2026-03-10 00:18:55` | `cowrie.command.input` |
| `2026-03-10 00:18:55` | `cowrie.command.input` |
| `2026-03-10 00:18:55` | `cowrie.command.input` |
| `2026-03-10 00:18:55` | `cowrie.command.input` |
| `2026-03-10 00:18:55` | `cowrie.log.closed` |
| `2026-03-10 00:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.71.0[.]105` to AbuseIPDB if not already reported
- [ ] Block `167.71.0[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1d6039a2534

| Field | Detail |
|---|---|
| **Source IP** | `159.223.228[.]242` |
| **First Seen** | 2026-03-10 01:06 |
| **Last Seen** | 2026-03-10 01:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 01:06:16` | `cowrie.session.connect` |
| `2026-03-10 01:06:16` | `cowrie.client.version` |
| `2026-03-10 01:06:16` | `cowrie.client.kex` |
| `2026-03-10 01:06:18` | `cowrie.login.success` |
| `2026-03-10 01:06:19` | `cowrie.session.params` |
| `2026-03-10 01:06:19` | `cowrie.command.input` |
| `2026-03-10 01:06:19` | `cowrie.command.input` |
| `2026-03-10 01:06:19` | `cowrie.command.input` |
| `2026-03-10 01:06:19` | `cowrie.command.input` |
| `2026-03-10 01:06:20` | `cowrie.log.closed` |
| `2026-03-10 01:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.228[.]242` to AbuseIPDB if not already reported
- [ ] Block `159.223.228[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bccb87ea7f1

| Field | Detail |
|---|---|
| **Source IP** | `159.223.228[.]242` |
| **First Seen** | 2026-03-10 01:07 |
| **Last Seen** | 2026-03-10 01:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 01:07:15` | `cowrie.session.connect` |
| `2026-03-10 01:07:15` | `cowrie.client.version` |
| `2026-03-10 01:07:15` | `cowrie.client.kex` |
| `2026-03-10 01:07:17` | `cowrie.login.success` |
| `2026-03-10 01:07:18` | `cowrie.session.params` |
| `2026-03-10 01:07:18` | `cowrie.command.input` |
| `2026-03-10 01:07:18` | `cowrie.command.input` |
| `2026-03-10 01:07:18` | `cowrie.command.input` |
| `2026-03-10 01:07:18` | `cowrie.command.input` |
| `2026-03-10 01:07:19` | `cowrie.log.closed` |
| `2026-03-10 01:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.228[.]242` to AbuseIPDB if not already reported
- [ ] Block `159.223.228[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9c57560548

| Field | Detail |
|---|---|
| **Source IP** | `159.223.228[.]242` |
| **First Seen** | 2026-03-10 01:08 |
| **Last Seen** | 2026-03-10 01:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 01:08:12` | `cowrie.session.connect` |
| `2026-03-10 01:08:12` | `cowrie.client.version` |
| `2026-03-10 01:08:12` | `cowrie.client.kex` |
| `2026-03-10 01:08:14` | `cowrie.login.success` |
| `2026-03-10 01:08:15` | `cowrie.session.params` |
| `2026-03-10 01:08:15` | `cowrie.command.input` |
| `2026-03-10 01:08:15` | `cowrie.command.input` |
| `2026-03-10 01:08:15` | `cowrie.command.input` |
| `2026-03-10 01:08:15` | `cowrie.command.input` |
| `2026-03-10 01:08:16` | `cowrie.log.closed` |
| `2026-03-10 01:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.228[.]242` to AbuseIPDB if not already reported
- [ ] Block `159.223.228[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ad9f98d70a

| Field | Detail |
|---|---|
| **Source IP** | `159.223.228[.]242` |
| **First Seen** | 2026-03-10 01:09 |
| **Last Seen** | 2026-03-10 01:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 01:09:06` | `cowrie.session.connect` |
| `2026-03-10 01:09:06` | `cowrie.client.version` |
| `2026-03-10 01:09:06` | `cowrie.client.kex` |
| `2026-03-10 01:09:07` | `cowrie.login.success` |
| `2026-03-10 01:09:08` | `cowrie.session.params` |
| `2026-03-10 01:09:08` | `cowrie.command.input` |
| `2026-03-10 01:09:08` | `cowrie.command.input` |
| `2026-03-10 01:09:08` | `cowrie.command.input` |
| `2026-03-10 01:09:08` | `cowrie.command.input` |
| `2026-03-10 01:09:09` | `cowrie.log.closed` |
| `2026-03-10 01:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.228[.]242` to AbuseIPDB if not already reported
- [ ] Block `159.223.228[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc2b78c840b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.228[.]242` |
| **First Seen** | 2026-03-10 01:09 |
| **Last Seen** | 2026-03-10 01:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 01:09:57` | `cowrie.session.connect` |
| `2026-03-10 01:09:57` | `cowrie.client.version` |
| `2026-03-10 01:09:57` | `cowrie.client.kex` |
| `2026-03-10 01:09:59` | `cowrie.login.success` |
| `2026-03-10 01:10:00` | `cowrie.session.params` |
| `2026-03-10 01:10:00` | `cowrie.command.input` |
| `2026-03-10 01:10:00` | `cowrie.command.input` |
| `2026-03-10 01:10:00` | `cowrie.command.input` |
| `2026-03-10 01:10:00` | `cowrie.command.input` |
| `2026-03-10 01:10:00` | `cowrie.log.closed` |
| `2026-03-10 01:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.228[.]242` to AbuseIPDB if not already reported
- [ ] Block `159.223.228[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3948169aa78a

| Field | Detail |
|---|---|
| **Source IP** | `212.72.14[.]244` |
| **First Seen** | 2026-03-10 02:49 |
| **Last Seen** | 2026-03-10 02:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 02:49:32` | `cowrie.session.connect` |
| `2026-03-10 02:49:32` | `cowrie.client.version` |
| `2026-03-10 02:49:32` | `cowrie.client.kex` |
| `2026-03-10 02:49:33` | `cowrie.login.success` |
| `2026-03-10 02:49:33` | `cowrie.session.params` |
| `2026-03-10 02:49:33` | `cowrie.command.input` |
| `2026-03-10 02:49:33` | `cowrie.log.closed` |
| `2026-03-10 02:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.72.14[.]244` to AbuseIPDB if not already reported
- [ ] Block `212.72.14[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d31d044e57c4

| Field | Detail |
|---|---|
| **Source IP** | `101.47.142[.]2` |
| **First Seen** | 2026-03-10 03:30 |
| **Last Seen** | 2026-03-10 03:31 |
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
| `2026-03-10 03:30:59` | `cowrie.session.connect` |
| `2026-03-10 03:30:59` | `cowrie.client.version` |
| `2026-03-10 03:30:59` | `cowrie.client.kex` |
| `2026-03-10 03:31:00` | `cowrie.login.success` |
| `2026-03-10 03:31:01` | `cowrie.session.params` |
| `2026-03-10 03:31:01` | `cowrie.command.input` |
| `2026-03-10 03:31:01` | `cowrie.command.failed` |
| `2026-03-10 03:31:01` | `cowrie.log.closed` |
| `2026-03-10 03:31:01` | `cowrie.session.params` |
| `2026-03-10 03:31:01` | `cowrie.command.input` |
| `2026-03-10 03:31:01` | `cowrie.session.file_download` |
| `2026-03-10 03:31:01` | `cowrie.log.closed` |
| `2026-03-10 03:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.142[.]2` to AbuseIPDB if not already reported
- [ ] Block `101.47.142[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0848e469e293

| Field | Detail |
|---|---|
| **Source IP** | `101.47.142[.]2` |
| **First Seen** | 2026-03-10 03:31 |
| **Last Seen** | 2026-03-10 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 03:31:07` | `cowrie.session.connect` |
| `2026-03-10 03:31:07` | `cowrie.client.version` |
| `2026-03-10 03:31:07` | `cowrie.client.kex` |
| `2026-03-10 03:31:08` | `cowrie.login.success` |
| `2026-03-10 03:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.142[.]2` to AbuseIPDB if not already reported
- [ ] Block `101.47.142[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc49e3fc8ea

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-03-10 05:17 |
| **Last Seen** | 2026-03-10 05:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 05:17:51` | `cowrie.session.connect` |
| `2026-03-10 05:17:51` | `cowrie.client.version` |
| `2026-03-10 05:17:52` | `cowrie.client.kex` |
| `2026-03-10 05:17:52` | `cowrie.login.success` |
| `2026-03-10 05:17:52` | `cowrie.session.params` |
| `2026-03-10 05:17:52` | `cowrie.command.input` |
| `2026-03-10 05:17:52` | `cowrie.command.failed` |
| `2026-03-10 05:17:53` | `cowrie.log.closed` |
| `2026-03-10 05:17:53` | `cowrie.session.params` |
| `2026-03-10 05:17:53` | `cowrie.command.input` |
| `2026-03-10 05:17:53` | `cowrie.session.file_download` |
| `2026-03-10 05:17:53` | `cowrie.log.closed` |
| `2026-03-10 05:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8b28c2e9df

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-03-10 05:17 |
| **Last Seen** | 2026-03-10 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 05:17:55` | `cowrie.session.connect` |
| `2026-03-10 05:17:55` | `cowrie.client.version` |
| `2026-03-10 05:17:55` | `cowrie.client.kex` |
| `2026-03-10 05:17:56` | `cowrie.login.success` |
| `2026-03-10 05:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-562a06e5ba6a

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-03-10 05:35 |
| **Last Seen** | 2026-03-10 05:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 05:35:33` | `cowrie.session.connect` |
| `2026-03-10 05:35:33` | `cowrie.client.version` |
| `2026-03-10 05:35:33` | `cowrie.client.kex` |
| `2026-03-10 05:35:33` | `cowrie.login.success` |
| `2026-03-10 05:35:34` | `cowrie.session.params` |
| `2026-03-10 05:35:34` | `cowrie.command.input` |
| `2026-03-10 05:35:34` | `cowrie.command.failed` |
| `2026-03-10 05:35:34` | `cowrie.log.closed` |
| `2026-03-10 05:35:34` | `cowrie.session.params` |
| `2026-03-10 05:35:34` | `cowrie.command.input` |
| `2026-03-10 05:35:34` | `cowrie.session.file_download` |
| `2026-03-10 05:35:34` | `cowrie.log.closed` |
| `2026-03-10 05:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89b6954b1da1

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-03-10 05:35 |
| **Last Seen** | 2026-03-10 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 05:35:36` | `cowrie.session.connect` |
| `2026-03-10 05:35:36` | `cowrie.client.version` |
| `2026-03-10 05:35:36` | `cowrie.client.kex` |
| `2026-03-10 05:35:37` | `cowrie.login.success` |
| `2026-03-10 05:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09739496aaea

| Field | Detail |
|---|---|
| **Source IP** | `8.209.213[.]180` |
| **First Seen** | 2026-03-10 06:07 |
| **Last Seen** | 2026-03-10 06:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:07:32` | `cowrie.session.connect` |
| `2026-03-10 06:07:32` | `cowrie.client.version` |
| `2026-03-10 06:07:32` | `cowrie.client.kex` |
| `2026-03-10 06:07:33` | `cowrie.login.success` |
| `2026-03-10 06:07:34` | `cowrie.session.params` |
| `2026-03-10 06:07:34` | `cowrie.command.input` |
| `2026-03-10 06:07:34` | `cowrie.command.failed` |
| `2026-03-10 06:07:34` | `cowrie.log.closed` |
| `2026-03-10 06:07:34` | `cowrie.session.params` |
| `2026-03-10 06:07:34` | `cowrie.command.input` |
| `2026-03-10 06:07:35` | `cowrie.session.file_download` |
| `2026-03-10 06:07:35` | `cowrie.log.closed` |
| `2026-03-10 06:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.209.213[.]180` to AbuseIPDB if not already reported
- [ ] Block `8.209.213[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9818201a4d

| Field | Detail |
|---|---|
| **Source IP** | `8.209.213[.]180` |
| **First Seen** | 2026-03-10 06:07 |
| **Last Seen** | 2026-03-10 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:07:38` | `cowrie.session.connect` |
| `2026-03-10 06:07:38` | `cowrie.client.version` |
| `2026-03-10 06:07:38` | `cowrie.client.kex` |
| `2026-03-10 06:07:39` | `cowrie.login.success` |
| `2026-03-10 06:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.209.213[.]180` to AbuseIPDB if not already reported
- [ ] Block `8.209.213[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27aa6cd5c7e4

| Field | Detail |
|---|---|
| **Source IP** | `134.199.152[.]21` |
| **First Seen** | 2026-03-10 06:15 |
| **Last Seen** | 2026-03-10 06:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:15:03` | `cowrie.session.connect` |
| `2026-03-10 06:15:03` | `cowrie.client.version` |
| `2026-03-10 06:15:03` | `cowrie.client.kex` |
| `2026-03-10 06:15:05` | `cowrie.login.success` |
| `2026-03-10 06:15:05` | `cowrie.session.params` |
| `2026-03-10 06:15:05` | `cowrie.command.input` |
| `2026-03-10 06:15:06` | `cowrie.log.closed` |
| `2026-03-10 06:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.152[.]21` to AbuseIPDB if not already reported
- [ ] Block `134.199.152[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e551d7498cf3

| Field | Detail |
|---|---|
| **Source IP** | `134.199.152[.]21` |
| **First Seen** | 2026-03-10 06:15 |
| **Last Seen** | 2026-03-10 06:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:15:57` | `cowrie.session.connect` |
| `2026-03-10 06:15:57` | `cowrie.client.version` |
| `2026-03-10 06:15:58` | `cowrie.client.kex` |
| `2026-03-10 06:15:58` | `cowrie.login.success` |
| `2026-03-10 06:15:59` | `cowrie.session.params` |
| `2026-03-10 06:15:59` | `cowrie.command.input` |
| `2026-03-10 06:15:59` | `cowrie.log.closed` |
| `2026-03-10 06:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.152[.]21` to AbuseIPDB if not already reported
- [ ] Block `134.199.152[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcac42de633e

| Field | Detail |
|---|---|
| **Source IP** | `134.199.152[.]21` |
| **First Seen** | 2026-03-10 06:16 |
| **Last Seen** | 2026-03-10 06:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:16:28` | `cowrie.session.connect` |
| `2026-03-10 06:16:28` | `cowrie.client.version` |
| `2026-03-10 06:16:28` | `cowrie.client.kex` |
| `2026-03-10 06:16:29` | `cowrie.login.success` |
| `2026-03-10 06:16:30` | `cowrie.session.params` |
| `2026-03-10 06:16:30` | `cowrie.command.input` |
| `2026-03-10 06:16:30` | `cowrie.log.closed` |
| `2026-03-10 06:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.152[.]21` to AbuseIPDB if not already reported
- [ ] Block `134.199.152[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de70eec6564

| Field | Detail |
|---|---|
| **Source IP** | `134.199.152[.]21` |
| **First Seen** | 2026-03-10 06:16 |
| **Last Seen** | 2026-03-10 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:16:39` | `cowrie.session.connect` |
| `2026-03-10 06:16:39` | `cowrie.client.version` |
| `2026-03-10 06:16:39` | `cowrie.client.kex` |
| `2026-03-10 06:16:40` | `cowrie.login.success` |
| `2026-03-10 06:16:40` | `cowrie.session.params` |
| `2026-03-10 06:16:40` | `cowrie.command.input` |
| `2026-03-10 06:16:40` | `cowrie.log.closed` |
| `2026-03-10 06:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.152[.]21` to AbuseIPDB if not already reported
- [ ] Block `134.199.152[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bb6273fae7

| Field | Detail |
|---|---|
| **Source IP** | `134.199.152[.]21` |
| **First Seen** | 2026-03-10 06:19 |
| **Last Seen** | 2026-03-10 06:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 06:19:08` | `cowrie.session.connect` |
| `2026-03-10 06:19:08` | `cowrie.client.version` |
| `2026-03-10 06:19:08` | `cowrie.client.kex` |
| `2026-03-10 06:19:09` | `cowrie.login.success` |
| `2026-03-10 06:19:09` | `cowrie.session.params` |
| `2026-03-10 06:19:09` | `cowrie.command.input` |
| `2026-03-10 06:19:10` | `cowrie.log.closed` |
| `2026-03-10 06:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.152[.]21` to AbuseIPDB if not already reported
- [ ] Block `134.199.152[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e8beaa4b8cf

| Field | Detail |
|---|---|
| **Source IP** | `106.75.162[.]193` |
| **First Seen** | 2026-03-10 07:39 |
| **Last Seen** | 2026-03-10 07:45 |
| **Session Duration** | 360s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 07:39:18` | `cowrie.session.connect` |
| `2026-03-10 07:40:18` | `cowrie.client.version` |
| `2026-03-10 07:40:18` | `cowrie.client.kex` |
| `2026-03-10 07:40:19` | `cowrie.login.success` |
| `2026-03-10 07:45:19` | `cowrie.session.file_upload` |
| `2026-03-10 07:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.162[.]193` to AbuseIPDB if not already reported
- [ ] Block `106.75.162[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6640ec440473

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]111` |
| **First Seen** | 2026-03-10 09:35 |
| **Last Seen** | 2026-03-10 09:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 09:35:28` | `cowrie.session.connect` |
| `2026-03-10 09:35:28` | `cowrie.client.version` |
| `2026-03-10 09:35:28` | `cowrie.client.kex` |
| `2026-03-10 09:35:28` | `cowrie.login.success` |
| `2026-03-10 09:35:29` | `cowrie.session.params` |
| `2026-03-10 09:35:29` | `cowrie.command.input` |
| `2026-03-10 09:35:29` | `cowrie.command.input` |
| `2026-03-10 09:35:29` | `cowrie.command.input` |
| `2026-03-10 09:35:29` | `cowrie.command.input` |
| `2026-03-10 09:35:29` | `cowrie.log.closed` |
| `2026-03-10 09:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]111` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ce02e6bff9

| Field | Detail |
|---|---|
| **Source IP** | `134.209.186[.]111` |
| **First Seen** | 2026-03-10 09:36 |
| **Last Seen** | 2026-03-10 09:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-10 09:36:43` | `cowrie.session.connect` |
| `2026-03-10 09:36:43` | `cowrie.client.version` |
| `2026-03-10 09:36:43` | `cowrie.client.kex` |
| `2026-03-10 09:36:44` | `cowrie.login.success` |
| `2026-03-10 09:36:45` | `cowrie.session.params` |
| `2026-03-10 09:36:45` | `cowrie.command.input` |
| `2026-03-10 09:36:45` | `cowrie.command.input` |
| `2026-03-10 09:36:45` | `cowrie.command.input` |
| `2026-03-10 09:36:45` | `cowrie.command.input` |
| `2026-03-10 09:36:45` | `cowrie.log.closed` |
| `2026-03-10 09:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.209.186[.]111` to AbuseIPDB if not already reported
- [ ] Block `134.209.186[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.135.170[.]0` | **25** | 2026-03-10 11:57 | 2026-03-10 12:03 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `216.180.127[.]201` | **22** | 2026-03-10 00:04 | 2026-03-10 02:31 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.88.240[.]151` | **14** | 2026-03-10 06:26 | 2026-03-10 06:50 | 22m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.125[.]241` | **11** | 2026-03-10 02:14 | 2026-03-10 02:36 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | **11** | 2026-03-10 00:03 | 2026-03-10 00:19 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.133.166[.]150` | **11** | 2026-03-10 02:07 | 2026-03-10 02:16 | 16m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.61[.]170` | **11** | 2026-03-10 05:14 | 2026-03-10 05:37 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.112[.]118` | **11** | 2026-03-10 06:47 | 2026-03-10 06:59 | 15m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.26[.]185` | **11** | 2026-03-10 02:19 | 2026-03-10 02:33 | 14m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.214.209[.]153` | **11** | 2026-03-10 11:00 | 2026-03-10 11:22 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.98[.]88` | **11** | 2026-03-10 01:04 | 2026-03-10 01:14 | 13m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.237.78[.]117` | **11** | 2026-03-10 02:37 | 2026-03-10 02:54 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.249.103[.]89` | **10** | 2026-03-10 05:58 | 2026-03-10 06:14 | 14m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.142[.]2` | **9** | 2026-03-10 03:08 | 2026-03-10 03:47 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `103.153.190[.]105` | **7** | 2026-03-10 00:02 | 2026-03-10 00:24 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **7** | 2026-03-10 05:22 | 2026-03-10 05:33 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `101.126.143[.]178` | **6** | 2026-03-10 00:00 | 2026-03-10 00:08 | 9m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.232.44[.]56` | **6** | 2026-03-10 08:11 | 2026-03-10 08:15 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `3.130.168[.]2` | **6** | 2026-03-10 08:54 | 2026-03-10 09:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `167.71.0[.]105` | **5** | 2026-03-10 00:13 | 2026-03-10 00:19 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `212.72.14[.]244` | **5** | 2026-03-10 02:43 | 2026-03-10 02:50 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `34.78.39[.]23` | **4** | 2026-03-10 09:29 | 2026-03-10 09:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.141.153[.]201` | **3** | 2026-03-10 10:15 | 2026-03-10 10:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.144.21[.]210` | **3** | 2026-03-10 03:29 | 2026-03-10 03:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.198.1[.]136` | **3** | 2026-03-10 05:15 | 2026-03-10 05:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `159.223.228[.]242` | **2** | 2026-03-10 01:04 | 2026-03-10 01:05 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.101.184[.]85` | **2** | 2026-03-10 00:33 | 2026-03-10 00:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.79.252[.]163` | **2** | 2026-03-10 09:29 | 2026-03-10 09:29 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-10 09:29 | 2026-03-10 09:33 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.71.37[.]214` | 1 | 2026-03-10 02:27 | 2026-03-10 02:27 | 14s | 0 | `T1592` | 🟢 LOW |
| `101.71.37[.]90` | 1 | 2026-03-10 00:48 | 2026-03-10 00:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.1.127[.]182` | 1 | 2026-03-10 05:37 | 2026-03-10 05:37 | 17s | 0 | `T1592` | 🟢 LOW |
| `106.75.162[.]193` | 1 | 2026-03-10 07:37 | 2026-03-10 07:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.173.82[.]99` | 1 | 2026-03-10 03:14 | 2026-03-10 03:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `110.37.79[.]235` | 1 | 2026-03-10 11:21 | 2026-03-10 11:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `114.171.170[.]38` | 1 | 2026-03-10 06:40 | 2026-03-10 06:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.176.58[.]252` | 1 | 2026-03-10 12:15 | 2026-03-10 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.208[.]20` | 1 | 2026-03-10 06:00 | 2026-03-10 06:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.29[.]193` | 1 | 2026-03-10 05:59 | 2026-03-10 05:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.230.180[.]198` | 1 | 2026-03-10 02:11 | 2026-03-10 02:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.236[.]178` | 1 | 2026-03-10 03:20 | 2026-03-10 03:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-03-10 05:57 | 2026-03-10 05:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.55.242[.]50` | 1 | 2026-03-10 07:51 | 2026-03-10 07:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.161.149[.]104` | 1 | 2026-03-10 07:29 | 2026-03-10 07:29 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]29` | 1 | 2026-03-10 02:38 | 2026-03-10 02:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.237.28[.]235` | 1 | 2026-03-10 07:53 | 2026-03-10 07:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `162.243.162[.]30` | 1 | 2026-03-10 04:16 | 2026-03-10 04:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `162.83.243[.]81` | 1 | 2026-03-10 08:21 | 2026-03-10 08:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.32.195[.]85` | 1 | 2026-03-10 08:19 | 2026-03-10 08:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.100.198[.]252` | 1 | 2026-03-10 11:19 | 2026-03-10 11:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.177.50[.]106` | 1 | 2026-03-10 09:45 | 2026-03-10 09:45 | 17s | 0 | `T1592` | 🟢 LOW |
| `180.76.141[.]1` | 1 | 2026-03-10 03:07 | 2026-03-10 03:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.176[.]249` | 1 | 2026-03-10 11:11 | 2026-03-10 11:12 | 34s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-03-10 04:59 | 2026-03-10 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.112.105[.]97` | 1 | 2026-03-10 07:40 | 2026-03-10 07:40 | 31s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]246` | 1 | 2026-03-10 03:45 | 2026-03-10 03:45 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]39` | 1 | 2026-03-10 03:45 | 2026-03-10 03:45 | 1s | 0 | `T1592` | 🟢 LOW |
| `195.94.24[.]183` | 1 | 2026-03-10 02:16 | 2026-03-10 02:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.106.54[.]198` | 1 | 2026-03-10 03:08 | 2026-03-10 03:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.18.99[.]81` | 1 | 2026-03-10 03:03 | 2026-03-10 03:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-10 02:54 | 2026-03-10 02:55 | 38s | 0 | `T1592` | 🟢 LOW |
| `60.167.165[.]58` | 1 | 2026-03-10 07:48 | 2026-03-10 07:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.77.88[.]90` | 1 | 2026-03-10 04:14 | 2026-03-10 04:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `78.188.173[.]81` | 1 | 2026-03-10 02:12 | 2026-03-10 02:12 | 12s | 0 | `T1592` | 🟢 LOW |
| `87.121.84[.]78` | 1 | 2026-03-10 10:01 | 2026-03-10 10:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]111` | 1 | 2026-03-10 04:27 | 2026-03-10 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]205` | 1 | 2026-03-10 04:27 | 2026-03-10 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.48.24[.]181` | 1 | 2026-03-10 00:14 | 2026-03-10 00:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `167.71.0[.]105` | NL | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `159.223.228[.]242` | NL | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `116.176.58[.]252` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 4 |
| `91.144.21[.]210` | SY | Tarassul Inetnet Service Provider | **100** ⚠️ | 45 |
| `101.71.37[.]90` | CN | UNICOM ZheJiang Province Network | **100** ⚠️ | 2 |
| `113.88.240[.]151` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `151.237.28[.]235` | BG | PON.BG Ltd. | **100** ⚠️ | 16 |
| `91.230.168[.]111` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `223.18.99[.]81` | HK | HGC Global Communications Limited | **100** ⚠️ | 14 |

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

## 🔕 False Positive Summary (236 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 11 |
| AbuseIPDB score 16 below threshold 25 | 46 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 16 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 8 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 52 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 76 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 544 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 112 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 236 filtered (43.4%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 2 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 27 priority case(s) shown individually · 68 recon entry/entries in table (29 group(s) consolidating 242 session(s)).

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
_Report time: 2026-03-10T12:56:04Z_
