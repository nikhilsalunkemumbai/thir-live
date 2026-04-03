# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T16:37:13Z |
| **Shift Time** | 16:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **55** |
| Confirmed Threats | **31** |
| False Positives Filtered | **24** (43.6%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **16** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **52** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **12** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `Unknown` | 2 |
| `Support` | 2 |
| `oracle` | 2 |
| `mysql` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123123123` | 2 |
| `123321` | 2 |
| `777777` | 2 |
| `123456` | 1 |
| `uploader` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `777777` | 2 |
| `mysql` | `123123123` | 1 |
| `Centos` | `123456` | 1 |
| `Supervisor` | `uploader` | 1 |
| `Unknown` | `123123123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `777777` | `111.70.34.60` | 2026-04-03T15:54:09 |
| `root` | `777777` | `59.93.36.136` | 2026-04-03T15:54:21 |
| `root` | `admin` | `179.43.186.241` | 2026-04-03T16:12:26 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **55** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 17 |
| Go SSH scanner | 4 |
| Unknown | 1 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 16 | 16 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 16 | 16 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **26** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS8473` | Bahnhof AB | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-644086699c90

| Field | Detail |
|---|---|
| **Source IP** | `111.70.34[.]60` |
| **First Seen** | 2026-04-03 15:54 |
| **Last Seen** | 2026-04-03 15:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 15:54:07` | `cowrie.session.connect` |
| `2026-04-03 15:54:07` | `cowrie.client.version` |
| `2026-04-03 15:54:07` | `cowrie.client.kex` |
| `2026-04-03 15:54:09` | `cowrie.login.success` |
| `2026-04-03 15:54:10` | `cowrie.direct-tcpip.request` |
| `2026-04-03 15:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.34[.]60` to AbuseIPDB if not already reported
- [ ] Block `111.70.34[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49051d71c252

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-04-03 15:54 |
| **Last Seen** | 2026-04-03 15:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 15:54:19` | `cowrie.session.connect` |
| `2026-04-03 15:54:20` | `cowrie.client.version` |
| `2026-04-03 15:54:20` | `cowrie.client.kex` |
| `2026-04-03 15:54:21` | `cowrie.login.success` |
| `2026-04-03 15:54:22` | `cowrie.direct-tcpip.request` |
| `2026-04-03 15:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf3ab3a827a

| Field | Detail |
|---|---|
| **Source IP** | `179.43.186[.]241` |
| **First Seen** | 2026-04-03 16:12 |
| **Last Seen** | 2026-04-03 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 16:12:25` | `cowrie.session.connect` |
| `2026-04-03 16:12:25` | `cowrie.client.version` |
| `2026-04-03 16:12:25` | `cowrie.client.kex` |
| `2026-04-03 16:12:26` | `cowrie.login.success` |
| `2026-04-03 16:12:26` | `cowrie.session.params` |
| `2026-04-03 16:12:26` | `cowrie.command.input` |
| `2026-04-03 16:12:26` | `cowrie.log.closed` |
| `2026-04-03 16:12:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.43.186[.]241` to AbuseIPDB if not already reported
- [ ] Block `179.43.186[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.230[.]55` | **3** | 2026-04-03 15:07 | 2026-04-03 15:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `1.212.225[.]99` | 1 | 2026-04-03 15:14 | 2026-04-03 15:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-04-03 15:53 | 2026-04-03 15:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.142.244[.]108` | 1 | 2026-04-03 15:18 | 2026-04-03 15:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-03 15:27 | 2026-04-03 15:28 | 31s | 0 | `T1592` | 🟢 LOW |
| `151.48.206[.]71` | 1 | 2026-04-03 16:10 | 2026-04-03 16:11 | 14s | 0 | `T1592` | 🟢 LOW |
| `179.185.29[.]233` | 1 | 2026-04-03 14:54 | 2026-04-03 14:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.94.74[.]94` | 1 | 2026-04-03 15:34 | 2026-04-03 15:34 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.222.55[.]187` | 1 | 2026-04-03 15:15 | 2026-04-03 15:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.134.90[.]55` | 1 | 2026-04-03 16:24 | 2026-04-03 16:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-04-03 15:33 | 2026-04-03 15:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.195.94[.]243` | 1 | 2026-04-03 15:34 | 2026-04-03 15:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.146.163[.]192` | 1 | 2026-04-03 15:02 | 2026-04-03 15:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `46.59.89[.]67` | 1 | 2026-04-03 16:13 | 2026-04-03 16:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.91[.]141` | 1 | 2026-04-03 16:13 | 2026-04-03 16:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.93[.]200` | 1 | 2026-04-03 16:04 | 2026-04-03 16:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.236.202[.]5` | 1 | 2026-04-03 15:09 | 2026-04-03 15:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `47.237.102[.]37` | 1 | 2026-04-03 15:00 | 2026-04-03 15:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `60.251.229[.]144` | 1 | 2026-04-03 15:25 | 2026-04-03 15:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.185.30[.]170` | 1 | 2026-04-03 16:33 | 2026-04-03 16:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.157[.]131` | 1 | 2026-04-03 14:46 | 2026-04-03 14:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.250[.]254` | 1 | 2026-04-03 16:32 | 2026-04-03 16:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-04-03 16:20 | 2026-04-03 16:21 | 10s | 0 | `T1592` | 🟢 LOW |
| `71.229.1[.]186` | 1 | 2026-04-03 15:45 | 2026-04-03 15:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.89.156[.]178` | 1 | 2026-04-03 16:30 | 2026-04-03 16:30 | 1s | 0 | `T1592` | 🟢 LOW |
| `8.219.197[.]92` | 1 | 2026-04-03 14:50 | 2026-04-03 14:50 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `46.59.91[.]141` | SE | Bahnhof AB | **100** ⚠️ | 6 |
| `151.48.206[.]71` | IT | WIND Telecomunicazioni S.p.A | **100** ⚠️ | 1 |
| `180.94.74[.]94` | AF | GCN/DCN Networks | **100** ⚠️ | 32 |
| `46.59.89[.]67` | SE | Bahnhof AB | **100** ⚠️ | 4 |
| `121.142.244[.]108` | KR | Sudogwonseobubonbu | **100** ⚠️ | 23 |
| `217.195.94[.]243` | RU | Natsionalniy informatsionniy kanal | **100** ⚠️ | 48 |
| `65.20.250[.]254` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 9 |
| `47.236.202[.]5` | SG | Alibaba Cloud LLC | **100** ⚠️ | 25 |
| `117.223.152[.]94` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 20 |
| `75.89.156[.]178` | US | WINDSTREAM COMMUNICATIONS LLC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 22 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 55 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (43.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 26 recon entry/entries in table (1 group(s) consolidating 3 session(s)).

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
_Report time: 2026-04-03T16:37:13Z_
