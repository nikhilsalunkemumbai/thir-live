# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-07 |
| **Generated At** | 2026-03-07T19:27:46Z |
| **Shift Time** | 19:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **260** |
| Confirmed Threats | **67** |
| False Positives Filtered | **193** (74.2%) |
| Unique Attacker IPs | **67** |
| Countries of Origin | **17** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **237** |

---

## 🚨 Confirmed Threats (67)

### 🔴 HIGH · IR-91073fd0fd5a

| Field | Detail |
|---|---|
| **Source IP** | `138.197.147.214` |
| **First Seen** | 2026-03-07T09:30:54.545747Z |
| **Last Seen** | 2026-03-07T09:31:00.055969Z |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:30:54` | `cowrie.session.connect` |
| `2026-03-07 09:30:54` | `cowrie.client.version` |
| `2026-03-07 09:30:54` | `cowrie.client.kex` |
| `2026-03-07 09:30:57` | `cowrie.login.success` |
| `2026-03-07 09:30:58` | `cowrie.session.params` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:58` | `cowrie.command.input` |
| `2026-03-07 09:30:59` | `cowrie.log.closed` |
| `2026-03-07 09:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.147.214` to AbuseIPDB if not already reported
- [ ] Block `138.197.147.214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b59fa4b68254

| Field | Detail |
|---|---|
| **Source IP** | `138.197.147.214` |
| **First Seen** | 2026-03-07T09:31:58.603021Z |
| **Last Seen** | 2026-03-07T09:32:03.647960Z |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:31:58` | `cowrie.session.connect` |
| `2026-03-07 09:31:58` | `cowrie.client.version` |
| `2026-03-07 09:31:58` | `cowrie.client.kex` |
| `2026-03-07 09:32:00` | `cowrie.login.success` |
| `2026-03-07 09:32:02` | `cowrie.session.params` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.command.input` |
| `2026-03-07 09:32:02` | `cowrie.log.closed` |
| `2026-03-07 09:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.147.214` to AbuseIPDB if not already reported
- [ ] Block `138.197.147.214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d13b9f971b

