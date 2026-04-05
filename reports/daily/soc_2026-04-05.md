# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T16:35:27Z |
| **Shift Time** | 16:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **23** |
| Confirmed Threats | **19** |
| False Positives Filtered | **4** (17.4%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **7** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **17** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **11** |
| Unique Credential Pairs | **7** |
| Unique Usernames | **4** |
| Unique Passwords | **7** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `345gs5662d34` | 3 |
| `runner` | 1 |
| `postgres` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 3 |
| `1234` | 1 |
| `Root12345!` | 1 |
| `root321@` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 3 |
| `runner` | `1234` | 1 |
| `root` | `Root12345!` | 1 |
| `root` | `root321@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root12345!` | `217.154.233.215` | 2026-04-05T16:07:46 |
| `root` | `3245gs5662d34` | `217.154.233.215` | 2026-04-05T16:07:50 |
| `root` | `root321@` | `217.154.233.215` | 2026-04-05T16:09:55 |
| `root` | `XXbb000` | `217.154.233.215` | 2026-04-05T16:11:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **23** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 15 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 14 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 14 | 2 | Modern SSH client |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.154.233.215`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **6** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | LOW |
| `AS8560` | IONOS SE | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS262588` | EXPLORERNET INFOLINK TECNOLOGIA E TELECOMUNICACOES | 1 | LOW |
| `AS135760` | Speednet Unique Network Pvt Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7db86d8e4933

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-05 16:07 |
| **Last Seen** | 2026-04-05 16:07 |
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
| `2026-04-05 16:07:46` | `cowrie.session.connect` |
| `2026-04-05 16:07:46` | `cowrie.client.version` |
| `2026-04-05 16:07:46` | `cowrie.client.kex` |
| `2026-04-05 16:07:46` | `cowrie.login.success` |
| `2026-04-05 16:07:47` | `cowrie.session.params` |
| `2026-04-05 16:07:47` | `cowrie.command.input` |
| `2026-04-05 16:07:47` | `cowrie.command.failed` |
| `2026-04-05 16:07:47` | `cowrie.log.closed` |
| `2026-04-05 16:07:47` | `cowrie.session.params` |
| `2026-04-05 16:07:47` | `cowrie.command.input` |
| `2026-04-05 16:07:47` | `cowrie.session.file_download` |
| `2026-04-05 16:07:47` | `cowrie.log.closed` |
| `2026-04-05 16:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b284ee26f08

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-05 16:07 |
| **Last Seen** | 2026-04-05 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:07:49` | `cowrie.session.connect` |
| `2026-04-05 16:07:49` | `cowrie.client.version` |
| `2026-04-05 16:07:50` | `cowrie.client.kex` |
| `2026-04-05 16:07:50` | `cowrie.login.success` |
| `2026-04-05 16:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922535b62579

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-05 16:09 |
| **Last Seen** | 2026-04-05 16:09 |
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
| `2026-04-05 16:09:55` | `cowrie.session.connect` |
| `2026-04-05 16:09:55` | `cowrie.client.version` |
| `2026-04-05 16:09:55` | `cowrie.client.kex` |
| `2026-04-05 16:09:55` | `cowrie.login.success` |
| `2026-04-05 16:09:56` | `cowrie.session.params` |
| `2026-04-05 16:09:56` | `cowrie.command.input` |
| `2026-04-05 16:09:56` | `cowrie.command.failed` |
| `2026-04-05 16:09:56` | `cowrie.log.closed` |
| `2026-04-05 16:09:56` | `cowrie.session.params` |
| `2026-04-05 16:09:56` | `cowrie.command.input` |
| `2026-04-05 16:09:56` | `cowrie.session.file_download` |
| `2026-04-05 16:09:56` | `cowrie.log.closed` |
| `2026-04-05 16:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5eddb48f40b

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-05 16:09 |
| **Last Seen** | 2026-04-05 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:09:58` | `cowrie.session.connect` |
| `2026-04-05 16:09:58` | `cowrie.client.version` |
| `2026-04-05 16:09:59` | `cowrie.client.kex` |
| `2026-04-05 16:09:59` | `cowrie.login.success` |
| `2026-04-05 16:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530bb34899d9

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-05 16:11 |
| **Last Seen** | 2026-04-05 16:12 |
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
| `2026-04-05 16:11:56` | `cowrie.session.connect` |
| `2026-04-05 16:11:56` | `cowrie.client.version` |
| `2026-04-05 16:11:56` | `cowrie.client.kex` |
| `2026-04-05 16:11:57` | `cowrie.login.success` |
| `2026-04-05 16:11:57` | `cowrie.session.params` |
| `2026-04-05 16:11:57` | `cowrie.command.input` |
| `2026-04-05 16:11:57` | `cowrie.command.failed` |
| `2026-04-05 16:11:58` | `cowrie.log.closed` |
| `2026-04-05 16:11:58` | `cowrie.session.params` |
| `2026-04-05 16:11:58` | `cowrie.command.input` |
| `2026-04-05 16:11:58` | `cowrie.session.file_download` |
| `2026-04-05 16:11:58` | `cowrie.log.closed` |
| `2026-04-05 16:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ce4ee04c71

| Field | Detail |
|---|---|
| **Source IP** | `217.154.233[.]215` |
| **First Seen** | 2026-04-05 16:12 |
| **Last Seen** | 2026-04-05 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 16:12:00` | `cowrie.session.connect` |
| `2026-04-05 16:12:00` | `cowrie.client.version` |
| `2026-04-05 16:12:00` | `cowrie.client.kex` |
| `2026-04-05 16:12:01` | `cowrie.login.success` |
| `2026-04-05 16:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.233[.]215` to AbuseIPDB if not already reported
- [ ] Block `217.154.233[.]215` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.190.142[.]147` | **4** | 2026-04-05 16:11 | 2026-04-05 16:18 | 6m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.154.233[.]215` | **4** | 2026-04-05 16:00 | 2026-04-05 16:12 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `118.145.66[.]151` | 1 | 2026-04-05 15:30 | 2026-04-05 15:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `160.22.131[.]9` | 1 | 2026-04-05 15:29 | 2026-04-05 15:29 | 14s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-05 16:25 | 2026-04-05 16:26 | 34s | 0 | `T1592` | 🟢 LOW |
| `61.78.98[.]181` | 1 | 2026-04-05 14:40 | 2026-04-05 14:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `8.210.123[.]17` | 1 | 2026-04-05 15:53 | 2026-04-05 15:54 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `160.22.131[.]9` | IN | SPEEDNET BROADBAND SERVICES | **100** ⚠️ | 9 |
| `118.145.66[.]151` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 14 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `217.154.233[.]215` | DE | IONOS SE | **100** ⚠️ | 50 |
| `61.78.98[.]181` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `115.190.142[.]147` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `8.210.123[.]17` | HK | Aliyun Computing Co.LTD | **100** ⚠️ | 0 |
| `68.220.62[.]105` | US | Microsoft Corporation | **65** | 0 |
| `177.75.49[.]106` | BR | EXPLORERNET INFOLINK TECNOLOGIA E TELECOMUNICACOES | **40** | 2 |
| `50.116.51[.]172` | US | Linode | 16 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 15 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 3 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 3 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 23 cases |
| Tool 34  | Credential Extractor        | ✅ 11 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (17.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 7 recon entry/entries in table (2 group(s) consolidating 8 session(s)).

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
_Report time: 2026-04-05T16:35:27Z_
