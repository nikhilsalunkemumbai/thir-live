# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T22:35:21Z |
| **Shift Time** | 22:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **53** |
| Confirmed Threats | **35** |
| False Positives Filtered | **18** (34.0%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **10** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **23** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **17** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `user` | 3 |
| `Ubnt` | 2 |
| `Debian` | 2 |
| `centos` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `alpine` | 2 |
| `123321` | 2 |
| `qwerty@123` | 1 |
| `33` | 1 |
| `passwd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `qwerty@123` | 1 |
| `centos` | `33` | 1 |
| `Ubnt` | `alpine` | 1 |
| `Blank` | `passwd` | 1 |
| `debian` | `6` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty@123` | `20.42.11.19` | 2026-04-01T20:47:46 |
| `root` | `Welcome@123` | `20.42.11.19` | 2026-04-01T21:02:10 |
| `root` | `P` | `180.76.172.156` | 2026-04-01T21:55:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **53** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 26 |
| OpenSSH | 18 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 18 | 17 |
| `03a80b21afa8...` | Modern SSH client | 16 | 2 |
| `19532158b559...` | Mirai/variant | 3 | 1 |
| `16443846184e...` | Generic scanner | 2 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 18 | 17 | Mirai/variant |
| `03a80b21afa8...` | libssh | 16 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 6 | 2 | — |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **22** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS45916` | Gujarat Telelink Pvt Ltd | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bdb765d489fb

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 20:47 |
| **Last Seen** | 2026-04-01 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 20:47:45` | `cowrie.session.connect` |
| `2026-04-01 20:47:45` | `cowrie.client.version` |
| `2026-04-01 20:47:45` | `cowrie.client.kex` |
| `2026-04-01 20:47:46` | `cowrie.login.success` |
| `2026-04-01 20:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f783d61925

| Field | Detail |
|---|---|
| **Source IP** | `20.42.11[.]19` |
| **First Seen** | 2026-04-01 21:02 |
| **Last Seen** | 2026-04-01 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 21:02:09` | `cowrie.session.connect` |
| `2026-04-01 21:02:09` | `cowrie.client.version` |
| `2026-04-01 21:02:09` | `cowrie.client.kex` |
| `2026-04-01 21:02:10` | `cowrie.login.success` |
| `2026-04-01 21:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.42.11[.]19` to AbuseIPDB if not already reported
- [ ] Block `20.42.11[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d28da3827fa

| Field | Detail |
|---|---|
| **Source IP** | `180.76.172[.]156` |
| **First Seen** | 2026-04-01 21:54 |
| **Last Seen** | 2026-04-01 21:55 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 21:54:27` | `cowrie.session.connect` |
| `2026-04-01 21:54:27` | `cowrie.client.version` |
| `2026-04-01 21:55:06` | `cowrie.client.kex` |
| `2026-04-01 21:55:11` | `cowrie.login.success` |
| `2026-04-01 21:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.172[.]156` to AbuseIPDB if not already reported
- [ ] Block `180.76.172[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `36.112.134[.]179` | **6** | 2026-04-01 20:43 | 2026-04-01 20:47 | 10m | 0 | `T1592` | 🟢 LOW |
| `115.244.235[.]242` | **2** | 2026-04-01 20:59 | 2026-04-01 21:19 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.172[.]156` | **2** | 2026-04-01 21:39 | 2026-04-01 21:47 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `8.210.142[.]27` | **2** | 2026-04-01 21:18 | 2026-04-01 21:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.88[.]251` | 1 | 2026-04-01 20:57 | 2026-04-01 20:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.250.160[.]76` | 1 | 2026-04-01 21:16 | 2026-04-01 21:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.23[.]235` | 1 | 2026-04-01 22:17 | 2026-04-01 22:17 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.211.77[.]86` | 1 | 2026-04-01 21:38 | 2026-04-01 21:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.56.184[.]174` | 1 | 2026-04-01 20:41 | 2026-04-01 20:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `123.129.245[.]249` | 1 | 2026-04-01 20:52 | 2026-04-01 20:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.139.124[.]120` | 1 | 2026-04-01 20:56 | 2026-04-01 20:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.189.81[.]2` | 1 | 2026-04-01 21:07 | 2026-04-01 21:07 | 12s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-04-01 22:28 | 2026-04-01 22:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.198.129[.]123` | 1 | 2026-04-01 21:55 | 2026-04-01 21:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `207.219.222[.]29` | 1 | 2026-04-01 22:06 | 2026-04-01 22:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.47.103[.]61` | 1 | 2026-04-01 21:58 | 2026-04-01 21:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.248.9[.]102` | 1 | 2026-04-01 21:11 | 2026-04-01 21:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.194[.]124` | 1 | 2026-04-01 20:51 | 2026-04-01 20:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.250.107[.]132` | 1 | 2026-04-01 21:35 | 2026-04-01 21:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.215.0[.]179` | 1 | 2026-04-01 21:11 | 2026-04-01 21:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.166.31[.]198` | 1 | 2026-04-01 21:29 | 2026-04-01 21:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.172.41[.]103` | 1 | 2026-04-01 22:14 | 2026-04-01 22:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-04-01 21:47 | 2026-04-01 21:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.229.46[.]153` | 1 | 2026-04-01 21:30 | 2026-04-01 21:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `119.56.184[.]174` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 1 |
| `218.248.9[.]102` | IN | National Internet Backbone | **100** ⚠️ | 7 |
| `103.250.160[.]76` | IN | Gtpl Broadband Pvt. Ltd. | **100** ⚠️ | 41 |
| `85.229.46[.]153` | SE | Telenor Sverige AB | **100** ⚠️ | 23 |
| `220.246.194[.]124` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 4 |
| `196.204.71[.]189` | EG | Local ISP | **100** ⚠️ | 26 |
| `111.70.23[.]235` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 23 |
| `78.66.44[.]246` | SE | Telia Network Services | **100** ⚠️ | 23 |
| `20.42.11[.]19` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `212.47.103[.]61` | LT | Telia Lietuva, AB | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 20 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 53 cases |
| Tool 34  | Credential Extractor        | ✅ 23 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (34.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 24 recon entry/entries in table (4 group(s) consolidating 12 session(s)).

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
_Report time: 2026-04-01T22:35:21Z_
