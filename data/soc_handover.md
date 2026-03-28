# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T18:37:56Z |
| **Shift Time** | 18:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **36** |
| Confirmed Threats | **28** |
| False Positives Filtered | **8** (22.2%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **14** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **33** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **19** |
| Unique Usernames | **13** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `admin` | 2 |
| `user` | 2 |
| `config` | 2 |
| `supervisor` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `maintenance` | 2 |
| `66666` | 1 |
| `administrator` | 1 |
| `admin2019` | 1 |
| `121212` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `maintenance` | 2 |
| `guest` | `66666` | 1 |
| `centos` | `administrator` | 1 |
| `admin` | `admin2019` | 1 |
| `user` | `121212` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `maintenance` | `103.118.150.139` | 2026-03-28T17:02:02 |
| `root` | `maintenance` | `182.227.214.33` | 2026-03-28T17:02:09 |
| `root` | `warmWLspot` | `86.50.116.224` | 2026-03-28T17:45:58 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **28** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS29518` | Bredband2 AB | 1 | MEDIUM |
| `AS1741` | CSC - Tieteen tietotekniikan keskus Oy | 1 | MEDIUM |
| `AS6327` | Shaw Communications | 1 | MEDIUM |
| `AS138754` | Kerala Vision Broad Band Private Limited | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a79ce8dafe3b

| Field | Detail |
|---|---|
| **Source IP** | `103.118.150[.]139` |
| **First Seen** | 2026-03-28 17:02 |
| **Last Seen** | 2026-03-28 17:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 17:02:00` | `cowrie.session.connect` |
| `2026-03-28 17:02:01` | `cowrie.client.version` |
| `2026-03-28 17:02:01` | `cowrie.client.kex` |
| `2026-03-28 17:02:02` | `cowrie.login.success` |
| `2026-03-28 17:02:02` | `cowrie.direct-tcpip.request` |
| `2026-03-28 17:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.118.150[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.118.150[.]139` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39efbd34f35b

| Field | Detail |
|---|---|
| **Source IP** | `182.227.214[.]33` |
| **First Seen** | 2026-03-28 17:02 |
| **Last Seen** | 2026-03-28 17:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 17:02:07` | `cowrie.session.connect` |
| `2026-03-28 17:02:08` | `cowrie.client.version` |
| `2026-03-28 17:02:08` | `cowrie.client.kex` |
| `2026-03-28 17:02:09` | `cowrie.login.success` |
| `2026-03-28 17:02:10` | `cowrie.direct-tcpip.request` |
| `2026-03-28 17:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.227.214[.]33` to AbuseIPDB if not already reported
- [ ] Block `182.227.214[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42301ccdca8

| Field | Detail |
|---|---|
| **Source IP** | `86.50.116[.]224` |
| **First Seen** | 2026-03-28 17:45 |
| **Last Seen** | 2026-03-28 17:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 17:45:56` | `cowrie.session.connect` |
| `2026-03-28 17:45:57` | `cowrie.client.version` |
| `2026-03-28 17:45:57` | `cowrie.client.kex` |
| `2026-03-28 17:45:58` | `cowrie.login.success` |
| `2026-03-28 17:45:58` | `cowrie.direct-tcpip.request` |
| `2026-03-28 17:46:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.50.116[.]224` to AbuseIPDB if not already reported
- [ ] Block `86.50.116[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `150.246.249[.]149` | **3** | 2026-03-28 16:33 | 2026-03-28 18:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `64.227.99[.]138` | **2** | 2026-03-28 16:59 | 2026-03-28 16:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.248.250[.]143` | **2** | 2026-03-28 17:41 | 2026-03-28 18:01 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.220.91[.]138` | 1 | 2026-03-28 17:21 | 2026-03-28 17:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.53.70[.]99` | 1 | 2026-03-28 16:35 | 2026-03-28 16:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.200.216[.]246` | 1 | 2026-03-28 17:41 | 2026-03-28 17:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.220.250[.]167` | 1 | 2026-03-28 17:31 | 2026-03-28 17:32 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.107.185[.]138` | 1 | 2026-03-28 17:50 | 2026-03-28 17:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.227.193[.]21` | 1 | 2026-03-28 17:22 | 2026-03-28 17:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `148.64.107[.]221` | 1 | 2026-03-28 16:44 | 2026-03-28 16:44 | 32s | 0 | `T1592` | 🟢 LOW |
| `173.9.9[.]142` | 1 | 2026-03-28 16:42 | 2026-03-28 16:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.1.36[.]218` | 1 | 2026-03-28 18:25 | 2026-03-28 18:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.93.165[.]103` | 1 | 2026-03-28 18:28 | 2026-03-28 18:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.149.108[.]67` | 1 | 2026-03-28 18:09 | 2026-03-28 18:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.39.74[.]26` | 1 | 2026-03-28 16:54 | 2026-03-28 16:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.94.115[.]164` | 1 | 2026-03-28 17:02 | 2026-03-28 17:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.185.89[.]241` | 1 | 2026-03-28 16:46 | 2026-03-28 16:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.158.142[.]145` | 1 | 2026-03-28 16:42 | 2026-03-28 16:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-03-28 16:42 | 2026-03-28 16:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]70` | 1 | 2026-03-28 16:37 | 2026-03-28 16:38 | 15s | 0 | `T1592` | 🟢 LOW |
| `97.113.167[.]222` | 1 | 2026-03-28 18:21 | 2026-03-28 18:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `218.94.115[.]164` | CN | Nanjing Yindu Advertising Business Co., Ltd | **100** ⚠️ | 50 |
| `103.220.91[.]138` | IN | Mft Internet Private Limited | **100** ⚠️ | 36 |
| `173.9.9[.]142` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 6 |
| `124.227.193[.]21` | CN | CHINANET Guangxi province network | **100** ⚠️ | 43 |
| `124.107.185[.]138` | PH | IPG | **100** ⚠️ | 8 |
| `50.223.176[.]171` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `49.158.142[.]145` | TW | TFN MEDIA CO., LTD. | **100** ⚠️ | 3 |
| `64.227.99[.]138` | US | DigitalOcean, LLC | **100** ⚠️ | 16 |
| `113.200.216[.]246` | CN | China Unicom Shannxi Province Network | **100** ⚠️ | 27 |
| `120.220.250[.]167` | CN | China Mobile Communications Corporation | **100** ⚠️ | 31 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 23 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 36 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (22.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 21 recon entry/entries in table (3 group(s) consolidating 7 session(s)).

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
_Report time: 2026-03-28T18:37:56Z_
