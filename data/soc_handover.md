# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T04:26:25Z |
| **Shift Time** | 04:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **38** |
| Confirmed Threats | **28** |
| False Positives Filtered | **10** (26.3%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **17** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **32** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **19** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **13** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `admin` | 2 |
| `Supervisor` | 1 |
| `debian` | 1 |
| `Nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `alpine` | 2 |
| `987654321` | 1 |
| `debian2025` | 1 |
| `passwd` | 1 |
| `ADMIN` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Supervisor` | `987654321` | 1 |
| `debian` | `debian2025` | 1 |
| `Nobody` | `passwd` | 1 |
| `admin` | `ADMIN` | 1 |
| `root` | `666666` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `666666` | `118.45.101.159` | 2026-03-25T03:10:01 |
| `root` | `letmein` | `122.160.50.155` | 2026-03-25T03:13:56 |
| `root` | `linux` | `112.194.142.167` | 2026-03-25T03:34:15 |
| `root` | `root2017` | `111.70.16.7` | 2026-03-25T03:55:58 |
| `root` | `nJQdb7fQZ6` | `47.86.5.176` | 2026-03-25T03:57:25 |
| `root` | `cOGrRrxLt4` | `47.86.5.176` | 2026-03-25T03:57:26 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **27** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS8452` | TE-AS | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |
| `AS262491` | Saulo J. de Moura Borba ME | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e65a3d753575

| Field | Detail |
|---|---|
| **Source IP** | `118.45.101[.]159` |
| **First Seen** | 2026-03-25 03:09 |
| **Last Seen** | 2026-03-25 03:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 03:09:58` | `cowrie.session.connect` |
| `2026-03-25 03:09:59` | `cowrie.client.version` |
| `2026-03-25 03:09:59` | `cowrie.client.kex` |
| `2026-03-25 03:10:01` | `cowrie.login.success` |
| `2026-03-25 03:10:01` | `cowrie.direct-tcpip.request` |
| `2026-03-25 03:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.101[.]159` to AbuseIPDB if not already reported
- [ ] Block `118.45.101[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4150e1ce6a3

| Field | Detail |
|---|---|
| **Source IP** | `122.160.50[.]155` |
| **First Seen** | 2026-03-25 03:13 |
| **Last Seen** | 2026-03-25 03:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 03:13:54` | `cowrie.session.connect` |
| `2026-03-25 03:13:55` | `cowrie.client.version` |
| `2026-03-25 03:13:55` | `cowrie.client.kex` |
| `2026-03-25 03:13:56` | `cowrie.login.success` |
| `2026-03-25 03:13:56` | `cowrie.direct-tcpip.request` |
| `2026-03-25 03:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.50[.]155` to AbuseIPDB if not already reported
- [ ] Block `122.160.50[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f902b30c989

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-03-25 03:34 |
| **Last Seen** | 2026-03-25 03:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 03:34:12` | `cowrie.session.connect` |
| `2026-03-25 03:34:12` | `cowrie.client.version` |
| `2026-03-25 03:34:12` | `cowrie.client.kex` |
| `2026-03-25 03:34:15` | `cowrie.login.success` |
| `2026-03-25 03:34:17` | `cowrie.direct-tcpip.request` |
| `2026-03-25 03:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d820d342da

| Field | Detail |
|---|---|
| **Source IP** | `111.70.16[.]7` |
| **First Seen** | 2026-03-25 03:55 |
| **Last Seen** | 2026-03-25 03:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 03:55:55` | `cowrie.session.connect` |
| `2026-03-25 03:55:56` | `cowrie.client.version` |
| `2026-03-25 03:55:56` | `cowrie.client.kex` |
| `2026-03-25 03:55:58` | `cowrie.login.success` |
| `2026-03-25 03:55:58` | `cowrie.direct-tcpip.request` |
| `2026-03-25 03:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.16[.]7` to AbuseIPDB if not already reported
- [ ] Block `111.70.16[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9e0ee5aaa8f

| Field | Detail |
|---|---|
| **Source IP** | `47.86.5[.]176` |
| **First Seen** | 2026-03-25 03:57 |
| **Last Seen** | 2026-03-25 03:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 03:57:24` | `cowrie.session.connect` |
| `2026-03-25 03:57:24` | `cowrie.client.version` |
| `2026-03-25 03:57:24` | `cowrie.client.kex` |
| `2026-03-25 03:57:25` | `cowrie.login.success` |
| `2026-03-25 03:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.86.5[.]176` to AbuseIPDB if not already reported
- [ ] Block `47.86.5[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d3864948eb

| Field | Detail |
|---|---|
| **Source IP** | `47.86.5[.]176` |
| **First Seen** | 2026-03-25 03:57 |
| **Last Seen** | 2026-03-25 03:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 03:57:26` | `cowrie.session.connect` |
| `2026-03-25 03:57:26` | `cowrie.client.version` |
| `2026-03-25 03:57:26` | `cowrie.client.kex` |
| `2026-03-25 03:57:26` | `cowrie.login.success` |
| `2026-03-25 03:57:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.86.5[.]176` to AbuseIPDB if not already reported
- [ ] Block `47.86.5[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.132.26[.]232` | **5** | 2026-03-25 03:40 | 2026-03-25 03:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `82.29.129[.]209` | **2** | 2026-03-25 03:00 | 2026-03-25 03:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.48.150[.]115` | 1 | 2026-03-25 03:30 | 2026-03-25 03:30 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.200.229[.]33` | 1 | 2026-03-25 04:16 | 2026-03-25 04:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.26[.]185` | 1 | 2026-03-25 03:58 | 2026-03-25 04:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.185.209[.]162` | 1 | 2026-03-25 03:36 | 2026-03-25 03:36 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `143.20.49[.]70` | 1 | 2026-03-25 04:13 | 2026-03-25 04:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `154.177.231[.]201` | 1 | 2026-03-25 04:11 | 2026-03-25 04:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.98[.]164` | 1 | 2026-03-25 03:54 | 2026-03-25 03:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.179.80[.]12` | 1 | 2026-03-25 02:56 | 2026-03-25 02:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.89.198[.]191` | 1 | 2026-03-25 03:36 | 2026-03-25 03:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.46[.]144` | 1 | 2026-03-25 02:13 | 2026-03-25 02:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `24.71.244[.]232` | 1 | 2026-03-25 02:37 | 2026-03-25 02:38 | 12s | 0 | `T1592` | 🟢 LOW |
| `46.161.196[.]5` | 1 | 2026-03-25 03:58 | 2026-03-25 03:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.36.143[.]189` | 1 | 2026-03-25 02:49 | 2026-03-25 02:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `83.239.0[.]202` | 1 | 2026-03-25 02:11 | 2026-03-25 02:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.202.127[.]206` | 1 | 2026-03-25 03:18 | 2026-03-25 03:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `128.185.209[.]162` | IN | BHARTI-AIRTEL | **100** ⚠️ | 2 |
| `143.20.49[.]70` | ID | Data Centre Global | **100** ⚠️ | 2 |
| `122.160.50[.]155` | IN | ABTS DELHI, | **100** ⚠️ | 50 |
| `219.89.198[.]191` | NZ | Spark New Zealand Trading Ltd | **100** ⚠️ | 15 |
| `83.239.0[.]202` | RU | OJSC Rostelecom Macroregional Branch South | **100** ⚠️ | 21 |
| `118.45.101[.]159` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `94.202.127[.]206` | AE | Emirates Integrated Telecommunications Company PJSC (EITC-DU) | **100** ⚠️ | 0 |
| `120.48.26[.]185` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 30 |
| `186.179.80[.]12` | CL | TELEFÓNICA CHILE S.A. (MAYORISTAS) | **100** ⚠️ | 33 |
| `46.161.196[.]5` | IQ | Valeen for General trading, Internet Services and Information Technology / Ltd | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 25 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 38 cases |
| Tool 34  | Credential Extractor        | ✅ 19 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (26.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 17 recon entry/entries in table (2 group(s) consolidating 7 session(s)).

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
_Report time: 2026-03-25T04:26:25Z_
