# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T07:10:44Z |
| **Shift Time** | 07:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **33** |
| Confirmed Threats | **14** |
| False Positives Filtered | **19** (57.6%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **16** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **33** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **8** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `User` | 2 |
| `admin` | 2 |
| `Test` | 1 |
| `postgres` | 1 |
| `config` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 2 |
| `dietpi` | 1 |
| `raspberry` | 1 |
| `1234567890` | 1 |
| `1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 2 |
| `User` | `dietpi` | 1 |
| `Test` | `raspberry` | 1 |
| `postgres` | `1234567890` | 1 |
| `config` | `1` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **20** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS12479` | Orange Espagne SA | 1 | MEDIUM |
| `AS16135` | Turkcell A.S. | 1 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | MEDIUM |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS15659` | NextGenTel AS | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |

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
| `112.78.177[.]144` | 1 | 2026-03-31 06:32 | 2026-03-31 06:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.242.185[.]233` | 1 | 2026-03-31 06:28 | 2026-03-31 06:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.215.199[.]37` | 1 | 2026-03-31 05:52 | 2026-03-31 05:53 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-03-31 06:04 | 2026-03-31 06:04 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-31 06:03 | 2026-03-31 06:03 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.215.198[.]204` | 1 | 2026-03-31 06:23 | 2026-03-31 06:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `188.43.204[.]45` | 1 | 2026-03-31 06:52 | 2026-03-31 06:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.59.88[.]234` | 1 | 2026-03-31 05:49 | 2026-03-31 05:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-31 05:52 | 2026-03-31 05:52 | 4s | 0 | `T1592` | 🟢 LOW |
| `43.250.107[.]151` | 1 | 2026-03-31 06:12 | 2026-03-31 06:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]12` | 1 | 2026-03-31 06:52 | 2026-03-31 06:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.166[.]171` | 1 | 2026-03-31 06:48 | 2026-03-31 06:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.29.219[.]168` | 1 | 2026-03-31 06:24 | 2026-03-31 06:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `89.10.237[.]211` | 1 | 2026-03-31 06:14 | 2026-03-31 06:14 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `117.242.185[.]233` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL | **100** ⚠️ | 9 |
| `65.20.166[.]171` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 0 |
| `49.124.151[.]12` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 13 |
| `125.215.199[.]37` | HK | C S (HK) CO LIMITED | **100** ⚠️ | 50 |
| `188.43.204[.]45` | RU | TTK | **100** ⚠️ | 39 |
| `89.10.237[.]211` | NO | XDSL access and service provider in Norway | **100** ⚠️ | 2 |
| `188.59.88[.]234` | TR | TURKCELL INTERNET | **100** ⚠️ | 9 |
| `175.215.198[.]204` | KR | Korea Telecom | **100** ⚠️ | 3 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 9 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 33 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (57.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 14 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-31T07:10:44Z_
