# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-17 |
| **Generated At** | 2026-03-17T04:19:04Z |
| **Shift Time** | 04:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **286** |
| Confirmed Threats | **87** |
| False Positives Filtered | **199** (69.6%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **18** |
| High Severity Cases | **44** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **242** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **174** |
| Unique Credential Pairs | **163** |
| Unique Usernames | **106** |
| Unique Passwords | **135** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 45 |
| `admin` | 5 |
| `ubuntu` | 4 |
| `minecraft` | 3 |
| `user1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 19 |
| `password` | 4 |
| `12345678` | 3 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `ubuntu` | 2 |
| `minecraft` | `123456` | 2 |
| `jack` | `jack` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `196.11.86.134` | 2026-03-17T01:53:52 |
| `root` | `test123` | `159.65.237.121` | 2026-03-17T02:03:33 |
| `root` | `rock` | `159.65.237.121` | 2026-03-17T02:03:59 |
| `root` | `Pass@123` | `159.65.237.121` | 2026-03-17T02:04:06 |
| `root` | `QWEqwe123` | `159.65.237.121` | 2026-03-17T02:04:25 |
| `root` | `test1234` | `159.65.237.121` | 2026-03-17T02:04:45 |
| `root` | `nPSpP4PBW0` | `159.65.237.121` | 2026-03-17T02:04:58 |
| `root` | `!Q2w3e4r` | `159.65.237.121` | 2026-03-17T02:05:24 |
| `root` | `phuvanduc` | `159.65.237.121` | 2026-03-17T02:05:30 |
| `root` | `password` | `159.65.237.121` | 2026-03-17T02:05:37 |
| `root` | `123456789` | `159.65.237.121` | 2026-03-17T02:05:44 |
| `root` | `P@ssw0rd123` | `159.65.237.121` | 2026-03-17T02:06:58 |
| `root` | `abc123456` | `161.35.121.57` | 2026-03-17T02:30:27 |
| `root` | `1qaz@WSX3edc` | `161.35.121.57` | 2026-03-17T02:30:34 |
| `root` | `ubuntu` | `161.35.121.57` | 2026-03-17T02:30:54 |
| `root` | `1234` | `161.35.121.57` | 2026-03-17T02:31:20 |
| `root` | `qq123456` | `161.35.121.57` | 2026-03-17T02:31:34 |
| `root` | `1qazxsw2` | `161.35.121.57` | 2026-03-17T02:31:41 |
| `root` | `aB123456` | `161.35.121.57` | 2026-03-17T02:31:54 |
| `root` | `!qaz@WSX` | `161.35.121.57` | 2026-03-17T02:32:07 |
| `root` | `kali` | `161.35.121.57` | 2026-03-17T02:32:27 |
| `root` | `helloworld` | `161.35.121.57` | 2026-03-17T02:32:34 |
| `root` | `!QAZ2wsx3edc` | `161.35.121.57` | 2026-03-17T02:32:41 |
| `root` | `parolamea` | `161.35.121.57` | 2026-03-17T02:33:20 |
| `root` | `qwe123456` | `161.35.121.57` | 2026-03-17T02:33:27 |
| `root` | `Password@123` | `161.35.121.57` | 2026-03-17T02:33:40 |
| `root` | `qwerty1` | `180.94.75.114` | 2026-03-17T02:36:01 |
| `root` | `147258` | `159.223.135.43` | 2026-03-17T03:12:46 |
| `root` | `P@ssword` | `159.223.135.43` | 2026-03-17T03:12:52 |
| `root` | `12qwaszx` | `159.223.135.43` | 2026-03-17T03:13:11 |
| `root` | `qwerty123` | `159.223.135.43` | 2026-03-17T03:13:24 |
| `root` | `redhat` | `159.223.135.43` | 2026-03-17T03:14:08 |
| `root` | `root123` | `159.223.135.43` | 2026-03-17T03:14:27 |
| `root` | `null` | `159.223.135.43` | 2026-03-17T03:15:11 |
| `root` | `!Q@W3e4r` | `159.223.135.43` | 2026-03-17T03:16:07 |
| `root` | `1qaz@WSX3edc` | `159.223.135.43` | 2026-03-17T03:17:09 |
| `root` | `China123` | `47.239.235.46` | 2026-03-17T03:21:43 |
| `root` | `3245gs5662d34` | `47.239.235.46` | 2026-03-17T03:21:46 |
| `root` | `5tgb^YHN` | `47.239.235.46` | 2026-03-17T03:23:22 |
| `root` | `123456@Abc` | `47.239.235.46` | 2026-03-17T03:23:51 |
| `root` | `stxadmin` | `112.184.45.204` | 2026-03-17T03:47:54 |
| `root` | `xmhdipc` | `46.39.251.94` | 2026-03-17T04:13:39 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **35** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5d0894404feb

| Field | Detail |
|---|---|
| **Source IP** | `196.11.86[.]134` |
| **First Seen** | 2026-03-17 01:53 |
| **Last Seen** | 2026-03-17 01:55 |
| **Session Duration** | 96s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 01:53:51` | `cowrie.session.connect` |
| `2026-03-17 01:53:51` | `cowrie.client.version` |
| `2026-03-17 01:53:52` | `cowrie.client.kex` |
| `2026-03-17 01:53:52` | `cowrie.login.success` |
| `2026-03-17 01:55:27` | `cowrie.session.file_upload` |
| `2026-03-17 01:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.11.86[.]134` to AbuseIPDB if not already reported
- [ ] Block `196.11.86[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23db0eec7dc

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:30 |
| **Last Seen** | 2026-03-17 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:30:26` | `cowrie.session.connect` |
| `2026-03-17 02:30:26` | `cowrie.client.version` |
| `2026-03-17 02:30:26` | `cowrie.client.kex` |
| `2026-03-17 02:30:27` | `cowrie.login.success` |
| `2026-03-17 02:30:27` | `cowrie.session.params` |
| `2026-03-17 02:30:27` | `cowrie.command.input` |
| `2026-03-17 02:30:28` | `cowrie.log.closed` |
| `2026-03-17 02:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57753b8e0695

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:30 |
| **Last Seen** | 2026-03-17 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:30:33` | `cowrie.session.connect` |
| `2026-03-17 02:30:33` | `cowrie.client.version` |
| `2026-03-17 02:30:33` | `cowrie.client.kex` |
| `2026-03-17 02:30:34` | `cowrie.login.success` |
| `2026-03-17 02:30:34` | `cowrie.session.params` |
| `2026-03-17 02:30:34` | `cowrie.command.input` |
| `2026-03-17 02:30:34` | `cowrie.log.closed` |
| `2026-03-17 02:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ea41a125e6

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:30 |
| **Last Seen** | 2026-03-17 02:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:30:53` | `cowrie.session.connect` |
| `2026-03-17 02:30:53` | `cowrie.client.version` |
| `2026-03-17 02:30:53` | `cowrie.client.kex` |
| `2026-03-17 02:30:54` | `cowrie.login.success` |
| `2026-03-17 02:30:54` | `cowrie.session.params` |
| `2026-03-17 02:30:54` | `cowrie.command.input` |
| `2026-03-17 02:30:54` | `cowrie.log.closed` |
| `2026-03-17 02:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d332fdfa123

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:31 |
| **Last Seen** | 2026-03-17 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:31:20` | `cowrie.session.connect` |
| `2026-03-17 02:31:20` | `cowrie.client.version` |
| `2026-03-17 02:31:20` | `cowrie.client.kex` |
| `2026-03-17 02:31:20` | `cowrie.login.success` |
| `2026-03-17 02:31:21` | `cowrie.session.params` |
| `2026-03-17 02:31:21` | `cowrie.command.input` |
| `2026-03-17 02:31:21` | `cowrie.log.closed` |
| `2026-03-17 02:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a67185334c6

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:31 |
| **Last Seen** | 2026-03-17 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:31:33` | `cowrie.session.connect` |
| `2026-03-17 02:31:33` | `cowrie.client.version` |
| `2026-03-17 02:31:33` | `cowrie.client.kex` |
| `2026-03-17 02:31:34` | `cowrie.login.success` |
| `2026-03-17 02:31:34` | `cowrie.session.params` |
| `2026-03-17 02:31:34` | `cowrie.command.input` |
| `2026-03-17 02:31:35` | `cowrie.log.closed` |
| `2026-03-17 02:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e980e3ae8ca7

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:31 |
| **Last Seen** | 2026-03-17 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:31:40` | `cowrie.session.connect` |
| `2026-03-17 02:31:40` | `cowrie.client.version` |
| `2026-03-17 02:31:40` | `cowrie.client.kex` |
| `2026-03-17 02:31:41` | `cowrie.login.success` |
| `2026-03-17 02:31:41` | `cowrie.session.params` |
| `2026-03-17 02:31:41` | `cowrie.command.input` |
| `2026-03-17 02:31:41` | `cowrie.log.closed` |
| `2026-03-17 02:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b692a707e00

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:31 |
| **Last Seen** | 2026-03-17 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:31:53` | `cowrie.session.connect` |
| `2026-03-17 02:31:53` | `cowrie.client.version` |
| `2026-03-17 02:31:53` | `cowrie.client.kex` |
| `2026-03-17 02:31:54` | `cowrie.login.success` |
| `2026-03-17 02:31:54` | `cowrie.session.params` |
| `2026-03-17 02:31:54` | `cowrie.command.input` |
| `2026-03-17 02:31:55` | `cowrie.log.closed` |
| `2026-03-17 02:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c588089a79e

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:32 |
| **Last Seen** | 2026-03-17 02:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:32:06` | `cowrie.session.connect` |
| `2026-03-17 02:32:06` | `cowrie.client.version` |
| `2026-03-17 02:32:07` | `cowrie.client.kex` |
| `2026-03-17 02:32:07` | `cowrie.login.success` |
| `2026-03-17 02:32:08` | `cowrie.session.params` |
| `2026-03-17 02:32:08` | `cowrie.command.input` |
| `2026-03-17 02:32:08` | `cowrie.log.closed` |
| `2026-03-17 02:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e875e6c8835

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:32 |
| **Last Seen** | 2026-03-17 02:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:32:26` | `cowrie.session.connect` |
| `2026-03-17 02:32:26` | `cowrie.client.version` |
| `2026-03-17 02:32:27` | `cowrie.client.kex` |
| `2026-03-17 02:32:27` | `cowrie.login.success` |
| `2026-03-17 02:32:28` | `cowrie.session.params` |
| `2026-03-17 02:32:28` | `cowrie.command.input` |
| `2026-03-17 02:32:28` | `cowrie.log.closed` |
| `2026-03-17 02:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a1d0cd4be9

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:32 |
| **Last Seen** | 2026-03-17 02:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:32:33` | `cowrie.session.connect` |
| `2026-03-17 02:32:33` | `cowrie.client.version` |
| `2026-03-17 02:32:33` | `cowrie.client.kex` |
| `2026-03-17 02:32:34` | `cowrie.login.success` |
| `2026-03-17 02:32:34` | `cowrie.session.params` |
| `2026-03-17 02:32:34` | `cowrie.command.input` |
| `2026-03-17 02:32:34` | `cowrie.log.closed` |
| `2026-03-17 02:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23c6f57ae28

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:32 |
| **Last Seen** | 2026-03-17 02:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:32:40` | `cowrie.session.connect` |
| `2026-03-17 02:32:40` | `cowrie.client.version` |
| `2026-03-17 02:32:40` | `cowrie.client.kex` |
| `2026-03-17 02:32:41` | `cowrie.login.success` |
| `2026-03-17 02:32:41` | `cowrie.session.params` |
| `2026-03-17 02:32:41` | `cowrie.command.input` |
| `2026-03-17 02:32:42` | `cowrie.log.closed` |
| `2026-03-17 02:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64151cf4e5f

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:33 |
| **Last Seen** | 2026-03-17 02:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:33:19` | `cowrie.session.connect` |
| `2026-03-17 02:33:20` | `cowrie.client.version` |
| `2026-03-17 02:33:20` | `cowrie.client.kex` |
| `2026-03-17 02:33:20` | `cowrie.login.success` |
| `2026-03-17 02:33:21` | `cowrie.session.params` |
| `2026-03-17 02:33:21` | `cowrie.command.input` |
| `2026-03-17 02:33:21` | `cowrie.log.closed` |
| `2026-03-17 02:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3a5af52e87

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:33 |
| **Last Seen** | 2026-03-17 02:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:33:26` | `cowrie.session.connect` |
| `2026-03-17 02:33:26` | `cowrie.client.version` |
| `2026-03-17 02:33:26` | `cowrie.client.kex` |
| `2026-03-17 02:33:27` | `cowrie.login.success` |
| `2026-03-17 02:33:28` | `cowrie.session.params` |
| `2026-03-17 02:33:28` | `cowrie.command.input` |
| `2026-03-17 02:33:28` | `cowrie.log.closed` |
| `2026-03-17 02:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e94701e19d3

| Field | Detail |
|---|---|
| **Source IP** | `161.35.121[.]57` |
| **First Seen** | 2026-03-17 02:33 |
| **Last Seen** | 2026-03-17 02:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:33:39` | `cowrie.session.connect` |
| `2026-03-17 02:33:39` | `cowrie.client.version` |
| `2026-03-17 02:33:39` | `cowrie.client.kex` |
| `2026-03-17 02:33:40` | `cowrie.login.success` |
| `2026-03-17 02:33:41` | `cowrie.session.params` |
| `2026-03-17 02:33:41` | `cowrie.command.input` |
| `2026-03-17 02:33:41` | `cowrie.log.closed` |
| `2026-03-17 02:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.121[.]57` to AbuseIPDB if not already reported
- [ ] Block `161.35.121[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7beca2cc3bf

| Field | Detail |
|---|---|
| **Source IP** | `180.94.75[.]114` |
| **First Seen** | 2026-03-17 02:35 |
| **Last Seen** | 2026-03-17 02:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 02:35:59` | `cowrie.session.connect` |
| `2026-03-17 02:35:59` | `cowrie.client.version` |
| `2026-03-17 02:35:59` | `cowrie.client.kex` |
| `2026-03-17 02:36:01` | `cowrie.login.success` |
| `2026-03-17 02:36:02` | `cowrie.direct-tcpip.request` |
| `2026-03-17 02:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.94.75[.]114` to AbuseIPDB if not already reported
- [ ] Block `180.94.75[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb821fa2d245

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:12 |
| **Last Seen** | 2026-03-17 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:12:45` | `cowrie.session.connect` |
| `2026-03-17 03:12:45` | `cowrie.client.version` |
| `2026-03-17 03:12:45` | `cowrie.client.kex` |
| `2026-03-17 03:12:46` | `cowrie.login.success` |
| `2026-03-17 03:12:46` | `cowrie.session.params` |
| `2026-03-17 03:12:46` | `cowrie.command.input` |
| `2026-03-17 03:12:46` | `cowrie.log.closed` |
| `2026-03-17 03:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02fcbede9104

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:12 |
| **Last Seen** | 2026-03-17 03:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:12:51` | `cowrie.session.connect` |
| `2026-03-17 03:12:51` | `cowrie.client.version` |
| `2026-03-17 03:12:51` | `cowrie.client.kex` |
| `2026-03-17 03:12:52` | `cowrie.login.success` |
| `2026-03-17 03:12:52` | `cowrie.session.params` |
| `2026-03-17 03:12:52` | `cowrie.command.input` |
| `2026-03-17 03:12:53` | `cowrie.log.closed` |
| `2026-03-17 03:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8dfe57f22d3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:13 |
| **Last Seen** | 2026-03-17 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:13:10` | `cowrie.session.connect` |
| `2026-03-17 03:13:10` | `cowrie.client.version` |
| `2026-03-17 03:13:11` | `cowrie.client.kex` |
| `2026-03-17 03:13:11` | `cowrie.login.success` |
| `2026-03-17 03:13:12` | `cowrie.session.params` |
| `2026-03-17 03:13:12` | `cowrie.command.input` |
| `2026-03-17 03:13:12` | `cowrie.log.closed` |
| `2026-03-17 03:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6307ee81d4d9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:13 |
| **Last Seen** | 2026-03-17 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:13:23` | `cowrie.session.connect` |
| `2026-03-17 03:13:23` | `cowrie.client.version` |
| `2026-03-17 03:13:23` | `cowrie.client.kex` |
| `2026-03-17 03:13:24` | `cowrie.login.success` |
| `2026-03-17 03:13:24` | `cowrie.session.params` |
| `2026-03-17 03:13:24` | `cowrie.command.input` |
| `2026-03-17 03:13:24` | `cowrie.log.closed` |
| `2026-03-17 03:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2b91d6a512

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:14 |
| **Last Seen** | 2026-03-17 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:14:07` | `cowrie.session.connect` |
| `2026-03-17 03:14:07` | `cowrie.client.version` |
| `2026-03-17 03:14:07` | `cowrie.client.kex` |
| `2026-03-17 03:14:08` | `cowrie.login.success` |
| `2026-03-17 03:14:08` | `cowrie.session.params` |
| `2026-03-17 03:14:08` | `cowrie.command.input` |
| `2026-03-17 03:14:09` | `cowrie.log.closed` |
| `2026-03-17 03:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee7450b8628

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:14 |
| **Last Seen** | 2026-03-17 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:14:26` | `cowrie.session.connect` |
| `2026-03-17 03:14:26` | `cowrie.client.version` |
| `2026-03-17 03:14:26` | `cowrie.client.kex` |
| `2026-03-17 03:14:27` | `cowrie.login.success` |
| `2026-03-17 03:14:27` | `cowrie.session.params` |
| `2026-03-17 03:14:27` | `cowrie.command.input` |
| `2026-03-17 03:14:27` | `cowrie.log.closed` |
| `2026-03-17 03:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80671c73e605

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:15 |
| **Last Seen** | 2026-03-17 03:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:15:10` | `cowrie.session.connect` |
| `2026-03-17 03:15:10` | `cowrie.client.version` |
| `2026-03-17 03:15:10` | `cowrie.client.kex` |
| `2026-03-17 03:15:11` | `cowrie.login.success` |
| `2026-03-17 03:15:11` | `cowrie.session.params` |
| `2026-03-17 03:15:11` | `cowrie.command.input` |
| `2026-03-17 03:15:11` | `cowrie.log.closed` |
| `2026-03-17 03:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37056f9678d4

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:16 |
| **Last Seen** | 2026-03-17 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:16:06` | `cowrie.session.connect` |
| `2026-03-17 03:16:06` | `cowrie.client.version` |
| `2026-03-17 03:16:06` | `cowrie.client.kex` |
| `2026-03-17 03:16:07` | `cowrie.login.success` |
| `2026-03-17 03:16:07` | `cowrie.session.params` |
| `2026-03-17 03:16:07` | `cowrie.command.input` |
| `2026-03-17 03:16:08` | `cowrie.log.closed` |
| `2026-03-17 03:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-262f830fa494

| Field | Detail |
|---|---|
| **Source IP** | `159.223.135[.]43` |
| **First Seen** | 2026-03-17 03:17 |
| **Last Seen** | 2026-03-17 03:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:17:08` | `cowrie.session.connect` |
| `2026-03-17 03:17:08` | `cowrie.client.version` |
| `2026-03-17 03:17:09` | `cowrie.client.kex` |
| `2026-03-17 03:17:09` | `cowrie.login.success` |
| `2026-03-17 03:17:10` | `cowrie.session.params` |
| `2026-03-17 03:17:10` | `cowrie.command.input` |
| `2026-03-17 03:17:10` | `cowrie.log.closed` |
| `2026-03-17 03:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.135[.]43` to AbuseIPDB if not already reported
- [ ] Block `159.223.135[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524fe72ef42e

| Field | Detail |
|---|---|
| **Source IP** | `47.239.235[.]46` |
| **First Seen** | 2026-03-17 03:21 |
| **Last Seen** | 2026-03-17 03:21 |
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
| `2026-03-17 03:21:43` | `cowrie.session.connect` |
| `2026-03-17 03:21:43` | `cowrie.client.version` |
| `2026-03-17 03:21:43` | `cowrie.client.kex` |
| `2026-03-17 03:21:43` | `cowrie.login.success` |
| `2026-03-17 03:21:43` | `cowrie.session.params` |
| `2026-03-17 03:21:43` | `cowrie.command.input` |
| `2026-03-17 03:21:43` | `cowrie.command.failed` |
| `2026-03-17 03:21:44` | `cowrie.log.closed` |
| `2026-03-17 03:21:44` | `cowrie.session.params` |
| `2026-03-17 03:21:44` | `cowrie.command.input` |
| `2026-03-17 03:21:44` | `cowrie.session.file_download` |
| `2026-03-17 03:21:44` | `cowrie.log.closed` |
| `2026-03-17 03:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.239.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557a431a874e

| Field | Detail |
|---|---|
| **Source IP** | `47.239.235[.]46` |
| **First Seen** | 2026-03-17 03:21 |
| **Last Seen** | 2026-03-17 03:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:21:46` | `cowrie.session.connect` |
| `2026-03-17 03:21:46` | `cowrie.client.version` |
| `2026-03-17 03:21:46` | `cowrie.client.kex` |
| `2026-03-17 03:21:46` | `cowrie.login.success` |
| `2026-03-17 03:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.239.235[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9802aeaeb202

| Field | Detail |
|---|---|
| **Source IP** | `47.239.235[.]46` |
| **First Seen** | 2026-03-17 03:23 |
| **Last Seen** | 2026-03-17 03:23 |
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
| `2026-03-17 03:23:22` | `cowrie.session.connect` |
| `2026-03-17 03:23:22` | `cowrie.client.version` |
| `2026-03-17 03:23:22` | `cowrie.client.kex` |
| `2026-03-17 03:23:22` | `cowrie.login.success` |
| `2026-03-17 03:23:22` | `cowrie.session.params` |
| `2026-03-17 03:23:22` | `cowrie.command.input` |
| `2026-03-17 03:23:22` | `cowrie.command.failed` |
| `2026-03-17 03:23:22` | `cowrie.log.closed` |
| `2026-03-17 03:23:23` | `cowrie.session.params` |
| `2026-03-17 03:23:23` | `cowrie.command.input` |
| `2026-03-17 03:23:23` | `cowrie.session.file_download` |
| `2026-03-17 03:23:23` | `cowrie.log.closed` |
| `2026-03-17 03:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.239.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfd6dfa5e05f

| Field | Detail |
|---|---|
| **Source IP** | `47.239.235[.]46` |
| **First Seen** | 2026-03-17 03:23 |
| **Last Seen** | 2026-03-17 03:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:23:25` | `cowrie.session.connect` |
| `2026-03-17 03:23:25` | `cowrie.client.version` |
| `2026-03-17 03:23:25` | `cowrie.client.kex` |
| `2026-03-17 03:23:25` | `cowrie.login.success` |
| `2026-03-17 03:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.239.235[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02553ecc8840

| Field | Detail |
|---|---|
| **Source IP** | `47.239.235[.]46` |
| **First Seen** | 2026-03-17 03:23 |
| **Last Seen** | 2026-03-17 03:23 |
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
| `2026-03-17 03:23:50` | `cowrie.session.connect` |
| `2026-03-17 03:23:50` | `cowrie.client.version` |
| `2026-03-17 03:23:50` | `cowrie.client.kex` |
| `2026-03-17 03:23:51` | `cowrie.login.success` |
| `2026-03-17 03:23:51` | `cowrie.session.params` |
| `2026-03-17 03:23:51` | `cowrie.command.input` |
| `2026-03-17 03:23:51` | `cowrie.command.failed` |
| `2026-03-17 03:23:51` | `cowrie.log.closed` |
| `2026-03-17 03:23:51` | `cowrie.session.params` |
| `2026-03-17 03:23:51` | `cowrie.command.input` |
| `2026-03-17 03:23:51` | `cowrie.session.file_download` |
| `2026-03-17 03:23:51` | `cowrie.log.closed` |
| `2026-03-17 03:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.239.235[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ad35b2f81c2

| Field | Detail |
|---|---|
| **Source IP** | `47.239.235[.]46` |
| **First Seen** | 2026-03-17 03:23 |
| **Last Seen** | 2026-03-17 03:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:23:53` | `cowrie.session.connect` |
| `2026-03-17 03:23:53` | `cowrie.client.version` |
| `2026-03-17 03:23:53` | `cowrie.client.kex` |
| `2026-03-17 03:23:54` | `cowrie.login.success` |
| `2026-03-17 03:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.239.235[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.239.235[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c790b69f20c

| Field | Detail |
|---|---|
| **Source IP** | `112.184.45[.]204` |
| **First Seen** | 2026-03-17 03:47 |
| **Last Seen** | 2026-03-17 03:48 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 03:47:50` | `cowrie.session.connect` |
| `2026-03-17 03:47:51` | `cowrie.client.version` |
| `2026-03-17 03:47:51` | `cowrie.client.kex` |
| `2026-03-17 03:47:54` | `cowrie.login.success` |
| `2026-03-17 03:47:55` | `cowrie.direct-tcpip.request` |
| `2026-03-17 03:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.184.45[.]204` to AbuseIPDB if not already reported
- [ ] Block `112.184.45[.]204` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c45f863727

| Field | Detail |
|---|---|
| **Source IP** | `46.39.251[.]94` |
| **First Seen** | 2026-03-17 04:13 |
| **Last Seen** | 2026-03-17 04:16 |
| **Session Duration** | 181s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox LRTPW` |
| **Download Attempts** | e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff |
| **Malware Analysis** | e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff (LOW) |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 04:13:38` | `cowrie.session.connect` |
| `2026-03-17 04:13:38` | `cowrie.telnet.option` |
| `2026-03-17 04:13:38` | `cowrie.login.failed` |
| `2026-03-17 04:13:39` | `cowrie.telnet.option` |
| `2026-03-17 04:13:39` | `cowrie.login.success` |
| `2026-03-17 04:13:39` | `cowrie.session.params` |
| `2026-03-17 04:13:39` | `cowrie.command.input` |
| `2026-03-17 04:13:39` | `cowrie.command.input` |
| `2026-03-17 04:13:39` | `cowrie.command.failed` |
| `2026-03-17 04:13:39` | `cowrie.command.input` |
| `2026-03-17 04:13:39` | `cowrie.command.failed` |
| `2026-03-17 04:13:39` | `cowrie.command.input` |
| `2026-03-17 04:13:39` | `cowrie.command.input` |
| `2026-03-17 04:13:39` | `cowrie.command.input` |
| `2026-03-17 04:13:40` | `cowrie.command.input` |
| `2026-03-17 04:13:40` | `cowrie.command.input` |
| `2026-03-17 04:13:40` | `cowrie.command.failed` |
| `2026-03-17 04:13:40` | `cowrie.command.input` |
| `2026-03-17 04:13:40` | `cowrie.command.input` |
| `2026-03-17 04:13:40` | `cowrie.command.input` |
| `2026-03-17 04:16:39` | `cowrie.session.file_download` |
| `2026-03-17 04:16:39` | `cowrie.log.closed` |
| `2026-03-17 04:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.39.251[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.39.251[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.201.57[.]104` | **15** | 2026-03-17 03:11 | 2026-03-17 03:27 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.42[.]17` | **15** | 2026-03-17 03:00 | 2026-03-17 03:10 | 20m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **3** | 2026-03-17 03:33 | 2026-03-17 03:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]42` | **2** | 2026-03-17 02:02 | 2026-03-17 02:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-17 02:20 | 2026-03-17 02:28 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.47.158[.]137` | 1 | 2026-03-17 03:53 | 2026-03-17 03:54 | 60s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-03-17 01:16 | 2026-03-17 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.67.161[.]37` | 1 | 2026-03-17 03:46 | 2026-03-17 03:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-03-17 00:51 | 2026-03-17 00:51 | 16s | 0 | `T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-17 02:49 | 2026-03-17 02:50 | 118s | 0 | `T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-17 02:37 | 2026-03-17 02:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `120.203.25[.]201` | 1 | 2026-03-17 01:27 | 2026-03-17 01:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-17 03:41 | 2026-03-17 03:42 | 62s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-17 03:04 | 2026-03-17 03:04 | 5s | 0 | `T1592` | 🟢 LOW |
| `151.42.177[.]4` | 1 | 2026-03-17 00:11 | 2026-03-17 00:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `185.52.51[.]123` | 1 | 2026-03-17 02:19 | 2026-03-17 02:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-03-17 02:55 | 2026-03-17 02:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `204.216.190[.]165` | 1 | 2026-03-17 04:03 | 2026-03-17 04:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.130.203[.]68` | 1 | 2026-03-17 01:22 | 2026-03-17 01:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `24.163.114[.]60` | 1 | 2026-03-17 00:02 | 2026-03-17 00:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `27.223.98[.]117` | 1 | 2026-03-17 02:44 | 2026-03-17 02:45 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.106.81[.]21` | 1 | 2026-03-17 00:43 | 2026-03-17 00:43 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.184.45[.]204` | KR | Korea Telecom | **100** ⚠️ | 9 |
| `180.94.75[.]114` | AF | GCN/DCN Networks | **100** ⚠️ | 5 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `120.198.138[.]185` | CN | China Mobile Communications Corporation | **100** ⚠️ | 22 |
| `118.163.178[.]146` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `197.156.97[.]198` | ET | To ERs logically close to BD-BR | **100** ⚠️ | 50 |
| `120.203.25[.]201` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `120.48.109[.]59` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 9 |
| `101.47.158[.]137` | SG | BYTEPLUS | **100** ⚠️ | 18 |
| `196.11.86[.]134` | MW | SIMBANET MALAWI LIMITED | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 195 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 130 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 44 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (199 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 39 |
| AbuseIPDB score 16 below threshold 25 | 26 |
| AbuseIPDB score 5 below threshold 25 | 15 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 115 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 286 cases |
| Tool 34  | Credential Extractor        | ✅ 174 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 199 filtered (69.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 22 recon entry/entries in table (5 group(s) consolidating 37 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-17T04:19:04Z_
