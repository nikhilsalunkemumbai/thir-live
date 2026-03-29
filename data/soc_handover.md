# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T14:32:21Z |
| **Shift Time** | 14:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **26** |
| Confirmed Threats | **20** |
| False Positives Filtered | **6** (23.1%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **12** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **14** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 2 |
| `Unknown` | 1 |
| `guest` | 1 |
| `Nobody` | 1 |
| `Guest` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e` | 1 |
| `333` | 1 |
| `99999` | 1 |
| `raspberry` | 1 |
| `12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Unknown` | `1q2w3e` | 1 |
| `admin` | `333` | 1 |
| `guest` | `99999` | 1 |
| `Nobody` | `raspberry` | 1 |
| `Guest` | `12345678` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **19** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS5410` | Bouygues Telecom SA | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS4808` | China Unicom Beijing Province Network | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS39775` | Limited Liability Company HyperNet | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |

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
| `18.116.101[.]220` | **4** | 2026-03-29 13:27 | 2026-03-29 13:34 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `150.246.249[.]149` | **2** | 2026-03-29 13:15 | 2026-03-29 13:31 | 1m | 0 | `T1592` | 🟢 LOW |
| `111.70.29[.]124` | 1 | 2026-03-29 13:07 | 2026-03-29 13:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-29 13:52 | 2026-03-29 13:52 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.118.108[.]206` | 1 | 2026-03-29 13:33 | 2026-03-29 13:33 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.49.149[.]159` | 1 | 2026-03-29 13:26 | 2026-03-29 13:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.54.22[.]11` | 1 | 2026-03-29 14:13 | 2026-03-29 14:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.170.1[.]244` | 1 | 2026-03-29 13:04 | 2026-03-29 13:05 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.212.65[.]237` | 1 | 2026-03-29 12:55 | 2026-03-29 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.117.96[.]174` | 1 | 2026-03-29 14:13 | 2026-03-29 14:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.25.253[.]242` | 1 | 2026-03-29 13:13 | 2026-03-29 13:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.219.2[.]91` | 1 | 2026-03-29 14:14 | 2026-03-29 14:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `62.192.46[.]73` | 1 | 2026-03-29 13:12 | 2026-03-29 13:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.116.85[.]183` | 1 | 2026-03-29 12:52 | 2026-03-29 12:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.30.248[.]213` | 1 | 2026-03-29 14:04 | 2026-03-29 14:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-03-29 13:24 | 2026-03-29 13:24 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `85.30.248[.]213` | RU | PJSC Rostelecom | **100** ⚠️ | 43 |
| `14.49.149[.]159` | KR | Korea Telecom | **100** ⚠️ | 12 |
| `27.219.2[.]91` | CN | China Unicom Shandong province network | **100** ⚠️ | 4 |
| `79.116.85[.]183` | ES | Digi Spain Telecom | **100** ⚠️ | 6 |
| `120.48.109[.]59` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `190.117.96[.]174` | PE | America Movil Peru S.A.C. | **100** ⚠️ | 50 |
| `196.25.253[.]242` | ZA | Telkom SA Limited | **100** ⚠️ | 10 |
| `62.192.46[.]73` | RU | LLC HyperNet | **100** ⚠️ | 2 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `111.70.29[.]124` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 13 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 26 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (23.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 16 recon entry/entries in table (2 group(s) consolidating 6 session(s)).

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
_Report time: 2026-03-29T14:32:21Z_
