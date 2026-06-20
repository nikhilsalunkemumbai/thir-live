# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T17:37:52Z |
| **Shift Time** | 17:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **35** |
| Confirmed Threats | **28** |
| False Positives Filtered | **7** (20.0%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **10** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **35** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **13** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **13** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `Admin` | 1 |
| `pi` | 1 |
| `local` | 1 |
| `lighthouse` | 1 |
| `nils` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1q2w3e4r5t` | 1 |
| `raspberry123` | 1 |
| `local1` | 1 |
| `1` | 1 |
| `nils` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Admin` | `1q2w3e4r5t` | 1 |
| `pi` | `raspberry123` | 1 |
| `local` | `local1` | 1 |
| `lighthouse` | `1` | 1 |
| `nils` | `nils` | 1 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **35** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 8 |
| libssh | 4 |
| Perl Net::SSH | 2 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 8 | 8 |
| `f555226df196...` | Mirai/variant | 4 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 8 | 8 | Mirai/variant |
| `f555226df196...` | libssh | 4 | 1 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **24** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 6 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |
| `AS9316` | DACOM-PUBNETPLUS | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | HIGH |
| `AS214664` | JSC Buduschee | 1 | HIGH |
| `AS152367` | PT Box Net Media | 1 | HIGH |

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
| `125.247.116[.]158` | **4** | 2026-06-20 15:14 | 2026-06-20 15:21 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `176.32.193[.]16` | **2** | 2026-06-20 15:49 | 2026-06-20 15:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.205.2[.]250` | 1 | 2026-06-20 14:51 | 2026-06-20 14:51 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-06-20 15:13 | 2026-06-20 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.176.45[.]238` | 1 | 2026-06-20 15:20 | 2026-06-20 15:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.147[.]13` | 1 | 2026-06-20 15:23 | 2026-06-20 15:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `134.209.241[.]3` | 1 | 2026-06-20 14:48 | 2026-06-20 14:50 | 100s | 0 | `T1592` | 🟢 LOW |
| `135.232.177[.]178` | 1 | 2026-06-20 17:37 | 2026-06-20 17:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `155.4.209[.]51` | 1 | 2026-06-20 16:50 | 2026-06-20 16:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.15.78[.]122` | 1 | 2026-06-20 17:32 | 2026-06-20 17:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.230.129[.]112` | 1 | 2026-06-20 14:43 | 2026-06-20 14:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `175.195.231[.]106` | 1 | 2026-06-20 17:08 | 2026-06-20 17:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.126.240[.]80` | 1 | 2026-06-20 15:50 | 2026-06-20 15:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `207.244.238[.]142` | 1 | 2026-06-20 15:59 | 2026-06-20 15:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]6` | 1 | 2026-06-20 15:48 | 2026-06-20 15:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.221.244[.]34` | 1 | 2026-06-20 16:11 | 2026-06-20 16:11 | 3s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-06-20 16:22 | 2026-06-20 16:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.231.89[.]112` | 1 | 2026-06-20 15:04 | 2026-06-20 15:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]114` | 1 | 2026-06-20 15:04 | 2026-06-20 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]119` | 1 | 2026-06-20 15:04 | 2026-06-20 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]156` | 1 | 2026-06-20 15:06 | 2026-06-20 15:06 | 4s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]201` | 1 | 2026-06-20 15:04 | 2026-06-20 15:04 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]75` | 1 | 2026-06-20 15:06 | 2026-06-20 15:06 | 1s | 0 | `T1592` | 🟢 LOW |
| `95.79.108[.]51` | 1 | 2026-06-20 15:09 | 2026-06-20 15:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 43/100 | 🟡 MEDIUM | **34/73** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 44/100 | 🟡 MEDIUM | **35/73** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `134.209.241[.]3` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `83.191.181[.]23` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 46 |
| `45.91.64[.]6` | RU | F6 | **100** ⚠️ | 50 |
| `157.15.78[.]122` | ID | PT Box Net Media | **100** ⚠️ | 2 |
| `157.230.129[.]112` | US | DigitalOcean, LLC | **100** ⚠️ | 5 |
| `120.48.154[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `188.126.240[.]80` | SE | Telia Network Services | **100** ⚠️ | 50 |
| `95.79.108[.]51` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |
| `117.205.2[.]250` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 22 |
| `91.231.89[.]156` | FR | FR ONYPHE | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 17 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 35 cases |
| Tool 34  | Credential Extractor        | ✅ 13 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 24 recon entry/entries in table (2 group(s) consolidating 6 session(s)).

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
_Report time: 2026-06-20T17:37:52Z_
