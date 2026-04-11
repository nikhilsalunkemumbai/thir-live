# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-11 |
| **Generated At** | 2026-04-11T05:24:31Z |
| **Shift Time** | 05:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **27** |
| Confirmed Threats | **13** |
| False Positives Filtered | **14** (51.8%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **8** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **3** |
| Unique Credential Pairs | **2** |
| Unique Usernames | **2** |
| Unique Passwords | **1** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 2 |
| `root` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 2 |
| `root` | `admin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `64.89.161.182` | 2026-04-11T02:15:17 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **27** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 7 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `4ed0d5b0dc3b...` | Mirai/variant | 1 | 1 |
| `19532158b559...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | libssh | 5 | 2 | — |
| `4ed0d5b0dc3b...` | libssh | 1 | 1 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS3269` | Telecom Italia S.p.A. | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS138245` | Xpress Net Solution | 1 | LOW |
| `AS56040` | China Mobile communications corporation | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2126e7beaeeb

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]182` |
| **First Seen** | 2026-04-11 02:15 |
| **Last Seen** | 2026-04-11 02:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 02:15:17` | `cowrie.session.connect` |
| `2026-04-11 02:15:17` | `cowrie.client.version` |
| `2026-04-11 02:15:17` | `cowrie.client.kex` |
| `2026-04-11 02:15:17` | `cowrie.login.success` |
| `2026-04-11 02:15:18` | `cowrie.direct-tcpip.request` |
| `2026-04-11 02:15:18` | `cowrie.direct-tcpip.data` |
| `2026-04-11 02:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]182` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.131.220[.]121` | **6** | 2026-04-11 02:44 | 2026-04-11 02:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.145.100[.]92` | **2** | 2026-04-11 02:45 | 2026-04-11 02:48 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-04-11 02:25 | 2026-04-11 02:26 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `43.134.94[.]132` | 1 | 2026-04-11 04:47 | 2026-04-11 04:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.161[.]182` | 1 | 2026-04-11 02:14 | 2026-04-11 02:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.222.172[.]218` | 1 | 2026-04-11 04:43 | 2026-04-11 04:43 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `43.134.94[.]132` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 10 |
| `8.222.172[.]218` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 27 |
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `64.89.161[.]182` | LU | Ghosty Networks LLC | **100** ⚠️ | 50 |
| `118.145.100[.]92` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 16 |
| `95.252.73[.]222` | IT | Telecom Italia S.p.A. | **69** | 0 |
| `154.65.121[.]140` | ZA | Letaba Wireless Internet CC | **65** | 2 |
| `8.217.90[.]114` | HK | Aliyun Computing Co.LTD | **32** | 0 |
| `103.181.161[.]11` | IN | MONGA TELECOM | 20 | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 10 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 27 cases |
| Tool 34  | Credential Extractor        | ✅ 3 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (51.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 6 recon entry/entries in table (2 group(s) consolidating 8 session(s)).

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
_Report time: 2026-04-11T05:24:31Z_
