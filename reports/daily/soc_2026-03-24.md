# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T14:56:07Z |
| **Shift Time** | 14:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **27** |
| Confirmed Threats | **21** |
| False Positives Filtered | **6** (22.2%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **14** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **9** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `admin` | 2 |
| `centos` | 2 |
| `default` | 2 |
| `Debian` | 1 |
| `pi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `c1@r0` | 1 |
| `12345678` | 1 |
| `P@ssw0rd` | 1 |
| `admin2022` | 1 |
| `centos2025` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `c1@r0` | 1 |
| `Debian` | `12345678` | 1 |
| `pi` | `P@ssw0rd` | 1 |
| `admin` | `admin2022` | 1 |
| `centos` | `centos2025` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qw123123` | `47.83.161.4` | 2026-03-24T13:33:45 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **23** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | LOW |
| `AS205254` | Valeen for General trading, Internet Services and Information Technology / Ltd | 1 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS719` | Elisa Oyj | 1 | LOW |
| `AS10429` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3f7489a5e781

| Field | Detail |
|---|---|
| **Source IP** | `47.83.161[.]4` |
| **First Seen** | 2026-03-24 13:33 |
| **Last Seen** | 2026-03-24 13:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `ls -la /` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 13:33:40` | `cowrie.session.connect` |
| `2026-03-24 13:33:40` | `cowrie.client.version` |
| `2026-03-24 13:33:40` | `cowrie.client.kex` |
| `2026-03-24 13:33:45` | `cowrie.login.success` |
| `2026-03-24 13:33:46` | `cowrie.session.params` |
| `2026-03-24 13:33:46` | `cowrie.command.input` |
| `2026-03-24 13:33:47` | `cowrie.log.closed` |
| `2026-03-24 13:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.161[.]4` to AbuseIPDB if not already reported
- [ ] Block `47.83.161[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.97.104[.]10` | **3** | 2026-03-24 13:06 | 2026-03-24 14:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.13.4[.]124` | 1 | 2026-03-24 13:14 | 2026-03-24 13:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.36.88[.]169` | 1 | 2026-03-24 13:32 | 2026-03-24 13:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.91.214[.]71` | 1 | 2026-03-24 13:25 | 2026-03-24 13:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.157.83[.]35` | 1 | 2026-03-24 13:10 | 2026-03-24 13:10 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.160.255[.]46` | 1 | 2026-03-24 13:30 | 2026-03-24 13:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.194[.]22` | 1 | 2026-03-24 13:41 | 2026-03-24 13:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-24 14:17 | 2026-03-24 14:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.71.9[.]31` | 1 | 2026-03-24 14:29 | 2026-03-24 14:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-03-24 14:04 | 2026-03-24 14:04 | 4s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]9` | 1 | 2026-03-24 13:17 | 2026-03-24 13:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.255.47[.]190` | 1 | 2026-03-24 14:42 | 2026-03-24 14:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-24 14:09 | 2026-03-24 14:10 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.109.205[.]160` | 1 | 2026-03-24 13:31 | 2026-03-24 13:31 | 12s | 0 | `T1592` | 🟢 LOW |
| `47.83.161[.]4` | 1 | 2026-03-24 13:31 | 2026-03-24 13:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]14` | 1 | 2026-03-24 13:12 | 2026-03-24 13:12 | 2s | 0 | `T1592` | 🟢 LOW |
| `58.58.122[.]14` | 1 | 2026-03-24 13:33 | 2026-03-24 13:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.2[.]19` | 1 | 2026-03-24 14:16 | 2026-03-24 14:17 | 49s | 0 | `T1592` | 🟢 LOW |

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
| `183.171.15[.]149` | MY | Celcom Axiata Berhad | **100** ⚠️ | 6 |
| `185.255.47[.]190` | IQ | Valeen for General trading, Internet Services and Information Technology / Ltd | **100** ⚠️ | 50 |
| `101.13.4[.]124` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 20 |
| `47.83.161[.]4` | HK | Alibaba Cloud LLC | **100** ⚠️ | 1 |
| `222.109.205[.]160` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `8.154.2[.]19` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 35 |
| `49.124.151[.]14` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 0 |
| `180.71.9[.]31` | KR | SK Broadband Co Ltd | **100** ⚠️ | 0 |
| `128.185.194[.]22` | IN | BHARTI-AIRTEL | **100** ⚠️ | 0 |
| `112.91.214[.]71` | CN | China Unicom Chaozhou city network, Leased line address | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 14 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 27 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (22.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 18 recon entry/entries in table (1 group(s) consolidating 3 session(s)).

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
_Report time: 2026-03-24T14:56:07Z_
