# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-27 |
| **Generated At** | 2026-04-27T21:07:44Z |
| **Shift Time** | 21:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **494** |
| Confirmed Threats | **462** |
| False Positives Filtered | **32** (6.5%) |
| Unique Attacker IPs | **22** |
| Countries of Origin | **13** |
| High Severity Cases | **8** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **486** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **11** |
| Unique Credential Pairs | **6** |
| Unique Usernames | **2** |
| Unique Passwords | **6** |
| Successful Auth Pairs | **7** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 8 |
| `345gs5662d34` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `` | 2 |
| `124578` | 1 |
| `mY123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `` | 2 |
| `root` | `124578` | 1 |
| `root` | `mY123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `124578` | `119.92.70.82` | 2026-04-27T19:43:14 |
| `root` | `3245gs5662d34` | `119.92.70.82` | 2026-04-27T19:43:18 |
| `root` | `mY123456` | `189.194.140.170` | 2026-04-27T19:48:40 |
| `root` | `3245gs5662d34` | `189.194.140.170` | 2026-04-27T19:48:47 |
| `root` | `` | `31.56.209.39` | 2026-04-27T20:09:49 |
| `root` | `QWERTY12345` | `34.93.128.179` | 2026-04-27T20:41:17 |
| `root` | `3245gs5662d34` | `34.93.128.179` | 2026-04-27T20:41:18 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **494** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 12 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 9 | 3 |
| `c118de82e19e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 9 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `c118de82e19e...` | OpenSSH | 2 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.93.128.179`, `119.92.70.82`, `189.194.140.170`

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
| `AS37133` | Airtel Tanzania | 3 | LOW |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS3326` | Datagroup PJSC | 1 | LOW |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | HIGH |
| `AS7679` | QTnet,Inc. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS56044` | China Mobile communications corporation | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (8)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-567f60d16fb0

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-04-27 19:43 |
| **Last Seen** | 2026-04-27 19:43 |
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
| `2026-04-27 19:43:14` | `cowrie.session.connect` |
| `2026-04-27 19:43:14` | `cowrie.client.version` |
| `2026-04-27 19:43:14` | `cowrie.client.kex` |
| `2026-04-27 19:43:14` | `cowrie.login.success` |
| `2026-04-27 19:43:15` | `cowrie.session.params` |
| `2026-04-27 19:43:15` | `cowrie.command.input` |
| `2026-04-27 19:43:15` | `cowrie.command.failed` |
| `2026-04-27 19:43:15` | `cowrie.log.closed` |
| `2026-04-27 19:43:15` | `cowrie.session.params` |
| `2026-04-27 19:43:15` | `cowrie.command.input` |
| `2026-04-27 19:43:15` | `cowrie.session.file_download` |
| `2026-04-27 19:43:15` | `cowrie.log.closed` |
| `2026-04-27 19:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea209340a62

| Field | Detail |
|---|---|
| **Source IP** | `119.92.70[.]82` |
| **First Seen** | 2026-04-27 19:43 |
| **Last Seen** | 2026-04-27 19:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 19:43:17` | `cowrie.session.connect` |
| `2026-04-27 19:43:17` | `cowrie.client.version` |
| `2026-04-27 19:43:17` | `cowrie.client.kex` |
| `2026-04-27 19:43:18` | `cowrie.login.success` |
| `2026-04-27 19:43:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.92.70[.]82` to AbuseIPDB if not already reported
- [ ] Block `119.92.70[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02df1cf2ff4f

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-27 19:48 |
| **Last Seen** | 2026-04-27 19:48 |
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
| `2026-04-27 19:48:38` | `cowrie.session.connect` |
| `2026-04-27 19:48:38` | `cowrie.client.version` |
| `2026-04-27 19:48:39` | `cowrie.client.kex` |
| `2026-04-27 19:48:40` | `cowrie.login.success` |
| `2026-04-27 19:48:41` | `cowrie.session.params` |
| `2026-04-27 19:48:41` | `cowrie.command.input` |
| `2026-04-27 19:48:41` | `cowrie.command.failed` |
| `2026-04-27 19:48:41` | `cowrie.log.closed` |
| `2026-04-27 19:48:42` | `cowrie.session.params` |
| `2026-04-27 19:48:42` | `cowrie.command.input` |
| `2026-04-27 19:48:42` | `cowrie.session.file_download` |
| `2026-04-27 19:48:42` | `cowrie.log.closed` |
| `2026-04-27 19:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce5176a36dc

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-27 19:48 |
| **Last Seen** | 2026-04-27 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 19:48:45` | `cowrie.session.connect` |
| `2026-04-27 19:48:45` | `cowrie.client.version` |
| `2026-04-27 19:48:46` | `cowrie.client.kex` |
| `2026-04-27 19:48:47` | `cowrie.login.success` |
| `2026-04-27 19:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab8051f679e

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-27 20:09 |
| **Last Seen** | 2026-04-27 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 20:09:48` | `cowrie.session.connect` |
| `2026-04-27 20:09:48` | `cowrie.client.version` |
| `2026-04-27 20:09:49` | `cowrie.client.kex` |
| `2026-04-27 20:09:49` | `cowrie.login.success` |
| `2026-04-27 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f852fdc68e03

