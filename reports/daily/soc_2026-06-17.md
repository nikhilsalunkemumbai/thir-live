# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-17 |
| **Generated At** | 2026-06-17T11:04:05Z |
| **Shift Time** | 11:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **234** |
| Confirmed Threats | **172** |
| False Positives Filtered | **62** (26.5%) |
| Unique Attacker IPs | **113** |
| Countries of Origin | **21** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **207** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **88** |
| Unique Credential Pairs | **88** |
| Unique Usernames | **54** |
| Unique Passwords | **74** |
| Successful Auth Pairs | **27** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `ubuntu` | 3 |
| `supervisor` | 2 |
| `ansible` | 2 |
| `deploy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 7 |
| `1234` | 4 |
| `12345` | 3 |
| `1` | 3 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `config` | `qwerty123456` | 1 |
| `ubnt` | `admin123` | 1 |
| `composer` | `composer123` | 1 |
| `supervisor` | `12345` | 1 |
| `supervisor` | `supervisor2010` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Welcome@123` | `176.65.139.94` | 2026-06-17T06:06:28 |
| `root` | `P@ssword` | `176.65.139.94` | 2026-06-17T06:06:54 |
| `root` | `Huawei@123` | `176.65.139.94` | 2026-06-17T06:07:00 |
| `root` | `r00t` | `176.65.139.94` | 2026-06-17T06:07:06 |
| `root` | `Password@123` | `176.65.139.94` | 2026-06-17T06:07:19 |
| `root` | `Pass1234` | `176.65.139.94` | 2026-06-17T06:08:35 |
| `root` | `pass` | `176.65.139.94` | 2026-06-17T06:08:47 |
| `root` | `changeme` | `176.65.139.94` | 2026-06-17T06:08:58 |
| `root` | `CatCult2025!` | `176.65.139.94` | 2026-06-17T06:09:10 |
| `root` | `123@@@` | `176.65.139.94` | 2026-06-17T06:09:59 |
| `root` | `Qq123456` | `176.65.139.94` | 2026-06-17T06:10:18 |
| `root` | `123321` | `176.65.139.94` | 2026-06-17T06:10:29 |
| `root` | `Password1` | `176.65.139.94` | 2026-06-17T06:10:42 |
| `root` | `11111111` | `176.65.139.94` | 2026-06-17T06:10:48 |
| `root` | `ZAQ!2wsx` | `176.65.139.94` | 2026-06-17T06:11:06 |
| `root` | `1qaz@WSX3edc` | `176.65.139.94` | 2026-06-17T06:11:12 |
| `root` | `Aa111111.` | `176.65.139.94` | 2026-06-17T06:11:18 |
| `root` | `1029384756` | `176.65.139.94` | 2026-06-17T06:11:23 |
| `root` | `Ac123456` | `176.65.139.94` | 2026-06-17T06:11:42 |
| `root` | `1qazxsw2` | `176.65.139.94` | 2026-06-17T06:12:01 |
| `root` | `Admin123!@#` | `176.65.139.94` | 2026-06-17T06:12:13 |
| `root` | `Root@123` | `176.65.139.94` | 2026-06-17T06:12:44 |
| `root` | `qwer1234` | `176.65.139.94` | 2026-06-17T06:14:08 |
| `root` | `root2011` | `106.112.194.160` | 2026-06-17T10:35:01 |
| `root` | `R00T` | `87.117.32.22` | 2026-06-17T10:39:59 |
| `root` | `1qaz@Wsx` | `47.82.206.233` | 2026-06-17T10:41:22 |
| `root` | `3245gs5662d34` | `47.82.206.233` | 2026-06-17T10:41:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **234** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 75 |
| OpenSSH | 10 |
| libssh | 8 |
| Unknown | 3 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 71 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 10 | 10 |
| `f555226df196...` | Mirai/variant | 6 | 4 |
| `e37f354a101a...` | Mirai/variant | 2 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 71 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 10 | 10 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 4 | Mirai/variant |
| `e37f354a101a...` | libssh | 2 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.82.206.233`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **113** |
| Unique ASNs | **61** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 12 | HIGH |
| `AS31898` | Oracle Corporation | 10 | HIGH |
| `AS8075` | Microsoft Corporation | 8 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS213412` | ONYPHE SAS | 5 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | MEDIUM |
| `AS40065` | CNSERVERS LLC | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4e7411559b31

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:06 |
| **Last Seen** | 2026-06-17 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:06:28` | `cowrie.session.connect` |
| `2026-06-17 06:06:28` | `cowrie.client.version` |
| `2026-06-17 06:06:28` | `cowrie.client.kex` |
| `2026-06-17 06:06:28` | `cowrie.login.success` |
| `2026-06-17 06:06:29` | `cowrie.session.params` |
| `2026-06-17 06:06:29` | `cowrie.command.input` |
| `2026-06-17 06:06:29` | `cowrie.log.closed` |
| `2026-06-17 06:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-519bab7818cb

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:06 |
| **Last Seen** | 2026-06-17 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:06:53` | `cowrie.session.connect` |
| `2026-06-17 06:06:53` | `cowrie.client.version` |
| `2026-06-17 06:06:53` | `cowrie.client.kex` |
| `2026-06-17 06:06:54` | `cowrie.login.success` |
| `2026-06-17 06:06:54` | `cowrie.session.params` |
| `2026-06-17 06:06:54` | `cowrie.command.input` |
| `2026-06-17 06:06:54` | `cowrie.log.closed` |
| `2026-06-17 06:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154c03095abd

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:07 |
| **Last Seen** | 2026-06-17 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:07:00` | `cowrie.session.connect` |
| `2026-06-17 06:07:00` | `cowrie.client.version` |
| `2026-06-17 06:07:00` | `cowrie.client.kex` |
| `2026-06-17 06:07:00` | `cowrie.login.success` |
| `2026-06-17 06:07:01` | `cowrie.session.params` |
| `2026-06-17 06:07:01` | `cowrie.command.input` |
| `2026-06-17 06:07:01` | `cowrie.log.closed` |
| `2026-06-17 06:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee9f2b427fc

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:07 |
| **Last Seen** | 2026-06-17 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:07:06` | `cowrie.session.connect` |
| `2026-06-17 06:07:06` | `cowrie.client.version` |
| `2026-06-17 06:07:06` | `cowrie.client.kex` |
| `2026-06-17 06:07:06` | `cowrie.login.success` |
| `2026-06-17 06:07:06` | `cowrie.session.params` |
| `2026-06-17 06:07:06` | `cowrie.command.input` |
| `2026-06-17 06:07:07` | `cowrie.log.closed` |
| `2026-06-17 06:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd7accb7800

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:07 |
| **Last Seen** | 2026-06-17 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:07:18` | `cowrie.session.connect` |
| `2026-06-17 06:07:18` | `cowrie.client.version` |
| `2026-06-17 06:07:18` | `cowrie.client.kex` |
| `2026-06-17 06:07:19` | `cowrie.login.success` |
| `2026-06-17 06:07:19` | `cowrie.session.params` |
| `2026-06-17 06:07:19` | `cowrie.command.input` |
| `2026-06-17 06:07:19` | `cowrie.log.closed` |
| `2026-06-17 06:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeeb46fd28cd

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:08 |
| **Last Seen** | 2026-06-17 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:08:34` | `cowrie.session.connect` |
| `2026-06-17 06:08:34` | `cowrie.client.version` |
| `2026-06-17 06:08:34` | `cowrie.client.kex` |
| `2026-06-17 06:08:35` | `cowrie.login.success` |
| `2026-06-17 06:08:35` | `cowrie.session.params` |
| `2026-06-17 06:08:35` | `cowrie.command.input` |
| `2026-06-17 06:08:35` | `cowrie.log.closed` |
| `2026-06-17 06:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacf889279e7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:08 |
| **Last Seen** | 2026-06-17 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:08:46` | `cowrie.session.connect` |
| `2026-06-17 06:08:46` | `cowrie.client.version` |
| `2026-06-17 06:08:46` | `cowrie.client.kex` |
| `2026-06-17 06:08:47` | `cowrie.login.success` |
| `2026-06-17 06:08:47` | `cowrie.session.params` |
| `2026-06-17 06:08:47` | `cowrie.command.input` |
| `2026-06-17 06:08:47` | `cowrie.log.closed` |
| `2026-06-17 06:08:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e483909ac175

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:08 |
| **Last Seen** | 2026-06-17 06:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:08:57` | `cowrie.session.connect` |
| `2026-06-17 06:08:57` | `cowrie.client.version` |
| `2026-06-17 06:08:58` | `cowrie.client.kex` |
| `2026-06-17 06:08:58` | `cowrie.login.success` |
| `2026-06-17 06:08:58` | `cowrie.session.params` |
| `2026-06-17 06:08:58` | `cowrie.command.input` |
| `2026-06-17 06:08:59` | `cowrie.log.closed` |
| `2026-06-17 06:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2428c13b59f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:09 |
| **Last Seen** | 2026-06-17 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:09:09` | `cowrie.session.connect` |
| `2026-06-17 06:09:09` | `cowrie.client.version` |
| `2026-06-17 06:09:09` | `cowrie.client.kex` |
| `2026-06-17 06:09:10` | `cowrie.login.success` |
| `2026-06-17 06:09:11` | `cowrie.session.params` |
| `2026-06-17 06:09:11` | `cowrie.command.input` |
| `2026-06-17 06:09:11` | `cowrie.log.closed` |
| `2026-06-17 06:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b67a65976788

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:09 |
| **Last Seen** | 2026-06-17 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:09:58` | `cowrie.session.connect` |
| `2026-06-17 06:09:58` | `cowrie.client.version` |
| `2026-06-17 06:09:58` | `cowrie.client.kex` |
| `2026-06-17 06:09:59` | `cowrie.login.success` |
| `2026-06-17 06:09:59` | `cowrie.session.params` |
| `2026-06-17 06:09:59` | `cowrie.command.input` |
| `2026-06-17 06:09:59` | `cowrie.log.closed` |
| `2026-06-17 06:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f291ac9cc3

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:10 |
| **Last Seen** | 2026-06-17 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:10:17` | `cowrie.session.connect` |
| `2026-06-17 06:10:17` | `cowrie.client.version` |
| `2026-06-17 06:10:17` | `cowrie.client.kex` |
| `2026-06-17 06:10:18` | `cowrie.login.success` |
| `2026-06-17 06:10:18` | `cowrie.session.params` |
| `2026-06-17 06:10:18` | `cowrie.command.input` |
| `2026-06-17 06:10:18` | `cowrie.log.closed` |
| `2026-06-17 06:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efaf54c22bf5

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:10 |
| **Last Seen** | 2026-06-17 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:10:29` | `cowrie.session.connect` |
| `2026-06-17 06:10:29` | `cowrie.client.version` |
| `2026-06-17 06:10:29` | `cowrie.client.kex` |
| `2026-06-17 06:10:29` | `cowrie.login.success` |
| `2026-06-17 06:10:30` | `cowrie.session.params` |
| `2026-06-17 06:10:30` | `cowrie.command.input` |
| `2026-06-17 06:10:30` | `cowrie.log.closed` |
| `2026-06-17 06:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9659f5bc8898

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:10 |
| **Last Seen** | 2026-06-17 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:10:41` | `cowrie.session.connect` |
| `2026-06-17 06:10:41` | `cowrie.client.version` |
| `2026-06-17 06:10:41` | `cowrie.client.kex` |
| `2026-06-17 06:10:42` | `cowrie.login.success` |
| `2026-06-17 06:10:42` | `cowrie.session.params` |
| `2026-06-17 06:10:42` | `cowrie.command.input` |
| `2026-06-17 06:10:42` | `cowrie.log.closed` |
| `2026-06-17 06:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7639429e0875

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:10 |
| **Last Seen** | 2026-06-17 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:10:47` | `cowrie.session.connect` |
| `2026-06-17 06:10:47` | `cowrie.client.version` |
| `2026-06-17 06:10:47` | `cowrie.client.kex` |
| `2026-06-17 06:10:48` | `cowrie.login.success` |
| `2026-06-17 06:10:48` | `cowrie.session.params` |
| `2026-06-17 06:10:48` | `cowrie.command.input` |
| `2026-06-17 06:10:48` | `cowrie.log.closed` |
| `2026-06-17 06:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daee23c0a176

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:11 |
| **Last Seen** | 2026-06-17 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:11:06` | `cowrie.session.connect` |
| `2026-06-17 06:11:06` | `cowrie.client.version` |
| `2026-06-17 06:11:06` | `cowrie.client.kex` |
| `2026-06-17 06:11:06` | `cowrie.login.success` |
| `2026-06-17 06:11:07` | `cowrie.session.params` |
| `2026-06-17 06:11:07` | `cowrie.command.input` |
| `2026-06-17 06:11:07` | `cowrie.log.closed` |
| `2026-06-17 06:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cbc7fb59c0f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:11 |
| **Last Seen** | 2026-06-17 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:11:12` | `cowrie.session.connect` |
| `2026-06-17 06:11:12` | `cowrie.client.version` |
| `2026-06-17 06:11:12` | `cowrie.client.kex` |
| `2026-06-17 06:11:12` | `cowrie.login.success` |
| `2026-06-17 06:11:13` | `cowrie.session.params` |
| `2026-06-17 06:11:13` | `cowrie.command.input` |
| `2026-06-17 06:11:13` | `cowrie.log.closed` |
| `2026-06-17 06:11:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-527ea2bbe348

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:11 |
| **Last Seen** | 2026-06-17 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:11:17` | `cowrie.session.connect` |
| `2026-06-17 06:11:17` | `cowrie.client.version` |
| `2026-06-17 06:11:17` | `cowrie.client.kex` |
| `2026-06-17 06:11:18` | `cowrie.login.success` |
| `2026-06-17 06:11:18` | `cowrie.session.params` |
| `2026-06-17 06:11:18` | `cowrie.command.input` |
| `2026-06-17 06:11:18` | `cowrie.log.closed` |
| `2026-06-17 06:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89182e2a6b02

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:11 |
| **Last Seen** | 2026-06-17 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:11:23` | `cowrie.session.connect` |
| `2026-06-17 06:11:23` | `cowrie.client.version` |
| `2026-06-17 06:11:23` | `cowrie.client.kex` |
| `2026-06-17 06:11:23` | `cowrie.login.success` |
| `2026-06-17 06:11:24` | `cowrie.session.params` |
| `2026-06-17 06:11:24` | `cowrie.command.input` |
| `2026-06-17 06:11:24` | `cowrie.log.closed` |
| `2026-06-17 06:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a52dad3beaf1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:11 |
| **Last Seen** | 2026-06-17 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:11:41` | `cowrie.session.connect` |
| `2026-06-17 06:11:41` | `cowrie.client.version` |
| `2026-06-17 06:11:42` | `cowrie.client.kex` |
| `2026-06-17 06:11:42` | `cowrie.login.success` |
| `2026-06-17 06:11:43` | `cowrie.session.params` |
| `2026-06-17 06:11:43` | `cowrie.command.input` |
| `2026-06-17 06:11:43` | `cowrie.log.closed` |
| `2026-06-17 06:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b72aff6a0330

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:12 |
| **Last Seen** | 2026-06-17 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:12:00` | `cowrie.session.connect` |
| `2026-06-17 06:12:00` | `cowrie.client.version` |
| `2026-06-17 06:12:00` | `cowrie.client.kex` |
| `2026-06-17 06:12:01` | `cowrie.login.success` |
| `2026-06-17 06:12:01` | `cowrie.session.params` |
| `2026-06-17 06:12:01` | `cowrie.command.input` |
| `2026-06-17 06:12:01` | `cowrie.log.closed` |
| `2026-06-17 06:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef1a8a0903c

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:12 |
| **Last Seen** | 2026-06-17 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:12:13` | `cowrie.session.connect` |
| `2026-06-17 06:12:13` | `cowrie.client.version` |
| `2026-06-17 06:12:13` | `cowrie.client.kex` |
| `2026-06-17 06:12:13` | `cowrie.login.success` |
| `2026-06-17 06:12:14` | `cowrie.session.params` |
| `2026-06-17 06:12:14` | `cowrie.command.input` |
| `2026-06-17 06:12:14` | `cowrie.log.closed` |
| `2026-06-17 06:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4fa4096734d

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:12 |
| **Last Seen** | 2026-06-17 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:12:43` | `cowrie.session.connect` |
| `2026-06-17 06:12:43` | `cowrie.client.version` |
| `2026-06-17 06:12:43` | `cowrie.client.kex` |
| `2026-06-17 06:12:44` | `cowrie.login.success` |
| `2026-06-17 06:12:44` | `cowrie.session.params` |
| `2026-06-17 06:12:44` | `cowrie.command.input` |
| `2026-06-17 06:12:44` | `cowrie.log.closed` |
| `2026-06-17 06:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa06d1679554

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]94` |
| **First Seen** | 2026-06-17 06:14 |
| **Last Seen** | 2026-06-17 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 06:14:07` | `cowrie.session.connect` |
| `2026-06-17 06:14:07` | `cowrie.client.version` |
| `2026-06-17 06:14:07` | `cowrie.client.kex` |
| `2026-06-17 06:14:08` | `cowrie.login.success` |
| `2026-06-17 06:14:08` | `cowrie.session.params` |
| `2026-06-17 06:14:08` | `cowrie.command.input` |
| `2026-06-17 06:14:08` | `cowrie.log.closed` |
| `2026-06-17 06:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]94` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee9d8f551ea

