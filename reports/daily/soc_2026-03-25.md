# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T08:48:22Z |
| **Shift Time** | 08:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **194** |
| Confirmed Threats | **58** |
| False Positives Filtered | **136** (70.1%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **12** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **193** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **10** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `operator` | 2 |
| `centos` | 2 |
| `Nobody` | 1 |
| `User` | 1 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwer1234` | 1 |
| `operator2003` | 1 |
| `654321` | 1 |
| `centos111` | 1 |
| `admin1234567` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Nobody` | `qwer1234` | 1 |
| `operator` | `operator2003` | 1 |
| `User` | `654321` | 1 |
| `centos` | `centos111` | 1 |
| `admin` | `admin1234567` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ab123456` | `47.83.161.4` | 2026-03-25T08:43:21 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **27** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS46562` | Performive LLC | 2 | LOW |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |
| `AS59497` | Buknet LLC | 1 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-32dfdef15c2d

| Field | Detail |
|---|---|
| **Source IP** | `47.83.161[.]4` |
| **First Seen** | 2026-03-25 08:43 |
| **Last Seen** | 2026-03-25 08:43 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 08:43:10` | `cowrie.session.connect` |
| `2026-03-25 08:43:12` | `cowrie.client.version` |
| `2026-03-25 08:43:12` | `cowrie.client.kex` |
| `2026-03-25 08:43:21` | `cowrie.login.success` |
| `2026-03-25 08:43:25` | `cowrie.session.params` |
| `2026-03-25 08:43:25` | `cowrie.command.input` |
| `2026-03-25 08:43:28` | `cowrie.log.closed` |
| `2026-03-25 08:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.161[.]4` to AbuseIPDB if not already reported
- [ ] Block `47.83.161[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]69` | **25** | 2026-03-25 07:49 | 2026-03-25 07:54 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.123[.]76` | **10** | 2026-03-25 08:18 | 2026-03-25 08:24 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `47.83.161[.]4` | **4** | 2026-03-25 08:40 | 2026-03-25 08:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.57[.]122` | **2** | 2026-03-25 08:33 | 2026-03-25 08:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.13.4[.]128` | 1 | 2026-03-25 07:25 | 2026-03-25 07:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.67.152[.]201` | 1 | 2026-03-25 08:08 | 2026-03-25 08:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.155.27[.]128` | 1 | 2026-03-25 06:59 | 2026-03-25 06:59 | 6s | 0 | `T1592` | 🟢 LOW |
| `111.70.12[.]84` | 1 | 2026-03-25 08:43 | 2026-03-25 08:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.66.124[.]148` | 1 | 2026-03-25 07:25 | 2026-03-25 07:25 | 10s | 0 | `T1592` | 🟢 LOW |
| `123.225.169[.]3` | 1 | 2026-03-25 07:15 | 2026-03-25 07:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `133.175.49[.]125` | 1 | 2026-03-25 07:04 | 2026-03-25 07:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `182.95.127[.]42` | 1 | 2026-03-25 07:19 | 2026-03-25 07:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `184.81.254[.]140` | 1 | 2026-03-25 08:15 | 2026-03-25 08:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.59[.]226` | 1 | 2026-03-25 07:40 | 2026-03-25 07:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.235.64[.]126` | 1 | 2026-03-25 07:19 | 2026-03-25 07:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.208.53[.]84` | 1 | 2026-03-25 08:34 | 2026-03-25 08:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.226.255[.]240` | 1 | 2026-03-25 08:10 | 2026-03-25 08:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.120.105[.]236` | 1 | 2026-03-25 07:31 | 2026-03-25 07:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `59.7.135[.]117` | 1 | 2026-03-25 07:44 | 2026-03-25 07:44 | 13s | 0 | `T1592` | 🟢 LOW |
| `70.89.116[.]5` | 1 | 2026-03-25 07:07 | 2026-03-25 07:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `111.70.12[.]84` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `58.226.255[.]240` | KR | SK Broadband Co Ltd | **100** ⚠️ | 39 |
| `133.175.49[.]125` | JP | ARTERIA Networks Corporation | **100** ⚠️ | 14 |
| `223.235.64[.]126` | IN | ABTS DELHI, | **100** ⚠️ | 41 |
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 0 |
| `103.67.152[.]201` | IN | Netfirre Communications Pvt Ltd | **100** ⚠️ | 0 |
| `104.155.27[.]128` | BE | Google LLC | **100** ⚠️ | 0 |
| `184.81.254[.]140` | US | Windstream Communications LLC | **100** ⚠️ | 0 |
| `47.83.161[.]4` | HK | Alibaba Cloud LLC | **100** ⚠️ | 0 |
| `121.66.124[.]148` | KR | LG Uplus | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (136 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 130 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 194 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 136 filtered (70.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 20 recon entry/entries in table (4 group(s) consolidating 41 session(s)).

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
_Report time: 2026-03-25T08:48:22Z_
