# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T20:36:35Z |
| **Shift Time** | 20:36 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **76** |
| Confirmed Threats | **71** |
| False Positives Filtered | **5** (6.6%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **12** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **71** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **54** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **38** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 11 |
| `root` | 5 |
| `345gs5662d34` | 2 |
| `Test` | 2 |
| `Nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 4 |
| `12345` | 4 |
| `123` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `Nobody` | `123abc` | 1 |
| `ubuntu` | `Asd!@#` | 1 |
| `ubuntu` | `ASD!@#` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `2011` | `190.0.63.226` | 2026-03-23T19:21:20 |
| `root` | `3245gs5662d34` | `190.0.63.226` | 2026-03-23T19:21:27 |
| `root` | `User@123` | `58.33.97.119` | 2026-03-23T19:25:36 |
| `root` | `123qwe,.` | `187.94.255.130` | 2026-03-23T19:37:56 |
| `root` | `3245gs5662d34` | `187.94.255.130` | 2026-03-23T19:38:03 |

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
echo "root:RQfw0VGOaKvK"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `58.33.97.119`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `187.94.255.130`, `190.0.63.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **17** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4812` | China Telecom (Group) | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |
| `AS10439` | CariNet, Inc. | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |
| `AS9269` | Hong Kong Broadband Network Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7cdc9e8de25d

| Field | Detail |
|---|---|
| **Source IP** | `190.0.63[.]226` |
| **First Seen** | 2026-03-23 19:21 |
| **Last Seen** | 2026-03-23 19:21 |
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
| `2026-03-23 19:21:19` | `cowrie.session.connect` |
| `2026-03-23 19:21:19` | `cowrie.client.version` |
| `2026-03-23 19:21:19` | `cowrie.client.kex` |
| `2026-03-23 19:21:20` | `cowrie.login.success` |
| `2026-03-23 19:21:21` | `cowrie.session.params` |
| `2026-03-23 19:21:21` | `cowrie.command.input` |
| `2026-03-23 19:21:21` | `cowrie.command.failed` |
| `2026-03-23 19:21:21` | `cowrie.log.closed` |
| `2026-03-23 19:21:22` | `cowrie.session.params` |
| `2026-03-23 19:21:22` | `cowrie.command.input` |
| `2026-03-23 19:21:22` | `cowrie.session.file_download` |
| `2026-03-23 19:21:22` | `cowrie.log.closed` |
| `2026-03-23 19:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.0.63[.]226` to AbuseIPDB if not already reported
- [ ] Block `190.0.63[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67eb44dc90d4

| Field | Detail |
|---|---|
| **Source IP** | `190.0.63[.]226` |
| **First Seen** | 2026-03-23 19:21 |
| **Last Seen** | 2026-03-23 19:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 19:21:26` | `cowrie.session.connect` |
| `2026-03-23 19:21:26` | `cowrie.client.version` |
| `2026-03-23 19:21:26` | `cowrie.client.kex` |
| `2026-03-23 19:21:27` | `cowrie.login.success` |
| `2026-03-23 19:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.0.63[.]226` to AbuseIPDB if not already reported
- [ ] Block `190.0.63[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f5ecf0f85c

| Field | Detail |
|---|---|
| **Source IP** | `58.33.97[.]119` |
| **First Seen** | 2026-03-23 19:25 |
| **Last Seen** | 2026-03-23 19:25 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RQfw0VGOaKvK"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 19:25:36` | `cowrie.session.connect` |
| `2026-03-23 19:25:36` | `cowrie.client.version` |
| `2026-03-23 19:25:36` | `cowrie.client.kex` |
| `2026-03-23 19:25:36` | `cowrie.login.success` |
| `2026-03-23 19:25:37` | `cowrie.session.params` |
| `2026-03-23 19:25:37` | `cowrie.command.input` |
| `2026-03-23 19:25:37` | `cowrie.command.failed` |
| `2026-03-23 19:25:37` | `cowrie.log.closed` |
| `2026-03-23 19:25:37` | `cowrie.session.params` |
| `2026-03-23 19:25:37` | `cowrie.command.input` |
| `2026-03-23 19:25:37` | `cowrie.session.file_download` |
| `2026-03-23 19:25:37` | `cowrie.log.closed` |
| `2026-03-23 19:25:50` | `cowrie.session.params` |
| `2026-03-23 19:25:50` | `cowrie.command.input` |
| `2026-03-23 19:25:51` | `cowrie.log.closed` |
| `2026-03-23 19:25:51` | `cowrie.session.params` |
| `2026-03-23 19:25:51` | `cowrie.command.input` |
| `2026-03-23 19:25:51` | `cowrie.log.closed` |
| `2026-03-23 19:25:51` | `cowrie.session.params` |
| `2026-03-23 19:25:51` | `cowrie.command.input` |
| `2026-03-23 19:25:51` | `cowrie.session.file_download` |
| `2026-03-23 19:25:51` | `cowrie.log.closed` |
| `2026-03-23 19:25:52` | `cowrie.session.params` |
| `2026-03-23 19:25:52` | `cowrie.command.input` |
| `2026-03-23 19:25:52` | `cowrie.log.closed` |
| `2026-03-23 19:25:52` | `cowrie.session.params` |
| `2026-03-23 19:25:52` | `cowrie.command.input` |
| `2026-03-23 19:25:52` | `cowrie.log.closed` |
| `2026-03-23 19:25:53` | `cowrie.session.params` |
| `2026-03-23 19:25:53` | `cowrie.command.input` |
| `2026-03-23 19:25:53` | `cowrie.command.input` |
| `2026-03-23 19:25:53` | `cowrie.log.closed` |
| `2026-03-23 19:25:53` | `cowrie.session.params` |
| `2026-03-23 19:25:53` | `cowrie.command.input` |
| `2026-03-23 19:25:53` | `cowrie.log.closed` |
| `2026-03-23 19:25:54` | `cowrie.session.params` |
| `2026-03-23 19:25:54` | `cowrie.command.input` |
| `2026-03-23 19:25:54` | `cowrie.log.closed` |
| `2026-03-23 19:25:54` | `cowrie.session.params` |
| `2026-03-23 19:25:54` | `cowrie.command.input` |
| `2026-03-23 19:25:54` | `cowrie.log.closed` |
| `2026-03-23 19:25:54` | `cowrie.session.params` |
| `2026-03-23 19:25:54` | `cowrie.command.input` |
| `2026-03-23 19:25:55` | `cowrie.log.closed` |
| `2026-03-23 19:25:55` | `cowrie.session.params` |
| `2026-03-23 19:25:55` | `cowrie.command.input` |
| `2026-03-23 19:25:55` | `cowrie.log.closed` |
| `2026-03-23 19:25:55` | `cowrie.session.params` |
| `2026-03-23 19:25:55` | `cowrie.command.input` |
| `2026-03-23 19:25:55` | `cowrie.log.closed` |
| `2026-03-23 19:25:56` | `cowrie.session.params` |
| `2026-03-23 19:25:56` | `cowrie.command.input` |
| `2026-03-23 19:25:56` | `cowrie.log.closed` |
| `2026-03-23 19:25:56` | `cowrie.session.params` |
| `2026-03-23 19:25:56` | `cowrie.command.input` |
| `2026-03-23 19:25:56` | `cowrie.log.closed` |
| `2026-03-23 19:25:57` | `cowrie.session.params` |
| `2026-03-23 19:25:57` | `cowrie.command.input` |
| `2026-03-23 19:25:57` | `cowrie.log.closed` |
| `2026-03-23 19:25:57` | `cowrie.session.params` |
| `2026-03-23 19:25:57` | `cowrie.command.input` |
| `2026-03-23 19:25:57` | `cowrie.log.closed` |
| `2026-03-23 19:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.33.97[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.33.97[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7185977868ee

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-03-23 19:37 |
| **Last Seen** | 2026-03-23 19:38 |
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
| `2026-03-23 19:37:54` | `cowrie.session.connect` |
| `2026-03-23 19:37:54` | `cowrie.client.version` |
| `2026-03-23 19:37:54` | `cowrie.client.kex` |
| `2026-03-23 19:37:56` | `cowrie.login.success` |
| `2026-03-23 19:37:56` | `cowrie.session.params` |
| `2026-03-23 19:37:56` | `cowrie.command.input` |
| `2026-03-23 19:37:56` | `cowrie.command.failed` |
| `2026-03-23 19:37:57` | `cowrie.log.closed` |
| `2026-03-23 19:37:57` | `cowrie.session.params` |
| `2026-03-23 19:37:57` | `cowrie.command.input` |
| `2026-03-23 19:37:58` | `cowrie.session.file_download` |
| `2026-03-23 19:37:58` | `cowrie.log.closed` |
| `2026-03-23 19:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08c05308f646

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-03-23 19:38 |
| **Last Seen** | 2026-03-23 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 19:38:01` | `cowrie.session.connect` |
| `2026-03-23 19:38:01` | `cowrie.client.version` |
| `2026-03-23 19:38:01` | `cowrie.client.kex` |
| `2026-03-23 19:38:03` | `cowrie.login.success` |
| `2026-03-23 19:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `187.94.255[.]130` | **15** | 2026-03-23 19:13 | 2026-03-23 19:46 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.81.33[.]183` | **13** | 2026-03-23 18:55 | 2026-03-23 20:35 | 5m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.33.97[.]119` | **10** | 2026-03-23 19:24 | 2026-03-23 19:33 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.0.63[.]226` | **6** | 2026-03-23 19:14 | 2026-03-23 19:25 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]233` | **5** | 2026-03-23 19:24 | 2026-03-23 19:28 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.149[.]158` | **5** | 2026-03-23 19:27 | 2026-03-23 19:37 | 6m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `36.95.194[.]52` | **2** | 2026-03-23 19:24 | 2026-03-23 19:27 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `68.7.114[.]69` | **2** | 2026-03-23 19:49 | 2026-03-23 19:53 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `118.212.37[.]145` | 1 | 2026-03-23 20:08 | 2026-03-23 20:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `173.12.128[.]65` | 1 | 2026-03-23 19:30 | 2026-03-23 19:30 | 34s | 0 | `T1592` | 🟢 LOW |
| `180.168.119[.]2` | 1 | 2026-03-23 20:11 | 2026-03-23 20:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.236[.]113` | 1 | 2026-03-23 19:46 | 2026-03-23 19:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `183.171.44[.]82` | 1 | 2026-03-23 20:26 | 2026-03-23 20:26 | 13s | 0 | `T1592` | 🟢 LOW |
| `51.83.68[.]69` | 1 | 2026-03-23 20:08 | 2026-03-23 20:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-03-23 19:39 | 2026-03-23 19:39 | 10s | 0 | `T1592` | 🟢 LOW |
| `92.100.187[.]157` | 1 | 2026-03-23 19:50 | 2026-03-23 19:50 | 7s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `14.103.149[.]158` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 31 |
| `92.100.187[.]157` | RU | St.Petersburg Telephone Network | **100** ⚠️ | 0 |
| `51.83.68[.]69` | FR | OVH SAS | **100** ⚠️ | 0 |
| `187.94.255[.]130` | BR | VITAL NET | **100** ⚠️ | 39 |
| `36.95.194[.]52` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 29 |
| `118.212.37[.]145` | CN | China Unicom Jiangxi province network | **100** ⚠️ | 30 |
| `68.7.114[.]69` | US | Cox Communications Inc. | **100** ⚠️ | 17 |
| `183.171.44[.]82` | MY | Celcom Axiata Berhad | **100** ⚠️ | 4 |
| `66.240.223[.]240` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `180.168.119[.]2` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 47 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 70 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 49 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 76 cases |
| Tool 34  | Credential Extractor        | ✅ 54 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (6.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 16 recon entry/entries in table (8 group(s) consolidating 58 session(s)).

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
_Report time: 2026-03-23T20:36:35Z_