| Field | Detail |
|---|---|
| **Source IP** | `138.197.147.214` |
| **First Seen** | 2026-03-07T09:33:55.004920Z |
| **Last Seen** | 2026-03-07T09:33:59.886109Z |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:33:55` | `cowrie.session.connect` |
| `2026-03-07 09:33:55` | `cowrie.client.version` |
| `2026-03-07 09:33:55` | `cowrie.client.kex` |
| `2026-03-07 09:33:57` | `cowrie.login.success` |
| `2026-03-07 09:33:58` | `cowrie.session.params` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:58` | `cowrie.command.input` |
| `2026-03-07 09:33:59` | `cowrie.log.closed` |
| `2026-03-07 09:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.197.147.214` to AbuseIPDB if not already reported
- [ ] Block `138.197.147.214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbb2f52ce26f

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:40:27.728515Z |
| **Last Seen** | 2026-03-07T09:40:45.336637Z |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:40:27` | `cowrie.session.connect` |
| `2026-03-07 09:40:30` | `cowrie.client.version` |
| `2026-03-07 09:40:30` | `cowrie.client.kex` |
| `2026-03-07 09:40:39` | `cowrie.login.success` |
| `2026-03-07 09:40:43` | `cowrie.session.params` |
| `2026-03-07 09:40:43` | `cowrie.command.input` |
| `2026-03-07 09:40:45` | `cowrie.log.closed` |
| `2026-03-07 09:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f690cf3e1b4

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:41:24.925931Z |
| **Last Seen** | 2026-03-07T09:41:35.714943Z |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:41:24` | `cowrie.session.connect` |
| `2026-03-07 09:41:26` | `cowrie.client.version` |
| `2026-03-07 09:41:26` | `cowrie.client.kex` |
| `2026-03-07 09:41:31` | `cowrie.login.success` |
| `2026-03-07 09:41:34` | `cowrie.session.params` |
| `2026-03-07 09:41:34` | `cowrie.command.input` |
| `2026-03-07 09:41:35` | `cowrie.log.closed` |
| `2026-03-07 09:41:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa06358333c

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:42:23.486928Z |
| **Last Seen** | 2026-03-07T09:42:26.097479Z |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:42:23` | `cowrie.session.connect` |
| `2026-03-07 09:42:23` | `cowrie.client.version` |
| `2026-03-07 09:42:23` | `cowrie.client.kex` |
| `2026-03-07 09:42:25` | `cowrie.login.success` |
| `2026-03-07 09:42:25` | `cowrie.session.params` |
| `2026-03-07 09:42:25` | `cowrie.command.input` |
| `2026-03-07 09:42:26` | `cowrie.log.closed` |
| `2026-03-07 09:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101c87c2fd40

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:42:29.693685Z |
| **Last Seen** | 2026-03-07T09:42:31.192033Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:42:29` | `cowrie.session.connect` |
| `2026-03-07 09:42:29` | `cowrie.client.version` |
| `2026-03-07 09:42:29` | `cowrie.client.kex` |
| `2026-03-07 09:42:30` | `cowrie.login.success` |
| `2026-03-07 09:42:31` | `cowrie.session.params` |
| `2026-03-07 09:42:31` | `cowrie.command.input` |
| `2026-03-07 09:42:31` | `cowrie.log.closed` |
| `2026-03-07 09:42:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-cf9d9ef24a3e

| Field | Detail |
|---|---|
| **Source IP** | `209.14.28.89` |
| **First Seen** | 2026-03-07T09:44:10.828908Z |
| **Last Seen** | 2026-03-07T09:44:23.247609Z |
| **Session Duration** | 12s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:44:10` | `cowrie.session.connect` |
| `2026-03-07 09:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `209.14.28.89`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-6019563285e7

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:44:24.444041Z |
| **Last Seen** | 2026-03-07T09:44:25.709401Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:44:24` | `cowrie.session.connect` |
| `2026-03-07 09:44:24` | `cowrie.client.version` |
| `2026-03-07 09:44:24` | `cowrie.client.kex` |
| `2026-03-07 09:44:25` | `cowrie.login.success` |
| `2026-03-07 09:44:25` | `cowrie.session.params` |
| `2026-03-07 09:44:25` | `cowrie.command.input` |
| `2026-03-07 09:44:25` | `cowrie.log.closed` |
| `2026-03-07 09:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c4c5784fc88

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:44:52.090991Z |
| **Last Seen** | 2026-03-07T09:44:53.406568Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:44:52` | `cowrie.session.connect` |
| `2026-03-07 09:44:52` | `cowrie.client.version` |
| `2026-03-07 09:44:52` | `cowrie.client.kex` |
| `2026-03-07 09:44:52` | `cowrie.login.success` |
| `2026-03-07 09:44:53` | `cowrie.session.params` |
| `2026-03-07 09:44:53` | `cowrie.command.input` |
| `2026-03-07 09:44:53` | `cowrie.log.closed` |
| `2026-03-07 09:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee7590d67a4

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:46:21.899255Z |
| **Last Seen** | 2026-03-07T09:46:23.227602Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:46:21` | `cowrie.session.connect` |
| `2026-03-07 09:46:21` | `cowrie.client.version` |
| `2026-03-07 09:46:22` | `cowrie.client.kex` |
| `2026-03-07 09:46:22` | `cowrie.login.success` |
| `2026-03-07 09:46:23` | `cowrie.session.params` |
| `2026-03-07 09:46:23` | `cowrie.command.input` |
| `2026-03-07 09:46:23` | `cowrie.log.closed` |
| `2026-03-07 09:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58fc6e3598db

| Field | Detail |
|---|---|
| **Source IP** | `209.38.80.132` |
| **First Seen** | 2026-03-07T09:47:00.562239Z |
| **Last Seen** | 2026-03-07T09:47:02.200555Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:47:00` | `cowrie.session.connect` |
| `2026-03-07 09:47:00` | `cowrie.client.version` |
| `2026-03-07 09:47:00` | `cowrie.client.kex` |
| `2026-03-07 09:47:01` | `cowrie.login.success` |
| `2026-03-07 09:47:02` | `cowrie.session.params` |
| `2026-03-07 09:47:02` | `cowrie.command.input` |
| `2026-03-07 09:47:02` | `cowrie.log.closed` |
| `2026-03-07 09:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.80.132` to AbuseIPDB if not already reported
- [ ] Block `209.38.80.132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-66b032c87586

| Field | Detail |
|---|---|
| **Source IP** | `183.87.217.222` |
| **First Seen** | 2026-03-07T09:47:30.219688Z |
| **Last Seen** | 2026-03-07T09:47:41.777980Z |
| **Session Duration** | 11s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:47:30` | `cowrie.session.connect` |
| `2026-03-07 09:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `183.87.217.222`
- [ ] No immediate escalation required

### 🟢 LOW · IR-0139a0427319

| Field | Detail |
|---|---|
| **Source IP** | `183.87.217.222` |
| **First Seen** | 2026-03-07T09:47:47.768835Z |
| **Last Seen** | 2026-03-07T09:47:54.377783Z |
| **Session Duration** | 6s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 09:47:47` | `cowrie.session.connect` |
| `2026-03-07 09:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `183.87.217.222`
- [ ] No immediate escalation required

### 🟢 LOW · IR-9064cd8f303a

| Field | Detail |
|---|---|
| **Source IP** | `1.225.62.211` |
| **First Seen** | 2026-03-07T10:20:35.274181Z |
| **Last Seen** | 2026-03-07T10:21:06.062261Z |
| **Session Duration** | 30s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 10:20:35` | `cowrie.session.connect` |
| `2026-03-07 10:21:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `1.225.62.211`
- [ ] No immediate escalation required

### 🟢 LOW · IR-ed56b38c222d

| Field | Detail |
|---|---|
| **Source IP** | `129.146.81.203` |
| **First Seen** | 2026-03-07T10:52:49.225010Z |
| **Last Seen** | 2026-03-07T10:52:57.225379Z |
| **Session Duration** | 8s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 10:52:49` | `cowrie.session.connect` |
| `2026-03-07 10:52:49` | `cowrie.client.version` |
| `2026-03-07 10:52:49` | `cowrie.client.kex` |
| `2026-03-07 10:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `129.146.81.203`
- [ ] No immediate escalation required

### 🟢 LOW · IR-556c8e2a6520

| Field | Detail |
|---|---|
| **Source IP** | `176.32.195.85` |
| **First Seen** | 2026-03-07T10:54:57.072656Z |
| **Last Seen** | 2026-03-07T10:54:57.235615Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 10:54:57` | `cowrie.session.connect` |
| `2026-03-07 10:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `176.32.195.85`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-6b60b0e6e9a2

| Field | Detail |
|---|---|
| **Source IP** | `46.101.42.97` |
| **First Seen** | 2026-03-07T10:55:08.337899Z |
| **Last Seen** | 2026-03-07T10:55:14.552281Z |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 10:55:08` | `cowrie.session.connect` |
| `2026-03-07 10:55:08` | `cowrie.client.version` |
| `2026-03-07 10:55:08` | `cowrie.client.kex` |
| `2026-03-07 10:55:11` | `cowrie.login.success` |
| `2026-03-07 10:55:13` | `cowrie.session.params` |
| `2026-03-07 10:55:13` | `cowrie.command.input` |
| `2026-03-07 10:55:13` | `cowrie.command.input` |
| `2026-03-07 10:55:13` | `cowrie.command.input` |
| `2026-03-07 10:55:13` | `cowrie.command.input` |
| `2026-03-07 10:55:13` | `cowrie.log.closed` |
| `2026-03-07 10:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.42.97` to AbuseIPDB if not already reported
- [ ] Block `46.101.42.97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce769dfb6da2

| Field | Detail |
|---|---|
| **Source IP** | `46.101.42.97` |
| **First Seen** | 2026-03-07T10:56:25.074103Z |
| **Last Seen** | 2026-03-07T10:56:31.521501Z |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 10:56:25` | `cowrie.session.connect` |
| `2026-03-07 10:56:25` | `cowrie.client.version` |
| `2026-03-07 10:56:25` | `cowrie.client.kex` |
| `2026-03-07 10:56:27` | `cowrie.login.success` |
| `2026-03-07 10:56:29` | `cowrie.session.params` |
| `2026-03-07 10:56:29` | `cowrie.command.input` |
| `2026-03-07 10:56:29` | `cowrie.command.input` |
| `2026-03-07 10:56:29` | `cowrie.command.input` |
| `2026-03-07 10:56:29` | `cowrie.command.input` |
| `2026-03-07 10:56:31` | `cowrie.log.closed` |
| `2026-03-07 10:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.42.97` to AbuseIPDB if not already reported
- [ ] Block `46.101.42.97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-695889cb74f1

| Field | Detail |
|---|---|
| **Source IP** | `46.101.42.97` |
| **First Seen** | 2026-03-07T10:57:43.906263Z |
| **Last Seen** | 2026-03-07T10:57:52.225854Z |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 10:57:43` | `cowrie.session.connect` |
| `2026-03-07 10:57:44` | `cowrie.client.version` |
| `2026-03-07 10:57:44` | `cowrie.client.kex` |
| `2026-03-07 10:57:47` | `cowrie.login.success` |
| `2026-03-07 10:57:48` | `cowrie.session.params` |
| `2026-03-07 10:57:48` | `cowrie.command.input` |
| `2026-03-07 10:57:48` | `cowrie.command.input` |
| `2026-03-07 10:57:48` | `cowrie.command.input` |
| `2026-03-07 10:57:48` | `cowrie.command.input` |
| `2026-03-07 10:57:51` | `cowrie.log.closed` |
| `2026-03-07 10:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.42.97` to AbuseIPDB if not already reported
- [ ] Block `46.101.42.97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-2b391e452f00

| Field | Detail |
|---|---|
| **Source IP** | `203.236.109.13` |
| **First Seen** | 2026-03-07T12:01:25.968596Z |
| **Last Seen** | 2026-03-07T12:01:38.439996Z |
| **Session Duration** | 12s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 12:01:25` | `cowrie.session.connect` |
| `2026-03-07 12:01:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `203.236.109.13`
- [ ] No immediate escalation required

### 🟢 LOW · IR-c018e48cd758

| Field | Detail |
|---|---|
| **Source IP** | `220.135.110.10` |
| **First Seen** | 2026-03-07T12:16:29.283724Z |
| **Last Seen** | 2026-03-07T12:16:59.995851Z |
| **Session Duration** | 30s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 12:16:29` | `cowrie.session.connect` |
| `2026-03-07 12:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `220.135.110.10`
- [ ] No immediate escalation required

### 🟢 LOW · IR-998c97561327

| Field | Detail |
|---|---|
| **Source IP** | `120.48.124.94` |
| **First Seen** | 2026-03-07T12:24:07.267524Z |
| **Last Seen** | 2026-03-07T12:26:07.322287Z |
| **Session Duration** | 120s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 12:24:07` | `cowrie.session.connect` |
| `2026-03-07 12:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `120.48.124.94`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-b194a82c6c49

| Field | Detail |
|---|---|
| **Source IP** | `49.235.133.223` |
| **First Seen** | 2026-03-07T12:31:14.805621Z |
| **Last Seen** | 2026-03-07T12:31:16.467489Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 12:31:14` | `cowrie.session.connect` |
| `2026-03-07 12:31:15` | `cowrie.client.version` |
| `2026-03-07 12:31:15` | `cowrie.client.kex` |
| `2026-03-07 12:31:16` | `cowrie.login.success` |
| `2026-03-07 12:31:16` | `cowrie.session.params` |
| `2026-03-07 12:31:16` | `cowrie.command.input` |
| `2026-03-07 12:31:16` | `cowrie.log.closed` |
| `2026-03-07 12:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.235.133.223` to AbuseIPDB if not already reported
- [ ] Block `49.235.133.223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-4f18e4e38c50

| Field | Detail |
|---|---|
| **Source IP** | `210.165.134.111` |
| **First Seen** | 2026-03-07T12:33:46.728545Z |
| **Last Seen** | 2026-03-07T12:33:59.553695Z |
| **Session Duration** | 12s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 12:33:46` | `cowrie.session.connect` |
| `2026-03-07 12:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `210.165.134.111`
- [ ] No immediate escalation required

### 🟢 LOW · IR-745bc84626be

| Field | Detail |
|---|---|
| **Source IP** | `98.82.11.67` |
| **First Seen** | 2026-03-07T12:54:54.897617Z |
| **Last Seen** | 2026-03-07T12:54:55.691331Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 12:54:54` | `cowrie.session.connect` |
| `2026-03-07 12:54:55` | `cowrie.client.version` |
| `2026-03-07 12:54:55` | `cowrie.client.kex` |
| `2026-03-07 12:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `98.82.11.67`
- [ ] No immediate escalation required

### 🟢 LOW · IR-a594e04eda5a

| Field | Detail |
|---|---|
| **Source IP** | `49.88.156.34` |
| **First Seen** | 2026-03-07T13:20:23.631221Z |
| **Last Seen** | 2026-03-07T13:22:23.633301Z |
| **Session Duration** | 120s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 13:20:23` | `cowrie.session.connect` |
| `2026-03-07 13:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `49.88.156.34`
- [ ] No immediate escalation required

### 🟢 LOW · IR-e2141c532a34

| Field | Detail |
|---|---|
| **Source IP** | `153.246.198.45` |
| **First Seen** | 2026-03-07T13:23:34.274446Z |
| **Last Seen** | 2026-03-07T13:24:05.021846Z |
| **Session Duration** | 30s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 13:23:34` | `cowrie.session.connect` |
| `2026-03-07 13:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `153.246.198.45`
- [ ] No immediate escalation required

### 🟢 LOW · IR-66dfe7d5669b

| Field | Detail |
|---|---|
| **Source IP** | `172.212.224.104` |
| **First Seen** | 2026-03-07T14:09:59.766057Z |
| **Last Seen** | 2026-03-07T14:10:10.015667Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 14:09:59` | `cowrie.session.connect` |
| `2026-03-07 14:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `172.212.224.104`
- [ ] No immediate escalation required

### 🟢 LOW · IR-992b4ef2f70c

| Field | Detail |
|---|---|
| **Source IP** | `172.212.224.104` |
| **First Seen** | 2026-03-07T14:10:10.261220Z |
| **Last Seen** | 2026-03-07T14:10:10.262556Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 14:10:10` | `cowrie.session.connect` |
| `2026-03-07 14:10:10` | `cowrie.client.version` |
| `2026-03-07 14:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `172.212.224.104`
- [ ] No immediate escalation required

### 🟢 LOW · IR-3a197d936430

| Field | Detail |
|---|---|
| **Source IP** | `120.241.79.66` |
| **First Seen** | 2026-03-07T14:28:32.781486Z |
| **Last Seen** | 2026-03-07T14:30:32.792494Z |
| **Session Duration** | 120s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 14:28:32` | `cowrie.session.connect` |
| `2026-03-07 14:28:32` | `cowrie.client.version` |
| `2026-03-07 14:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `120.241.79.66`
- [ ] No immediate escalation required

### 🟢 LOW · IR-a046356602b3

| Field | Detail |
|---|---|
| **Source IP** | `101.200.236.207` |
| **First Seen** | 2026-03-07T14:37:16.223955Z |
| **Last Seen** | 2026-03-07T14:37:20.561093Z |
| **Session Duration** | 4s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 14:37:16` | `cowrie.session.connect` |
| `2026-03-07 14:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `101.200.236.207`
- [ ] No immediate escalation required

### 🟢 LOW · IR-632faf6f7dfd

| Field | Detail |
|---|---|
| **Source IP** | `101.200.236.207` |
| **First Seen** | 2026-03-07T14:38:09.511481Z |
| **Last Seen** | 2026-03-07T14:40:09.566322Z |
| **Session Duration** | 120s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 14:38:09` | `cowrie.session.connect` |
| `2026-03-07 14:38:09` | `cowrie.client.version` |
| `2026-03-07 14:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `101.200.236.207`
- [ ] No immediate escalation required

### 🟢 LOW · IR-9b6b708e4f31

| Field | Detail |
|---|---|
| **Source IP** | `70.162.251.153` |
| **First Seen** | 2026-03-07T14:40:59.897983Z |
| **Last Seen** | 2026-03-07T14:41:12.081833Z |
| **Session Duration** | 12s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 14:40:59` | `cowrie.session.connect` |
| `2026-03-07 14:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `70.162.251.153`
- [ ] No immediate escalation required

### 🟢 LOW · IR-a2e3034e958d

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:05:58.644908Z |
| **Last Seen** | 2026-03-07T15:05:58.806321Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:05:58` | `cowrie.session.connect` |
| `2026-03-07 15:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `134.199.171.189`
- [ ] No immediate escalation required

### 🟢 LOW · IR-efc533753c53

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:07:04.075780Z |
| **Last Seen** | 2026-03-07T15:07:07.482163Z |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:07:04` | `cowrie.session.connect` |
| `2026-03-07 15:07:04` | `cowrie.client.version` |
| `2026-03-07 15:07:04` | `cowrie.client.kex` |
| `2026-03-07 15:07:06` | `cowrie.login.failed` |
| `2026-03-07 15:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `134.199.171.189`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-281cf327a49e

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:07:56.872379Z |
| **Last Seen** | 2026-03-07T15:08:00.445040Z |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:07:56` | `cowrie.session.connect` |
| `2026-03-07 15:07:57` | `cowrie.client.version` |
| `2026-03-07 15:07:57` | `cowrie.client.kex` |
| `2026-03-07 15:07:58` | `cowrie.login.success` |
| `2026-03-07 15:07:59` | `cowrie.session.params` |
| `2026-03-07 15:07:59` | `cowrie.command.input` |
| `2026-03-07 15:07:59` | `cowrie.command.input` |
| `2026-03-07 15:07:59` | `cowrie.command.input` |
| `2026-03-07 15:07:59` | `cowrie.command.input` |
| `2026-03-07 15:08:00` | `cowrie.log.closed` |
| `2026-03-07 15:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.171.189` to AbuseIPDB if not already reported
- [ ] Block `134.199.171.189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c9e51f8b4b

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:08:49.338418Z |
| **Last Seen** | 2026-03-07T15:08:53.005916Z |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:08:49` | `cowrie.session.connect` |
| `2026-03-07 15:08:49` | `cowrie.client.version` |
| `2026-03-07 15:08:49` | `cowrie.client.kex` |
| `2026-03-07 15:08:51` | `cowrie.login.success` |
| `2026-03-07 15:08:52` | `cowrie.session.params` |
| `2026-03-07 15:08:52` | `cowrie.command.input` |
| `2026-03-07 15:08:52` | `cowrie.command.input` |
| `2026-03-07 15:08:52` | `cowrie.command.input` |
| `2026-03-07 15:08:52` | `cowrie.command.input` |
| `2026-03-07 15:08:52` | `cowrie.log.closed` |
| `2026-03-07 15:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.171.189` to AbuseIPDB if not already reported
- [ ] Block `134.199.171.189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-8f75678875f7

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:09:42.896856Z |
| **Last Seen** | 2026-03-07T15:09:46.138742Z |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:09:42` | `cowrie.session.connect` |
| `2026-03-07 15:09:43` | `cowrie.client.version` |
| `2026-03-07 15:09:43` | `cowrie.client.kex` |
| `2026-03-07 15:09:44` | `cowrie.login.failed` |
| `2026-03-07 15:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `134.199.171.189`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-0cf9c325fcf2

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:10:37.381031Z |
| **Last Seen** | 2026-03-07T15:10:41.556995Z |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:10:37` | `cowrie.session.connect` |
| `2026-03-07 15:10:37` | `cowrie.client.version` |
| `2026-03-07 15:10:37` | `cowrie.client.kex` |
| `2026-03-07 15:10:39` | `cowrie.login.success` |
| `2026-03-07 15:10:40` | `cowrie.session.params` |
| `2026-03-07 15:10:40` | `cowrie.command.input` |
| `2026-03-07 15:10:40` | `cowrie.command.input` |
| `2026-03-07 15:10:40` | `cowrie.command.input` |
| `2026-03-07 15:10:40` | `cowrie.command.input` |
| `2026-03-07 15:10:41` | `cowrie.log.closed` |
| `2026-03-07 15:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.171.189` to AbuseIPDB if not already reported
- [ ] Block `134.199.171.189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-2159fc455ac3

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:11:43.003432Z |
| **Last Seen** | 2026-03-07T15:11:43.004412Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:11:43` | `cowrie.session.connect` |
| `2026-03-07 15:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `134.199.171.189`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-48fbcee146b5

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:11:43.155301Z |
| **Last Seen** | 2026-03-07T15:11:44.461449Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:11:43` | `cowrie.session.connect` |
| `2026-03-07 15:11:43` | `cowrie.client.version` |
| `2026-03-07 15:11:43` | `cowrie.client.kex` |
| `2026-03-07 15:11:43` | `cowrie.login.success` |
| `2026-03-07 15:11:44` | `cowrie.session.params` |
| `2026-03-07 15:11:44` | `cowrie.command.input` |
| `2026-03-07 15:11:44` | `cowrie.command.input` |
| `2026-03-07 15:11:44` | `cowrie.command.input` |
| `2026-03-07 15:11:44` | `cowrie.command.input` |
| `2026-03-07 15:11:44` | `cowrie.log.closed` |
| `2026-03-07 15:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.171.189` to AbuseIPDB if not already reported
- [ ] Block `134.199.171.189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-97a7e884845a

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:13:04.582770Z |
| **Last Seen** | 2026-03-07T15:13:04.617187Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:13:04` | `cowrie.session.connect` |
| `2026-03-07 15:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `134.199.171.189`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-87e6fb5c452c

| Field | Detail |
|---|---|
| **Source IP** | `134.199.171.189` |
| **First Seen** | 2026-03-07T15:13:04.769232Z |
| **Last Seen** | 2026-03-07T15:13:06.418528Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ; , uname -s -v -n -m 2 > /dev/null, uname -m 2 > /dev/null, cat /proc/uptime 2 > /dev/null | cut -d. -f1` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:13:04` | `cowrie.session.connect` |
| `2026-03-07 15:13:04` | `cowrie.client.version` |
| `2026-03-07 15:13:04` | `cowrie.client.kex` |
| `2026-03-07 15:13:05` | `cowrie.login.success` |
| `2026-03-07 15:13:05` | `cowrie.session.params` |
| `2026-03-07 15:13:05` | `cowrie.command.input` |
| `2026-03-07 15:13:05` | `cowrie.command.input` |
| `2026-03-07 15:13:05` | `cowrie.command.input` |
| `2026-03-07 15:13:05` | `cowrie.command.input` |
| `2026-03-07 15:13:06` | `cowrie.log.closed` |
| `2026-03-07 15:13:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.199.171.189` to AbuseIPDB if not already reported
- [ ] Block `134.199.171.189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-50a1ca75ba1e

