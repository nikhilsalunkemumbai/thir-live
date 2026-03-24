# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T07:01:26Z |
| **Shift Time** | 07:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **125** |
| Confirmed Threats | **28** |
| False Positives Filtered | **97** (77.6%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **13** |
| High Severity Cases | **89** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **36** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **108** |
| Unique Credential Pairs | **107** |
| Unique Usernames | **19** |
| Unique Passwords | **102** |
| Successful Auth Pairs | **89** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 90 |
| `james` | 1 |
| `bwadmin` | 1 |
| `sql` | 1 |
| `unknown` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 2 |
| `rootpass` | 2 |
| `12345` | 2 |
| `qwerty123` | 2 |
| `pass` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `rootpass` | 2 |
| `james` | `James123` | 1 |
| `bwadmin` | `12345678` | 1 |
| `sql` | `sql123` | 1 |
| `unknown` | `unknown2005` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `rootpass` | `37.28.177.141` | 2026-03-24T04:22:37 |
| `root` | `rootpass` | `203.192.247.84` | 2026-03-24T04:22:49 |
| `root` | `123` | `64.236.176.194` | 2026-03-24T05:18:51 |
| `root` | `1234` | `64.236.176.194` | 2026-03-24T05:19:23 |
| `root` | `password` | `64.236.176.194` | 2026-03-24T05:19:55 |
| `root` | `12345678` | `64.236.176.194` | 2026-03-24T05:20:48 |
| `root` | `12345` | `64.236.176.194` | 2026-03-24T05:21:33 |
| `root` | `admin` | `64.236.176.194` | 2026-03-24T05:21:54 |
| `root` | `solana` | `64.236.176.194` | 2026-03-24T05:22:45 |
| `root` | `ubuntu` | `64.236.176.194` | 2026-03-24T05:23:27 |
| `root` | `123456789` | `64.236.176.194` | 2026-03-24T05:24:03 |
| `root` | `sol` | `64.236.176.194` | 2026-03-24T05:25:02 |
| `root` | `qwerty` | `64.236.176.194` | 2026-03-24T05:26:21 |
| `root` | `admin123` | `64.236.176.194` | 2026-03-24T05:27:13 |
| `root` | `1` | `64.236.176.194` | 2026-03-24T05:28:06 |
| `root` | `P@ssw0rd` | `64.236.176.194` | 2026-03-24T05:29:00 |
| `root` | `111111` | `64.236.176.194` | 2026-03-24T05:30:04 |
| `root` | `1qaz@WSX` | `64.236.176.194` | 2026-03-24T05:31:21 |
| `root` | `validator` | `64.236.176.194` | 2026-03-24T05:32:51 |
| `root` | `solv` | `64.236.176.194` | 2026-03-24T05:34:47 |
| `root` | `passw0rd` | `64.236.176.194` | 2026-03-24T05:36:41 |
| `root` | `1234567` | `64.236.176.194` | 2026-03-24T05:38:22 |
| `root` | `root123` | `64.236.176.194` | 2026-03-24T05:39:47 |
| `root` | `abc123` | `64.236.176.194` | 2026-03-24T05:41:10 |
| `root` | `password1` | `64.236.176.194` | 2026-03-24T05:42:26 |
| `root` | `1234567890` | `64.236.176.194` | 2026-03-24T05:43:38 |
| `root` | `123123` | `64.236.176.194` | 2026-03-24T05:44:47 |
| `root` | `1q2w3e4r` | `64.236.176.194` | 2026-03-24T05:45:53 |
| `root` | `node` | `64.236.176.194` | 2026-03-24T05:46:55 |
| `root` | `firedancer` | `64.236.176.194` | 2026-03-24T05:47:58 |
| `root` | `welcome` | `64.236.176.194` | 2026-03-24T05:49:00 |
| `root` | `letmein` | `64.236.176.194` | 2026-03-24T05:49:58 |
| `root` | `654321` | `64.236.176.194` | 2026-03-24T05:51:00 |
| `root` | `test` | `64.236.176.194` | 2026-03-24T05:52:05 |
| `root` | `qwer1234` | `64.236.176.194` | 2026-03-24T05:53:15 |
| `root` | `123qwe` | `64.236.176.194` | 2026-03-24T05:54:28 |
| `root` | `p@ssw0rd` | `64.236.176.194` | 2026-03-24T05:55:47 |
| `root` | `trader` | `64.236.176.194` | 2026-03-24T05:57:08 |
| `root` | `root2004` | `111.70.41.194` | 2026-03-24T05:57:46 |
| `root` | `bot` | `64.236.176.194` | 2026-03-24T05:58:29 |
| `root` | `user` | `64.236.176.194` | 2026-03-24T05:59:52 |
| `root` | `1234qwer` | `64.236.176.194` | 2026-03-24T06:01:14 |
| `root` | `1111` | `64.236.176.194` | 2026-03-24T06:02:32 |
| `root` | `!@#` | `64.236.176.194` | 2026-03-24T06:03:49 |
| `root` | `4rfv$RFV` | `64.236.176.194` | 2026-03-24T06:05:00 |
| `root` | `raydium` | `64.236.176.194` | 2026-03-24T06:06:09 |
| `root` | `trading` | `64.236.176.194` | 2026-03-24T06:07:18 |
| `root` | `Aa123456` | `64.236.176.194` | 2026-03-24T06:08:25 |
| `root` | `qwerty123` | `64.236.176.194` | 2026-03-24T06:09:33 |
| `root` | `toor` | `64.236.176.194` | 2026-03-24T06:10:44 |
| `root` | `(public key)` | `64.236.176.194` | 2026-03-24T06:11:58 |
| `root` | `test123` | `64.236.176.194` | 2026-03-24T06:13:12 |
| `root` | `pass123` | `64.236.176.194` | 2026-03-24T06:14:27 |
| `root` | `evm` | `64.236.176.194` | 2026-03-24T06:15:42 |
| `root` | `123abc` | `64.236.176.194` | 2026-03-24T06:16:59 |
| `root` | `321` | `64.236.176.194` | 2026-03-24T06:18:18 |
| `root` | `jito` | `64.236.176.194` | 2026-03-24T06:19:35 |
| `root` | `eigenlayer` | `64.236.176.194` | 2026-03-24T06:20:50 |
| `root` | `default` | `64.236.176.194` | 2026-03-24T06:22:04 |
| `root` | `guest` | `64.236.176.194` | 2026-03-24T06:23:19 |
| `root` | `000000` | `64.236.176.194` | 2026-03-24T06:24:37 |
| `root` | `12` | `64.236.176.194` | 2026-03-24T06:25:55 |
| `root` | `administrator` | `64.236.176.194` | 2026-03-24T06:27:14 |
| `root` | `debian` | `64.236.176.194` | 2026-03-24T06:28:32 |
| `root` | `123321` | `64.236.176.194` | 2026-03-24T06:29:50 |
| `root` | `centos` | `64.236.176.194` | 2026-03-24T06:31:09 |
| `root` | `ethereum` | `64.236.176.194` | 2026-03-24T06:32:26 |
| `root` | `sniper` | `64.236.176.194` | 2026-03-24T06:33:43 |
| `root` | `mysql` | `64.236.176.194` | 2026-03-24T06:34:57 |
| `root` | `admin@123` | `64.236.176.194` | 2026-03-24T06:36:12 |
| `root` | `docker` | `64.236.176.194` | 2026-03-24T06:37:29 |
| `root` | `4$RFV` | `64.236.176.194` | 2026-03-24T06:38:46 |
| `root` | `evmbot` | `64.236.176.194` | 2026-03-24T06:40:06 |
| `root` | `1qaz2wsx` | `64.236.176.194` | 2026-03-24T06:41:25 |
| `root` | `raspberry` | `64.236.176.194` | 2026-03-24T06:42:45 |
| `root` | `pass` | `64.236.176.194` | 2026-03-24T06:44:06 |
| `root` | `ubnt` | `64.236.176.194` | 2026-03-24T06:45:27 |
| `root` | `oracle` | `64.236.176.194` | 2026-03-24T06:46:47 |
| `root` | `wasd` | `64.236.176.194` | 2026-03-24T06:48:05 |
| `root` | `eigen` | `64.236.176.194` | 2026-03-24T06:49:23 |
| `root` | `postgres` | `64.236.176.194` | 2026-03-24T06:50:40 |
| `root` | `Admin@123` | `64.236.176.194` | 2026-03-24T06:51:55 |
| `root` | `P@ssw0rd123` | `64.236.176.194` | 2026-03-24T06:53:12 |
| `root` | `54321` | `64.236.176.194` | 2026-03-24T06:54:34 |
| `root` | `123qwerty` | `64.236.176.194` | 2026-03-24T06:55:51 |
| `root` | `4321` | `64.236.176.194` | 2026-03-24T06:57:12 |
| `root` | `www` | `64.236.176.194` | 2026-03-24T06:58:31 |
| `root` | `qwe123` | `64.236.176.194` | 2026-03-24T06:59:50 |
| `root` | `apache` | `64.236.176.194` | 2026-03-24T07:01:09 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **22** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS17421` | Mobile Business Group | 2 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 2 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS25159` | PJSC MegaFon | 1 | HIGH |
| `AS2516` | KDDI CORPORATION | 1 | LOW |
| `AS9299` | Philippine Long Distance Telephone Company | 1 | HIGH |
| `AS17665` | ONEOTT INTERTAINMENT LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-db599a490b42

| Field | Detail |
|---|---|
| **Source IP** | `37.28.177[.]141` |
| **First Seen** | 2026-03-24 04:22 |
| **Last Seen** | 2026-03-24 04:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 04:22:35` | `cowrie.session.connect` |
| `2026-03-24 04:22:36` | `cowrie.client.version` |
| `2026-03-24 04:22:36` | `cowrie.client.kex` |
| `2026-03-24 04:22:37` | `cowrie.login.success` |
| `2026-03-24 04:22:38` | `cowrie.direct-tcpip.request` |
| `2026-03-24 04:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.28.177[.]141` to AbuseIPDB if not already reported
- [ ] Block `37.28.177[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3c03e80198

| Field | Detail |
|---|---|
| **Source IP** | `203.192.247[.]84` |
| **First Seen** | 2026-03-24 04:22 |
| **Last Seen** | 2026-03-24 04:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 04:22:47` | `cowrie.session.connect` |
| `2026-03-24 04:22:48` | `cowrie.client.version` |
| `2026-03-24 04:22:48` | `cowrie.client.kex` |
| `2026-03-24 04:22:49` | `cowrie.login.success` |
| `2026-03-24 04:22:50` | `cowrie.direct-tcpip.request` |
| `2026-03-24 04:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.192.247[.]84` to AbuseIPDB if not already reported
- [ ] Block `203.192.247[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c412e679e653

| Field | Detail |
|---|---|
| **Source IP** | `111.70.41[.]194` |
| **First Seen** | 2026-03-24 05:57 |
| **Last Seen** | 2026-03-24 05:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 05:57:44` | `cowrie.session.connect` |
| `2026-03-24 05:57:45` | `cowrie.client.version` |
| `2026-03-24 05:57:45` | `cowrie.client.kex` |
| `2026-03-24 05:57:46` | `cowrie.login.success` |
| `2026-03-24 05:57:47` | `cowrie.direct-tcpip.request` |
| `2026-03-24 05:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.41[.]194` to AbuseIPDB if not already reported
- [ ] Block `111.70.41[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.125.165[.]132` | **10** | 2026-03-24 06:38 | 2026-03-24 06:58 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `161.132.180[.]118` | **5** | 2026-03-24 04:19 | 2026-03-24 04:28 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.91[.]34` | 1 | 2026-03-24 04:28 | 2026-03-24 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.32[.]11` | 1 | 2026-03-24 05:40 | 2026-03-24 05:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-03-24 05:19 | 2026-03-24 05:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.55.141[.]201` | 1 | 2026-03-24 04:24 | 2026-03-24 04:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-03-24 05:51 | 2026-03-24 05:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-03-24 06:27 | 2026-03-24 06:27 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-03-24 05:59 | 2026-03-24 05:59 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.70[.]124` | 1 | 2026-03-24 04:25 | 2026-03-24 04:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.98.68[.]61` | 1 | 2026-03-24 05:09 | 2026-03-24 05:09 | 14s | 0 | `T1592` | 🟢 LOW |
| `94.254.244[.]211` | 1 | 2026-03-24 04:42 | 2026-03-24 04:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `122.55.141[.]201` | PH | IPG | **100** ⚠️ | 9 |
| `183.93.165[.]103` | CN | China Unicom Hubei Province Network | **100** ⚠️ | 6 |
| `2.55.70[.]124` | IL | Partner Communications Ltd. | **100** ⚠️ | 28 |
| `111.70.41[.]194` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 2 |
| `111.70.32[.]11` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 7 |
| `203.192.247[.]84` | IN | Indusind Media And Communication Ltd. | **100** ⚠️ | 27 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `183.247.171[.]186` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `59.98.68[.]61` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 0 |
| `101.126.91[.]34` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 118 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 89 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 11 |

---

## 🔕 False Positive Summary (97 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 87 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 125 cases |
| Tool 34  | Credential Extractor        | ✅ 108 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 16 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 97 filtered (77.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 12 recon entry/entries in table (2 group(s) consolidating 15 session(s)).

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
_Report time: 2026-03-24T07:01:26Z_
