# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-03 |
| **Generated At** | 2026-04-03T10:41:06Z |
| **Shift Time** | 10:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **25** |
| Confirmed Threats | **23** |
| False Positives Filtered | **2** (8.0%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **17** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **24** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **12** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `config` | 2 |
| `user` | 2 |
| `ubnt` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `77777` | 2 |
| `passw0rd` | 2 |
| `kjashd123sadhj123d1SS` | 1 |
| `777` | 1 |
| `user222` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `kjashd123sadhj123d1SS` | 1 |
| `config` | `77777` | 1 |
| `user` | `777` | 1 |
| `user` | `user222` | 1 |
| `centos` | `centos2020` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `kjashd123sadhj123d1SS` | `77.72.198.224` | 2026-04-03T08:56:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **25** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 15 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `c118de82e19e...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `c118de82e19e...` | OpenSSH | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **22** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS56260` | PT Pascal Indonesia | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS17853` | LGTELECOM | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS26599` | TELEFÔNICA BRASIL S.A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5b46122a4190

| Field | Detail |
|---|---|
| **Source IP** | `77.72.198[.]224` |
| **First Seen** | 2026-04-03 08:56 |
| **Last Seen** | 2026-04-03 08:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-03 08:56:46` | `cowrie.session.connect` |
| `2026-04-03 08:56:46` | `cowrie.client.version` |
| `2026-04-03 08:56:46` | `cowrie.client.kex` |
| `2026-04-03 08:56:48` | `cowrie.login.success` |
| `2026-04-03 08:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.72.198[.]224` to AbuseIPDB if not already reported
- [ ] Block `77.72.198[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.220.237[.]230` | **2** | 2026-04-03 10:12 | 2026-04-03 10:14 | 2m | 0 | `T1592` | 🟢 LOW |
| `40.76.99[.]43` | **2** | 2026-04-03 09:07 | 2026-04-03 09:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.29.185[.]162` | 1 | 2026-04-03 09:23 | 2026-04-03 09:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-04-03 09:05 | 2026-04-03 09:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.170.98[.]139` | 1 | 2026-04-03 10:40 | 2026-04-03 10:40 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-03 10:00 | 2026-04-03 10:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `152.70.134[.]120` | 1 | 2026-04-03 09:55 | 2026-04-03 09:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.94.236[.]211` | 1 | 2026-04-03 10:01 | 2026-04-03 10:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.174.95[.]245` | 1 | 2026-04-03 10:21 | 2026-04-03 10:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.43.186[.]241` | 1 | 2026-04-03 10:23 | 2026-04-03 10:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-04-03 10:15 | 2026-04-03 10:15 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.37.223[.]58` | 1 | 2026-04-03 08:58 | 2026-04-03 08:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.156[.]254` | 1 | 2026-04-03 09:25 | 2026-04-03 09:25 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.171.89[.]199` | 1 | 2026-04-03 09:17 | 2026-04-03 09:17 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]235` | 1 | 2026-04-03 09:42 | 2026-04-03 09:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.211[.]96` | 1 | 2026-04-03 10:23 | 2026-04-03 10:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.100.204[.]121` | 1 | 2026-04-03 09:53 | 2026-04-03 09:54 | 32s | 0 | `T1592` | 🟢 LOW |
| `81.236.211[.]54` | 1 | 2026-04-03 10:34 | 2026-04-03 10:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.144.158[.]62` | 1 | 2026-04-03 09:03 | 2026-04-03 09:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.135.208[.]210` | 1 | 2026-04-03 10:27 | 2026-04-03 10:28 | 60s | 1 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `183.93.165[.]103` | CN | China Unicom Hubei Province Network | **100** ⚠️ | 10 |
| `49.124.152[.]235` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `183.220.237[.]230` | CN | China Mobile Communications Corporation | **100** ⚠️ | 38 |
| `122.170.98[.]139` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `152.70.134[.]120` | US | Oracle Corporation | **100** ⚠️ | 14 |
| `174.94.236[.]211` | CA | Bell Mobility, Inc. | **100** ⚠️ | 15 |
| `177.174.95[.]245` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `77.72.198[.]224` | IT | Trentino Digitale SPA | **100** ⚠️ | 0 |
| `218.4.156[.]254` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `91.144.158[.]62` | RU | CJSC ER-Telecom Holding Naberezhnye Chelny branch | **100** ⚠️ | 37 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 17 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 25 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (8.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 20 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-04-03T10:41:06Z_
