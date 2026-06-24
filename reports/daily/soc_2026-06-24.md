# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-24 |
| **Generated At** | 2026-06-24T07:43:59Z |
| **Shift Time** | 07:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **88** |
| Confirmed Threats | **60** |
| False Positives Filtered | **28** (31.8%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **13** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **87** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **8** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `user` | 2 |
| `root` | 2 |
| `nn` | 1 |
| `test` | 1 |
| `unknown` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 1 |
| `1994` | 1 |
| `3333` | 1 |
| `123321` | 1 |
| `maintenance` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nn` | `123456` | 1 |
| `user` | `1994` | 1 |
| `test` | `3333` | 1 |
| `unknown` | `123321` | 1 |
| `blank` | `maintenance` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `83.177.240.110` | 2026-06-24T06:12:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **88** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 6 |
| libssh | 3 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 6 | 6 |
| `f555226df196...` | Mirai/variant | 2 | 2 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 6 | 6 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `f555226df196...` | libssh | 2 | 2 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **23** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS211298` | Driftnet Ltd | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS56046` | China Mobile communications corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c410e539fd56

| Field | Detail |
|---|---|
| **Source IP** | `83.177.240[.]110` |
| **First Seen** | 2026-06-24 06:12 |
| **Last Seen** | 2026-06-24 06:13 |
| **Session Duration** | 42s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-24 06:12:46` | `cowrie.session.connect` |
| `2026-06-24 06:12:46` | `cowrie.client.version` |
| `2026-06-24 06:12:46` | `cowrie.client.kex` |
| `2026-06-24 06:12:47` | `cowrie.login.failed` |
| `2026-06-24 06:12:48` | `cowrie.login.success` |
| `2026-06-24 06:12:49` | `cowrie.session.params` |
| `2026-06-24 06:12:49` | `cowrie.command.input` |
| `2026-06-24 06:12:49` | `cowrie.command.failed` |
| `2026-06-24 06:12:49` | `cowrie.log.closed` |
| `2026-06-24 06:12:50` | `cowrie.session.params` |
| `2026-06-24 06:12:50` | `cowrie.command.input` |
| `2026-06-24 06:12:50` | `cowrie.log.closed` |
| `2026-06-24 06:12:50` | `cowrie.session.params` |
| `2026-06-24 06:12:50` | `cowrie.command.input` |
| `2026-06-24 06:12:50` | `cowrie.log.closed` |
| `2026-06-24 06:12:51` | `cowrie.session.params` |
| `2026-06-24 06:12:51` | `cowrie.command.input` |
| `2026-06-24 06:12:51` | `cowrie.log.closed` |
| `2026-06-24 06:12:52` | `cowrie.session.params` |
| `2026-06-24 06:12:52` | `cowrie.command.input` |
| `2026-06-24 06:12:52` | `cowrie.log.closed` |
| `2026-06-24 06:12:52` | `cowrie.session.params` |
| `2026-06-24 06:12:52` | `cowrie.command.input` |
| `2026-06-24 06:12:53` | `cowrie.log.closed` |
| `2026-06-24 06:12:53` | `cowrie.session.params` |
| `2026-06-24 06:12:53` | `cowrie.command.input` |
| `2026-06-24 06:12:53` | `cowrie.log.closed` |
| `2026-06-24 06:12:54` | `cowrie.session.params` |
| `2026-06-24 06:12:54` | `cowrie.command.input` |
| `2026-06-24 06:12:54` | `cowrie.log.closed` |
| `2026-06-24 06:12:54` | `cowrie.session.params` |
| `2026-06-24 06:12:54` | `cowrie.command.input` |
| `2026-06-24 06:12:55` | `cowrie.log.closed` |
| `2026-06-24 06:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.177.240[.]110` to AbuseIPDB if not already reported
- [ ] Block `83.177.240[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.135.41[.]132` | **25** | 2026-06-24 04:11 | 2026-06-24 04:16 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `206.81.2[.]201` | **4** | 2026-06-24 06:07 | 2026-06-24 06:52 | 2m | 0 | `T1592` | 🟢 LOW |
| `46.32.228[.]2` | **4** | 2026-06-24 04:56 | 2026-06-24 06:04 | 5m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]228` | **4** | 2026-06-24 06:36 | 2026-06-24 06:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]148` | **2** | 2026-06-24 04:04 | 2026-06-24 04:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-06-24 07:20 | 2026-06-24 07:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]166` | **2** | 2026-06-24 05:37 | 2026-06-24 05:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]171` | **2** | 2026-06-24 06:22 | 2026-06-24 06:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.211[.]111` | 1 | 2026-06-24 06:08 | 2026-06-24 06:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.165.72[.]15` | 1 | 2026-06-24 04:31 | 2026-06-24 04:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.229[.]247` | 1 | 2026-06-24 05:04 | 2026-06-24 05:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.75.211[.]204` | 1 | 2026-06-24 07:03 | 2026-06-24 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.53[.]200` | 1 | 2026-06-24 04:26 | 2026-06-24 04:27 | 10s | 0 | `T1592` | 🟢 LOW |
| `211.178.247[.]182` | 1 | 2026-06-24 04:26 | 2026-06-24 04:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.33.204[.]130` | 1 | 2026-06-24 06:55 | 2026-06-24 06:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.206.136[.]24` | 1 | 2026-06-24 07:01 | 2026-06-24 07:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.64.33[.]82` | 1 | 2026-06-24 05:26 | 2026-06-24 05:26 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `48.214.54[.]114` | 1 | 2026-06-24 07:43 | 2026-06-24 07:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.154[.]169` | 1 | 2026-06-24 05:58 | 2026-06-24 05:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.206.201[.]253` | 1 | 2026-06-24 07:22 | 2026-06-24 07:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.199.224[.]55` | 1 | 2026-06-24 06:03 | 2026-06-24 06:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.150.220[.]233` | 1 | 2026-06-24 07:40 | 2026-06-24 07:40 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/73** 🔴 |
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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/73 ✅ |
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
| `46.32.228[.]2` | GB | Heart Internet Ltd | **100** ⚠️ | 2 |
| `139.135.41[.]132` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 8 |
| `183.171.53[.]200` | MY | Celcom Axiata Berhad | **100** ⚠️ | 23 |
| `115.190.211[.]111` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 31 |
| `49.206.201[.]253` | IN | ACT Hyderabad | **100** ⚠️ | 50 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `66.132.224[.]228` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.186[.]166` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `20.64.105[.]148` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `36.64.33[.]82` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 12 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 88 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (31.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 22 recon entry/entries in table (8 group(s) consolidating 45 session(s)).

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
_Report time: 2026-06-24T07:43:59Z_
