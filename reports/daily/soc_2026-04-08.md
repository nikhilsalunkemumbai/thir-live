# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T19:13:16Z |
| **Shift Time** | 19:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **11** |
| Confirmed Threats | **9** |
| False Positives Filtered | **2** (18.2%) |
| Unique Attacker IPs | **8** |
| Countries of Origin | **5** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **10** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **4** |
| Unique Credential Pairs | **4** |
| Unique Usernames | **3** |
| Unique Passwords | **4** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `admin` | 1 |
| `ubnt` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 1 |
| `ubnt` | 1 |
| `root` | 1 |
| `1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 1 |
| `ubnt` | `ubnt` | 1 |
| `root` | `root` | 1 |
| `root` | `1` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1` | `64.236.145.64` | 2026-04-08T18:44:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **11** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| AsyncSSH (Python) | 3 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `fda360b1b4f4...` | Mirai/variant | 3 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `fda360b1b4f4...` | AsyncSSH (Python) | 3 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **8** |
| Unique ASNs | **6** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS7552` | Viettel Group | 1 | HIGH |
| `AS29852` | Honest Networks, LLC | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS6849` | JSC Ukrtelecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-18ed431bc878

| Field | Detail |
|---|---|
| **Source IP** | `64.236.145[.]64` |
| **First Seen** | 2026-04-08 18:44 |
| **Last Seen** | 2026-04-08 18:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `nproc 2>/dev/null || (grep -c '^processor' /proc/cpuinfo 2>/dev/null) || echo 0, grep -c ^processor /proc/cpuinfo 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 18:44:47` | `cowrie.session.connect` |
| `2026-04-08 18:44:47` | `cowrie.client.version` |
| `2026-04-08 18:44:47` | `cowrie.client.kex` |
| `2026-04-08 18:44:48` | `cowrie.login.success` |
| `2026-04-08 18:44:49` | `cowrie.session.params` |
| `2026-04-08 18:44:49` | `cowrie.command.input` |
| `2026-04-08 18:44:49` | `cowrie.command.input` |
| `2026-04-08 18:44:49` | `cowrie.log.closed` |
| `2026-04-08 18:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.236.145[.]64` to AbuseIPDB if not already reported
- [ ] Block `64.236.145[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `27.79.43[.]155` | **3** | 2026-04-08 16:59 | 2026-04-08 17:01 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `52.180.146[.]167` | **2** | 2026-04-08 19:11 | 2026-04-08 19:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `147.185.154[.]204` | 1 | 2026-04-08 18:23 | 2026-04-08 18:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-08 17:35 | 2026-04-08 17:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `46.200.77[.]171` | 1 | 2026-04-08 18:30 | 2026-04-08 18:31 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `27.79.43[.]155` | VN | Viettel Group | **100** ⚠️ | 1 |
| `147.185.154[.]204` | US | Honest Networks, LLC | **100** ⚠️ | 0 |
| `52.180.146[.]167` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `64.236.145[.]64` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `46.200.77[.]171` | UA | JSC Ukrtelecom | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 11 cases |
| Tool 34  | Credential Extractor        | ✅ 4 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 8 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (18.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 6 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 5 recon entry/entries in table (2 group(s) consolidating 5 session(s)).

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
_Report time: 2026-04-08T19:13:16Z_
