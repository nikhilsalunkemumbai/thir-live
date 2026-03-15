# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-15 |
| **Generated At** | 2026-03-15T20:27:21Z |
| **Shift Time** | 20:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **792** |
| Confirmed Threats | **0** |
| False Positives Filtered | **792** (100.0%) |
| Unique Attacker IPs | **165** |
| Countries of Origin | **0** |
| High Severity Cases | **127** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **665** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **422** |
| Unique Credential Pairs | **322** |
| Unique Usernames | **204** |
| Unique Passwords | **216** |
| Successful Auth Pairs | **122** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 137 |
| `345gs5662d34` | 18 |
| `admin` | 15 |
| `pi` | 5 |
| `deploy` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 39 |
| `12345` | 21 |
| `password` | 20 |
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `root` | `123456` | 5 |
| `root` | `123456789` | 5 |
| `root` | `admin` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `167.71.132.83` | 2026-03-15T02:08:47 |
| `root` | `password` | `167.71.132.83` | 2026-03-15T02:09:35 |
| `root` | `admin` | `167.71.132.83` | 2026-03-15T02:10:54 |
| `root` | `12345` | `167.71.132.83` | 2026-03-15T02:11:56 |
| `root` | `1234` | `167.71.132.83` | 2026-03-15T02:13:09 |
| `root` | `Huawei@123#` | `118.194.230.250` | 2026-03-15T02:26:43 |
| `root` | `3245gs5662d34` | `118.194.230.250` | 2026-03-15T02:26:47 |
| `root` | `Devops123` | `118.194.230.250` | 2026-03-15T02:28:46 |
| `root` | `123456@Abc` | `101.52.130.122` | 2026-03-15T02:40:34 |
| `root` | `Aa@123123` | `105.27.148.94` | 2026-03-15T02:45:02 |
| `root` | `Aa@123123` | `189.152.42.213` | 2026-03-15T02:45:07 |
| `root` | `3245gs5662d34` | `105.27.148.94` | 2026-03-15T02:45:08 |
| `root` | `3245gs5662d34` | `189.152.42.213` | 2026-03-15T02:45:13 |
| `root` | `201314` | `179.183.192.58` | 2026-03-15T02:56:53 |
| `root` | `3245gs5662d34` | `179.183.192.58` | 2026-03-15T02:57:00 |
| `root` | `pippo123` | `118.193.36.245` | 2026-03-15T04:49:22 |
| `root` | `3245gs5662d34` | `118.193.36.245` | 2026-03-15T04:49:25 |
| `root` | `1qaz2wsx` | `206.189.138.45` | 2026-03-15T05:00:28 |
| `root` | `qwerty123456` | `206.189.138.45` | 2026-03-15T05:01:09 |
| `root` | `123456Q!` | `118.193.36.245` | 2026-03-15T05:01:27 |
| `root` | `!root` | `206.189.138.45` | 2026-03-15T05:01:48 |
| `root` | `root!@#` | `206.189.138.45` | 2026-03-15T05:02:28 |
| `root` | `P@ssw0rd2026` | `206.189.138.45` | 2026-03-15T05:03:06 |
| `root` | `Qwerty123456789` | `118.193.36.245` | 2026-03-15T05:03:28 |
| `root` | `Admin2026!` | `206.189.138.45` | 2026-03-15T05:03:44 |
| `root` | `root2026` | `206.189.138.45` | 2026-03-15T05:04:25 |
| `root` | `ZXCasd123` | `129.222.203.37` | 2026-03-15T05:07:37 |
| `root` | `3245gs5662d34` | `129.222.203.37` | 2026-03-15T05:07:45 |
| `root` | `1234567` | `172.210.53.192` | 2026-03-15T06:26:54 |
| `root` | `12345678` | `172.210.53.192` | 2026-03-15T06:41:08 |
| `root` | `123456789` | `172.210.53.192` | 2026-03-15T06:55:30 |
| `root` | `admin` | `46.101.119.234` | 2026-03-15T06:58:31 |
| `root` | `password` | `46.101.119.234` | 2026-03-15T06:59:18 |
| `root` | `toor` | `46.101.119.234` | 2026-03-15T07:00:52 |
| `root` | `qwerty` | `46.101.119.234` | 2026-03-15T07:01:40 |
| `root` | `12345` | `46.101.119.234` | 2026-03-15T07:02:32 |
| `root` | `root@123` | `172.210.53.192` | 2026-03-15T07:39:13 |
| `root` | `admin` | `161.35.170.148` | 2026-03-15T07:48:29 |
| `root` | `password` | `161.35.170.148` | 2026-03-15T07:49:32 |
| `root` | `123456789` | `161.35.170.148` | 2026-03-15T07:51:34 |
| `root` | `root@1234` | `172.210.53.192` | 2026-03-15T08:08:40 |
| `root` | `admin` | `172.210.53.192` | 2026-03-15T08:23:26 |
| `root` | `root123` | `165.22.214.235` | 2026-03-15T08:36:04 |
| `root` | `root321` | `165.22.214.235` | 2026-03-15T08:36:56 |
| `root` | `administrator` | `172.210.53.192` | 2026-03-15T08:53:03 |
| `root` | `Administrator` | `172.210.53.192` | 2026-03-15T09:07:53 |
| `root` | `Admin` | `172.210.53.192` | 2026-03-15T09:22:47 |
| `root` | `Hello123!` | `118.194.250.47` | 2026-03-15T09:26:54 |
| `root` | `3245gs5662d34` | `118.194.250.47` | 2026-03-15T09:26:57 |
| `root` | `admin1234` | `172.210.53.192` | 2026-03-15T09:37:46 |
| `root` | `Admin@123` | `103.95.13.221` | 2026-03-15T09:46:49 |
| `root` | `admin12345` | `172.210.53.192` | 2026-03-15T09:52:46 |
| `root` | `1` | `143.244.140.97` | 2026-03-15T09:56:54 |
| `root` | `12` | `143.244.140.97` | 2026-03-15T09:57:39 |
| `root` | `123` | `143.244.140.97` | 2026-03-15T09:58:23 |
| `root` | `1234` | `143.244.140.97` | 2026-03-15T09:59:07 |
| `root` | `12345` | `143.244.140.97` | 2026-03-15T09:59:51 |
| `root` | `Admin12345` | `172.210.53.192` | 2026-03-15T10:23:04 |
| `root` | `xmhdipc` | `112.81.45.208` | 2026-03-15T10:32:56 |
| `root` | `1234567890` | `167.99.95.73` | 2026-03-15T10:48:23 |
| `root` | `password1` | `167.99.95.73` | 2026-03-15T10:49:12 |
| `root` | `admin123` | `167.99.95.73` | 2026-03-15T10:50:00 |
| `root` | `1234` | `167.99.95.73` | 2026-03-15T10:51:08 |
| `root` | `123` | `167.99.95.73` | 2026-03-15T10:52:07 |
| `root` | `Admin@123` | `172.210.53.192` | 2026-03-15T10:53:30 |
| `root` | `administrator123` | `172.210.53.192` | 2026-03-15T11:08:42 |
| `root` | `Pass@123` | `104.248.59.8` | 2026-03-15T11:55:38 |
| `root` | `admin1234` | `104.248.59.8` | 2026-03-15T11:56:23 |
| `root` | `admin123` | `104.248.59.8` | 2026-03-15T11:56:44 |
| `root` | `ubuntu` | `104.248.59.8` | 2026-03-15T11:56:59 |
| `root` | `P@ssword` | `104.248.59.8` | 2026-03-15T11:57:20 |
| `root` | `123456789` | `104.248.59.8` | 2026-03-15T11:57:27 |
| `root` | `root@2026` | `104.248.59.8` | 2026-03-15T11:58:17 |
| `root` | `1qaz2wsx` | `143.110.244.207` | 2026-03-15T12:29:21 |
| `root` | `qwerty123456` | `143.110.244.207` | 2026-03-15T12:30:04 |
| `root` | `!root` | `143.110.244.207` | 2026-03-15T12:30:51 |
| `root` | `root!@#` | `143.110.244.207` | 2026-03-15T12:31:34 |
| `root` | `P@ssw0rd2026` | `143.110.244.207` | 2026-03-15T12:32:16 |
| `root` | `Admin2026!` | `143.110.244.207` | 2026-03-15T12:33:02 |
| `root` | `root2026` | `143.110.244.207` | 2026-03-15T12:33:49 |
| `root` | `1` | `64.227.132.19` | 2026-03-15T14:19:11 |
| `root` | `12` | `64.227.132.19` | 2026-03-15T14:20:01 |
| `root` | `123` | `64.227.132.19` | 2026-03-15T14:20:58 |
| `root` | `1234` | `64.227.132.19` | 2026-03-15T14:21:57 |
| `root` | `qwerty` | `68.183.29.199` | 2026-03-15T14:33:29 |
| `root` | `Pass1234` | `68.183.29.199` | 2026-03-15T14:34:13 |
| `root` | `123123` | `68.183.29.199` | 2026-03-15T14:35:22 |
| `root` | `12345qwert` | `68.183.29.199` | 2026-03-15T14:35:43 |
| `root` | `Admin@123456` | `68.183.29.199` | 2026-03-15T14:35:51 |
| `root` | `1234567890` | `68.183.29.199` | 2026-03-15T14:36:05 |
| `root` | `qq123456` | `68.183.29.199` | 2026-03-15T14:36:55 |
| `root` | `123456789aA` | `157.15.59.120` | 2026-03-15T14:37:09 |
| `root` | `abcd@1234` | `68.183.29.199` | 2026-03-15T14:37:10 |
| `root` | `3245gs5662d34` | `157.15.59.120` | 2026-03-15T14:37:11 |
| `root` | `12qwaszx` | `68.183.29.199` | 2026-03-15T14:37:31 |
| `root` | `Aa123456.` | `68.183.29.199` | 2026-03-15T14:39:48 |
| `root` | `password` | `157.245.70.163` | 2026-03-15T15:56:51 |
| `root` | `admin` | `157.245.70.163` | 2026-03-15T15:58:06 |
| `root` | `centos` | `124.239.153.90` | 2026-03-15T15:58:14 |
| `root` | `toor` | `157.245.70.163` | 2026-03-15T15:59:21 |
| `root` | `12345` | `157.245.70.163` | 2026-03-15T16:00:49 |
| `root` | `123456789` | `157.245.70.163` | 2026-03-15T16:02:06 |
| `root` | `dodol123` | `102.210.149.105` | 2026-03-15T16:08:54 |
| `root` | `3245gs5662d34` | `102.210.149.105` | 2026-03-15T16:08:58 |
| `root` | `Linux123` | `180.76.141.1` | 2026-03-15T16:36:16 |
| `root` | `Admin-12345` | `129.222.203.37` | 2026-03-15T16:37:58 |
| `root` | `Secure123` | `129.222.203.37` | 2026-03-15T16:38:58 |
| `root` | `Qwert12345` | `186.4.240.226` | 2026-03-15T16:42:17 |
| `root` | `3245gs5662d34` | `186.4.240.226` | 2026-03-15T16:42:24 |
| `root` | `Qazwsx123` | `112.184.119.22` | 2026-03-15T17:30:26 |
| `root` | `3245gs5662d34` | `112.184.119.22` | 2026-03-15T17:30:30 |
| `root` | `Zh123456.` | `103.158.132.160` | 2026-03-15T18:19:36 |
| `root` | `3245gs5662d34` | `103.158.132.160` | 2026-03-15T18:19:38 |
| `root` | `Qwert12` | `183.232.212.207` | 2026-03-15T20:00:45 |
| `root` | `3245gs5662d34` | `183.232.212.207` | 2026-03-15T20:00:51 |
| `root` | `root1` | `68.183.91.110` | 2026-03-15T20:08:29 |
| `root` | `root12` | `68.183.91.110` | 2026-03-15T20:09:13 |
| `root` | `root123` | `68.183.91.110` | 2026-03-15T20:09:59 |
| `root` | `123qwe` | `68.183.91.110` | 2026-03-15T20:10:49 |
| `root` | `123qwerty` | `68.183.91.110` | 2026-03-15T20:11:31 |
| `root` | `qwerty` | `68.183.91.110` | 2026-03-15T20:12:12 |
| `root` | `wasd` | `68.183.91.110` | 2026-03-15T20:12:52 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **165** |
| Unique ASNs | **73** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 20 | LOW |
| `AS14061` | DigitalOcean, LLC | 19 | LOW |
| `AS63949` | Akamai Connected Cloud | 7 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 7 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 7 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 6 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | LOW |
| `AS16509` | Amazon.com, Inc. | 5 | LOW |

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

## 🦠 Malware Analysis Results (9 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 498 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 291 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 127 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 56 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |

---

## 🔕 False Positive Summary (792 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 792 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 792 cases |
| Tool 34  | Credential Extractor        | ✅ 422 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 0 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 165 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 792 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 73 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 9 files |
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
_Report time: 2026-03-15T20:27:21Z_