| Field | Detail |
|---|---|
| **Source IP** | `13.89.125.255` |
| **First Seen** | 2026-03-07T15:53:16.495120Z |
| **Last Seen** | 2026-03-07T15:53:26.733337Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:53:16` | `cowrie.session.connect` |
| `2026-03-07 15:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `13.89.125.255`
- [ ] No immediate escalation required

### 🟢 LOW · IR-2f1b6535588b

| Field | Detail |
|---|---|
| **Source IP** | `13.89.125.255` |
| **First Seen** | 2026-03-07T15:53:26.988158Z |
| **Last Seen** | 2026-03-07T15:53:27.248933Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 15:53:26` | `cowrie.session.connect` |
| `2026-03-07 15:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `13.89.125.255`
- [ ] No immediate escalation required

### 🟢 LOW · IR-06de2b5e6694

| Field | Detail |
|---|---|
| **Source IP** | `139.19.117.130` |
| **First Seen** | 2026-03-07T16:12:38.892540Z |
| **Last Seen** | 2026-03-07T16:12:48.893348Z |
| **Session Duration** | 10s |
| **Login Attempts** | 2 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 16:12:38` | `cowrie.session.connect` |
| `2026-03-07 16:12:38` | `cowrie.client.version` |
| `2026-03-07 16:12:39` | `cowrie.client.kex` |
| `2026-03-07 16:12:39` | `cowrie.client.fingerprint` |
| `2026-03-07 16:12:39` | `cowrie.login.failed` |
| `2026-03-07 16:12:39` | `cowrie.client.fingerprint` |
| `2026-03-07 16:12:39` | `cowrie.login.failed` |
| `2026-03-07 16:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `139.19.117.130`
- [ ] No immediate escalation required

