# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T08:30:06Z |
| **Shift Time** | 08:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **27** |
| Confirmed Threats | **26** |
| False Positives Filtered | **1** (3.7%) |
| Unique Attacker IPs | **9** |
| Countries of Origin | **7** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **24** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **10** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `admin` | 2 |
| `a` | 2 |
| `Test` | 1 |
| `nil` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root` | 2 |
| `admin` | 2 |
| `a` | 2 |
| `` | 2 |
| `3245gs5662d34` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root` | 2 |
| `a` | `a` | 2 |
| `root` | `3245gs5662d34` | 1 |
| `root` | `admin` | 1 |
| `Test` | `test123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3245gs5662d34` | `172.208.24.217` | 2026-03-21T07:52:06 |
| `root` | `admin` | `178.175.167.17` | 2026-03-21T07:54:10 |
| `root` | `` | `183.87.217.222` | 2026-03-21T08:20:02 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **9** |
| Unique ASNs | **7** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS45117` | Ishan's Network | 1 | HIGH |
| `AS43132` | PJSC Rostelecom | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS211504` | STUDIO AN-TV SRL | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-00515dae19bf

| Field | Detail |
|---|---|
| **Source IP** | `172.208.24[.]217` |
| **First Seen** | 2026-03-21 07:52 |
| **Last Seen** | 2026-03-21 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 07:52:06` | `cowrie.login.success` |
| `2026-03-21 07:52:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.208.24[.]217` to AbuseIPDB if not already reported
- [ ] Block `172.208.24[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f20fbbb0810

| Field | Detail |
|---|---|
| **Source IP** | `178.175.167[.]17` |
| **First Seen** | 2026-03-21 07:54 |
| **Last Seen** | 2026-03-21 07:55 |
| **Session Duration** | 90s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 07:54:06` | `cowrie.session.connect` |
| `2026-03-21 07:54:06` | `cowrie.client.version` |
| `2026-03-21 07:54:07` | `cowrie.client.kex` |
| `2026-03-21 07:54:09` | `cowrie.login.failed` |
| `2026-03-21 07:54:10` | `cowrie.login.success` |
| `2026-03-21 07:54:11` | `cowrie.session.params` |
| `2026-03-21 07:54:11` | `cowrie.command.input` |
| `2026-03-21 07:54:11` | `cowrie.command.failed` |
| `2026-03-21 07:54:11` | `cowrie.log.closed` |
| `2026-03-21 07:54:11` | `cowrie.session.params` |
| `2026-03-21 07:54:11` | `cowrie.command.input` |
| `2026-03-21 07:54:11` | `cowrie.log.closed` |
| `2026-03-21 07:54:12` | `cowrie.session.params` |
| `2026-03-21 07:54:12` | `cowrie.command.input` |
| `2026-03-21 07:54:12` | `cowrie.log.closed` |
| `2026-03-21 07:54:13` | `cowrie.session.params` |
| `2026-03-21 07:54:13` | `cowrie.command.input` |
| `2026-03-21 07:54:13` | `cowrie.log.closed` |
| `2026-03-21 07:54:13` | `cowrie.session.params` |
| `2026-03-21 07:54:13` | `cowrie.command.input` |
| `2026-03-21 07:54:14` | `cowrie.log.closed` |
| `2026-03-21 07:54:14` | `cowrie.session.params` |
| `2026-03-21 07:54:14` | `cowrie.command.input` |
| `2026-03-21 07:54:14` | `cowrie.log.closed` |
| `2026-03-21 07:54:15` | `cowrie.session.params` |
| `2026-03-21 07:54:15` | `cowrie.command.input` |
| `2026-03-21 07:54:15` | `cowrie.log.closed` |
| `2026-03-21 07:54:15` | `cowrie.session.params` |
| `2026-03-21 07:54:15` | `cowrie.command.input` |
| `2026-03-21 07:54:16` | `cowrie.log.closed` |
| `2026-03-21 07:54:16` | `cowrie.session.params` |
| `2026-03-21 07:54:16` | `cowrie.command.input` |
| `2026-03-21 07:54:16` | `cowrie.log.closed` |
| `2026-03-21 07:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.175.167[.]17` to AbuseIPDB if not already reported
- [ ] Block `178.175.167[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee11916172b7

| Field | Detail |
|---|---|
| **Source IP** | `183.87.217[.]222` |
| **First Seen** | 2026-03-21 08:19 |
| **Last Seen** | 2026-03-21 08:20 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 08:19:27` | `cowrie.session.connect` |
| `2026-03-21 08:19:28` | `cowrie.client.version` |
| `2026-03-21 08:19:30` | `cowrie.client.kex` |
| `2026-03-21 08:20:02` | `cowrie.login.success` |
| `2026-03-21 08:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.87.217[.]222` to AbuseIPDB if not already reported
- [ ] Block `183.87.217[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.87.217[.]222` | **11** | 2026-03-21 08:10 | 2026-03-21 08:19 | 9m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.85[.]58` | **6** | 2026-03-21 08:21 | 2026-03-21 08:25 | 8m | 0 | `T1592` | 🟢 LOW |
| `20.169.83[.]157` | **2** | 2026-03-21 08:24 | 2026-03-21 08:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-21 08:27 | 2026-03-21 08:27 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.208.24[.]217` | 1 | 2026-03-21 07:52 | 2026-03-21 07:52 | 6s | 0 | `T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-03-21 08:06 | 2026-03-21 08:06 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.183.82[.]70` | 1 | 2026-03-21 08:05 | 2026-03-21 08:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `112.168.71[.]109` | KR | Sudogwongangnambonbujang | **100** ⚠️ | 42 |
| `179.184.85[.]167` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 30 |
| `178.175.167[.]17` | MD | STUDIO AN-TV SRL | **100** ⚠️ | 6 |
| `183.87.217[.]222` | IN | Ishan Netsol Pvt Ltd | **100** ⚠️ | 37 |
| `172.208.24[.]217` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `62.183.82[.]70` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 50 |
| `101.126.85[.]58` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 13 |
| `20.169.83[.]157` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `52.176.138[.]192` | US | Microsoft Corporation | **44** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 27 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 9 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (3.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 7 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 7 recon entry/entries in table (3 group(s) consolidating 19 session(s)).

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
_Report time: 2026-03-21T08:30:06Z_
