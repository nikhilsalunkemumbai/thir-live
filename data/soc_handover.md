# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T13:14:52Z |
| **Shift Time** | 13:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **237** |
| Confirmed Threats | **233** |
| False Positives Filtered | **4** (1.7%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **19** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **185** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **220** |
| Unique Credential Pairs | **214** |
| Unique Usernames | **81** |
| Unique Passwords | **170** |
| Successful Auth Pairs | **52** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `oracle` | 9 |
| `admin` | 7 |
| `guest` | 6 |
| `es` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 31 |
| `123` | 6 |
| `abc123` | 4 |
| `3245gs5662d34` | 4 |
| `345gs5662d34` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 4 |
| `345gs5662d34` | `345gs5662d34` | 3 |
| `guest` | `guest` | 2 |
| `admin` | `123456` | 1 |
| `root` | `1Q2w3e4r` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1Q2w3e4r` | `197.156.67.84` | 2026-03-30T11:00:23 |
| `root` | `p@ssw0rd` | `197.156.67.84` | 2026-03-30T11:00:58 |
| `root` | `1234` | `197.156.67.84` | 2026-03-30T11:01:22 |
| `root` | `1Q2W3E4R` | `197.156.67.84` | 2026-03-30T11:02:45 |
| `root` | `Qq123456` | `197.156.67.84` | 2026-03-30T11:03:21 |
| `root` | `passw0rd` | `197.156.67.84` | 2026-03-30T11:04:20 |
| `root` | `1qaz2wsx` | `197.156.67.84` | 2026-03-30T11:05:19 |
| `root` | `Qwerty` | `197.156.67.84` | 2026-03-30T11:08:18 |
| `root` | `4e2q1w3r` | `197.156.67.84` | 2026-03-30T11:10:05 |
| `root` | `root123` | `197.156.67.84` | 2026-03-30T11:11:16 |
| `root` | `!Q@W3e4r` | `197.156.67.84` | 2026-03-30T11:12:39 |
| `root` | `P@55w0rd` | `197.156.67.84` | 2026-03-30T11:13:26 |
| `root` | `1234567890` | `197.156.67.84` | 2026-03-30T11:13:38 |
| `root` | `!QAZ2wsx` | `197.156.67.84` | 2026-03-30T11:15:49 |
| `root` | `!Qaz@Wsx` | `197.156.67.84` | 2026-03-30T11:16:49 |
| `root` | `QWERTY123` | `197.156.67.84` | 2026-03-30T11:17:48 |
| `root` | `12345` | `197.156.67.84` | 2026-03-30T11:18:00 |
| `root` | `Password1` | `197.156.67.84` | 2026-03-30T11:18:24 |
| `root` | `AA123456` | `197.156.67.84` | 2026-03-30T11:20:10 |
| `root` | `!QAZ@WSX` | `197.156.67.84` | 2026-03-30T11:20:22 |
| `root` | `Passw0rd` | `197.156.67.84` | 2026-03-30T11:20:46 |
| `root` | `Password` | `197.156.67.84` | 2026-03-30T11:21:46 |
| `root` | `123` | `197.156.67.84` | 2026-03-30T11:22:45 |
| `root` | `default` | `185.118.128.34` | 2026-03-30T11:23:43 |
| `root` | `123321` | `197.156.67.84` | 2026-03-30T11:24:56 |
| `root` | `1qaz@WSX` | `197.156.67.84` | 2026-03-30T11:26:07 |
| `root` | `aB123456` | `197.156.67.84` | 2026-03-30T11:28:18 |
| `root` | `a123456A` | `197.156.67.84` | 2026-03-30T11:28:30 |
| `root` | `Admin@123` | `197.156.67.84` | 2026-03-30T11:28:41 |
| `root` | `qq123456` | `197.156.67.84` | 2026-03-30T11:28:54 |
| `root` | `1qazXSW@` | `197.156.67.84` | 2026-03-30T11:29:17 |
| `root` | `QQ123456` | `197.156.67.84` | 2026-03-30T11:30:05 |
| `root` | `1qazxsw2` | `197.156.67.84` | 2026-03-30T11:30:28 |
| `root` | `toor` | `197.156.67.84` | 2026-03-30T11:31:04 |
| `root` | `qwerty` | `197.156.67.84` | 2026-03-30T11:31:16 |
| `root` | `aa123456` | `197.156.67.84` | 2026-03-30T11:31:52 |
| `root` | `1q2w3e4r` | `197.156.67.84` | 2026-03-30T11:32:03 |
| `root` | `root@123` | `197.156.67.84` | 2026-03-30T11:32:15 |
| `root` | `111111` | `197.156.67.84` | 2026-03-30T11:32:27 |
| `root` | `A123456a` | `197.156.67.84` | 2026-03-30T11:33:02 |
| `root` | `passwd` | `197.156.67.84` | 2026-03-30T11:34:14 |
| `root` | `Ac123456` | `197.156.67.84` | 2026-03-30T11:35:37 |
| `root` | `123456789` | `197.156.67.84` | 2026-03-30T11:36:25 |
| `root` | `rootroot` | `197.156.67.84` | 2026-03-30T11:36:36 |
| `root` | `nima` | `101.47.142.111` | 2026-03-30T12:27:21 |
| `root` | `3245gs5662d34` | `101.47.142.111` | 2026-03-30T12:27:24 |
| `root` | `8886.cn` | `197.153.57.103` | 2026-03-30T13:03:46 |
| `root` | `3245gs5662d34` | `197.153.57.103` | 2026-03-30T13:03:51 |
| `root` | `qwertz1234` | `58.209.234.84` | 2026-03-30T13:05:02 |
| `root` | `3245gs5662d34` | `58.209.234.84` | 2026-03-30T13:05:12 |
| `root` | `!@#$QWER` | `160.174.129.232` | 2026-03-30T13:07:22 |
| `root` | `3245gs5662d34` | `160.174.129.232` | 2026-03-30T13:07:25 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox FFHSB
```
Source IPs: `185.118.128.34`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `160.174.129.232`, `197.153.57.103`, `58.209.234.84`, `101.47.142.111`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **31** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS56041` | China Mobile communications corporation | 2 | HIGH |
| `AS37457` | Telkom SA Ltd. | 2 | HIGH |
| `AS8434` | Telenor Sverige AB | 2 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |
| `AS3301` | Telia Company AB | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1d3bd849d2fa

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:00 |
| **Last Seen** | 2026-03-30 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:00:22` | `cowrie.session.connect` |
| `2026-03-30 11:00:22` | `cowrie.client.version` |
| `2026-03-30 11:00:22` | `cowrie.client.kex` |
| `2026-03-30 11:00:23` | `cowrie.login.success` |
| `2026-03-30 11:00:23` | `cowrie.session.params` |
| `2026-03-30 11:00:23` | `cowrie.command.input` |
| `2026-03-30 11:00:23` | `cowrie.log.closed` |
| `2026-03-30 11:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483919b6b419

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:00 |
| **Last Seen** | 2026-03-30 11:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:00:57` | `cowrie.session.connect` |
| `2026-03-30 11:00:57` | `cowrie.client.version` |
| `2026-03-30 11:00:57` | `cowrie.client.kex` |
| `2026-03-30 11:00:58` | `cowrie.login.success` |
| `2026-03-30 11:00:58` | `cowrie.session.params` |
| `2026-03-30 11:00:58` | `cowrie.command.input` |
| `2026-03-30 11:00:58` | `cowrie.log.closed` |
| `2026-03-30 11:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10f48aeb8033

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:01 |
| **Last Seen** | 2026-03-30 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:01:21` | `cowrie.session.connect` |
| `2026-03-30 11:01:21` | `cowrie.client.version` |
| `2026-03-30 11:01:21` | `cowrie.client.kex` |
| `2026-03-30 11:01:22` | `cowrie.login.success` |
| `2026-03-30 11:01:22` | `cowrie.session.params` |
| `2026-03-30 11:01:22` | `cowrie.command.input` |
| `2026-03-30 11:01:22` | `cowrie.log.closed` |
| `2026-03-30 11:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205a2b8e85fe

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:02 |
| **Last Seen** | 2026-03-30 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:02:44` | `cowrie.session.connect` |
| `2026-03-30 11:02:44` | `cowrie.client.version` |
| `2026-03-30 11:02:44` | `cowrie.client.kex` |
| `2026-03-30 11:02:45` | `cowrie.login.success` |
| `2026-03-30 11:02:45` | `cowrie.session.params` |
| `2026-03-30 11:02:45` | `cowrie.command.input` |
| `2026-03-30 11:02:45` | `cowrie.log.closed` |
| `2026-03-30 11:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f802fafa1e

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:03 |
| **Last Seen** | 2026-03-30 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:03:20` | `cowrie.session.connect` |
| `2026-03-30 11:03:20` | `cowrie.client.version` |
| `2026-03-30 11:03:20` | `cowrie.client.kex` |
| `2026-03-30 11:03:21` | `cowrie.login.success` |
| `2026-03-30 11:03:21` | `cowrie.session.params` |
| `2026-03-30 11:03:21` | `cowrie.command.input` |
| `2026-03-30 11:03:21` | `cowrie.log.closed` |
| `2026-03-30 11:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b22beae4b038

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:04 |
| **Last Seen** | 2026-03-30 11:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:04:19` | `cowrie.session.connect` |
| `2026-03-30 11:04:19` | `cowrie.client.version` |
| `2026-03-30 11:04:19` | `cowrie.client.kex` |
| `2026-03-30 11:04:20` | `cowrie.login.success` |
| `2026-03-30 11:04:20` | `cowrie.session.params` |
| `2026-03-30 11:04:20` | `cowrie.command.input` |
| `2026-03-30 11:04:20` | `cowrie.log.closed` |
| `2026-03-30 11:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23915a9de55

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:05 |
| **Last Seen** | 2026-03-30 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:05:19` | `cowrie.session.connect` |
| `2026-03-30 11:05:19` | `cowrie.client.version` |
| `2026-03-30 11:05:19` | `cowrie.client.kex` |
| `2026-03-30 11:05:19` | `cowrie.login.success` |
| `2026-03-30 11:05:20` | `cowrie.session.params` |
| `2026-03-30 11:05:20` | `cowrie.command.input` |
| `2026-03-30 11:05:20` | `cowrie.log.closed` |
| `2026-03-30 11:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e91ee7aa9606

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:08 |
| **Last Seen** | 2026-03-30 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:08:17` | `cowrie.session.connect` |
| `2026-03-30 11:08:17` | `cowrie.client.version` |
| `2026-03-30 11:08:17` | `cowrie.client.kex` |
| `2026-03-30 11:08:18` | `cowrie.login.success` |
| `2026-03-30 11:08:18` | `cowrie.session.params` |
| `2026-03-30 11:08:18` | `cowrie.command.input` |
| `2026-03-30 11:08:18` | `cowrie.log.closed` |
| `2026-03-30 11:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016698badadf

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:10 |
| **Last Seen** | 2026-03-30 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:10:04` | `cowrie.session.connect` |
| `2026-03-30 11:10:04` | `cowrie.client.version` |
| `2026-03-30 11:10:04` | `cowrie.client.kex` |
| `2026-03-30 11:10:05` | `cowrie.login.success` |
| `2026-03-30 11:10:05` | `cowrie.session.params` |
| `2026-03-30 11:10:05` | `cowrie.command.input` |
| `2026-03-30 11:10:05` | `cowrie.log.closed` |
| `2026-03-30 11:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de07db03bc21

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:11 |
| **Last Seen** | 2026-03-30 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:11:15` | `cowrie.session.connect` |
| `2026-03-30 11:11:15` | `cowrie.client.version` |
| `2026-03-30 11:11:15` | `cowrie.client.kex` |
| `2026-03-30 11:11:16` | `cowrie.login.success` |
| `2026-03-30 11:11:16` | `cowrie.session.params` |
| `2026-03-30 11:11:16` | `cowrie.command.input` |
| `2026-03-30 11:11:16` | `cowrie.log.closed` |
| `2026-03-30 11:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9cf2f12b42d

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:12 |
| **Last Seen** | 2026-03-30 11:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:12:38` | `cowrie.session.connect` |
| `2026-03-30 11:12:38` | `cowrie.client.version` |
| `2026-03-30 11:12:38` | `cowrie.client.kex` |
| `2026-03-30 11:12:39` | `cowrie.login.success` |
| `2026-03-30 11:12:39` | `cowrie.session.params` |
| `2026-03-30 11:12:39` | `cowrie.command.input` |
| `2026-03-30 11:12:39` | `cowrie.log.closed` |
| `2026-03-30 11:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76720f6a45cb

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:13 |
| **Last Seen** | 2026-03-30 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:13:26` | `cowrie.session.connect` |
| `2026-03-30 11:13:26` | `cowrie.client.version` |
| `2026-03-30 11:13:26` | `cowrie.client.kex` |
| `2026-03-30 11:13:26` | `cowrie.login.success` |
| `2026-03-30 11:13:27` | `cowrie.session.params` |
| `2026-03-30 11:13:27` | `cowrie.command.input` |
| `2026-03-30 11:13:27` | `cowrie.log.closed` |
| `2026-03-30 11:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-764b206adfbd

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:13 |
| **Last Seen** | 2026-03-30 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:13:38` | `cowrie.session.connect` |
| `2026-03-30 11:13:38` | `cowrie.client.version` |
| `2026-03-30 11:13:38` | `cowrie.client.kex` |
| `2026-03-30 11:13:38` | `cowrie.login.success` |
| `2026-03-30 11:13:39` | `cowrie.session.params` |
| `2026-03-30 11:13:39` | `cowrie.command.input` |
| `2026-03-30 11:13:39` | `cowrie.log.closed` |
| `2026-03-30 11:13:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77098f87978e

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:15 |
| **Last Seen** | 2026-03-30 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:15:48` | `cowrie.session.connect` |
| `2026-03-30 11:15:48` | `cowrie.client.version` |
| `2026-03-30 11:15:49` | `cowrie.client.kex` |
| `2026-03-30 11:15:49` | `cowrie.login.success` |
| `2026-03-30 11:15:50` | `cowrie.session.params` |
| `2026-03-30 11:15:50` | `cowrie.command.input` |
| `2026-03-30 11:15:50` | `cowrie.log.closed` |
| `2026-03-30 11:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c12509c70f

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:16 |
| **Last Seen** | 2026-03-30 11:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:16:48` | `cowrie.session.connect` |
| `2026-03-30 11:16:48` | `cowrie.client.version` |
| `2026-03-30 11:16:48` | `cowrie.client.kex` |
| `2026-03-30 11:16:49` | `cowrie.login.success` |
| `2026-03-30 11:16:49` | `cowrie.session.params` |
| `2026-03-30 11:16:49` | `cowrie.command.input` |
| `2026-03-30 11:16:49` | `cowrie.log.closed` |
| `2026-03-30 11:16:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9175b43b1000

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:17 |
| **Last Seen** | 2026-03-30 11:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:17:47` | `cowrie.session.connect` |
| `2026-03-30 11:17:47` | `cowrie.client.version` |
| `2026-03-30 11:17:48` | `cowrie.client.kex` |
| `2026-03-30 11:17:48` | `cowrie.login.success` |
| `2026-03-30 11:17:49` | `cowrie.session.params` |
| `2026-03-30 11:17:49` | `cowrie.command.input` |
| `2026-03-30 11:17:49` | `cowrie.log.closed` |
| `2026-03-30 11:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b50a04f0b5c

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:17 |
| **Last Seen** | 2026-03-30 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:17:59` | `cowrie.session.connect` |
| `2026-03-30 11:17:59` | `cowrie.client.version` |
| `2026-03-30 11:17:59` | `cowrie.client.kex` |
| `2026-03-30 11:18:00` | `cowrie.login.success` |
| `2026-03-30 11:18:00` | `cowrie.session.params` |
| `2026-03-30 11:18:00` | `cowrie.command.input` |
| `2026-03-30 11:18:01` | `cowrie.log.closed` |
| `2026-03-30 11:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee6a29c4dd1

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:18 |
| **Last Seen** | 2026-03-30 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:18:23` | `cowrie.session.connect` |
| `2026-03-30 11:18:23` | `cowrie.client.version` |
| `2026-03-30 11:18:23` | `cowrie.client.kex` |
| `2026-03-30 11:18:24` | `cowrie.login.success` |
| `2026-03-30 11:18:24` | `cowrie.session.params` |
| `2026-03-30 11:18:24` | `cowrie.command.input` |
| `2026-03-30 11:18:24` | `cowrie.log.closed` |
| `2026-03-30 11:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44fc26f1fa69

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:20 |
| **Last Seen** | 2026-03-30 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:20:10` | `cowrie.session.connect` |
| `2026-03-30 11:20:10` | `cowrie.client.version` |
| `2026-03-30 11:20:10` | `cowrie.client.kex` |
| `2026-03-30 11:20:10` | `cowrie.login.success` |
| `2026-03-30 11:20:11` | `cowrie.session.params` |
| `2026-03-30 11:20:11` | `cowrie.command.input` |
| `2026-03-30 11:20:11` | `cowrie.log.closed` |
| `2026-03-30 11:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01d7c5a82e2b

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:20 |
| **Last Seen** | 2026-03-30 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:20:22` | `cowrie.session.connect` |
| `2026-03-30 11:20:22` | `cowrie.client.version` |
| `2026-03-30 11:20:22` | `cowrie.client.kex` |
| `2026-03-30 11:20:22` | `cowrie.login.success` |
| `2026-03-30 11:20:23` | `cowrie.session.params` |
| `2026-03-30 11:20:23` | `cowrie.command.input` |
| `2026-03-30 11:20:23` | `cowrie.log.closed` |
| `2026-03-30 11:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33677599b21

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:20 |
| **Last Seen** | 2026-03-30 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:20:46` | `cowrie.session.connect` |
| `2026-03-30 11:20:46` | `cowrie.client.version` |
| `2026-03-30 11:20:46` | `cowrie.client.kex` |
| `2026-03-30 11:20:46` | `cowrie.login.success` |
| `2026-03-30 11:20:47` | `cowrie.session.params` |
| `2026-03-30 11:20:47` | `cowrie.command.input` |
| `2026-03-30 11:20:47` | `cowrie.log.closed` |
| `2026-03-30 11:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af0700c6514d

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:21 |
| **Last Seen** | 2026-03-30 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:21:45` | `cowrie.session.connect` |
| `2026-03-30 11:21:45` | `cowrie.client.version` |
| `2026-03-30 11:21:45` | `cowrie.client.kex` |
| `2026-03-30 11:21:46` | `cowrie.login.success` |
| `2026-03-30 11:21:46` | `cowrie.session.params` |
| `2026-03-30 11:21:46` | `cowrie.command.input` |
| `2026-03-30 11:21:46` | `cowrie.log.closed` |
| `2026-03-30 11:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98e4603b9726

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:22 |
| **Last Seen** | 2026-03-30 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:22:44` | `cowrie.session.connect` |
| `2026-03-30 11:22:44` | `cowrie.client.version` |
| `2026-03-30 11:22:44` | `cowrie.client.kex` |
| `2026-03-30 11:22:45` | `cowrie.login.success` |
| `2026-03-30 11:22:45` | `cowrie.session.params` |
| `2026-03-30 11:22:45` | `cowrie.command.input` |
| `2026-03-30 11:22:45` | `cowrie.log.closed` |
| `2026-03-30 11:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff60b3f2285

| Field | Detail |
|---|---|
| **Source IP** | `185.118.128[.]34` |
| **First Seen** | 2026-03-30 11:23 |
| **Last Seen** | 2026-03-30 11:25 |
| **Session Duration** | 104s |
| **Login Attempts** | 3 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox FFHSB` |
| **Download Attempts** | tfxxp://5.69.112[.]58:40214/.i |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:23:40` | `cowrie.session.connect` |
| `2026-03-30 11:23:41` | `cowrie.telnet.option` |
| `2026-03-30 11:23:41` | `cowrie.login.failed` |
| `2026-03-30 11:23:41` | `cowrie.telnet.option` |
| `2026-03-30 11:23:42` | `cowrie.login.failed` |
| `2026-03-30 11:23:42` | `cowrie.telnet.option` |
| `2026-03-30 11:23:43` | `cowrie.login.success` |
| `2026-03-30 11:23:43` | `cowrie.session.params` |
| `2026-03-30 11:23:43` | `cowrie.command.input` |
| `2026-03-30 11:23:43` | `cowrie.command.input` |
| `2026-03-30 11:23:43` | `cowrie.command.failed` |
| `2026-03-30 11:23:43` | `cowrie.command.input` |
| `2026-03-30 11:23:43` | `cowrie.command.failed` |
| `2026-03-30 11:23:43` | `cowrie.command.input` |
| `2026-03-30 11:23:43` | `cowrie.command.input` |
| `2026-03-30 11:23:43` | `cowrie.command.input` |
| `2026-03-30 11:23:44` | `cowrie.command.input` |
| `2026-03-30 11:23:44` | `cowrie.command.input` |
| `2026-03-30 11:23:44` | `cowrie.command.failed` |
| `2026-03-30 11:23:44` | `cowrie.command.input` |
| `2026-03-30 11:23:44` | `cowrie.command.input` |
| `2026-03-30 11:24:06` | `cowrie.session.file_download` |
| `2026-03-30 11:25:25` | `cowrie.log.closed` |
| `2026-03-30 11:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.118.128[.]34` to AbuseIPDB if not already reported
- [ ] Block `185.118.128[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371b51ff869f

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:24 |
| **Last Seen** | 2026-03-30 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:24:55` | `cowrie.session.connect` |
| `2026-03-30 11:24:55` | `cowrie.client.version` |
| `2026-03-30 11:24:55` | `cowrie.client.kex` |
| `2026-03-30 11:24:56` | `cowrie.login.success` |
| `2026-03-30 11:24:56` | `cowrie.session.params` |
| `2026-03-30 11:24:56` | `cowrie.command.input` |
| `2026-03-30 11:24:56` | `cowrie.log.closed` |
| `2026-03-30 11:24:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e973cee660a

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:26 |
| **Last Seen** | 2026-03-30 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:26:06` | `cowrie.session.connect` |
| `2026-03-30 11:26:06` | `cowrie.client.version` |
| `2026-03-30 11:26:07` | `cowrie.client.kex` |
| `2026-03-30 11:26:07` | `cowrie.login.success` |
| `2026-03-30 11:26:08` | `cowrie.session.params` |
| `2026-03-30 11:26:08` | `cowrie.command.input` |
| `2026-03-30 11:26:08` | `cowrie.log.closed` |
| `2026-03-30 11:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ca4453173c

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:28 |
| **Last Seen** | 2026-03-30 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:28:17` | `cowrie.session.connect` |
| `2026-03-30 11:28:17` | `cowrie.client.version` |
| `2026-03-30 11:28:17` | `cowrie.client.kex` |
| `2026-03-30 11:28:18` | `cowrie.login.success` |
| `2026-03-30 11:28:18` | `cowrie.session.params` |
| `2026-03-30 11:28:18` | `cowrie.command.input` |
| `2026-03-30 11:28:19` | `cowrie.log.closed` |
| `2026-03-30 11:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017ea33e9cf1

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:28 |
| **Last Seen** | 2026-03-30 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:28:29` | `cowrie.session.connect` |
| `2026-03-30 11:28:29` | `cowrie.client.version` |
| `2026-03-30 11:28:29` | `cowrie.client.kex` |
| `2026-03-30 11:28:30` | `cowrie.login.success` |
| `2026-03-30 11:28:30` | `cowrie.session.params` |
| `2026-03-30 11:28:30` | `cowrie.command.input` |
| `2026-03-30 11:28:30` | `cowrie.log.closed` |
| `2026-03-30 11:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64c20243fefe

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:28 |
| **Last Seen** | 2026-03-30 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:28:41` | `cowrie.session.connect` |
| `2026-03-30 11:28:41` | `cowrie.client.version` |
| `2026-03-30 11:28:41` | `cowrie.client.kex` |
| `2026-03-30 11:28:41` | `cowrie.login.success` |
| `2026-03-30 11:28:42` | `cowrie.session.params` |
| `2026-03-30 11:28:42` | `cowrie.command.input` |
| `2026-03-30 11:28:42` | `cowrie.log.closed` |
| `2026-03-30 11:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bd43cc0503

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:28 |
| **Last Seen** | 2026-03-30 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:28:53` | `cowrie.session.connect` |
| `2026-03-30 11:28:53` | `cowrie.client.version` |
| `2026-03-30 11:28:53` | `cowrie.client.kex` |
| `2026-03-30 11:28:54` | `cowrie.login.success` |
| `2026-03-30 11:28:54` | `cowrie.session.params` |
| `2026-03-30 11:28:54` | `cowrie.command.input` |
| `2026-03-30 11:28:54` | `cowrie.log.closed` |
| `2026-03-30 11:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaeb98f5b936

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:29 |
| **Last Seen** | 2026-03-30 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:29:17` | `cowrie.session.connect` |
| `2026-03-30 11:29:17` | `cowrie.client.version` |
| `2026-03-30 11:29:17` | `cowrie.client.kex` |
| `2026-03-30 11:29:17` | `cowrie.login.success` |
| `2026-03-30 11:29:18` | `cowrie.session.params` |
| `2026-03-30 11:29:18` | `cowrie.command.input` |
| `2026-03-30 11:29:18` | `cowrie.log.closed` |
| `2026-03-30 11:29:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f699079068da

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:30 |
| **Last Seen** | 2026-03-30 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:30:04` | `cowrie.session.connect` |
| `2026-03-30 11:30:04` | `cowrie.client.version` |
| `2026-03-30 11:30:04` | `cowrie.client.kex` |
| `2026-03-30 11:30:05` | `cowrie.login.success` |
| `2026-03-30 11:30:05` | `cowrie.session.params` |
| `2026-03-30 11:30:05` | `cowrie.command.input` |
| `2026-03-30 11:30:05` | `cowrie.log.closed` |
| `2026-03-30 11:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44edc63ccd25

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:30 |
| **Last Seen** | 2026-03-30 11:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:30:28` | `cowrie.session.connect` |
| `2026-03-30 11:30:28` | `cowrie.client.version` |
| `2026-03-30 11:30:28` | `cowrie.client.kex` |
| `2026-03-30 11:30:28` | `cowrie.login.success` |
| `2026-03-30 11:30:28` | `cowrie.session.params` |
| `2026-03-30 11:30:28` | `cowrie.command.input` |
| `2026-03-30 11:30:29` | `cowrie.log.closed` |
| `2026-03-30 11:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3178a2b7dfe9

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:31 |
| **Last Seen** | 2026-03-30 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:31:03` | `cowrie.session.connect` |
| `2026-03-30 11:31:03` | `cowrie.client.version` |
| `2026-03-30 11:31:03` | `cowrie.client.kex` |
| `2026-03-30 11:31:04` | `cowrie.login.success` |
| `2026-03-30 11:31:04` | `cowrie.session.params` |
| `2026-03-30 11:31:04` | `cowrie.command.input` |
| `2026-03-30 11:31:05` | `cowrie.log.closed` |
| `2026-03-30 11:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871a61ea1879

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:31 |
| **Last Seen** | 2026-03-30 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:31:15` | `cowrie.session.connect` |
| `2026-03-30 11:31:15` | `cowrie.client.version` |
| `2026-03-30 11:31:15` | `cowrie.client.kex` |
| `2026-03-30 11:31:16` | `cowrie.login.success` |
| `2026-03-30 11:31:16` | `cowrie.session.params` |
| `2026-03-30 11:31:16` | `cowrie.command.input` |
| `2026-03-30 11:31:16` | `cowrie.log.closed` |
| `2026-03-30 11:31:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-076e7c3e7691

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:31 |
| **Last Seen** | 2026-03-30 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:31:51` | `cowrie.session.connect` |
| `2026-03-30 11:31:51` | `cowrie.client.version` |
| `2026-03-30 11:31:51` | `cowrie.client.kex` |
| `2026-03-30 11:31:52` | `cowrie.login.success` |
| `2026-03-30 11:31:52` | `cowrie.session.params` |
| `2026-03-30 11:31:52` | `cowrie.command.input` |
| `2026-03-30 11:31:52` | `cowrie.log.closed` |
| `2026-03-30 11:31:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2cb60ee52dd

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:32 |
| **Last Seen** | 2026-03-30 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:32:03` | `cowrie.session.connect` |
| `2026-03-30 11:32:03` | `cowrie.client.version` |
| `2026-03-30 11:32:03` | `cowrie.client.kex` |
| `2026-03-30 11:32:03` | `cowrie.login.success` |
| `2026-03-30 11:32:04` | `cowrie.session.params` |
| `2026-03-30 11:32:04` | `cowrie.command.input` |
| `2026-03-30 11:32:04` | `cowrie.log.closed` |
| `2026-03-30 11:32:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261653a95c35

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:32 |
| **Last Seen** | 2026-03-30 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:32:14` | `cowrie.session.connect` |
| `2026-03-30 11:32:14` | `cowrie.client.version` |
| `2026-03-30 11:32:15` | `cowrie.client.kex` |
| `2026-03-30 11:32:15` | `cowrie.login.success` |
| `2026-03-30 11:32:16` | `cowrie.session.params` |
| `2026-03-30 11:32:16` | `cowrie.command.input` |
| `2026-03-30 11:32:16` | `cowrie.log.closed` |
| `2026-03-30 11:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c28bc39cf6a

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:32 |
| **Last Seen** | 2026-03-30 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:32:26` | `cowrie.session.connect` |
| `2026-03-30 11:32:26` | `cowrie.client.version` |
| `2026-03-30 11:32:27` | `cowrie.client.kex` |
| `2026-03-30 11:32:27` | `cowrie.login.success` |
| `2026-03-30 11:32:28` | `cowrie.session.params` |
| `2026-03-30 11:32:28` | `cowrie.command.input` |
| `2026-03-30 11:32:28` | `cowrie.log.closed` |
| `2026-03-30 11:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f826cfeb55

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:33 |
| **Last Seen** | 2026-03-30 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:33:02` | `cowrie.session.connect` |
| `2026-03-30 11:33:02` | `cowrie.client.version` |
| `2026-03-30 11:33:02` | `cowrie.client.kex` |
| `2026-03-30 11:33:02` | `cowrie.login.success` |
| `2026-03-30 11:33:03` | `cowrie.session.params` |
| `2026-03-30 11:33:03` | `cowrie.command.input` |
| `2026-03-30 11:33:03` | `cowrie.log.closed` |
| `2026-03-30 11:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b483a9734089

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:34 |
| **Last Seen** | 2026-03-30 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:34:13` | `cowrie.session.connect` |
| `2026-03-30 11:34:13` | `cowrie.client.version` |
| `2026-03-30 11:34:13` | `cowrie.client.kex` |
| `2026-03-30 11:34:14` | `cowrie.login.success` |
| `2026-03-30 11:34:14` | `cowrie.session.params` |
| `2026-03-30 11:34:14` | `cowrie.command.input` |
| `2026-03-30 11:34:15` | `cowrie.log.closed` |
| `2026-03-30 11:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c8049c4f18

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:35 |
| **Last Seen** | 2026-03-30 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:35:36` | `cowrie.session.connect` |
| `2026-03-30 11:35:36` | `cowrie.client.version` |
| `2026-03-30 11:35:36` | `cowrie.client.kex` |
| `2026-03-30 11:35:37` | `cowrie.login.success` |
| `2026-03-30 11:35:37` | `cowrie.session.params` |
| `2026-03-30 11:35:37` | `cowrie.command.input` |
| `2026-03-30 11:35:37` | `cowrie.log.closed` |
| `2026-03-30 11:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ddd84e0be9

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:36 |
| **Last Seen** | 2026-03-30 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:36:24` | `cowrie.session.connect` |
| `2026-03-30 11:36:24` | `cowrie.client.version` |
| `2026-03-30 11:36:24` | `cowrie.client.kex` |
| `2026-03-30 11:36:25` | `cowrie.login.success` |
| `2026-03-30 11:36:25` | `cowrie.session.params` |
| `2026-03-30 11:36:25` | `cowrie.command.input` |
| `2026-03-30 11:36:25` | `cowrie.log.closed` |
| `2026-03-30 11:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406721708be2

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 11:36 |
| **Last Seen** | 2026-03-30 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 11:36:36` | `cowrie.session.connect` |
| `2026-03-30 11:36:36` | `cowrie.client.version` |
| `2026-03-30 11:36:36` | `cowrie.client.kex` |
| `2026-03-30 11:36:36` | `cowrie.login.success` |
| `2026-03-30 11:36:37` | `cowrie.session.params` |
| `2026-03-30 11:36:37` | `cowrie.command.input` |
| `2026-03-30 11:36:37` | `cowrie.log.closed` |
| `2026-03-30 11:36:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f89866a7e7c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.142[.]111` |
| **First Seen** | 2026-03-30 12:27 |
| **Last Seen** | 2026-03-30 12:27 |
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
| `2026-03-30 12:27:21` | `cowrie.session.connect` |
| `2026-03-30 12:27:21` | `cowrie.client.version` |
| `2026-03-30 12:27:21` | `cowrie.client.kex` |
| `2026-03-30 12:27:21` | `cowrie.login.success` |
| `2026-03-30 12:27:22` | `cowrie.session.params` |
| `2026-03-30 12:27:22` | `cowrie.command.input` |
| `2026-03-30 12:27:22` | `cowrie.command.failed` |
| `2026-03-30 12:27:22` | `cowrie.log.closed` |
| `2026-03-30 12:27:22` | `cowrie.session.params` |
| `2026-03-30 12:27:22` | `cowrie.command.input` |
| `2026-03-30 12:27:22` | `cowrie.session.file_download` |
| `2026-03-30 12:27:22` | `cowrie.log.closed` |
| `2026-03-30 12:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.142[.]111` to AbuseIPDB if not already reported
- [ ] Block `101.47.142[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d062a36612

| Field | Detail |
|---|---|
| **Source IP** | `101.47.142[.]111` |
| **First Seen** | 2026-03-30 12:27 |
| **Last Seen** | 2026-03-30 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 12:27:23` | `cowrie.session.connect` |
| `2026-03-30 12:27:23` | `cowrie.client.version` |
| `2026-03-30 12:27:23` | `cowrie.client.kex` |
| `2026-03-30 12:27:24` | `cowrie.login.success` |
| `2026-03-30 12:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.142[.]111` to AbuseIPDB if not already reported
- [ ] Block `101.47.142[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdf378186ac

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-03-30 13:03 |
| **Last Seen** | 2026-03-30 13:03 |
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
| `2026-03-30 13:03:45` | `cowrie.session.connect` |
| `2026-03-30 13:03:45` | `cowrie.client.version` |
| `2026-03-30 13:03:45` | `cowrie.client.kex` |
| `2026-03-30 13:03:46` | `cowrie.login.success` |
| `2026-03-30 13:03:46` | `cowrie.session.params` |
| `2026-03-30 13:03:46` | `cowrie.command.input` |
| `2026-03-30 13:03:46` | `cowrie.command.failed` |
| `2026-03-30 13:03:46` | `cowrie.log.closed` |
| `2026-03-30 13:03:47` | `cowrie.session.params` |
| `2026-03-30 13:03:47` | `cowrie.command.input` |
| `2026-03-30 13:03:47` | `cowrie.session.file_download` |
| `2026-03-30 13:03:47` | `cowrie.log.closed` |
| `2026-03-30 13:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8aabbe332783

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-03-30 13:03 |
| **Last Seen** | 2026-03-30 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 13:03:50` | `cowrie.session.connect` |
| `2026-03-30 13:03:50` | `cowrie.client.version` |
| `2026-03-30 13:03:50` | `cowrie.client.kex` |
| `2026-03-30 13:03:51` | `cowrie.login.success` |
| `2026-03-30 13:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfc5853387a

| Field | Detail |
|---|---|
| **Source IP** | `58.209.234[.]84` |
| **First Seen** | 2026-03-30 13:05 |
| **Last Seen** | 2026-03-30 13:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 13:05:02` | `cowrie.session.connect` |
| `2026-03-30 13:05:02` | `cowrie.client.version` |
| `2026-03-30 13:05:02` | `cowrie.client.kex` |
| `2026-03-30 13:05:02` | `cowrie.login.success` |
| `2026-03-30 13:05:03` | `cowrie.session.params` |
| `2026-03-30 13:05:03` | `cowrie.command.input` |
| `2026-03-30 13:05:03` | `cowrie.command.failed` |
| `2026-03-30 13:05:03` | `cowrie.log.closed` |
| `2026-03-30 13:05:03` | `cowrie.session.params` |
| `2026-03-30 13:05:03` | `cowrie.command.input` |
| `2026-03-30 13:05:03` | `cowrie.session.file_download` |
| `2026-03-30 13:05:03` | `cowrie.log.closed` |
| `2026-03-30 13:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.209.234[.]84` to AbuseIPDB if not already reported
- [ ] Block `58.209.234[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d373fed386

| Field | Detail |
|---|---|
| **Source IP** | `58.209.234[.]84` |
| **First Seen** | 2026-03-30 13:05 |
| **Last Seen** | 2026-03-30 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 13:05:11` | `cowrie.session.connect` |
| `2026-03-30 13:05:11` | `cowrie.client.version` |
| `2026-03-30 13:05:12` | `cowrie.client.kex` |
| `2026-03-30 13:05:12` | `cowrie.login.success` |
| `2026-03-30 13:05:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.209.234[.]84` to AbuseIPDB if not already reported
- [ ] Block `58.209.234[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b90ddfec5ac

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-03-30 13:07 |
| **Last Seen** | 2026-03-30 13:07 |
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
| `2026-03-30 13:07:21` | `cowrie.session.connect` |
| `2026-03-30 13:07:21` | `cowrie.client.version` |
| `2026-03-30 13:07:21` | `cowrie.client.kex` |
| `2026-03-30 13:07:22` | `cowrie.login.success` |
| `2026-03-30 13:07:22` | `cowrie.session.params` |
| `2026-03-30 13:07:22` | `cowrie.command.input` |
| `2026-03-30 13:07:22` | `cowrie.command.failed` |
| `2026-03-30 13:07:22` | `cowrie.log.closed` |
| `2026-03-30 13:07:22` | `cowrie.session.params` |
| `2026-03-30 13:07:22` | `cowrie.command.input` |
| `2026-03-30 13:07:23` | `cowrie.session.file_download` |
| `2026-03-30 13:07:23` | `cowrie.log.closed` |
| `2026-03-30 13:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4239ee8066a

| Field | Detail |
|---|---|
| **Source IP** | `160.174.129[.]232` |
| **First Seen** | 2026-03-30 13:07 |
| **Last Seen** | 2026-03-30 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 13:07:25` | `cowrie.session.connect` |
| `2026-03-30 13:07:25` | `cowrie.client.version` |
| `2026-03-30 13:07:25` | `cowrie.client.kex` |
| `2026-03-30 13:07:25` | `cowrie.login.success` |
| `2026-03-30 13:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.174.129[.]232` to AbuseIPDB if not already reported
- [ ] Block `160.174.129[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.156.67[.]84` | **144** | 2026-03-30 11:00 | 2026-03-30 11:37 | 2m | 144 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.42[.]199` | **7** | 2026-03-30 13:12 | 2026-03-30 13:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.47.142[.]111` | 1 | 2026-03-30 12:27 | 2026-03-30 12:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `105.186.155[.]165` | 1 | 2026-03-30 12:55 | 2026-03-30 12:56 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-30 12:10 | 2026-03-30 12:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.90.144[.]18` | 1 | 2026-03-30 11:48 | 2026-03-30 11:48 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.164.35[.]146` | 1 | 2026-03-30 12:22 | 2026-03-30 12:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.19.183[.]202` | 1 | 2026-03-30 11:02 | 2026-03-30 11:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-03-30 13:04 | 2026-03-30 13:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.174.129[.]232` | 1 | 2026-03-30 13:07 | 2026-03-30 13:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.22.88[.]35` | 1 | 2026-03-30 12:42 | 2026-03-30 12:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `166.130.176[.]136` | 1 | 2026-03-30 11:52 | 2026-03-30 11:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.78.240[.]94` | 1 | 2026-03-30 11:14 | 2026-03-30 11:14 | 4s | 0 | `T1592` | 🟢 LOW |
| `183.245.232[.]31` | 1 | 2026-03-30 12:48 | 2026-03-30 12:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-03-30 11:42 | 2026-03-30 11:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-30 12:02 | 2026-03-30 12:02 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.153.57[.]103` | 1 | 2026-03-30 13:03 | 2026-03-30 13:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.222.71[.]218` | 1 | 2026-03-30 12:48 | 2026-03-30 12:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.245.95[.]11` | 1 | 2026-03-30 11:22 | 2026-03-30 11:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.93.229[.]230` | 1 | 2026-03-30 11:08 | 2026-03-30 11:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.186.68[.]153` | 1 | 2026-03-30 13:02 | 2026-03-30 13:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.190.160[.]216` | 1 | 2026-03-30 11:13 | 2026-03-30 11:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `44.204.184[.]42` | 1 | 2026-03-30 12:55 | 2026-03-30 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.143.82[.]212` | 1 | 2026-03-30 11:10 | 2026-03-30 11:11 | 15s | 0 | `T1592` | 🟢 LOW |
| `49.213.194[.]139` | 1 | 2026-03-30 12:37 | 2026-03-30 12:38 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.209.234[.]84` | 1 | 2026-03-30 13:05 | 2026-03-30 13:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.20.136[.]183` | 1 | 2026-03-30 13:02 | 2026-03-30 13:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-03-30 11:28 | 2026-03-30 11:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.227.142[.]225` | 1 | 2026-03-30 12:02 | 2026-03-30 12:02 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.238.92[.]245` | 1 | 2026-03-30 12:29 | 2026-03-30 12:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.231.90[.]253` | 1 | 2026-03-30 12:28 | 2026-03-30 12:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.144.158[.]62` | 1 | 2026-03-30 13:07 | 2026-03-30 13:07 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `85.231.90[.]253` | SE | Telenor Sverige AB | **100** ⚠️ | 9 |
| `200.222.71[.]218` | BR | V tal | **100** ⚠️ | 50 |
| `31.190.160[.]216` | IT | Network and company tech merge from AS24608 into As1267 | **100** ⚠️ | 2 |
| `65.20.136[.]183` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 27 |
| `83.227.142[.]225` | SE | Telenor Sverige AB | **100** ⚠️ | 6 |
| `165.22.88[.]35` | DE | DigitalOcean, LLC | **100** ⚠️ | 6 |
| `150.139.201[.]247` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `44.204.184[.]42` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 13 |
| `222.186.68[.]153` | CN | ZHENJIANG YIQUAN HOTEL | **100** ⚠️ | 50 |
| `210.245.95[.]11` | VN | FPT Telecom Company | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 220 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 167 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 237 cases |
| Tool 34  | Credential Extractor        | ✅ 220 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 32 recon entry/entries in table (2 group(s) consolidating 151 session(s)).

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
_Report time: 2026-03-30T13:14:52Z_
