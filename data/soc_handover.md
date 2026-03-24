# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T08:51:24Z |
| **Shift Time** | 08:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **155** |
| Confirmed Threats | **15** |
| False Positives Filtered | **140** (90.3%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **15** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **90** |
| Unique Usernames | **9** |
| Unique Passwords | **90** |
| Successful Auth Pairs | **80** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 80 |
| `admin` | 2 |
| `Centos` | 2 |
| `mysql` | 1 |
| `ubnt` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `server` | 1 |
| `Admin123` | 1 |
| `git` | 1 |
| `linux` | 1 |
| `111` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `server` | 1 |
| `root` | `Admin123` | 1 |
| `root` | `git` | 1 |
| `root` | `linux` | 1 |
| `root` | `111` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `server` | `64.236.176.194` | 2026-03-24T07:02:29 |
| `root` | `Admin123` | `64.236.176.194` | 2026-03-24T07:03:49 |
| `root` | `git` | `64.236.176.194` | 2026-03-24T07:05:10 |
| `root` | `linux` | `64.236.176.194` | 2026-03-24T07:06:29 |
| `root` | `111` | `64.236.176.194` | 2026-03-24T07:07:47 |
| `root` | `nginx` | `64.236.176.194` | 2026-03-24T07:09:07 |
| `root` | `passwd` | `64.236.176.194` | 2026-03-24T07:10:25 |
| `root` | `a` | `64.236.176.194` | 2026-03-24T07:11:45 |
| `root` | `P@ssword` | `64.236.176.194` | 2026-03-24T07:13:06 |
| `root` | `root@123` | `64.236.176.194` | 2026-03-24T07:14:28 |
| `root` | `n8n` | `64.236.176.194` | 2026-03-24T07:15:50 |
| `root` | `q1w2e3r4` | `64.236.176.194` | 2026-03-24T07:17:12 |
| `root` | `alpine` | `64.236.176.194` | 2026-03-24T07:18:33 |
| `root` | `rootroot` | `64.236.176.194` | 2026-03-24T07:19:54 |
| `root` | `1qaz!QAZ` | `64.236.176.194` | 2026-03-24T07:21:14 |
| `root` | `hadoop` | `64.236.176.194` | 2026-03-24T07:22:33 |
| `root` | `test1` | `64.236.176.194` | 2026-03-24T07:23:52 |
| `root` | `euler` | `64.236.176.194` | 2026-03-24T07:25:13 |
| `root` | `staking` | `64.236.176.194` | 2026-03-24T07:26:31 |
| `root` | `testuser` | `64.236.176.194` | 2026-03-24T07:27:52 |
| `root` | `password123` | `64.236.176.194` | 2026-03-24T07:29:16 |
| `root` | `ALC#FGU` | `64.236.176.194` | 2026-03-24T07:30:40 |
| `root` | `jenkins` | `64.236.176.194` | 2026-03-24T07:32:01 |
| `root` | `Password` | `64.236.176.194` | 2026-03-24T07:33:24 |
| `root` | `123123123` | `64.236.176.194` | 2026-03-24T07:34:48 |
| `root` | `system` | `64.236.176.194` | 2026-03-24T07:36:12 |
| `root` | `eth` | `64.236.176.194` | 2026-03-24T07:37:34 |
| `root` | `abcd1234` | `64.236.176.194` | 2026-03-24T07:38:55 |
| `root` | `deploy` | `64.236.176.194` | 2026-03-24T07:40:15 |
| `root` | `user1` | `64.236.176.194` | 2026-03-24T07:41:36 |
| `root` | `ftpuser` | `64.236.176.194` | 2026-03-24T07:42:57 |
| `root` | `vps` | `64.236.176.194` | 2026-03-24T07:44:19 |
| `root` | `demo` | `64.236.176.194` | 2026-03-24T07:45:42 |
| `root` | `oracle123` | `64.236.176.194` | 2026-03-24T07:47:07 |
| `root` | `admin1` | `64.236.176.194` | 2026-03-24T07:48:31 |
| `root` | `Password1` | `64.236.176.194` | 2026-03-24T07:49:56 |
| `root` | `d` | `64.236.176.194` | 2026-03-24T07:51:19 |
| `root` | `1qazXSW@` | `64.236.176.194` | 2026-03-24T07:52:43 |
| `root` | `web` | `64.236.176.194` | 2026-03-24T07:54:07 |
| `root` | `Passw0rd` | `64.236.176.194` | 2026-03-24T07:55:28 |
| `root` | `root1234` | `64.236.176.194` | 2026-03-24T07:56:48 |
| `root` | `dev` | `64.236.176.194` | 2026-03-24T07:58:09 |
| `root` | `s` | `64.236.176.194` | 2026-03-24T07:59:31 |
| `root` | `qwerty123456` | `64.236.176.194` | 2026-03-24T08:00:56 |
| `root` | `elastic` | `64.236.176.194` | 2026-03-24T08:02:19 |
| `root` | `vagrant` | `64.236.176.194` | 2026-03-24T08:03:42 |
| `root` | `steam` | `64.236.176.194` | 2026-03-24T08:05:05 |
| `root` | `ubuntu123` | `64.236.176.194` | 2026-03-24T08:06:28 |
| `root` | `m` | `64.236.176.194` | 2026-03-24T08:07:52 |
| `root` | `aA123456` | `64.236.176.194` | 2026-03-24T08:09:15 |
| `root` | `p` | `64.236.176.194` | 2026-03-24T08:10:37 |
| `root` | `kali` | `64.236.176.194` | 2026-03-24T08:11:59 |
| `root` | `weblogic` | `64.236.176.194` | 2026-03-24T08:13:23 |
| `root` | `0` | `64.236.176.194` | 2026-03-24T08:14:45 |
| `root` | `orangepi` | `64.236.176.194` | 2026-03-24T08:16:09 |
| `root` | `uftp` | `64.236.176.194` | 2026-03-24T08:17:34 |
| `root` | `0000` | `64.236.176.194` | 2026-03-24T08:18:59 |
| `root` | `21` | `64.236.176.194` | 2026-03-24T08:20:26 |
| `root` | `!QAZ@WSX` | `64.236.176.194` | 2026-03-24T08:21:48 |
| `root` | `ftp` | `64.236.176.194` | 2026-03-24T08:23:11 |
| `root` | `root1` | `64.236.176.194` | 2026-03-24T08:24:36 |
| `root` | `support` | `64.236.176.194` | 2026-03-24T08:25:59 |
| `root` | `zabbix` | `64.236.176.194` | 2026-03-24T08:27:19 |
| `root` | `g` | `64.236.176.194` | 2026-03-24T08:28:40 |
| `root` | `!@#$%^` | `64.236.176.194` | 2026-03-24T08:29:59 |
| `root` | `P@55w0rd` | `64.236.176.194` | 2026-03-24T08:31:23 |
| `root` | `sysadmin` | `64.236.176.194` | 2026-03-24T08:32:48 |
| `root` | `aaa` | `64.236.176.194` | 2026-03-24T08:34:11 |
| `root` | `adminadmin` | `64.236.176.194` | 2026-03-24T08:35:34 |
| `root` | `1qazxsw2` | `64.236.176.194` | 2026-03-24T08:36:59 |
| `root` | `master` | `64.236.176.194` | 2026-03-24T08:38:25 |
| `root` | `FAqY7=MZk66k-ob3Rmk` | `64.236.176.194` | 2026-03-24T08:39:51 |
| `root` | `Qwerty` | `64.236.176.194` | 2026-03-24T08:41:13 |
| `root` | `app123` | `64.236.176.194` | 2026-03-24T08:42:33 |
| `root` | `elasticsearch` | `64.236.176.194` | 2026-03-24T08:43:54 |
| `root` | `postgres123` | `64.236.176.194` | 2026-03-24T08:45:14 |
| `root` | `Aa123123` | `64.236.176.194` | 2026-03-24T08:46:36 |
| `root` | `shred` | `64.236.176.194` | 2026-03-24T08:47:57 |
| `root` | `P` | `64.236.176.194` | 2026-03-24T08:49:18 |
| `root` | `root123456` | `64.236.176.194` | 2026-03-24T08:50:43 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **26** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS10030` | Celcom Axiata Berhad | 1 | HIGH |
| `AS28370` | GUIFAMI Informática Ltda. | 1 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS26666` | Interserver, Inc | 1 | LOW |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | LOW |
| `AS13280` | Three Ireland (Hutchison) limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `18.218.168[.]5` | **3** | 2026-03-24 08:03 | 2026-03-24 08:03 | 0m | 0 | `T1592` | 🟢 LOW |
| `124.123.77[.]62` | **2** | 2026-03-24 07:29 | 2026-03-24 08:43 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.235.199[.]67` | 1 | 2026-03-24 08:08 | 2026-03-24 08:08 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.158.200[.]53` | 1 | 2026-03-24 07:48 | 2026-03-24 07:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `113.215.47[.]156` | 1 | 2026-03-24 07:47 | 2026-03-24 07:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-03-24 07:24 | 2026-03-24 07:25 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.78.28[.]55` | 1 | 2026-03-24 08:02 | 2026-03-24 08:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-03-24 07:44 | 2026-03-24 07:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `46.210.95[.]88` | 1 | 2026-03-24 07:32 | 2026-03-24 07:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]17` | 1 | 2026-03-24 07:13 | 2026-03-24 07:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-24 08:30 | 2026-03-24 08:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `80.233.12[.]109` | 1 | 2026-03-24 08:49 | 2026-03-24 08:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `46.210.95[.]88` | IL | Cellcom Fixed Line Communication L.P | **100** ⚠️ | 19 |
| `178.78.28[.]55` | RU | JSC ER-Telecom Holding Krasnodar branch | **100** ⚠️ | 7 |
| `80.233.12[.]109` | IE | Three Ireland (Hutchison) limited | **100** ⚠️ | 36 |
| `118.123.116[.]93` | CN | CHINANET Sichuan province network | **100** ⚠️ | 28 |
| `183.171.15[.]149` | MY | Celcom Axiata Berhad | **100** ⚠️ | 6 |
| `113.215.47[.]156` | CN | Huashu media&Network Limited | **100** ⚠️ | 2 |
| `101.235.199[.]67` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 19 |
| `124.123.77[.]62` | IN | ACT Hyderabad | **100** ⚠️ | 1 |
| `49.124.153[.]17` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 13 |
| `112.158.200[.]53` | KR | LG POWERCOMM | **100** ⚠️ | 24 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 94 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 24 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1057](https://attack.mitre.org/techniques/T1057) | 10 |

---

## 🔕 False Positive Summary (140 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 18 below threshold 25 | 80 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 25 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 155 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 15 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 140 filtered (90.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 12 recon entry/entries in table (2 group(s) consolidating 5 session(s)).

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
_Report time: 2026-03-24T08:51:24Z_
