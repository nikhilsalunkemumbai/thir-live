# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T06:48:21Z |
| **Shift Time** | 06:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **23** |
| Confirmed Threats | **19** |
| False Positives Filtered | **4** (17.4%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **8** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **23** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **13** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `test` | 2 |
| `Support` | 1 |
| `ftpuser` | 1 |
| `term2` | 1 |
| `crafty` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 2 |
| `55555555` | 1 |
| `ftp` | 1 |
| `Crafty123` | 1 |
| `12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Support` | `55555555` | 1 |
| `ftpuser` | `ftp` | 1 |
| `term2` | `123456` | 1 |
| `crafty` | `Crafty123` | 1 |
| `iot` | `12345678` | 1 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS272274` | RB TELECOM | 1 | HIGH |
| `AS262766` | VITAL NET | 1 | HIGH |
| `AS30722` | Fastweb SpA | 1 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |

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
| `187.94.255[.]130` | **10** | 2026-03-22 05:45 | 2026-03-22 06:10 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.59.42[.]139` | 1 | 2026-03-22 06:00 | 2026-03-22 06:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `125.20.251[.]70` | 1 | 2026-03-22 05:35 | 2026-03-22 05:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.205.151[.]177` | 1 | 2026-03-22 06:24 | 2026-03-22 06:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `179.125.104[.]245` | 1 | 2026-03-22 06:05 | 2026-03-22 06:05 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.18[.]67` | 1 | 2026-03-22 06:39 | 2026-03-22 06:39 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.126.86[.]138` | 1 | 2026-03-22 05:53 | 2026-03-22 05:53 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]224` | 1 | 2026-03-22 06:44 | 2026-03-22 06:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.222.136[.]218` | 1 | 2026-03-22 06:00 | 2026-03-22 06:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `93.145.118[.]40` | 1 | 2026-03-22 05:39 | 2026-03-22 05:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `175.205.151[.]177` | KR | Chungbukbonbujang | **100** ⚠️ | 2 |
| `125.20.251[.]70` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 17 |
| `179.185.18[.]67` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 26 |
| `93.145.118[.]40` | IT | Vodafone Italia S.p.A. | **100** ⚠️ | 24 |
| `216.126.86[.]138` | CA | Frontier Networks Inc | **100** ⚠️ | 4 |
| `8.222.136[.]218` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 26 |
| `49.124.152[.]224` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `179.125.104[.]245` | BR | RB TELECOM | **100** ⚠️ | 21 |
| `124.59.42[.]139` | KR | LG POWERCOMM | **100** ⚠️ | 29 |
| `187.94.255[.]130` | BR | VITAL NET | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 14 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 23 cases |
| Tool 34  | Credential Extractor        | ✅ 14 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (17.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 10 recon entry/entries in table (1 group(s) consolidating 10 session(s)).

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
_Report time: 2026-03-22T06:48:21Z_
