# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T18:42:48Z |
| **Shift Time** | 18:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **81** |
| Confirmed Threats | **24** |
| False Positives Filtered | **57** (70.4%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **16** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **77** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **15** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `GET / HTTP/1.0` | 2 |
| `OPTIONS / HTTP/1.0` | 2 |
| `test` | 2 |
| `Nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 4 |
| `ankurkudintzi` | 2 |
| `qwerty123456` | 1 |
| `ubuntu` | 1 |
| `66666` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.0` | `` | 2 |
| `OPTIONS / HTTP/1.0` | `` | 2 |
| `root` | `ankurkudintzi` | 2 |
| `Nobody` | `qwerty123456` | 1 |
| `root` | `ubuntu` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `4.17.226.146` | 2026-04-03T16:47:20 |
| `root` | `ankurkudintzi` | `139.59.62.105` | 2026-04-03T18:14:43 |
| `root` | `ankurkudintzi` | `209.38.92.238` | 2026-04-03T18:22:59 |
| `root` | `hunt5759` | `138.118.152.18` | 2026-04-03T18:32:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **81** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 12 |
| Go SSH scanner | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 12 | 12 |
| `16443846184e...` | Generic scanner | 2 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 12 | 12 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `16443846184e...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox BKQTF
```
Source IPs: `138.118.152.18`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **27** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS29518` | Bredband2 AB | 1 | MEDIUM |
| `AS20001` | Charter Communications Inc | 1 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS3301` | Telia Company AB | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-505b17b38db3

| Field | Detail |
|---|---|
| **Source IP** | `4.17.226[.]146` |
| **First Seen** | 2026-04-03 16:47 |
| **Last Seen** | 2026-04-03 16:48 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 16:47:19` | `cowrie.session.connect` |
| `2026-04-03 16:47:19` | `cowrie.client.version` |
| `2026-04-03 16:47:20` | `cowrie.client.kex` |
| `2026-04-03 16:47:20` | `cowrie.login.success` |
| `2026-04-03 16:48:46` | `cowrie.session.file_upload` |
| `2026-04-03 16:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.17.226[.]146` to AbuseIPDB if not already reported
- [ ] Block `4.17.226[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70aecf92f15a

| Field | Detail |
|---|---|
| **Source IP** | `139.59.62[.]105` |
| **First Seen** | 2026-04-03 18:14 |
| **Last Seen** | 2026-04-03 18:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 18:14:38` | `cowrie.session.connect` |
| `2026-04-03 18:14:39` | `cowrie.client.version` |
| `2026-04-03 18:14:39` | `cowrie.client.kex` |
| `2026-04-03 18:14:43` | `cowrie.login.success` |
| `2026-04-03 18:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.59.62[.]105` to AbuseIPDB if not already reported
- [ ] Block `139.59.62[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f5bae1d155

| Field | Detail |
|---|---|
| **Source IP** | `209.38.92[.]238` |
| **First Seen** | 2026-04-03 18:22 |
| **Last Seen** | 2026-04-03 18:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 18:22:53` | `cowrie.session.connect` |
| `2026-04-03 18:22:54` | `cowrie.client.version` |
| `2026-04-03 18:22:54` | `cowrie.client.kex` |
| `2026-04-03 18:22:59` | `cowrie.login.success` |
| `2026-04-03 18:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.92[.]238` to AbuseIPDB if not already reported
- [ ] Block `209.38.92[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fbba939818d

| Field | Detail |
|---|---|
| **Source IP** | `138.118.152[.]18` |
| **First Seen** | 2026-04-03 18:32 |
| **Last Seen** | 2026-04-03 18:34 |
| **Session Duration** | 105s |
| **Login Attempts** | 3 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox BKQTF` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 18:32:24` | `cowrie.session.connect` |
| `2026-04-03 18:32:25` | `cowrie.telnet.option` |
| `2026-04-03 18:32:25` | `cowrie.login.failed` |
| `2026-04-03 18:32:26` | `cowrie.telnet.option` |
| `2026-04-03 18:32:26` | `cowrie.login.failed` |
| `2026-04-03 18:32:27` | `cowrie.telnet.option` |
| `2026-04-03 18:32:27` | `cowrie.login.success` |
| `2026-04-03 18:32:27` | `cowrie.session.params` |
| `2026-04-03 18:32:28` | `cowrie.command.input` |
| `2026-04-03 18:32:28` | `cowrie.command.input` |
| `2026-04-03 18:32:28` | `cowrie.command.failed` |
| `2026-04-03 18:32:28` | `cowrie.command.input` |
| `2026-04-03 18:32:28` | `cowrie.command.failed` |
| `2026-04-03 18:32:28` | `cowrie.command.input` |
| `2026-04-03 18:32:28` | `cowrie.command.input` |
| `2026-04-03 18:32:28` | `cowrie.command.input` |
| `2026-04-03 18:32:29` | `cowrie.command.input` |
| `2026-04-03 18:32:29` | `cowrie.command.input` |
| `2026-04-03 18:32:29` | `cowrie.command.failed` |
| `2026-04-03 18:32:29` | `cowrie.command.input` |
| `2026-04-03 18:32:30` | `cowrie.command.input` |
| `2026-04-03 18:32:30` | `cowrie.command.input` |
| `2026-04-03 18:32:30` | `cowrie.command.input` |
| `2026-04-03 18:32:30` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.input` |
| `2026-04-03 18:32:31` | `cowrie.command.failed` |
| `2026-04-03 18:34:09` | `cowrie.log.closed` |
| `2026-04-03 18:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.152[.]18` to AbuseIPDB if not already reported
- [ ] Block `138.118.152[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.211.7[.]162` | 1 | 2026-04-03 18:29 | 2026-04-03 18:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.1.128[.]94` | 1 | 2026-04-03 17:16 | 2026-04-03 17:16 | 21s | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]240` | 1 | 2026-04-03 18:10 | 2026-04-03 18:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.7[.]45` | 1 | 2026-04-03 18:04 | 2026-04-03 18:04 | 1s | 0 | `T1592` | 🟢 LOW |
| `139.59.62[.]105` | 1 | 2026-04-03 18:12 | 2026-04-03 18:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.29.204[.]161` | 1 | 2026-04-03 17:31 | 2026-04-03 17:31 | 6s | 0 | `T1592` | 🟢 LOW |
| `14.38.208[.]166` | 1 | 2026-04-03 17:09 | 2026-04-03 17:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `166.130.176[.]136` | 1 | 2026-04-03 17:11 | 2026-04-03 17:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]134` | 1 | 2026-04-03 17:02 | 2026-04-03 17:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.186.183[.]88` | 1 | 2026-04-03 18:29 | 2026-04-03 18:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]29` | 1 | 2026-04-03 17:50 | 2026-04-03 17:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `209.38.92[.]238` | 1 | 2026-04-03 18:20 | 2026-04-03 18:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.66.196[.]11` | 1 | 2026-04-03 18:00 | 2026-04-03 18:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `24.45.233[.]231` | 1 | 2026-04-03 16:43 | 2026-04-03 16:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.41.81[.]65` | 1 | 2026-04-03 17:41 | 2026-04-03 17:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.188.204[.]213` | 1 | 2026-04-03 16:52 | 2026-04-03 16:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.137.147[.]126` | 1 | 2026-04-03 17:39 | 2026-04-03 17:39 | 14s | 0 | `T1592` | 🟢 LOW |
| `65.20.167[.]117` | 1 | 2026-04-03 18:00 | 2026-04-03 18:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.80.65[.]214` | 1 | 2026-04-03 17:22 | 2026-04-03 17:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.187.230[.]168` | 1 | 2026-04-03 18:09 | 2026-04-03 18:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
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
| `213.66.196[.]11` | SE | Telia Network services | **100** ⚠️ | 12 |
| `188.186.183[.]88` | RU | CJSC ER-Telecom Holding Tyumen' branch | **100** ⚠️ | 10 |
| `61.137.147[.]126` | CN | China Unicom Liaoning province network | **100** ⚠️ | 7 |
| `4.17.226[.]146` | US | Level 3 Parent, LLC | **100** ⚠️ | 50 |
| `24.45.233[.]231` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 12 |
| `31.41.81[.]65` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `190.90.79[.]29` | CO | IP TECHNOLOGIES S.A.S. | **100** ⚠️ | 2 |
| `209.38.92[.]238` | AU | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `78.187.230[.]168` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 5 |
| `166.130.176[.]136` | US | AT&T Enterprises, LLC | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 32 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 81 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (70.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 20 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-03T18:42:48Z_