### 🟢 LOW · IR-cfa788087ae2

| Field | Detail |
|---|---|
| **Source IP** | `49.88.156.34` |
| **First Seen** | 2026-03-07T16:55:09.313795Z |
| **Last Seen** | 2026-03-07T16:56:31.901099Z |
| **Session Duration** | 82s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 16:55:09` | `cowrie.session.connect` |
| `2026-03-07 16:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `49.88.156.34`
- [ ] No immediate escalation required

### 🟢 LOW · IR-5f7794388756

| Field | Detail |
|---|---|
| **Source IP** | `14.103.99.176` |
| **First Seen** | 2026-03-07T17:14:44.901443Z |
| **Last Seen** | 2026-03-07T17:14:44.902377Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 17:14:44` | `cowrie.session.connect` |
| `2026-03-07 17:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `14.103.99.176`
- [ ] No immediate escalation required

### 🟢 LOW · IR-f09eb3346c61

| Field | Detail |
|---|---|
| **Source IP** | `95.99.117.67` |
| **First Seen** | 2026-03-07T17:24:54.292159Z |
| **Last Seen** | 2026-03-07T17:25:08.153949Z |
| **Session Duration** | 13s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 17:24:54` | `cowrie.session.connect` |
| `2026-03-07 17:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `95.99.117.67`
- [ ] No immediate escalation required

