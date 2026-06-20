# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T14:10:39Z |
| **Shift Time** | 14:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **62** |
| Confirmed Threats | **32** |
| False Positives Filtered | **30** (48.4%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **13** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **60** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **14** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **12** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `operator` | 2 |
| `dietpi` | 1 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: curl/7.64.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `root1` | 1 |
| `dietpi` | 1 |
| `Host: 13.235.92.17:2223` | 1 |
| `Accept: */*` | 1 |
| `123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root1` | 1 |
| `dietpi` | `dietpi` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:2223` | 1 |
| `User-Agent: curl/7.64.1` | `Accept: */*` | 1 |
| `simon` | `123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root1` | `49.43.35.54` | 2026-06-20T10:53:10 |
| `root` | `0l0ctyQh243O63uD` | `117.241.77.78` | 2026-06-20T11:40:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **62** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 9 |
| Go SSH scanner | 7 |
| libssh | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 9 | 9 |
| `0a07365cc01f...` | Generic scanner | 3 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 2 | 2 |
| `f555226df196...` | Mirai/variant | 1 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 9 | 9 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 2 | 2 | — |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **27** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS4230` | CLARO S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-94414056a671

| Field | Detail |
|---|---|
| **Source IP** | `49.43.35[.]54` |
| **First Seen** | 2026-06-20 10:53 |
| **Last Seen** | 2026-06-20 10:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 10:53:07` | `cowrie.session.connect` |
| `2026-06-20 10:53:09` | `cowrie.client.version` |
| `2026-06-20 10:53:09` | `cowrie.client.kex` |
| `2026-06-20 10:53:10` | `cowrie.login.success` |
| `2026-06-20 10:53:11` | `cowrie.direct-tcpip.request` |
| `2026-06-20 10:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.43.35[.]54` to AbuseIPDB if not already reported
- [ ] Block `49.43.35[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182441827bdc

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-06-20 11:40 |
| **Last Seen** | 2026-06-20 11:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 11:40:53` | `cowrie.session.connect` |
| `2026-06-20 11:40:54` | `cowrie.client.version` |
| `2026-06-20 11:40:54` | `cowrie.client.kex` |
| `2026-06-20 11:40:56` | `cowrie.login.success` |
| `2026-06-20 11:40:56` | `cowrie.direct-tcpip.request` |
| `2026-06-20 11:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.138[.]178` | **6** | 2026-06-20 11:04 | 2026-06-20 11:13 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `47.88.12[.]190` | **3** | 2026-06-20 10:55 | 2026-06-20 10:55 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `134.209.241[.]3` | **2** | 2026-06-20 11:02 | 2026-06-20 11:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.98.128[.]249` | **2** | 2026-06-20 13:28 | 2026-06-20 13:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-06-20 10:48 | 2026-06-20 10:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-06-20 12:55 | 2026-06-20 12:55 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.73.101[.]168` | 1 | 2026-06-20 14:03 | 2026-06-20 14:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `111.70.9[.]143` | 1 | 2026-06-20 12:40 | 2026-06-20 12:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.186.7[.]9` | 1 | 2026-06-20 13:33 | 2026-06-20 13:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.166.252[.]192` | 1 | 2026-06-20 12:43 | 2026-06-20 12:44 | 12s | 0 | `T1592` | 🟢 LOW |
| `132.251.234[.]110` | 1 | 2026-06-20 12:22 | 2026-06-20 12:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.126[.]104` | 1 | 2026-06-20 13:38 | 2026-06-20 13:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `158.178.197[.]7` | 1 | 2026-06-20 13:25 | 2026-06-20 13:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `171.25.158[.]57` | 1 | 2026-06-20 10:55 | 2026-06-20 10:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.52.52[.]162` | 1 | 2026-06-20 10:54 | 2026-06-20 10:54 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.49.97[.]15` | 1 | 2026-06-20 13:10 | 2026-06-20 13:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.179[.]251` | 1 | 2026-06-20 11:22 | 2026-06-20 11:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.49.223[.]131` | 1 | 2026-06-20 13:32 | 2026-06-20 13:33 | 32s | 0 | `T1592` | 🟢 LOW |
| `81.237.155[.]113` | 1 | 2026-06-20 12:52 | 2026-06-20 12:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.34.96[.]151` | 1 | 2026-06-20 11:50 | 2026-06-20 11:50 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `47.88.12[.]190` | US | Alibaba Cloud - US | **100** ⚠️ | 27 |
| `117.241.77[.]78` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `134.209.241[.]3` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `158.178.197[.]7` | FR | Oracle Corporation | **100** ⚠️ | 4 |
| `189.52.52[.]162` | BR | Claro S/A | **100** ⚠️ | 50 |
| `89.34.96[.]151` | GB | Hydra Communications Ltd | **100** ⚠️ | 6 |
| `132.251.234[.]110` | BO | Comteco Ltda | **100** ⚠️ | 4 |
| `103.203.57[.]19` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `103.73.101[.]168` | PK | KK Networks | **100** ⚠️ | 8 |
| `64.49.97[.]15` | US | ProTek Communications, LLC | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 21 below threshold 25 | 24 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 62 cases |
| Tool 34  | Credential Extractor        | ✅ 14 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (48.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 20 recon entry/entries in table (5 group(s) consolidating 15 session(s)).

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
_Report time: 2026-06-20T14:10:39Z_