| Field | Detail |
|---|---|
| **Source IP** | `106.112.194[.]160` |
| **First Seen** | 2026-06-17 10:34 |
| **Last Seen** | 2026-06-17 10:35 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 10:34:58` | `cowrie.session.connect` |
| `2026-06-17 10:34:59` | `cowrie.client.version` |
| `2026-06-17 10:34:59` | `cowrie.client.kex` |
| `2026-06-17 10:35:01` | `cowrie.login.success` |
| `2026-06-17 10:35:02` | `cowrie.direct-tcpip.request` |
| `2026-06-17 10:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.112.194[.]160` to AbuseIPDB if not already reported
- [ ] Block `106.112.194[.]160` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3722289429b8

| Field | Detail |
|---|---|
| **Source IP** | `87.117.32[.]22` |
| **First Seen** | 2026-06-17 10:39 |
| **Last Seen** | 2026-06-17 10:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 10:39:57` | `cowrie.session.connect` |
| `2026-06-17 10:39:58` | `cowrie.client.version` |
| `2026-06-17 10:39:58` | `cowrie.client.kex` |
| `2026-06-17 10:39:59` | `cowrie.login.success` |
| `2026-06-17 10:39:59` | `cowrie.direct-tcpip.request` |
| `2026-06-17 10:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.117.32[.]22` to AbuseIPDB if not already reported
- [ ] Block `87.117.32[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8290017cc116

| Field | Detail |
|---|---|
| **Source IP** | `47.82.206[.]233` |
| **First Seen** | 2026-06-17 10:41 |
| **Last Seen** | 2026-06-17 10:41 |
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
| `2026-06-17 10:41:22` | `cowrie.session.connect` |
| `2026-06-17 10:41:22` | `cowrie.client.version` |
| `2026-06-17 10:41:22` | `cowrie.client.kex` |
| `2026-06-17 10:41:22` | `cowrie.login.success` |
| `2026-06-17 10:41:22` | `cowrie.session.params` |
| `2026-06-17 10:41:22` | `cowrie.command.input` |
| `2026-06-17 10:41:22` | `cowrie.command.failed` |
| `2026-06-17 10:41:22` | `cowrie.log.closed` |
| `2026-06-17 10:41:23` | `cowrie.session.params` |
| `2026-06-17 10:41:23` | `cowrie.command.input` |
| `2026-06-17 10:41:23` | `cowrie.session.file_download` |
| `2026-06-17 10:41:23` | `cowrie.log.closed` |
| `2026-06-17 10:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `47.82.206[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0489ac384ef

| Field | Detail |
|---|---|
| **Source IP** | `47.82.206[.]233` |
| **First Seen** | 2026-06-17 10:41 |
| **Last Seen** | 2026-06-17 10:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-17 10:41:24` | `cowrie.session.connect` |
| `2026-06-17 10:41:24` | `cowrie.client.version` |
| `2026-06-17 10:41:24` | `cowrie.client.kex` |
| `2026-06-17 10:41:24` | `cowrie.login.success` |
| `2026-06-17 10:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.206[.]233` to AbuseIPDB if not already reported
- [ ] Block `47.82.206[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `176.65.139[.]94` | **49** | 2026-06-17 06:05 | 2026-06-17 06:13 | 1m | 48 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.230.150[.]187` | **12** | 2026-06-17 07:28 | 2026-06-17 10:41 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `113.119.10[.]32` | **4** | 2026-06-17 10:29 | 2026-06-17 10:29 | 4m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-06-17 07:42 | 2026-06-17 07:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]68` | **2** | 2026-06-17 10:56 | 2026-06-17 10:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]105` | **2** | 2026-06-17 10:39 | 2026-06-17 10:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-06-17 11:00 | 2026-06-17 11:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.176.230[.]83` | **2** | 2026-06-17 07:00 | 2026-06-17 07:01 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]190` | **2** | 2026-06-17 05:46 | 2026-06-17 05:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]199` | **2** | 2026-06-17 10:43 | 2026-06-17 10:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.21.70[.]131` | **2** | 2026-06-17 05:39 | 2026-06-17 06:25 | 1m | 0 | `T1592` | 🟢 LOW |
| `1.212.225[.]99` | 1 | 2026-06-17 06:52 | 2026-06-17 06:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.121.27[.]218` | 1 | 2026-06-17 06:13 | 2026-06-17 06:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.155.100[.]64` | 1 | 2026-06-17 09:28 | 2026-06-17 09:30 | 78s | 0 | `T1592` | 🟢 LOW |
| `103.251.143[.]14` | 1 | 2026-06-17 05:43 | 2026-06-17 05:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.170.140[.]246` | 1 | 2026-06-17 05:05 | 2026-06-17 05:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `111.170.172[.]166` | 1 | 2026-06-17 08:30 | 2026-06-17 08:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `112.26.101[.]76` | 1 | 2026-06-17 05:37 | 2026-06-17 05:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.108.88[.]121` | 1 | 2026-06-17 04:37 | 2026-06-17 04:37 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.66.31[.]58` | 1 | 2026-06-17 07:46 | 2026-06-17 07:47 | 34s | 0 | `T1592` | 🟢 LOW |
| `129.154.218[.]157` | 1 | 2026-06-17 04:32 | 2026-06-17 04:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `138.199.39[.]178` | 1 | 2026-06-17 10:49 | 2026-06-17 10:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.2.119[.]204` | 1 | 2026-06-17 10:07 | 2026-06-17 10:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `138.2.232[.]123` | 1 | 2026-06-17 09:01 | 2026-06-17 09:02 | 31s | 0 | `T1592` | 🟢 LOW |
| `139.99.38[.]177` | 1 | 2026-06-17 07:53 | 2026-06-17 07:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.123[.]19` | 1 | 2026-06-17 07:27 | 2026-06-17 07:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.29.170[.]54` | 1 | 2026-06-17 06:38 | 2026-06-17 06:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `148.135.78[.]155` | 1 | 2026-06-17 06:54 | 2026-06-17 06:55 | 30s | 0 | `T1592` | 🟢 LOW |
| `152.67.208[.]137` | 1 | 2026-06-17 07:04 | 2026-06-17 07:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `152.70.92[.]224` | 1 | 2026-06-17 10:10 | 2026-06-17 10:11 | 31s | 0 | `T1592` | 🟢 LOW |
| `154.201.88[.]169` | 1 | 2026-06-17 06:42 | 2026-06-17 06:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `157.66.26[.]151` | 1 | 2026-06-17 05:23 | 2026-06-17 05:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `16.162.188[.]118` | 1 | 2026-06-17 09:09 | 2026-06-17 09:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `163.192.50[.]170` | 1 | 2026-06-17 09:35 | 2026-06-17 09:35 | 30s | 0 | `T1592` | 🟢 LOW |
| `164.152.39[.]78` | 1 | 2026-06-17 06:14 | 2026-06-17 06:15 | 31s | 0 | `T1592` | 🟢 LOW |
| `168.138.43[.]181` | 1 | 2026-06-17 06:11 | 2026-06-17 06:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `170.245.251[.]214` | 1 | 2026-06-17 07:31 | 2026-06-17 07:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `171.114.226[.]230` | 1 | 2026-06-17 10:22 | 2026-06-17 10:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `182.243.186[.]176` | 1 | 2026-06-17 10:07 | 2026-06-17 10:07 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.90.187[.]155` | 1 | 2026-06-17 08:19 | 2026-06-17 08:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `20.125.149[.]183` | 1 | 2026-06-17 09:55 | 2026-06-17 09:55 | 31s | 0 | `T1592` | 🟢 LOW |
| `20.235.132[.]245` | 1 | 2026-06-17 05:19 | 2026-06-17 05:20 | 31s | 0 | `T1592` | 🟢 LOW |
| `20.44.58[.]80` | 1 | 2026-06-17 05:19 | 2026-06-17 05:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `202.73.4[.]102` | 1 | 2026-06-17 09:10 | 2026-06-17 09:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `218.21.246[.]238` | 1 | 2026-06-17 06:43 | 2026-06-17 06:43 | 4s | 0 | `T1592` | 🟢 LOW |
| `220.246.42[.]212` | 1 | 2026-06-17 04:44 | 2026-06-17 04:44 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-06-17 04:59 | 2026-06-17 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `223.80.102[.]26` | 1 | 2026-06-17 07:03 | 2026-06-17 07:04 | 31s | 0 | `T1592` | 🟢 LOW |
| `23.144.124[.]238` | 1 | 2026-06-17 09:04 | 2026-06-17 09:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.224.105[.]122` | 1 | 2026-06-17 09:12 | 2026-06-17 09:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.224.130[.]178` | 1 | 2026-06-17 09:11 | 2026-06-17 09:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.225.228[.]26` | 1 | 2026-06-17 09:11 | 2026-06-17 09:11 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.82.124[.]157` | 1 | 2026-06-17 06:34 | 2026-06-17 06:34 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.95.7[.]118` | 1 | 2026-06-17 04:41 | 2026-06-17 04:41 | 34s | 0 | `T1592` | 🟢 LOW |
| `24.37.212[.]62` | 1 | 2026-06-17 06:42 | 2026-06-17 06:42 | 13s | 0 | `T1592` | 🟢 LOW |
| `27.29.166[.]53` | 1 | 2026-06-17 08:54 | 2026-06-17 08:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.4.110[.]201` | 1 | 2026-06-17 10:19 | 2026-06-17 10:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `36.251.141[.]8` | 1 | 2026-06-17 07:50 | 2026-06-17 07:51 | 31s | 0 | `T1592` | 🟢 LOW |
| `38.175.198[.]44` | 1 | 2026-06-17 04:24 | 2026-06-17 04:24 | 47s | 0 | `T1592` | 🟢 LOW |
| `41.60.251[.]71` | 1 | 2026-06-17 08:54 | 2026-06-17 08:54 | 14s | 0 | `T1592` | 🟢 LOW |
| `43.248.213[.]232` | 1 | 2026-06-17 09:35 | 2026-06-17 09:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.20.109[.]223` | 1 | 2026-06-17 05:56 | 2026-06-17 05:57 | 30s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]30` | 1 | 2026-06-17 10:41 | 2026-06-17 10:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-06-17 05:31 | 2026-06-17 05:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.209.49[.]194` | 1 | 2026-06-17 05:41 | 2026-06-17 05:41 | 15s | 0 | `T1592` | 🟢 LOW |
| `64.181.242[.]79` | 1 | 2026-06-17 05:08 | 2026-06-17 05:09 | 30s | 0 | `T1592` | 🟢 LOW |
| `70.153.81[.]141` | 1 | 2026-06-17 05:01 | 2026-06-17 05:02 | 30s | 0 | `T1592` | 🟢 LOW |
| `74.225.28[.]48` | 1 | 2026-06-17 05:18 | 2026-06-17 05:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `74.225.30[.]8` | 1 | 2026-06-17 05:19 | 2026-06-17 05:19 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.229.133[.]190` | 1 | 2026-06-17 04:24 | 2026-06-17 04:24 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]140` | 1 | 2026-06-17 10:08 | 2026-06-17 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]141` | 1 | 2026-06-17 10:08 | 2026-06-17 10:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]143` | 1 | 2026-06-17 10:08 | 2026-06-17 10:08 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]187` | 1 | 2026-06-17 10:08 | 2026-06-17 10:08 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]39` | 1 | 2026-06-17 10:10 | 2026-06-17 10:10 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/73 ✅ |
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
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
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
| `91.230.168[.]39` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `46.20.109[.]223` | HK | Nearoute Limited | **100** ⚠️ | 0 |
| `20.125.149[.]183` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `34.4.110[.]201` | US | Google LLC | **100** ⚠️ | 1 |
| `163.192.50[.]170` | US | Oracle Corporation | **100** ⚠️ | 1 |
| `23.224.130[.]178` | US | CloudRadium L.L.C | **100** ⚠️ | 0 |
| `152.67.208[.]137` | KR | Oracle Public Cloud | **100** ⚠️ | 0 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `16.162.188[.]118` | HK | Amazon Data Services Hong Kong | **100** ⚠️ | 0 |
| `218.21.246[.]238` | CN | InnerMongoliaWuhaiGanSuErJian | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 98 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (62 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 51 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 234 cases |
| Tool 34  | Credential Extractor        | ✅ 88 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 113 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 62 filtered (26.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 75 recon entry/entries in table (11 group(s) consolidating 81 session(s)).

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
_Report time: 2026-06-17T11:04:05Z_
