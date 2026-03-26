# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T08:52:42Z |
| **Shift Time** | 08:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **21** |
| Confirmed Threats | **17** |
| False Positives Filtered | **4** (19.1%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **12** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **19** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **10** |
| Unique Credential Pairs | **9** |
| Unique Usernames | **8** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `pi` | 2 |
| `debian` | 1 |
| `ubnt` | 1 |
| `test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `4321` | 2 |
| `logon` | 2 |
| `debian2020` | 1 |
| `ubnt2012` | 1 |
| `44444` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `4321` | 2 |
| `debian` | `debian2020` | 1 |
| `ubnt` | `ubnt2012` | 1 |
| `test` | `44444` | 1 |
| `pi` | `1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `4321` | `96.1.40.151` | 2026-03-26T07:41:33 |
| `root` | `4321` | `178.178.222.56` | 2026-03-26T07:41:40 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS852` | TELUS Communications Inc. | 2 | HIGH |
| `AS135905` | VIETNAM POSTS AND TELECOMMUNICATIONS GROUP | 1 | LOW |
| `AS27818` | Cotesma | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | MEDIUM |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6cb41c5ff111

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-03-26 07:41 |
| **Last Seen** | 2026-03-26 07:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 07:41:31` | `cowrie.session.connect` |
| `2026-03-26 07:41:32` | `cowrie.client.version` |
| `2026-03-26 07:41:32` | `cowrie.client.kex` |
| `2026-03-26 07:41:33` | `cowrie.login.success` |
| `2026-03-26 07:41:34` | `cowrie.direct-tcpip.request` |
| `2026-03-26 07:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd906934a994

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]56` |
| **First Seen** | 2026-03-26 07:41 |
| **Last Seen** | 2026-03-26 07:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 07:41:39` | `cowrie.session.connect` |
| `2026-03-26 07:41:39` | `cowrie.client.version` |
| `2026-03-26 07:41:39` | `cowrie.client.kex` |
| `2026-03-26 07:41:40` | `cowrie.login.success` |
| `2026-03-26 07:41:41` | `cowrie.direct-tcpip.request` |
| `2026-03-26 07:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]56` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.237.187[.]97` | **8** | 2026-03-26 08:32 | 2026-03-26 08:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `111.70.51[.]23` | 1 | 2026-03-26 07:20 | 2026-03-26 07:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.204.1[.]45` | 1 | 2026-03-26 08:49 | 2026-03-26 08:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `136.248.73[.]230` | 1 | 2026-03-26 07:46 | 2026-03-26 07:47 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.114.143[.]79` | 1 | 2026-03-26 07:20 | 2026-03-26 07:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.148.187[.]172` | 1 | 2026-03-26 08:23 | 2026-03-26 08:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-26 08:02 | 2026-03-26 08:02 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `207.6.37[.]197` | 1 | 2026-03-26 07:23 | 2026-03-26 07:23 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `117.204.1[.]45` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 2 |
| `96.1.40[.]151` | CA | TELUS Mobility-Ontario | **100** ⚠️ | 50 |
| `111.70.51[.]23` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 16 |
| `136.248.73[.]230` | BR | Oracle Corporation | **100** ⚠️ | 29 |
| `186.201.54[.]90` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `178.178.222[.]56` | RU | PJSC MegaFon | **100** ⚠️ | 42 |
| `186.148.187[.]172` | CO | TV AZTECA SUCURSAL COLOMBIA | **100** ⚠️ | 0 |
| `207.6.37[.]197` | CA | TELUS-FIBRE-VANCBC06 | **100** ⚠️ | 0 |
| `181.114.143[.]79` | AR | Cotesma | **100** ⚠️ | 0 |
| `112.237.187[.]97` | CN | China Unicom Shandong province network | **91** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 21 cases |
| Tool 34  | Credential Extractor        | ✅ 10 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (19.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 8 recon entry/entries in table (1 group(s) consolidating 8 session(s)).

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
_Report time: 2026-03-26T08:52:42Z_
