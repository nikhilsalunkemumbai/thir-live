# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-20 |
| **Generated At** | 2026-06-20T19:41:44Z |
| **Shift Time** | 19:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **47** |
| Confirmed Threats | **42** |
| False Positives Filtered | **5** (10.6%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **10** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **43** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **7** |
| Unique Passwords | **9** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `User` | 1 |
| `nobody` | 1 |
| `admin` | 1 |
| `support` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `iDirect` | 2 |
| `jwQUjwsICF` | 1 |
| `1` | 1 |
| `nobody2004` | 1 |
| `Symbol` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `iDirect` | 2 |
| `root` | `jwQUjwsICF` | 1 |
| `User` | `1` | 1 |
| `nobody` | `nobody2004` | 1 |
| `admin` | `Symbol` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `jwQUjwsICF` | `49.233.180.26` | 2026-06-20T18:06:12 |
| `root` | `iDirect` | `49.118.249.73` | 2026-06-20T18:35:54 |
| `root` | `33333333` | `65.20.202.4` | 2026-06-20T19:16:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **47** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 9 |
| Unknown | 3 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 7 | 7 |
| `f8e6c99abb65...` | Mirai/variant | 2 | 1 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 7 | 7 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `f8e6c99abb65...` | OpenSSH | 2 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 1 | `T1105, T1059.004` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
/bin/busybox junI2lF1
```
Source IPs: `49.118.249.73`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **15** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS42682` | JSC ER-Telecom Holding | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS22773` | Cox Communications Inc. | 1 | LOW |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS142647` | Nasstec Airnet Networks Private Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4ffc777d2470

| Field | Detail |
|---|---|
| **Source IP** | `49.233.180[.]26` |
| **First Seen** | 2026-06-20 18:06 |
| **Last Seen** | 2026-06-20 18:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:06:11` | `cowrie.session.connect` |
| `2026-06-20 18:06:11` | `cowrie.client.version` |
| `2026-06-20 18:06:11` | `cowrie.client.kex` |
| `2026-06-20 18:06:12` | `cowrie.login.success` |
| `2026-06-20 18:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.233.180[.]26` to AbuseIPDB if not already reported
- [ ] Block `49.233.180[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30595b44016

| Field | Detail |
|---|---|
| **Source IP** | `49.118.249[.]73` |
| **First Seen** | 2026-06-20 18:35 |
| **Last Seen** | 2026-06-20 18:38 |
| **Session Duration** | 155s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/busybox junI2lF1 ` |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:35:50` | `cowrie.session.connect` |
| `2026-06-20 18:35:50` | `cowrie.client.version` |
| `2026-06-20 18:35:50` | `cowrie.client.kex` |
| `2026-06-20 18:35:52` | `cowrie.login.failed` |
| `2026-06-20 18:35:54` | `cowrie.login.success` |
| `2026-06-20 18:35:54` | `cowrie.client.size` |
| `2026-06-20 18:35:54` | `cowrie.session.params` |
| `2026-06-20 18:35:54` | `cowrie.command.input` |
| `2026-06-20 18:35:54` | `cowrie.command.input` |
| `2026-06-20 18:38:25` | `cowrie.log.closed` |
| `2026-06-20 18:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.118.249[.]73` to AbuseIPDB if not already reported
- [ ] Block `49.118.249[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d2529ca061

| Field | Detail |
|---|---|
| **Source IP** | `49.118.249[.]73` |
| **First Seen** | 2026-06-20 18:38 |
| **Last Seen** | 2026-06-20 18:40 |
| **Session Duration** | 153s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/busybox junI2lF1 ` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 18:38:25` | `cowrie.session.connect` |
| `2026-06-20 18:38:25` | `cowrie.client.version` |
| `2026-06-20 18:38:25` | `cowrie.client.kex` |
| `2026-06-20 18:38:27` | `cowrie.login.success` |
| `2026-06-20 18:38:27` | `cowrie.client.size` |
| `2026-06-20 18:38:27` | `cowrie.session.params` |
| `2026-06-20 18:38:28` | `cowrie.command.input` |
| `2026-06-20 18:38:28` | `cowrie.command.input` |
| `2026-06-20 18:40:58` | `cowrie.log.closed` |
| `2026-06-20 18:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.118.249[.]73` to AbuseIPDB if not already reported
- [ ] Block `49.118.249[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ec757d5c43

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-06-20 19:16 |
| **Last Seen** | 2026-06-20 19:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-20 19:16:27` | `cowrie.session.connect` |
| `2026-06-20 19:16:27` | `cowrie.client.version` |
| `2026-06-20 19:16:27` | `cowrie.client.kex` |
| `2026-06-20 19:16:28` | `cowrie.login.success` |
| `2026-06-20 19:16:29` | `cowrie.direct-tcpip.request` |
| `2026-06-20 19:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.173.7[.]161` | **25** | 2026-06-20 17:44 | 2026-06-20 17:49 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `103.220.91[.]138` | 1 | 2026-06-20 18:17 | 2026-06-20 18:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-06-20 19:16 | 2026-06-20 19:17 | 29s | 0 | `T1592` | 🟢 LOW |
| `172.183.149[.]72` | 1 | 2026-06-20 19:41 | 2026-06-20 19:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `20.171.46[.]137` | 1 | 2026-06-20 19:00 | 2026-06-20 19:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `24.229.22[.]106` | 1 | 2026-06-20 19:20 | 2026-06-20 19:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.28.253[.]144` | 1 | 2026-06-20 18:46 | 2026-06-20 18:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.206.194[.]29` | 1 | 2026-06-20 18:21 | 2026-06-20 18:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.231.89[.]119` | 1 | 2026-06-20 19:13 | 2026-06-20 19:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]174` | 1 | 2026-06-20 19:15 | 2026-06-20 19:15 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]205` | 1 | 2026-06-20 19:13 | 2026-06-20 19:13 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]11` | 1 | 2026-06-20 18:14 | 2026-06-20 18:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]5` | 1 | 2026-06-20 18:14 | 2026-06-20 18:14 | 3s | 0 | `T1592` | 🟢 LOW |
| `95.79.57[.]221` | 1 | 2026-06-20 18:37 | 2026-06-20 18:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `103.173.7[.]161` | PK | GRACE BROADBAND | **100** ⚠️ | 8 |
| `103.220.91[.]138` | IN | Mft Internet Private Limited | **100** ⚠️ | 50 |
| `94.231.206[.]11` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `65.20.202[.]4` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `49.206.194[.]29` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 50 |
| `106.246.89[.]70` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `172.183.149[.]72` | US | Microsoft Limited | **100** ⚠️ | 7 |
| `91.231.89[.]119` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `94.231.206[.]5` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `20.171.46[.]137` | US | Microsoft Corporation | **100** ⚠️ | 5 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 13 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 12 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 47 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (10.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 14 recon entry/entries in table (1 group(s) consolidating 25 session(s)).

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
_Report time: 2026-06-20T19:41:44Z_
