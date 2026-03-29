# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T22:28:53Z |
| **Shift Time** | 22:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **66** |
| Confirmed Threats | **61** |
| False Positives Filtered | **5** (7.6%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **16** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **62** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **27** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **16** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `guest` | 3 |
| `debian` | 2 |
| `mysql` | 2 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `ubuntu` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `111` | 1 |
| `mickael` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `mysql` | `ubuntu` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `debian` | `111` | 1 |
| `root` | `mickael` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `mickael` | `172.210.249.152` | 2026-03-29T20:34:55 |
| `root` | `3245gs5662d34` | `172.210.249.152` | 2026-03-29T20:35:00 |
| `root` | `Admin%123` | `103.187.165.26` | 2026-03-29T20:49:35 |
| `root` | `3245gs5662d34` | `103.187.165.26` | 2026-03-29T20:49:37 |

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
Source IPs: `172.210.249.152`, `103.187.165.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **32** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS8048` | CANTV Servicios, Venezuela | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS0` |  | 1 | HIGH |
| `AS6167` | Verizon Business | 1 | HIGH |
| `AS17598` | LG HelloVision Corp. | 1 | HIGH |
| `AS6300` | Fidium | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cd7e440fd736

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-03-29 20:34 |
| **Last Seen** | 2026-03-29 20:35 |
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
| `2026-03-29 20:34:53` | `cowrie.session.connect` |
| `2026-03-29 20:34:53` | `cowrie.client.version` |
| `2026-03-29 20:34:54` | `cowrie.client.kex` |
| `2026-03-29 20:34:55` | `cowrie.login.success` |
| `2026-03-29 20:34:55` | `cowrie.session.params` |
| `2026-03-29 20:34:55` | `cowrie.command.input` |
| `2026-03-29 20:34:55` | `cowrie.command.failed` |
| `2026-03-29 20:34:55` | `cowrie.log.closed` |
| `2026-03-29 20:34:56` | `cowrie.session.params` |
| `2026-03-29 20:34:56` | `cowrie.command.input` |
| `2026-03-29 20:34:56` | `cowrie.session.file_download` |
| `2026-03-29 20:34:56` | `cowrie.log.closed` |
| `2026-03-29 20:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd173ab182a

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-03-29 20:34 |
| **Last Seen** | 2026-03-29 20:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 20:34:59` | `cowrie.session.connect` |
| `2026-03-29 20:34:59` | `cowrie.client.version` |
| `2026-03-29 20:34:59` | `cowrie.client.kex` |
| `2026-03-29 20:35:00` | `cowrie.login.success` |
| `2026-03-29 20:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24078bf560d2

| Field | Detail |
|---|---|
| **Source IP** | `103.187.165[.]26` |
| **First Seen** | 2026-03-29 20:49 |
| **Last Seen** | 2026-03-29 20:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 20:49:34` | `cowrie.session.connect` |
| `2026-03-29 20:49:34` | `cowrie.client.version` |
| `2026-03-29 20:49:34` | `cowrie.client.kex` |
| `2026-03-29 20:49:35` | `cowrie.login.success` |
| `2026-03-29 20:49:35` | `cowrie.session.params` |
| `2026-03-29 20:49:35` | `cowrie.command.input` |
| `2026-03-29 20:49:35` | `cowrie.command.failed` |
| `2026-03-29 20:49:35` | `cowrie.log.closed` |
| `2026-03-29 20:49:35` | `cowrie.session.params` |
| `2026-03-29 20:49:35` | `cowrie.command.input` |
| `2026-03-29 20:49:35` | `cowrie.session.file_download` |
| `2026-03-29 20:49:35` | `cowrie.log.closed` |
| `2026-03-29 20:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.165[.]26` to AbuseIPDB if not already reported
- [ ] Block `103.187.165[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24ebdfd44df8

| Field | Detail |
|---|---|
| **Source IP** | `103.187.165[.]26` |
| **First Seen** | 2026-03-29 20:49 |
| **Last Seen** | 2026-03-29 20:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 20:49:37` | `cowrie.session.connect` |
| `2026-03-29 20:49:37` | `cowrie.client.version` |
| `2026-03-29 20:49:37` | `cowrie.client.kex` |
| `2026-03-29 20:49:37` | `cowrie.login.success` |
| `2026-03-29 20:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.165[.]26` to AbuseIPDB if not already reported
- [ ] Block `103.187.165[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.212.40[.]244` | **25** | 2026-03-29 21:17 | 2026-03-29 21:23 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `47.86.90[.]254` | **2** | 2026-03-29 21:22 | 2026-03-29 21:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.187.165[.]26` | 1 | 2026-03-29 20:49 | 2026-03-29 20:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.29.185[.]162` | 1 | 2026-03-29 20:29 | 2026-03-29 20:29 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.14.182[.]77` | 1 | 2026-03-29 21:08 | 2026-03-29 21:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.120.49[.]14` | 1 | 2026-03-29 20:49 | 2026-03-29 20:49 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.7[.]45` | 1 | 2026-03-29 21:08 | 2026-03-29 21:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.91.214[.]71` | 1 | 2026-03-29 21:48 | 2026-03-29 21:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.86.227[.]79` | 1 | 2026-03-29 21:48 | 2026-03-29 21:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `150.249.252[.]237` | 1 | 2026-03-29 20:54 | 2026-03-29 20:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `156.47.147[.]217` | 1 | 2026-03-29 21:50 | 2026-03-29 21:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-03-29 21:14 | 2026-03-29 21:14 | 10s | 0 | `T1592` | 🟢 LOW |
| `172.210.249[.]152` | 1 | 2026-03-29 20:34 | 2026-03-29 20:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.174.95[.]245` | 1 | 2026-03-29 21:28 | 2026-03-29 21:28 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.104[.]208` | 1 | 2026-03-29 21:57 | 2026-03-29 21:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.98[.]164` | 1 | 2026-03-29 21:46 | 2026-03-29 21:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.72.17[.]75` | 1 | 2026-03-29 20:49 | 2026-03-29 20:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `201.243.120[.]51` | 1 | 2026-03-29 20:36 | 2026-03-29 20:36 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `208.96.233[.]67` | 1 | 2026-03-29 20:29 | 2026-03-29 20:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.238.237[.]254` | 1 | 2026-03-29 21:38 | 2026-03-29 21:38 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.13.214[.]18` | 1 | 2026-03-29 21:28 | 2026-03-29 21:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.170.171[.]204` | 1 | 2026-03-29 22:28 | 2026-03-29 22:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.92.61[.]242` | 1 | 2026-03-29 21:13 | 2026-03-29 21:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.82.97[.]51` | 1 | 2026-03-29 20:29 | 2026-03-29 20:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.97[.]98` | 1 | 2026-03-29 21:31 | 2026-03-29 21:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.188.204[.]213` | 1 | 2026-03-29 22:08 | 2026-03-29 22:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.120.105[.]236` | 1 | 2026-03-29 21:15 | 2026-03-29 21:16 | 14s | 0 | `T1592` | 🟢 LOW |
| `63.135.169[.]175` | 1 | 2026-03-29 22:27 | 2026-03-29 22:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `63.47.149[.]59` | 1 | 2026-03-29 21:18 | 2026-03-29 21:18 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.250[.]93` | 1 | 2026-03-29 22:09 | 2026-03-29 22:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `72.56.239[.]58` | 1 | 2026-03-29 20:57 | 2026-03-29 20:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.251.107[.]177` | 1 | 2026-03-29 22:27 | 2026-03-29 22:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `63.135.169[.]175` | US | MacStadium, Inc. | **100** ⚠️ | 16 |
| `115.86.227[.]79` | KR | HVYeongseo | **100** ⚠️ | 24 |
| `222.92.61[.]242` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `156.47.147[.]217` | US | Fidium | **100** ⚠️ | 5 |
| `63.47.149[.]59` | US | Verizon Business | **100** ⚠️ | 50 |
| `102.212.40[.]244` | NG | Connect, Surf and Smile Limited | **100** ⚠️ | 5 |
| `83.251.107[.]177` | SE | Tele2 Sverige AB | **100** ⚠️ | 4 |
| `47.86.90[.]254` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 5 |
| `180.76.104[.]208` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 23 |
| `190.72.17[.]75` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 31 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 23 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 66 cases |
| Tool 34  | Credential Extractor        | ✅ 27 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (7.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 32 recon entry/entries in table (2 group(s) consolidating 27 session(s)).

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
_Report time: 2026-03-29T22:28:53Z_