### 🟢 LOW · IR-3db5b3fab2e3

| Field | Detail |
|---|---|
| **Source IP** | `190.215.90.80` |
| **First Seen** | 2026-03-07T17:49:28.888050Z |
| **Last Seen** | 2026-03-07T17:50:00.262304Z |
| **Session Duration** | 31s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 17:49:28` | `cowrie.session.connect` |
| `2026-03-07 17:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `190.215.90.80`
- [ ] No immediate escalation required

### 🟢 LOW · IR-105b03c6f8a1

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:21:00.868288Z |
| **Last Seen** | 2026-03-07T18:21:01.623394Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:21:00` | `cowrie.session.connect` |
| `2026-03-07 18:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-5a9fe12a9cc6

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:22:53.038731Z |
| **Last Seen** | 2026-03-07T18:22:53.502730Z |
| **Session Duration** | 0s |
| **Login Attempts** | 3 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:22:53` | `cowrie.session.connect` |
| `2026-03-07 18:22:53` | `cowrie.login.failed` |
| `2026-03-07 18:22:53` | `cowrie.login.failed` |
| `2026-03-07 18:22:53` | `cowrie.login.failed` |
| `2026-03-07 18:22:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-b7b162ca2f20

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:24:54.886465Z |
| **Last Seen** | 2026-03-07T18:24:55.117155Z |
| **Session Duration** | 0s |
| **Login Attempts** | 3 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:24:54` | `cowrie.session.connect` |
| `2026-03-07 18:24:54` | `cowrie.login.failed` |
| `2026-03-07 18:24:54` | `cowrie.login.failed` |
| `2026-03-07 18:24:54` | `cowrie.login.failed` |
| `2026-03-07 18:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-789385420570

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:26:48.520395Z |
| **Last Seen** | 2026-03-07T18:26:48.522146Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:26:48` | `cowrie.session.connect` |
| `2026-03-07 18:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-00b8c62f88ef

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:28:37.672646Z |
| **Last Seen** | 2026-03-07T18:28:47.761871Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:28:37` | `cowrie.session.connect` |
| `2026-03-07 18:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-5db056b07a95

