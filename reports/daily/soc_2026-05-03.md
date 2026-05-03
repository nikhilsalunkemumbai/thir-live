# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-03 |
| **Generated At** | 2026-05-03T14:52:33Z |
| **Shift Time** | 14:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **177** |
| Confirmed Threats | **58** |
| False Positives Filtered | **119** (67.2%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **14** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **177** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **6** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 3 |
| `ovpn` | 1 |
| `test2` | 1 |
| `btserver` | 1 |
| `testuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin@654321` | 1 |
| `0123456789` | 1 |
| `ovpn123` | 1 |
| `admin` | 1 |
| `1q2w3e4r` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin@654321` | 1 |
| `admin` | `0123456789` | 1 |
| `ovpn` | `ovpn123` | 1 |
| `admin` | `admin` | 1 |
| `test2` | `1q2w3e4r` | 1 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **177** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 31 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 26 | 1 |
| `af8223ac9914...` | libssh-based | 5 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 26 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 5 | 2 | libssh-based |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **22** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS17638` | ASN for TIANJIN Provincial Net of CT | 1 | HIGH |
| `AS36903` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 1 | LOW |
| `AS141995` | Contabo Asia Private Limited | 1 | MEDIUM |
| `AS11664` | Techtel LMDS Comunicaciones Interactivas S.A. | 1 | LOW |
| `AS27837` | Dialnet de Colombia S.A. E.S.P. | 1 | LOW |
| `AS263402` | INFORMATICA.COM LTDA | 1 | LOW |
| `AS270570` | JuniorNet Fibra | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | HIGH |

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
| `180.213.44[.]242` | **26** | 2026-05-03 14:18 | 2026-05-03 14:52 | 44m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `62.72.47[.]216` | **22** | 2026-05-03 14:11 | 2026-05-03 14:52 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `173.249.52[.]138` | **4** | 2026-05-03 14:24 | 2026-05-03 14:43 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `134.185.117[.]241` | 1 | 2026-05-03 14:06 | 2026-05-03 14:07 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.64.171[.]136` | 1 | 2026-05-03 14:26 | 2026-05-03 14:27 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `201.17.133[.]138` | 1 | 2026-05-03 14:23 | 2026-05-03 14:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.229.156[.]171` | 1 | 2026-05-03 13:51 | 2026-05-03 13:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.127.80[.]34` | 1 | 2026-05-03 13:57 | 2026-05-03 13:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | 1 | 2026-05-03 14:12 | 2026-05-03 14:12 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `134.185.117[.]241` | KR | Oracle Corporation | **100** ⚠️ | 50 |
| `183.64.171[.]136` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 6 |
| `59.127.80[.]34` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 6 |
| `66.132.172[.]182` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `201.17.133[.]138` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 50 |
| `173.249.52[.]138` | FR | Contabo GmbH | **100** ⚠️ | 50 |
| `180.213.44[.]242` | CN | CHINANET TIANJIN PROVINCE NETWORK | **100** ⚠️ | 40 |
| `45.229.156[.]171` | BR | Brnet Telecomunicacoes LTDA - ME | **97** ⚠️ | 1 |
| `62.72.47[.]216` | SG | Contabo GmbH | **89** ⚠️ | 0 |
| `217.146.67[.]166` | EE | Zone Media LLC | **70** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 32 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |

---

## 🔕 False Positive Summary (119 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 111 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 177 cases |
| Tool 34  | Credential Extractor        | ✅ 8 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 119 filtered (67.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 9 recon entry/entries in table (3 group(s) consolidating 52 session(s)).

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
_Report time: 2026-05-03T14:52:33Z_
