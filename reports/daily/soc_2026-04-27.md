# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-27 |
| **Generated At** | 2026-04-27T10:21:30Z |
| **Shift Time** | 10:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **64** |
| False Positives Filtered | **51** (44.4%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **12** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **115** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1** |
| Unique Credential Pairs | **1** |
| Unique Usernames | **1** |
| Unique Passwords | **1** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 1 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **115** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Nmap scanner | 7 |
| libssh | 4 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `af8223ac9914...` | libssh-based | 2 | 2 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |
| `a20aced7c982...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 2 | 2 | — |
| `af8223ac9914...` | libssh | 2 | 2 | libssh-based |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `a20aced7c982...` | Nmap scanner | 1 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **23** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS56005` | Zhengzhou Fastidc Technology Co.,Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS197350` | AL Zaytona Company For Communication Ltd. | 1 | MEDIUM |
| `AS267452` | CABONNET INTERNET LTDA | 1 | LOW |
| `AS138423` | CMPak Limited | 1 | HIGH |

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
| `59.103.104[.]251` | **14** | 2026-04-27 09:08 | 2026-04-27 09:11 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.35[.]128` | **10** | 2026-04-27 06:30 | 2026-04-27 06:32 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `35.205.244[.]229` | **10** | 2026-04-27 07:41 | 2026-04-27 07:41 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `170.233.68[.]217` | **9** | 2026-04-27 07:59 | 2026-04-27 08:11 | 14m | 0 | `T1592` | 🟢 LOW |
| `46.60.15[.]90` | **4** | 2026-04-27 09:19 | 2026-04-27 09:27 | 8m | 0 | `T1592` | 🟢 LOW |
| `82.75.11[.]146` | **3** | 2026-04-27 09:18 | 2026-04-27 09:22 | 6m | 0 | `T1592` | 🟢 LOW |
| `222.88.163[.]204` | **2** | 2026-04-27 09:45 | 2026-04-27 09:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `35.233.20[.]248` | **2** | 2026-04-27 07:40 | 2026-04-27 07:41 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.105.199[.]177` | **2** | 2026-04-27 08:47 | 2026-04-27 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.53.147[.]80` | 1 | 2026-04-27 08:27 | 2026-04-27 08:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.121[.]4` | 1 | 2026-04-27 08:19 | 2026-04-27 08:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.245.243[.]118` | 1 | 2026-04-27 09:48 | 2026-04-27 09:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-04-27 07:58 | 2026-04-27 07:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.209.190[.]245` | 1 | 2026-04-27 06:55 | 2026-04-27 06:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.134.94[.]69` | 1 | 2026-04-27 06:52 | 2026-04-27 06:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `42.51.40[.]180` | 1 | 2026-04-27 09:48 | 2026-04-27 09:49 | 50s | 0 | `T1592` | 🟢 LOW |
| `45.23.218[.]218` | 1 | 2026-04-27 06:51 | 2026-04-27 06:52 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `220.134.94[.]69` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 4 |
| `118.196.121[.]4` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `223.123.35[.]128` | PK | CMPak Limited | **100** ⚠️ | 2 |
| `170.233.68[.]217` | AR | NETLATIN S.R.L. | **100** ⚠️ | 2 |
| `35.205.244[.]229` | BE | Google LLC | **100** ⚠️ | 0 |
| `35.233.20[.]248` | BE | Google LLC | **100** ⚠️ | 0 |
| `157.245.243[.]118` | US | DigitalOcean, LLC | **100** ⚠️ | 20 |
| `165.154.225[.]20` | HK | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 50 |
| `45.23.218[.]218` | US | AT&T Enterprises, LLC | **100** ⚠️ | 14 |
| `111.53.147[.]80` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 15 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 39 |
| AbuseIPDB score 23 below threshold 25 | 4 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 115 cases |
| Tool 34  | Credential Extractor        | ✅ 1 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (44.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 17 recon entry/entries in table (9 group(s) consolidating 56 session(s)).

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
_Report time: 2026-04-27T10:21:30Z_
