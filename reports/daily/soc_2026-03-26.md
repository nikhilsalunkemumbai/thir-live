# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T13:09:43Z |
| **Shift Time** | 13:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **111** |
| Confirmed Threats | **97** |
| False Positives Filtered | **14** (12.6%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **12** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **109** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **71** |
| Unique Credential Pairs | **70** |
| Unique Usernames | **59** |
| Unique Passwords | **69** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `test` | 3 |
| `root` | 3 |
| `debian` | 3 |
| `ubnt` | 2 |
| `guest` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `unitrends1` | 2 |
| `hadoop` | 2 |
| `12345678` | 1 |
| `ubnt2015` | 1 |
| `Host: 13.235.92.17:23` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `unitrends1` | 2 |
| `Supervisor` | `12345678` | 1 |
| `ubnt` | `ubnt2015` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36` | `Accept: */*` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `unitrends1` | `111.70.38.54` | 2026-03-26T12:09:27 |
| `root` | `unitrends1` | `122.136.195.32` | 2026-03-26T12:09:38 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **27** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS3549` | Level 3 Parent, LLC | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS26599` | TELEFÔNICA BRASIL S.A | 1 | MEDIUM |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f5c4e9c14b71

| Field | Detail |
|---|---|
| **Source IP** | `111.70.38[.]54` |
| **First Seen** | 2026-03-26 12:09 |
| **Last Seen** | 2026-03-26 12:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 12:09:24` | `cowrie.session.connect` |
| `2026-03-26 12:09:25` | `cowrie.client.version` |
| `2026-03-26 12:09:25` | `cowrie.client.kex` |
| `2026-03-26 12:09:27` | `cowrie.login.success` |
| `2026-03-26 12:09:28` | `cowrie.direct-tcpip.request` |
| `2026-03-26 12:09:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.38[.]54` to AbuseIPDB if not already reported
- [ ] Block `111.70.38[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-245266461b7c

| Field | Detail |
|---|---|
| **Source IP** | `122.136.195[.]32` |
| **First Seen** | 2026-03-26 12:09 |
| **Last Seen** | 2026-03-26 12:09 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 12:09:33` | `cowrie.session.connect` |
| `2026-03-26 12:09:34` | `cowrie.client.version` |
| `2026-03-26 12:09:34` | `cowrie.client.kex` |
| `2026-03-26 12:09:38` | `cowrie.login.success` |
| `2026-03-26 12:09:39` | `cowrie.direct-tcpip.request` |
| `2026-03-26 12:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.136.195[.]32` to AbuseIPDB if not already reported
- [ ] Block `122.136.195[.]32` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `114.67.110[.]59` | **61** | 2026-03-26 11:42 | 2026-03-26 12:14 | 13m | 54 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.91.210[.]63` | **17** | 2026-03-26 10:52 | 2026-03-26 10:54 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `66.228.53[.]157` | **2** | 2026-03-26 11:09 | 2026-03-26 11:09 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `103.190.91[.]99` | 1 | 2026-03-26 11:50 | 2026-03-26 11:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.122.196[.]230` | 1 | 2026-03-26 11:09 | 2026-03-26 11:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.1[.]97` | 1 | 2026-03-26 11:54 | 2026-03-26 11:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-03-26 12:35 | 2026-03-26 12:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.218.57[.]50` | 1 | 2026-03-26 12:15 | 2026-03-26 12:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.171.78[.]250` | 1 | 2026-03-26 12:54 | 2026-03-26 12:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.216.132[.]3` | 1 | 2026-03-26 10:58 | 2026-03-26 10:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.216.132[.]31` | 1 | 2026-03-26 11:45 | 2026-03-26 11:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `207.254.71[.]129` | 1 | 2026-03-26 12:53 | 2026-03-26 12:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.81.224[.]7` | 1 | 2026-03-26 12:55 | 2026-03-26 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `36.137.38[.]119` | 1 | 2026-03-26 12:36 | 2026-03-26 12:36 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.159.224[.]116` | 1 | 2026-03-26 12:31 | 2026-03-26 12:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-26 12:19 | 2026-03-26 12:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.20.136[.]183` | 1 | 2026-03-26 11:38 | 2026-03-26 11:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.167[.]78` | 1 | 2026-03-26 11:48 | 2026-03-26 11:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `190.171.78[.]250` | CO | ONRED SOLUCIONES DE CONECTIVIDAD S.A.S. | **100** ⚠️ | 1 |
| `190.216.132[.]31` | CO | Level 3 Colombia S.A. | **100** ⚠️ | 4 |
| `49.159.224[.]116` | TW | TFN MEDIA CO., LTD. | **100** ⚠️ | 5 |
| `118.122.196[.]230` | CN | CHINANET Sichuan province network | **100** ⚠️ | 43 |
| `36.137.38[.]119` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `3.81.224[.]7` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 10 |
| `66.228.53[.]157` | US | Linode | **100** ⚠️ | 50 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 1 |
| `179.185.1[.]97` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 15 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 111 cases |
| Tool 34  | Credential Extractor        | ✅ 71 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (12.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 18 recon entry/entries in table (3 group(s) consolidating 80 session(s)).

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
_Report time: 2026-03-26T13:09:43Z_