| Field | Detail |
|---|---|
| **Source IP** | `91.196.152.176` |
| **First Seen** | 2026-03-07T18:30:08.345424Z |
| **Last Seen** | 2026-03-07T18:30:08.392240Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:30:08` | `cowrie.session.connect` |
| `2026-03-07 18:30:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.196.152.176`
- [ ] No immediate escalation required

### 🟢 LOW · IR-d6c098d11cc6

| Field | Detail |
|---|---|
| **Source IP** | `91.196.152.208` |
| **First Seen** | 2026-03-07T18:30:08.528203Z |
| **Last Seen** | 2026-03-07T18:30:18.670001Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:30:08` | `cowrie.session.connect` |
| `2026-03-07 18:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.196.152.208`
- [ ] No immediate escalation required

### 🟢 LOW · IR-d9c44ac379c5

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:30:15.769177Z |
| **Last Seen** | 2026-03-07T18:30:25.979678Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:30:15` | `cowrie.session.connect` |
| `2026-03-07 18:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-4ba4432868cd

| Field | Detail |
|---|---|
| **Source IP** | `91.196.152.210` |
| **First Seen** | 2026-03-07T18:30:32.783411Z |
| **Last Seen** | 2026-03-07T18:30:32.785079Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:30:32` | `cowrie.session.connect` |
| `2026-03-07 18:30:32` | `cowrie.client.version` |
| `2026-03-07 18:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.196.152.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-3aa7894429ff

