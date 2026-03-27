# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T08:49:54Z |
| **Shift Time** | 08:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **21** |
| Confirmed Threats | **16** |
| False Positives Filtered | **5** (23.8%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **10** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **17** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **15** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **10** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 2 |
| `user` | 2 |
| `blank` | 1 |
| `test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `Root!12345` | 1 |
| `qwerty` | 1 |
| `test88` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `Root!12345` | 1 |
| `blank` | `qwerty` | 1 |
| `test` | `test88` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root!12345` | `185.16.214.226` | 2026-03-27T07:04:14 |
| `root` | `3245gs5662d34` | `185.16.214.226` | 2026-03-27T07:04:19 |
| `root` | `1q2w3e..` | `47.253.123.236` | 2026-03-27T07:33:52 |
| `root` | `3245gs5662d34` | `47.253.123.236` | 2026-03-27T07:33:58 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.253.123.236`, `185.16.214.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **15** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS4771` | Spark New Zealand Trading Ltd. | 1 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS38109` | SK Broadband Co Ltd | 1 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-610768661638

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-03-27 07:04 |
| **Last Seen** | 2026-03-27 07:04 |
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
| `2026-03-27 07:04:13` | `cowrie.session.connect` |
| `2026-03-27 07:04:13` | `cowrie.client.version` |
| `2026-03-27 07:04:14` | `cowrie.client.kex` |
| `2026-03-27 07:04:14` | `cowrie.login.success` |
| `2026-03-27 07:04:15` | `cowrie.session.params` |
| `2026-03-27 07:04:15` | `cowrie.command.input` |
| `2026-03-27 07:04:15` | `cowrie.command.failed` |
| `2026-03-27 07:04:15` | `cowrie.log.closed` |
| `2026-03-27 07:04:15` | `cowrie.session.params` |
| `2026-03-27 07:04:15` | `cowrie.command.input` |
| `2026-03-27 07:04:15` | `cowrie.session.file_download` |
| `2026-03-27 07:04:15` | `cowrie.log.closed` |
| `2026-03-27 07:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a7ec6652af

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-03-27 07:04 |
| **Last Seen** | 2026-03-27 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 07:04:18` | `cowrie.session.connect` |
| `2026-03-27 07:04:18` | `cowrie.client.version` |
| `2026-03-27 07:04:18` | `cowrie.client.kex` |
| `2026-03-27 07:04:19` | `cowrie.login.success` |
| `2026-03-27 07:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edda48a0d888

| Field | Detail |
|---|---|
| **Source IP** | `47.253.123[.]236` |
| **First Seen** | 2026-03-27 07:33 |
| **Last Seen** | 2026-03-27 07:33 |
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
| `2026-03-27 07:33:51` | `cowrie.session.connect` |
| `2026-03-27 07:33:51` | `cowrie.client.version` |
| `2026-03-27 07:33:51` | `cowrie.client.kex` |
| `2026-03-27 07:33:52` | `cowrie.login.success` |
| `2026-03-27 07:33:53` | `cowrie.session.params` |
| `2026-03-27 07:33:53` | `cowrie.command.input` |
| `2026-03-27 07:33:53` | `cowrie.command.failed` |
| `2026-03-27 07:33:53` | `cowrie.log.closed` |
| `2026-03-27 07:33:53` | `cowrie.session.params` |
| `2026-03-27 07:33:53` | `cowrie.command.input` |
| `2026-03-27 07:33:54` | `cowrie.session.file_download` |
| `2026-03-27 07:33:54` | `cowrie.log.closed` |
| `2026-03-27 07:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.123[.]236` to AbuseIPDB if not already reported
- [ ] Block `47.253.123[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ffc86083da

| Field | Detail |
|---|---|
| **Source IP** | `47.253.123[.]236` |
| **First Seen** | 2026-03-27 07:33 |
| **Last Seen** | 2026-03-27 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 07:33:56` | `cowrie.session.connect` |
| `2026-03-27 07:33:56` | `cowrie.client.version` |
| `2026-03-27 07:33:57` | `cowrie.client.kex` |
| `2026-03-27 07:33:58` | `cowrie.login.success` |
| `2026-03-27 07:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.123[.]236` to AbuseIPDB if not already reported
- [ ] Block `47.253.123[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.93.37[.]178` | 1 | 2026-03-27 07:42 | 2026-03-27 07:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.171.127[.]190` | 1 | 2026-03-27 08:43 | 2026-03-27 08:43 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.140.95[.]2` | 1 | 2026-03-27 07:06 | 2026-03-27 07:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.61.43[.]103` | 1 | 2026-03-27 07:13 | 2026-03-27 07:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]123` | 1 | 2026-03-27 08:23 | 2026-03-27 08:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.109.195[.]179` | 1 | 2026-03-27 08:02 | 2026-03-27 08:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.16.214[.]226` | 1 | 2026-03-27 07:04 | 2026-03-27 07:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.8.17[.]38` | 1 | 2026-03-27 07:21 | 2026-03-27 07:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.89.198[.]191` | 1 | 2026-03-27 07:26 | 2026-03-27 07:26 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.75.156[.]89` | 1 | 2026-03-27 07:47 | 2026-03-27 07:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.253.123[.]236` | 1 | 2026-03-27 07:33 | 2026-03-27 07:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.191[.]12` | 1 | 2026-03-27 07:41 | 2026-03-27 07:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `111.171.127[.]190` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `47.253.123[.]236` | US | Alibaba Cloud - US | **100** ⚠️ | 1 |
| `113.140.95[.]2` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 24 |
| `219.89.198[.]191` | NZ | Spark New Zealand Trading Ltd | **100** ⚠️ | 17 |
| `65.20.191[.]12` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 48 |
| `183.109.195[.]179` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `118.61.43[.]103` | KR | Korea Telecom | **100** ⚠️ | 14 |
| `187.8.17[.]38` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 43 |
| `178.178.194[.]123` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 20 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 15 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 21 cases |
| Tool 34  | Credential Extractor        | ✅ 15 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (23.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 12 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-27T08:49:54Z_
