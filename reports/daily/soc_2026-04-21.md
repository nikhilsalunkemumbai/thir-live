# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-21 |
| **Generated At** | 2026-04-21T13:51:27Z |
| **Shift Time** | 13:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **119** |
| Confirmed Threats | **41** |
| False Positives Filtered | **78** (65.5%) |
| Unique Attacker IPs | **9** |
| Countries of Origin | **7** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **107** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **39** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **19** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 6 |
| `deploy` | 2 |
| `n8n` | 2 |
| `steam` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `qwe@123` | 1 |
| `git123456` | 1 |
| `tEST` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `ftpuser` | `qwe@123` | 1 |
| `git` | `git123456` | 1 |
| `test` | `tEST` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root!2025` | `43.255.118.11` | 2026-04-21T12:37:33 |
| `root` | `3245gs5662d34` | `43.255.118.11` | 2026-04-21T12:37:38 |
| `root` | `131313` | `43.255.118.11` | 2026-04-21T12:41:08 |
| `root` | `P@ssw0rd123123` | `43.255.118.11` | 2026-04-21T12:43:51 |
| `root` | `Passw0rd@2025` | `43.255.118.11` | 2026-04-21T12:44:45 |
| `root` | `222222` | `43.255.118.11` | 2026-04-21T12:49:23 |
| `root` | `innocent` | `43.255.118.11` | 2026-04-21T12:51:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **119** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 37 |
| Paramiko (Python) | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 37 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 37 | 1 | libssh-based |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.255.118.11`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **9** |
| Unique ASNs | **1** |
| High-Risk ASNs | **1** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 9 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-71ecc62c082b

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:37 |
| **Last Seen** | 2026-04-21 12:37 |
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
| `2026-04-21 12:37:32` | `cowrie.session.connect` |
| `2026-04-21 12:37:32` | `cowrie.client.version` |
| `2026-04-21 12:37:33` | `cowrie.client.kex` |
| `2026-04-21 12:37:33` | `cowrie.login.success` |
| `2026-04-21 12:37:34` | `cowrie.session.params` |
| `2026-04-21 12:37:34` | `cowrie.command.input` |
| `2026-04-21 12:37:34` | `cowrie.command.failed` |
| `2026-04-21 12:37:34` | `cowrie.log.closed` |
| `2026-04-21 12:37:35` | `cowrie.session.params` |
| `2026-04-21 12:37:35` | `cowrie.command.input` |
| `2026-04-21 12:37:35` | `cowrie.session.file_download` |
| `2026-04-21 12:37:35` | `cowrie.log.closed` |
| `2026-04-21 12:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1922ccb59afc

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:37 |
| **Last Seen** | 2026-04-21 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 12:37:37` | `cowrie.session.connect` |
| `2026-04-21 12:37:37` | `cowrie.client.version` |
| `2026-04-21 12:37:38` | `cowrie.client.kex` |
| `2026-04-21 12:37:38` | `cowrie.login.success` |
| `2026-04-21 12:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ccaab8f2fb0

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:41 |
| **Last Seen** | 2026-04-21 12:41 |
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
| `2026-04-21 12:41:07` | `cowrie.session.connect` |
| `2026-04-21 12:41:07` | `cowrie.client.version` |
| `2026-04-21 12:41:07` | `cowrie.client.kex` |
| `2026-04-21 12:41:08` | `cowrie.login.success` |
| `2026-04-21 12:41:08` | `cowrie.session.params` |
| `2026-04-21 12:41:08` | `cowrie.command.input` |
| `2026-04-21 12:41:08` | `cowrie.command.failed` |
| `2026-04-21 12:41:08` | `cowrie.log.closed` |
| `2026-04-21 12:41:09` | `cowrie.session.params` |
| `2026-04-21 12:41:09` | `cowrie.command.input` |
| `2026-04-21 12:41:09` | `cowrie.session.file_download` |
| `2026-04-21 12:41:09` | `cowrie.log.closed` |
| `2026-04-21 12:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95adf9510ec

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:41 |
| **Last Seen** | 2026-04-21 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 12:41:12` | `cowrie.session.connect` |
| `2026-04-21 12:41:12` | `cowrie.client.version` |
| `2026-04-21 12:41:12` | `cowrie.client.kex` |
| `2026-04-21 12:41:13` | `cowrie.login.success` |
| `2026-04-21 12:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b0bf707ff2

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:43 |
| **Last Seen** | 2026-04-21 12:43 |
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
| `2026-04-21 12:43:50` | `cowrie.session.connect` |
| `2026-04-21 12:43:50` | `cowrie.client.version` |
| `2026-04-21 12:43:50` | `cowrie.client.kex` |
| `2026-04-21 12:43:51` | `cowrie.login.success` |
| `2026-04-21 12:43:51` | `cowrie.session.params` |
| `2026-04-21 12:43:51` | `cowrie.command.input` |
| `2026-04-21 12:43:51` | `cowrie.command.failed` |
| `2026-04-21 12:43:52` | `cowrie.log.closed` |
| `2026-04-21 12:43:52` | `cowrie.session.params` |
| `2026-04-21 12:43:52` | `cowrie.command.input` |
| `2026-04-21 12:43:52` | `cowrie.session.file_download` |
| `2026-04-21 12:43:52` | `cowrie.log.closed` |
| `2026-04-21 12:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18541384b4c1

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:43 |
| **Last Seen** | 2026-04-21 12:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 12:43:55` | `cowrie.session.connect` |
| `2026-04-21 12:43:55` | `cowrie.client.version` |
| `2026-04-21 12:43:55` | `cowrie.client.kex` |
| `2026-04-21 12:43:56` | `cowrie.login.success` |
| `2026-04-21 12:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae86cc78ba85

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:44 |
| **Last Seen** | 2026-04-21 12:44 |
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
| `2026-04-21 12:44:44` | `cowrie.session.connect` |
| `2026-04-21 12:44:44` | `cowrie.client.version` |
| `2026-04-21 12:44:44` | `cowrie.client.kex` |
| `2026-04-21 12:44:45` | `cowrie.login.success` |
| `2026-04-21 12:44:45` | `cowrie.session.params` |
| `2026-04-21 12:44:45` | `cowrie.command.input` |
| `2026-04-21 12:44:45` | `cowrie.command.failed` |
| `2026-04-21 12:44:45` | `cowrie.log.closed` |
| `2026-04-21 12:44:46` | `cowrie.session.params` |
| `2026-04-21 12:44:46` | `cowrie.command.input` |
| `2026-04-21 12:44:46` | `cowrie.session.file_download` |
| `2026-04-21 12:44:46` | `cowrie.log.closed` |
| `2026-04-21 12:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4473f0611d11

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:44 |
| **Last Seen** | 2026-04-21 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 12:44:49` | `cowrie.session.connect` |
| `2026-04-21 12:44:49` | `cowrie.client.version` |
| `2026-04-21 12:44:49` | `cowrie.client.kex` |
| `2026-04-21 12:44:50` | `cowrie.login.success` |
| `2026-04-21 12:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1a8f2dd4b2

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:49 |
| **Last Seen** | 2026-04-21 12:49 |
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
| `2026-04-21 12:49:22` | `cowrie.session.connect` |
| `2026-04-21 12:49:22` | `cowrie.client.version` |
| `2026-04-21 12:49:22` | `cowrie.client.kex` |
| `2026-04-21 12:49:23` | `cowrie.login.success` |
| `2026-04-21 12:49:23` | `cowrie.session.params` |
| `2026-04-21 12:49:23` | `cowrie.command.input` |
| `2026-04-21 12:49:23` | `cowrie.command.failed` |
| `2026-04-21 12:49:24` | `cowrie.log.closed` |
| `2026-04-21 12:49:24` | `cowrie.session.params` |
| `2026-04-21 12:49:24` | `cowrie.command.input` |
| `2026-04-21 12:49:24` | `cowrie.session.file_download` |
| `2026-04-21 12:49:24` | `cowrie.log.closed` |
| `2026-04-21 12:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad88c472c927

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:49 |
| **Last Seen** | 2026-04-21 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 12:49:27` | `cowrie.session.connect` |
| `2026-04-21 12:49:27` | `cowrie.client.version` |
| `2026-04-21 12:49:27` | `cowrie.client.kex` |
| `2026-04-21 12:49:28` | `cowrie.login.success` |
| `2026-04-21 12:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-424610655d4c

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:51 |
| **Last Seen** | 2026-04-21 12:51 |
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
| `2026-04-21 12:51:06` | `cowrie.session.connect` |
| `2026-04-21 12:51:06` | `cowrie.client.version` |
| `2026-04-21 12:51:06` | `cowrie.client.kex` |
| `2026-04-21 12:51:07` | `cowrie.login.success` |
| `2026-04-21 12:51:08` | `cowrie.session.params` |
| `2026-04-21 12:51:08` | `cowrie.command.input` |
| `2026-04-21 12:51:08` | `cowrie.command.failed` |
| `2026-04-21 12:51:08` | `cowrie.log.closed` |
| `2026-04-21 12:51:08` | `cowrie.session.params` |
| `2026-04-21 12:51:08` | `cowrie.command.input` |
| `2026-04-21 12:51:09` | `cowrie.session.file_download` |
| `2026-04-21 12:51:09` | `cowrie.log.closed` |
| `2026-04-21 12:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28ba25f2be71

