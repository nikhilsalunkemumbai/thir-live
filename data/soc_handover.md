# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T10:45:22Z |
| **Shift Time** | 10:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **297** |
| Confirmed Threats | **214** |
| False Positives Filtered | **83** (28.0%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **14** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **286** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **46** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **30** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **11** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `user` | 3 |
| `blank` | 2 |
| `default` | 2 |
| `es` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 4 |
| `update` | 1 |
| `test2014` | 1 |
| `cable` | 1 |
| `asdfgh` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `update` | `update` | 1 |
| `test` | `test2014` | 1 |
| `blank` | `cable` | 1 |
| `Nobody` | `asdfgh` | 1 |
| `user` | `user2015` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWERTY123` | `113.141.70.64` | 2026-03-27T10:23:37 |
| `root` | `A123456a` | `113.141.70.64` | 2026-03-27T10:24:33 |
| `root` | `toor` | `113.141.70.64` | 2026-03-27T10:24:50 |
| `root` | `123456789` | `113.141.70.64` | 2026-03-27T10:24:58 |
| `root` | `rootroot` | `113.141.70.64` | 2026-03-27T10:25:00 |
| `root` | `111111` | `113.141.70.64` | 2026-03-27T10:25:14 |
| `root` | `aa123456` | `113.141.70.64` | 2026-03-27T10:25:14 |
| `root` | `1q2w3e4r` | `113.141.70.64` | 2026-03-27T10:25:18 |
| `root` | `1qazxsw2` | `113.141.70.64` | 2026-03-27T10:25:19 |
| `root` | `Ac123456` | `113.141.70.64` | 2026-03-27T10:25:33 |
| `root` | `Password` | `113.141.70.64` | 2026-03-27T10:25:35 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **24** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS20081` | NET2ATLANTA.COM LLC | 1 | MEDIUM |
| `AS4804` | Microplex PTY LTD | 1 | HIGH |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS137166` | Satellite Netcom Private Limited | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-964290f9503d

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:23 |
| **Last Seen** | 2026-03-27 10:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:23:29` | `cowrie.session.connect` |
| `2026-03-27 10:23:31` | `cowrie.client.version` |
| `2026-03-27 10:23:31` | `cowrie.client.kex` |
| `2026-03-27 10:23:37` | `cowrie.login.success` |
| `2026-03-27 10:23:37` | `cowrie.session.params` |
| `2026-03-27 10:23:37` | `cowrie.command.input` |
| `2026-03-27 10:23:38` | `cowrie.log.closed` |
| `2026-03-27 10:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb70be0f439c

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:23 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 116s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:23:39` | `cowrie.session.connect` |
| `2026-03-27 10:23:39` | `cowrie.client.version` |
| `2026-03-27 10:25:34` | `cowrie.client.kex` |
| `2026-03-27 10:25:35` | `cowrie.login.success` |
| `2026-03-27 10:25:35` | `cowrie.session.params` |
| `2026-03-27 10:25:35` | `cowrie.command.input` |
| `2026-03-27 10:25:35` | `cowrie.log.closed` |
| `2026-03-27 10:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ac4050b569

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:10` | `cowrie.session.connect` |
| `2026-03-27 10:25:18` | `cowrie.client.version` |
| `2026-03-27 10:25:18` | `cowrie.client.kex` |
| `2026-03-27 10:25:19` | `cowrie.login.success` |
| `2026-03-27 10:25:19` | `cowrie.session.params` |
| `2026-03-27 10:25:19` | `cowrie.command.input` |
| `2026-03-27 10:25:19` | `cowrie.log.closed` |
| `2026-03-27 10:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122002c2a50f

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:11` | `cowrie.session.connect` |
| `2026-03-27 10:24:11` | `cowrie.client.version` |
| `2026-03-27 10:25:14` | `cowrie.client.kex` |
| `2026-03-27 10:25:14` | `cowrie.login.success` |
| `2026-03-27 10:25:15` | `cowrie.session.params` |
| `2026-03-27 10:25:15` | `cowrie.command.input` |
| `2026-03-27 10:25:15` | `cowrie.log.closed` |
| `2026-03-27 10:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e168822ac6

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:12` | `cowrie.session.connect` |
| `2026-03-27 10:24:12` | `cowrie.client.version` |
| `2026-03-27 10:25:18` | `cowrie.client.kex` |
| `2026-03-27 10:25:18` | `cowrie.login.success` |
| `2026-03-27 10:25:19` | `cowrie.session.params` |
| `2026-03-27 10:25:19` | `cowrie.command.input` |
| `2026-03-27 10:25:19` | `cowrie.log.closed` |
| `2026-03-27 10:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c4b79beb2d

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:13` | `cowrie.session.connect` |
| `2026-03-27 10:24:13` | `cowrie.client.version` |
| `2026-03-27 10:25:14` | `cowrie.client.kex` |
| `2026-03-27 10:25:14` | `cowrie.login.success` |
| `2026-03-27 10:25:15` | `cowrie.session.params` |
| `2026-03-27 10:25:15` | `cowrie.command.input` |
| `2026-03-27 10:25:15` | `cowrie.log.closed` |
| `2026-03-27 10:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6561f314d365

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:24 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:16` | `cowrie.session.connect` |
| `2026-03-27 10:24:33` | `cowrie.client.version` |
| `2026-03-27 10:24:33` | `cowrie.client.kex` |
| `2026-03-27 10:24:33` | `cowrie.login.success` |
| `2026-03-27 10:24:34` | `cowrie.session.params` |
| `2026-03-27 10:24:34` | `cowrie.command.input` |
| `2026-03-27 10:24:34` | `cowrie.log.closed` |
| `2026-03-27 10:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a839846775f

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:24 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:16` | `cowrie.session.connect` |
| `2026-03-27 10:24:16` | `cowrie.client.version` |
| `2026-03-27 10:24:49` | `cowrie.client.kex` |
| `2026-03-27 10:24:50` | `cowrie.login.success` |
| `2026-03-27 10:24:50` | `cowrie.session.params` |
| `2026-03-27 10:24:50` | `cowrie.command.input` |
| `2026-03-27 10:24:50` | `cowrie.log.closed` |
| `2026-03-27 10:24:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfd64a2825f

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:23` | `cowrie.session.connect` |
| `2026-03-27 10:24:23` | `cowrie.client.version` |
| `2026-03-27 10:25:32` | `cowrie.client.kex` |
| `2026-03-27 10:25:33` | `cowrie.login.success` |
| `2026-03-27 10:25:33` | `cowrie.session.params` |
| `2026-03-27 10:25:33` | `cowrie.command.input` |
| `2026-03-27 10:25:33` | `cowrie.log.closed` |
| `2026-03-27 10:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33643a13235

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:24 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:26` | `cowrie.session.connect` |
| `2026-03-27 10:24:26` | `cowrie.client.version` |
| `2026-03-27 10:24:57` | `cowrie.client.kex` |
| `2026-03-27 10:24:58` | `cowrie.login.success` |
| `2026-03-27 10:24:58` | `cowrie.session.params` |
| `2026-03-27 10:24:58` | `cowrie.command.input` |
| `2026-03-27 10:24:58` | `cowrie.log.closed` |
| `2026-03-27 10:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301a9e8115f7

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-03-27 10:24 |
| **Last Seen** | 2026-03-27 10:25 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 10:24:27` | `cowrie.session.connect` |
| `2026-03-27 10:24:27` | `cowrie.client.version` |
| `2026-03-27 10:24:59` | `cowrie.client.kex` |
| `2026-03-27 10:25:00` | `cowrie.login.success` |
| `2026-03-27 10:25:00` | `cowrie.session.params` |
| `2026-03-27 10:25:00` | `cowrie.command.input` |
| `2026-03-27 10:25:00` | `cowrie.log.closed` |
| `2026-03-27 10:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.141.70[.]64` | **186** | 2026-03-27 10:16 | 2026-03-27 10:24 | 348m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.105[.]16` | **2** | 2026-03-27 09:27 | 2026-03-27 10:23 | 4m | 0 | `T1592` | 🟢 LOW |
| `101.13.9[.]48` | 1 | 2026-03-27 08:49 | 2026-03-27 08:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.158.138[.]179` | 1 | 2026-03-27 09:24 | 2026-03-27 09:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.31.39[.]188` | 1 | 2026-03-27 09:45 | 2026-03-27 09:45 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.23[.]253` | 1 | 2026-03-27 10:05 | 2026-03-27 10:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.74.243[.]231` | 1 | 2026-03-27 09:10 | 2026-03-27 09:10 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]74` | 1 | 2026-03-27 09:27 | 2026-03-27 09:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-27 10:16 | 2026-03-27 10:16 | 31s | 0 | `T1592` | 🟢 LOW |
| `172.184.211[.]65` | 1 | 2026-03-27 10:44 | 2026-03-27 10:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.184.218[.]49` | 1 | 2026-03-27 10:04 | 2026-03-27 10:04 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.59.178[.]23` | 1 | 2026-03-27 10:12 | 2026-03-27 10:12 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.54.85[.]220` | 1 | 2026-03-27 09:30 | 2026-03-27 09:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.234.9[.]218` | 1 | 2026-03-27 10:26 | 2026-03-27 10:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.103.205[.]196` | 1 | 2026-03-27 09:04 | 2026-03-27 09:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.64.30[.]151` | 1 | 2026-03-27 10:32 | 2026-03-27 10:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.157[.]131` | 1 | 2026-03-27 09:44 | 2026-03-27 09:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `179.184.218[.]49` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 23 |
| `36.64.30[.]151` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 39 |
| `2.54.85[.]220` | IL | Partner Communications Ltd. | **100** ⚠️ | 32 |
| `218.103.205[.]196` | HK | Hong Kong Telecommunications (HKT) Limited | **100** ⚠️ | 19 |
| `180.76.105[.]16` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `188.59.178[.]23` | TR | TURKCELL INTERNET | **100** ⚠️ | 9 |
| `103.158.138[.]179` | IN | Sneha Sales And Services Pvt.ltd. | **100** ⚠️ | 37 |
| `103.31.39[.]188` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 34 |
| `213.234.9[.]218` | RU | OAO Bank Petrokommerc | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 191 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 35 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |

---

## 🔕 False Positive Summary (83 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 81 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 297 cases |
| Tool 34  | Credential Extractor        | ✅ 46 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 83 filtered (28.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 17 recon entry/entries in table (2 group(s) consolidating 188 session(s)).

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
_Report time: 2026-03-27T10:45:22Z_