| Field | Detail |
|---|---|
| **Source IP** | `31.56.209[.]39` |
| **First Seen** | 2026-04-27 20:09 |
| **Last Seen** | 2026-04-27 20:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 20:09:48` | `cowrie.session.connect` |
| `2026-04-27 20:09:48` | `cowrie.client.version` |
| `2026-04-27 20:09:49` | `cowrie.client.kex` |
| `2026-04-27 20:09:49` | `cowrie.login.success` |
| `2026-04-27 20:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.209[.]39` to AbuseIPDB if not already reported
- [ ] Block `31.56.209[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93ea6bfa352

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-04-27 20:41 |
| **Last Seen** | 2026-04-27 20:41 |
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
| `2026-04-27 20:41:17` | `cowrie.session.connect` |
| `2026-04-27 20:41:17` | `cowrie.client.version` |
| `2026-04-27 20:41:17` | `cowrie.client.kex` |
| `2026-04-27 20:41:17` | `cowrie.login.success` |
| `2026-04-27 20:41:17` | `cowrie.session.params` |
| `2026-04-27 20:41:17` | `cowrie.command.input` |
| `2026-04-27 20:41:17` | `cowrie.command.failed` |
| `2026-04-27 20:41:17` | `cowrie.log.closed` |
| `2026-04-27 20:41:17` | `cowrie.session.params` |
| `2026-04-27 20:41:17` | `cowrie.command.input` |
| `2026-04-27 20:41:17` | `cowrie.session.file_download` |
| `2026-04-27 20:41:17` | `cowrie.log.closed` |
| `2026-04-27 20:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe692b4ff29

| Field | Detail |
|---|---|
| **Source IP** | `34.93.128[.]179` |
| **First Seen** | 2026-04-27 20:41 |
| **Last Seen** | 2026-04-27 20:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 20:41:18` | `cowrie.session.connect` |
| `2026-04-27 20:41:18` | `cowrie.client.version` |
| `2026-04-27 20:41:18` | `cowrie.client.kex` |
| `2026-04-27 20:41:18` | `cowrie.login.success` |
| `2026-04-27 20:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.93.128[.]179` to AbuseIPDB if not already reported
- [ ] Block `34.93.128[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `39.152.6[.]7` | **441** | 2026-04-27 20:21 | 2026-04-27 20:22 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `18.219.193[.]156` | **3** | 2026-04-27 19:51 | 2026-04-27 19:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.89.148[.]7` | 1 | 2026-04-27 20:55 | 2026-04-27 20:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `119.47.179[.]44` | 1 | 2026-04-27 20:44 | 2026-04-27 20:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `119.92.70[.]82` | 1 | 2026-04-27 19:43 | 2026-04-27 19:43 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.78[.]222` | 1 | 2026-04-27 20:47 | 2026-04-27 20:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `147.147.21[.]171` | 1 | 2026-04-27 20:42 | 2026-04-27 20:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.194.140[.]170` | 1 | 2026-04-27 19:48 | 2026-04-27 19:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.93.128[.]179` | 1 | 2026-04-27 20:41 | 2026-04-27 20:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.71.184[.]62` | 1 | 2026-04-27 20:07 | 2026-04-27 20:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `72.186.202[.]53` | 1 | 2026-04-27 21:04 | 2026-04-27 21:04 | 12s | 0 | `T1592` | 🟢 LOW |
| `92.25.195[.]48` | 1 | 2026-04-27 20:15 | 2026-04-27 20:17 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `120.48.78[.]222` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 2 |
| `72.186.202[.]53` | US | Charter Communications Inc | **100** ⚠️ | 7 |
| `147.147.21[.]171` | GB | Plusnet PLC | **100** ⚠️ | 0 |
| `189.194.140[.]170` | MX | Mega Cable, S.A. de C.V. | **100** ⚠️ | 50 |
| `92.25.195[.]48` | GB | TalkTalk Communications Limited | **100** ⚠️ | 4 |
| `39.152.6[.]7` | CN | China Mobile Communications Corporation | **100** ⚠️ | 15 |
| `34.93.128[.]179` | IN | Google LLC | **100** ⚠️ | 50 |
| `119.92.70[.]82` | PH | IPG | **100** ⚠️ | 50 |
| `119.47.179[.]44` | JP | QTnet, Inc. | **100** ⚠️ | 0 |
| `101.89.148[.]7` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 8 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 12 |
| AbuseIPDB score 10 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 494 cases |
| Tool 34  | Credential Extractor        | ✅ 11 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 22 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (6.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 19 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 8 priority case(s) shown individually · 12 recon entry/entries in table (2 group(s) consolidating 444 session(s)).

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
_Report time: 2026-04-27T21:07:44Z_
