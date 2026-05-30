# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-30 |
| **Generated At** | 2026-05-30T13:46:23Z |
| **Shift Time** | 13:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **275** |
| Confirmed Threats | **197** |
| False Positives Filtered | **78** (28.4%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **11** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **261** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **72** |
| Unique Usernames | **56** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `frappe` | 2 |
| `ubuntu` | 2 |
| `admin` | 2 |
| `azureuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 8 |
| `azureuser` | 1 |
| `backup` | 1 |
| `data` | 1 |
| `qwe123!@` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `azureuser` | `azureuser` | 1 |
| `backup` | `backup` | 1 |
| `data` | `data` | 1 |
| `root` | `qwe123!@` | 1 |
| `elasticsearch` | `elasticsearch@1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwe123!@` | `47.237.83.105` | 2026-05-30T10:03:20 |
| `root` | `abcd@1234` | `47.237.83.105` | 2026-05-30T10:03:55 |
| `root` | `test@123` | `47.237.83.105` | 2026-05-30T10:03:58 |
| `root` | `!qaz@WSX` | `47.237.83.105` | 2026-05-30T10:04:38 |
| `root` | `0` | `47.237.83.105` | 2026-05-30T10:04:41 |
| `root` | `Huawei123` | `47.237.83.105` | 2026-05-30T10:04:44 |
| `root` | `root1234` | `47.237.83.105` | 2026-05-30T10:04:47 |
| `root` | `t0talc0ntr0l4!` | `47.237.83.105` | 2026-05-30T10:04:50 |
| `root` | `Aa123321` | `47.237.83.105` | 2026-05-30T10:05:49 |
| `root` | `111` | `47.237.83.105` | 2026-05-30T10:06:13 |
| `root` | `Pass@123` | `47.237.83.105` | 2026-05-30T10:06:16 |
| `root` | `Password@123` | `47.237.83.105` | 2026-05-30T10:06:19 |
| `root` | `QWEqwe123` | `47.237.83.105` | 2026-05-30T10:06:22 |
| `root` | `test1234` | `47.237.83.105` | 2026-05-30T10:06:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **275** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 74 |
| Unknown | 2 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 72 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 72 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **16** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS2614` | RoEduNet | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
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
| `206.189.25[.]100` | **155** | 2026-05-30 10:03 | 2026-05-30 13:45 | 144m | 0 | `T1592` | 🟠 MEDIUM |
| `72.255.18[.]52` | **21** | 2026-05-30 12:14 | 2026-05-30 12:18 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `135.148.33[.]168` | **4** | 2026-05-30 10:22 | 2026-05-30 13:15 | 2m | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | **3** | 2026-05-30 10:35 | 2026-05-30 13:38 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]191` | **2** | 2026-05-30 12:11 | 2026-05-30 12:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]201` | **2** | 2026-05-30 10:19 | 2026-05-30 10:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.79.77[.]73` | **2** | 2026-05-30 10:11 | 2026-05-30 10:11 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]181` | **2** | 2026-05-30 12:29 | 2026-05-30 12:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.196.56[.]74` | 1 | 2026-05-30 11:33 | 2026-05-30 11:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.142[.]184` | 1 | 2026-05-30 11:52 | 2026-05-30 11:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-05-30 10:21 | 2026-05-30 10:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `196.190.213[.]44` | 1 | 2026-05-30 13:34 | 2026-05-30 13:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `44.203.47[.]141` | 1 | 2026-05-30 13:10 | 2026-05-30 13:10 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.75.213[.]171` | 1 | 2026-05-30 13:40 | 2026-05-30 13:40 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `196.190.213[.]44` | ET | Ethio Telecom | **100** ⚠️ | 0 |
| `194.102.73[.]93` | RO | Universitatea de Stiinte Agricole si Medicina Veterinara Cluj-Napoca | **100** ⚠️ | 0 |
| `118.196.56[.]74` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 18 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `44.203.47[.]141` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 0 |
| `34.79.77[.]73` | BE | Google LLC | **100** ⚠️ | 1 |
| `61.75.213[.]171` | KR | Korea Telecom | **100** ⚠️ | 3 |
| `14.103.142[.]184` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `66.132.172[.]181` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 58 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |

---

## 🔕 False Positive Summary (78 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 74 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 275 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 78 filtered (28.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 16 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 14 recon entry/entries in table (8 group(s) consolidating 191 session(s)).

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
_Report time: 2026-05-30T13:46:23Z_
