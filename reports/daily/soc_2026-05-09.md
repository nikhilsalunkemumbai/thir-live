# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T13:24:36Z |
| **Shift Time** | 13:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **527** |
| Confirmed Threats | **517** |
| False Positives Filtered | **10** (1.9%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **12** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **525** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **2** |
| Unique Credential Pairs | **1** |
| Unique Usernames | **1** |
| Unique Passwords | **1** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `toor` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `toor` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor` | `185.71.233.73` | 2026-05-09T11:09:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **527** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `748f8c627d3f...` | Mirai/variant | 2 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `748f8c627d3f...` | Unknown | 2 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **18** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8781` | Ooredoo Q.S.C. | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS19318` | Interserver, Inc | 1 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS211101` | Nasteka Maksim Viktorovich | 1 | LOW |
| `AS8193` | "Uzbektelekom" Joint Stock Company | 1 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS201767` | Uzbektelekom Joint Stock Company | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fcf17b0d29f3

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 11:09 |
| **Last Seen** | 2026-05-09 11:09 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `?, apt-get update -y, sudo apt-get update -y, root` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 11:09:01` | `cowrie.session.connect` |
| `2026-05-09 11:09:01` | `cowrie.client.version` |
| `2026-05-09 11:09:01` | `cowrie.client.kex` |
| `2026-05-09 11:09:02` | `cowrie.login.success` |
| `2026-05-09 11:09:03` | `cowrie.client.size` |
| `2026-05-09 11:09:03` | `cowrie.session.params` |
| `2026-05-09 11:09:05` | `cowrie.command.input` |
| `2026-05-09 11:09:05` | `cowrie.command.failed` |
| `2026-05-09 11:09:05` | `cowrie.command.input` |
| `2026-05-09 11:09:05` | `cowrie.command.input` |
| `2026-05-09 11:09:06` | `cowrie.command.input` |
| `2026-05-09 11:09:22` | `cowrie.command.input` |
| `2026-05-09 11:09:23` | `cowrie.command.input` |
| `2026-05-09 11:09:23` | `cowrie.command.failed` |
| `2026-05-09 11:09:39` | `cowrie.log.closed` |
| `2026-05-09 11:09:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8fad1e7aeb

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 12:28 |
| **Last Seen** | 2026-05-09 12:29 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `?, apt-get update -y, sudo apt-get update -y, root` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 12:28:33` | `cowrie.session.connect` |
| `2026-05-09 12:28:33` | `cowrie.client.version` |
| `2026-05-09 12:28:34` | `cowrie.client.kex` |
| `2026-05-09 12:28:35` | `cowrie.login.success` |
| `2026-05-09 12:28:35` | `cowrie.client.size` |
| `2026-05-09 12:28:36` | `cowrie.session.params` |
| `2026-05-09 12:28:37` | `cowrie.command.input` |
| `2026-05-09 12:28:37` | `cowrie.command.failed` |
| `2026-05-09 12:28:37` | `cowrie.command.input` |
| `2026-05-09 12:28:37` | `cowrie.command.input` |
| `2026-05-09 12:28:38` | `cowrie.command.input` |
| `2026-05-09 12:28:54` | `cowrie.command.input` |
| `2026-05-09 12:28:55` | `cowrie.command.input` |
| `2026-05-09 12:28:55` | `cowrie.command.failed` |
| `2026-05-09 12:29:11` | `cowrie.log.closed` |
| `2026-05-09 12:29:11` | `cowrie.session.closed` |

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
| `206.183.111[.]36` | **447** | 2026-05-09 11:02 | 2026-05-09 13:24 | 247m | 0 | `T1592` | 🟠 MEDIUM |
| `72.255.19[.]22` | **25** | 2026-05-09 11:45 | 2026-05-09 11:50 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `68.168.211[.]82` | **22** | 2026-05-09 11:01 | 2026-05-09 13:08 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **15** | 2026-05-09 11:24 | 2026-05-09 13:24 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `157.245.147[.]189` | **2** | 2026-05-09 11:16 | 2026-05-09 11:18 | 4m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-05-09 12:23 | 2026-05-09 12:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `122.222.1[.]177` | 1 | 2026-05-09 13:09 | 2026-05-09 13:09 | 13s | 0 | `T1592` | 🟢 LOW |
| `52.207.238[.]74` | 1 | 2026-05-09 12:57 | 2026-05-09 12:57 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `52.207.238[.]74` | US | Amazon Technologies Inc. | **100** ⚠️ | 34 |
| `68.168.211[.]82` | US | Interserver, Inc | **100** ⚠️ | 1 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `185.71.233[.]73` | CZ | United Networks SE | **100** ⚠️ | 3 |
| `206.183.111[.]36` | IN | Web Werks | **100** ⚠️ | 1 |
| `157.245.147[.]189` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `122.222.1[.]177` | JP | GMO Internet,Inc. | **88** ⚠️ | 0 |
| `72.255.19[.]22` | PK | Cyber Internet Services Pakistan | **84** ⚠️ | 1 |
| `84.54.73[.]72` | UZ | Uzbektelekom Joint Stock Company | **51** | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 3 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 527 cases |
| Tool 34  | Credential Extractor        | ✅ 2 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (1.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 8 recon entry/entries in table (6 group(s) consolidating 513 session(s)).

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
_Report time: 2026-05-09T13:24:36Z_
