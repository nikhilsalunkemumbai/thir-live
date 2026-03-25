# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T13:05:02Z |
| **Shift Time** | 13:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **30** |
| Confirmed Threats | **21** |
| False Positives Filtered | **9** (30.0%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **13** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **28** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **15** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `me` | 1 |
| `snake` | 1 |
| `admin` | 1 |
| `postgres` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `me` | 1 |
| `snake` | 1 |
| `windows` | 1 |
| `maintenance` | 1 |
| `p@ssword` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `me` | `me` | 1 |
| `snake` | `snake` | 1 |
| `admin` | `windows` | 1 |
| `postgres` | `maintenance` | 1 |
| `Nobody` | `p@ssword` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `user` | `37.157.219.158` | 2026-03-25T11:09:26 |
| `root` | `Password01` | `183.109.153.176` | 2026-03-25T12:00:15 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox GVLAD
```
Source IPs: `37.157.219.158`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **21** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS44395` | Ucom CJSC | 1 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | MEDIUM |
| `AS37457` | Telkom SA Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b7811a5f3959

| Field | Detail |
|---|---|
| **Source IP** | `37.157.219[.]158` |
| **First Seen** | 2026-03-25 11:09 |
| **Last Seen** | 2026-03-25 11:11 |
| **Session Duration** | 102s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox GVLAD` |
| **Download Attempts** | tfxxp://37.157.219[.]158:16470/.i |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 11:09:25` | `cowrie.session.connect` |
| `2026-03-25 11:09:26` | `cowrie.telnet.option` |
| `2026-03-25 11:09:26` | `cowrie.login.success` |
| `2026-03-25 11:09:26` | `cowrie.session.params` |
| `2026-03-25 11:09:26` | `cowrie.command.input` |
| `2026-03-25 11:09:26` | `cowrie.command.input` |
| `2026-03-25 11:09:26` | `cowrie.command.failed` |
| `2026-03-25 11:09:26` | `cowrie.command.input` |
| `2026-03-25 11:09:26` | `cowrie.command.failed` |
| `2026-03-25 11:09:26` | `cowrie.command.input` |
| `2026-03-25 11:09:27` | `cowrie.command.input` |
| `2026-03-25 11:09:27` | `cowrie.command.input` |
| `2026-03-25 11:09:27` | `cowrie.command.input` |
| `2026-03-25 11:09:27` | `cowrie.command.input` |
| `2026-03-25 11:09:27` | `cowrie.command.failed` |
| `2026-03-25 11:09:28` | `cowrie.command.input` |
| `2026-03-25 11:09:28` | `cowrie.command.input` |
| `2026-03-25 11:10:04` | `cowrie.session.file_download` |
| `2026-03-25 11:11:08` | `cowrie.log.closed` |
| `2026-03-25 11:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.157.219[.]158` to AbuseIPDB if not already reported
- [ ] Block `37.157.219[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef4d5abe5f9a

| Field | Detail |
|---|---|
| **Source IP** | `183.109.153[.]176` |
| **First Seen** | 2026-03-25 12:00 |
| **Last Seen** | 2026-03-25 12:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 12:00:12` | `cowrie.session.connect` |
| `2026-03-25 12:00:13` | `cowrie.client.version` |
| `2026-03-25 12:00:13` | `cowrie.client.kex` |
| `2026-03-25 12:00:15` | `cowrie.login.success` |
| `2026-03-25 12:00:16` | `cowrie.direct-tcpip.request` |
| `2026-03-25 12:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.109.153[.]176` to AbuseIPDB if not already reported
- [ ] Block `183.109.153[.]176` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.23.104[.]96` | **3** | 2026-03-25 11:48 | 2026-03-25 11:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.158.22[.]150` | **2** | 2026-03-25 11:53 | 2026-03-25 11:57 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `34.133.99[.]235` | **2** | 2026-03-25 10:46 | 2026-03-25 10:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `105.186.160[.]30` | 1 | 2026-03-25 10:51 | 2026-03-25 10:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.102.48[.]129` | 1 | 2026-03-25 11:30 | 2026-03-25 11:30 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.201.59[.]224` | 1 | 2026-03-25 11:18 | 2026-03-25 11:18 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.38[.]223` | 1 | 2026-03-25 13:03 | 2026-03-25 13:03 | 4s | 0 | `T1592` | 🟢 LOW |
| `13.222.169[.]249` | 1 | 2026-03-25 12:53 | 2026-03-25 12:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `186.215.204[.]109` | 1 | 2026-03-25 11:08 | 2026-03-25 11:08 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.208.209[.]215` | 1 | 2026-03-25 12:19 | 2026-03-25 12:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.92.189[.]112` | 1 | 2026-03-25 12:28 | 2026-03-25 12:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `221.206.7[.]126` | 1 | 2026-03-25 12:21 | 2026-03-25 12:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]32` | 1 | 2026-03-25 11:50 | 2026-03-25 11:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.22.255[.]28` | 1 | 2026-03-25 12:06 | 2026-03-25 12:06 | 11s | 0 | `T1592` | 🟢 LOW |
| `85.159.165[.]216` | 1 | 2026-03-25 10:55 | 2026-03-25 10:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `49.124.153[.]32` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 21 |
| `221.206.7[.]126` | CN | China Unicom Heilongjiang Province Network | **100** ⚠️ | 13 |
| `13.222.169[.]249` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 11 |
| `120.48.38[.]223` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 13 |
| `34.133.99[.]235` | US | Google LLC | **100** ⚠️ | 5 |
| `186.215.204[.]109` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 0 |
| `3.23.104[.]96` | US | Amazon Technologies Inc. | **100** ⚠️ | 0 |
| `112.102.48[.]129` | CN | CHINANET HEILONGJIANG PROVINCE NETWORK | **100** ⚠️ | 0 |
| `185.158.22[.]150` | IQ | Trade Link Logistics General Trading & Contracting Company W.L.L., L.L.C. | **100** ⚠️ | 0 |
| `58.22.255[.]28` | CN | Longyan city, fujian provincial network of CNCGROUP | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 16 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 30 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (30.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 15 recon entry/entries in table (3 group(s) consolidating 7 session(s)).

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
_Report time: 2026-03-25T13:05:02Z_
