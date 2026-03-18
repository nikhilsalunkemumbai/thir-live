# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-18 |
| **Generated At** | 2026-03-18T20:38:17Z |
| **Shift Time** | 20:38 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1222** |
| Confirmed Threats | **0** |
| False Positives Filtered | **1222** (100.0%) |
| Unique Attacker IPs | **242** |
| Countries of Origin | **0** |
| High Severity Cases | **106** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1116** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **596** |
| Unique Credential Pairs | **510** |
| Unique Usernames | **311** |
| Unique Passwords | **351** |
| Successful Auth Pairs | **99** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 113 |
| `345gs5662d34` | 22 |
| `admin` | 21 |
| `ubuntu` | 16 |
| `user` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 52 |
| `345gs5662d34` | 22 |
| `1234` | 21 |
| `3245gs5662d34` | 21 |
| `123` | 20 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 21 |
| `root` | `` | 6 |
| `admin` | `admin` | 5 |
| `root` | `ubuntu` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `147.189.161.77` | 2026-03-18T00:05:03 |
| `root` | `Admin1235` | `183.81.33.183` | 2026-03-18T00:08:28 |
| `root` | `66666` | `61.145.163.164` | 2026-03-18T00:09:57 |
| `root` | `66666` | `197.155.225.93` | 2026-03-18T00:10:11 |
| `root` | `admin@123` | `143.244.146.173` | 2026-03-18T00:13:54 |
| `root` | `1` | `143.244.146.173` | 2026-03-18T00:14:26 |
| `root` | `QWERTY123` | `143.244.146.173` | 2026-03-18T00:14:59 |
| `root` | `Pass@123` | `143.244.146.173` | 2026-03-18T00:15:18 |
| `root` | `!Q@W3e4r` | `143.244.146.173` | 2026-03-18T00:15:24 |
| `root` | `Admin1236` | `183.81.33.183` | 2026-03-18T00:24:25 |
| `root` | `Admin1237` | `183.81.33.183` | 2026-03-18T00:41:56 |
| `root` | `server123` | `120.48.174.68` | 2026-03-18T00:43:29 |
| `root` | `Admin1238` | `183.81.33.183` | 2026-03-18T00:58:35 |
| `root` | `admin` | `116.110.23.141` | 2026-03-18T01:02:08 |
| `root` | `Admin1239` | `183.81.33.183` | 2026-03-18T01:14:32 |
| `root` | `Admin12310` | `183.81.33.183` | 2026-03-18T01:30:07 |
| `root` | `explorer` | `116.110.156.14` | 2026-03-18T01:32:28 |
| `root` | `Admin12340` | `183.81.33.183` | 2026-03-18T01:47:37 |
| `root` | `a1s2d3f4` | `137.184.78.9` | 2026-03-18T02:03:40 |
| `root` | `Qq123456` | `137.184.78.9` | 2026-03-18T02:03:53 |
| `root` | `!QAZ2wsx` | `137.184.78.9` | 2026-03-18T02:04:07 |
| `root` | `root12345` | `137.184.78.9` | 2026-03-18T02:04:47 |
| `root` | `passwd` | `137.184.78.9` | 2026-03-18T02:05:07 |
| `root` | `123321` | `137.184.78.9` | 2026-03-18T02:05:27 |
| `root` | `Aa123456.` | `137.184.78.9` | 2026-03-18T02:06:06 |
| `root` | `Abc123456` | `137.184.78.9` | 2026-03-18T02:06:26 |
| `root` | `201314` | `101.36.106.113` | 2026-03-18T03:24:41 |
| `root` | `3245gs5662d34` | `101.36.106.113` | 2026-03-18T03:24:44 |
| `root` | `ubuntu` | `219.153.106.29` | 2026-03-18T04:12:51 |
| `root` | `qwer!234` | `180.76.245.60` | 2026-03-18T05:04:43 |
| `root` | `lj123456` | `103.7.41.144` | 2026-03-18T06:12:24 |
| `root` | `3245gs5662d34` | `103.7.41.144` | 2026-03-18T06:12:27 |
| `root` | `QWERTY123` | `174.138.33.218` | 2026-03-18T06:41:35 |
| `root` | `1` | `174.138.33.218` | 2026-03-18T06:41:48 |
| `root` | `12345678` | `174.138.33.218` | 2026-03-18T06:42:14 |
| `root` | `P@ssw0rd2026` | `174.138.33.218` | 2026-03-18T06:42:39 |
| `root` | `root@2026` | `174.138.33.218` | 2026-03-18T06:42:52 |
| `root` | `redhat` | `174.138.33.218` | 2026-03-18T06:43:43 |
| `root` | `qazwsx123` | `174.138.33.218` | 2026-03-18T06:44:09 |
| `root` | `Admin123` | `174.138.33.218` | 2026-03-18T06:44:27 |
| `root` | `11` | `174.138.33.218` | 2026-03-18T06:44:53 |
| `root` | `Qwerty1` | `174.138.33.218` | 2026-03-18T06:45:05 |
| `root` | `Password` | `174.138.33.218` | 2026-03-18T06:45:49 |
| `root` | `eve` | `174.138.33.218` | 2026-03-18T06:47:05 |
| `root` | `ubuntu` | `41.111.172.2` | 2026-03-18T06:54:08 |
| `root` | `Welcome@2024` | `95.70.212.76` | 2026-03-18T07:57:09 |
| `root` | `3245gs5662d34` | `95.70.212.76` | 2026-03-18T07:57:14 |
| `root` | `nigger` | `186.4.240.226` | 2026-03-18T07:58:01 |
| `root` | `3245gs5662d34` | `186.4.240.226` | 2026-03-18T07:58:08 |
| `root` | `1q2w3e4r5t6y7u` | `95.70.212.76` | 2026-03-18T08:05:04 |
| `root` | `6666` | `90.173.78.90` | 2026-03-18T09:04:47 |
| `root` | `qwer1234QWER` | `120.62.8.17` | 2026-03-18T10:47:34 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-03-18T10:47:36 |
| `root` | `Lm123456` | `197.248.8.33` | 2026-03-18T10:48:24 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-03-18T10:48:29 |
| `root` | `Lai123456` | `197.248.8.33` | 2026-03-18T10:55:07 |
| `root` | `Aa@13579` | `197.248.8.33` | 2026-03-18T10:56:01 |
| `root` | `a111222` | `177.92.51.57` | 2026-03-18T11:00:57 |
| `root` | `3245gs5662d34` | `177.92.51.57` | 2026-03-18T11:01:04 |
| `root` | `root@123` | `177.92.51.57` | 2026-03-18T11:16:33 |
| `root` | `Aa123123` | `103.237.144.204` | 2026-03-18T11:18:47 |
| `root` | `3245gs5662d34` | `103.237.144.204` | 2026-03-18T11:18:52 |
| `root` | `rootroot` | `157.245.94.161` | 2026-03-18T11:34:19 |
| `root` | `pass` | `157.245.94.161` | 2026-03-18T11:34:33 |
| `root` | `aA123456` | `157.245.94.161` | 2026-03-18T11:34:47 |
| `root` | `Admin@123456` | `157.245.94.161` | 2026-03-18T11:34:53 |
| `root` | `redhat` | `157.245.94.161` | 2026-03-18T11:35:06 |
| `root` | `11` | `157.245.94.161` | 2026-03-18T11:35:39 |
| `root` | `passw0rd` | `157.245.94.161` | 2026-03-18T11:36:12 |
| `root` | `Root@123` | `157.245.94.161` | 2026-03-18T11:36:32 |
| `root` | `qq123456` | `157.245.94.161` | 2026-03-18T11:36:38 |
| `root` | `123abc456` | `157.245.94.161` | 2026-03-18T11:36:51 |
| `root` | `Pass@123` | `157.245.94.161` | 2026-03-18T11:37:31 |
| `root` | `12345qwert` | `157.245.94.161` | 2026-03-18T11:37:58 |
| `root` | `debian` | `180.76.175.142` | 2026-03-18T11:46:12 |
| `root` | `!Aa123456` | `43.100.77.140` | 2026-03-18T12:23:09 |
| `root` | `3245gs5662d34` | `43.100.77.140` | 2026-03-18T12:23:12 |
| `root` | `abc123$%^` | `43.100.77.140` | 2026-03-18T12:30:49 |
| `root` | `!Qaz@Wsx` | `67.205.184.189` | 2026-03-18T14:28:19 |
| `root` | `null` | `67.205.184.189` | 2026-03-18T14:28:26 |
| `root` | `123abc456` | `67.205.184.189` | 2026-03-18T14:29:38 |
| `root` | `admin@123` | `112.194.142.167` | 2026-03-18T14:43:10 |
| `root` | `11221122` | `103.153.190.105` | 2026-03-18T14:56:16 |
| `root` | `3245gs5662d34` | `103.153.190.105` | 2026-03-18T14:56:19 |
| `root` | `root2023` | `114.98.63.18` | 2026-03-18T15:38:55 |
| `root` | `Aa@112233` | `179.32.33.161` | 2026-03-18T15:39:25 |
| `root` | `3245gs5662d34` | `179.32.33.161` | 2026-03-18T15:39:32 |
| `root` | `abc123456.` | `180.167.96.50` | 2026-03-18T15:42:57 |
| `root` | `Welkom01` | `113.137.40.250` | 2026-03-18T15:43:40 |
| `root` | `3245gs5662d34` | `113.137.40.250` | 2026-03-18T15:43:45 |
| `root` | `Aa147258` | `34.135.200.178` | 2026-03-18T18:22:15 |
| `root` | `3245gs5662d34` | `34.135.200.178` | 2026-03-18T18:22:21 |
| `root` | `root@2019` | `183.91.11.36` | 2026-03-18T18:47:06 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-03-18T18:47:09 |
| `root` | `Windows10` | `183.91.11.36` | 2026-03-18T18:49:36 |
| `root` | `qwerty1234` | `35.130.111.146` | 2026-03-18T18:56:03 |
| `root` | `qwerty1234` | `103.220.91.138` | 2026-03-18T18:56:10 |
| `root` | `secretpassxd` | `103.153.190.105` | 2026-03-18T19:48:50 |
| `root` | `$BLANKPASS` | `113.192.60.129` | 2026-03-18T20:36:36 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **242** |
| Unique ASNs | **107** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 13 | LOW |
| `AS22773` | Cox Communications Inc. | 13 | LOW |
| `AS4134` | CHINANET-BACKBONE | 13 | LOW |
| `AS46562` | Performive LLC | 11 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 10 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 8 | LOW |
| `AS14061` | DigitalOcean, LLC | 7 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 6 | LOW |

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

_No reconnaissance sessions this shift._

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
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

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 701 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 483 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 106 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |

---

## 🔕 False Positive Summary (1222 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1222 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1222 cases |
| Tool 34  | Credential Extractor        | ✅ 596 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 242 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1222 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 107 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-18T20:38:17Z_
