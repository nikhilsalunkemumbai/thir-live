# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-07 |
| **Generated At** | 2026-03-07T11:26:41Z |
| **Shift Time** | 11:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **160** |
| Confirmed Threats | **17** |
| False Positives Filtered | **143** (89.4%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **9** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **144** |

---

## 🚨 Confirmed Threats (17)

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `1.225.62.211` | KR | SK Broadband Co Ltd | **100** ⚠️ | 11 |
| `209.14.28.89` | BR | WIX NET DO BRASIL LTDA | **100** ⚠️ | 2 |
| `129.146.81.203` | US | Oracle Corporation | **100** ⚠️ | 18 |
| `176.32.195.85` | AM | Interactive TV LLC | **100** ⚠️ | 50 |
| `183.87.217.222` | IN | Ishan Netsol Pvt Ltd | **100** ⚠️ | 31 |
| `138.197.147.214` | CA | DigitalOcean, LLC | **56** | 0 |
| `85.172.77.15` | RU | OJSC Rostelecom Macroregional Branch South | **52** | 0 |
| `27.123.241.4` | IN | Ani Network Pvt Ltd | **48** | 0 |
| `209.38.80.132` | AU | DigitalOcean, LLC | **43** | 0 |
| `27.123.241.169` | IN | Ani Network Pvt Ltd | **43** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |

---

## 🔕 False Positive Summary (143 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 13 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 126 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 160 cases |
| Tool 27 | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29 | False Positive Tracker      | ✅ 143 filtered (89.4%) |
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
_Report time: 2026-03-07T11:26:41Z_
