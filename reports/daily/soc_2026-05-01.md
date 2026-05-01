# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-01 |
| **Generated At** | 2026-05-01T17:00:53Z |
| **Shift Time** | 17:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **252** |
| Confirmed Threats | **36** |
| False Positives Filtered | **216** (85.7%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **20** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **251** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **1** |
| Unique Credential Pairs | **1** |
| Unique Usernames | **1** |
| Unique Passwords | **1** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `------fuck------` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `------fuck------` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `222.73.51.231` | 2026-05-01T16:09:50 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **252** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 3 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `af8223ac9914...` | libssh-based | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **38** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS131464` | Digi Jadoo Broadband Ltd | 4 | LOW |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS20207` | Gigared S.A. | 1 | LOW |
| `AS137687` | Luoyang, Henan Province, P.R.China. | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS27951` | Media Commerce Partners S.A | 1 | LOW |
| `AS52363` | Jumpnet Soluciones de Internet S.R.L. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f96266f7603

| Field | Detail |
|---|---|
| **Source IP** | `222.73.51[.]231` |
| **First Seen** | 2026-05-01 16:09 |
| **Last Seen** | 2026-05-01 16:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 16:09:45` | `cowrie.session.connect` |
| `2026-05-01 16:09:47` | `cowrie.client.version` |
| `2026-05-01 16:09:47` | `cowrie.client.kex` |
| `2026-05-01 16:09:50` | `cowrie.login.success` |
| `2026-05-01 16:09:51` | `cowrie.session.params` |
| `2026-05-01 16:09:51` | `cowrie.command.input` |
| `2026-05-01 16:09:52` | `cowrie.log.closed` |
| `2026-05-01 16:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.73.51[.]231` to AbuseIPDB if not already reported
- [ ] Block `222.73.51[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.42.75[.]108` | **25** | 2026-05-01 16:39 | 2026-05-01 16:44 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `20.65.202[.]2` | **2** | 2026-05-01 16:10 | 2026-05-01 16:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `123.157.223[.]90` | 1 | 2026-05-01 15:13 | 2026-05-01 15:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.24.19[.]233` | 1 | 2026-05-01 16:45 | 2026-05-01 16:45 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.73.51[.]231` | 1 | 2026-05-01 16:09 | 2026-05-01 16:09 | 1s | 0 | `T1592` | 🟢 LOW |
| `36.99.46[.]101` | 1 | 2026-05-01 15:04 | 2026-05-01 15:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.100.183[.]18` | 1 | 2026-05-01 15:11 | 2026-05-01 15:11 | 28s | 0 | `T1592` | 🟢 LOW |
| `47.84.187[.]228` | 1 | 2026-05-01 16:08 | 2026-05-01 16:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-05-01 15:00 | 2026-05-01 15:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.164.31[.]200` | 1 | 2026-05-01 16:15 | 2026-05-01 16:15 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `91.164.31[.]200` | FR | Scaleway SAS | **100** ⚠️ | 0 |
| `123.157.223[.]90` | CN | China Unicom Zhejiang province network | **100** ⚠️ | 30 |
| `222.73.51[.]231` | CN | CHINANET shanghai province network | **100** ⚠️ | 13 |
| `47.84.187[.]228` | SG | Alibaba Cloud LLC | **100** ⚠️ | 22 |
| `115.42.75[.]108` | PK | CMPak Limited | **100** ⚠️ | 3 |
| `39.100.183[.]18` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `66.240.236[.]116` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `36.99.46[.]101` | CN | CHINANET henan province network | **100** ⚠️ | 50 |
| `20.65.202[.]2` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `144.24.19[.]233` | US | Oracle Corp UK Ltd | **96** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 5 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (216 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 2 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 185 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 252 cases |
| Tool 34  | Credential Extractor        | ✅ 1 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 216 filtered (85.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 10 recon entry/entries in table (2 group(s) consolidating 27 session(s)).

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
_Report time: 2026-05-01T17:00:53Z_
