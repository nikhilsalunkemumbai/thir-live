# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T14:55:05Z |
| **Shift Time** | 14:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **625** |
| Confirmed Threats | **532** |
| False Positives Filtered | **93** (14.9%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **13** |
| High Severity Cases | **87** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **538** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **91** |
| Unique Credential Pairs | **86** |
| Unique Usernames | **2** |
| Unique Passwords | **86** |
| Successful Auth Pairs | **84** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 89 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `toor` | 4 |
| `123456` | 2 |
| `admin` | 2 |
| `poison` | 1 |
| `tabata` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `toor` | 4 |
| `root` | `123456` | 2 |
| `admin` | `admin` | 2 |
| `root` | `poison` | 1 |
| `root` | `tabata` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `poison` | `124.116.244.88` | 2026-05-09T13:25:09 |
| `root` | `tabata` | `124.116.244.88` | 2026-05-09T13:25:09 |
| `root` | `nantes44` | `124.116.244.88` | 2026-05-09T13:25:10 |
| `root` | `supermotard` | `124.116.244.88` | 2026-05-09T13:25:10 |
| `root` | `morpheus` | `124.116.244.88` | 2026-05-09T13:25:11 |
| `root` | `student1` | `124.116.244.88` | 2026-05-09T13:25:11 |
| `root` | `messenger` | `124.116.244.88` | 2026-05-09T13:25:12 |
| `root` | `strato` | `124.116.244.88` | 2026-05-09T13:25:12 |
| `root` | `larousse` | `124.116.244.88` | 2026-05-09T13:25:14 |
| `root` | `silure` | `124.116.244.88` | 2026-05-09T13:25:14 |
| `root` | `shayna` | `124.116.244.88` | 2026-05-09T13:25:15 |
| `root` | `jenny1` | `124.116.244.88` | 2026-05-09T13:25:15 |
| `root` | `sensuel` | `124.116.244.88` | 2026-05-09T13:25:16 |
| `root` | `indien` | `124.116.244.88` | 2026-05-09T13:25:16 |
| `root` | `selma` | `124.116.244.88` | 2026-05-09T13:25:18 |
| `root` | `science1` | `124.116.244.88` | 2026-05-09T13:25:20 |
| `root` | `samoht` | `124.116.244.88` | 2026-05-09T13:25:21 |
| `root` | `roxane1` | `124.116.244.88` | 2026-05-09T13:25:22 |
| `root` | `reda` | `124.116.244.88` | 2026-05-09T13:25:24 |
| `root` | `davide` | `124.116.244.88` | 2026-05-09T13:25:24 |
| `root` | `raymart1` | `124.116.244.88` | 2026-05-09T13:25:26 |
| `root` | `darkangel` | `124.116.244.88` | 2026-05-09T13:25:26 |
| `root` | `rajaoui` | `124.116.244.88` | 2026-05-09T13:25:27 |
| `root` | `abdelkader` | `124.116.244.88` | 2026-05-09T13:25:27 |
| `root` | `rabbit1` | `124.116.244.88` | 2026-05-09T13:25:28 |
| `root` | `putri1` | `124.116.244.88` | 2026-05-09T13:25:30 |
| `root` | `pussycat1` | `124.116.244.88` | 2026-05-09T13:25:32 |
| `root` | `pucette` | `124.116.244.88` | 2026-05-09T13:25:33 |
| `root` | `pti` | `124.116.244.88` | 2026-05-09T13:25:34 |
| `root` | `prissou` | `124.116.244.88` | 2026-05-09T13:25:36 |
| `root` | `portugal91` | `124.116.244.88` | 2026-05-09T13:25:37 |
| `root` | `penis` | `124.116.244.88` | 2026-05-09T13:25:39 |
| `root` | `partir` | `124.116.244.88` | 2026-05-09T13:25:41 |
| `root` | `paris10` | `124.116.244.88` | 2026-05-09T13:25:42 |
| `root` | `palomino` | `124.116.244.88` | 2026-05-09T13:25:43 |
| `root` | `outlaw` | `124.116.244.88` | 2026-05-09T13:25:45 |
| `root` | `onetreehill` | `124.116.244.88` | 2026-05-09T13:25:47 |
| `root` | `odyssee` | `124.116.244.88` | 2026-05-09T13:25:48 |
| `root` | `nov` | `124.116.244.88` | 2026-05-09T13:25:50 |
| `root` | `nikki` | `124.116.244.88` | 2026-05-09T13:25:52 |
| `root` | `nausicaa` | `124.116.244.88` | 2026-05-09T13:25:53 |
| `root` | `naughty1` | `124.116.244.88` | 2026-05-09T13:25:54 |
| `root` | `polochon` | `124.116.244.88` | 2026-05-09T13:27:13 |
| `root` | `kaiser` | `124.116.244.88` | 2026-05-09T13:27:15 |
| `root` | `gil` | `124.116.244.88` | 2026-05-09T13:27:16 |
| `root` | `demarrer` | `124.116.244.88` | 2026-05-09T13:27:17 |
| `root` | `chicago` | `124.116.244.88` | 2026-05-09T13:27:18 |
| `root` | `mostaganem` | `124.116.244.88` | 2026-05-09T13:27:20 |
| `root` | `gendarme` | `124.116.244.88` | 2026-05-09T13:27:21 |
| `root` | `femme` | `124.116.244.88` | 2026-05-09T13:27:23 |
| `root` | `disney` | `124.116.244.88` | 2026-05-09T13:27:24 |
| `root` | `Dqu` | `124.116.244.88` | 2026-05-09T13:27:26 |
| `root` | `1965` | `124.116.244.88` | 2026-05-09T13:27:27 |
| `root` | `monalisa` | `124.116.244.88` | 2026-05-09T13:27:29 |
| `root` | `mario` | `124.116.244.88` | 2026-05-09T13:27:30 |
| `root` | `juninho` | `124.116.244.88` | 2026-05-09T13:27:32 |
| `root` | `toor` | `185.71.233.73` | 2026-05-09T13:27:33 |
| `root` | `eureka` | `124.116.244.88` | 2026-05-09T13:27:33 |
| `root` | `booba` | `124.116.244.88` | 2026-05-09T13:27:34 |
| `root` | `asse42` | `124.116.244.88` | 2026-05-09T13:27:36 |
| `root` | `080` | `124.116.244.88` | 2026-05-09T13:27:38 |
| `root` | `westside` | `124.116.244.88` | 2026-05-09T13:27:39 |
| `root` | `trompette` | `124.116.244.88` | 2026-05-09T13:27:40 |
| `root` | `tornade` | `124.116.244.88` | 2026-05-09T13:27:42 |
| `root` | `panasonic` | `124.116.244.88` | 2026-05-09T13:27:44 |
| `root` | `oli` | `124.116.244.88` | 2026-05-09T13:27:45 |
| `root` | `noumea` | `124.116.244.88` | 2026-05-09T13:27:46 |
| `root` | `mafille` | `124.116.244.88` | 2026-05-09T13:27:48 |
| `root` | `kevin1` | `124.116.244.88` | 2026-05-09T13:27:49 |
| `root` | `emilien` | `124.116.244.88` | 2026-05-09T13:27:50 |
| `root` | `carambar` | `124.116.244.88` | 2026-05-09T13:27:51 |
| `root` | `ann` | `124.116.244.88` | 2026-05-09T13:27:53 |
| `root` | `jesusc` | `124.116.244.88` | 2026-05-09T13:27:54 |
| `root` | `gladiator` | `124.116.244.88` | 2026-05-09T13:27:56 |
| `root` | `del` | `124.116.244.88` | 2026-05-09T13:27:57 |
| `root` | `cupidon` | `124.116.244.88` | 2026-05-09T13:27:59 |
| `root` | `amaury` | `124.116.244.88` | 2026-05-09T13:28:00 |
| `root` | `19831983` | `124.116.244.88` | 2026-05-09T13:28:01 |
| `root` | `volcom` | `124.116.244.88` | 2026-05-09T13:28:03 |
| `root` | `techno` | `124.116.244.88` | 2026-05-09T13:28:04 |
| `root` | `anubis` | `124.116.244.88` | 2026-05-09T13:28:05 |
| `root` | `sylvia` | `124.116.244.88` | 2026-05-09T13:28:07 |
| `root` | `sucette` | `124.116.244.88` | 2026-05-09T13:28:08 |
| `root` | `oxuhlaa` | `124.116.244.88` | 2026-05-09T13:28:09 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **625** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 86 |
| Unknown | 8 |
| libssh | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `01ca35584ad5...` | Modern SSH client | 85 | 1 |
| `748f8c627d3f...` | Mirai/variant | 5 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `01ca35584ad5...` | Go SSH scanner | 85 | 1 | Modern SSH client |
| `748f8c627d3f...` | Unknown | 5 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 3 | 2 | — |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS213412` | ONYPHE SAS | 1 | HIGH |
| `AS215929` | Data Campus Limited | 1 | HIGH |
| `AS199739` | Earthlink Telecommunications Equipment Trading & Services DMCC | 1 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS201533` | United Networks SE | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f7c065526052

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 13:27 |
| **Last Seen** | 2026-05-09 13:28 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, root` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 13:27:31` | `cowrie.session.connect` |
| `2026-05-09 13:27:31` | `cowrie.client.version` |
| `2026-05-09 13:27:32` | `cowrie.client.kex` |
| `2026-05-09 13:27:33` | `cowrie.login.success` |
| `2026-05-09 13:27:33` | `cowrie.client.size` |
| `2026-05-09 13:27:34` | `cowrie.session.params` |
| `2026-05-09 13:27:35` | `cowrie.command.input` |
| `2026-05-09 13:27:51` | `cowrie.command.input` |
| `2026-05-09 13:27:52` | `cowrie.command.input` |
| `2026-05-09 13:27:52` | `cowrie.command.failed` |
| `2026-05-09 13:28:08` | `cowrie.log.closed` |
| `2026-05-09 13:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae7bfea4b6bf

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 13:41 |
| **Last Seen** | 2026-05-09 13:42 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 13:41:40` | `cowrie.session.connect` |
| `2026-05-09 13:41:40` | `cowrie.client.version` |
| `2026-05-09 13:41:41` | `cowrie.client.kex` |
| `2026-05-09 13:41:41` | `cowrie.login.success` |
| `2026-05-09 13:41:42` | `cowrie.client.size` |
| `2026-05-09 13:41:42` | `cowrie.session.params` |
| `2026-05-09 13:41:44` | `cowrie.command.input` |
| `2026-05-09 13:42:00` | `cowrie.command.input` |
| `2026-05-09 13:42:01` | `cowrie.command.input` |
| `2026-05-09 13:42:01` | `cowrie.command.failed` |
| `2026-05-09 13:42:17` | `cowrie.log.closed` |
| `2026-05-09 13:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca6c2758164

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 14:18 |
| **Last Seen** | 2026-05-09 14:19 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 14:18:52` | `cowrie.session.connect` |
| `2026-05-09 14:18:52` | `cowrie.client.version` |
| `2026-05-09 14:18:52` | `cowrie.client.kex` |
| `2026-05-09 14:18:53` | `cowrie.login.success` |
| `2026-05-09 14:18:54` | `cowrie.client.size` |
| `2026-05-09 14:18:54` | `cowrie.session.params` |
| `2026-05-09 14:18:55` | `cowrie.command.input` |
| `2026-05-09 14:19:11` | `cowrie.command.input` |
| `2026-05-09 14:19:12` | `cowrie.command.input` |
| `2026-05-09 14:19:12` | `cowrie.command.failed` |
| `2026-05-09 14:19:28` | `cowrie.log.closed` |
| `2026-05-09 14:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae6476c13c0

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 14:42 |
| **Last Seen** | 2026-05-09 14:43 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 14:42:35` | `cowrie.session.connect` |
| `2026-05-09 14:42:35` | `cowrie.client.version` |
| `2026-05-09 14:42:35` | `cowrie.client.kex` |
| `2026-05-09 14:42:36` | `cowrie.login.success` |
| `2026-05-09 14:42:37` | `cowrie.client.size` |
| `2026-05-09 14:42:37` | `cowrie.session.params` |
| `2026-05-09 14:42:38` | `cowrie.command.input` |
| `2026-05-09 14:42:54` | `cowrie.command.input` |
| `2026-05-09 14:42:55` | `cowrie.command.input` |
| `2026-05-09 14:42:55` | `cowrie.command.failed` |
| `2026-05-09 14:43:11` | `cowrie.log.closed` |
| `2026-05-09 14:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.183.111[.]36` | **480** | 2026-05-09 13:24 | 2026-05-09 14:54 | 270m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.35[.]128` | **24** | 2026-05-09 14:45 | 2026-05-09 14:50 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **13** | 2026-05-09 13:36 | 2026-05-09 14:53 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `20.64.106[.]155` | **2** | 2026-05-09 14:15 | 2026-05-09 14:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.196.157[.]119` | 1 | 2026-05-09 14:17 | 2026-05-09 14:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `135.232.182[.]226` | 1 | 2026-05-09 14:50 | 2026-05-09 14:50 | 40s | 0 | `T1592` | 🟢 LOW |
| `138.197.147[.]76` | 1 | 2026-05-09 13:32 | 2026-05-09 13:33 | 43s | 0 | `T1592` | 🟢 LOW |
| `153.99.92[.]11` | 1 | 2026-05-09 14:08 | 2026-05-09 14:09 | 51s | 0 | `T1592` | 🟢 LOW |
| `185.71.233[.]73` | 1 | 2026-05-09 14:09 | 2026-05-09 14:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.24.211[.]95` | 1 | 2026-05-09 14:37 | 2026-05-09 14:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.132.49[.]144` | 1 | 2026-05-09 13:55 | 2026-05-09 13:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `68.168.211[.]82` | 1 | 2026-05-09 14:13 | 2026-05-09 14:14 | 38s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]119` | 1 | 2026-05-09 14:13 | 2026-05-09 14:13 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `223.123.35[.]128` | PK | CMPak Limited | **100** ⚠️ | 6 |
| `135.232.182[.]226` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `138.197.147[.]76` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `206.183.111[.]36` | IN | Web Werks | **100** ⚠️ | 1 |
| `121.196.157[.]119` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `185.71.233[.]73` | CZ | United Networks SE | **100** ⚠️ | 3 |
| `68.168.211[.]82` | US | Interserver, Inc | **100** ⚠️ | 1 |
| `20.64.106[.]155` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `153.99.92[.]11` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 96 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 87 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 4 |

---

## 🔕 False Positive Summary (93 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 87 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 625 cases |
| Tool 34  | Credential Extractor        | ✅ 91 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 93 filtered (14.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 13 recon entry/entries in table (4 group(s) consolidating 519 session(s)).

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
_Report time: 2026-05-09T14:55:05Z_
