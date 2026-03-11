# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-11 |
| **Generated At** | 2026-03-11T14:44:18Z |
| **Shift Time** | 14:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **436** |
| Confirmed Threats | **243** |
| False Positives Filtered | **193** (44.3%) |
| Unique Attacker IPs | **90** |
| Countries of Origin | **24** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **384** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (36)

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

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `94.26.106[.]200` | **48** | 2026-03-11 14:16 | 2026-03-11 14:40 | 0m | 42 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.43[.]2` | **25** | 2026-03-11 04:38 | 2026-03-11 04:43 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `94.26.106[.]201` | **17** | 2026-03-11 13:09 | 2026-03-11 13:23 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.208.69[.]47` | **11** | 2026-03-11 08:01 | 2026-03-11 08:25 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `83.111.76[.]194` | **11** | 2026-03-11 01:49 | 2026-03-11 02:12 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `134.199.145[.]236` | **9** | 2026-03-11 10:05 | 2026-03-11 10:13 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `192.109.200[.]220` | **8** | 2026-03-11 14:22 | 2026-03-11 14:22 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `165.22.201[.]90` | **6** | 2026-03-11 08:39 | 2026-03-11 08:45 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `3.129.187[.]38` | **6** | 2026-03-11 06:21 | 2026-03-11 06:26 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `118.194.249[.]72` | **4** | 2026-03-11 00:27 | 2026-03-11 00:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.59.45[.]9` | **3** | 2026-03-11 10:17 | 2026-03-11 10:23 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `164.92.151[.]106` | **3** | 2026-03-11 06:20 | 2026-03-11 06:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.191.69[.]170` | **3** | 2026-03-11 10:30 | 2026-03-11 10:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]201` | **3** | 2026-03-11 03:36 | 2026-03-11 03:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.200.243[.]197` | **2** | 2026-03-11 03:20 | 2026-03-11 03:20 | 0m | 0 | `T1592` | 🟢 LOW |
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
| `101.71.37[.]68` | 1 | 2026-03-11 10:41 | 2026-03-11 10:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.156.221[.]242` | 1 | 2026-03-11 06:05 | 2026-03-11 06:06 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.197.227[.]24` | 1 | 2026-03-11 09:36 | 2026-03-11 09:37 | 24s | 0 | `T1592` | 🟢 LOW |
| `117.251.207[.]153` | 1 | 2026-03-11 01:37 | 2026-03-11 01:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.196.26[.]161` | 1 | 2026-03-11 12:03 | 2026-03-11 12:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-11 03:59 | 2026-03-11 04:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-03-11 14:40 | 2026-03-11 14:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.149[.]244` | 1 | 2026-03-11 03:07 | 2026-03-11 03:07 | 8s | 0 | `T1592` | 🟢 LOW |
| `151.64.133[.]183` | 1 | 2026-03-11 11:12 | 2026-03-11 11:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `170.64.114[.]194` | 1 | 2026-03-11 07:59 | 2026-03-11 07:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-11 11:18 | 2026-03-11 11:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.32.195[.]85` | 1 | 2026-03-11 05:04 | 2026-03-11 05:05 | 31s | 0 | `T1592` | 🟢 LOW |
| `211.250.12[.]75` | 1 | 2026-03-11 03:13 | 2026-03-11 03:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `24.193.152[.]228` | 1 | 2026-03-11 04:20 | 2026-03-11 04:20 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.128.77[.]56` | 1 | 2026-03-11 14:39 | 2026-03-11 14:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.34.242[.]99` | 1 | 2026-03-11 00:01 | 2026-03-11 00:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `42.56.161[.]165` | 1 | 2026-03-11 14:16 | 2026-03-11 14:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.170.129[.]132` | 1 | 2026-03-11 13:10 | 2026-03-11 13:10 | 31s | 0 | `T1592` | 🟢 LOW |
| `49.142.74[.]66` | 1 | 2026-03-11 02:04 | 2026-03-11 02:04 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-11 06:09 | 2026-03-11 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `54.91.92[.]82` | 1 | 2026-03-11 12:56 | 2026-03-11 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.126.177[.]227` | 1 | 2026-03-11 09:20 | 2026-03-11 09:20 | 30s | 0 | `T1592` | 🟢 LOW |
| `61.78.98[.]181` | 1 | 2026-03-11 07:30 | 2026-03-11 07:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `68.199.97[.]245` | 1 | 2026-03-11 01:14 | 2026-03-11 01:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-03-11 05:34 | 2026-03-11 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.128.114[.]118` | 1 | 2026-03-11 10:26 | 2026-03-11 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.203.107[.]10` | 1 | 2026-03-11 09:52 | 2026-03-11 09:53 | 30s | 0 | `T1592` | 🟢 LOW |
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
| `164.92.151[.]106` | NL | DigitalOcean, LLC | **100** ⚠️ | 37 |
| `103.156.221[.]242` | ID | PT Gading Bhakti Utama | **100** ⚠️ | 14 |
| `223.123.43[.]2` | PK | CMPak Limited | **100** ⚠️ | 31 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `211.250.12[.]75` | KR | Korea Telecom | **100** ⚠️ | 18 |
| `69.164.217[.]245` | US | Linode | **100** ⚠️ | 50 |
| `37.34.242[.]99` | KW | ZAIN KW | **100** ⚠️ | 8 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `139.59.45[.]9` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `101.126.54[.]23` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

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

## 🔕 False Positive Summary (193 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 29 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 7 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 6 |
| AbuseIPDB score 4 below threshold 25 | 6 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 137 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 436 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 90 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 193 filtered (44.3%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 2 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 36 priority case(s) shown individually · 54 recon entry/entries in table (24 group(s) consolidating 177 session(s)).

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
_Report time: 2026-03-11T14:44:18Z_
