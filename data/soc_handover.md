# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-18 |
| **Generated At** | 2026-04-18T20:41:29Z |
| **Shift Time** | 20:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **31** |
| Confirmed Threats | **18** |
| False Positives Filtered | **13** (41.9%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **8** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **28** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **7** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **4** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.86 Safari/537.36` | 1 |
| `Accept-Encoding: gzip` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 2 |
| `---fuck_you----` | 1 |
| `ubuntu` | 1 |
| `admin` | 1 |
| `Host: 13.235.92.17:2323` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `---fuck_you----` | 1 |
| `root` | `ubuntu` | 1 |
| `root` | `` | 1 |
| `root` | `admin` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:2323` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `---fuck_you----` | `113.249.159.58` | 2026-04-18T18:58:44 |
| `root` | `ubuntu` | `109.122.217.21` | 2026-04-18T19:44:02 |
| `root` | `admin` | `185.220.101.139` | 2026-04-18T20:05:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **31** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 2 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **10** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 4 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4760` | HKT Limited | 1 | MEDIUM |
| `AS62214` | Rackforest Zrt. | 1 | HIGH |
| `AS134420` | Chongqing Telecom | 1 | MEDIUM |
| `AS14618` | Amazon.com, Inc. | 1 | MEDIUM |
| `AS60729` | Stiftung Erneuerbare Freiheit | 1 | HIGH |
| `AS131275` | Logon Broadband Pvt. Limited | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d54cea900993

| Field | Detail |
|---|---|
| **Source IP** | `113.249.159[.]58` |
| **First Seen** | 2026-04-18 18:58 |
| **Last Seen** | 2026-04-18 18:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 18:58:42` | `cowrie.session.connect` |
| `2026-04-18 18:58:42` | `cowrie.client.version` |
| `2026-04-18 18:58:42` | `cowrie.client.kex` |
| `2026-04-18 18:58:44` | `cowrie.login.success` |
| `2026-04-18 18:58:44` | `cowrie.session.params` |
| `2026-04-18 18:58:44` | `cowrie.command.input` |
| `2026-04-18 18:58:45` | `cowrie.log.closed` |
| `2026-04-18 18:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.249.159[.]58` to AbuseIPDB if not already reported
- [ ] Block `113.249.159[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b098c75261

| Field | Detail |
|---|---|
| **Source IP** | `109.122.217[.]21` |
| **First Seen** | 2026-04-18 19:44 |
| **Last Seen** | 2026-04-18 19:44 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 19:44:01` | `cowrie.session.connect` |
| `2026-04-18 19:44:01` | `cowrie.client.version` |
| `2026-04-18 19:44:01` | `cowrie.client.kex` |
| `2026-04-18 19:44:02` | `cowrie.login.success` |
| `2026-04-18 19:44:46` | `cowrie.session.file_upload` |
| `2026-04-18 19:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.122.217[.]21` to AbuseIPDB if not already reported
- [ ] Block `109.122.217[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9c11ad515c

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]139` |
| **First Seen** | 2026-04-18 20:05 |
| **Last Seen** | 2026-04-18 20:05 |
| **Session Duration** | 24s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 20:05:08` | `cowrie.session.connect` |
| `2026-04-18 20:05:08` | `cowrie.client.version` |
| `2026-04-18 20:05:08` | `cowrie.client.kex` |
| `2026-04-18 20:05:09` | `cowrie.client.fingerprint` |
| `2026-04-18 20:05:09` | `cowrie.login.failed` |
| `2026-04-18 20:05:10` | `cowrie.login.success` |
| `2026-04-18 20:05:32` | `cowrie.direct-tcpip.request` |
| `2026-04-18 20:05:32` | `cowrie.direct-tcpip.ja4` |
| `2026-04-18 20:05:32` | `cowrie.direct-tcpip.data` |
| `2026-04-18 20:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]139` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.156.128[.]91` | **5** | 2026-04-18 20:21 | 2026-04-18 20:21 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `45.156.128[.]94` | **3** | 2026-04-18 20:21 | 2026-04-18 20:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]93` | **2** | 2026-04-18 20:21 | 2026-04-18 20:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.147.143[.]81` | 1 | 2026-04-18 19:08 | 2026-04-18 19:08 | 31s | 0 | `T1592` | 🟢 LOW |
| `20.55.222[.]81` | 1 | 2026-04-18 20:41 | 2026-04-18 20:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.78.212[.]97` | 1 | 2026-04-18 20:21 | 2026-04-18 20:21 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]92` | 1 | 2026-04-18 20:21 | 2026-04-18 20:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `59.7.135[.]117` | 1 | 2026-04-18 20:32 | 2026-04-18 20:32 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `45.156.128[.]92` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `59.7.135[.]117` | KR | Sudogwonseobubonbu | **100** ⚠️ | 30 |
| `109.122.217[.]21` | HU | RackForest | **100** ⚠️ | 8 |
| `121.147.143[.]81` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `45.156.128[.]91` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `45.156.128[.]93` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `45.156.128[.]94` | NL | INAP-AMS-1 | **100** ⚠️ | 50 |
| `185.220.101[.]139` | DE | CIA TRIAD SECURITY LLC | **100** ⚠️ | 0 |
| `20.55.222[.]81` | US | Microsoft Corporation | **97** ⚠️ | 0 |
| `219.78.212[.]97` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **85** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 31 cases |
| Tool 34  | Credential Extractor        | ✅ 7 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (41.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 8 recon entry/entries in table (3 group(s) consolidating 10 session(s)).

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
_Report time: 2026-04-18T20:41:29Z_
