# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T20:41:19Z |
| **Shift Time** | 20:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **45** |
| Confirmed Threats | **36** |
| False Positives Filtered | **9** (20.0%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **14** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **40** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **15** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `Debian` | 2 |
| `admin` | 2 |
| `Centos` | 2 |
| `postgres` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `raspberry` | 1 |
| `qwerty` | 1 |
| `test` | 1 |
| `qwerty1` | 1 |
| `ubuntu` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Debian` | `raspberry` | 1 |
| `root` | `qwerty` | 1 |
| `postgres` | `test` | 1 |
| `Debian` | `qwerty1` | 1 |
| `root` | `ubuntu` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty` | `20.42.11.19` | 2026-04-01T19:07:02 |
| `root` | `ubuntu` | `20.42.11.19` | 2026-04-01T19:21:27 |
| `root` | `secret` | `20.42.11.19` | 2026-04-01T19:35:42 |
| `root` | `qwerty123` | `20.42.11.19` | 2026-04-01T20:04:28 |
| `root` | `ubuntu123` | `20.42.11.19` | 2026-04-01T20:18:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **45** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 15 |
| Go SSH scanner | 6 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 15 | 15 |
| `16443846184e...` | Generic scanner | 6 | 2 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 15 | 15 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 2 | Generic scanner |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **25** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | HIGH |
| `AS3352` | TELEFONICA DE ESPANA S.A.U. | 1 | HIGH |
| `AS8434` | Telenor Sverige AB | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1858728033f0

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 19:07 |
| **Last Seen** | 2026-04-01 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 19:07:01` | `cowrie.session.connect` |
| `2026-04-01 19:07:01` | `cowrie.client.version` |
| `2026-04-01 19:07:02` | `cowrie.client.kex` |
| `2026-04-01 19:07:02` | `cowrie.login.success` |
| `2026-04-01 19:07:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a17eb4fc8a4

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 19:21 |
| **Last Seen** | 2026-04-01 19:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 19:21:25` | `cowrie.session.connect` |
| `2026-04-01 19:21:25` | `cowrie.client.version` |
| `2026-04-01 19:21:25` | `cowrie.client.kex` |
| `2026-04-01 19:21:27` | `cowrie.login.success` |
| `2026-04-01 19:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a2838ef267

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 19:35 |
| **Last Seen** | 2026-04-01 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 19:35:41` | `cowrie.session.connect` |
| `2026-04-01 19:35:41` | `cowrie.client.version` |
| `2026-04-01 19:35:42` | `cowrie.client.kex` |
| `2026-04-01 19:35:42` | `cowrie.login.success` |
| `2026-04-01 19:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7786ae7ac0

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 20:04 |
| **Last Seen** | 2026-04-01 20:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 20:04:25` | `cowrie.session.connect` |
| `2026-04-01 20:04:26` | `cowrie.client.version` |
| `2026-04-01 20:04:26` | `cowrie.client.kex` |
| `2026-04-01 20:04:28` | `cowrie.login.success` |
| `2026-04-01 20:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9db41dc8ba

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 20:18 |
| **Last Seen** | 2026-04-01 20:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 20:18:45` | `cowrie.session.connect` |
| `2026-04-01 20:18:45` | `cowrie.client.version` |
| `2026-04-01 20:18:45` | `cowrie.client.kex` |
| `2026-04-01 20:18:48` | `cowrie.login.success` |
| `2026-04-01 20:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `72.255.3[.]161` | **11** | 2026-04-01 18:58 | 2026-04-01 19:00 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `106.12.76[.]223` | 1 | 2026-04-01 19:20 | 2026-04-01 19:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.41[.]194` | 1 | 2026-04-01 20:40 | 2026-04-01 20:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.241.177[.]8` | 1 | 2026-04-01 20:15 | 2026-04-01 20:15 | 33s | 0 | `T1592` | 🟢 LOW |
| `120.194.50[.]39` | 1 | 2026-04-01 19:02 | 2026-04-01 19:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.52.236[.]2` | 1 | 2026-04-01 19:57 | 2026-04-01 19:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `161.139.152[.]2` | 1 | 2026-04-01 20:34 | 2026-04-01 20:34 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-01 19:59 | 2026-04-01 19:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]57` | 1 | 2026-04-01 19:39 | 2026-04-01 19:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.166.162[.]78` | 1 | 2026-04-01 20:12 | 2026-04-01 20:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.205.51[.]98` | 1 | 2026-04-01 20:00 | 2026-04-01 20:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.186.183[.]88` | 1 | 2026-04-01 19:33 | 2026-04-01 19:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.42.11[.]19` | 1 | 2026-04-01 19:50 | 2026-04-01 19:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.230.64[.]246` | 1 | 2026-04-01 19:20 | 2026-04-01 19:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.185.89[.]241` | 1 | 2026-04-01 19:19 | 2026-04-01 19:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.91[.]141` | 1 | 2026-04-01 19:21 | 2026-04-01 19:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.148[.]195` | 1 | 2026-04-01 20:37 | 2026-04-01 20:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.145.181[.]7` | 1 | 2026-04-01 19:39 | 2026-04-01 19:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.57.238[.]229` | 1 | 2026-04-01 20:32 | 2026-04-01 20:32 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.45.128[.]82` | 1 | 2026-04-01 19:50 | 2026-04-01 19:50 | 13s | 0 | `T1592` | 🟢 LOW |
| `85.231.90[.]253` | 1 | 2026-04-01 20:20 | 2026-04-01 20:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `188.186.183[.]88` | RU | CJSC ER-Telecom Holding Tyumen' branch | **100** ⚠️ | 10 |
| `69.57.238[.]229` | KN | Cable & Wireless Antigua and Barbuda Ltd | **100** ⚠️ | 14 |
| `46.59.91[.]141` | SE | Bahnhof AB | **100** ⚠️ | 6 |
| `213.230.64[.]246` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 50 |
| `111.70.41[.]194` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 18 |
| `181.205.51[.]98` | CO | Colombia Móvil | **100** ⚠️ | 40 |
| `85.231.90[.]253` | SE | Telenor Sverige AB | **100** ⚠️ | 14 |
| `81.45.128[.]82` | ES | Telefonica de Espana SAU | **100** ⚠️ | 17 |
| `180.166.162[.]78` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 45 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 21 recon entry/entries in table (1 group(s) consolidating 11 session(s)).

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
_Report time: 2026-04-01T20:41:19Z_
