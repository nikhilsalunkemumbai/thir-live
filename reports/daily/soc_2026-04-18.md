# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-18 |
| **Generated At** | 2026-04-18T05:43:09Z |
| **Shift Time** | 05:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **39** |
| Confirmed Threats | **22** |
| False Positives Filtered | **17** (43.6%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **10** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4** |
| Unique Credential Pairs | **4** |
| Unique Usernames | **3** |
| Unique Passwords | **4** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: curl/7.64.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `centos` | 1 |
| `---fuck_you----` | 1 |
| `Host: 13.235.92.17:2323` | 1 |
| `Accept: */*` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `centos` | 1 |
| `root` | `---fuck_you----` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:2323` | 1 |
| `User-Agent: curl/7.64.1` | `Accept: */*` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `centos` | `101.96.230.94` | 2026-04-18T04:00:55 |
| `root` | `---fuck_you----` | `120.26.150.54` | 2026-04-18T04:13:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **39** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Unknown | 3 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Unknown | 3 | 1 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS215439` | PLAY2GO INTERNATIONAL LIMITED | 1 | HIGH |
| `AS18049` | Taiwan Infrastructure Network Technologie | 1 | HIGH |
| `AS17858` | LG POWERCOMM | 1 | HIGH |
| `AS58487` | CV. Rumahweb Indonesia | 1 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0057b0dd7d34

| Field | Detail |
|---|---|
| **Source IP** | `101.96.230[.]94` |
| **First Seen** | 2026-04-18 04:00 |
| **Last Seen** | 2026-04-18 04:05 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 04:00:54` | `cowrie.session.connect` |
| `2026-04-18 04:00:54` | `cowrie.client.version` |
| `2026-04-18 04:00:54` | `cowrie.client.kex` |
| `2026-04-18 04:00:55` | `cowrie.login.success` |
| `2026-04-18 04:05:55` | `cowrie.session.file_upload` |
| `2026-04-18 04:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.230[.]94` to AbuseIPDB if not already reported
- [ ] Block `101.96.230[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-117830aad068

| Field | Detail |
|---|---|
| **Source IP** | `120.26.150[.]54` |
| **First Seen** | 2026-04-18 04:13 |
| **Last Seen** | 2026-04-18 04:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 04:13:46` | `cowrie.session.connect` |
| `2026-04-18 04:13:46` | `cowrie.client.version` |
| `2026-04-18 04:13:46` | `cowrie.client.kex` |
| `2026-04-18 04:13:47` | `cowrie.login.success` |
| `2026-04-18 04:13:47` | `cowrie.session.params` |
| `2026-04-18 04:13:47` | `cowrie.command.input` |
| `2026-04-18 04:13:47` | `cowrie.log.closed` |
| `2026-04-18 04:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.150[.]54` to AbuseIPDB if not already reported
- [ ] Block `120.26.150[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.131.220[.]121` | **5** | 2026-04-18 03:29 | 2026-04-18 03:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `78.187.30[.]37` | **4** | 2026-04-18 05:34 | 2026-04-18 05:38 | 8m | 0 | `T1592` | 🟢 LOW |
| `8.216.7[.]102` | **3** | 2026-04-18 04:43 | 2026-04-18 04:43 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `101.96.230[.]94` | **2** | 2026-04-18 03:56 | 2026-04-18 04:00 | 4m | 0 | `T1592` | 🟢 LOW |
| `135.237.126[.]202` | **2** | 2026-04-18 05:25 | 2026-04-18 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `182.211.221[.]139` | 1 | 2026-04-18 03:14 | 2026-04-18 03:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `2.26.54[.]59` | 1 | 2026-04-18 03:36 | 2026-04-18 03:36 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.127.164[.]236` | 1 | 2026-04-18 04:19 | 2026-04-18 04:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.213.219[.]10` | 1 | 2026-04-18 03:27 | 2026-04-18 03:28 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `49.213.219[.]10` | TW | Asia Pacific Network Information Centre | **100** ⚠️ | 10 |
| `135.237.126[.]202` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `182.211.221[.]139` | KR | LG POWERCOMM | **100** ⚠️ | 19 |
| `101.96.230[.]94` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `8.216.7[.]102` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 21 |
| `2.26.54[.]59` | DE | play2go.cloud - Cheap and reliable hosting | **100** ⚠️ | 6 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `221.127.164[.]236` | HK | HGC Global Communications Limited | **100** ⚠️ | 50 |
| `78.187.30[.]37` | TR | Turk Telekomunikasyon Anonim Sirketi | **95** ⚠️ | 1 |
| `139.135.59[.]140` | PK | Cyber Internet Services Pakistan | **79** | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 7 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 13 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 39 cases |
| Tool 34  | Credential Extractor        | ✅ 4 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (43.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 9 recon entry/entries in table (5 group(s) consolidating 16 session(s)).

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
_Report time: 2026-04-18T05:43:09Z_
