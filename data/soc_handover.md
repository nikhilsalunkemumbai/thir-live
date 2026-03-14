# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-14 |
| **Generated At** | 2026-03-14T04:09:36Z |
| **Shift Time** | 04:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **256** |
| Confirmed Threats | **54** |
| False Positives Filtered | **202** (78.9%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **13** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **249** |
| Malware Samples Analyzed | **0** HIGH · **1** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (1)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c423d371a03d

| Field | Detail |
|---|---|
| **Source IP** | `223.197.145[.]33` |
| **First Seen** | 2026-03-14 00:34 |
| **Last Seen** | 2026-03-14 00:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-14 00:34:47` | `cowrie.session.connect` |
| `2026-03-14 00:34:48` | `cowrie.client.version` |
| `2026-03-14 00:34:48` | `cowrie.client.kex` |
| `2026-03-14 00:34:50` | `cowrie.login.success` |
| `2026-03-14 00:34:51` | `cowrie.direct-tcpip.request` |
| `2026-03-14 00:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.145[.]33` to AbuseIPDB if not already reported
- [ ] Block `223.197.145[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `59.103.108[.]27` | **25** | 2026-03-14 00:16 | 2026-03-14 00:21 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **5** | 2026-03-14 03:21 | 2026-03-14 03:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.220.237[.]230` | **4** | 2026-03-14 02:58 | 2026-03-14 02:58 | 4m | 0 | `T1592` | 🟢 LOW |
| `8.211.52[.]151` | **3** | 2026-03-14 03:34 | 2026-03-14 03:34 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `101.200.236[.]207` | 1 | 2026-03-14 03:39 | 2026-03-14 03:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `102.38.3[.]181` | 1 | 2026-03-14 01:52 | 2026-03-14 01:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-14 00:21 | 2026-03-14 00:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-14 00:16 | 2026-03-14 00:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.242.152[.]189` | 1 | 2026-03-14 01:21 | 2026-03-14 01:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.43.231[.]252` | 1 | 2026-03-14 02:31 | 2026-03-14 02:31 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.151[.]153` | 1 | 2026-03-14 01:03 | 2026-03-14 01:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-03-14 01:06 | 2026-03-14 01:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.246.198[.]45` | 1 | 2026-03-14 03:51 | 2026-03-14 03:52 | 30s | 0 | `T1592` | 🟢 LOW |
| `179.181.133[.]153` | 1 | 2026-03-14 00:54 | 2026-03-14 00:54 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.148[.]79` | 1 | 2026-03-14 03:31 | 2026-03-14 03:31 | 19s | 0 | `T1592` | 🟢 LOW |
| `183.171.4[.]155` | 1 | 2026-03-14 03:48 | 2026-03-14 03:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `183.237.33[.]162` | 1 | 2026-03-14 02:11 | 2026-03-14 02:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-03-14 00:01 | 2026-03-14 00:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.106.79[.]211` | 1 | 2026-03-14 01:14 | 2026-03-14 01:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]59` | 1 | 2026-03-14 00:54 | 2026-03-14 00:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (3 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `183.171.148[.]79` | MY | Celcom Axiata Berhad | **100** ⚠️ | 5 |
| `179.181.133[.]153` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 25 |
| `8.211.52[.]151` | DE | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `183.237.33[.]162` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `183.56.179[.]201` | CN | CHINANET Guangdong province network | **100** ⚠️ | 44 |
| `112.19.44[.]93` | CN | China Mobile Communications Corporation | **100** ⚠️ | 8 |
| `102.38.3[.]181` | LY | Giga for Telecommunication and Technology Limited | **100** ⚠️ | 5 |
| `117.242.152[.]189` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 3 |
| `183.171.4[.]155` | MY | Celcom Axiata Berhad | **100** ⚠️ | 14 |
| `203.106.79[.]211` | MY | TM TECHNOLOGY SERVICES SDN. BHD. | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |

---

## 🔕 False Positive Summary (202 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 30 |
| AbuseIPDB score 12 below threshold 25 | 134 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 33 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 256 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 42 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 202 filtered (78.9%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 3 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 1 priority case(s) shown individually · 20 recon entry/entries in table (4 group(s) consolidating 37 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.1 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-14T04:09:36Z_
