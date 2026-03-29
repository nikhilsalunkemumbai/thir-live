# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T18:39:20Z |
| **Shift Time** | 18:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **125** |
| Confirmed Threats | **56** |
| False Positives Filtered | **69** (55.2%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **14** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **125** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **10** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `mysql` | 3 |
| `Test` | 2 |
| `unknown` | 2 |
| `ubnt` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `toor` | 2 |
| `123456789` | 1 |
| `77` | 1 |
| `user2019` | 1 |
| `333` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Test` | `123456789` | 1 |
| `ubnt` | `77` | 1 |
| `user` | `user2019` | 1 |
| `mysql` | `toor` | 1 |
| `unknown` | `333` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **28** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS18881` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS25490` | PJSC Rostelecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]3` | **23** | 2026-03-29 17:56 | 2026-03-29 18:01 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `39.99.214[.]254` | **3** | 2026-03-29 16:58 | 2026-03-29 16:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]180` | **3** | 2026-03-29 16:34 | 2026-03-29 16:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]94` | **3** | 2026-03-29 16:35 | 2026-03-29 16:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]233` | **3** | 2026-03-29 16:34 | 2026-03-29 16:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `186.215.204[.]109` | **2** | 2026-03-29 17:03 | 2026-03-29 17:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.61[.]119` | **2** | 2026-03-29 17:53 | 2026-03-29 17:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.23.254[.]239` | 1 | 2026-03-29 16:33 | 2026-03-29 16:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.210[.]119` | 1 | 2026-03-29 17:12 | 2026-03-29 17:12 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.196.52[.]107` | 1 | 2026-03-29 17:12 | 2026-03-29 17:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.166.253[.]226` | 1 | 2026-03-29 18:11 | 2026-03-29 18:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.235.236[.]63` | 1 | 2026-03-29 16:51 | 2026-03-29 16:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]50` | 1 | 2026-03-29 17:12 | 2026-03-29 17:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-03-29 17:52 | 2026-03-29 17:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.154.80[.]51` | 1 | 2026-03-29 16:32 | 2026-03-29 16:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.93.167[.]144` | 1 | 2026-03-29 18:07 | 2026-03-29 18:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]163` | 1 | 2026-03-29 18:26 | 2026-03-29 18:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-29 16:56 | 2026-03-29 16:56 | 47s | 0 | `T1592` | 🟢 LOW |
| `59.120.8[.]61` | 1 | 2026-03-29 18:12 | 2026-03-29 18:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.141[.]202` | 1 | 2026-03-29 18:02 | 2026-03-29 18:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.224[.]228` | 1 | 2026-03-29 17:39 | 2026-03-29 17:39 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.205.236[.]231` | 1 | 2026-03-29 17:07 | 2026-03-29 17:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.227.142[.]225` | 1 | 2026-03-29 17:52 | 2026-03-29 17:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.239.0[.]202` | 1 | 2026-03-29 18:31 | 2026-03-29 18:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `66.132.195[.]94` | US | Censys, Inc. | **100** ⚠️ | 9 |
| `102.23.254[.]239` | ZA | JENNY INTERNET (PTY) LTD | **100** ⚠️ | 30 |
| `183.247.171[.]186` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `83.239.0[.]202` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 31 |
| `220.93.167[.]144` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `66.132.224[.]228` | US | Censys, Inc. | **100** ⚠️ | 7 |
| `178.178.222[.]50` | RU | PJSC MegaFon | **100** ⚠️ | 45 |
| `66.132.186[.]180` | US | Censys, Inc. | **100** ⚠️ | 12 |
| `66.205.236[.]231` | CA | UPTele Inc. | **100** ⚠️ | 8 |
| `66.132.224[.]233` | US | Censys, Inc. | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |

---

## 🔕 False Positive Summary (69 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 42 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 125 cases |
| Tool 34  | Credential Extractor        | ✅ 14 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 69 filtered (55.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 24 recon entry/entries in table (7 group(s) consolidating 39 session(s)).

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
_Report time: 2026-03-29T18:39:20Z_
