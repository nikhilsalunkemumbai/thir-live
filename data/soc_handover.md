# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T07:46:53Z |
| **Shift Time** | 07:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **127** |
| Confirmed Threats | **23** |
| False Positives Filtered | **104** (81.9%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **127** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **12** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `Centos` | 3 |
| `Ubnt` | 2 |
| `nobody` | 2 |
| `default` | 1 |
| `Blank` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3333` | 1 |
| `toor` | 1 |
| `root` | 1 |
| `Passw@rd` | 1 |
| `operator2005` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `3333` | 1 |
| `Blank` | `toor` | 1 |
| `Centos` | `root` | 1 |
| `Ubnt` | `Passw@rd` | 1 |
| `operator` | `operator2005` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **22** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS10029` | SHYAM SPECTRA PVT LTD | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS206264` | Amarutu Technology Ltd | 1 | HIGH |
| `AS10796` | Charter Communications Inc | 1 | HIGH |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 1 | MEDIUM |

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
| `45.64.134[.]75` | **3** | 2026-03-30 06:24 | 2026-03-30 06:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.173[.]2` | **2** | 2026-03-30 06:31 | 2026-03-30 06:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.174.189[.]18` | 1 | 2026-03-30 06:52 | 2026-03-30 06:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `103.31.39[.]188` | 1 | 2026-03-30 06:23 | 2026-03-30 06:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.91.176[.]244` | 1 | 2026-03-30 06:03 | 2026-03-30 06:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.218[.]118` | 1 | 2026-03-30 06:50 | 2026-03-30 06:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-30 07:36 | 2026-03-30 07:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `175.195.231[.]106` | 1 | 2026-03-30 07:10 | 2026-03-30 07:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.233.85[.]194` | 1 | 2026-03-30 07:29 | 2026-03-30 07:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.81.169[.]235` | 1 | 2026-03-30 07:29 | 2026-03-30 07:29 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.243.200[.]248` | 1 | 2026-03-30 06:32 | 2026-03-30 06:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.208.165[.]75` | 1 | 2026-03-30 06:10 | 2026-03-30 06:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.92.36[.]109` | 1 | 2026-03-30 06:13 | 2026-03-30 06:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.156[.]254` | 1 | 2026-03-30 07:02 | 2026-03-30 07:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.112[.]126` | 1 | 2026-03-30 07:43 | 2026-03-30 07:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]41` | 1 | 2026-03-30 07:10 | 2026-03-30 07:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.12.5[.]190` | 1 | 2026-03-30 06:42 | 2026-03-30 06:43 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.10.180[.]65` | 1 | 2026-03-30 06:30 | 2026-03-30 06:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.84.21[.]186` | 1 | 2026-03-30 07:22 | 2026-03-30 07:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.102.148[.]242` | 1 | 2026-03-30 07:23 | 2026-03-30 07:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `98.102.148[.]242` | US | VERENA AT HILLIARD | **100** ⚠️ | 50 |
| `40.124.173[.]2` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `201.208.165[.]75` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 4 |
| `103.31.39[.]188` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 38 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `49.124.153[.]41` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 10 |
| `60.12.5[.]190` | CN | XIYINGYINGBINGUAN,HANGZHOU,ZHEJIANG | **100** ⚠️ | 26 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `128.185.218[.]118` | IN | BHARTI-AIRTEL | **100** ⚠️ | 47 |
| `27.123.112[.]126` | IN | Bharti Airtel Limited | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |

---

## 🔕 False Positive Summary (104 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 102 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 127 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 104 filtered (81.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 20 recon entry/entries in table (2 group(s) consolidating 5 session(s)).

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
_Report time: 2026-03-30T07:46:53Z_
