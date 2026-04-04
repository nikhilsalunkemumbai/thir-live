# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T06:58:13Z |
| **Shift Time** | 06:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **38** |
| Confirmed Threats | **29** |
| False Positives Filtered | **9** (23.7%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **15** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **14** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `config` | 4 |
| `mysql` | 2 |
| `Blank` | 1 |
| `admin` | 1 |
| `guest` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `marketing` | 2 |
| `5` | 1 |
| `passw0rd` | 1 |
| `8` | 1 |
| `config999` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `mysql` | `marketing` | 2 |
| `config` | `5` | 1 |
| `Blank` | `passw0rd` | 1 |
| `admin` | `8` | 1 |
| `config` | `config999` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `189.127.109.198` | 2026-04-04T05:54:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **38** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 18 |
| Go SSH scanner | 1 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 17 | 17 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 17 | 17 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **25** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS3301` | Telia Company AB | 1 | HIGH |
| `AS59591` | WIRENET LLC | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | HIGH |
| `AS11139` | Cable & Wireless Dominica | 1 | HIGH |
| `AS8359` | MTS PJSC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-31c08b4d9928

| Field | Detail |
|---|---|
| **Source IP** | `189.127.109[.]198` |
| **First Seen** | 2026-04-04 05:54 |
| **Last Seen** | 2026-04-04 05:56 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 05:54:57` | `cowrie.session.connect` |
| `2026-04-04 05:54:57` | `cowrie.client.version` |
| `2026-04-04 05:54:57` | `cowrie.client.kex` |
| `2026-04-04 05:54:58` | `cowrie.login.success` |
| `2026-04-04 05:56:42` | `cowrie.session.file_upload` |
| `2026-04-04 05:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.127.109[.]198` to AbuseIPDB if not already reported
- [ ] Block `189.127.109[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `122.116.6[.]195` | **7** | 2026-04-04 05:34 | 2026-04-04 05:42 | 6m | 0 | `T1592` | 🟢 LOW |
| `111.70.41[.]194` | 1 | 2026-04-04 06:56 | 2026-04-04 06:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.30.177[.]100` | 1 | 2026-04-04 05:08 | 2026-04-04 05:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-04-04 06:39 | 2026-04-04 06:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.175.18[.]126` | 1 | 2026-04-04 05:58 | 2026-04-04 05:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.239.169[.]52` | 1 | 2026-04-04 06:41 | 2026-04-04 06:41 | 2s | 0 | `T1592` | 🟢 LOW |
| `125.19.244[.]62` | 1 | 2026-04-04 05:21 | 2026-04-04 05:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.194.128[.]158` | 1 | 2026-04-04 06:00 | 2026-04-04 06:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.118.13[.]206` | 1 | 2026-04-04 05:39 | 2026-04-04 05:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.145[.]55` | 1 | 2026-04-04 05:11 | 2026-04-04 05:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.168.86[.]6` | 1 | 2026-04-04 06:39 | 2026-04-04 06:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.57.233[.]133` | 1 | 2026-04-04 04:43 | 2026-04-04 04:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.208.191[.]179` | 1 | 2026-04-04 06:05 | 2026-04-04 06:06 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.252.10[.]4` | 1 | 2026-04-04 05:27 | 2026-04-04 05:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.140.127[.]160` | 1 | 2026-04-04 06:22 | 2026-04-04 06:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-04-04 04:30 | 2026-04-04 04:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.174.39[.]82` | 1 | 2026-04-04 05:41 | 2026-04-04 05:41 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.153[.]146` | 1 | 2026-04-04 06:44 | 2026-04-04 06:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.57.238[.]229` | 1 | 2026-04-04 04:22 | 2026-04-04 04:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.225.109[.]18` | 1 | 2026-04-04 06:25 | 2026-04-04 06:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.244.113[.]178` | 1 | 2026-04-04 04:49 | 2026-04-04 04:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.131.211[.]168` | 1 | 2026-04-04 05:46 | 2026-04-04 05:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
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
| `122.175.18[.]126` | IN | ABTS (Hyderabad), | **100** ⚠️ | 44 |
| `189.127.109[.]198` | BR | SAMM TECNOLOGIA E TELECOMUNICACOES S.A | **100** ⚠️ | 3 |
| `188.168.86[.]6` | RU | TTK-Chita/BRAS in Chita | **100** ⚠️ | 50 |
| `94.131.211[.]168` | UA | Kruiz LLC | **100** ⚠️ | 50 |
| `183.171.145[.]55` | MY | Celcom Axiata Berhad | **100** ⚠️ | 6 |
| `115.86.227[.]79` | KR | HVYeongseo | **100** ⚠️ | 24 |
| `190.57.233[.]133` | AR | Gigared S.A. | **100** ⚠️ | 29 |
| `111.70.41[.]194` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 20 |
| `60.174.39[.]82` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `91.244.113[.]178` | RU | WIRENET LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 5 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 38 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (23.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 22 recon entry/entries in table (1 group(s) consolidating 7 session(s)).

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
_Report time: 2026-04-04T06:58:13Z_
