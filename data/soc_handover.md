# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T20:36:28Z |
| **Shift Time** | 20:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **31** |
| Confirmed Threats | **23** |
| False Positives Filtered | **8** (25.8%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **14** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **14** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `operator` | 1 |
| `support` | 1 |
| `Ubnt` | 1 |
| `default` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1qazxsw2` | 2 |
| `4` | 2 |
| `22222` | 2 |
| `abc123` | 2 |
| `operator2016` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `1qazxsw2` | 2 |
| `root` | `22222` | 2 |
| `operator` | `operator2016` | 1 |
| `support` | `test` | 1 |
| `Ubnt` | `1q2w3e4r` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qazxsw2` | `200.105.141.172` | 2026-03-27T19:33:11 |
| `root` | `1qazxsw2` | `223.107.72.234` | 2026-03-27T19:33:19 |
| `root` | `4` | `60.161.14.45` | 2026-03-27T19:50:16 |
| `root` | `22222` | `112.94.5.43` | 2026-03-27T20:21:41 |
| `root` | `22222` | `61.10.180.65` | 2026-03-27T20:21:53 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **27** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS17622` | China Unicom Guangzhou network | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS4812` | China Telecom (Group) | 1 | HIGH |
| `AS24165` | UNION BROADBAND NETWORK | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4369f9b3694b

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-03-27 19:33 |
| **Last Seen** | 2026-03-27 19:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 19:33:08` | `cowrie.session.connect` |
| `2026-03-27 19:33:08` | `cowrie.client.version` |
| `2026-03-27 19:33:08` | `cowrie.client.kex` |
| `2026-03-27 19:33:11` | `cowrie.login.success` |
| `2026-03-27 19:33:11` | `cowrie.direct-tcpip.request` |
| `2026-03-27 19:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa610d335b49

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-03-27 19:33 |
| **Last Seen** | 2026-03-27 19:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 19:33:17` | `cowrie.session.connect` |
| `2026-03-27 19:33:18` | `cowrie.client.version` |
| `2026-03-27 19:33:18` | `cowrie.client.kex` |
| `2026-03-27 19:33:19` | `cowrie.login.success` |
| `2026-03-27 19:33:20` | `cowrie.direct-tcpip.request` |
| `2026-03-27 19:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc12b17bd10

| Field | Detail |
|---|---|
| **Source IP** | `60.161.14[.]45` |
| **First Seen** | 2026-03-27 19:50 |
| **Last Seen** | 2026-03-27 19:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 19:50:13` | `cowrie.session.connect` |
| `2026-03-27 19:50:14` | `cowrie.client.version` |
| `2026-03-27 19:50:14` | `cowrie.client.kex` |
| `2026-03-27 19:50:16` | `cowrie.login.success` |
| `2026-03-27 19:50:17` | `cowrie.direct-tcpip.request` |
| `2026-03-27 19:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.161.14[.]45` to AbuseIPDB if not already reported
- [ ] Block `60.161.14[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a44948522360

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-03-27 20:21 |
| **Last Seen** | 2026-03-27 20:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 20:21:39` | `cowrie.session.connect` |
| `2026-03-27 20:21:40` | `cowrie.client.version` |
| `2026-03-27 20:21:40` | `cowrie.client.kex` |
| `2026-03-27 20:21:41` | `cowrie.login.success` |
| `2026-03-27 20:21:42` | `cowrie.direct-tcpip.request` |
| `2026-03-27 20:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030d625fe9c7

| Field | Detail |
|---|---|
| **Source IP** | `61.10.180[.]65` |
| **First Seen** | 2026-03-27 20:21 |
| **Last Seen** | 2026-03-27 20:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 20:21:51` | `cowrie.session.connect` |
| `2026-03-27 20:21:52` | `cowrie.client.version` |
| `2026-03-27 20:21:52` | `cowrie.client.kex` |
| `2026-03-27 20:21:53` | `cowrie.login.success` |
| `2026-03-27 20:21:54` | `cowrie.direct-tcpip.request` |
| `2026-03-27 20:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.10.180[.]65` to AbuseIPDB if not already reported
- [ ] Block `61.10.180[.]65` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `110.37.81[.]245` | 1 | 2026-03-27 19:05 | 2026-03-27 19:05 | 14s | 0 | `T1592` | 🟢 LOW |
| `111.171.125[.]94` | 1 | 2026-03-27 19:30 | 2026-03-27 19:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-03-27 19:50 | 2026-03-27 19:50 | 7s | 0 | `T1592` | 🟢 LOW |
| `119.201.59[.]224` | 1 | 2026-03-27 20:02 | 2026-03-27 20:02 | 17s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.254.1[.]68` | 1 | 2026-03-27 19:32 | 2026-03-27 19:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `138.36.127[.]80` | 1 | 2026-03-27 19:10 | 2026-03-27 19:10 | 7s | 0 | `T1592` | 🟢 LOW |
| `139.135.41[.]173` | 1 | 2026-03-27 20:15 | 2026-03-27 20:15 | 11s | 0 | `T1592` | 🟢 LOW |
| `147.92.66[.]188` | 1 | 2026-03-27 19:25 | 2026-03-27 19:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]47` | 1 | 2026-03-27 19:53 | 2026-03-27 19:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.167.207[.]234` | 1 | 2026-03-27 20:31 | 2026-03-27 20:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.72.17[.]75` | 1 | 2026-03-27 20:12 | 2026-03-27 20:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.25.113[.]218` | 1 | 2026-03-27 19:01 | 2026-03-27 19:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.69[.]224` | 1 | 2026-03-27 19:05 | 2026-03-27 19:05 | 3s | 0 | `T1592` | 🟢 LOW |
| `202.82.20[.]241` | 1 | 2026-03-27 20:01 | 2026-03-27 20:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.2.40[.]10` | 1 | 2026-03-27 19:13 | 2026-03-27 19:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-03-27 19:10 | 2026-03-27 19:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.127.187[.]151` | 1 | 2026-03-27 19:47 | 2026-03-27 19:47 | 31s | 0 | `T1592` | 🟢 LOW |
| `60.172.41[.]103` | 1 | 2026-03-27 20:10 | 2026-03-27 20:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `122.254.1[.]68` | TW | TFN MEDIA CO., LTD. | **100** ⚠️ | 6 |
| `147.92.66[.]188` | CA | Bell Canada | **100** ⚠️ | 32 |
| `111.171.125[.]94` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `60.172.41[.]103` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `119.152.102[.]54` | PK | Pakistan Telecommunication Company Limited | **100** ⚠️ | 23 |
| `119.201.59[.]224` | KR | Korea Telecom | **100** ⚠️ | 31 |
| `2.55.69[.]224` | IL | Partner Communications Ltd. | **100** ⚠️ | 26 |
| `221.2.40[.]10` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `200.105.141[.]172` | BO | AXS Bolivia S. A. | **100** ⚠️ | 50 |
| `178.178.222[.]47` | RU | PJSC MegaFon | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 31 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (25.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 18 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-27T20:36:28Z_
