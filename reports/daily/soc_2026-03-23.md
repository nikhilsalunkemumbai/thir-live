# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T18:52:14Z |
| **Shift Time** | 18:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **52** |
| Confirmed Threats | **45** |
| False Positives Filtered | **7** (13.5%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **13** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **12** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 7 |
| `Test` | 3 |
| `root` | 3 |
| `test` | 1 |
| `Nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `qwerty1234` | 2 |
| `root2011` | 2 |
| `test10` | 1 |
| `password` | 1 |
| `supervisor2023` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Test` | `qwerty1234` | 2 |
| `root` | `root2011` | 2 |
| `test` | `test10` | 1 |
| `Nobody` | `password` | 1 |
| `supervisor` | `supervisor2023` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz2wsx` | `111.70.32.6` | 2026-03-23T18:13:48 |
| `root` | `root2011` | `112.30.7.45` | 2026-03-23T18:37:15 |
| `root` | `root2011` | `183.82.108.109` | 2026-03-23T18:37:22 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **19** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | LOW |
| `AS18403` | FPT Telecom Company | 1 | HIGH |
| `AS24323` | aamra networks limited, | 1 | HIGH |
| `AS131740` | PT Smart Media Pratama | 1 | HIGH |
| `AS10439` | CariNet, Inc. | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-365cf1e254ad

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-03-23 18:13 |
| **Last Seen** | 2026-03-23 18:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 18:13:45` | `cowrie.session.connect` |
| `2026-03-23 18:13:46` | `cowrie.client.version` |
| `2026-03-23 18:13:46` | `cowrie.client.kex` |
| `2026-03-23 18:13:48` | `cowrie.login.success` |
| `2026-03-23 18:13:49` | `cowrie.direct-tcpip.request` |
| `2026-03-23 18:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75679a50f7be

| Field | Detail |
|---|---|
| **Source IP** | `112.30.7[.]45` |
| **First Seen** | 2026-03-23 18:37 |
| **Last Seen** | 2026-03-23 18:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 18:37:12` | `cowrie.session.connect` |
| `2026-03-23 18:37:13` | `cowrie.client.version` |
| `2026-03-23 18:37:13` | `cowrie.client.kex` |
| `2026-03-23 18:37:15` | `cowrie.login.success` |
| `2026-03-23 18:37:15` | `cowrie.direct-tcpip.request` |
| `2026-03-23 18:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.30.7[.]45` to AbuseIPDB if not already reported
- [ ] Block `112.30.7[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7684c665f909

| Field | Detail |
|---|---|
| **Source IP** | `183.82.108[.]109` |
| **First Seen** | 2026-03-23 18:37 |
| **Last Seen** | 2026-03-23 18:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 18:37:20` | `cowrie.session.connect` |
| `2026-03-23 18:37:21` | `cowrie.client.version` |
| `2026-03-23 18:37:21` | `cowrie.client.kex` |
| `2026-03-23 18:37:22` | `cowrie.login.success` |
| `2026-03-23 18:37:22` | `cowrie.direct-tcpip.request` |
| `2026-03-23 18:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.108[.]109` to AbuseIPDB if not already reported
- [ ] Block `183.82.108[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `47.93.159[.]83` | **26** | 2026-03-23 17:39 | 2026-03-23 18:40 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `183.81.33[.]183` | **7** | 2026-03-23 17:57 | 2026-03-23 18:47 | 3m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `43.245.249[.]251` | **2** | 2026-03-23 17:39 | 2026-03-23 17:43 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `120.230.180[.]244` | 1 | 2026-03-23 18:08 | 2026-03-23 18:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.187.191[.]77` | 1 | 2026-03-23 17:27 | 2026-03-23 17:27 | 12s | 0 | `T1592` | 🟢 LOW |
| `154.177.231[.]201` | 1 | 2026-03-23 18:03 | 2026-03-23 18:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.160.114[.]72` | 1 | 2026-03-23 17:19 | 2026-03-23 17:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.248.0[.]242` | 1 | 2026-03-23 17:00 | 2026-03-23 17:00 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.58.73[.]238` | 1 | 2026-03-23 17:24 | 2026-03-23 17:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-03-23 17:28 | 2026-03-23 17:28 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `111.70.32[.]6` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 34 |
| `121.187.191[.]77` | KR | Korea Telecom | **100** ⚠️ | 7 |
| `43.245.249[.]251` | ID | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `120.230.180[.]244` | CN | China Mobile Communications Corporation | **100** ⚠️ | 5 |
| `112.30.7[.]45` | CN | China Mobile Communications Corporation | **100** ⚠️ | 37 |
| `66.240.236[.]116` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `47.93.159[.]83` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 0 |
| `183.81.33[.]183` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `218.248.0[.]242` | IN | National Internet Backbone | **100** ⚠️ | 16 |
| `182.160.114[.]72` | BD | Aamra Networks Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 52 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 10 recon entry/entries in table (3 group(s) consolidating 35 session(s)).

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
_Report time: 2026-03-23T18:52:14Z_
