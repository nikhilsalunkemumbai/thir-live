# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-02 |
| **Generated At** | 2026-04-02T07:08:54Z |
| **Shift Time** | 07:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **15** |
| Confirmed Threats | **14** |
| False Positives Filtered | **1** (6.7%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **7** |
| High Severity Cases | **0** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **15** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **11** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **0** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `Nobody` | 2 |
| `config` | 1 |
| `debian` | 1 |
| `guest` | 1 |
| `support` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `5555555` | 1 |
| `99999` | 1 |
| `8` | 1 |
| `555555` | 1 |
| `qwerty123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `5555555` | 1 |
| `debian` | `99999` | 1 |
| `guest` | `8` | 1 |
| `support` | `555555` | 1 |
| `Admin` | `qwerty123456` | 1 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **15** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| OpenSSH | 12 |
| libssh | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 12 | 12 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 12 | 12 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **14** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS55201` | SkyQuantum Internet Service | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4812` | China Telecom (Group) | 1 | HIGH |
| `AS8151` | UNINET | 1 | HIGH |
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS10066` | LG HelloVision Corp. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.219.154[.]156` | 1 | 2026-04-02 07:07 | 2026-04-02 07:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.158.205[.]225` | 1 | 2026-04-02 07:02 | 2026-04-02 07:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.41.61[.]9` | 1 | 2026-04-02 06:43 | 2026-04-02 06:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-04-02 05:47 | 2026-04-02 05:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.107.185[.]138` | 1 | 2026-04-02 06:00 | 2026-04-02 06:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.168.60[.]146` | 1 | 2026-04-02 06:08 | 2026-04-02 06:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-04-02 06:39 | 2026-04-02 06:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.218.57[.]50` | 1 | 2026-04-02 06:03 | 2026-04-02 06:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `192.200.205[.]244` | 1 | 2026-04-02 06:20 | 2026-04-02 06:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.128.15[.]190` | 1 | 2026-04-02 05:43 | 2026-04-02 05:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.128.15[.]127` | 1 | 2026-04-02 06:25 | 2026-04-02 06:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.236.155[.]146` | 1 | 2026-04-02 06:42 | 2026-04-02 06:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-04-02 06:23 | 2026-04-02 06:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `70.89.116[.]5` | 1 | 2026-04-02 06:40 | 2026-04-02 06:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `58.57.154[.]146` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 40 |
| `124.107.185[.]138` | PH | IPG | **100** ⚠️ | 17 |
| `192.200.205[.]244` | US | SKYQUANTUM TELECOM LTD. | **100** ⚠️ | 7 |
| `222.236.155[.]146` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `222.128.15[.]127` | CN | China Unicom Beijing province network | **100** ⚠️ | 50 |
| `115.41.61[.]9` | KR | HVGaya | **100** ⚠️ | 8 |
| `180.168.60[.]146` | CN | Shanghai Xianshang Trading Co., Ltd. | **100** ⚠️ | 50 |
| `187.218.57[.]50` | MX | UNINET | **100** ⚠️ | 50 |
| `118.123.116[.]93` | CN | CHINANET Sichuan province network | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 13 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 12 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 15 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (6.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 14 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-02T07:08:54Z_
