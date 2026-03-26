# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T07:04:41Z |
| **Shift Time** | 07:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **38** |
| Confirmed Threats | **29** |
| False Positives Filtered | **9** (23.7%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **11** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **38** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **18** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ay` | 2 |
| `ocs` | 2 |
| `zhj` | 2 |
| `kingbase` | 1 |
| `centos` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345` | 2 |
| `1234` | 2 |
| `password` | 2 |
| `ocs123` | 2 |
| `zhj1234` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ay` | `1234` | 2 |
| `ocs` | `ocs123` | 2 |
| `zhj` | `zhj1234` | 2 |
| `kingbase` | `Kingbase123!` | 1 |
| `centos` | `p@ssword` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **19** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 3 | HIGH |
| `AS23956` | AmberIT Limited | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

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
| `118.179.200[.]67` | **5** | 2026-03-26 06:09 | 2026-03-26 06:20 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.142[.]202` | **4** | 2026-03-26 06:08 | 2026-03-26 06:22 | 2m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `118.179.102[.]248` | **3** | 2026-03-26 05:41 | 2026-03-26 05:46 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.84[.]77` | **3** | 2026-03-26 05:42 | 2026-03-26 05:44 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `164.90.159[.]214` | **2** | 2026-03-26 06:10 | 2026-03-26 06:14 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.55[.]67` | 1 | 2026-03-26 05:40 | 2026-03-26 05:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.39[.]216` | 1 | 2026-03-26 06:59 | 2026-03-26 07:00 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.251.207[.]141` | 1 | 2026-03-26 06:18 | 2026-03-26 06:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-03-26 06:09 | 2026-03-26 06:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.229.172[.]19` | 1 | 2026-03-26 06:13 | 2026-03-26 06:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-26 05:50 | 2026-03-26 05:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-03-26 05:57 | 2026-03-26 05:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.188.93[.]169` | 1 | 2026-03-26 05:42 | 2026-03-26 05:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.198.173[.]137` | 1 | 2026-03-26 06:03 | 2026-03-26 06:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.201.226[.]253` | 1 | 2026-03-26 06:39 | 2026-03-26 06:39 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]254` | 1 | 2026-03-26 06:39 | 2026-03-26 06:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.185.30[.]170` | 1 | 2026-03-26 05:41 | 2026-03-26 05:41 | 5s | 0 | `T1592` | 🟢 LOW |

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
| `111.70.39[.]216` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 25 |
| `180.184.36[.]192` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `118.179.200[.]67` | BD | Amber IT Limited | **100** ⚠️ | 50 |
| `61.185.30[.]170` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 40 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `196.188.93[.]169` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `218.201.226[.]253` | CN | China Mobile Communications Corporation - guizhou | **100** ⚠️ | 0 |
| `49.124.152[.]254` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 0 |
| `180.184.84[.]77` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `101.47.142[.]202` | SG | BYTEPLUS | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 38 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (23.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 17 session(s)).

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
_Report time: 2026-03-26T07:04:41Z_
