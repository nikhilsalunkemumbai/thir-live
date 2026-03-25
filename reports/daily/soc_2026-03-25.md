# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T10:46:46Z |
| **Shift Time** | 10:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **72** |
| Confirmed Threats | **58** |
| False Positives Filtered | **14** (19.4%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **15** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **70** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **54** |
| Unique Credential Pairs | **53** |
| Unique Usernames | **51** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `nobody` | 3 |
| `root` | 2 |
| `Root` | 1 |
| `Operator` | 1 |
| `test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Pratap@123` | 2 |
| `112233` | 1 |
| `webadmin` | 1 |
| `nobody2020` | 1 |
| `qwerty123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `Pratap@123` | 2 |
| `nobody` | `112233` | 1 |
| `Root` | `webadmin` | 1 |
| `nobody` | `nobody2020` | 1 |
| `Operator` | `qwerty123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Pratap@123` | `157.66.144.16` | 2026-03-25T10:04:49 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **26** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6274d242d890

| Field | Detail |
|---|---|
| **Source IP** | `157.66.144[.]16` |
| **First Seen** | 2026-03-25 10:04 |
| **Last Seen** | 2026-03-25 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 10:04:49` | `cowrie.session.connect` |
| `2026-03-25 10:04:49` | `cowrie.client.version` |
| `2026-03-25 10:04:49` | `cowrie.client.kex` |
| `2026-03-25 10:04:49` | `cowrie.login.success` |
| `2026-03-25 10:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.144[.]16` to AbuseIPDB if not already reported
- [ ] Block `157.66.144[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffb2029fe27

| Field | Detail |
|---|---|
| **Source IP** | `157.66.144[.]16` |
| **First Seen** | 2026-03-25 10:04 |
| **Last Seen** | 2026-03-25 10:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 10:04:49` | `cowrie.session.connect` |
| `2026-03-25 10:04:49` | `cowrie.client.version` |
| `2026-03-25 10:04:49` | `cowrie.client.kex` |
| `2026-03-25 10:04:49` | `cowrie.login.success` |
| `2026-03-25 10:04:49` | `cowrie.session.params` |
| `2026-03-25 10:04:49` | `cowrie.command.input` |
| `2026-03-25 10:04:50` | `cowrie.log.closed` |
| `2026-03-25 10:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.66.144[.]16` to AbuseIPDB if not already reported
- [ ] Block `157.66.144[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.88.137[.]213` | **15** | 2026-03-25 10:10 | 2026-03-25 10:30 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.248.8[.]33` | **15** | 2026-03-25 10:13 | 2026-03-25 10:28 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.133.99[.]235` | **13** | 2026-03-25 10:15 | 2026-03-25 10:44 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `1.235.192[.]130` | 1 | 2026-03-25 09:55 | 2026-03-25 09:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-03-25 10:14 | 2026-03-25 10:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.12[.]202` | 1 | 2026-03-25 10:15 | 2026-03-25 10:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.73.168[.]9` | 1 | 2026-03-25 08:50 | 2026-03-25 08:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.237[.]122` | 1 | 2026-03-25 10:07 | 2026-03-25 10:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.84[.]77` | 1 | 2026-03-25 10:16 | 2026-03-25 10:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.53[.]82` | 1 | 2026-03-25 08:50 | 2026-03-25 08:51 | 29s | 0 | `T1592` | 🟢 LOW |
| `185.242.3[.]105` | 1 | 2026-03-25 10:36 | 2026-03-25 10:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `187.8.3[.]230` | 1 | 2026-03-25 09:24 | 2026-03-25 09:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.226.132[.]113` | 1 | 2026-03-25 10:34 | 2026-03-25 10:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.159.21[.]170` | 1 | 2026-03-25 09:32 | 2026-03-25 09:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.180.2[.]62` | 1 | 2026-03-25 09:34 | 2026-03-25 09:34 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]59` | 1 | 2026-03-25 09:47 | 2026-03-25 09:47 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
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
| `121.73.168[.]9` | NZ | One New Zealand Group Limited | **100** ⚠️ | 4 |
| `34.133.99[.]235` | US | Google LLC | **100** ⚠️ | 5 |
| `1.235.192[.]130` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `122.187.237[.]122` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 28 |
| `188.226.132[.]113` | NL | Digital Ocean, Inc. | **100** ⚠️ | 37 |
| `180.184.84[.]77` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 24 |
| `183.171.53[.]82` | MY | Celcom Axiata Berhad | **100** ⚠️ | 18 |
| `120.48.20[.]170` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `197.248.8[.]33` | KE | Safaricom Limited | **100** ⚠️ | 50 |
| `157.66.144[.]16` | IN | BLUELINE BROADBAND PRIVATE LIMITED | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 57 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 52 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 72 cases |
| Tool 34  | Credential Extractor        | ✅ 54 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (19.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 16 recon entry/entries in table (3 group(s) consolidating 43 session(s)).

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
_Report time: 2026-03-25T10:46:46Z_
