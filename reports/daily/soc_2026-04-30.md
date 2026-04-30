# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-30 |
| **Generated At** | 2026-04-30T19:28:33Z |
| **Shift Time** | 19:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **386** |
| Confirmed Threats | **64** |
| False Positives Filtered | **322** (83.4%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **17** |
| High Severity Cases | **18** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **368** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **50** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **17** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 18 |
| `345gs5662d34` | 9 |
| `postgres` | 3 |
| `test` | 3 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `test` | 2 |
| `Admin@123` | 1 |
| `1` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 9 |
| `odoo` | `Admin@123` | 1 |
| `ts3` | `1` | 1 |
| `newftpuser` | `newftpuser123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ali` | `43.130.90.166` | 2026-04-30T18:20:26 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-04-30T18:20:32 |
| `root` | `adminserver` | `43.130.90.166` | 2026-04-30T18:21:53 |
| `root` | `test` | `43.130.90.166` | 2026-04-30T18:24:05 |
| `root` | `oracleadmin` | `43.130.90.166` | 2026-04-30T18:27:41 |
| `root` | `reza` | `43.130.90.166` | 2026-04-30T18:29:13 |
| `root` | `rootadmin` | `43.130.90.166` | 2026-04-30T18:31:22 |
| `root` | `test2019` | `43.130.90.166` | 2026-04-30T18:35:01 |
| `root` | `123India` | `195.178.191.5` | 2026-04-30T18:51:15 |
| `root` | `3245gs5662d34` | `195.178.191.5` | 2026-04-30T18:51:19 |
| `root` | `ww123456` | `144.48.243.18` | 2026-04-30T19:02:45 |
| `root` | `3245gs5662d34` | `144.48.243.18` | 2026-04-30T19:02:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **386** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 53 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 44 | 1 |
| `af8223ac9914...` | libssh-based | 7 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 44 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 7 | 3 | libssh-based |
| `95420f9d932d...` | libssh | 2 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `144.48.243.18`, `195.178.191.5`, `43.130.90.166`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **26** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS135799` | Rapidnet Private Limited | 2 | LOW |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS8473` | Bahnhof AB | 1 | HIGH |
| `AS49635` | CLOUDI NEXTGEN SL | 1 | LOW |
| `AS55286` | B2 Net Solutions Inc. | 1 | LOW |
| `AS24544` | Overcasts Limited | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-437d16fa28f4

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:20 |
| **Last Seen** | 2026-04-30 18:20 |
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
| `2026-04-30 18:20:25` | `cowrie.session.connect` |
| `2026-04-30 18:20:25` | `cowrie.client.version` |
| `2026-04-30 18:20:25` | `cowrie.client.kex` |
| `2026-04-30 18:20:26` | `cowrie.login.success` |
| `2026-04-30 18:20:27` | `cowrie.session.params` |
| `2026-04-30 18:20:27` | `cowrie.command.input` |
| `2026-04-30 18:20:27` | `cowrie.command.failed` |
| `2026-04-30 18:20:27` | `cowrie.log.closed` |
| `2026-04-30 18:20:28` | `cowrie.session.params` |
| `2026-04-30 18:20:28` | `cowrie.command.input` |
| `2026-04-30 18:20:28` | `cowrie.session.file_download` |
| `2026-04-30 18:20:28` | `cowrie.log.closed` |
| `2026-04-30 18:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b19727f104

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:20 |
| **Last Seen** | 2026-04-30 18:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:20:31` | `cowrie.session.connect` |
| `2026-04-30 18:20:31` | `cowrie.client.version` |
| `2026-04-30 18:20:31` | `cowrie.client.kex` |
| `2026-04-30 18:20:32` | `cowrie.login.success` |
| `2026-04-30 18:20:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4616d6830c67

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:21 |
| **Last Seen** | 2026-04-30 18:22 |
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
| `2026-04-30 18:21:52` | `cowrie.session.connect` |
| `2026-04-30 18:21:52` | `cowrie.client.version` |
| `2026-04-30 18:21:52` | `cowrie.client.kex` |
| `2026-04-30 18:21:53` | `cowrie.login.success` |
| `2026-04-30 18:21:54` | `cowrie.session.params` |
| `2026-04-30 18:21:54` | `cowrie.command.input` |
| `2026-04-30 18:21:54` | `cowrie.command.failed` |
| `2026-04-30 18:21:54` | `cowrie.log.closed` |
| `2026-04-30 18:21:55` | `cowrie.session.params` |
| `2026-04-30 18:21:55` | `cowrie.command.input` |
| `2026-04-30 18:21:55` | `cowrie.session.file_download` |
| `2026-04-30 18:21:55` | `cowrie.log.closed` |
| `2026-04-30 18:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3518845fc2ab

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:21 |
| **Last Seen** | 2026-04-30 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:21:58` | `cowrie.session.connect` |
| `2026-04-30 18:21:58` | `cowrie.client.version` |
| `2026-04-30 18:21:58` | `cowrie.client.kex` |
| `2026-04-30 18:21:59` | `cowrie.login.success` |
| `2026-04-30 18:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc896eb0da7

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:24 |
| **Last Seen** | 2026-04-30 18:24 |
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
| `2026-04-30 18:24:04` | `cowrie.session.connect` |
| `2026-04-30 18:24:04` | `cowrie.client.version` |
| `2026-04-30 18:24:04` | `cowrie.client.kex` |
| `2026-04-30 18:24:05` | `cowrie.login.success` |
| `2026-04-30 18:24:06` | `cowrie.session.params` |
| `2026-04-30 18:24:06` | `cowrie.command.input` |
| `2026-04-30 18:24:06` | `cowrie.command.failed` |
| `2026-04-30 18:24:06` | `cowrie.log.closed` |
| `2026-04-30 18:24:07` | `cowrie.session.params` |
| `2026-04-30 18:24:07` | `cowrie.command.input` |
| `2026-04-30 18:24:07` | `cowrie.session.file_download` |
| `2026-04-30 18:24:07` | `cowrie.log.closed` |
| `2026-04-30 18:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c8831670b0

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:24 |
| **Last Seen** | 2026-04-30 18:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:24:10` | `cowrie.session.connect` |
| `2026-04-30 18:24:10` | `cowrie.client.version` |
| `2026-04-30 18:24:10` | `cowrie.client.kex` |
| `2026-04-30 18:24:11` | `cowrie.login.success` |
| `2026-04-30 18:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82ad05228b84

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:27 |
| **Last Seen** | 2026-04-30 18:27 |
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
| `2026-04-30 18:27:40` | `cowrie.session.connect` |
| `2026-04-30 18:27:40` | `cowrie.client.version` |
| `2026-04-30 18:27:40` | `cowrie.client.kex` |
| `2026-04-30 18:27:41` | `cowrie.login.success` |
| `2026-04-30 18:27:42` | `cowrie.session.params` |
| `2026-04-30 18:27:42` | `cowrie.command.input` |
| `2026-04-30 18:27:42` | `cowrie.command.failed` |
| `2026-04-30 18:27:42` | `cowrie.log.closed` |
| `2026-04-30 18:27:43` | `cowrie.session.params` |
| `2026-04-30 18:27:43` | `cowrie.command.input` |
| `2026-04-30 18:27:43` | `cowrie.session.file_download` |
| `2026-04-30 18:27:43` | `cowrie.log.closed` |
| `2026-04-30 18:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baacf94969de

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:27 |
| **Last Seen** | 2026-04-30 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:27:46` | `cowrie.session.connect` |
| `2026-04-30 18:27:46` | `cowrie.client.version` |
| `2026-04-30 18:27:46` | `cowrie.client.kex` |
| `2026-04-30 18:27:47` | `cowrie.login.success` |
| `2026-04-30 18:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a5fb244b25

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:29 |
| **Last Seen** | 2026-04-30 18:29 |
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
| `2026-04-30 18:29:11` | `cowrie.session.connect` |
| `2026-04-30 18:29:11` | `cowrie.client.version` |
| `2026-04-30 18:29:11` | `cowrie.client.kex` |
| `2026-04-30 18:29:13` | `cowrie.login.success` |
| `2026-04-30 18:29:13` | `cowrie.session.params` |
| `2026-04-30 18:29:13` | `cowrie.command.input` |
| `2026-04-30 18:29:13` | `cowrie.command.failed` |
| `2026-04-30 18:29:13` | `cowrie.log.closed` |
| `2026-04-30 18:29:14` | `cowrie.session.params` |
| `2026-04-30 18:29:14` | `cowrie.command.input` |
| `2026-04-30 18:29:14` | `cowrie.session.file_download` |
| `2026-04-30 18:29:14` | `cowrie.log.closed` |
| `2026-04-30 18:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bdd1f9e2e1

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:29 |
| **Last Seen** | 2026-04-30 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:29:17` | `cowrie.session.connect` |
| `2026-04-30 18:29:17` | `cowrie.client.version` |
| `2026-04-30 18:29:18` | `cowrie.client.kex` |
| `2026-04-30 18:29:19` | `cowrie.login.success` |
| `2026-04-30 18:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8cdc7544744

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:31 |
| **Last Seen** | 2026-04-30 18:31 |
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
| `2026-04-30 18:31:21` | `cowrie.session.connect` |
| `2026-04-30 18:31:21` | `cowrie.client.version` |
| `2026-04-30 18:31:21` | `cowrie.client.kex` |
| `2026-04-30 18:31:22` | `cowrie.login.success` |
| `2026-04-30 18:31:22` | `cowrie.session.params` |
| `2026-04-30 18:31:22` | `cowrie.command.input` |
| `2026-04-30 18:31:22` | `cowrie.command.failed` |
| `2026-04-30 18:31:23` | `cowrie.log.closed` |
| `2026-04-30 18:31:23` | `cowrie.session.params` |
| `2026-04-30 18:31:23` | `cowrie.command.input` |
| `2026-04-30 18:31:24` | `cowrie.session.file_download` |
| `2026-04-30 18:31:24` | `cowrie.log.closed` |
| `2026-04-30 18:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073262d9a9c6

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:31 |
| **Last Seen** | 2026-04-30 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:31:27` | `cowrie.session.connect` |
| `2026-04-30 18:31:27` | `cowrie.client.version` |
| `2026-04-30 18:31:27` | `cowrie.client.kex` |
| `2026-04-30 18:31:28` | `cowrie.login.success` |
| `2026-04-30 18:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4452da997eb0

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:35 |
| **Last Seen** | 2026-04-30 18:35 |
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
| `2026-04-30 18:35:00` | `cowrie.session.connect` |
| `2026-04-30 18:35:00` | `cowrie.client.version` |
| `2026-04-30 18:35:00` | `cowrie.client.kex` |
| `2026-04-30 18:35:01` | `cowrie.login.success` |
| `2026-04-30 18:35:02` | `cowrie.session.params` |
| `2026-04-30 18:35:02` | `cowrie.command.input` |
| `2026-04-30 18:35:02` | `cowrie.command.failed` |
| `2026-04-30 18:35:02` | `cowrie.log.closed` |
| `2026-04-30 18:35:02` | `cowrie.session.params` |
| `2026-04-30 18:35:02` | `cowrie.command.input` |
| `2026-04-30 18:35:03` | `cowrie.session.file_download` |
| `2026-04-30 18:35:03` | `cowrie.log.closed` |
| `2026-04-30 18:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa618c3042d8

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-04-30 18:35 |
| **Last Seen** | 2026-04-30 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:35:06` | `cowrie.session.connect` |
| `2026-04-30 18:35:06` | `cowrie.client.version` |
| `2026-04-30 18:35:06` | `cowrie.client.kex` |
| `2026-04-30 18:35:07` | `cowrie.login.success` |
| `2026-04-30 18:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b44f7580ae

| Field | Detail |
|---|---|
| **Source IP** | `195.178.191[.]5` |
| **First Seen** | 2026-04-30 18:51 |
| **Last Seen** | 2026-04-30 18:51 |
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
| `2026-04-30 18:51:14` | `cowrie.session.connect` |
| `2026-04-30 18:51:14` | `cowrie.client.version` |
| `2026-04-30 18:51:14` | `cowrie.client.kex` |
| `2026-04-30 18:51:15` | `cowrie.login.success` |
| `2026-04-30 18:51:15` | `cowrie.session.params` |
| `2026-04-30 18:51:15` | `cowrie.command.input` |
| `2026-04-30 18:51:15` | `cowrie.command.failed` |
| `2026-04-30 18:51:15` | `cowrie.log.closed` |
| `2026-04-30 18:51:15` | `cowrie.session.params` |
| `2026-04-30 18:51:15` | `cowrie.command.input` |
| `2026-04-30 18:51:16` | `cowrie.session.file_download` |
| `2026-04-30 18:51:16` | `cowrie.log.closed` |
| `2026-04-30 18:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.191[.]5` to AbuseIPDB if not already reported
- [ ] Block `195.178.191[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98a67f67e726

| Field | Detail |
|---|---|
| **Source IP** | `195.178.191[.]5` |
| **First Seen** | 2026-04-30 18:51 |
| **Last Seen** | 2026-04-30 18:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 18:51:18` | `cowrie.session.connect` |
| `2026-04-30 18:51:18` | `cowrie.client.version` |
| `2026-04-30 18:51:18` | `cowrie.client.kex` |
| `2026-04-30 18:51:19` | `cowrie.login.success` |
| `2026-04-30 18:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.191[.]5` to AbuseIPDB if not already reported
- [ ] Block `195.178.191[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced56e948f1f

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-30 19:02 |
| **Last Seen** | 2026-04-30 19:02 |
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
| `2026-04-30 19:02:44` | `cowrie.session.connect` |
| `2026-04-30 19:02:44` | `cowrie.client.version` |
| `2026-04-30 19:02:44` | `cowrie.client.kex` |
| `2026-04-30 19:02:45` | `cowrie.login.success` |
| `2026-04-30 19:02:45` | `cowrie.session.params` |
| `2026-04-30 19:02:45` | `cowrie.command.input` |
| `2026-04-30 19:02:45` | `cowrie.command.failed` |
| `2026-04-30 19:02:45` | `cowrie.log.closed` |
| `2026-04-30 19:02:45` | `cowrie.session.params` |
| `2026-04-30 19:02:45` | `cowrie.command.input` |
| `2026-04-30 19:02:45` | `cowrie.session.file_download` |
| `2026-04-30 19:02:45` | `cowrie.log.closed` |
| `2026-04-30 19:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-556690e8b596

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-30 19:02 |
| **Last Seen** | 2026-04-30 19:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 19:02:47` | `cowrie.session.connect` |
| `2026-04-30 19:02:47` | `cowrie.client.version` |
| `2026-04-30 19:02:47` | `cowrie.client.kex` |
| `2026-04-30 19:02:47` | `cowrie.login.success` |
| `2026-04-30 19:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `43.130.90[.]166` | **30** | 2026-04-30 18:13 | 2026-04-30 18:37 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `131.222.250[.]195` | **4** | 2026-04-30 17:26 | 2026-04-30 17:32 | 8m | 0 | `T1592` | 🟢 LOW |
| `64.72.221[.]187` | **3** | 2026-04-30 18:12 | 2026-04-30 18:18 | 6m | 0 | `T1592` | 🟢 LOW |
| `193.74.150[.]109` | **2** | 2026-04-30 17:32 | 2026-04-30 17:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.13.23[.]58` | 1 | 2026-04-30 18:53 | 2026-04-30 18:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.213[.]116` | 1 | 2026-04-30 18:58 | 2026-04-30 18:59 | 21s | 0 | `T1592` | 🟢 LOW |
| `144.48.243[.]18` | 1 | 2026-04-30 19:02 | 2026-04-30 19:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.141[.]1` | 1 | 2026-04-30 18:11 | 2026-04-30 18:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.178.191[.]5` | 1 | 2026-04-30 18:51 | 2026-04-30 18:51 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.99.237[.]57` | 1 | 2026-04-30 17:46 | 2026-04-30 17:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `8.219.249[.]135` | 1 | 2026-04-30 18:01 | 2026-04-30 18:01 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `64.72.221[.]187` | US | American Fiber INC. | **100** ⚠️ | 1 |
| `193.74.150[.]109` | BE | Proximus NV | **100** ⚠️ | 0 |
| `118.145.213[.]116` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 10 |
| `106.13.23[.]58` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 2 |
| `144.48.243[.]18` | HK | Overcasts Limited | **100** ⚠️ | 48 |
| `8.219.249[.]135` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 24 |
| `180.76.141[.]1` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `47.99.237[.]57` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 5 |
| `43.130.90[.]166` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `195.178.191[.]5` | SE | Bahnhof AB | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 53 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 32 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 18 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (322 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 15 below threshold 25 | 10 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 280 |
| AbuseIPDB score 24 below threshold 25 | 6 |
| AbuseIPDB score 4 below threshold 25 | 13 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| AbuseIPDB score 6 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 386 cases |
| Tool 34  | Credential Extractor        | ✅ 50 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 322 filtered (83.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 11 recon entry/entries in table (4 group(s) consolidating 39 session(s)).

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
_Report time: 2026-04-30T19:28:33Z_
