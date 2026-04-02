# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T22:29:23Z |
| **Shift Time** | 22:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **27** |
| Confirmed Threats | **22** |
| False Positives Filtered | **5** (18.5%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **14** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **27** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **12** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `guest` | 4 |
| `centos` | 2 |
| `ubnt` | 2 |
| `config` | 2 |
| `User` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `7777` | 2 |
| `centos2010` | 1 |
| `777777` | 1 |
| `admin123` | 1 |
| `6666666` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `7777` | 2 |
| `centos` | `centos2010` | 1 |
| `centos` | `777777` | 1 |
| `User` | `admin123` | 1 |
| `guest` | `6666666` | 1 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **27** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 19 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 18 | 18 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 18 | 18 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **22** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS7633` | Software Technology Parks of India - Bangalore | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS17858` | LG POWERCOMM | 1 | HIGH |
| `AS267788` | IP TECHNOLOGIES S.A.S. | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS12479` | Orange Espagne SA | 1 | HIGH |

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
| `116.47.238[.]46` | 1 | 2026-04-02 22:16 | 2026-04-02 22:16 | 30s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]186` | 1 | 2026-04-02 21:49 | 2026-04-02 21:49 | 17s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.84.147[.]45` | 1 | 2026-04-02 21:29 | 2026-04-02 21:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-04-02 22:11 | 2026-04-02 22:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.24.206[.]213` | 1 | 2026-04-02 20:52 | 2026-04-02 20:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.20.228[.]146` | 1 | 2026-04-02 21:16 | 2026-04-02 21:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-02 21:28 | 2026-04-02 21:28 | 31s | 0 | `T1592` | 🟢 LOW |
| `152.52.213[.]98` | 1 | 2026-04-02 21:16 | 2026-04-02 21:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]26` | 1 | 2026-04-02 21:53 | 2026-04-02 21:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.126[.]88` | 1 | 2026-04-02 20:34 | 2026-04-02 20:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.82.20[.]241` | 1 | 2026-04-02 21:35 | 2026-04-02 21:36 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.193.147[.]37` | 1 | 2026-04-02 21:31 | 2026-04-02 21:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.193.147[.]75` | 1 | 2026-04-02 22:14 | 2026-04-02 22:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.39.140[.]2` | 1 | 2026-04-02 21:51 | 2026-04-02 21:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.28.177[.]141` | 1 | 2026-04-02 21:55 | 2026-04-02 21:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]14` | 1 | 2026-04-02 22:08 | 2026-04-02 22:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]7` | 1 | 2026-04-02 21:12 | 2026-04-02 21:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]146` | 1 | 2026-04-02 20:58 | 2026-04-02 20:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.217[.]64` | 1 | 2026-04-02 21:49 | 2026-04-02 21:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.65.140[.]218` | 1 | 2026-04-02 22:10 | 2026-04-02 22:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.188.38[.]227` | 1 | 2026-04-02 20:50 | 2026-04-02 20:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.176.241[.]140` | 1 | 2026-04-02 22:18 | 2026-04-02 22:18 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `123.129.245[.]249` | CN | China Unicom Shandong Province Network | **100** ⚠️ | 50 |
| `49.124.151[.]7` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 12 |
| `65.20.217[.]64` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 38 |
| `203.193.147[.]75` | IN | Software Technology Parks of India | **100** ⚠️ | 40 |
| `49.124.152[.]146` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 8 |
| `116.47.238[.]46` | KR | LG POWERCOMM | **100** ⚠️ | 26 |
| `123.24.206[.]213` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 29 |
| `2.55.126[.]88` | IL | Partner Communications Ltd. | **100** ⚠️ | 26 |
| `202.82.20[.]241` | HK | Hong Kong Telecommunications (HKT) Limited Business Internet | **100** ⚠️ | 50 |
| `90.188.38[.]227` | RU | OJSC Sibirtelecom | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 27 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 22 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-02T22:29:23Z_
