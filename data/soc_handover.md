# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T17:20:02Z |
| **Shift Time** | 17:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **6** |
| Confirmed Threats | **4** |
| False Positives Filtered | **2** (33.3%) |
| Unique Attacker IPs | **5** |
| Countries of Origin | **5** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3** |
| Unique Credential Pairs | **3** |
| Unique Usernames | **2** |
| Unique Passwords | **2** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 2 |
| `root` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `root` | 1 |
| `root` | `admin` | 1 |
| `admin` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `83.233.242.192` | 2026-04-16T16:00:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **6** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **5** |
| Unique ASNs | **5** |
| High-Risk ASNs | **3** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS25106` | Mobile TeleSystems JLLC | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS48090` | TECHOFF SRV LIMITED | 1 | HIGH |
| `AS29518` | Bredband2 AB | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7b420eb44e0c

| Field | Detail |
|---|---|
| **Source IP** | `83.233.242[.]192` |
| **First Seen** | 2026-04-16 16:00 |
| **Last Seen** | 2026-04-16 16:01 |
| **Session Duration** | 55s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 16:00:40` | `cowrie.session.connect` |
| `2026-04-16 16:00:40` | `cowrie.client.version` |
| `2026-04-16 16:00:40` | `cowrie.client.kex` |
| `2026-04-16 16:00:42` | `cowrie.login.failed` |
| `2026-04-16 16:00:43` | `cowrie.login.success` |
| `2026-04-16 16:00:43` | `cowrie.session.params` |
| `2026-04-16 16:00:43` | `cowrie.command.input` |
| `2026-04-16 16:00:43` | `cowrie.command.failed` |
| `2026-04-16 16:00:43` | `cowrie.log.closed` |
| `2026-04-16 16:00:44` | `cowrie.session.params` |
| `2026-04-16 16:00:44` | `cowrie.command.input` |
| `2026-04-16 16:00:44` | `cowrie.log.closed` |
| `2026-04-16 16:00:44` | `cowrie.session.params` |
| `2026-04-16 16:00:44` | `cowrie.command.input` |
| `2026-04-16 16:00:45` | `cowrie.log.closed` |
| `2026-04-16 16:00:45` | `cowrie.session.params` |
| `2026-04-16 16:00:45` | `cowrie.command.input` |
| `2026-04-16 16:00:45` | `cowrie.log.closed` |
| `2026-04-16 16:00:46` | `cowrie.session.params` |
| `2026-04-16 16:00:46` | `cowrie.command.input` |
| `2026-04-16 16:00:46` | `cowrie.log.closed` |
| `2026-04-16 16:00:46` | `cowrie.session.params` |
| `2026-04-16 16:00:46` | `cowrie.command.input` |
| `2026-04-16 16:00:47` | `cowrie.log.closed` |
| `2026-04-16 16:00:47` | `cowrie.session.params` |
| `2026-04-16 16:00:47` | `cowrie.command.input` |
| `2026-04-16 16:00:47` | `cowrie.log.closed` |
| `2026-04-16 16:00:48` | `cowrie.session.params` |
| `2026-04-16 16:00:48` | `cowrie.command.input` |
| `2026-04-16 16:00:48` | `cowrie.log.closed` |
| `2026-04-16 16:00:48` | `cowrie.session.params` |
| `2026-04-16 16:00:48` | `cowrie.command.input` |
| `2026-04-16 16:00:49` | `cowrie.log.closed` |
| `2026-04-16 16:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.233.242[.]192` to AbuseIPDB if not already reported
- [ ] Block `83.233.242[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.51.122[.]184` | **2** | 2026-04-16 17:08 | 2026-04-16 17:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-04-16 16:08 | 2026-04-16 16:08 | 31s | 1 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.51.122[.]184` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `195.178.110[.]204` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 50 |
| `83.233.242[.]192` | SE | Bredband2 AB | **100** ⚠️ | 4 |
| `46.216.38[.]231` | BY | Mobile TeleSystems JLLC | **25** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 1 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 6 cases |
| Tool 34  | Credential Extractor        | ✅ 3 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 5 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (33.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 5 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 2 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-04-16T17:20:02Z_
