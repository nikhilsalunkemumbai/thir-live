# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T06:10:23Z |
| **Shift Time** | 06:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **299** |
| Confirmed Threats | **262** |
| False Positives Filtered | **37** (12.4%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **7** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **280** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **74** |
| Unique Credential Pairs | **72** |
| Unique Usernames | **46** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `deploy` | 2 |
| `oracle` | 2 |
| `elasticsearch` | 2 |
| `uftp` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 9 |
| `` | 3 |
| `a` | 2 |
| `Aa123456` | 1 |
| `mysql` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `a` | `a` | 2 |
| `root` | `` | 2 |
| `root` | `Aa123456` | 1 |
| `mysql` | `mysql` | 1 |
| `app` | `app` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa123456` | `113.141.70.64` | 2026-04-24T03:31:35 |
| `root` | `passwd` | `113.141.70.64` | 2026-04-24T03:33:09 |
| `root` | `Ac123456` | `113.141.70.64` | 2026-04-24T03:33:12 |
| `root` | `1qazXSW@` | `113.141.70.64` | 2026-04-24T03:33:13 |
| `root` | `123456789` | `113.141.70.64` | 2026-04-24T03:33:14 |
| `root` | `111111` | `113.141.70.64` | 2026-04-24T03:33:21 |
| `root` | `a123456A` | `113.141.70.64` | 2026-04-24T03:33:29 |
| `root` | `1qazxsw2` | `113.141.70.64` | 2026-04-24T03:33:35 |
| `root` | `qwerty` | `113.141.70.64` | 2026-04-24T03:33:37 |
| `root` | `QQ123456` | `113.141.70.64` | 2026-04-24T03:33:37 |
| `root` | `toor` | `113.141.70.64` | 2026-04-24T03:33:42 |
| `root` | `qq123456` | `113.141.70.64` | 2026-04-24T03:33:42 |
| `root` | `aB123456` | `113.141.70.64` | 2026-04-24T03:33:44 |
| `root` | `aa123456` | `113.141.70.64` | 2026-04-24T03:33:46 |
| `root` | `A123456a` | `113.141.70.64` | 2026-04-24T03:33:52 |
| `root` | `rootroot` | `113.141.70.64` | 2026-04-24T03:34:00 |
| `root` | `!QAZ@WSX` | `113.141.70.64` | 2026-04-24T03:34:08 |
| `root` | `` | `118.178.225.236` | 2026-04-24T05:31:36 |
| `root` | `` | `31.56.209.39` | 2026-04-24T05:31:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **299** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 225 |
| OpenSSH | 12 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 59 | 1 |
| `c118de82e19e...` | Mirai/variant | 12 | 3 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Go SSH scanner | 165 | 2 | — |
| `0a07365cc01f...` | Go SSH scanner | 59 | 1 | Generic scanner |
| `c118de82e19e...` | OpenSSH | 12 | 3 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **10** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 2 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS5483` | Magyar Telekom Plc. | 1 | MEDIUM |
| `AS216472` | High Speed For Internet Services L.L.C | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS209373` | SWISSNET LLC | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (19)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cb699fb9a8f8

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:30 |
| **Last Seen** | 2026-04-24 03:31 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:30:54` | `cowrie.session.connect` |
| `2026-04-24 03:30:54` | `cowrie.client.version` |
| `2026-04-24 03:31:30` | `cowrie.client.kex` |
| `2026-04-24 03:31:35` | `cowrie.login.success` |
| `2026-04-24 03:31:35` | `cowrie.session.params` |
| `2026-04-24 03:31:35` | `cowrie.command.input` |
| `2026-04-24 03:31:35` | `cowrie.log.closed` |
| `2026-04-24 03:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514f6aa652e2

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:34 |
| **Session Duration** | 116s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:13` | `cowrie.session.connect` |
| `2026-04-24 03:32:13` | `cowrie.client.version` |
| `2026-04-24 03:34:08` | `cowrie.client.kex` |
| `2026-04-24 03:34:08` | `cowrie.login.success` |
| `2026-04-24 03:34:09` | `cowrie.session.params` |
| `2026-04-24 03:34:09` | `cowrie.command.input` |
| `2026-04-24 03:34:09` | `cowrie.log.closed` |
| `2026-04-24 03:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09859b5b156f

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 69s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:34` | `cowrie.session.connect` |
| `2026-04-24 03:33:43` | `cowrie.client.version` |
| `2026-04-24 03:33:43` | `cowrie.client.kex` |
| `2026-04-24 03:33:44` | `cowrie.login.success` |
| `2026-04-24 03:33:44` | `cowrie.session.params` |
| `2026-04-24 03:33:44` | `cowrie.command.input` |
| `2026-04-24 03:33:44` | `cowrie.log.closed` |
| `2026-04-24 03:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-831ecd3be85b

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:36` | `cowrie.session.connect` |
| `2026-04-24 03:32:36` | `cowrie.client.version` |
| `2026-04-24 03:33:29` | `cowrie.client.kex` |
| `2026-04-24 03:33:29` | `cowrie.login.success` |
| `2026-04-24 03:33:30` | `cowrie.session.params` |
| `2026-04-24 03:33:30` | `cowrie.command.input` |
| `2026-04-24 03:33:30` | `cowrie.log.closed` |
| `2026-04-24 03:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9894c5fcb125

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:38` | `cowrie.session.connect` |
| `2026-04-24 03:32:38` | `cowrie.client.version` |
| `2026-04-24 03:33:41` | `cowrie.client.kex` |
| `2026-04-24 03:33:42` | `cowrie.login.success` |
| `2026-04-24 03:33:42` | `cowrie.session.params` |
| `2026-04-24 03:33:42` | `cowrie.command.input` |
| `2026-04-24 03:33:42` | `cowrie.log.closed` |
| `2026-04-24 03:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c36548f8256

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:39` | `cowrie.session.connect` |
| `2026-04-24 03:33:12` | `cowrie.client.version` |
| `2026-04-24 03:33:13` | `cowrie.client.kex` |
| `2026-04-24 03:33:13` | `cowrie.login.success` |
| `2026-04-24 03:33:13` | `cowrie.session.params` |
| `2026-04-24 03:33:13` | `cowrie.command.input` |
| `2026-04-24 03:33:14` | `cowrie.log.closed` |
| `2026-04-24 03:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7bc306d343e

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:40` | `cowrie.session.connect` |
| `2026-04-24 03:32:40` | `cowrie.client.version` |
| `2026-04-24 03:33:37` | `cowrie.client.kex` |
| `2026-04-24 03:33:37` | `cowrie.login.success` |
| `2026-04-24 03:33:38` | `cowrie.session.params` |
| `2026-04-24 03:33:38` | `cowrie.command.input` |
| `2026-04-24 03:33:38` | `cowrie.log.closed` |
| `2026-04-24 03:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731b2184c9d7

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:41` | `cowrie.session.connect` |
| `2026-04-24 03:32:41` | `cowrie.client.version` |
| `2026-04-24 03:33:35` | `cowrie.client.kex` |
| `2026-04-24 03:33:35` | `cowrie.login.success` |
| `2026-04-24 03:33:36` | `cowrie.session.params` |
| `2026-04-24 03:33:36` | `cowrie.command.input` |
| `2026-04-24 03:33:36` | `cowrie.log.closed` |
| `2026-04-24 03:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b953b1e510a

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:43` | `cowrie.session.connect` |
| `2026-04-24 03:32:43` | `cowrie.client.version` |
| `2026-04-24 03:33:37` | `cowrie.client.kex` |
| `2026-04-24 03:33:37` | `cowrie.login.success` |
| `2026-04-24 03:33:38` | `cowrie.session.params` |
| `2026-04-24 03:33:38` | `cowrie.command.input` |
| `2026-04-24 03:33:38` | `cowrie.log.closed` |
| `2026-04-24 03:33:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed4bbbe1f773

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:45` | `cowrie.session.connect` |
| `2026-04-24 03:32:45` | `cowrie.client.version` |
| `2026-04-24 03:33:45` | `cowrie.client.kex` |
| `2026-04-24 03:33:46` | `cowrie.login.success` |
| `2026-04-24 03:33:46` | `cowrie.session.params` |
| `2026-04-24 03:33:46` | `cowrie.command.input` |
| `2026-04-24 03:33:46` | `cowrie.log.closed` |
| `2026-04-24 03:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb05c57f8c6d

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:45` | `cowrie.session.connect` |
| `2026-04-24 03:32:47` | `cowrie.client.version` |
| `2026-04-24 03:33:41` | `cowrie.client.kex` |
| `2026-04-24 03:33:42` | `cowrie.login.success` |
| `2026-04-24 03:33:42` | `cowrie.session.params` |
| `2026-04-24 03:33:42` | `cowrie.command.input` |
| `2026-04-24 03:33:42` | `cowrie.log.closed` |
| `2026-04-24 03:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9f8ded5764

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:47` | `cowrie.session.connect` |
| `2026-04-24 03:33:21` | `cowrie.client.version` |
| `2026-04-24 03:33:21` | `cowrie.client.kex` |
| `2026-04-24 03:33:21` | `cowrie.login.success` |
| `2026-04-24 03:33:22` | `cowrie.session.params` |
| `2026-04-24 03:33:22` | `cowrie.command.input` |
| `2026-04-24 03:33:22` | `cowrie.log.closed` |
| `2026-04-24 03:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723ebaea81b7

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:48` | `cowrie.session.connect` |
| `2026-04-24 03:32:48` | `cowrie.client.version` |
| `2026-04-24 03:33:51` | `cowrie.client.kex` |
| `2026-04-24 03:33:52` | `cowrie.login.success` |
| `2026-04-24 03:33:52` | `cowrie.session.params` |
| `2026-04-24 03:33:52` | `cowrie.command.input` |
| `2026-04-24 03:33:52` | `cowrie.log.closed` |
| `2026-04-24 03:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c684b5a08c8

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:52` | `cowrie.session.connect` |
| `2026-04-24 03:33:09` | `cowrie.client.version` |
| `2026-04-24 03:33:09` | `cowrie.client.kex` |
| `2026-04-24 03:33:09` | `cowrie.login.success` |
| `2026-04-24 03:33:10` | `cowrie.session.params` |
| `2026-04-24 03:33:10` | `cowrie.command.input` |
| `2026-04-24 03:33:10` | `cowrie.log.closed` |
| `2026-04-24 03:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d14ed521710a

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:55` | `cowrie.session.connect` |
| `2026-04-24 03:32:55` | `cowrie.client.version` |
| `2026-04-24 03:33:12` | `cowrie.client.kex` |
| `2026-04-24 03:33:12` | `cowrie.login.success` |
| `2026-04-24 03:33:13` | `cowrie.session.params` |
| `2026-04-24 03:33:13` | `cowrie.command.input` |
| `2026-04-24 03:33:13` | `cowrie.log.closed` |
| `2026-04-24 03:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c20a627c12be

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:33 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:58` | `cowrie.session.connect` |
| `2026-04-24 03:32:58` | `cowrie.client.version` |
| `2026-04-24 03:33:14` | `cowrie.client.kex` |
| `2026-04-24 03:33:14` | `cowrie.login.success` |
| `2026-04-24 03:33:15` | `cowrie.session.params` |
| `2026-04-24 03:33:15` | `cowrie.command.input` |
| `2026-04-24 03:33:15` | `cowrie.log.closed` |
| `2026-04-24 03:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9706dd33882c

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-24 03:32 |
| **Last Seen** | 2026-04-24 03:34 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 03:32:59` | `cowrie.session.connect` |
| `2026-04-24 03:32:59` | `cowrie.client.version` |
| `2026-04-24 03:34:00` | `cowrie.client.kex` |
| `2026-04-24 03:34:00` | `cowrie.login.success` |
| `2026-04-24 03:34:01` | `cowrie.session.params` |
| `2026-04-24 03:34:01` | `cowrie.command.input` |
| `2026-04-24 03:34:01` | `cowrie.log.closed` |
| `2026-04-24 03:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebfcbc17a5c9

| Field | Detail |
|---|---|
| **Source IP** | `118.178.225[.]236` |
| **First Seen** | 2026-04-24 05:31 |
| **Last Seen** | 2026-04-24 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 05:31:36` | `cowrie.session.connect` |
| `2026-04-24 05:31:36` | `cowrie.client.version` |
| `2026-04-24 05:31:36` | `cowrie.client.kex` |
| `2026-04-24 05:31:36` | `cowrie.login.success` |
| `2026-04-24 05:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.178.225[.]236` to AbuseIPDB if not already reported
- [ ] Block `118.178.225[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f61477b39b4

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-24 05:31 |
| **Last Seen** | 2026-04-24 05:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps" | sh, cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps
` |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 05:31:40` | `cowrie.session.connect` |
| `2026-04-24 05:31:40` | `cowrie.client.version` |
| `2026-04-24 05:31:40` | `cowrie.client.kex` |
| `2026-04-24 05:31:41` | `cowrie.login.success` |
| `2026-04-24 05:31:41` | `cowrie.client.size` |
| `2026-04-24 05:31:42` | `cowrie.session.params` |
| `2026-04-24 05:31:42` | `cowrie.command.input` |
| `2026-04-24 05:31:42` | `cowrie.command.input` |
| `2026-04-24 05:31:42` | `cowrie.command.failed` |
| `2026-04-24 05:31:42` | `cowrie.command.input` |
| `2026-04-24 05:31:47` | `cowrie.log.closed` |
| `2026-04-24 05:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.141.70[.]64` | **226** | 2026-04-24 03:25 | 2026-04-24 03:33 | 414m | 42 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.178.225[.]236` | **9** | 2026-04-24 05:31 | 2026-04-24 05:31 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.164[.]82` | **5** | 2026-04-24 06:04 | 2026-04-24 06:06 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.214.179[.]202` | 1 | 2026-04-24 04:50 | 2026-04-24 04:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `195.62.50[.]220` | 1 | 2026-04-24 03:24 | 2026-04-24 03:24 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-24 03:54 | 2026-04-24 03:56 | 86s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `118.178.225[.]236` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `31.56.209[.]39` | NL | SWISSNET LLC | **100** ⚠️ | 43 |
| `195.62.50[.]220` | TR | hiperonline iletisim hizmetleri san. tic. ltd. sti. | **100** ⚠️ | 1 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `1.214.179[.]202` | KR | LG Uplus | **100** ⚠️ | 29 |
| `113.141.70[.]64` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 22 |
| `118.145.164[.]82` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 10 |
| `35.189.252[.]109` | BE | Google LLC | **75** | 0 |
| `84.3.104[.]220` | HU | Magyar Telekom Plc. | **52** | 0 |
| `47.103.144[.]128` | CN | Aliyun Computing Co., LTD | **45** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 237 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 54 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 299 cases |
| Tool 34  | Credential Extractor        | ✅ 74 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (12.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 19 priority case(s) shown individually · 6 recon entry/entries in table (3 group(s) consolidating 240 session(s)).

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
_Report time: 2026-04-24T06:10:23Z_
