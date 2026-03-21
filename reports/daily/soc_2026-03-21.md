# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T22:21:50Z |
| **Shift Time** | 22:21 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **61** |
| Confirmed Threats | **32** |
| False Positives Filtered | **29** (47.5%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **9** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **59** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **8** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **6** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `supervisor` | 2 |
| `root` | 2 |
| `default` | 1 |
| `admin` | 1 |
| `blank` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 1 |
| `supervisor2020` | 1 |
| `password123` | 1 |
| `supervisor2012` | 1 |
| `server` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `123` | 1 |
| `supervisor` | `supervisor2020` | 1 |
| `admin` | `password123` | 1 |
| `supervisor` | `supervisor2012` | 1 |
| `root` | `server` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `server` | `186.103.136.43` | 2026-03-21T21:26:51 |
| `root` | `root6` | `101.13.4.128` | 2026-03-21T21:56:59 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **18** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS24158` | Taiwan Mobile Co., Ltd. | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS7565` | BDCOM-BD | 1 | HIGH |
| `AS15311` | TELEFONICA EMPRESAS CHILE SA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7b5c45bfcca7

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-03-21 21:26 |
| **Last Seen** | 2026-03-21 21:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 21:26:48` | `cowrie.session.connect` |
| `2026-03-21 21:26:49` | `cowrie.client.version` |
| `2026-03-21 21:26:49` | `cowrie.client.kex` |
| `2026-03-21 21:26:51` | `cowrie.login.success` |
| `2026-03-21 21:26:52` | `cowrie.direct-tcpip.request` |
| `2026-03-21 21:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712ec7a43847

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]128` |
| **First Seen** | 2026-03-21 21:56 |
| **Last Seen** | 2026-03-21 21:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 21:56:56` | `cowrie.session.connect` |
| `2026-03-21 21:56:57` | `cowrie.client.version` |
| `2026-03-21 21:56:57` | `cowrie.client.kex` |
| `2026-03-21 21:56:59` | `cowrie.login.success` |
| `2026-03-21 21:57:00` | `cowrie.direct-tcpip.request` |
| `2026-03-21 21:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]71` | **15** | 2026-03-21 20:49 | 2026-03-21 20:53 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `49.124.153[.]40` | **2** | 2026-03-21 21:18 | 2026-03-21 22:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-21 20:56 | 2026-03-21 21:13 | 3m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]245` | 1 | 2026-03-21 20:32 | 2026-03-21 20:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.37.112[.]211` | 1 | 2026-03-21 21:43 | 2026-03-21 21:43 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.124.96[.]19` | 1 | 2026-03-21 20:26 | 2026-03-21 20:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `113.11.34[.]221` | 1 | 2026-03-21 20:56 | 2026-03-21 20:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.232.19[.]229` | 1 | 2026-03-21 20:28 | 2026-03-21 20:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.175.160[.]58` | 1 | 2026-03-21 22:04 | 2026-03-21 22:04 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.192.42[.]14` | 1 | 2026-03-21 21:34 | 2026-03-21 21:34 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-21 20:39 | 2026-03-21 20:39 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-03-21 21:45 | 2026-03-21 21:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]254` | 1 | 2026-03-21 22:16 | 2026-03-21 22:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.171[.]218` | 1 | 2026-03-21 21:15 | 2026-03-21 21:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `101.13.4[.]128` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 28 |
| `223.123.43[.]71` | PK | CMPak Limited | **100** ⚠️ | 35 |
| `65.20.171[.]218` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 13 |
| `120.48.109[.]59` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 10 |
| `183.247.171[.]186` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `113.11.34[.]221` | BD | BDCOM Online Limited, Internet Service Provider, | **100** ⚠️ | 50 |
| `116.232.19[.]229` | CN | CHINANET Shanghai province network | **100** ⚠️ | 11 |
| `101.126.54[.]245` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 46 |
| `186.103.136[.]43` | CL | CONSEJO DE DEFENSA DEL NINO/CIUDAD DEL NINO | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 61 cases |
| Tool 34  | Credential Extractor        | ✅ 8 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (47.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 14 recon entry/entries in table (3 group(s) consolidating 19 session(s)).

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
_Report time: 2026-03-21T22:21:50Z_
