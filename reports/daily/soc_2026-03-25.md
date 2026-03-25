# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T14:56:47Z |
| **Shift Time** | 14:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **41** |
| Confirmed Threats | **36** |
| False Positives Filtered | **5** (12.2%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **15** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **35** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **16** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `blank` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `88` | 2 |
| `vizxv` | 2 |
| `12345` | 2 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `88` | 2 |
| `root` | `vizxv` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `88` | `65.20.202.4` | 2026-03-25T13:14:09 |
| `root` | `88` | `59.14.191.130` | 2026-03-25T13:14:21 |
| `root` | `vizxv` | `27.123.112.126` | 2026-03-25T13:23:12 |
| `root` | `vizxv` | `50.67.177.253` | 2026-03-25T13:23:21 |
| `root` | `root2021` | `187.8.3.230` | 2026-03-25T14:26:43 |
| `root` | `root2021` | `91.144.158.62` | 2026-03-25T14:26:51 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **23** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS4808` | China Unicom Beijing Province Network | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS42116` | JSC ER-Telecom Holding | 1 | HIGH |
| `AS13428` | Surf Air Wireless, LLC | 1 | LOW |
| `AS4780` | Digital United Inc. | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-574669df3b62

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-03-25 13:14 |
| **Last Seen** | 2026-03-25 13:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 13:14:08` | `cowrie.session.connect` |
| `2026-03-25 13:14:08` | `cowrie.client.version` |
| `2026-03-25 13:14:08` | `cowrie.client.kex` |
| `2026-03-25 13:14:09` | `cowrie.login.success` |
| `2026-03-25 13:14:09` | `cowrie.direct-tcpip.request` |
| `2026-03-25 13:14:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbae42181257

| Field | Detail |
|---|---|
| **Source IP** | `59.14.191[.]130` |
| **First Seen** | 2026-03-25 13:14 |
| **Last Seen** | 2026-03-25 13:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 13:14:19` | `cowrie.session.connect` |
| `2026-03-25 13:14:19` | `cowrie.client.version` |
| `2026-03-25 13:14:19` | `cowrie.client.kex` |
| `2026-03-25 13:14:21` | `cowrie.login.success` |
| `2026-03-25 13:14:22` | `cowrie.direct-tcpip.request` |
| `2026-03-25 13:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.14.191[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.14.191[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8a0ef2419f

| Field | Detail |
|---|---|
| **Source IP** | `27.123.112[.]126` |
| **First Seen** | 2026-03-25 13:23 |
| **Last Seen** | 2026-03-25 13:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 13:23:10` | `cowrie.session.connect` |
| `2026-03-25 13:23:10` | `cowrie.client.version` |
| `2026-03-25 13:23:10` | `cowrie.client.kex` |
| `2026-03-25 13:23:12` | `cowrie.login.success` |
| `2026-03-25 13:23:12` | `cowrie.direct-tcpip.request` |
| `2026-03-25 13:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.123.112[.]126` to AbuseIPDB if not already reported
- [ ] Block `27.123.112[.]126` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1fe3a29f5a

| Field | Detail |
|---|---|
| **Source IP** | `50.67.177[.]253` |
| **First Seen** | 2026-03-25 13:23 |
| **Last Seen** | 2026-03-25 13:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 13:23:18` | `cowrie.session.connect` |
| `2026-03-25 13:23:19` | `cowrie.client.version` |
| `2026-03-25 13:23:19` | `cowrie.client.kex` |
| `2026-03-25 13:23:21` | `cowrie.login.success` |
| `2026-03-25 13:23:22` | `cowrie.direct-tcpip.request` |
| `2026-03-25 13:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.67.177[.]253` to AbuseIPDB if not already reported
- [ ] Block `50.67.177[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e95f06bde815

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-03-25 14:26 |
| **Last Seen** | 2026-03-25 14:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 14:26:40` | `cowrie.session.connect` |
| `2026-03-25 14:26:40` | `cowrie.client.version` |
| `2026-03-25 14:26:40` | `cowrie.client.kex` |
| `2026-03-25 14:26:43` | `cowrie.login.success` |
| `2026-03-25 14:26:44` | `cowrie.direct-tcpip.request` |
| `2026-03-25 14:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c4174052a7

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-03-25 14:26 |
| **Last Seen** | 2026-03-25 14:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 14:26:49` | `cowrie.session.connect` |
| `2026-03-25 14:26:50` | `cowrie.client.version` |
| `2026-03-25 14:26:50` | `cowrie.client.kex` |
| `2026-03-25 14:26:51` | `cowrie.login.success` |
| `2026-03-25 14:26:51` | `cowrie.direct-tcpip.request` |
| `2026-03-25 14:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.176[.]249` | **10** | 2026-03-25 13:37 | 2026-03-25 13:51 | 14m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.218.118[.]203` | **6** | 2026-03-25 14:06 | 2026-03-25 14:10 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `102.88.10[.]10` | 1 | 2026-03-25 14:17 | 2026-03-25 14:17 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.242.112[.]197` | 1 | 2026-03-25 13:52 | 2026-03-25 13:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.180.129[.]87` | 1 | 2026-03-25 13:45 | 2026-03-25 13:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.171.78[.]250` | 1 | 2026-03-25 13:34 | 2026-03-25 13:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.154.80[.]51` | 1 | 2026-03-25 13:56 | 2026-03-25 13:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.64.36[.]101` | 1 | 2026-03-25 13:35 | 2026-03-25 13:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]25` | 1 | 2026-03-25 13:14 | 2026-03-25 13:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.206.201[.]253` | 1 | 2026-03-25 14:47 | 2026-03-25 14:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.153[.]146` | 1 | 2026-03-25 14:05 | 2026-03-25 14:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.179[.]251` | 1 | 2026-03-25 13:24 | 2026-03-25 13:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.12.241[.]225` | 1 | 2026-03-25 14:48 | 2026-03-25 14:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.231.206[.]12` | 1 | 2026-03-25 14:40 | 2026-03-25 14:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]15` | 1 | 2026-03-25 14:42 | 2026-03-25 14:42 | 1s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]4` | 1 | 2026-03-25 14:40 | 2026-03-25 14:40 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `49.124.151[.]25` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 15 |
| `65.20.153[.]146` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `94.231.206[.]12` | SG | FR ONYPHE | **100** ⚠️ | 35 |
| `121.242.112[.]197` | IN | Internet Service Provider | **100** ⚠️ | 5 |
| `50.67.177[.]253` | CA | Shaw Communications | **100** ⚠️ | 16 |
| `102.88.10[.]10` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `71.12.241[.]225` | US | Charter Communications LLC | **100** ⚠️ | 35 |
| `65.20.179[.]251` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `59.14.191[.]130` | KR | Sudogwonseobubonbu | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 31 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 41 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (12.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 16 recon entry/entries in table (2 group(s) consolidating 16 session(s)).

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
_Report time: 2026-03-25T14:56:47Z_
