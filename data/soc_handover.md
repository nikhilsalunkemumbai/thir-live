# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T16:55:42Z |
| **Shift Time** | 16:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **51** |
| Confirmed Threats | **19** |
| False Positives Filtered | **32** (62.7%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **13** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **51** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **9** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 5 |
| `admin` | 3 |
| `Blank` | 2 |
| `blank` | 2 |
| `Debian` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `maintenance` | 1 |
| `Password1` | 1 |
| `admin!@#` | 1 |
| `Admin!@#` | 1 |
| `qwerty123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Debian` | `maintenance` | 1 |
| `admin` | `Password1` | 1 |
| `ubuntu` | `admin!@#` | 1 |
| `ubuntu` | `Admin!@#` | 1 |
| `Blank` | `qwerty123456` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **17** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | LOW |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | HIGH |
| `AS18403` | FPT Telecom Company | 1 | HIGH |
| `AS42831` | UK Dedicated Servers Limited | 1 | LOW |
| `AS12849` | Hot-Net internet services Ltd. | 1 | HIGH |

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
| `183.81.33[.]183` | **6** | 2026-03-23 15:00 | 2026-03-23 15:43 | 2m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `223.123.42[.]182` | **4** | 2026-03-23 16:54 | 2026-03-23 16:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-03-23 15:55 | 2026-03-23 15:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.53.70[.]99` | 1 | 2026-03-23 15:46 | 2026-03-23 15:46 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.122.196[.]230` | 1 | 2026-03-23 14:59 | 2026-03-23 14:59 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-23 16:02 | 2026-03-23 16:02 | 31s | 0 | `T1592` | 🟢 LOW |
| `154.118.162[.]194` | 1 | 2026-03-23 16:32 | 2026-03-23 16:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.12.237[.]243` | 1 | 2026-03-23 15:31 | 2026-03-23 15:31 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.6.17[.]69` | 1 | 2026-03-23 15:11 | 2026-03-23 15:11 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.172.203[.]43` | 1 | 2026-03-23 16:28 | 2026-03-23 16:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.142.173[.]63` | 1 | 2026-03-23 15:36 | 2026-03-23 15:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `112.53.70[.]99` | CN | China Mobile Communications Corporation | **100** ⚠️ | 34 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `220.172.203[.]43` | CN | CHINANET Guizhou province network | **100** ⚠️ | 50 |
| `37.142.173[.]63` | IL | Hot-Net internet services Ltd. | **100** ⚠️ | 29 |
| `183.6.17[.]69` | CN | CHINANET Guangdong province network | **100** ⚠️ | 1 |
| `118.122.196[.]230` | CN | CHINANET Sichuan province network | **100** ⚠️ | 38 |
| `154.118.162[.]194` | ML | Orange Mali SA | **100** ⚠️ | 38 |
| `177.12.237[.]243` | BR | ALOO TELECOM - FSF TECNOLOGIA SA | **100** ⚠️ | 1 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `183.81.33[.]183` | VN | FPT Telecom Company | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 51 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (62.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 11 recon entry/entries in table (2 group(s) consolidating 10 session(s)).

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
_Report time: 2026-03-23T16:55:42Z_