| Field | Detail |
|---|---|
| **Source IP** | `91.196.152.214` |
| **First Seen** | 2026-03-07T18:30:33.058798Z |
| **Last Seen** | 2026-03-07T18:30:36.063092Z |
| **Session Duration** | 3s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:30:33` | `cowrie.session.connect` |
| `2026-03-07 18:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.196.152.214`
- [ ] No immediate escalation required

### 🟢 LOW · IR-e2a8e9a380ec

| Field | Detail |
|---|---|
| **Source IP** | `3.143.162.210` |
| **First Seen** | 2026-03-07T18:30:45.043967Z |
| **Last Seen** | 2026-03-07T18:30:45.202991Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:30:45` | `cowrie.session.connect` |
| `2026-03-07 18:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.143.162.210`
- [ ] No immediate escalation required

### 🟢 LOW · IR-fb0193093218

| Field | Detail |
|---|---|
| **Source IP** | `91.196.152.223` |
| **First Seen** | 2026-03-07T18:32:09.571345Z |
| **Last Seen** | 2026-03-07T18:32:11.239383Z |
| **Session Duration** | 1s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:32:09` | `cowrie.session.connect` |
| `2026-03-07 18:32:09` | `cowrie.client.version` |
| `2026-03-07 18:32:09` | `cowrie.client.kex` |
| `2026-03-07 18:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.196.152.223`
- [ ] No immediate escalation required

### 🟢 LOW · IR-740dc7075700

| Field | Detail |
|---|---|
| **Source IP** | `91.231.89.2` |
| **First Seen** | 2026-03-07T18:32:09.703499Z |
| **Last Seen** | 2026-03-07T18:32:11.378223Z |
| **Session Duration** | 1s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:32:09` | `cowrie.session.connect` |
| `2026-03-07 18:32:10` | `cowrie.client.version` |
| `2026-03-07 18:32:10` | `cowrie.client.kex` |
| `2026-03-07 18:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `91.231.89.2`
- [ ] No immediate escalation required

### 🟢 LOW · IR-48314f43d3c2

| Field | Detail |
|---|---|
| **Source IP** | `49.88.156.34` |
| **First Seen** | 2026-03-07T18:35:23.662629Z |
| **Last Seen** | 2026-03-07T18:37:23.763957Z |
| **Session Duration** | 120s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 18:35:23` | `cowrie.session.connect` |
| `2026-03-07 18:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `49.88.156.34`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-7f8626670710

| Field | Detail |
|---|---|
| **Source IP** | `14.103.99.176` |
| **First Seen** | 2026-03-07T19:14:42.354295Z |
| **Last Seen** | 2026-03-07T19:14:43.763268Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 19:14:42` | `cowrie.session.connect` |
| `2026-03-07 19:14:42` | `cowrie.client.version` |
| `2026-03-07 19:14:42` | `cowrie.client.kex` |
| `2026-03-07 19:14:43` | `cowrie.login.success` |
| `2026-03-07 19:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.99.176` to AbuseIPDB if not already reported
- [ ] Block `14.103.99.176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-82031d767720

| Field | Detail |
|---|---|
| **Source IP** | `101.71.37.79` |
| **First Seen** | 2026-03-07T19:22:44.469636Z |
| **Last Seen** | 2026-03-07T19:22:57.967116Z |
| **Session Duration** | 13s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-07 19:22:44` | `cowrie.session.connect` |
| `2026-03-07 19:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `101.71.37.79`
- [ ] No immediate escalation required

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `172.212.224.104` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `91.196.152.214` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `98.82.11.67` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 29 |
| `14.103.99.176` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 1 |
| `183.87.217.222` | IN | Ishan Netsol Pvt Ltd | **100** ⚠️ | 32 |
| `139.19.117.130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `91.196.152.223` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `203.236.109.13` | KR | Korea Telecom | **100** ⚠️ | 30 |
| `91.196.152.176` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `91.196.152.208` | FR | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |

---

## 🔕 False Positive Summary (193 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 13 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 28 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 144 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 260 cases |
| Tool 27 | Threat Intel Feeder         | ✅ 67 IPs enriched |
| Tool 29 | False Positive Tracker      | ✅ 193 filtered (74.2%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 28 | SOC Handover Report         | ✅ This report |

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL IR cases in `data/ir_cases.json`
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, run Tool 31 malware analyzer
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-07T19:27:46Z_