| Field | Detail |
|---|---|
| **Source IP** | `43.255.118[.]11` |
| **First Seen** | 2026-04-21 12:51 |
| **Last Seen** | 2026-04-21 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 12:51:11` | `cowrie.session.connect` |
| `2026-04-21 12:51:11` | `cowrie.client.version` |
| `2026-04-21 12:51:12` | `cowrie.client.kex` |
| `2026-04-21 12:51:12` | `cowrie.login.success` |
| `2026-04-21 12:51:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.255.118[.]11` to AbuseIPDB if not already reported
- [ ] Block `43.255.118[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `43.255.118[.]11` | **25** | 2026-04-21 12:28 | 2026-04-21 12:54 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `100.26.45[.]212` | 1 | 2026-04-21 12:55 | 2026-04-21 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `109.105.210[.]92` | 1 | 2026-04-21 13:01 | 2026-04-21 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.56.235[.]140` | 1 | 2026-04-21 13:48 | 2026-04-21 13:49 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `94.156.14[.]80` | 1 | 2026-04-21 12:37 | 2026-04-21 12:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
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
| `94.156.14[.]80` | RO | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 7 |
| `43.255.118[.]11` | HK | SHATIN TELECOM (HONGKONG) LIMITED | **100** ⚠️ | 4 |
| `100.26.45[.]212` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 19 |
| `183.56.235[.]140` | CN | CHINANET Guangdong province network | **100** ⚠️ | 27 |
| `109.105.210[.]92` | US | ICG-ZEN-DFW | **100** ⚠️ | 48 |
| `132.248.44[.]87` | MX | Universidad Nacional Autonoma de Mexico | **77** | 50 |
| `103.72.9[.]120` | IN | SWIFTIFY PRIVATE LIMITED | **49** | 0 |
| `222.252.31[.]106` | VN | Hanoi Post and Telecom Company | **42** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 39 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (78 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 77 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 119 cases |
| Tool 34  | Credential Extractor        | ✅ 39 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 9 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 78 filtered (65.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 1 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 5 recon entry/entries in table (1 group(s) consolidating 25 session(s)).

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
_Report time: 2026-04-21T13:51:27Z_
