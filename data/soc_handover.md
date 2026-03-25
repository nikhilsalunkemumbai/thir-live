# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T17:00:29Z |
| **Shift Time** | 17:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **60** |
| Confirmed Threats | **44** |
| False Positives Filtered | **16** (26.7%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **14** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **59** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **28** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `support` | 2 |
| `etc` | 2 |
| `ubuntu` | 1 |
| `yzh` | 1 |
| `Centos` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 4 |
| `1234` | 3 |
| `111111` | 3 |
| `etc` | 2 |
| `123123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `etc` | `etc` | 2 |
| `ubuntu` | `123123` | 1 |
| `yzh` | `1234` | 1 |
| `Centos` | `123321` | 1 |
| `support` | `1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@$$w0rd` | `183.106.59.245` | 2026-03-25T15:50:47 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **27** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS41668` | JSC ER-Telecom Holding | 1 | HIGH |
| `AS5089` | Virgin Media Limited | 1 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3aa996d3fad5

| Field | Detail |
|---|---|
| **Source IP** | `183.106.59[.]245` |
| **First Seen** | 2026-03-25 15:50 |
| **Last Seen** | 2026-03-25 15:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 15:50:44` | `cowrie.session.connect` |
| `2026-03-25 15:50:45` | `cowrie.client.version` |
| `2026-03-25 15:50:45` | `cowrie.client.kex` |
| `2026-03-25 15:50:47` | `cowrie.login.success` |
| `2026-03-25 15:50:47` | `cowrie.direct-tcpip.request` |
| `2026-03-25 15:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.106.59[.]245` to AbuseIPDB if not already reported
- [ ] Block `183.106.59[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.138.194[.]82` | **8** | 2026-03-25 15:18 | 2026-03-25 15:38 | 14m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.155[.]89` | **8** | 2026-03-25 16:18 | 2026-03-25 16:37 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `58.33.97[.]119` | **8** | 2026-03-25 16:03 | 2026-03-25 16:09 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `77.110.98[.]213` | **7** | 2026-03-25 16:19 | 2026-03-25 16:37 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `111.171.125[.]94` | 1 | 2026-03-25 15:30 | 2026-03-25 15:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.25.140[.]211` | 1 | 2026-03-25 15:30 | 2026-03-25 15:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-25 16:43 | 2026-03-25 16:43 | 6s | 0 | `T1592` | 🟢 LOW |
| `122.187.229[.]220` | 1 | 2026-03-25 16:53 | 2026-03-25 16:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.118.230[.]64` | 1 | 2026-03-25 16:41 | 2026-03-25 16:41 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `140.84.179[.]128` | 1 | 2026-03-25 16:33 | 2026-03-25 16:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.230.204[.]246` | 1 | 2026-03-25 16:04 | 2026-03-25 16:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.216.132[.]12` | 1 | 2026-03-25 16:13 | 2026-03-25 16:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `210.86.162[.]220` | 1 | 2026-03-25 15:08 | 2026-03-25 15:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-25 15:01 | 2026-03-25 15:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-03-25 16:57 | 2026-03-25 16:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `92.255.196[.]185` | 1 | 2026-03-25 16:11 | 2026-03-25 16:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `120.48.109[.]59` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 12 |
| `111.171.125[.]94` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `183.106.59[.]245` | KR | Korea Telecom | **100** ⚠️ | 26 |
| `183.230.204[.]246` | CN | China Mobile Communications Corporation | **100** ⚠️ | 44 |
| `196.189.155[.]89` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `122.187.229[.]220` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `92.255.196[.]185` | RU | CJSC Company ER-Telecom Kazan' | **100** ⚠️ | 50 |
| `59.126.16[.]66` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 0 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 0 |
| `77.110.98[.]213` | DE | AEZA GROUP LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 49 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 60 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (26.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 16 recon entry/entries in table (4 group(s) consolidating 31 session(s)).

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
_Report time: 2026-03-25T17:00:29Z_
