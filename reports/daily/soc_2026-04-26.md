# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-26 |
| **Generated At** | 2026-04-26T16:50:42Z |
| **Shift Time** | 16:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **109** |
| Confirmed Threats | **11** |
| False Positives Filtered | **98** (89.9%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **11** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **108** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **5** |
| Unique Credential Pairs | **4** |
| Unique Usernames | **3** |
| Unique Passwords | **4** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `pi` | 2 |
| `admin` | 2 |
| `root` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 2 |
| `raspberryraspberry993311` | 1 |
| `raspberry` | 1 |
| `------fuck------` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `` | 2 |
| `pi` | `raspberryraspberry993311` | 1 |
| `pi` | `raspberry` | 1 |
| `root` | `------fuck------` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `------fuck------` | `180.76.171.14` | 2026-04-26T16:37:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **109** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Unknown | 2 |
| OpenSSH | 2 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `ec7378c1a92f...` | Generic scanner | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `ec7378c1a92f...` | OpenSSH | 2 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **13** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS51396` | Pfcloud UG | 4 | HIGH |
| `AS25019` | Saudi Telecom Company JSC | 1 | LOW |
| `AS20011` | Dimension Data | 1 | LOW |
| `AS5384` | Emirates Internet | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS24086` | Viettel Corporation | 1 | HIGH |
| `AS6057` | Administracion Nacional de Telecomunicaciones | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b01134c20274

| Field | Detail |
|---|---|
| **Source IP** | `180.76.171[.]14` |
| **First Seen** | 2026-04-26 16:37 |
| **Last Seen** | 2026-04-26 16:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 16:37:25` | `cowrie.session.connect` |
| `2026-04-26 16:37:25` | `cowrie.client.version` |
| `2026-04-26 16:37:26` | `cowrie.client.kex` |
| `2026-04-26 16:37:27` | `cowrie.login.success` |
| `2026-04-26 16:37:28` | `cowrie.session.params` |
| `2026-04-26 16:37:28` | `cowrie.command.input` |
| `2026-04-26 16:37:30` | `cowrie.log.closed` |
| `2026-04-26 16:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.171[.]14` to AbuseIPDB if not already reported
- [ ] Block `180.76.171[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `116.105.173[.]160` | **2** | 2026-04-26 15:54 | 2026-04-26 15:55 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `204.76.203[.]224` | **2** | 2026-04-26 15:44 | 2026-04-26 15:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-26 16:11 | 2026-04-26 16:11 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.149[.]209` | 1 | 2026-04-26 16:23 | 2026-04-26 16:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.76.171[.]14` | 1 | 2026-04-26 16:37 | 2026-04-26 16:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]225` | 1 | 2026-04-26 15:44 | 2026-04-26 15:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]226` | 1 | 2026-04-26 15:44 | 2026-04-26 15:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.97.227[.]74` | 1 | 2026-04-26 14:50 | 2026-04-26 14:50 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `92.97.227[.]74` | AE | Emirates Telecommunications Corporation | **100** ⚠️ | 10 |
| `176.65.149[.]209` | NL | Pfcloud UG | **100** ⚠️ | 37 |
| `204.76.203[.]226` | NL | Intelligence Hosting LLC | **100** ⚠️ | 6 |
| `204.76.203[.]224` | NL | Intelligence Hosting LLC | **100** ⚠️ | 9 |
| `204.76.203[.]225` | NL | Intelligence Hosting LLC | **100** ⚠️ | 11 |
| `116.105.173[.]160` | VN | Viettel Group | **100** ⚠️ | 15 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `180.76.171[.]14` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 31 |
| `190.134.67[.]35` | UY | Administracion Nacional de Telecomunicaciones | **45** | 0 |
| `125.43.8[.]62` | CN | China Unicom Henan province network | **31** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (98 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 61 |
| AbuseIPDB score 13 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 6 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 109 cases |
| Tool 34  | Credential Extractor        | ✅ 5 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 98 filtered (89.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 8 recon entry/entries in table (2 group(s) consolidating 4 session(s)).

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
_Report time: 2026-04-26T16:50:42Z_
