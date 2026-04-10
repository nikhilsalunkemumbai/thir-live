# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T13:04:43Z |
| **Shift Time** | 13:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **57** |
| Confirmed Threats | **25** |
| False Positives Filtered | **32** (56.1%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **3** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **56** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **7** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `root` | 1 |
| `oracle` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `!Q2w3e4r` | 1 |
| `oracle` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `root` | `!Q2w3e4r` | 1 |
| `oracle` | `oracle` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!Q2w3e4r` | `112.124.1.210` | 2026-04-10T12:01:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **57** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 14 |
| libssh | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 11 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 11 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 1 | 1 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **9** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS138245` | Xpress Net Solution | 1 | LOW |
| `AS139549` | Crisp Enterprises | 1 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS20115` | Charter Communications LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-332aa5beddb2

| Field | Detail |
|---|---|
| **Source IP** | `112.124.1[.]210` |
| **First Seen** | 2026-04-10 12:01 |
| **Last Seen** | 2026-04-10 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 12:01:07` | `cowrie.session.connect` |
| `2026-04-10 12:01:07` | `cowrie.client.version` |
| `2026-04-10 12:01:07` | `cowrie.client.kex` |
| `2026-04-10 12:01:08` | `cowrie.login.success` |
| `2026-04-10 12:01:08` | `cowrie.session.params` |
| `2026-04-10 12:01:08` | `cowrie.command.input` |
| `2026-04-10 12:01:08` | `cowrie.log.closed` |
| `2026-04-10 12:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.124.1[.]210` to AbuseIPDB if not already reported
- [ ] Block `112.124.1[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.124.1[.]210` | **13** | 2026-04-10 11:47 | 2026-04-10 12:01 | 4m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **7** | 2026-04-10 11:54 | 2026-04-10 12:03 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `180.110.149[.]157` | 1 | 2026-04-10 13:03 | 2026-04-10 13:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.143[.]203` | 1 | 2026-04-10 13:01 | 2026-04-10 13:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.92.180[.]146` | 1 | 2026-04-10 12:57 | 2026-04-10 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `97.93.152[.]80` | 1 | 2026-04-10 11:44 | 2026-04-10 11:44 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `180.76.143[.]203` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `3.92.180[.]146` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 16 |
| `97.93.152[.]80` | US | Charter Communications LLC | **100** ⚠️ | 18 |
| `112.124.1[.]210` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 27 |
| `180.110.149[.]157` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 32 |
| `13.233.179[.]153` | IN | Amazon Data Services India | **48** | 0 |
| `103.146.111[.]106` | IN | Crisp Enterprises | **35** | 1 |
| `103.181.160[.]47` | IN | MONGA TELECOM | 23 | 2 |
| `13.83.216[.]97` | US | Microsoft Corporation | 17 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 16 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 57 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (56.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 9 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 6 recon entry/entries in table (2 group(s) consolidating 20 session(s)).

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
_Report time: 2026-04-10T13:04:43Z_
